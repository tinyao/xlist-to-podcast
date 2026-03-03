"""
文件存储层，替代 SQLite/SQLAlchemy。

布局：
  data/static/
    {podcast_id}/
      podcast.json
      cover.jpg
      feed.xml
      episodes/
        {YYYY-MM-DD}/
          episode.json
          posts.md  script.md  audio.mp3  shownotes.md
"""
from __future__ import annotations

import asyncio
import shutil
import uuid
from datetime import datetime, date
from pathlib import Path
from typing import Optional

from pydantic import BaseModel, Field

from app.services.oss import public_url

STATIC_DIR = Path("data/static")


# ── helpers ──────────────────────────────────────────────────────────────────

def _new_id() -> str:
    return str(uuid.uuid4())


def _now() -> datetime:
    return datetime.utcnow()


# ── models ───────────────────────────────────────────────────────────────────

class Podcast(BaseModel):
    id: str = Field(default_factory=_new_id)
    name: str
    description: str = ""
    twitter_list_id: str
    twitter_list_url: str
    voice: str = "nova"
    language: str = "zh"
    cover_path: str = ""
    publish_hour: int = 8
    is_active: bool = True
    created_at: datetime = Field(default_factory=_now)
    updated_at: datetime = Field(default_factory=_now)

    model_config = {"from_attributes": True}

    @property
    def cover_url(self) -> str:
        return public_url(self.cover_path)

    @property
    def feed_url(self) -> str:
        return public_url(f"{self.id}/feed.xml")


class Episode(BaseModel):
    id: str = Field(default_factory=_new_id)
    podcast_id: str
    date: date
    title: str = ""
    script: str = ""
    shownotes: str = ""
    audio_path: str = ""
    audio_duration: int = 0
    audio_size: int = 0
    tweet_count: int = 0
    status: str = "pending"
    error_msg: str = ""
    created_at: datetime = Field(default_factory=_now)

    model_config = {"from_attributes": True}

    @property
    def audio_url(self) -> str:
        return public_url(self.audio_path)


# ── Podcast CRUD ─────────────────────────────────────────────────────────────

def _podcast_path(podcast_id: str) -> Path:
    return STATIC_DIR / podcast_id / "podcast.json"


def _save_podcast_sync(podcast: Podcast) -> None:
    path = _podcast_path(podcast.id)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(podcast.model_dump_json(), encoding="utf-8")


def _load_podcast_sync(podcast_id: str) -> Optional[Podcast]:
    path = _podcast_path(podcast_id)
    if not path.exists():
        return None
    return Podcast.model_validate_json(path.read_text(encoding="utf-8"))


def _list_podcasts_sync() -> list[Podcast]:
    podcasts: list[Podcast] = []
    for path in STATIC_DIR.glob("*/podcast.json"):
        try:
            podcasts.append(Podcast.model_validate_json(path.read_text(encoding="utf-8")))
        except Exception:
            pass
    podcasts.sort(key=lambda p: p.created_at, reverse=True)
    return podcasts


def _delete_podcast_sync(podcast_id: str) -> None:
    podcast_dir = STATIC_DIR / podcast_id
    if podcast_dir.exists():
        shutil.rmtree(podcast_dir)


async def save_podcast(podcast: Podcast) -> None:
    await asyncio.to_thread(_save_podcast_sync, podcast)


async def get_podcast(podcast_id: str) -> Optional[Podcast]:
    return await asyncio.to_thread(_load_podcast_sync, podcast_id)


async def list_podcasts() -> list[Podcast]:
    return await asyncio.to_thread(_list_podcasts_sync)


async def delete_podcast(podcast_id: str) -> None:
    await asyncio.to_thread(_delete_podcast_sync, podcast_id)


# ── Episode CRUD ──────────────────────────────────────────────────────────────

def _episode_json_path(podcast_id: str, ep_date: date) -> Path:
    return STATIC_DIR / podcast_id / "episodes" / str(ep_date) / "episode.json"


def _save_episode_sync(episode: Episode) -> None:
    path = _episode_json_path(episode.podcast_id, episode.date)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(episode.model_dump_json(), encoding="utf-8")


def _load_episode_sync(podcast_id: str, ep_date: date) -> Optional[Episode]:
    path = _episode_json_path(podcast_id, ep_date)
    if not path.exists():
        return None
    return Episode.model_validate_json(path.read_text(encoding="utf-8"))


def _list_episodes_sync(podcast_id: str, limit: int = 50) -> list[Episode]:
    ep_root = STATIC_DIR / podcast_id / "episodes"
    if not ep_root.exists():
        return []
    episodes: list[Episode] = []
    for path in ep_root.glob("*/episode.json"):
        try:
            episodes.append(Episode.model_validate_json(path.read_text(encoding="utf-8")))
        except Exception:
            pass
    episodes.sort(key=lambda e: e.date, reverse=True)
    return episodes[:limit]


async def save_episode(episode: Episode) -> None:
    await asyncio.to_thread(_save_episode_sync, episode)


async def get_episode(podcast_id: str, ep_date: date) -> Optional[Episode]:
    return await asyncio.to_thread(_load_episode_sync, podcast_id, ep_date)


async def list_episodes(podcast_id: str, limit: int = 50) -> list[Episode]:
    return await asyncio.to_thread(_list_episodes_sync, podcast_id, limit)
