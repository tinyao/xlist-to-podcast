# XList to Podcast — 技术方案

**版本**: v1.0
**日期**: 2026-02-27

---

## 1. 整体架构

```
┌─────────────────────────────────────────────────────┐
│                    用户浏览器                        │
│           Next.js Frontend (Static Export)          │
└──────────────────────┬──────────────────────────────┘
                       │ HTTP / REST
┌──────────────────────▼──────────────────────────────┐
│                 Python FastAPI                       │
│  ┌────────────┐  ┌──────────────┐  ┌─────────────┐ │
│  │ Podcast    │  │  Episode     │  │  Admin      │ │
│  │ CRUD API   │  │  Generate API│  │  API        │ │
│  └─────┬──────┘  └──────┬───────┘  └──────┬──────┘ │
└────────┼────────────────┼─────────────────┼─────────┘
         │                │                 │
┌────────▼────────┐  ┌────▼──────────────────▼───────┐
│   SQLite / DB   │  │        Task Queue (APScheduler │
│  (Podcast 配置) │  │        + Celery 可选)           │
└─────────────────┘  └────────────┬──────────────────┘
                                   │
              ┌────────────────────┼──────────────────┐
              │                    │                  │
    ┌─────────▼──────┐  ┌─────────▼──────┐  ┌───────▼───────┐
    │  Twitter API v2 │  │  OpenAI API    │  │ 阿里云 OSS    │
    │  (List Timeline)│  │  GPT-4o + TTS  │  │ (MP3 + XML)   │
    └─────────────────┘  └────────────────┘  └───────────────┘
```

### 架构决策

| 决策 | 选择 | 理由 |
|------|------|------|
| 后端框架 | **Python FastAPI** | 异步支持好，与 OpenAI/OSS SDK 生态契合 |
| 前端 | **Next.js (App Router)** | 快速开发，静态导出可直接放 OSS |
| 数据库 | **SQLite + SQLAlchemy** | 单机部署简单，数据量小 |
| 任务调度 | **APScheduler** | 轻量，内嵌 FastAPI 进程，无需额外服务 |
| 部署 | **单台 VPS / Docker** | 成本低，流量小 |

---

## 2. 技术栈

### 后端

```
Python 3.11+
FastAPI 0.110+
SQLAlchemy 2.0 (async)
APScheduler 3.x
tweepy 4.x          # Twitter API v2 客户端
openai 1.x          # GPT-4o + TTS
oss2                # 阿里云 OSS Python SDK
Pydantic v2
python-multipart    # 文件上传
lxml / feedgen      # RSS XML 生成
```

### 前端

```
Next.js 14 (App Router)
TypeScript
Tailwind CSS
shadcn/ui
React Hook Form + Zod  # 表单验证
```

### 基础设施

```
Docker + Docker Compose
Nginx (反向代理)
阿里云 OSS (音频 + RSS + 封面存储)
```

---

## 3. 数据模型

### 3.1 Podcast（播客配置）

```python
class Podcast(Base):
    __tablename__ = "podcasts"

    id: str             # UUID，也是 OSS 路径前缀
    name: str           # 播客名称
    description: str    # 播客描述
    twitter_list_id: str  # Twitter List ID（从 URL 解析）
    twitter_list_url: str # 原始 URL
    voice: str          # OpenAI TTS 音色
    language: str       # zh / en
    cover_oss_key: str  # OSS 封面路径
    feed_oss_key: str   # OSS feed.xml 路径
    publish_hour: int   # 每日发布小时（Asia/Shanghai）
    is_active: bool
    created_at: datetime
    updated_at: datetime
```

### 3.2 Episode（每期节目）

```python
class Episode(Base):
    __tablename__ = "episodes"

    id: str             # UUID
    podcast_id: str     # FK -> Podcast
    date: date          # 节目日期 YYYY-MM-DD
    title: str          # 节目标题
    script: str         # 完整朗读稿
    shownotes: str      # Markdown shownotes
    audio_oss_key: str  # OSS MP3 路径
    audio_duration: int # 秒
    audio_size: int     # bytes
    tweet_count: int    # 本期处理的推文数
    status: str         # pending / processing / done / failed
    error_msg: str      # 失败原因
    created_at: datetime
```

---

## 4. API 设计

### 4.1 Podcast CRUD

