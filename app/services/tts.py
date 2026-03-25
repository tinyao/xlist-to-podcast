import base64
import io
import json
import logging
import re
import uuid

import requests
from mutagen.mp3 import MP3
from openai import OpenAI

from app.config import settings

logger = logging.getLogger(__name__)

_MAX_CHARS = 4000  # OpenAI TTS 单次请求上限略低于 4096，留余量
_DOUBAO_MAX_CHARS = 4000  # 豆包 TTS 单次请求字符上限
_DOUBAO_API_URL = "https://openspeech.bytedance.com/api/v1/tts"


def _split_text(text: str, max_chars: int = _MAX_CHARS) -> list[str]:
    """按句子边界切割长文本，避免在句子中间断开。"""
    # 匹配中英文句末标点
    sentences = re.split(r"(?<=[。！？.!?])\s*", text)
    chunks: list[str] = []
    current = ""
    for sentence in sentences:
        if len(current) + len(sentence) > max_chars:
            if current:
                chunks.append(current.strip())
            current = sentence
        else:
            current += sentence
    if current.strip():
        chunks.append(current.strip())
    return chunks


def _openai_tts(text: str, voice: str) -> bytes:
    """使用 OpenAI TTS 合成音频，返回 MP3 字节。"""
    client = OpenAI(api_key=settings.openai_api_key)
    chunks = _split_text(text, _MAX_CHARS)
    parts: list[bytes] = []

    for chunk in chunks:
        response = client.audio.speech.create(
            model="tts-1-hd",
            voice=voice,
            input=chunk,
            response_format="mp3",
        )
        parts.append(response.content)

    return b"".join(parts)


def _doubao_tts(text: str, voice: str) -> bytes:
    """使用火山引擎豆包 TTS 合成音频，返回 MP3 字节。"""
    appid = settings.volcengine_tts_appid
    token = settings.volcengine_tts_token
    if not appid or not token:
        raise ValueError("豆包 TTS 需要配置 VOLCENGINE_TTS_APPID 和 VOLCENGINE_TTS_TOKEN")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer;{token}",
    }

    chunks = _split_text(text, _DOUBAO_MAX_CHARS)
    parts: list[bytes] = []

    for chunk in chunks:
        body = {
            "app": {
                "appid": appid,
                "token": token,
                "cluster": "volcano_tts",
            },
            "user": {
                "uid": "xlist-to-podcast",
            },
            "audio": {
                "voice_type": voice,
                "encoding": "mp3",
                "speed_ratio": 1.0,
            },
            "request": {
                "reqid": str(uuid.uuid4()),
                "text": chunk,
                "operation": "query",
            },
        }

        resp = requests.post(_DOUBAO_API_URL, headers=headers, data=json.dumps(body), timeout=60)
        resp.raise_for_status()
        result = resp.json()

        if result.get("code") == 3000:
            audio_bytes = base64.b64decode(result["data"])
            parts.append(audio_bytes)
        else:
            raise RuntimeError(
                f"豆包 TTS 错误: code={result.get('code')}, message={result.get('message', 'Unknown')}"
            )

    return b"".join(parts)


def text_to_speech(text: str, voice: str, provider: str = "openai") -> tuple[bytes, int]:
    """
    将文本转为 MP3 音频。
    长文本自动分段请求后拼接。
    返回 (mp3_bytes, duration_seconds)。

    provider: "openai" 或 "doubao"
    """
    if provider == "doubao":
        mp3_bytes = _doubao_tts(text, voice)
    else:
        mp3_bytes = _openai_tts(text, voice)

    # 计算时长
    audio = MP3(io.BytesIO(mp3_bytes))
    duration = int(audio.info.length)

    return mp3_bytes, duration
