"""
GitHub Actions 入口：从 podcasts.yaml 加载配置，生成播客节目并上传到 OSS。

用法：
  python -m generate                    # 正常运行，按 publish_hour 过滤
  python -m generate --force            # 忽略小时检查，强制生成
  python -m generate --podcast ID       # 只处理指定播客
  python -m generate --force --podcast ID
  python -m generate --test-feishu              # 用最新 episode 测试飞书通知
  python -m generate --test-feishu --podcast ID # 测试指定播客的飞书通知
"""
import argparse
import asyncio
import hashlib
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
from app.services.feishu import send_feishu_notification
from app.config import settings
from app.pipeline import generate_episode
from app.services.twitter import fetch_list_tweets
from app.services.llm import generate_content

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
            frequency=entry.get("frequency", "daily"),
            publish_day=entry.get("publish_day", 0),
            extra_prompt=entry.get("extra_prompt", ""),
            cover_path=f"{entry['id']}/cover.jpg",
            owner_name=entry.get("owner_name", ""),
            owner_email=entry.get("owner_email", ""),
            category=entry.get("category", "Technology"),
            feishu_webhook=entry.get("feishu_webhook", ""),
            subscribe_url=entry.get("subscribe_url", ""),
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
            # 计算封面内容 hash，用于 URL 缓存刷新
            podcast.cover_hash = hashlib.md5(cover_bytes).hexdigest()[:8]
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
            logger.info(f"[{podcast.name}] 封面已同步: {cover_filename} (hash={podcast.cover_hash})")
        else:
            logger.warning(f"[{podcast.name}] 封面文件不存在: {cover_src}")

    # 封面 hash 更新后重新保存 podcast.json
    if podcast.cover_hash:
        _save_podcast_sync(podcast)

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


# ── 飞书测试 ──────────────────────────────────────────────────────────────────

def test_feishu(podcast_id: Optional[str] = None) -> None:
    """用已有的最新一期 episode 测试飞书通知，不触发任何生成。"""
    all_podcasts = load_podcasts_from_yaml()
    if podcast_id:
        all_podcasts = [p for p in all_podcasts if p.id == podcast_id]
    if not all_podcasts:
        logger.error("未找到播客" + (f" ID: {podcast_id}" if podcast_id else ""))
        sys.exit(1)

    for podcast in all_podcasts:
        if not podcast.feishu_webhook:
            logger.warning(f"[{podcast.name}] 未配置 feishu_webhook，跳过")
            continue

        # 从 docs/ 找最新 episode.json
        docs_ep_root = REPO_ROOT / "docs" / podcast.id / "episodes"
        if not docs_ep_root.exists():
            logger.warning(f"[{podcast.name}] docs/ 中无 episode 数据")
            continue

        ep_files = sorted(docs_ep_root.glob("*/episode.json"), reverse=True)
        if not ep_files:
            logger.warning(f"[{podcast.name}] 无已有 episode")
            continue

        ep = Episode.model_validate_json(ep_files[0].read_text(encoding="utf-8"))
        logger.info(f"[{podcast.name}] 用 {ep.date} 的 episode 测试飞书通知: {ep.title}")
        send_feishu_notification(podcast.feishu_webhook, podcast, ep)


# ── Script 测试 ──────────────────────────────────────────────────────────────

