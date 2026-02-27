"""
Episode 生成完整流程：
Twitter 抓取 → LLM 生成 → TTS → OSS 上传 → Feed 更新
"""
import logging
from datetime import datetime, timedelta, timezone, date

from sqlalchemy import select

from app.database import AsyncSessionLocal
from app.models import Podcast, Episode
from app.services import oss
from app.services.twitter import fetch_list_tweets
from app.services.llm import generate_content
from app.services.tts import text_to_speech
from app.services.feed import build_and_upload_feed

logger = logging.getLogger(__name__)

MIN_TWEETS = 3  # 推文数低于此值跳过当日生成


async def generate_episode(podcast_id: str) -> None:
    async with AsyncSessionLocal() as db:
        podcast = await db.get(Podcast, podcast_id)
        if not podcast or not podcast.is_active:
            return

        today = date.today()

        # 检查今日是否已生成
        existing = await db.execute(
            select(Episode).where(
                Episode.podcast_id == podcast_id,
                Episode.date == today,
                Episode.status.in_(["done", "processing"]),
            )
        )
        if existing.scalar_one_or_none():
            logger.info(f"[{podcast.name}] 今日节目已存在，跳过")
            return

        # 创建 episode 记录，标记为 processing
        episode = Episode(
            podcast_id=podcast_id,
            date=today,
            status="processing",
        )
        db.add(episode)
        await db.commit()
        await db.refresh(episode)

        try:
            await _run_pipeline(db, podcast, episode, today)
        except Exception as e:
            logger.exception(f"[{podcast.name}] 生成失败: {e}")
            episode.status = "failed"
            episode.error_msg = str(e)
            await db.commit()


async def _run_pipeline(db, podcast: Podcast, episode: Episode, today: date) -> None:
    since = datetime.now(timezone.utc) - timedelta(hours=24)

    # 1. 抓取推文
    logger.info(f"[{podcast.name}] 抓取推文...")
    tweets = fetch_list_tweets(podcast.twitter_list_id, since)

    if len(tweets) < MIN_TWEETS:
        logger.info(f"[{podcast.name}] 推文数量不足（{len(tweets)} 条），跳过")
        episode.status = "failed"
        episode.error_msg = f"推文数量不足（{len(tweets)} 条，最少需要 {MIN_TWEETS} 条）"
        await db.commit()
        return

    # 2. LLM 生成 script + shownotes
    logger.info(f"[{podcast.name}] 生成内容（{len(tweets)} 条推文）...")
    script, shownotes = generate_content(
        tweets=tweets,
        podcast_name=podcast.name,
        language=podcast.language,
        today=today,
    )

    date_str = today.strftime("%Y年%m月%d日") if podcast.language == "zh" else today.strftime("%B %d, %Y")
    title = f"{podcast.name} · {date_str}"

    # 3. TTS 转音频
    logger.info(f"[{podcast.name}] TTS 转换...")
    mp3_bytes, duration = text_to_speech(script, podcast.voice)

    # 4. 上传 MP3
    audio_key = f"{podcast.id}/episodes/{today}.mp3"
    oss.upload(audio_key, mp3_bytes, content_type="audio/mpeg")

    # 5. 上传 shownotes
    notes_key = f"{podcast.id}/episodes/{today}.md"
    oss.upload(notes_key, shownotes.encode("utf-8"), content_type="text/markdown; charset=utf-8")

    # 6. 更新 Episode 记录
    episode.title = title
    episode.script = script
    episode.shownotes = shownotes
    episode.audio_oss_key = audio_key
    episode.audio_duration = duration
    episode.audio_size = len(mp3_bytes)
    episode.tweet_count = len(tweets)
    episode.status = "done"
    await db.commit()
    await db.refresh(episode)

    # 7. 重新生成 feed.xml
    logger.info(f"[{podcast.name}] 更新 Feed...")
    from sqlalchemy import select
    result = await db.execute(
        select(Episode)
        .where(Episode.podcast_id == podcast.id, Episode.status == "done")
        .order_by(Episode.date.desc())
        .limit(30)
    )
    episodes = result.scalars().all()
    build_and_upload_feed(podcast, episodes)

    logger.info(f"[{podcast.name}] 生成完成：{title}")
