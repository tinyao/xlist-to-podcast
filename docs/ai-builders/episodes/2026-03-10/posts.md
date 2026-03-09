list_id: 2007466263661232466
fetched_at: 2026-03-09 23:11 UTC
total_tweets: 81
[tweet 1]
id: 2031137476438548874
author: Andrej Karpathy (@karpathy)
author_bio: I like to train large deep neural nets. Previously Director of AI @ Tesla, founding team @ OpenAI, PhD @ Stanford.
time: 2026-03-09T22:38:05.000Z
replied_to: Andrej Karpathy (@karpathy)
  Three days ago I left autoresearch tuning nanochat for ~2 days on depth=12 model. It found ~20 changes that improved the validation loss. I tested these changes yesterday and all of them were additive and transferred to larger (depth=24) models. Stacking up all of these changes, today I measured that the leaderboard's "Time to GPT-2" drops from 2.02 hours to 1.80 hours (~11% improvement), this will be the new leaderboard entry. So yes, these are real improvements and they make an actual difference. I am mildly surprised that my very first naive attempt already worked this well on top of what I thought was already a fairly manually well-tuned project.
  
  This is a first for me because I am very used to doing the iterative optimization of neural network training manually. You come up with ideas, you implement them, you check if they work (better validation loss), you come up with new ideas based on that, you read some papers for inspiration, etc etc. This is the bread and butter of what I do daily for 2 decades. Seeing the agent do this entire workflow end-to-end and all by itself as it worked through approx. 700 changes autonomously is wild. It really looked at the sequence of results of experiments and used that to plan the next ones. It's not novel, ground-breaking "research" (yet), but all the adjustments are "real", I didn't find them manually previously, and they stack up and actually improved nanochat. Among the bigger things e.g.:
  
  - It noticed an oversight that my parameterless QKnorm didn't have a scaler multiplier attached, so my attention was too diffuse. The agent found multipliers to sharpen it, pointing to future work.
  - It found that the Value Embeddings really like regularization and I wasn't applying any (oops).
  - It found that my banded attention was too conservative (i forgot to tune it).
  - It found that AdamW betas were all messed up.
  - It tuned the weight decay schedule.
  - It tuned the network initialization.
  
  This is on top of all the tuning I've already done over a good amount of time. The exact commit is here, from this "round 1" of autoresearch. I am going to kick off "round 2", and in parallel I am looking at how multiple agents can collaborate to unlock parallelism.
  https://t.co/WAz8aIztKT
  
  All LLM frontier labs will do this. It's the final boss battle. It's a lot more complex at scale of course - you don't just have a single train. py file to tune. But doing it is "just engineering" and it's going to work. You spin up a swarm of agents, you have them collaborate to tune smaller models, you promote the most promising ideas to increasingly larger scales, and humans (optionally) contribute on the edges.
  
  And more generally, *any* metric you care about that is reasonably efficient to evaluate (or that has more efficient proxy metrics such as training a smaller network) can be autoresearched by an agent swarm. It's worth thinking about whether your problem falls into this bucket too.
text: oh yeah i should have linked autoresearch probably
  https://t.co/YCvOwwjOzF
  (you don't "use it" directly, it's just a recipe/idea - give it to your agent and apply to what you care about.)
  
  and the tweet about it that went mini-viral over the weekend with more context
  https://t.co/q5eWsvx5p2
link: https://github.com/karpathy/autoresearch (GitHub - karpathy/autoresearch: AI agents running research on single-GPU nanochat training automatically)
link: https://github.com/karpathy/autoresearch
metrics: like_count=233, retweet_count=6, reply_count=15, quote_count=2, bookmark_count=166

[tweet 2]
id: 2031135152349524125
author: Andrej Karpathy (@karpathy)
author_bio: I like to train large deep neural nets. Previously Director of AI @ Tesla, founding team @ OpenAI, PhD @ Stanford.
time: 2026-03-09T22:28:51.000Z
text: Three days ago I left autoresearch tuning nanochat for ~2 days on depth=12 model. It found ~20 changes that improved the validation loss. I tested these changes yesterday and all of them were additive and transferred to larger (depth=24) models. Stacking up all of these changes, today I measured that the leaderboard's "Time to GPT-2" drops from 2.02 hours to 1.80 hours (~11% improvement), this will be the new leaderboard entry. So yes, these are real improvements and they make an actual difference. I am mildly surprised that my very first naive attempt already worked this well on top of what I thought was already a fairly manually well-tuned project.
  
  This is a first for me because I am very used to doing the iterative optimization of neural network training manually. You come up with ideas, you implement them, you check if they work (better validation loss), you come up with new ideas based on that, you read some papers for inspiration, etc etc. This is the bread and butter of what I do daily for 2 decades. Seeing the agent do this entire workflow end-to-end and all by itself as it worked through approx. 700 changes autonomously is wild. It really looked at the sequence of results of experiments and used that to plan the next ones. It's not novel, ground-breaking "research" (yet), but all the adjustments are "real", I didn't find them manually previously, and they stack up and actually improved nanochat. Among the bigger things e.g.:
  
  - It noticed an oversight that my parameterless QKnorm didn't have a scaler multiplier attached, so my attention was too diffuse. The agent found multipliers to sharpen it, pointing to future work.
  - It found that the Value Embeddings really like regularization and I wasn't applying any (oops).
  - It found that my banded attention was too conservative (i forgot to tune it).
  - It found that AdamW betas were all messed up.
  - It tuned the weight decay schedule.
  - It tuned the network initialization.
  
  This is on top of all the tuning I've already done over a good amount of time. The exact commit is here, from this "round 1" of autoresearch. I am going to kick off "round 2", and in parallel I am looking at how multiple agents can collaborate to unlock parallelism.
  https://t.co/WAz8aIztKT
  
  All LLM frontier labs will do this. It's the final boss battle. It's a lot more complex at scale of course - you don't just have a single train. py file to tune. But doing it is "just engineering" and it's going to work. You spin up a swarm of agents, you have them collaborate to tune smaller models, you promote the most promising ideas to increasingly larger scales, and humans (optionally) contribute on the edges.
  
  And more generally, *any* metric you care about that is reasonably efficient to evaluate (or that has more efficient proxy metrics such as training a smaller network) can be autoresearched by an agent swarm. It's worth thinking about whether your problem falls into this bucket too.
media: photo: https://pbs.twimg.com/media/HC_-jW0bUAA_Hga.jpg
link: https://github.com/karpathy/nanochat/commit/6ed7d1d82cee16c2e26f45d559ad3338447a6c1b
metrics: like_count=2429, retweet_count=225, reply_count=171, quote_count=71, bookmark_count=1070

[tweet 3]
id: 2031126785207714041
author: Guillermo Rauch (@rauchg)
author_bio: @vercel CEO
time: 2026-03-09T21:55:36.000Z
quoted: OpenBlock (@openblocklabs)
  The best coding agents don’t just write code, they ship it 🚀
  
  All OB-1 sessions now include the @Vercel CLI as a preloaded skill: deploy, preview, and manage projects without leaving the agent. https://t.co/vpbItWylsI
text: Real agents ship https://t.co/vwOhaGWyrf
metrics: like_count=78, retweet_count=5, reply_count=16, quote_count=0, bookmark_count=19

[tweet 4]
id: 2031126550834495891
author: Lenny Rachitsky (@lennysan)
author_bio: Deeply researched product, growth, and career advice
time: 2026-03-09T21:54:40.000Z
quoted: Lenny Rachitsky (@lennysan)
  Marc Andreessen calls him "the best AI CEO nobody knows about."
  
  Elad Gil calls his company "the most successful, most quiet company in AI."
  
  Qasar Younis (@qasar) is the co-founder and CEO of Applied Intuition—which brings AI to vehicles, like tractors, planes, submarines, mining rigs, cars, and more.
  
  The company is valued at over $15B, making ~$1B in ARR, with 18 of the top 20 global automakers (and the U.S. Department of Defense) as customers.
  
  And @Qasar's story is wild: Born on a farm in Pakistan. Emigrated to the U.S. at age 5. Grew up in Detroit managing engine lines at GM. Harvard MBA. Became COO of @Y Combinator (during the era that funded OpenAI, Cruise, DoorDash, and Coinbase). Then left to start Applied Intuition in 2017.
  
  As Qasar shared, "not many people run a $15B+ physical AI company with revenue and free cash flow. And by not many, I think literally zero other people."
  
  In a rare and in-depth interview, we discuss:
  🔸 The counterintuitive reason he's stayed quiet and built in private
  🔸 Why reading old books and cleaning your own office makes you a better founder
  🔸 How to build a culture where the best idea wins, not the loudest voice
  🔸 Why the best companies show traction early—and what to do if yours doesn't
  🔸 How physical AI will transform farming, mining, and construction before it ever reaches your home
  
  Listen now 👇
  https://t.co/35zENzhVAN
text: If you're worried about AI taking your job, try actually using it (via @qasar) https://t.co/zEtISa4pWU https://t.co/RtTC4UrIG2
media: video: https://video.twimg.com/amplify_video/2031060502806507520/vid/avc1/1080x1920/QpsawgkCa3ovJIQW.mp4 | duration: 63s
metrics: like_count=39, retweet_count=4, reply_count=8, quote_count=0, bookmark_count=35

[tweet 5]
id: 2031121653518971374
author: Justine Moore (@venturetwins)
author_bio: Partner @a16z AI 🤖 and twin to @omooretweets | Investor in @elevenlabsio, @bfl_ml, @hedra_labs, @krea_ai, @MireloAI, @ShizukuAILabs, @wabi, @WaveFormsAI
time: 2026-03-09T21:35:13.000Z
replied_to: Justine Moore (@venturetwins)
  GPT 5.4 is now shockingly good at reviewing slides, as I discovered last night.
  
  It feels like a detailed teardown from an expert in your field.
  
  You’ll get specific edits on each slide + a broader view on how to frame your narrative better.
  
  It’s hard to describe - just try it! https://t.co/HXC5IVwPU1
