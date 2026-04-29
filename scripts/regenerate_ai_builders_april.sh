#!/usr/bin/env bash
# 批量重生成 ai-builders 的 4 月 3 ~ 20 日节目（每期 ~5 分钟，共 ~90 分钟）。
# 复用 docs/ai-builders/episodes/<date>/posts.md，跳过推文抓取，跑 LLM + TTS + feed。
# 失败的日期会记下但不中断后续，整批跑完再汇总。
#
# Usage:
#   scripts/regenerate_ai_builders_april.sh                # 默认 04-03..04-20
#   scripts/regenerate_ai_builders_april.sh 2026-04-08 2026-04-12   # 自定义闭区间
set -uo pipefail

cd "$(dirname "$0")/.."

if [ -f .venv/bin/activate ]; then
    # shellcheck disable=SC1091
    source .venv/bin/activate
fi

START=${1:-2026-04-03}
END=${2:-2026-04-20}

LOG="/tmp/regen-ai-builders-$(date +%Y%m%d-%H%M%S).log"
echo "Logging to $LOG"
echo "Range: $START .. $END"

# 生成日期列表（GNU date 和 BSD date 语法不同，这里用 python 求闭区间）
DATES=$(python - <<PY
from datetime import date, timedelta
s = date.fromisoformat("$START")
e = date.fromisoformat("$END")
d = s
while d <= e:
    print(d.isoformat())
    d += timedelta(days=1)
PY
)

failed=()
ok=()
total=$(echo "$DATES" | wc -l | tr -d ' ')
i=0

for d in $DATES; do
    i=$((i + 1))
    echo "" | tee -a "$LOG"
    echo "=== [$i/$total] $d ===" | tee -a "$LOG"
    if python -m generate --regenerate-date "$d" --podcast ai-builders 2>&1 | tee -a "$LOG"; then
        ok+=("$d")
    else
        echo "FAILED: $d" | tee -a "$LOG"
        failed+=("$d")
    fi
done

echo "" | tee -a "$LOG"
echo "=== Summary ===" | tee -a "$LOG"
echo "OK     ${#ok[@]} of $total" | tee -a "$LOG"
echo "Failed ${#failed[@]} of $total" | tee -a "$LOG"
if [ ${#failed[@]} -gt 0 ]; then
    printf '  - %s\n' "${failed[@]}" | tee -a "$LOG"
    exit 1
fi
