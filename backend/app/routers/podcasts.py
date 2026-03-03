import asyncio
from pathlib import Path

from fastapi import APIRouter, HTTPException, UploadFile, File, Form

from app.storage import Podcast, save_podcast, get_podcast, list_podcasts, delete_podcast
from app.schemas import PodcastOut
from app.services.twitter import parse_list_id
from app.services.feed import build_feed
from app.services.oss import upload_file_sync, is_enabled as oss_enabled

router = APIRouter(prefix="/api/podcasts", tags=["podcasts"])

STATIC_DIR = Path("data/static")


@router.post("", response_model=PodcastOut, status_code=201)
async def create_podcast(
    name: str = Form(...),
    description: str = Form(""),
    twitter_list_url: str = Form(...),
    voice: str = Form("nova"),
    language: str = Form("zh"),
    publish_hour: int = Form(8),
    cover: UploadFile = File(...),
):
    try:
        list_id = parse_list_id(twitter_list_url)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))

    podcast = Podcast(
        name=name.strip(),
        description=description.strip(),
        twitter_list_id=list_id,
        twitter_list_url=twitter_list_url,
        voice=voice,
        language=language,
        publish_hour=publish_hour,
    )

    podcast_dir = STATIC_DIR / podcast.id
    podcast_dir.mkdir(parents=True, exist_ok=True)

    cover_path = f"{podcast.id}/cover.jpg"
    cover_bytes = await cover.read()
    (podcast_dir / "cover.jpg").write_bytes(cover_bytes)
    podcast.cover_path = cover_path

    await save_podcast(podcast)

    xml_bytes = build_feed(podcast, [])
    (podcast_dir / "feed.xml").write_bytes(xml_bytes)

    if oss_enabled():
        await asyncio.to_thread(upload_file_sync, cover_path, cover_bytes)
        podcast_json = (podcast_dir / "podcast.json").read_bytes()
        await asyncio.to_thread(upload_file_sync, f"{podcast.id}/podcast.json", podcast_json)
        await asyncio.to_thread(upload_file_sync, f"{podcast.id}/feed.xml", xml_bytes)

    return podcast


@router.get("", response_model=list[PodcastOut])
async def list_podcasts_route():
    return await list_podcasts()


@router.get("/{podcast_id}", response_model=PodcastOut)
async def get_podcast_route(podcast_id: str):
    podcast = await get_podcast(podcast_id)
    if not podcast:
        raise HTTPException(status_code=404, detail="播客不存在")
    return podcast


@router.delete("/{podcast_id}", status_code=204)
async def delete_podcast_route(podcast_id: str):
    podcast = await get_podcast(podcast_id)
    if not podcast:
        raise HTTPException(status_code=404, detail="播客不存在")
    await delete_podcast(podcast_id)
