# Not all AI-assisted programming is vibe coding (but vibe coding rocks)

*Plus Mistral Small 3.1, OLMo 2 32B and using GitHub Actions with GitHub Pages*

Published: 2025-03-19
Source: https://simonw.substack.com/p/not-all-ai-assisted-programming-is

---

In this newsletter:

* Not all AI\-assisted programming is vibe coding (but vibe coding rocks)

Plus 13 links and 2 quotations and 2 TILs

### [Not all AI\-assisted programming is vibe coding (but vibe coding rocks)](https://simonwillison.net/2025/Mar/19/vibe-coding/) \- 2025\-03\-19

**Vibe coding** is having a moment. The term [was coined by Andrej Karpathy](https://twitter.com/karpathy/status/1886192184808149383) just a few weeks ago (on February 6th) and has since been featured [in the New York Times](https://www.nytimes.com/2025/02/27/technology/personaltech/vibecoding-ai-software-programming.html), [Ars Technica](https://arstechnica.com/ai/2025/03/is-vibe-coding-with-ai-gnarly-or-reckless-maybe-some-of-both/), [the Guardian](https://www.theguardian.com/technology/2025/mar/16/ai-software-coding-programmer-expertise-jobs-threat) and countless online discussions.

I'm concerned that the definition is already escaping its original intent. I'm seeing people apply the term "vibe coding" to all forms of code written with the assistance of AI. I think that both dilutes the term and gives a false impression of what's possible with responsible [AI\-assisted programming](https://simonwillison.net/tags/ai-assisted-programming/).

Vibe coding is *not* the same thing as writing code with the help of LLMs!

To quote Andrej's [original tweet](https://twitter.com/karpathy/status/1886192184808149383) in full (with my emphasis added):

> There's a new kind of coding I call "vibe coding", where you fully give in to the vibes, embrace exponentials, and **forget that the code even exists**. It's possible because the LLMs (e.g. Cursor Composer w Sonnet) are getting too good. Also I just talk to Composer with SuperWhisper so I barely even touch the keyboard.
> 
> I ask for the dumbest things like "decrease the padding on the sidebar by half" because I'm too lazy to find it. I "Accept All" always, I don't read the diffs anymore. When I get error messages I just copy paste them in with no comment, usually that fixes it. The code grows beyond my usual comprehension, I'd have to really read through it for a while. Sometimes the LLMs can't fix a bug so I just work around it or ask for random changes until it goes away.
> 
> **It's not too bad for throwaway weekend projects, but still quite amusing**. I'm building a project or webapp, but it's not really coding \- I just see stuff, say stuff, run stuff, and copy paste stuff, and it mostly works.

I *love* this definition. Andrej is an extremely talented and experienced programmer \- he has no need for AI assistance at all. He's using LLMs like this because it's fun to try out wild new ideas, and the speed at which an LLM can produce code is an order of magnitude faster than even the most skilled human programmers. For low stakes projects and prototypes why not just *let it rip*?

When I talk about vibe coding I mean **building software with an LLM without reviewing the code it writes**.

#### Using LLMs for code responsibly is not vibe coding

Let's contrast this "forget that the code even exists" approach to how professional software developers use LLMs.

The job of a software developer is not (just) to churn out code and features. We need to create code that demonstrably works, and can be understood by other humans (and machines), and that will support continued development in the future.

We need to consider performance, accessibility, security, maintainability, cost efficiency. Software engineering is all about trade\-offs \- our job is to pick from dozens of potential solutions by balancing all manner of requirements, both explicit and implied.

We also *need* to read the code. My golden rule for production\-quality AI\-assisted programming is that I won't commit any code to my repository if I couldn't explain exactly what it does to somebody else.

If an LLM wrote the code for you, and you then reviewed it, tested it thoroughly and made sure you could explain how it works to someone else that's not vibe coding, it's software development. The usage of an LLM to support that activity is immaterial.

I wrote extensively about my own process in [Here’s how I use LLMs to help me write code](https://simonwillison.net/2025/Mar/11/using-llms-for-code/). Vibe coding only describes a small subset of my approach.

#### Let's not lose track of what makes vibe coding special

I don't want "vibe coding" to become a negative term that's synonymous with irresponsible AI\-assisted programming either. This weird new shape of programming has so much to offer the world!

I believe **everyone deserves the ability** to automate tedious tasks in their lives with computers. You shouldn't need a computer science degree or programming bootcamp in order to get computers to do extremely specific tasks for you.

If vibe coding grants millions of new people the ability to build their own custom tools, I could not be happier about it.

Some of those people will get bitten by the programming bug and go on to become proficient software developers. One of the biggest barriers to that profession is the incredibly steep initial learning curve \- vibe coding shaves that initial barrier down to almost flat.

Vibe coding also has a ton to offer experienced developers. I've talked before about how [using LLMs for code is difficult](https://simonwillison.net/2025/Mar/11/using-llms-for-code/) \- figuring out what does and doesn't work is a case of building intuition over time, and there are plenty of hidden sharp edges and traps along the way.

I think vibe coding is the best tool we have to help experienced developers build that intuition as to what LLMs can and cannot do for them. I've published more than [80 experiments](https://tools.simonwillison.net/colophon) I built with vibe coding and I've learned so much along the way. I would encourage any other developer, no matter their skill level, to try the same.

#### When is it OK to vibe code?

If you're an experienced engineer this is likely obvious to you already, so I'm writing this section for people who are just getting started building software.

* Projects should be **low stakes**. Think about how much harm the code you are writing could cause if it has bugs or security vulnerabilities. Could somebody be harmed \- damaged reputation, lost money or something worse? This is particularly important if you plan to build software that will be used by other people!
* Consider **security**. This is a really difficult one \- security is a huge topic. Some high level notes:

	+ Watch out for **secrets** \- anything that looks similar in shape to a password, such as the API key used to access an online tool. If your code involves secrets you need to take care not to accidentally expose them, which means you need to understand how the code works!
	+ Think about **data privacy**. If you are building a tool that has access to private data \- anything you wouldn't want to display to the world in a screen\-sharing session \- approach with caution. It's possible to vibe code personal tools that you paste private information into but you need to be very sure you understand if there are ways that data might leave your machine.
* Be a **good network citizen**. Anything that makes requests out to other platforms could increase the load (and hence the cost) on those services. This is a reason I like [Claude Artifacts](https://simonwillison.net/tags/claude-artifacts/) \- their sandbox prevents accidents from causing harm elsewhere.
* Is **your money on the line**? I've seen horror stories about people who vibe coded a feature against some API without a billing limit and racked up thousands of dollars in charges. Be very careful about using vibe coding against anything that's charged based on usage.

If you're going to vibe code anything that might be used by other people, I recommend checking in with someone more experienced for a vibe check (hah) before you share it with the world.

#### How do we make vibe coding better?

I think there are some fascinating software design challenges to be solved here.

Safe vibe coding for complete beginners starts with a [sandbox](https://en.wikipedia.org/wiki/Sandbox_(computer_security)). Claude Artifacts was one of the first widely available vibe coding platforms and their approach to sandboxing is fantastic: code is restricted to running in a locked down `<iframe>`, can load only approved libraries and can't make any network requests to other sites.

This makes it very difficult for people to mess up and cause any harm with their projects. It also greatly limits what those projects can do \- you can't use a Claude Artifact project to access data from external APIs for example, or even to build software that runs your own prompts against an LLM.

Other popular vibe coding tools like Cursor (which was initially intended for professional developers) have far less safety rails.

There's plenty of room for innovation in this space. I'm hoping to see a cambrian explosion in tooling to help people build their own custom tools as productively and safely as possible.

#### Go forth and vibe code

I really don't want to discourage people who are new to software from trying out vibe coding. The best way to learn anything is to build a project!

For experienced programmers this is an amazing way to start developing an intuition for what LLMs can and can't do. For beginners there's no better way to open your eyes to what's possible to achieve with code itself.

But please, don't confuse vibe coding with all other uses of LLMs for code.

---

**Link** 2025\-03\-14 [Merklemap runs a 16TB PostgreSQL](https://news.ycombinator.com/item?id=43364668#43365833):

Interesting thread on Hacker News where Pierre Barre describes the database architecture behind [Merklemap](https://www.merklemap.com/), a certificate transparency search engine.

> I run a 100 billion\+ rows Postgres database \[0], that is around 16TB, it's pretty painless!
> 
> There are a few tricks that make it run well (PostgreSQL compiled with a non\-standard block size, ZFS, careful VACUUM planning). But nothing too out of the ordinary.
> 
> ATM, I insert about 150,000 rows a second, run 40,000 transactions a second, and read 4 million rows a second.
> 
> \[...]
> 
> It's self\-hosted on bare metal, with standby replication, normal settings, nothing "weird" there.
> 
> 6 NVMe drives in raidz\-1, 1024GB of memory, a 96 core AMD EPYC cpu.
> 
> \[...]
> 
> About 28K euros of hardware per replica \[one\-time cost] IIRC \+ \[ongoing] colo costs.

---

**Link** 2025\-03\-14 [Something Is Rotten in the State of Cupertino](https://daringfireball.net/2025/03/something_is_rotten_in_the_state_of_cupertino):

John Gruber's blazing takedown of Apple's failure to ship many of the key Apple Intelligence features they've been actively promoting for the past twelve months.

> The fiasco here is not that Apple is late on AI. It's also not that they had to announce an embarrassing delay on promised features last week. Those are problems, not fiascos, and problems happen. They're inevitable. \[...] The fiasco is that Apple pitched a story that wasn't true, one that *some* people within the company surely understood wasn't true, and they set a course based on that.

John divides the Apple Intelligence features into the ones that were demonstrated to members of the press (including himself) at various events over the past year compared to things like "personalized Siri" that were only ever shown as concept videos. The ones that were demonstrated have all shipped. The concept video features are [indeterminably delayed](https://simonwillison.net/2025/Mar/8/delaying-personalized-siri/).

---

**Link** 2025\-03\-14 [How ProPublica Uses AI Responsibly in Its Investigations](https://www.propublica.org/article/using-ai-responsibly-for-reporting):

Charles Ornstein describes how ProPublic used an LLM to help analyze data for their recent story [A Study of Mint Plants. A Device to Stop Bleeding. This Is the Scientific Research Ted Cruz Calls “Woke.”](https://www.propublica.org/article/ted-cruz-woke-grants-national-science-foundation) by Agnel Philip and Lisa Song.

They ran \~3,400 grant descriptions through a prompt that included the following:

> As an investigative journalist, I am looking for the following information
> 
> \-\-
> 
> `woke_description`: A short description (at maximum a paragraph) on why this grant is being singled out for promoting "woke" ideology, Diversity, Equity, and Inclusion (DEI) or advanced neo\-Marxist class warfare propaganda. Leave this blank if it's unclear.
> 
> `why_flagged`: Look at the "STATUS", "SOCIAL JUSTICE CATEGORY", "RACE CATEGORY", "GENDER CATEGORY" and "ENVIRONMENTAL JUSTICE CATEGORY" fields. If it's filled out, it means that the author of this document believed the grant was promoting DEI ideology in that way. Analyze the "AWARD DESCRIPTIONS" field and see if you can figure out why the author may have flagged it in this way. Write it in a way that is thorough and easy to understand with only one description per type and award.
> 
> `citation_for_flag`: Extract a very concise text quoting the passage of "AWARDS DESCRIPTIONS" that backs up the "why\_flagged" data.

This was only the first step in the analysis of the data:

> Of course, members of our staff reviewed and confirmed every detail before we published our story, and we called all the named people and agencies seeking comment, which remains a must\-do even in the world of AI.

I think journalists are particularly well positioned to take advantage of LLMs in this way, because a big part of journalism is about deriving the truth from multiple unreliable sources of information. Journalists are deeply familiar with fact\-checking, which is a critical skill if you're going to report with the assistance of these powerful but unreliable models.

Agnel Philip:

> The tech holds a ton of promise in lead generation and pointing us in the right direction. But in my experience, it still needs a lot of human supervision and vetting. If used correctly, it can both really speed up the process of understanding large sets of information, and if you’re creative with your prompts and critically read the output, it can help uncover things that you may not have thought of.

---

**Link** 2025\-03\-14 [Apple’s Siri Chief Calls AI Delays Ugly and Embarrassing, Promises Fixes](https://www.bloomberg.com/news/articles/2025-03-14/apple-s-siri-chief-calls-ai-delays-ugly-and-embarrassing-promises-fixes):

Mark Gurman reports on some leaked details from internal Apple meetings concerning the delays in shipping personalized Siri. This note in particular stood out to me:

> Walker said the decision to delay the features was made because of quality issues and that the company has found the technology only works properly up to two\-thirds to 80% of the time. He said the group “can make more progress to get those percentages up, so that users get something they can really count on.” \[...]
> 
> But Apple wants to maintain a high bar and only deliver the features when they’re polished, he said. “These are not quite ready to go to the general public, even though our competitors might have launched them in this state or worse.”

I imagine it's a lot harder to get reliable results out of small, local LLMs that run on an iPhone. Features that fail 1/3 to 1/5 of the time are unacceptable for a consumer product like this.

---

**Link** 2025\-03\-14 [TIL: Styling an HTML dialog modal to take the full height of the viewport](https://til.simonwillison.net/css/dialog-full-height):

I spent some time today trying to figure out how to have a modal `<dialog>` element present as a full height side panel that animates in from the side. The full height bit was hard, until Natalie helped me figure out that browsers apply a default `max-height: calc(100% - 6px - 2em);` rule which needs to be over\-ridden.

Also included: some [spelunking through the HTML spec](https://til.simonwillison.net/css/dialog-full-height#user-content-spelunking-through-the-html-specification) to figure out where that `calc()` expression was first introduced. The answer was [November 2020](https://github.com/whatwg/html/commit/979af1532).

---

**Quote** 2025\-03\-15

> *Some people today are discouraging others from learning programming on the grounds AI will automate it. This advice will be seen as some of the worst career advice ever given. I disagree with the Turing Award and Nobel prize winner who wrote, “It is far more likely that the programming occupation will become extinct \[...] than that it will become all\-powerful. More and more, computers will program themselves.”​ Statements discouraging people from learning to code are harmful!   
>   
> In the 1960s, when programming moved from punchcards (where a programmer had to laboriously make holes in physical cards to write code character by character) to keyboards with terminals, programming became easier. And that made it a better time than before to begin programming. Yet it was in this era that Nobel laureate Herb Simon wrote the words quoted in the first paragraph. Today’s arguments not to learn to code continue to echo his comment.   
>   
> As coding becomes easier, more people should code, not fewer!*

[Andrew Ng](https://www.deeplearning.ai/the-batch/issue-292/)

---

**Link** 2025\-03\-16 [mlx\-community/OLMo\-2\-0325\-32B\-Instruct\-4bit](https://huggingface.co/mlx-community/OLMo-2-0325-32B-Instruct-4bit):

OLMo 2 32B [claims to be](https://simonwillison.net/2025/Mar/13/ai2/) "the first fully\-open model (all data, code, weights, and details are freely available) to outperform GPT3\.5\-Turbo and GPT\-4o mini". Thanks to the MLX project here's a recipe that worked for me to run it on my Mac, via my [llm\-mlx](https://github.com/simonw/llm-mlx) plugin.

To install the model:

```
llm install llm-mlx
llm mlx download-model mlx-community/OLMo-2-0325-32B-Instruct-4bit
```

That downloads 17GB to `~/.cache/huggingface/hub/models--mlx-community--OLMo-2-0325-32B-Instruct-4bit`.

To start an interactive chat with OLMo 2:

```
llm chat -m mlx-community/OLMo-2-0325-32B-Instruct-4bit
```

Or to run a prompt:

```
llm -m mlx-community/OLMo-2-0325-32B-Instruct-4bit 'Generate an SVG of a pelican riding a bicycle' -o unlimited 1
```

The `-o unlimited 1` removes the cap on the number of output tokens \- the default for `llm-mlx` is 1024 which isn't enough to attempt to draw a pelican.

The [pelican it drew](https://gist.github.com/simonw/53f00731d494439d4aeca6bdd55368ca) is refreshingly abstract:

[![Blue and black wiggly lines looking more like a circuit diagram than a pelican riding a bicycle](https://substackcdn.com/image/fetch/$s_!VtC9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa82bca16-000d-4f58-abbd-e6a5a57d1c7f_928x780.jpeg "Blue and black wiggly lines looking more like a circuit diagram than a pelican riding a bicycle")](https://substackcdn.com/image/fetch/$s_!VtC9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa82bca16-000d-4f58-abbd-e6a5a57d1c7f_928x780.jpeg)

---

**Link** 2025\-03\-16 [Backstory on the default styles for the HTML dialog modal](https://news.ycombinator.com/item?id=43378225#43380129):

My TIL about [Styling an HTML dialog modal to take the full height of the viewport](https://til.simonwillison.net/css/dialog-full-height) (here's the [interactive demo](https://tools.simonwillison.net/side-panel-dialog)) showed up [on Hacker News](https://news.ycombinator.com/item?id=43378225) this morning, and attracted this fascinating comment from Chromium engineer Ian Kilpatrick.

> There's quite a bit of history here, but the abbreviated version is that the dialog element was originally added as a replacement for window.alert(), and there were a libraries polyfilling dialog and being surprisingly widely used.
> 
> The mechanism which dialog was originally positioned was relatively complex, and slightly hacky (magic values for the insets).
> 
> Changing the behaviour basically meant that we had to add "overflow:auto", and some form of "max\-height"/"max\-width" to ensure that the content within the dialog was actually reachable.
> 
> The better solution to this was to add "max\-height:stretch", "max\-width:stretch". You can see [the discussion for this here](https://github.com/whatwg/html/pull/5936#discussion_r513642207).
> 
> The problem is that no browser had (and still has) shipped the "stretch" keyword. (Blink [likely will "soon"](https://groups.google.com/a/chromium.org/g/blink-dev/c/SiZ2nDt3B9E/m/kP_rKOaDAgAJ?pli=1))
> 
> However this was pushed back against as this had to go in a specification \- and nobody implemented it ("\-webit\-fill\-available" would have been an acceptable substitute in Blink but other browsers didn't have this working the same yet).
> 
> Hence the calc() variant. (Primarily because of "box\-sizing:content\-box" being the default, and pre\-existing border/padding styles on dialog that we didn't want to touch). \[...]

I particularly enjoyed this insight into the challenges of evolving the standards that underlie the web, even for something this small:

> One thing to keep in mind is that any changes that changes web behaviour is under some time pressure. If you leave something too long, sites will start relying on the previous behaviour \- so it would have been arguably worse not to have done anything.

Also from the comments I learned that Firefox DevTools *can* show you user\-agent styles, but that option is turned off by default \- [notes on that here](https://til.simonwillison.net/css/dialog-full-height#user-content-update-firefox-can-show-browser-styles). Once I turned this option on I saw references to an `html.css` stylesheet, so I dug around and [found that in the Firefox source code](https://searchfox.org/mozilla-central/source/layout/style/res/html.css). Here's [the commit history](https://github.com/mozilla/gecko-dev/commits/HEAD/layout/style/res/html.css) for that file on the official GitHub mirror, which provides a detailed history of how Firefox default HTML styles have evolved with the standards over time.

And [via uallo](https://news.ycombinator.com/item?id=43378225#43380255) here are the same default HTML styles for other browsers:

* Chromium: [third\_party/blink/renderer/core/html/resources/html.css](https://github.com/chromium/chromium/blob/main/third_party/blink/renderer/core/html/resources/html.css)
* WebKit: [Source/WebCore/css/html.css](https://github.com/WebKit/WebKit/blob/main/Source/WebCore/css/html.css)

---

**Link** 2025\-03\-16 [Now you don’t even need code to be a programmer. But you do still need expertise](https://www.theguardian.com/technology/2025/mar/16/ai-software-coding-programmer-expertise-jobs-threat):

My recent piece on [how I use LLMs to help me write code](https://simonwillison.net/2025/Mar/11/using-llms-for-code/) got a positive mention in John Naughton's column about vibe\-coding in the Guardian this weekend.

My [hunch about Apple Intelligence Siri features being delayed](https://simonwillison.net/2025/Mar/8/delaying-personalized-siri/) due to prompt injection also got a mention in [the most recent episode](https://podcasts.apple.com/us/podcast/apples-siri-ous-problem-how-starlink-took-over-the/id1528594034?i=1000699160930) of the New York Times Hard Fork podcast.

---

**Link** 2025\-03\-17 [Mistral Small 3\.1](https://mistral.ai/fr/news/mistral-small-3-1):

Mistral Small 3 [came out in January](https://simonwillison.net/2025/Jan/30/mistral-small-3/) and was a notable, genuinely excellent local model that used an Apache 2\.0 license.

Mistral Small 3\.1 offers a significant improvement: it's multi\-modal (images) and has an increased 128,000 token context length, while still "fitting within a single RTX 4090 or a 32GB RAM MacBook once quantized" (according to their [model card](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503)). Mistral's own benchmarks show it outperforming Gemma 3 and GPT\-4o Mini, but I haven't seen confirmation from external benchmarks.

Despite their mention of a 32GB MacBook I haven't actually seen any quantized GGUF or MLX releases yet, which is a little surprising since they partnered with Ollama on launch day for their previous Mistral Small 3\. I expect we'll see various quantized models released by the community shortly.

The model *is* available via their [La Plateforme API](https://docs.mistral.ai/api/), which means you can access it via my [llm\-mistral](https://github.com/simonw/llm-mistral) plugin.

Here's the model describing [my photo of two pelicans in flight](https://static.simonwillison.net/static/2025/two-pelicans.jpg):

```
llm install llm-mistral
# Run this if you have previously installed the plugin:
llm mistral refresh
llm -m mistral/mistral-small-2503 'describe' \
  -a https://static.simonwillison.net/static/2025/two-pelicans.jpg
```

> The image depicts two brown pelicans in flight against a clear blue sky. Pelicans are large water birds known for their long bills and large throat pouches, which they use for catching fish. The birds in the image have long, pointed wings and are soaring gracefully. Their bodies are streamlined, and their heads and necks are elongated. The pelicans appear to be in mid\-flight, possibly gliding or searching for food. The clear blue sky in the background provides a stark contrast, highlighting the birds' silhouettes and making them stand out prominently.

I [added Mistral's API prices](https://github.com/simonw/tools/commit/f528e115e3fc487e3f5c5435d7cc04dd7314dd91) to my [tools.simonwillison.net/llm\-prices](https://tools.simonwillison.net/llm-prices) pricing calculator by pasting screenshots of [Mistral's pricing](https://mistral.ai/products/la-plateforme#pricing) tables [into Claude](https://claude.ai/share/a9313f0d-274c-48d2-9d77-346fe68556a5).

---

**Link** 2025\-03\-17 [suitenumerique/docs](https://github.com/suitenumerique/docs):

New open source (MIT licensed) collaborative text editing web application, similar to Google Docs or Notion, notable because it's a joint effort funded by the French and German governments and "currently onboarding the Netherlands".

It's built using Django and React:

> Docs is built on top of [Django Rest Framework](https://www.django-rest-framework.org/), [Next.js](https://nextjs.org/), [BlockNote.js](https://www.blocknotejs.org/), [HocusPocus](https://tiptap.dev/docs/hocuspocus/introduction) and [Yjs](https://yjs.dev/).

Deployments currently [require](https://github.com/suitenumerique/docs/blob/main/docs/installation.md) Kubernetes, PostgreSQL, memcached, an S3 bucket (or compatible) and an OIDC provider.

---

**Link** 2025\-03\-17 [OpenTimes](https://sno.ws/opentimes/):

Spectacular new open geospatial project by [Dan Snow](https://sno.ws/):

> OpenTimes is a database of pre\-computed, point\-to\-point travel times between United States Census geographies. It lets you download bulk travel time data for free and with no limits.

Here's [what I get](https://opentimes.org/?id=060816135022&mode=car#9.76/37.5566/-122.3085) for travel times by car from El Granada, California:

[![Isochrone map showing driving times from the El Granada census tract to other places in the San Francisco Bay Area](https://substackcdn.com/image/fetch/$s_!xHF0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9391ef99-9485-499c-9501-7e3bd2836c86_2120x1486.jpeg "Isochrone map showing driving times from the El Granada census tract to other places in the San Francisco Bay Area")](https://substackcdn.com/image/fetch/$s_!xHF0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9391ef99-9485-499c-9501-7e3bd2836c86_2120x1486.jpeg)

The technical details are *fascinating*:

> * The entire OpenTimes backend is just static Parquet files on [Cloudflare's R2](https://www.cloudflare.com/developer-platform/products/r2/). There's no RDBMS or running service, just files and a CDN. The whole thing costs about $10/month to host and costs nothing to serve. In my opinion, this is a *great* way to serve infrequently updated, large public datasets at low cost (as long as you partition the files correctly).

Sure enough, [R2 pricing](https://developers.cloudflare.com/r2/pricing/) charges "based on the total volume of data stored" \- $0\.015 / GB\-month for standard storage, then $0\.36 / million requests for "Class B" operations which include reads. They charge nothing for outbound bandwidth.

> * All travel times were calculated by pre\-building the inputs (OSM, OSRM networks) and then distributing the compute over [hundreds of GitHub Actions jobs](https://github.com/dfsnow/opentimes/actions/workflows/calculate-times.yaml). This worked shockingly well for this specific workload (and was also completely free).

Here's a [GitHub Actions run](https://github.com/dfsnow/opentimes/actions/runs/13094249792) of the [calculate\-times.yaml workflow](https://github.com/dfsnow/opentimes/blob/a6a5f7abcdd69559b3e29f360fe0ff0399dbb400/.github/workflows/calculate-times.yaml#L78-L80) which uses a matrix to run 255 jobs!

[![GitHub Actions run: calculate-times.yaml run by workflow_dispatch taking 1h49m to execute 255 jobs with names like run-job (2020-01) ](https://substackcdn.com/image/fetch/$s_!KX00!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f1e85fc-bb6d-4178-ac15-9a1b63a95e33_2576x1030.jpeg "GitHub Actions run: calculate-times.yaml run by workflow_dispatch taking 1h49m to execute 255 jobs with names like run-job (2020-01) ")](https://substackcdn.com/image/fetch/$s_!KX00!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f1e85fc-bb6d-4178-ac15-9a1b63a95e33_2576x1030.jpeg)

Relevant YAML:

```
  matrix:
    year: ${{ fromJSON(needs.setup-jobs.outputs.years) }}
    state: ${{ fromJSON(needs.setup-jobs.outputs.states) }}
```

Where those JSON files were created by the previous step, which reads in the year and state values from [this params.yaml file](https://github.com/dfsnow/opentimes/blob/a6a5f7abcdd69559b3e29f360fe0ff0399dbb400/data/params.yaml#L72-L132).

> * The query layer uses a single DuckDB database file with *views* that point to static Parquet files via HTTP. This lets you query a table with hundreds of billions of records after downloading just the \~5MB pointer file.

This is a really creative use of DuckDB's feature that lets you run queries against large data from a laptop using HTTP range queries to avoid downloading the whole thing.

The README shows [how to use that from R and Python](https://github.com/dfsnow/opentimes/blob/3439fa2c54af227e40997b4a5f55678739e0f6df/README.md#using-duckdb) \- I got this working in the `duckdb` client (`brew install duckdb`):

```
INSTALL httpfs;
LOAD httpfs;
ATTACH 'https://data.opentimes.org/databases/0.0.1.duckdb' AS opentimes;

SELECT origin_id, destination_id, duration_sec
  FROM opentimes.public.times
  WHERE version = '0.0.1'
      AND mode = 'car'
      AND year = '2024'
      AND geography = 'tract'
      AND state = '17'
      AND origin_id LIKE '17031%' limit 10;
```

In answer to a question about adding public transit times [Dan said](https://news.ycombinator.com/item?id=43392521#43393183):

> In the next year or so maybe. The biggest obstacles to adding public transit are:
> 
> * Collecting all the necessary scheduling data (e.g. GTFS feeds) for every transit system in the county. Not insurmountable since there are services that do this currently.
> * Finding a routing engine that can compute nation\-scale travel time matrices quickly. Currently, the two fastest open\-source engines I've tried (OSRM and Valhalla) don't support public transit for matrix calculations and the engines that do support public transit (R5, OpenTripPlanner, etc.) are too slow.

[GTFS](https://gtfs.org/) is a popular CSV\-based format for sharing transit schedules \- here's [an official list](https://gtfs.org/resources/data/) of available feed directories.

---

**Link** 2025\-03\-18 [Building and deploying a custom site using GitHub Actions and GitHub Pages](https://til.simonwillison.net/github-actions/github-pages):

I figured out a minimal example of how to use GitHub Actions to run custom scripts to build a website and then publish that static site to GitHub Pages. I turned [the example](https://github.com/simonw/minimal-github-pages-from-actions/) into a template repository, which should make getting started for a new project extremely quick.

I've needed this for various projects over the years, but today I finally put these notes together while setting up [a system](https://github.com/simonw/recent-california-brown-pelicans) for scraping the [iNaturalist](https://www.inaturalist.org/) API for recent sightings of the California Brown Pelican and converting those into an Atom feed that I can subscribe to in [NetNewsWire](https://netnewswire.com/):

[![Screenshot of a Brown Pelican sighting Atom feed in NetNewsWire showing a list of entries on the left sidebar and detailed view of "Brown Pelican at Art Museum, Isla Vista, CA 93117, USA" on the right with date "MAR 13, 2025 AT 10:40 AM", coordinates "34.4115542997, -119.8500448", and a photo of three brown pelicans in water near a dock with copyright text "(c) Ery, all rights reserved"](https://substackcdn.com/image/fetch/$s_!Y-gu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F91fb113f-70bf-42c8-8f2f-dd6217efbe21_980x1003.jpeg "Screenshot of a Brown Pelican sighting Atom feed in NetNewsWire showing a list of entries on the left sidebar and detailed view of \"Brown Pelican at Art Museum, Isla Vista, CA 93117, USA\" on the right with date \"MAR 13, 2025 AT 10:40 AM\", coordinates \"34.4115542997, -119.8500448\", and a photo of three brown pelicans in water near a dock with copyright text \"(c) Ery, all rights reserved\"")](https://substackcdn.com/image/fetch/$s_!Y-gu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F91fb113f-70bf-42c8-8f2f-dd6217efbe21_980x1003.jpeg)

I got Claude [to write](https://claude.ai/share/533a1d59-60db-4686-bd50-679dd01a585e) me [the script](https://github.com/simonw/recent-california-brown-pelicans/blob/81f87b378b6626e97eeca0719e89c87ace141816/to_atom.py) that converts the scraped JSON to atom.

**Update**: I just [found out](https://sfba.social/@kueda/114185945871929778) iNaturalist have their own atom feeds! Here's their own [feed of recent Pelican observations](https://www.inaturalist.org/observations.atom?verifiable=true&taxon_id=123829).

---

**Quote** 2025\-03\-19

> *An **agent** is something that acts in an environment; it does something. Agents include worms, dogs, thermostats, airplanes, robots, humans, companies, and countries.*

[David L. Poole and Alan K. Mackworth](https://artint.info/3e/html/ArtInt3e.Ch1.S1.html)

---

**Link** 2025\-03\-19 [My Thoughts on the Future of "AI"](https://nicholas.carlini.com/writing/2025/thoughts-on-future-ai.html):

Nicholas Carlini, previously deeply skeptical about the utility of LLMs, discusses at length his thoughts on where the technology might go.

He presents compelling, detailed arguments for both ends of the spectrum \- his key message is that it's best to maintain very wide error bars for what might happen next:

> I wouldn't be surprised if, in three to five years, language models are capable of performing most (all?) cognitive economically\-useful tasks beyond the level of human experts. And I also wouldn't be surprised if, in five years, the best models we have are better than the ones we have today, but only in “normal” ways where costs continue to decrease considerably and capabilities continue to get better but there's no fundamental paradigm shift that upends the world order. To deny the *potential* for either of these possibilities seems to me to be a mistake.

If LLMs do hit a wall, it's not at all clear what that wall might be:

> I still believe there is something fundamental that will get in the way of our ability to build LLMs that grow exponentially in capability. But I will freely admit to you now that I have no earthly idea what that limitation will be. I have no evidence that this line exists, other than to make some form of vague argument that when you try and scale something across many orders of magnitude, you'll probably run into problems you didn't see coming.

There's lots of great stuff in here. I particularly liked this explanation of how you get R1:

> You take DeepSeek v3, and ask it to solve a bunch of hard problems, and when it gets the answers right, you train it to do more of that and less of whatever it did when it got the answers wrong. The idea here is actually really simple, and it works surprisingly well.

---