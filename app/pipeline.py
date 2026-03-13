"""
Episode 生成完整流程：
Twitter 抓取 → LLM 生成 → TTS → 写文件 → 更新 feed.xml

中间文件先写入 data/static/，最终由 generate.py 复制到 docs/ 供 GitHub Pages 托管。
每期目录结构（data/static/ 和 docs/ 下相同）：
  {podcast_id}/episodes/{YYYY-MM-DD}/
    ├── posts.md       抓取的原始推文
    ├── script.md      播客朗读稿
    ├── audio-{ts}.mp3 TTS 音频（仅 data/static/，docs/ 不含音频）
    └── shownotes.md   节目说明
"""
import asyncio
import logging
import re
import time
from datetime import datetime, timedelta, timezone, date
from pathlib import Path
from typing import Optional

from app.storage import (
    Podcast, Episode,
    get_podcast, get_episode, save_episode, list_episodes,
)
from app.services.twitter import fetch_list_tweets, FetchResult
from app.services.llm import generate_content
from app.services.tts import text_to_speech
from app.services.feed import build_feed
from app.services.feishu import send_feishu_notification
from app.services.oss import upload_file_sync, is_enabled as oss_enabled

logger = logging.getLogger(__name__)

STATIC_DIR = Path("data/static")
SHANGHAI_TZ = timezone(timedelta(hours=8))
MIN_TWEETS = 3


def _episode_dir(podcast_id: str, ep_date: date) -> Path:
    d = STATIC_DIR / podcast_id / "episodes" / str(ep_date)
    d.mkdir(parents=True, exist_ok=True)
    return d


REPO_ROOT = Path(__file__).resolve().parent.parent


def _load_existing_posts(podcast_id: str, ep_date: date) -> Optional[FetchResult]:
    """尝试从本地或 docs/ 加载已有的 posts.md，返回 FetchResult 或 None。"""
    candidates = [
        STATIC_DIR / podcast_id / "episodes" / str(ep_date) / "posts.md",
        REPO_ROOT / "docs" / podcast_id / "episodes" / str(ep_date) / "posts.md",
    ]
    for path in candidates:
        if path.exists():
            text = path.read_text(encoding="utf-8")
            count = len(re.findall(r"^\[tweet \d+\]", text, re.MULTILINE))
            if count > 0:
                return FetchResult(count=count, text=text)
    return None


async def generate_episode(podcast_id: str, max_posts: Optional[int] = None, frequency: str = "daily", extra_prompt: str = "", ep_date: Optional[date] = None) -> None:
    podcast = await get_podcast(podcast_id)
    if not podcast or not podcast.is_active:
        return

    target_date = ep_date or datetime.now(SHANGHAI_TZ).date()

    # 显式指定日期时允许重新生成，否则跳过已存在的节目
    if ep_date is None:
        existing = await get_episode(podcast_id, target_date)
        if existing and existing.status in ("done", "processing"):
            logger.info(f"[{podcast.name}] 今日节目已存在，跳过")
            return

    episode = Episode(podcast_id=podcast_id, date=target_date, status="processing")
    await save_episode(episode)

    try:
        await _run_pipeline(podcast, episode, target_date, max_posts=max_posts, frequency=frequency, extra_prompt=extra_prompt, reuse_posts=ep_date is not None)
    except Exception as e:
        logger.exception(f"[{podcast.name}] 生成失败: {e}")
        episode.status = "failed"
        episode.error_msg = str(e)
        await save_episode(episode)


async def _run_pipeline(podcast: Podcast, episode: Episode, today: date, max_posts: Optional[int] = None, frequency: str = "daily", extra_prompt: str = "", reuse_posts: bool = False) -> None:
    lookback_hours = 168 if frequency == "weekly" else 24
    since = datetime.now(timezone.utc) - timedelta(hours=lookback_hours)
    ep_dir = _episode_dir(podcast.id, today)

    # 1. 抓取推文（或复用已有 posts）
    tweets = None
    if reuse_posts:
        tweets = _load_existing_posts(podcast.id, today)
        if tweets:
            logger.info(f"[{podcast.name}] 复用已有 posts.md（{len(tweets)} 条推文）")

    if tweets is None:
        logger.info(f"[{podcast.name}] 抓取推文...")
        fetch_kwargs = {"list_id": podcast.twitter_list_id, "since": since}
        if max_posts is not None:
            fetch_kwargs["max_tweets"] = max_posts
        tweets = await asyncio.to_thread(lambda: fetch_list_tweets(**fetch_kwargs))

    if len(tweets) < MIN_TWEETS:
        logger.info(f"[{podcast.name}] 推文数量不足（{len(tweets)} 条），跳过")
        episode.status = "failed"
        episode.error_msg = f"推文数量不足（{len(tweets)} 条，最少需要 {MIN_TWEETS} 条）"
        await save_episode(episode)
        return

    posts_text = tweets.text
    (ep_dir / "posts.md").write_text(posts_text, encoding="utf-8")

    # 1.5 获取近期 episodes（仅 daily 播客）
    recent_episodes = []
    if frequency == "daily":
        all_eps = await list_episodes(podcast.id, limit=5)
        recent_episodes = [e for e in all_eps if e.status == "done" and e.date < today][:2]

    # 2. LLM 生成 script + shownotes + title
    logger.info(f"[{podcast.name}] 生成内容（{len(tweets)} 条推文）...")
    script, shownotes, title = await asyncio.to_thread(
        generate_content, tweets, podcast.name, podcast.language, today, frequency, extra_prompt,
        prompt_file=podcast.prompt_file,
        recent_episodes=recent_episodes,
    )

    (ep_dir / "script.md").write_text(script, encoding="utf-8")
    (ep_dir / "shownotes.md").write_text(shownotes, encoding="utf-8")

    date_str = today.strftime("%Y年%m月%d日") if podcast.language == "zh" else today.strftime("%B %d, %Y")
    title = title or f"{podcast.name} · {date_str}"

    # 3. TTS 转音频
    logger.info(f"[{podcast.name}] TTS 转换...")
    mp3_bytes, duration = await asyncio.to_thread(text_to_speech, script, podcast.voice)

    audio_filename = f"audio-{int(time.time())}.mp3"
    audio_rel = f"{podcast.id}/episodes/{today}/{audio_filename}"
    (ep_dir / audio_filename).write_bytes(mp3_bytes)
    if oss_enabled():
        await asyncio.to_thread(upload_file_sync, audio_rel, mp3_bytes)

    # 4. 更新 Episode 记录
    episode.title = title
    episode.script = script
    episode.shownotes = shownotes
    episode.audio_path = audio_rel
    episode.audio_duration = duration
    episode.audio_size = len(mp3_bytes)
    episode.tweet_count = len(tweets)
    episode.status = "done"
    await save_episode(episode)

    # 5. 重新生成 feed.xml
    logger.info(f"[{podcast.name}] 更新 feed.xml...")
    episodes = await list_episodes(podcast.id, limit=30)
    done_episodes = [e for e in episodes if e.status == "done"]
    xml_bytes = await asyncio.to_thread(build_feed, podcast, done_episodes)
    feed_file = STATIC_DIR / podcast.id / "feed.xml"
    feed_file.write_bytes(xml_bytes)

    # 6. 飞书通知
    if podcast.feishu_webhook:
        try:
            await asyncio.to_thread(send_feishu_notification, podcast.feishu_webhook, podcast, episode)
        except Exception:
            logger.warning(f"[{podcast.name}] 飞书通知发送失败", exc_info=True)

    logger.info(f"[{podcast.name}] 生成完成：{title}")
