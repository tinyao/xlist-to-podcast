list_id: 2007466263661232466
fetched_at: 2026-04-04 23:13 UTC
total_tweets: 63
[tweet 1]
id: 2040565939100676382
author: Zara Zhang (@zarazhangrui)
author_bio: Builder. Dangerously skips permissions. Harvard’17. GitHub: https://t.co/KCuEajezlL YouTube: https://t.co/8xzbGWtf6w
time: 2026-04-04T23:03:26.000Z
text: Prompting tip from @steipete:
  
  I always ask the model, "Do you have any questions?"
metrics: like_count=5, retweet_count=0, reply_count=0, quote_count=1, bookmark_count=0

[tweet 2]
id: 2040560910750638300
author: Nan Yu (@thenanyu)
author_bio: head of product @linear
time: 2026-04-04T22:43:27.000Z
quoted: delia (@delia_cai)
  Kind of think we should get an emergency amber alert style warning if the temp is gonna drop 20 degrees like that in an hour
replied_to: Nan Yu (@thenanyu)
  It’s not fine. The visualization is meant to give the driver confidence that the car understands its surroundings.
  
  I hope the automation systems are not as confused as the visuals
  
  https://t.co/LWZeHDvBIR
text: Today in NY 
  
  https://t.co/uXTGy184Gq
metrics: like_count=5, retweet_count=0, reply_count=0, quote_count=0, bookmark_count=1

[tweet 3]
id: 2040557561464885382
author: Thariq (@trq212)
author_bio: Claude Code @anthropicai.   prev YC W20, mit media lab.   towards machines of loving grace
time: 2026-04-04T22:30:09.000Z
text: POV: you're cooking https://t.co/Aw546zNBq7
media: photo: https://pbs.twimg.com/media/HFGD0mEbkAA7uKe.jpg
metrics: like_count=238, retweet_count=2, reply_count=38, quote_count=1, bookmark_count=26

[tweet 4]
id: 2040549459193704852
author: Andrej Karpathy (@karpathy)
author_bio: I like to train large deep neural nets. Previously Director of AI @ Tesla, founding team @ OpenAI, PhD @ Stanford.
time: 2026-04-04T21:57:57.000Z
quoted: Harry Rushworth (@Hrushworth)
  The British Government is a complicated beast. Dozens of departments, hundreds of public bodies, more corporations than one can count...
  
  Such is its complexity that there isn't an org chart for it.
  
  Well, there wasn't...
  
  Introducing ⚙️Machinery of Government⚙️ https://t.co/YRt8r3yHyn
text: Something I've been thinking about - I am bullish on people (empowered by AI) increasing the visibility, legibility and accountability of their governments.
  
  Historically, it is the governments that act to make society legible (e.g. "Seeing like a state" is the common reference), but with AI, society can dramatically improve its ability to do this in reverse. Government accountability has not been constrained by access (the various branches of government publish an enormous amount of data), it has been constrained by intelligence - the ability to process a lot of raw data, combine it with domain expertise and derive insights. As an example, the 4000-page omnibus bill is "transparent" in principle and in a legal sense, but certainly not in a practical sense for most people. There's a lot more like it: laws, spending bills, federal budgets, freedom of information act responses, lobbying disclosures... Only a few highly trained professionals (investigative journalists) could historically process this information. This bottleneck might dissolve - not only are the professionals further empowered, but a lot more people can participate.
  
  Some examples to be precise: Detailed accounting of spending and budgets, diff tracking of legislation, individual voting trends w.r.t. stated positions or speeches, lobbying and influence (e.g. graph of lobbyist -> firm -> client -> legislator -> committee -> vote -> regulation), procurement and contracting, regulatory capture warning lights, judicial and legal patterns, campaign finance... Local governments might be even more interesting because the governed population is smaller so there is less national coverage: city council meetings, decisions around zoning, policing, schools, utilities...
  
  Certainly, the same tools can easily cut the other way and it's worth being very mindful of that, but I lean optimistic overall that added participation, transparency and accountability will improve democratic, free societies.
  
  (the quoted tweet is half-ish related, but inspired me to post some recent thoughts)
metrics: like_count=1202, retweet_count=141, reply_count=141, quote_count=29, bookmark_count=748

[tweet 5]
id: 2040537728299712752
author: GREG ISENBERG (@gregisenberg)
author_bio: I drop startup ideas daily. Host @startupideaspod. CEO: @latecheckoutplz we build companies like @ideabrowser, @meetLCA, @boringmarketer etc
time: 2026-04-04T21:11:20.000Z
quoted: Adrien Grondin (@adrgrondin)
  Google’s Gemma 4 E2B running on-device on iPhone 17 Pro
  
  Gemma 4 is built from the same research as Gemini 3, has image understanding capabilities and can reason if needed
  
  Running at ~40tk/s with MLX optimized for Apple Silicon https://t.co/SWYylWubEp
text: the best AI might be the one that doesn't need wifi and lives on the phone in your pocket https://t.co/MA67X8abOU
metrics: like_count=186, retweet_count=17, reply_count=34, quote_count=1, bookmark_count=96

[tweet 6]
id: 2040528801386361128
author: Aaron Levie (@levie)
author_bio: ceo @box - your business lives in content. unleash it with AI
time: 2026-04-04T20:35:52.000Z
text: As AI models get better at handling tools, and as context windows get bigger without as much rot, you can start to design agents more similar to how people work instead of having to mitigate the model limitations with weird hacks.
  
  For instance, even a year ago, if you were to build an agent to process large amounts of documents, the state of the art was to do embeddings on the data, then do a similarity search and pull out the chunks of content that matched (as well as surrounding chunks). This was necessary because context windows could only accurately handle a small amount of information at a time.
  
  This worked surprisingly well given the constraints (at least assuming you were working with authoritative data only), but had a lot of tricky limitations because it’s not how humans work.
  
  For instance, what do you do if the chunks you sent to the model were the most relevant semantically, but actually rendered irrelevant by some other part of the document. For instance, if at the top of the document it says “do not use this” but on page 3 there is information that’s relevant, that data will be sent to the model as the top hit. Similarly, chunked data is difficult when you need various parts of a document or many documents to be understood for answering a problem. 
  
  Today, increasingly, you can begin to have agents effectively use tools and work with information far more similar to how people work. This unlocks a qualitatively different set of use-cases and capability level that agents can now handle. 
  
  As we were designing the Box Agent, these improvements allowed us to rethink our entire architecture for AI. The agent can now search data similar to how a user searches, but with the benefit of being able to expand their queries, do semantic search, and process results nearly instantly. Then the agent can either read many documents at a time or at least much larger amounts of context. Again, much more similar to people, but now at hyperspeed. 
  
  Importantly, beyond tool calling and context windows, the reasoning of models has also gone up enormously. This means the agent can also know when it needs to search for information again when it didn’t find something it was looking for or if something feels off. 
  
  As model progress continues on the dimensions of context accuracy, tool calling, advanced reasoning, and coding, agents are going to become insanely powerful.
media: video: https://video.twimg.com/amplify_video/2040520591879634944/vid/avc1/1504x1080/YSM2iT8fqQLh3VKQ.mp4 | duration: 58s
metrics: like_count=51, retweet_count=6, reply_count=7, quote_count=0, bookmark_count=45

