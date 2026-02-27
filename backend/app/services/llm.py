import re
from datetime import date

from openai import OpenAI

from app.config import settings
from app.services.twitter import Tweet


_SYSTEM_ZH = """你是一位专业的播客主播和内容编辑。
你的任务是将 Twitter 推文列表整理成一期播客节目。
要求：
- 口语化、流畅，适合 TTS 朗读，避免表情符号和网络缩写
- 按话题归类，不逐条念推文原文，提炼关键洞察和观点
- 结构：开场白（问候 + 今日日期）→ 主体内容（3-5 个话题块）→ 结尾语
- 字数约 1500-4000 字"""

_SYSTEM_EN = """You are a professional podcast host and content editor.
Your task is to turn a list of tweets into a podcast episode.
Requirements:
- Conversational, fluent, optimized for TTS; no emojis or internet slang
- Group by topic, extract key insights rather than reading tweets verbatim
- Structure: intro (greeting + today's date) → body (3-5 topic sections) → outro
- Target length: 750-2000 words"""

_USER_TEMPLATE = """播客名称：{podcast_name}
今日日期：{date}

以下是今日 Twitter List 的推文（共 {count} 条）：

{tweets_text}

请生成：
1. 【播客朗读稿】（Script）用 <script>...</script> 包裹
2. 【节目说明】（Shownotes，Markdown 格式）用 <shownotes>...</shownotes> 包裹

Shownotes 格式：
## 今日摘要
（3-5 句话概括本期内容）

## 关键话题
- #话题标签

## 推文来源
- @用户名：推文摘要（一句话）
"""

_USER_TEMPLATE_EN = """Podcast name: {podcast_name}
Today's date: {date}

Here are today's tweets from the Twitter List ({count} tweets):

{tweets_text}

Please generate:
1. **Podcast Script** wrapped in <script>...</script>
2. **Show Notes** (Markdown) wrapped in <shownotes>...</shownotes>

Show Notes format:
## Summary
(3-5 sentences)

## Key Topics
- #TopicTag

## Tweet Sources
- @username: one-sentence summary
"""


def _format_tweets(tweets: list[Tweet], language: str) -> str:
    lines = []
    for i, t in enumerate(tweets, 1):
        if language == "zh":
            lines.append(f"{i}. @{t.author_username}（{t.author_name}）：{t.text}")
        else:
            lines.append(f"{i}. @{t.author_username} ({t.author_name}): {t.text}")
    return "\n\n".join(lines)


def _extract_tag(text: str, tag: str) -> str:
    pattern = rf"<{tag}>(.*?)</{tag}>"
    match = re.search(pattern, text, re.DOTALL)
    return match.group(1).strip() if match else ""


def generate_content(
    tweets: list[Tweet],
    podcast_name: str,
    language: str,
    today: date,
) -> tuple[str, str]:
    """
    调用 GPT-4o 生成 (script, shownotes)。
    返回 (朗读稿, shownotes_markdown)。
    """
    client = OpenAI(api_key=settings.openai_api_key)

    system = _SYSTEM_ZH if language == "zh" else _SYSTEM_EN
    template = _USER_TEMPLATE if language == "zh" else _USER_TEMPLATE_EN

    user_msg = template.format(
        podcast_name=podcast_name,
        date=today.strftime("%Y年%m月%d日") if language == "zh" else today.strftime("%B %d, %Y"),
        count=len(tweets),
        tweets_text=_format_tweets(tweets, language),
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user_msg},
        ],
        temperature=0.7,
    )

    raw = response.choices[0].message.content or ""
    script = _extract_tag(raw, "script")
    shownotes = _extract_tag(raw, "shownotes")

    if not script:
        raise ValueError("LLM 未返回有效的 <script> 内容")

    return script, shownotes
