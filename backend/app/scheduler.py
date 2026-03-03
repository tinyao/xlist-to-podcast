import asyncio
import logging
from datetime import datetime
from zoneinfo import ZoneInfo

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from app.storage import list_podcasts

logger = logging.getLogger(__name__)
scheduler = AsyncIOScheduler(timezone="Asia/Shanghai")


async def _dispatch_hourly():
    """每小时整点：找出设定在当前小时发布的播客并触发生成。"""
    current_hour = datetime.now(ZoneInfo("Asia/Shanghai")).hour
    logger.info(f"[Scheduler] 整点检查 hour={current_hour}")

    podcasts = await list_podcasts()
    due = [p for p in podcasts if p.is_active and p.publish_hour == current_hour]
    logger.info(f"[Scheduler] 找到 {len(due)} 个播客需要生成")

    from app.pipeline import generate_episode
    for podcast in due:
        asyncio.create_task(generate_episode(podcast.id))


def start():
    scheduler.add_job(
        _dispatch_hourly,
        CronTrigger(minute=0),
        id="hourly_dispatch",
        replace_existing=True,
        misfire_grace_time=300,
    )
    scheduler.start()
    logger.info("[Scheduler] 已启动，每小时整点检查播客生成任务")


def stop():
    scheduler.shutdown(wait=False)
