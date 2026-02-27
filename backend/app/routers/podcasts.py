from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import Podcast
from app.schemas import PodcastCreate, PodcastOut
from app.services import oss
from app.services.twitter import parse_list_id

router = APIRouter(prefix="/api/podcasts", tags=["podcasts"])


@router.post("", response_model=PodcastOut, status_code=201)
async def create_podcast(
    name: str = Form(...),
    description: str = Form(""),
    twitter_list_url: str = Form(...),
    voice: str = Form("nova"),
    language: str = Form("zh"),
    publish_hour: int = Form(8),
    cover: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
):
    # 验证 List URL
    try:
        list_id = parse_list_id(twitter_list_url)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))

    # 创建 Podcast 记录（先拿到 id，用于 OSS 路径）
    podcast = Podcast(
        name=name.strip(),
        description=description.strip(),
        twitter_list_id=list_id,
        twitter_list_url=twitter_list_url,
        voice=voice,
        language=language,
        publish_hour=publish_hour,
    )
    db.add(podcast)
    await db.flush()  # 获取生成的 id

    # 上传封面
    cover_data = await cover.read()
    cover_key = f"{podcast.id}/cover.jpg"
    oss.upload(cover_key, cover_data, content_type=cover.content_type or "image/jpeg")
    podcast.cover_oss_key = cover_key

    # 初始化空 feed.xml
    feed_key = f"{podcast.id}/feed.xml"
    podcast.feed_oss_key = feed_key

    await db.commit()
    await db.refresh(podcast)

    # 生成初始 feed（无 episode）
    from app.services.feed import build_and_upload_feed
    build_and_upload_feed(podcast, [])

    return podcast


@router.get("", response_model=list[PodcastOut])
async def list_podcasts(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Podcast).order_by(Podcast.created_at.desc()))
    return result.scalars().all()


@router.get("/{podcast_id}", response_model=PodcastOut)
async def get_podcast(podcast_id: str, db: AsyncSession = Depends(get_db)):
    podcast = await db.get(Podcast, podcast_id)
    if not podcast:
        raise HTTPException(status_code=404, detail="播客不存在")
    return podcast


@router.delete("/{podcast_id}", status_code=204)
async def delete_podcast(podcast_id: str, db: AsyncSession = Depends(get_db)):
    podcast = await db.get(Podcast, podcast_id)
    if not podcast:
        raise HTTPException(status_code=404, detail="播客不存在")
    await db.delete(podcast)
    await db.commit()
