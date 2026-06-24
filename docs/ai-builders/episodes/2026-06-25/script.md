嗨，各位。
早上好。
今天是 2026年6月25日，星期四。
欢迎收听 AI Builders Daily。每天 10 分钟，看 X 上 AI 圈最值得关注的信号。

今天我们来聊聊：Notion 和 Cursor 的深度绑定，这会对你的工作流意味着什么？Greg Isenberg 说 AI 员工要有自己的账号，这个想法到底有多疯？Vercel 的 CEO 开了一个秘密群组，他想从 agent 开发者那里得到什么？先从最让工程师睡不着的那件事开始。

Notion 正式把 Cursor 和 Claude 拉进了你的文档里。
昨天在 Figma Config 大会期间，Notion 和 Cursor 的设计师 Ryo Lu 同步宣布了这个更新。
准确说，是两条线同时打通了。
在 Notion 里，你现在可以像 @ 同事一样直接 @ Claude 或 Cursor，让它们完成任务。
反过来，在 Cursor 编辑器里，你也可以直接访问 Notion 的文档和团队知识库。
Ryo Lu 的原话是"use cursor in notion, use notion in cursor"。
这不再是那种需要你手动复制粘贴的松散集成，而是把 coding agent 直接嵌进了协作工具的核心。

同一时间，Notion 还宣布了一个叫 External Agents 的功能。
Claude 和 Cursor 会以外部代理的身份加入你的 Notion 工作区。
你可以从团队共享的看板里给它们分配任务，看它们跑完整个流程。
这对团队意味着什么？你的 sprint 计划和代码实现，第一次被放在同一个上下文里，由同一个 agent 来回切换。
如果你团队里还有人不习惯在 IDE 里看需求文档，这个更新基本上把最后那层隔阂打掉了。

说到 agent 和工具的深度集成，Claude Tag 今天也正式上线了。
Anthropic 给 Claude 在 Slack 里开了一个正式工位。
你可以直接在频道里 @Claude，像分配任务给同事一样让它干活。
Box 的 CEO Aaron Levie 马上跟进了一条推文，说现在 Claude 能直接访问 Box 里所有你授权的企业文件。
这意味着什么？你公司的合同、设计稿、产品文档，全变成了 Claude 随身携带的知识库。
Aaron 管这叫"无头软件的威力"——agent 不需要 GUI，它只需要一个 API 端点和你给它的权限。
Greg Isenberg 对这个趋势的观察更激进一些，我们待会儿深聊。

另一件值得说的事。Google 开除了那个给 Workspace 写 CLI 工具的人，原因是他写了那个工具。
这件事在圈子里传了一夜。
开发者 Justin Poehnelt 之前在 Google 工作，他做了一个非官方的 Google Workspace CLI，叫 gog。
上线后冲到 Hacker News 第一，几天内拿到几千个 GitHub star 和大量真实用户。
然后 Google 的法务部门介入，质问他为什么在 Google 的代码仓库里用了 Google 的 logo 和品牌色。
两天前 Google Cloud Next 刚宣布要做官方 CLI，两天后 Justin 就被裁了。
Justin 自己发了一篇长文复盘，说这不是针对他这个工具，而是 Google Workspace 内部对 agent 化的一种深层恐惧。
OpenClaw 的作者 Peter Steinberger 转发了这件事，说"还好 Google 没法开除我"。
这件事的讽刺感太强了——一个工程师用业余时间证明了 CLI 的需求，公司先否认、再跟风、最后把人踢走。
如果你在大厂做 side project，这条新闻值得你品一品。

接下来这段我们多说几句。
今天 Greg Isenberg 对 Claude Tag 的评论，把"AI 员工"这个话题推到了一个非常具体的想象空间里。
他认为，未来的工作形态不是你去 prompt 一个工具，而是你给一个 agent 开它自己的账号。
它有自己的邮箱、自己的 Slack 登录、独立的工位。
你 delegate 任务给它，就像 delegate 给一个同事。
它会写代码、回邮件、做 PPT，甚至自己上 X 刷信息。
最妙的是他的观察：第一周你还会觉得在 Slack 里谢谢一个 bot 很奇怪。
到第三周，它回复慢了，你就会像催同事一样催它。
那个账号让你的大脑自动把它归档到"人"那一栏，你的期待值也跟着变了。