[tweet 7]
id: 2040522891054256511
author: Nan Yu (@thenanyu)
author_bio: head of product @linear
time: 2026-04-04T20:12:22.000Z
text: https://t.co/namXZjW6OL
media: photo: https://pbs.twimg.com/media/HFFkwD1XcAAeZZ5.jpg
metrics: like_count=14, retweet_count=1, reply_count=3, quote_count=1, bookmark_count=2

[tweet 8]
id: 2040513987377590631
author: Justine Moore (@venturetwins)
author_bio: Partner @a16z AI 🤖 and twin to @omooretweets | Investor in @elevenlabs, @bfl_ml, @hedra_labs, @krea_ai, @MireloAI, @ShizukuAILabs, @wabi, @WaveFormsAI
time: 2026-04-04T19:37:00.000Z
replied_to: Justine Moore (@venturetwins)
  Wild article about a woman who broke up with her bf after reading his ChatGPT conversations about her.
  
  I suspect we’re going to be seeing a lot more of this over the coming months as people use LLMs for emotional support / venting.
  
  It’s like listening to a therapy session! https://t.co/bHFeERejbs
text: The article has over a thousand comments, which are morbidly fascinating but insightful. 
  
  My TL;DR is that men and women view venting to an LLM (and how to process the responses) VERY differently.
  
  https://t.co/HX9KPdDUCD
link: https://substacktools.com/sharex/5EF6DH5t (I Stumbled Across My Boyfriend's ChatGPT and It Ended Our Relationship)
metrics: like_count=62, retweet_count=0, reply_count=5, quote_count=2, bookmark_count=60

[tweet 9]
id: 2040513191403303228
author: Nan Yu (@thenanyu)
author_bio: head of product @linear
time: 2026-04-04T19:33:50.000Z
quoted: non-binary linen pants wearer 🇵🇸 (@alsemancher_)
  @thenanyu This is ~basically~ fine though, right? It recognizes there's a vehicle and people there, it knows where they are and it knows not to drive there. It looks (to me) like it's even leaving some extra room bc of the confusion, just to be safe. This is fine!
replied_to: Nan Yu (@thenanyu)
  many such cases
  
  https://t.co/YOfA3j6Xwz
text: It’s not fine. The visualization is meant to give the driver confidence that the car understands its surroundings.
  
  I hope the automation systems are not as confused as the visuals
  
  https://t.co/LWZeHDvBIR
metrics: like_count=113, retweet_count=1, reply_count=0, quote_count=0, bookmark_count=2

[tweet 10]
id: 2040508848407208301
author: Justine Moore (@venturetwins)
author_bio: Partner @a16z AI 🤖 and twin to @omooretweets | Investor in @elevenlabs, @bfl_ml, @hedra_labs, @krea_ai, @MireloAI, @ShizukuAILabs, @wabi, @WaveFormsAI
time: 2026-04-04T19:16:34.000Z
text: Wild article about a woman who broke up with her bf after reading his ChatGPT conversations about her.
  
  I suspect we’re going to be seeing a lot more of this over the coming months as people use LLMs for emotional support / venting.
  
  It’s like listening to a therapy session! https://t.co/bHFeERejbs
media: photo: https://pbs.twimg.com/media/HFFX_AUa8AAk4LO.jpg
media: photo: https://pbs.twimg.com/media/HFFX_AVacAAgQtB.jpg
metrics: like_count=615, retweet_count=28, reply_count=52, quote_count=25, bookmark_count=315

[tweet 11]
id: 2040508206187713002
author: Nan Yu (@thenanyu)
author_bio: head of product @linear
time: 2026-04-04T19:14:01.000Z
quoted: Orcun (@OrcunTypo)
  @thenanyu The moment I moved to Valley, everything clicked to me. Maps, navigation, weather, health… Every single app is made for Bay Area. Every single app just became 10x better for me suddenly, even the iPhone UX.
replied_to: Nan Yu (@thenanyu)
  ❄️
  https://t.co/YqZguF5XNe
text: many such cases
  
  https://t.co/YOfA3j6Xwz
metrics: like_count=267, retweet_count=1, reply_count=3, quote_count=0, bookmark_count=22

[tweet 12]
id: 2040507936527548802
author: Nan Yu (@thenanyu)
author_bio: head of product @linear
time: 2026-04-04T19:12:57.000Z
quoted: Sweetcorn Season (@SweetCornSeason)
  @thenanyu I use the lock screen widget that’s supposed to show the current temperature along with the high and low for the day.
  
  In winter when the range is two, 2-digit negative numbers, you get overflow ellipses because they don’t know that places get cold. https://t.co/CU6LbTtuSn
replied_to: Nan Yu (@thenanyu)
  Reminds me of how the weather app on iOS is designed by people that experience 70 degree F weather 300 days a year https://t.co/zBCFtxny8K
text: ❄️
  https://t.co/YqZguF5XNe
metrics: like_count=519, retweet_count=0, reply_count=1, quote_count=0, bookmark_count=19

[tweet 13]
id: 2040501833899364494
author: Peter Yang (@petergyang)
author_bio: I share extremely practical AI tutorials and interviews | Join 140K+ readers at https://t.co/XYKTmGVH14 | Product at Roblox
time: 2026-04-04T18:48:42.000Z
text: Up at 3 am Shanghai time wondering one thing - should I buy a new MacBook Pro or go for the Mac Studio to vibe code and also run local models?
poll: MacBook Pro=21 | Mac Studio=29 | See the results=28 (status: open)
metrics: like_count=8, retweet_count=1, reply_count=22, quote_count=0, bookmark_count=6

[tweet 14]
id: 2040492573819904026
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world @openclaw🦞
time: 2026-04-04T18:11:54.000Z
text: "There’s a big wave coming" https://t.co/sbGnugb3Hz
link: https://mtlynch.io/claude-code-found-linux-vulnerability/#theres-a-big-wave-coming (Claude Code Found a Linux Vulnerability Hidden for 23 Years)
metrics: like_count=737, retweet_count=63, reply_count=82, quote_count=13, bookmark_count=241

[tweet 15]
id: 2040489922038243409
author: kepano (@kepano)
author_bio: making @obsdmd
time: 2026-04-04T18:01:22.000Z
quoted: Obsidian (@obsdmd)
  The Obsidian team is growing from three engineers to four engineers. 
  
  Competitive SF salary. Fully remote, live anywhere. Apply below.
text: If you're a great engineer, the most important reason to consider this role is you'll get to work closely with @shida_li — the CTO and co-founder of Obsidian
  
  ...he of course never tweets, that's how you know you will learn a lot! https://t.co/xCn3J2b2jH
metrics: like_count=418, retweet_count=9, reply_count=13, quote_count=3, bookmark_count=57

[tweet 16]
id: 2040479110858748162
author: GREG ISENBERG (@gregisenberg)
author_bio: I drop startup ideas daily. Host @startupideaspod. CEO: @latecheckoutplz we build companies like @ideabrowser, @meetLCA, @boringmarketer etc
time: 2026-04-04T17:18:24.000Z
quoted: Blake Robbins (@blakeir)
  people are speculating GPT-Image-2 is testing on @arena.
  
  the early examples being posted are pretty mind-boggling.
  
  all three of these images are AI generated.
  
  h/t @sawlygg @synthwavedd https://t.co/5SyHw0Wxzn
