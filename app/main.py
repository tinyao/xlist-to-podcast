"""
本地开发用的最小 FastAPI 服务，仅提供 static 文件服务。
生产环境使用 generate.py + OSS，不需要这个服务。
"""
import logging
import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)

os.makedirs("data/static", exist_ok=True)

app = FastAPI(title="XList to Podcast", version="1.0.0")

app.mount("/static", StaticFiles(directory="data/static"), name="static")


@app.get("/health")
async def health():
    return {"status": "ok"}
