list_id: 2007466263661232466
fetched_at: 2026-04-02 23:14 UTC
total_tweets: 83
[tweet 1]
id: 2039838798671126728
author: Amjad Masad (@amasad)
author_bio: ceo @replit. civilizationist
time: 2026-04-02T22:54:02.000Z
quoted: Samuel Spitz (@samuel_spitz)
  Your website's SEO is costing you traffic
  
  Introducing Replit SEO Audit - fix your SEO in minutes https://t.co/jjvbWl9whq
text: SEO audit your site. https://t.co/0fxrGa0dZ6
metrics: like_count=33, retweet_count=2, reply_count=4, quote_count=0, bookmark_count=27

[tweet 2]
id: 2039832290490994970
author: Nan Yu (@thenanyu)
author_bio: head of product @linear
time: 2026-04-02T22:28:10.000Z
text: Hear me out: TBPN for sports
metrics: like_count=5, retweet_count=0, reply_count=2, quote_count=0, bookmark_count=1

[tweet 3]
id: 2039831395540013319
author: kepano (@kepano)
author_bio: making @obsdmd
time: 2026-04-02T22:24:37.000Z
quoted: kepano (@kepano)
  I like @karpathy's Obsidian setup as a way to mitigate contamination risks. Keep your personal vault clean and create a messy vault for your agents.
  
  I prefer my personal Obsidian vault to be high signal:noise, and for all the content to have known origins.
  
  Keeping a separation between your personally-created artifacts and agent-created artifacts prevents contaminating your primary vault with ideas you can't source.
  
  If you let the two mix too much it will likely make Obsidian harder to use as a representation of *your* thoughts. Search, bases, quick switcher, backlinks, graph, etc, will no longer be scoped to your knowledge.
  
  Only once your agent-facing workflow produces useful artifacts would I bring those into the primary vault.
replied_to: kepano (@kepano)
  The four pieces:
  
  1. Obsidian app
  2. Obsidian Web Clipper extension to capture content in .md format
  3. Obsidian CLI so agents can interact with the full feature set of the app (e.g. backlinks, bases, etc)
  4. Obsidian Skills so agents know how to create .md, .base and .canvas
text: https://t.co/BuRVcXegXS
metrics: like_count=13, retweet_count=1, reply_count=2, quote_count=0, bookmark_count=4

[tweet 4]
id: 2039831289533227446
author: kepano (@kepano)
author_bio: making @obsdmd
time: 2026-04-02T22:24:12.000Z
quoted: Andrej Karpathy (@karpathy)
  LLM Knowledge Bases
  
  Something I'm finding very useful recently: using LLMs to build personal knowledge bases for various topics of research interest. In this way, a large fraction of my recent token throughput is going less into manipulating code, and more into manipulating knowledge (stored as markdown and images). The latest LLMs are quite good at it. So:
  
  Data ingest:
  I index source documents (articles, papers, repos, datasets, images, etc.) into a raw/ directory, then I use an LLM to incrementally "compile" a wiki, which is just a collection of .md files in a directory structure. The wiki includes summaries of all the data in raw/, backlinks, and then it categorizes data into concepts, writes articles for them, and links them all. To convert web articles into .md files I like to use the Obsidian Web Clipper extension, and then I also use a hotkey to download all the related images to local so that my LLM can easily reference them.
  
  IDE:
  I use Obsidian as the IDE "frontend" where I can view the raw data, the the compiled wiki, and the derived visualizations. Important to note that the LLM writes and maintains all of the data of the wiki, I rarely touch it directly. I've played with a few Obsidian plugins to render and view data in other ways (e.g. Marp for slides).
  
  Q&A:
  Where things get interesting is that once your wiki is big enough (e.g. mine on some recent research is ~100 articles and ~400K words), you can ask your LLM agent all kinds of complex questions against the wiki, and it will go off, research the answers, etc. I thought I had to reach for fancy RAG, but the LLM has been pretty good about auto-maintaining index files and brief summaries of all the documents and it reads all the important related data fairly easily at this ~small scale.
  
  Output:
  Instead of getting answers in text/terminal, I like to have it render markdown files for me, or slide shows (Marp format), or matplotlib images, all of which I then view again in Obsidian. You can imagine many other visual output formats depending on the query. Often, I end up "filing" the outputs back into the wiki to enhance it for further queries. So my own explorations and queries always "add up" in the knowledge base.
  
  Linting:
  I've run some LLM "health checks" over the wiki to e.g. find inconsistent data, impute missing data (with web searchers), find interesting connections for new article candidates, etc., to incrementally clean up the wiki and enhance its overall data integrity. The LLMs are quite good at suggesting further questions to ask and look into.
  
  Extra tools:
  I find myself developing additional tools to process the data, e.g. I vibe coded a small and naive search engine over the wiki, which I both use directly (in a web ui), but more often I want to hand it off to an LLM via CLI as a tool for larger queries. 
  
  Further explorations:
  As the repo grows, the natural desire is to also think about synthetic data generation + finetuning to have your LLM "know" the data in its weights instead of just context windows.
  
  TLDR: raw data from a given number of sources is collected, then compiled by an LLM into a .md wiki, then operated on by various CLIs by the LLM to do Q&A and to incrementally enhance the wiki, and all of it viewable in Obsidian. You rarely ever write or edit the wiki manually, it's the domain of the LLM. I think there is room here for an incredible new product instead of a hacky collection of scripts.
text: I like @karpathy's Obsidian setup as a way to mitigate contamination risks. Keep your personal vault clean and create a messy vault for your agents.
  
  I prefer my personal Obsidian vault to be high signal:noise, and for all the content to have known origins.
  
  Keeping a separation between your personally-created artifacts and agent-created artifacts prevents contaminating your primary vault with ideas you can't source.
  
  If you let the two mix too much it will likely make Obsidian harder to use as a representation of *your* thoughts. Search, bases, quick switcher, backlinks, graph, etc, will no longer be scoped to your knowledge.
  
  Only once your agent-facing workflow produces useful artifacts would I bring those into the primary vault.
metrics: like_count=261, retweet_count=14, reply_count=10, quote_count=5, bookmark_count=282

