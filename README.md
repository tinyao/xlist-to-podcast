# XList to Podcast

将 Twitter List 自动转为每日播客，支持所有主流播客客户端 RSS 订阅。

## 快速开始（本地开发）

### 1. 环境配置

```bash
cp .env.example .env
# 编辑 .env，填入 Twitter / OpenAI / OSS 密钥
```

### 2. 启动 Backend

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

mkdir -p data
uvicorn app.main:app --reload
# → http://localhost:8000
```

### 3. 启动 Frontend

```bash
cd frontend
npm install
cp .env.example .env.local
# 编辑 .env.local：NEXT_PUBLIC_API_URL=http://localhost:8000

npm run dev
# → http://localhost:3000
```

## 部署到 Railway

1. 在 Railway 新建 Project，连接此 GitHub 仓库
2. 添加两个 Service：
   - `backend`：Root Directory 设为 `backend/`
   - `frontend`：Root Directory 设为 `frontend/`
3. 为 `backend` service 挂载 Volume（Mount Path: `/app/data`）
4. 在 `backend` service Variables 中添加所有 `.env.example` 中的变量
5. 在 `frontend` service Variables 中设置：
   ```
   NEXT_PUBLIC_API_URL=https://<backend-railway-domain>
   ```
6. 触发部署

## 项目结构

```
├── backend/          # Python FastAPI
│   └── app/
│       ├── main.py           # 入口
│       ├── models.py         # 数据库模型
│       ├── pipeline.py       # 生成主流程
│       ├── scheduler.py      # 定时任务
│       ├── routers/          # API 路由
│       └── services/         # 各服务封装
│           ├── twitter.py    # 推文抓取
│           ├── llm.py        # 内容生成
│           ├── tts.py        # 语音合成
│           ├── oss.py        # OSS 操作
│           └── feed.py       # RSS 生成
└── frontend/         # Next.js 14
    └── src/app/
        ├── page.tsx                    # 创建播客
        ├── podcasts/page.tsx           # 播客列表
        └── podcasts/[id]/page.tsx      # 播客详情
```
