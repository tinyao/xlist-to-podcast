import logging
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.routers import podcasts, episodes
from app import scheduler

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)

os.makedirs("data/static", exist_ok=True)

app = FastAPI(title="XList to Podcast", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="data/static"), name="static")

app.include_router(podcasts.router)
app.include_router(episodes.router)


@app.on_event("startup")
async def startup():
    scheduler.start()


@app.on_event("shutdown")
async def shutdown():
    scheduler.stop()


@app.get("/health")
async def health():
    return {"status": "ok"}