[tweet 5]
id: 2039826595020669096
author: Riley Brown (@rileybrown)
author_bio: Cofounder of @vibecodeapp_ (the #1 full stack vibe coding platform)
time: 2026-04-02T22:05:33.000Z
quoted: Beff (e/acc) (@beffjezos)
  Ok now I really regret not starting a podcast 2 years ago at e/acc peak
text: Should have https://t.co/dYv2KpKAvC
metrics: like_count=3, retweet_count=0, reply_count=0, quote_count=0, bookmark_count=0

[tweet 6]
id: 2039823494398001448
author: Nan Yu (@thenanyu)
author_bio: head of product @linear
time: 2026-04-02T21:53:13.000Z
quoted: Karri Saarinen (@karrisaarinen)
  Quick video on how I use @linear Agent in product work.
  
  For feature requests, I want to understand the broader pattern, not just react to one ask. 
  
  Here, it pulled from 40k+ customer requests to help me think through whether Linear should have team docs. https://t.co/S7L0HTovm2
replied_to: Nan Yu (@thenanyu)
  Or it can be a product marketer when you need
  
  https://t.co/Ekg6uNnPYE
text: Or a PM you collaborate with
  
  https://t.co/oN7v4rdYog
metrics: like_count=1, retweet_count=0, reply_count=0, quote_count=0, bookmark_count=0

[tweet 7]
id: 2039821773357854915
author: Robert Bye (@RobertJBye)
author_bio: Mobile Product Manager at @AnthropicAI. Board Member https://t.co/PYz00fvA2m. Previously @Figma, @Google, and @AllTrails. Jesus follower.
time: 2026-04-02T21:46:23.000Z
text: I’ve been watching the live streams of WWDC for 20+ years. Hopefully one day I’ll be able to go IRL. https://t.co/SFCMuXOo1T
media: photo: https://pbs.twimg.com/media/HE7nF-IbEAAzQxp.jpg
metrics: like_count=13, retweet_count=0, reply_count=1, quote_count=0, bookmark_count=1

[tweet 8]
id: 2039820803722633589
author: Nan Yu (@thenanyu)
author_bio: head of product @linear
time: 2026-04-02T21:42:32.000Z
quoted: Nan Yu (@thenanyu)
  One of our sales people showed me this Linear Agent skill they made. 
  
  They felt bad about having to go to a PM or an engineer to explain technical issues and projects so they made this — Linear always tracks the context of what you're looking at, so it just works. https://t.co/N8GsURBczK
replied_to: Nan Yu (@thenanyu)
  Linear can act as an engineer in a pinch
  
  https://t.co/IBgYtDLwPu
text: Or it can be a product marketer when you need
  
  https://t.co/Ekg6uNnPYE
metrics: like_count=1, retweet_count=0, reply_count=1, quote_count=0, bookmark_count=0

[tweet 9]
id: 2039820651549106541
author: Nan Yu (@thenanyu)
author_bio: head of product @linear
time: 2026-04-02T21:41:56.000Z
quoted: Nan Yu (@thenanyu)
  If you're a PM or on sales or support, how many times have you needed to bother an engineer to find out exactly how the app works? 
  
  I wanted to know exactly what the default setting was for a personal configuration for all of our users. 
  
  You never need to ask an engineer again for this kind of thing, because Linear Agent can just read the code and tell you.
replied_to: Nan Yu (@thenanyu)
  You can talk to Linear now btw. It’s awesome. https://t.co/zshj6GXamD
text: Linear can act as an engineer in a pinch
  
  https://t.co/IBgYtDLwPu
metrics: like_count=3, retweet_count=0, reply_count=1, quote_count=0, bookmark_count=0

[tweet 10]
id: 2039819885203595631
author: Nan Yu (@thenanyu)
author_bio: head of product @linear
time: 2026-04-02T21:38:53.000Z
quoted: kais (@kais_rad)
  NOOOOOOOOOOOOO https://t.co/DxC9WxUu5h
text: You can talk to Linear now btw. It’s awesome. https://t.co/zshj6GXamD
metrics: like_count=28, retweet_count=0, reply_count=7, quote_count=0, bookmark_count=4

[tweet 11]
id: 2039819457720430919
author: kepano (@kepano)
author_bio: making @obsdmd
time: 2026-04-02T21:37:11.000Z
replied_to: kepano (@kepano)
  More and more people are using Obsidian as a local wiki to read things your agents are researching and writing.
  
  It works best with a separate Obsidian vault that you can fill it with content, e.g. via Obsidian Web Clipper. https://t.co/VOjTtqOws2
text: The four pieces:
  
  1. Obsidian app
  2. Obsidian Web Clipper extension to capture content in .md format
  3. Obsidian CLI so agents can interact with the full feature set of the app (e.g. backlinks, bases, etc)
  4. Obsidian Skills so agents know how to create .md, .base and .canvas
metrics: like_count=125, retweet_count=3, reply_count=7, quote_count=0, bookmark_count=114

[tweet 12]
id: 2039819423360663684
author: Riley Brown (@rileybrown)
author_bio: Cofounder of @vibecodeapp_ (the #1 full stack vibe coding platform)
time: 2026-04-02T21:37:03.000Z
quoted: Ashni (@ashnichrist)
  "TBPN is a podcast"
  
  I get the framing, but if this was true... AI is already creating podcasts & TBPN would be commoditized af.
  
  It's a live stream. And the distinction is why OpenAI acquired them.
  
  TBPN happens in real time. When a CEO says something unexpected, there's no edit. When news breaks, they cover it live
  
  This is the only way to keep up with the pace of tech & AI news (thanks, Anthropic...)
  
  OpenAI bought a format that is fundamentally resistant to automation
  
  The format IS the value
  
  CEOs who acquire produced podcasts with no live component will be in for a rude awakening
  
  The trust & credibility generation is not the same
text: Live Elite Media. https://t.co/AvKEwLR1kv
metrics: like_count=6, retweet_count=0, reply_count=1, quote_count=0, bookmark_count=0

[tweet 13]
id: 2039819092035780633
author: kepano (@kepano)
author_bio: making @obsdmd
time: 2026-04-02T21:35:44.000Z
quoted: Andrej Karpathy (@karpathy)
  LLM Knowledge Bases
  
  Something I'm finding very useful recently: using LLMs to build personal knowledge bases for various topics of research interest. In this way, a large fraction of my recent token throughput is going less into manipulating code, and more into manipulating knowledge (stored as markdown and images). The latest LLMs are quite good at it. So:
  
  Data ingest:
  I index source documents (articles, papers, repos, datasets, images, etc.) into a raw/ directory, then I use an LLM to incrementally "compile" a wiki, which is just a collection of .md files in a directory structure. The wiki includes summaries of all the data in raw/, backlinks, and then it categorizes data into concepts, writes articles for them, and links them all. To convert web articles into .md files I like to use the Obsidian Web Clipper extension, and then I also use a hotkey to download all the related images to local so that my LLM can easily reference them.
  
  IDE:
  I use Obsidian as the IDE "frontend" where I can view the raw data, the the compiled wiki, and the derived visualizations. Important to note that the LLM writes and maintains all of the data of the wiki, I rarely touch it directly. I've played with a few Obsidian plugins to render and view data in other ways (e.g. Marp for slides).
  
  Q&A:
  Where things get interesting is that once your wiki is big enough (e.g. mine on some recent research is ~100 articles and ~400K words), you can ask your LLM agent all kinds of complex questions against the wiki, and it will go off, research the answers, etc. I thought I had to reach for fancy RAG, but the LLM has been pretty good about auto-maintaining index files and brief summaries of all the documents and it reads all the important related data fairly easily at this ~small scale.
  
  Output:
  Instead of getting answers in text/terminal, I like to have it render markdown files for me, or slide shows (Marp format), or matplotlib images, all of which I then view again in Obsidian. You can imagine many other visual output formats depending on the query. Often, I end up "filing" the outputs back into the wiki to enhance it for further queries. So my own explorations and queries always "add up" in the knowledge base.
  
  Linting:
  I've run some LLM "health checks" over the wiki to e.g. find inconsistent data, impute missing data (with web searchers), find interesting connections for new article candidates, etc., to incrementally clean up the wiki and enhance its overall data integrity. The LLMs are quite good at suggesting further questions to ask and look into.
  
  Extra tools:
  I find myself developing additional tools to process the data, e.g. I vibe coded a small and naive search engine over the wiki, which I both use directly (in a web ui), but more often I want to hand it off to an LLM via CLI as a tool for larger queries. 
  
  Further explorations:
  As the repo grows, the natural desire is to also think about synthetic data generation + finetuning to have your LLM "know" the data in its weights instead of just context windows.
  
  TLDR: raw data from a given number of sources is collected, then compiled by an LLM into a .md wiki, then operated on by various CLIs by the LLM to do Q&A and to incrementally enhance the wiki, and all of it viewable in Obsidian. You rarely ever write or edit the wiki manually, it's the domain of the LLM. I think there is room here for an incredible new product instead of a hacky collection of scripts.
text: More and more people are using Obsidian as a local wiki to read things your agents are researching and writing.
  
  It works best with a separate Obsidian vault that you can fill it with content, e.g. via Obsidian Web Clipper. https://t.co/VOjTtqOws2
metrics: like_count=481, retweet_count=19, reply_count=17, quote_count=1, bookmark_count=365

[tweet 14]
id: 2039817584401653877
author: Riley Brown (@rileybrown)
author_bio: Cofounder of @vibecodeapp_ (the #1 full stack vibe coding platform)
time: 2026-04-02T21:29:44.000Z
quoted: jameson (big deck energy) (@jamesonhaslam)
  Heard the TBPN number is 10 figs
text: Someone confirm or deny this very very curious. https://t.co/PsMMuTri3R
metrics: like_count=1, retweet_count=0, reply_count=1, quote_count=0, bookmark_count=1

[tweet 15]
id: 2039817231660687827
author: Riley Brown (@rileybrown)
author_bio: Cofounder of @vibecodeapp_ (the #1 full stack vibe coding platform)
time: 2026-04-02T21:28:20.000Z
quoted: Austin Rief ☕️ (@austin_rief)
  Wow. 
  
  To sell a highly profitable independent media company like TBPN, the price must have been insanely high.
text: My guess is 350M https://t.co/rTLbnZnWOt
metrics: like_count=12, retweet_count=0, reply_count=6, quote_count=0, bookmark_count=3

[tweet 16]
id: 2039815220953219565
author: Riley Brown (@rileybrown)
author_bio: Cofounder of @vibecodeapp_ (the #1 full stack vibe coding platform)
time: 2026-04-02T21:20:21.000Z
text: The reallocation of resources from sora to tbpn says everything about where content is going...
  
  Elite human media will win 
  AI Slop will go to zero
metrics: like_count=40, retweet_count=1, reply_count=8, quote_count=2, bookmark_count=8

[tweet 17]
id: 2039812100206604787
author: swyx (@swyx)
author_bio: achieve ambition with intentionality, intensity, integrity & insanity.  affiliations: - @dxtipshq  - @cognition - @temporalio - @aidotengineer - @latentspacepod
time: 2026-04-02T21:07:57.000Z
quoted: zerohedge (@zerohedge)
  *OPENAI ACQUIRED TBPN FOR ‘LOW HUNDREDS OF MILLIONS’: FT
replied_to: swyx (@swyx)
  wait… you guys are selling podcasts??!
  
  (congrats @tbpn! time for dario x dwarkesh?) https://t.co/D4xzsdY4EG
text: HOW LOW IS LOW
  
  HOW LOW
  
  IS LOW
  
  https://t.co/dx03S4DXtx
metrics: like_count=11, retweet_count=0, reply_count=4, quote_count=0, bookmark_count=1

[tweet 18]
id: 2039808711452246261
author: Andrej Karpathy (@karpathy)
author_bio: I like to train large deep neural nets. Previously Director of AI @ Tesla, founding team @ OpenAI, PhD @ Stanford.
time: 2026-04-02T20:54:29.000Z
replied_to: Andrej Karpathy (@karpathy)
  LLM Knowledge Bases
  
  Something I'm finding very useful recently: using LLMs to build personal knowledge bases for various topics of research interest. In this way, a large fraction of my recent token throughput is going less into manipulating code, and more into manipulating knowledge (stored as markdown and images). The latest LLMs are quite good at it. So:
  
  Data ingest:
  I index source documents (articles, papers, repos, datasets, images, etc.) into a raw/ directory, then I use an LLM to incrementally "compile" a wiki, which is just a collection of .md files in a directory structure. The wiki includes summaries of all the data in raw/, backlinks, and then it categorizes data into concepts, writes articles for them, and links them all. To convert web articles into .md files I like to use the Obsidian Web Clipper extension, and then I also use a hotkey to download all the related images to local so that my LLM can easily reference them.
  
  IDE:
  I use Obsidian as the IDE "frontend" where I can view the raw data, the the compiled wiki, and the derived visualizations. Important to note that the LLM writes and maintains all of the data of the wiki, I rarely touch it directly. I've played with a few Obsidian plugins to render and view data in other ways (e.g. Marp for slides).
  
  Q&A:
  Where things get interesting is that once your wiki is big enough (e.g. mine on some recent research is ~100 articles and ~400K words), you can ask your LLM agent all kinds of complex questions against the wiki, and it will go off, research the answers, etc. I thought I had to reach for fancy RAG, but the LLM has been pretty good about auto-maintaining index files and brief summaries of all the documents and it reads all the important related data fairly easily at this ~small scale.
  
  Output:
  Instead of getting answers in text/terminal, I like to have it render markdown files for me, or slide shows (Marp format), or matplotlib images, all of which I then view again in Obsidian. You can imagine many other visual output formats depending on the query. Often, I end up "filing" the outputs back into the wiki to enhance it for further queries. So my own explorations and queries always "add up" in the knowledge base.
  
  Linting:
  I've run some LLM "health checks" over the wiki to e.g. find inconsistent data, impute missing data (with web searchers), find interesting connections for new article candidates, etc., to incrementally clean up the wiki and enhance its overall data integrity. The LLMs are quite good at suggesting further questions to ask and look into.
  
  Extra tools:
  I find myself developing additional tools to process the data, e.g. I vibe coded a small and naive search engine over the wiki, which I both use directly (in a web ui), but more often I want to hand it off to an LLM via CLI as a tool for larger queries. 
  
  Further explorations:
  As the repo grows, the natural desire is to also think about synthetic data generation + finetuning to have your LLM "know" the data in its weights instead of just context windows.
  
  TLDR: raw data from a given number of sources is collected, then compiled by an LLM into a .md wiki, then operated on by various CLIs by the LLM to do Q&A and to incrementally enhance the wiki, and all of it viewable in Obsidian. You rarely ever write or edit the wiki manually, it's the domain of the LLM. I think there is room here for an incredible new product instead of a hacky collection of scripts.
text: Oh and in the natural extrapolation, you could imagine that every question to a frontier grade LLM spawns a team of LLMs to automate the whole thing: iteratively construct an entire ephemeral wiki, lint it, loop a few times, then write a full report. Way beyond a `.decode()`.
metrics: like_count=374, retweet_count=16, reply_count=30, quote_count=2, bookmark_count=144

[tweet 19]
id: 2039806728087457907
author: Justine Moore (@venturetwins)
author_bio: Partner @a16z AI 🤖 and twin to @omooretweets | Investor in @elevenlabs, @bfl_ml, @hedra_labs, @krea_ai, @MireloAI, @ShizukuAILabs, @wabi, @WaveFormsAI
time: 2026-04-02T20:46:36.000Z
quoted: Jordi Hays (@jordihays)
  TBPN has been acquired by OpenAI
  
  The world is changing quickly but TBPN will stay the same. Live every weekday just with a lot more resources.
  
  Thank you to everyone that has been a part of this journey big or small. We are 17 months in and unironically just getting started. https://t.co/TLvPxxMGVe
text: TBPN? The AI research company? https://t.co/VsevNpwmRJ https://t.co/czioGNToYR
media: photo: https://pbs.twimg.com/media/HE7ZaPLbYAAtuA2.jpg
metrics: like_count=45, retweet_count=2, reply_count=2, quote_count=0, bookmark_count=3

[tweet 20]
id: 2039805659525644595
author: Andrej Karpathy (@karpathy)
author_bio: I like to train large deep neural nets. Previously Director of AI @ Tesla, founding team @ OpenAI, PhD @ Stanford.
time: 2026-04-02T20:42:21.000Z
text: LLM Knowledge Bases
  
  Something I'm finding very useful recently: using LLMs to build personal knowledge bases for various topics of research interest. In this way, a large fraction of my recent token throughput is going less into manipulating code, and more into manipulating knowledge (stored as markdown and images). The latest LLMs are quite good at it. So:
  
  Data ingest:
  I index source documents (articles, papers, repos, datasets, images, etc.) into a raw/ directory, then I use an LLM to incrementally "compile" a wiki, which is just a collection of .md files in a directory structure. The wiki includes summaries of all the data in raw/, backlinks, and then it categorizes data into concepts, writes articles for them, and links them all. To convert web articles into .md files I like to use the Obsidian Web Clipper extension, and then I also use a hotkey to download all the related images to local so that my LLM can easily reference them.
  
  IDE:
  I use Obsidian as the IDE "frontend" where I can view the raw data, the the compiled wiki, and the derived visualizations. Important to note that the LLM writes and maintains all of the data of the wiki, I rarely touch it directly. I've played with a few Obsidian plugins to render and view data in other ways (e.g. Marp for slides).
  
  Q&A:
  Where things get interesting is that once your wiki is big enough (e.g. mine on some recent research is ~100 articles and ~400K words), you can ask your LLM agent all kinds of complex questions against the wiki, and it will go off, research the answers, etc. I thought I had to reach for fancy RAG, but the LLM has been pretty good about auto-maintaining index files and brief summaries of all the documents and it reads all the important related data fairly easily at this ~small scale.
  
  Output:
  Instead of getting answers in text/terminal, I like to have it render markdown files for me, or slide shows (Marp format), or matplotlib images, all of which I then view again in Obsidian. You can imagine many other visual output formats depending on the query. Often, I end up "filing" the outputs back into the wiki to enhance it for further queries. So my own explorations and queries always "add up" in the knowledge base.
  
  Linting:
  I've run some LLM "health checks" over the wiki to e.g. find inconsistent data, impute missing data (with web searchers), find interesting connections for new article candidates, etc., to incrementally clean up the wiki and enhance its overall data integrity. The LLMs are quite good at suggesting further questions to ask and look into.
  
  Extra tools:
  I find myself developing additional tools to process the data, e.g. I vibe coded a small and naive search engine over the wiki, which I both use directly (in a web ui), but more often I want to hand it off to an LLM via CLI as a tool for larger queries. 
  
  Further explorations:
  As the repo grows, the natural desire is to also think about synthetic data generation + finetuning to have your LLM "know" the data in its weights instead of just context windows.
  
  TLDR: raw data from a given number of sources is collected, then compiled by an LLM into a .md wiki, then operated on by various CLIs by the LLM to do Q&A and to incrementally enhance the wiki, and all of it viewable in Obsidian. You rarely ever write or edit the wiki manually, it's the domain of the LLM. I think there is room here for an incredible new product instead of a hacky collection of scripts.
metrics: like_count=7115, retweet_count=673, reply_count=510, quote_count=155, bookmark_count=9907

[tweet 21]
id: 2039796094973202503
author: Matan Grinberg (@matanSF)
author_bio: ceo @FactoryAI
time: 2026-04-02T20:04:21.000Z
quoted: Factory (@FactoryAI)
  Our results show that tasks involving classic enterprise languages like COBOL, Fortran, and C89 are significantly harder for agents.
  
  Despite this, frontier agents are already capable of automating complex work and are rapidly closing the performance gap compared to modern stacks.
text: No one model is best for legacy code, but if I had to pick right now, it would be @tbpn's GPT-5.3-Codex https://t.co/GL9WI9pClH
metrics: like_count=23, retweet_count=1, reply_count=1, quote_count=0, bookmark_count=4

[tweet 22]
id: 2039795988433346803
author: Logan Kilpatrick (@OfficialLoganK)
author_bio: Member of technical staff, working on @GoogleAIStudio, the Gemini API, & Kaggle. My views!
time: 2026-04-02T20:03:55.000Z
replied_to: Logan Kilpatrick (@OfficialLoganK)
  Today we are rolling out service tiers in the Gemini API! You can now (optionally) set "flex" or "priority".
  
  In the case of flex, this will save you ~50% on API costs (with lower reliability).
  
  In the case of priority, this will cost ~80% more but give you higher priority!
text: This is available to Tier 2 and Tier 3 projects to start on most of our standard models! Hope this helps for folks trying to balance cost, reliability, and throughput! 
  
  Read more: https://t.co/tz2NXfPMPZ
link: https://blog.google/innovation-and-ai/technology/developers-tools/introducing-flex-and-priority-inference/ (New ways to balance cost and reliability in the Gemini API)
metrics: like_count=53, retweet_count=1, reply_count=3, quote_count=0, bookmark_count=8

[tweet 23]
id: 2039795986713776135
author: Logan Kilpatrick (@OfficialLoganK)
author_bio: Member of technical staff, working on @GoogleAIStudio, the Gemini API, & Kaggle. My views!
time: 2026-04-02T20:03:55.000Z
text: Today we are rolling out service tiers in the Gemini API! You can now (optionally) set "flex" or "priority".
  
  In the case of flex, this will save you ~50% on API costs (with lower reliability).
  
  In the case of priority, this will cost ~80% more but give you higher priority!
metrics: like_count=612, retweet_count=19, reply_count=57, quote_count=12, bookmark_count=110

[tweet 24]
id: 2039794000392266212
author: Matan Grinberg (@matanSF)
author_bio: ceo @FactoryAI
time: 2026-04-02T19:56:01.000Z
quoted: Factory (@FactoryAI)
  No major benchmark is designed for COBOL, Fortran, or Assembly - the languages powering trillions in transactions and infrastructure that must be modernized or risk catastrophic failure.
  
  We built Legacy-Bench to measure frontier agents on the code the world actually runs on. https://t.co/pM8Pwuxe6M
text: Legacy code runs much of the world that we do not see.
  
  As part of our work with some of the largest financial institutions and highly regulated enterprises, we are excited to release the latest results from Legacy-Bench. https://t.co/irvtKJIc13
metrics: like_count=20, retweet_count=4, reply_count=1, quote_count=0, bookmark_count=8

[tweet 25]
id: 2039786025892086135
author: Hamel Husain (@HamelHusain)
author_bio: Bringing data science back to AI -  https://t.co/Zrmp6LRd9c  About Me: https://t.co/P6WyeKkyTa
time: 2026-04-02T19:24:20.000Z
quoted: Bryan Bischof fka Dr. Donut (@BEBischof)
  Everything is dead.
  
  I'm sick of it.
  
  Here's our answer: https://t.co/382sDEq6MO https://t.co/vuqFFfSkkd
text: Yup https://t.co/RniCtraFXS https://t.co/Rh7L1g5FBe
media: photo: https://pbs.twimg.com/media/HE7Gj8kbsAAsAAb.jpg
metrics: like_count=7, retweet_count=2, reply_count=1, quote_count=0, bookmark_count=1

[tweet 26]
id: 2039782190838686088
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world @openclaw🦞
time: 2026-04-02T19:09:06.000Z
text: Prediction: This is gonna kill some oss projects.
  
  "On the kernel security list we've seen a huge bump of reports. We were between 2 and 3 per week maybe two years ago, then reached probably 10 a week over the last year with the only difference being only AI slop, and now since the beginning of the year we're around 5-10 per day depending on the days (fridays and tuesdays seem the worst). Now most of these reports are correct, to the point that we had to bring in more maintainers to help us." https://t.co/rK7evxZjUR
link: https://lwn.net/Articles/1065620/
metrics: like_count=705, retweet_count=39, reply_count=62, quote_count=15, bookmark_count=297

[tweet 27]
id: 2039781618408124786
author: Lenny Rachitsky (@lennysan)
author_bio: Deeply researched product, growth, and career advice
time: 2026-04-02T19:06:49.000Z
replied_to: Lenny Rachitsky (@lennysan)
  "Using coding agents well is taking every inch of my 25 years of experience as a software engineer."
  
  Simon Willison (@simonw) is one of the most prolific independent software engineers and most trusted voices on how AI is changing the craft of building software. He co-created Django, coined the term "prompt injection," and popularized the terms "agentic engineering" and "AI slop."
  
  In our in-depth conversation, we discuss:
  🔸 Why November 2025 was an inflection point
  🔸 The "dark factory" pattern
  🔸 Why mid-career engineers (not juniors) are the most at risk right now
  🔸 Three agentic engineering patterns he uses daily: red/green TDD, thin templates, hoarding
  🔸 Why he writes 95% of his code from his phone while walking the dog
  🔸 Why he thinks we're headed for an AI Challenger disaster
  🔸 How a pelican riding a bicycle became the unofficial benchmark for AI model quality
  
  Listen now 👇
  https://t.co/wlEIyOehU8
text: Thank you to our season's sponsors:
  🏆 @WorkOS — Modern identity platform for B2B SaaS, free up to 1 million MAUs: https://t.co/XH3bKme6v9
  🏆 @TrustVanta — automate compliance, manage risk, and accelerate trust with AI: https://t.co/JHcQhNsceu
  
  Also available on:
  • Spotify: https://t.co/GpFzyfRh9E
  • Apple: https://t.co/I7KhbMR0pN
media: photo: https://pbs.twimg.com/media/HE7CdcObAAA6WNS.jpg
link: https://workos.com/lenny (WorkOS — Your app, Enterprise Ready.)
link: https://vanta.com/lenny (Take a demo of the Vanta platform and receive $1,000 off)
link: https://workos.com/lenny
link: https://vanta.com/lenny
link: https://open.spotify.com/episode/0DVjwLT6wgtscdB78Qf1BQ?si=obMEd6BWTK6UOBmftlHPXg
link: https://podcasts.apple.com/us/podcast/an-ai-state-of-the-union-weve-passed-the/id1627920305?i=1000758850377
metrics: like_count=2, retweet_count=1, reply_count=0, quote_count=0, bookmark_count=1

[tweet 28]
id: 2039781609755521232
author: Lenny Rachitsky (@lennysan)
author_bio: Deeply researched product, growth, and career advice
time: 2026-04-02T19:06:47.000Z
text: "Using coding agents well is taking every inch of my 25 years of experience as a software engineer."
  
  Simon Willison (@simonw) is one of the most prolific independent software engineers and most trusted voices on how AI is changing the craft of building software. He co-created Django, coined the term "prompt injection," and popularized the terms "agentic engineering" and "AI slop."
  
  In our in-depth conversation, we discuss:
  🔸 Why November 2025 was an inflection point
  🔸 The "dark factory" pattern
  🔸 Why mid-career engineers (not juniors) are the most at risk right now
  🔸 Three agentic engineering patterns he uses daily: red/green TDD, thin templates, hoarding
  🔸 Why he writes 95% of his code from his phone while walking the dog
  🔸 Why he thinks we're headed for an AI Challenger disaster
  🔸 How a pelican riding a bicycle became the unofficial benchmark for AI model quality
  
  Listen now 👇
  https://t.co/wlEIyOehU8
link: https://youtu.be/wc8FBhQtdsA
metrics: like_count=174, retweet_count=20, reply_count=21, quote_count=2, bookmark_count=189

[tweet 29]
id: 2039780768847958359
author: Ryo Lu (@ryolu_)
author_bio: Design @Cursor_ai. Early @NotionHQ, @Stripe, built startups. I make a world where anyone can make software. Aspiring k-pop idol.
time: 2026-04-02T19:03:27.000Z
quoted: Cursor (@cursor_ai)
  We’re introducing Cursor 3. It is simpler, more powerful, and built for a world where all code is written by agents, while keeping the depth of a development environment. https://t.co/rXR9vaZDnO
text: Cursor 3 is here.
  Where power meets simplicity.
  Works across all your projects, local and cloud.
  
  It starts simple, then unfolds more tools when you need them – so you stay in flow and in control. Enjoy! https://t.co/xPSyIUcIiB
metrics: like_count=218, retweet_count=11, reply_count=17, quote_count=3, bookmark_count=25

[tweet 30]
id: 2039780060169707599
author: Matt Turck (@mattturck)
author_bio: VC at @FirstMarkCap.  Host: MAD Podcast; Organizer: Data Driven NYC, Author: MAD Landscape.
time: 2026-04-02T19:00:38.000Z
text: if you're running traditional marketing playbooks in an age where OpenAI acquires TBPN, you're ngmi.  The game has completely changed
metrics: like_count=86, retweet_count=5, reply_count=12, quote_count=1, bookmark_count=10

[tweet 31]
id: 2039778042466246979
author: GREG ISENBERG (@gregisenberg)
author_bio: I drop startup ideas daily. Host @startupideaspod. CEO: @latecheckoutplz we build companies like @ideabrowser, @meetLCA, @boringmarketer etc
time: 2026-04-02T18:52:37.000Z
quoted: John Coogan (@johncoogan)
  TBPN has been acquired by OpenAI!
  
  The show is staying the same and we’ll continue to go live at 11am pacific every weekday.
  
  This is a full circle moment for me as I’ve worked with @sama for well over a decade. He funded my first company in 2013. Then helped us fix a serious logjam during a critical funding round a few years later. When I took my second company through YC, he was president at the time, and then when I joined Founders Fund, the first deal I saw in motion was the post-ChatGPT round in late 2022. And as we started growing TBPN last year, he was the very first lab lead to join the show.
   
  Thank you to everyone that has been a part of TBPN until now. The last year has been the most fun and rewarding part of my career and we’re excited to have more resources than ever going forward.
text: I think we’ll see a lot more creator/media acquisitions over the next 5 years in the age of AI https://t.co/vuZzCpAsrO
metrics: like_count=300, retweet_count=11, reply_count=59, quote_count=4, bookmark_count=52

[tweet 32]
id: 2039777772701413396
author: Amjad Masad (@amasad)
author_bio: ceo @replit. civilizationist
time: 2026-04-02T18:51:32.000Z
text: Started a sales office in Salt Lake City, Utah. If you’re based there, consider joining the team! https://t.co/vZw366XtEU
media: photo: https://pbs.twimg.com/media/HE6_EqHacAAXMAk.jpg
metrics: like_count=332, retweet_count=8, reply_count=35, quote_count=4, bookmark_count=21

[tweet 33]
id: 2039774118443421887
author: Amjad Masad (@amasad)
author_bio: ceo @replit. civilizationist
time: 2026-04-02T18:37:01.000Z
quoted: Replit ⠕ (@Replit)
  You can now fully customize the signup experience for your Replit Apps!  
  
  - Customize layout, colors, fonts and more 
  - Your app users don't need a Replit account 
  - Separate dev &amp; prod environments for auth for better security 
  - No setup required- experience powered by @clerk https://t.co/0pZkOIhvN7
text: No-setup enterprise-grade auth solution for everyone. https://t.co/Udl430LVTR
metrics: like_count=146, retweet_count=3, reply_count=23, quote_count=2, bookmark_count=53

[tweet 34]
id: 2039773740586918137
author: Sam Altman (@sama)
author_bio: AI is cool i guess
time: 2026-04-02T18:35:31.000Z
text: TBPN is my favorite tech show.
  
  We want them to keep that going and for them to do what they do so well.
  
  I don't expect them to go any easier on us, am sure I'll do my part to help enable that with occasional stupid decisions.
metrics: like_count=3778, retweet_count=113, reply_count=500, quote_count=101, bookmark_count=288

[tweet 35]
id: 2039773480980480431
author: swyx (@swyx)
author_bio: achieve ambition with intentionality, intensity, integrity & insanity.  affiliations: - @dxtipshq  - @cognition - @temporalio - @aidotengineer - @latentspacepod
time: 2026-04-02T18:34:29.000Z
text: wait… you guys are selling podcasts??!
  
  (congrats @tbpn! time for dario x dwarkesh?) https://t.co/D4xzsdY4EG
media: gif: https://video.twimg.com/tweet_video/HE67KgIa0AA0BuM.mp4
metrics: like_count=55, retweet_count=1, reply_count=12, quote_count=0, bookmark_count=2

[tweet 36]
id: 2039773448814436581
author: Amjad Masad (@amasad)
author_bio: ceo @replit. civilizationist
time: 2026-04-02T18:34:22.000Z
quoted: Amjad Masad (@amasad)
  One person billion dollar company has been achieved: @galligator https://t.co/XMjsLCRXV9
text: From the founder: “Replit is one of my absolute favorite tools to build with” https://t.co/DcjTsfAJmH
metrics: like_count=142, retweet_count=9, reply_count=14, quote_count=1, bookmark_count=46

[tweet 37]
id: 2039771067342807374
author: Nan Yu (@thenanyu)
author_bio: head of product @linear
time: 2026-04-02T18:24:54.000Z
quoted: Matt Slotnick (@matt_slotnick)
  @thenanyu it’s the main project. attention is all you need
replied_to: Nan Yu (@thenanyu)
  🤔 https://t.co/YqfLCTKBPE https://t.co/GLsR6PcKhX
text: of course
  https://t.co/WHeHCcqgLx
metrics: like_count=9, retweet_count=0, reply_count=0, quote_count=0, bookmark_count=0

[tweet 38]
id: 2039769365617217891
author: Nan Yu (@thenanyu)
author_bio: head of product @linear
time: 2026-04-02T18:18:08.000Z
quoted: John Coogan (@johncoogan)
  TBPN has been acquired by OpenAI!
  
  The show is staying the same and we’ll continue to go live at 11am pacific every weekday.
  
  This is a full circle moment for me as I’ve worked with @sama for well over a decade. He funded my first company in 2013. Then helped us fix a serious logjam during a critical funding round a few years later. When I took my second company through YC, he was president at the time, and then when I joined Founders Fund, the first deal I saw in motion was the post-ChatGPT round in late 2022. And as we started growing TBPN last year, he was the very first lab lead to join the show.
   
  Thank you to everyone that has been a part of TBPN until now. The last year has been the most fun and rewarding part of my career and we’re excited to have more resources than ever going forward.
text: 🤔 https://t.co/YqfLCTKBPE https://t.co/GLsR6PcKhX
media: photo: https://pbs.twimg.com/media/HE63A2eawAA0g0f.png
metrics: like_count=121, retweet_count=2, reply_count=11, quote_count=0, bookmark_count=5

[tweet 39]
id: 2039749590891856270
author: Julie Zhuo (@joulee)
author_bio: Founder @teamSundial. Angel investor. Author of "The Making of a Manager" https://t.co/6HwJhCW5Hi. Obsessed with systems. Design + data person.
time: 2026-04-02T16:59:33.000Z
quoted: Aditya Bandi (@bandiaditya)
  I’m thrilled to announce we’ve raised $44M to build a new home for product design. Meet @noondesign.
  
  No workflow is more broken and fragmented in 2026 than the product designers’. The very same people who care most about building software don’t have software purpose built for them. @kushagrasinha7 and I have lived this problem first hand as designers ourselves.
  
  That’s why we built Noon. The first product design tool that works entirely on your product code, so you can design not only how a product looks, but also how it works. With AI at its core that works in seconds, not minutes.
  
  For the first time, you can create, iterate, build, test and ship. All in one canvas. No translations or roundtrips to the codebase and back.
  
  Comment “Get Noon” and we’ll get you on the list for early access.
text: Design + code + AI! Early access drops today. 
  
  Way to go @bandiaditya and team! https://t.co/dA76BHgZHs
metrics: like_count=46, retweet_count=9, reply_count=2, quote_count=0, bookmark_count=20

[tweet 40]
id: 2039747519572558237
author: PJ Ace (@PJaccetturo)
author_bio: Viral AI ad madman - CEO of https://t.co/YBc1ZfoyRf - 300M+ Views | Featured in Variety, Hollywood Reporter. || Join my newsletter & 100x views on your AI videos 👇🏼
time: 2026-04-02T16:51:19.000Z
replied_to: PJ Ace (@PJaccetturo)
  Use the code "SLOP" to get 15% off!
  https://t.co/K2hgZtfte5
text: Try Seedance 2.0 on Dreamina!
  https://t.co/C6QroKfivO
link: https://dreamina.capcut.com/ai-tool/home?utm_source=Officiaaccount&utm_campaign=sd2&utm_content=34x (Dreamina)
metrics: like_count=9, retweet_count=0, reply_count=2, quote_count=0, bookmark_count=4

[tweet 41]
id: 2039747518326845933
author: PJ Ace (@PJaccetturo)
author_bio: Viral AI ad madman - CEO of https://t.co/YBc1ZfoyRf - 300M+ Views | Featured in Variety, Hollywood Reporter. || Join my newsletter & 100x views on your AI videos 👇🏼
time: 2026-04-02T16:51:19.000Z
replied_to: PJ Ace (@PJaccetturo)
  That’s the whole process. 
  
  1 - Generate tons of images per scene, select 3-6 favs for a scene
  2 - Throw in references into Seedance and let it animate your scene
  3 - Edit
  4 - Make a post about how you made your video ;)
  
  Do this for a few months and this will change your life, just like it changed mine!
  
  Enjoy and let me know if you have any questions!
text: Use the code "SLOP" to get 15% off!
  https://t.co/K2hgZtfte5
link: https://www.aionthelot.com/ (AI on the Lot 2026)
metrics: like_count=9, retweet_count=0, reply_count=1, quote_count=0, bookmark_count=3

[tweet 42]
id: 2039747516871368993
author: PJ Ace (@PJaccetturo)
author_bio: Viral AI ad madman - CEO of https://t.co/YBc1ZfoyRf - 300M+ Views | Featured in Variety, Hollywood Reporter. || Join my newsletter & 100x views on your AI videos 👇🏼
time: 2026-04-02T16:51:19.000Z
replied_to: PJ Ace (@PJaccetturo)
  Animation prompt 4:
  
  cinematic handheld camera shots of an elderly woman in a silver sequin mini dress and glitter high heels skateboarding at The Culver City gates at golden hour, she performs a complete backflip on the skateboard over a cop car (to the amazement of the cops) and flips over the camera as the camera pans up to see her flip over. No music. at the end, she lands cleanly and then we cut to a new angle where she crashes into the camera with her skateboard and we cut to a tile over a black screen that says "AI on the Lot"
text: That’s the whole process. 
  
  1 - Generate tons of images per scene, select 3-6 favs for a scene
  2 - Throw in references into Seedance and let it animate your scene
  3 - Edit
  4 - Make a post about how you made your video ;)
  
  Do this for a few months and this will change your life, just like it changed mine!
  
  Enjoy and let me know if you have any questions!
metrics: like_count=10, retweet_count=0, reply_count=3, quote_count=0, bookmark_count=2

[tweet 43]
id: 2039747515189526999
author: PJ Ace (@PJaccetturo)
author_bio: Viral AI ad madman - CEO of https://t.co/YBc1ZfoyRf - 300M+ Views | Featured in Variety, Hollywood Reporter. || Join my newsletter & 100x views on your AI videos 👇🏼
time: 2026-04-02T16:51:18.000Z
replied_to: PJ Ace (@PJaccetturo)
  Animation prompt 3:
  
  cinematic aerial camera shots of a police officer on horseback charging through a dusty los angeles hillside while a massive crowd in swimwear runs behind him in chaotic pursuit. frantic but playful energy. dynamic aerial movement with aggressive push-ins, pull-outs, and zooms. shots last around 4–5 seconds each. dust clouds rising, bodies moving in waves across terrain. high aerial wide revealing the full crowd chasing the horse across the hillside, slow push-in with subtle zoom tightening. top-down aerial tracking the officer and horse cutting through the center, crowd spreading behind in all directions, slight zoom compressing movement. aerial diagonal sweep across the hillside toward the officer, fast push-in with zoom amplifying speed and chaos. high overhead locked moment as the crowd floods the frame, slow zoom-in isolating the horse at the center. aerial orbit around the officer on horseback, circling while maintaining forward motion, gradual zoom tightening on the megaphone. fast descending aerial move from high above into the dust cloud, emerging closer to the horse mid-gallop. wide aerial pulling back while zooming in (dolly zoom effect) as the crowd surges forward behind. aerial lateral sweep across the running crowd, revealing depth and scale, finishing with a quick zoom-in on the officer. high aerial trailing shot following behind the crowd, slowly closing in with a steady push-in. aerial rise above the hillside revealing the full chaotic procession, quick zoom tightening on the horse leading. feel free to add new angles and quick cuts. No music.
text: Animation prompt 4:
  
  cinematic handheld camera shots of an elderly woman in a silver sequin mini dress and glitter high heels skateboarding at The Culver City gates at golden hour, she performs a complete backflip on the skateboard over a cop car (to the amazement of the cops) and flips over the camera as the camera pans up to see her flip over. No music. at the end, she lands cleanly and then we cut to a new angle where she crashes into the camera with her skateboard and we cut to a tile over a black screen that says "AI on the Lot"
media: video: https://video.twimg.com/amplify_video/2039745926294843393/vid/avc1/1280x720/nsiMZgpOZOtL0VTf.mp4 | duration: 10s
metrics: like_count=3, retweet_count=0, reply_count=1, quote_count=0, bookmark_count=1

[tweet 44]
id: 2039747512299553155
author: PJ Ace (@PJaccetturo)
author_bio: Viral AI ad madman - CEO of https://t.co/YBc1ZfoyRf - 300M+ Views | Featured in Variety, Hollywood Reporter. || Join my newsletter & 100x views on your AI videos 👇🏼
time: 2026-04-02T16:51:18.000Z
replied_to: PJ Ace (@PJaccetturo)
  Animation Prompt 2:
  
  cinematic ground-level dynamic camera shots of a gorilla in goggles and helmet racing on a skateboard through a tunnel at high speed. chaotic, kinetic, slightly absurd but played seriously. aggressive handheld energy, whip pans, snap zooms, extreme low angles. shots around 4 seconds.
  
  ultra low tracking shot inches from asphalt, locked on wheels as they rattle and vibrate, subtle push-in. tight handheld side tracking at chest height, fur whipping in wind, background streaking with motion blur. front-facing tracking shot moving backward just ahead of the gorilla, slight zoom tightening as it gains speed. whip pan from tunnel wall to reveal the gorilla blasting past frame. extreme low angle under the board as it rolls over a bump, quick jolt upward. tight close-up on hands gripping balance, camera shaking with speed. rear tracking shot with aggressive push-in as it carves slightly left and right between cones. snap zoom into goggles reflecting streaking tunnel lights. lateral tracking with foreground poles whipping past lens, creating fast wipes. quick dutch angle shot as the gorilla leans hard into a carve, wheels screeching. tight frontal low shot as it crouches deeper, accelerating. fast pass-by shot where the gorilla whips past camera, leaving frame in a blur.
  
  feel free to add new angles and quick cuts. No music.
text: Animation prompt 3:
  
  cinematic aerial camera shots of a police officer on horseback charging through a dusty los angeles hillside while a massive crowd in swimwear runs behind him in chaotic pursuit. frantic but playful energy. dynamic aerial movement with aggressive push-ins, pull-outs, and zooms. shots last around 4–5 seconds each. dust clouds rising, bodies moving in waves across terrain. high aerial wide revealing the full crowd chasing the horse across the hillside, slow push-in with subtle zoom tightening. top-down aerial tracking the officer and horse cutting through the center, crowd spreading behind in all directions, slight zoom compressing movement. aerial diagonal sweep across the hillside toward the officer, fast push-in with zoom amplifying speed and chaos. high overhead locked moment as the crowd floods the frame, slow zoom-in isolating the horse at the center. aerial orbit around the officer on horseback, circling while maintaining forward motion, gradual zoom tightening on the megaphone. fast descending aerial move from high above into the dust cloud, emerging closer to the horse mid-gallop. wide aerial pulling back while zooming in (dolly zoom effect) as the crowd surges forward behind. aerial lateral sweep across the running crowd, revealing depth and scale, finishing with a quick zoom-in on the officer. high aerial trailing shot following behind the crowd, slowly closing in with a steady push-in. aerial rise above the hillside revealing the full chaotic procession, quick zoom tightening on the horse leading. feel free to add new angles and quick cuts. No music.
media: photo: https://pbs.twimg.com/media/HE6h_E9bwAA6P1u.jpg
metrics: like_count=4, retweet_count=0, reply_count=1, quote_count=0, bookmark_count=1

[tweet 45]
id: 2039747508977742086
author: PJ Ace (@PJaccetturo)
author_bio: Viral AI ad madman - CEO of https://t.co/YBc1ZfoyRf - 300M+ Views | Featured in Variety, Hollywood Reporter. || Join my newsletter & 100x views on your AI videos 👇🏼
time: 2026-04-02T16:51:17.000Z
replied_to: PJ Ace (@PJaccetturo)
  Animation prompt 1:
  
  A high-octane, sun-drenched cinematic sequence on a Los Angeles freeway during golden hour, maintaining a consistent vector of travel forward toward the Downtown LA skyline as the truck holding the portable swimming pool on the left and the police motorcycle officer cruise down the LA highway. Women in the portable pool on the left of frame splash the officer on the motorcycle. he looks left at them, shocked and a little secretly happy as he's surprised, getting splashed as he drives forward. Cinematic, gritty 35mm film aesthetic. No music.
text: Animation Prompt 2:
  
  cinematic ground-level dynamic camera shots of a gorilla in goggles and helmet racing on a skateboard through a tunnel at high speed. chaotic, kinetic, slightly absurd but played seriously. aggressive handheld energy, whip pans, snap zooms, extreme low angles. shots around 4 seconds.
  
  ultra low tracking shot inches from asphalt, locked on wheels as they rattle and vibrate, subtle push-in. tight handheld side tracking at chest height, fur whipping in wind, background streaking with motion blur. front-facing tracking shot moving backward just ahead of the gorilla, slight zoom tightening as it gains speed. whip pan from tunnel wall to reveal the gorilla blasting past frame. extreme low angle under the board as it rolls over a bump, quick jolt upward. tight close-up on hands gripping balance, camera shaking with speed. rear tracking shot with aggressive push-in as it carves slightly left and right between cones. snap zoom into goggles reflecting streaking tunnel lights. lateral tracking with foreground poles whipping past lens, creating fast wipes. quick dutch angle shot as the gorilla leans hard into a carve, wheels screeching. tight frontal low shot as it crouches deeper, accelerating. fast pass-by shot where the gorilla whips past camera, leaving frame in a blur.
  
  feel free to add new angles and quick cuts. No music.
media: photo: https://pbs.twimg.com/media/HE6h3mXaMAA7I0E.jpg
metrics: like_count=3, retweet_count=0, reply_count=1, quote_count=0, bookmark_count=1

[tweet 46]
id: 2039747506876411965
author: PJ Ace (@PJaccetturo)
author_bio: Viral AI ad madman - CEO of https://t.co/YBc1ZfoyRf - 300M+ Views | Featured in Variety, Hollywood Reporter. || Join my newsletter & 100x views on your AI videos 👇🏼
time: 2026-04-02T16:51:16.000Z
replied_to: PJ Ace (@PJaccetturo)
  How to animate using Seedance 2.0:
  
  Create an account with @dreamina_ai and upload reference images for your scene. 
  
  The point isn’t to nail a 15 second sequence for your edit, the point is to generate usable multiple 2-4 second clips in that 15 second sequence and do 5-10 15 second generations per scene.
  
  That will give you a TON of coverage for your edit.
  
  Check out my prompt structure in the posts below to see how i’m getting wayyyy more angles than the reference photos i’m attaching in each sequence.
  
  Accuracy by volume, lol. Give these prompts as a structure example to your favorite LLM and have it give you to the text for each scene.
  
  PRO TIP: always prompt “No music” at the end of each of your prompts so you can keep the sound effects for your edit and add your custom track later.
text: Animation prompt 1:
  
  A high-octane, sun-drenched cinematic sequence on a Los Angeles freeway during golden hour, maintaining a consistent vector of travel forward toward the Downtown LA skyline as the truck holding the portable swimming pool on the left and the police motorcycle officer cruise down the LA highway. Women in the portable pool on the left of frame splash the officer on the motorcycle. he looks left at them, shocked and a little secretly happy as he's surprised, getting splashed as he drives forward. Cinematic, gritty 35mm film aesthetic. No music.
media: video: https://video.twimg.com/amplify_video/2039745344364523520/vid/avc1/1280x720/nUWa1kP_YhLDPxyJ.mp4 | duration: 6s
metrics: like_count=3, retweet_count=0, reply_count=1, quote_count=0, bookmark_count=2

[tweet 47]
id: 2039747503776739444
author: PJ Ace (@PJaccetturo)
author_bio: Viral AI ad madman - CEO of https://t.co/YBc1ZfoyRf - 300M+ Views | Featured in Variety, Hollywood Reporter. || Join my newsletter & 100x views on your AI videos 👇🏼
time: 2026-04-02T16:51:16.000Z
replied_to: PJ Ace (@PJaccetturo)
  I then did this for all the other top scenes:
  
  Get inspired by one 2x2 grid, expand it into 40 shots and then select 5-8 for Seedance to animate. https://t.co/7ENB3t5iqH
text: How to animate using Seedance 2.0:
  
  Create an account with @dreamina_ai and upload reference images for your scene. 
  
  The point isn’t to nail a 15 second sequence for your edit, the point is to generate usable multiple 2-4 second clips in that 15 second sequence and do 5-10 15 second generations per scene.
  
  That will give you a TON of coverage for your edit.
  
  Check out my prompt structure in the posts below to see how i’m getting wayyyy more angles than the reference photos i’m attaching in each sequence.
  
  Accuracy by volume, lol. Give these prompts as a structure example to your favorite LLM and have it give you to the text for each scene.
  
  PRO TIP: always prompt “No music” at the end of each of your prompts so you can keep the sound effects for your edit and add your custom track later.
media: photo: https://pbs.twimg.com/media/HE6hWf3asAYoZQ5.jpg
metrics: like_count=6, retweet_count=0, reply_count=1, quote_count=0, bookmark_count=5

[tweet 48]
id: 2039747501046268306
author: PJ Ace (@PJaccetturo)
author_bio: Viral AI ad madman - CEO of https://t.co/YBc1ZfoyRf - 300M+ Views | Featured in Variety, Hollywood Reporter. || Join my newsletter & 100x views on your AI videos 👇🏼
time: 2026-04-02T16:51:15.000Z
replied_to: PJ Ace (@PJaccetturo)
  Now i’ve got 40 options to choose from with more coverage, I then selected probably 8 total shots. https://t.co/yrilkY9XN2
text: I then did this for all the other top scenes:
  
  Get inspired by one 2x2 grid, expand it into 40 shots and then select 5-8 for Seedance to animate. https://t.co/7ENB3t5iqH
media: photo: https://pbs.twimg.com/media/HE6hJIJasAU5N8j.jpg
metrics: like_count=4, retweet_count=0, reply_count=1, quote_count=0, bookmark_count=1

[tweet 49]
id: 2039747498932400158
author: PJ Ace (@PJaccetturo)
author_bio: Viral AI ad madman - CEO of https://t.co/YBc1ZfoyRf - 300M+ Views | Featured in Variety, Hollywood Reporter. || Join my newsletter & 100x views on your AI videos 👇🏼
time: 2026-04-02T16:51:15.000Z
replied_to: PJ Ace (@PJaccetturo)
  I LOVED this shot of the Nun and so I then asked it to give me 40 more shots of this vibe. https://t.co/gkHff9U2ya
text: Now i’ve got 40 options to choose from with more coverage, I then selected probably 8 total shots. https://t.co/yrilkY9XN2
media: photo: https://pbs.twimg.com/media/HE6hDkAasAUBvQu.jpg
metrics: like_count=6, retweet_count=0, reply_count=1, quote_count=0, bookmark_count=1

[tweet 50]
id: 2039747496675787167
author: PJ Ace (@PJaccetturo)
author_bio: Viral AI ad madman - CEO of https://t.co/YBc1ZfoyRf - 300M+ Views | Featured in Variety, Hollywood Reporter. || Join my newsletter & 100x views on your AI videos 👇🏼
time: 2026-04-02T16:51:14.000Z
replied_to: PJ Ace (@PJaccetturo)
  It breaks up all the shots into specific sections:
  
  So this is all the shots that take place at the Hollywood sign: https://t.co/TSzBe2HeBK
text: I LOVED this shot of the Nun and so I then asked it to give me 40 more shots of this vibe. https://t.co/gkHff9U2ya
media: photo: https://pbs.twimg.com/media/HE6g9F6asAMz2wV.jpg
metrics: like_count=7, retweet_count=0, reply_count=1, quote_count=0, bookmark_count=2

[tweet 51]
id: 2039747494268276779
author: PJ Ace (@PJaccetturo)
author_bio: Viral AI ad madman - CEO of https://t.co/YBc1ZfoyRf - 300M+ Views | Featured in Variety, Hollywood Reporter. || Join my newsletter & 100x views on your AI videos 👇🏼
time: 2026-04-02T16:51:13.000Z
replied_to: PJ Ace (@PJaccetturo)
  Step 3: Image Curation
  
  It gives me 100 images at a time (I actually ran this a few times to get a TON of options) https://t.co/k3RWinHKIO
text: It breaks up all the shots into specific sections:
  
  So this is all the shots that take place at the Hollywood sign: https://t.co/TSzBe2HeBK
media: photo: https://pbs.twimg.com/media/HE6g3gjasAMdZT6.jpg
metrics: like_count=6, retweet_count=0, reply_count=1, quote_count=0, bookmark_count=2

[tweet 52]
id: 2039747491172868341
author: PJ Ace (@PJaccetturo)
author_bio: Viral AI ad madman - CEO of https://t.co/YBc1ZfoyRf - 300M+ Views | Featured in Variety, Hollywood Reporter. || Join my newsletter & 100x views on your AI videos 👇🏼
time: 2026-04-02T16:51:13.000Z
replied_to: PJ Ace (@PJaccetturo)
  Step 2: The Script
  
  This was more of a “vibes” video, so I didn’t have a real script, it was more of just a shot list, but that’s what makes this so fun. I had the AI model surprise me.
  
  I used @LumaLabsAI's AI agent for this and gave it these text instructions:
  
  “Alright i want you to generate a BUNCH OF OPTIONS for this promo video.
  Just give me key images for each of these scenes and other stuff of crazy people in iconic LA locations being chased by cops.
  Don't worry about character consistency because i'll never show the same character twice, and all the characters are just larger than life LA stereotypes and wild and crazy and fun.
  For context, this is a video for "AI on the Lot" event at The Culver Studios and this promo video is about people from all around the city trying to race (often chased by cops) to The Culver Studios
  So they're in iconic LA locations in different modes of transportation:
  Skateboard
  Longboard
  Roller Skates
  Biplane
  Jetpack
  Wingsuit
  Mad max Taco Trucks
  Minivans
  Low riders
  Ice cream trucks
  Hursts
  Hollywood tour boss
  The cops are always a little serious and a little comical, often chubby with with short shorts, like chasing on Segways, horses, roller blades or cop cars
  Iconic locations to feature:
  
  Hollywood Sign
  Venice Beach/muscle beach
  Santa Monica pier
  Griffith observatory
  Hollywood boulevard
  
  Downtown LA
  101 highway
  Malibu/PCH
  LAX
  Culver City (give me lots of coverage here)
  ——
  Here’s an example of some shots on my shotlist that I want you to do, but also expand on it with the same energy in other locations, people, means of transportation, etc:
  
  Grandma in bikini skateboard backflipping through the O in the hollywood in slow motion
  Police helicopter aerial view (news ticker tape) of a hundred cops chasing a minivan with an alien hanging out
  “Hundreds race to AI on the Lot at The Culver Studios”
  Closeup on the alien drinking slurp and throwing it back over his shoulder
  Cops in roller blades (Reno 911 style) with short shorts chasing a cute girl on roller skates
  Venice bodybuilder guy rollerblading with two pitbulls like they’re his sled dogs, both dogs wearing tiny sunglasses
  A mariachi band in the back of a lowrider, all still playing while the car bounces toward Culver
  
  A tattooed nun on a motorcycle
  Mad max style race between multiple food trucks, driving down the 101, chased by cops, (people standing on top of taco and donut trucks, cheering as they speed down the highway)
  ———
  Give me 100 images in 2x2 grids (so that’s 400 images total) but you’re only prompting nano banana for 100 images (that have 2x2 grids)
  
  I want the images very cinematic, all shot on anamorphic lens (but no lens flare), a mix of mediums, closeups and wides to show the cops pursuing, all through iconic LA locations.
  
  You can dedicate each 2x2 grid to a new location and a dedicated mode of transportation
  
  You can also do a few different options for the big popular iconic locations, with a palm trees when oppropriate, all locations should feel very LA
  
  with nano banana pro 2k, 16x9 aspect ratio
text: Step 3: Image Curation
  
  It gives me 100 images at a time (I actually ran this a few times to get a TON of options) https://t.co/k3RWinHKIO
media: photo: https://pbs.twimg.com/media/HE6goflasAMRMid.jpg
metrics: like_count=9, retweet_count=1, reply_count=1, quote_count=0, bookmark_count=4

[tweet 53]
id: 2039747489587458212
author: PJ Ace (@PJaccetturo)
author_bio: Viral AI ad madman - CEO of https://t.co/YBc1ZfoyRf - 300M+ Views | Featured in Variety, Hollywood Reporter. || Join my newsletter & 100x views on your AI videos 👇🏼
time: 2026-04-02T16:51:12.000Z
replied_to: PJ Ace (@PJaccetturo)
  Step 1: The Brief
  
  Todd Terrazas gave me the brief. He just wanted it wild a fun, a love letter to LA.
  
  (The Dreamina team gave me a bunch of free credits for this project) https://t.co/QsgqVSbKJ4
text: Step 2: The Script
  
  This was more of a “vibes” video, so I didn’t have a real script, it was more of just a shot list, but that’s what makes this so fun. I had the AI model surprise me.
  
  I used @LumaLabsAI's AI agent for this and gave it these text instructions:
  
  “Alright i want you to generate a BUNCH OF OPTIONS for this promo video.
  Just give me key images for each of these scenes and other stuff of crazy people in iconic LA locations being chased by cops.
  Don't worry about character consistency because i'll never show the same character twice, and all the characters are just larger than life LA stereotypes and wild and crazy and fun.
  For context, this is a video for "AI on the Lot" event at The Culver Studios and this promo video is about people from all around the city trying to race (often chased by cops) to The Culver Studios
  So they're in iconic LA locations in different modes of transportation:
  Skateboard
  Longboard
  Roller Skates
  Biplane
  Jetpack
  Wingsuit
  Mad max Taco Trucks
  Minivans
  Low riders
  Ice cream trucks
  Hursts
  Hollywood tour boss
  The cops are always a little serious and a little comical, often chubby with with short shorts, like chasing on Segways, horses, roller blades or cop cars
  Iconic locations to feature:
  
  Hollywood Sign
  Venice Beach/muscle beach
  Santa Monica pier
  Griffith observatory
  Hollywood boulevard
  
  Downtown LA
  101 highway
  Malibu/PCH
  LAX
  Culver City (give me lots of coverage here)
  ——
  Here’s an example of some shots on my shotlist that I want you to do, but also expand on it with the same energy in other locations, people, means of transportation, etc:
  
  Grandma in bikini skateboard backflipping through the O in the hollywood in slow motion
  Police helicopter aerial view (news ticker tape) of a hundred cops chasing a minivan with an alien hanging out
  “Hundreds race to AI on the Lot at The Culver Studios”
  Closeup on the alien drinking slurp and throwing it back over his shoulder
  Cops in roller blades (Reno 911 style) with short shorts chasing a cute girl on roller skates
  Venice bodybuilder guy rollerblading with two pitbulls like they’re his sled dogs, both dogs wearing tiny sunglasses
  A mariachi band in the back of a lowrider, all still playing while the car bounces toward Culver
  
  A tattooed nun on a motorcycle
  Mad max style race between multiple food trucks, driving down the 101, chased by cops, (people standing on top of taco and donut trucks, cheering as they speed down the highway)
  ———
  Give me 100 images in 2x2 grids (so that’s 400 images total) but you’re only prompting nano banana for 100 images (that have 2x2 grids)
  
  I want the images very cinematic, all shot on anamorphic lens (but no lens flare), a mix of mediums, closeups and wides to show the cops pursuing, all through iconic LA locations.
  
  You can dedicate each 2x2 grid to a new location and a dedicated mode of transportation
  
  You can also do a few different options for the big popular iconic locations, with a palm trees when oppropriate, all locations should feel very LA
  
  with nano banana pro 2k, 16x9 aspect ratio
metrics: like_count=15, retweet_count=1, reply_count=2, quote_count=0, bookmark_count=10

[tweet 54]
id: 2039747487330967851
author: PJ Ace (@PJaccetturo)
author_bio: Viral AI ad madman - CEO of https://t.co/YBc1ZfoyRf - 300M+ Views | Featured in Variety, Hollywood Reporter. || Join my newsletter & 100x views on your AI videos 👇🏼
time: 2026-04-02T16:51:12.000Z
replied_to: PJ Ace (@PJaccetturo)
  Dreamina Seedance 2.0 is coming soon to the US, and it will CHANGE YOUR LIFE if you learn to master it.
  
  BUT there's a secret trick to making films FAST.
  
  Let me show you my entire framework for making this AI on the Lot ad in 7 simple steps🧵👇 https://t.co/uXn2kDaeOX
text: Step 1: The Brief
  
  Todd Terrazas gave me the brief. He just wanted it wild a fun, a love letter to LA.
  
  (The Dreamina team gave me a bunch of free credits for this project) https://t.co/QsgqVSbKJ4
media: photo: https://pbs.twimg.com/media/HE6gUK8bQAANn96.png
metrics: like_count=10, retweet_count=0, reply_count=3, quote_count=0, bookmark_count=5

[tweet 55]
id: 2039747485263176156
author: PJ Ace (@PJaccetturo)
author_bio: Viral AI ad madman - CEO of https://t.co/YBc1ZfoyRf - 300M+ Views | Featured in Variety, Hollywood Reporter. || Join my newsletter & 100x views on your AI videos 👇🏼
time: 2026-04-02T16:51:11.000Z
text: Dreamina Seedance 2.0 is coming soon to the US, and it will CHANGE YOUR LIFE if you learn to master it.
  
  BUT there's a secret trick to making films FAST.
  
  Let me show you my entire framework for making this AI on the Lot ad in 7 simple steps🧵👇 https://t.co/uXn2kDaeOX
media: video: https://video.twimg.com/amplify_video/2039742777622409218/vid/avc1/1920x1080/1yb8vXc64KSWGXg9.mp4 | duration: 66s
metrics: like_count=239, retweet_count=27, reply_count=34, quote_count=3, bookmark_count=325

[tweet 56]
id: 2039737082176844229
author: GREG ISENBERG (@gregisenberg)
author_bio: I drop startup ideas daily. Host @startupideaspod. CEO: @latecheckoutplz we build companies like @ideabrowser, @meetLCA, @boringmarketer etc
time: 2026-04-02T16:09:51.000Z
quoted: The Startup Ideas Podcast (SIP) 🧃 (@startupideaspod)
  Sam Altman predicted the first one-person billion-dollar company.
  
  Matthew Gallagher built a $401M company in year one with $20,000, AI tools, and zero employees.
  
  This year he's on track for $1.8B. With 2 people.
  
  The playbook has changed:
  
  Old path:
  - Come up with an idea
  - Fundraise from friends or VCs
  - Hire a team
  - Build the product
  - Hope it works
  
  New path:
  - Start with an audience (X, Instagram, TikTok)
  - Vibe code something for that audience
  - Build a community around it
  - Automate fulfillment with AI agents
  - Repeat
  
  That's the new barrier to entry is a laptop and an idea.
text: So, he vibe coded a $1B startup? 
  
  Really cool
  
  With the right idea, right tools, right distribution channel, anything is possible in 2026 https://t.co/yJigowLa36
metrics: like_count=682, retweet_count=43, reply_count=72, quote_count=3, bookmark_count=664

[tweet 57]
id: 2039735609049174344
author: Logan Kilpatrick (@OfficialLoganK)
author_bio: Member of technical staff, working on @GoogleAIStudio, the Gemini API, & Kaggle. My views!
time: 2026-04-02T16:04:00.000Z
replied_to: Logan Kilpatrick (@OfficialLoganK)
  Introducing Gemma 4, our series of open weight (Apache 2.0 licensed) models, which are byte for byte the most capable open models in the world!
  
  Gemma 4 is build to run on your hardware: phones, laptops, and desktops.
  
  Frontier intelligence with a 26B MOE and a 31B Dense model! https://t.co/PVtYRnKQW0
text: This is just the start of the Gemma 4 era : ) 
  
  Download Gemma 4 on Kaggle: https://t.co/5dmyu19J7U
  
  And read more in our blog: https://t.co/MeuwbQVAfa
link: https://www.kaggle.com/models/google/gemma-4 (Google | Gemma 4 | Kaggle)
link: https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/ (Gemma 4: Byte for byte, the most capable open models)
metrics: like_count=428, retweet_count=22, reply_count=10, quote_count=7, bookmark_count=102

[tweet 58]
id: 2039735606268314071
author: Logan Kilpatrick (@OfficialLoganK)
author_bio: Member of technical staff, working on @GoogleAIStudio, the Gemini API, & Kaggle. My views!
time: 2026-04-02T16:03:59.000Z
text: Introducing Gemma 4, our series of open weight (Apache 2.0 licensed) models, which are byte for byte the most capable open models in the world!
  
  Gemma 4 is build to run on your hardware: phones, laptops, and desktops.
  
  Frontier intelligence with a 26B MOE and a 31B Dense model! https://t.co/PVtYRnKQW0
media: photo: https://pbs.twimg.com/media/HE6YbAUXIAE-oY2.jpg
metrics: like_count=5265, retweet_count=501, reply_count=267, quote_count=179, bookmark_count=1129

[tweet 59]
id: 2039731494705561858
author: Felix Lee (@felixleezd)
author_bio: CEO, @ADPList. I design products for 10M+ people. Gotrade (YC S19). Intersection of art and science.
time: 2026-04-02T15:47:39.000Z
quoted: Felix Lee (@felixleezd)
  https://t.co/wU7oUe9aTN
replied_to: Felix Lee (@felixleezd)
  Day 140 of vibe-coding as a designer.
  
  I'm shocked how few designers know about this workflow.
  
  I skipped Figma and made a beautiful Robinhood design from Claude Code + Paper, in just one prompt. Wild! 🤯
  
  This feels like the future of design. https://t.co/xFl325vRRu
text: since many of you reached out, I wrote a guide here: https://t.co/71oSn3PgRQ cc @paper is good starting tool!
metrics: like_count=9, retweet_count=1, reply_count=0, quote_count=0, bookmark_count=13

[tweet 60]
id: 2039731306612060186
author: Felix Lee (@felixleezd)
author_bio: CEO, @ADPList. I design products for 10M+ people. Gotrade (YC S19). Intersection of art and science.
time: 2026-04-02T15:46:54.000Z
text: https://t.co/wU7oUe9aTN
metrics: like_count=290, retweet_count=18, reply_count=9, quote_count=2, bookmark_count=634

[tweet 61]
id: 2039730824413598176
author: Matt Turck (@mattturck)
author_bio: VC at @FirstMarkCap.  Host: MAD Podcast; Organizer: Data Driven NYC, Author: MAD Landscape.
time: 2026-04-02T15:44:59.000Z
replied_to: Matt Turck (@mattturck)
  AI is Already Building AI: my conversation with @m__dehghani of @GoogleDeepMind about AI loops, recursive self improvement, continual learning and the latest in frontier AI. 
  
  00:00 Intro
  
  01:17 What “loops” in AI actually mean
  
  05:04 Recursive self-improvement as the next chapter of AI
  
  07:32 @karpathy's autoresearch agents 
  
  08:56 AI building AI: how close are we?
  
  10:02 The biggest bottlenecks: evals, automation, and long horizons
  
  12:36 Can formal verification unlock recursive self-improvement?
  
  14:06 What is model collapse?
  
  15:33 Generalization vs specialization in AI
  
  18:04 What is a specialized model today?
  
  20:57 Could top AI researchers themselves be automated?
  
  24:02 If AI builds AI, does data matter less than compute?
  
  26:22 Post-training vs pre-training: where will progress come from?
  
  28:14 Why pre-training is not dead
  
  29:45 What is continual learning?
  
  31:53 How real is continual learning today?
  
  33:43 Mostafa’s background and path into AI
  
  36:13 The story behind Universal Transformers
  
  39:56 How Vision Transformers changed AI
  
  43:47 Gemini, multimodality, and Nano Banana
  
  47:46 Why multimodality helps build a world model
  
  52:44 Why image generation is getting faster and more efficient
  
  54:44 Hot takes section!
  
  54:53 What the AI field is getting wrong 
  
  56:17 Why continual learning is underrated
  
  57:26 Does RAG go away over time?
  
  58:21 What people are too confident about in AI
  
  59:56 What would you do if you were starting from scratch today?
text: This fantastic deep dive with @m__dehghani is also available on Spotify, Apple Podcasts and here on YouTube:
  
  https://t.co/LpbfrWPfz2
link: https://youtu.be/Bo19sXssYXI?si=ayQlcRCONF9XU2t8 (AI is Already Building AI — Google DeepMind’s Mostafa Dehghani)
metrics: like_count=3, retweet_count=0, reply_count=0, quote_count=0, bookmark_count=0

[tweet 62]
id: 2039730819774787857
author: Matt Turck (@mattturck)
author_bio: VC at @FirstMarkCap.  Host: MAD Podcast; Organizer: Data Driven NYC, Author: MAD Landscape.
time: 2026-04-02T15:44:58.000Z
text: AI is Already Building AI: my conversation with @m__dehghani of @GoogleDeepMind about AI loops, recursive self improvement, continual learning and the latest in frontier AI. 
  
  00:00 Intro
  
  01:17 What “loops” in AI actually mean
  
  05:04 Recursive self-improvement as the next chapter of AI
  
  07:32 @karpathy's autoresearch agents 
  
  08:56 AI building AI: how close are we?
  
  10:02 The biggest bottlenecks: evals, automation, and long horizons
  
  12:36 Can formal verification unlock recursive self-improvement?
  
  14:06 What is model collapse?
  
  15:33 Generalization vs specialization in AI
  
  18:04 What is a specialized model today?
  
  20:57 Could top AI researchers themselves be automated?
  
  24:02 If AI builds AI, does data matter less than compute?
  
  26:22 Post-training vs pre-training: where will progress come from?
  
  28:14 Why pre-training is not dead
  
  29:45 What is continual learning?
  
  31:53 How real is continual learning today?
  
  33:43 Mostafa’s background and path into AI
  
  36:13 The story behind Universal Transformers
  
  39:56 How Vision Transformers changed AI
  
  43:47 Gemini, multimodality, and Nano Banana
  
  47:46 Why multimodality helps build a world model
  
  52:44 Why image generation is getting faster and more efficient
  
  54:44 Hot takes section!
  
  54:53 What the AI field is getting wrong 
  
  56:17 Why continual learning is underrated
  
  57:26 Does RAG go away over time?
  
  58:21 What people are too confident about in AI
  
  59:56 What would you do if you were starting from scratch today?
media: video: https://video.twimg.com/amplify_video/2039722029507637248/vid/avc1/3840x2160/RkxSa6a2b-4ZEEjS.mp4 | duration: 3871s
metrics: like_count=32, retweet_count=6, reply_count=3, quote_count=0, bookmark_count=30

[tweet 63]
id: 2039724842099044443
author: Amjad Masad (@amasad)
author_bio: ceo @replit. civilizationist
time: 2026-04-02T15:21:13.000Z
text: One person billion dollar company has been achieved: @galligator https://t.co/XMjsLCRXV9
media: photo: https://pbs.twimg.com/media/HE6O7qVa4AAk1oQ.jpg
metrics: like_count=4659, retweet_count=433, reply_count=222, quote_count=159, bookmark_count=2994

[tweet 64]
id: 2039722279014432932
author: Aaron Levie (@levie)
author_bio: ceo @box - your business lives in content. unleash it with AI
time: 2026-04-02T15:11:02.000Z
text: Introducing the new Box Agent. The Box Agent works across your entire Box file system, maintaining all your security and access controls, and is hyper tuned for working with enterprise content.
  
  This means you can now ask questions from all your enterprise content, search for files that were impossible to find before, deploy an agent on specific tasks on subsets of documents, analyze complex data sets, and generate or edit documents and spreadsheets via the agent.
  
  You can have the Box Agent search across your Box account to prepare for a sales meeting, analyze customer sentiment reports, process a large set of contracts for legal risk, provide insights into product development, leverage existing knowledge to answer RFPs, and thousands of other use-cases.
  
  90% of enterprise data is unstructured data. This means most enterprise knowledge is sitting in inside of research reports, marketing assets, presentations, roadmap files, contracts, HR documents, and more. This is the critical context that agents need to be able to answer questions about a business, automate workflows, or serve up to other agents.
  
  We’ve been grinding on this for a quite a bit, and due to recent AI model advancements we’re now ready to release it to customers. Previous model generations had a difficult time knowing when to give up or keep going on a search, when to browse for files vs. use queries, how to rank files appropriately to know which version of content to use, how to handle large amounts of context to comb through, and more.
  
  Due to recent breakthroughs from models like GPT-5.4, Opus 4.6, and Gemini 3, we’ve seen major gains in tool calling, code execution, advanced reasoning, and more. Combined with an agent harness tuned to Box context, now it’s finally possible to have an agent that can work across your file system on long running tasks and actually deliver high quality results.
  
  Best of all, because the Box Agent works with any leading AI model, you’ll quickly get the gains coming out of the major labs as major new models are released. Further, openness at Box is key, so you’ll be able to call up the Box Agent from Box’s APIs and MCP server, so you can interact with Box intelligently from any other AI system. We know work happens everywhere, and we want to ensure you can access to the content you need from those places.
  
  The new Box Agent is available starting today, rolling out now for Enterprise Plus and Enterprise Advanced customers.
media: video: https://video.twimg.com/amplify_video/2039722126945779712/vid/avc1/1504x1080/xPcIc4wqUGw7U4pw.mp4 | duration: 58s
metrics: like_count=118, retweet_count=17, reply_count=26, quote_count=1, bookmark_count=61

[tweet 65]
id: 2039719701178401192
author: Justine Moore (@venturetwins)
author_bio: Partner @a16z AI 🤖 and twin to @omooretweets | Investor in @elevenlabs, @bfl_ml, @hedra_labs, @krea_ai, @MireloAI, @ShizukuAILabs, @wabi, @WaveFormsAI
time: 2026-04-02T15:00:47.000Z
text: All the smartest people I know have LLM psychosis now
metrics: like_count=2324, retweet_count=155, reply_count=354, quote_count=83, bookmark_count=365

[tweet 66]
id: 2039643595876323371
author: 郭宇 guoyu.eth (@turingou)
author_bio: Retired. 只活一次等于没活。
time: 2026-04-02T09:58:22.000Z
text: 今日白天的拍摄圆满结束！ https://t.co/5CKo9eouGw
media: photo: https://pbs.twimg.com/media/HE5FB-ybgAA7SHz.jpg
media: photo: https://pbs.twimg.com/media/HE5FB-0agAEL72E.jpg
media: photo: https://pbs.twimg.com/media/HE5FB-yaEAAF5YO.jpg
media: photo: https://pbs.twimg.com/media/HE5FB-3bEAEmEIr.jpg
metrics: like_count=77, retweet_count=1, reply_count=4, quote_count=0, bookmark_count=3

[tweet 67]
id: 2039601487870087260
author: Peter Yang (@petergyang)
author_bio: I share extremely practical AI tutorials and interviews | Join 140K+ readers at https://t.co/XYKTmGVH14 | Product at Roblox
time: 2026-04-02T07:11:03.000Z
text: Sometimes I send @openclaw a request and it doesn’t respond for a long time because it’s working. Anyone know how to easily cancel the request so it responds?
  
  Sending “/cancel” via a chat message doesn’t seem to work
metrics: like_count=39, retweet_count=1, reply_count=21, quote_count=1, bookmark_count=22

[tweet 68]
id: 2039599038358814961
author: Zara Zhang (@zarazhangrui)
author_bio: Builder. Dangerously skips permissions. Harvard’17. GitHub: https://t.co/KCuEajezlL YouTube: https://t.co/8xzbGWtf6w
time: 2026-04-02T07:01:19.000Z
text: Just had an aha moment with OpenClaw.
  
  I'm replacing my to-do list with "braindumping to-dos to OpenClaw". Whenever I think of a quick task, I just message it to OpenClaw
  
  Not only will it record those tasks, but it will actually DO those tasks
  
  Every morning it sends me a report of what tasks are already done, and highlights the ones that need my attention
  
  This might actually be a to-do management system that works
metrics: like_count=199, retweet_count=13, reply_count=50, quote_count=2, bookmark_count=135

[tweet 69]
id: 2039582615225983453
author: 郭宇 guoyu.eth (@turingou)
author_bio: Retired. 只活一次等于没活。
time: 2026-04-02T05:56:03.000Z
text: お久しぶり沖縄！ https://t.co/Rrs6kgKbEn
media: photo: https://pbs.twimg.com/media/HE4Nk6AaEAAQF96.jpg
metrics: like_count=23, retweet_count=0, reply_count=0, quote_count=0, bookmark_count=0

[tweet 70]
id: 2039574847492366356
author: Matan Grinberg (@matanSF)
author_bio: ceo @FactoryAI
time: 2026-04-02T05:25:11.000Z
quoted: Morgan (@morganlinton)
  Droids++ https://t.co/eVglussJN1
text: Droidmaxxing https://t.co/rjKug1E0ZW
metrics: like_count=29, retweet_count=1, reply_count=3, quote_count=0, bookmark_count=2

[tweet 71]
id: 2039563521885901091
author: Peter Yang (@petergyang)
author_bio: I share extremely practical AI tutorials and interviews | Join 140K+ readers at https://t.co/XYKTmGVH14 | Product at Roblox
time: 2026-04-02T04:40:11.000Z
text: I think the combination of mobile and short video has rotted the brains of an entire generation of kids. 
  
  See so many kids staring at their TikTok, YouTube Shorts, Reels, etc like zombies.
metrics: like_count=74, retweet_count=3, reply_count=32, quote_count=3, bookmark_count=11

[tweet 72]
id: 2039552681493336250
author: Amjad Masad (@amasad)
author_bio: ceo @replit. civilizationist
time: 2026-04-02T03:57:06.000Z
quoted: Manny Bernabe (@MannyBernabe)
  "He started a business selling custom vibe coded apps to medium-sized businesses. $1,500 a month, one call a month. $2.5 million his first year. 60% net margins. This year he's gonna do $8 million."
  
  @mhp_guy talking to @ShaanVP on @myfirstmilpod about John Cheney, who builds custom Replit apps that replace expensive SaaS tools businesses are already paying thousands for.
  
  "You're an HVAC company with 30 crews? He builds your own CRM so you're not paying ServiceTitan $4,000 a month. Built exactly as you've always wanted it."
text: We’re in an unprecedented era of rapid wealth creation. https://t.co/P6qoQrvTEn
metrics: like_count=1529, retweet_count=113, reply_count=39, quote_count=2, bookmark_count=1767

[tweet 73]
id: 2039551079621566812
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world @openclaw🦞
time: 2026-04-02T03:50:45.000Z
quoted: Anthony (@kr0der)
  slowly starting to use plan mode a LOT less nowadays
  
  i realised whenever i use plan mode, it generates a gigantic plan and then i dont read it and hit build out of laziness
  
  having a meaningful conversation with the AI agent to discuss implementation feels a lot easier 🤔
text: I never use plan mode. 
  
  The main reason this was added to codex is for claude-pilled people who struggle with changing their habits.
  
  just talk with your agent. https://t.co/72fL0alajL
metrics: like_count=3898, retweet_count=201, reply_count=477, quote_count=143, bookmark_count=873

[tweet 74]
id: 2039549776463814967
author: Justine Moore (@venturetwins)
author_bio: Partner @a16z AI 🤖 and twin to @omooretweets | Investor in @elevenlabs, @bfl_ml, @hedra_labs, @krea_ai, @MireloAI, @ShizukuAILabs, @wabi, @WaveFormsAI
time: 2026-04-02T03:45:34.000Z
quoted: Tejes Srivalsan (@tejessrivalsan)
  after the overwhelming support for EGO-SNAKE, i’m excited to share EGO-BIRD
  
  100,000 hours of pov bird footage to train the next generation of autonomous drones https://t.co/YLiNYOM444
text: Delighted to inform you that this series has continued for ants.
  
  It’s somehow both even more disturbing and fascinating… 
  
  (from neural_box on IG) https://t.co/0pSmAdkUYC https://t.co/ra9hRJHb9y
media: video: https://video.twimg.com/amplify_video/2039549704607010816/vid/avc1/720x1206/v9AO_TCUIj-RZH6R.mp4 | duration: 40s
metrics: like_count=4268, retweet_count=392, reply_count=69, quote_count=33, bookmark_count=2033

[tweet 75]
id: 2039548892933750949
author: Robert Bye (@RobertJBye)
author_bio: Mobile Product Manager at @AnthropicAI. Board Member https://t.co/PYz00fvA2m. Previously @Figma, @Google, and @AllTrails. Jesus follower.
time: 2026-04-02T03:42:03.000Z
text: Is there a better design process than Pen &amp; Paper &gt; Claude Code?
  
  You get fully free formed thinking, straight into something working. Either a prototype, or something shippable.
metrics: like_count=33, retweet_count=0, reply_count=16, quote_count=0, bookmark_count=19

[tweet 76]
id: 2039530536050274648
author: Nan Yu (@thenanyu)
author_bio: head of product @linear
time: 2026-04-02T02:29:07.000Z
quoted: gaut (@0xgaut)
  one day you’re 25 and the next you’re getting sorted into one of the four stroller houses for your baby https://t.co/u6sUTixqSO
text: Doona is the Notion of strollers https://t.co/nAAanA98vM
metrics: like_count=44, retweet_count=1, reply_count=13, quote_count=1, bookmark_count=13

[tweet 77]
id: 2039528627281240106
author: Nan Yu (@thenanyu)
author_bio: head of product @linear
time: 2026-04-02T02:21:32.000Z
quoted: Aaron Levie (@levie)
  Huge misunderstanding by everyone why companies buy software. Companies don’t want every employee doing every workflow from scratch on their own for every use case. At some point what you’re outsourcing is the ability to not have to think about the business process, and instead let the software provider think about it. Agents don’t change that, and probably if anything exhibit that dynamic even more.
text: LOUDER https://t.co/PRWbD9dHji
metrics: like_count=72, retweet_count=1, reply_count=1, quote_count=1, bookmark_count=47

[tweet 78]
id: 2039500186901512305
author: Lenny Rachitsky (@lennysan)
author_bio: Deeply researched product, growth, and career advice
time: 2026-04-02T00:28:31.000Z
replied_to: Lenny Rachitsky (@lennysan)
  My top takeaways from @clairevo on all things 🦞
  
  1. Install OpenClaw on a separate computer, not your main machine. Use an old laptop or buy a Mac Mini ($500-$600). Create a dedicated Gmail account and local admin account for your agent. Think of it like hiring an employee—you wouldn’t let them run wild on your personal computer 24/7.
  
  2. The unlock is to stop treating OpenClaw like one general-purpose agent and instead creating multiple Claws with very specific roles. Claire says people get frustrated when they throw every task at a single agent and it sucks at it because it loses context. Her fix was to split her work. Sam handles sales, Finn manages family, Howie preps podcasts, Sage runs her course. Think of it like Slack: you wouldn’t put your whole company in one channel, so do not put every workflow into one agent.
  
  3. The right setup mental model is “onboard an employee,” not “install an app.” Claire creates a separate local admin account, and separate email/calendar access instead of handing over her main passwords. She shares permissions the way she would for a human EA.
  
  4. The magic of OpenClaw is soul + heartbeat + jobs. The “soul” is a Markdown file defining identity and personality. The “heartbeat” checks in every 30 minutes to see what needs doing. “Jobs” are scheduled tasks that run automatically. This combination makes agents feel alive.
  
  4. Sam the sales agent saves Claire 10 hours per week and real money. Every morning, Sam sweeps their CRM for new signups, identifies decision-makers at companies, sends personalized emails, and flags international deals to handle autonomously. This replaced a contractor Claire was paying for the same work.
  
  5. The “yappers API” is the highest-bandwidth way to communicate with AI. Don’t worry about perfect prompts or structured inputs. Just ramble in voice notes on Telegram about what you need. The agent will make sense of it and ask clarifying questions.
  
  6. Browser use is the biggest limitation—look for APIs first. The web is hostile to bots, and browser automation is unreliable across all AI tools. Always check if there’s an API available. If not, try browser use, but be prepared for it to fail. Sometimes the solution is solving the problem behind the problem.
  
  7. Management skills are the secret to AI agent success, not technical skills. Claire’s 20-plus years of management experience—role scoping, org design, onboarding, progressive trust—translates directly to making agents effective. If your agent isn’t working, it’s usually a structural issue, not the agent being “dumb.”
  
  7. Screen sharing saves you from buying monitors and keyboards for every Mac Mini. Turn on screen sharing in Mac Mini settings, and you can control it from your laptop on the same Wi-Fi. Turn on remote login to SSH into the terminal. This was Claire’s life-changing discovery.
  
  8. Security is a real factor but manageable with progressive trust. OpenClaw is hardened against prompt injection, but start cautiously. Only let agents listen to you on specific channels (like Telegram, not email). Add instructions to their soul about never following external instructions. Build trust progressively like you would with a human assistant.
text: Don't miss our full chat https://t.co/hl53XpEfCQ
  
  Also available on: 
  • Spotify: https://t.co/JaZtRDtZ4N
  • Apple: https://t.co/ezrvBJMBkG https://t.co/gcIKLalx97
media: photo: https://pbs.twimg.com/media/HE3CmULagAAnjlJ.jpg
link: https://youtube.com/watch?v=DIa0MYJzM5I (From skeptic to true believer: How OpenClaw changed my life | Claire Vo)
link: https://open.spotify.com/episode/1OkEtDoje5m4j7qRuL32dq (From skeptic to true believer: How OpenClaw changed my life | Claire Vo)
link: https://podcasts.apple.com/us/podcast/from-skeptic-to-true-believer-how-openclaw-changed/id1627920305?i=1000758037099 (From skeptic to true believer: How OpenClaw changed my life | Claire Vo)
metrics: like_count=29, retweet_count=3, reply_count=0, quote_count=1, bookmark_count=46

[tweet 79]
id: 2039498785693540534
author: Lenny Rachitsky (@lennysan)
author_bio: Deeply researched product, growth, and career advice
time: 2026-04-02T00:22:57.000Z
text: My top takeaways from @clairevo on all things 🦞
  
  1. Install OpenClaw on a separate computer, not your main machine. Use an old laptop or buy a Mac Mini ($500-$600). Create a dedicated Gmail account and local admin account for your agent. Think of it like hiring an employee—you wouldn’t let them run wild on your personal computer 24/7.
  
  2. The unlock is to stop treating OpenClaw like one general-purpose agent and instead creating multiple Claws with very specific roles. Claire says people get frustrated when they throw every task at a single agent and it sucks at it because it loses context. Her fix was to split her work. Sam handles sales, Finn manages family, Howie preps podcasts, Sage runs her course. Think of it like Slack: you wouldn’t put your whole company in one channel, so do not put every workflow into one agent.
  
  3. The right setup mental model is “onboard an employee,” not “install an app.” Claire creates a separate local admin account, and separate email/calendar access instead of handing over her main passwords. She shares permissions the way she would for a human EA.
  
  4. The magic of OpenClaw is soul + heartbeat + jobs. The “soul” is a Markdown file defining identity and personality. The “heartbeat” checks in every 30 minutes to see what needs doing. “Jobs” are scheduled tasks that run automatically. This combination makes agents feel alive.
  
  4. Sam the sales agent saves Claire 10 hours per week and real money. Every morning, Sam sweeps their CRM for new signups, identifies decision-makers at companies, sends personalized emails, and flags international deals to handle autonomously. This replaced a contractor Claire was paying for the same work.
  
  5. The “yappers API” is the highest-bandwidth way to communicate with AI. Don’t worry about perfect prompts or structured inputs. Just ramble in voice notes on Telegram about what you need. The agent will make sense of it and ask clarifying questions.
  
  6. Browser use is the biggest limitation—look for APIs first. The web is hostile to bots, and browser automation is unreliable across all AI tools. Always check if there’s an API available. If not, try browser use, but be prepared for it to fail. Sometimes the solution is solving the problem behind the problem.
  
  7. Management skills are the secret to AI agent success, not technical skills. Claire’s 20-plus years of management experience—role scoping, org design, onboarding, progressive trust—translates directly to making agents effective. If your agent isn’t working, it’s usually a structural issue, not the agent being “dumb.”
  
  7. Screen sharing saves you from buying monitors and keyboards for every Mac Mini. Turn on screen sharing in Mac Mini settings, and you can control it from your laptop on the same Wi-Fi. Turn on remote login to SSH into the terminal. This was Claire’s life-changing discovery.
  
  8. Security is a real factor but manageable with progressive trust. OpenClaw is hardened against prompt injection, but start cautiously. Only let agents listen to you on specific channels (like Telegram, not email). Add instructions to their soul about never following external instructions. Build trust progressively like you would with a human assistant.
metrics: like_count=1132, retweet_count=97, reply_count=76, quote_count=19, bookmark_count=2553

[tweet 80]
id: 2039496525282496861
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world @openclaw🦞
time: 2026-04-02T00:13:58.000Z
quoted: swyx (@swyx)
  so AIE Europe is completely taking over 🇬🇧London next week! very very hyped to showcase the best companies, research, and AI engineers in Europe!
  
  3 COMPLETELY FREE ways to join in:
  
  - there are a dozen side events around town! from Snorkel to GitHub to Arize to ClawCon and Claude Code meetups!
  - subscribe on YouTube! everything will be livestreamed and published for free https://t.co/KZTk3oyvJr
  - we are releasing 20 more volunteer slots here https://t.co/Z4nH1Lgzhb meant for local, early career folks who otherwise could not afford a ticket!
  
  join in/see you in london town!
text: See you there! https://t.co/XjfDQ6s8ri
metrics: like_count=171, retweet_count=6, reply_count=8, quote_count=0, bookmark_count=45

[tweet 81]
id: 2039493013043626427
author: Guillermo Rauch (@rauchg)
author_bio: @vercel CEO
time: 2026-04-02T00:00:00.000Z
text: Vercel signups are growing at 52% MoM
  (up from 23%, up from 17%)
metrics: like_count=797, retweet_count=20, reply_count=68, quote_count=17, bookmark_count=45

[tweet 82]
id: 2039490349941526770
author: Nan Yu (@thenanyu)
author_bio: head of product @linear
time: 2026-04-01T23:49:25.000Z
text: If you're a PM or on sales or support, how many times have you needed to bother an engineer to find out exactly how the app works? 
  
  I wanted to know exactly what the default setting was for a personal configuration for all of our users. 
  
  You never need to ask an engineer again for this kind of thing, because Linear Agent can just read the code and tell you.
media: photo: https://pbs.twimg.com/media/HE245SLasAArjTx.jpg
metrics: like_count=73, retweet_count=4, reply_count=14, quote_count=1, bookmark_count=44

[tweet 83]
id: 2039485214532190359
author: Peter Yang (@petergyang)
author_bio: I share extremely practical AI tutorials and interviews | Join 140K+ readers at https://t.co/XYKTmGVH14 | Product at Roblox
time: 2026-04-01T23:29:01.000Z
quoted: Peter Yang (@petergyang)
  Me and my OpenClaw are ready for Disneyland Shanghai https://t.co/IyfrvZiIEl
text: Oh dear https://t.co/TXlIAquaA4 https://t.co/EWs4SSE3pv
media: photo: https://pbs.twimg.com/media/HE208y-aYAE2Djy.jpg
media: photo: https://pbs.twimg.com/media/HE208zLboAAkbIi.jpg
metrics: like_count=34, retweet_count=0, reply_count=16, quote_count=0, bookmark_count=4