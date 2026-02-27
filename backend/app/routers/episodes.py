import asyncio

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import Podcast, Episode
from app.schemas import EpisodeOut, EpisodeDetail

router = APIRouter(prefix="/api/podcasts", tags=["episodes"])


@router.get("/{podcast_id}/episodes", response_model=list[EpisodeOut])
async def list_episodes(podcast_id: str, db: AsyncSession = Depends(get_db)):
    podcast = await db.get(Podcast, podcast_id)
    if not podcast:
        raise HTTPException(status_code=404, detail="播客不存在")

    result = await db.execute(
        select(Episode)
        .where(Episode.podcast_id == podcast_id)
        .order_by(Episode.date.desc())
        .limit(50)
    )
    return result.scalars().all()


@router.get("/{podcast_id}/episodes/{episode_date}", response_model=EpisodeDetail)
async def get_episode(podcast_id: str, episode_date: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Episode).where(
            Episode.podcast_id == podcast_id,
            Episode.date == episode_date,
        )
    )
    episode = result.scalar_one_or_none()
    if not episode:
        raise HTTPException(status_code=404, detail="节目不存在")
    return episode


@router.post("/{podcast_id}/episodes/trigger", status_code=202)
async def trigger_episode(podcast_id: str, db: AsyncSession = Depends(get_db)):
    """手动触发当日节目生成（异步，立即返回）。"""
    podcast = await db.get(Podcast, podcast_id)
    if not podcast:
        raise HTTPException(status_code=404, detail="播客不存在")

    from app.pipeline import generate_episode
    asyncio.create_task(generate_episode(podcast_id))

    return {"message": "生成任务已触发", "podcast_id": podcast_id}
