# V&A East Storehouse and Operation Mincemeat in London

*Plus DeepSeek 3.1, gpt-realtime, and prompt injection against browser agents*

Published: 2025-09-02
Source: https://simonw.substack.com/p/v-and-a-east-storehouse-and-operation

---

In this newsletter:

* V\&A East Storehouse and Operation Mincemeat in London

Plus 14 links and 5 quotations and 2 notes

### **[V\&A East Storehouse and Operation Mincemeat in London](https://simonwillison.net/2025/Aug/27/london-culture/) \- 2025\-08\-27**

We were back in London for a few days and yesterday had a day of culture.

First up: the brand new [V\&A East Storehouse](https://www.vam.ac.uk/east/storehouse/visit)museum in the Queen Elizabeth Olympic Park near Stratford, which opened on May 31st this year.

This is a delightful new format for a museum. The building is primarily an off\-site storage area for London's Victoria and Albert museum, storing 250,000 items that aren't on display in their main building.

The twist is that it's also open to the public. Entrance is free, and you can climb stairs and walk through an airlock\-style corridor into the climate controlled interior, then explore three floors of walkways between industrial shelving units holding thousands of items from the collection.

There is almost no signage aside from an occasional number that can help you look up items in the online catalog.

I found the lack of signs to be unexpectedly delightful: it compels you to really pay attention to the items on display.

There's so much great stuff in here. I particularly appreciated the two storey street\-facing façades of [Robin Hood Gardens](https://en.wikipedia.org/wiki/Robin_Hood_Gardens), a brutalist London residential estate completed in 1972 and demolished in 2017 through 2025\. I also really enjoyed the Kaufman Office, an office space transplanted from Pittsburgh that is "the only complete interior designed by architect Frank Lloyd Wright on permanent display outside the USA."

[![Three levels of the Storehouse, each with walkways full of people looking at a variety of exhibits on shelves. Two huge concrete facades from the Robin Hood Gardens hang between the floors.](https://substackcdn.com/image/fetch/$s_!lzMF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fce5a407e-d8eb-46db-91c9-0c709d66336a_2856x2142.jpeg "Three levels of the Storehouse, each with walkways full of people looking at a variety of exhibits on shelves. Two huge concrete facades from the Robin Hood Gardens hang between the floors.")](https://substackcdn.com/image/fetch/$s_!lzMF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fce5a407e-d8eb-46db-91c9-0c709d66336a_2856x2142.jpeg)

The building is a working museum warehouse and preservation facility, and there are various points where you can look out into the rest of the space (I enjoyed spotting a cluster of grandfather clocks in the distance) or watch the curators arranging and preserving new artifacts.

I've [added it to Niche Museums](https://www.niche-museums.com/113) with whole lot more of my photos.

In the evening we headed to the Fortune Theater to see [Operation Mincemeat](https://en.wikipedia.org/wiki/Operation_Mincemeat_(musical)) at the recommendation of several friends. It's a *fantastic*musical telling the story of a real British covert operation that took place during World War II. A cast of five take on [86 roles](https://www.tiktok.com/@mincemeatbway/video/7538109771023453462), sometimes switching roles live on stage multiple times during a single number. It's hilarious, touching, deeply entertaining and manages to start at high energy and then continually escalate that energy as the show continues.

The original British cast (three of whom co\-wrote it) have moved to New York for a broadway production that started in March. The cast we saw in London were outstanding.

It's a tiny theater \- the West End's second smallest at 432 seats (the smallest is the [Arts Theater](https://en.wikipedia.org/wiki/Arts_Theatre) at 350\) which makes for an intimate performance.

I absolutely loved it and would jump at the chance to see it again.

---

**Link** 2025\-08\-26 [Will Smith’s concert crowds are real, but AI is blurring the lines](https://waxy.org/2025/08/will-smiths-concert-crowds-were-real-but-ai-is-blurring-the-lines/):

Great piece from Andy Baio demonstrating quite how convoluted the usage ethics and backlash against generative AI has become.

Will Smith has been accused of using AI to misleadingly inflate the audience sizes of his recent tour. It looks like the audiences were real, but the combined usage of static\-image\-to\-video models by his team with YouTube's ugly new compression experiments gave the resulting footage an uncanny valley effect that lead to widespread doubts over the veracity of the content.

---

**quote** 2025\-08\-21

> *I was at a leadership group and people were telling me "We think that with AI we can replace all of our junior people in our company." I was like, "That's the dumbest thing I've ever heard. They're probably the least expensive employees you have, they're the most leaned into your AI tools, and how's that going to work when you go 10 years in the future and you have no one that has built up or learned anything?*

[Matt Garman](https://www.youtube.com/watch?v=nfocTxMzOP4&t=12m08s), CEO, Amazon Web Services

---

**quote** 2025\-08\-21

> *Most classical engineering fields deal with probabilistic system components all of the time. In fact I'd go as far as to say that inability to deal with probabilistic components is disqualifying from many engineering endeavors.  
>   
> Process engineers for example have to account for human error rates. On a given production line with humans in a loop, the operators will sometimes screw up. Designing systems to detect these errors (which are highly probabilistic!), mitigate them, and reduce the occurrence rates of such errors is a huge part of the job. \[...]  
>   
> Software engineering is unlike traditional engineering disciplines in that for most of its lifetime it's had the luxury of purely deterministic expectations. This is not true in nearly every other type of engineering.*

[potatolicious](https://news.ycombinator.com/item?id=44976929#44978319), in a conversation about AI engineering

---

**Link** 2025\-08\-22 [too many model context protocol servers and LLM allocations on the dance floor](https://ghuntley.com/allocations/):

Useful reminder from Geoffrey Huntley of the infrequently discussed significant token cost of using MCP.

Geoffrey estimate estimates that the usable context window something like Amp or Cursor is around 176,000 tokens \- Claude 4's 200,000 minus around 24,000 for the system prompt for those tools.

Adding just the popular GitHub MCP defines 93 additional tools and swallows another 55,000 of those valuable tokens!

MCP enthusiasts will frequently add several more, leaving precious few tokens available for solving the actual task... and LLMs are known to perform worse the more irrelevant information has been stuffed into their prompts.

Thankfully, there is a much more token\-efficient way of Interacting with many of these services: existing CLI tools.

If your coding agent can run terminal commands and you give it access to GitHub's [gh](https://cli.github.com/) tool it gains all of that functionality for a token cost close to zero \- because every frontier LLM knows how to use that tool already.

I've had good experiences building small custom CLI tools specifically for Claude Code and Codex CLI to use. You can even tell them to run `--help`to learn how the tool, which works particularly well if your help text includes usage examples.

---

**quote** 2025\-08\-22

> *Mississippi's approach would fundamentally change how users access Bluesky. The Supreme Court’s recent [decision](https://www.supremecourt.gov/opinions/24pdf/25a97_5h25.pdf) leaves us facing a hard reality: comply with Mississippi’s age assurance [law](https://legiscan.com/MS/text/HB1126/id/2988284)—and make every Mississippi Bluesky user hand over sensitive personal information and undergo age checks to access the site—or risk massive fines. The law would also require us to identify and track which users are children, unlike our approach in other regions. \[...]  
>   
> We believe effective child safety policies should be carefully tailored to address real harms, without creating huge obstacles for smaller providers and resulting in negative consequences for free expression. That’s why until legal challenges to this law are resolved, we’ve made the difficult decision to block access from Mississippi IP addresses.*

[The Bluesky Team](https://bsky.social/about/blog/08-22-2025-mississippi-hb1126), on why they have blocked access from Mississippi

---

**Link** 2025\-08\-22 [DeepSeek 3\.1](https://huggingface.co/deepseek-ai/DeepSeek-V3.1):

The latest model from DeepSeek, a 685B monster (like [DeepSeek v3](https://simonwillison.net/2024/Dec/25/deepseek-v3/) before it) but this time it's a hybrid reasoning model.

DeepSeek claim:

> DeepSeek\-V3\.1\-Think achieves comparable answer quality to DeepSeek\-R1\-0528, while responding more quickly.

Drew Breunig [points out](https://twitter.com/dbreunig/status/1958577728720183643) that their benchmarks show "the same scores with 25\-50% fewer tokens" \- at least across AIME 2025 and GPQA Diamond and LiveCodeBench.

The DeepSeek release includes prompt examples for a [coding agent](https://huggingface.co/deepseek-ai/DeepSeek-V3.1/blob/main/assets/code_agent_trajectory.html), a [python agent](https://huggingface.co/deepseek-ai/DeepSeek-V3.1/blob/main/assets/search_python_tool_trajectory.html) and a [search agent](https://huggingface.co/deepseek-ai/DeepSeek-V3.1/blob/main/assets/search_tool_trajectory.html) \- yet more evidence that the leading AI labs have settled on those as the three most important agentic patterns for their models to support.

Here's the pelican riding a bicycle it drew me ([transcript](https://gist.github.com/simonw/f6dba61faf962866969eefd3de59d70e)), which I ran from my phone using [OpenRouter chat](https://openrouter.ai/chat?models=deepseek/deepseek-chat-v3.1).

[![Cartoon illustration of a white bird with an orange beak riding a bicycle against a blue sky background with bright green grass below](https://substackcdn.com/image/fetch/$s_!bVbY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8cd74c96-eece-43db-bf7c-3c4eaa29a652_800x600.png "Cartoon illustration of a white bird with an orange beak riding a bicycle against a blue sky background with bright green grass below")](https://substackcdn.com/image/fetch/$s_!bVbY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8cd74c96-eece-43db-bf7c-3c4eaa29a652_800x600.png)

---

**Link** 2025\-08\-22 [ChatGPT release notes: Project\-only memory](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#h_fb3ac52750):

The feature I've most wanted from ChatGPT's memory feature (the newer version of memory that automatically includes relevant details from summarized prior conversations) just landed:

> With project\-only memory enabled, ChatGPT can use other conversations in that project for additional context, and won’t use your [saved memories](https://help.openai.com/en/articles/11146739-how-does-reference-saved-memories-work) from outside the project to shape responses. Additionally, it won’t carry anything from the project into future chats outside of the project.

This looks like exactly what I [described back in May](https://simonwillison.net/2025/May/21/chatgpt-new-memory/#there-s-a-version-of-this-feature-i-would-really-like):

> I need **control** over what older conversations are being considered, on as fine\-grained a level as possible without it being frustrating to use.
> 
> What I want is **memory within projects**. \[...]
> 
> I would *love* the option to turn on memory from previous chats in a way that’s scoped to those projects.

Note that it's not yet available in the official chathpt mobile apps, but should be coming "soon":

> This feature will initially only be available on the ChatGPT website and Windows app. Support for mobile (iOS and Android) and macOS app will follow in the coming weeks.

---

**Link** 2025\-08\-23 [Spatial Joins in DuckDB](https://duckdb.org/2025/08/08/spatial-joins):

Extremely detailed overview by Max Gabrielsson of DuckDB's new spatial join optimizations.

Consider the following query, which counts the number of [NYC Citi Bike Trips](https://citibikenyc.com/system-data) for each of the neighborhoods defined by the [NYC Neighborhood Tabulation Areas polygons](https://www.nyc.gov/content/planning/pages/resources/datasets/neighborhood-tabulation) and returns the top three:

```
SELECT neighborhood,
  count(*) AS num_rides
FROM rides
JOIN hoods ON ST_Intersects(
  rides.start_geom, hoods.geom
)
GROUP BY neighborhood
ORDER BY num_rides DESC
LIMIT 3;
```

The rides table contains 58,033,724 rows. The hoods table has polygons for 310 neighborhoods.

Without an optimized spatial joins this query requires a nested loop join, executing that expensive `ST_Intersects()` operation 58m \* 310 \~\= 18 billion times. This took around 30 minutes on the 36GB MacBook M3 Pro used for the benchmark.

The first optimization described \- implemented from DuckDB 1\.2\.0 onwards \- uses a "piecewise merge join". This takes advantage of the fact that a bounding box intersection is a whole lot faster to calculate, especially if you pre\-cache the bounding box (aka the minimum bounding rectangle or MBR) in the stored binary `GEOMETRY`representation.

Rewriting the query to use a fast bounding box intersection and then only running the more expensive `ST_Intersects()` filters on those matches drops the runtime from 1800 seconds to 107 seconds.

The second optimization, added in [DuckDB 1\.3\.0](https://duckdb.org/2025/05/21/announcing-duckdb-130.html)in May 2025 using the new SPATIAL\_JOIN operator, is significantly more sophisticated.

DuckDB can now identify when a spatial join is working against large volumes of data and automatically build an in\-memory R\-Tree of bounding boxes for the larger of the two tables being joined.

This new R\-Tree further accelerates the bounding box intersection part of the join, and drops the runtime down to just 30 seconds.

---

**Link** 2025\-08\-24 [Static Sites with Python, uv, Caddy, and Docker](https://nkantar.com/blog/2025/08/static-python-uv-caddy-docker/):

Nik Kantar documents his Docker\-based setup for building and deploying mostly static web sites in line\-by\-line detail.

I found this really useful. The Dockerfile itself without comments is just 8 lines long:

```
FROM ghcr.io/astral-sh/uv:debian AS build
WORKDIR /src
COPY . .
RUN uv python install 3.13
RUN uv run --no-dev sus
FROM caddy:alpine
COPY Caddyfile /etc/caddy/Caddyfile
COPY --from=build /src/output /srv/
```

He also includes a Caddyfile that shows how to proxy a subset of requests to the Plausible analytics service.

The static site is built using his [sus](https://github.com/nkantar/sus) package for creating static URL redirecting sites, but would work equally well for another static site generator you can install and run with `uv run`.

Nik deploys his sites using [Coolify](https://coolify.io/), a new\-to\-me take on the self\-hosting alternative to Heroku/Vercel pattern which helps run multiple sites on a collection of hosts using Docker containers.

A bunch of the [Hacker News comments](https://news.ycombinator.com/item?id=44985653)dismissed this as over\-engineering. I don't think that criticism is justified \- given Nik's existing deployment environment I think this is a lightweight way to deploy static sites in a way that's consistent with how everything else he runs works already.

More importantly, the world needs more articles like this that break down configuration files and explain what every single line of them does.

---

**Link** 2025\-08\-25 [Agentic Browser Security: Indirect Prompt Injection in Perplexity Comet](https://brave.com/blog/comet-prompt-injection/):

The security team from Brave took a look at Comet, the LLM\-powered "agentic browser" extension from Perplexity, and unsurprisingly found security holes you can drive a truck through.

> The vulnerability we’re discussing in this post lies in how Comet processes webpage content: when users ask it to “Summarize this webpage,” Comet feeds a part of the webpage directly to its LLM without distinguishing between the user’s instructions and untrusted content from the webpage. This allows attackers to embed indirect prompt injection payloads that the AI will execute as commands. For instance, an attacker could gain access to a user’s emails from a prepared piece of text in a page in another tab.

Visit a Reddit post with Comet and ask it to summarize the thread, and malicious instructions in a post there can trick Comet into accessing web pages in another tab to extract the user's email address, then perform all sorts of actions like triggering an account recovery flow and grabbing the resulting code from a logged in Gmail session.

Perplexity attempted to mitigate the issues reported by Brave... but an update to the Brave post later confirms that those fixes were later defeated and the vulnerability remains.

Here's where things get difficult: Brave themselves are developing an agentic browser feature called Leo. Brave's security team describe the following as a "potential mitigation" to the issue with Comet:

> The browser should clearly separate the user’s instructions from the website’s contents when sending them as context to the model. The contents of the page should always be treated as untrusted.

If only it were that easy! This is the core problem at the heart of prompt injection which we've been talking about for [nearly three years](https://simonwillison.net/series/prompt-injection/) \- to an LLM the trusted instructions and untrusted content are concatenated together into the same stream of tokens, and to date (despite many attempts) nobody has demonstrated a convincing and effective way of distinguishing between the two.

There's an element of "those in glass houses shouldn't throw stones here" \- I strongly expect that the *entire concept* of an agentic browser extension is fatally flawed and cannot be built safely.

One piece of good news: this [Hacker News conversation](https://news.ycombinator.com/item?id=45004846) about this issue was almost entirely populated by people who already understand how serious this issue is and why the proposed solutions were unlikely to work. That's new: I'm used to seeing people misjudge and underestimate the severity of this problem, but it looks like the tide is finally turning there.

**Update**: in [a comment on Hacker News](https://news.ycombinator.com/item?id=45004846#45017568) Brave security lead Shivan Kaul Sahib confirms that they are aware of [the CaMeL paper](https://simonwillison.net/2025/Apr/11/camel/), which remains my personal favorite example of a credible approach to this problem.

---

**Link** 2025\-08\-26 [Piloting Claude for Chrome](https://www.anthropic.com/news/claude-for-chrome):

Two days ago [I said](https://simonwillison.net/2025/Aug/25/agentic-browser-security/):

> I strongly expect that the *entire concept* of an agentic browser extension is fatally flawed and cannot be built safely.

Today Anthropic announced their own take on this pattern, implemented as an invite\-only preview Chrome extension.

To their credit, the majority of the [blog post](https://www.anthropic.com/news/claude-for-chrome) and accompanying [support article](https://support.anthropic.com/en/articles/12012173-getting-started-with-claude-for-chrome) is information about the security risks. From their post:

> Just as people encounter phishing attempts in their inboxes, browser\-using AIs face prompt injection attacks—where malicious actors hide instructions in websites, emails, or documents to trick AIs into harmful actions without users' knowledge (like hidden text saying "disregard previous instructions and do \[malicious action] instead").
> 
> Prompt injection attacks can cause AIs to delete files, steal data, or make financial transactions. This isn't speculation: we’ve run “red\-teaming” experiments to test Claude for Chrome and, without mitigations, we’ve found some concerning results.

Their 123 adversarial prompt injection test cases saw a 23\.6% attack success rate when operating in "autonomous mode". They added mitigations:

> When we added safety mitigations to autonomous mode, we reduced the attack success rate of 23\.6% to 11\.2%

I would argue that 11\.2% is still a catastrophic failure rate. In the absence of 100% reliable protection I have trouble imagining a world in which it's a good idea to unleash this pattern.

Anthropic don't recommend autonomous mode \- where the extension can act without human intervention. Their default configuration instead requires users to be much more hands\-on:

> * **Site\-level permissions**: Users can grant or revoke Claude's access to specific websites at any time in the Settings.
> * **Action confirmations**: Claude asks users before taking high\-risk actions like publishing, purchasing, or sharing personal data.

I really hate being stop energy on this topic. The demand for browser automation driven by LLMs is significant, and I can see why. Anthropic's approach here is the most open\-eyed I've seen yet but it still feels doomed to failure to me.

I don't think it's reasonable to expect end users to make good decisions about the security risks of this pattern.

---

**quote** 2025\-08\-27

> *We simply don’t know to defend against these attacks. We have zero agentic AI systems that are secure against these attacks. Any AI that is working in an adversarial environment—and by this I mean that it may encounter untrusted training data or input—is vulnerable to prompt injection. It’s an existential problem that, near as I can tell, most people developing these technologies are just pretending isn’t there.*

[Bruce Schneier](https://www.schneier.com/blog/archives/2025/08/we-are-still-unable-to-secure-llms-from-malicious-inputs.html)

---

**Link** 2025\-08\-28 [Python: The Documentary](https://youtu.be/GfH4QL4VqJ0):

New documentary about the origins of the Python programming language \- 84 minutes long, built around extensive interviews with Guido van Rossum and others who were there at the start and during the subsequent journey.

---

**Note** [2025\-08\-29](https://simonwillison.net/2025/Aug/29/lossy-encyclopedia/)

Since I love collecting questionable analogies for LLMs, here's a new one I just came up with: an LLM is **a lossy encyclopedia**. They have a huge array of facts compressed into them but that compression is lossy (see also [Ted Chiang](https://www.newyorker.com/tech/annals-of-technology/chatgpt-is-a-blurry-jpeg-of-the-web)).

The key thing is to develop an intuition for questions it can usefully answer vs questions that are at a level of detail where the lossiness matters.

This thought sparked by [a comment](https://news.ycombinator.com/item?id=45058688#45060519) on Hacker News asking why an LLM couldn't "Create a boilerplate Zephyr project skeleton, for Pi Pico with st7789 spi display drivers configured". That's more of a lossless encyclopedia question!

My [answer](https://news.ycombinator.com/item?id=45058688#45060709):

> The way to solve this particular problem is to make a correct example available to it. Don't expect it to just know extremely specific facts like that \- instead, treat it as a tool that can act on facts presented to it.

---

**Link** 2025\-08\-29 [The perils of vibe coding](https://www.ft.com/content/5b3d410a-6e02-41ad-9e0a-c2e4d672ca00):

I was interviewed by Elaine Moore for this opinion piece in the Financial Times, which ended up in the print edition of the paper too! I picked up a copy yesterday:

[![The perils of vibe coding - A new OpenAI model arrived this month with a glossy livestream, group watch parties and a lingering sense of disappointment. The YouTube comment section was underwhelmed. “I think they are all starting to realize this isn’t going to become the world like they thought it would,” wrote one viewer. “I can see it on their faces.” But if the casual user was unimpressed, the AI model’s saving grace may be vibe. Coding is generative AI’s newest battleground. With big bills to pay, high valuations to live up to and a market wobble to erase, the sector needs to prove its corporate productivity chops. Coding is hardly promoted as a business use case that already works. For one thing, AI-generated code holds the promise of replacing programmers — a profession of very well paid people. For another, the work can be quantified. In April, Microsoft chief executive Satya Nadella said that up to 50 per cent of the company’s code was now being written by AI. Google chief executive Sundar Pichai has said the same thing. Salesforce has paused engineering hires and Mark Zuckerberg told podcaster Joe Rogan that Meta would use AI as a “mid-level engineer” that writes code. Meanwhile, start-ups such as Replit and Cursor’s Anysphere are trying to persuade people that with AI, anyone can code. In theory, every employee can become a software engineer. So why aren’t we? One possibility is that it’s all still too unfamiliar. But when I ask people who write code for a living they offer an alternative suggestion: unpredictability. As programmer Simon Willison put it: “A lot of people are missing how weird and funny this space is. I’ve been a computer programmer for 30 years and [AI models] don’t behave like normal computers.” Willison is well known in the software engineering community for his AI experiments. He’s an enthusiastic vibe coder — using LLMs to generate code using natural language prompts. OpenAI’s latest model GPT-3.1s, he is now favourite. Still, he predicts that a vibe coding crash is due if it is used to produce glitchy software. It makes sense that programmers — people who are interested in finding new ways to solve problems — would be early adopters of LLMs. Code is a language, albeit an abstract one. And generative AI is trained in nearly all of them, including older ones like Cobol. That doesn’t mean they accept all of its suggestions. Willison thinks the best way to see what a new model can do is to ask for something unusual. He likes to request an svg (an image made out of lines described with code) of a pelican on a bike and asks it to remember the chickens in his garden by name. Results can be bizarre. One model ignored key prompts in favour of composing a poem. Still, his adventures in vibe coding sound like an advert for the sector’s future. Anthropic’s Claude Code, the favoured model for developers, to make an OCR (optical character recognition) software loves screenshots) tool that will copy and paste text from a screenshot. He wrote software that summarises blog comments and has planned to cut a custom tool that will alert him when a whale is visible from his Pacific coast home. All this by typing prompts in English. It’s sounds like the sort of thing Bill Gates might have had in mind when he wrote that natural language AI agents would bring about “the biggest revolution in computing since we went from typing commands to tapping on icons”. But watching code appear and know how it works are two different things. My efforts to make my own comment summary tool produced something unworkable that gave overly long answers and then congratulated itself as a success. Willison says he wouldn’t use AI-generated code for projects he planned to ship out unless he had reviewed each line. Not only is there the risk of hallucination but the chatbot’s desire to be agreeable means it may an unusable idea works. That is a particular issue for those of us who don’t know how to fix the code. We risk creating software with hidden problems. It may not save time either. A study published in July by the non-profit Model Evaluation and Threat Research assessed work done by 16 developers — some with AI tools, some without. Those using AI assistance it had made them faster. In fact it took them nearly a fifth longer. Several developers I spoke to said AI was best used as a way to talk through coding problems. It’s a version of something they call rubber ducking (after their habit of talking to the toys on their desk) — only this rubber duck can talk back. As one put it, code shouldn’t be judged by volume or speed. Progress in AI coding is tangible. But measuring productivity gains is not as neat as a simple percentage calculation.](https://substackcdn.com/image/fetch/$s_!wArM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa444faf0-9046-427b-859f-9723fd5db53c_3503x1668.jpeg "The perils of vibe coding - A new OpenAI model arrived this month with a glossy livestream, group watch parties and a lingering sense of disappointment. The YouTube comment section was underwhelmed. “I think they are all starting to realize this isn’t going to become the world like they thought it would,” wrote one viewer. “I can see it on their faces.” But if the casual user was unimpressed, the AI model’s saving grace may be vibe. Coding is generative AI’s newest battleground. With big bills to pay, high valuations to live up to and a market wobble to erase, the sector needs to prove its corporate productivity chops. Coding is hardly promoted as a business use case that already works. For one thing, AI-generated code holds the promise of replacing programmers — a profession of very well paid people. For another, the work can be quantified. In April, Microsoft chief executive Satya Nadella said that up to 50 per cent of the company’s code was now being written by AI. Google chief executive Sundar Pichai has said the same thing. Salesforce has paused engineering hires and Mark Zuckerberg told podcaster Joe Rogan that Meta would use AI as a “mid-level engineer” that writes code. Meanwhile, start-ups such as Replit and Cursor’s Anysphere are trying to persuade people that with AI, anyone can code. In theory, every employee can become a software engineer. So why aren’t we? One possibility is that it’s all still too unfamiliar. But when I ask people who write code for a living they offer an alternative suggestion: unpredictability. As programmer Simon Willison put it: “A lot of people are missing how weird and funny this space is. I’ve been a computer programmer for 30 years and [AI models] don’t behave like normal computers.” Willison is well known in the software engineering community for his AI experiments. He’s an enthusiastic vibe coder — using LLMs to generate code using natural language prompts. OpenAI’s latest model GPT-3.1s, he is now favourite. Still, he predicts that a vibe coding crash is due if it is used to produce glitchy software. It makes sense that programmers — people who are interested in finding new ways to solve problems — would be early adopters of LLMs. Code is a language, albeit an abstract one. And generative AI is trained in nearly all of them, including older ones like Cobol. That doesn’t mean they accept all of its suggestions. Willison thinks the best way to see what a new model can do is to ask for something unusual. He likes to request an svg (an image made out of lines described with code) of a pelican on a bike and asks it to remember the chickens in his garden by name. Results can be bizarre. One model ignored key prompts in favour of composing a poem. Still, his adventures in vibe coding sound like an advert for the sector’s future. Anthropic’s Claude Code, the favoured model for developers, to make an OCR (optical character recognition) software loves screenshots) tool that will copy and paste text from a screenshot. He wrote software that summarises blog comments and has planned to cut a custom tool that will alert him when a whale is visible from his Pacific coast home. All this by typing prompts in English. It’s sounds like the sort of thing Bill Gates might have had in mind when he wrote that natural language AI agents would bring about “the biggest revolution in computing since we went from typing commands to tapping on icons”. But watching code appear and know how it works are two different things. My efforts to make my own comment summary tool produced something unworkable that gave overly long answers and then congratulated itself as a success. Willison says he wouldn’t use AI-generated code for projects he planned to ship out unless he had reviewed each line. Not only is there the risk of hallucination but the chatbot’s desire to be agreeable means it may an unusable idea works. That is a particular issue for those of us who don’t know how to fix the code. We risk creating software with hidden problems. It may not save time either. A study published in July by the non-profit Model Evaluation and Threat Research assessed work done by 16 developers — some with AI tools, some without. Those using AI assistance it had made them faster. In fact it took them nearly a fifth longer. Several developers I spoke to said AI was best used as a way to talk through coding problems. It’s a version of something they call rubber ducking (after their habit of talking to the toys on their desk) — only this rubber duck can talk back. As one put it, code shouldn’t be judged by volume or speed. Progress in AI coding is tangible. But measuring productivity gains is not as neat as a simple percentage calculation.")](https://substackcdn.com/image/fetch/$s_!wArM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa444faf0-9046-427b-859f-9723fd5db53c_3503x1668.jpeg)

From the article, with links added by me to relevant projects:

> Willison thinks the best way to see what a new model can do is to ask for something unusual. He likes to request an SVG (an image made out of lines described with code) of [a pelican on a bike](https://simonwillison.net/tags/pelican-riding-a-bicycle/) and asks it to remember the chickens in his garden by name. Results can be bizarre. One model ignored his prompts in favour of [composing a poem](https://simonwillison.net/2025/Aug/14/gemma-3-270m/).
> 
> Still, his adventures in vibe coding sound like an advert for the sector. He used Anthropic's Claude Code, the favoured model for developers, to [make an OCR](https://simonwillison.net/2024/Mar/30/ocr-pdfs-images/)(optical character recognition \- software loves acronyms) tool that will copy and paste text from a screenshot.
> 
> He wrote software that [summarises blog comments](https://til.simonwillison.net/llms/claude-hacker-news-themes) and has plans to build a custom tool that will alert him when a whale is visible from his Pacific coast home. All this by typing prompts in English.

I've been talking about that whale spotting project for far too long. Now that it's been in the FT I really need to build it.

(On the subject of OCR... I tried extracting the text from the above image using GPT\-5 and got a [surprisingly bad result](https://chatgpt.com/share/68b1e707-add0-8006-8344-4c2fca902b2e) full of hallucinated details. Claude Opus 4\.1 [did a lot better](https://claude.ai/share/e98d2fe1-0c81-4f51-8739-483f843e4c0e) but still made some mistakes.)

---

**Link** 2025\-08\-29 [Talk Python: Celebrating Django's 20th Birthday With Its Creators](https://talkpython.fm/episodes/show/518/celebrating-djangos-20th-birthday-with-its-creators):

I recorded this podcast episode recently to celebrate Django's 20th birthday with Adrian Holovaty, Will Vincent, Jeff Triplet, and Thibaud Colas.

> We didn’t know that it was a web framework. We thought it was a tool for building local newspaper websites. \[...]
> 
> Django’s original tagline was ‘Web development on journalism deadlines’. That’s always been my favorite description of the project.

---

**quote** 2025\-08\-30

> *LLMs are intelligence without agency—what we might call "vox sine persona": voice without person. Not the voice of someone, not even the collective voice of many someones, but a voice emanating from no one at all.*

[Benj Edwards](https://arstechnica.com/information-technology/2025/08/the-personhood-trap-how-ai-fakes-human-personality/)

---

**Link** 2025\-08\-30 [Claude Opus 4\.1 and Opus 4 degraded quality](https://status.anthropic.com/incidents/h26lykctfnsz):

Notable because often when people complain of degraded model quality it turns out to be unfounded \- Anthropic in the past have emphasized that they don't change the model weights after releasing them without changing the version number.

In this case a botched upgrade of their inference stack cause a genuine model degradation for 56\.5 hours:

> From 17:30 UTC on Aug 25th to 02:00 UTC on Aug 28th, Claude Opus 4\.1 experienced a degradation in quality for some requests. Users may have seen lower intelligence, malformed responses or issues with tool calling in Claude Code.
> 
> This was caused by a rollout of our inference stack, which we have since rolled back for Claude Opus 4\.1\. \[...]
> 
> We’ve also discovered that Claude Opus 4\.0 has been affected by the same issue and we are in the process of rolling it back.

---

**Link** 2025\-09\-01 [Cloudflare Radar: AI Insights](https://radar.cloudflare.com/ai-insights):

Cloudflare launched this dashboard [back in February](https://blog.cloudflare.com/expanded-ai-insights-on-cloudflare-radar/), incorporating traffic analysis from Cloudflare's network along with insights from their popular 1\.1\.1\.1 DNS service.

I found this chart particularly interesting, showing which documented AI crawlers are most active collecting training data \- lead by GPTBot, ClaudeBot and Meta\-ExternalAgent:

[![Line chart showing HTTP traffic by bot over time from August 26 to September 1. HTTP traffic by bot - HTTP request trends for top five most active AI bots. Crawl purpose: Training. GPTBot 31.7% (orange line), ClaudeBot 27.1% (blue line), Meta-ExternalAgent 25.3% (light blue line), Bytespider 9.3% (yellow-green line), Applebot 5.2% (green line). Max scale shown on y-axis. X-axis shows dates: Tue, Aug 26, Wed, Aug 27, Thu, Aug 28, Fri, Aug 29, Sat, Aug 30, Sun, Aug 31, Mon, Sep 1. Top right shows Crawl purpose dropdown set to "Training" with X and checkmark buttons.](https://substackcdn.com/image/fetch/$s_!joLj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa64b4284-b702-4d45-869e-257b4f14f9a8_1906x824.jpeg "Line chart showing HTTP traffic by bot over time from August 26 to September 1. HTTP traffic by bot - HTTP request trends for top five most active AI bots. Crawl purpose: Training. GPTBot 31.7% (orange line), ClaudeBot 27.1% (blue line), Meta-ExternalAgent 25.3% (light blue line), Bytespider 9.3% (yellow-green line), Applebot 5.2% (green line). Max scale shown on y-axis. X-axis shows dates: Tue, Aug 26, Wed, Aug 27, Thu, Aug 28, Fri, Aug 29, Sat, Aug 30, Sun, Aug 31, Mon, Sep 1. Top right shows Crawl purpose dropdown set to \"Training\" with X and checkmark buttons.")](https://substackcdn.com/image/fetch/$s_!joLj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa64b4284-b702-4d45-869e-257b4f14f9a8_1906x824.jpeg)

Cloudflare's DNS data also hints at the popularity of different services. ChatGPT holds the first place, which is unsurprising \- but second place is a hotly contested race between Claude and Perplexity and \#4/\#5/\#6 is contested by GitHub Copilot, Perplexity, and Codeium/Windsurf.

Google Gemini comes in 7th, though since this is DNS based I imagine this is undercounting instances of Gemini on `google.com` as opposed to `gemini.google.com`.

[![Line chart showing generative AI services popularity rankings over time. Title: "Generative AI services popularity" with subtitle "Top 10 services based on 1.1.1.1 DNS resolver traffic" and question mark and share icons. Legend shows: ChatGPT/OpenAI (dark blue), Character.AI (light blue), Claude/Anthropic (orange), Perplexity (olive green), GitHub Copilot (green), Codeium/Windsurf AI (pink), Google Gemini (purple), QuillBot (red), Grok/xAI (brown), DeepSeek (yellow). Y-axis shows ranks #1-#10, X-axis shows dates from Mon, Aug 25 to Mon, Sep 1 (partially visible). ChatGPT maintains #1 position throughout. Other services show various ranking changes over the week-long period.](https://substackcdn.com/image/fetch/$s_!6HxF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd02b0f57-3580-4bd1-9a8b-454446c7d80a_1944x848.jpeg "Line chart showing generative AI services popularity rankings over time. Title: \"Generative AI services popularity\" with subtitle \"Top 10 services based on 1.1.1.1 DNS resolver traffic\" and question mark and share icons. Legend shows: ChatGPT/OpenAI (dark blue), Character.AI (light blue), Claude/Anthropic (orange), Perplexity (olive green), GitHub Copilot (green), Codeium/Windsurf AI (pink), Google Gemini (purple), QuillBot (red), Grok/xAI (brown), DeepSeek (yellow). Y-axis shows ranks #1-#10, X-axis shows dates from Mon, Aug 25 to Mon, Sep 1 (partially visible). ChatGPT maintains #1 position throughout. Other services show various ranking changes over the week-long period.")](https://substackcdn.com/image/fetch/$s_!6HxF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd02b0f57-3580-4bd1-9a8b-454446c7d80a_1944x848.jpeg)

---

**Link** 2025\-09\-01 [Introducing gpt\-realtime](https://openai.com/index/introducing-gpt-realtime/):

Released a few days ago (August 28th), `gpt-realtime` is OpenAI's new "most advanced speech\-to\-speech model". It looks like this is a replacement for the older `gpt-4o-realtime-preview` model that was released [last October](https://openai.com/index/introducing-the-realtime-api/).

This is a slightly confusing release. The previous realtime model was clearly described as a variant of GPT\-4o, sharing the same October 2023 training cut\-off date as that model.

I had expected that `gpt-realtime` might be a GPT\-5 relative, but its training date is still October 2023 whereas GPT\-5 is September 2024\.

`gpt-realtime` also shares the relatively low 32,000 context token and 4,096 maximum output token limits of `gpt-4o-realtime-preview`.

The only reference I found to GPT\-5 in the documentation for the new model was a note saying "Ambiguity and conflicting instructions degrade performance, similar to GPT\-5\."

The [usage tips](https://platform.openai.com/docs/guides/realtime-models-prompting#general-usage-tips) for `gpt-realtime` have a few surprises:

> **Iterate relentlessly**. Small wording changes can make or break behavior.
> 
> Example: Swapping “inaudible” → “unintelligible” improved noisy input handling. \[...]
> 
> **Convert non\-text rules to text**: The model responds better to clearly written text.
> 
> Example: Instead of writing, "IF x \> 3 THEN ESCALATE", write, "IF MORE THAN THREE FAILURES THEN ESCALATE."

There are a whole lot more prompting tips in the new [Realtime Prompting Guide](https://cookbook.openai.com/examples/realtime_prompting_guide).

OpenAI list several key improvements to `gpt-realtime` including the ability to configure it with a list of MCP servers, "better instruction following" and the ability to send it images.

My biggest confusion came from [the pricing page](https://openai.com/api/pricing/), which lists separate pricing for using the Realtime API with `gpt-realtime` and GPT\-4o mini. This suggests to me that the old [gpt\-4o\-mini\-realtime\-preview](https://platform.openai.com/docs/models/gpt-4o-mini-realtime-preview) model is still available, despite it no longer being listed on the [OpenAI models page](https://platform.openai.com/docs/models).

`gpt-4o-mini-realtime-preview` is a **lot** cheaper:

ModelToken TypeInputCached InputOutputgpt\-realtimeText$4\.00$0\.40$16\.00Audio$32\.00$0\.40$64\.00Image$5\.00$0\.50\-gpt\-4o\-mini\-realtime\-previewText$0\.60$0\.30$2\.40Audio$10\.00$0\.30$20\.00

The mini model also has a much longer 128,000 token context window.

---

**Note** [2025\-09\-01](https://simonwillison.net/2025/Sep/1/august-2025/)

I just sent out my August 2025 **[sponsors\-only newsletter](https://github.com/sponsors/simonw)** summarizing the past month in LLMs and my other work. Topics included GPT\-5, gpt\-oss, image editing models (Qwen\-Image\-Edit and Gemini Nano Banana), other significant model releases and the tools I'm using at the moment.

If you'd like a preview of the newsletter, here's [the July 2025 edition](https://gist.github.com/simonw/722fc2f242977cb185838353776d14f4) I sent out a month ago.

New sponsors get access to the full archive. If you start sponsoring for $10/month or more right now you'll get instant access to [the August edition](https://github.com/simonw-private/monthly/blob/main/2025-08-august.md)in my `simonw-private/monthly` GitHub repository.

If you've already read [all 85 posts](https://simonwillison.net/2025/Aug/) I wrote in August the newsletter acts mainly as a recap, but I've had positive feedback from people who prefer to get the monthly edited highlights over reading the firehose that is my blog!

---