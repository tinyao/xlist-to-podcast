"""飞书 Webhook 通知服务。"""
import json
import logging
from urllib.request import Request, urlopen

from app.storage import Podcast, Episode

logger = logging.getLogger(__name__)


def send_feishu_notification(webhook_url: str, podcast: Podcast, episode: Episode) -> None:
    """发送飞书 interactive card 通知，失败只 log 不抛异常。"""
    actions = [
        {
            "tag": "button",
            "text": {"tag": "plain_text", "content": "🎧 收听本期"},
            "url": episode.audio_url,
            "type": "primary_filled",
        },
    ]
    if podcast.subscribe_url:
        actions.append({
            "tag": "button",
            "text": {"tag": "plain_text", "content": "🌟 订阅播客"},
            "url": podcast.subscribe_url,
            "type": "default",
        })

    card = {
        "msg_type": "interactive",
        "card": {
            "header": {
                "title": {"tag": "plain_text", "content": f"🎙 {episode.title}"},
                "template": "blue",
                "padding": "12px 12px 12px 12px"
            },
            "elements": [
                {"tag": "markdown", "content": episode.shownotes},
                {"tag": "hr"},
                {"tag": "action", "actions": actions},
            ],
        },
    }

    body = json.dumps(card, ensure_ascii=False).encode("utf-8")
    req = Request(webhook_url, data=body, headers={"Content-Type": "application/json; charset=utf-8"})

    try:
        with urlopen(req, timeout=10) as resp:
            result = json.loads(resp.read())
            if result.get("code", 0) != 0:
                logger.warning(f"[{podcast.name}] 飞书返回错误: {result}")
            else:
                logger.info(f"[{podcast.name}] 飞书通知已发送")
    except Exception:
        logger.warning(f"[{podcast.name}] 飞书通知发送失败", exc_info=True)
