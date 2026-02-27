from __future__ import annotations

import uuid
from datetime import datetime, date

from sqlalchemy import String, Boolean, Integer, Date, DateTime, Text, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


def new_uuid() -> str:
    return str(uuid.uuid4())


class Podcast(Base):
    __tablename__ = "podcasts"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, default="")
    twitter_list_id: Mapped[str] = mapped_column(String(64), nullable=False)
    twitter_list_url: Mapped[str] = mapped_column(String(512), nullable=False)
    voice: Mapped[str] = mapped_column(String(32), default="nova")
    language: Mapped[str] = mapped_column(String(8), default="zh")
    cover_oss_key: Mapped[str] = mapped_column(String(512), default="")
    feed_oss_key: Mapped[str] = mapped_column(String(512), default="")
    publish_hour: Mapped[int] = mapped_column(Integer, default=8)  # Asia/Shanghai
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )

    episodes: Mapped[list["Episode"]] = relationship(
        back_populates="podcast", order_by="Episode.date.desc()"
    )

    @property
    def cover_url(self) -> str:
        from app.config import settings
        return f"{settings.oss_base_url}/{self.cover_oss_key}" if self.cover_oss_key else ""

    @property
    def feed_url(self) -> str:
        from app.config import settings
        return f"{settings.oss_base_url}/{self.feed_oss_key}" if self.feed_oss_key else ""


class Episode(Base):
    __tablename__ = "episodes"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    podcast_id: Mapped[str] = mapped_column(String(36), ForeignKey("podcasts.id", ondelete="CASCADE"))
    date: Mapped[date] = mapped_column(Date, nullable=False)
    title: Mapped[str] = mapped_column(String(200), default="")
    script: Mapped[str] = mapped_column(Text, default="")
    shownotes: Mapped[str] = mapped_column(Text, default="")
    audio_oss_key: Mapped[str] = mapped_column(String(512), default="")
    audio_duration: Mapped[int] = mapped_column(Integer, default=0)   # 秒
    audio_size: Mapped[int] = mapped_column(Integer, default=0)        # bytes
    tweet_count: Mapped[int] = mapped_column(Integer, default=0)
    status: Mapped[str] = mapped_column(String(16), default="pending")
    # pending / processing / done / failed
    error_msg: Mapped[str] = mapped_column(Text, default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    podcast: Mapped["Podcast"] = relationship(back_populates="episodes")

    @property
    def audio_url(self) -> str:
        from app.config import settings
        return f"{settings.oss_base_url}/{self.audio_oss_key}" if self.audio_oss_key else ""
