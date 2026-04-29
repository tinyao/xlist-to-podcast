"""直接调 `claude -p` 跑 ai-builders 当天的 prompt，逐条打印 stream-json 事件。

用法：
    python -m tools.probe_claude_cli --podcast ai-builders --date 2026-04-02
    python -m tools.probe_claude_cli --podcast ai-builders --date 2026-04-02 --model sonnet
    python -m tools.probe_claude_cli --prompt-file /tmp/foo.txt    # 跳过 prompt 构建，直接用文件

每个事件打印：
    [ELAPSED.s] <event_type> <summary>
其中 assistant 事件会展开 content blocks 的 type + 字符数（可见 thinking vs text）。
"""
from __future__ import annotations

import argparse
import asyncio
import json
import re
import shutil
import subprocess
import sys
import threading
import time
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from app.services.llm import _build_prompt  # noqa: E402
from app.services.twitter import FetchResult  # noqa: E402
from app.storage import get_podcast, list_episodes  # noqa: E402


def _short(s: str, n: int = 80) -> str:
    s = s.replace("\n", "\\n")
    return s if len(s) <= n else s[:n] + "…"


async def _build_prompt_for(podcast_id: str, ep_date: date, prompt_path: Path | None) -> str:
    if prompt_path:
        return prompt_path.read_text(encoding="utf-8")

    podcast = await get_podcast(podcast_id)
    if not podcast:
        raise SystemExit(f"podcast not found: {podcast_id}")

    posts_path = REPO / "docs" / podcast.id / "episodes" / str(ep_date) / "posts.md"
    if not posts_path.exists():
        raise SystemExit(f"posts.md not found: {posts_path}")
    posts_text = posts_path.read_text(encoding="utf-8")
    tweet_count = len(re.findall(r"^\[tweet \d+\]", posts_text, re.MULTILINE))
    tweets = FetchResult(count=tweet_count, text=posts_text)

    recent = []
    if podcast.frequency == "daily":
        all_eps = await list_episodes(podcast.id, limit=5)
        recent = [e for e in all_eps if e.status == "done" and e.date < ep_date][:2]

    return _build_prompt(
        tweets=tweets,
        podcast_name=podcast.name,
        language=podcast.language,
        today=ep_date,
        frequency=podcast.frequency,
        extra_prompt="",
        prompt_file=podcast.prompt_file,
        recent_episodes=recent,
    )


