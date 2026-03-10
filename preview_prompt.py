"""
Prompt 预览工具：用已有的 posts.md + 指定 prompt 文件，测试 LLM 生成效果。

结果保存在对应 episode 目录下的 preview/ 子文件夹，不影响正式文件。

用法：
  python -m preview_prompt --podcast ai-builders --date 2026-03-10
  python -m preview_prompt --podcast ai-builders --date 2026-03-10 --prompt prompts/zh-tech-daily.md
  python -m preview_prompt --podcast ai-builders --date 2026-03-10 --prompt prompts/my-new-prompt.md --extra-prompt "额外要求"
"""
import argparse
import logging
import re
import sys
from datetime import date, datetime
from pathlib import Path

import yaml

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

REPO_ROOT = Path(__file__).resolve().parent
YAML_PATH = REPO_ROOT / "podcasts.yaml"
DOCS_DIR = REPO_ROOT / "docs"


def _find_posts(podcast_id: str, ep_date: str) -> str:
    """从 docs/ 查找 posts.md 内容。"""
    posts_path = DOCS_DIR / podcast_id / "episodes" / ep_date / "posts.md"
    if not posts_path.exists():
        raise FileNotFoundError(f"posts.md 不存在: {posts_path}")
    return posts_path.read_text(encoding="utf-8")


def _count_posts(posts_text: str) -> int:
    """从 posts.md 文本中计算推文数量。"""
    return len(re.findall(r"^\[tweet \d+\]", posts_text, re.MULTILINE))


def _load_podcast_config(podcast_id: str) -> dict:
    """从 podcasts.yaml 读取播客配置。"""
    data = yaml.safe_load(YAML_PATH.read_text(encoding="utf-8"))
    for entry in data.get("podcasts") or []:
        if entry["id"] == podcast_id:
            return entry
    raise ValueError(f"播客 ID 未找到: {podcast_id}")


def main() -> None:
    parser = argparse.ArgumentParser(description="用已有 posts 测试 prompt 生成效果")
    parser.add_argument("--podcast", type=str, required=True, help="播客 ID")
    parser.add_argument("--date", type=str, required=True, help="节目日期 (YYYY-MM-DD)")
    parser.add_argument("--prompt", type=str, default=None, help="prompt 文件路径（相对仓库根目录），留空使用播客配置的 prompt_file")
    parser.add_argument("--extra-prompt", type=str, default=None, help="补充 prompt（覆盖播客配置的 extra_prompt）")
    args = parser.parse_args()

    # 1. 加载播客配置
    config = _load_podcast_config(args.podcast)
    podcast_name = config["name"]
    language = config.get("language", "zh")
    frequency = config.get("frequency", "daily")

    # 确定 prompt 文件
    prompt_file = args.prompt or config.get("prompt_file", "")
    extra_prompt = args.extra_prompt if args.extra_prompt is not None else config.get("extra_prompt", "")

    # 2. 读取 posts.md
    logger.info(f"[{podcast_name}] 读取 posts: docs/{args.podcast}/episodes/{args.date}/posts.md")
    posts_text = _find_posts(args.podcast, args.date)
    count = _count_posts(posts_text)
    logger.info(f"[{podcast_name}] 共 {count} 条推文")

    # 3. 调用 LLM 生成
    # 延迟导入，避免在没有配置环境变量时立即报错
    from app.services.twitter import FetchResult
    from app.services.llm import generate_content

    ep_date = date.fromisoformat(args.date)
    tweets = FetchResult(count=count, text=posts_text)

    logger.info(f"[{podcast_name}] 使用 prompt: {prompt_file or '(默认)'}")
    if extra_prompt:
        logger.info(f"[{podcast_name}] extra_prompt: {extra_prompt[:80]}...")

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
    (preview_dir / "title.txt").write_text(title, encoding="utf-8")

    # 记录使用的 prompt 文件，便于对照
    meta = f"prompt_file: {prompt_file or '(默认)'}\nextra_prompt: {extra_prompt or '(无)'}\ngenerated_at: {datetime.utcnow().isoformat()}Z\n"
    (preview_dir / "meta.txt").write_text(meta, encoding="utf-8")

    logger.info(f"[{podcast_name}] 预览结果已保存到: {preview_dir}")
    logger.info(f"[{podcast_name}] 标题: {title}")

    # 输出摘要到 stdout
    print(f"\n{'='*60}")
    print(f"标题: {title}")
    print(f"Script 字数: {len(script)}")
    print(f"保存位置: {preview_dir}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
