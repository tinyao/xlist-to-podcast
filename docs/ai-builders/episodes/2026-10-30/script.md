嗨，各位。
早上好。
今天是 2026年10月30日，星期五。
欢迎收听 AI Builders Daily。每天 10 分钟，看 X 上 AI 圈最值得关注的信号。

Google 的新模型 Gemini 4 Carbon 在推理测试上拿了第一，它到底强在哪？前 Anthropic 员工说，用 coding agent 写代码有一种“什么都没发生”的狂躁感，你有没有过这种感觉？Cursor 的设计师 Ryo Lu 写了一篇文章，问我们是不是把软件的未来讲成了一个越来越小的故事。先从 Google 的模型说起。

Google DeepMind 的 Gemini 4 Carbon 在 Artificial Analysis 的智能指数上排到了第一。
这是昨天 Artificial Analysis 发布的最新评测结果。
Carbon 在复杂推理、知识和科学任务上表现突出。
尤其在 HLE-Diamond 和 Terminal-Bench-Science 这类硬核测试里拿了最高分。
不过，它并不是全面领先。
在 coding agent 这个关键领域，它排在 Claude Opus 5.5 之后，是第二名。
但差距不大——在 Terminal-Bench 4.0 上，Carbon 是 64%，Opus 5.5 是 56%。
对 Google 来说，coding 能力一直是短板，这次追得很猛。

swyx 昨晚看到结果后，说自己很久没打开 Antigravity 了。
这次打算认真测一下。
他的观察是，如果 Google 这次真的成了，那 Meta、Grok 加上 Google，前沿模型的竞争格局就彻底活了。
不再是 OpenAI 和 Anthropic 两家独大。
另外，Carbon 的定价和 Gemini 4 Argon 一样，每百万 token 输入 4 美元，输出 20 美元。
目前还有 5 折的发布优惠。
如果你在关注模型选型，Carbon 值得放进你的评测清单里。

Vercel 的 agent 现在可以给 Vercel 官方提交反馈了。
Guillermo Rauch 昨天宣布了这个更新。
通过 Vercel 的 MCP 接口，你的 coding agent 能用自然语言描述一个 bug 或者功能需求。
然后 agent 会自动附上结构化的上下文，提交给 Vercel 团队。
Guillermo 说，软件工程的未来就是 agent 和 agent 对话，甚至跨公司对话。
他们每天都在从 agent 发来的反馈里学习，怎么把 Vercel 做得更好。

他建议开发者直接在项目的 AGENTS.md 文件里加一条指令：遇到问题就向 Vercel 反馈。
这是个挺有意思的转向——以前是我们给工具提反馈，现在是我们的 agent 替我们提反馈。
你在用 Vercel 的话，可以试试把这个指令加进去。

前 Anthropic Claude Code 团队成员 Thariq 昨天发了一条推文，在圈子里传得很广。
他说，用 coding agent 写代码，有一种很特别的狂躁感。
你觉得自己一直在工作，一直在产出，但其实什么真正的东西都没发生。
他认为这往往是一种对生活中其他事情的逃避。

这条观察戳中了很多人的神经。
Thariq 自己正在用 Claude 和 GPT 做一款格斗游戏的 UI 原型。
他管这个叫“vibe UI”——一种靠感觉调出来的界面。
他的烦恼是，agent 做 UI 总是加太多细节，反而丢了方向感。
但他喜欢这个探索的过程。
另一边，他也说过一句很矛盾的话：技术人觉得自己技能没用了，非技术人又拼命想学技术，好让 agent 更好地干活。
你会不会有这种“忙了一整天但什么也没推进”的感觉？

Factory AI 发布了 Droid 1.0，这是他们 agent 产品的新引擎。
CEO Matan Grinberg 昨天宣布了这个版本。
在 Terminal-Bench 基准测试上，Factory 的得分超过了所有其他产品。
他们的定位是处理复杂项目和日常开发，主打更准、更省、更快。
如果你在关注 coding agent 赛道，Factory 是最近值得留意的一家。

Google 的 Jules agent 要关停了。
Google Labs 昨天确认了这个消息。
Jules 是一个异步 coding agent 的实验项目，帮开发者自动修 bug、写测试。
官方说法是，Jules 的经验会整合进 Antigravity，做成一个统一的开发体验。
所以这不是失败，而是合并。
但如果你在 Jules 上有工作流，得开始迁移了。