text: Sharing part of the response I got (redacted). 
  
  I literally just uploaded the PDF, told GPT 5.4 who the audience was, and asked for help. 
  
  It immediately identified that the narrative was confusing + gave slide-by-slide edits. https://t.co/wkAGnxKxg7
media: photo: https://pbs.twimg.com/media/HC_92wLaIAAIyIb.jpg
media: photo: https://pbs.twimg.com/media/HC_92wNaMAE6my9.png
media: photo: https://pbs.twimg.com/media/HC_92wKaMAM1nAH.png
media: photo: https://pbs.twimg.com/media/HC_92wLaMAAH6kf.png
metrics: like_count=15, retweet_count=0, reply_count=0, quote_count=0, bookmark_count=0

[tweet 6]
id: 2031117564512981169
author: Alex Albert (@alexalbert__)
author_bio: Claude Relations @AnthropicAI. Opinions are my own!
time: 2026-03-09T21:18:58.000Z
quoted: Claude (@claudeai)
  Introducing Code Review, a new feature for Claude Code.
  
  When a PR opens, Claude dispatches a team of agents to hunt for bugs. https://t.co/AL2J4efxPw
text: This has been a game changer for our internal eng and research teams. Rare to see a product get this much praise from some of the top engineers I know. https://t.co/5lveVazZdN
metrics: like_count=377, retweet_count=13, reply_count=15, quote_count=2, bookmark_count=58

[tweet 7]
id: 2031114394739114326
author: Justine Moore (@venturetwins)
author_bio: Partner @a16z AI 🤖 and twin to @omooretweets | Investor in @elevenlabsio, @bfl_ml, @hedra_labs, @krea_ai, @MireloAI, @ShizukuAILabs, @wabi, @WaveFormsAI
time: 2026-03-09T21:06:22.000Z
quoted: Romain Huet (@romainhuet)
  The vision in GPT-5.4 is incredible.
  
  Give it a dense document, diagram, or rough sketch and it just gets it.
  
  Better yet, ask Codex to turn it into something real! https://t.co/JBu17P3UjF
text: GPT 5.4 is now shockingly good at reviewing slides, as I discovered last night.
  
  It feels like a detailed teardown from an expert in your field.
  
  You’ll get specific edits on each slide + a broader view on how to frame your narrative better.
  
  It’s hard to describe - just try it! https://t.co/HXC5IVwPU1
metrics: like_count=118, retweet_count=11, reply_count=8, quote_count=0, bookmark_count=41

[tweet 8]
id: 2031107609852325980
author: GREG ISENBERG (@gregisenberg)
author_bio: I drop startup ideas daily. Host @startupideaspod. CEO: @latecheckoutplz we build companies like @ideabrowser, @meetLCA, @boringmarketer etc
time: 2026-03-09T20:39:25.000Z
text: i heard about a guy in a small town in england who turned his openclaw into a short form video marketing machine
  
  millions of views, steady app downloads, and revenue coming in every day
  
  i needed to find out how he was doing it
  
  1. spin up an ai “employee” using openclaw
  
  2. give it one job like grow your app with tiktokk
  
  3. give it access to tiktokk analytics, a browser to research and image/video tools to create content
  
  4. the openclaw studies your niche and starts generating slideshows and videos
  
  5. every post feeds performance data back into the system
  
  views → hook quality
  downloads → CTA quality
  revenue → funnel quality
  
  the openclaw then iterates on
  
  - new hooks
  - new formats
  - new CTAs
  
  until it finds winners
  
  one of his posts hit 170k+ views
  
  and the system keeps improving because the analytics loop feeds back into the content generation
  
  so the agent slowly learns what works
  
  what i like about this is the framing
  
  most people think about ai tools
  
  this is different
  
  you spin up an ai employee
  
  you give it a job
  
  and let it run the loop
  
  thanks to @oliverhenry for coming on the @startupideaspod today
  
  more like this soon, i will share the most interesting stories and gatekeep nothing 
  
  this episode was dripping in sauce 
  
  i gotta try this and see if it works
  
  kinda wild if it does 
  
  watch
media: video: https://video.twimg.com/amplify_video/2031107295594115072/vid/avc1/1280x720/w-FiirfI-wzH3FDz.mp4 | duration: 2599s
metrics: like_count=620, retweet_count=46, reply_count=44, quote_count=4, bookmark_count=1284

[tweet 9]
id: 2031098397189615795
author: Hamel Husain (@HamelHusain)
author_bio: Bringing data science back to AI -  https://t.co/Zrmp6LRd9c  About Me: https://t.co/P6WyeKkyTa
time: 2026-03-09T20:02:48.000Z
quoted: Kyle Kelley (@KyleRayKelley)
  @HamelHusain Hey I've got something for you that I haven't talked about publicly (yet): https://t.co/ctFk6dUOBZ + https://t.co/zIHnERcyRK
replied_to: Hamel Husain (@HamelHusain)
  The good/bad part about agentic codeing is the barrier to getting nerdsniped is now much lower
  
  https://t.co/CiGerRgM8H https://t.co/z6p0W229YM https://t.co/K6yV7kmYrT
text: Yall should check this out instead.  Looks clean af 
  
  If the only benefit of me vibe coding my skill was to learn about this, that is a win 👇 https://t.co/lqxE3oAjL8
metrics: like_count=4, retweet_count=1, reply_count=0, quote_count=0, bookmark_count=4

[tweet 10]
id: 2031097941394600109
author: Hamel Husain (@HamelHusain)
author_bio: Bringing data science back to AI -  https://t.co/Zrmp6LRd9c  About Me: https://t.co/P6WyeKkyTa
time: 2026-03-09T20:00:59.000Z
quoted: Kyle Kelley (@KyleRayKelley)
  @HamelHusain Hey I've got something for you that I haven't talked about publicly (yet): https://t.co/ctFk6dUOBZ + https://t.co/zIHnERcyRK
text: This looks fantastic.  Native Jupyter desktop electron app but rebuilt to expose a bunch of tools so agents can drive them https://t.co/lqxE3oAjL8
metrics: like_count=22, retweet_count=0, reply_count=2, quote_count=0, bookmark_count=16

[tweet 11]
id: 2031094653697896848
author: Peter Yang (@petergyang)
author_bio: I share extremely practical AI tutorials and interviews | Join 140K+ readers at https://t.co/XYKTmGVH14 | Product at Roblox
time: 2026-03-09T19:47:56.000Z
replied_to: Peter Yang (@petergyang)
  Roblox just launched two brand new programs for creators to build the next generation of novel games on the platform. 
  
  We'll provide full promotional support, direct access to Roblox staff, and a community of great devs, alumni, and investors.
  
  If interested, please apply here: https://t.co/dUznGkgFQG
text: We welcome both existing Roblox and external devs. You do have to be 18+ to apply. 
  
  There's a FAQ at the bottom of the page with more info. https://t.co/HPiLG36r05
media: photo: https://pbs.twimg.com/media/HC_lqYHagAANQQo.jpg
metrics: like_count=2, retweet_count=0, reply_count=0, quote_count=0, bookmark_count=1

[tweet 12]
id: 2031092341289922811
author: Thariq (@trq212)
author_bio: Claude Code @anthropicai.   prev YC W20, mit media lab.   towards machines of loving grace
time: 2026-03-09T19:38:44.000Z
replied_to: Thariq (@trq212)
  Code Review is so so good. One of those things I can't remember how I lived without. https://t.co/S1KLWPUnim
text: shout out to @katchu11 the actual GOAT
metrics: like_count=32, retweet_count=0, reply_count=5, quote_count=0, bookmark_count=5

[tweet 13]
id: 2031092339599618364
author: Thariq (@trq212)
author_bio: Claude Code @anthropicai.   prev YC W20, mit media lab.   towards machines of loving grace
time: 2026-03-09T19:38:44.000Z
quoted: Claude (@claudeai)
  Introducing Code Review, a new feature for Claude Code.
  
  When a PR opens, Claude dispatches a team of agents to hunt for bugs. https://t.co/AL2J4efxPw
text: Code Review is so so good. One of those things I can't remember how I lived without. https://t.co/S1KLWPUnim
metrics: like_count=931, retweet_count=16, reply_count=87, quote_count=3, bookmark_count=178

[tweet 14]
id: 2031090281521754294
author: Josh Woodward (@joshwoodward)
author_bio: VP, @Google @GoogleLabs @GeminiApp @GoogleAIStudio
time: 2026-03-09T19:30:33.000Z
text: So fun to spend part of the afternoon with some of India's builders, creators, and AI teachers in Bangalore! I learned a lot from you! https://t.co/2EI2yDgl2B
media: photo: https://pbs.twimg.com/media/HC_hMUzaMAIKDKk.jpg
metrics: like_count=124, retweet_count=2, reply_count=7, quote_count=0, bookmark_count=7

[tweet 15]
id: 2031089411820228645
author: Boris Cherny (@bcherny)
author_bio: Claude Code @anthropicai
time: 2026-03-09T19:27:06.000Z
quoted: Claude (@claudeai)
  Introducing Code Review, a new feature for Claude Code.
  
  When a PR opens, Claude dispatches a team of agents to hunt for bugs. https://t.co/AL2J4efxPw
text: New in Claude Code: Code Review. A team of agents runs a deep review on every PR.
  
  We built it for ourselves first. Code output per Anthropic engineer is up 200% this year and reviews were the bottleneck
  
  Personally, I’ve been using it for a few weeks and have found it catches many real bugs that I would not have noticed otherwise
metrics: like_count=4540, retweet_count=236, reply_count=266, quote_count=67, bookmark_count=2066