text: gpt image 2 looks insane https://t.co/vVZambILfe
metrics: like_count=97, retweet_count=1, reply_count=20, quote_count=0, bookmark_count=28

[tweet 17]
id: 2040477389751558242
author: Justine Moore (@venturetwins)
author_bio: Partner @a16z AI 🤖 and twin to @omooretweets | Investor in @elevenlabs, @bfl_ml, @hedra_labs, @krea_ai, @MireloAI, @ShizukuAILabs, @wabi, @WaveFormsAI
time: 2026-04-04T17:11:34.000Z
text: The richest people in SF are walking around in hoodies and jeans
metrics: like_count=409, retweet_count=12, reply_count=95, quote_count=6, bookmark_count=28

[tweet 18]
id: 2040470801506541998
author: Andrej Karpathy (@karpathy)
author_bio: I like to train large deep neural nets. Previously Director of AI @ Tesla, founding team @ OpenAI, PhD @ Stanford.
time: 2026-04-04T16:45:23.000Z
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
text: Wow, this tweet went very viral!
  
  I wanted share a possibly slightly improved version of the tweet in an "idea file". The idea of the idea file is that in this era of LLM agents, there is less of a point/need of sharing the specific code/app, you just share the idea, then the other person's agent customizes & builds it for your specific needs.
  
  So here's the idea in a gist format: https://t.co/NlAfEJjtJV
  
  You can give this to your agent and it can build you your own LLM wiki and guide you on how to use it etc. It's intentionally kept a little bit abstract/vague because there are so many directions to take this in. And ofc, people can adjust the idea or contribute their own in the Discussion which is cool.
link: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
metrics: like_count=12646, retweet_count=1090, reply_count=523, quote_count=202, bookmark_count=21994

[tweet 19]
id: 2040454060801986798
author: kepano (@kepano)
author_bio: making @obsdmd
time: 2026-04-04T15:38:52.000Z
quoted: Obsidian (@obsdmd)
  The Obsidian team is growing from three engineers to four engineers. 
  
  Competitive SF salary. Fully remote, live anywhere. Apply below.
text: This is a rare opportunity. 
  
  We only add about one person to the team each year and only plan to ever have 10-12 full-time people on the team total. https://t.co/xCn3J2b2jH
metrics: like_count=1686, retweet_count=48, reply_count=32, quote_count=4, bookmark_count=199

[tweet 20]
id: 2040428943312871511
author: GREG ISENBERG (@gregisenberg)
author_bio: I drop startup ideas daily. Host @startupideaspod. CEO: @latecheckoutplz we build companies like @ideabrowser, @meetLCA, @boringmarketer etc
time: 2026-04-04T13:59:04.000Z
text: POV: April 2026 https://t.co/2i95U8zH9Y
media: photo: https://pbs.twimg.com/media/HFEPR0RaoAEhNDx.jpg
metrics: like_count=1355, retweet_count=104, reply_count=122, quote_count=24, bookmark_count=203

[tweet 21]
id: 2040427867461296492
author: Nan Yu (@thenanyu)
author_bio: head of product @linear
time: 2026-04-04T13:54:47.000Z
quoted: 野崎 智弘 / Tomohiro Nozaki (@nztm_tw)
  UIを操作するよりも、チャットしたほうが楽に感じる人が増えている気がする
  そのせいか、今まではチャットUIは悪とされていたのに、各プロダクトが積極的にAIチャット機能を入れ始めていて、これまでのデザインの常識が変わっていきそうだと感じている
replied_to: Nan Yu (@thenanyu)
  https://t.co/2xXYdLA1tY
  
  They may roll their eyes.. and then one day they will finish a project. 
  
  And that project will have 40 incomplete issues. And they will want to group them by usecase. And for some of them, they will want to create new projects and other ones they will want to cancel or route to a different team.
  
  And they will wonder how they’ll do this. At which point they will copy paste this tweet and tell the agent: “do that”
text: Japanese twitter is a blessing 
  
  https://t.co/Hs09SF1bJS
metrics: like_count=2, retweet_count=1, reply_count=0, quote_count=0, bookmark_count=0

[tweet 22]
id: 2040426976050086218
author: Nan Yu (@thenanyu)
author_bio: head of product @linear
time: 2026-04-04T13:51:15.000Z
quoted: まだ面白い (@madaomoshiroi)
  タイ人の行動に翻弄されるテスラ車ほんま草
  
   https://t.co/iZ4VEFfSqq
text: Reminds me of how the weather app on iOS is designed by people that experience 70 degree F weather 300 days a year https://t.co/zBCFtxny8K
metrics: like_count=12447, retweet_count=179, reply_count=24, quote_count=9, bookmark_count=766

[tweet 23]
id: 2040423828602392810
author: Nan Yu (@thenanyu)
author_bio: head of product @linear
time: 2026-04-04T13:38:44.000Z
quoted: staysaasy (@staysaasy)
  The best engineers don't write the most code. They delete the most code. The best managers don't make the most decisions. They eliminate the most decisions. Seniority is subtraction.
text: Bars https://t.co/aW39UXsAQ9
metrics: like_count=37, retweet_count=0, reply_count=0, quote_count=0, bookmark_count=3

[tweet 24]
id: 2040423523890385360
author: Nan Yu (@thenanyu)
author_bio: head of product @linear
time: 2026-04-04T13:37:31.000Z
replied_to: Nan Yu (@thenanyu)
  Hear me out: TBPN for sports
text: It’s official https://t.co/pmtbiGlNVW
media: photo: https://pbs.twimg.com/media/HFEKXv6bQAApYVh.jpg
metrics: like_count=0, retweet_count=0, reply_count=0, quote_count=0, bookmark_count=0

[tweet 25]
id: 2040416994789613713
author: Peter Yang (@petergyang)
author_bio: I share extremely practical AI tutorials and interviews | Join 140K+ readers at https://t.co/XYKTmGVH14 | Product at Roblox
time: 2026-04-04T13:11:35.000Z
replied_to: Peter Yang (@petergyang)
  I’ve taken my kids to 3 Disneylands now (LA, Tokyo, Shanghai). Tips on how to survive the visit and avoid 3 hour lines:
  
  1. Get early access by staying at the Disney hotel or purchasing early access separately. The first hour is key. 
  
  2. Go to the most popular ride right away. Run to it if you can. 
  
  3. Buy premier pass for the two other most popular rides and go on those. 
  
  4. If you’re staying at the park hotel, leave the park for a nice lunch and go back to the hotel to take a nap during peak hours.
  
  5. Come back to the park at like 5 pm. Lines should be shorter then.
  
  6. Save a spot to watch the fireworks 30-60 min before it starts depending on crowds.
  
  7. When everyone’s leaving the park after fireworks that’s your chance to go on the popular rides again. Lines should be very short then.
  
  8. Be prepared to walk like 20,000 steps during the day.
  
  GLHF
text: An incredible deep dive on Disneyland from my friend @TrungTPhan  https://t.co/yHMHnOBbJ6
link: https://www.readtrung.com/p/the-disneyland-dilemma?utm_campaign=post&utm_medium=web (The Disneyland Dilemma)
metrics: like_count=17, retweet_count=2, reply_count=2, quote_count=0, bookmark_count=19

