嗨，各位。

早上好。

今天是 2026年04月02日，星期四。

欢迎收听 AI Builders Daily。每天 10 分钟，看 X 上 AI 圈最值得关注的信号。

Claude Code 把整个终端渲染重写了一遍，这件事比看起来重要。红杉发了一张让所有人转发的图——超过 1 万亿美元的服务市场，正在被 AI agent 接管。Aaron Levie 在 axios 那件事之后写了一段话：AI 生产力没有免费午餐。先从最技术的那件事说起。

Claude Code 把终端渲染整个重写了，新模式叫 NO_FLICKER。Anthropic 团队的 Boris Cherny 昨晚宣布了这个实验性渲染器。启用方式是把环境变量 CLAUDE_CODE_NO_FLICKER 设为 1。

这件事的难度需要解释一下。终端只能用 ANSI 转义码画字符——它没有「把光标移到屏幕外」这种指令。传统 app 想重绘超出视口的内容，只能清掉整屏再重画——这就是大家平时看到的闪烁。

Boris 的方案是把整个 viewport 虚拟化，自己接管键盘和鼠标事件。好处很直接：不再闪烁、不再跳动、内存和 CPU 在长对话里也保持稳定。鼠标点击在终端里也能用了——你可以点输入框移光标，也可以滚轮翻历史。

代价也很具体。原生 cmd-f 不能用，得按 ctrl+o 加斜杠搜索；原生复制粘贴逻辑也变了，选中默认自动入剪贴板，可以在 settings.json 里改回 ctrl+c。

为什么这件事比看起来重要。Claude Code 是 Anthropic 自己的旗舰开发产品——渲染器这种底层重写一次成本极高，团队愿意做，意味着他们认为现在的终端体验就是不够好。这背后是 Anthropic 把 CLI 当一等公民的态度。

同事 Thariq 特意补了一句：不是愚人节玩笑。4 月 1 日发布的产品确实让人本能怀疑，但这是真东西，Anthropic 内部用户大多数已经更喜欢这个新渲染器。

同时 Claude Code 团队的 cat 也补了一段。她说她经常在手机 App 上发想法，回笔记本再继续——CLI 现在支持把 session 直接 teleport 到本地。这条更新和 NO_FLICKER 放在一起读，是一个信号：团队在认真对待重度用户的工作流。

如果你是 Claude Code 重度用户，今晚就可以把这个环境变量打开试一下。生产环境再等一两个迭代。

另一件值得放在一起说的事——企业级 agent 的真正天花板，被一句话点破了：「AI 生产力没有免费午餐。」

写下这句话的是 Box CEO Aaron Levie。背景是过去 48 小时的两件事：axios 被植入后门、Claude Code 源码疑似泄露。

他的核心观点是这样。Agent 带来的生产力提升，最终会被卡在安全、合规、治理这些环节上。企业不会真的让 agent 在所有数据上为所欲为——审查能力和监管兼容，才是真正的速率限制。

他还有一个更具体的判断。每多一个 agent，企业的 governance 成本不是线性增加，而是指数上升——你不只要审查它写的代码，还要审查它访问哪些数据、调了什么 API、有没有越权。

Aaron 用了一个挺尖锐的说法：之前我们对企业愿意 vibe code 多少东西，是「住在童话世界里」。这话从一个企业级软件 CEO 嘴里出来，分量不一样。

「童话世界」这个比喻，背后是一个具体的失败模式。过去半年很多创业公司发了 demo，让企业 CEO 在台上 vibe code 自己的内部工具——但这些 demo 距离真正部署，要走的合规路径完全不一样。Aaron 在意的，正是这种 demo 与生产之间的距离，被低估了。

做企业产品的，今天的功课很具体。你的 agent 能力，怎么对接客户已有的治理框架——这不是要不要做的问题，是早做晚做的问题。

换个方向。Cloudflare 在愚人节发布了一个产品，不过底下的技术架构是真的。产品名叫 EmDash——号称是 WordPress 的精神继承者。

创业者郭宇昨晚分析了一下。传统 WordPress 的 plugin 直接执行任意代码——这也是 WP 历史上大量大规模漏洞的来源。EmDash 把所有 plugin 装进 V8 sandbox，叫 Dynamic Worker，每个都跑在隔离环境里。

这是 Cloudflare 之前推出 Dynamic Worker 时的延续。LLM 生成的代码是不确定的，而执行环境必须是确定的。你不能假设 agent 写的代码没问题，所以底层必须是隔离的。

这种隔离沙箱思路，最近半年在 agent infra 圈里越来越是共识。E2B、Modal、Daytona 这些 sandbox 公司都在做类似的事——只是 Cloudflare 把它直接绑到 Worker 平台上，让 plugin 开发体验和写 Worker 一样简单。

这件事的意义不在 WordPress 本身——而在它示范了一个方向：下一代平台需要的，是一个能跑陌生代码、又不会爆炸的沙箱。如果你在搭 agent 工具链，今天值得花十分钟看一下 Dynamic Worker 的设计思路。

