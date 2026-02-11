# Vibe engineering

*Plus news from OpenAI DevDay, GPT-5 Pro, gpt-image-1-mini, and Python 3.14*

Published: 2025-10-08
Source: https://simonw.substack.com/p/vibe-engineering

---

In this newsletter:

* Vibe engineering
* OpenAI DevDay 2025 live blog
* GPT\-5 Pro and gpt\-image\-1\-mini
* Python 3\.14

Plus 4 links and 2 quotations and 2 notes

### [Vibe engineering](https://simonwillison.net/2025/Oct/7/vibe-engineering/) \- 2025\-10\-07

I feel like **vibe coding** is [pretty well established now](https://simonwillison.net/2025/Mar/19/vibe-coding/) as covering the fast, loose and irresponsible way of building software with AI \- entirely prompt\-driven, and with no attention paid to how the code actually works. This leaves us with a terminology gap: what should we call the other end of the spectrum, where seasoned professionals accelerate their work with LLMs while staying proudly and confidently accountable for the software they produce?

I propose we call this **vibe engineering**, with my tongue only partially in my cheek.

One of the lesser spoken truths of working productively with LLMs as a software engineer on non\-toy\-projects is that it’s *difficult*. There’s a lot of depth to understanding how to use the tools, there are plenty of traps to avoid, and the pace at which they can churn out working code raises the bar for what the human participant can and should be contributing.

The rise of **coding agents** \- tools like [Claude Code](https://www.claude.com/product/claude-code) (released February 2025\), OpenAI’s [Codex CLI](https://github.com/openai/codex) (April) and [Gemini CLI](https://github.com/google-gemini/gemini-cli) (June) that can iterate on code, actively testing and modifying it until it achieves a specified goal, has dramatically increased the usefulness of LLMs for real\-world coding problems.

I’m increasingly hearing from experienced, credible software engineers who are running multiple copies of agents at once, tackling several problems in parallel and expanding the scope of what they can take on. I was skeptical of this at first but [I’ve started running multiple agents myself now](https://simonwillison.net/2025/Oct/5/parallel-coding-agents/) and it’s surprisingly effective, if mentally exhausting!

This feels very different from classic vibe coding, where I outsource a simple, low\-stakes task to an LLM and accept the result if it appears to work. Most of my [tools.simonwillison.net](https://simonwillison.net/) collection ([previously](https://simonwillison.net/2025/Sep/4/highlighted-tools/)) were built like that. Iterating with coding agents to produce production\-quality code that I’m confident I can maintain in the future feels like a different process entirely.

It’s also become clear to me that LLMs actively reward existing top tier software engineering practices:

* **Automated testing**. If your project has a robust, comprehensive and stable test suite agentic coding tools can *fly* with it. Without tests? Your agent might claim something works without having actually tested it at all, plus any new change could break an unrelated feature without you realizing it. Test\-first development is particularly effective with agents that can iterate in a loop.
* **Planning in advance**. Sitting down to hack something together goes much better if you start with a high level plan. Working with an agent makes this even more important \- you can iterate on the plan first, then hand it off to the agent to write the code.
* **Comprehensive documentation**. Just like human programmers, an LLM can only keep a subset of the codebase in its context at once. Being able to feed in relevant documentation lets it use APIs from other areas without reading the code first. Write good documentation first and the model may be able to build the matching implementation from that input alone.
* **Good version control habits**. Being able to undo mistakes and understand when and how something was changed is even more important when a coding agent might have made the changes. LLMs are also fiercely competent at Git \- they can navigate the history themselves to track down the origin of bugs, and they’re better than most developers at using [git bisect](https://til.simonwillison.net/git/git-bisect). Use that to your advantage.
* Having **effective automation** in place. Continuous integration, automated formatting and linting, continuous deployment to a preview environment \- all things that agentic coding tools can benefit from too. LLMs make writing quick automation scripts easier as well, which can help them then repeat tasks accurately and consistently next time.
* A **culture of code review**. This one explains itself. If you’re fast and productive at code review you’re going to have a much better time working with LLMs than if you’d rather write code yourself than review the same thing written by someone (or something) else.
* A **very weird form of management**. Getting good results out of a coding agent feels uncomfortably close to getting good results out of a human collaborator. You need to provide clear instructions, ensure they have the necessary context and provide actionable feedback on what they produce. It’s a *lot* easier than working with actual people because you don’t have to worry about offending or discouraging them \- but any existing management experience you have will prove surprisingly useful.
* Really good **manual QA (quality assurance)**. Beyond automated tests, you need to be really good at manually testing software, including predicting and digging into edge\-cases.
* Strong **research skills**. There are dozens of ways to solve any given coding problem. Figuring out the best options and proving an approach has always been important, and remains a blocker on unleashing an agent to write the actual code.
* The ability to **ship to a preview environment**. If an agent builds a feature, having a way to safely preview that feature (without deploying it straight to production) makes reviews much more productive and greatly reduces the risk of shipping something broken.
* An instinct for **what can be outsourced** to AI and what you need to manually handle yourself. This is constantly evolving as the models and tools become more effective. A big part of working effectively with LLMs is maintaining a strong intuition for when they can best be applied.
* An updated **sense of estimation**. Estimating how long a project will take has always been one of the hardest but most important parts of being a senior engineer, especially in organizations where budget and strategy decisions are made based on those estimates. AI\-assisted coding makes this *even harder* \- things that used to take a long time are much faster, but estimations now depend on new factors which we’re all still trying to figure out.

If you’re going to really exploit the capabilities of these new tools, you need to be operating *at the top of your game*. You’re not just responsible for writing the code \- you’re researching approaches, deciding on high\-level architecture, writing specifications, defining success criteria, [designing agentic loops](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/), planning QA, managing a growing army of weird digital interns who will absolutely cheat if you give them a chance, and spending *so much time on code review*.

Almost all of these are characteristics of senior software engineers already!

AI tools **amplify existing expertise**. The more skills and experience you have as a software engineer the faster and better the results you can get from working with LLMs and coding agents.

#### “Vibe engineering”, really?

Is this a stupid name? Yeah, probably. “Vibes” as a concept in AI feels a little tired at this point. “Vibe coding” itself is used by a lot of developers in a dismissive way. I’m ready to reclaim vibes for something more constructive.

I’ve never really liked the artificial distinction between “coders” and “engineers” \- that’s always smelled to me a bit like gatekeeping. But in this case a bit of gatekeeping is exactly what we need!

**Vibe engineering** establishes a clear distinction from vibe coding. It signals that this is a different, harder and more sophisticated way of working with AI tools to build production software.

I like that this is cheeky and likely to be controversial. This whole space is still absurd in all sorts of different ways. We shouldn’t take ourselves too seriously while we figure out the most productive ways to apply these new tools.

I’ve tried in the past to get terms like **[AI\-assisted programming](https://simonwillison.net/tags/ai-assisted-programming/)** to stick, with approximately zero success. May as well try rubbing some vibes on it and see what happens.

I also really like the clear mismatch between “vibes” and “engineering”. It makes the combined term self\-contradictory in a way that I find mischievous and (hopefully) sticky.

*This post was discussed [on Hacker News](https://news.ycombinator.com/item?id=45503867) and [on lobste.rs](https://lobste.rs/s/xbxhvq/vibe_engineering).*

---

### [OpenAI DevDay 2025 live blog](https://simonwillison.net/2025/Oct/6/openai-devday-live-blog/) \- 2025\-10\-06

I spent Monday at [OpenAI DevDay](https://devday.openai.com/2025) in Fort Mason, San Francisco. As [I did last year](https://simonwillison.net/2024/Oct/1/openai-devday-2024-live-blog/), I live blogged the announcements from the kenote. Unlike last year, this year [there was a livestream](https://www.youtube.com/live/hS1YqcewH0c).

*Disclosure: OpenAI provides me with a free ticket and reserved me a seat in the press/influencer section for the keynote.*

You can read [the liveblog on my site](https://simonwillison.net/2025/Oct/6/openai-devday-live-blog/). I joined Alex Volkov for a ten minute debrief directly after the keynote to discuss highlights, that segment is available [on the ThursdAI YouTube channel](https://www.youtube.com/live/M6paPiur4yQ?si=XXKkIKY2J71QCJKW&t=7551).

---

**Note** [2025\-10\-06](https://simonwillison.net/2025/Oct/6/bad-bots/)

Two of my public Datasette instances \- for [my TILs](https://til.simonwillison.net/) and my [blog’s backup mirror](https://datasette.simonwillison.net/) \- were getting *hammered* with misbehaving bot traffic today. Scaling them up to more Fly instances got them running again but I’d rather not pay extra just so bots can crawl me harder.

The log files showed the main problem was [facets](https://docs.datasette.io/en/stable/facets.html): Datasette provides these by default on the table page, but they can be combined in ways that keep poorly written crawlers busy visiting different variants of the same page over and over again.

So I turned those off. I’m now running those instances with `--setting allow_facet off` ([described here](https://docs.datasette.io/en/stable/settings.html#allow-facet)), and my logs are full of lines that look like this. The “400 Bad Request” means a bot was blocked from loading the page:

`GET /simonwillisonblog/blog_entry?_facet_date=created&_facet=series_id&_facet_size=max&_facet=extra_head_html&_sort=is_draft&created__date=2012-01-30 HTTP/1.1” 400 Bad Request`

---

**quote** 2025\-10\-06

> *I believed that giving users such a simple way to navigate the internet would unlock creativity and collaboration on a global scale. If you could put anything on it, then after a while, it would have everything on it.   
>   
> But for the web to have everything on it, everyone had to be able to use it, and want to do so. This was already asking a lot. I couldn’t also ask that they pay for each search or upload they made. In order to succeed, therefore, it would have to be free. That’s why, in 1993, I convinced my Cern managers to donate the intellectual property of the world wide web, putting it into the public domain. We gave the web away to everyone.*

[Tim Berners\-Lee](https://www.theguardian.com/technology/2025/sep/28/why-i-gave-the-world-wide-web-away-for-free), Why I gave the world wide web away for free

---

**Link** 2025\-10\-06 [GPT\-5 pro](https://platform.openai.com/docs/models/gpt-5-pro):

Here’s OpenAI’s model documentation for their GPT\-5 pro model, released to their API today at their DevDay event.

It has similar base characteristics to [GPT\-5](https://platform.openai.com/docs/models/gpt-5): both share a September 30, 2024 knowledge cutoff and 400,000 context limit.

GPT\-5 pro has maximum output tokens 272,000 max, an increase from 128,000 for GPT\-5\.

> As our most advanced reasoning model, GPT\-5 pro defaults to (and only supports) `reasoning.effort: high`

It’s only available via OpenAI’s Responses API. My [LLM](https://llm.datasette.io/) tool doesn’t support that in core yet, but the [llm\-openai\-plugin](https://github.com/simonw/llm-openai-plugin) plugin does. I released [llm\-openai\-plugin 0\.7](https://github.com/simonw/llm-openai-plugin/releases/tag/0.7) adding support for the new model, then ran this:

```
llm install -U llm-openai-plugin
llm -m openai/gpt-5-pro “Generate an SVG of a pelican riding a bicycle”
```

It’s very, very slow. The model took 6 minutes 8 seconds to respond and charged me for 16 input and 9,205 output tokens. At $15/million input and $120/million output this pelican [cost me $1\.10](https://www.llm-prices.com/#it=16&ot=9205&ic=15&oc=120&sb=output&sd=descending)!

[![It's obviously a pelican riding a bicycle. Half the spokes are missing on each wheel and the pelican is a bit squat looking.](https://substackcdn.com/image/fetch/$s_!z5uG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4e56a540-1957-41e3-a3e7-bc3287b64bfa_800x533.png "It's obviously a pelican riding a bicycle. Half the spokes are missing on each wheel and the pelican is a bit squat looking.")](https://substackcdn.com/image/fetch/$s_!z5uG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4e56a540-1957-41e3-a3e7-bc3287b64bfa_800x533.png)

Here’s [the full transcript](https://gist.github.com/simonw/9a06ab36f486f31401fec1fc104a8ce5). It looks visually pretty simpler to the much, much cheaper result I [got from GPT\-5](https://simonwillison.net/2025/Aug/7/gpt-5/#and-some-svgs-of-pelicans).

---

**Link** 2025\-10\-06 [gpt\-image\-1\-mini](https://platform.openai.com/docs/models/gpt-image-1-mini):

OpenAI released a new image model today: `gpt-image-1-mini`, which they describe as “A smaller image generation model that’s 80% less expensive than the large model.”

They released it very quietly \- I didn’t hear about this in the DevDay keynote but I later spotted it on the [DevDay 2025 announcements page](https://openai.com/devday/).

It wasn’t instantly obvious to me how to use this via their API. I ended up vibe coding a Python CLI tool for it so I could try it out.

I dumped the [plain text diff version](https://github.com/openai/openai-python/commit/9ada2c74f3f5865a2bfb19afce885cc98ad6a4b3.diff) of the commit to the OpenAI Python library titled [feat(api): dev day 2025 launches](https://github.com/openai/openai-python/commit/9ada2c74f3f5865a2bfb19afce885cc98ad6a4b3) into ChatGPT GPT\-5 Thinking and worked with it to figure out how to use the new image model and build a script for it. Here’s [the transcript](https://chatgpt.com/share/68e44023-7fc4-8006-8991-3be661799c9f) and the [the openai\_image.py script](https://github.com/simonw/tools/blob/main/python/openai_image.py) it wrote.

I had it add inline script dependencies, so you can run it with `uv` like this:

```
export OPENAI_API_KEY=”$(llm keys get openai)”
uv run https://tools.simonwillison.net/python/openai_image.py “A pelican riding a bicycle”
```

It picked this illustration style without me specifying it:

[![A nice illustration of a pelican riding a bicycle, both pelican and bicycle are exactly as you would hope. Looks sketched, maybe colored pencils? The pelican's two legs are on the pedals but it also has a weird sort of paw on an arm on the handlebars.](https://substackcdn.com/image/fetch/$s_!ExDl!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa258ebb2-9cf8-4f3d-8ce3-96f510d90df6_1024x1536.jpeg "A nice illustration of a pelican riding a bicycle, both pelican and bicycle are exactly as you would hope. Looks sketched, maybe colored pencils? The pelican's two legs are on the pedals but it also has a weird sort of paw on an arm on the handlebars.")](https://substackcdn.com/image/fetch/$s_!ExDl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa258ebb2-9cf8-4f3d-8ce3-96f510d90df6_1024x1536.jpeg)

(This is a very different test from my normal “Generate an SVG of a pelican riding a bicycle” since it’s using a dedicated image generator, not having a text\-based model try to generate SVG code.)

My tool accepts a prompt, and optionally a filename (if you don’t provide one it saves to a filename like `/tmp/image-621b29.png`).

It also accepts options for model and dimensions and output quality \- the `--help` output lists those, you can [see that here](https://tools.simonwillison.net/python/#openai_imagepy).

OpenAI’s pricing is a little confusing. The [model page](https://platform.openai.com/docs/models/gpt-image-1-mini) claims low quality images should cost around half a cent and medium quality around a cent and a half. It also lists an image token price of $8/million tokens. It turns out there’s a default “high” quality setting \- most of the images I’ve generated have reported between 4,000 and 6,000 output tokens, which costs between [3\.2](https://www.llm-prices.com/#ot=4000&oc=8) and [4\.8 cents](https://www.llm-prices.com/#ot=6000&oc=8).

One last demo, this time using `--quality low`:

```
 uv run https://tools.simonwillison.net/python/openai_image.py \
  ‘racoon eating cheese wearing a top hat, realistic photo’ \
  /tmp/racoon-hat-photo.jpg \
  --size 1024x1024 \
  --output-format jpeg \
  --quality low
```

This saved the following:

[![It's a square photo of a raccoon eating cheese and wearing a top hat. It looks pretty realistic.](https://substackcdn.com/image/fetch/$s_!uxrT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9e670287-92af-4c08-adf2-f3147b6681f2_1024x1024.jpeg "It's a square photo of a raccoon eating cheese and wearing a top hat. It looks pretty realistic.")](https://substackcdn.com/image/fetch/$s_!uxrT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9e670287-92af-4c08-adf2-f3147b6681f2_1024x1024.jpeg)

And reported this to standard error:

```
{
  “background”: “opaque”,
  “created”: 1759790912,
  “generation_time_in_s”: 20.87331541599997,
  “output_format”: “jpeg”,
  “quality”: “low”,
  “size”: “1024x1024”,
  “usage”: {
    “input_tokens”: 17,
    “input_tokens_details”: {
      “image_tokens”: 0,
      “text_tokens”: 17
    },
    “output_tokens”: 272,
    “total_tokens”: 289
  }
}
```

This took 21s, but I’m on an unreliable conference WiFi connection so I don’t trust that measurement very much.

272 output tokens \= [0\.2 cents](https://www.llm-prices.com/#ot=272&oc=8) so this is much closer to the expected pricing from the model page.

---

**Note** [2025\-10\-06](https://simonwillison.net/2025/Oct/6/work-independently/)

I’ve settled on agents as meaning [“LLMs calling tools in a loop to achieve a goal”](https://simonwillison.net/2025/Sep/18/agents/) but OpenAI continue to muddy the waters with much more vague definitions. Swyx [spotted this one](https://twitter.com/swyx/status/1975335082048246159) in the press pack OpenAI sent out for their DevDay announcements today:

> **How does OpenAl define an “agent”?** An Al agent is a system that can do work independently on behalf of the user.

Adding this one [to my collection](https://simonwillison.net/tags/agent-definitions/).

---

**Link** 2025\-10\-06 [Deloitte to pay money back to Albanese government after using AI in $440,000 report](https://www.theguardian.com/australia-news/2025/oct/06/deloitte-to-pay-money-back-to-albanese-government-after-using-ai-in-440000-report):

Ouch:

> Deloitte will provide a partial refund to the federal government over a $440,000 report that contained several errors, after admitting it used generative artificial intelligence to help produce it.

(I was initially confused by the “Albanese government” reference in the headline since this is a story about the Australian federal government. That’s because the current Australia Prime Minister is Anthony Albanese.)

Here’s [the page for the report](https://www.dewr.gov.au/assuring-integrity-targeted-compliance-framework/resources/targeted-compliance-framework-assurance-review-final-report). The PDF now includes this note:

> This Report was updated on 26 September 2025 and replaces the Report dated 4 July 2025\. The Report has been updated to correct those citations and reference list entries which contained errors in the previously issued version, to amend the summary of the Amato proceeding which contained errors, and to make revisions to improve clarity and readability. The updates made in no way impact or affect the substantive content, findings and recommendations in the Report.

---

**quote** 2025\-10\-07

> *For quite some I wanted to write a small static image gallery so I can share my pictures with friends and family. Of course there are a gazillion tools like this, but, well, sometimes I just want to roll my own. \[...]   
>   
> I used the old, well tested technique I call **brain coding**, where you start with an empty vim buffer and type some code (Perl, HTML, CSS) until you’re happy with the result. It helps to think a bit (aka use your brain) during this process.*

[Thomas Klausner](https://domm.plix.at/perl/2025_10_braincoded_static_image_gallery.html), coining “brain coding”

---

**Link** 2025\-10\-08 [Python 3\.14](https://www.python.org/downloads/release/python-3140/):

This year’s major Python version, Python 3\.14, just made its first stable release!

As usual the [what’s new in Python 3\.14](https://docs.python.org/3.14/whatsnew/3.14.html) document is the best place to get familiar with the new release:

> The biggest changes include [template string literals](https://docs.python.org/3.14/whatsnew/3.14.html#whatsnew314-template-string-literals), [deferred evaluation of annotations](https://docs.python.org/3.14/whatsnew/3.14.html#whatsnew314-deferred-annotations), and support for [subinterpreters](https://docs.python.org/3.14/whatsnew/3.14.html#whatsnew314-multiple-interpreters) in the standard library.
> 
> The library changes include significantly improved capabilities for [introspection in asyncio](https://docs.python.org/3.14/whatsnew/3.14.html#whatsnew314-asyncio-introspection), [support for Zstandard](https://docs.python.org/3.14/whatsnew/3.14.html#whatsnew314-zstandard) via a new [compression.zstd](https://docs.python.org/3.14/library/compression.zstd.html#module-compression.zstd) module, syntax highlighting in the REPL, as well as the usual deprecations and removals, and improvements in user\-friendliness and correctness.

Subinterpreters look particularly interesting as a way to use multiple CPU cores to run Python code despite the continued existence of the GIL. If you’re feeling brave and [your dependencies cooperate](https://hugovk.github.io/free-threaded-wheels/) you can also use the free\-threaded build of Python 3\.14 \- [now officially supported](https://docs.python.org/3.14/whatsnew/3.14.html#whatsnew314-free-threaded-now-supported) \- to skip the GIL entirely.

A new major Python release means an older release hits the [end of its support lifecycle](https://devguide.python.org/versions/) \- in this case that’s Python 3\.9\. If you maintain open source libraries that target every supported Python versions (as I do) this means features introduced in Python 3\.10 can now be depended on! [What’s new in Python 3\.10](https://docs.python.org/3.14/whatsnew/3.10.html) lists those \- I’m most excited by [structured pattern matching](https://docs.python.org/3.14/whatsnew/3.10.html#pep-634-structural-pattern-matching) (the `match/case` statement) and the [union type operator](https://docs.python.org/3.14/whatsnew/3.10.html#pep-604-new-type-union-operator), allowing `int | float | None` as a type annotation in place of `Optional[Union[int, float]]`.

If you use `uv` you can grab a copy of 3\.14 using:

```
uv self update
uv python upgrade 3.14
uvx python@3.14
```

Or for free\-threaded Python 3\.1;:

```
uvx python@3.14t
```

The `uv` team wrote [about their Python 3\.14 highlights](https://astral.sh/blog/python-3.14) in their announcement of Python 3\.14’s availability via `uv`.

---