```
POST   /api/podcasts              # 创建播客
GET    /api/podcasts              # 列表
GET    /api/podcasts/{id}         # 详情（含 Feed URL）
DELETE /api/podcasts/{id}         # 删除
```

**POST /api/podcasts 请求体** (multipart/form-data)：
```
name:             string
description:      string (optional)
twitter_list_url: string
voice:            enum[alloy,echo,fable,onyx,nova,shimmer]
language:         enum[zh,en]
publish_hour:     integer 0-23 (optional, default: 8)
cover:            file
```

**响应**：
```json
{
  "id": "abc123",
  "name": "AI 日报",
  "feed_url": "https://{bucket}.oss-cn-hangzhou.aliyuncs.com/abc123/feed.xml",
  "cover_url": "https://{bucket}.oss-cn-hangzhou.aliyuncs.com/abc123/cover.jpg"
}
```

### 4.2 Episode 管理

```
GET    /api/podcasts/{id}/episodes          # 节目列表
GET    /api/podcasts/{id}/episodes/{date}   # 节目详情（含 shownotes）
POST   /api/podcasts/{id}/episodes/trigger  # 手动触发生成（测试用）
```

---

## 5. 核心工作流详解

### 5.1 每日生成任务流程

```python
async def generate_episode(podcast_id: str):
    # 1. 加载播客配置
    podcast = await db.get_podcast(podcast_id)
    today = date.today()

    # 2. 抓取推文
    tweets = await fetch_list_tweets(
        list_id=podcast.twitter_list_id,
        since=datetime.now() - timedelta(hours=24)
    )
    if len(tweets) < 3:
        # 内容太少，跳过本日
        return

    # 3. LLM 生成 Script + Shownotes
    script, shownotes = await generate_content(
        tweets=tweets,
        podcast_name=podcast.name,
        language=podcast.language,
        date=today
    )

    # 4. TTS 生成音频
    mp3_bytes = await text_to_speech(
        text=script,
        voice=podcast.voice
    )

    # 5. 上传到 OSS
    audio_key = f"{podcast.id}/episodes/{today}.mp3"
    await oss_upload(audio_key, mp3_bytes, content_type="audio/mpeg")

    # 6. 存储 shownotes
    notes_key = f"{podcast.id}/episodes/{today}.md"
    await oss_upload(notes_key, shownotes.encode(), content_type="text/markdown")

    # 7. 更新 feed.xml
    await update_feed(podcast, episode)

    # 8. 写入数据库
    await db.save_episode(episode)
```

### 5.2 推文抓取（Tweepy v2）

```python
async def fetch_list_tweets(list_id: str, since: datetime) -> list[Tweet]:
    client = tweepy.AsyncClient(bearer_token=TWITTER_BEARER_TOKEN)

    tweets = []
    async for response in tweepy.AsyncPaginator(
        client.get_list_tweets,
        id=list_id,
        tweet_fields=["created_at", "author_id", "text", "public_metrics"],
        expansions=["author_id"],
        user_fields=["username", "name"],
        start_time=since,
        max_results=100,
        limit=1  # 只取第一页，避免超额
    ):
        for tweet in (response.data or []):
            # 过滤规则
            if tweet.text.startswith("RT @"):  continue  # 纯转推
            if tweet.text.startswith("@"):     continue  # 回复
            if len(tweet.text) < 20:           continue  # 太短
            tweets.append(tweet)

    return tweets
```

### 5.3 LLM 内容生成

**Prompt 设计（中文）**：

```python
SYSTEM_PROMPT = """你是一位专业的播客主播和内容编辑。
你的任务是将 Twitter 推文列表整理成一期播客节目。
要求：
- 口语化、流畅，适合 TTS 朗读
- 按话题归类，不逐条念推文原文
- 提炼关键洞察和观点，去除网络用语和表情符号
- 中文播客：约 1500-4000 字；英文播客：约 750-2000 词
- 结构：开场白 → 主体内容（3-5个话题块）→ 结尾"""

USER_PROMPT = """
播客名称：{podcast_name}
今日日期：{date}
以下是今日 Twitter List 的推文：

{tweets_text}

请生成：
1. 【播客朗读稿】（Script）用 <script>...</script> 包裹
2. 【节目说明】（Shownotes，Markdown格式）用 <shownotes>...</shownotes> 包裹

Shownotes 包含：今日摘要（3-5句话）、关键话题标签、推文来源列表（@用户名: 推文摘要）
"""
```

