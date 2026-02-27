import re
from dataclasses import dataclass
from datetime import datetime, timezone

import tweepy

from app.config import settings


@dataclass
class Tweet:
    id: str
    text: str
    author_username: str
    author_name: str
    created_at: datetime
    like_count: int
    retweet_count: int


def parse_list_id(url: str) -> str:
    """
    从 Twitter List URL 提取 list_id。
    支持格式：
      https://x.com/i/lists/1234567890
      https://twitter.com/user/lists/some-slug  （slug 格式暂不支持，需要用户提供数字 ID 链接）
    """
    match = re.search(r"/lists/(\d+)", url)
    if not match:
        raise ValueError(
            f"无法从 URL 解析 List ID，请使用数字 ID 格式的链接：{url}\n"
            "例如：https://x.com/i/lists/1234567890"
        )
    return match.group(1)


def _is_valid_tweet(text: str) -> bool:
    """过滤纯转推、@回复、过短推文。"""
    if text.startswith("RT @"):
        return False
    if text.startswith("@"):
        return False
    if len(text.strip()) < 20:
        return False
    return True


def fetch_list_tweets(list_id: str, since: datetime) -> list[Tweet]:
    """
    同步抓取指定 List 自 since 时间以来的推文。
    返回过滤后的推文列表，最多 100 条。
    """
    client = tweepy.Client(
        bearer_token=settings.twitter_bearer_token,
        wait_on_rate_limit=False,
    )

    # 确保 since 带时区
    if since.tzinfo is None:
        since = since.replace(tzinfo=timezone.utc)

    response = client.get_list_tweets(
        id=list_id,
        tweet_fields=["created_at", "author_id", "text", "public_metrics"],
        expansions=["author_id"],
        user_fields=["username", "name"],
        start_time=since,
        max_results=100,
    )

    if not response.data:
        return []

    # 构建 author 映射
    users: dict[str, tweepy.User] = {}
    if response.includes and "users" in response.includes:
        for user in response.includes["users"]:
            users[user.id] = user

    tweets: list[Tweet] = []
    for raw in response.data:
        if not _is_valid_tweet(raw.text):
            continue

        author = users.get(raw.author_id)
        metrics = raw.public_metrics or {}

        tweets.append(Tweet(
            id=raw.id,
            text=raw.text,
            author_username=author.username if author else "",
            author_name=author.name if author else "",
            created_at=raw.created_at or since,
            like_count=metrics.get("like_count", 0),
            retweet_count=metrics.get("retweet_count", 0),
        ))

    return tweets
