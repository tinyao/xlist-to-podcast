import io
import re

from mutagen.mp3 import MP3
from openai import OpenAI

from app.config import settings

_MAX_CHARS = 4000  # OpenAI TTS 单次请求上限略低于 4096，留余量


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


def text_to_speech(text: str, voice: str) -> tuple[bytes, int]:
    """
    将文本转为 MP3 音频。
    长文本自动分段请求后拼接。
    返回 (mp3_bytes, duration_seconds)。
    """
    client = OpenAI(api_key=settings.openai_api_key)
    chunks = _split_text(text)
    parts: list[bytes] = []

    for chunk in chunks:
        response = client.audio.speech.create(
            model="tts-1-hd",
            voice=voice,
            input=chunk,
            response_format="mp3",
        )
        parts.append(response.content)

    mp3_bytes = b"".join(parts)

    # 计算时长
    audio = MP3(io.BytesIO(mp3_bytes))
    duration = int(audio.info.length)

    return mp3_bytes, duration