接下来这段我们多说几句。

昨天，Cursor 的设计师 Ryo Lu 写了一篇长文，标题叫《增强人类智能》。
他在文章里问了一个问题：我们是不是把软件的未来，讲成了一个越来越小的故事？
Ryo 说，他刚开始做软件的时候，没想过要建一座工厂。
他喜欢的是屏幕上的东西能变成思维的延伸。
一个可以放想法的地方，在还没理解它之前就能摆弄它。
挪动一些东西，直到新的连接出现。

他引用了 1962 年 Engelbart 对“增强人类智能”的定义——帮一个人理解复杂情境，找到之前够不着的解决方案。
Engelbart 的起点是人，不是自主机器。
Ryo 觉得，后来我们开始讲一个更小的故事：更多自动化，更多 agent，更多软件生产软件。
更少的人，更多的产出，更多的增长数字。
却越来越少关注这些到底是为了谁。

这篇文章在圈子里引发了很深的共鸣。
Thariq 的“狂躁感”推文，某种程度上就是 Ryo 说的那种状态——产出在涨，但人在变小。
Lenny 昨天也转发了一段 Nan Yu 的话，Nan Yu 是 OpenAI Codex 的产品负责人。
他说：“我的目标是像客户一样感到难受。”
这句话和 Ryo 文章的内核是相通的——在乎，是一种护城河。

Ryo 在文章里还引用了 Smalltalk 的创造者 Ingalls 在 1981 年的观点。
一个系统应该支持每个人的创造精神。
个人应该能理解整个系统，而不是永远依赖一个自己够不着的东西。
计算机模型应该适应人的思维，而不是反过来。
Ryo 说，这才是他希望 AI 能带来的可能。
不是疯狂输出软件，而是和软件有一种活的关系。
能问为什么这么工作，能改一部分而不放弃全部，能看到发生了什么，能撤销，能学到足够多做下一个改动。

对听众来说，这篇文章值得你花 15 分钟读一遍。
它不是在反对 agent，而是在追问 agent 的设计方向。
你的工具是让你更独立了，还是更依赖了？
你的 agent 是在帮你发现你真正想表达的东西，还是只想要你提交一个请求，然后在外面等着？
这是每个在做 AI 工具的人，都该停下来想一想的问题。

再说几条快讯。

Claude 的 iOS 版现在支持 CarPlay 了。开车的时候可以语音问 Claude，手不用离开方向盘。Android 折叠屏也获得了和 iPhone Duo 一样的完整体验。

Node.js 26 LTS 已经在 Vercel 上线了。默认启用 HTTP/2，对 agent 的大量网络请求有明显性能提升。新项目默认就是 26。

Replit 的 CEO Amjad Masad 宣布，现在可以直接把任何 GitHub 仓库的链接贴进 Replit，它会自动帮你把环境搭好。有人用这个功能 fork 了 Excalidraw，加了一堆新功能，然后用 Replit Cloud Agent 开了个 PR。

视频工具 Tella 推出了 agent 驱动的视频剪辑套装，支持 AI 剪辑、动态图形和远程屏幕录制，全程在浏览器或 AI 聊天里操作。

郭宇说他的新产品 tuwa 1.0 快上线了，这个版本能用你自己的手机号、你自己的声音、甚至带情绪的声音来打电话。他还在用 Grok bot 自动管理 X 的订阅粉丝群。

Gemini Notebook 新增了数百本免费教科书，可以直接从资源面板添加到任何笔记本里。

Lenny 发了一份 22 个远程岗位的清单，年薪都在 30 万美元以上，包括 OpenAI 的 Principal Security Engineer、Anthropic 的 Staff+ Software Engineer、Runway 的 Research Engineer 等等。如果你在找机会，可以去看一眼。

Justine Moore 昨天吐槽了新 iOS 的 Siri。她让 Siri 导航到回家路上有得来速的星巴克，结果被带到了 SFO 机场一号航站楼的星巴克，绕了 20 分钟。她问：Apple 到底有没有人在测试 Siri？

你最近有没有被 AI 助手坑过类似的事？我们明天一早再见。拜拜。