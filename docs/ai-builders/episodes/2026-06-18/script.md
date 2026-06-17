嗨，各位。
早上好。
今天是 2026年06月18日，星期四。
欢迎收听 AI Builders Daily。每天 10 分钟，看 X 上 AI 圈最值得关注的信号。

Vercel 昨晚发布了他们的 agent 框架 eve，它对标的是 Next.js 在 web 应用里的位置吗？GLM-5.2 开源模型跑分超过了 Opus 4.8，中国公司现在连 IDE 都开始像素级复刻了？设计师在终端里写代码这件事，到底在动摇什么？先从最让工程师睡不着的那件事开始。

Vercel 昨晚在伦敦的 SHIP 活动上发布了 agent 框架 eve。Guillermo 亲自下场解释它的设计哲学：就像当年 Next.js 用 pages/index.js 定义 web 应用一样，eve 用 agent/instructions.md 来定义 agent。一个 agent 就是一个目录，里面有工具、技能、沙箱和调度文件。你往 instructions.md 里写一段英文，它就变成一个可部署的 agent。

Guillermo 的原话是"比 Next.js 要求更少"。而就在同一天，中国 AI 公司智谱的 GLM-5.2 模型在 Vercel 自家的 Next.js Evals 跑分上超过了 Opus 4.8。Guillermo 在宣布 eve 的同时专门提了这件事，说模型竞争太激烈了，AI SDK 比以往任何时候都重要。Box 的 CEO Aaron Levie 也发了一条长推，说开源模型和闭源模型之间的差距到底有多大，会决定整个芯片栈、推理部署、主权 AI 和利润率结构。目前来看，开源阵营咬得很紧。

Vercel 这次发布的其实是一整套 agent 基础设施。除了 eve 框架，还有 Vercel Connect 解决 agent 连接外部数据时的 OAuth 和凭证问题，沙箱运行时间从 30 分钟拉长到 24 小时。Guillermo 说 agent 最难的部分不是构建 agent 本身，而是数据——你有一个 AGI 坐在那里等着被释放，结果卡在 OAuth 上了。如果你正在搭 agent 产品，eve 这套文件系统优先的设计思路值得看一眼。

智谱的 GLM-5.2 今天在圈子里传了一夜。开源权重，MIT 许可，1M 上下文窗口，两个推理档位。Riley Brown 已经发了教程教大家在 Cursor 里接入这个模型，通过 OpenRouter 走。但更有意思的是另一件事：智谱还发了一个叫 ZCode 的桌面 coding agent，Riley 直接说它是 Codex 的像素级复刻。界面长得一模一样，也支持从 Telegram 或 Discord 远程给 agent 派任务。区别在于底层跑的是国产模型，成本低得多。

有人觉得这是抄袭，也有人觉得这说明开源模型的能力差距正在急剧缩小。Aaron Levie 的观点是，如果开源模型只落后三到六个月，和落后好几年，会是完全不同的市场结构。目前看，开源阵营没有掉队。

Replit 的 Vibecon 大会昨天开幕了。Amjad 在现场宣布了两件事：Replit Agent 现在支持语音输入，手机端和桌面端都可以；另外 Claude Design 和 Replit 打通了，你可以在 Claude 里做设计，然后一键发到 Replit 生成可运行的应用。Amjad 的原话是"用 Claude 设计，用 Replit 交付"。同时 Anthropic 的 Claude Design 本身也更新了画布编辑功能，Robert Bye 说可以直接在画布上编辑、保持品牌设计系统一致性。设计到代码这条链路正在被压缩到几乎没有摩擦。

Anthropic 的 Fable 5 模型还在被美国政府卡着。WIRED 报道说，特朗普政府官员告诉 Anthropic，如果想重新发布 Fable 5，必须确保模型的护栏无法被绕过。安全专家说这做不到。Peter Yang 的评论很直接：把大家付了钱的模型还给用户。这个事我们已经聊过几次，今天没有实质进展，但 WIRED 这篇报道算是一个正式的媒体确认。