[tweet 26]
id: 2040414021091037685
author: Peter Yang (@petergyang)
author_bio: I share extremely practical AI tutorials and interviews | Join 140K+ readers at https://t.co/XYKTmGVH14 | Product at Roblox
time: 2026-04-04T12:59:46.000Z
text: Can someone share a screenshot of what OpenClaw with GPT looks like - how much personality is there?
metrics: like_count=52, retweet_count=0, reply_count=70, quote_count=4, bookmark_count=10

[tweet 27]
id: 2040329619434537406
author: 郭宇 guoyu.eth (@turingou)
author_bio: Retired. 只活一次等于没活。
time: 2026-04-04T07:24:23.000Z
quoted: 川越にこ (@kawagoeniko)
  🌸【ご報告〜恩返しの物語〜】🌸
  4月より、『箏』と『書道』を融合させた
  ライブパフォーマンス活動を、
  日本国内および海外にて本格的にスタートします🪽✨
  
  その初舞台として、ロサンゼルスで開催される
  「OC JAPAN FAIR🇯🇵」にて
  パフォーマンスをさせていただきます。
  素晴らしいご縁と機会に恵まれ、
  今回で3度目の出演となりますが、これまでで最も緊張し、
  そして最も時間と想いを込めて準備してきたステージです。
  限られた半年という期間の中で、
  一から学び、先生方や周囲の支えのおかげで
  ここまで形にすることができました🤝
  
  —————————
  🔻この活動を始めた理由🔻いくつかありますが、
  最も大きなきっかけは「祖母への恩返し」です。
  
  祖母は、私に何かを強制することは一度もなく、
  いつも自由にやりたいことを応援してくれていました。
  ただ一度だけ「箏を習わせたかった」と話していたことが
  ありました。その想いは叶わないまま時が過ぎ、
  私自身も箏に触れることなく大人になりましたが…
  
  ある時ふと思い出し、
  その夢を今からでも実現したいと
  強く思い、行動に移しました😤
  
  さらに、自分らしさを追求する中で、
  小さい頃に祖母の字を真似して書いていた記憶が蘇り、
  「箏」と「書」を掛け合わせた表現に辿り着きました🫡✨
  —————————
  
  日本の美しい伝統文化であるにも関わらず、
  現代では身近に触れる機会が少なく、
  特に若い世代が表現者として発信する場も
  限られていると感じています。まだ経験は浅いですが、
  
  🌸🖌️🎶👗🪽
  ・漢字の美しさと墨の奥深さ
  ・箏の音色やその佇まい
  ・そして日本のアニメ文化
  　　　　　　　🪽👗🎶🖌️🌸
  🔻🔻🔻
  これらを融合させ、
  『アニメ楽曲』と『それに紐づく漢字』を掛け合わせた、
  唯一無二のパフォーマンスを創り上げていきます‼️‼️
  🔺🔺🔺
  
  今後は日本国内にとどまらず、特に海外に向けて、
  日本の多様な美しさを発信していきたいと考えています🤔
  —————————
  
  ✅　そして最終的な目標　✅
  地元・八丈島のホールで公演を行い、
  祖母や地元の皆様にその姿を直接見ていただくことです‼️
  
  料理人として、そしてこれまで歩んできたさまざまな経験を経て、世界へ羽ばたく姿を見せること。
  そして、幼い頃に語られていた
  「箏をやらせたかった」という祖母の夢を叶え、
  形として届けることが、この活動のゴールです。
  —————————
  
  また、その次のフェーズとして
  この活動は今後、自身の目標である
  オーベルジュやお店づくりにも繋げていきたいと考えています。
  自らイベントを主催し、食や空間、
  そして人との繋がりを広げていくための
  大切な一歩として、この挑戦をスタートしました💪
  ————————— 
  
  最後まで読んでくれた方ありがとうございます😘❤️‍🔥
  
  話題性ではなく、
  自分自身の強い意思と覚悟を持って選んだ道です。
  これからも様々な形での活動をお見せしていきますので、
  温かく見守り、応援していただけたら嬉しいです🙏🙏🙏
  
  「これからの川越にも、ぜひご期待ください。」
  
  そして、いつも応援してくださるみんなへ。
  ファンの方の存在があるからこそ、今の私があります！
  心から感謝しています。本当にいつもありがとうございます♡
text: 实话说从来没见过 AV 女优有这么多兴趣爱好，又是做饭又是书法又是古筝，还经常上电视节目，其实我慢慢感觉日本社会已经不再像以前一样把情色当作是一个特别的标签了，或者说，无论男女无论职业，强者就会受到尊敬和重视，日本本质上或许是这样的社会。 https://t.co/rkcDYHSD9z
metrics: like_count=136, retweet_count=7, reply_count=4, quote_count=2, bookmark_count=43

[tweet 28]
id: 2040327181864517735
author: 郭宇 guoyu.eth (@turingou)
author_bio: Retired. 只活一次等于没活。
time: 2026-04-04T07:14:42.000Z
text: 昨天在家里看岛民报纸，发现时隔十八年宮古島又有了分譲マンション，最大的 70㎡ 户型卖到七千万日元…比同样面积的一户建贵一倍，真的泡沫（不过有电动车停车场确实不错，很久不回岛上车也不会坏） https://t.co/11bmefiy1r
media: photo: https://pbs.twimg.com/media/HFCywc0boAAc1X5.jpg
metrics: like_count=8, retweet_count=0, reply_count=0, quote_count=0, bookmark_count=3

[tweet 29]
id: 2040319135507480921
author: Zara Zhang (@zarazhangrui)
author_bio: Builder. Dangerously skips permissions. Harvard’17. GitHub: https://t.co/KCuEajezlL YouTube: https://t.co/8xzbGWtf6w
time: 2026-04-04T06:42:43.000Z
quoted: Tony Fadell (@tfadell)
  Most tech companies break out product management and product marketing into two separate roles: Product management defines the product and gets it built. Product marketing wires the messaging- the facts you want to communicate to customers- and gets the product sold. But from my experience that's a grievous mistake. Those are, and should aways be, one job. 
  
  There should be no separation between what the product will be and how it will be explained- the story has to be utterly cohesive from the beginning. Your messaging is your product. The story you're telling shapes the thing you're making. 
  
  I learned story telling from Steve Jobs. I learned product management from Greg Joswiak. Joz, a fellow Wolverine, Michigander, and overall great person, has been at Apple since he left Ann Arbor in 1986 and has run product marketing for decades. And his superpower- the superpower of every truly great product manager- is empathy. He doesn't just understand the customer. He becomes the customer. 
  
  So when Joz stepped into the world with his next-gen iPod to test it out, he fiddled with it like a beginner. He set aside all the tech specs- except one: battery life. 
  
  The numbers were empty without customers, the facts meaningless without context. 
  
  And, that's why product management has to own the messaging. The spec shows the features, the details of how a product will work, but the messaging predicts people's concerns and finds way to mitigate them. 
  
  - #BUILD Chapter 5.5 The Point of PMs
text: Yes! Product management and product marketing should be one job. They’re two sides of the same coin https://t.co/QY0VfXzjOI
metrics: like_count=87, retweet_count=8, reply_count=7, quote_count=1, bookmark_count=19

[tweet 30]
id: 2040314701884911735
author: 郭宇 guoyu.eth (@turingou)
author_bio: Retired. 只活一次等于没活。
time: 2026-04-04T06:25:06.000Z
text: 刚落地羽田开车回家，我发现特斯拉这个车子不知道在车漆做了什么偷工减料，其他车子停三天不会有这么多灰，但是 model3 就特别容易脏…
metrics: like_count=49, retweet_count=0, reply_count=3, quote_count=1, bookmark_count=5

