"""
Episode 生成完整流程：
Twitter 抓取 → LLM 生成 → TTS → 写文件 → 更新 feed.xml

每期输出目录：data/static/{podcast_id}/episodes/{YYYY-MM-DD}/
  ├── posts.md       抓取的原始推文（xtest.py 格式）
  ├── script.md      播客朗读稿
  ├── audio.mp3      TTS 音频
  └── shownotes.md   节目说明
"""
import asyncio
import logging
from datetime import datetime, timedelta, timezone, date
from pathlib import Path
from typing import Optional

from app.storage import (
    Podcast, Episode,
    get_podcast, get_episode, save_episode, list_episodes,
)
from app.services.twitter import fetch_list_tweets
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


async def generate_episode(podcast_id: str, max_posts: Optional[int] = None, frequency: str = "daily", extra_prompt: str = "", prompt_file: Optional[str] = None) -> None:
    podcast = await get_podcast(podcast_id)
    if not podcast or not podcast.is_active:
        return

    today = datetime.now(SHANGHAI_TZ).date()

    existing = await get_episode(podcast_id, today)
    if existing and existing.status in ("done", "processing"):
        logger.info(f"[{podcast.name}] 今日节目已存在，跳过")
        return

    episode = Episode(podcast_id=podcast_id, date=today, status="processing")
    await save_episode(episode)

    try:
        await _run_pipeline(podcast, episode, today, max_posts=max_posts, frequency=frequency, extra_prompt=extra_prompt, prompt_file=prompt_file)
    except Exception as e:
        logger.exception(f"[{podcast.name}] 生成失败: {e}")
        episode.status = "failed"
        episode.error_msg = str(e)
        await save_episode(episode)


async def _run_pipeline(podcast: Podcast, episode: Episode, today: date, max_posts: Optional[int] = None, frequency: str = "daily", extra_prompt: str = "", prompt_file: Optional[str] = None) -> None:
    lookback_hours = 168 if frequency == "weekly" else 24
    since = datetime.now(timezone.utc) - timedelta(hours=lookback_hours)
    ep_dir = _episode_dir(podcast.id, today)

    # 1. 抓取推文
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

    # 2. LLM 生成 script + shownotes + title
    logger.info(f"[{podcast.name}] 生成内容（{len(tweets)} 条推文）...")
    script, shownotes, title = await asyncio.to_thread(
        generate_content, tweets, podcast.name, podcast.language, today, frequency, extra_prompt, prompt_file,
    )

    (ep_dir / "script.md").write_text(script, encoding="utf-8")
    (ep_dir / "shownotes.md").write_text(shownotes, encoding="utf-8")

    date_str = today.strftime("%Y年%m月%d日") if podcast.language == "zh" else today.strftime("%B %d, %Y")
    title = title or f"{podcast.name} · {date_str}"

    # 3. TTS 转音频
    logger.info(f"[{podcast.name}] TTS 转换...")
    mp3_bytes, duration = await asyncio.to_thread(text_to_speech, script, podcast.voice)

    audio_rel = f"{podcast.id}/episodes/{today}/audio.mp3"
    (ep_dir / "audio.mp3").write_bytes(mp3_bytes)
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