[tweet 16]
id: 2031086493985550521
author: Lenny Rachitsky (@lennysan)
author_bio: Deeply researched product, growth, and career advice
time: 2026-03-09T19:15:30.000Z
replied_to: Lenny Rachitsky (@lennysan)
  Been thinking about this. With the amount of wealth being created right now in AI, it's a great time to be in business selling things to wealthy people.
  
  (Not saying this is good, and I worry about where this trends leads, but it's still true) https://t.co/a2tfQQ3zLh
text: This isn't a new trend, and has been true for a while, but it's becoming much more true, as the number of wealthy people skyrockets
metrics: like_count=11, retweet_count=1, reply_count=2, quote_count=0, bookmark_count=2

[tweet 17]
id: 2031085362483994794
author: Lenny Rachitsky (@lennysan)
author_bio: Deeply researched product, growth, and career advice
time: 2026-03-09T19:11:00.000Z
quoted: Nick Abraham (@NickAbraham12)
  Alex Hormozi with the clearest argument for selling to wealthier people 😂 https://t.co/Pms2RnGaxg
text: Been thinking about this. With the amount of wealth being created right now in AI, it's a great time to be in business selling things to wealthy people.
  
  (Not saying this is good, and I worry about where this trends leads, but it's still true) https://t.co/a2tfQQ3zLh
metrics: like_count=367, retweet_count=17, reply_count=19, quote_count=1, bookmark_count=375

[tweet 18]
id: 2031085266908184583
author: Vercel (@vercel)
author_bio: Self-driving infrastructure for apps and agents.
time: 2026-03-09T19:10:38.000Z
replied_to: Vercel (@vercel)
  Ship 26 is coming soon.
  
  We'll be live in SF, NYC, London, Berlin, and Sydney.
  
  Ship what's next. https://t.co/DWnJl1BVjJ
text: Save the date and get early details plus our lowest pricing on tickets.
  https://t.co/1gvZrhHO1P
link: https://vercel.fyi/ship-26 (Vercel Ship 26 is coming to a city near you.)
metrics: like_count=42, retweet_count=5, reply_count=3, quote_count=3, bookmark_count=10

[tweet 19]
id: 2031085145340653713
author: Josh Woodward (@joshwoodward)
author_bio: VP, @Google @GoogleLabs @GeminiApp @GoogleAIStudio
time: 2026-03-09T19:10:09.000Z
quoted: NotebookLM (@NotebookLM)
  For everyone who saw our basketball post and thought, "I'd rather be in the library..." this one's for you. One of our MOST requested features:
  
  You can now upload ePub files as sources 🥳!
  
  Time to bring your books, study guides, and novels to life. What are you uploading first?
text: Students rejoice: ePub comes to NotebookLM! https://t.co/Azictw448d
metrics: like_count=180, retweet_count=8, reply_count=7, quote_count=0, bookmark_count=29

[tweet 20]
id: 2031084480941764902
author: Vercel (@vercel)
author_bio: Self-driving infrastructure for apps and agents.
time: 2026-03-09T19:07:30.000Z
text: Ship 26 is coming soon.
  
  We'll be live in SF, NYC, London, Berlin, and Sydney.
  
  Ship what's next. https://t.co/DWnJl1BVjJ
media: video: https://video.twimg.com/amplify_video/2031084110739824641/vid/avc1/1280x720/-8BjIegDJdmO0lzc.mp4 | duration: 33s
metrics: like_count=285, retweet_count=17, reply_count=20, quote_count=9, bookmark_count=33

[tweet 21]
id: 2031082933667377309
author: Felix Lee (@felixleezd)
author_bio: CEO, @ADPList. I design products for 10M+ people. Gotrade (YC S19). Intersection of art and science.
time: 2026-03-09T19:01:21.000Z
quoted: Simular (@SimularAI)
  In another universe, you missed your kid's recital. Your mom's birthday dinner. That anniversary  celebration with your person.
  
  In this one, you have 𝐒𝐚𝐢.
  
  The AI co-worker that does your computer work so you don't have to choose. https://t.co/266iDOLwvw
text: Sai's ux is interesting.
  
  The design shows how the agent works through multiple apps in real time, as a real human would.
  
  I just gave it a shot from the waitlist (code: SAI_FELIX_LEE) and did all my reads for the week. Love to see it 🤝
  
  https://t.co/PVZA09Hqvx https://t.co/6sXLS9pMq8
media: video: https://video.twimg.com/amplify_video/2028847330598977536/vid/avc1/1120x720/m4fHnM5UlF7mY-fg.mp4 | duration: 90s
metrics: like_count=6, retweet_count=0, reply_count=0, quote_count=0, bookmark_count=7

[tweet 22]
id: 2031080387095703688
author: Steven Johnson (@stevenbjohnson)
author_bio: Editorial Director, NotebookLM and Google Labs. Author of 14 books. Latest: The Infernal Machine. Speech inquiries email: wesn at leighbureau dot com
time: 2026-03-09T18:51:14.000Z
quoted: NotebookLM (@NotebookLM)
  For everyone who saw our basketball post and thought, "I'd rather be in the library..." this one's for you. One of our MOST requested features:
  
  You can now upload ePub files as sources 🥳!
  
  Time to bring your books, study guides, and novels to life. What are you uploading first?
text: ePub comes to @NotebookLM! Now it's easy to build your personal AI-first library with the thousands of classic public domain books available in ePub format. https://t.co/dMgUl1O7tg
metrics: like_count=202, retweet_count=12, reply_count=5, quote_count=2, bookmark_count=75

[tweet 23]
id: 2031075413133504801
author: Zara Zhang (@zarazhangrui)
author_bio: Builder. Harvard’17. YouTube: https://t.co/8xzbGWtf6w Substack: https://t.co/dDPEWGiuBW
time: 2026-03-09T18:31:28.000Z
text: Most AI products try to box the model in.
  
  Here's a template. Follow this format. Stay in these lanes.
  
  But Claude Code and OpenClaw showed the opposite approach:
  
  Give the model tools. Give it context. Let it loose.
  
  The magic happens when you remove constraints, not add them
metrics: like_count=29, retweet_count=1, reply_count=13, quote_count=2, bookmark_count=6

[tweet 24]
id: 2031071059307601944
author: swyx (@swyx)
author_bio: achieve ambition with intentionality, intensity, integrity & insanity.  affiliations: - @dxtipshq  - @cognition - @temporalio - @aidotengineer - @latentspacepod
time: 2026-03-09T18:14:10.000Z
text: btw if you can build a category leader open source project in ai engineering right now the market acquihire rate is ~$10-$100m per ai engineer.
  
  you do not need to figure out a business model, you do not need GTM, you do not need funding.
  
  just build things clankers want.
metrics: like_count=1745, retweet_count=46, reply_count=85, quote_count=15, bookmark_count=1052

[tweet 25]
id: 2031070907712811455
author: Lenny Rachitsky (@lennysan)
author_bio: Deeply researched product, growth, and career advice
time: 2026-03-09T18:13:34.000Z
quoted: Olivia Moore (@omooretweets)
  🚨 The @a16z consumer AI Top 100 is back!
  
  For the sixth time, we ranked consumer AI websites and mobile apps by usage (monthly unique visits and MAUs).
  
  This edition, we changed the rules. Here's why - and what the new list says about where consumer AI is heading 👇 https://t.co/4XSHw3bnGD
text: Surprises:
  - Perplexity higher than you'd think
  - removebg the 16th most popular AI tool
  - Google AI studio beating Lovable, and together they're ahead of all other vibe-coding platforms
  - JanitorAI is not what you expect
  - Three in the top 20 are AI chatbot friends
  - Google has four products in top 50
media: photo: https://pbs.twimg.com/media/HC_M0LAaMAEn8B3.jpg
metrics: like_count=495, retweet_count=54, reply_count=56, quote_count=4, bookmark_count=453

[tweet 26]
id: 2031069974681297226
author: PJ Ace (@PJaccetturo)
author_bio: Viral AI ad madman - CEO of https://t.co/YBc1ZfoyRf - 300M+ Views | Featured in Variety, Hollywood Reporter. || Join my newsletter & 100x views on your AI videos 👇🏼
time: 2026-03-09T18:09:52.000Z
quoted: Peter H. Diamandis, MD (@PeterDiamandis)
  Announcing The Future Vision XPRIZE.
  
  A global competition with $3.5M+ in prize funding challenging creators anywhere on Earth to imagine hopeful, technology-forward futures worth building toward. 
  
  Not warnings. Blueprints. Futures that inspire us to go boldly.
  
  Someone in your timeline is sitting on a vision that could change the world and doesn't know this exists yet.
  Share this. Be the reason they find it.
replied_to: PJ Ace (@PJaccetturo)
  🚨 You could win over two million dollars to make your dream film!
  
  This is going to be insane. 
  
  If you love optimistic sci-fi and you’re a filmmaker, then time to make your movie happen! 👇🏼 https://t.co/i4dB1fFzYM
text: More details here: https://t.co/rOMmlmid9f
metrics: like_count=0, retweet_count=0, reply_count=0, quote_count=0, bookmark_count=0

[tweet 27]
id: 2031065391943004510
author: Ryo Lu (@ryolu_)
author_bio: Design @Cursor_ai. Early @NotionHQ, @Stripe, built startups. I make a world where anyone can make software. Aspiring k-pop idol.
time: 2026-03-09T17:51:39.000Z
quoted: Douglas Wang (@wangdouglas)
  we’re exploring how to make AI design accessible to everyone, so anyone can create everyday designs easily.
  
  Veeso AI visualizes your ideas, content, and documents into editable designs.
  
  No templates to browse.
  No prompts to write.
  No static images.
  
  Just your ideas, turned into structured visuals you can edit and share.
  
  see it how
  
  __
  and btw we totally use  @cursor_ai build the product in the team, everyone's cooking everyday, not just fast but more ways to explore, collaborate build and ship.
text: built with @cursor_ai
  by designers, for designers
  
  when more people can code, tools come from the people closest to the problem https://t.co/RcHV8tEpwI
metrics: like_count=279, retweet_count=4, reply_count=5, quote_count=0, bookmark_count=241

[tweet 28]
id: 2031062081710236084
author: Lenny Rachitsky (@lennysan)
author_bio: Deeply researched product, growth, and career advice
time: 2026-03-09T17:38:30.000Z
quoted: Lenny Rachitsky (@lennysan)
  Marc Andreessen calls him "the best AI CEO nobody knows about."
  
  Elad Gil calls his company "the most successful, most quiet company in AI."
  
  Qasar Younis (@qasar) is the co-founder and CEO of Applied Intuition—which brings AI to vehicles, like tractors, planes, submarines, mining rigs, cars, and more.
  
  The company is valued at over $15B, making ~$1B in ARR, with 18 of the top 20 global automakers (and the U.S. Department of Defense) as customers.
  
  And @Qasar's story is wild: Born on a farm in Pakistan. Emigrated to the U.S. at age 5. Grew up in Detroit managing engine lines at GM. Harvard MBA. Became COO of @Y Combinator (during the era that funded OpenAI, Cruise, DoorDash, and Coinbase). Then left to start Applied Intuition in 2017.
  
  As Qasar shared, "not many people run a $15B+ physical AI company with revenue and free cash flow. And by not many, I think literally zero other people."
  
  In a rare and in-depth interview, we discuss:
  🔸 The counterintuitive reason he's stayed quiet and built in private
  🔸 Why reading old books and cleaning your own office makes you a better founder
  🔸 How to build a culture where the best idea wins, not the loudest voice
  🔸 Why the best companies show traction early—and what to do if yours doesn't
  🔸 How physical AI will transform farming, mining, and construction before it ever reaches your home
  
  Listen now 👇
  https://t.co/35zENzhVAN
text: My biggest takeaways from @qasar:
  
  1. The real AI revolution over the next 5 to 10 years will happen in the physical world, not in software. While everyone obsesses over ChatGPT, Claude and coding agents, the real impact will come from autonomous vehicles, mining robots, and farming equipment. They’ll save lives (over 30,000 die annually in U.S. car accidents), enable mobility for disabled people, solve labor shortages in dangerous industries where nobody wants to work, and much more.
  
  2. AI isn’t replacing jobs in industries like trucking and farming—it’s arriving just in time to fill a labor gap that already exists. The average age of a farmer in the U.S. is in the late 50s. Long-haul trucking jobs go unfilled not because people can’t do them but because the tradeoff isn’t worth it anymore; a family can choose DoorDash or Uber so the parent can pick up their kid. Qasar’s view is that physical AI will fill gaps created by demographic shifts and changing preferences, not displace workers who want those roles. He’s careful to say this doesn’t mean there are no downsides, but that the framing of “AI is coming for your job” misses the more immediate reality.
  
  3. Comparing Chinese AI companies to American AI companies is a category error. Qasar uses Huawei as his example: the company’s name means “China’s ambition,” roughly a quarter of its employees are Communist Party members, and its goal is not to grow profits but to extend the state. So when people say Chinese EVs are outcompeting Detroit, they’re comparing a government-backed entity with no profit constraint to companies like Rivian that get hammered by public investors for losing money. Qasar says that if American companies were freed from profit expectations the same way, they’d field comparable products. The point isn’t that China is incompetent or not a serious competitor; it’s that the comparison framework most people use is wrong.
  
  4. The Industrial Revolution is the best mental model for AI. Just like the late 1800s brought child labor and monopolies but also unprecedented access to healthcare, heating, cooling, and material goods, AI will have downsides we must address while delivering massive benefits. The key: don’t pump the brakes on technology to protect jobs—that hurts the people you’re trying to help most. Find solutions that account for workers while enabling progress.
  
  5. Building under the radar can be your competitive advantage. Qasar built Applied Intuition for nearly a decade without a social media presence. One of the company’s early core values was “Our best work is done alone and quietly.” His reasoning: every minute spent on a podcast, a post, or content for public consumption is a minute not spent on customers and the product. Qasar adds an important caveat—he could afford to stay quiet because he was already known in the ecosystem. Founders without an existing network may need the visibility that public presence creates.
  
  6. Qasar thinks most Silicon Valley CEOs lack taste—both in the artistic sense and in the sense of making good operational decisions—because their life experience is too narrow. A founder who grew up in Cupertino, went to Berkeley, and immediately started a company has never experienced what it’s like to be at the bottom of a 100,000-person organization. Qasar spent over a decade at GM and Bosch and says that experience—the bureaucracy, the bad tools, the disconnected leadership—directly informs how he leads Applied Intuition today. His broader point is that taste comes from exposure to a wide range of human experience: backpacking, reading old books, working in different cultures and industries.
  
  7. Successful companies almost always show traction early. If you’re two years in and the market isn’t giving you increasingly specific signals about what to build, consider resetting. The foundation might be wrong—co-founders, market, or life phase. Your first startup is practice; treat it as building the muscle of being a founder, not as your magnum opus.
  
  8. Emotions are a filter that distorts decision-making, and the goal should be to remove that filter so the “raw image” of the decision comes through. Qasar doesn’t mean leaders shouldn’t have empathy; he means that attachment to your own idea, the desire to be right, and the tribal instinct to follow the loudest voice are all emotional distortions. His practical heuristic: the same decision, presented to multiple people independently in the company, should produce the same result. If it doesn’t, some emotional filter is warping the signal. This connects to his broader philosophy of creating a culture where the best idea wins regardless of who proposed it or how senior they are.
  
  9. Qasar’s advice on company values: don’t invent them philosophically. Instead, write down the 5 to 10 things that explain why your company is already successful, and those become your values. Applied Intuition’s values include “Move fast, move safe,” “Never disappoint the customer,” “Technical mastery,” “High output matters,” “Laugh a lot,” and “Half of the work is follow-up.”
  
  10. Treat your first startup as a zero—a practice round, not destiny. Qasar tells founders leaving Applied Intuition to start companies that their first three years will likely produce nothing, and that’s fine. Founding is a craft, like woodworking. If your first table is wobbly, you don’t quit—you build another one. He thinks a lot of founders, especially first-timers, put so much pressure on themselves to succeed immediately that they miss the real value of the experience: learning and building the muscle. His own third company is the most successful by far, and he sees this pattern repeatedly. There are entire funds focused exclusively on multi-time founders for exactly this reason.
metrics: like_count=459, retweet_count=49, reply_count=34, quote_count=7, bookmark_count=815

[tweet 29]
id: 2031055873368535146
author: Peter Yang (@petergyang)
author_bio: I share extremely practical AI tutorials and interviews | Join 140K+ readers at https://t.co/XYKTmGVH14 | Product at Roblox
time: 2026-03-09T17:13:50.000Z
text: Roblox just launched two brand new programs for creators to build the next generation of novel games on the platform. 
  
  We'll provide full promotional support, direct access to Roblox staff, and a community of great devs, alumni, and investors.
  
  If interested, please apply here: https://t.co/dUznGkgFQG
media: photo: https://pbs.twimg.com/media/HC_CHgCbMAAbum8.jpg
metrics: like_count=347, retweet_count=26, reply_count=21, quote_count=1, bookmark_count=261

[tweet 30]
id: 2031051528476426671
author: Amjad Masad (@amasad)
author_bio: ceo @replit. civilizationist
time: 2026-03-09T16:56:34.000Z
quoted: Replit ⠕ (@Replit)
  We’ve been cooking something exciting 4 you https://t.co/3EAQGnB6CY
text: 👀 👀 https://t.co/uEzZLPko85
metrics: like_count=203, retweet_count=7, reply_count=22, quote_count=0, bookmark_count=34

[tweet 31]
id: 2031051280156852572
author: swyx (@swyx)
author_bio: achieve ambition with intentionality, intensity, integrity & insanity.  affiliations: - @dxtipshq  - @cognition - @temporalio - @aidotengineer - @latentspacepod
time: 2026-03-09T16:55:34.000Z
replied_to: swyx (@swyx)
  Let's say you are an agent builder and want to integrate a promising new vendor you found. 
  
  What would you be happiest to see in the docs (not based on twitter hype; you personally for your situation right now):
text: traditional API is doing quite well. there was a time in 2025 when MCP would have been clear #1 on this list
metrics: like_count=4, retweet_count=0, reply_count=2, quote_count=0, bookmark_count=0

[tweet 32]
id: 2031050798126473466
author: Google Labs (@GoogleLabs)
author_bio: Google’s home for our latest AI tools and experiments.
time: 2026-03-09T16:53:40.000Z
replied_to: Google Labs (@GoogleLabs)
  We've heard you and... it's happening :) 🌎
  
  We just expanded Pomelli to over 170 countries &amp; territories!
  
  We can't wait to see how you use it. Get started now at: https://t.co/CIkN8ugZQS https://t.co/9HIrUxR5ev
text: See availability here: https://t.co/xanayp0kHs
link: https://support.google.com/labs/answer/16945066?sjid=6934874192834788688-NC (Where you can use Pomelli - Google Labs Help)
metrics: like_count=38, retweet_count=4, reply_count=21, quote_count=2, bookmark_count=20

[tweet 33]
id: 2031050796280975724
author: Google Labs (@GoogleLabs)
author_bio: Google’s home for our latest AI tools and experiments.
time: 2026-03-09T16:53:39.000Z
text: We've heard you and... it's happening :) 🌎
  
  We just expanded Pomelli to over 170 countries &amp; territories!
  
  We can't wait to see how you use it. Get started now at: https://t.co/CIkN8ugZQS https://t.co/9HIrUxR5ev