接下来这段我们多说几句。

红杉昨晚发了一篇博客，标题叫《Services is the new software》——服务即软件。配的那张图，把超过 1 万亿美元的服务市场切成了几十格。每一格——法律、保险、客服、税务、人力——都对应着一个具体的 agent 替代场景。

这张图在圈里传了一整夜。不过比图本身更有意思的，是同时出现的两个完全相反的判断。

Greg Isenberg 写了一份长文，列了他「睡不着觉的 14 件事」。第一件叫 ambient business——agent 监控市场、处理客户，创始人几天检查一次。他说七八位数年收的公司，可以接近零日常人工。

另外两个判断更尖锐。SaaS 定价正从 per seat 翻向 per result——他认为光是把存量 SaaS 转成 outcome-based pricing 这一件事，就能做出十亿美元生意。Vertical AI 替代的 headcount 市场，是过去 vertical SaaS 的十倍。

他还提了一个挺反直觉的观察。「ghost team 组织架构」正在成型——两个真人加十二个有名字、有头像的 agent，about 页面外人看不出来。「1000 真粉丝」也变成「100 真粉丝」——agent 把成本压得足够低，100 个客户每月 500 美元，就是一个真实的单人生意。

不过 Box CEO Aaron Levie 在同一个晚上说了相反的话。他说我们对企业愿意 vibe code 多少东西，是「住在童话世界里」。Agent 会被安全、合规、治理这些环节卡很久。

这两个声音放在一起，描述的是同一件事的两面。消费端和创业公司层面，Greg 的预测正在以接近实时的速度发生——「一个小时建一家公司」不是夸张。但企业级——涉及客户数据、合规、安全的部分——会在 Aaron 描述的 governance 层卡很久。

顺带说一个佐证。Gumroad 创始人 Sahil Lavingia 昨天宣布把 CEO 职位交给一个叫 Gumclaw 的 AI agent——它接管 devops、客服、营销。仅在 4 月 1 日当天，Gumclaw 就关掉了 251 个客服工单，比团队所有人手动关掉的还多。

Sahil 自己点破了一个细节。本来想用愚人节当幌子发布，但 Gumclaw 已经在干。Lenny 转发评论：这是未来的样子。

不过请注意。Gumroad 是 SaaS 产品本身，目标客户主要是创作者和小生意人——不是 Fortune 500。它正好落在 Greg 的世界里。

再给你一个对照。Linear 的产品负责人 Nan Yu 今天分享了一个例子：他们公司的销售自己做了一个 Linear Agent skill，不需要工程师参与。

这是 Greg 的世界——agent 让非技术岗也能造工具。不过同一个产品想进 Fortune 500 客户，Linear 还是得过 SSO、SOC 2、合规审查。这就是 Aaron 的世界。

怎么判断你在哪个世界？三个问题。第一，你的客户能不能直接刷信用卡，还是必须走采购流程？第二，你的产品能不能让普通员工 5 分钟跑通，还是必须让 IT 部门集成？第三，出了问题谁负责，是你还是客户的合规部门？

如果三个答案都偏前者，你在 Greg 的世界。如果都偏后者，你在 Aaron 的世界。中间地带——那才是真正的难题。

所以今天问的不是「服务即软件这件事是真是假」。要问的是：你做的那块，今天属于 Greg 的世界，还是 Aaron 的世界？消费端是天级别的卷，企业端是季度级别——两边的打法完全不一样。

再说几条快讯。

Google AI Studio 今天上了一批 QoL 更新——playground 保存临时聊天、两步把 chat 转成 app、移动端 vibe coding UI 简化、新增 STT 按钮。Google AI Studio 的 Logan Kilpatrick 特意点了一句：这些更新都是用 Gemini 自己做的。

OpenAI 内部模型解出了三个 Erdős 未解之谜，论文已经发出来。OpenAI 的 VP Kevin Weil 的观察是：AI 不光在解题，证明本身也变得更优雅。

ADPList 的 CEO Felix Lee 第 140 天 vibe coding——昨天他完全跳过 Figma，用 Claude Code 加 Pencil，一个 prompt 做出一个 Robinhood 风格的界面。如果你是设计师，这套工作流值得花一晚试。

另外一个使用技巧。a16z 的 Justine Moore 提醒：很多时候 agent 说「我做不到」，你只需回一句「我不管，想办法」，它就做出来了。下次卡住可以试一下。

最后一条。老朋友 swyx 看了 Codex 的增长数据，发现 3 月几乎是平的——前面两周还在 +40 万。郭宇也提到第一次在 Codex 上看到「Selected model is at capacity」的提示。你最近用 Codex 有没有遇到限额？

今天最值得花十五分钟做的事：去 Claude Code 试一下 NO_FLICKER 模式。然后给自己问一个具体问题——你做的产品，governance 这块准备好了吗？

我们明天一早再见。拜拜。