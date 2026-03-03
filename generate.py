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
import sys
from datetime import datetime, timezone, timedelta, date
from pathlib import Path
from typing import Optional

import yaml

from app.storage import (
    Podcast, Episode, STATIC_DIR,
    _save_podcast_sync, _list_episodes_sync,
)
from app.services.oss import (
    upload_file_sync, download_file_sync,
    public_url, is_enabled as oss_enabled,
)
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
            is_active=True,
        ))
    return podcasts


# ── Bootstrap ────────────────────────────────────────────────────────────────

def _podcast_json_with_urls(podcast: Podcast) -> dict:
    """在 podcast 的 JSON 字典中注入计算后的 cover_url 和 feed_url。"""
    d = json.loads(podcast.model_dump_json())
    d["cover_url"] = podcast.cover_url
    d["feed_url"] = podcast.feed_url
    return d


def _episode_json_with_urls(episode: Episode) -> dict:
    """在 episode 的 JSON 字典中注入计算后的 audio_url。"""
    d = json.loads(episode.model_dump_json())
    d["audio_url"] = episode.audio_url
    return d


def bootstrap_podcast(podcast: Podcast) -> None:
    """
    初始化播客：
    1. 写 podcast.json（含 URL）到本地和 OSS
    2. 上传封面图到 OSS
    3. 从 OSS 下载 episodes/index.json 到本地（让 list_episodes() 能工作）
    """
    # 1. 写 podcast.json
    _save_podcast_sync(podcast)
    podcast_dict = _podcast_json_with_urls(podcast)
    podcast_json_bytes = json.dumps(podcast_dict, ensure_ascii=False, indent=2).encode("utf-8")

    if oss_enabled():
        upload_file_sync(f"{podcast.id}/podcast.json", podcast_json_bytes)
        # 也写入本地（覆盖 storage 写的，因为我们需要带 URL 的版本）
        podcast_json_path = STATIC_DIR / podcast.id / "podcast.json"
        podcast_json_path.write_bytes(podcast_json_bytes)

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
            logger.info(f"[{podcast.name}] 封面已同步: {cover_filename}")
        else:
            logger.warning(f"[{podcast.name}] 封面文件不存在: {cover_src}")

    # 3. 从 OSS 下载 episodes/index.json → 还原本地 episode.json 文件
    if oss_enabled():
        index_data = download_file_sync(f"{podcast.id}/episodes/index.json")
        if index_data:
            episodes_list = json.loads(index_data)
            for ep_dict in episodes_list:
                ep_date = ep_dict.get("date")
                if ep_date:
                    ep_dir = STATIC_DIR / podcast.id / "episodes" / ep_date
                    ep_dir.mkdir(parents=True, exist_ok=True)
                    ep_path = ep_dir / "episode.json"
                    ep_path.write_text(
                        json.dumps(ep_dict, ensure_ascii=False, indent=2),
                        encoding="utf-8",
                    )
            logger.info(f"[{podcast.name}] 已从 OSS 恢复 {len(episodes_list)} 个节目索引")


# ── 索引文件上传 ─────────────────────────────────────────────────────────────

def upload_episode_index(podcast: Podcast) -> None:
    """构建并上传 {podcast_id}/episodes/index.json（去掉 script 字段）。"""
    episodes = _list_episodes_sync(podcast.id, limit=100)
    index = []
    for ep in episodes:
        d = _episode_json_with_urls(ep)
        d.pop("script", None)  # 索引中不需要 script，节省带宽
        index.append(d)

    index_bytes = json.dumps(index, ensure_ascii=False, indent=2).encode("utf-8")

    # 写本地
    index_dir = STATIC_DIR / podcast.id / "episodes"
    index_dir.mkdir(parents=True, exist_ok=True)
    (index_dir / "index.json").write_bytes(index_bytes)

    # 上传 OSS
    if oss_enabled():
        upload_file_sync(f"{podcast.id}/episodes/index.json", index_bytes)

    logger.info(f"[{podcast.name}] episodes/index.json 已更新 ({len(index)} 期)")


def upload_episode_detail(podcast: Podcast, ep_date: date) -> None:
    """上传带 audio_url 的 episode.json 到 OSS。"""
    ep_path = STATIC_DIR / podcast.id / "episodes" / str(ep_date) / "episode.json"
    if not ep_path.exists():
        return

    ep = Episode.model_validate_json(ep_path.read_text(encoding="utf-8"))
    ep_dict = _episode_json_with_urls(ep)
    ep_bytes = json.dumps(ep_dict, ensure_ascii=False, indent=2).encode("utf-8")

    # 覆写本地（带 URL）
    ep_path.write_bytes(ep_bytes)

    if oss_enabled():
        upload_file_sync(f"{podcast.id}/episodes/{ep_date}/episode.json", ep_bytes)


def upload_podcasts_index(podcasts: list[Podcast]) -> None:
    """构建并上传全局 podcasts.json。"""
    index = [_podcast_json_with_urls(p) for p in podcasts]
    index_bytes = json.dumps(index, ensure_ascii=False, indent=2).encode("utf-8")

    # 写本地
    STATIC_DIR.mkdir(parents=True, exist_ok=True)
    (STATIC_DIR / "podcasts.json").write_bytes(index_bytes)

    # 上传 OSS
    if oss_enabled():
        upload_file_sync("podcasts.json", index_bytes)

    logger.info(f"podcasts.json 已更新 ({len(index)} 个播客)")


# ── 主流程 ───────────────────────────────────────────────────────────────────

async def main(force: bool = False, podcast_id: Optional[str] = None) -> None:
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
        await generate_episode(podcast.id)

        # 上传带 URL 的 episode.json
        today = date.today()
        await asyncio.to_thread(upload_episode_detail, podcast, today)

    # 上传索引文件
    for podcast in all_podcasts:
        await asyncio.to_thread(upload_episode_index, podcast)

    await asyncio.to_thread(upload_podcasts_index, all_podcasts)

    logger.info("全部完成")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="生成播客节目并上传到 OSS")
    parser.add_argument("--force", action="store_true", help="忽略 publish_hour 检查")
    parser.add_argument("--podcast", type=str, default=None, help="只处理指定播客 ID")
    args = parser.parse_args()

    asyncio.run(main(force=args.force, podcast_id=args.podcast))
