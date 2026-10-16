嗨，各位。
早上好。
今天是 2026年10月17日，星期六。
欢迎收听 AI Builders Daily。每天 10 分钟，看 X 上 AI 圈最值得关注的信号。

Anthropic 把 Code Review 推到正式版，Boris 说它已经是团队速度和质量的双重秘诀。Vercel 给 libfx 装了 durability 层，手机扔进黑洞也能把 prompt 跑完，这是怎么做的？Greg Isenberg 发现 agent 工具在快速垂直化，哪几个方向已经在赚 27 万 5 千美元 MRR？先从最让你睡不着的那件事说起。

Anthropic 把 Code Review 推到了正式版。Team 和 Enterprise 计划都能用了。Claude 团队的 Boris Cherny 昨天说，自己已经离不开这个功能了。

每个 PR 都会自动跑 Code Review。几乎每个 bug 都能在上线前抓到。管理员可以给每个 repo 选 Quick、Standard 或 Deep 三档深度。

Boris 说这正是团队快速迭代、同时把质量标尺拉高的秘诀。同一天他还推了 Claude Slides。做 deck 的时候，一句话就能让 Claude 生成幻灯片。

Boris 说他再也不用去搜 iPhone 边框 SVG 了。如果你在 Team 或 Enterprise 计划里，今天就把 Code Review 接进核心 repo。或者用 Claude Slides 做一次月度汇报。

另一件值得说的事。fx 发布了 v0.0.14。libfx 现在开箱就支持 durable。Guillermo Rauch 昨天宣布了这个更新。

同一个 createFxAgent 调用，在笔记本或云端都能持久运行。agent 需要长时间算力。但也得能容忍重启、重新部署、超时、崩溃。

具体来说，用户发一个 prompt，然后手机被扔进黑洞，这个 turn 还是会跑到完成。如果进程在工具调用中途崩溃，它就从那里恢复。

实现上，libfx 引入了一个简单的 durability adapter API。在 Vercel 上，一行代码就能用上 durable workflows 和 queues 的基础设施。Guillermo 说接下来会把同样的 durability 带给 Pi、OpenCode 和自定义 harness。

如果你在做生产级 agent，这个 durability 层值得参考。你的 agent 现在能扛住进程重启吗？

换个方向。Perplexity 把 pplx-decider 升级到了 v1.2。同时发布了一个 flash 版本。CTO Denis Yarats 昨天宣布了这个更新。

新模型在文本和视觉上的表现都提升了。训练计算和数据集规模显著增加。还多了 reranking 能力。推理速度最高提升 5 倍，一次请求里的所有问题只跑一轮。

flash 是 40 亿参数的小模型，专做超快推理。另外，模型引入了 slug。pplx-decider-latest 永远指向最新版本。每个新 checkpoint 都不会在之前能力上倒退。

如果你在用 pplx-decider 做决策或排序，可以直接切到 latest。精度优先就选 v1.2，速度优先就选 flash。

说到个人工具，今年第 19 款产品 sofatap 开始 TestFlight 公测。作者是独立开发者郭宇。

这是一个开源的 iPhone 工具。它把手机变成触控板和键盘。躺在沙发上就能操作电视上的电脑。

场景很具体。他在客厅用电视连电脑跑 vibe coding。agent 在跑任务，他想窝在沙发上看剧打游戏。但要操作电脑就得起身找键盘鼠标。

sofatap 用 iPhone 扫电视上的二维码就能配对。滑动控制光标，轻点操作，双指滚动。支持 Mac、Windows、Linux。还支持索尼和小米的 Google TV。

如果你有类似的客厅办公场景，这个工具可以试试。你目前怎么处理人不想离开沙发、电脑却要操作这个断点？

先把节奏放慢一点，说一下今天最值得想清楚的一件事。

Greg Isenberg 昨天看到 Postiz 的数据。MRR 27 万 5 千美元，1433 个活跃试用，8052 个客户。Postiz 的创始人 Nevo David 说，自己总能找到竞争对手不去的获客渠道。

Greg 把这类生意归成三类。卖给 agents，喂 agents，或者给 agents 提供住所。然后他列了六个方向。

数据经纪，是把稀有专家知识卖给 labs 和训练 agent 的公司。agent 托管，是租常开电脑，让人 24/7 跑 agent。计算转售，是批量买 GPU，再按小时租给小团队。

垂直 harness，是专为某一行业某一工作流做的 agent。比如保险理赔、建筑投标。技能，是把打包好的能力卖给别人。

代客 agent 设置，是帮本地商家搭 agent。就像当年帮他们建网站。

同一天 swyx 也提到 Compute Trading。Jump 和 DRW 这样的做市商开始进入 emergent compute market。他们当年在数字资产上押注，现在在算力上押注。

这跟 Greg 说的计算转售方向高度呼应。

如果你是一个工程师或创业者，这六个方向里，你离哪个最近？数据经纪需要你有特殊数据源。agent 托管需要运维能力。

计算转售需要批量采购渠道。垂直 harness 需要行业知识。不要试图做一个通用工具。

找一个你已经了解的工作流，把它做深。或者换一个问法，你手里的哪个技能可以打包成 agent 技能卖出去？

再说几条快讯。

Reflection 的 Beam 模型现在在 Vercel AI Gateway 上免费。这个美国产的开源模型之前以 stealth/cat-jam 的名字跑了很久。Guillermo 说，把它接进 eve agent 或者 fx 就能开始用。

Vercel Shop 昨天正式 GA。这是一个基于 Shopify 和 Next.js 的商店前端，agent-ready 开箱即用。Vercel 自己的 merch 商店已经在用它。

Nick Cammarata 发了一篇关于可解释性的长文。他说自己从悲观转向了乐观。Sam Altman 转发了并说很高兴看到这个。

Lenny 分享了 Stripe 设计负责人 Katie Dill 的演讲。主题是别把做完了和做得好混为一谈。

如果你今天只做一件事，建议你打开 Code Review 跑一次 Deep 审查，看看它到底能抓到什么。我们明天一早再见。拜拜。