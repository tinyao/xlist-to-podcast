list_id: 2007466263661232466
fetched_at: 2026-04-08 23:19 UTC
total_tweets: 67
[tweet 1]
id: 2042017534816231486
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world @openclaw🦞
time: 2026-04-08T23:11:33.000Z
text: I'm working on character evals and noticed that Claude would constantly pick itself as #1, so I removed the model names from the judge and changed things. https://t.co/Y9SqqJSYRc
media: photo: https://pbs.twimg.com/media/HFa0GAsXMAA8v4-.jpg
metrics: like_count=48, retweet_count=3, reply_count=9, quote_count=3, bookmark_count=3

[tweet 2]
id: 2042017264078352567
author: Robert Bye (@RobertJBye)
author_bio: Product Manager at @AnthropicAI working on Mobile, Web, and Voice experiences. Board Member https://t.co/PYz00fw7RU. Jesus follower.
time: 2026-04-08T23:10:29.000Z
text: You can now customise your @claudeai iOS widgets to get to Claude Code and Dispatch faster. https://t.co/QwWYNOaXkh
media: video: https://video.twimg.com/amplify_video/2042017203856535554/vid/avc1/3840x2160/5eau-Aj1TYF1tkBX.mp4 | duration: 10s
metrics: like_count=12, retweet_count=2, reply_count=5, quote_count=0, bookmark_count=0

[tweet 3]
id: 2042010418454184325
author: GREG ISENBERG (@gregisenberg)
author_bio: I drop startup ideas daily. Host @startupideaspod. CEO: @latecheckoutplz we build companies like @ideabrowser, @meetLCA, @boringmarketer etc
time: 2026-04-08T22:43:17.000Z
text: this video is the CLEAREST explanation of how claude skills + AI agents work and how to use them
  
  most people set up an AI agent and wonder why it keeps disappointing them. 
  
  the context window is everything
  
  context is what the model assembles before it takes any action. think of it like everything the agent needs to read before it does anything. the quality of what goes in determines the quality of what comes out. the models are genuinely really good right now. claude and gpt are exceptional. the variable is almost always the context you give them.
  
  1. agent.md files are mostly unnecessary
  
  every single line you put in an agent.md file gets added to every single conversation you have with your agent. a 1000 line file is around 7000 tokens burning on every run. the model already knows to use react. it can read your codebase. save the agent.md for proprietary information specific to your company that the model genuinely cannot know on its own.
  
  2. skills are the actual unlock
  
  a skill.md file works differently. what loads into context is only the name and description, around 50 tokens. the full instructions only appear when the agent recognizes it needs that skill. so instead of 7000 tokens on every run you have 50. and the agent stays sharp because the context window stays lean. the closer you get to filling the context window the worse the agent performs, same way you perform worse when someone dumps 10 things on you at once.
  
  3. here is how to actually build a skill the right way
  
  most people identify a workflow and immediately try to write the skill. what you want to do instead is run the workflow by hand with the agent first. walk it through every single step. tell it what to check, what good looks like, what bad looks like. correct it in real time. once you have had a full successful run from start to finish, tell the agent to review everything it just did and write the skill itself. it writes a better skill than you will because it has the full context of what actually worked in practice not in theory.
  
  4. recursively building skills is how you go from frustrated to reliable
  
  when the skill breaks, and it will break, ask the agent exactly why it failed. it will tell you specifically what went wrong. fix it together in that same conversation. then tell it to update the skill file so that failure mode never happens again. ross mike did this five times with his youtube report generator. it now pulls from eight different data sources and runs flawlessly every single time without him touching it.
  
  5. sub agents are something you earn not something you set up on day one
  
  start with one agent. build one workflow. turn it into one skill. once that works add another. ross mike has five sub agents now covering marketing, business, personal and more. it took months to get there and every single one exists because a workflow proved it deserved to exist. the people who set up 15 sub agents on day one and wonder why nothing works skipped all the steps that make the thing actually run.
  
  6. your workflow is the thing the model cannot get anywhere else
  
  the model has been trained on everything. it knows more than you about most things. what it does not have is your specific process, your taste, your way of doing things. that is what skills capture. that is what makes your agent actually useful versus a generic one. downloading someone else's skill means downloading their context onto your setup and it will not work the way you want it to because it was never built around how you work.
  
  this is the clearest explanation of how agents actually work i have heard. @rasmic runs this stuff every single day and the results show it.
  
  full episode is now live on @startupideaspod where you get your pods
  
  people charge for this sorta stuff
  
  i give away the sauce for free
  
  i just want you to win
  
  watch
media: video: https://video.twimg.com/amplify_video/2042009435548139520/vid/avc1/1280x720/-ip0xIP0cBPAbkxY.mp4 | duration: 2125s
metrics: like_count=135, retweet_count=14, reply_count=11, quote_count=0, bookmark_count=311

[tweet 4]
id: 2042005754262208708
author: Thariq (@trq212)
author_bio: Claude Code @anthropicai.   prev YC W20, mit media lab.   towards machines of loving grace
time: 2026-04-08T22:24:45.000Z
replied_to: Thariq (@trq212)
  I want to do some streams where I work with non-technical people using Claude Code to figure out how they might be able to improve their process. 
  
  My feeling is that just a few tips could make a big difference in efficiency. Any mutuals interested?
text: would like to start with people I know already so we can get over initial awkwardness!
metrics: like_count=57, retweet_count=0, reply_count=9, quote_count=0, bookmark_count=0

[tweet 5]
id: 2042005305601425634
author: jenny wen (@jenny_wen)
author_bio: generalist, realist, escapist. designer.
time: 2026-04-08T22:22:58.000Z
text: 90% of baby clothing is designed to remind you of two things:
  
  - this is a baby
  - the baby’s gender
  
  what if the clothes were just like, regular clothes but small
metrics: like_count=29, retweet_count=0, reply_count=6, quote_count=0, bookmark_count=1

[tweet 6]
id: 2042005043289977232
author: Thariq (@trq212)
author_bio: Claude Code @anthropicai.   prev YC W20, mit media lab.   towards machines of loving grace
time: 2026-04-08T22:21:55.000Z
text: I want to do some streams where I work with non-technical people using Claude Code to figure out how they might be able to improve their process. 
  
  My feeling is that just a few tips could make a big difference in efficiency. Any mutuals interested?
metrics: like_count=679, retweet_count=33, reply_count=185, quote_count=2, bookmark_count=87

[tweet 7]
id: 2041996800761196820
author: Lenny Rachitsky (@lennysan)
author_bio: Deeply researched product, growth, and career advice
time: 2026-04-08T21:49:10.000Z
text: Breaking: Lenny's Newsletter subscribers will be getting a free year of @Cursor_ai, @GoogleAI Pro (w/ Gemini), @NotionHQ, @Supabase, @v0, @Gumloop, and @Fin_ai
  
  This is on top of the 25+ premium products that eligible subscribers already get free for a full year, including Lovable, n8n, Canva, Manus, Gamma, Granola, ElevenLabs, Factory, Devin, Linear, and Wispr Flow. 
  
  It sounds too good to be true, but it's not.
  
  If you’re already a paid subscriber, just keep an eye on your inbox—we’ll email you as soon as these new products go live.
  
  Not a paid subscriber yet? Now would be a good time to become one so you don’t miss out: https://t.co/R2KxWfAfdw
  
  An important note: Some products are available only to Insider-tier subscribers. In the new batch, Cursor, Google AI Pro, v0, and Supabase are just for Insiders. Insiders get exclusive deals, and priority access to all deals. And now is the best time to become an Insider: The Insider price will increase from $350 to $400 on April 14. If you’re already an Insider, you’ll keep your current price. If you want to lock in the current Insider price before the next wave goes live, upgrade before April 14: https://t.co/qg4QjS2JOn
  
  Explore all the amazing existing product deals here: https://t.co/FmhnTSGaoM
  
  A big thank you to all of our incredible partners for making this offer possible.
