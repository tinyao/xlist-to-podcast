"""
X List 推文抓取 + 预处理文本生成。
输出格式参考 xtest.py，生成 agent-readable 结构化纯文本，直接送入 LLM。
"""
import re
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional

import requests

from app.config import settings

BASE_URL = "https://api.x.com/2"

TWEET_FIELDS = ",".join([
    "attachments", "author_id", "conversation_id", "created_at",
    "entities", "id", "in_reply_to_user_id",
    "note_tweet", "public_metrics", "referenced_tweets", "text",
])

EXPANSIONS = ",".join([
    "attachments.media_keys", "attachments.poll_ids", "author_id",
    "in_reply_to_user_id",
    "referenced_tweets.id", "referenced_tweets.id.author_id",
])

MEDIA_FIELDS = ",".join([
    "alt_text", "duration_ms", "media_key", "type", "url", "variants",
])

USER_FIELDS = "description,id,name,url,username"
POLL_FIELDS = "duration_minutes,end_datetime,id,options,voting_status"


def parse_list_id(url: str) -> str:
    """从 X List URL 提取数字 list_id。"""
    match = re.search(r"/lists/(\d+)", url)
    if not match:
        raise ValueError(
            f"无法从 URL 解析 List ID，请使用数字 ID 格式的链接：{url}\n"
            "例如：https://x.com/i/lists/1234567890"
        )
    return match.group(1)


# ---------------------------------------------------------------------------
# 内部工具函数
# ---------------------------------------------------------------------------

def _api_get(session: requests.Session, url: str, params: dict) -> Optional[dict]:
    while True:
        resp = session.get(url, params=params, timeout=30)
        if resp.status_code == 429:
            reset = resp.headers.get("x-rate-limit-reset")
            wait = max(int(reset) - int(time.time()) + 2, 5) if reset else 60
            time.sleep(wait)
            continue
        if resp.status_code != 200:
            raise RuntimeError(f"X API {resp.status_code}: {resp.text[:300]}")
        return resp.json()


def _build_maps(includes: dict) -> dict:
    return {
        "users":  {u["id"]:         u for u in includes.get("users",  [])},
        "media":  {m["media_key"]:  m for m in includes.get("media",  [])},
        "tweets": {t["id"]:         t for t in includes.get("tweets", [])},
        "polls":  {p["id"]:         p for p in includes.get("polls",  [])},
    }


def _full_text(tweet: dict) -> str:
    """长推文优先取 note_tweet.text，否则取 text 字段。"""
    note = tweet.get("note_tweet")
    if note and note.get("text"):
        return note["text"]
    return tweet.get("text", "")


def _best_video_url(media: dict) -> Optional[str]:
    mp4s = [v for v in media.get("variants", []) if v.get("content_type") == "video/mp4"]
    if not mp4s:
        return None
    mp4s.sort(key=lambda v: v.get("bit_rate", 0), reverse=True)
    return mp4s[0].get("url")


def _expanded_urls(tweet: dict) -> list[str]:
    """提取外部 URL，排除 t.co 包装的 x.com/twitter.com 自身链接。"""
    urls = []
    for src in [tweet.get("entities") or {}, (tweet.get("note_tweet") or {}).get("entities") or {}]:
        for u in src.get("urls", []):
            exp = u.get("expanded_url", "")
            if exp and "twitter.com" not in exp and "x.com" not in exp:
                title = u.get("title")
                urls.append(f"{exp} ({title})" if title else exp)
    return urls


def _is_valid(tweet: dict) -> bool:
    """过滤纯转推、@回复、过短推文。"""
    text = _full_text(tweet)
    if text.startswith("RT @"):
        return False
    if text.startswith("@"):
        return False
    if len(text.strip()) < 20:
        return False
    return True


# ---------------------------------------------------------------------------
# 格式化：生成 agent-readable 结构化文本（与 xtest.py 格式一致）
# ---------------------------------------------------------------------------

