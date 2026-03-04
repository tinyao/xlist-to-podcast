"""
GitHub Actions 入口：从 podcasts.yaml 加载配置，生成播客节目并上传到 OSS。

用法：
  python -m generate                    # 正常运行，按 publish_hour 过滤
  python -m generate --force            # 忽略小时检查，强制生成
  python -m generate --podcast ID       # 只处理指定播客
  python -m generate --force --podcast ID
"""
import argparse
import asyncio
import json
import logging
import shutil
import sys
from datetime import datetime, timezone, timedelta, date
from pathlib import Path
from typing import Optional

import yaml

from app.storage import (
    Podcast, Episode, STATIC_DIR,
    _save_podcast_sync,
)
from app.services.oss import upload_file_sync, is_enabled as oss_enabled
from app.config import settings
from app.pipeline import generate_episode

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

REPO_ROOT = Path(__file__).resolve().parent
YAML_PATH = REPO_ROOT / "podcasts.yaml"

SHANGHAI_TZ = timezone(timedelta(hours=8))


# ── YAML → Podcast ──────────────────────────────────────────────────────────

def load_podcasts_from_yaml() -> list[Podcast]:
    """读取 podcasts.yaml，返回 Podcast 模型列表。"""
    data = yaml.safe_load(YAML_PATH.read_text(encoding="utf-8"))
    entries = data.get("podcasts") or []
    podcasts: list[Podcast] = []
    for entry in entries:
        podcasts.append(Podcast(
            id=entry["id"],
            name=entry["name"],
            description=entry.get("description", ""),
            twitter_list_url=entry["twitter_list_url"],
            twitter_list_id=entry["twitter_list_id"],
            voice=entry.get("voice", "nova"),
            language=entry.get("language", "zh"),
            publish_hour=entry.get("publish_hour", 8),
            cover_path=f"{entry['id']}/cover.jpg",
            owner_name=entry.get("owner_name", ""),
            owner_email=entry.get("owner_email", ""),
            category=entry.get("category", "Technology"),
            is_active=True,
        ))
    return podcasts


# ── Bootstrap ────────────────────────────────────────────────────────────────

def _episode_json_with_urls(episode: Episode) -> dict:
    """在 episode 的 JSON 字典中注入计算后的 audio_url。"""
    d = json.loads(episode.model_dump_json())
    d["audio_url"] = episode.audio_url
    return d


def bootstrap_podcast(podcast: Podcast) -> None:
    """
    初始化播客：
    1. 写 podcast.json 到本地
    2. 同步封面（本地 + OSS + docs/）
    3. 从 docs/ 恢复 episode.json 到本地（让 list_episodes() 能工作）
    """
    # 1. 写 podcast.json（仅本地，供 pipeline 读取）
    _save_podcast_sync(podcast)

    # 2. 上传封面
    cover_filename = None
    yaml_data = yaml.safe_load(YAML_PATH.read_text(encoding="utf-8"))
    for entry in yaml_data.get("podcasts") or []:
        if entry["id"] == podcast.id:
            cover_filename = entry.get("cover_file")
            break

    if cover_filename:
        cover_src = REPO_ROOT / "covers" / cover_filename
        if cover_src.exists():
            cover_bytes = cover_src.read_bytes()
            # 写到本地
            local_cover = STATIC_DIR / podcast.id / "cover.jpg"
            local_cover.parent.mkdir(parents=True, exist_ok=True)
            local_cover.write_bytes(cover_bytes)
            # 上传 OSS
            if oss_enabled():
                upload_file_sync(f"{podcast.id}/cover.jpg", cover_bytes)
            # 复制到 docs/
            if settings.site_url:
                docs_cover = REPO_ROOT / "docs" / podcast.id / "cover.jpg"
                docs_cover.parent.mkdir(parents=True, exist_ok=True)
                docs_cover.write_bytes(cover_bytes)
            logger.info(f"[{podcast.name}] 封面已同步: {cover_filename}")
        else:
            logger.warning(f"[{podcast.name}] 封面文件不存在: {cover_src}")

    # 3. 从 docs/ 读取 episode.json → 还原本地 episode.json 文件
    docs_ep_root = REPO_ROOT / "docs" / podcast.id / "episodes"
    if docs_ep_root.exists():
        count = 0
        for ep_json_file in docs_ep_root.glob("*/episode.json"):
            ep_date = ep_json_file.parent.name
            ep_dir = STATIC_DIR / podcast.id / "episodes" / ep_date
            ep_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ep_json_file, ep_dir / "episode.json")
            count += 1
        if count:
            logger.info(f"[{podcast.name}] 已从 docs/ 恢复 {count} 个节目")


