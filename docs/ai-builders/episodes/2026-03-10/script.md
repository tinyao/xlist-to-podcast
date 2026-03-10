今天是2026年3月10日，欢迎收听 AI Builders Daily。

今天有三件事值得你认真听：Karpathy 的 AI 自动调参实验刷新了我对「AI做研究」的认知；Claude Code 推出了多智能体 Code Review，Anthropic 内部工程师效率直接翻倍；还有 Google 的 Pomelli 正式面向全球开放。我们开始。


第一个话题，Karpathy 的 autoresearch 实验。

这件事我觉得是过去 24 小时里信息密度最高的一条。

Karpathy 上周让一个 AI agent 自主运行了大约两天，对他的 nanochat 项目做超参数调优。结果怎么样？agent 自己跑了大概 700 次实验，找出了 20 个能真实改善模型表现的改动，把他那个「Time to GPT-2」的 benchmark 从 2.02 小时压到了 1.80 小时，提升了大约 11%。

更有意思的是他发现了什么。agent 找出来的问题，都是 Karpathy 自己没注意到的真实 bug。比如他的 QKnorm 没有加缩放系数，导致 attention 太分散；Value Embedding 缺了正则化；AdamW 的 beta 参数也乱了。这些不是什么天才发现，但它们是真实的、可叠加的改进，而且 Karpathy 自己调了那么久都没发现。

Karpathy 说，他做神经网络训练调优已经二十年了，这是他第一次看到 agent 把这整套工作流——想点子、跑实验、看结果、再想新点子——完全端到端地自己跑下来。他用的词是「wild」，有点震撼的意思。

他还说了一段很有意思的话，大意是：所有前沿 AI 实验室都会走这条路，这是「最终 boss 战」。你搭一个 agent 群，让它们协作调小模型，把最有希望的改动推到更大规模去验证，人类只在边缘做贡献。他的判断是，这「只是工程问题」，它就是会 work。

我想在这里多说一句。Karpathy 说的这件事，和「AI 写代码」不是一个量级的事情。写代码是执行，这里说的是 AI 在做科研里最核心的那个循环——假设、实验、迭代。它还不是「突破性研究」，但它已经在做真实有效的工作了。如果这个方向继续走下去，AI 实验室的研究员和工程师的工作方式会发生根本性的变化。这条推文的收藏量超过 2500，在技术圈引发了大量讨论，值得你去读原文。


好，我们来看第二个话题，Claude Code 的 Code Review 功能。

Anthropic 今天正式发布了 Claude Code 的 Code Review 功能。逻辑很简单：每次你开一个 PR，Claude 会自动派出一组 agent，专门来找 bug。

听起来好像不算什么大新闻，但有几个细节值得注意。

第一，这是 Anthropic 内部先用的。负责 Claude Code 的工程师 Boris Cherny 说，Anthropic 内部工程师今年的代码产出已经提升了 200%，而 Code Review 是那个瓶颈环节。他自己用了几周，说确实抓到了他自己不会注意到的真实 bug。

第二，反馈异常好。另一位 Claude Code 团队成员 Alex Albert 说，这个功能在 Anthropic 内部顶级工程师里获得的好评，是他很少见到的。这不是营销话术，而是一个内部人员在说「我们自己都在用，而且真的好用」。

第三，多 agent 做 review 这件事本身有点意思。不是一个 Claude 看一遍，而是一个团队的 agent 分工来找问题。这在架构上和 Karpathy 说的 agent 群协作是同一个方向——单个 agent 的上限有限，但多个 agent 协作可以覆盖更多角落。

说到这里，你可能注意到今天有一个贯穿的主题：agent 不再只是「帮你写代码的工具」，它开始承接整个工作流里的质量控制环节。从 Karpathy 的自动调参，到 Claude Code 的自动 review，agent 正在接管「检查和迭代」这件事。这个转变，我觉得比「AI 写代码更快」要深刻得多。


第三个话题，我们来聊一个有意思的信号：OpenClaw 在深圳开了实体展厅。

这条消息是 Peter Steinberger 转发的，他的反应就是三个字：「there's a store now?」

我觉得这个问号本身就很有意思。OpenClaw 是一个 AI coding agent 工具，它开实体店这件事，放在两年前你根本想不到。但如果你想想 Apple Store 的逻辑——让人摸到、感受到、在空间里体验——这其实是一个非常聪明的品牌动作。AI 工具的竞争已经卷到了线下体验层。

Peter Steinberger 这两天本人也在密集折腾 OpenClaw 和 Codex 的互联互通。他搭了一套 agent 互相调用的架构，让 Codex 可以通过 ACP 协议调用 OpenClaw，反过来也行。他还用 AI 来检测并屏蔽那些在推特上发 AI 垃圾内容的账号——用 AI 对抗 AI，有种赛博朋克的幽默感。

另外他今天还发布了 gogcli 0.12.0，这是一个把 Google 工作区工具全部搬进终端的命令行工具，支持 Docs、Sheets、Calendar、Forms、Slides 等等，可以用 brew 直接安装。这个工具的收藏量超过 1000，说明有不少人在认真把 Google Workspace 纳入自己的 agent 工作流。


快讯时间，我们快速过几条。

首先，Google 的 Pomelli 正式扩展到全球 170 多个国家和地区。这条消息的互动量非常高，收藏将近 2800。Pomelli 是 Google Labs 推出的一个 AI 工具，之前只在部分地区可用，现在全面开放。如果你之前没机会用，现在可以去试试。

另外，NotebookLM 现在支持上传 ePub 文件了。这是用户呼声最高的功能之一。NotebookLM 的 Editorial Director Steven Johnson 说，这意味着你可以把公共领域里成千上万本经典书籍直接导入，建立你自己的 AI 优先个人图书馆。对于喜欢读书、做研究的人来说，这个更新很实用。

顺带一提，a16z 发布了新一期消费者 AI Top 100 榜单。Lenny Rachitsky 提到了几个有意思的点：Perplexity 的排名比大多数人预期的高；removebg 居然是第 16 名最受欢迎的 AI 工具；Google AI Studio 的流量超过了 Lovable；前 20 名里有三个是 AI 聊天伴侣类应用；Google 一家在前 50 名里占了四个产品。这个榜单值得你去看看，里面有不少反直觉的数据点。

还有一条，swyx 发了一个很直白的观点：如果你现在能在 AI 工程领域做出一个类别领先的开源项目，市场的收购价大概是每个 AI 工程师 1000 万到 1 亿美元。他说你不需要想清楚商业模式，不需要 GTM，不需要融资，就是做出 AI 工程师想用的东西就够了。这句话背后是一个真实的市场信号：现在工具层的人才和项目，稀缺程度远超想象。

最后一条，Greg Isenberg 说 AI 会大规模增加「一人公司」的数量：1 个一人十亿美元公司，10 个一人十亿级公司，100 个一人亿级公司，以此类推。这个预测听起来很大胆，但结合今天聊的所有内容——agent 自动调参、agent 自动 review、agent 自动做内容运营——你会发现这不是科幻，而是已经在发生的事情。


好，今天就到这里。

如果今天只带走一个 takeaway，我会选 Karpathy 那句话：任何你关心的、能被高效评估的指标，都可以被 agent 群自动优化。这不只是关于 AI 训练的，这是关于你手头所有工作的。

感谢收听 AI Builders Daily，如果觉得有收获，记得订阅，明天见。