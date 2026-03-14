## 今日摘要
Anthropic 宣布为期两周的春假双倍额度，同步推出 `/effort max` 等一批 Claude Code 新功能。OpenClaw 迎来高光周末：Chrome DevTools MCP 正式集成上线、NVIDIA 工程师协助安全审查、Microsoft 加入 Teams 集成建设、lossless-claw 插件收藏量破三千。郭宇用纯 Qwen 3.5 六个 agent 在东京"开"了一家装置艺术公司 KOUROKU，跑了 1036 轮后因 sandbox 超时终止。Aaron Levie 提出 agent 采购论：没有好 API 的平台将对 agent 隐形。

## 重点话题
- **Anthropic 春假礼包**：非高峰时段和周末 Claude 使用额度翻倍，持续两周；新增 `/effort max` 深度推理模式（需按 session 开启）、setup script 支持、postcompact hook 等多项功能更新
- **OpenClaw 大周末**：Chrome DevTools MCP 正式进入 beta（支持真实浏览器控制）；NVIDIA 工程师协助处理安全问题；Microsoft 6 名员工投入 Teams 集成；lossless-claw 无损上下文插件爆火（3153 收藏）；并行工具调用即将到来
- **郭宇 KOUROKU 实验**：目标东京装置艺术公司，6 个 Qwen 3.5 agent，1036 轮 / 6.6 小时，产出 82 个文件（含 WebGL 官网、商业计划书、品牌系统），因 sandbox 超时终止且交付物丢失；郭宇在单向街现场展示 wanman AI
- **Aaron Levie 的 agent 采购论**：为 AI agent 从零重新设计流程 vs 叠加 AI 到现有流程，差距将持续拉大；未来 agent 会成为软件采购的主要决策者，没有可调用 API 的平台将对 agent 隐形

## 快讯
- Meta 宣布裁员超过 20%，来源路透社
- Axiom Math 完成 2 亿美元 A 轮，专注用形式证明语言 Lean 做数学推理 AI，Putnam 竞赛 12/12
- ClawCon Austin：15 岁用户用 OpenClaw 拿到超 3 万美元合同
- agent-browser 全面改写为 Rust，冷启动快 1.6x，内存减少 18x，安装包缩小 99x
- Ramp CPO：25 个 PM 三阶段 Claude Code 技能（问题框定 → 6-10 个并行 agent 研究 → 规格整合）去年交付 500+ 功能
- swyx：agentic AI 本质上是后端工程，核心是事件驱动、数据管道、分布式系统和可观测性
- 郭宇观察：同样产品中文社区做了没水花，英语社区做了上 Product Hunt，创新重心回到硅谷

## 值得阅读
- [Claude March 2026 usage promotion](https://support.claude.com/en/articles/14063676-claude-march-2026-usage-promotion) — Anthropic 官方说明
- [Claude Code CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) — /effort max 等新功能完整列表
- [Chrome DevTools MCP](https://developer.chrome.com/blog/chrome-devtools-mcp-debug-your-browser-session) — OpenClaw 集成的浏览器控制技术文档
- [lossless-claw](https://github.com/martian-engineering/lossless-claw) — OpenClaw 无损上下文管理插件（3153 收藏）
- [Ramp AI-native PM workflow](https://www.youtube.com/@peteryangyt?sub_confirmation=1) — Peter Yang 访谈 Ramp CPO，三阶段 Claude Code 产品规格技能
- [Axiom Math interview with Matt Turck](https://t.co/E7Od96LZJc) — 2 亿 A 轮数学推理 AI 深度访谈
- Zara Zhang 精选阅读单（8 篇关于 AI 时代产品构建的文章）— 包括 Aaron Levie「Building for Trillions of Agents」、Thariq「Seeing like an Agent」等