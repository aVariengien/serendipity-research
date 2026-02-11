# December in LLMs has been a lot

*Plus notes on OpenAI's o3, and my approach to running a link blog*

Published: 2024-12-22
Source: https://simonw.substack.com/p/december-in-llms-has-been-a-lot

---

In this newsletter:

* December in LLMs has been a lot
* My approach to running a link blog

Plus 3 links and 2 quotations

### [December in LLMs has been a lot](https://simonwillison.net/2024/Dec/20/december-in-llms-has-been-a-lot/) \- 2024\-12\-20

I had big plans for December: for one thing, I was hoping to get to an actual RC of Datasette 1\.0, in preparation for a full release in January. Instead, I've found myself distracted by a [constant barrage](https://simonwillison.net/search/?tag=llms&year=2024&month=12) of new LLM releases.

On December 4th Amazon introduced the **[Amazon Nova family](https://simonwillison.net/2024/Dec/4/amazon-nova/)** of multi\-modal models \- clearly priced to compete with the excellent and inexpensive Gemini 1\.5 series from Google. I got those working with [LLM](https://llm.datasette.io/) via a new [llm\-bedrock](https://github.com/simonw/llm-bedrock) plugin.

The next big release was **[Llama 3\.3 70B\-Instruct](https://simonwillison.net/2024/Dec/6/llama-33/)**, on December 6th. Meta claimed that this 70B model was comparable in quality to their much larger 405B model, and those claims seem to hold weight.

I wrote about how [I can now run a GPT\-4 class model on my laptop](https://simonwillison.net/2024/Dec/9/llama-33-70b/) \- the same laptop that was running a GPT\-3 class model just 20 months ago.

Llama 3\.3 70B has started showing up from API providers now, including super\-fast hosted versions from both [Groq](https://groq.com/new-ai-inference-speed-benchmark-for-llama-3-3-70b-powered-by-groq/) (276 tokens/second) and [Cerebras](https://cerebras.ai/inference) (a quite frankly absurd 2,200 tokens/second). If you haven't tried Val Town's [Cerebras Coder](https://cerebrascoder.com/) demo you really should.

I think the huge gains in model efficiency are one of the defining stories of LLMs in 2024\. It's not just the local models that have benefited: the price of proprietary hosted LLMs has dropped through the floor, a result of both competition between vendors and the increasing efficiency of the models themselves.

Last year the running joke was that every time Google put out a new Gemini release OpenAI would ship something more impressive that same day to undermine them.

The tides have turned! This month Google shipped four updates that took the wind out of OpenAI's sails.

The first was **[gemini\-exp\-1206](https://simonwillison.net/2024/Dec/6/gemini-exp-1206/)** on December 6th, an experimental model that jumped straight to the top of some of the leaderboards. Was this our first glimpse of Gemini 2\.0?

That was followed by **[Gemini 2\.0 Flash](https://simonwillison.net/2024/Dec/11/gemini-2/)** on December 11th, the first official release in Google's Gemini 2\.0 series. The streaming support was particularly impressive, with <https://aistudio.google.com/live> demonstrating streaming audio and webcam communication with the multi\-modal LLM a full day before OpenAI released their own streaming camera/audio features in an update to ChatGPT.

Then this morning Google shipped **[Gemini 2\.0 Flash "Thinking mode"](https://simonwillison.net/2024/Dec/19/gemini-thinking-mode/)**, their version of the inference scaling technique pioneered by OpenAI's o1\. I did *not* expect Gemini to ship a version of that before 2024 had even ended.

OpenAI have one day left in their [12 Days of OpenAI](https://openai.com/12-days/) event. Previous highlights have included the full **o1** model (an upgrade from o1\-preview) and **o1\-pro**, [Sora](https://simonwillison.net/2024/Dec/9/sora/) (later upstaged a week later by Google's [Veo 2](https://simonwillison.net/2024/Dec/16/veo-2/)), Canvas (with a confusing [second way to run Python](https://simonwillison.net/2024/Dec/10/chatgpt-canvas/)), [Advanced Voice with video streaming](https://simonwillison.net/2024/Dec/13/openai-voice-mode-faq/) and Santa and a *very* cool new [WebRTC streaming API](https://simonwillison.net/2024/Dec/17/openai-webrtc/), ChatGPT Projects (pretty much a direct lift of the similar Claude feature) and the 1\-800\-CHATGPT phone line.

… (*update from* *a day later*) they announced benchmarks for their new o3 model. [I live\-blogged their announcement here](https://simonwillison.net/2024/Dec/20/live-blog-the-12th-day-of-openai/), and strongly recommend reading François Chollet’s commentary on the ARC Prize blog: [OpenAI o3 breakthrough high score on ARC\-AGI\-PUB](https://arcprize.org/blog/oai-o3-pub-breakthrough).

---

### [My approach to running a link blog](https://simonwillison.net/2024/Dec/22/link-blog/) \- 2024\-12\-22

I started running a basic link blog on this domain [back in November 2003](https://simonwillison.net/2003/Nov/24/blogmarks/) \- publishing links (which I called "blogmarks") with a title, URL, short snippet of commentary and a "via" links where appropriate.

So far I've published [7,607 link blog posts](https://simonwillison.net/search/?type=blogmark) and counting.

In April of this year I finally [upgraded my link blog to support Markdown](https://simonwillison.net/2024/Apr/25/blogmarks-that-use-markdown/), allowing me to expand my link blog into something with a lot more room.

The way I use my link blog has evolved substantially in the eight months since then. I'm going to describe the informal set of guidelines I've set myself for how I link blog, in the hope that it might encourage other people to give this a try themselves.

* [Writing about things I've found](https://simonwillison.net/2024/Dec/22/link-blog/#writing-about-things-i-ve-found)
* [Trying to add something extra](https://simonwillison.net/2024/Dec/22/link-blog/#trying-to-add-something-extra)
* [The technology](https://simonwillison.net/2024/Dec/22/link-blog/#the-technology)
* [More people should do this](https://simonwillison.net/2024/Dec/22/link-blog/#more-people-should-do-this)

#### Writing about things I've found

Back in November 2022 I wrote [What to blog about](https://simonwillison.net/2022/Nov/6/what-to-blog-about/), which started with this:

> You should start a blog. Having your own little corner of the internet is good for the soul!

The point of that article was to emphasize that blogging doesn't have to be about unique insights. The value is in writing frequently and having something to show for it over time \- worthwhile even if you don't attract much of an audience (or any audience at all).

In that article I proposed two categories of content that are low stakes and high value: **things I learned** and **descriptions of my projects**.

I realize now that link blogging deserves to be included a third category of low stakes, high value writing. We could think of that category as **things I've found**.

That's the purpose of my link blog: it's an ongoing log of things I've found \- effectively a combination of public bookmarks and my own thoughts and commentary on why those things are interesting.

#### Trying to add something extra

When I first started link blogging I would often post a link with a one sentence summary of the linked content, and maybe a tiny piece of opinionated commentary.

After I upgraded my link blog to support additional markup (links, images, quotations) I decided to be more ambitious. Here are some of the things I try to do:

* I always include **the names of the people** who created the content I a linking to, if I can figure that out. Credit is really important, and it's also useful for myself because I can later search for someone's name and find other interesting things they have created that I linked to in the past. If I've linked to someone's work three or more times I also try to notice and upgrade them to [a dedicated tag](https://simonwillison.net/tags/).
* I try to **add something extra**. My goal with any link blog post is that if you read both my post and the source material you'll have an enhanced experience over if you read just the source material itself.

	+ Ideally I'd like you to take something useful away even if you don't follow the link itself. This can be a slightly tricky balance: I don't wont to steal attention from the authors and plagiarize their message. Generally I'll try to find some key idea that's worth emphasizing. Slightly cynically, I may try to capture that idea as backup against the original source vanishing from the internet. Link rot is real!
	+ My most basic version of this is trying to provide context as to why I think this particular thing is worth reading \- especially important for longer content. A good recent example is my post about Anthropic's [Building effective agents](https://simonwillison.net/2024/Dec/20/building-effective-agents/) essay the other day.
	+ I might tie it together to other similar concepts, including things I've written about in the past, for example linking [Prompt caching with Claude](https://simonwillison.net/2024/Aug/14/prompt-caching-with-claude/) to my coverage of [Context caching for Google Gemini](https://simonwillison.net/2024/May/14/context-caching-for-google-gemini/).
	+ If part of the material is a video, I might **quote a snippet of the transcript** (often extracted using MacWhisper) like I did in [this post about Anthropic's Clio](https://simonwillison.net/2024/Dec/12/clio/).
	+ A lot of stuff I link to involves programming. I'll often include a **direct link to relevant code**, using the GitHub feature where I can link to a snippet as\-of a particular commit. One example is the [fetch\-rss.py link in this post](https://simonwillison.net/2024/Oct/5/uv-with-github-actions-to-run-an-rss-to-readme-project/).
* I'm liberal with **quotations**. Finding and quoting a paragraph that captures the key theme of a post is a very quick and effective way to summarize it and help people decide if it's worth reading the whole thing. My post on [François Chollet's o3 ARC\-AGI analysis](https://simonwillison.net/2024/Dec/20/openai-o3-breakthrough/) is an example of that.
* If the original author reads my post, I want them to **feel good about it**. I know from my own experience that often when you publish something online the silence can be deafening. Knowing that someone else read, appreciated, understood and then shared your work can be very pleasant.
* A slightly self\-involved concern I have is that I like to **prove that I've read it**. This is more for me than for anyone else: I don't like to recommend something if I've not read that thing myself, and sticking in a detail that shows I read past the first paragraph helps keep me honest about that.
* I've started leaning more into **screenshots** and even short video or audio clips. A screenshot can be considered a visual quotation \- I'll sometimes snap these from interesting frames in a YouTube video or live demo associated with the content I'm linking to. I used a screenshot of the Clay debugger in [my post about Clay](https://simonwillison.net/2024/Dec/21/clay-ui-library/).
* There are a lot of great link blogs out there, but the one that has influenced me the most in how I approach my own is John Gruber's [Daring Fireball](https://daringfireball.net/). I really like the way he mixes commentary, quotations and value\-added relevant information.

#### The technology

The technology behind my link blog is probably the least interesting thing about it. It's part of my [simonwillisonblog](https://github.com/simonw/simonwillisonblog) Django application \- the main model is called [Blogmark](https://github.com/simonw/simonwillisonblog/blob/c781a1a42ab0a0237f75c7790f069bacc2d70d3f/blog/models.py#L328-L337) and it inherits from a [BaseModel](https://github.com/simonw/simonwillisonblog/blob/c781a1a42ab0a0237f75c7790f069bacc2d70d3f/blog/models.py#L172-L203) defining things like tags and draft modes that are shared across my other types of content (entries and quotations).

I use the Django Admin to create and edit entries, [configured here](https://github.com/simonw/simonwillisonblog/blob/c781a1a42ab0a0237f75c7790f069bacc2d70d3f/blog/admin.py#L73-L76).

The most cumbersome part of link blogging for me right now is images. I convert these into smaller JPEGs using a [tiny custom tool](https://tools.simonwillison.net/image-resize-quality) I built ([with Claude](https://gist.github.com/simonw/58a06a8028515999e5949a0166cd4c4f)), then upload them to my `static.simonwillison.net` S3 bucket using Transmit and drop them into my posts using a Markdown image reference. I generate a first draft of the alt text using a Claude Project with [these custom instructions](https://gist.github.com/simonw/1fa7e4e3dcb18fdeca2b3d6ac2c6c628), then usually make a few changes before including that in the markup. At some point I'll wire together a UI that makes this process a little smoother.

That `static.simonwillison.net` buckt is then served via Cloudflare's free tier, which means I effectively never have to think about the cost of serving up those image files.

I wrote up a TIL about [Building a blog in Django](https://til.simonwillison.net/django/building-a-blog-in-django) a while ago which describes a similar setup to the one I'm using for my link blog, including how the RSS feed works (using [Django's syndication framework](https://docs.djangoproject.com/en/4.2/ref/contrib/syndication/)).

The most technically interesting component is my [search feature](https://simonwillison.net/search/?type=blogmark). I wrote about how that works in [Implementing faceted search with Django and PostgreSQL](https://simonwillison.net/2017/Oct/5/django-postgresql-faceted-search/) \- the most recent code for that can be found in [blog/search.py](https://github.com/simonw/simonwillisonblog/blob/main/blog/search.py) on GitHub.

I also send out an approximately weekly [email newsletter](https://simonw.substack.com/) version of my blog, for people who want to subscribe in their inbox. This is a straight copy of content from my blog \- Substack doesn't have an API for this but their editor does accept copy and paste, so I have a delightful digital duct tape solution for assembling the newsletter which I described in [Semi\-automating a Substack newsletter with an Observable notebook](https://simonwillison.net/2023/Apr/4/substack-observable/).

#### More people should do this

I posted this on Bluesky [last night](https://bsky.app/profile/simonwillison.net/post/3ldu6jywnos2j):

> I wish people would post more links to interesting things
> 
> I feel like Twitter and LinkedIn and Instagram and TikTok have pushed a lot of people out of the habit of doing that, by penalizing shared links in the various "algorithms"
> 
> Bluesky doesn't have that misfeature, thankfully!
> 
> (In my ideal world everyone would get their own link blog too, but sharing links on Bluesky and Mastodon is almost as good)

Sharing interesting links with commentary is a low effort, high value way to contribute to internet life at large.

---

**Quote** 2024\-12\-20

> *50% of cybersecurity is endlessly explaining that consumer VPNs don’t address any real cybersecurity issues. They are basically only useful for bypassing geofences and making money telling people they need to buy a VPN.   
>   
> Man\-in\-the\-middle attacks on Public WiFi networks haven't been a realistic threat in a decade. Almost all websites use encryption by default, and anything of value uses HSTS to prevent attackers from downgrading / disabling encryption. It's a non issue.*

[Marcus Hutchins](https://bsky.app/profile/malwaretech.com/post/3ldpfzxdyqs2d)

---

**Link** 2024\-12\-20 [Building effective agents](https://www.anthropic.com/research/building-effective-agents):

My principal complaint about the term "agents" is that while it has many different potential definitions most of the people who use it seem to assume that everyone else shares and understands the definition that they have chosen to use.

This outstanding piece by Erik Schluntz and Barry Zhang at Anthropic bucks that trend from the start, providing a clear definition that they then use throughout.

They discuss "agentic systems" as a parent term, then define a distinction between "workflows" \- systems where multiple LLMs are orchestrated together using pre\-defined patterns \- and "agents", where the LLMs "dynamically direct their own processes and tool usage". This second definition is later expanded with this delightfully clear description:

> Agents begin their work with either a command from, or interactive discussion with, the human user. Once the task is clear, agents plan and operate independently, potentially returning to the human for further information or judgement. During execution, it's crucial for the agents to gain “ground truth” from the environment at each step (such as tool call results or code execution) to assess its progress. Agents can then pause for human feedback at checkpoints or when encountering blockers. The task often terminates upon completion, but it’s also common to include stopping conditions (such as a maximum number of iterations) to maintain control.

That's a definition I can live with!

They also introduce a term that I *really* like: **the augmented LLM**. This is an LLM with augmentations such as tools \- I've seen people use the term "agents" just for this, which never felt right to me.

The rest of the article is the clearest practical guide to building systems that combine multiple LLM calls that I've seen anywhere.

Most of the focus is actually on workflows. They describe five different patterns for workflows in detail:

* Prompt chaining, e.g. generating a document and then translating it to a separate language as a second LLM call
* Routing, where an initial LLM call decides which model or call should be used next (sending easy tasks to Haiku and harder tasks to Sonnet, for example)
* Parallelization, where a task is broken up and run in parallel (e.g. image\-to\-text on multiple document pages at once) or processed by some kind of voting mechanism
* Orchestrator\-workers, where a orchestrator triggers multiple LLM calls that are then synthesized together, for example running searches against multiple sources and combining the results
* Evaluator\-optimizer, where one model checks the work of another in a loop

These patterns all make sense to me, and giving them clear names makes them easier to reason about.

When should you upgrade from basic prompting to workflows and then to full agents? The authors provide this sensible warning:

> When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all.

But assuming you do need to go beyond what can be achieved even with the aforementioned workflow patterns, their model for agents may be a useful fit:

> Agents can be used for open\-ended problems where it’s difficult or impossible to predict the required number of steps, and where you can’t hardcode a fixed path. The LLM will potentially operate for many turns, and you must have some level of trust in its decision\-making. Agents' autonomy makes them ideal for scaling tasks in trusted environments.
> 
> The autonomous nature of agents means higher costs, and the potential for compounding errors. We recommend extensive testing in sandboxed environments, along with the appropriate guardrails

They also warn against investing in complex agent frameworks before you've exhausted your options using direct API access and simple code.

The article is accompanied by a brand new set of [cookbook recipes](https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents) illustrating all five of the workflow patterns. The [Evaluator\-Optimizer Workflow](https://github.com/anthropics/anthropic-cookbook/blob/main/patterns/agents/evaluator_optimizer.ipynb) example is particularly fun, setting up a code generating prompt and an code reviewing evaluator prompt and having them loop until the evaluator is happy with the result.

---

**Quote** 2024\-12\-20

> *OpenAI's new o3 system \- trained on the ARC\-AGI\-1 Public Training set \- has scored a breakthrough 75\.7% on the Semi\-Private Evaluation set at our stated public leaderboard $10k compute limit. A high\-compute (172x) o3 configuration scored 87\.5%.   
>   
> This is a surprising and important step\-function increase in AI capabilities, showing novel task adaptation ability never seen before in the GPT\-family models. For context, ARC\-AGI\-1 took 4 years to go from 0% with GPT\-3 in 2020 to 5% in 2024 with GPT\-4o. All intuition about AI capabilities will need to get updated for o3\.*

[François Chollet](https://arcprize.org/blog/oai-o3-pub-breakthrough)

---

**Link** 2024\-12\-20 [OpenAI o3 breakthrough high score on ARC\-AGI\-PUB](https://arcprize.org/blog/oai-o3-pub-breakthrough):

François Chollet is the co\-founder of the ARC Prize and had advanced access to today's o3 results. His article here is the most insightful coverage I've seen of o3, going beyond just the benchmark results to talk about what this all means for the field in general.

One fascinating detail: it cost $6,677 to run o3 in "high efficiency" mode against the 400 public ARC\-AGI puzzles for a score of 82\.8%, and an undisclosed amount of money to run the "low efficiency" mode model to score 91\.5%. A note says:

> o3 high\-compute costs not available as pricing and feature availability is still TBD. The amount of compute was roughly 172x the low\-compute configuration.

So we can get a ballpark estimate here in that 172 \* $6,677 \= $1,148,444!

Here's how François explains the likely mechanisms behind o3, which reminds me of how a brute\-force chess computer might work.

> For now, we can only speculate about the exact specifics of how o3 works. But o3's core mechanism appears to be natural language program search and execution within token space – at test time, the model searches over the space of possible Chains of Thought (CoTs) describing the steps required to solve the task, in a fashion perhaps not too dissimilar to AlphaZero\-style Monte\-Carlo tree search. In the case of o3, the search is presumably guided by some kind of evaluator model. To note, Demis Hassabis hinted back in a June 2023 interview that DeepMind had been researching this very idea – this line of work has been a long time coming.
> 
> So while single\-generation LLMs struggle with novelty, o3 overcomes this by generating and executing its own programs, where the program itself (the CoT) becomes the artifact of knowledge recombination. Although this is not the only viable approach to test\-time knowledge recombination (you could also do test\-time training, or search in latent space), it represents the current state\-of\-the\-art as per these new ARC\-AGI numbers.
> 
> Effectively, o3 represents a form of deep learning\-guided program search. The model does test\-time search over a space of "programs" (in this case, natural language programs – the space of CoTs that describe the steps to solve the task at hand), guided by a deep learning prior (the base LLM). The reason why solving a single ARC\-AGI task can end up taking up tens of millions of tokens and cost thousands of dollars is because this search process has to explore an enormous number of paths through program space – including backtracking.

I'm not sure if o3 (and o1 and similar models) even qualifies as an LLM any more \- there's clearly a whole lot more going on here than just next\-token prediction.

On the question of if o3 should qualify as AGI (whatever that might mean):

> Passing ARC\-AGI does not equate to achieving AGI, and, as a matter of fact, I don't think o3 is AGI yet. o3 still fails on some very easy tasks, indicating fundamental differences with human intelligence.
> 
> Furthermore, early data points suggest that the upcoming ARC\-AGI\-2 benchmark will still pose a significant challenge to o3, potentially reducing its score to under 30% even at high compute (while a smart human would still be able to score over 95% with no training).

The post finishes with examples of the puzzles that o3 *didn't* manage to solve, including this one which reassured me that I can still solve at least some puzzles that couldn't be handled with thousands of dollars of GPU compute!

[![A puzzle with colored squares, where drawing a line between the single blue squares and turning any intersected rectangles blue is clearly the solution.](https://substackcdn.com/image/fetch/$s_!i17s!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fec711211-5a14-4dde-97fb-eabe77bb3212_1600x891.png "A puzzle with colored squares, where drawing a line between the single blue squares and turning any intersected rectangles blue is clearly the solution.")](https://substackcdn.com/image/fetch/$s_!i17s!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fec711211-5a14-4dde-97fb-eabe77bb3212_1600x891.png)

---

**Link** 2024\-12\-21 [Clay UI library](https://www.nicbarker.com/clay):

Fascinating project by Nic Barker, who describes Clay like this:

> Clay is a flex\-box style UI auto layout library in C, with declarative syntax and microsecond performance.

His [intro video](https://www.youtube.com/watch?v=DYWTw19_8r4) to the library is outstanding: I learned a ton about how UI layout works from this, and the animated visual explanations are clear, tasteful and really helped land the different concepts:

Clay is a C library delivered in a single \~2000 line [clay.h](https://github.com/nicbarker/clay/blob/main/clay.h) dependency\-free header file. It only handles layout calculations: if you want to render the result you need to add an additional rendering layer.

In a fascinating demo of the library, the [Clay site itself](https://www.nicbarker.com/clay) is rendered using Clay C compiled to WebAssembly! You can even switch between the default HTML renderer and an alternative based on Canvas.

This isn't necessarily a great idea: because the layout is entirely handled using `<div>` elements positioned using `transform: translate(0px, 70px)` style CSS attempting to select text across multiple boxes behaves strangely, and it's not clear to me what the accessibility implications are.

**Update**: [Matt Campbell](https://toot.cafe/@matt/113693374074675126):

> The accessibility implications are as serious as you might guess. The links aren't properly labeled, there's no semantic markup such as headings, and since there's a div for every line, continuous reading with a screen reader is choppy, that is, it pauses at the end of every physical line.

It does make for a very compelling demo of what Clay is capable of though, especially when you resize your browser window and the page layout is recalculated in real\-time via the Clay WebAssembly bridge.

You can hit "D" on the website and open up a custom Clay debugger showing the hierarchy of layout elements on the page:

[![Clay website on the left, on the right is a panel showing a tree of UI layout elements, one has been selected and is showing details in a box at the bottom of the panel: Bounding Box: { x: 278, y: 13, width: 101, height: 24}, Layout Direction: LEFT_TO_RIGHT, Sizing: width: FITQ, height: FITQ, Padding: {x:8,uy:0}](https://substackcdn.com/image/fetch/$s_!tPhc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0ad7f26c-8e7e-4349-9fca-c5cf9cbef825_2222x1432.jpeg "Clay website on the left, on the right is a panel showing a tree of UI layout elements, one has been selected and is showing details in a box at the bottom of the panel: Bounding Box: { x: 278, y: 13, width: 101, height: 24}, Layout Direction: LEFT_TO_RIGHT, Sizing: width: FITQ, height: FITQ, Padding: {x:8,uy:0}")](https://substackcdn.com/image/fetch/$s_!tPhc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0ad7f26c-8e7e-4349-9fca-c5cf9cbef825_2222x1432.jpeg)

This also means that the entire page is defined using C code! Given that, I find the code itself [surprisingly readable](https://github.com/nicbarker/clay/blob/35d72e5fba6872be48d15ed9d84269a86cd72b4e/examples/clay-official-website/main.c#L124-L139)

```
void DeclarativeSyntaxPageDesktop() {
  CLAY(CLAY_ID("SyntaxPageDesktop"), CLAY_LAYOUT({ .sizing = { CLAY_SIZING_GROW(), CLAY_SIZING_FIT({ .min = windowHeight - 50 }) }, .childAlignment = {0, CLAY_ALIGN_Y_CENTER}, .padding = {.x = 50} })) {
    CLAY(CLAY_ID("SyntaxPage"), CLAY_LAYOUT({ .sizing = { CLAY_SIZING_GROW(), CLAY_SIZING_GROW() }, .childAlignment = { 0, CLAY_ALIGN_Y_CENTER }, .padding = { 32, 32 }, .childGap = 32 }), CLAY_BORDER({ .left = { 2, COLOR_RED }, .right = { 2, COLOR_RED } })) {
      CLAY(CLAY_ID("SyntaxPageLeftText"), CLAY_LAYOUT({ .sizing = { CLAY_SIZING_PERCENT(0.5) }, .layoutDirection = CLAY_TOP_TO_BOTTOM, .childGap = 8 })) {
        CLAY_TEXT(CLAY_STRING("Declarative Syntax"), CLAY_TEXT_CONFIG({ .fontSize = 52, .fontId = FONT_ID_TITLE_56, .textColor = COLOR_RED }));
        CLAY(CLAY_ID("SyntaxSpacer"), CLAY_LAYOUT({ .sizing = { CLAY_SIZING_GROW({ .max = 16 }) } })) {}
        CLAY_TEXT(CLAY_STRING("Flexible and readable declarative syntax with nested UI element hierarchies."), CLAY_TEXT_CONFIG({ .fontSize = 28, .fontId = FONT_ID_BODY_36, .textColor = COLOR_RED }));
        CLAY_TEXT(CLAY_STRING("Mix elements with standard C code like loops, conditionals and functions."), CLAY_TEXT_CONFIG({ .fontSize = 28, .fontId = FONT_ID_BODY_36, .textColor = COLOR_RED }));
        CLAY_TEXT(CLAY_STRING("Create your own library of re-usable components from UI primitives like text, images and rectangles."), CLAY_TEXT_CONFIG({ .fontSize = 28, .fontId = FONT_ID_BODY_36, .textColor = COLOR_RED }));
      }
      CLAY(CLAY_ID("SyntaxPageRightImage"), CLAY_LAYOUT({ .sizing = { CLAY_SIZING_PERCENT(0.50) }, .childAlignment = {.x = CLAY_ALIGN_X_CENTER} })) {
        CLAY(CLAY_ID("SyntaxPageRightImageInner"), CLAY_LAYOUT({ .sizing = { CLAY_SIZING_GROW({ .max = 568 }) } }), CLAY_IMAGE({ .sourceDimensions = {1136, 1194}, .sourceURL = CLAY_STRING("/clay/images/declarative.png") })) {}
      }
    }
  }
}
```

I'm not ready to ditch HTML and CSS for writing my web pages in C compiled to WebAssembly just yet, but as an exercise in understanding layout engines (and a potential tool for building non\-web interfaces in the future) this is a really interesting project to dig into.

To clarify here: I don't think the web layout / WebAssembly thing is the key idea behind Clay at all \- I think it's a neat demo of the library, but it's not what Clay is *for*. It's certainly an interesting way to provide a demo of a layout library!

Nic [confirms](https://bsky.app/profile/nicbarker.com/post/3ldu44rxyx22h):

> You totally nailed it, the fact that you can compile to wasm and run in HTML stemmed entirely from a “wouldn’t it be cool if…” It was designed for my C projects first and foremost!

---