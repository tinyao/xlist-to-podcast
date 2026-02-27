import asyncio
import logging
from zoneinfo import ZoneInfo

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from sqlalchemy import select

from app.database import AsyncSessionLocal
from app.models import Podcast

logger = logging.getLogger(__name__)
scheduler = AsyncIOScheduler(timezone="Asia/Shanghai")


async def _dispatch_hourly():
    """每小时整点：找出设定在当前小时发布的播客并触发生成。"""
    from zoneinfo import ZoneInfo
    from datetime import datetime

    current_hour = datetime.now(ZoneInfo("Asia/Shanghai")).hour
    logger.info(f"[Scheduler] 整点检查 hour={current_hour}")

    async with AsyncSessionLocal() as db:
        result = await db.execute(
            select(Podcast).where(
                Podcast.publish_hour == current_hour,
                Podcast.is_active == True,
            )
        )
        podcasts = result.scalars().all()

    logger.info(f"[Scheduler] 找到 {len(podcasts)} 个播客需要生成")

    from app.pipeline import generate_episode
    for podcast in podcasts:
        asyncio.create_task(generate_episode(podcast.id))


def start():
    scheduler.add_job(
        _dispatch_hourly,
        CronTrigger(minute=0),  # 每小时 :00 触发
        id="hourly_dispatch",
        replace_existing=True,
        misfire_grace_time=300,  # 5 分钟内补跑
    )
    scheduler.start()
    logger.info("[Scheduler] 已启动，每小时整点检查播客生成任务")


def stop():
    scheduler.shutdown(wait=False)