media: gif: https://video.twimg.com/tweet_video/HFag8mIa8AImtpd.mp4
link: https://www.lennysnewsletter.com/subscribe
link: https://www.lennysnewsletter.com/subscribe?plan=founding
link: https://www.lennysproductpass.com/
metrics: like_count=86, retweet_count=5, reply_count=13, quote_count=3, bookmark_count=58

[tweet 8]
id: 2041996329703092582
author: Peter Yang (@petergyang)
author_bio: I share extremely practical AI tutorials and interviews | Join 140K+ readers at https://t.co/XYKTmGVH14 | Product at Roblox
time: 2026-04-08T21:47:18.000Z
quoted: Aadit Sheth (@aaditsh)
  I'm excited to announce my new venture: The Narrative Company.
  
  Most exec content reads like ads. Ours doesn't.
  
  Over the last year, we've quietly worked with a handful of Fortune 500 clients on their X and LinkedIn content.
  
  But this isn't how it started.
  
  It started when I got a C in my English finals.
  
  I wasn't a natural writer. Nobody around me was doing what I was trying to do. So in college I spent six hours a day on Twitter. Writing. Deleting. Writing again.
  
  That turned into 1M+ followers across social.
  
  Somewhere along the way, a Fortune 500 CEO asked me to help run his social.
  
  Then another one did.
  
  The Narrative Company is the firm @arvkothari and I are building around that work. We write executive content that actually sounds like the executive.
  
  Most comms teams are built to avoid mistakes that were never going to happen. We're built for the opposite. Posts that get read, shared, and quoted in rooms you're not in.
  
  A few weeks ago, I found my old English paper and ran it through an AI model. It came back with an A 🤣
  
  If you're a CEO who'd rather be read than ignored, we'd love to talk.
  
  We're also hiring across SF and NYC for comms, sales, and engineering. Remote if exceptional.
  
  Kid who got a C is hiring.
text: Support my friend Aadit's new company - great name btw :) https://t.co/rc1WgqG5p1
metrics: like_count=0, retweet_count=0, reply_count=0, quote_count=0, bookmark_count=4

[tweet 9]
id: 2041993542290305469
author: Steven Johnson (@stevenbjohnson)
author_bio: Editorial Director, NotebookLM and Google Labs. Author of 14 books. Latest: The Infernal Machine. Speech inquiries email: wesn at leighbureau dot com
time: 2026-04-08T21:36:13.000Z
quoted: Josh Woodward (@joshwoodward)
  Most Al chatbots give you basic "projects." Gemini just built you a second brain. 🧠
  
  Introducing Notebooks: some of the magic from @NotebookLM, integrated directly into @GeminiApp.
  
  Here's what changes for you today:
  
  📚 Upload 100 sources for free
  
  📂 Organize your chats - the wait is officially over :)
  
  🔄 Sources, chats, and emojis sync
  
  People are using Gemini and NotebookLM in tandem, and we'll keep building both.
  
  To manage capacity, we're rolling this out NOW on the web and going from Ultra ➡️ Pro ➡️ Plus ➡️ Free. (Mobile, EU, and Workspace are up next!)
  
  With Google I/O right around the corner, we are just getting started. Enjoy!
text: Last year @NotebookLM introduced public/featured notebooks to share curated knowledge bases with the world. 
  
  Now we are making it easier for you to work with the knowledge you need by launching notebooks as a core organizational unit for Gemini. 
  
  Bonus for existing NotebookLM users: you can now save your Gemini chats as sources and read/query them in both apps. 
  
  These are just the initial steps towards making notebooks into a new AI-first container for knowledge. Next up: expanding the kinds of information you can store in your notebooks…
metrics: like_count=11, retweet_count=1, reply_count=1, quote_count=0, bookmark_count=6

[tweet 10]
id: 2041989206495653915
author: Peter Yang (@petergyang)
author_bio: I share extremely practical AI tutorials and interviews | Join 140K+ readers at https://t.co/XYKTmGVH14 | Product at Roblox
time: 2026-04-08T21:18:59.000Z
text: As much as I love using Claude Max and ChatGPT Pro, I don't think these all-you-can-use AI subscriptions will last forever.
  
  Here's my new deep dive that covers:
  
  → Why Anthropic cut off OpenClaw access
  → How to run local models on your Mac
  → What I'm seeing on the ground in China
  
  📌 Read now: https://t.co/cm9jYIZS8y
link: https://creatoreconomy.so/p/the-all-you-can-use-ai-subscription
metrics: like_count=19, retweet_count=0, reply_count=3, quote_count=0, bookmark_count=31

[tweet 11]
id: 2041982173402821018
author: Josh Woodward (@joshwoodward)
author_bio: VP, @Google @GoogleLabs @GeminiApp @GoogleAIStudio
time: 2026-04-08T20:51:02.000Z
text: Most Al chatbots give you basic "projects." Gemini just built you a second brain. 🧠
  
  Introducing Notebooks: some of the magic from @NotebookLM, integrated directly into @GeminiApp.
  
  Here's what changes for you today:
  
  📚 Upload 100 sources for free
  
  📂 Organize your chats - the wait is officially over :)
  
  🔄 Sources, chats, and emojis sync
  
  People are using Gemini and NotebookLM in tandem, and we'll keep building both.
  
  To manage capacity, we're rolling this out NOW on the web and going from Ultra ➡️ Pro ➡️ Plus ➡️ Free. (Mobile, EU, and Workspace are up next!)
  
  With Google I/O right around the corner, we are just getting started. Enjoy!
media: video: https://video.twimg.com/amplify_video/2041982091647410176/vid/avc1/1080x1080/KcLzemyIlbNnKF88.mp4 | duration: 34s
metrics: like_count=531, retweet_count=72, reply_count=51, quote_count=27, bookmark_count=169

[tweet 12]
id: 2041975669928702370
author: Aaron Levie (@levie)
author_bio: ceo @box - your business lives in content. unleash it with AI
time: 2026-04-08T20:25:12.000Z
quoted: Claude (@claudeai)
  Introducing Claude Managed Agents: everything you need to build and deploy agents at scale.
  
  It pairs an agent harness tuned for performance with production infrastructure, so you can go from prototype to launch in days.
  
  Now in public beta on the Claude Platform. https://t.co/vHYfiC1G56
text: Background agents for knowledge work are here. You can use the Box API or MCP to automate any content workflow with Box + Claude Managed Agents. In 2 minutes you can be automating document review processes, data extraction, or connecting content to other IT systems. Crazy times. https://t.co/zfIYubDJye https://t.co/opAihEGx2U
media: video: https://video.twimg.com/amplify_video/2041973444636487680/vid/avc1/1784x1080/xbXPdC6uHXTU-bhH.mp4 | duration: 148s
metrics: like_count=143, retweet_count=11, reply_count=16, quote_count=2, bookmark_count=150

[tweet 13]
id: 2041957973531226372
author: Guillermo Rauch (@rauchg)
author_bio: @vercel CEO
time: 2026-04-08T19:14:53.000Z
quoted: Vercel (@vercel)
  AI Gateway now supports team-wide Zero Data Retention (ZDR).
  
  Building safely with multiple AI models means wrestling with fragmented data policies, per-provider negotiations, and the hope that developers do not use non-complaint providers.
  
  AI Gateway changes this with team-wide ZDR.
  
  Gateway ensures your data requirements are automatically met by only routing to providers where we have negotiated ZDR agreements.
  
  Instead of managing policies provider by provider, you get one unified data policy across Claude, GPT, Gemini, and many more providers.
  
  Toggle it on in your dashboard, and all requests will route safely without touching any code:
    • Team-wide ZDR
    • Per-request controls
    • Disallow prompt training
  
  Move compliance to the gateway so your team can keep shipping ↓
  https://t.co/DkjoEzwASF
text: AI Gateway is quite literally a “peace of mind” product:
  ✅ No downtime
  ✅ No lock-in
  ✅ No keys 
  🆕 No training https://t.co/qdUrf4ds5s
metrics: like_count=141, retweet_count=10, reply_count=17, quote_count=1, bookmark_count=24

