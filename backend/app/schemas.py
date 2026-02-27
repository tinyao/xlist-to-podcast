from __future__ import annotations

from datetime import datetime, date
from typing import Literal

from pydantic import BaseModel, HttpUrl, field_validator


VOICES = Literal["alloy", "echo", "fable", "onyx", "nova", "shimmer"]
LANGUAGES = Literal["zh", "en"]
EPISODE_STATUS = Literal["pending", "processing", "done", "failed"]


# ── Podcast ──────────────────────────────────────────────────────────────────

class PodcastCreate(BaseModel):
    name: str
    description: str = ""
    twitter_list_url: str
    voice: VOICES = "nova"
    language: LANGUAGES = "zh"
    publish_hour: int = 8

    @field_validator("name")
    @classmethod
    def name_not_empty(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("播客名称不能为空")
        if len(v) > 100:
            raise ValueError("播客名称不能超过 100 字符")
        return v

    @field_validator("publish_hour")
    @classmethod
    def valid_hour(cls, v: int) -> int:
        if not 0 <= v <= 23:
            raise ValueError("publish_hour 必须在 0-23 之间")
        return v


class PodcastOut(BaseModel):
    id: str
    name: str
    description: str
    twitter_list_url: str
    voice: str
    language: str
    publish_hour: int
    cover_url: str
    feed_url: str
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}


# ── Episode ───────────────────────────────────────────────────────────────────

class EpisodeOut(BaseModel):
    id: str
    podcast_id: str
    date: date
    title: str
    shownotes: str
    audio_url: str
    audio_duration: int
    tweet_count: int
    status: str
    error_msg: str
    created_at: datetime

    model_config = {"from_attributes": True}


class EpisodeDetail(EpisodeOut):
    script: str
