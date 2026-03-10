"""
GitHub Actions 入口：从 podcasts.yaml 加载配置，生成播客节目并上传到 OSS。

用法：
  python -m generate                    # 正常运行，按 publish_hour 过滤
  python -m generate --force            # 忽略小时检查，强制生成
  python -m generate --podcast ID       # 只处理指定播客
  python -m generate --force --podcast ID
  python -m generate --regenerate --podcast ID  # 跳过推文抓取，用已有 posts.md 重新生成
  python -m generate --test-feishu              # 用最新 episode 测试飞书通知
  python -m generate --test-feishu --podcast ID # 测试指定播客的飞书通知
"""
import argparse
import asyncio
import hashlib
import html
import json
import logging
import shutil
import sys
from datetime import datetime, timezone, timedelta, date
from pathlib import Path
from typing import Optional

import yaml

from app.storage import (
    Podcast, Episode, STATIC_DIR,
    _save_podcast_sync,
)
from app.services.oss import upload_file_sync, is_enabled as oss_enabled
from app.services.feishu import send_feishu_notification
from app.config import settings
from app.pipeline import generate_episode

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

REPO_ROOT = Path(__file__).resolve().parent
YAML_PATH = REPO_ROOT / "podcasts.yaml"

SHANGHAI_TZ = timezone(timedelta(hours=8))


# ── YAML → Podcast ──────────────────────────────────────────────────────────

def load_podcasts_from_yaml() -> list[Podcast]:
    """读取 podcasts.yaml，返回 Podcast 模型列表。"""
    data = yaml.safe_load(YAML_PATH.read_text(encoding="utf-8"))
    entries = data.get("podcasts") or []
    podcasts: list[Podcast] = []
    for entry in entries:
        podcasts.append(Podcast(
            id=entry["id"],
            name=entry["name"],
            description=entry.get("description", ""),
            twitter_list_url=entry["twitter_list_url"],
            twitter_list_id=entry["twitter_list_id"],
            voice=entry.get("voice", "nova"),
            language=entry.get("language", "zh"),
            publish_hour=entry.get("publish_hour", 8),
            frequency=entry.get("frequency", "daily"),
            publish_day=entry.get("publish_day", 0),
            extra_prompt=entry.get("extra_prompt", ""),
            cover_path=f"{entry['id']}/cover.jpg",
            owner_name=entry.get("owner_name", ""),
            owner_email=entry.get("owner_email", ""),
            category=entry.get("category", "Technology"),
            feishu_webhook=entry.get("feishu_webhook", ""),
            subscribe_url=entry.get("subscribe_url", ""),
            subscribe_links=entry.get("subscribe_links", {}),
            is_active=True,
        ))
    return podcasts


# ── Bootstrap ────────────────────────────────────────────────────────────────

def _episode_json_with_urls(episode: Episode) -> dict:
    """在 episode 的 JSON 字典中注入计算后的 audio_url。"""
    d = json.loads(episode.model_dump_json())
    d["audio_url"] = episode.audio_url
    return d