def _print_event(elapsed: float, event: dict) -> None:
    ev_type = event.get("type", "?")
    prefix = f"[{elapsed:7.1f}s] {ev_type:12s}"

    if ev_type == "system" and event.get("subtype") == "init":
        print(f"{prefix} model={event.get('model')} session={event.get('session_id', '?')[:12]}")
        return

    if ev_type == "assistant":
        msg = event.get("message", {}) or {}
        blocks = msg.get("content", []) or []
        usage = msg.get("usage") or {}
        block_summary = ", ".join(
            f"{b.get('type', '?')}:{len(b.get('text', '') or b.get('thinking', '') or '')}c"
            for b in blocks if isinstance(b, dict)
        )
        usage_summary = ""
        if usage:
            usage_summary = (
                f" usage={{in:{usage.get('input_tokens', '?')},"
                f"out:{usage.get('output_tokens', '?')},"
                f"cache_r:{usage.get('cache_read_input_tokens', 0)},"
                f"cache_w:{usage.get('cache_creation_input_tokens', 0)}}}"
            )
        print(f"{prefix} blocks=[{block_summary}]{usage_summary}")
        # also print first ~80 chars of any text block to confirm content
        for b in blocks:
            if isinstance(b, dict) and b.get("type") == "text":
                txt = b.get("text", "") or ""
                if txt:
                    print(f"{' ' * 22}text-preview: {_short(txt, 100)}")
            elif isinstance(b, dict) and b.get("type") == "thinking":
                t = b.get("thinking", "") or ""
                if t:
                    print(f"{' ' * 22}thinking-preview: {_short(t, 100)}")
        return

    if ev_type == "result":
        print(
            f"{prefix} subtype={event.get('subtype')} "
            f"result_chars={len(event.get('result', '') or '')} "
            f"cost_usd={event.get('total_cost_usd', '?')} "
            f"duration_ms={event.get('duration_ms', '?')}"
        )
        return

    # fallback for unknown event types
    keys = list(event.keys())
    print(f"{prefix} keys={keys}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--podcast", default="ai-builders")
    parser.add_argument("--date", default="2026-04-02")
    parser.add_argument("--model", default="opus", help="passed to claude --model (opus|sonnet|haiku)")
    parser.add_argument("--prompt-file", type=Path, default=None,
                        help="skip prompt build and read from this file")
    parser.add_argument("--save-prompt", type=Path, default=None,
                        help="dump the assembled prompt to this file (for reuse)")
    parser.add_argument("--timeout", type=int, default=1500)
    args = parser.parse_args()

    ep_date = date.fromisoformat(args.date) if args.date else date.today()
    prompt = asyncio.run(_build_prompt_for(args.podcast, ep_date, args.prompt_file))
    print(f"prompt: {len(prompt)} chars", file=sys.stderr)
    if args.save_prompt:
        args.save_prompt.write_text(prompt, encoding="utf-8")
        print(f"prompt saved to {args.save_prompt}", file=sys.stderr)

    claude_path = shutil.which("claude")
    if not claude_path:
        raise SystemExit("claude CLI not found")

    cmd = [
        claude_path, "-p",
        "--model", args.model,
        "--max-turns", "1",
        "--output-format", "stream-json",
        "--verbose",
        "--no-session-persistence",
    ]
    print(f"running: {' '.join(cmd)}", file=sys.stderr)

    proc = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1,
    )

    stderr_lines: list[str] = []

    def _drain_stderr() -> None:
        for raw in proc.stderr:  # type: ignore[union-attr]
            stripped = raw.rstrip()
            if stripped:
                stderr_lines.append(stripped)
                print(f"[stderr] {stripped}", file=sys.stderr)

    def _write_stdin() -> None:
        try:
            proc.stdin.write(prompt)  # type: ignore[union-attr]
        finally:
            proc.stdin.close()  # type: ignore[union-attr]

    timed_out = threading.Event()

    def _on_timeout() -> None:
        timed_out.set()
        proc.kill()

    threading.Thread(target=_drain_stderr, daemon=True).start()
    threading.Thread(target=_write_stdin, daemon=True).start()
    watchdog = threading.Timer(args.timeout, _on_timeout)
    watchdog.start()

    start = time.monotonic()
    last_event_at = 0.0
    heartbeat_stop = threading.Event()

    def _heartbeat() -> None:
        while not heartbeat_stop.is_set():
            if heartbeat_stop.wait(timeout=30):
                return
            elapsed = time.monotonic() - start
            since_last = elapsed - last_event_at
            if since_last >= 30:
                print(f"[{elapsed:7.1f}s] (heartbeat) no events for {since_last:.0f}s",
                      file=sys.stderr)

    threading.Thread(target=_heartbeat, daemon=True).start()

    try:
        for raw in proc.stdout:  # type: ignore[union-attr]
            stripped = raw.strip()
            if not stripped:
                continue
            try:
                event = json.loads(stripped)
            except json.JSONDecodeError:
                print(f"[non-json] {_short(stripped, 200)}", file=sys.stderr)
                continue
            elapsed = time.monotonic() - start
            last_event_at = elapsed
            _print_event(elapsed, event)
        proc.wait()
    finally:
        watchdog.cancel()
        heartbeat_stop.set()

    if timed_out.is_set():
        print(f"\nTIMEOUT after {args.timeout}s", file=sys.stderr)
    print(f"\nexit={proc.returncode} stderr_lines={len(stderr_lines)}", file=sys.stderr)


if __name__ == "__main__":
    main()