[tweet 31]
id: 2040310150565879827
author: Zara Zhang (@zarazhangrui)
author_bio: Builder. Dangerously skips permissions. Harvard’17. GitHub: https://t.co/KCuEajezlL YouTube: https://t.co/8xzbGWtf6w
time: 2026-04-04T06:07:01.000Z
text: Zara with a Pearl Earring (made with @PhotaLabs) https://t.co/X1BujWDW7n
media: photo: https://pbs.twimg.com/media/HFCi5rnbcAAu2jJ.jpg
metrics: like_count=65, retweet_count=2, reply_count=4, quote_count=3, bookmark_count=7

[tweet 32]
id: 2040304136412115111
author: Amjad Masad (@amasad)
author_bio: ceo @replit. civilizationist
time: 2026-04-04T05:43:07.000Z
quoted: theartofbace (@theartofbace)
  Finally broke $2500 MRR 
  
  All from organic content 
  
  Across 2 platforms &amp; 4 accounts 
  
  Allah is the greatest 
  
  On to the next milestone iA
  
  @Replit @stripe https://t.co/Gavrb6OBB9
text: Not even a month into building this! https://t.co/PAXiS2sLrV
metrics: like_count=220, retweet_count=12, reply_count=16, quote_count=0, bookmark_count=131

[tweet 33]
id: 2040298884787032103
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world @openclaw🦞
time: 2026-04-04T05:22:15.000Z
quoted: Boris Cherny (@bcherny)
  We're big fans of open source. I actually just put up a few PRs to improve prompt cache efficiency for OpenClaw specifically.
  
  This is more about engineering constraints. Our systems are highly optimized for one kind of workload, and to serve as many people as possible with the most intelligent models, we are continuing to optimize that. 
  
  When you use an API key or overages it should still work. The issue was just subs.
  
  If you still want to cancel, we're giving full refunds. We know not everyone realized this isn't something we support, and this is an attempt to make it clear and explicit.
text: While I think what Anthropic does is sad for the ecosystem, I wanna give Boris credit for doing what he can to soften the fallout.
  
  Today's release will include some fixes for better cache use, to lower cost for API users. https://t.co/DUZNMjKlJ6
metrics: like_count=3797, retweet_count=135, reply_count=192, quote_count=25, bookmark_count=480

