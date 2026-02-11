# Language models on the command-line

*Plus Datasette Studio, prompt injection against GitHub Copilot Chat and more*

Published: 2024-06-19
Source: https://simonw.substack.com/p/language-models-on-the-command-line

---

In this newsletter:

* Language models on the command\-line
* A homepage redesign for my blog's 22nd birthday
* Weeknotes: Datasette Studio and a whole lot of blogging

Plus 20 links and 7 quotations and 1 TIL

### [Language models on the command\-line](https://simonwillison.net/2024/Jun/17/cli-language-models/) \- 2024\-06\-17

I gave a talk about accessing Large Language Models from the command\-line last week as part of the [Mastering LLMs: A Conference For Developers \& Data Scientists](https://maven.com/parlance-labs/fine-tuning) six week long online conference. The talk focused on my [LLM](https://llm.datasette.io/) Python command\-line utility and ways you can use it (and [its plugins](https://llm.datasette.io/en/stable/plugins/index.html)) to explore LLMs and use them for useful tasks.

The talk was recorded and is available [on YouTube](https://www.youtube.com/watch?v=QUXQNi6jQ30). Here I've turned it into an [annotated presentation](https://simonwillison.net/tags/annotatedtalks/), with detailed notes and screenshots (there were no slides) to accompany the video.

Here’s [the full set of notes](https://simonwillison.net/2024/Jun/17/cli-language-models/).

---

### [A homepage redesign for my blog's 22nd birthday](https://simonwillison.net/2024/Jun/12/homepage-redesign/) \- 2024\-06\-12

This blog is 22 years old today! I wrote up [a whole bunch of higlights](https://simonwillison.net/2022/Jun/12/twenty-years/) for the 20th birthday a couple of years ago. Today I'm celebrating with something a bit smaller: I finally redesigned the homepage.

I publish three kinds of content on my blog: [entries](https://simonwillison.net/search/?type=entry) (like this one), "[blogmarks](https://simonwillison.net/search/?type=blogmark)" (aka annotated links) and [quotations](https://simonwillison.net/search/?type=quotation). Until recently the entries were the main feature on the (desktop) homepage, with blogmarks and quotations relegated to the sidebar.

Back in April I [implemented Markdown support](https://simonwillison.net/2024/Apr/25/blogmarks-that-use-markdown/) for my blogmarks, allowing me to include additional links and quotations in the body of those descriptions.

I was inspired in this by [Daring Fireball](https://daringfireball.net/), which has long published a combination of annotated links combined with longer essay style entries.

It turns out I *really like* posting longer\-form content attached to links! Here's one from [earlier today](https://simonwillison.net/2024/Jun/12/generative-ai-is-not-going-to-build-your-engineering-team/) which rivals my full entries in length.

These were looking pretty cramped in the sidebar:

[![Screenshot of my blog with a big entry about Thoughts on the WWDC 2024 keynote on the left and a sidebar with a long blogmark description in the sidebar on the right](https://substackcdn.com/image/fetch/$s_!Ahmj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8a16e10d-481b-4365-9ed8-1cc35bc3de7f_2070x1872.jpeg "Screenshot of my blog with a big entry about Thoughts on the WWDC 2024 keynote on the left and a sidebar with a long blogmark description in the sidebar on the right")](https://substackcdn.com/image/fetch/$s_!Ahmj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8a16e10d-481b-4365-9ed8-1cc35bc3de7f_2070x1872.jpeg)

So I've done a small redesign. The right hand column on my homepage now displays entries, quotations and blogmarks as a combined list, reusing the format I already had in place for the [tag page](https://simonwillison.net/tags/blogging/).

The right hand column is for "highlights", aka my longer form blog entries.

[![Screenshot of my blog with a blogmark on the left and a list of article headlines on the right](https://substackcdn.com/image/fetch/$s_!LEv3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0f57af03-354d-4627-b4ae-39935a42fc45_2178x1858.jpeg "Screenshot of my blog with a blogmark on the left and a list of article headlines on the right")](https://substackcdn.com/image/fetch/$s_!LEv3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0f57af03-354d-4627-b4ae-39935a42fc45_2178x1858.jpeg)

The mobile version of my site was already serving content mixed together like this, so this change mainly brings the desktop version in line with the mobile one.

Here's [the issue on GitHub](https://github.com/simonw/simonwillisonblog/issues/438) and [the commit that implemented the change](https://github.com/simonw/simonwillisonblog/commit/8e38a3f51ec50501fcb6fcc19a26acde2fa5cd4b).

---

### [Weeknotes: Datasette Studio and a whole lot of blogging](https://simonwillison.net/2024/Jun/19/datasette-studio/) \- 2024\-06\-19

I'm still spinning back up after my trip back to the UK, so actual time spent building things has been less than I'd like. I presented [an hour long workshop on command\-line LLM usage](https://simonwillison.net/2024/Jun/17/cli-language-models/), wrote five full blog entries (since my last weeknotes) and I've also been leaning more into short\-form link blogging \- a lot more prominent on this site now since my [homepage redesign](https://simonwillison.net/2024/Jun/12/homepage-redesign/) last week.

#### Datasette Studio

I ran a workshop for a data journalism class recently which included having students try running structured data extraction using [datasette\-extract](https://github.com/datasette/datasette-extract). I didn't want to talk them through installing Python etc on their own machines, so I instead took advantage of a project I've been tinkering with for a little while called **Datasette Studio**.

Datasette Studio is actually two things. The first is a [distribution of Datasette](https://github.com/datasette/datasette-studio) which bundles the core application along with a selection of plugins that greatly increase its capabilities as a tool for cleaning and analyzing data. You can install that like this:

```
pipx install datasette-studio
```

Then run `datasette-studio` to start the server or `datasette-studio install xyz` to install additional plugins.

Datasette Studio runs the [latest Datasette 1\.0 alpha](https://docs.datasette.io/en/1.0a13/), and will upgrade to 1\.0 stable as soon as that is released.

Quoting the [pyproject.toml file](https://github.com/datasette/datasette-studio/blob/main/pyproject.toml), the current list of plugins is this:

* [datasette\-edit\-schema](https://github.com/simonw/datasette-edit-schema)
* [datasette\-write\-ui](https://github.com/datasette/datasette-write-ui)
* [datasette\-configure\-fts](https://github.com/simonw/datasette-configure-fts)
* [datasette\-write](https://github.com/simonw/datasette-write)
* [datasette\-upload\-csvs](https://github.com/simonw/datasette-upload-csvs)
* [datasette\-enrichments](https://github.com/datasette/datasette-enrichments)
* [datasette\-enrichments\-quickjs](https://github.com/datasette/datasette-enrichments-quickjs)
* [datasette\-enrichments\-re2](https://github.com/datasette/datasette-enrichments-re2)
* [datasette\-enrichments\-jinja](https://github.com/datasette/datasette-enrichments-jinja)
* [datasette\-copyable](https://github.com/simonw/datasette-copyable)
* [datasette\-export\-database](https://github.com/datasette/datasette-export-database)
* [datasette\-enrichments\-gpt](https://github.com/datasette/datasette-enrichments-gpt)
* [datasette\-import](https://github.com/datasette/datasette-import)
* [datasette\-extract](https://github.com/datasette/datasette-extract)
* [datasette\-secrets](https://github.com/datasette/datasette-secrets)

I plan to grow this list over time. A neat thing about `datasette-studio` is that the entire application is defined by a single `pyproject.toml` that lists those dependecies and [sets up](https://github.com/datasette/datasette-studio/blob/b4bdc2ceadabc3b184ff960effb4de59506c2ee2/pyproject.toml#L37-L38) the `datasette-studio` CLI console script, which is then [published to PyPI](https://pypi.org/project/datasette-studio/).

The second part of Datasette Studio is a GitHub repository that's designed to help run it in GitHub Codespaces, with a very pleasing URL:

<https://github.com/datasette/studio>

Visit that page, click the green "Code" button and click "Create codespace on main" to launch a virtual machine running in GitHub's Azure environment, preconfigured to launch a private instance of Datasette as soon as the Codespace has started running.

[![Screenshot of the GitHub Codespaces UI running Datasette Studio](https://substackcdn.com/image/fetch/$s_!72wp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fadb451b4-7f9e-4727-afad-d3de6f00ac32_2395x1030.jpeg "Screenshot of the GitHub Codespaces UI running Datasette Studio")](https://substackcdn.com/image/fetch/$s_!72wp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fadb451b4-7f9e-4727-afad-d3de6f00ac32_2395x1030.jpeg)

You can then start using it directly \- uploading CSVs or JSON data, or even set your own OpenAI key (using the "Manage secrets" menu item) to enable OpenAI features such as GPT enrichments and structured data extraction.

I'm still fleshing out the idea, but I really like this as a starting point for a completely free Datasette trial environment that's entirely hosted (and paid for) by Microsoft/GitHub!

#### More blog improvements

In addition to the redesign of the homepage \- moving my linkblog and quotations out of the sidebar and into the main content, at least on desktop \- I've made a couple of other tweaks.

* I added [optional descriptions to my tags](https://simonwillison.net/2024/Jun/18/tags-with-descriptions/), so now pages like [/tags/datasette/](https://simonwillison.net/tags/datasette/) or [/tags/sqliteutils/](https://simonwillison.net/tags/sqliteutils/) can clarify themselves and link to the relevant projects.
* I [started displaying images in more places](https://github.com/simonw/simonwillisonblog/issues/444). I've been creating "social media card" images for many of my posts for a few years, to show up when those URLs are shared in places like Mastodon or Twitter or Discord or Slack. Those images now display in various places on my blog as well, including the homepage, search results and the tag pages. My [annotatedtalks tag page](https://simonwillison.net/tags/annotatedtalks/) looks a whole lot more interesting with accompanying presentation title slides.

#### Blog entries

* [Language models on the command\-line](https://simonwillison.net/2024/Jun/17/cli-language-models/)
* [A homepage redesign for my blog's 22nd birthday](https://simonwillison.net/2024/Jun/12/homepage-redesign/)
* [Thoughts on the WWDC 2024 keynote on Apple Intelligence](https://simonwillison.net/2024/Jun/10/apple-intelligence/)
* [Accidental prompt injection against RAG applications](https://simonwillison.net/2024/Jun/6/accidental-prompt-injection/)
* [Training is not the same as chatting: ChatGPT and other LLMs don't remember everything you say](https://simonwillison.net/2024/May/29/training-not-chatting/)

#### Releases

* **[datasette\-faiss 0\.2\.1](https://github.com/simonw/datasette-faiss/releases/tag/0.2.1)** \- 2024\-06\-17  
Maintain a FAISS index for specified Datasette tables
* **[datasette\-cluster\-map 0\.18\.2](https://github.com/simonw/datasette-cluster-map/releases/tag/0.18.2)** \- 2024\-06\-13  
Datasette plugin that shows a map for any data with latitude/longitude columns
* **[datasette 0\.64\.7](https://github.com/simonw/datasette/releases/tag/0.64.7)** \- 2024\-06\-12  
An open source multi\-tool for exploring and publishing data
* **[datasette\-studio 0\.1a4](https://github.com/datasette/datasette-studio/releases/tag/0.1a4)** \- 2024\-06\-05  
Datasette pre\-configured with useful plugins. Experimental alpha.

#### TILs

* [Upgrade Postgres.app on macOS](https://til.simonwillison.net/postgresql/upgrade-postgres-app) \- 2024\-06\-16
* [Cloudflare redirect rules with dynamic expressions](https://til.simonwillison.net/cloudflare/redirect-rules) \- 2024\-05\-29

---

**Quote** 2024\-06\-10

> *There is a big difference between tech as augmentation versus automation. Augmentation (think Excel and accountants) benefits workers while automation (think traffic lights versus traffic wardens) benefits capital.   
>   
> LLMs are controversial because the tech is best at augmentation but is being sold by lots of vendors as automation.*

[Dare Obasanjo](https://mas.to/@carnage4life/112593042823322764)

---

**Link** 2024\-06\-11 [Private Cloud Compute: A new frontier for AI privacy in the cloud](https://security.apple.com/blog/private-cloud-compute/):

Here are the details about Apple's Private Cloud Compute infrastructure, and they are pretty extraordinary.

The goal with PCC is to allow Apple to run larger AI models that won't fit on a device, but in a way that guarantees that private data passed from the device to the cloud cannot leak in any way \- not even to Apple engineers with SSH access who are debugging an outage.

This is an extremely challenging problem, and their proposed solution includes a wide range of new innovations in private computing.

The most impressive part is their approach to technically enforceable guarantees and verifiable transparency. How do you ensure that privacy isn't broken by a future code change? And how can you allow external experts to verify that the software running in your data center is the same software that they have independently audited?

> When we launch Private Cloud Compute, we’ll take the extraordinary step of making software images of every production build of PCC publicly available for security research. This promise, too, is an enforceable guarantee: user devices will be willing to send data only to PCC nodes that can cryptographically attest to running publicly listed software.

These code releases will be included in an "append\-only and cryptographically tamper\-proof transparency log" \- similar to [certificate transparency logs](https://en.wikipedia.org/wiki/Certificate_Transparency).

---

**Link** 2024\-06\-11 [Introducing Apple’s On\-Device and Server Foundation Models](https://machinelearning.apple.com/research/introducing-apple-foundation-models):

Apple Intelligence uses both on\-device and in\-the\-cloud models that were trained from scratch by Apple.

Their on\-device model is a 3B model that "outperforms larger models including Phi\-3\-mini, Mistral\-7B, and Gemma\-7B", while the larger cloud model is comparable to GPT\-3\.5\.

The language models were trained on unlicensed scraped data \- I was hoping they might have managed to avoid that, but sadly not:

> We train our foundation models on licensed data, including data selected to enhance specific features, as well as publicly available data collected by our web\-crawler, AppleBot.

The most interesting thing here is the way they apply fine\-tuning to the local model to specialize it for different tasks. Apple call these "adapters", and they use LoRA for this \- a technique first published [in 2021](https://arxiv.org/abs/2106.09685). This lets them run multiple on\-device models based on a shared foundation, specializing in tasks such as summarization and proof\-reading.

Here's the [section of the Platforms State of the Union talk](https://www.youtube.com/watch?v=YJZ5YcMsgD4&t=135s) that talks about the foundation models and their fine\-tuned variants.

As [Hamel Husain](https://twitter.com/HamelHusain/status/1800546715277357263) says:

> This talk from Apple is the best ad for fine tuning that probably exists.

The video also describes their approach to quantization:

> The next step we took is compressing the model. We leveraged state\-of\-the\-art quantization techniques to take a 16\-bit per parameter model down to an average of less than 4 bits per parameter to fit on Apple Intelligence\-supported devices, all while maintaining model quality.

Still no news on how their on\-device image model was trained. I'd love to find out it was trained exclusively using licensed imagery \- Apple [struck a deal with Shutterstock](https://9to5mac.com/2024/04/06/apple-ai-deal-shutterstock/) a few months ago.

---

**Link** 2024\-06\-11 [First Came ‘Spam.’ Now, With A.I., We’ve Got ‘Slop’](https://www.nytimes.com/2024/06/11/style/ai-search-slop.html):

First [the Guardian](https://simonwillison.net/2024/May/19/spam-junk-slop-the-latest-wave-of-ai-behind-the-zombie-internet/), now the NYT. I've apparently made a habit of getting quoted by journalists talking about slop!

I got the closing quote in this one:

> Society needs concise ways to talk about modern A.I. — both the positives and the negatives. ‘Ignore that email, it’s spam,’ and ‘Ignore that article, it’s slop,’ are both useful lessons.

---

**Quote** 2024\-06\-11

> *Apple’s terminology distinguishes between “personal intelligence,” on\-device and under their control, and “world knowledge,” which is prone to hallucinations – but is also what consumers expect when they use AI, and it’s what may replace Google search as the “point of first intent” one day soon.   
>   
> It’s wise for them to keep world knowledge separate, behind a very clear gate, but still engage with it. Protects the brand and hedges their bets.*

[Matt Webb](https://interconnected.org/home/2024/06/11/siri)

---

**Link** 2024\-06\-12 [Generative AI Is Not Going To Build Your Engineering Team For You](https://stackoverflow.blog/2024/06/10/generative-ai-is-not-going-to-build-your-engineering-team-for-you/):

This barnstormer of an essay is a long read by Charity Majors, and I find myself wanting to quote almost every paragraph.

It thoroughly and passionately debunks the idea that generative AI means that teams no longer need to hire junior programmers.

This is for several key reasons. First is the familiar pipeline argument \- we need juniors in order to grow new intermediate and senior engineers:

> Software is an apprenticeship industry. You can’t learn to be a software engineer by reading books. You can only learn by doing…and doing, and doing, and doing some more. No matter what your education consists of, most learning happens on the job—period. And it never ends! Learning and teaching are lifelong practices; they have to be, the industry changes so fast.
> 
> It takes a solid seven\-plus years to forge a competent software engineer. (Or as most job ladders would call it, a “senior software engineer”.) That’s many years of writing, reviewing, and deploying code every day, on a team alongside more experienced engineers. That’s just how long it seems to take.

What does it mean to be a senior engineer? It’s a lot more than just writing code:

> To me, being a senior engineer is not primarily a function of your ability to write code. It has far more to do with your ability to understand, maintain, explain, and manage a large body of software in production over time, as well as the ability to translate business needs into technical implementation. So much of the work is around crafting and curating these large, complex sociotechnical systems, and code is just one representation of these systems.
> 
> \[…]
> 
> People act like writing code is the hard part of software. It is not. It never has been, it never will be. **Writing code is the easiest part of software engineering**, and it’s getting easier by the day. The hard parts are what you do with that code—operating it, understanding it, extending it, and governing it over its entire lifecycle.

But I find the most convincing arguments are the ones about team structure itself:

> **Hiring engineers is about composing teams**. The smallest unit of software ownership is not the individual, it’s the team
> 
> \[…]
> 
> Have you ever been on a team packed exclusively with staff or principal engineers? It is *not fun*. That is not a high\-functioning team. There is only so much high\-level architecture and planning work to go around, there are only so many big decisions that need to be made. These engineers spend most of their time doing work that feels boring and repetitive, so they tend to over\-engineer solutions and/or cut corners—sometimes at the same time. They compete for the “fun” stuff and find reasons to pick technical fights with each other. They chronically under\-document and under\-invest in the work that makes systems simple and tractable.
> 
> \[…]
> 
> The best teams are ones where no one is bored, because every single person is working on something that challenges them and pushes their boundaries. The only way you can get this is by having a range of skill levels on the team.

Charity finishes with advice on hiring juniors, including ensuring that your organization is in the right shape to do so effectively.

> The only thing worse than never hiring any junior engineers is hiring them into an awful experience where they can’t learn anything.

Seriously though, read the whole thing. It contains such a density of accumulated engineering management wisdom.

---

**Quote** 2024\-06\-12

> *Contrast \[Apple Intelligence] to what OpenAI is trying to accomplish with its GPT models, or Google with Gemini, or Anthropic with Claude: those large language models are trying to incorporate all of the available public knowledge to know everything; it’s a dramatically larger and more difficult problem space, which is why they get stuff wrong. There is also a lot of stuff that they don’t know because that information is locked away — like all of the information on an iPhone.*

[Ben Thompson](https://observablehq.com/@simonw/blog-to-newsletter#)

---

**Link** 2024\-06\-12 [Datasette 0\.64\.7](https://docs.datasette.io/en/stable/changelog.html#v0-64-7):

A very minor dot\-fix release for Datasette stable, addressing [this bug](https://github.com/simonw/datasette/issues/2353) where Datasette running against the latest version of SQLite \- 3\.46\.0 \- threw an error on canned queries that included `:named` parameters in their SQL.

The root cause was Datasette using [a now invalid clever trick](https://github.com/simonw/datasette/blob/7437d40e5dd4d614bb769e16c0c1b96c6c19647f/datasette/utils/__init__.py#L1137-L1150) I came up with against the undocumented and unstable opcodes returned by a SQLite `EXPLAIN` query.

I asked on the SQLite forum and learned that the feature I was using was removed in [this commit to SQLite](https://sqlite.org/src/info/dd5977c9a8a418be). D. Richard Hipp [explains](https://sqlite.org/forum/forumpost/1cafc721009cef7f):

> The P4 parameter to OP\_Variable was not being used for anything. By omitting it, we make the prepared statement slightly smaller, reduce the size of the SQLite library by a few bytes, and help sqlite3\_prepare() and similar run slightly faster.

---

**Link** 2024\-06\-13 [PDF to Podcast](https://pdf-to-podcast.com/):

At first glance this project by Stephan Fitzpatrick is a cute demo of a terrible sounding idea... but then I tried it out and the results are weirdly effective. You can listen to a fake podcast version of the transformers paper, or upload your own PDF (with your own OpenAI API key) to make your own.

It's open source (Apache 2\) so I had a poke around in [the code](https://github.com/knowsuchagency/pdf-to-podcast). It gets a lot done with a single [180 line Python script](https://github.com/knowsuchagency/pdf-to-podcast/blob/512bfbdb4fd658ad4b301336020c4ea16cb69e18/main.py).

When I'm exploring code like this I always jump straight to [the prompt](https://github.com/knowsuchagency/pdf-to-podcast/blob/512bfbdb4fd658ad4b301336020c4ea16cb69e18/main.py#L47-L80) \- it's quite long, and starts like this:

> Your task is to take the input text provided and turn it into an engaging, informative podcast dialogue. The input text may be messy or unstructured, as it could come from a variety of sources like PDFs or web pages. Don't worry about the formatting issues or any irrelevant information; your goal is to extract the key points and interesting facts that could be discussed in a podcast. \[...]

So I grabbed a copy of it and pasted in [my blog entry about WWDC](https://simonwillison.net/2024/Jun/10/apple-intelligence/), which produced [this result](https://gist.github.com/simonw/edac62f6c11640abe98925cbc17f4ac3#apple-intelligence-a-deep-dive-into-the-future-of-ai) when I ran it through Gemini Flash using [llm\-gemini](https://github.com/simonw/llm-gemini):

`cat prompt.txt | llm -m gemini-1.5-flash-latest`

Then I piped the result through my [ospeak](https://simonwillison.net/2023/Nov/7/ospeak/) CLI tool for running text\-to\-speech with the OpenAI TTS models (after truncating to 690 tokens with [ttok](https://github.com/simonw/ttok) because it turned out to be slightly too long for the API to handle):

`llm logs --response | ttok -t 690 | ospeak -s -o wwdc-auto-podcast.mp3`

And [here's the result](https://static.simonwillison.net/static/2024/wwdc-auto-podcast.mp3) (3\.9MB 3m14s MP3\).

It's not as good as the PDF\-to\-Podcast version because Stephan has some [really clever code](https://github.com/knowsuchagency/pdf-to-podcast/blob/512bfbdb4fd658ad4b301336020c4ea16cb69e18/main.py#L115-L126) that uses different TTS voices for each of the characters in the transcript, but it's still a surprisingly fun way of repurposing text from my blog. I enjoyed listening to it while I was cooking dinner.

---

**Link** 2024\-06\-13 [Optimal SQLite settings for Django](https://gcollazo.com/optimal-sqlite-settings-for-django/):

Giovanni Collazo put the work in to figure out settings to make SQLite work well for production Django workloads. WAL mode and a `busy_timeout` of 5000 make sense, but the most interesting recommendation here is `"transaction_mode": "IMMEDIATE"` to avoid locking errors when a transaction is upgraded to a write transaction.

Giovanni's configuration depends on the new `"init_command"` support for SQLite PRAGMA options [introduced in Django 5\.1alpha](https://docs.djangoproject.com/en/5.1/ref/databases/#setting-pragma-options).

---

**Link** 2024\-06\-13 [tantivy\-cli](https://github.com/quickwit-oss/tantivy-cli):

I tried out this Rust based search engine today and I was very impressed.

[Tantivy](https://github.com/quickwit-oss/tantivy) is the core project \- it's an open source (MIT) Rust library that implements Lucene\-style full text search, with a very full set of features: BM25 ranking, faceted search, range queries, incremental indexing etc.

`tantivy-cli` offers a CLI wrapper around the Rust library. It's not actually as full\-featured as I hoped: it's intended as more of a demo than a full exposure of the library's features. The JSON API server it runs can only be used to run simple keyword or phrase searches for example, no faceting or filtering.

Tantivy's performance is fantastic. I was able to index the entire contents of my link blog in a fraction of a second.

I found [this post](https://fulmicoton.com/posts/behold-tantivy/) from 2017 where Tantivy creator Paul Masurel described the initial architecture of his new search side\-project that he created to help him learn Rust. Paul went on to found [Quickwit](https://quickwit.io/), an impressive looking analytics platform that uses Tantivy as one of its core components.

The [Python bindings](https://github.com/quickwit-oss/tantivy-py) for Tantivy look well maintained, wrapping the Rust library using [maturin](https://github.com/PyO3/maturin). Those are probably the best way for a developer like myself to really start exploring what it can do.

Also notable: the [Hacker News thread](https://news.ycombinator.com/item?id=40492834) has dozens of posts from happy Tantivy users reporting successful use on their projects.

---

**Link** 2024\-06\-13 [Transcripts on Apple Podcasts](https://podcasters.apple.com/support/5316-transcripts-on-apple-podcasts):

I missed this when it launched [back in March](https://www.apple.com/newsroom/2024/03/apple-introduces-transcripts-for-apple-podcasts/): the Apple Podcasts app now features searchable transcripts, including the ability to tap on text and jump to that point in the audio.

Confusingly, you can only tap to navigate using the view of the transcript that comes up when you hit the quote mark icon during playback \- if you click the Transcript link from the episode listing page you get a static transcript without the navigation option.

Transcripts are created automatically server\-side by Apple, or podcast authors can upload their own edited transcript using Apple Podcasts Connect.

---

**Quote** 2024\-06\-14

> *(Blaming something on “politics” is usually a way of accidentally confessing that you don’t actually understand the constraints someone is operating under, IMO.)*

[Charity Majors](https://charity.wtf/2022/06/13/advice-for-engineering-managers-who-want-to-climb-the-ladder/)

---

**Link** 2024\-06\-15 [Using DuckDB for Embeddings and Vector Search](https://blog.brunk.io/posts/similarity-search-with-duckdb/):

Sören Brunk's comprehensive tutorial combining DuckDB 1\.0, a subset of German Wikipedia from Hugging Face (loaded using Parquet), the [BGE M3](https://huggingface.co/BAAI/bge-m3) embedding model and DuckDB's [new vss extension](https://duckdb.org/2024/05/03/vector-similarity-search-vss.html) for implementing an HNSW vector index.

---

**Quote** 2024\-06\-15

> *I understand people are upset about AI art making it to the final cut, but please try to also google artist names and compare to their portfolio before accusing them of using AI. I'm genuinely pretty upset to be accused of this. It's no fun to work on your craft for decades and then be told by some 'detection site' that your work is machine generated and people are spreading this around as a fact.*

[Johanna Tarkela](https://twitter.com/johisart/status/1801751726694744155)

---

**Link** 2024\-06\-15 [Notes on upgrading by blog's Heroku database plan](https://github.com/simonw/simonwillisonblog/issues/439):

Heroku discontinued the "Basic" PostgreSQL plan I've been using for my blog, so I just upgraded to the new "essential\-0" tier. Here are my notes as a GitHub issue \- it was very straightforward, and I'm really only linking to it now to test that writes to the new database work correctly.   
  
I try to create an issue like this any time I do even a minor ops task, mainly so I have somewhere to drop screenshots of any web UI interactions for future reference.

---

**Link** 2024\-06\-16 [GitHub Copilot Chat: From Prompt Injection to Data Exfiltration](https://embracethered.com/blog/posts/2024/github-copilot-chat-prompt-injection-data-exfiltration/):

Yet another example of the same vulnerability we see time and time again.

If you build an LLM\-based chat interface that gets exposed to both private and untrusted data (in this case the code in VS Code that Copilot Chat can see) and your chat interface supports Markdown images, you have a data exfiltration prompt injection vulnerability.

The fix, applied by GitHub here, is to disable Markdown image references to untrusted domains. That way an attack can't trick your chatbot into embedding an image that leaks private data in the URL.

Previous examples: [ChatGPT itself](https://simonwillison.net/2023/Apr/14/new-prompt-injection-attack-on-chatgpt-web-version-markdown-imag/), [Google Bard](https://simonwillison.net/2023/Nov/4/hacking-google-bard-from-prompt-injection-to-data-exfiltration/), [Writer.com](https://simonwillison.net/2023/Dec/15/writercom-indirect-prompt-injection/), [Amazon Q](https://simonwillison.net/2024/Jan/19/aws-fixes-data-exfiltration/), [Google NotebookLM](https://simonwillison.net/2024/Apr/16/google-notebooklm-data-exfiltration/). I'm tracking them here using my new [markdownexfiltration tag](https://simonwillison.net/tags/markdownexfiltration/).

---

**TIL** 2024\-06\-16 [Upgrade Postgres.app on macOS](https://til.simonwillison.net/postgresql/upgrade-postgres-app):

I've been using [Postgres.app](https://postgresapp.com/) to run PostgreSQL on my Mac for years. I like that it's easy to install, gives me a task tray icon to control it and means I don't have to run a full Docker environment just to hack on projects like [my blog](https://github.com/simonw/simonwillisonblog). …

---

**Link** 2024\-06\-16 [Jina AI Reader](https://jina.ai/reader/):

Jina AI provide a number of different AI\-related platform products, including an excellent [family of embedding models](https://huggingface.co/collections/jinaai/jina-embeddings-v2-65708e3ec4993b8fb968e744), but one of their most instantly useful is Jina Reader, an API for turning any URL into Markdown content suitable for piping into an LLM.

Add `r.jina.ai` to the front of a URL to get back Markdown of that page, for example [https://r.jina.ai/https://simonwillison.net/2024/Jun/16/jina\-ai\-reader/](https://r.jina.ai/https://simonwillison.net/2024/Jun/16/jina-ai-reader/) \- in addition to converting the content to Markdown it also does a decent job of extracting just the content and ignoring the surrounding navigation.

The API is free but rate\-limited (presumably by IP) to 20 requests per minute without an API key or 200 request per minute with a free API key, and you can pay to increase your allowance beyond that.

The Apache 2 licensed source code for the hosted service is [on GitHub](https://github.com/jina-ai/reader) \- it's written in TypeScript and [uses Puppeteer](https://github.com/jina-ai/reader/blob/main/backend/functions/src/services/puppeteer.ts) to run [Readabiliy.js](https://github.com/mozilla/readability) and [Turndown](https://github.com/mixmark-io/turndown) against the scraped page.

It can also handle PDFs, which have their contents extracted [using PDF.js](https://github.com/jina-ai/reader/blob/main/backend/functions/src/services/pdf-extract.ts).

There's also a search feature, `s.jina.ai/search+term+goes+here`, which [uses the Brave Search API](https://github.com/jina-ai/reader/blob/main/backend/functions/src/services/brave-search.ts).

---

**Quote** 2024\-06\-16

> *We're adding the human touch, but that often requires a deep, developmental edit on a piece of writing. The grammar and word choice just sound weird. You're always cutting out flowery words like 'therefore' and 'nevertheless' that don't fit in casual writing. Plus, you have to fact\-check the whole thing because AI just makes things up, which takes forever because it's not just big ideas. AI hallucinates these flippant little things in throwaway lines that you'd never notice. \[...]   
>   
> It's tedious, horrible work, and they pay you next to nothing for it.*

[Catrina Cowart](https://www.bbc.com/future/article/20240612-the-people-making-ai-sound-more-human)

---

**Quote** 2024\-06\-17

> *Most people think that we format Go code with gofmt to make code look nicer or to end debates among team members about program layout. But the most important reason for gofmt is that if an algorithm defines how Go source code is formatted, then programs, like goimports or gorename or go fix, can edit the source code more easily, without introducing spurious formatting changes when writing the code back. This helps you maintain code over time.*

[Russ Cox](https://research.swtch.com/vgo-eng)

---

**Link** 2024\-06\-17 [How researchers cracked an 11\-year\-old password to a crypto wallet](https://www.wired.com/story/roboform-password-3-million-dollar-crypto-wallet/):

If you used the RoboForm password manager to generate a password prior to their 2015 bug fix that password was generated using a pseudo\-random number generator based on your device's current time \- which means an attacker may be able to brute\-force the password from a shorter list of options if they can derive the rough date when it was created.   
  
(In this case the password cracking was consensual, to recover a lost wallet, but this still serves as a warning to any RoboForm users with passwords from that era.)

---

**Link** 2024\-06\-17 [pkgutil.resolve\_name(name)](https://docs.python.org/3/library/pkgutil.html#pkgutil.resolve_name):

Adam Johnson pointed out this utility method, added to the Python standard library in Python 3\.9\. It lets you provide a string that specifies a Python identifier to import from a module \- a pattern frequently used in things like Django's configuration.

```
Path = pkgutil.resolve_name("pathlib:Path")

```

---

**Link** 2024\-06\-18 [Anthropic release notes](https://docs.anthropic.com/en/release-notes/overview):

Anthropic have started publishing release notes! Currently available for [their API](https://docs.anthropic.com/en/release-notes/api) and [their apps (mobile and web)](https://docs.anthropic.com/en/release-notes/claude-apps).

What I'd really like to see are release notes for the models themselves, though as far as I can tell there haven't been any updates to those since the Claude 3 models were first released (the Haiku model name in the API is still `claude-3-haiku-20240307` and Anthropic say they'll change that identifier after any updates to the model).

---

**Link** 2024\-06\-18 [Claude: Building evals and test cases](https://docs.anthropic.com/en/docs/build-with-claude/develop-tests):

More documentation updates from Anthropic: this section on writing evals for Claude is new today and includes Python code examples for a number of different evaluation techniques.

Included are several examples of the LLM\-as\-judge pattern, plus an example using cosine similarity and another that uses the new\-to\-me [Rouge](https://pypi.org/project/rouge/) Python library that implements the [ROUGE metric](https://aclanthology.org/W04-1013/) for evaluating the quality of summarized text.

---

**Link** 2024\-06\-18 [Tags with descriptions](https://simonwillison.net/dashboard/tags-with-descriptions/):

Tiny new feature on my blog: I can now add optional descriptions to my tag pages, for example on [datasette](https://simonwillison.net/tags/datasette/) and [sqliteutils](https://simonwillison.net/tags/sqliteutils/) and [promptinjection](https://simonwillison.net/tags/promptinjection/).

I built this feature on a live call this morning as an unplanned demonstration of GitHub's new [Copilot Workspace](https://githubnext.com/projects/copilot-workspace) feature, where you can run a prompt against a repository and have it plan, implement and file a pull request implementing a change to the code.

My prompt was:

> Add a feature that lets me add a description to my tag pages, stored in the database table for tags and visible on the /tags/x/ page at the top

It wasn't as compelling a demo as I expected: Copilot Workspace currently has to stream an entire copy of each file it modifies, which can take a long time if your codebase includes several large files that need to be changed.

It did create [a working implementation](https://github.com/simonw/simonwillisonblog/pull/443/commits/b48f4bd1c7ec6845b097ebc1f4fca02d97c468ef) on its first try, though I had given it an extra tip not to forget the database migration. I ended up making a bunch of changes myself before I shipped it, [listed in the pull request](https://github.com/simonw/simonwillisonblog/pull/443).

I've been using Copilot Workspace quite a bit recently as a code explanation tool \- I'll prompt it to e.g. "add architecture documentation to the README" on a random repository not owned by me, then read its initial plan to see what it's figured out without going all the way through to the implementation and PR phases. Example in [this tweet](https://twitter.com/simonw/status/1802432912568279441) where I figured out the rough design of the Jina AI Reader API for [this post](https://simonwillison.net/2024/Jun/16/jina-ai-reader/).

---

**Link** 2024\-06\-19 [I’ve stopped using box plots. Should you?](https://nightingaledvs.com/ive-stopped-using-box-plots-should-you/):

Nick Desbarats explains box plots (including with [this excellent short YouTube video](https://www.youtube.com/watch?v=iBq23-eQhp8)) and then discusses why he thinks "typically less than 20 percent" of participants in his workshops already understand how to read them.

A key problem is that they are unintuitive: a box plot has four sections, two thin lines (the top and bottom whisker segments) and two larger boxes, joined around the median. Each of these elements represents the same number of samples (one quartile each) but the thin lines v.s. thick boxes imply that the whiskers contain less samples than the boxes.

---

**Link** 2024\-06\-19 [About the Lawrence Times](https://lawrencekstimes.com/about/):

The town of Lawrence, Kansas is where [Django was born](https://simonwillison.net/2010/Aug/24/what-is-the-history/). I'm delighted to learn that it has a new independent online news publication as\-of March 2021 \- the Lawrence Times.

It's always exciting to see local media startups like this one, and they've been publishing for three years now supported by both advertiser revenue and optional paid subscriptions.

---