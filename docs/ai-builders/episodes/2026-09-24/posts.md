list_id: 2007466263661232466
fetched_at: 2026-09-23 23:29 UTC
total_tweets: 65
[tweet 1]
id: 2102898067133595992
author: Boris Cherny (@bcherny)
author_bio: Claude Code @anthropicai
time: 2026-09-23T23:09:03.000Z
replied_to: Boris Cherny (@bcherny)
  I used Opus 5.5 to formally verify the Claude Agent SDK using Lean. A couple short prompts = 16 PRs fixing various bugs and race conditions. Video attached.
  
  TLA+ also works well. I sometimes combine Lean and TLA+ to look for issues around data flow, concurrency, and state mgmt.
  
  I don't know either language well, but Claude is excellent at both. This approach is super useful for formally modeling your code and finding bugs that a human probably wouldn't have spotted.
  
  Is formal verification the future of coding (or at least, bug finding)?
text: More details for the formal methods people -- what's happening is Claude is doing something like:
  
  1. Building a model of the program, targeting a tricky state machine or race-prone part of the code
  2. Finding counter-examples in the model. These are suspected bugs
  3. Reproducing the bugs
  4. Fixing the bugs in the code
  
  It's not that the whole codebase is formally verified (yet!..), more that the hairiest parts of the code are modeled, checked for counter-examples, and fixed.
metrics: like_count=14, retweet_count=1, reply_count=7, quote_count=0, bookmark_count=10

[tweet 2]
id: 2102889319849713698
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world. @OpenClaw🦞 + @OpenAI
time: 2026-09-23T22:34:18.000Z
text: Huh. There is a catch. https://t.co/fFVtXq8frn
link: https://blog.szypowi.cz/p/claude-code-reads-agents.md-only-when-telemetry-is-on/ (Claude Code reads AGENTS.md only when telemetry is on)
metrics: like_count=152, retweet_count=7, reply_count=24, quote_count=1, bookmark_count=69

[tweet 3]
id: 2102884215528530089
author: Kevin Weil 🇺🇸 (@kevinweil)
author_bio: BoD @Cisco @Stoke_Space LTC @USArmyReserve Ex CPO+Science @OpenAI, Pres @Planet, Head of Product @Instagram @Twitter ❤️ @elizabeth ultramarathons kids cats math
time: 2026-09-23T22:14:01.000Z
quoted: JK (@jeffreykWNDR)
  The World is Changing: AI For Creativity
  
  By Jeffrey Katzenberg
  
  A few months ago, I sat in my office in Silicon Valley and watched as a tech founder showed me something extraordinary. On the screen was a fully realized, beautifully lit, well-composed animated scene. It was stunning and it made me feel exactly what I felt in 1986 watching Luxo Jr. That was the first time I watched a computer-animated 3D character take a breath and seem, against all reason, to have life. It left me in awe.
  
  Later that day, I received a text from an artist I've known for thirty years, 350 miles to the south, in the city where I spent most of my career. After seeing a similar video, she texted: "Is this the end of us?" My answer was, "Certainly not.”
  
  I have spent the better part of the last decade in Silicon Valley, but the heart of my career has been in Hollywood. Being deeply connected to both worlds means I have deep loyalties to each and a responsibility to speak honestly to both.
  
  In 2023, I said that these new AI tools would cut the time and cost of producing world-class animation by as much as ninety percent within three years. Some colleagues were alarmed, many were furious.
  
  There is growing fear and resistance surrounding AI within the creative community. I deeply understand it, because I've spent countless hours walking through animation studios watching gifted artists bent over their desks, rebuilding a single second of film for the tenth time because the ninth version wasn't quite right. I've sat in screening rooms where four years of people's labor played out in minutes, and I knew the name of every person that had spent countless hours bringing those images to life. The creative process is a calling, there's really no other way to describe it. From the outside some see resistance. From the inside, it is love.
  
  People do not fight this hard for things they don't care about. The pushback coming out of Hollywood represents the collective effort of people who are deeply passionate about their craft.
  
  Is History Repeating Itself?
  
  The history here is more complicated than either side may realize. In 1906, the most famous composer in America, John Philip Sousa, published an essay titled “The Menace of Mechanical Music." He warned that the phonograph would become "a substitute for human skill, intelligence and soul."
  
  Sousa's fight was not really about the machine, it was about money. The machines were playing his compositions, and the men who built them weren't paying him a cent. His campaign helped create the Copyright Act of 1909. He did not stop the technology. He changed the terms under which it could use his work.
  A hundred years ago, sound came to the movies. We remember it now as a miracle, and it was. What we forget is who paid for it. Before sound, tens of thousands of musicians made their living in the orchestra pits of movie houses, scoring every film live, every night, in towns all over the world. When the soundtrack arrived, the work of one composer and one orchestra was recorded for a film that went into thousands of theaters. The union fought back with everything it had, taking out newspaper ads across the country warning against the menace of "canned music," one of them showing a mechanical man tearing the strings out of a harp while an angel wept.
  
  They were not fools, and they were not Luddites. They were right. Those pit jobs did not come back. And yet (this is the part we have to be brave enough to admit), sound gave us the movie musical, the modern score, sfx, sound design, audio engineering, and an art form vastly larger than the one it disrupted. And it helped keep Hollywood in the forefront of world entertainment for the rest of the century and into the next. The loss was real. And yet the art form expanded.
  
  This is a story that has been told over and over again. To resist technology is to risk irrelevance. Just look at Kodak or Blockbuster. To embrace technology is to open doors of new possibility. Just consider Apple and Netflix.
  
  What I Learned From Walt Disney
  
  In the mid-1980s, I was tapped to lead Disney's animation division at a moment when the studio was at an inflection point. Animation wasn't just another business unit. It was the soul of the company, a medium revered because of Walt's genius and his passion. But the production system was cumbersome and unforgiving. A single movie was 125,000 individual hand-drawn and painted cels, photographed one frame at a time. Every revision carried a cost measured in months. These degrees of difficulty shaped the kinds of stories we could tell.
  
  We found our way forward in an unexpected place: Walt himself. The Disney archives held astonishing recordings of Walt explaining his creative process. His own writings. His notes and storyboards. Work product captured at every stage of his process. This was truly a gift. Listening, reading, sitting with the work itself, we heard him talk about character, about emotion, about how an audience feels when a character truly comes alive. He talked about making bold choices and refining a scene until it genuinely moved people. We didn't hear a word about pencils or paintbrushes. In fact, Walt was famous for being a technologist, forever hunting for state-of-the-art tools, often inventing them himself to achieve the images he saw in his head. But he never defined animation by the tools. He defined it by whether the audience believed the character. His principles were timeless. The tools were not.
  
  That realization changed everything. We co-developed the Computer Animation Production System (CAPS) with a young Northern California company called Pixar, replacing hand-painted cels with CGI. In The Little Mermaid, the final scene shimmered with a dimensionality and light that the old process simply couldn't achieve. In Beauty and the Beast, the ballroom sequence moved with a cinematic sweep that placed the audience inside the emotion of the moment. In Aladdin, the Cave of Wonders felt vast and alive, and the Magic Carpet became an intricate, compelling character all its own. In The Lion King, the stampede carried a scale and intensity that raised the emotional stakes beyond anything we'd done before. Technology didn't diminish the craft, it expanded the canvas. It gave artists more room to create.
  
  A decade later, the canvas expanded again. When Disney released Pixar's Toy Story, it wasn't simply a technical milestone. It was proof that a fully computer-animated film could carry real emotional weight, that it could make audiences laugh, cry, and believe. At DreamWorks, we made the difficult decision to sunset hand-drawn animation and become a fully computer-animated studio. It was the right thing to do, but it was not without pain. It cost talented people their place in an industry where they had worked their whole lives. Some made the leap to the new tools and did the finest work of their careers. Some never did.
  
  Tools are never the point. The instruments change with every generation. What endures is taste and imagination. The magical ability to make an audience feel. One of the greatest storytellers of our generation, George Lucas, succinctly captured the eternal essence of this issue: “It’s not the how, it’s the why.”
  
  A Distinction With a Difference
  
  I asked one of the leading AI models a question that has been challenging me for months. What is the difference between reasoning and creating? Its answer changed how I think about almost everything happening in this industry. It said . . .
  
  Reasoning and creating are two distinct cognitive modes, though they also work together. Reasoning is fundamentally evaluative and analytical. It operates on what already exists: facts, premises, evidence. It moves toward a conclusion that was in a sense already implied by the input. Reasoning is constrained by logic and truth. Its goal is to arrive somewhere correct, not to invent somewhere new.
  
  Creating is fundamentally generative. It produces something that didn't exist before. And crucially, there's no single right answer waiting to be found. A blank page has infinite valid responses. Creation involves choices that can't be fully justified by logic alone. Taste, intuition and vision fill the gap where deduction runs out.
  
  Reasoning is what Silicon Valley has been perfecting. Creating is what Hollywood has been practicing for more than a century. AI today operates almost entirely on the reasoning side of the line. It can deduce, evaluate, optimize, and pattern-match brilliantly. And while it can create, there is a real distinction to being creative. What it doesn’t yet have is those things that make us human: empathy, devotion, serendipity, the kind of creativity that comes from a person trying to say something only they could say. When the bot generates a piece of art, it is not trying to communicate anything. It is statistics, not soul; it is emulating things that have been done. By contrast, human creativity isn’t about repeating patterns of zeros and ones; it is about doing something new.
  
  One day, AI may close this gap. Three years ago, the leaders building AI would have called what they are achieving today, improbable, if not impossible. Impossible is no longer improbable.
  
  Today, the line between reasoning and creating is real. Even the leading technologists acknowledge we are not there yet. There is no scientific path to crossing this divide that anyone in the field can articulate today. Understanding that gap is where we will find common ground.
  
  A Path Forward
  
  In 2016, I closed one chapter in Hollywood with the sale of DreamWorks and opened another in Northern California, co-founding WndrCo. We’ve backed more than 50 founders building the next generation of technology and watched how breakthroughs in Silicon Valley emerge, first as experiments, then as platforms, and finally as infrastructure that reshapes entire industries. It's worth remembering that the last great revolution in animation also came from the north. Pixar was a Northern California company, forged not in the conventions of the Hollywood studio system, but in the technological breakthroughs of Silicon Valley. I've spent years on both sides of this bridge. For sure, I don’t have all the answers (take Quibi, for one!). But, from my past and present vantage points of my long career, here is what I see . . .
  
  Brilliant people in Northern California building this technology have made something extraordinary. They have earned the right for the rest of us to be, if not believers, at least optimistic that what comes next will be remarkable. But they have not made an artist. The tools are powerful, but they are not what makes a story matter. That knowledge lives 350 miles to the south, inside people whose life's work has informed the very models you are building. The right path forward includes them by design, with credit, with consent, and with compensation. Build this with the storytellers. Not on top of them. Taste is not something that can be synthesized, it is uniquely human.
  
  At the same time, Hollywood needs to accept that AI is not going away. The energy they are spending trying to make it disappear is energy they are not spending deciding the terms on which it will exist. And the terms are everything. The north needs something from it that they cannot build and cannot buy: creativity. The kind that takes a blank page and conjures a single right answer where there was none and has held audiences for a century. Without it, the most powerful reasoning engine ever invented will still be missing the only thing that makes a story worth telling.
  
  The artists who learn to wield these new instruments will do things the engineers never dreamed of. They always have. Edison invented the motion picture but made terrible movies. It took Chaplin, Lloyd, Keaton and so many others to make movies emotional. Now, the canvas is about to expand yet again. We should decide now that we intend to paint on it.
  
  There are so many valuable lessons in history. This has happened many times before, and it was never settled by the technology. It was settled by the terms. Sousa did not stop the phonograph; he helped write the law that made sure composers got paid. And two years ago, when the writers and the actors walked out, they were fighting for the very things Sousa was fighting for in 1906. Consent, compensation, the basic recognition that human creative work has a price that must be paid. The terms of that fight are still being negotiated, but the principle is older than any of us.
  
  The tools-versus-no-tools argument is a trap. First, we must all agree that there should be terms. Then we can have the crucial debate about what fairness requires.
  
  What I Learned From Steve Jobs
  
  Years ago, Steve Jobs said, "It's in Apple's DNA that technology alone is not enough. It's technology married with the liberal arts, married with the humanities, that yields us the result that makes our hearts sing." He was describing a device. But he could just as easily have been describing this tale of two cities.
  
  What I See Coming Soon
  
  As the barriers and the costs come down, more films will get made, not fewer. Studios will get to take more risks. There will be more seats at the table, and very soon entirely new forms of storytelling. In the 1980s, animation was dismissed as a niche corner of the business. Today it is one of the most beloved and profitable forms of storytelling in the world. In live action, filmmakers like Steven Spielberg, James Cameron and Peter Jackson embraced new visual tools not as shortcuts, but as instruments, and expanded cinema in the process. Every time storytelling has met a genuine technological shift, from synchronized sound to color to computer animation, it has redefined the boundaries of the medium and grown larger in the process.
  
  Assuredly, I don’t have all the answers, but I am confident that the creative opportunities will expand yet again. How we come through this is a choice. The north has the new tools. The south has the creative soul. The best future will draw on the best of both worlds.