今天值得展开聊的，是设计师这个角色在 AI 时代到底变成了什么。

起因是 Peter Yang 发的一条推。他说他合作过的最好的设计师之一，现在头衔变成了 principal engineer。这个人要求匿名，但他现在 95% 的工作是在终端和 coding harness 里完成的。工作流是这样的：先让 AI 生成一个设计文档，再让 AI 生成组件，然后不断给反馈直到感觉对了。Peter 的结论是，这不只是设计师的新技能，而是任何 builder 的核心技能。你不需要放弃 Figma，但你必须学会这套流程。

Cursor 的设计师 Ryo Lu 几乎同时发了一条推，呼应了同一个话题。他说 Cursor 移动端最疯狂的事，是另一位设计师 rikcreation 用 Cursor 写了大部分真实代码。"头衔什么都不是，你直接造就行了。"Ryo 自己也是设计师出身，之前在 Notion 和 Stripe 做过设计，现在在 Cursor 带设计团队。他的立场很明确：设计师和工程师的边界正在消失。

Linear 的产品负责人 Nan Yu 给这个话题加了一个重要的区分。他说"taste"不只是审美品味，就像"design"不只是视觉设计。Paul Graham 谈品味的时候穿着工装短裤，他显然不是在谈裤子的品味。Nan Yu 说的是，圈子里一半的争论都是因为大家对"设计"这个词的定义不一样。有人觉得设计师写代码是越界，有人觉得这本来就是设计的一部分。

这三条线串在一起，指向同一个变化：设计师的工作界面正在从画布迁移到终端。不是说要扔掉 Figma，而是说"用代码直接表达设计意图"变成了一种效率更高的路径。Peter 提到的那位匿名设计师，工作流的关键一步是"让 AI 先生成设计文档"——他把设计决策先变成了文字，再变成组件，再通过迭代把 taste 注入进去。这个流程里，设计师的 taste 没有消失，只是表达方式变了。

对你的启发可能是这样的。如果你带设计团队，现在应该鼓励设计师至少学会用 AI coding 工具做原型。不需要成为工程师，但需要能把想法直接变成可交互的东西。如果你自己是设计师，Ryo Lu 和 Peter 说的那条路径——先写设计文档，再生成组件，再迭代——是一个可以今天就试的工作流。而 Nan Yu 的提醒也很重要：别在"设计师该不该写代码"这种定义问题上浪费时间，taste 本身才是稀缺资源。

再说几条快讯。

Unreal Engine 5.8 今天发布，实验性地支持 MCP 协议。这意味着游戏引擎可以直接接入 agent 工作流，你的 AI agent 可以操控 UE 里的资产和管线。

ADPList 的 CEO Felix Lee 发了一个 MCP 服务器，让你的 agent 能在 Claude 里直接帮你预约真人导师。告诉 agent 你在做什么，它会找到做过这件事的人，帮你约好通话。如果你在用 Claude 做项目，这个工具值得装一下。

Google Labs 的 VP Josh Woodward 转发了 Stitch 的一个案例。设计公司 Voltage 用 Stitch 在 24 小时内把一个客户项目从头脑风暴变成了可交互的多屏原型。客户本来只期待几张静态线框图。

Lenny 公布了接下来播客的嘉宾名单，包括 Google DeepMind 首席科学家 Jeff Dean、Codex 的产品和工程负责人 Andrew Ambrosino、Claude Code 的工程负责人 Fiona Fung、ChatGPT 生产力线的负责人 Tara Seshan、Anthropic 研究产品负责人 Dianne Penn，还有 Netflix 的 CPTO Elizabeth Stone。这阵容基本上把当前 AI 产品层的关键人物一网打尽了。

你最近有没有试过让设计师直接用 AI coding 工具出原型？效果怎么样？我们明天一早再见。拜拜。