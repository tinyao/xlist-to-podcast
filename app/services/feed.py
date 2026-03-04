from datetime import timezone

from feedgen.feed import FeedGenerator

from app.config import settings


def build_feed(podcast, episodes: list) -> bytes:
    """
    根据 Podcast 和 Episode 列表生成 RSS feed XML，返回字节流。
    podcast: Podcast ORM 对象
    episodes: 最近 30 期 Episode ORM 对象列表（按日期倒序）
    """
    fg = FeedGenerator()
    fg.load_extension("podcast")

    feed_url = podcast.feed_url
    fg.id(feed_url)
    fg.title(podcast.name)
    fg.description(podcast.description or podcast.name)
    fg.language(podcast.language)
    fg.link(href=feed_url, rel="self")
    fg.link(href=feed_url, rel="alternate")

    if podcast.cover_url:
        fg.image(podcast.cover_url)
        fg.podcast.itunes_image(podcast.cover_url)

    fg.podcast.itunes_explicit("false")
    fg.podcast.itunes_author(podcast.owner_name or podcast.name)
    fg.podcast.itunes_type("episodic")
    fg.podcast.itunes_summary(podcast.description or podcast.name)
    fg.podcast.itunes_category(podcast.category or "Technology")
    if podcast.owner_name or podcast.owner_email:
        fg.podcast.itunes_owner(
            name=podcast.owner_name or podcast.name,
            email=podcast.owner_email or "",
        )

    for ep in reversed(episodes[:30]):
        if ep.status != "done":
            continue

        fe = fg.add_entry()
        fe.id(ep.audio_url)
        fe.title(ep.title or str(ep.date))
        fe.description(ep.shownotes or "")

        published = ep.created_at.replace(tzinfo=timezone.utc)
        fe.published(published)
        fe.updated(published)

        fe.enclosure(ep.audio_url, str(ep.audio_size), "audio/mpeg")
        fe.podcast.itunes_duration(str(ep.audio_duration))
        fe.podcast.itunes_summary((ep.shownotes or "")[:500])
        fe.podcast.itunes_episode_type("full")

    return fg.rss_str(pretty=True)