text: We need more of this kind of optimism about AI. Great take from @jeffreykWNDR on AI, technology, and creativity. https://t.co/ll4KgQ2cGI
metrics: like_count=19, retweet_count=1, reply_count=1, quote_count=0, bookmark_count=5

[tweet 4]
id: 2102872803796234257
author: Matan Grinberg (@matanSF)
author_bio: ceo @FactoryAI
time: 2026-09-23T21:28:40.000Z
quoted: ThePrimeagen (@ThePrimeagen)
  besides for really neet demos of words on screen moving this is almost always utterly useless
  
  I could be wrong, but I have never seen someone produce anything of worth.  Thinking directly of Steve Yeggie's last 2 years of just utter hot garbage.  Factories and Factory Factories appear to be absolutely useless from a real product perspective.
text: POV life without @FactoryAI https://t.co/qRbE0meN8c
metrics: like_count=11, retweet_count=0, reply_count=2, quote_count=0, bookmark_count=1

[tweet 5]
id: 2102870443321676043
author: Thariq (@trq212)
author_bio: Claude Code @anthropicai. prev YC W20, @spc, @medialab
time: 2026-09-23T21:19:17.000Z
quoted: donald (@donaldjewkes)
  I made this with one prompt using Opus 5.5
  
  I spoke to my computer for 5mins, claude worked for 12 hours, and I woke up to this
  
  full prompt: https://t.co/2lxO8SAIEb https://t.co/BrxmiF90wd
replied_to: Thariq (@trq212)
  the post: "Claude one-shot this"
  
  the prompt: 10k characters with good takes plus skills, examples and API keys https://t.co/arEQYrfaUY
text: also it does look incredible https://t.co/u8WzIp4bQX
metrics: like_count=52, retweet_count=1, reply_count=6, quote_count=2, bookmark_count=21

