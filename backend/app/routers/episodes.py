import asyncio
from datetime import date

from fastapi import APIRouter, HTTPException

from app.storage import get_podcast, get_episode, list_episodes
from app.schemas import EpisodeOut, EpisodeDetail

router = APIRouter(prefix="/api/podcasts", tags=["episodes"])


@router.get("/{podcast_id}/episodes", response_model=list[EpisodeOut])
async def list_episodes_route(podcast_id: str):
    podcast = await get_podcast(podcast_id)
    if not podcast:
        raise HTTPException(status_code=404, detail="播客不存在")
    return await list_episodes(podcast_id)


@router.get("/{podcast_id}/episodes/{episode_date}", response_model=EpisodeDetail)
async def get_episode_route(podcast_id: str, episode_date: str):
    try:
        ep_date = date.fromisoformat(episode_date)
    except ValueError:
        raise HTTPException(status_code=422, detail="日期格式无效，应为 YYYY-MM-DD")
    episode = await get_episode(podcast_id, ep_date)
    if not episode:
        raise HTTPException(status_code=404, detail="节目不存在")
    return episode


@router.post("/{podcast_id}/episodes/trigger", status_code=202)
async def trigger_episode(podcast_id: str):
    """手动触发当日节目生成（异步，立即返回）。"""
    podcast = await get_podcast(podcast_id)
    if not podcast:
        raise HTTPException(status_code=404, detail="播客不存在")

    from app.pipeline import generate_episode
    asyncio.create_task(generate_episode(podcast_id))

    return {"message": "生成任务已触发", "podcast_id": podcast_id}
