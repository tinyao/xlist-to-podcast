import logging
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import init_db
from app.routers import podcasts, episodes
from app import scheduler

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)

app = FastAPI(title="XList to Podcast", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Railway 部署后替换为实际前端域名
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(podcasts.router)
app.include_router(episodes.router)


@app.on_event("startup")
async def startup():
    # 确保数据目录存在（本地开发用）
    os.makedirs("data", exist_ok=True)
    await init_db()
    scheduler.start()


@app.on_event("shutdown")
async def shutdown():
    scheduler.stop()


@app.get("/health")
async def health():
    return {"status": "ok"}