### 5.4 TTS 分段处理

OpenAI TTS 单次请求限制 4096 字符，长文本需分段：

```python
async def text_to_speech(text: str, voice: str) -> bytes:
    client = AsyncOpenAI(api_key=OPENAI_API_KEY)
    chunks = split_text(text, max_chars=4000)  # 按句子边界切割
    audio_parts = []

    for chunk in chunks:
        response = await client.audio.speech.create(
            model="tts-1-hd",
            voice=voice,
            input=chunk,
            response_format="mp3"
        )
        audio_parts.append(response.content)

    # 拼接 MP3（简单二进制拼接对 MP3 有效）
    return b"".join(audio_parts)


def split_text(text: str, max_chars: int) -> list[str]:
    """按句子边界切割，避免断句"""
    sentences = re.split(r'(?<=[。！？.!?])\s*', text)
    chunks, current = [], ""
    for s in sentences:
        if len(current) + len(s) > max_chars:
            if current:
                chunks.append(current.strip())
            current = s
        else:
            current += s
    if current:
        chunks.append(current.strip())
    return chunks
```

### 5.5 RSS Feed 生成

```python
def build_feed_xml(podcast: Podcast, episodes: list[Episode]) -> str:
    """生成符合 Apple Podcasts 规范的 RSS 2.0"""
    # 使用 feedgen 库
    fg = FeedGenerator()
    fg.load_extension('podcast')

    fg.id(podcast.feed_url)
    fg.title(podcast.name)
    fg.description(podcast.description)
    fg.language(podcast.language)
    fg.link(href=podcast.feed_url, rel='self')
    fg.podcast.itunes_image(podcast.cover_url)
    fg.podcast.itunes_explicit('no')
    fg.podcast.itunes_category('Technology')  # 可配置

    for ep in episodes[-30:]:  # 最近 30 期
        fe = fg.add_entry()
        fe.id(ep.audio_url)
        fe.title(ep.title)
        fe.description(ep.shownotes)  # HTML or Markdown
        fe.enclosure(ep.audio_url, str(ep.audio_size), 'audio/mpeg')
        fe.published(ep.created_at)
        fe.podcast.itunes_duration(str(ep.audio_duration))
        fe.podcast.itunes_summary(ep.shownotes[:500])

    return fg.rss_str(pretty=True).decode()
```

---

## 6. 任务调度

使用 **APScheduler** 内嵌于 FastAPI 进程：

```python
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

scheduler = AsyncIOScheduler(timezone="Asia/Shanghai")

@app.on_event("startup")
async def start_scheduler():
    # 每小时整点检查：是否有播客需要在此小时生成
    scheduler.add_job(
        dispatch_hourly_jobs,
        CronTrigger(minute=0),  # 每小时 :00 执行
        id="hourly_dispatch"
    )
    scheduler.start()

async def dispatch_hourly_jobs():
    current_hour = datetime.now(ZoneInfo("Asia/Shanghai")).hour
    podcasts = await db.get_podcasts_by_hour(current_hour)
    for podcast in podcasts:
        asyncio.create_task(generate_episode_safe(podcast.id))
```

---

## 7. OSS 文件访问策略

| 文件类型 | OSS ACL | 原因 |
|----------|---------|------|
| `cover.jpg` | 公共读 | 播客客户端需要直接访问 |
| `feed.xml` | 公共读 | RSS 订阅需要 |
| `episodes/*.mp3` | 公共读 | 播客客户端流媒体播放 |
| `episodes/*.md` | 私有 | 仅后端读取 |

> 注意：OSS bucket 不设置为全部公开，通过对象级 ACL 控制各文件权限。

---

## 8. 目录结构

```
xlist-to-podcast/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI 入口
│   │   ├── models.py            # SQLAlchemy 模型
│   │   ├── schemas.py           # Pydantic 模型
│   │   ├── database.py          # DB 连接
│   │   ├── scheduler.py         # APScheduler 配置
│   │   ├── routers/
│   │   │   ├── podcasts.py      # 播客 CRUD
│   │   │   └── episodes.py      # 节目管理
│   │   └── services/
│   │       ├── twitter.py       # 推文抓取
│   │       ├── llm.py           # LLM 内容生成
│   │       ├── tts.py           # 语音合成
│   │       ├── oss.py           # OSS 上下传
│   │       └── feed.py          # RSS 生成
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── app/
│   │   ├── page.tsx             # 创建播客表单
│   │   └── podcasts/
│   │       └── [id]/page.tsx    # 播客详情
│   ├── components/
│   └── package.json
├── docs/
│   ├── PRD.md
│   └── TECH_SPEC.md
├── docker-compose.yml
└── .env.example
```

