"""
Episode 生成完整流程：
Twitter 抓取 → LLM 生成 → TTS → 写文件 → 更新 feed.xml

中间文件先写入 data/static/，最终由 generate.py 复制到 docs/ 供 GitHub Pages 托管。
每期目录结构（data/static/ 和 docs/ 下相同）：
  {podcast_id}/episodes/{YYYY-MM-DD}/
    ├── posts.md       抓取的原始推文
    ├── script.md      播客朗读稿
    ├── audio.mp3      TTS 音频（仅 data/static/，docs/ 不含音频）
    └── shownotes.md   节目说明
"""
import asyncio
import logging
import re
from datetime import datetime, time, timedelta, timezone, date
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

REPO_ROOT = Path(__file__).resolve().parent.parent
STATIC_DIR = Path("data/static")
DOCS_DIR = REPO_ROOT / "docs"
SHANGHAI_TZ = timezone(timedelta(hours=8))
MIN_TWEETS = 3


def _episode_dir(podcast_id: str, ep_date: date) -> Path:
    d = STATIC_DIR / podcast_id / "episodes" / str(ep_date)
    d.mkdir(parents=True, exist_ok=True)
    return d


async def generate_episode(podcast_id: str, max_posts: Optional[int] = None, frequency: str = "daily", extra_prompt: str = "") -> None:
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
        await _run_pipeline(podcast, episode, today, max_posts=max_posts, frequency=frequency, extra_prompt=extra_prompt)
    except Exception as e:
        logger.exception(f"[{podcast.name}] 生成失败: {e}")
        episode.status = "failed"
        episode.error_msg = str(e)
        await save_episode(episode)


async def _run_pipeline(podcast: Podcast, episode: Episode, today: date, max_posts: Optional[int] = None, frequency: str = "daily", extra_prompt: str = "") -> None:
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

    (ep_dir / "posts.md").write_text(tweets.text, encoding="utf-8")

    await _finalize_episode(podcast, episode, today, tweets, frequency, extra_prompt)


async def _finalize_episode(podcast: Podcast, episode: Episode, ep_date: date, tweets: FetchResult, frequency: str, extra_prompt: str) -> None:
    """LLM → TTS → episode.json → feed.xml → 飞书通知。被首次生成和重新生成共享。"""
    ep_dir = _episode_dir(podcast.id, ep_date)

    # 1. 获取近期 episodes（仅 daily 播客）
    recent_episodes = []
    if frequency == "daily":
        all_eps = await list_episodes(podcast.id, limit=5)
        recent_episodes = [e for e in all_eps if e.status == "done" and e.date < ep_date][:2]

    # 2. LLM 生成 script + shownotes + title
    logger.info(f"[{podcast.name}] 生成内容（{len(tweets)} 条推文）...")
    script, shownotes, title = await asyncio.to_thread(
        generate_content, tweets, podcast.name, podcast.language, ep_date, frequency, extra_prompt,
        prompt_file=podcast.prompt_file,
        recent_episodes=recent_episodes,
    )

    (ep_dir / "script.md").write_text(script, encoding="utf-8")
    (ep_dir / "shownotes.md").write_text(shownotes, encoding="utf-8")

    date_str = ep_date.strftime("%Y年%m月%d日") if podcast.language == "zh" else ep_date.strftime("%B %d, %Y")
    title = title or f"{podcast.name} · {date_str}"

    # 3. TTS 转音频
    logger.info(f"[{podcast.name}] TTS 转换...")
    mp3_bytes, duration = await asyncio.to_thread(text_to_speech, script, podcast.voice, podcast.tts_provider)

    audio_rel = f"{podcast.id}/episodes/{ep_date}/audio.mp3"
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
    episode.error_msg = ""
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


async def regenerate_episode(podcast_id: str, ep_date: date, extra_prompt: str = "") -> None:
    """复用已有 posts.md 重新生成某一期：跳过推文抓取，重跑 LLM + TTS + feed + 通知。"""
    podcast = await get_podcast(podcast_id)
    if not podcast or not podcast.is_active:
        logger.error(f"未找到或未启用的播客: {podcast_id}")
        return

    ep_dir = _episode_dir(podcast.id, ep_date)
    posts_path = ep_dir / "posts.md"

    # data/static/ 没有就从 docs/ 拷过来（CI 环境下 bootstrap 只恢复 episode.json）
    if not posts_path.exists():
        docs_posts = DOCS_DIR / podcast.id / "episodes" / str(ep_date) / "posts.md"
        if not docs_posts.exists():
            raise FileNotFoundError(
                f"找不到 posts.md，无法重新生成: {docs_posts}（同时检查了 {posts_path}）"
            )
        posts_path.write_text(docs_posts.read_text(encoding="utf-8"), encoding="utf-8")
        logger.info(f"[{podcast.name}] 从 docs/ 恢复 posts.md")

    posts_text = posts_path.read_text(encoding="utf-8")
    tweet_count = len(re.findall(r"^\[tweet \d+\]", posts_text, re.MULTILINE))
    if tweet_count == 0:
        logger.warning(f"[{podcast.name}] posts.md 中未识别到推文，仍然继续")
    tweets = FetchResult(count=tweet_count, text=posts_text)

    # 沿用已有 episode.json 的 created_at；新建时把 created_at 钉在 ep_date 中午 UTC，
    # 避免重新生成历史节目时 feed.xml 的 pubDate 全部贴成今天。
    existing = await get_episode(podcast.id, ep_date)
    if existing:
        episode = existing
    else:
        episode = Episode(
            podcast_id=podcast.id,
            date=ep_date,
            created_at=datetime.combine(ep_date, time(12, 0)),
        )
    episode.status = "processing"
    episode.error_msg = ""
    await save_episode(episode)

    logger.info(f"[{podcast.name}] 重新生成 {ep_date} 的 episode（{tweet_count} 条推文，跳过抓取）")
    try:
        await _finalize_episode(podcast, episode, ep_date, tweets, podcast.frequency, extra_prompt)
    except Exception as e:
        logger.exception(f"[{podcast.name}] 重新生成失败: {e}")
        episode.status = "failed"
        episode.error_msg = str(e)
        await save_episode(episode)