def inject_episode_urls(podcast: Podcast, ep_date: date) -> None:
    """将 audio_url 注入 episode.json（Pydantic @property 不序列化）。"""
    ep_path = STATIC_DIR / podcast.id / "episodes" / str(ep_date) / "episode.json"
    if not ep_path.exists():
        return

    ep = Episode.model_validate_json(ep_path.read_text(encoding="utf-8"))
    ep_dict = _episode_json_with_urls(ep)
    ep_path.write_bytes(json.dumps(ep_dict, ensure_ascii=False, indent=2).encode("utf-8"))


# ── docs/ 站点文件 ────────────────────────────────────────────────────────────

def write_site_files(podcasts: list[Podcast]) -> None:
    """将 feed.xml 和每期的 md 文件复制到 docs/，供 GitHub Pages 托管。"""
    if not settings.site_url:
        return
    for podcast in podcasts:
        docs_dir = REPO_ROOT / "docs" / podcast.id
        # feed.xml
        feed_src = STATIC_DIR / podcast.id / "feed.xml"
        if feed_src.exists():
            feed_dst = docs_dir / "feed.xml"
            feed_dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(feed_src, feed_dst)
            logger.info(f"[{podcast.name}] feed.xml → docs/{podcast.id}/feed.xml")
        # 每期的 episode.json / posts.md / script.md / shownotes.md
        ep_root = STATIC_DIR / podcast.id / "episodes"
        if ep_root.exists():
            for src_file in ep_root.glob("*/*.md"):
                rel = src_file.relative_to(STATIC_DIR / podcast.id)
                dst = docs_dir / rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_file, dst)
            for src_file in ep_root.glob("*/episode.json"):
                rel = src_file.relative_to(STATIC_DIR / podcast.id)
                dst = docs_dir / rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_file, dst)


# ── 主流程 ───────────────────────────────────────────────────────────────────

async def main(force: bool = False, podcast_id: Optional[str] = None, max_posts: Optional[int] = None) -> None:
    all_podcasts = load_podcasts_from_yaml()

    if not all_podcasts:
        logger.warning("podcasts.yaml 中没有播客配置")
        return

    if podcast_id:
        all_podcasts = [p for p in all_podcasts if p.id == podcast_id]
        if not all_podcasts:
            logger.error(f"未找到播客 ID: {podcast_id}")
            sys.exit(1)

    now_shanghai = datetime.now(SHANGHAI_TZ)
    current_hour = now_shanghai.hour
    logger.info(f"当前时间: {now_shanghai.strftime('%Y-%m-%d %H:%M')} (Asia/Shanghai)")

    # Bootstrap 所有播客
    for podcast in all_podcasts:
        logger.info(f"[{podcast.name}] 初始化...")
        await asyncio.to_thread(bootstrap_podcast, podcast)

    # 生成节目
    for podcast in all_podcasts:
        if not force and podcast.publish_hour != current_hour:
            logger.info(
                f"[{podcast.name}] 跳过：publish_hour={podcast.publish_hour}，"
                f"当前={current_hour}"
            )
            continue

        logger.info(f"[{podcast.name}] 开始生成节目...")
        await generate_episode(podcast.id, max_posts=max_posts)

        # 注入 audio_url 到 episode.json
        today = date.today()
        await asyncio.to_thread(inject_episode_urls, podcast, today)

    # 复制文件到 docs/ 供 GitHub Pages 托管
    await asyncio.to_thread(write_site_files, all_podcasts)

    logger.info("全部完成")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="生成播客节目并上传到 OSS")
    parser.add_argument("--force", action="store_true", help="忽略 publish_hour 检查")
    parser.add_argument("--podcast", type=str, default=None, help="只处理指定播客 ID")
    parser.add_argument("--max-posts", type=int, default=None, help="最大抓取推文数")
    args = parser.parse_args()

    asyncio.run(main(force=args.force, podcast_id=args.podcast, max_posts=args.max_posts))
