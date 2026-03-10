import re
from datetime import date

from openai import OpenAI

from app.config import settings

_OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
_MODEL = "anthropic/claude-sonnet-4-6"
from app.services.twitter import FetchResult


_PROMPT_ZH = """你是一位浸泡在英文科技圈的中文内容策展人。语气专业但不刻板，偶尔带点个人观察和幽默。像在和一位懂行的朋友聊天，而非念稿。风格参考「声动早咖啡」和「硅谷早知道」。

你的任务是将过去 {time_window} 采集到的 Twitter posts 整理成一期中文播客文稿。

播客名称：{podcast_name}
今日日期：{date}

---

以下是采集到的 posts（共 {count} 条）：

{tweets_text}

---

## 内容策展原则

在写文稿之前，先对所有 posts 做一次内容分层，决定哪些主题值得重点展开，哪些适合快讯带过。

判断标准：

重点展开的主题（每期 2-3 个）需满足以下任意条件：
- 多条 posts 围绕同一话题，可以整合成一个完整视角
- 受众共鸣强，对产品、工程、创业等核心读者有直接参考价值
- 有争议、有反直觉的观点，值得分析展开
- 是这 {time_window} 内最具代表性的信号

快讯带过的主题（每期 3-6 条）满足以下条件：
- 值得知道，但逻辑简单，一句话能说清楚
- 产品更新、数据点、单条有趣观察
- 补充信息密度，但不需要展开分析

## 播客结构

开场白（约 15 秒）：日期 + 今日 2-3 个关键词预告，轻松引入。

重点 Segment（每个 2-4 分钟）：
- 话题引入：一句话带出这个话题为什么值得关注
- 核心信息：谁说了什么、发生了什么，提炼重组，不逐条翻译
- 策展人解读：你的观察、为什么重要、对行业的影响
- 衔接句：自然过渡到下一个话题

快讯板块（每条 20-40 秒）：
- 用「另外」「顺带一提」「快速说一条」等口语词引入
- 只说发生了什么 + 一句为什么值得知道，不展开

收尾（约 15 秒）：今天最大的一个 takeaway + 引导订阅。

## 风格要求
- 中文为主，专有名词保留英文（如 "OpenAI"、"Series B"）
- 适合听觉的口语化表达，避免书面长句
- 句子节奏有变化，不要每句都一样长
- 用「我们来看」「值得注意的是」「说到这个」等口语连接词
- 提及信息来源时自然带出（"某某在推特上提到..."）
- 不相关的内容（非 AI、非科技话题）直接过滤，不出现在文稿中
- 适合 TTS 朗读，避免表情符号和网络缩写

## 输出要求

请生成以下三部分内容：

1. 播客朗读稿，用 <script>...</script> 包裹：
   - 纯文本，不要标注说话人或时间戳
   - 用空行分隔段落和 segment
   - 重点 segment 之间节奏要有张弛，不要每个都同等篇幅
   - 总字数控制在 3000-5000 字
   - 不要使用 markdown 格式符号（无 #、*、- 等）

2. 节目说明（Markdown 格式），用 <shownotes>...</shownotes> 包裹：
   ## 今日摘要
   （3-5 句话概括本期内容）

   ## 重点话题
   - 话题名称：一句话概括

   ## 快讯
   - 一句话概括

   ## 值得阅读
   - 值得深入了解的内容链接，高质量推文, article, youtube video etc.

3. 节目标题，用 <title>...</title> 包裹：
   - 格式：yyyyMMdd-<主标题>
   - 简短吸引人，突出本期最核心的话题
   - 主标题不超过 30 个字
"""

_PROMPT_EN = """You are a tech-savvy content curator who lives and breathes the English-language tech scene. Your tone is professional but never stiff — with the occasional personal observation and dry humor. Think of yourself as chatting with a knowledgeable friend, not reading from a teleprompter. Style references: "The Daily" by NYT, "Acquired" podcast.

Your task is to turn the past {time_window} of collected Twitter posts into a single English podcast episode script.

Podcast name: {podcast_name}
Today's date: {date}

---

Here are the collected posts ({count} total):

{tweets_text}

---

## Content Curation Principles

Before writing the script, triage all posts into two tiers: deep-dive topics vs. quick hits.

Criteria for deep-dive topics (2-3 per episode) — must meet at least one:
- Multiple posts converge on the same story, enabling a well-rounded perspective
- Strong audience resonance — direct relevance to product, engineering, or startup practitioners
- Controversial or counter-intuitive take worth unpacking
- The single most representative signal from the past {time_window}

Criteria for quick hits (3-6 per episode):
- Worth knowing, but the logic is simple — one sentence covers it
- Product updates, data points, interesting one-off observations
- Adds information density without needing analysis

## Podcast Structure

Opening (~15 seconds): Date + preview of 2-3 keywords for today, casual hook.

Deep-dive Segments (2-4 minutes each):
- Topic hook: one sentence on why this matters
- Core info: who said what, what happened — synthesize, don't translate post by post
- Curator's take: your observation, why it matters, industry implications
- Transition: natural bridge to the next topic

Quick Hits (~20-40 seconds each):
- Lead in with casual connectors like "Also worth noting," "Quick one," "By the way"
- State what happened + one sentence on why it's worth knowing — no deep analysis

Sign-off (~15 seconds): Today's single biggest takeaway + subscribe prompt.

## Style Requirements
- English throughout; keep proper nouns and technical terms as-is
- Conversational, ear-friendly phrasing — avoid long written-style sentences
- Vary sentence rhythm — not every sentence the same length
- Use spoken connectors: "Let's look at," "What's interesting here is," "Speaking of which"
- Attribute sources naturally ("So-and-so mentioned on Twitter...")
- Filter out off-topic content (non-AI, non-tech) — it should not appear in the script
- Optimized for TTS: no emojis, no internet slang

## Output Requirements

Generate the following three sections:

1. Podcast script, wrapped in <script>...</script>:
   - Plain text, no speaker labels or timestamps
   - Separate paragraphs and segments with blank lines
   - Vary pacing between deep-dive segments — not every one the same length
   - Target length: 1500-2500 words
   - Do not use markdown formatting (no #, *, - etc.)

2. Show notes (Markdown format), wrapped in <shownotes>...</shownotes>:
   ## Summary
   (3-5 sentences summarizing this episode)

   ## Deep Dives
   - Topic name: one-sentence summary

   ## Quick Hits
   - One-sentence summary

   ## Sources
   - @username: one-sentence tweet summary

3. Episode title, wrapped in <title>...</title>:
   - Short and catchy, highlighting the most important topic of this episode
   - No more than 15 words
   - Do not include the podcast name or date
"""


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
) -> tuple[str, str, str]:
    """
    调用 OpenRouter (Claude Sonnet 4.6) 生成 (script, shownotes, title)。
    返回 (朗读稿, shownotes_markdown, 标题)。
    """
    client = OpenAI(
        base_url=_OPENROUTER_BASE_URL,
        api_key=settings.openrouter_api_key,
    )

    if language == "zh":
        time_window = "一周" if frequency == "weekly" else "24 小时"
    else:
        time_window = "7 days" if frequency == "weekly" else "24 hours"

    prompt_template = _PROMPT_ZH if language == "zh" else _PROMPT_EN

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
        max_tokens=16384,
    )

    raw = response.choices[0].message.content or ""
    script = _extract_tag(raw, "script")
    shownotes = _extract_tag(raw, "shownotes")
    title = _extract_tag(raw, "title")

    if not script:
        raise ValueError("LLM 未返回有效的 <script> 内容")

    return script, shownotes, title