def _format_tweet(tweet: dict, maps: dict, index: int) -> str:
    lines = []

    author_id = tweet.get("author_id")
    user = maps["users"].get(author_id, {})

    lines.append(f"[tweet {index + 1}]")
    lines.append(f"id: {tweet.get('id')}")
    lines.append(f"author: {user.get('name', '?')} (@{user.get('username', '?')})")
    if user.get("description"):
        lines.append(f"author_bio: {user['description'].replace(chr(10), ' ')}")
    lines.append(f"time: {tweet.get('created_at', '')}")

    # 引用 / 回复原文
    for ref in tweet.get("referenced_tweets", []):
        ref_tweet = maps["tweets"].get(ref.get("id"))
        if ref_tweet:
            ref_user = maps["users"].get(ref_tweet.get("author_id"), {})
            ref_label = f"{ref_user.get('name', '?')} (@{ref_user.get('username', '?')})"
            ref_text = _full_text(ref_tweet).replace("\n", "\n  ")
            lines.append(f"{ref.get('type')}: {ref_label}")
            lines.append(f"  {ref_text}")
        else:
            lines.append(f"{ref.get('type')}: [unavailable] id={ref.get('id')}")

    # 正文（多行缩进对齐）
    lines.append(f"text: {_full_text(tweet).replace(chr(10), chr(10) + '  ')}")

    # 媒体
    for mk in tweet.get("attachments", {}).get("media_keys", []):
        m = maps["media"].get(mk)
        if not m:
            continue
        mtype = m.get("type", "")
        if mtype == "photo":
            entry = f"photo: {m.get('url', '')}"
            if m.get("alt_text"):
                entry += f" | alt: {m['alt_text']}"
            lines.append(f"media: {entry}")
        elif mtype == "video":
            url = _best_video_url(m) or m.get("preview_image_url", "")
            entry = f"video: {url}"
            if m.get("duration_ms"):
                entry += f" | duration: {m['duration_ms'] // 1000}s"
            lines.append(f"media: {entry}")
        elif mtype == "animated_gif":
            lines.append(f"media: gif: {_best_video_url(m) or ''}")

    # 投票
    for pid in tweet.get("attachments", {}).get("poll_ids", []):
        poll = maps["polls"].get(pid)
        if poll:
            opts = [f"{o.get('label')}={o.get('votes', 0)}" for o in poll.get("options", [])]
            lines.append(f"poll: {' | '.join(opts)} (status: {poll.get('voting_status', '?')})")

    # 外部链接
    for u in _expanded_urls(tweet):
        lines.append(f"link: {u}")

    # 互动数据
    pm = tweet.get("public_metrics", {})
    if pm:
        keys = ["like_count", "retweet_count", "reply_count", "quote_count", "bookmark_count"]
        parts = [f"{k}={pm[k]}" for k in keys if k in pm]
        if parts:
            lines.append(f"metrics: {', '.join(parts)}")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# 对外接口
# ---------------------------------------------------------------------------

@dataclass
class FetchResult:
    """抓取结果：推文数 + 格式化文本（直接送入 LLM）。"""
    count: int
    text: str

    def __len__(self) -> int:
        return self.count


def fetch_list_tweets(list_id: str, since: datetime, max_tweets: int = 300) -> FetchResult:
    """
    抓取 X List 自 since 起的推文，返回 agent-readable 格式化文本。
    同步函数，在 pipeline 中应通过 asyncio.to_thread 调用。
    """
    if since.tzinfo is None:
        since = since.replace(tzinfo=timezone.utc)

    session = requests.Session()
    session.headers["Authorization"] = f"Bearer {settings.twitter_bearer_token}"

    all_tweets: list[dict] = []
    global_maps: dict = {"users": {}, "media": {}, "tweets": {}, "polls": {}}
    pagination_token = None

    while len(all_tweets) < max_tweets:
        params: dict = {
            "max_results": 100,
            "tweet.fields": TWEET_FIELDS,
            "expansions": EXPANSIONS,
            "media.fields": MEDIA_FIELDS,
            "user.fields": USER_FIELDS,
            "poll.fields": POLL_FIELDS,
        }
        if pagination_token:
            params["pagination_token"] = pagination_token

        resp = _api_get(session, f"{BASE_URL}/lists/{list_id}/tweets", params)
        data = resp.get("data") if resp else None
        if not data:
            break

        # 合并 includes maps（跨页去重）
        maps = _build_maps(resp.get("includes", {}))
        for key in global_maps:
            global_maps[key].update(maps[key])

        # 过滤：时间范围 + 内容规则
        page_has_new = False
        for t in data:
            created = t.get("created_at", "")
            if created:
                tweet_time = datetime.fromisoformat(created.replace("Z", "+00:00"))
                if tweet_time < since:
                    continue
                page_has_new = True
            if _is_valid(t):
                all_tweets.append(t)

        # 本页全部早于 since，无需继续翻页
        if not page_has_new:
            break

        pagination_token = (resp.get("meta") or {}).get("next_token")
        if not pagination_token:
            break

        time.sleep(0.5)  # 避免过快触发限速

    # 按时间倒序（最新在前）
    all_tweets.sort(key=lambda t: t.get("created_at", ""), reverse=True)
    all_tweets = all_tweets[:max_tweets]

    # 生成 agent-readable 文本
    header_lines = [
        f"list_id: {list_id}",
        f"fetched_at: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        f"total_tweets: {len(all_tweets)}",
        "",
    ]
    blocks = [_format_tweet(t, global_maps, i) for i, t in enumerate(all_tweets)]
    formatted_text = "\n".join(header_lines) + "\n\n".join(blocks)

    return FetchResult(count=len(all_tweets), text=formatted_text)