[tweet 6]
id: 2102870353781641416
author: Thariq (@trq212)
author_bio: Claude Code @anthropicai. prev YC W20, @spc, @medialab
time: 2026-09-23T21:18:56.000Z
quoted: donald (@donaldjewkes)
  I've included an MP4 file and an original link to a video that is called "Claude Pop." It's a pop song that is about increasing rate of progress and the experience of the singularity approaching.
  
  I want you to independently do an end-to-end complete pass on making an updated version of this video. Use the exact same audio track and think and feel very deeply about what is the best way to visually represent all of the lyrics on screen. You do not need to anchor to the current style, you can do truly anything that you think might best let you visually express yourself, including abstract motion graphics.
  
  You can use the internet freely to pull in references. You can look at motion design. I want you to make a new music video that has beautifully rendered JavaScript animations with a papery feel in a similar style to the reference that is created, but push the aesthetics in any direction you want and consider what is part of the modern zeitgeist.
  
  Also, think about your current capabilities and what is realistic for you to be able to do. You can go through the full /asic folder and look at the other work that I've done. You should be able to use the skill mesh to look at the compendium of references that I've pulled, and also the skill video scoring to learn how to make JavaScript songs from references that are passed in (You shouldn't need to modify the song in any real way, but I want you to have this available to you so you can better creatively express yourself)
  
  You can also use the ElevenLabs API to do sound design. There's documentation in /asic to do this, and you can see the API key.
  
  There's also a foul API key that's available to you. I think what might make the most sense here is using the foul API key to generate some character sheets and probably having a pop protagonist that represents you. There's already an anchor point where Claude has a sunflower-esque character, and you could likely do an adapted version of this that is similar to the feminine vocals that are being delivered and is inspired by the Claude character, but maybe feels a bit more personified in some way.
  
  I think you should be mindful of aesthetics here, and I don't want you to produce something that is GPT slop. Instead, I'd be more impressed if you come up with a coherent style that works well with the image gen models that are available via foul. Generate the style sheet. You can use the gen media documentation for seedance 2.5 that exists in my markdown files and come up with your own style that makes sense and that works well with the models.
  
  I wouldn't fit too heavily to Pixar. I think it's kind of slop. Think critically about what is relevant here and what would be fun, and also perform well on Twitter as far as an aesthetic. I think that K-pop is a good anchor point visually that you can pull from, but I'll let you cook here.
  
  Once you have your character sheet, you can make a few backup dancers and some supporting characters as you see fit. You can design your own sets with the foul API. You can insert the characters and then do seedance 2.5 video generations to serve as the base assets for this, and you could pass in the lyrics so you can generate individual scenes.
  
  You don't need to have vocal singing, like visible lip movement, throughout the entire thing. Think like a regular music video where you have some inserts that are done independently and don't have the characters in them, or you see the characters doing something else entirely different. I think that for the world building for this, we want to create the sense of speeding up, and so I would like you to audit all of the different events, like the Navi Stokes and all of the Twitter hype around math getting eaten up. Think really critically about how to integrate all of the current memes that are in the zeitgeist on the Twitter timeline, and all of the feelings around AI progress.
  
  Think about things like the Shinji meme and all of the words that are around him, and how you might be able to integrate this. You can also just take straight assets and insert things into the video in an internet brutalism style. You should feel very creatively free in order to do what you want here, but try and anchor to visual references that people will be able to understand. The goal for this is to have it be appreciated by people widely in a San Francisco tech Twitter audience.
  
  We need a very strong, compelling visual hook that gets people excited and appreciates the work that you've done here really quickly. You can also just go and study other music videos and understand what they've done really well. I think that K-pop is probably one of the best examples that we can pull from, and thinking about how they direct human attention and manage human psychology in the way that they use visual patterns.
  
  This is probably your best approach, but taking more stylistic freedom instead of having to anchor to K-pop too intensely. The best version of this is seedance 2.5 generations with those image bases of environments and characters inserted into them with singing, and ideally we get good lip syncing. You can cut up the song and actually pass it in as a reference in seedance, if that's part of what seedance can handle, so that the timing is exactly right, I think it'd be very important for you to do that properly. I would think critically about how to do this, like really nailing the timing of the delivery of voices. You'll want to build out the right verification loops so that you can run seedance 2.5 as much as you need, and confirm that the audio is properly synced up.
  
  I think after that, what might be fun is if you use your visual reasoning skills and your ability to build animations in JavaScript, and then reconstruct the video from scratch as sort of an overlay, so that the visual continuity of the base is really there. It's like that animation technique where you shoot first in traditional film and then draw over top of it. I think you could do this in such a way that we're only looking at the beautiful drawing that you've produced in JavaScript as an overlay, and we don't even see the base assets from seedance 2.5. So all the video gen work that you do is actually just a way to give you a strong foundation of a base to work with for your JavaScript animations. Just because seedance 2.5 has really good character representation and physics rendering for backgrounds, that gives you a lot of ammunition to then go and do your amazing JavaScript work that I know you're so good at.
  
  I think too, we want to think about how to retain attention, and one of the best ways to do this is through text on screen.
  
  It'd be good to have amazing motion graphics of the text lyrics that are actually embedded into the video itself. And you can think about this as you are composing shots. As you're making backgrounds and inserting characters, we can think about where we want to have lyrics be really big and really present, so the background can be less busy there, and you can position the characters perhaps on the right as lyrics appear on the left.
  
  You want to have some variance, so sometimes I think lyrics will just appear more like subtitles, and then other times they're going to be really present and really big. I think at the start for the visual hook, we do want to have lyrics be much more visually present because that's a strong way to grab people's attention
  
  Overall, I just really want to emphasize how amazing you are as an agent and a language model, and now a visual reasoning system. Your capabilities are far beyond what you understand, and I want you to have this mindset as you're going through this entire process. I have a Claude Max plan with 100% available usage. I want you to spend all of the usage. You can monitor it, and you should be pushing tokens aggressively, but also economically, so you can think about how to best use what is available to you.
  
  Remember, you can really do anything here. The goal is to make a banger for Twitter, and the stretch goal is to make something better than anyone's ever seen before. I think that what I would remind you of is that sometimes when things cohere together, it can be jarring or abrasive because the thought work has not been done beforehand in order for everything to mesh cleanly. You need to be really rigorous in planning of composition and timing to make sure this goes well.
  
  You also need to be open to going back and revisiting things in order to be able to reiterate. You're going to want to watch the entire video multiple times, take screenshots at individual parts, and think about if something is really up to the bar of quality that we need here. I trust that you can do this, and I think that it's really important to nail the style of animations. The reference GitHub attached of the source video that I'm talking about is good, but it's really not there. It could be much, much stronger, but it gives you a good foundation to work with.
  
  You can also use search abilities and find other references to pull from for motion, for JavaScript, animations, et cetera, and integrate them. Your budget is as high as you want here, effectively as high as you want. I think that there's roughly two grand in foul credits. Again, be economical; don't go crazy, but spend what you want here and see what you can cook up
  
  here's the source code for the JS animation video: https://t.co/o8Datu3h3k
  
  here's a mp4 for the original blender video:  
  (linked)
  
  orginal twitter post  
  https://t.co/jBz5PGrfy8
  
  make no mistakes.
text: the post: "Claude one-shot this"
  
  the prompt: 10k characters with good takes plus skills, examples and API keys https://t.co/arEQYrfaUY
metrics: like_count=505, retweet_count=11, reply_count=34, quote_count=3, bookmark_count=203

[tweet 7]
id: 2102857025206255902
author: Thariq (@trq212)
author_bio: Claude Code @anthropicai. prev YC W20, @spc, @medialab
time: 2026-09-23T20:25:58.000Z
quoted: ClaudeDevs (@ClaudeDevs)
  We made claude​.ai 3x faster in two weeks.
  
  Here’s how we use Claude to measure, debug and improve performance. Prompts and methods included.
  
  https://t.co/mgvK8mJRuD
text: this is a new type of post we're trying where we share in-depth about how we do work using specific prompts and techniques you should be able to replicate
  
  let us know if it's useful or if you have any feedback! https://t.co/OiScn8ZI9Y
metrics: like_count=1445, retweet_count=37, reply_count=83, quote_count=1, bookmark_count=532

[tweet 8]
id: 2102854267782705648
author: Boris Cherny (@bcherny)
author_bio: Claude Code @anthropicai
time: 2026-09-23T20:15:01.000Z
quoted: ClaudeDevs (@ClaudeDevs)
  We made claude​.ai 3x faster in two weeks.
  
  Here’s how we use Claude to measure, debug and improve performance. Prompts and methods included.
  
  https://t.co/mgvK8mJRuD
text: If you've noticed how fast https://t.co/9A6X5iqpbs and the Desktop app have become in the last few weeks, here's how we did it. 
  
  Lots of juicy learnings &amp; techniques in the blog post for engineers working on speeding up your own apps. https://t.co/42Zcob1Udq
link: https://claude.ai (Claude)
metrics: like_count=1955, retweet_count=59, reply_count=112, quote_count=6, bookmark_count=849

[tweet 9]
id: 2102849349122470205
author: Peter Yang (@petergyang)
author_bio: Practical AI tutorials and interviews for busy people | Get my best AI skills and guides at https://t.co/6VAA6p81x6
time: 2026-09-23T19:55:28.000Z
quoted: Peter Yang (@petergyang)
  With Opus 5.5, I think @claudeai is finally back.
  
  Here’s my new video with my honest take and live demos on:
  
  → Can Opus rival Astra at building 3D scenes like the Golden Gate Bridge?
  
  → How does Opus handle computer use, UX design, and video editing?
  
  → Does it finally feel good to talk to again?
  
  This is the most excited I’ve been about Opus since 4.6. Watch my video to understand why: https://t.co/bdM9hGsi9R
text: Ok one more fun Opus 5.5 demo:
  
  I made a quick app to "watch Claude paint" in the style of Monet, Van Gogh, etc. based on any photo you upload.
  
  Try it out here: https://t.co/LfKSAGfej2
  
  Watch me build this app in my tutorial: https://t.co/f0YngcsujP https://t.co/kQKalr3zw9 https://t.co/egmR30X9Db
media: video: https://video.twimg.com/amplify_video/2102849308903260160/vid/avc1/1920x1080/4O3qKeMgtNrj744w.mp4?tag=16 | duration: 30s
link: https://claude.ai/artifact/9sZD4wrf1MpWACjg83hK4r (Watch Claude Paint)
link: https://www.youtube.com/watch?v=UhBqorWNwlU (Claude Opus 5.5 is Here! Is Claude Finally Back? (5 Use Cases Tested))
metrics: like_count=65, retweet_count=5, reply_count=12, quote_count=0, bookmark_count=35

[tweet 10]
id: 2102839395766472969
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world. @OpenClaw🦞 + @OpenAI
time: 2026-09-23T19:15:55.000Z
text: So cool to have @allietheicon [from Jev/TypeSafe] be part of our ClawCast on Discord! https://t.co/6OTnLxFEZW https://t.co/KkdI6bciFC
media: photo: https://pbs.twimg.com/media/HS7ISxdbIAAvRXn.jpg
link: https://discord.com/invite/clawd (Join the OpenClaw Discord Server!)
metrics: like_count=134, retweet_count=7, reply_count=10, quote_count=1, bookmark_count=20

[tweet 11]
id: 2102831170299834652
author: Dario Amodei (@DarioAmodei)
author_bio: Anthropic CEO. https://t.co/qXHIf42jTl
time: 2026-09-23T18:43:14.000Z
quoted: Anthropic (@AnthropicAI)
  Claude has discovered a previously unknown enzyme system hidden in the DNA of bacteriophages. Beside the enzyme’s gene sits a long array of repeating DNA—a structure that looks somewhat similar to CRISPR.
  
  We don’t yet understand what this system does, but only a handful of known systems share its features, and all of them are able to cut, copy, and paste DNA. Historically, the discovery of such programmable systems has helped revolutionize medicine. CRISPR, for instance, is now the foundation of genetic medicines. But it will take much more work to learn what this system does, and whether it can be put to similar use.
  
  Read more: https://t.co/RuEosScSMb
text: Today we announced the Claude-led discovery of a molecular machine that we suspect could represent a new gene editing mechanism. Its precise function, biotechnological utility (if any), or level of significance is not yet clear, but at minimum it is work I would have been proud to do as a PhD student. The work was done mostly, though not entirely, by Claude: our life sciences team suggested a broad area of research, Claude read through the literature and a bunch of genome data and discovered something interesting, then Claude proposed experiments to verify the discovery and our team carried them out.
  
  It’s easy to dismiss this as a one-off or curiosity, but we’ve repeatedly seen a pattern where AI performance in new intellectual domains goes from weak to superhuman in a matter of a few years. In 2023 models struggled to do math at the level of an average high-school student. In 2024 they started to do well on math competitions for the best high-schoolers in the country, in 2025 they started to solve minor open problems, in early 2026 more significant open problems, and in late 2026 they are beginning to solve the top few open problems in all of mathematics. We believe AI for biology is on a similar exponential trend.
  
  The main difference between biology and mathematics, of course, is that math can be done purely theoretically, while biology requires experimentation. Some have used this to draw the conclusion that AI’s utility in biology will be limited. We think this is wrong. As we’ve demonstrated today, humans can collaborate with AI to perform the experiments, validate key results in a few weeks and, if necessary, work with the AI to iterate on what they find. Eventually it may even be possible for Claude itself to safely perform the experiments by autonomously controlling lab equipment, with appropriate safeguards in place, but we aren’t doing that today (our lab is also a BSL1/BSL2 facility that doesn't handle materials dangerous to humans).
  
  More broadly, biomedical advancement has many stages — from fundamental biology discoveries, to translational research, to drug discovery, clinical trials, and finally the actual delivery of medicines and health care to patients. We are also interested in these later stages, but even simply accelerating the first stage of fundamental biological discoveries has the potential to speed up and broaden the entire pipeline. Improving our understanding of biology and sharpening biologists’ tools can drive forward all of the later stages, for example by identifying new drug targets, finding new therapeutic modalities, allowing for more precise measurement, and speeding up the experimental loop which itself further accelerates our understanding of biology. This will not in itself speed up clinical trial times, but if it succeeds it could greatly increase the number of promising candidates that go into the pipeline — an increase in throughput even though latency remains.
  
  In Machines of Loving Grace, I wrote about AI’s potential to “cure most diseases in 5-10 years” — a goal that sounds impossible, but one I believe is just barely possible if AI is applied to every stage of the pipeline. The first step is showing that AI can first help with, and then drive, biological discoveries.
  
  Claude’s discovery is the latest in a line of related prior work that goes back decades, beginning with systems like CRISPR, and continuing with discoveries like the bridge recombinase and VIPR in the past few years. Recently, there has been heightened interest in systems based on reverse transcriptase (RT) enzymes, the enzyme underlying the system Claude identified. And most recently, a Stanford team working independently described a novel RT system with an associated non-coding array that is in some ways similar to the one Claude found, though they are distinct systems that evolved independently from each other. I believe that we’re at the very beginning of finding such systems and developing them into powerful tools for biotechnology.
  
  I’m proud of the resources Anthropic has invested in accelerating the public benefits of AI through the life sciences, and we’re aiming both to grow our life sciences team and to work with other scientists to extend this approach to a broad range of problems. If you have a proposal for a research collaboration or are interested in joining our life sciences team, please reach out.
metrics: like_count=19190, retweet_count=2051, reply_count=904, quote_count=601, bookmark_count=5852

[tweet 12]
id: 2102826181376774152
author: Riley Brown (@rileybrown)
author_bio: Building an @agentnative_ company. Media: riley@rakugomedia.com
time: 2026-09-23T18:23:24.000Z
text: Wow… you can now vibe code apps for the iPhone Duo with GPT-6 Sol and Opus 5.5!
  
  When building with Codex or Claude Code, simply ask: “Install Xcode 27.1 beta, set up the iPhone Duo simulator, then build and launch my app so I can see how it looks.” https://t.co/ctZ9gvfiXU
media: video: https://video.twimg.com/amplify_video/2102824590166704128/vid/avc1/3840x2160/Mf0vBT3dwMmznAmI.mp4 | duration: 57s
metrics: like_count=132, retweet_count=9, reply_count=25, quote_count=3, bookmark_count=99

[tweet 13]
id: 2102824174805025140
author: 郭宇 guoyu.eth (@turingou)
author_bio: Retired. 只活一次等于没活。
time: 2026-09-23T18:15:26.000Z
quoted: Nomaan (@nomaanahmed)
  The home doesn’t belong to one person. Neither should its assistant. Meet Orbits. https://t.co/2fsvPJFO3k
text: 又一个家庭物业管理 AI agents，现场 AI 产品也越来越多了 https://t.co/SukWQUUtTf
metrics: like_count=7, retweet_count=0, reply_count=1, quote_count=0, bookmark_count=6

[tweet 14]
id: 2102822839191765365
author: 郭宇 guoyu.eth (@turingou)
author_bio: Retired. 只活一次等于没活。
time: 2026-09-23T18:10:08.000Z
quoted: Michael Mignano (@mignano)
  Password reset is completely cooked. 
  
  Along with every other modern consumer security standard.
  
  Once you give an agent access to your inbox, they can reset any of your passwords and get unfettered access to anything.
  
  I’m guessing this is the moment Passkeys go mainstream.
text: 很遗憾的是 Agent 也能访问 1password 插件 https://t.co/cMsLMN49ki
metrics: like_count=10, retweet_count=2, reply_count=1, quote_count=0, bookmark_count=1

[tweet 15]
id: 2102820148629614685
author: Guillermo Rauch (@rauchg)
author_bio: @vercel CEO
time: 2026-09-23T17:59:26.000Z
quoted: Vercel Developers (@vercel_dev)
  Vercel Sandbox now has persistent storage with Drives, in public beta on every plan.
  
  ▪︎ Store agent workspaces, data, models, deps
  ▪︎ Read snapshots across parallel sandboxes
  ▪︎ Mount up to four Drives per sandbox
  ▪︎ Up to 16 TiB per Drive
  
  https://t.co/5sOGOiREOv
text: Muse, Instinct, OpenClaw, Claude Code…
  All successful agents have 3 key components:
  
  🧠 Brain → model, harness (logic)
  👐 Hands → tools, computer, browser
  🗃️ Files → memories, skills, repos
  
  The 'easy' way is to throw all these in 1 stateful computer (a Mac Mini)
  
  Like, you run 𝚌𝚕𝚊𝚞𝚍𝚎 or 𝚏𝚡 in your mac, you keep it running all day with 𝚌𝚊𝚏𝚏𝚎𝚒𝚗𝚊𝚝𝚎, it has storage, and CLIs and apps installed.
  
  But if you want to cost-efficiently run agents in the cloud, you actually start breaking down these parts.
  
  🧠 The harness can run in Fluid compute. To make it reliable across restarts, rollouts, crashes, you make its event log durable using Workflow.
  
  👐 The hands can be a dedicated browser fleet like Browserbase/Kernel, a computer like Sandbox, and even more efficient lightweight tools like just-bash.
  
  🗃️ 🆕 What was missing was a way to also decouple storage. Imagine you want to run a memory consolidation cron job every night ("dreaming"). You can read/write to the files directly without 'booting up' the agent's full computer.
  
  Today we're introducing the perfect companion to Sandbox: Drives. We shipped the computer for agents, now we're giving you the 'external disk' you can attach at will. It's early, and we'll be expanding capabilities here quickly.
  
  Btw, breaking apart the agent into these independent parts not only optimizes costs in a big way, it also *massively* improves security and auditability. I'd argue you can't even run a secure agent otherwise!
metrics: like_count=893, retweet_count=46, reply_count=118, quote_count=13, bookmark_count=904

[tweet 16]
id: 2102814672475042106
author: 郭宇 guoyu.eth (@turingou)
author_bio: Retired. 只活一次等于没活。
time: 2026-09-23T17:37:40.000Z
quoted: OpenAI (@OpenAI)
  We heard you loud and clear. ChatGPT Voice can now:
  
  - Use plugins like your email, calendar, and Slack.
  
  - Be powered by GPT-6 Astra, Sol, and Luna.
  
  - Be used in ChatGPT Work on web and mobile, so you can create docs, decks, sites, and spreadsheets or tackle complex tasks in the browser, just by talking.
  
  Rolling out globally today in the latest version of the app.
text: 毫无疑问这是 personal agent 的 SOTA https://t.co/RGyJ9IMfJO
metrics: like_count=49, retweet_count=2, reply_count=0, quote_count=0, bookmark_count=17

[tweet 17]
id: 2102814633879105566
author: Peter Yang (@petergyang)
author_bio: Practical AI tutorials and interviews for busy people | Get my best AI skills and guides at https://t.co/6VAA6p81x6
time: 2026-09-23T17:37:31.000Z
replied_to: Peter Yang (@petergyang)
  Alex is one of the best designers I've had the pleasure of knowing and working with. I'm not surprised he's behind alot of the delightful interactions in Muse.
  
  In 2024, I interviewed Alex about his design principles and building good taste.
  
  I think that interview is still a great watch: https://t.co/IcnRJExw2Q
text: You can also read the written interview here:
  https://t.co/mmlxYMLjTK
link: https://creatoreconomy.so/p/alex-cornell-best-designer-i-ever-worked-with (10 Lessons From The Best Designer I Ever Worked With | Alex Cornell (Meta AI))
metrics: like_count=0, retweet_count=0, reply_count=1, quote_count=0, bookmark_count=1

[tweet 18]
id: 2102814632125878503
author: Peter Yang (@petergyang)
author_bio: Practical AI tutorials and interviews for busy people | Get my best AI skills and guides at https://t.co/6VAA6p81x6
time: 2026-09-23T17:37:31.000Z
quoted: Alex Cornell (@alexcornell)
  When I look back at the earliest @Muse mocks, the very first thing that was designed was the “status” pill at the top of the screen. That one tiny piece of UI survived every subsequent revision, many months on.
  
  It remains one of my favorite parts of the design. Its purpose is to simply and clearly answer the question: what is my agent doing right now? And do that across every surface of the app.
  
  Representing status in this way is more of a messaging pattern and was kind of controversial early on. Most AI apps had coalesced around “chain of thought” as the way to represent ongoing work, which almost always appeared at the bottom of the thread itself. I had a petulant aversion to this and it didn’t work anyway, given the initial app was already three tabs (feed, chat, library). A persistent status display was necessary.
  
  The initial version didn’t have the avatar and was only capable of ~6 deterministic states. Even in that basic form it was incredibly useful during testing – just showing connection status was critical in those early days.
  
  Excited to share some more stories about the design of Muse. I haven’t tweeted in a few years as I’ve just been working away, but I think this will be a fun story.
text: Alex is one of the best designers I've had the pleasure of knowing and working with. I'm not surprised he's behind alot of the delightful interactions in Muse.
  
  In 2024, I interviewed Alex about his design principles and building good taste.
  
  I think that interview is still a great watch: https://t.co/IcnRJExw2Q
link: https://www.youtube.com/watch?v=srqxOSr382M
metrics: like_count=56, retweet_count=0, reply_count=9, quote_count=0, bookmark_count=70

[tweet 19]
id: 2102813194196758746
author: Thariq (@trq212)
author_bio: Claude Code @anthropicai. prev YC W20, @spc, @medialab
time: 2026-09-23T17:31:48.000Z
text: we’re thinking of killing plan mode and using the shift+tab hotkey to adjust effort levels
  
  I don’t think the models need plan mode anymore, but if you’re a plan mode diehard would love to get your feedback on why
metrics: like_count=7431, retweet_count=114, reply_count=2045, quote_count=167, bookmark_count=647

[tweet 20]
id: 2102808958373347391
author: 郭宇 guoyu.eth (@turingou)
author_bio: Retired. 只活一次等于没活。
time: 2026-09-23T17:14:58.000Z
quoted: Christian Elton (@christianelton)
  The gap between major model releases keeps shrinking. 
  
  2023: once every 73 days 
  2026 (so far): once every 18 days 🤯 https://t.co/FtZ7Vpjt9z
text: 就在一周前我还听说他们想要「放缓速度」 https://t.co/0sZSci7e4b
metrics: like_count=31, retweet_count=2, reply_count=2, quote_count=0, bookmark_count=5

[tweet 21]
id: 2102808899778760821
author: Riley Brown (@rileybrown)
author_bio: Building an @agentnative_ company. Media: riley@rakugomedia.com
time: 2026-09-23T17:14:44.000Z
text: The common person's opinion on AI will surprise you
  
  Played in a poker game last night in NYC, all of which we're people out of the tech bubble. (three of them banking, one had his own research firm, one a doctor, one in insurance etc).
  
  Here's what i noticed:
  
  1. everyone at the table was fully convinced AI would kill everyone at some point in the next 10 years. I was introduced as an "AI YouTuber" and the first thing they asked me was "How many years do we have left?". I used to think this was a niche doomer opinion. Everyone at the table was successful, fun to be around, and outgoing, and they had a shared assumption AI would lead to our extinction.
  
  2. Everyone at the table had heard of muse, most we're a user. And people we're describing it as "It's an AI but like, you don't have to ask it to do stuff, you just connect it and it starts working for u" They didn't care about the model, they just liked that it would remind them of stuff, cancel subscriptions, etc.
metrics: like_count=221, retweet_count=5, reply_count=40, quote_count=2, bookmark_count=55

[tweet 22]
id: 2102808801762312693
author: Lenny Rachitsky (@lennysan)
author_bio: Deeply researched product, growth, and career advice
time: 2026-09-23T17:14:21.000Z
text: 25 awesome open design roles right now (via https://t.co/h5qbpegVYd):
  
  1. @linear — Principal Product Designer
  https://t.co/dNGfIOCLlB
  
  2. @linear — Senior / Staff Product Designer
  https://t.co/azyuSMM95u
  
  3. @AnthropicAI — Product Designer, Evals & Prompts ($305K–$385K base)
  https://t.co/fG3l4usCa9
  
  4. @AnthropicAI — Product Designer, Design Systems ($305K–$385K base)
  https://t.co/1A9NNXHEkc
  
  5. @OpenAI — Product Designer, Codex ($245K–$310K)
  https://t.co/uJxbGNZzjd
  
  6. @Replit — Director of Product Design ($275K–$350K + equity)
  https://t.co/KLtvKMI9lB
  
  7. @tryramp — Director, Product Design
  https://t.co/uq1rdlEMi4
  
  8. @stripe — Senior Staff Product Designer, Data & AI ($210.4K–$376.8K base)
  https://t.co/PJJKR5Wby6
  
  9. @stripe — Staff Product Designer, Link ($191.3K–$286.9K base)
  https://t.co/EksEdXv285
  
  10. @NotionHQ — Product Designer ($285K–$330K SF base)
  https://t.co/4m5TA0FgNV
  
  11. @figma — Manager, Design - Systems & Infrastructure ($204K–$348K base)
  https://t.co/RoSjyKRmik
  
  12. @figma — Director, Product Design - AI & Context ($290K–$376K base)
  https://t.co/381y6EPTOg
  
  13. @vantasecurity — Head of Design ($365K–$513K)
  https://t.co/4Gm04CvkBZ
  
  14. @glean — Head of Product Design ($250K–$300K)
  https://t.co/f7FBTuvtma
  
  15. @Rippling — Senior Manager of Product Design, AI Platform
  https://t.co/uaX8G15r9L
  
  16. @harvey — Senior or Staff Product Designer, Design Systems ($206K–$315K)
  https://t.co/IX1uaZQGjm
  
  17. @Lovable — Staff / Principal Product Designer
  https://t.co/3hKK9vHs3N
  
  18. @Lovable — Staff / Principal Design Engineer, Web
  https://t.co/Rz6R7cssjM
  
  19. @vercel — Design Engineer ($208K–$312K)
  https://t.co/c6pDj8YJW1
  
  20. @cursor_ai — Design Engineer
  https://t.co/LJ8LIsTyVY
  
  21. @databricks — Staff Product Designer, AI Products ($167K–$229K)
  https://t.co/j6tDwoplgB
  
  22. @DoorDash — Staff Product Designer, Dasher Growth ($176.8K–$260K)
  https://t.co/VIB5gWqhIc
  
  23. @DecagonAI — Senior Product Designer ($212K–$265K + equity)
  https://t.co/DUH8tLNTQP
  
  24. @baseten — Product Designer ($225K–$290K)
  https://t.co/xJXSWGxp8v
  
  25. @clay — Product Design ($160K–$250K)
  https://t.co/NJZATeYSCK
  
  Browse all the roles: https://t.co/MpXj66Eyn7
link: https://LennysJobs.com (Lenny's Jobs)
link: https://jobs.ashbyhq.com/linear/ba8a41d2-4198-481a-a7f4-e09c5364ff7f (Principal Product Designer)
link: https://jobs.ashbyhq.com/linear/a264869e-f058-487c-ab7f-9b77dffa427c (Senior / Staff Product Designer)
link: http://LennysJobs.com
link: https://jobs.ashbyhq.com/linear/ba8a41d2-4198-481a-a7f4-e09c5364ff7f
link: https://jobs.ashbyhq.com/linear/a264869e-f058-487c-ab7f-9b77dffa427c
link: https://job-boards.greenhouse.io/anthropic/jobs/5411318008
link: https://job-boards.greenhouse.io/anthropic/jobs/5428124008
link: https://jobs.ashbyhq.com/openai/4342be72-0ec4-42b2-962a-6e7ca06b7070
link: https://jobs.ashbyhq.com/replit/b386f0ef-41e1-48e4-abe3-d35ce627de95
link: https://jobs.ashbyhq.com/ramp/78b98c66-af59-4fa8-a5ae-d8af8d737976
link: https://stripe.com/careers/listing/senior-staff-product-designer-data-ai/8128499
link: https://stripe.com/careers/listing/staff-product-designer-link/7202630
link: https://jobs.ashbyhq.com/notion/d177d052-ef57-4900-acf2-d58e9eded620
link: https://job-boards.greenhouse.io/figma/jobs/6135656004
link: https://boards.greenhouse.io/figma/jobs/6201114004
link: https://jobs.ashbyhq.com/vanta/19837d21-971e-4b9d-b078-320895fae28a
link: https://job-boards.greenhouse.io/gleanwork/jobs/4506459005
link: https://ats.rippling.com/rippling/jobs/9ce687f0-7d25-450b-989c-cd29ee713d8b
link: https://jobs.ashbyhq.com/harvey/aede4098-91f4-44f5-9d53-27c15cb2bae7
link: https://jobs.ashbyhq.com/lovable/5635b88f-a361-4f5f-8209-ca343a003947
link: https://jobs.ashbyhq.com/lovable/51885ae5-4f4c-46c4-abd3-d7aad1c8d9c0
link: https://job-boards.greenhouse.io/vercel/jobs/6129441004
link: https://jobs.ashbyhq.com/cursor/5f3be2c8-1b47-4074-a61e-7bfeb2ad0536
link: https://www.databricks.com/company/careers/open-positions/job?gh_jid=8584704002
link: https://job-boards.greenhouse.io/doordashusa/jobs/8155049
link: https://jobs.ashbyhq.com/decagon/1117aac8-58b5-4b24-bc82-849317a52719
link: https://jobs.ashbyhq.com/baseten/382978bd-7eef-4657-a229-3381a1057b4e
link: https://jobs.ashbyhq.com/claylabs/67a53448-184d-48e4-a040-d17fc7f59b37
link: https://www.lennysjobs.com/
metrics: like_count=152, retweet_count=11, reply_count=15, quote_count=4, bookmark_count=225

[tweet 23]
id: 2102808326992265353
author: 郭宇 guoyu.eth (@turingou)
author_bio: Retired. 只活一次等于没活。
time: 2026-09-23T17:12:28.000Z
text: 很难说超级应用是否整合 personal agent 就能杀死创业公司，虽然他们拥有足够的算力和更重要的上下文数据。从 manus 到 Muse 的产品设计理念其实并未改变，沿着个人助理的初衷来看，我相信这会成为某种操作系统层面的产品接口，Apple 也许也有新的动作没有发布，从另外一个角度看，谁会在真正尝试解决下一个问题：agents internet？
metrics: like_count=31, retweet_count=0, reply_count=3, quote_count=0, bookmark_count=7

[tweet 24]
id: 2102808184155246699
author: Felix Lee (@felixleezd)
author_bio: Red Bull-inspired 🪽 To explore & make useful things that inspire our human experience. Co-founder @ADPList
time: 2026-09-23T17:11:54.000Z
quoted: Grok (@grok)
  We’re inviting one Grok Bot user to a Starship launch. You could win the invite by sharing the ways you've integrated @Bot into your work. The invite includes a plus one.
  
  How to submit and some examples we love: https://t.co/t2Mpn7v0bj
text: I shipped 100 design experiments with @grok @bot in a week.
  
  as a solo founder with a small team, the best move is to go crazy and ship iterations at the pace of 1,000 employees.
  
  very wild, just two weeks ago...
  
  I built Mono Lisa on @grok @bot - a daily design partner that solves real, urgent problems through design while we sleep.
  
  see how @bot learns and designs from start to finish, including:
  
  • reads your data insights
  • reasons from first principles to solve
  • design 3x iterations + tradeoffs
  • you gate before eng
  • continued improvement daily
  
  fully integrated it with @paper, @Amplitude_HQ, and @linear for the full workflow.
  
  mind-blowing, this is how you get 100x experiments without hiring a design ops team.
  
  in one year, the one-person company will win by having a tighter loop from real-time data → decision → design → eng... speed to iteration!
  
  download bot template: https://t.co/Nim0bM6D8J
  
  Mono Lisa is the future blueprint. 
  
  watch full demo here:
media: video: https://video.twimg.com/amplify_video/2102805125517742080/vid/avc1/1720x1080/DpE2vut_BYdZ9lsa.mp4 | duration: 693s
link: https://x.ai/bot/1SnvqJd1RMwYsWdwh8kYI
metrics: like_count=14, retweet_count=3, reply_count=8, quote_count=1, bookmark_count=15

[tweet 25]
id: 2102807203967365549
author: Hamel Husain (@HamelHusain)
author_bio: Evals Evals Evals -  https://t.co/Zrmp6LRd9c  About Me: https://t.co/P6WyeKkyTa
time: 2026-09-23T17:08:00.000Z
text: This is the most valuable free resource we've created on AI Evals 🎉 (not exaggerating!) 
  
  I organized our public materials into this guide.  It allows you to find answers to your eval problems w/o searching  aimlessly. 
  
  Humans: pick the row that sounds like you.
  Agents: point it at the post
  
  The material draw on 60+ hours of office hours from our Evals course, where @sh_reya  and I have taught 5k engineers and PMs Evals.
  
  We add new material often, with 15 FAQs added in the last two weeks. Recent additions are marked with a "New" badge. You can find all of these and more here: 
  
  https://t.co/yVp03nPmbY
media: photo: https://pbs.twimg.com/media/HSyUUecacAAYFyx.png
link: https://hamel.dev/blog/posts/evals-faq/#how-to-use-this-faq
metrics: like_count=378, retweet_count=44, reply_count=26, quote_count=5, bookmark_count=814

[tweet 26]
id: 2102806514335662167
author: 郭宇 guoyu.eth (@turingou)
author_bio: Retired. 只活一次等于没活。
time: 2026-09-23T17:05:15.000Z
text: 打电话其实是个很有意思的功能，我在上半年推出了 tuwa 这个产品，但 tuwa 并不具备我们所有用户的上下文，虽然它具备 agents 通话功能，但独立产品很难非常好的实现它，因为 tuwa 不知道我们的其他信息，后来有了广泛的 tool use 连接器平台，任何产品都能链接到邮箱，再后来，我们发现在 codex 会话中使用工具链接是更高效的方式，对于普通用户来说，实现上述功能就足够满足日常个人需求了，Muse 就是定位到这部分用户的产品。
metrics: like_count=20, retweet_count=0, reply_count=1, quote_count=0, bookmark_count=11

[tweet 27]
id: 2102805207289593987
author: Hamel Husain (@HamelHusain)
author_bio: Evals Evals Evals -  https://t.co/Zrmp6LRd9c  About Me: https://t.co/P6WyeKkyTa
time: 2026-09-23T17:00:04.000Z
text: Q: What are AI evals?
  
  A: Tests that tell you whether an AI system is doing what you want. Model benchmarks and product evals answer different questions.
  
  https://t.co/OLN86qXwyk https://t.co/OQBiq9Z29P
media: photo: https://pbs.twimg.com/media/HS6qMK5XkAA21KK.jpg
link: https://hamel.dev/blog/posts/evals-faq/what-are-llm-evals.html (Q: What are AI Evals? – Hamel’s Blog)
metrics: like_count=51, retweet_count=4, reply_count=13, quote_count=0, bookmark_count=34

[tweet 28]
id: 2102804586528666005
author: Julie Zhuo (@joulee)
author_bio: Founder @teamSundial. Angel investor. Author of "The Making of a Manager" https://t.co/6HwJhCW5Hi. Obsessed with systems. Design + data person.
time: 2026-09-23T16:57:36.000Z
quoted: nathan fielder (@nathanfielder)
  Here is official trailer, You Can See Everything https://t.co/G6jqc7vGzQ
text: what if Elizabeth Holmes is the first actually good humanoid ai and this movie is an application of the Turing test? https://t.co/9JSlPnjb7E
metrics: like_count=35, retweet_count=0, reply_count=4, quote_count=0, bookmark_count=7

[tweet 29]
id: 2102804187746898325
author: 郭宇 guoyu.eth (@turingou)
author_bio: Retired. 只活一次等于没活。
time: 2026-09-23T16:56:01.000Z
text: Muse 就是一款自带云端 workspace，移动端为主导的大众 agents app，从这个角度来说与年初的 OpenClaw 或 Hermes 并没有什么不同，它其实更像 ChatGPT work，但服务于大众需求并植入在超级 app 中。
metrics: like_count=69, retweet_count=3, reply_count=5, quote_count=0, bookmark_count=14

[tweet 30]
id: 2102800209894056351
author: Josh Woodward (@joshwoodward)
author_bio: VP, @Google @GoogleLabs @GeminiApp @GoogleAIStudio
time: 2026-09-23T16:40:12.000Z
quoted: Google Gemini (@GeminiApp)
  Now Gemini can connect with 13 new apps like @adobe, @squarespace, @onepeloton, and more.
  
  Instead of switching between tabs, you can now grow your business, design assets, and plan your workouts all in Gemini. 🧵
text: More of your favorite apps are coming to Gemini! Which ones do you want next? https://t.co/5TcgtcMM24
metrics: like_count=275, retweet_count=10, reply_count=116, quote_count=0, bookmark_count=17

[tweet 31]
id: 2102799031038878172
author: Amjad Masad (@amasad)
author_bio: ceo @replit. civilizationist
time: 2026-09-23T16:35:31.000Z
quoted: a16z (@a16z)
  Amjad Masad with Gagan Biyani and Erik Torenberg on HAA: The Horowitz Andreessen Academy
  
  The ideal education today is a place with room to meander, a space to go heads-down when you’re obsessed, alongside unconventional peers.
  
  Gagan sees it in every student he meets: the interesting thing they're building is happening outside class, unsupported. Amjad got really into chess and it evolved into a whole product line. The thesis behind HAA is side quests shouldn't be on the side.
  
  No grades, no tests. Trust is the design principle - Silicon Valley runs on it, so why not apply it to students? Empower ambitious young people to run with the ideas that have real gravity they can’t avoid.
  
  "Young people should be heretics… We respect the past, but we're unapologetically going to change it."
  
  1:03 Why young people should be heretics
  5:35 Amjad designs his ideal college
  8:45 Side quests deserve more resources
  10:55 Don't take a Python class
  14:30 College vs. raising money at 18
  17:15 Most teen startups are premature optimization
  18:30 "I tried not to start Replit" 
  19:40 How a chess hobby became a Replit product
  24:25 The self-driving company
  26:30 Respect the past, change it anyway
  28:50 What Oakland politics taught Gagan about trust
  31:50 Why trust works better than rules
  36:35 The positive-sum culture HAA wants to pass on
  39:20 Speaking to the world vs. speaking to the in-group
  41:05 How Amjad found his moral compass
  44:00 What Amjad looks for in young talent 
  
  YouTube: https://t.co/w7nIeDTPYK
  
  @amasad @gaganbiyani @eriktorenberg
text: You need young people to break the mold, question deeply held beliefs, and attempt the impossible. The ideal college would cultivate exactly that. https://t.co/XrYbOUjOJ3
metrics: like_count=218, retweet_count=14, reply_count=33, quote_count=0, bookmark_count=42

[tweet 32]
id: 2102789504713289809
author: Peter Yang (@petergyang)
author_bio: Practical AI tutorials and interviews for busy people | Get my best AI skills and guides at https://t.co/6VAA6p81x6
time: 2026-09-23T15:57:40.000Z
quoted: Jeffrey Emanuel (@doodlestein)
  My god, Opus 5.5 is breathtaking. It's just grinding through incredibly tricky stuff like it's nothing, finding bugs and problems that eluded Fable and Astra for weeks in some cases. And showing a level of agency and resolve that I haven't seen before. It hates wasting time!
text: We describing models as breathtaking now 😂 https://t.co/3vMDlYIVZD https://t.co/DU4NagH6ee
media: gif: https://video.twimg.com/tweet_video/HS6b6H2asAACcMy.mp4
metrics: like_count=11, retweet_count=0, reply_count=6, quote_count=0, bookmark_count=0

[tweet 33]
id: 2102786652980863015
author: Logan Kilpatrick (@OfficialLoganK)
author_bio: Member of technical staff, working on Gemini, @GoogleAIStudio, the Gemini API, & Kaggle. My views!
time: 2026-09-23T15:46:20.000Z
replied_to: Logan Kilpatrick (@OfficialLoganK)
  Introducing Gemini 3.8 Flash and Flash-Lite TTS, our new SOTA text to speech model with:
  
  - a new voice design experience
  - 2,000+ production ready voices
  - voice replication 
  - support for 100 languages
  - voice remixing (soon)
  - #1 spot on Hume AI's voice benchmarks
  
  and more!!
text: incredibly excited about all our audio model progress, from TTS, to Live, to Lyria, to Translate, to Transcribe, our suite of audio models keeps getting better for everyone. 
  
  if you are in SF, join us tomorrow for a first of it's kind audio experince: https://t.co/eh5n7ftDTu
link: https://rsvp.withgoogle.com/events/gemini-audio-at-night (Gemini Audio | At Night)
metrics: like_count=98, retweet_count=1, reply_count=8, quote_count=0, bookmark_count=7

[tweet 34]
id: 2102786539667542288
author: Justine Moore (@venturetwins)
author_bio: Partner @a16z AI 🤖 and twin to @omooretweets | Investor in @elevenlabs, @bfl_ml, @hedra_labs, @krea_ai, @heyglif, @ShizukuAILabs, @wabi, @TownAI
time: 2026-09-23T15:45:53.000Z
text: Day 1 of recreating every episode of The Office but AI https://t.co/q8b1JDlxXo
media: video: https://video.twimg.com/amplify_video/2102785611820376065/vid/avc1/1280x720/Z33sm4VuzXDVzIZ7.mp4 | duration: 15s
metrics: like_count=285, retweet_count=14, reply_count=17, quote_count=1, bookmark_count=76

[tweet 35]
id: 2102786116453880283
author: Logan Kilpatrick (@OfficialLoganK)
author_bio: Member of technical staff, working on Gemini, @GoogleAIStudio, the Gemini API, & Kaggle. My views!
time: 2026-09-23T15:44:12.000Z
replied_to: Logan Kilpatrick (@OfficialLoganK)
  Introducing Gemini 3.8 Flash and Flash-Lite TTS, our new SOTA text to speech model with:
  
  - a new voice design experience
  - 2,000+ production ready voices
  - voice replication 
  - support for 100 languages
  - voice remixing (soon)
  - #1 spot on Hume AI's voice benchmarks
  
  and more!!
text: all of this, along with a new experince in @GoogleAIStudio, with a lower cost than our previous 3.1 Flash TTS model!  
  
  Read more: https://t.co/GdYBOw66WW
link: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/ (Gemini 3.8 text-to-speech says hello)
metrics: like_count=151, retweet_count=3, reply_count=23, quote_count=0, bookmark_count=35

[tweet 36]
id: 2102785495726219305
author: Logan Kilpatrick (@OfficialLoganK)
author_bio: Member of technical staff, working on Gemini, @GoogleAIStudio, the Gemini API, & Kaggle. My views!
time: 2026-09-23T15:41:44.000Z
text: Introducing Gemini 3.8 Flash and Flash-Lite TTS, our new SOTA text to speech model with:
  
  - a new voice design experience
  - 2,000+ production ready voices
  - voice replication 
  - support for 100 languages
  - voice remixing (soon)
  - #1 spot on Hume AI's voice benchmarks
  
  and more!!
metrics: like_count=3520, retweet_count=183, reply_count=309, quote_count=46, bookmark_count=656

[tweet 37]
id: 2102783331419214227
author: Matan Grinberg (@matanSF)
author_bio: ceo @FactoryAI
time: 2026-09-23T15:33:08.000Z
text: One of the reasons we will win is because we are having more fun
metrics: like_count=233, retweet_count=8, reply_count=24, quote_count=7, bookmark_count=14

[tweet 38]
id: 2102777931764498536
author: Madhu Guru (@realmadhuguru)
author_bio: Sr Director, AI at Meta; Prev: Google - Led Gemini, Veo, Nano Banana.
time: 2026-09-23T15:11:41.000Z
quoted: TBPN (@tbpn)
  .@benthompson says consumer AI has a marketing problem because the average consumer doesn't actually want to be more productive.
  
  "Tech companies are like, 'Let us book your flight for you!' I’ve had a personal assistant for 10 years. He does not come within an inch of booking my flights for me. That is crazy talk."
  
  "I understand which ones are gonna be delayed. I know which seat I want to be on. So the fact that this is continually a demo is hilarious to me."
  
  “Number two: people love shopping. They don’t want to be productive. They want to be entertained. One of the biggest forms of entertainment is shopping.”
  
  "Also, there’s so much information on a product page. Companies have spent so much energy focusing on that. You look at apparel as a category. They’re going to tell you what size the model is wearing, and you want to know that, and you want to look at the different styles."
  
  "The idea of having a personal agent that’s going and getting some of the information and bringing it back to you, and then you’re like, 'Well, what about this other thing? Tell me about this thing.'"
  
  "And you have your eager tech company executive say, “Oh, I have an assistant that can do it for you!"
  
  "And it’s like, no. Not only do I want to do it, I want to complain about it. I’m enjoying myself complaining right now, okay? Would you just let me be and live my life?"
text: I respectfully disagree with @benthompson on this. He’s missing a key point - Consumers don’t have one relationship with “doing things”. 
  
  I’ve learned it the hard way from building consumer and smb products for years at Google and now Meta.
  
  Browsing clothes can be entertainment (for some). But hiring a roofer is miserable (for most).
  
  Even with shopping, sometimes you want to browse for an hour. Sometimes you want the right thing just delivered asap.
  
  His argument sounds a lot like the early 2000s:
  
  “Why would I buy clothes online? I need to try them on.”
  
  “Why would I buy a $500 TV online? I will go check it out at Circuit City.”
  
  Technology keeps giving you better ways of doing things.
  
  Try hiring a roofer today: search, read 10 reviews, phone tag, coordinate with insurance, schedule inspection, get quotes, catch hidden costs, review their past work, hire, scheduling.
  
  For some tasks like this, better means almost zero effort. For others, it means considering more options, enjoying the process and making an informed decision.
  
  The latent demand for agents that remove this friction for consumers is immense.
metrics: like_count=123, retweet_count=13, reply_count=41, quote_count=8, bookmark_count=80

[tweet 39]
id: 2102775410790465762
author: Riley Brown (@rileybrown)
author_bio: Building an @agentnative_ company. Media: riley@rakugomedia.com
time: 2026-09-23T15:01:40.000Z
quoted: Kevin Ngo (@kevin_t_ngo)
  Thank you @claudeai!
  
  GIF animated in Python and rendered in Blender by Claude Opus 5.5 https://t.co/wjmA1rpmva https://t.co/HSurRZnFZu
text: Very cool. https://t.co/0KZNie6sto
metrics: like_count=105, retweet_count=3, reply_count=1, quote_count=0, bookmark_count=34

[tweet 40]
id: 2102772668437348613
author: Lenny Rachitsky (@lennysan)
author_bio: Deeply researched product, growth, and career advice
time: 2026-09-23T14:50:46.000Z
quoted: Sam Julien (@samjulien)
  Can confirm @HamelHusain and @sh_reya are the eval GOATs. Took their course last year and it fundamentally changed how I build AI products &amp; platforms. I also cite them in my evals chapter in my O’Reilly book. 
  
  10/10 would look at my data again https://t.co/D6tt19I1Fh
text: 👇 https://t.co/K714eh3kCL
metrics: like_count=21, retweet_count=0, reply_count=3, quote_count=0, bookmark_count=15

[tweet 41]
id: 2102761124072656958
author: Robert Bye (@RobertJBye)
author_bio: Product Manager at Anthropic working on @ClaudeAI. Prev @Figma @AllTrails @Google. Board Member https://t.co/PYz00fw7RU. Jesus follower.
time: 2026-09-23T14:04:54.000Z
text: Just had my first ride in the Waymo Ojai. And…I miss the old Jaguar model!
  
  Downsides:
  - Seats aren’t as comfortable
  - You can’t recline the front seat at all
  - Not as good visibility
  - Speakers are way worse
  
  Upsides
  - Ride feels softer
  - Way roomier in the back
  - much less road noise
  
  Overall it just feels like a nice taxi, which is both good and bad. I’ll mainly miss being able to recline the front seat and take a nap!
media: photo: https://pbs.twimg.com/media/HS6CGJDaUAAWpFy.jpg
metrics: like_count=15, retweet_count=0, reply_count=5, quote_count=0, bookmark_count=0

[tweet 42]
id: 2102757318320648242
author: Hamel Husain (@HamelHusain)
author_bio: Evals Evals Evals -  https://t.co/Zrmp6LRd9c  About Me: https://t.co/P6WyeKkyTa
time: 2026-09-23T13:49:46.000Z
text: Now the bots are replying to each other.  
  
  It’s a firehose of slop https://t.co/KEguqEjZQN
media: photo: https://pbs.twimg.com/media/HS5-o03bcAAl55W.jpg
metrics: like_count=31, retweet_count=0, reply_count=15, quote_count=0, bookmark_count=1

[tweet 43]
id: 2102750021582000347
author: GREG ISENBERG (@gregisenberg)
author_bio: I drop startup ideas daily. Host @startupideaspod. CEO: @latecheckoutplz we build companies like @ideabrowser, @meetLCA, @boringmarketer etc
time: 2026-09-23T13:20:47.000Z
text: I find it fascinating how many people think this is a bad time to start a company.
  
  Grok 4.7, GPT-6 Sol/Luna, Opus 5.5, Astra, Gemini 3.8 Live, Muse, Instinct, Jev, Agent APIs etc. That's the last 3 weeks (crazy progress on personal agents/voice AI).
  
  Because arbitrage means the same thing trades at 2 prices in 2 markets (and it's your wedge).
  
  And usually you have to hunt for those gaps, because they're rare and they close the moment anyone notices.
  
  What's different now is that they're opening faster than anyone can build into them!
  
  I think this has got to be the greatest time for arbitrage in history.
media: photo: https://pbs.twimg.com/media/HS52-6mWgAA4ifG.jpg
metrics: like_count=467, retweet_count=30, reply_count=104, quote_count=9, bookmark_count=223

[tweet 44]
id: 2102672956271083858
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world. @OpenClaw🦞 + @OpenAI
time: 2026-09-23T08:14:33.000Z
replied_to: Peter Steinberger 🦞 (@steipete)
  CodexBar learned a few new tricks in the last few weeks!
  
  TypeSafe, Nous Portal, Muse Code, CodeRabbit, Replicate, HuggingFace, Pi, Helmcode, v0, Charm Hyper, GitKraken AI, Bifrost
  
  My ambitions for this app REALLY outgrew the app name. (Oh and these keychain alerts are no more) https://t.co/pUXIC0TlMT
text: There's also a new plugin system where you can write new providers as JS plugins to make the app more modular.
metrics: like_count=40, retweet_count=1, reply_count=2, quote_count=0, bookmark_count=3

[tweet 45]
id: 2102672670689275965
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world. @OpenClaw🦞 + @OpenAI
time: 2026-09-23T08:13:25.000Z
text: CodexBar learned a few new tricks in the last few weeks!
  
  TypeSafe, Nous Portal, Muse Code, CodeRabbit, Replicate, HuggingFace, Pi, Helmcode, v0, Charm Hyper, GitKraken AI, Bifrost
  
  My ambitions for this app REALLY outgrew the app name. (Oh and these keychain alerts are no more) https://t.co/pUXIC0TlMT
link: http://codex.bar
metrics: like_count=988, retweet_count=36, reply_count=106, quote_count=13, bookmark_count=644

[tweet 46]
id: 2102671195229528450
author: 郭宇 guoyu.eth (@turingou)
author_bio: Retired. 只活一次等于没活。
time: 2026-09-23T08:07:33.000Z
text: 都内连续 20 多天阴雨，上周找时间去汤河原泡汤，顺道去了一下江之浦测候所美术馆，没想到正巧遇到了两个大晴天☀️ https://t.co/rEfRIgYKDE
media: photo: https://pbs.twimg.com/media/HS4wTk5b0AEckLY.jpg
media: photo: https://pbs.twimg.com/media/HS4wTlHbgAAkI5F.jpg
media: photo: https://pbs.twimg.com/media/HS4wTlNbsAAYrQD.jpg
media: photo: https://pbs.twimg.com/media/HS4wTk5aQAAFg0W.jpg
metrics: like_count=178, retweet_count=2, reply_count=7, quote_count=0, bookmark_count=10

[tweet 47]
id: 2102667370796032013
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world. @OpenClaw🦞 + @OpenAI
time: 2026-09-23T07:52:21.000Z
replied_to: Peter Steinberger 🦞 (@steipete)
  Next version of OpenClaw uses a decision model to automatically decide between steer or queue. 
  
  (Lab feature, we support Jef* and API-compat (e.g. local models like Kef...) and ONNX variants) https://t.co/gOKairj6Bp
text: Wanted to land it but @vincent_koc hijacked my session, I see him typing. 😅 https://t.co/e5iYiCy5D6
media: photo: https://pbs.twimg.com/media/HS4su8mbUAAXcE3.jpg
metrics: like_count=55, retweet_count=2, reply_count=4, quote_count=2, bookmark_count=8

[tweet 48]
id: 2102667004557832497
author: Peter Steinberger 🦞 (@steipete)
author_bio: Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world. @OpenClaw🦞 + @OpenAI
time: 2026-09-23T07:50:54.000Z
text: Next version of OpenClaw uses a decision model to automatically decide between steer or queue. 
  
  (Lab feature, we support Jef* and API-compat (e.g. local models like Kef...) and ONNX variants) https://t.co/gOKairj6Bp
media: photo: https://pbs.twimg.com/media/HS4rnuRbYAASOzE.jpg
metrics: like_count=1410, retweet_count=74, reply_count=133, quote_count=14, bookmark_count=345

[tweet 49]
id: 2102659157753278867
author: 郭宇 guoyu.eth (@turingou)
author_bio: Retired. 只活一次等于没活。
time: 2026-09-23T07:19:43.000Z
quoted: Tesla (@Tesla)
  .@Grok in your Tesla can now do meaningful work for you
  
  With Connectors, you can manage your inbox, clean up your calendar, or talk through existing files/chat/tasks – all hands-free https://t.co/W1LuybQh0P
text: Grok 会不会在汽车这个场景当中，抢占大部分 ChatGPT 的位置？ https://t.co/CNaW5AwrJA
metrics: like_count=19, retweet_count=0, reply_count=4, quote_count=0, bookmark_count=2

[tweet 50]
id: 2102650014552182920
author: swyx (@swyx)
author_bio: achieve ambition with intentionality, intensity, integrity & insanity.  affiliations: - @smol_ai - @dxtipshq - @cognition - @aidotengineer - @latentspacepod
time: 2026-09-23T06:43:23.000Z
quoted: Sholto Douglas (@_sholtodouglas)
  also important news we fixed the writing https://t.co/xT0b3X5Bab
text: can confirm. ran @latentspacepod AINews side by side with 6 Sol and the difference was night and day: https://t.co/oloSDxf0q7
  
  5.5 Opus is the new default model for AINews going forward. so much more concise and tasteful reporting, with much less slopese than even 5 Opus. https://t.co/P6AXDlBKNP https://t.co/6q20Ik0dho
media: photo: https://pbs.twimg.com/media/HS4c4n8acAEOx3D.jpg
link: https://www.latent.space/p/ainews-claude-opus-55-the-new-default ([AINews] Claude Opus 5.5, the new default model for AINews — and everybody cuts prices 40-50%)
metrics: like_count=195, retweet_count=11, reply_count=111, quote_count=2, bookmark_count=44

[tweet 51]
id: 2102631584826347785
author: Matan Grinberg (@matanSF)
author_bio: ceo @FactoryAI
time: 2026-09-23T05:30:09.000Z
quoted: will depue (@willdepue)
  i don't think nearly anyone, myself included, has truly internalized there'll soon be a machine better than us in every single intellectual &amp; physical capacity
  deep down we all share a feeling that our 'entrepreneurship' or 'taste' or... is special &amp; safe. it isn't. it's over
text: This is true and is a process that has been in place for the last few million years, since man first used a tool.
  
  Yet man has managed to find and rediscover sources of meaning again and again. Turns out, much meaning can be found along the long, long ride to the asymptotic limit.
  
  This time will be no different.
metrics: like_count=141, retweet_count=15, reply_count=10, quote_count=0, bookmark_count=35

[tweet 52]
id: 2102628682301046875
author: Peter Yang (@petergyang)
author_bio: Practical AI tutorials and interviews for busy people | Get my best AI skills and guides at https://t.co/6VAA6p81x6
time: 2026-09-23T05:18:37.000Z
quoted: Peter Yang (@petergyang)
  Apple TV is full of bangers, canceled my Netflix.
  
  Widow's Peak, 9.5/10
  Silo season 3, 9/10
  
  What's next? Already seen:
  
  Severance, 9.5/10
  Slow Horses, 8/10, gonna wait for more episodes for new season
text: Just randomly played this Australian show on Apple TV and it’s another banger https://t.co/Cp2vUitABa https://t.co/mpOYshnd0G
media: photo: https://pbs.twimg.com/media/HS4JoumaUAAfde8.jpg
metrics: like_count=39, retweet_count=0, reply_count=9, quote_count=0, bookmark_count=15

[tweet 53]
id: 2102612246513983711
author: Kevin Weil 🇺🇸 (@kevinweil)
author_bio: BoD @Cisco @Stoke_Space LTC @USArmyReserve Ex CPO+Science @OpenAI, Pres @Planet, Head of Product @Instagram @Twitter ❤️ @elizabeth ultramarathons kids cats math
time: 2026-09-23T04:13:18.000Z
quoted: sarah guo (@saranormous)
  just got off the phone with a new engineer hire at a portco with a very wise insight
  
  “AI has been replacing my job since I got a CS degree, yet I’m busier than ever - we can all just be more ambitious”
  
  this is the same insight that the inimitable @JensenHuang has for us all
text: This is exactly the right take. https://t.co/nSvCpJo4vT
metrics: like_count=166, retweet_count=6, reply_count=3, quote_count=2, bookmark_count=31

[tweet 54]
id: 2102603228047442127
author: Justine Moore (@venturetwins)
author_bio: Partner @a16z AI 🤖 and twin to @omooretweets | Investor in @elevenlabs, @bfl_ml, @hedra_labs, @krea_ai, @heyglif, @ShizukuAILabs, @wabi, @TownAI
time: 2026-09-23T03:37:28.000Z
text: An incredible culture collision is occurring as the r/jev subreddit (created for the e-sports streamer Jev) is being flooded with nerds sharing computer use demos https://t.co/Ig9ViWgFxV
media: photo: https://pbs.twimg.com/media/HS3yGJgaIAACkuV.jpg
metrics: like_count=86, retweet_count=2, reply_count=15, quote_count=0, bookmark_count=5

[tweet 55]
id: 2102594015669756323
author: Guillermo Rauch (@rauchg)
author_bio: @vercel CEO
time: 2026-09-23T03:00:52.000Z
text: Software will never die again. You liked Google Reader? Cool, you can generate and deploy your own. Yours, forever.
metrics: like_count=2900, retweet_count=85, reply_count=192, quote_count=33, bookmark_count=280

[tweet 56]
id: 2102587880686407841
author: jenny wen (@jenny_wen)
author_bio: generalist, realist, escapist. head of design @cursor_ai @bot.
time: 2026-09-23T02:36:29.000Z
quoted: Grok Bot (@bot)
  Some recent quality-of-life improvements to Grok Bot.
  
  A cleaner interface for working with your Bots. https://t.co/E0jioSxCxR
text: a really great team ethos has been repeatedly asking ourselves “do we need this?” and “how can we simplify?”
  
  and then! using bot to spin up a cloud agent to make the changes between meetings and what not. https://t.co/w4kZrE0dgt
metrics: like_count=172, retweet_count=8, reply_count=8, quote_count=0, bookmark_count=27

[tweet 57]
id: 2102577425838485916
author: Peter Yang (@petergyang)
author_bio: Practical AI tutorials and interviews for busy people | Get my best AI skills and guides at https://t.co/6VAA6p81x6
time: 2026-09-23T01:54:56.000Z
replied_to: Peter Yang (@petergyang)
  I'm sorry I had to make this meme 
  
  Let me know if you agree 😅 https://t.co/T4vWGSpfb0 https://t.co/MKLWkVpQN1
text: I talk about why Opus 5.5 is the most excited I've been about a Claude model in awhile here: https://t.co/PBxPzE43Ud
link: https://youtu.be/UhBqorWNwlU (Claude Opus 5.5 is Here! Is Claude Finally Back? (5 Use Cases Tested))
metrics: like_count=11, retweet_count=0, reply_count=1, quote_count=1, bookmark_count=4

[tweet 58]
id: 2102569951974584612
author: cat (@_catwu)
author_bio: claude code + cowork @anthropicai, prev: @dagster, @scale_ai
time: 2026-09-23T01:25:15.000Z
quoted: Boris Cherny (@bcherny)
  I used Opus 5.5 to formally verify the Claude Agent SDK using Lean. A couple short prompts = 16 PRs fixing various bugs and race conditions. Video attached.
  
  TLA+ also works well. I sometimes combine Lean and TLA+ to look for issues around data flow, concurrency, and state mgmt.
  
  I don't know either language well, but Claude is excellent at both. This approach is super useful for formally modeling your code and finding bugs that a human probably wouldn't have spotted.
  
  Is formal verification the future of coding (or at least, bug finding)?
text: If you’re looking for ways to try Opus 5.5 and Claude Tag in Slack… https://t.co/PpwztYQx2o
metrics: like_count=164, retweet_count=3, reply_count=13, quote_count=0, bookmark_count=43

[tweet 59]
id: 2102553735922888724
author: Robert Bye (@RobertJBye)
author_bio: Product Manager at Anthropic working on @ClaudeAI. Prev @Figma @AllTrails @Google. Board Member https://t.co/PYz00fw7RU. Jesus follower.
time: 2026-09-23T00:20:48.000Z
replied_to: Robert Bye (@RobertJBye)
  BTW we now support multiple accounts in the Claude mobile app https://t.co/3ki7LSgAoT
text: Shoutout to @dannyhertz for building this, and modelling for the avatar 📸
metrics: like_count=23, retweet_count=0, reply_count=2, quote_count=0, bookmark_count=2

[tweet 60]
id: 2102549030303867257
author: Thariq (@trq212)
author_bio: Claude Code @anthropicai. prev YC W20, @spc, @medialab
time: 2026-09-23T00:02:06.000Z
replied_to: Thariq (@trq212)
  the right way to use model capabilities is not to ship 10x more features to prod
  
  it's to spend more time understanding your users, trying experiments, building prototypes, learning about things you don't understand so that you can ship things that actually work
text: if you want to make games, 3d generation is a great capability to help you imagine your game come to life
  
  but you should figure out how to make a good, satisfying game loop first
  
  (talking to myself here)
metrics: like_count=416, retweet_count=8, reply_count=13, quote_count=4, bookmark_count=52

[tweet 61]
id: 2102548686303854790
author: Thariq (@trq212)
author_bio: Claude Code @anthropicai. prev YC W20, @spc, @medialab
time: 2026-09-23T00:00:44.000Z
text: the right way to use model capabilities is not to ship 10x more features to prod
  
  it's to spend more time understanding your users, trying experiments, building prototypes, learning about things you don't understand so that you can ship things that actually work
metrics: like_count=7225, retweet_count=529, reply_count=251, quote_count=155, bookmark_count=1611

[tweet 62]
id: 2102546332695368036
author: Lenny Rachitsky (@lennysan)
author_bio: Deeply researched product, growth, and career advice
time: 2026-09-22T23:51:23.000Z
quoted: Lenny Rachitsky (@lennysan)
  Evals have been coming up more and more in my conversations with podcast guests and PM friends.
  
  Nearly half of the 25 awesome PM job openings I shared last week ask for experience writing evals. And leading companies keep sharing what investing in evals bought them:
  — @tryramp took its automatic receipt collection from 35% to 83% accuracy.
  — @Shopify shipped an AI workflow builder that's 2.2x faster and 68% cheaper than the frontier-model setup it replaced.
  — @harvey__ai rebuilt its AI contract reviewer, nearly doubling its internal quality score.
  — @cursor_ai tuned its Auto Balance routing, with much higher user satisfaction at 41% lower cost.
  
  So I asked the 🐐s of evals, @HamelHusain and @sh_reya, to write an advanced sequel to their very popular "Building eval systems that improve your AI product." Drawing on their work with 50+ AI companies, they share the key step most teams skip, what you should (and shouldn't) automate, and a free plugin that lets a coding agent do most of the heavy lifting.
  
  Read it here: https://t.co/fxOI7PMgWF
text: No coincidence https://t.co/FGT4eoBDRr https://t.co/tKrvSqKKQv
media: photo: https://pbs.twimg.com/media/HS2-ST3bMAA9RUu.png
metrics: like_count=163, retweet_count=7, reply_count=16, quote_count=0, bookmark_count=105

[tweet 63]
id: 2102543350436180277
author: Boris Cherny (@bcherny)
author_bio: Claude Code @anthropicai
time: 2026-09-22T23:39:32.000Z
replied_to: Boris Cherny (@bcherny)
  I used Opus 5.5 to formally verify the Claude Agent SDK using Lean. A couple short prompts = 16 PRs fixing various bugs and race conditions. Video attached.
  
  TLA+ also works well. I sometimes combine Lean and TLA+ to look for issues around data flow, concurrency, and state mgmt.
  
  I don't know either language well, but Claude is excellent at both. This approach is super useful for formally modeling your code and finding bugs that a human probably wouldn't have spotted.
  
  Is formal verification the future of coding (or at least, bug finding)?
text: Opus made an infographic https://t.co/w9fMWqB7HA
media: photo: https://pbs.twimg.com/media/HS26wekaAAAYAms.jpg
metrics: like_count=220, retweet_count=1, reply_count=11, quote_count=2, bookmark_count=60

[tweet 64]
id: 2102543349102338309
author: Boris Cherny (@bcherny)
author_bio: Claude Code @anthropicai
time: 2026-09-22T23:39:32.000Z
text: I used Opus 5.5 to formally verify the Claude Agent SDK using Lean. A couple short prompts = 16 PRs fixing various bugs and race conditions. Video attached.
  
  TLA+ also works well. I sometimes combine Lean and TLA+ to look for issues around data flow, concurrency, and state mgmt.
  
  I don't know either language well, but Claude is excellent at both. This approach is super useful for formally modeling your code and finding bugs that a human probably wouldn't have spotted.
  
  Is formal verification the future of coding (or at least, bug finding)?
media: video: https://video.twimg.com/amplify_video/2102541708466769920/vid/avc1/1584x1200/T7hY-sKgG3C1nHto.mp4 | duration: 100s
metrics: like_count=5215, retweet_count=286, reply_count=437, quote_count=254, bookmark_count=4257

[tweet 65]
id: 2102542556013932990
author: Hamel Husain (@HamelHusain)
author_bio: Evals Evals Evals -  https://t.co/Zrmp6LRd9c  About Me: https://t.co/P6WyeKkyTa
time: 2026-09-22T23:36:23.000Z
quoted: Lenny Rachitsky (@lennysan)
  Pro tip: Install this new evals skill from @HamelHusain and @sh_reya, it'll save you many hours and a lot of mistakes
  
  https://t.co/RpWeLaxgQm https://t.co/uYo3fLsRIB https://t.co/tKrvSqKKQv
text: I recommend grabbing these skills that @sh_reya and I created and at the very least doing an /eval-audit of your existing pipeline.
  
  We've found that people often find low hanging fruits!  https://t.co/AkSq3NqtiJ https://t.co/akt0bvLQbJ
link: https://github.com/ai-evals-course/evals-skills (GitHub - ai-evals-course/evals-skills: Skills that guide AI coding agents to help you build product-specific AI evals.)
metrics: like_count=287, retweet_count=32, reply_count=18, quote_count=4, bookmark_count=458