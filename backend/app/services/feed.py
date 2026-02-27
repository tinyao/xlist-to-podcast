from datetime import timezone

from feedgen.feed import FeedGenerator

from app.config import settings


def build_and_upload_feed(podcast, episodes: list) -> None:
    """
    重新生成 feed.xml 并上传覆盖 OSS。
    podcast: Podcast ORM 对象
    episodes: 最近 30 期 Episode ORM 对象列表（按日期倒序）
    """
    from app.services import oss  # 避免循环导入

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

    fg.podcast.itunes_explicit("no")
    fg.podcast.itunes_author(podcast.name)

    # 只保留最近 30 期，按时间正序加入（RSS 规范：新在前，feedgen 会倒序）
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

    xml_bytes = fg.rss_str(pretty=True)
    oss.upload(podcast.feed_oss_key, xml_bytes, content_type="application/rss+xml")