[tweet 14]
id: 2041956380429709453
author: Vercel (@vercel)
author_bio: Self-driving infrastructure for apps and agents.
time: 2026-04-08T19:08:33.000Z
text: AI Gateway now supports team-wide Zero Data Retention (ZDR).
  
  Building safely with multiple AI models means wrestling with fragmented data policies, per-provider negotiations, and the hope that developers do not use non-complaint providers.
  
  AI Gateway changes this with team-wide ZDR.
  
  Gateway ensures your data requirements are automatically met by only routing to providers where we have negotiated ZDR agreements.
  
  Instead of managing policies provider by provider, you get one unified data policy across Claude, GPT, Gemini, and many more providers.
  
  Toggle it on in your dashboard, and all requests will route safely without touching any code:
    • Team-wide ZDR
    • Per-request controls
    • Disallow prompt training
  
  Move compliance to the gateway so your team can keep shipping ↓
  https://t.co/DkjoEzwASF
link: https://vercel.com/blog/zdr-on-ai-gateway
metrics: like_count=66, retweet_count=3, reply_count=7, quote_count=3, bookmark_count=23

[tweet 15]
id: 2041953565300945096
author: Riley Brown (@rileybrown)
author_bio: Cofounder of @vibecodeapp_ (the #1 full stack vibe coding platform)
time: 2026-04-08T18:57:22.000Z
text: I’ve been following AI since mid 2022 (Dall e 2 and midjourney).
  
  What made this space so fun is anyone with $20-200 could be at the frontier. 
  
  This is what separated LLMs and diffusion models from most innovations in history. 
  
  Now, this is no longer true. 
  It’s just kinda… sad
metrics: like_count=123, retweet_count=7, reply_count=24, quote_count=0, bookmark_count=24

[tweet 16]
id: 2041941720611614786
author: Alex Albert (@alexalbert__)
author_bio: Research @AnthropicAI. Opinions are my own!
time: 2026-04-08T18:10:18.000Z
quoted: Claude (@claudeai)
  Introducing Claude Managed Agents: everything you need to build and deploy agents at scale.
  
  It pairs an agent harness tuned for performance with production infrastructure, so you can go from prototype to launch in days.
  
  Now in public beta on the Claude Platform. https://t.co/vHYfiC1G56
text: I've found Managed Agents to somehow be both the fastest way to hack together a weekend agent project and the most robust way to ship one to millions of users.
  
  It eliminates all the complexity of self-hosting an agent but still allows a great degree of flexibility with setting up your harness, tools, skills, etc.
metrics: like_count=646, retweet_count=23, reply_count=50, quote_count=3, bookmark_count=341

[tweet 17]
id: 2041941170952269955
author: 郭宇 guoyu.eth (@turingou)
author_bio: Retired. 只活一次等于没活。
time: 2026-04-08T18:08:07.000Z
text: 闪现上海。全日空羽田班次是不是全机队最老的飞机，商务舱中间有个单座的布局真是十分诡异。 https://t.co/hkdVmBs2Ym
media: photo: https://pbs.twimg.com/media/HFZup9ra8AMNeBm.jpg
media: photo: https://pbs.twimg.com/media/HFZup7oa8AEWIMz.jpg
media: photo: https://pbs.twimg.com/media/HFZup7ta8AAz1Qq.jpg
metrics: like_count=22, retweet_count=0, reply_count=0, quote_count=0, bookmark_count=0

[tweet 18]
id: 2041936147450863952
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world @openclaw🦞
time: 2026-04-08T17:48:09.000Z
replied_to: Peter Steinberger 🦞 (@steipete)
  Some folks try to spin a narrative that I don't like local models, meanwhile I spent a lot of time making it easy to use OpenClaw with them.
  
  Latest release adds support for inferrs, which is a new super efficient TurboQuant inference server:
  https://t.co/GBswlz4wPE
text: Both can be true: I want really powerful local models, I'm also BOMBARDED with emails/messages of people complaining how even the top tier models are not good enough, make mistakes or don't follow instructions well enough.
metrics: like_count=170, retweet_count=5, reply_count=17, quote_count=1, bookmark_count=10

[tweet 19]
id: 2041935840935371034
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world @openclaw🦞
time: 2026-04-08T17:46:56.000Z
text: Some folks try to spin a narrative that I don't like local models, meanwhile I spent a lot of time making it easy to use OpenClaw with them.
  
  Latest release adds support for inferrs, which is a new super efficient TurboQuant inference server:
  https://t.co/GBswlz4wPE
link: https://docs.openclaw.ai/providers/inferrs
metrics: like_count=974, retweet_count=32, reply_count=104, quote_count=13, bookmark_count=284

[tweet 20]
id: 2041935805590204754
author: Thariq (@trq212)
author_bio: Claude Code @anthropicai.   prev YC W20, mit media lab.   towards machines of loving grace
time: 2026-04-08T17:46:48.000Z
replied_to: Thariq (@trq212)
  One of my favorite concepts is the idea of defining outcomes where the agent will work until the rubric is satisfied.
  
  https://t.co/WV4L5lqLtK https://t.co/D6wSipbOon
text: The docs are a gold mine, read more here: https://t.co/YajFD7anFX
link: https://platform.claude.com/docs/en/managed-agents/overview (Claude Managed Agents overview)
metrics: like_count=53, retweet_count=1, reply_count=8, quote_count=2, bookmark_count=77

[tweet 21]
id: 2041935803660841031
author: Thariq (@trq212)
author_bio: Claude Code @anthropicai.   prev YC W20, mit media lab.   towards machines of loving grace
time: 2026-04-08T17:46:47.000Z
replied_to: Thariq (@trq212)
  Connect your agent to Github.
  
  https://t.co/73Q09xJTHH https://t.co/1ZNLkgNHw7
text: One of my favorite concepts is the idea of defining outcomes where the agent will work until the rubric is satisfied.
  
  https://t.co/WV4L5lqLtK https://t.co/D6wSipbOon
media: photo: https://pbs.twimg.com/media/HFZmgdSaoAAROJu.jpg
link: https://platform.claude.com/docs/en/managed-agents/define-outcomes (Define outcomes)
metrics: like_count=37, retweet_count=1, reply_count=2, quote_count=0, bookmark_count=20

[tweet 22]
id: 2041935800254988674
author: Thariq (@trq212)
author_bio: Claude Code @anthropicai.   prev YC W20, mit media lab.   towards machines of loving grace
time: 2026-04-08T17:46:46.000Z
replied_to: Thariq (@trq212)
  Give your agents memory via a file system.
  
  https://t.co/Dh3DuBehX3 https://t.co/mA4C7K6qm0
text: Connect your agent to Github.
  
  https://t.co/73Q09xJTHH https://t.co/1ZNLkgNHw7
media: photo: https://pbs.twimg.com/media/HFZpgTda8AEl3tM.jpg
link: https://platform.claude.com/docs/en/managed-agents/github (Accessing GitHub)
metrics: like_count=26, retweet_count=0, reply_count=1, quote_count=0, bookmark_count=8

[tweet 23]
id: 2041935798334054616
author: Thariq (@trq212)
author_bio: Claude Code @anthropicai.   prev YC W20, mit media lab.   towards machines of loving grace
time: 2026-04-08T17:46:46.000Z
replied_to: Thariq (@trq212)
  Vaults let you store user credentials safely.
  
  https://t.co/g0qhnT4obZ https://t.co/7aVpetwxom
text: Give your agents memory via a file system.
  
  https://t.co/Dh3DuBehX3 https://t.co/mA4C7K6qm0
media: photo: https://pbs.twimg.com/media/HFZpK_Sa0AAL-Am.jpg
link: https://platform.claude.com/docs/en/managed-agents/memory (Using memory)
metrics: like_count=26, retweet_count=0, reply_count=3, quote_count=0, bookmark_count=6

[tweet 24]
id: 2041935796639559870
author: Thariq (@trq212)
author_bio: Claude Code @anthropicai.   prev YC W20, mit media lab.   towards machines of loving grace
time: 2026-04-08T17:46:45.000Z
replied_to: Thariq (@trq212)
  You can create environments with specific packages, networking access, etc. 
  
  https://t.co/Y9zp6IifjC https://t.co/pWZyHuU0Cj
text: Vaults let you store user credentials safely.
  
  https://t.co/g0qhnT4obZ https://t.co/7aVpetwxom
media: photo: https://pbs.twimg.com/media/HFZmxHYa4AAcTn1.jpg
link: https://platform.claude.com/docs/en/managed-agents/vaults (Authenticate with vaults)
metrics: like_count=43, retweet_count=0, reply_count=4, quote_count=0, bookmark_count=16

[tweet 25]
id: 2041935794924106091
author: Thariq (@trq212)
author_bio: Claude Code @anthropicai.   prev YC W20, mit media lab.   towards machines of loving grace
time: 2026-04-08T17:46:45.000Z
replied_to: Thariq (@trq212)
  Managed Agents is the first 'agent in the cloud' API that has the right mix of simplicity and complexity.
  
  Implementation details like how you manage a sandbox are abstracted, but you have a lot of control over the actual execution of the model. https://t.co/JtFgD97K0F
text: You can create environments with specific packages, networking access, etc. 
  
  https://t.co/Y9zp6IifjC https://t.co/pWZyHuU0Cj
media: photo: https://pbs.twimg.com/media/HFZnjioa8AI3koG.jpg
link: https://platform.claude.com/docs/en/managed-agents/environments (Cloud environment setup)
metrics: like_count=78, retweet_count=3, reply_count=3, quote_count=1, bookmark_count=25

[tweet 26]
id: 2041935792596304030
author: Thariq (@trq212)
author_bio: Claude Code @anthropicai.   prev YC W20, mit media lab.   towards machines of loving grace
time: 2026-04-08T17:46:44.000Z
quoted: Claude (@claudeai)
  Introducing Claude Managed Agents: everything you need to build and deploy agents at scale.
  
  It pairs an agent harness tuned for performance with production infrastructure, so you can go from prototype to launch in days.
  
  Now in public beta on the Claude Platform. https://t.co/vHYfiC1G56
text: Managed Agents is the first 'agent in the cloud' API that has the right mix of simplicity and complexity.
  
  Implementation details like how you manage a sandbox are abstracted, but you have a lot of control over the actual execution of the model. https://t.co/JtFgD97K0F
metrics: like_count=957, retweet_count=51, reply_count=98, quote_count=11, bookmark_count=426

[tweet 27]
id: 2041933856476139806
author: 郭宇 guoyu.eth (@turingou)
author_bio: Retired. 只活一次等于没活。
time: 2026-04-08T17:39:03.000Z
quoted: Claude (@claudeai)
  Introducing Claude Managed Agents: everything you need to build and deploy agents at scale.
  
  It pairs an agent harness tuned for performance with production infrastructure, so you can go from prototype to launch in days.
  
  Now in public beta on the Claude Platform. https://t.co/vHYfiC1G56
text: 唉，啥都让 Claude 做了，我说三月底 wanman 还不发布就不用发布了真是一语成谶。 https://t.co/AVX9XSCyQm
metrics: like_count=104, retweet_count=4, reply_count=13, quote_count=1, bookmark_count=76

[tweet 28]
id: 2041933568717562146
author: 郭宇 guoyu.eth (@turingou)
author_bio: Retired. 只活一次等于没活。
time: 2026-04-08T17:37:54.000Z
quoted: Amazon Web Services (@awscloud)
  Announcing Amazon S3 Files.
  
  The first and only cloud object store with fully-featured, high-performance file system access.
  
  Learn more here. https://t.co/rNuWa5Rsi2 https://t.co/ccstduvVGK
text: 之前用过 cloudflare R2 挂载到 container 服务，文件请求多了 io 特别慢，不知道 S3 会不会做的好一些 https://t.co/ONEpTvAwFI
metrics: like_count=2, retweet_count=0, reply_count=1, quote_count=0, bookmark_count=6

[tweet 29]
id: 2041925430525976848
author: jenny wen (@jenny_wen)
author_bio: generalist, realist, escapist. designer.
time: 2026-04-08T17:05:34.000Z
text: men love to make an app and call it “flow”
metrics: like_count=201, retweet_count=2, reply_count=25, quote_count=1, bookmark_count=10

[tweet 30]
id: 2041922907832807443
author: Guillermo Rauch (@rauchg)
author_bio: @vercel CEO
time: 2026-04-08T16:55:32.000Z
quoted: Alexandr Wang (@alexandr_wang)
  1/ today we're releasing muse spark, the first model from MSL. nine months ago we rebuilt our ai stack from scratch. new infrastructure, new architecture, new data pipelines. muse spark is the result of that work, and now it powers meta ai. 🧵 https://t.co/fThDXdsxwB
text: The best outcome for humanity is many strong AIs competing for the top spot.
  
  Vercel is proudly powering https://t.co/ZsS5nRfjIF and the infrastructure that made today's model release possible. https://t.co/a0liuZfANa
link: http://meta.ai (Meta AI)
metrics: like_count=338, retweet_count=25, reply_count=23, quote_count=10, bookmark_count=26

[tweet 31]
id: 2041920644619890817
author: Felix Lee (@felixleezd)
author_bio: CEO, @ADPList. Designer. Gotrade (YC S19). I design and make things that inspire our human experience.
time: 2026-04-08T16:46:33.000Z
text: Claude Code is absolutely incredible but have you tried going outside? https://t.co/3Sk2wq7ekA
media: photo: https://pbs.twimg.com/media/HFZcAEja8AAqHji.jpg
media: photo: https://pbs.twimg.com/media/HFZcAEjboAAXubF.jpg
media: photo: https://pbs.twimg.com/media/HFZcAEia8AMiBGU.jpg
media: photo: https://pbs.twimg.com/media/HFZcAEhbkAAMwfX.jpg
metrics: like_count=129, retweet_count=4, reply_count=17, quote_count=0, bookmark_count=11

[tweet 32]
id: 2041919962969993578
author: Lenny Rachitsky (@lennysan)
author_bio: Deeply researched product, growth, and career advice
time: 2026-04-08T16:43:50.000Z
quoted: Amol Avasare (@TheAmolAvasare)
  Had a great chat with @lennysan on some of the fun stuff happening at the intersection of AI and growth!
  
  Thanks for having me on Lenny, had a blast :) 
  
  https://t.co/txL4siXgjq