def bootstrap_podcast(podcast: Podcast) -> None:
    """
    初始化播客：
    1. 写 podcast.json 到本地
    2. 同步封面（本地 + OSS + docs/）
    3. 从 docs/ 恢复 episode.json 到本地（让 list_episodes() 能工作）
    """
    # 1. 写 podcast.json（仅本地，供 pipeline 读取）
    _save_podcast_sync(podcast)

    # 2. 上传封面
    cover_filename = None
    yaml_data = yaml.safe_load(YAML_PATH.read_text(encoding="utf-8"))
    for entry in yaml_data.get("podcasts") or []:
        if entry["id"] == podcast.id:
            cover_filename = entry.get("cover_file")
            break

    if cover_filename:
        cover_src = REPO_ROOT / "covers" / cover_filename
        if cover_src.exists():
            cover_bytes = cover_src.read_bytes()
            # 计算封面内容 hash，用于 URL 缓存刷新
            podcast.cover_hash = hashlib.md5(cover_bytes).hexdigest()[:8]
            # 写到本地
            local_cover = STATIC_DIR / podcast.id / "cover.jpg"
            local_cover.parent.mkdir(parents=True, exist_ok=True)
            local_cover.write_bytes(cover_bytes)
            # 上传 OSS
            if oss_enabled():
                upload_file_sync(f"{podcast.id}/cover.jpg", cover_bytes)
            # 复制到 docs/
            if settings.site_url:
                docs_cover = REPO_ROOT / "docs" / podcast.id / "cover.jpg"
                docs_cover.parent.mkdir(parents=True, exist_ok=True)
                docs_cover.write_bytes(cover_bytes)
            logger.info(f"[{podcast.name}] 封面已同步: {cover_filename} (hash={podcast.cover_hash})")
        else:
            logger.warning(f"[{podcast.name}] 封面文件不存在: {cover_src}")

    # 封面 hash 更新后重新保存 podcast.json
    if podcast.cover_hash:
        _save_podcast_sync(podcast)

    # 3. 从 docs/ 读取 episode.json → 还原本地 episode.json 文件
    docs_ep_root = REPO_ROOT / "docs" / podcast.id / "episodes"
    if docs_ep_root.exists():
        count = 0
        for ep_json_file in docs_ep_root.glob("*/episode.json"):
            ep_date = ep_json_file.parent.name
            ep_dir = STATIC_DIR / podcast.id / "episodes" / ep_date
            ep_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ep_json_file, ep_dir / "episode.json")
            count += 1
        if count:
            logger.info(f"[{podcast.name}] 已从 docs/ 恢复 {count} 个节目")


def inject_episode_urls(podcast: Podcast, ep_date: date) -> None:
    """将 audio_url 注入 episode.json（Pydantic @property 不序列化）。"""
    ep_path = STATIC_DIR / podcast.id / "episodes" / str(ep_date) / "episode.json"
    if not ep_path.exists():
        return

    ep = Episode.model_validate_json(ep_path.read_text(encoding="utf-8"))
    ep_dict = _episode_json_with_urls(ep)
    ep_path.write_bytes(json.dumps(ep_dict, ensure_ascii=False, indent=2).encode("utf-8"))


# ── HTML 模板 ─────────────────────────────────────────────────────────────────

_HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{PODCAST_NAME}}</title>
<meta name="description" content="{{PODCAST_DESCRIPTION}}">
<link rel="alternate" type="application/rss+xml" title="{{PODCAST_NAME}}" href="{{FEED_URL}}">
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;700&family=Source+Han+Sans+SC:wght@400;600&display=swap');

*, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }

:root {
  --bg: #faf8f5;
  --bg-card: #ffffff;
  --text: #1a1a1a;
  --text-secondary: #6b635a;
  --text-tertiary: #9e9588;
  --accent: #c45d3e;
  --accent-hover: #a8482d;
  --border: #e8e2da;
  --border-light: #f0ece6;
  --radius: 10px;
  --shadow: 0 1px 3px rgba(0,0,0,0.04), 0 4px 12px rgba(0,0,0,0.03);
  --font-serif: 'Noto Serif SC', 'Songti SC', serif;
  --font-sans: 'Source Han Sans SC', -apple-system, 'PingFang SC', sans-serif;
  --sidebar-width: 280px;
}

body {
  font-family: var(--font-sans);
  background: var(--bg);
  color: var(--text);
  line-height: 1.7;
  min-height: 100vh;
  -webkit-font-smoothing: antialiased;
}

/* ── Two-column Layout ── */
.layout {
  display: flex;
  min-height: 100vh;
  max-width: 1080px;
  margin: 0 auto;
}

.sidebar {
  width: var(--sidebar-width);
  flex-shrink: 0;
  border-right: 1px solid var(--border);
}

.sidebar-inner {
  position: sticky;
  top: 0;
  padding: 48px 32px;
  height: 100vh;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
}

.cover {
  width: 100%;
  aspect-ratio: 1;
  border-radius: var(--radius);
  object-fit: cover;
  box-shadow: var(--shadow);
  margin-bottom: 20px;
}

.podcast-name {
  font-family: var(--font-serif);
  font-size: 20px;
  font-weight: 700;
  line-height: 1.3;
  margin-bottom: 8px;
  letter-spacing: 0.3px;
}

.podcast-desc {
  font-size: 13px;
  color: var(--text-secondary);
  line-height: 1.7;
}

.subscribe-bar {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-top: 20px;
}

.btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 7px 14px;
  font-size: 13px;
  font-weight: 600;
  border-radius: 6px;
  text-decoration: none;
  transition: all 0.15s ease;
  border: 1px solid var(--border);
  color: var(--text-secondary);
  background: var(--bg-card);
}

.btn:hover {
  border-color: var(--accent);
  color: var(--accent);
}

.btn-primary {
  background: var(--accent);
  color: #fff;
  border-color: var(--accent);
}

.btn-primary:hover {
  background: var(--accent-hover);
  border-color: var(--accent-hover);
  color: #fff;
}

.btn svg { width: 14px; height: 14px; flex-shrink: 0; }

.sidebar-footer {
  margin-top: auto;
  padding-top: 24px;
  font-size: 12px;
  color: var(--text-tertiary);
}

/* ── Main Content ── */
.main {
  flex: 1;
  min-width: 0;
  max-width: 720px;
  padding: 48px 40px;
}

/* ── Episode List ── */
.episode-list {
  list-style: none;
}

.episode-item {
  display: block;
  padding: 18px 0;
  border-bottom: 1px solid var(--border-light);
  text-decoration: none;
  color: inherit;
  transition: background 0.1s;
  cursor: pointer;
}

.episode-item:first-child { padding-top: 0; }

.episode-item:hover { background: rgba(0,0,0,0.01); }

.ep-date {
  font-size: 12px;
  color: var(--text-tertiary);
  font-variant-numeric: tabular-nums;
  margin-bottom: 4px;
}

.ep-title {
  font-size: 15px;
  font-weight: 600;
  line-height: 1.5;
  margin-bottom: 4px;
  color: var(--text);
}

.ep-summary {
  font-size: 13px;
  color: var(--text-tertiary);
  line-height: 1.6;
  margin-bottom: 6px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.ep-meta {
  font-size: 12px;
  color: var(--text-tertiary);
  display: flex;
  gap: 12px;
}

/* ── Detail View ── */
.detail { padding-bottom: 64px; }

.back-link {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 13px;
  color: var(--text-tertiary);
  text-decoration: none;
  padding: 0 0 20px;
  transition: color 0.15s;
}

.back-link:hover { color: var(--accent); }

.back-link svg { width: 16px; height: 16px; }

.detail-title {
  font-family: var(--font-serif);
  font-size: 22px;
  font-weight: 700;
  line-height: 1.4;
  margin-bottom: 10px;
}

.detail-meta {
  font-size: 13px;
  color: var(--text-tertiary);
  display: flex;
  gap: 14px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}

.player {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 14px 16px;
  margin-bottom: 28px;
  box-shadow: var(--shadow);
  display: flex;
  align-items: center;
  gap: 14px;
}

.player-btn {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border: none;
  background: var(--accent);
  color: #fff;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  transition: background 0.15s;
}

.player-btn:hover { background: var(--accent-hover); }

.player-btn svg { width: 16px; height: 16px; }

.player-body { flex: 1; min-width: 0; }

.player-bar {
  width: 100%;
  height: 4px;
  background: var(--border);
  border-radius: 2px;
  cursor: pointer;
  position: relative;
}

.player-progress {
  height: 100%;
  background: var(--accent);
  border-radius: 2px;
  width: 0%;
  transition: width 0.1s linear;
}

.player-time {
  display: flex;
  justify-content: space-between;
  font-size: 11px;
  color: var(--text-tertiary);
  margin-top: 6px;
  font-variant-numeric: tabular-nums;
}

.player-speed {
  border: none;
  background: none;
  color: var(--text-tertiary);
  font-size: 11px;
  font-weight: 600;
  cursor: pointer;
  padding: 2px 6px;
  border-radius: 4px;
  flex-shrink: 0;
  transition: color 0.15s;
  font-variant-numeric: tabular-nums;
}

.player-speed:hover { color: var(--accent); }

/* ── Shownotes ── */
.shownotes {
  font-size: 15px;
  line-height: 1.8;
}

.shownotes h2 {
  font-family: var(--font-serif);
  font-size: 17px;
  font-weight: 700;
  margin: 28px 0 10px;
  padding-bottom: 6px;
  border-bottom: 1px solid var(--border-light);
  color: var(--text);
}

.shownotes h2:first-child { margin-top: 0; }

.shownotes p {
  margin-bottom: 12px;
  color: var(--text-secondary);
}

.shownotes ul {
  margin: 0 0 12px 0;
  padding-left: 20px;
}

.shownotes li {
  margin-bottom: 6px;
  color: var(--text-secondary);
}

.shownotes a {
  color: var(--accent);
  text-decoration: none;
  border-bottom: 1px solid transparent;
  transition: border-color 0.15s;
}

.shownotes a:hover {
  border-bottom-color: var(--accent);
}

/* ── States ── */
.loading {
  text-align: center;
  padding: 48px 0;
  color: var(--text-tertiary);
  font-size: 14px;
}

.empty {
  text-align: center;
  padding: 48px 0;
  color: var(--text-tertiary);
  font-size: 14px;
}

/* ── Animations ── */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}