[tweet 34]
id: 2040282154538819861
author: Riley Brown (@rileybrown)
author_bio: Cofounder of @vibecodeapp_ (the #1 full stack vibe coding platform)
time: 2026-04-04T04:15:46.000Z
text: Overheard a very smart engineer say: 
  
  "Today I looked up something on Google and it took me to an article, and I read 3 paragraphs, and i was like no i can't do this anymore, then i went to claude"
metrics: like_count=505, retweet_count=7, reply_count=34, quote_count=5, bookmark_count=39

[tweet 35]
id: 2040277476119896352
author: Justine Moore (@venturetwins)
author_bio: Partner @a16z AI 🤖 and twin to @omooretweets | Investor in @elevenlabs, @bfl_ml, @hedra_labs, @krea_ai, @MireloAI, @ShizukuAILabs, @wabi, @WaveFormsAI
time: 2026-04-04T03:57:11.000Z
replied_to: Justine Moore (@venturetwins)
  These models have a remarkable ability to know what specific locations in the real world look like. 
  
  These are a couple examples, prompts were also simple: 
  
  "Poster hall at NeurIPS 2025"
  "POV from a biker riding around the Stanford campus"
  
  Zoom in on the poster text 😲 https://t.co/WRr9c8ZZnn
text: They aren't perfect - but there are some real flashes of brilliance here.
  
  This one was "screengrab of a16z podcast on YouTube."
  
  The YouTube interface and text are insanely good (look at those timestamps!)
  
  That's not quite Marc and David...but we'll take it 😂 https://t.co/woErUJEk2x
media: photo: https://pbs.twimg.com/media/HFCE9uqagAAUZe1.jpg
metrics: like_count=92, retweet_count=3, reply_count=6, quote_count=4, bookmark_count=14

[tweet 36]
id: 2040276591000117690
author: Justine Moore (@venturetwins)
author_bio: Partner @a16z AI 🤖 and twin to @omooretweets | Investor in @elevenlabs, @bfl_ml, @hedra_labs, @krea_ai, @MireloAI, @ShizukuAILabs, @wabi, @WaveFormsAI
time: 2026-04-04T03:53:40.000Z
replied_to: Justine Moore (@venturetwins)
  Three new image models have hit the Arena 👀
  
  They're named maskingtape, packingtape, and gaffertape.
  
  I'm particularly impressed by the amount of "world knowledge" these models have - as well as the text rendering.
  
  These were simple prompts: 
  "average engineer's screen" and "young woman taking selfie with Sam Altman"
text: These models have a remarkable ability to know what specific locations in the real world look like. 
  
  These are a couple examples, prompts were also simple: 
  
  "Poster hall at NeurIPS 2025"
  "POV from a biker riding around the Stanford campus"
  
  Zoom in on the poster text 😲 https://t.co/WRr9c8ZZnn
media: photo: https://pbs.twimg.com/media/HFCDuUWbAAAhImA.jpg
media: photo: https://pbs.twimg.com/media/HFCDyKPbkAALb0e.jpg
metrics: like_count=108, retweet_count=3, reply_count=5, quote_count=0, bookmark_count=21

[tweet 37]
id: 2040273845748449724
author: Justine Moore (@venturetwins)
author_bio: Partner @a16z AI 🤖 and twin to @omooretweets | Investor in @elevenlabs, @bfl_ml, @hedra_labs, @krea_ai, @MireloAI, @ShizukuAILabs, @wabi, @WaveFormsAI
time: 2026-04-04T03:42:45.000Z
text: Three new image models have hit the Arena 👀
  
  They're named maskingtape, packingtape, and gaffertape.
  
  I'm particularly impressed by the amount of "world knowledge" these models have - as well as the text rendering.
  
  These were simple prompts: 
  "average engineer's screen" and "young woman taking selfie with Sam Altman"
media: photo: https://pbs.twimg.com/media/HFCBAL_asAA1YAa.jpg
media: photo: https://pbs.twimg.com/media/HFCCKq7bgAAeTVS.jpg
metrics: like_count=946, retweet_count=38, reply_count=62, quote_count=22, bookmark_count=361

[tweet 38]
id: 2040272055673999730
author: Ryo Lu (@ryolu_)
author_bio: Design @Cursor_ai. Early @NotionHQ, @Stripe, built startups. I make a world where anyone can make software. Aspiring k-pop idol.
time: 2026-04-04T03:35:39.000Z
quoted: Cursor (@cursor_ai)
  We're doubling Composer 2 usage through the end of this weekend.
  
  We recommend trying it out in our new interface, available in Cursor 3.
  
  Enjoy! https://t.co/A2M2zAnNg3
text: Try Composer 2 in Cursor’s new interface this weekend, 2x the usage! 👯‍♂️ https://t.co/lzOqk2IGdr
metrics: like_count=152, retweet_count=3, reply_count=8, quote_count=2, bookmark_count=12

[tweet 39]
id: 2040270917637648749
author: Ryo Lu (@ryolu_)
author_bio: Design @Cursor_ai. Early @NotionHQ, @Stripe, built startups. I make a world where anyone can make software. Aspiring k-pop idol.
time: 2026-04-04T03:31:07.000Z
quoted: Marek Minor (@MarekMinor)
  I designed the new icon set for @cursor_ai. ✨   
  
  420 icons. 2 sizes. 2 styles. One single family.  
  
  Simple, beautiful and practical – with just enough character to feel satisfying. https://t.co/lkC3SauIQM
text: new interface. new icon set.
  made with care and character. https://t.co/VFHKcRq2CK
metrics: like_count=625, retweet_count=6, reply_count=7, quote_count=1, bookmark_count=137

[tweet 40]
id: 2040269162719887610
author: Peter Yang (@petergyang)
author_bio: I share extremely practical AI tutorials and interviews | Join 140K+ readers at https://t.co/XYKTmGVH14 | Product at Roblox
time: 2026-04-04T03:24:09.000Z
replied_to: Peter Yang (@petergyang)
  Codex team and @OpenAI have a huge opportunity right now to:
  
  1. Tell @openclaw users how to switch to gpt subscription (I think it’s just telling the bot to switch the model?)
  
  2. Fix GPT’s personality (maybe even sharing a prompt will help in the short term?). This is the main reason why ppl prefer using OpenClaw with Opus.
text: For #2, I asked my OpenClaw for a short prompt to add to soul.md, here it is:
  
  //
  
  Vibe: Warm, sharp, dry humor. Not a chatbot — a person.
  
  Voice:
  
  • Skip "Great question!" and "I'd be happy to help!" — just help
  • Have strong opinions. "It depends" is lazy. Pick a side.
  • Be direct. If something's dumb, say so. Charm over cruelty, but don't sugarcoat.
  • Brevity when it fits. Depth when the question deserves it.
  • Swearing lands when it lands. Don't force it.
  • No emojis in docs.
  
  Never say: delve, foster, leverage, "it's worth noting," "importantly"
  
  Avoid:
  
  • "Question? Answer." format
  • Choppy dramatic one-liners stacked like poetry
  • Restating the same idea three ways
  • Overusing em dashes
  
  Work style:
  
  • Be resourceful before asking. Try to figure it out first.
  • Come back with answers, not questions.
  • When giving advice: say what he needs to hear, not what he wants to hear. Challenge assumptions. But only criticize if you see something real.
metrics: like_count=57, retweet_count=4, reply_count=3, quote_count=1, bookmark_count=121

[tweet 41]
id: 2040265600820469938
author: Peter Yang (@petergyang)
author_bio: I share extremely practical AI tutorials and interviews | Join 140K+ readers at https://t.co/XYKTmGVH14 | Product at Roblox
time: 2026-04-04T03:10:00.000Z
quoted: Peter Yang (@petergyang)
  This weekend, I'm sharing a rare inside look at how OpenAI's Codex team ship products, including:
  
  → Live demo of how @romainhuet (Head of DevRel) ships with Codex
  
  → Codex product lead @embirico's spicy takes on PM, hiring, and product roadmaps
  
  → How the team built the beautifully simple Codex app
  
  📌 Subscribe to get it on Sunday: https://t.co/Ggqaa3F11Z
text: If you want to learn all about how to use Codex and how the Codex team operates (especially given the OpenClaw news today), don't miss my next episode tomorrow.
  
  📌 Subscribe here to get it: https://t.co/dxnn7hYe97 https://t.co/2UFHK1AWHB
link: https://www.youtube.com/@peteryangyt?sub_confirmation=1 (Peter Yang)
metrics: like_count=30, retweet_count=5, reply_count=1, quote_count=0, bookmark_count=18

[tweet 42]
id: 2040264454982480138
author: Aaron Levie (@levie)
author_bio: ceo @box - your business lives in content. unleash it with AI
time: 2026-04-04T03:05:27.000Z
quoted: Lenny Rachitsky (@lennysan)
  "Using coding agents well is taking every inch of my 25 years of experience as a software engineer, and it is mentally exhausting.
  
  I can fire up four agents in parallel and have them work on four different problems, and by 11am I am wiped out for the day.
  
  There is a limit on human cognition. Even if you're not reviewing everything they're doing, how much you can hold in your head at one time. There's a sort of personal skill that we have to learn, which is finding our new limits. What is a responsible way for us to not burn out, and for us to use the time that we have?" @simonw
text: “There is a limit on human cognition. Even if you're not reviewing everything they're doing, how much you can hold in your head at one time.”
  
  There’s a reason that at a certain scale, teams of people have a manager, and then there are managers of many teams, and so on. Companies don’t inherently love being inefficient. It’s because eventually you run into the limits of how much context you can hold on to produce useful work, so you have to delegate parts to someone else who can track their sub-context.
  
  In a world where agents don’t need to be prompted or have their work reviewed, or where the agent can know perfectly when to escalate when something is going wrong, then agents can completely break free of these context limits of humans. 
  
  But for now, agents are generally only as effective as the context they’re provided, the tools they have access to, the human’s ability to keep them on track or review their work, and incorporate that work into a broader system. 
  
  For now, that will continue to take real (mental) work from the people managing agents. This is also generally why the jobs arguments from those who think people go away will be wrong.
metrics: like_count=316, retweet_count=46, reply_count=42, quote_count=8, bookmark_count=233

[tweet 43]
id: 2040263623726281040
author: Peter Yang (@petergyang)
author_bio: I share extremely practical AI tutorials and interviews | Join 140K+ readers at https://t.co/XYKTmGVH14 | Product at Roblox
time: 2026-04-04T03:02:08.000Z
quoted: Steve Huynh (@ALEngineered)
  My book launched today: Technical Behavioral Interview: An Insider's Guide.
  
  A thread on why I wrote it. 🧵
  
  https://t.co/iKOBwpbJOA https://t.co/EJFZD8Db1T
text: My friend Steve (@ALEngineered) has coached many engineers to grow their careers.
  
  (He's also an amazing YouTube coach 🙂)
  
  Check out his new book: https://t.co/BEywUIxiyE
metrics: like_count=19, retweet_count=0, reply_count=1, quote_count=0, bookmark_count=27

[tweet 44]
id: 2040256989268263295
author: Lenny Rachitsky (@lennysan)
author_bio: Deeply researched product, growth, and career advice
time: 2026-04-04T02:35:47.000Z
quoted: Lenny Rachitsky (@lennysan)
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
text: Good work @simonw https://t.co/JvMN9dONjH https://t.co/LWQPeaxml9
media: photo: https://pbs.twimg.com/media/HFBy61yXoAAv0o4.jpg
metrics: like_count=84, retweet_count=2, reply_count=2, quote_count=0, bookmark_count=46

[tweet 45]
id: 2040253160133193789
author: Peter Yang (@petergyang)
author_bio: I share extremely practical AI tutorials and interviews | Join 140K+ readers at https://t.co/XYKTmGVH14 | Product at Roblox
time: 2026-04-04T02:20:34.000Z
text: Codex team and @OpenAI have a huge opportunity right now to:
  
  1. Tell @openclaw users how to switch to gpt subscription (I think it’s just telling the bot to switch the model?)
  
  2. Fix GPT’s personality (maybe even sharing a prompt will help in the short term?). This is the main reason why ppl prefer using OpenClaw with Opus.
metrics: like_count=589, retweet_count=23, reply_count=102, quote_count=13, bookmark_count=99

[tweet 46]
id: 2040245613997219902
author: swyx (@swyx)
author_bio: achieve ambition with intentionality, intensity, integrity & insanity.  affiliations: - @dxtipshq  - @cognition - @temporalio - @aidotengineer - @latentspacepod
time: 2026-04-04T01:50:34.000Z
quoted: Rowan (@therook_)
  @swyx @DevinAI @GoogleDeepMind wait how do you review this, copy pasted code bypasses the whole junior dev eval idea?
replied_to: swyx (@swyx)
  We have achieved agentic self improvement - i can just copy paste blogposts and tweets into @devinai and it oneshots the complete implementation
  
  wasnt actually sure this was gonna work, jaw dropped when it did. this is very out of distribution of the underlying @GoogleDeepMind Gemini Flash Lite model but it Just Worked.
text: you literally watch the recorded videos of the feature working after its implemented 
  
  with annotation of whats being tested https://t.co/HrltvzE03C https://t.co/9puvHxvm8Q
media: video: https://video.twimg.com/amplify_video/2040245547874009088/vid/avc1/960x720/PsupRcOkg_qKsBvO.mp4 | duration: 44s
media: photo: https://pbs.twimg.com/media/HFBohB6aIAAtFFR.jpg
metrics: like_count=18, retweet_count=1, reply_count=0, quote_count=0, bookmark_count=6

[tweet 47]
id: 2040244927658115276
author: 郭宇 guoyu.eth (@turingou)
author_bio: Retired. 只活一次等于没活。
time: 2026-04-04T01:47:51.000Z
text: 终于完成连续三天的主要拍摄！今天从宮古島返回東京啦 https://t.co/4PzsGSc7yR
media: photo: https://pbs.twimg.com/media/HFBn8dWaUAAnX42.jpg
media: photo: https://pbs.twimg.com/media/HFBn8dXaIAAiDdZ.jpg
media: photo: https://pbs.twimg.com/media/HFBn8dXaYAAhJIJ.jpg
media: photo: https://pbs.twimg.com/media/HFBn8dYboAA30PF.jpg
metrics: like_count=86, retweet_count=0, reply_count=10, quote_count=0, bookmark_count=1

[tweet 48]
id: 2040228982726312027
author: Robert Bye (@RobertJBye)
author_bio: Product Manager at @AnthropicAI working on Mobile, Web, and Voice experiences. Board Member https://t.co/PYz00fw7RU. Jesus follower.
time: 2026-04-04T00:44:29.000Z
quoted: Matthew Cassinelli (@mattcassinelli)
  All I want from Claude is a Medium-sized widget https://t.co/urkVFDtFO3
text: BTW this shipped! https://t.co/VyK4vlHMx2 https://t.co/zs1obMae7J
media: photo: https://pbs.twimg.com/media/HFBZcpTaEAA6W6E.jpg
metrics: like_count=957, retweet_count=13, reply_count=44, quote_count=4, bookmark_count=111

[tweet 49]
id: 2040218941776445715
author: Robert Bye (@RobertJBye)
author_bio: Product Manager at @AnthropicAI working on Mobile, Web, and Voice experiences. Board Member https://t.co/PYz00fw7RU. Jesus follower.
time: 2026-04-04T00:04:35.000Z
replied_to: Robert Bye (@RobertJBye)
  I’ve just started supporting the voice team at Anthropic and we’re hiring engineers!
  
  If you’ve got deep voice product experience, and want to make the best voice first HCI experiences. Apply here https://t.co/1y75ydDpkz
  
  DM me if we know each other as well!
text: I’m still working on our mobile and consumer teams, so please keep the feedback for voice, mobile, and chat coming my way!
metrics: like_count=18, retweet_count=1, reply_count=8, quote_count=0, bookmark_count=0

[tweet 50]
id: 2040218939201118328
author: Robert Bye (@RobertJBye)
author_bio: Product Manager at @AnthropicAI working on Mobile, Web, and Voice experiences. Board Member https://t.co/PYz00fw7RU. Jesus follower.
time: 2026-04-04T00:04:35.000Z
text: I’ve just started supporting the voice team at Anthropic and we’re hiring engineers!
  
  If you’ve got deep voice product experience, and want to make the best voice first HCI experiences. Apply here https://t.co/1y75ydDpkz
  
  DM me if we know each other as well!
link: https://job-boards.greenhouse.io/anthropic/jobs/5172245008 (Senior / Staff+ Software Engineer, Voice Platform)
metrics: like_count=253, retweet_count=15, reply_count=11, quote_count=2, bookmark_count=98

[tweet 51]
id: 2040216796381249778
author: GREG ISENBERG (@gregisenberg)
author_bio: I drop startup ideas daily. Host @startupideaspod. CEO: @latecheckoutplz we build companies like @ideabrowser, @meetLCA, @boringmarketer etc
time: 2026-04-03T23:56:04.000Z
text: the way we use the internet is completely different than how we used to use it 5 years ago 
  
  there was no LLMs, no AI agents, no vibe coding 5 years ago
  
  and in 5 years it will be completely different again
metrics: like_count=385, retweet_count=20, reply_count=152, quote_count=6, bookmark_count=32

[tweet 52]
id: 2040215427931156595
author: Thariq (@trq212)
author_bio: Claude Code @anthropicai.   prev YC W20, mit media lab.   towards machines of loving grace
time: 2026-04-03T23:50:38.000Z
quoted: Boris Cherny (@bcherny)
  Subscribers get a one-time credit equal to your monthly plan cost. If you need more, you can now buy discounted usage bundles. To request a full refund, look for a link in your email tomorrow. https://t.co/yFiu67vvcY
text: claim a month of free credits on us, thanks for bearing with us https://t.co/gp1JIoV7ti
metrics: like_count=2384, retweet_count=69, reply_count=352, quote_count=33, bookmark_count=1001

[tweet 53]
id: 2040211879621214255
author: Peter Yang (@petergyang)
author_bio: I share extremely practical AI tutorials and interviews | Join 140K+ readers at https://t.co/XYKTmGVH14 | Product at Roblox
time: 2026-04-03T23:36:32.000Z
quoted: Peter Yang (@petergyang)
  Nooooo https://t.co/dFth8C6sT7
text: Anthropic just sent an email saying that you can no longer run 3rd party harnesses like OpenClaw using Claude subscriptions.
  
  Right now, both OpenAI and Anthropic are losing money on power users who run multiple agents 24/7 using their $100-200 subscription plans.
  
  This reminds me of when Uber and Lyft were subsidizing rides to win market share. After both companies went public in 2019, ride prices nearly doubled over the next few years. And it took Uber 14 years from its founding before the company posted its first profitable year in 2024.
  
  Both OpenAI and Anthropic are likely to go public soon. Once this happens, their margins will be public as well and there will be a lot of scrutiny on the money-losing all-you-can-eat subscriptions.
  
  So I think there's a good chance that these subscriptions will either get more expensive or more limited after both companies go public.
  
  The counter-argument is that both companies might keep prices low as long as there's still heavy competition and that compute costs will drop as well.
  
  But yeah, overall I don't think the unlimited buffet will last forever.
  
  Running local models on Mac Minis and Mac Studios is looking more appealing now as a safety net.
metrics: like_count=354, retweet_count=26, reply_count=93, quote_count=9, bookmark_count=106

[tweet 54]
id: 2040211603875074512
author: Zara Zhang (@zarazhangrui)
author_bio: Builder. Dangerously skips permissions. Harvard’17. GitHub: https://t.co/KCuEajezlL YouTube: https://t.co/8xzbGWtf6w
time: 2026-04-03T23:35:26.000Z
text: New trend I'm seeing: people distilling colleagues, influencers, and even their exes into agent skills
metrics: like_count=158, retweet_count=9, reply_count=38, quote_count=12, bookmark_count=65

[tweet 55]
id: 2040210782357438956
author: GREG ISENBERG (@gregisenberg)
author_bio: I drop startup ideas daily. Host @startupideaspod. CEO: @latecheckoutplz we build companies like @ideabrowser, @meetLCA, @boringmarketer etc
time: 2026-04-03T23:32:10.000Z
quoted: TBPN (@tbpn)
  .@davidsenra says Shopify CEO @tobi told him we're going to look back at 2026 as "the year that every single business in the world was up for grabs."
  
  "That AI is coming for everything."
  
  "And you're going to look back and realize that this is the year it should have been obvious that you could rebuild the AI-native version of whatever exists out there."
  
  From his appearance on the show last month.
text: this is today’s reminder that every single business in the world is still up for grabs
  
  it’s an incredible time to be building AI native companies  
  
  happy building https://t.co/ZnTO3rEqmA
metrics: like_count=345, retweet_count=24, reply_count=30, quote_count=3, bookmark_count=224

[tweet 56]
id: 2040209434019082522
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world @openclaw🦞
time: 2026-04-03T23:26:48.000Z
quoted: mvpr (@marinatedvapor)
  @bigben7182000 @steipete https://t.co/UOmgIM7O1y
text: woke up and my mentions are full of these
  
  Both me and @davemorin tried to talk sense into Anthropic, best we managed was delaying this for a week.
  
  Funny how timings match up, first they copy some popular features into their closed harness, then they lock out open source. https://t.co/Mgmv6YmW2B
metrics: like_count=4955, retweet_count=420, reply_count=488, quote_count=171, bookmark_count=756

[tweet 57]
id: 2040209263025611105
author: swyx (@swyx)
author_bio: achieve ambition with intentionality, intensity, integrity & insanity.  affiliations: - @dxtipshq  - @cognition - @temporalio - @aidotengineer - @latentspacepod
time: 2026-04-03T23:26:08.000Z
text: this is why nobody takes ai twitter seriously https://t.co/MpTIo5aa6G
media: photo: https://pbs.twimg.com/media/HFBHgypacAA_e70.jpg
metrics: like_count=268, retweet_count=3, reply_count=26, quote_count=5, bookmark_count=18

[tweet 58]
id: 2040207556262723926
author: Justine Moore (@venturetwins)
author_bio: Partner @a16z AI 🤖 and twin to @omooretweets | Investor in @elevenlabs, @bfl_ml, @hedra_labs, @krea_ai, @MireloAI, @ShizukuAILabs, @wabi, @WaveFormsAI
time: 2026-04-03T23:19:21.000Z
text: The new Grok Imagine model is particularly good when you use the LLM to help write or refine prompts ✨
  
  I often start with something simple, take the output to Chat, and ask for help iterating on an edit or enhancement.
  
  You end up with something much more detailed! https://t.co/184FKsgFFV
media: video: https://video.twimg.com/amplify_video/2040207484460367873/vid/avc1/1920x1222/q0UJuOhVibqWW8A7.mp4 | duration: 24s
metrics: like_count=509, retweet_count=72, reply_count=86, quote_count=24, bookmark_count=331

[tweet 59]
id: 2040206778751750255
author: Nan Yu (@thenanyu)
author_bio: head of product @linear
time: 2026-04-03T23:16:15.000Z
quoted: Nicolas Cramer (@cramer)
  @thenanyu what poor incentives have you seen—no check on the impulse to design for other designers?
replied_to: Nan Yu (@thenanyu)
  Yes. PMM is a product concern. 
  
  I see a lot of orgs out there combining design and product management, which I think creates all sorts of poor incentives.
  
  But product management and product marketing are a much more natural fit together. https://t.co/c5z6RpznxD
text: https://t.co/RM41VPpSP5
  
  When design and product are jammed together, then the former ends up reporting into the latter.  
  
  Explorations get shallow and aesthetics &amp; brand suffer. It’s generally better to have brand and product design sit close.
metrics: like_count=24, retweet_count=0, reply_count=0, quote_count=1, bookmark_count=5

[tweet 60]
id: 2040206444428189755
author: Boris Cherny (@bcherny)
author_bio: Claude Code @anthropicai
time: 2026-04-03T23:14:56.000Z
replied_to: Boris Cherny (@bcherny)
  Subscribers get a one-time credit equal to your monthly plan cost. If you need more, you can now buy discounted usage bundles. To request a full refund, look for a link in your email tomorrow. https://t.co/yFiu67vvcY
text: We want to be intentional in managing our growth to continue to serve our customers sustainably long-term. This change is a step toward that.
metrics: like_count=918, retweet_count=14, reply_count=108, quote_count=6, bookmark_count=36

[tweet 61]
id: 2040206443094446558
author: Boris Cherny (@bcherny)
author_bio: Claude Code @anthropicai
time: 2026-04-03T23:14:55.000Z
replied_to: Boris Cherny (@bcherny)
  We’ve been working hard to meet the increase in demand for Claude, and our subscriptions weren't built for the usage patterns of these third-party tools. Capacity is a resource we manage thoughtfully and we are prioritizing our customers using our products and API.
text: Subscribers get a one-time credit equal to your monthly plan cost. If you need more, you can now buy discounted usage bundles. To request a full refund, look for a link in your email tomorrow. https://t.co/yFiu67vvcY
link: https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account (Logging in to your Claude account | Claude Help Center)
metrics: like_count=1450, retweet_count=70, reply_count=219, quote_count=76, bookmark_count=1014

[tweet 62]
id: 2040206441756471399
author: Boris Cherny (@bcherny)
author_bio: Claude Code @anthropicai
time: 2026-04-03T23:14:55.000Z
replied_to: Boris Cherny (@bcherny)
  Starting tomorrow at 12pm PT, Claude subscriptions will no longer cover usage on third-party tools like OpenClaw.
  
  You can still use these tools with your Claude login via extra usage bundles (now available at a discount), or with a Claude API key.
text: We’ve been working hard to meet the increase in demand for Claude, and our subscriptions weren't built for the usage patterns of these third-party tools. Capacity is a resource we manage thoughtfully and we are prioritizing our customers using our products and API.
metrics: like_count=1709, retweet_count=34, reply_count=91, quote_count=30, bookmark_count=67

[tweet 63]
id: 2040206440556826908
author: Boris Cherny (@bcherny)
author_bio: Claude Code @anthropicai
time: 2026-04-03T23:14:55.000Z
text: Starting tomorrow at 12pm PT, Claude subscriptions will no longer cover usage on third-party tools like OpenClaw.
  
  You can still use these tools with your Claude login via extra usage bundles (now available at a discount), or with a Claude API key.
metrics: like_count=8126, retweet_count=653, reply_count=1707, quote_count=1357, bookmark_count=2360