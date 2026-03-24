## 今日摘要
LiteLLM PyPI 遭供应链攻击，单次 pip install 可泄露所有凭据，Karpathy 发出警告；Claude Code 推出 Auto Mode，彻底告别权限弹窗；Figma MCP 进入开放 beta，AI agent 可直接在画布上设计；Vercel CEO 分享内部实践，几乎所有 SaaS 工具已被生成式 app 替代；Lenny 2026 年初就业报告显示 PM 和工程师需求创新高，设计岗持平。

## 重点话题
- **LiteLLM 供应链攻击**：PyPI 1.82.8 版本被植入恶意代码，可窃取 SSH 密钥、云服务凭据等所有敏感信息，在线不足一小时即被发现，影响所有依赖 litellm 的项目
- **Claude Code Auto Mode**：不再需要逐条批准权限，也不需要跳过全部权限，由 Claude 在 safeguard 保护下自主判断每个操作是否安全，目前仅限 Teams 计划
- **Figma MCP 开放 beta**：AI agent 通过 use_figma MCP 工具直接操作 Figma 画布，Claude Code 生成 Plugin API 代码来执行设计动作，支持双向 Code↔Figma 转换
- **SaaSpocalypse 内部实践**：Vercel 内部几乎所有 SaaS 工具已被生成 app 替代，Guillermo 和 Aaron Levie 判断软件正从人机界面演变为 agent 操作的业务逻辑层
- **2026 年初科技就业市场报告**：PM 岗位 7300+ 个（3 年来最高），工程师 67000+ 个，AI 岗位曲棍球棒增长，设计岗位持平，PM 需求是设计的 1.27 倍

## 快讯
- OpenAI 成立 OpenAI Foundation，一年投入超 10 亿美元，Wojciech Zaremba 转任"AI Resilience"负责人
- Sora 应用关闭，swyx 称为"OpenAI 清理副业的第一个牺牲品"，Justine Moore 致敬其 remix 文化设计理念
- 哈佛物理学家 Matthew Schwartz：Claude Opus 4.5 相当于二年级博士生水平，研究速度提升 10 倍
- Cloudflare 推出 Dynamic Workers，AI 生成代码可在轻量隔离环境执行，速度比传统容器快 100 倍
- Peter Steinberger 分享 Codex 代码评审工作流，CodexBar 更新至 0.19.0 支持阿里 Coding Plan
- 郭宇昨日完成 131 个提交，nkmc gateway 开源，两款新 vibe 产品准备上线

## 值得阅读
- [Karpathy 关于 LiteLLM 供应链攻击的原帖](https://twitter.com/karpathy/status/2036487306585268612)（附详细技术分析）
- [Figma MCP 官方公告及文档](https://twitter.com/figma/status/2036442891346755787)
- [Thariq 主持的 Claude Code × Figma 直播（3 月 31 日）](https://fig-events.figma.com/claude-to-figma)
- [Guillermo Rauch 关于 SaaSpocalypse 的完整推文](https://twitter.com/rauchg/status/2036447879985037495)
- [Lenny Rachitsky 2026 年初产品岗位市场完整报告](https://www.lennysnewsletter.com/p/state-of-the-product-job-market-in-ee9)
- [Alex Albert 推荐：Claude Opus 4.5 做理论物理研究（Anthropic 博客）](https://twitter.com/alexalbert__/status/2036232980059062550)