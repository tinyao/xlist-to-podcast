"""
用已有的 posts.md 和指定 prompt 文件测试 LLM 生成 script / shownotes。
结果保存在对应 episode 目录的 preview/ 子文件夹下。

用法：
  python preview_content.py --podcast ai-builders --date 2026-03-09
  python preview_content.py --podcast ai-builders --date 2026-03-09 --prompt prompts/tech-daily.md
  python preview_content.py --podcast ai-builders --date 2026-03-09 --prompt prompts/tech-daily.md --extra-prompt "多关注 AI Agent 相关内容"
"""
import argparse
import logging
import re
import sys
from datetime import date
from pathlib import Path

from app.services.llm import generate_content
from app.services.twitter import FetchResult

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

REPO_ROOT = Path(__file__).resolve().parent
DOCS_DIR = REPO_ROOT / "docs"


def _find_posts_md(podcast_id: str, ep_date: str) -> Path:
    """在 docs/ 中查找指定 episode 的 posts.md。"""
    path = DOCS_DIR / podcast_id / "episodes" / ep_date / "posts.md"
    if path.exists():
        return path
    raise FileNotFoundError(
        f"未找到 posts.md: {path}\n"
        f"请确认 podcast_id={podcast_id} 和 date={ep_date} 是否正确"
    )


def _count_tweets(text: str) -> int:
    """从 posts.md 中统计推文数量。"""
    return len(re.findall(r"^\[tweet \d+\]", text, re.MULTILINE))


def _load_podcast_config(podcast_id: str) -> dict:
    """从 podcasts.yaml 读取指定播客的配置。"""
    import yaml
    yaml_path = REPO_ROOT / "podcasts.yaml"
    data = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    for entry in data.get("podcasts") or []:
        if entry["id"] == podcast_id:
            return entry
    raise ValueError(f"podcasts.yaml 中未找到播客 ID: {podcast_id}")


def main() -> None:
    parser = argparse.ArgumentParser(description="用已有 posts 测试 LLM 生成 script/shownotes")
    parser.add_argument("--podcast", required=True, help="播客 ID")
    parser.add_argument("--date", required=True, help="Episode 日期（YYYY-MM-DD）")
    parser.add_argument("--prompt", default="", help="自定义 prompt 文件路径（相对仓库根目录）")
    parser.add_argument("--extra-prompt", default="", help="补充 LLM 提示词")
    args = parser.parse_args()

    # 1. 读取 posts.md
    posts_path = _find_posts_md(args.podcast, args.date)
    posts_text = posts_path.read_text(encoding="utf-8")
    tweet_count = _count_tweets(posts_text)
    logger.info(f"读取 posts.md: {posts_path} ({tweet_count} 条推文)")

    tweets = FetchResult(count=tweet_count, text=posts_text)

    # 2. 读取播客配置
    config = _load_podcast_config(args.podcast)
    podcast_name = config["name"]
    language = config.get("language", "zh")
    frequency = config.get("frequency", "daily")

    # prompt_file 优先使用命令行参数，否则使用 podcasts.yaml 中的配置
    prompt_file = args.prompt or config.get("prompt_file", "")
    # extra_prompt 合并：yaml 配置 + 命令行参数
    extra_prompt_parts = []
    if config.get("extra_prompt"):
        extra_prompt_parts.append(config["extra_prompt"])
    if args.extra_prompt:
        extra_prompt_parts.append(args.extra_prompt)
    extra_prompt = "\n\n".join(extra_prompt_parts)

    ep_date = date.fromisoformat(args.date)

    logger.info(f"播客: {podcast_name}, 语言: {language}, prompt: {prompt_file or '(默认)'}")

    # 3. 调用 LLM 生成
    logger.info("调用 LLM 生成 script + shownotes...")
    script, shownotes, title = generate_content(
        tweets=tweets,
        podcast_name=podcast_name,
        language=language,
        today=ep_date,
        frequency=frequency,
        extra_prompt=extra_prompt,
        prompt_file=prompt_file,
    )

    # 4. 保存到 preview/ 子文件夹
    preview_dir = DOCS_DIR / args.podcast / "episodes" / args.date / "preview"
    preview_dir.mkdir(parents=True, exist_ok=True)

    (preview_dir / "script.md").write_text(script, encoding="utf-8")
    (preview_dir / "shownotes.md").write_text(shownotes, encoding="utf-8")
    if title:
        (preview_dir / "title.txt").write_text(title, encoding="utf-8")

    logger.info(f"预览结果已保存到: {preview_dir}")
    logger.info(f"  标题: {title}")
    logger.info(f"  script.md: {len(script)} 字符")
    logger.info(f"  shownotes.md: {len(shownotes)} 字符")


if __name__ == "__main__":
    main()