.fade-in {
  animation: fadeUp 0.3s ease both;
}

.episode-item { animation: fadeUp 0.3s ease both; }

/* ── Responsive ── */
@media (max-width: 768px) {
  .layout { flex-direction: column; }
  .sidebar {
    width: 100%;
    border-right: none;
    border-bottom: 1px solid var(--border);
  }
  .sidebar-inner {
    position: static;
    height: auto;
    padding: 32px 20px;
    flex-direction: row;
    gap: 20px;
    align-items: flex-start;
  }
  .cover {
    width: 88px;
    height: 88px;
    margin-bottom: 0;
    flex-shrink: 0;
  }
  .sidebar-text { flex: 1; min-width: 0; }
  .subscribe-bar { flex-direction: row; flex-wrap: wrap; }
  .sidebar-footer { display: none; }
  .main { padding: 24px 20px; }
  .detail-title { font-size: 19px; }
}
</style>
</head>
<body>
<div class="layout">
  <aside class="sidebar">
    <div class="sidebar-inner">
      <img class="cover" src="{{COVER_URL}}" alt="{{PODCAST_NAME}}">
      <div class="sidebar-text">
        <h1 class="podcast-name">{{PODCAST_NAME}}</h1>
        <p class="podcast-desc">{{PODCAST_DESCRIPTION}}</p>
        <div class="subscribe-bar" id="subscribeBar">
          <a class="btn btn-primary" href="{{FEED_URL}}" target="_blank">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="6.18" cy="17.82" r="2.18"/><path d="M4 4.44A15.56 15.56 0 0 1 19.56 20"/><path d="M4 11.22A8.78 8.78 0 0 1 12.78 20"/></svg>
            RSS
          </a>
        </div>
      </div>
      <div class="sidebar-footer">由 AI 生成，每日自动更新</div>
    </div>
  </aside>
  <main class="main" id="app">
    <div class="loading">加载中...</div>
  </main>