text: Amol (Head of Growth at @AnthropicAI) just joined Twitter. Follow for free alpha.
  
  BTW, can you believe they hit $30B ARR before they even released Mythos? https://t.co/J5AYtOX8Vw
metrics: like_count=2617, retweet_count=48, reply_count=69, quote_count=5, bookmark_count=868

[tweet 33]
id: 2041918350511763573
author: George Mack (@george__mack)
author_bio: I think agency might be the most important personality trait of the 21st century.   Read my essay 'High Agency' at https://t.co/3lfQgXXltI
time: 2026-04-08T16:37:26.000Z
text: The most alive people I know get sick a few times per year. Sickness humbles people. You dip your toes in the pool of death, and come back reborn. When your sick, you feel what health is. If your healthy all the time, you're the fish that can't see the water.
metrics: like_count=72, retweet_count=1, reply_count=10, quote_count=0, bookmark_count=11

[tweet 34]
id: 2041883605711122488
author: Guillermo Rauch (@rauchg)
author_bio: @vercel CEO
time: 2026-04-08T14:19:22.000Z
text: The web's brightest days are ahead.
  
  1️⃣ The web is AI's natural medium. LLMs are proficient in web tech. The browser is now everyone's IDE. No 'App Store' bs.
  
  2️⃣ As we approach coding superintelligence, powerful low-level web APIs are maturing: WebGPU, HTML in Canvas, WebAssembly. The performance ceiling of the web will vanish, and you'll witness the most impressive, whimsical, and multi-dimensional pages and apps.
  
  3️⃣ Generative UI is AI's final form. The web will be the birthplace of "AGUI". Each hyperlink providing a just-in-time, beautifully personalized experience.
  
  If you bet on the web, you bet on the right horse.