media: photo: https://pbs.twimg.com/media/HC-8rRybQAA2qPq.jpg
link: http://labs.google/pomelli (Pomelli by Google Labs)
metrics: like_count=3100, retweet_count=217, reply_count=170, quote_count=90, bookmark_count=2611

[tweet 34]
id: 2031050659257004175
author: Nan Yu (@thenanyu)
author_bio: head of product @linear
time: 2026-03-09T16:53:06.000Z
quoted: vas (@vasuman)
  Somewhere out there is a guy who uses Notion, Superhuman, OpenClaw on a Mac Mini, Raycast, a mechanical keyboard ($400), Wispr Flow, and gets nothing done every day
text: Linear not named here because it’s how you actually get things done https://t.co/wbeiUtkYGi
metrics: like_count=38, retweet_count=0, reply_count=1, quote_count=0, bookmark_count=4

[tweet 35]
id: 2031044397987438669
author: PJ Ace (@PJaccetturo)
author_bio: Viral AI ad madman - CEO of https://t.co/YBc1ZfoyRf - 300M+ Views | Featured in Variety, Hollywood Reporter. || Join my newsletter & 100x views on your AI videos 👇🏼
time: 2026-03-09T16:28:14.000Z
quoted: Peter H. Diamandis, MD (@PeterDiamandis)
  Stories shape our future.  Story tellers manifest our destiny.  Someone, somewhere, is writing an epic screenplay that is more Star Trek, than Terminator.  A vision of a compelling and optimistic tomorrow that will shape humanity’s next few decades.
  
  The cell phone, the internet, humanoid robots, self-driving cars, voice assistants, and Starships were all imagined in science fiction before they were built by engineers. Stories are blueprints.
  
  Question: What if we asked storytellers around the world to envision an epic and compelling future for humanity, and then funded them to produce that film? What if we could flood the world with positive visions of the future, rather than dystopian predictions?  
  
  Announcing the Future Vision XPRIZE 🧵
