# Imitation Intelligence keynote at PyCon 2024

*And: Give people something to link to so they can talk about your features and ideas*

Published: 2024-07-15
Source: https://simonw.substack.com/p/imitation-intelligence-keynote-at

---

In this newsletter:

* Imitation Intelligence, my keynote for PyCon US 2024
* Give people something to link to so they can talk about your features and ideas

Plus 14 links and 12 quotations and 2 TILs

### **[Imitation Intelligence, my keynote for PyCon US 2024](https://simonwillison.net/2024/Jul/14/pycon/) \- 2024\-07\-14**

I gave an invited keynote at PyCon US 2024 in Pittsburgh this year. My goal was to say some interesting things about AI \- specifically about Large Language Models \- both to help catch people up who may not have been paying close attention, but also to give people who *were*paying close attention some new things to think about.

The video is now [available on YouTube](https://www.youtube.com/watch?v=P1-KQZZarpc&t=248). Below is a fully annotated version of the slides and transcript.

* [The origins of the term "artificial intelligence"](https://simonwillison.net/2024/Jul/14/pycon/#pycon-2024.002.jpeg)
* [Why I prefer "imitation intelligence" instead](https://simonwillison.net/2024/Jul/14/pycon/#pycon-2024.008.jpeg)
* [How they are built](https://simonwillison.net/2024/Jul/14/pycon/#pycon-2024.011.jpeg)
* [Why I think they're interesting](https://simonwillison.net/2024/Jul/14/pycon/#pycon-2024.013.jpeg)
* [Evaluating their vibes](https://simonwillison.net/2024/Jul/14/pycon/#pycon-2024.016.jpeg)
* [Openly licensed models](https://simonwillison.net/2024/Jul/14/pycon/#pycon-2024.019.jpeg)
* [Accessing them from the command\-line with LLM](https://simonwillison.net/2024/Jul/14/pycon/#pycon-2024.022-old.jpeg)
* [Prompt engineering](https://simonwillison.net/2024/Jul/14/pycon/#pycon-2024.023.jpeg)

	+ [for chatbots](https://simonwillison.net/2024/Jul/14/pycon/#pycon-2024.024.jpeg)
	+ [for Retrieval Augmented Generation](https://simonwillison.net/2024/Jul/14/pycon/#pycon-2024.026.jpeg)
	+ [for function calling and tools](https://simonwillison.net/2024/Jul/14/pycon/#pycon-2024.029.jpeg)
* [Prompt injection](https://simonwillison.net/2024/Jul/14/pycon/#pycon-2024.031.jpeg)
* [ChatGPT Code Interpreter](https://simonwillison.net/2024/Jul/14/pycon/#pycon-2024.037.jpeg)
* [Building my AI speech counter with the help of GPT\-4o](https://simonwillison.net/2024/Jul/14/pycon/#pycon-2024.043.jpeg)
* [Structured data extraction with Datasette](https://simonwillison.net/2024/Jul/14/pycon/#pycon-2024.051.jpeg)
* [Transformative AI, not Generative AI](https://simonwillison.net/2024/Jul/14/pycon/#pycon-2024.056.jpeg)
* [Personal AI ethics and slop](https://simonwillison.net/2024/Jul/14/pycon/#pycon-2024.058.jpeg)
* [LLMs are shockingly good at code](https://simonwillison.net/2024/Jul/14/pycon/#pycon-2024.064.jpeg)
* [What should we, the Python community, do about this all?](https://simonwillison.net/2024/Jul/14/pycon/#pycon-2024.066.jpeg)

---

### **[Give people something to link to so they can talk about your features and ideas](https://simonwillison.net/2024/Jul/13/give-people-something-to-link-to/) \- 2024\-07\-13**

If you have a project, an idea, a product feature, or anything else that you want other people to understand and have conversations about... give them something to link to!

Two illustrative examples are ChatGPT Code Interpreter and Boring Technology.

#### **ChatGPT Code Interpreter is effectively invisible**

**ChatGPT Code Interpreter** has been one of my favourite AI tools for over a year. It's the feature of ChatGPT which allows the bot to write *and then execute* Python code as part of responding to your prompts. It's incredibly powerful... and almost invisible! If you don't know how to use prompts to activate the feature you may not realize it exists.

OpenAI don't even have a help page for it (and it very desperately needs documentation) \- if you search their site you'll find [confusing technical docs](https://platform.openai.com/docs/assistants/tools/code-interpreter) about an API feature and [misleading outdated forum threads](https://community.openai.com/t/how-can-i-access-the-code-interpreter-plugin-model/205304).

I evangelize this tool *a lot*, but OpenAI really aren't helping me do that. I end up linking people to [my code\-interpreter tag page](https://simonwillison.net/tags/code-interpreter/) because it's more useful than anything on OpenAI's own site.

Compare this with Claude's similar Artifacts feature which at least has an [easily discovered help page](https://support.anthropic.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them) \- though [the Artifacts announcement post](https://www.anthropic.com/news/claude-3-5-sonnet) was shared with Claude 3\.5 Sonnet so isn't obviously linkable. Even that help page isn't quite what I'm after. Features deserve dedicated pages!

GitHub understand this: here are their feature landing pages for [Codespaces](https://github.com/features/codespaces) and [Copilot](https://github.com/features/copilot) (I could even guess the URL for Copilot's page based on the Codespaces one).

**Update:** It turns out there IS documentation about Code Interpreter mode... but I failed to find it because it didn't use those terms anywhere on the page! The title is [Data analysis with ChatGPT](https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt).

This amuses me greatly because OpenAI have been oscillating on the name for this feature almost since they launched \- Code Interpreter, then Advanced Data Analysis, now Data analysis with ChatGPT. I made fun of this [last year](https://simonwillison.net/2023/Oct/17/open-questions/#open-questions.034.jpeg).

#### **Boring Technology: an idea with a website**

Dan McKinley coined the term **Boring Technology** in [an essay in 2015](https://mcfunley.com/choose-boring-technology). The key idea is that any development team has a limited capacity to solve new problems which should be reserved for the things that make their product unique. For everything else they should pick the most boring and well\-understood technologies available to them \- stuff where any bugs or limitations have been understood and discussed online for years.

(I'm very proud that Django has earned the honorific of "boring technology" in this context!)

Dan turned that essay into a talk, and then he turned that talk into a website with a brilliant domain name:

**[boringtechnology.club](https://boringtechnology.club/)**

The idea has stuck. I've had many productive conversations about it, and more importantly if someone *hasn't* heard the term before I can drop in that one link and they'll be up to speed a few minutes later.

I've tried to do this myself for some of my own ideas: [baked data](https://simonwillison.net/2021/Jul/28/baked-data/), [git scraping](https://simonwillison.net/2020/Oct/9/git-scraping/) and [prompt injection](https://simonwillison.net/series/prompt-injection/) all have pages that I frequently link people to. I never went as far as committing to a domain though and I think maybe that was a mistake \- having a clear message that "this is the key page to link to" is a very powerful thing.

#### **This is about both SEO and conversations**

One obvious goal here is SEO: if someone searches for your product feature you want them to land on your own site, not surrender valuable attention to someone else who's squatting on the search term.

I personally value the conversation side of it even more. Hyperlinks are the best thing about the web \- if I want to talk about something I'd much rather drop in a link to the definitive explanation rather than waste a paragraph (as I did earlier with Code Interpreter) explaining what the thing is for the upmteenth time!

If you have an idea, project or feature that you want people to understand and discuss, build it the web page it deserves. **Give people something to link to!**

---

**Link** 2024\-07\-08 [Jevons paradox](https://en.wikipedia.org/wiki/Jevons_paradox):

I've been thinking recently about how the demand for professional software engineers might be affected by the fact that LLMs are getting so good at producing working code, when prompted in the right way.

One possibility is that the price for writing code will fall, in a way that massively increases the demand for custom solutions \- resulting in a greater demand for software engineers since the increased value they can provide makes it much easier to justify the expense of hiring them in the first place.

TIL about the related idea of the Jevons paradox, currently explained by Wikipedia like so:

> \[...] when technological progress increases the efficiency with which a resource is used (reducing the amount necessary for any one use), but the falling cost of use induces increases in demand enough that resource use is increased, rather than reduced.

---

**Quote** 2024\-07\-09

> *Inside the labs we have these capable models, and they're not that far ahead from what the public has access to for free. And that's a completely different trajectory for bringing technology into the world that what we've seen historically. It's a great opportunity because it brings people along. It gives them intuitive sense for the capabilities and risks and allows people to prepare for the advent of bringing advanced AI into the world.*

[Mira Murati](https://www.youtube.com/watch?v=BD0Us5Bn6Lw&t=900s)

---

**Quote** 2024\-07\-09

> *Chrome's biggest innovation was the short release cycle with a silent unceremonious autoupdate.  
>   
> When updates were big, rare, and manual, buggy and outdated browsers were lingering for soo long, that we were giving bugs names. We documented the bugs in magazines and books, as if they were a timeless foundation of WebDev.  
>   
> Nowadays browser vendors can fix bugs in 6 weeks (even Safari can…). New\-ish stuff is still buggy, but rarely for long enough for the bugs to make it to schools' curriculums.*

[Kornel Lesiński](https://mastodon.social/@kornel/112752977103985802)

---

**Link** 2024\-07\-09 [Deactivating an API, one step at a time](https://apichangelog.substack.com/p/deactivating-an-api-one-step-at-a):

Bruno Pedro describes a sensible approach for web API deprecation, using API keys to first block new users from using the old API, then track which existing users are depending on the old version and reaching out to them with a sunset period.

The only suggestion I'd add is to implement API brownouts \- short periods of time where the deprecated API returns errors, several months before the final deprecation. This can help give users who don't read emails from you notice that they need to pay attention before their integration breaks entirely.

I've seen GitHub use this brownout technique successfully several times over the last few years \- here's [one example](https://github.blog/changelog/2021-08-10-brownout-notice-api-authentication-via-query-parameters-for-48-hours/).

---

**Link** 2024\-07\-09 [hangout\_services/thunk.js](https://github.com/chromium/chromium/blob/128.0.6586.1/chrome/browser/resources/hangout_services/thunk.js):

It turns out Google Chrome (via Chromium) includes a default extension which makes extra services available to code running on the `*.google.com` domains \- tweeted about today [by Luca Casonato](https://twitter.com/lcasdev/status/1810696257137959018), but the code has been there in the public repo [since October 2013](https://github.com/chromium/chromium/commit/422c736b82e7ee763c67109cde700db81ca7b443) as far as I can tell.

It looks like it's a way to let Google Hangouts (or presumably its modern predecessors) get additional information from the browser, including the current load on the user's CPU. Update: On Hacker News a Googler [confirms](https://news.ycombinator.com/item?id=40918742)that the Google Meet "troubleshooting" feature uses this to review CPU utilization.

I got GPT\-4o to [help me figure out how to trigger it](https://chatgpt.com/share/25008fdd-319e-447a-97b4-ea2c87cba583) (I tried Claude 3\.5 Sonnet first but it [refused](https://twitter.com/simonw/status/1810734848019157149), saying "Doing so could potentially violate terms of service or raise security and privacy concerns"). Paste the following into your Chrome DevTools console on any Google site to see the result:

```
chrome.runtime.sendMessage(
  "nkeimhogjdpnpccoofpliimaahmaaome",
  { method: "cpu.getInfo" },
  (response) => {
    console.log(JSON.stringify(response, null, 2));
  },
);

```

I get back a response that starts like this:

```
{
  "value": {
    "archName": "arm64",
    "features": [],
    "modelName": "Apple M2 Max",
    "numOfProcessors": 12,
    "processors": [
      {
        "usage": {
          "idle": 26890137,
          "kernel": 5271531,
          "total": 42525857,
          "user": 10364189
        }
      }, ...

```

The code doesn't do anything on non\-Google domains.

Luca [says this](https://twitter.com/lcasdev/status/1810696259184779750) \- I'm inclined to agree:

> This is interesting because it is a clear violation of the idea that browser vendors should not give preference to their websites over anyone elses.

---

**Link** 2024\-07\-09 [Claude: You can now publish, share, and remix artifacts](https://twitter.com/alexalbert__/status/1810699033524195673):

Artifacts is the feature Anthropic released a few weeks ago to accompany Claude 3\.5 Sonnet, allowing Claude to create interactive HTML\+JavaScript tools in response to prompts.

This morning they added the ability to make those artifacts public and share links to them, which makes them even more useful!

Here's my [box shadow playground](https://claude.site/artifacts/c6908120-c3d7-4e99-bdee-d3d80448af0f) from [the other day](https://simonwillison.net/2024/Jul/8/box-shadow-css-generator/), and an [example page I requested](https://claude.site/artifacts/6065c03c-d799-40fe-ae36-8de821bc58ad)demonstrating the [Milligram CSS framework](https://milligram.io/) \- Artifacts can load most code that is available via [cdnjs](https://cdnjs.com/) so they're great for quickly trying out new libraries.

---

**TIL** 2024\-07\-10 [Accessing 1Password items from the terminal](https://til.simonwillison.net/macos/1password-terminal):

I save things like API keys in [1Password](https://1password.com/). Today I figured out how to access those from macOS terminal scripts. …

---

**Quote** 2024\-07\-10

> *Content slop has three important characteristics. The first being that, to the user, the viewer, the customer, it feels worthless. This might be because it was clearly generated in bulk by a machine or because of how much of that particular content is being created. The next important feature of slop is that feels forced upon us, whether by a corporation or an algorithm. It’s in the name. We’re the little piggies and it’s the gruel in the trough. But the last feature is the most crucial. It not only feels worthless and ubiquitous, it also feels optimized to be so. The Charli XCX “Brat summer” meme does not feel like slop, nor does Kendrick Lamar’s extremely long “Not Like Us” roll out. But Taylor Swift’s cascade of alternate versions of her songs does. The jury’s still out on Sabrina Carpenter. Similarly, last summer’s Barbenheimer phenomenon did not, to me, feel like slop. Dune: Part Two didn’t either. But Deadpool \& Wolverine, at least in the marketing, definitely does.*

[Ryan Broderick](https://www.garbageday.email/p/slop-void)

---

**Link** 2024\-07\-10 [Vision language models are blind](https://vlmsareblind.github.io/):

A new paper exploring vision LLMs, comparing GPT\-4o, Gemini 1\.5 Pro, Claude 3 Sonnet and Claude 3\.5 Sonnet (I'm surprised they didn't include Claude 3 Opus and Haiku, which are more interesting than Claude 3 Sonnet in my opinion).

I don't like the title and framing of this paper. They describe seven tasks that vision models have trouble with \- mainly geometric analysis like identifying intersecting shapes or counting things \- and use those to support the following statement:

> The shockingly poor performance of four state\-of\-the\-art VLMs suggests their vision is, at best, like of a person with myopia seeing fine details as blurry, and at worst, like an intelligent person that is blind making educated guesses.

While the failures they describe are certainly interesting, I don't think they justify that conclusion.

I've felt starved for information about the strengths and weaknesses of these vision LLMs since the good ones started becoming available last November (GPT\-4 Vision at OpenAI DevDay) so identifying tasks like this that they fail at is useful. But just like pointing out an LLM can't count letters doesn't mean that LLMs are useless, these limitations of vision models shouldn't be used to declare them "blind" as a sweeping statement.

---

**Link** 2024\-07\-10 [Anthropic cookbook: multimodal](https://github.com/anthropics/anthropic-cookbook/tree/main/multimodal):

I'm currently on the lookout for high quality sources of information about vision LLMs, including prompting tricks for getting the most out of them.

This set of Jupyter notebooks from Anthropic (published four months ago to accompany the original Claude 3 models) is the best I've found so far. [Best practices for using vision with Claude](https://github.com/anthropics/anthropic-cookbook/blob/main/multimodal/best_practices_for_vision.ipynb) includes advice on multi\-shot prompting with example, plus this interesting think step\-by\-step style prompt for improving Claude's ability to count the dogs in an image:

> You have perfect vision and pay great attention to detail which makes you an expert at counting objects in images. How many dogs are in this picture? Before providing the answer in `<answer>`tags, think step by step in `<thinking>` tags and analyze every part of the image.

---

**Quote** 2024\-07\-10

> *Yeah, unfortunately vision prompting has been a tough nut to crack. We've found it's very challenging to improve Claude's actual "vision" through just text prompts, but we can of course improve its reasoning and thought process once it extracts info from an image.   
>   
> In general, I think vision is still in its early days, although 3\.5 Sonnet is noticeably better than older models.*

[Alex Albert (Anthropic)](https://twitter.com/alexalbert__/status/1811101055054402019)

---

**Link** 2024\-07\-10 [Early Apple tech bloggers are shocked to find their name and work have been AI\-zombified](https://www.theverge.com/2024/7/10/24195858/tuaw-unofficial-apple-tech-blog-ai-web-orange-khan):

> TUAW (“The Unofficial Apple Weblog”) was shut down by AOL in 2015, but this past year, a new owner scooped up the domain and began posting articles under the bylines of former writers *who haven’t worked there for over a decade*.

They're using AI\-generated images against real names of original contributors, then publishing LLM\-rewritten articles because they didn't buy the rights to the original content!

---

**Quote** 2024\-07\-11

> *My main concern is that the substantial cost to develop and run Al technology means that Al applications must solve extremely complex and important problems for enterprises to earn an appropriate return on investment.  
>   
> We estimate that the Al infrastructure buildout will cost over $1tn in the next several years alone, which includes spending on data centers, utilities, and applications. So, the crucial question is: What $1tn problem will Al solve? Replacing low\-wage jobs with tremendously costly technology is basically the polar opposite of the prior technology transitions I've witnessed in my thirty years of closely following the tech industry.*

[Jim Covello, Goldman Sachs](https://www.goldmansachs.com/intelligence/pages/gen-ai-too-much-spend-too-little-benefit.html)

---

**Link** 2024\-07\-11 [The economics of a Postgres free tier](https://xata.io/blog/postgres-free-tier):

[Xata](https://xata.io/) offer a hosted PostgreSQL service with a generous free tier (15GB of volume). I'm very suspicious of free tiers that don't include a detailed breakdown of the unit economics... and in this post they've described exactly that, in great detail.

The trick is that they run their free tier on shared clusters \- with each $630/month cluster supporting 2,000 free instances for $0\.315 per instance per month. Then inactive databases get downgraded to even cheaper auto\-scaling clusters that can host 20,000 databases for $180/month (less than 1c each).

They also cover the volume cost of $0\.10/GB/month \- so up to $1\.50/month per free instance, but most instances only use a small portion of that space.

It's reassuring to see this spelled out in so much detail.

---

**Quote** 2024\-07\-11

> *\[On Paddington 3] If this movie is anywhere near as good as the second one, we are going to need to have an extremely serious conversation about this being one of the greatest film trilogies ever made.*

[Brian Grubb](https://briancgrubb.substack.com/p/the-five-spot-knives-out-more-like)

---

**Link** 2024\-07\-12 [Why The Atlantic signed a deal with OpenAI](https://www.theverge.com/2024/7/11/24196396/the-atlantic-openai-licensing-deal-ai-news-journalism-web-future-decoder-podcasts):

Interesting conversation between Nilay Patel and The Atlantic CEO (and former journalist/editor) Nicholas Thompson about the relationship between media organizations and LLM companies like OpenAI.

On the impact of these deals on the ongoing New York Times lawsuit:

> One of the ways that we \[The Atlantic] can help the industry is by making deals and setting a market. I believe that us doing a deal with OpenAI makes it easier for us to make deals with the other large language model companies if those come about, I think it makes it easier for other journalistic companies to make deals with OpenAI and others, and I think it makes it more likely that The Times wins their lawsuit.

How could it help? Because deals like this establish a market value for training content, important for the fair use component of the legal argument.

---

**Quote** 2024\-07\-12

> *Fighting bots is fighting humans \[...] remind you that "only allow humans to access" is just not an achievable goal. Any attempt at limiting bot access will inevitably allow some bots through and prevent some humans from accessing the site, and it's about deciding where you want to set the cutoff. I fear that media outlets and other websites, in attempting to "protect" their material from AI scrapers, will go too far in the anti\-human direction.*

[Molly White](https://www.mollywhite.net/micro/entry/fighting-bots-is-fighting-humans)

---

**Link** 2024\-07\-12 [The Death of the Junior Developer](https://sourcegraph.com/blog/the-death-of-the-junior-developer):

Steve Yegge's speculative take on the impact LLM\-assisted coding could have on software careers.

Steve works on Cody, an AI programming assistant, so he's hardly an unbiased source of information. Nevertheless, his collection of anecdotes here matches what I've been seeing myself.

Steve coins the term here CHOP, for Chat Oriented Programming, where the majority of code is typed by an LLM that is directed by a programmer. Steve describes it as "coding via iterative prompt refinement", and argues that the models only recently got good enough to support this style with GPT\-4o, Gemini Pro and Claude 3 Opus.

I've been experimenting with this approach myself on a few small projects (see [this Claude example](https://simonwillison.net/2024/Apr/8/files-to-prompt/)) and it really is a surprisingly effective way to work.

Also included: a story about how GPT\-4o produced a bewitchingly tempting proposal with long\-term damaging effects that only a senior engineer with deep understanding of the problem space could catch!

I'm in strong agreement with this thought on the skills that are becoming most important:

> Everyone will need to get a lot more serious about testing and reviewing code.

---

**Link** 2024\-07\-12 [Searching an aerial photo with text queries](https://blog.rtwilson.com/searching-an-aerial-photo-with-text-queries-a-demo-and-how-it-works/):

Robin Wilson built[a demo](https://server1.rtwilson.com/aerial/static/index.html)that lets you search a large aerial photograph of Southampton for things like "roundabout" or "tennis court". He explains how it works in detail: he used the[SkyCLIP](https://github.com/wangzhecheng/SkyScript)model, which is trained on "5\.2 million remote sensing image\-text pairs in total, covering more than 29K distinct semantic tags" to generate embeddings for 200x200 image segments (with 100px of overlap), then stored them in Pinecone.

---

**Link** 2024\-07\-12 [datasette\-python](https://github.com/datasette/datasette-python):

I just released a small new plugin for Datasette to assist with debugging. It adds a `python`subcommand which runs a Python process in the same virtual environment as Datasette itself.

I built it initially to help debug some issues in Datasette installed via Homebrew. The Homebrew installation has its own virtual environment, and sometimes it can be useful to run commands like `pip list` in the same environment as Datasette itself.

Now you can do this:

```
brew install datasette
datasette install datasette-python
datasette python -m pip list

```

I built a similar plugin for LLM last year, called [llm\-python](https://github.com/simonw/llm-python) \- it's proved useful enough that I duplicated the design for Datasette.

---

**Link** 2024\-07\-12 [Free\-threaded CPython is ready to experiment with!](https://labs.quansight.org/blog/free-threaded-python-rollout):

The Python 3\.13 beta releases that include a "free\-threaded" version that removes the GIL are now available to test! A team from Quansight Labs, home of the PyData core team, just launched [py\-free\-threading.github.io](https://py-free-threading.github.io/) to help document the new builds and track compatibility with Python's larger ecosystem.

Free\-threading mode will not be enabled in Python installations by default. You can install special builds that have the option enabled today \- I used the macOS installer and, after enabling the new build in the "Customize" panel in the installer, ended up with a `/usr/local/bin/python3.13t` binary which shows "Python 3\.13\.0b3 experimental free\-threading build" when I run it.

Here's [my TIL describing my experiments so far](https://til.simonwillison.net/python/trying-free-threaded-python)installing and running the 3\.13 beta on macOS, which also includes a correction to an embarrassing bug that Claude introduced but I failed to catch!

---

**TIL** 2024\-07\-13 [Trying out free\-threaded Python on macOS](https://til.simonwillison.net/python/trying-free-threaded-python):

Inspired by [py\-free\-threading.github.io](https://py-free-threading.github.io/) I decided to try out a beta of Python 3\.13 with the new free\-threaded mode enabled, which removes the GIL. …

---

**Quote** 2024\-07\-13

> *Third, X fails to **provide access to its public data to researchers** in line with the conditions set out in the DSA. In particular, X prohibits eligible researchers from **independently accessing** its public data, such as by scraping, as stated in its terms of service. In addition, X's process to **grant eligible researchers access to its application programming interface (API)**appears to dissuade researchers from carrying out their research projects or leave them with no other choice than to pay disproportionally high fees.*

[European Commission](https://ec.europa.eu/commission/presscorner/detail/en/IP_24_3761)

---

**Quote** 2024\-07\-13

> *Add tests in a commit before the fix. They should pass, showing the behavior before your change. Then, the commit with your change will update the tests. The diff between these commits represents the change in behavior. This helps the author test their tests (I've written tests thinking they covered the relevant case but didn't), the reviewer to more precisely see the change in behavior and comment on it, and the wider community to understand what the PR description is about.*

[Ed Page](https://news.ycombinator.com/item?id=40949229#40951540)

---

**Quote** 2024\-07\-13

> *We respect wildlife in the wilderness because we’re in their house. We don’t fully understand the complexity of most ecosystems, so we seek to minimize our impact on those ecosystems since we can’t always predict what outcomes our interactions with nature might have.  
>   
> In software, many disastrous mistakes stem from not understanding why a system was built the way it was, but changing it anyway. It’s super common for a new leader to come in, see something they see as “useless”, and get rid of it – without understanding the implications. Good leaders make sure they understand before they mess around.*

[Jacob Kaplan\-Moss](https://jacobian.org/2024/jul/12/lnt-for-engineering-leadership/)

---

**Link** 2024\-07\-13 [Load Balancing](https://samwho.dev/load-balancing/):

Sam Rose built this interactive essay explaining how different load balancing strategies work. It's part of[a series](https://samwho.dev/)that includes[memory allocation](https://samwho.dev/memory-allocation/),[bloom filters](https://samwho.dev/bloom-filters/)and more.

---

**Quote** 2024\-07\-13

> *My architecture is a monolith written in Go (this is intentional, I sacrificed scalability to improve my shipping speed), and this is where SQLite shines. With a DB located on the local NVMe disk, a 5$ VPS can deliver a whopping 60K reads and 20K writes per second.*

[Nikita Melkozerov](https://twitter.com/meln1k/status/1812116658300817477)

---

**Quote** 2024\-07\-14

> *So much of knowledge/intelligence involves translating ideas between fields (domains). Those domains are walls the keep ideas siloed. But LLMs can help break those walls down and encourage humans to do more interdisciplinary thinking, which may lead to faster discoveries.  
>   
> And note that I am implying that humans will make the breakthroughs, using LLMs as translation tools when appropriate, to help make connections. LLMs are strongest as translators of information that you provide. BYOD: Bring your own data!*

[Benj Edwards](https://twitter.com/benjedwards/status/1812507226428342528)

---