</div>
<script>
(function() {
  var episodes = [];
  var cache = {};

  function formatDuration(s) {
    if (!s) return '';
    var m = Math.floor(s / 60);
    var sec = s % 60;
    return m + ':' + (sec < 10 ? '0' : '') + sec;
  }

  function renderMd(text) {
    var lines = text.split('\\n');
    var out = '';
    var inList = false;
    for (var i = 0; i < lines.length; i++) {
      var line = lines[i];
      if (/^## /.test(line)) {
        if (inList) { out += '</ul>'; inList = false; }
        out += '<h2>' + esc(line.slice(3)) + '</h2>';
      } else if (/^- /.test(line)) {
        if (!inList) { out += '<ul>'; inList = true; }
        out += '<li>' + inline(line.slice(2)) + '</li>';
      } else if (line.trim() === '') {
        if (inList) { out += '</ul>'; inList = false; }
      } else {
        if (inList) { out += '</ul>'; inList = false; }
        out += '<p>' + inline(line) + '</p>';
      }
    }
    if (inList) out += '</ul>';
    return out;
  }

  function esc(s) {
    var d = document.createElement('div');
    d.textContent = s;
    return d.innerHTML;
  }

  function inline(s) {
    s = esc(s);
    s = s.replace(/\\*\\*(.+?)\\*\\*/g, '<strong>$1</strong>');
    s = s.replace(/\\[([^\\]]+)\\]\\(([^)]+)\\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>');
    return s;
  }

  function renderList() {
    if (!episodes.length) {
      app.innerHTML = '<div class="empty">暂无节目</div>';
      return;
    }
    var h = '<ul class="episode-list">';
    for (var i = 0; i < episodes.length; i++) {
      var ep = episodes[i];
      h += '<li class="episode-item" onclick="location.hash=\\'' + ep.date + '\\'" style="animation-delay:' + (i * 0.04) + 's">';
      h += '<div class="ep-date">' + ep.date + '</div>';
      h += '<div class="ep-title">' + esc(ep.title.replace(/^\\d{8}-/, '')) + '</div>';
      if (ep.summary) h += '<div class="ep-summary">' + esc(ep.summary) + '</div>';
      h += '<div class="ep-meta">';
      h += '<span>' + formatDuration(ep.audio_duration) + '</span>';
      if (ep.tweet_count) h += '<span>' + ep.tweet_count + ' 条推文</span>';
      h += '</div></li>';
    }
    h += '</ul>';
    app.innerHTML = h;
  }

  function renderDetail(date) {
    var ep = null;
    for (var i = 0; i < episodes.length; i++) {
      if (episodes[i].date === date) { ep = episodes[i]; break; }
    }
    if (!ep) { location.hash = ''; return; }

    var title = ep.title.replace(/^\\d{8}-/, '');
    var h = '<div class="detail fade-in">';
    h += '<a class="back-link" href="#"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 18l-6-6 6-6"/></svg>返回列表</a>';
    h += '<h2 class="detail-title">' + esc(title) + '</h2>';
    h += '<div class="detail-meta">';
    h += '<span>' + ep.date + '</span>';
    h += '<span>' + formatDuration(ep.audio_duration) + '</span>';
    if (ep.tweet_count) h += '<span>' + ep.tweet_count + ' 条推文</span>';
    h += '</div>';
    if (ep.audio_url) {
      h += '<div class="player">';
      h += '<button class="player-btn" id="playBtn" aria-label="播放"><svg viewBox="0 0 24 24" fill="currentColor"><polygon points="6,3 20,12 6,21"/></svg></button>';
      h += '<div class="player-body"><div class="player-bar" id="playerBar"><div class="player-progress" id="playerProgress"></div></div>';
      h += '<div class="player-time"><span id="playerCur">0:00</span><span id="playerDur">' + formatDuration(ep.audio_duration) + '</span></div></div>';
      h += '<button class="player-speed" id="speedBtn">1x</button>';
      h += '</div>';
      h += '<audio id="audioEl" preload="none" src="' + esc(ep.audio_url) + '"></audio>';
    }
    h += '<div class="shownotes" id="shownotes"><div class="loading">加载内容...</div></div>';
    h += '</div>';
    app.innerHTML = h;

    initPlayer();

    var url = 'episodes/' + date + '/shownotes.md';
    if (cache[url]) {
      document.getElementById('shownotes').innerHTML = renderMd(cache[url]);
      return;
    }
    fetch(url).then(function(r) { return r.ok ? r.text() : ''; }).then(function(text) {
      cache[url] = text;
      var el = document.getElementById('shownotes');
      if (el) el.innerHTML = text ? renderMd(text) : '<div class="empty">暂无内容</div>';
    });
  }

  var playSvg = '<svg viewBox="0 0 24 24" fill="currentColor"><polygon points="6,3 20,12 6,21"/></svg>';
  var pauseSvg = '<svg viewBox="0 0 24 24" fill="currentColor"><rect x="5" y="3" width="4" height="18"/><rect x="15" y="3" width="4" height="18"/></svg>';
  var speeds = [1, 1.25, 1.5, 2, 0.75];

  function initPlayer() {
    var audio = document.getElementById('audioEl');
    var btn = document.getElementById('playBtn');
    var bar = document.getElementById('playerBar');
    var prog = document.getElementById('playerProgress');
    var cur = document.getElementById('playerCur');
    var dur = document.getElementById('playerDur');
    var speedBtn = document.getElementById('speedBtn');
    if (!audio || !btn) return;
    var si = 0;

    btn.onclick = function() {
      if (audio.paused) { audio.play(); btn.innerHTML = pauseSvg; }
      else { audio.pause(); btn.innerHTML = playSvg; }
    };

    audio.addEventListener('timeupdate', function() {
      if (!audio.duration) return;
      var pct = (audio.currentTime / audio.duration) * 100;
      prog.style.width = pct + '%';
      cur.textContent = formatDuration(Math.floor(audio.currentTime));
    });

    audio.addEventListener('loadedmetadata', function() {
      dur.textContent = formatDuration(Math.floor(audio.duration));
    });

    audio.addEventListener('ended', function() {
      btn.innerHTML = playSvg;
      prog.style.width = '0%';
      cur.textContent = '0:00';
    });

    bar.onclick = function(e) {
      if (!audio.duration) return;
      var rect = bar.getBoundingClientRect();
      var ratio = (e.clientX - rect.left) / rect.width;
      audio.currentTime = ratio * audio.duration;
    };

    speedBtn.onclick = function() {
      si = (si + 1) % speeds.length;
      audio.playbackRate = speeds[si];
      speedBtn.textContent = speeds[si] + 'x';
    };
  }

  var app = document.getElementById('app');

  var subscribeLinks = {{SUBSCRIBE_LINKS}};
  var platformInfo = {
    spotify: { name: 'Spotify', icon: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.66 0 12 0zm5.52 17.34c-.24.36-.66.48-1.02.24-2.82-1.74-6.36-2.1-10.56-1.14-.42.12-.78-.18-.9-.54-.12-.42.18-.78.54-.9 4.56-1.02 8.52-.6 11.7 1.32.42.18.48.66.24 1.02zm1.44-3.3c-.3.42-.84.6-1.26.3-3.24-1.98-8.16-2.58-11.94-1.38-.48.12-.99-.12-1.11-.6-.12-.48.12-.99.6-1.11 4.38-1.32 9.78-.66 13.5 1.62.36.18.54.78.21 1.17zm.12-3.36C15.24 8.4 8.82 8.16 5.16 9.3c-.6.18-1.2-.18-1.38-.72-.18-.6.18-1.2.72-1.38 4.26-1.26 11.28-1.02 15.72 1.62.54.3.72 1.02.42 1.56-.3.42-1.02.6-1.56.3z"/></svg>' },
    apple: { name: 'Apple', icon: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M18.9 10.2c-.1-2.1 1.7-3.1 1.8-3.2-1-1.5-2.5-1.7-3.1-1.7-1.3-.1-2.5.8-3.2.8-.7 0-1.7-.8-2.8-.7-1.5 0-2.8.9-3.6 2.2-1.5 2.6-.4 6.5 1.1 8.7.7 1 1.6 2.2 2.7 2.1 1.1 0 1.5-.7 2.8-.7s1.7.7 2.8.7c1.2 0 2-1 2.7-2.1.8-1.2 1.2-2.4 1.2-2.5-.1-.1-2.4-.9-2.4-3.6zM16.6 3.8c.6-.7 1-1.7.9-2.7-.9 0-1.9.6-2.5 1.3-.6.6-1 1.7-.9 2.6.9.1 1.9-.5 2.5-1.2z"/></svg>' },
    xiaoyuzhou: { name: '小宇宙', icon: '<svg viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="12" r="10" fill="none" stroke="currentColor" stroke-width="1.5"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="1.5"/><circle cx="12" cy="12" r="1.5"/></svg>' }
  };
  var bar = document.getElementById('subscribeBar');
  Object.keys(platformInfo).forEach(function(key) {
    if (!subscribeLinks[key]) return;
    var p = platformInfo[key];
    var a = document.createElement('a');
    a.className = 'btn';
    a.href = subscribeLinks[key];
    a.target = '_blank';
    a.innerHTML = p.icon + ' ' + p.name;
    bar.appendChild(a);
  });

  function route() {
    var hash = location.hash.slice(1);
    if (hash) renderDetail(hash);
    else renderList();
  }

  window.addEventListener('hashchange', route);

  fetch('episodes/index.json').then(function(r) { return r.json(); }).then(function(data) {
    episodes = data;
    route();
  }).catch(function() {
    app.innerHTML = '<div class="empty">加载失败</div>';
  });
})();
</script>
</body>
</html>
"""


# ── docs/ 站点文件 ────────────────────────────────────────────────────────────

def _build_episode_index(docs_dir: Path) -> list[dict]:
    """从 docs/{id}/episodes/*/episode.json 构建节目索引列表。"""
    ep_root = docs_dir / "episodes"
    if not ep_root.exists():
        return []
    episodes = []
    for ep_file in ep_root.glob("*/episode.json"):
        try:
            ep = json.loads(ep_file.read_text(encoding="utf-8"))
            if ep.get("status") != "done":
                continue
            # 从 shownotes 提取摘要：第一个 ## 标题后的第一段文字
            summary = ""
            shownotes = ep.get("shownotes", "")
            if shownotes:
                for line in shownotes.split("\n"):
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    summary = line
                    break
            episodes.append({
                "date": ep["date"],
                "title": ep.get("title", ""),
                "summary": summary,
                "audio_duration": ep.get("audio_duration", 0),
                "audio_url": ep.get("audio_url", ""),
                "tweet_count": ep.get("tweet_count", 0),
            })
        except Exception:
            pass
    episodes.sort(key=lambda e: e["date"], reverse=True)
    return episodes


def _build_index_html(podcast: Podcast) -> str:
    """生成播客前端页面 HTML。"""
    site = settings.site_url.rstrip("/")
    cover_url = f"{site}/{podcast.id}/cover.jpg"
    if podcast.cover_hash:
        cover_url += f"?v={podcast.cover_hash}"
    feed_url = f"{site}/{podcast.id}/feed.xml"
    # 合并 subscribe_links 和旧的 subscribe_url（向后兼容）
    links = dict(podcast.subscribe_links)
    if podcast.subscribe_url and "spotify" not in links:
        links["spotify"] = podcast.subscribe_url
    links_json = json.dumps(links, ensure_ascii=False)

    return _HTML_TEMPLATE.replace(
        "{{PODCAST_NAME}}", html.escape(podcast.name)
    ).replace(
        "{{PODCAST_DESCRIPTION}}", html.escape(podcast.description)
    ).replace(
        "{{COVER_URL}}", html.escape(cover_url)
    ).replace(
        "{{FEED_URL}}", html.escape(feed_url)
    ).replace(
        "{{SUBSCRIBE_LINKS}}", links_json
    )


def write_site_files(podcasts: list[Podcast]) -> None:
    """将 feed.xml、md、index.json、index.html 复制/生成到 docs/。"""
    if not settings.site_url:
        return
    for podcast in podcasts:
        docs_dir = REPO_ROOT / "docs" / podcast.id
        # feed.xml
        feed_src = STATIC_DIR / podcast.id / "feed.xml"
        if feed_src.exists():
            feed_dst = docs_dir / "feed.xml"
            feed_dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(feed_src, feed_dst)
            logger.info(f"[{podcast.name}] feed.xml → docs/{podcast.id}/feed.xml")
        # 每期的 episode.json / posts.md / script.md / shownotes.md
        ep_root = STATIC_DIR / podcast.id / "episodes"
        if ep_root.exists():
            for src_file in ep_root.glob("*/*.md"):
                rel = src_file.relative_to(STATIC_DIR / podcast.id)
                dst = docs_dir / rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_file, dst)
            for src_file in ep_root.glob("*/episode.json"):
                rel = src_file.relative_to(STATIC_DIR / podcast.id)
                dst = docs_dir / rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_file, dst)
        # 节目索引 index.json
        episodes_index = _build_episode_index(docs_dir)
        idx_path = docs_dir / "episodes" / "index.json"
        idx_path.parent.mkdir(parents=True, exist_ok=True)
        idx_path.write_text(
            json.dumps(episodes_index, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        logger.info(f"[{podcast.name}] episodes/index.json ({len(episodes_index)} 期)")
        # 前端页面 index.html
        index_html = _build_index_html(podcast)
        (docs_dir / "index.html").write_text(index_html, encoding="utf-8")
        logger.info(f"[{podcast.name}] index.html → docs/{podcast.id}/index.html")


# ── 飞书测试 ──────────────────────────────────────────────────────────────────

def test_feishu(podcast_id: Optional[str] = None) -> None:
    """用已有的最新一期 episode 测试飞书通知，不触发任何生成。"""
    all_podcasts = load_podcasts_from_yaml()
    if podcast_id:
        all_podcasts = [p for p in all_podcasts if p.id == podcast_id]
    if not all_podcasts:
        logger.error("未找到播客" + (f" ID: {podcast_id}" if podcast_id else ""))
        sys.exit(1)

    for podcast in all_podcasts:
        if not podcast.feishu_webhook:
            logger.warning(f"[{podcast.name}] 未配置 feishu_webhook，跳过")
            continue

        # 从 docs/ 找最新 episode.json
        docs_ep_root = REPO_ROOT / "docs" / podcast.id / "episodes"
        if not docs_ep_root.exists():
            logger.warning(f"[{podcast.name}] docs/ 中无 episode 数据")
            continue

        ep_files = sorted(docs_ep_root.glob("*/episode.json"), reverse=True)
        if not ep_files:
            logger.warning(f"[{podcast.name}] 无已有 episode")
            continue

        ep = Episode.model_validate_json(ep_files[0].read_text(encoding="utf-8"))
        logger.info(f"[{podcast.name}] 用 {ep.date} 的 episode 测试飞书通知: {ep.title}")
        send_feishu_notification(podcast.feishu_webhook, podcast, ep)


# ── 主流程 ───────────────────────────────────────────────────────────────────

async def main(force: bool = False, podcast_id: Optional[str] = None, max_posts: Optional[int] = None, regenerate: bool = False) -> None:
    all_podcasts = load_podcasts_from_yaml()

    if not all_podcasts:
        logger.warning("podcasts.yaml 中没有播客配置")
        return

    if podcast_id:
        all_podcasts = [p for p in all_podcasts if p.id == podcast_id]
        if not all_podcasts:
            logger.error(f"未找到播客 ID: {podcast_id}")
            sys.exit(1)

    now_shanghai = datetime.now(SHANGHAI_TZ)
    current_hour = now_shanghai.hour
    current_weekday = now_shanghai.weekday()
    logger.info(f"当前时间: {now_shanghai.strftime('%Y-%m-%d %H:%M')} (Asia/Shanghai)")

    # Bootstrap 所有播客
    for podcast in all_podcasts:
        logger.info(f"[{podcast.name}] 初始化...")
        await asyncio.to_thread(bootstrap_podcast, podcast)

    # 生成节目
    for podcast in all_podcasts:
        if not force and podcast.publish_hour != current_hour:
            logger.info(
                f"[{podcast.name}] 跳过：publish_hour={podcast.publish_hour}，"
                f"当前={current_hour}"
            )
            continue

        if not force and podcast.frequency == "weekly" and podcast.publish_day != current_weekday:
            logger.info(
                f"[{podcast.name}] 跳过：publish_day={podcast.publish_day}，"
                f"当前={current_weekday}"
            )
            continue

        logger.info(f"[{podcast.name}] 开始生成节目...")
        await generate_episode(podcast.id, max_posts=max_posts, frequency=podcast.frequency, extra_prompt=podcast.extra_prompt, regenerate=regenerate)

        # 注入 audio_url 到 episode.json
        today = datetime.now(SHANGHAI_TZ).date()
        await asyncio.to_thread(inject_episode_urls, podcast, today)

    # 复制文件到 docs/ 供 GitHub Pages 托管
    await asyncio.to_thread(write_site_files, all_podcasts)

    logger.info("全部完成")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="生成播客节目并上传到 OSS")
    parser.add_argument("--force", action="store_true", help="忽略 publish_hour 检查")
    parser.add_argument("--podcast", type=str, default=None, help="只处理指定播客 ID")
    parser.add_argument("--max-posts", type=int, default=None, help="最大抓取推文数")
    parser.add_argument("--regenerate", action="store_true", help="跳过推文抓取，使用已有 posts.md 重新生成")
    parser.add_argument("--test-feishu", action="store_true", help="用最新已有 episode 测试飞书通知")
    args = parser.parse_args()

    if args.test_feishu:
        test_feishu(podcast_id=args.podcast)
    else:
        force = args.force or args.regenerate  # --regenerate 隐含 --force
        asyncio.run(main(force=force, podcast_id=args.podcast, max_posts=args.max_posts, regenerate=args.regenerate))