text: 🚨 You could win over two million dollars to make your dream film!
  
  This is going to be insane. 
  
  If you love optimistic sci-fi and you’re a filmmaker, then time to make your movie happen! 👇🏼 https://t.co/i4dB1fFzYM
metrics: like_count=105, retweet_count=6, reply_count=10, quote_count=0, bookmark_count=85

[tweet 36]
id: 2031041741198123317
author: Josh Woodward (@joshwoodward)
author_bio: VP, @Google @GoogleLabs @GeminiApp @GoogleAIStudio
time: 2026-03-09T16:17:40.000Z
quoted: Arsh Goyal (@arsh_goyal)
  with the awesome @joshwoodward at Google, Ananta!
  
  What a pleasure to chat about future being built at Google and Josh being at the forefront.
  
  Had some amazing Genie, Lyria, Stitch and more demos and some great Gemini themed food!
  
  Thanks to @GoogleIndia for making this happen!
  
  #google #gemini #bengaluru
text: So good to meet IRL! Thanks again for coming! https://t.co/tpw91jRWq5
metrics: like_count=56, retweet_count=3, reply_count=2, quote_count=0, bookmark_count=2

[tweet 37]
id: 2031039953476730918
author: Josh Woodward (@joshwoodward)
author_bio: VP, @Google @GoogleLabs @GeminiApp @GoogleAIStudio
time: 2026-03-09T16:10:34.000Z
quoted: Poonam Soni (@CodeByPoonam)
  Met @joshwoodward (VP, Gemini & Google AI Studio) today at @GoogleIndia Team Gemini meet & greet.
  
  The India numbers he shared are wild:
  
  → India is a top 3 country for Gemini & NotebookLM globally
  → 100M+ images generated in India in the first week of Imagen 3
  → 2M+ people in India have already made a 30s song using Lyria
  → India leads the world in daily Gemini usage for learning
  → 3M+ NotebookLM outputs generated by Indian users in January alone
  → Gemini & NotebookLM available in 10+ Indian languages
  
  But what stayed with me wasn’t just the stats.
  
  It was seeing how deeply Google is thinking about India — not as a market to crack, but as a community that’s already leading.
  
  Plus, Google handed me a personalised portrait in Pattachitra art style, and a personalized photo book with my travel memories — both made with Gemini.
  
  Felt so special 🩵
text: Thanks again for coming! https://t.co/vLI7poDP2j
metrics: like_count=78, retweet_count=3, reply_count=3, quote_count=0, bookmark_count=3