---

## 9. 环境变量

```bash
# Twitter
TWITTER_BEARER_TOKEN=

# OpenAI
OPENAI_API_KEY=

# 阿里云 OSS
OSS_ACCESS_KEY_ID=
OSS_ACCESS_KEY_SECRET=
OSS_BUCKET_NAME=
OSS_ENDPOINT=oss-cn-hangzhou.aliyuncs.com
OSS_BASE_URL=https://{bucket}.oss-cn-hangzhou.aliyuncs.com

# 应用
DATABASE_URL=sqlite+aiosqlite:///./data/app.db
SECRET_KEY=
```

---

## 10. 部署方案（Railway）

### 架构

Railway 上部署两个独立 Service，共用一套环境变量：

```
Railway Project: xlist-to-podcast
├── Service: backend   (Python FastAPI, Nixpacks 自动检测)
│   └── Volume: /app/data  (SQLite 持久化)
└── Service: frontend  (Next.js, Nixpacks 自动检测)
```

### Monorepo 配置

根目录 `railway.toml`（Railway 用于识别多服务）不需要额外配置，Railway 通过各自目录下的文件自动识别：
- `backend/` → 检测到 `requirements.txt`，使用 Python Nixpack
- `frontend/` → 检测到 `package.json`，使用 Node Nixpack

### backend 配置

```toml
# backend/railway.toml
[build]
builder = "nixpacks"

[deploy]
startCommand = "uvicorn app.main:app --host 0.0.0.0 --port $PORT"
healthcheckPath = "/health"
restartPolicyType = "on-failure"
restartPolicyMaxRetries = 3
```

```
# backend/Procfile（备用）
web: uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

### frontend 配置

```toml
# frontend/railway.toml
[build]
builder = "nixpacks"

[deploy]
startCommand = "node .next/standalone/server.js"
```

Next.js 需开启 standalone 模式：
```js
// frontend/next.config.ts
const nextConfig = {
  output: 'standalone',
}
```

### 持久化 Volume

在 Railway Dashboard 为 backend service 挂载 Volume：
- Mount Path: `/app/data`
- 用于存放 `app.db`（SQLite 文件）

### 环境变量

在 Railway Dashboard → Variables 中配置（backend service）：

```bash
TWITTER_BEARER_TOKEN=
OPENAI_API_KEY=
OSS_ACCESS_KEY_ID=
OSS_ACCESS_KEY_SECRET=
OSS_BUCKET_NAME=
OSS_ENDPOINT=oss-cn-hangzhou.aliyuncs.com
OSS_BASE_URL=https://{bucket}.oss-cn-hangzhou.aliyuncs.com
DATABASE_URL=sqlite+aiosqlite:////app/data/app.db
```

frontend service 需要：
```bash
NEXT_PUBLIC_API_URL=${{backend.RAILWAY_PUBLIC_DOMAIN}}
```

### 部署流程

```bash
# 1. 安装 Railway CLI
npm install -g @railway/cli

# 2. 登录并关联项目
railway login
railway link

# 3. 推送部署（Railway 监听 GitHub 仓库自动部署）
git push origin main
```

---

## 11. 关键风险与应对

| 风险 | 概率 | 应对 |
|------|------|------|
| Twitter API 限流 | 中 | 每个 List 每天仅请求一次；记录 rate limit header 自适应 |
| OpenAI TTS 超时 | 低 | 分段请求 + 超时重试（max 3次） |
| 推文量太少（< 3条） | 中 | 跳过当日生成，记录日志，不报错 |
| OSS 上传失败 | 低 | 重试 3 次，失败后保留本地文件备用 |
| LLM 生成内容质量差 | 中 | Prompt 迭代优化；支持手动触发重新生成 |

---

## 12. 后续迭代方向（超出 v1.0）

- 支持多用户（Auth 系统）
- 支持 RSS Webhooks（新 episode 通知）
- 支持自定义 Prompt 模板
- 支持从 Twitter 用户主页聚合（非 List）
- 播客 Web 播放器页面
- 成本统计面板（Token 用量 / TTS 字符数）