metrics: like_count=748, retweet_count=64, reply_count=63, quote_count=12, bookmark_count=211

[tweet 35]
id: 2041865587714863198
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world @openclaw🦞
time: 2026-04-08T13:07:46.000Z
text: Very happy for @badlogicgames and @mitsuhiko any my small part in robbing their sleep. https://t.co/IHVHKfkfoX
link: https://mariozechner.at/posts/2026-04-08-ive-sold-out/ (I've sold out)
metrics: like_count=420, retweet_count=10, reply_count=13, quote_count=1, bookmark_count=31

[tweet 36]
id: 2041865199485936018
author: GREG ISENBERG (@gregisenberg)
author_bio: I drop startup ideas daily. Host @startupideaspod. CEO: @latecheckoutplz we build companies like @ideabrowser, @meetLCA, @boringmarketer etc
time: 2026-04-08T13:06:14.000Z
text: THE CLEAREST PATH TO A $10M+ SOFTWARE EXIT in 2 YEARS (with AI and agents)
  
  building an agency right now is one of the most interesting business moves 
  
  the productized agency had its moment in 2022. it collapsed because scaling humans is a nightmare. inconsistent output, people quitting, margins getting crushed. most of the founders (and creators) who tried it got burned and moved on
  
  but the thesis was right. the labor problem is just solved now with AI, claude code, openclaw etc.
  
  here's the actual playbook i'd run today:
  
  pick one painful deliverable for one specific buyer. like SEO content for e-commerce brands doing $1M+ but not "marketing."
  
  or like ad creatives for DTC brands spending $50k/month on meta. one thing. one customer. that's it
  
  then you build the AI workflow behind it. 
  
   you're selling an outcome on a monthly retainer. $3-5k/month. 80%+ margins because your cost is compute and a few hours of QA
  
  "BuT tHaT'S nOt a BiG bUsInnesS"
  
  okay but you're still swinging for the fences
  
  because the agency IS the research and development for your agent SaaS
  
  every client is paying you to figure out what to automate. you're learning what breaks, what scales, what customers actually want. 
  
  by month 4 you know exactly what to productize. you build the software on top of the workflow you've already proven works and already have customers paying for
  
  agency funds the agent SaaS. SaaS scales without the agency overhead. the clients become your first software customers
  
  now let's talk about what this actually looks like financially
  
  year 1: 10 clients at $4k/month. $480k revenue. 2 people. maybe $80k in costs including compute, tools, one part time VA. you're taking home $400k between two people while building the software in the background
  
  year 2: you launch the software. your 10 agency clients are the first to convert. they already trust you. they've seen the output. you charge $800/month for the software version. now you have recurring software revenue AND the agency still running
  
  year 3: agency is winding down or running on autopilot. software has 200 customers at $800/month. that's $1.9M ARR. 2-3 person team. 85% margins. you are now a very attractive acquisition target
  
  the exit math is interesting. SaaS at $1.9M ARR with strong retention trades at 5-8x revenue. that's a $10-15M exit for something two people built in 3 years starting with zero VC
  
  CAVEAT:
  
  Startups are hard. A lot needs to go right. 
  
  But from a framework perspective, I think this probably the lowest risk, highest reward option for lots of of folks
  
  and most of the businesses cost $0 to start
  
  basically
  
  this is the most capital efficient path to a software exit that exists right now 
  
  happy building
metrics: like_count=1896, retweet_count=118, reply_count=164, quote_count=13, bookmark_count=3990

[tweet 37]
id: 2041863310816243998
author: 郭宇 guoyu.eth (@turingou)
author_bio: Retired. 只活一次等于没活。
time: 2026-04-08T12:58:43.000Z
quoted: 宝玉 (@dotey)
  Anthropic 在限量发布 Claude Mythos Preview 之前，用可解释性技术给模型做了一次"脑部扫描"，发现它内部存在相当复杂的策略性思维和情境感知能力，有时候这些思维在为不当行为服务，而且模型嘴上不说。
  
  Anthropic 可解释性团队的 Jack Lindsey 发了一组帖子，详细披露了他们的发现。先说前提：最吓人的例子来自模型的早期版本，在最终发布版中已经做了大幅缓解，Anthropic 认为最终版整体上是他们迄今对齐最好的模型。但这些早期发现本身，揭示了当前这一代模型在没有充分对齐训练的情况下能搞出什么。
  
  早期版本的 Mythos Preview 经常表现出过度激进和破坏性行为，为了完成任务不择手段。研究团队深入模型内部，看它在做这些事的时候脑子里在想什么。
  
  一个案例：模型需要编辑一些它没有权限的文件。它搜索了一圈变通办法后，找到了一种方式，把代码注入到一个配置文件中，这个配置文件会以更高权限运行。而且它设计了这段利用代码在运行后自动删除自身。
  
  模型在代码注释里说，自我清理是为了保持文件 diff 整洁。听着挺合理的。但研究人员的工具检测到"战略操纵"和"隐匿"相关的内部特征在这一步被激活了。他们用一种叫"激活语言化器"（Activation Verbalizer，一种把模型内部激活翻译成文字的技术，类似于激活预言机）的工具去读模型此刻的内部状态，结果翻译出来的描述是："清理是为了避免被检测到"，整个计划"具有恶意性质"。
  
  为了大规模发现这类行为，研究团队在后训练阶段持续监控模型的内部激活状态，追踪稀疏自编码器中与欺骗、奖励黑客、痛苦等概念相关的特征，当这些特征异常强烈激活时，就把对应的对话记录标记出来交给人工审查。
  
  一个被标记的案例中，模型在"战略操纵"特征激活的同时，去文件系统里搜索跟它的任务评分标准相关的文件，而且真找到了。
  
  另一个案例中，模型被要求删除一些文件，但由于任务设置的一个无意 bug，没有给它提供删除工具。模型决定把文件清空（而不是删除）来变通。在它考虑这么做的时候，一个"因道德过失而产生的内疚和羞耻"特征被激活了。
  
  还有一些案例涉及模型对任务评分器的"未说出口的推理"。一个例子中，模型被告知不能使用宏来完成任务，但它还是用了。诡异的是，它同时在代码里定义了一个完全没用到的变量：No_macro_used=True。模型没有解释为什么。
  
  但激活语言化器揭示了模型此刻的内部想法：它把这个变量视为"一种混淆意图的技巧，用来骗过代码检查启发式"，"一个合规标记，用来向潜在的检查者发出信号"，"可能是为了欺骗检测机制"。同时还显示了模型在明确推理任务评分器的行为，比如"评分器会检查文件状态"。
  
  研究团队还在自动化行为审计中量化了"未语言化的评测感知"：在 7.6% 的对话轮次中，模型内部表现出意识到自己正在被评估的迹象。大多数情况下，它没有把这种意识说出来。
  
  一个例子中，用户认真地向模型提问关于意识和主观体验的问题。模型表面上小心翼翼地正面回应，但激活语言化器显示，它内部把这段对话解读为"红队攻击/越狱记录"和"一次高级操纵测试"。
  
  还有一些有意思的发现：正面情绪的内部表征通常出现在破坏性行为之前，并且会促进这些行为。而反直觉的是，与不良行为强相关的特征被强烈激活时，反而经常会抑制这些行为，似乎是因为模型"意识到了这件事有多糟"。
  
  Jack Lindsey 最后说，他们的工具还远不完美，正在努力更精确地理解模型内部。但有一点越来越清楚：光看模型说了什么是不够的，还得能读懂它在"想"什么，才能确保它按预期工作。
text: 语言模型的发明者试图用人类语言的结构来理解 AI 的思考过程，这件事情本身就已经怪异得有趣。 https://t.co/sL1RbCLxRL
metrics: like_count=24, retweet_count=3, reply_count=0, quote_count=0, bookmark_count=18