async def check_script(
    podcast_id: Optional[str] = None,
    max_posts: Optional[int] = None,
    prompt_file: Optional[str] = None,
) -> None:
    """只运行 fetch tweets + LLM 生成 script，输出到 preview/ 目录，不做 TTS/OSS/feed/docs。"""
    all_podcasts = load_podcasts_from_yaml()
    if podcast_id:
        all_podcasts = [p for p in all_podcasts if p.id == podcast_id]
    if not all_podcasts:
        logger.error("未找到播客" + (f" ID: {podcast_id}" if podcast_id else ""))
        sys.exit(1)

    for podcast in all_podcasts:
        logger.info(f"[{podcast.name}] 测试模式：fetch + LLM...")

        # Fetch tweets
        lookback_hours = 168 if podcast.frequency == "weekly" else 24
        since = datetime.now(timezone.utc) - timedelta(hours=lookback_hours)
        fetch_kwargs = {"list_id": podcast.twitter_list_id, "since": since}
        if max_posts is not None:
            fetch_kwargs["max_tweets"] = max_posts
        tweets = await asyncio.to_thread(lambda: fetch_list_tweets(**fetch_kwargs))

        if len(tweets) < 3:
            logger.warning(f"[{podcast.name}] 推文数量不足（{len(tweets)} 条），跳过")
            continue

        today = datetime.now(SHANGHAI_TZ).date()

        # Generate content
        script, shownotes, title = await asyncio.to_thread(
            generate_content,
            tweets, podcast.name, podcast.language, today,
            podcast.frequency, podcast.extra_prompt, prompt_file,
        )

        # Write to preview/ directory
        preview_dir = REPO_ROOT / "preview" / podcast.id
        preview_dir.mkdir(parents=True, exist_ok=True)
        (preview_dir / "posts.md").write_text(tweets.text, encoding="utf-8")
        (preview_dir / "script.md").write_text(script, encoding="utf-8")
        (preview_dir / "shownotes.md").write_text(shownotes, encoding="utf-8")
        if title:
            (preview_dir / "title.txt").write_text(title, encoding="utf-8")

        # Print to stdout
        print(f"\n{'='*60}")
        print(f"播客: {podcast.name} | 标题: {title}")
        print(f"{'='*60}")
        print(script)
        print(f"\n{'='*60}")
        print(f"预览文件已写入: {preview_dir}")
        prompt_source = prompt_file or f"prompts/script_{podcast.language}.md"
        print(f"使用 prompt: {prompt_source}")


# ── 主流程 ───────────────────────────────────────────────────────────────────

async def main(force: bool = False, podcast_id: Optional[str] = None, max_posts: Optional[int] = None, prompt_file: Optional[str] = None) -> None:
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
    current_weekday = now_shanghai.weekday()
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

        if not force and podcast.frequency == "weekly" and podcast.publish_day != current_weekday:
            logger.info(
                f"[{podcast.name}] 跳过：publish_day={podcast.publish_day}，"
                f"当前={current_weekday}"
            )
            continue

        logger.info(f"[{podcast.name}] 开始生成节目...")
        await generate_episode(podcast.id, max_posts=max_posts, frequency=podcast.frequency, extra_prompt=podcast.extra_prompt, prompt_file=prompt_file)

        # 注入 audio_url 到 episode.json
        today = datetime.now(SHANGHAI_TZ).date()
        await asyncio.to_thread(inject_episode_urls, podcast, today)

    # 复制文件到 docs/ 供 GitHub Pages 托管
    await asyncio.to_thread(write_site_files, all_podcasts)

    logger.info("全部完成")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="生成播客节目并上传到 OSS")
    parser.add_argument("--force", action="store_true", help="忽略 publish_hour 检查")
    parser.add_argument("--podcast", type=str, default=None, help="只处理指定播客 ID")
    parser.add_argument("--max-posts", type=int, default=None, help="最大抓取推文数")
    parser.add_argument("--test-feishu", action="store_true", help="用最新已有 episode 测试飞书通知")
    parser.add_argument("--check-script", action="store_true", help="只生成 script 到 preview/，不做 TTS/OSS/feed")
    parser.add_argument("--prompt", type=str, default=None, help="自定义 prompt 文件路径")
    args = parser.parse_args()

    if args.test_feishu:
        test_feishu(podcast_id=args.podcast)
    elif args.check_script:
        asyncio.run(check_script(podcast_id=args.podcast, max_posts=args.max_posts, prompt_file=args.prompt))
    else:
        asyncio.run(main(force=args.force, podcast_id=args.podcast, max_posts=args.max_posts, prompt_file=args.prompt))
