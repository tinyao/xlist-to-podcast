# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

### Backend (from `backend/`)
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### Frontend (from `frontend/`)
```bash
npm install
npm run dev        # http://localhost:3000
npm run build
npm run lint
```

### Makefile shortcuts (from repo root)
```bash
make setup          # install both backend and frontend deps
make dev-backend    # uvicorn on :8000
make dev-frontend   # next dev on :3000
```

### Manual episode trigger (for testing without the UI)
```
POST http://localhost:8000/api/podcasts/{id}/episodes/trigger
```

## Architecture

### Overview
Full-stack app that turns an X (Twitter) List into a daily podcast. Backend is FastAPI + APScheduler; frontend is Next.js 14 App Router.

```
X List → tweets → LLM (GPT-4o) → TTS (OpenAI) → MP3 + RSS feed
```

### Backend (`backend/app/`)

**Entry point**: `main.py` — mounts `data/static/` as StaticFiles at `/static`, starts the scheduler on startup, no DB migrations (uses SQLAlchemy `create_all`).

**Pipeline** (`pipeline.py`): The core logic. All sync IO (Twitter fetch, LLM, TTS) is wrapped in `asyncio.to_thread()` to avoid blocking the FastAPI event loop. Per-episode output written to:
```
data/static/{podcast_id}/episodes/{YYYY-MM-DD}/
    posts.md       # raw tweets (xtest.py agent-readable format)
    script.md      # podcast script
    audio.mp3      # TTS audio
    shownotes.md   # show notes
data/static/{podcast_id}/feed.xml   # overwritten after each episode
```

**Scheduler** (`scheduler.py`): APScheduler runs `_dispatch_hourly()` at every `:00`. It queries all active podcasts whose `publish_hour` matches the current hour in `Asia/Shanghai`, then fires `generate_episode()` as an async task for each.

**Services**:
- `twitter.py` — Raw `requests` against X API v2. Returns `FetchResult(count: int, text: str)`. The `text` field is agent-readable structured plaintext (xtest.py format: `[tweet N]`, `author:`, `text:`, `media:`, `link:`, `metrics:`). Fetches up to 300 tweets with pagination, `wait_on_rate_limit=True`.
- `llm.py` — Calls GPT-4o with the full `FetchResult.text` directly (no re-formatting). Parses `<script>` and `<shownotes>` XML tags from the response.
- `tts.py` — Calls OpenAI `tts-1-hd`. Splits long scripts at sentence boundaries (4000 char chunks), concatenates MP3 bytes, uses `mutagen` to compute duration.
- `feed.py` — `build_feed(podcast, episodes) -> bytes`. Pure function, no file I/O. Caller writes the bytes.

**Data model** (`models.py`):
- `Podcast`: stores `cover_path` (relative to `data/static/`). `feed_url` and `cover_url` are computed `@property` fields pointing to `/static/...`.
- `Episode`: stores `audio_path` (relative to `data/static/`). Status values: `pending / processing / done / failed`. Script and shownotes are also stored in DB columns (in addition to files).
- DB uses SQLite + aiosqlite. No migration tool — schema is recreated via `create_all` on startup (destructive if schema changes).

**Config** (`config.py`): Pydantic `BaseSettings`, reads from `backend/.env`. Required: `TWITTER_BEARER_TOKEN`, `OPENAI_API_KEY`. Optional: `DATABASE_URL` (default: `sqlite+aiosqlite:///./data/app.db`), `SERVER_BASE_URL` (default: `http://localhost:8000`).

### Frontend (`frontend/src/`)

Next.js 14 App Router, Tailwind CSS, no state management library.

- `lib/api.ts` — All API calls. `BASE_URL` from `NEXT_PUBLIC_API_URL` env var (set in `frontend/.env.local`).
- `app/page.tsx` — Redirect or landing.
- `app/podcasts/page.tsx` — List podcasts, create new (multipart form with cover image upload).
- `app/podcasts/[id]/page.tsx` — Podcast detail: episode list, manual trigger button, RSS feed URL copy.

### Key design decisions
- **No oss abstraction**: Files are written directly with `pathlib.Path`. `data/static/` is served by FastAPI StaticFiles.
- **Feed is a static file** at `data/static/{podcast_id}/feed.xml`, overwritten after each episode. URL: `{SERVER_BASE_URL}/static/{podcast_id}/feed.xml`.
- **Blocking calls** in the pipeline use `asyncio.to_thread()` — never call sync services directly from async context.
- **Twitter fetch** returns preprocessed text (`FetchResult.text`), not raw tweet objects. LLM receives this text directly.