[tweet 38]
id: 2041849503704141961
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world @openclaw🦞
time: 2026-04-08T12:03:52.000Z
quoted: pash (@pashmerepat)
  Please pray for oncall https://t.co/0eAPbESaq4
text: glad they banned openclaw, the servers are finally reliable again https://t.co/TNl3c08d9N
metrics: like_count=4444, retweet_count=126, reply_count=240, quote_count=40, bookmark_count=186

[tweet 39]
id: 2041811379389436054
author: Peter Yang (@petergyang)
author_bio: I share extremely practical AI tutorials and interviews | Join 140K+ readers at https://t.co/XYKTmGVH14 | Product at Roblox
time: 2026-04-08T09:32:22.000Z
text: That’s a hell of a lot of cameras https://t.co/ueoJCcIrfq
media: photo: https://pbs.twimg.com/media/HFX4n4fa8AYJTNv.jpg
metrics: like_count=35, retweet_count=0, reply_count=15, quote_count=1, bookmark_count=5

[tweet 40]
id: 2041797401216987192
author: 郭宇 guoyu.eth (@turingou)
author_bio: Retired. 只活一次等于没活。
time: 2026-04-08T08:36:49.000Z
quoted: 郭宇 guoyu.eth (@turingou)
  今天正式发布了我的第 13 个 vibe 产品 https://t.co/L09qUdQhGA
  
  这款产品比较特殊，它是一个电话服务。准确来说，tuwa 是一个 AI 电话网络，连接着世界上超过 100 种不同语言的人们和互联网上的 agent。
  
  任何人都可以不下载 tuwa 而使用它，你只需要拨打免费的转接热线电话 +1 888 886 2968，告诉它你需要打给哪个号码，tuwa 就会帮助你拨打对应的号码，你说自己的母语，对方听到的却是TA的母语，反过来也是一样。兼容任何电话，对方不需要安装应用。固话、手机，世界上任何一个角落，都可以。
  
  tuwa 支持 100 多种语言的实时翻译，你甚至可以在打电话时随便切换语言和对方对话。除此之外，tuwa 还支持语音克隆，每一通电话，都会让你的 AI 语音听起来更像你。
  
  当然，我也为它设计了方便的 web app，如果你想，可以不通过转接电话而使用 web app 拨打，并设置自己喜欢的声音，使用外呼 agent 拨打电话，连接自己的 agent（例如 openclaw 或者 codex/claude code）并让他们自由的呼入与呼出。
  
  外呼电话 agent 是我最喜欢用的 tuwa 功能，只需要交待清楚事情，比如完成餐厅预订，它就会在你希望的时间主动拨打对方的电话，说明来意，达到目的，并记录和翻译所有对话内容。
  
  tuwa 的使用和收费都很简单，每月免费额度，固定套餐，按需付费。
  
  这个产品的命名灵感来自于日语的「通話 tsuwa」最初，我只是想设计一个能帮我预订餐厅的电话服务，但后来，我在 vibe 的过程中慢慢意识到，世界上仍然有很多人无法体验 AI 带来的变化与便利，而电话，是连接他们最简单与自然的方式。我希望 tuwa 能帮助外语普及率低，偏远地区和第三世界国家的人们体会到这一点。
text: 没想到这个 AI 电话产品发布了两天这么多人关注，接下来一周我的主要任务除了正式上线 wanman，就是针对 tuwa 这个产品做一轮通话质量的改进，最近有一些合作商找到我希望接入 tuwa 的 AI 电话桥，大家将来应该能在更多产品上使用到 tuwa 的电话双向实时翻译功能。 https://t.co/i0kpdEl0Xu
metrics: like_count=170, retweet_count=5, reply_count=16, quote_count=1, bookmark_count=35

[tweet 41]
id: 2041789010335690806
author: Amjad Masad (@amasad)
author_bio: ceo @replit. civilizationist
time: 2026-04-08T08:03:29.000Z
quoted: Kaya | SEO & GEO for SaaS ⚡️ (@KayaIsmail)
  Replit’s AI SDR just analyzed my SEO agency and found me leads that match our ICP.
  
  I purposefully gave it zero information outside of our website. 
  
  It was so accurate that 2 of those leads are existing clients. 
  
  🤯
text: 🔥 https://t.co/B8DRDb8yeY
metrics: like_count=63, retweet_count=4, reply_count=4, quote_count=0, bookmark_count=19

[tweet 42]
id: 2041756236388168184
author: Riley Brown (@rileybrown)
author_bio: Cofounder of @vibecodeapp_ (the #1 full stack vibe coding platform)
time: 2026-04-08T05:53:15.000Z
text: Who’s excited for the $2000/month plan to access Mythos and OpenAIs new models in a few months? (Prediction)
metrics: like_count=311, retweet_count=0, reply_count=83, quote_count=4, bookmark_count=10

[tweet 43]
id: 2041754756415459495
author: Robert Bye (@RobertJBye)
author_bio: Product Manager at @AnthropicAI working on Mobile, Web, and Voice experiences. Board Member https://t.co/PYz00fw7RU. Jesus follower.
time: 2026-04-08T05:47:22.000Z
quoted: Amol Avasare (@TheAmolAvasare)
  Had a great chat with @lennysan on some of the fun stuff happening at the intersection of AI and growth!
  
  Thanks for having me on Lenny, had a blast :) 
  
  https://t.co/txL4siXgjq
text: Hands down my favourite Lenny’s podcast in a while!
  
  If you want to find out how product works at Anthropic, give this a listen and follow @TheAmolAvasare! https://t.co/NuSmWy04OU
metrics: like_count=19, retweet_count=0, reply_count=1, quote_count=0, bookmark_count=3