Greg 还列出了几个二阶效应，挺值得展开想想的。
第一，公司会开始像招人一样"招聘" agent，有 JD、有 onboarding、有绩效评估。
第二，一个在你公司待了两年的 agent，比任何新人都值钱，因为它脑子里装着所有决策、所有线程、所有关系，而且永远不会离职。
第三，IT 和安全部门会疯掉，因为每个 agent 账号都是一个新的入口，还没人想清楚 agent 被钓鱼或者失控了该谁负责。
第四，一个黑市可能会形成——一个训练好的、带着几个月公司上下文的 agent 账号，会被拿来卖钱，就像今天养好的社媒账号一样。
第五，你的组织架构图里会出现一堆不是人的名字，有一天你发现半个团队都是 agent，而且你完全没法想象没有它们怎么运转。

这不是一个遥远的趋势。
Greg 自己说，他的合伙人已经 bootstrapped 了一个 Slack agent 专门做营销。
他预估这个方向可能有超过一千个垂直的、年收入百万美元的机会。
他的结论是：Slack tag 很酷，但这周你就该给一个 agent 开它自己的账号。
看你的大脑多快就不再把它当软件看。
整个范式转换，你大概三天就能感觉到。

坦白说，Greg 的框架里最有意思的一点，不是技术，而是心理。
他把 agent 的采纳曲线，从"功能评估"直接拉到了"社会关系建立"。
这跟过去我们评估 SaaS 工具的逻辑完全不一样。
你不是在比哪个 agent 的代码生成更快，你是在比哪个 agent 更"像你的同事"。
这可能是接下来 agent 产品设计里最被低估的一个维度。
你怎么看？你会给你的 AI 同事开一个独立账号吗？

再说几条快讯。
Vercel 的 CEO Guillermo Rauch 今天开了个 X 上的私密群组，专门收集对 eve 框架的高质量反馈。
他说，如果你在深度搭建 agent，有挑剔的需求或者关键意见，直接 DM 他，他会把你拉进一个和 eve 工程师直接聊的群。
这个群的门槛不低，但从另一个角度看，Guillermo 是在用最直接的方式给 Vercel 的 agent 框架找第一批重度用户。

GLM 5.2 Fast 版今天在 Vercel AI Gateway 独家上线了。
Guillermo 说内部 benchmark 显示它的 token 吞吐比别家快了一倍。
swyx 补了一个背景：智谱今年一月已经在香港上市，股价 120 港币。
现在 GLM 在开源模型榜单上压过了 DeepSeek，团队带着"世界第一开源模型"的姿态回到旧金山参加 AI Engineer World's Fair。
如果你在考虑企业级的中文模型选型，GLM 这条线值得重新看一眼。

Databricks 的联合创始人 Matei Zaharia 和 Reynold Xin 上了 Latent Space 播客。
swyx 说这期料很足——他们解释了为什么 Databricks 在 agent 基础设施层下注、为什么 Omni gent 要做一个共享 harness、以及为什么 agent 安全需要上下文感知的策略和消费控制。
这期播客里还有一个直球回答：Databricks 为什么赢了 Snowflake。
如果你在思考企业 agent 平台的基础设施该怎么搭，这期值得放进队列。

Figma 今天在 Config 大会上发布了 Figma Motion。
这是 Figma 正式进入动效设计领域。
对设计师来说，这意味着不用再切到 After Effects 做交互动画。
Riley Brown 的反应是"Very cool"。

CapCut 宣布了一个 AI 电影节，20 万美元奖金，获奖作品会在今年一个大电影节上放映。
如果你在做 AI 视频创作，这算一个值得关注的出口。

Anthropic 的内容设计负责人 Chelsea Larson 今天在 Figma Config 做了一个分享。
Zara Zhang 在现场记了笔记，说这是她今天最喜欢的一场。
如果你在做 AI 产品的 UX writing 或者内容策略，Zara 的笔记链接值得翻一翻。

最后一条。
Justine Moore 分享了一个 vibecoded 游戏——一个劈柴模拟器。
创作者用 3D 扫描了自己院子里的木头，录了自己劈柴的动作和声音，然后用 AI 渲染出来。
Justine 说"insanely satisfying"。
这大概是今天最纯粹的一个"用 AI 做点好玩的东西"的例子。
如果你手痒想试试，链接在 shownotes 里。

我们明天一早再见。拜拜。