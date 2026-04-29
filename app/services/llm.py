import logging
import re
import shutil
import subprocess
from datetime import date
from pathlib import Path
from typing import TYPE_CHECKING, List, Optional

from openai import OpenAI

from app.config import settings
from app.services.twitter import FetchResult

if TYPE_CHECKING:
    from app.storage import Episode

logger = logging.getLogger(__name__)

_OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
_OPENROUTER_MODEL = "anthropic/claude-sonnet-4-6"

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def _load_prompt_template(prompt_file: str, language: str) -> str:
    """Load prompt template from file. Falls back to built-in default if not specified."""
    if prompt_file:
        path = _REPO_ROOT / prompt_file
        if path.exists():
            return path.read_text(encoding="utf-8")
        raise FileNotFoundError(f"Prompt file not found: {path}")

    # Fallback: use built-in default
    path = _REPO_ROOT / "prompts/tech-daily.md"
    if path.exists():
        return path.read_text(encoding="utf-8")
    raise FileNotFoundError(
        f"No prompt_file configured and default prompt not found: {path}"
    )


def _build_recent_context(recent_episodes: list["Episode"]) -> str:
    """Build recent episodes context string for prompt injection."""
    if not recent_episodes:
        return ""

    sections = []
    for ep in recent_episodes:
        content = ep.script or ep.shownotes
        if not content:
            continue
        title_part = ep.title or str(ep.date)
        label = "往期文稿" if ep.script else "往期摘要"
        sections.append(f"【{ep.date}】{title_part}\n<{label}>\n{content}\n</{label}>")

    if not sections:
        return ""

    return (
        "\n---\n\n"
        "## 近期节目回顾\n\n"
        "以下是最近几期节目的完整文稿。你必须仔细对照这些文稿，判断今日 posts 中哪些信息已经讲过、哪些是真正的新进展。\n\n"
        + "\n\n".join(sections)
    )


def _extract_tag(text: str, tag: str) -> str:
    pattern = rf"<{tag}>(.*?)</{tag}>"
    match = re.search(pattern, text, re.DOTALL)
    return match.group(1).strip() if match else ""


def _build_prompt(
    tweets: FetchResult,
    podcast_name: str,
    language: str,
    today: date,
    frequency: str,
    extra_prompt: str,
    prompt_file: str,
    recent_episodes: Optional[List["Episode"]],
) -> str:
    """Assemble the full prompt from template, tweets, recent context, and extra instructions."""
    if language == "zh":
        time_window = "一周" if frequency == "weekly" else "24 小时"
    else:
        time_window = "7 days" if frequency == "weekly" else "24 hours"

    prompt_template = _load_prompt_template(prompt_file, language)
    recent_context = _build_recent_context(recent_episodes or [])

    format_kwargs = dict(
        podcast_name=podcast_name,
        date=today.strftime("%Y年%m月%d日") if language == "zh" else today.strftime("%B %d, %Y"),
        count=tweets.count,
        tweets_text=tweets.text,
        time_window=time_window,
    )

    # Only inject recent_context if the template has the placeholder
    if "{recent_context}" in prompt_template:
        format_kwargs["recent_context"] = recent_context

    prompt = prompt_template.format(**format_kwargs)

    # If template lacked {recent_context}, append it directly
    if "{recent_context}" not in prompt_template and recent_context:
        prompt += recent_context

    if extra_prompt:
        prompt += f"\n\n## 补充要求\n\n{extra_prompt}"

    return prompt


def _generate_via_claude_cli(prompt: str) -> str:
    """Call Claude CLI to generate content.

    Pipes prompt via stdin to avoid OS argument length limits
    with large prompts (100+ tweets + recent episode context).
    """
    claude_path = shutil.which("claude")
    if not claude_path:
        raise RuntimeError(
            "Claude CLI not found. Install with: npm install -g @anthropic-ai/claude-code"
        )

    logger.info("Using Claude CLI for content generation (%d chars prompt)", len(prompt))
    result = subprocess.run(
        [
            claude_path,
            "-p",
            "--model", "sonnet",
            "--max-turns", "1",
            "--output-format", "text",
            "--no-session-persistence",
        ],
        input=prompt,
        capture_output=True,
        text=True,
        timeout=1200,
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"Claude CLI failed (exit code {result.returncode}): {result.stderr}"
        )

    return result.stdout


def _generate_via_openrouter(prompt: str) -> str:
    """Call OpenRouter API to generate content."""
    logger.info("Using OpenRouter API for content generation")
    client = OpenAI(
        base_url=_OPENROUTER_BASE_URL,
        api_key=settings.openrouter_api_key,
    )

    response = client.chat.completions.create(
        model=_OPENROUTER_MODEL,
        messages=[
            {"role": "user", "content": prompt},
        ],
        max_tokens=16384,
        temperature=0.7,
    )

    return response.choices[0].message.content or ""


def generate_content(
    tweets: FetchResult,
    podcast_name: str,
    language: str,
    today: date,
    frequency: str = "daily",
    extra_prompt: str = "",
    prompt_file: str = "",
    recent_episodes: Optional[List] = None,
) -> tuple[str, str, str]:
    """
    生成 (script, shownotes, title)。
    支持 Claude CLI（默认）和 OpenRouter 两种后端，通过 LLM_BACKEND 环境变量切换。
    """
    prompt = _build_prompt(
        tweets, podcast_name, language, today, frequency,
        extra_prompt, prompt_file, recent_episodes,
    )

    if settings.llm_backend == "claude-cli":
        raw = _generate_via_claude_cli(prompt)
    else:
        raw = _generate_via_openrouter(prompt)

    script = _extract_tag(raw, "script")
    shownotes = _extract_tag(raw, "shownotes")
    title = _extract_tag(raw, "title")

    if not script:
        raise ValueError("LLM 未返回有效的 <script> 内容")

    return script, shownotes, title