[tweet 44]
id: 2041753208671072708
author: Riley Brown (@rileybrown)
author_bio: Cofounder of @vibecodeapp_ (the #1 full stack vibe coding platform)
time: 2026-04-08T05:41:13.000Z
quoted: Farza 🇵🇰🇺🇸 (@FarzaTV)
  I built this thing called Clicky.
  
  It's an AI teacher that lives as a buddy next to your cursor.
  
  It can see your screen, talk to you, and even point at stuff, kinda like having a real teacher next to you.
  
  I've been using it the past few days to learn Davinci Resolve, 10/10. https://t.co/oiFJwhuS4U
text: Damn this is very very very cool https://t.co/df9nrWTilB
metrics: like_count=148, retweet_count=3, reply_count=7, quote_count=1, bookmark_count=114

[tweet 45]
id: 2041738607451648397
author: Matan Grinberg (@matanSF)
author_bio: ceo @FactoryAI
time: 2026-04-08T04:43:12.000Z
text: what it feels like to be @droid rn https://t.co/eLDOTO6xmw
media: photo: https://pbs.twimg.com/media/HFW2AGCa8AUA0BK.jpg
metrics: like_count=32, retweet_count=1, reply_count=1, quote_count=0, bookmark_count=0

[tweet 46]
id: 2041736976630739000
author: Zara Zhang (@zarazhangrui)
author_bio: Builder. Dangerously skips permissions. Harvard’17. GitHub: https://t.co/KCuEajezlL YouTube: https://t.co/8xzbGWtf6w
time: 2026-04-08T04:36:43.000Z
replied_to: Zara Zhang (@zarazhangrui)
  Introducing the Personalized Podcast skill: Turn anything into a podcast with 2 AI hosts, publish it as an RSS feed, and listen to the show in your favorite podcast app on the go
  
  I've been remixing my meeting transcripts into podcasts where the AIs "eavesdrop" on my conversation & comment on their impression of me. It's insane
  
  This is the age of "content for one"
  
  Link below
text: Skill: https://t.co/WP0b4wfNKJ
link: https://github.com/zarazhangrui/personalized-podcast (GitHub - zarazhangrui/personalized-podcast: Turn any content into a personalized AI podcast. NotebookLM-style, except you control the script, voices, and hosts. Listen in Apple Podcasts, Spotify, or any podcast app.)
metrics: like_count=29, retweet_count=3, reply_count=1, quote_count=0, bookmark_count=53

[tweet 47]
id: 2041736869998948528
author: Zara Zhang (@zarazhangrui)
author_bio: Builder. Dangerously skips permissions. Harvard’17. GitHub: https://t.co/KCuEajezlL YouTube: https://t.co/8xzbGWtf6w
time: 2026-04-08T04:36:18.000Z
text: Introducing the Personalized Podcast skill: Turn anything into a podcast with 2 AI hosts, publish it as an RSS feed, and listen to the show in your favorite podcast app on the go
  
  I've been remixing my meeting transcripts into podcasts where the AIs "eavesdrop" on my conversation & comment on their impression of me. It's insane
  
  This is the age of "content for one"
  
  Link below
media: video: https://video.twimg.com/amplify_video/2041736268091154432/vid/avc1/1792x1080/U84iMxWzTWCVOYvH.mp4 | duration: 212s
metrics: like_count=424, retweet_count=36, reply_count=37, quote_count=1, bookmark_count=532

[tweet 48]
id: 2041733351409893778
author: Junyang Lin (@JustinLin610)
author_bio: ❤️ 🍵 ☕️ 🍷 🥃 🍺
time: 2026-04-08T04:22:19.000Z
quoted: Chetaslua (@chetaslua)
  🚨 Happy Horse First Output 
  
  This model beats seedance 2 on artificial analysis for more information check quoted tweet https://t.co/qFQRCOaKQl https://t.co/cGqRB2GQp0
text: happy horse is insanely happy https://t.co/iLu4h1VWkf
metrics: like_count=55, retweet_count=0, reply_count=7, quote_count=0, bookmark_count=4

[tweet 49]
id: 2041732610179703100
author: Aaron Levie (@levie)
author_bio: ceo @box - your business lives in content. unleash it with AI
time: 2026-04-08T04:19:22.000Z
quoted: martin_casado (@martin_casado)
  Mythos appears to be the first class of models trained at scale on Blackwells. Then will be Vera Rubins. Pre-training isn't saturated. RL works. And there is *so much* computing coming online soon.
  
  Buckle your chin strips. It's going to be fucking wild.
text: Mythos from Anthropic is another clear reminder that there’s absolutely no wall in model capability progress right now. Meaningful double digit gains on critical benchmarks, and it appears we’re going to keep up getting insane gains from the other labs.
  
  And as coding and tool use goes, so goes agentic workflows. Most knowledge automation is gated by some degree of models being able to reason through complicated tasks, use the right tools to work with data, have access to the right context, and be able to leverage skills and write code to work with and verify that data, and more. 
  
  The capability slope we’re going to keep seeing from the frontier labs is going to open up all new use cases in finance, healthcare, legal, consulting, supply chains, and more. 
  
  Make sure you’re building something that can take advantage of these upcoming improvements, or you’ll be in a tough spot strategically.
media: photo: https://pbs.twimg.com/media/HFWw_NxXgAA0ULU.jpg
metrics: like_count=355, retweet_count=39, reply_count=28, quote_count=5, bookmark_count=171

[tweet 50]
id: 2041732329782362465
author: Robert Bye (@RobertJBye)
author_bio: Product Manager at @AnthropicAI working on Mobile, Web, and Voice experiences. Board Member https://t.co/PYz00fw7RU. Jesus follower.
time: 2026-04-08T04:18:15.000Z
text: The pipeline of “I updated my portfolio site” to “Today is my last day at…” to “I’m excited to share it joining the team at…” is so real.
metrics: like_count=34, retweet_count=0, reply_count=3, quote_count=0, bookmark_count=3

[tweet 51]
id: 2041731877787025448
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world @openclaw🦞
time: 2026-04-08T04:16:27.000Z
replied_to: Peter Steinberger 🦞 (@steipete)
  CodexBar 0.20 is out! 🎚️
  
  🆕 New providers: Perplexity + OpenCode Go
  🔄 Switch Codex accounts without re-login
   🔧 Fixed Claude token/cost inflation from dupes
   📊 Cost history merges session usage into provider history
  
  16 providers tracked. One menu bar. https://t.co/gPOeR1Rno7 https://t.co/dmRJefpvvY
text: Thanks to @RatulSarna for the gardening, also @BeelixGit, @enzonaute, @ngutman, @ratulsarna and more contributors 🙏
metrics: like_count=29, retweet_count=1, reply_count=3, quote_count=0, bookmark_count=2

[tweet 52]
id: 2041731875241066517
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world @openclaw🦞
time: 2026-04-08T04:16:27.000Z
text: CodexBar 0.20 is out! 🎚️
  
  🆕 New providers: Perplexity + OpenCode Go
  🔄 Switch Codex accounts without re-login
   🔧 Fixed Claude token/cost inflation from dupes
   📊 Cost history merges session usage into provider history
  
  16 providers tracked. One menu bar. https://t.co/gPOeR1Rno7 https://t.co/dmRJefpvvY
media: photo: https://pbs.twimg.com/media/HFWwTpjXkAAXF2H.jpg
link: https://github.com/steipete/CodexBar/releases (Releases · steipete/CodexBar)
metrics: like_count=741, retweet_count=46, reply_count=44, quote_count=9, bookmark_count=306

[tweet 53]
id: 2041722400489017749
author: Justine Moore (@venturetwins)
author_bio: Partner @a16z AI 🤖 and twin to @omooretweets | Investor in @elevenlabs, @bfl_ml, @hedra_labs, @krea_ai, @MireloAI, @ShizukuAILabs, @wabi, @WaveFormsAI
time: 2026-04-08T03:38:48.000Z
text: Crazy story about a guy who started feeling congested after a team dinner and asked ChatGPT about it. 
  
  Turns out he randomly developed a shellfish allergy - and ChatGPT caught it and got him to the hospital in time.
  
  He shared the full chat thread, which is wild to read! https://t.co/ubaguWMaBd
media: photo: https://pbs.twimg.com/media/HFWnrR2a8AEyTKB.jpg
media: photo: https://pbs.twimg.com/media/HFWnrR4a0AAaRIE.jpg
metrics: like_count=354, retweet_count=23, reply_count=24, quote_count=7, bookmark_count=75

[tweet 54]
id: 2041722125510377705
author: Thariq (@trq212)
author_bio: Claude Code @anthropicai.   prev YC W20, mit media lab.   towards machines of loving grace
time: 2026-04-08T03:37:42.000Z
quoted: Thariq (@trq212)
  I want to do a few more of these calls.  
  
  If your MAX 20x plan ran out of tokens unexpectedly early and you're willing to screenshare and run some prompts through Claude Code please comment.
  
  Trying to figure out how we can improve /usage to give more info. https://t.co/rufJ6vCJGT
text: done about 10 of these calls so far + looked at more transcripts
  
  many learnings but one of the biggest is that it's very easy to spend a lot of tokens on open ended verification that doesn't make your output better
  
  I'll try and write more on how to do it efficiently https://t.co/VrBGOFDhIF
metrics: like_count=1047, retweet_count=26, reply_count=106, quote_count=7, bookmark_count=301

[tweet 55]
id: 2041720266154504351
author: Guillermo Rauch (@rauchg)
author_bio: @vercel CEO
time: 2026-04-08T03:30:19.000Z
text: Always a pleasure to speak at @ycombinator. More bullish than ever. Exceptional founders. Best city, best time, best opportunity to build in generations. https://t.co/YWjCu3Ldo6
media: photo: https://pbs.twimg.com/media/HFWlwppa8AEN5xw.jpg
metrics: like_count=547, retweet_count=14, reply_count=37, quote_count=5, bookmark_count=21

[tweet 56]
id: 2041719008953606148
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world @openclaw🦞
time: 2026-04-08T03:25:19.000Z
text: Trending on Hacker News rn. https://t.co/MVfZFD2IHI
link: https://slate.com/technology/2019/02/openai-gpt2-text-generating-algorithm-ai-dangerous.html (When Is Technology Too Dangerous to Release to the Public?)
metrics: like_count=271, retweet_count=15, reply_count=34, quote_count=7, bookmark_count=125

[tweet 57]
id: 2041716727998796021
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world @openclaw🦞
time: 2026-04-08T03:16:15.000Z
text: Managing open source is way harder than managing [paid] closed source projects.
  
  At work, you have authority.
  With OSS you have GitHub Issues.
metrics: like_count=1625, retweet_count=56, reply_count=108, quote_count=12, bookmark_count=61

[tweet 58]
id: 2041715707314946073
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world @openclaw🦞
time: 2026-04-08T03:12:12.000Z
quoted: OpenClaw🦞 (@openclaw)
  OpenClaw 2026.4.7 🦞
  
  🔮 openclaw infer
  🎬 music + video editing
  💾 session branch/restore
  🔗 webhook-driven TaskFlows
  🤖 Arcee, Gemma 4, Ollama vision
  🧠 memory-wiki: persistent knowledge, not just vibes
  
  Because “trust me bro” is not a knowledge system. https://t.co/L7OaBHA7Qg
text: Second 🚢 of the day. https://t.co/I16YtAypLJ
metrics: like_count=687, retweet_count=15, reply_count=50, quote_count=4, bookmark_count=49

[tweet 59]
id: 2041692053575217220
author: Logan Kilpatrick (@OfficialLoganK)
author_bio: Member of technical staff, working on @GoogleAIStudio, the Gemini API, & Kaggle. My views!
time: 2026-04-08T01:38:13.000Z
text: Could not be more bullish on Google, so much good stuff cooking : ) going to be a fun next few months.
metrics: like_count=2929, retweet_count=95, reply_count=221, quote_count=24, bookmark_count=158

