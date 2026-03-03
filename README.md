# XList to Podcast

将 X (Twitter) List 自动转为每日播客。GitHub Actions 定时运行，生成 RSS feed，支持所有主流播客客户端订阅。

## 工作原理

```
podcasts.yaml → GitHub Actions (hourly) → OSS (audio) + GitHub Pages (feed)
```

1. 从 X List 抓取过去 24 小时的推文
2. LLM 生成播客稿件 + shownotes
3. OpenAI TTS 转为音频，上传到 OSS
4. 生成 RSS feed，通过 GitHub Pages 提供订阅

## 快速开始

### 1. Fork 并配置

```bash
cp .env.example .env
# 填入 Twitter / OpenAI / OpenRouter / OSS 密钥
```

### 2. 定义播客

编辑 `podcasts.yaml`，添加你的播客配置：

```yaml
podcasts:
  - id: "my-podcast"
    name: "AI 日报"
    description: "每日 AI 科技动态"
    twitter_list_url: "https://x.com/i/lists/123456"
    twitter_list_id: "123456"
    voice: "nova"          # OpenAI TTS 音色
    language: "zh"          # zh / en
    publish_hour: 8         # 北京时间
    cover_file: "cover.jpg" # covers/ 目录下的封面图
```

### 3. 配置 GitHub

**Secrets**（Settings → Secrets and variables → Actions → Secrets）：

| Secret | 说明 |
|---|---|
| `TWITTER_BEARER_TOKEN` | X API v2 Bearer Token |
| `OPENAI_API_KEY` | OpenAI API Key (TTS) |
| `OPENROUTER_API_KEY` | OpenRouter API Key (LLM) |
| `OSS_ACCESS_KEY_ID` | 阿里云 OSS Access Key |
| `OSS_ACCESS_KEY_SECRET` | 阿里云 OSS Secret |
| `OSS_ENDPOINT` | OSS Endpoint |
| `OSS_BUCKET_NAME` | OSS Bucket 名称 |
| `OSS_CDN_URL` | OSS CDN 地址 |

**Variables**（Settings → Secrets and variables → Actions → Variables）：

| Variable | 说明 |
|---|---|
| `SITE_URL` | GitHub Pages 域名，如 `https://podcast.example.com` |

**Pages**（Settings → Pages）：
- Source: Deploy from a branch
- Branch: `main`, folder: `/docs`

### 4. 本地测试

```bash
pip install -r requirements.txt
python -m generate --force --podcast <ID>             # 生成一期
python -m generate --force --podcast <ID> --max-posts 5  # 限制推文数，省 token
```

### 5. 订阅

RSS 地址：`{SITE_URL}/{podcast_id}/feed.xml`

## 项目结构

```
├── generate.py              # CLI 入口
├── podcasts.yaml            # 播客配置
├── covers/                  # 封面图
├── docs/                    # GitHub Pages (feed.xml, episode data)
├── app/
│   ├── config.py            # 配置 (Pydantic BaseSettings)
│   ├── storage.py           # JSON 文件存储
│   ├── pipeline.py          # 核心流程: 抓取 → LLM → TTS → feed
│   └── services/
│       ├── twitter.py       # X API v2
│       ├── llm.py           # LLM 内容生成
│       ├── tts.py           # OpenAI TTS
│       ├── feed.py          # RSS feed 生成
│       └── oss.py           # 阿里云 OSS (音频+封面)
├── .github/workflows/
│   └── generate.yml         # 每小时 cron + 手动触发
└── .env.example
```

## 存储分布

- **OSS** — 音频 (`audio.mp3`) + 封面 (`cover.jpg`)
- **GitHub Pages (`docs/`)** — `feed.xml`、`episode.json`、`posts.md`、`script.md`、`shownotes.md`