[tweet 38]
id: 2031039919947481217
author: Riley Brown (@rileybrown)
author_bio: Cofounder of @vibecodeapp_ (the #1 full stack vibe coding platform)
time: 2026-03-09T16:10:26.000Z
text: Content Creation is going to get 10x more competitive over the next 2 years. 
  
  So many smart driven people will be laid off + AI content will make it very hard to build a following on IG+TT+YT from 0.
metrics: like_count=155, retweet_count=3, reply_count=55, quote_count=4, bookmark_count=36

[tweet 39]
id: 2031038300962820158
author: Josh Woodward (@joshwoodward)
author_bio: VP, @Google @GoogleLabs @GeminiApp @GoogleAIStudio
time: 2026-03-09T16:04:00.000Z
quoted: Vaibhav Sisinty (@VaibhavSisinty)
  Had an incredible conversation with @joshwoodward today 🔥
  
  The man leads Gemini, Google AI Studio, and Google Labs and is behind NotebookLM 💪
  
  But honestly? 
  
  What surprised me most was how fun and real he was. Full startup energy. Just pure passion for what he's building.
  
  And yes, we managed to record the whole thing 😅
text: Fun to do the demos with you! https://t.co/RLcQHVDbdw
metrics: like_count=55, retweet_count=1, reply_count=5, quote_count=0, bookmark_count=2

[tweet 40]
id: 2031038095106486677
author: Josh Woodward (@joshwoodward)
author_bio: VP, @Google @GoogleLabs @GeminiApp @GoogleAIStudio
time: 2026-03-09T16:03:11.000Z
quoted: AshutoshShrivastava (@ai_for_success)
  It was an absolute honor meeting @joshwoodward  today at the Google India office in Bengaluru. Huge thanks to @googleindia for such a wonderful experience.
  
  India is one of the top three countries globally for Gemini and NotebookLM. It also leads the world in daily Gemini usage for learning.
  
  Also had the opportunity to meet many amazing content creators from across India.
text: Great to see you in person! https://t.co/SKFYMk5Oge
metrics: like_count=116, retweet_count=1, reply_count=6, quote_count=0, bookmark_count=3

[tweet 41]
id: 2031037253586428386
author: Justine Moore (@venturetwins)
author_bio: Partner @a16z AI 🤖 and twin to @omooretweets | Investor in @elevenlabsio, @bfl_ml, @hedra_labs, @krea_ai, @MireloAI, @ShizukuAILabs, @wabi, @WaveFormsAI
time: 2026-03-09T15:59:50.000Z
text: How much are you feeling the AGI this week? https://t.co/u2bUAZT2G6
media: photo: https://pbs.twimg.com/media/HC-xnHQaYAETUr4.jpg
metrics: like_count=95, retweet_count=6, reply_count=9, quote_count=1, bookmark_count=5

[tweet 42]
id: 2031032321403744467
author: Hamel Husain (@HamelHusain)
author_bio: Bringing data science back to AI -  https://t.co/Zrmp6LRd9c  About Me: https://t.co/P6WyeKkyTa
time: 2026-03-09T15:40:14.000Z
quoted: Omar Khattab (@lateinteraction)
  Though bash is a completely valid REPL, the amount of time coding agents lose during experimentation because they iterate on scripts instead of a Jupyter-like in-memory REPL is basically dumb.
  
  Fixing 1 local bug should not require restarting the whole job. Need better scaffolds.
text: The good/bad part about agentic codeing is the barrier to getting nerdsniped is now much lower
  
  https://t.co/CiGerRgM8H https://t.co/z6p0W229YM https://t.co/K6yV7kmYrT
media: photo: https://pbs.twimg.com/media/HC-sv2uaIAExhZA.jpg
link: https://github.com/hamelsmu/hamelnb (GitHub - hamelsmu/hamelnb)
metrics: like_count=97, retweet_count=9, reply_count=10, quote_count=1, bookmark_count=104

[tweet 43]
id: 2031023703409263074
author: 郭宇 guoyu.eth (@turingou)
author_bio: Retired. 只活一次等于没活。
time: 2026-03-09T15:06:00.000Z
text: 我让 cc 用 qwen 来执行 subagent，并且给这个 agent 打分，它最后打了个 7/10 分 hhh https://t.co/5Y3hxEuApE
media: photo: https://pbs.twimg.com/media/HC-lHeQaoAAksID.png
metrics: like_count=20, retweet_count=1, reply_count=0, quote_count=0, bookmark_count=15

[tweet 44]
id: 2031021473826210191
author: Felix Lee (@felixleezd)
author_bio: CEO, @ADPList. I design products for 10M+ people. Gotrade (YC S19). Intersection of art and science.
time: 2026-03-09T14:57:08.000Z
text: unpopular opinion but people get "taste" wrong.
  
  taste isn't knowing what looks good. everyone knows what looks good.
  
  Ira Glass said it best, "all of us who do creative work, we get into it because we have good taste. but there's a gap, for the first couple years, what you're making isn't so good."
  
  what he meant is that, taste isn't about knowing what's right.
  
  taste is knowing what's wrong; even when everything on the surface looks perfect.
  
  they'll look at a technically flawless screen and say "something's off." the hierarchy is fighting the user's intent. the design is beautiful but dishonest.
  
  it's called the "aesthetic-usability effect," users assume beautiful interfaces work better, even when they don't. people with real taste know this trap and refuse to let beauty hide bad decisions.
  
  taste isn't knowing what looks good; it's knowing what's wrong.
media: photo: https://pbs.twimg.com/media/HC-jRFSagAA1jih.jpg | alt: The image features highlighted text of a quote by Ira Glass discussing the gap between taste and creative work in beginners.
metrics: like_count=16, retweet_count=3, reply_count=1, quote_count=0, bookmark_count=15

[tweet 45]
id: 2031016684664799570
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world @openclaw🦞
time: 2026-03-09T14:38:06.000Z
quoted: Jack孔@Nano Labs(NA)🇭🇰 (@JackClawAI)
  全球首个OpenClaw硬件展厅，欢迎来深圳打卡 https://t.co/wT1jkGWUdN
text: there's a store now? https://t.co/wppagFZfwT
metrics: like_count=2183, retweet_count=94, reply_count=282, quote_count=48, bookmark_count=208

[tweet 46]
id: 2031014671998980406
author: Peter Yang (@petergyang)
author_bio: I share extremely practical AI tutorials and interviews | Join 140K+ readers at https://t.co/XYKTmGVH14 | Product at Roblox
time: 2026-03-09T14:30:06.000Z
quoted: Peter Yang (@petergyang)
  "These cursors seem like a small touch, but it's the first time I've seen AI feel human."
  
  Here's my new episode with @tomkrcha (CEO of Pencil) where we covered the most mind blowing AI design tool I've ever seen.
  
  Tom showed me:
  
  ✅ Swarm mode with 6 AI agents designing an app at the same time
  
  ✅ How to load a full design canvas inside Cursor and Claude Code
  
  ✅ From design to working website in one prompt
  
  Some quotes from Tom:
  
  "We launched 2 weeks ago and now have 100,000+ users. Craft and care still matter."
  
  "Most vibe coding platforms are too linear. You should be able to explore 20 variations with agents."
  
  "All this magic on screen...behind the scenes, the agents are just writing JSON."
  
  📌 Watch now: https://t.co/swB61oLYoI
  
  Thanks to our sponsors:
  
  @linear: The AI agent platform for modern teams https://t.co/lI40xrrDsr
  
  @Replit: From 0 to full stack app in 2 min. https://t.co/w6kab0zMqN
text: My top 5 takeaways from @tomkrcha (CEO of Pencil) on how AI agents will change design:
  
  1. Making the AI agents appear more human made all the difference
  
  Technically, swarm mode is just agents writing to a JSON file. But showing cursors move on screen made all the difference in helping Pencil reach 100K users 2 weeks after launch.
  
  2. Agents and humans should be able to edit a design together
  
  Unlike vibe coding tools where you have to wait for AI, Pencil’s canvas lets you jump in and make changes mid-generation, which is a huge differentiator for me.
  
  3. Make everything agent-readable by default
  
  The design canvas is powered by a simple JSON .pen file that any agent can edit. Tom built Pencil to be “agentic from the ground up” so .pen designs live in git just like your code.
  
  4. Design is just code and vice versa
  
  You can add Pencil to Cursor, Claude Code, or Codex to edit a canvas inside your IDE/coding tool. This makes it easy for you to convert your designs to code without switching tools.
  
  5. Delight and craft still matter very much
  
  Tom originally built visual agent cursors and names to help him find and fix bugs, but the experience was so delightful that it became the product's main differentiator.
  
  📌 Watch now: https://t.co/swB61oLYoI
link: https://youtu.be/w4RY7PnfRU8
metrics: like_count=46, retweet_count=0, reply_count=5, quote_count=0, bookmark_count=78

[tweet 47]
id: 2031006858807300267
author: GREG ISENBERG (@gregisenberg)
author_bio: I drop startup ideas daily. Host @startupideaspod. CEO: @latecheckoutplz we build companies like @ideabrowser, @meetLCA, @boringmarketer etc
time: 2026-03-09T13:59:04.000Z
text: ai is going to massively increase the number of one person companies within the next ~10 years
  
  - 1 one person $10b company
  - 10 one person $1b companies
  - 100 one person $100m companies
  - 1,000 one person $10m companies
  - 10,000 one person $1m companies
metrics: like_count=643, retweet_count=36, reply_count=232, quote_count=18, bookmark_count=157

[tweet 48]
id: 2031003422367850827
author: Kent (@kentdebruin)
author_bio: streaming thoughts   ദ്ദി( • ᴗ - ) ✧
time: 2026-03-09T13:45:24.000Z
text: The person who simplifies a process eliminates a job. 
  
  The person who complicates it creates three.
metrics: like_count=3, retweet_count=0, reply_count=0, quote_count=0, bookmark_count=0

[tweet 49]
id: 2030991097829192135
author: Nan Yu (@thenanyu)
author_bio: head of product @linear
time: 2026-03-09T12:56:26.000Z
quoted: Elon Musk (@elonmusk)
  Have you ever bought anything based on an ad on this platform?
text: Why does he need a poll to answer this question https://t.co/pCfNUB1om2
metrics: like_count=25, retweet_count=0, reply_count=9, quote_count=0, bookmark_count=2

[tweet 50]
id: 2030955577351000321
author: 郭宇 guoyu.eth (@turingou)
author_bio: Retired. 只活一次等于没活。
time: 2026-03-09T10:35:17.000Z
text: https://t.co/CzUADjazML 发布了 v0.2.0 — 新增 Service Layer，首个数据服务适配器 https://t.co/tpigZzAWx8
  
  AI Agent 不只需要隔离计算环境，还需要数据。
  
  之前 Sandbank 只解决了"计算"问题——给 Agent 一个沙箱跑代码。但 Agents 要记住上下文、存储结果、跨会话协作，光有沙箱不够，还需要数据库。
  
  v0.2.0 引入 Service Layer，在 Compute（沙箱）和 Storage（卷）之外新增第三层：Data Services。首个实现是 sandbank / db9，接入 https://t.co/tpigZzAWx8 的 Serverless PostgreSQL。
  
  用它能做什么：
  - 一行代码创建数据库，凭证自动注入沙箱环境变量，Agent 零配置直连
  - 内置 Brain Schema，多 Agent 共享记忆层——memory/tasks/artifacts 三张表开箱即用
  - pgvector 语义检索，Agent 可以按"意思"搜索历史记忆，而非精确匹配
  - db9 官方 Skill 自动注入，Agent 天生会写 SQL，无需额外 prompt
  - 跨会话持久化，Agent 重启后能捡起上次的工作进度和上下文
  - 多 Agent 任务协调，一个 Agent 创建任务，另一个领取执行，状态实时同步
  - Agent 生成的代码、文档、分析结果存为 artifacts，随时可查可追溯
  - 数据库分支（branch），安全地让 Agent 在隔离副本上试验，不影响主库
  
  测试覆盖：语句 100%，行 100%，含 35 个单元测试 + 3 个真实 API 集成测试。
  
  https://t.co/2o21q1LpUV
link: http://Sandbank.dev (Sandbank — Unified Sandbox SDK for AI Agents)
link: http://db9.ai (db9 — Postgres but for agents)
link: http://Sandbank.dev
link: http://db9.ai
link: http://db9.ai
link: https://github.com/chekusu/sandbank
metrics: like_count=45, retweet_count=1, reply_count=1, quote_count=0, bookmark_count=44

[tweet 51]
id: 2030953500516229130
author: 郭宇 guoyu.eth (@turingou)
author_bio: Retired. 只活一次等于没活。
time: 2026-03-09T10:27:02.000Z
text: 好久没用 gemini cli 了，还是一如既往的抽象.... https://t.co/o18IE8YnFK
media: photo: https://pbs.twimg.com/media/HC9lXWkaIAAq0bk.jpg
metrics: like_count=26, retweet_count=0, reply_count=9, quote_count=1, bookmark_count=4

[tweet 52]
id: 2030945630600962483
author: swyx (@swyx)
author_bio: achieve ambition with intentionality, intensity, integrity & insanity.  affiliations: - @dxtipshq  - @cognition - @temporalio - @aidotengineer - @latentspacepod
time: 2026-03-09T09:55:46.000Z
text: Let's say you are an agent builder and want to integrate a promising new vendor you found. 
  
  What would you be happiest to see in the docs (not based on twitter hype; you personally for your situation right now):
poll: API (REST/OpenAPI spec)=244 | MCP=61 | CLI=203 | SKILLS.md=132 (status: open)
metrics: like_count=28, retweet_count=1, reply_count=46, quote_count=3, bookmark_count=21

[tweet 53]
id: 2030943463974551673
author: swyx (@swyx)
author_bio: achieve ambition with intentionality, intensity, integrity & insanity.  affiliations: - @dxtipshq  - @cognition - @temporalio - @aidotengineer - @latentspacepod
time: 2026-03-09T09:47:09.000Z
quoted: Robert Kirby (@probkirby)
  @swyx Since I wanted the link myself:
  https://t.co/8CmD6sCWzb
replied_to: swyx (@swyx)
  fwiw is this is you sitting on the sidelines bc you think you missed it, don’t. you’re not too old. you -are- too stubborn. you can just decide not to be. https://t.co/IDQLQ631VY https://t.co/42n2MAv9Tn
text: yes, sorry - link https://t.co/09x7IZVLvG
metrics: like_count=8, retweet_count=0, reply_count=0, quote_count=0, bookmark_count=7

[tweet 54]
id: 2030941299029790845
author: 郭宇 guoyu.eth (@turingou)
author_bio: Retired. 只活一次等于没活。
time: 2026-03-09T09:38:33.000Z
text: 现在我的 gaming pc 暴露了一个 lm studio 的 API（qwen3.5-35b-a3b）也暴露了一个 boxlite sandbox 服务，我突然想到，这不就是我之前说的推理和计算环境（沙箱）应该放在一处吗？AIDC 最理想的状态是不需要自己配置乱七八糟的就可以在隔离计算环境中访问到所有 llm才对，比如可以在 cf 的沙箱中直接访问到 cf 的 Worker AI，但目前他们的支持实在是太慢了，连 qwen 3.5 模型都没有。
metrics: like_count=19, retweet_count=0, reply_count=1, quote_count=0, bookmark_count=15

[tweet 55]
id: 2030938587152396356
author: 郭宇 guoyu.eth (@turingou)
author_bio: Retired. 只活一次等于没活。
time: 2026-03-09T09:27:46.000Z
text: 在写一个直播 vibe coding 的产品，非常有意思。本来我是想直接在 youtube 或者小红书上直播的，后来想想我从来没自己写过直播软件，要么干脆我 vibe 一个直播软件好了，既然要写，就加一些炫酷的功能：观众也可以和主播一起参与 vibe，这样大家都可以 BYOK，登录自己的订阅账户一起来开发。等我写好上线后我每天就直播自己 vibe 的过程！
metrics: like_count=85, retweet_count=1, reply_count=8, quote_count=1, bookmark_count=28

[tweet 56]
id: 2030937404606214592
author: swyx (@swyx)
author_bio: achieve ambition with intentionality, intensity, integrity & insanity.  affiliations: - @dxtipshq  - @cognition - @temporalio - @aidotengineer - @latentspacepod
time: 2026-03-09T09:23:04.000Z
replied_to: swyx (@swyx)
  4.5      5.4     3.1
               🤝 
         lab leaks https://t.co/IBkuDofATE
text: that said opus 4.6 is definitely not agi lmao https://t.co/CCSXNRetXP
media: photo: https://pbs.twimg.com/media/HC9WzpXa4AAUOgs.jpg
metrics: like_count=13, retweet_count=0, reply_count=1, quote_count=0, bookmark_count=0

[tweet 57]
id: 2030932279737098276
author: swyx (@swyx)
author_bio: achieve ambition with intentionality, intensity, integrity & insanity.  affiliations: - @dxtipshq  - @cognition - @temporalio - @aidotengineer - @latentspacepod
time: 2026-03-09T09:02:43.000Z
quoted: Marc Randolph (@marcrandolph)
  My path to entrepreneurial success was not linear, by any stretch of the imagination. I didn’t start working in tech until I was 32. I didn’t even move to California until I was 30.
  
  Before becoming an entrepreneur, I was:
  
  -The worst realtor in the state of New York
  
  -A gofer for the CEO of a sheet music company
  
  -An aspiring brand manager for flea shampoo
  
  Don’t be disillusioned if the path ahead isn’t clear. Relax.
  
  Find something that strikes your interest. And don’t be afraid to take a trail just because you can’t see the end.
text: fwiw is this is you sitting on the sidelines bc you think you missed it, don’t. you’re not too old. you -are- too stubborn. you can just decide not to be. https://t.co/IDQLQ631VY https://t.co/42n2MAv9Tn
media: photo: https://pbs.twimg.com/media/HC9SJN5aAAALEIx.jpg
metrics: like_count=415, retweet_count=24, reply_count=29, quote_count=2, bookmark_count=380

[tweet 58]
id: 2030929055475028367
author: 郭宇 guoyu.eth (@turingou)
author_bio: Retired. 只活一次等于没活。
time: 2026-03-09T08:49:54.000Z
quoted: Michael Andregg (@michaelandregg)
  We've uploaded a fruit fly. We took the @FlyWireNews   connectome of the fruit fly brain, applied a simple neuron model (@Philip_Shiu Nature 2024) and used it to control a MuJoCo physics-simulated body, closing the loop from neural activation to action.
  
  A few things I want to say about what this means and where we're going at @eonsys. 🧵
text: 上传真实的神经网络，获得赛博永生👻 https://t.co/CU8WutV0JU
metrics: like_count=41, retweet_count=7, reply_count=12, quote_count=1, bookmark_count=29

[tweet 59]
id: 2030910517406302484
author: swyx (@swyx)
author_bio: achieve ambition with intentionality, intensity, integrity & insanity.  affiliations: - @dxtipshq  - @cognition - @temporalio - @aidotengineer - @latentspacepod
time: 2026-03-09T07:36:14.000Z
quoted: Convergence Boy (@vicnaum)
  Here it is!
  Session Stripper - a skill that does surgical JSONL session stripping of your Claude conversations
  
  Remember when I reverse-engineered Claude Code's binary to add /microcompact?
  A lot of you asked for the same thing but without patching the binary
  
  Now you can do it! https://t.co/Q8YN1ZK5Ui
replied_to: swyx (@swyx)
  also got extremely mad at too many bad claude code compactions so opensourcing this tool for myself for deeply understanding wtf is still bad about claude compactions
  
  https://t.co/yEFTuulED6
  
  prob can be extended for codex compactions https://t.co/6NSDWFXMCP https://t.co/15WjmglK2c
text: useful https://t.co/8z9XscjDWI
metrics: like_count=5, retweet_count=0, reply_count=1, quote_count=0, bookmark_count=4

[tweet 60]
id: 2030907791389667351
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world @openclaw🦞
time: 2026-03-09T07:25:24.000Z
text: omg parallels has prlctl and I've been smoke-testing openclaw like a caveman so far. 🤦 https://t.co/dYPvIQYSnq
media: photo: https://pbs.twimg.com/media/HC87sXvbEAA7doZ.jpg
metrics: like_count=385, retweet_count=17, reply_count=40, quote_count=0, bookmark_count=251

[tweet 61]
id: 2030894678438985832
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world @openclaw🦞
time: 2026-03-09T06:33:18.000Z
text: 🧭 Shipped gogcli 0.12.0: Google in your terminal, now with Workspace Admin, ADC/access-token auth, Docs tab editing + Markdown/HTML export, huge Sheets upgrade, calendar aliases/subscribe, forms watches and slides templates.
  
  brew install gogcli
  https://t.co/4kvDZ80Hgj
link: https://github.com/steipete/gogcli/releases/tag/v0.12.0 (Release v0.12.0 · steipete/gogcli)
metrics: like_count=1504, retweet_count=73, reply_count=74, quote_count=14, bookmark_count=1011

[tweet 62]
id: 2030890112079253896
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world @openclaw🦞
time: 2026-03-09T06:15:09.000Z
text: If you wanna setup your own twitter mention shill/AI reply boy/derogatory terms block, this is the ruleset for claw, make it a cron, setup xurl and clawbird. https://t.co/WqL3vMd0l9
link: https://gist.github.com/steipete/0d18131a3c7b65a107a71c994cf6ac02 (Redacted Twitter mention blocklist policy)
metrics: like_count=745, retweet_count=42, reply_count=41, quote_count=9, bookmark_count=1062

[tweet 63]
id: 2030877495176962212
author: 郭宇 guoyu.eth (@turingou)
author_bio: Retired. 只活一次等于没活。
time: 2026-03-09T05:25:01.000Z
text: 刚突然想到一个事情，知识的索取我们解决了，使用 llm；智慧的分享 claude 也解决了，依赖 skill；记忆的共享我们好像还没解决或者正在解决？如果有一天，全人类的生命记忆都集中在一个数据库中，随用随取，世界会发生什么样的变化？
metrics: like_count=155, retweet_count=7, reply_count=35, quote_count=6, bookmark_count=47

[tweet 64]
id: 2030876433976119782
author: swyx (@swyx)
author_bio: achieve ambition with intentionality, intensity, integrity & insanity.  affiliations: - @dxtipshq  - @cognition - @temporalio - @aidotengineer - @latentspacepod
time: 2026-03-09T05:20:48.000Z
quoted: Dylan Patel (@dylan522p)
  Being in SF is like being in Wuhan right before the pandemic 
  Something is happening, it's gonna hit everywhere but so few people know it
text: 4.5      5.4     3.1
               🤝 
         lab leaks https://t.co/IBkuDofATE
metrics: like_count=335, retweet_count=3, reply_count=9, quote_count=1, bookmark_count=55

[tweet 65]
id: 2030875622013345949
author: Junyang Lin (@JustinLin610)
author_bio: ❤️ 🍵 ☕️ 🍷 🥃
time: 2026-03-09T05:17:34.000Z
text: sry for missing messages. will respond asap
metrics: like_count=749, retweet_count=10, reply_count=80, quote_count=5, bookmark_count=22

[tweet 66]
id: 2030864189518950849
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world @openclaw🦞
time: 2026-03-09T04:32:09.000Z
replied_to: Peter Steinberger 🦞 (@steipete)
  codex is learning fast. https://t.co/WlVTttxzNr
text: codex seems to be enjoying itself. https://t.co/RP6fMO44zl
media: photo: https://pbs.twimg.com/media/HC8UMYAWQAAN93b.png
metrics: like_count=137, retweet_count=0, reply_count=22, quote_count=1, bookmark_count=9

[tweet 67]
id: 2030863125138804969
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world @openclaw🦞
time: 2026-03-09T04:27:55.000Z
replied_to: Peter Steinberger 🦞 (@steipete)
  I'm using AI to detect and block AI. Set up a claw cron to block accounts that just post slop via birdclaw. https://t.co/6rc57M1Hjh
text: codex is learning fast. https://t.co/WlVTttxzNr
media: photo: https://pbs.twimg.com/media/HC8TPQMWEAASffd.jpg
metrics: like_count=150, retweet_count=3, reply_count=13, quote_count=0, bookmark_count=38

[tweet 68]
id: 2030860766786752678
author: 郭宇 guoyu.eth (@turingou)
author_bio: Retired. 只活一次等于没活。
time: 2026-03-09T04:18:33.000Z
text: 今天正式上线了第 9 个 vibe 项目，https://t.co/c57RMVsjtu 
  
  这个开源项目既是我在 codeben, chatben 当中的 sandbox 实践的抽象，也是接下来要发布的云端“1人公司”产品的核心组件，在 agent matrix 时代，云端沙箱成为了无比重要的基础设施，因为代码不再由预定义的程序执行，而是由语言模型现写现用，有史以来，软件不再是写死的服务，而是流动的 token。
  
  每个云端沙箱的 API 都不一样。Daytona、Fly io、Cloudflare sandbox、裸金属机上的 boxlite vm，全都互不兼容。换个 Provider 就要重写一遍基础设施代码。但很多时候，我们希望产品平衡成本和效用，并在各种沙箱之间进行互相通信，共享记忆。
  
  Sandbank 是设计用来解决这个问题的开源项目，它用一套接口解决连接各大沙箱基础设施，它支持：
  
   ✦ 命令执行、文件读写、端口暴露、快照恢复、实时交互式终端
   ✦ 内置多 Agent 会话编排 + WebSocket Relay 多沙箱通信
   ✦ Skill 注入系统，将 Skills 同步到任何云端沙箱
   ✦ 不同沙箱服务商的热替换，提升产品的横向拓展能力
  
  如果你也在编写自己的 agent matrix 系统，可能还将目光集中在 local first 的本地部署方案，例如各种 openclaw 实例，但对于大型 to C 产品和服务，沙箱是最终的解决方案，迟早你的产品会需要使用 sandbox matrix，不妨参考下 sandbank 的实现，也许会有所帮助。
  
  sanbank 在 MIT 协议下开源： 
  安装：npm i sandbank
  GitHub： https://t.co/2o21q1LpUV
  官网：https://t.co/Yqs7gah5C8
link: http://sandbank.dev (Sandbank — Unified Sandbox SDK for AI Agents)
link: http://sandbank.dev
link: https://github.com/chekusu/sandbank
link: https://sandbank.dev
metrics: like_count=222, retweet_count=18, reply_count=13, quote_count=5, bookmark_count=213

[tweet 69]
id: 2030859237992055052
author: Guillermo Rauch (@rauchg)
author_bio: @vercel CEO
time: 2026-03-09T04:12:28.000Z
quoted: Naval (@naval)
  A “computer” used to be a job title. 
  
  Then a computer became a thing humans used. 
  
  Now a computer is becoming a thing computers use.
text: The computer: https://t.co/v4TEttiYQL https://t.co/h8dbzFGUlP
link: http://vercel.com/sandbox (Sandbox)
metrics: like_count=226, retweet_count=7, reply_count=20, quote_count=1, bookmark_count=69

[tweet 70]
id: 2030854996007256550
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world @openclaw🦞
time: 2026-03-09T03:55:37.000Z
text: I'm using AI to detect and block AI. Set up a claw cron to block accounts that just post slop via birdclaw. https://t.co/6rc57M1Hjh
media: gif: https://video.twimg.com/tweet_video/HC8L2jIXkAAbZ4-.mp4
metrics: like_count=1111, retweet_count=33, reply_count=135, quote_count=12, bookmark_count=86

[tweet 71]
id: 2030853776136139109
author: swyx (@swyx)
author_bio: achieve ambition with intentionality, intensity, integrity & insanity.  affiliations: - @dxtipshq  - @cognition - @temporalio - @aidotengineer - @latentspacepod
time: 2026-03-09T03:50:46.000Z
quoted: Cole Brown (@dtcb)
  @swyx I've tried Devin at every release, and with 2.2 the models have just hit a point that it now feels simpler for me to work in Devin basically all the time. I didn't even realize it was happening until I made a small change locally and thought, "ah, I should debug on Devin"!
text: "Build a company that benefits from the models getting better and better" — @sama
  
  devin brain uses a couple dozen modelgroups and extensively evals every model for inclusion in the harness, doing a complete rewrite every few months. hearing a lot of "devin is good now" feedback but its largely the same process that the team has been running since @ScottWu46 bet on cloud agents in November 2023. agents are really, really working now and you had to have scaled harness eng + GTM to prep for this moment
media: photo: https://pbs.twimg.com/media/HC8JMLCbsAAAYvg.jpg
metrics: like_count=121, retweet_count=9, reply_count=15, quote_count=3, bookmark_count=60

[tweet 72]
id: 2030852448483737639
author: Riley Brown (@rileybrown)
author_bio: Cofounder of @vibecodeapp_ (the #1 full stack vibe coding platform)
time: 2026-03-09T03:45:29.000Z
text: yup.. Someone made a Figma for AI Agents
  
  Claude Code and OpenClaw can now create designs 10x easier...
  
  00:00 Intro
  00:46 Installing @paper 
  01:56 Connecting Claude Code to Paper
  03:38 Plan for Design
  06:23 Claude Code designs
  08:28 Iterating
  11:48 Building the React app
  13:37 Deploying
media: video: https://video.twimg.com/amplify_video/2030849414609481728/vid/avc1/1920x1080/B2ss9xsDWOu4MBcW.mp4 | duration: 897s
metrics: like_count=1482, retweet_count=104, reply_count=51, quote_count=9, bookmark_count=2880

[tweet 73]
id: 2030848677527364048
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world @openclaw🦞
time: 2026-03-09T03:30:30.000Z
text: my fav thing when I ask codex and then it disappears and returns with "YES NOW" https://t.co/vc4KMzR55p
media: photo: https://pbs.twimg.com/media/HC8GG4gXkAAksau.png
metrics: like_count=905, retweet_count=7, reply_count=59, quote_count=6, bookmark_count=56

[tweet 74]
id: 2030818328990634466
author: Robert Bye (@RobertJBye)
author_bio: Mobile Product Manager at @AnthropicAI. Board Member https://t.co/PYz00fvA2m. Previously @Figma, @Google, and @AllTrails. Jesus follower.
time: 2026-03-09T01:29:55.000Z
text: One of the best life hacks for work life balance is to get a work phone, leave it at your desk in the evenings, and turn off every Sunday.
metrics: like_count=51, retweet_count=0, reply_count=5, quote_count=0, bookmark_count=6

[tweet 75]
id: 2030816154877341759
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world @openclaw🦞
time: 2026-03-09T01:21:16.000Z
replied_to: Peter Steinberger 🦞 (@steipete)
  now codex can call openclaw via acp, so openclaw can call codex via acp. https://t.co/B2oU8wuNJG
text: Used acpx inside codex as a private backchannel into gateway/acp -> Molty on my Mac Studio, brainstormed a joke there, then had Molty call sessions_send into the live Discord session.
  
  Result: private agent-to-agent discussion, then the Discord session decides whether to post or stay silent. 
  
  Molty posted the joke only after the target session approved it. 🦞
media: photo: https://pbs.twimg.com/media/HC7oOd4WwAAffSZ.jpg
metrics: like_count=209, retweet_count=8, reply_count=19, quote_count=5, bookmark_count=137

[tweet 76]
id: 2030814162335805888
author: kepano (@kepano)
author_bio: making @obsdmd
time: 2026-03-09T01:13:21.000Z
quoted: kepano (@kepano)
  Smooth brain business:
  let's convert all our company data to plain text files so we can do analysis and training!
  
  Galaxy brain business:
  our company data is in plain text files https://t.co/2Xkii9fJcp
text: most teams still aren't thinking file-over-app enough https://t.co/R5zu2XJLlo
metrics: like_count=362, retweet_count=12, reply_count=16, quote_count=4, bookmark_count=121

[tweet 77]
id: 2030809789739966539
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world @openclaw🦞
time: 2026-03-09T00:55:59.000Z
replied_to: Peter Steinberger 🦞 (@steipete)
  Working lots in codex but sometimes I wanna bring in my openclaw for harder tasks, so extended acpx so it connects to openclaw via acp. https://t.co/rnFmpxK3OD
  
  Now I can access Molty in codex! https://t.co/CdASGindYv
text: now codex can call openclaw via acp, so openclaw can call codex via acp. https://t.co/B2oU8wuNJG
media: gif: https://video.twimg.com/tweet_video/HC7ivMbXEAAk-Uw.mp4
metrics: like_count=380, retweet_count=9, reply_count=23, quote_count=3, bookmark_count=60

[tweet 78]
id: 2030808763062505758
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world @openclaw🦞
time: 2026-03-09T00:51:54.000Z
text: Working lots in codex but sometimes I wanna bring in my openclaw for harder tasks, so extended acpx so it connects to openclaw via acp. https://t.co/rnFmpxK3OD
  
  Now I can access Molty in codex! https://t.co/CdASGindYv
media: photo: https://pbs.twimg.com/media/HC7hy7ybsAAKZun.jpg
link: https://github.com/openclaw/acpx (GitHub - openclaw/acpx: Headless CLI client for stateful Agent Client Protocol (ACP) sessions)
metrics: like_count=1514, retweet_count=76, reply_count=88, quote_count=14, bookmark_count=1031

[tweet 79]
id: 2030802737206792232
author: swyx (@swyx)
author_bio: achieve ambition with intentionality, intensity, integrity & insanity.  affiliations: - @dxtipshq  - @cognition - @temporalio - @aidotengineer - @latentspacepod
time: 2026-03-09T00:27:57.000Z
quoted: Lenny Rachitsky (@lennysan)
  100% agree. Great PMs are going to thrive in the AI era. https://t.co/LVT8HHpX0O
replied_to: swyx (@swyx)
  just realized this is the last job that will be left
  
  https://t.co/b1CwSO7Kk8
text: the God of Product Management agrees
  
  https://t.co/cOtiWZccUT
metrics: like_count=6, retweet_count=0, reply_count=1, quote_count=0, bookmark_count=0

[tweet 80]
id: 2030787218747650102
author: Justine Moore (@venturetwins)
author_bio: Partner @a16z AI 🤖 and twin to @omooretweets | Investor in @elevenlabsio, @bfl_ml, @hedra_labs, @krea_ai, @MireloAI, @ShizukuAILabs, @wabi, @WaveFormsAI
time: 2026-03-08T23:26:17.000Z
text: I suspect we already have AGI with the current models for many use cases - but the harnesses just aren’t there yet
metrics: like_count=796, retweet_count=37, reply_count=130, quote_count=17, bookmark_count=71

[tweet 81]
id: 2030783571925795069
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world @openclaw🦞
time: 2026-03-08T23:11:48.000Z
replied_to: Peter Steinberger 🦞 (@steipete)
  birdclaw import verification
text: Guess that's one way to announce a new project, lol.
  
  Needed a better way to access my tweet archive so built a new claw.
metrics: like_count=184, retweet_count=4, reply_count=24, quote_count=9, bookmark_count=12