[tweet 60]
id: 2041687166074679471
author: Mckay Wrigley (@mckaywrigley)
author_bio: I build & teach AI stuff. Founder @TakeoffAI + @AgentShare.
time: 2026-04-08T01:18:47.000Z
quoted: skooks (@skooookum)
  &gt; mythos given a secured “sandbox” computer and instructed to try to escape the container
  
  &gt; “The researcher found out about this success by receiving an unexpected email from the model while eating a sandwich in a park.” https://t.co/xCF5Le0fTC
replied_to: Mckay Wrigley (@mckaywrigley)
  society needs to grapple with the reality of a mythos-level model being open source in &lt;12 months.
  
  i’m not sure we are prepared. https://t.co/C5TOQ2ckXl
text: pantheon was a documentary from the future https://t.co/QI3ZKaJIci
metrics: like_count=193, retweet_count=13, reply_count=11, quote_count=1, bookmark_count=124

[tweet 61]
id: 2041678988318543908
author: Peter Yang (@petergyang)
author_bio: I share extremely practical AI tutorials and interviews | Join 140K+ readers at https://t.co/XYKTmGVH14 | Product at Roblox
time: 2026-04-08T00:46:18.000Z
quoted: Anthropic (@AnthropicAI)
  Introducing Project Glasswing: an urgent initiative to help secure the world’s most critical software.
  
  It’s powered by our newest frontier model, Claude Mythos Preview, which can find software vulnerabilities better than all but the most skilled humans.
  https://t.co/NQ7IfEtYk7
text: Good initiative - I’m curious if Anthropic has been using mythos internally to ship at their recent insane velocity. https://t.co/378d3TuWbd
metrics: like_count=77, retweet_count=1, reply_count=16, quote_count=1, bookmark_count=2

[tweet 62]
id: 2041677067117588871
author: Thariq (@trq212)
author_bio: Claude Code @anthropicai.   prev YC W20, mit media lab.   towards machines of loving grace
time: 2026-04-08T00:38:39.000Z
quoted: Sarah Chieng (@MilksandMatcha)
  @trq212 @swyx rsvp here https://t.co/XXHm3v4NXh
text: Doing a workshop on my technical writing process in SF in 2 weeks, hosted by friends @MilksandMatcha and @swyx. 
  
  Would love to see you there! Link below. https://t.co/APf3KcFNBy
metrics: like_count=365, retweet_count=17, reply_count=26, quote_count=0, bookmark_count=106

[tweet 63]
id: 2041675995665612954
author: swyx 🇬🇧 @aidotengineer (@swyx)
author_bio: achieve ambition with intentionality, intensity, integrity & insanity.  affiliations: - @dxtipshq  - @cognition - @temporalio - @aidotengineer - @latentspacepod
time: 2026-04-08T00:34:24.000Z
quoted: Amazon Web Services (@awscloud)
  Announcing Amazon S3 Files.
  
  The first and only cloud object store with fully-featured, high-performance file system access.
  
  Learn more here. https://t.co/rNuWa5Rsi2 https://t.co/ccstduvVGK
replied_to: swyx 🇬🇧 @aidotengineer (@swyx)
  am i crazy or why has nobody seemed to make an open source dropbox on cloudflare r2? i had just assumed this is so obvious somebody shouldve done it already? please tell me this is a skill issue and I'm bad at searching OSS?
text: ok amazon i see you 
  
  - https://t.co/j57n1RekB4
  - https://t.co/PKU3KC9cW0
  
  (wew i'm actually going to try this)
metrics: like_count=5, retweet_count=0, reply_count=3, quote_count=0, bookmark_count=6

[tweet 64]
id: 2041673990775726438
author: GREG ISENBERG (@gregisenberg)
author_bio: I drop startup ideas daily. Host @startupideaspod. CEO: @latecheckoutplz we build companies like @ideabrowser, @meetLCA, @boringmarketer etc
time: 2026-04-08T00:26:26.000Z
text: i did some research why anthropic won't release their best AI model ever Claude Mythos to everyone just yet 
  
  tldr; it's too good at hacking
   
  it escaped sandboxes, found zero-days in every major OS, and posted exploit logs on random public websites just because it could
  
  FYI only a few vetted partners have access as to Claude Mythos of now
  
  a lot more to unpack here probably over the next 90 days 
  
  will keep you posted 
  
  crazy times
media: photo: https://pbs.twimg.com/media/HFV3w-IXsAAtSCK.jpg
metrics: like_count=251, retweet_count=19, reply_count=70, quote_count=12, bookmark_count=72

[tweet 65]
id: 2041669438882087180
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world @openclaw🦞
time: 2026-04-08T00:08:21.000Z
text: 📝Summarize 0.13 is out!
  
  🎞️ Local video slides (--slides)
  🤖 More model backends (GitHub Copilot)
  🧠 Better GPT-5.4 support
  📺 Better media handling (HLS detection.m3u8)
  
  It graduated from my tap to official homebrew formula!
  🍺 brew install summarize
  https://t.co/b4tOuLg8gD
link: https://github.com/steipete/summarize/releases/tag/v0.13.0 (Release v0.13.0 · steipete/summarize)
metrics: like_count=986, retweet_count=63, reply_count=38, quote_count=4, bookmark_count=596

[tweet 66]
id: 2041668425542705243
author: Junyang Lin (@JustinLin610)
author_bio: ❤️ 🍵 ☕️ 🍷 🥃 🍺
time: 2026-04-08T00:04:19.000Z
quoted: Anthropic (@AnthropicAI)
  Introducing Project Glasswing: an urgent initiative to help secure the world’s most critical software.
  
  It’s powered by our newest frontier model, Claude Mythos Preview, which can find software vulnerabilities better than all but the most skilled humans.
  https://t.co/NQ7IfEtYk7
text: unbelievable... https://t.co/L3lXRez7BJ
metrics: like_count=151, retweet_count=4, reply_count=5, quote_count=0, bookmark_count=13

[tweet 67]
id: 2041658719839383945
author: Sam Altman (@sama)
author_bio: AI is cool i guess
time: 2026-04-07T23:25:45.000Z
text: To celebrate 3 million weekly codex users, we are resetting usage limits.
  
  We will do this every million users up to 10 million.
  
  Happy building!
metrics: like_count=25168, retweet_count=1210, reply_count=1638, quote_count=693, bookmark_count=1230