import logging
import re
from datetime import date
from pathlib import Path
from typing import Optional

from openai import OpenAI

from app.config import settings

_OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
_MODEL = "anthropic/claude-sonnet-4-6"
from app.services.twitter import FetchResult

logger = logging.getLogger(__name__)

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def _load_prompt_template(language: str, prompt_file: Optional[str] = None) -> str:
    """
    加载 prompt 模板。优先级：
    1. prompt_file 参数指定的文件
    2. prompts/script_{language}.md
    3. 内置 fallback（抛错，因为文件应该总是存在）
    """
    if prompt_file:
        p = Path(prompt_file)
        if not p.is_absolute():
            p = _REPO_ROOT / p
        if p.exists():
            logger.info(f"使用自定义 prompt 文件: {p}")
            return p.read_text(encoding="utf-8")
        raise FileNotFoundError(f"指定的 prompt 文件不存在: {p}")

    default_path = _REPO_ROOT / "prompts" / f"script_{language}.md"
    if default_path.exists():
        return default_path.read_text(encoding="utf-8")

    raise FileNotFoundError(
        f"默认 prompt 文件不存在: {default_path}，"
        f"请确保 prompts/script_{language}.md 已创建"
    )


def _extract_tag(text: str, tag: str) -> str:
    pattern = rf"<{tag}>(.*?)</{tag}>"
    match = re.search(pattern, text, re.DOTALL)
    return match.group(1).strip() if match else ""


def generate_content(
    tweets: FetchResult,
    podcast_name: str,
    language: str,
    today: date,
    frequency: str = "daily",
    extra_prompt: str = "",
    prompt_file: Optional[str] = None,
) -> tuple[str, str, str]:
    """
    调用 OpenRouter (Claude Sonnet 4.6) 生成 (script, shownotes, title)。
    返回 (朗读稿, shownotes_markdown, 标题)。

    prompt_file: 可选，指定自定义 prompt 模板文件路径。
    """
    client = OpenAI(
        base_url=_OPENROUTER_BASE_URL,
        api_key=settings.openrouter_api_key,
    )

    if language == "zh":
        time_window = "一周" if frequency == "weekly" else "24 小时"
    else:
        time_window = "7 days" if frequency == "weekly" else "24 hours"

    prompt_template = _load_prompt_template(language, prompt_file)

    prompt = prompt_template.format(
        podcast_name=podcast_name,
        date=today.strftime("%Y年%m月%d日") if language == "zh" else today.strftime("%B %d, %Y"),
        count=tweets.count,
        tweets_text=tweets.text,
        time_window=time_window,
    )

    if extra_prompt:
        prompt += f"\n\n## 补充要求\n\n{extra_prompt}"

    response = client.chat.completions.create(
        model=_MODEL,
        messages=[
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
    )

    raw = response.choices[0].message.content or ""
    script = _extract_tag(raw, "script")
    shownotes = _extract_tag(raw, "shownotes")
    title = _extract_tag(raw, "title")

    if not script:
        raise ValueError("LLM 未返回有效的 <script> 内容")

    return script, shownotes, title
