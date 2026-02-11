# Claude 3.5 Haiku

*Plus monthnotes for October*

Published: 2024-11-05
Source: https://simonw.substack.com/p/claude-35-haiku

---

In this newsletter:

* Claude 3\.5 Haiku
* W̶e̶e̶k̶n̶o̶t̶e̶s̶ Monthnotes for October

Plus 14 links and 3 quotations

### **[Claude 3\.5 Haiku](https://simonwillison.net/2024/Nov/4/haiku/) \- 2024\-11\-04**

Anthropic [released Claude 3\.5 Haiku](https://www.anthropic.com/claude/haiku) today, a few days later than expected (they said it would be out by the end of October).

I was expecting this to be a complete replacement for their existing Claude 3 Haiku model, in the same way that Claude 3\.5 Sonnet eclipsed the existing Claude 3 Sonnet while maintaining the same pricing.

Claude 3\.5 Haiku is different. First, it doesn't (yet) support image inputs \- so Claude 3 Haiku remains the least expensive Anthropic model for handling those.

Secondly, it's not priced the same as the previous Haiku. That was $0\.25/million input and $1\.25/million for output \- the new 3\.5 Haiku is 4x that at $1/million input and $5/million output.

Anthropic [tweeted](https://twitter.com/anthropicai/status/1853498270724542658):

> During final testing, Haiku surpassed Claude 3 Opus, our previous flagship model, on many benchmarks—at a fraction of the cost.
> 
> As a result, we've increased pricing for Claude 3\.5 Haiku to reflect its increase in intelligence.

Given that Anthropic claim that their new Haiku out\-performs their older Claude 3 Opus (still $15/m input and $75/m output!) this price isn't disappointing, but it's a small surprise nonetheless.

#### **Accessing Claude 3\.5 Haiku with LLM**

I released a new version of my [llm\-claude\-3](https://github.com/simonw/llm-claude-3) plugin with support for the new model. You can install (or upgrade) the plugin and run it like this:

```
llm install --upgrade llm-claude-3
llm keys set claude
# Paste API key here
llm -m claude-3.5-haiku 'describe memory management in Rust'
```

Here's the [output from that prompt](https://gist.github.com/simonw/f5ff50e2d0af91876dd994d992277736).

#### **Comparing prices**

I added the new price to my [LLM pricing calculator](https://tools.simonwillison.net/llm-prices), which inspired me to extract this comparison table for the leading models from Gemini, Anthropic and OpenAI. Here they are sorted from least to most expensive:

[![](https://substackcdn.com/image/fetch/$s_!nz-e!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa6a97057-b995-42e2-bda9-3b94ce09ea02_982x472.jpeg)](https://substackcdn.com/image/fetch/$s_!nz-e!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa6a97057-b995-42e2-bda9-3b94ce09ea02_982x472.jpeg)

[Gemini 1\.5 Flash\-8B](https://developers.googleblog.com/en/gemini-15-flash-8b-is-now-generally-available-for-use/) remains the model to beat on pricing: it's 1/6th of the price of the new Haiku \- far less capable, but still extremely useful for tasks such as [audio transcription](https://simonwillison.net/2024/Oct/29/llm-multi-modal/#using-a-plugin-to-run-audio-and-video-against-gemini).

Also notable from Anthropic's [model comparison table](https://docs.anthropic.com/en/docs/about-claude/models#model-comparison-table): Claude 3\.5 Haiku has a max output of 8,192 tokens (same as 3\.5 Sonnet, but twice that of Claude 3 Opus and Claude 3 Haiku). 3\.5 Haiku has a training cut\-off date of July 2024, the most recent of any Anthropic model. 3\.5 Sonnet is April 2024 and the Claude 3 family are all August 2023\.

---

### **[W̶e̶e̶k̶n̶o̶t̶e̶s̶ Monthnotes for October](https://simonwillison.net/2024/Oct/30/monthnotes/) \- 2024\-10\-30**

I try to publish [weeknotes](https://simonwillison.net/tags/weeknotes/) at least once every two weeks. It's been four since the last entry, so I guess this one counts as monthnotes instead.

In my defense, the reason I've fallen behind on weeknotes is that I've been publishing a *lot* of long\-form blog entries this month.

#### **Plentiful LLM vendor news**

A lot of LLM stuff happened. OpenAI had their DevDay, which I used as an opportunity to [try out live blogging](https://simonwillison.net/2024/Oct/1/openai-devday-2024-live-blog/) for the first time. I figured out [video scraping](https://simonwillison.net/2024/Oct/17/video-scraping/) with Google Gemini and generally got excited about how incredibly inexpensive the Gemini models are. Anthropic launched [Computer Use](https://simonwillison.net/2024/Oct/22/computer-use/) and [JavaScript analysis](https://simonwillison.net/2024/Oct/24/claude-analysis-tool/), and the month ended with [GitHub Universe](https://simonwillison.net/2024/Oct/30/copilot-models/).

#### **My LLM tool goes multi\-modal**

My big achievement of the month was finally shipping [multi\-modal support for my LLM tool](https://simonwillison.net/2024/Oct/29/llm-multi-modal/). This has been almost a year in the making: GPT\-4 vision kicked off the new era of vision LLMs at OpenAI DevDay last November and I've been watching the space with keen interest ever since.

I had a couple of false starts at the feature, which was difficult at first because LLM acts as a cross\-model abstraction layer, and it's hard to design those effectively without plenty of examples of different models.

Initially I thought the feature would just be for images, but then Google Gemini launched the ability to feed in PDFs, audio files and videos as well. That's why I renamed it from `-i/--image` to `-a/--attachment` \- I'm glad I hadn't committed to the image UI before realizing that file attachments could be so much more.

I'm really happy with how the feature turned out. The one missing piece at the moment is local models: I prototyped some incomplete local model plugins to verify the API design would work, but I've not yet pushed any of them to a state where I think they're ready to release. My [research into mistral.rs](https://simonwillison.net/2024/Oct/19/mistralrs/) was part of that process.

Now that attachments have landed I'm free to start thinking about the next major LLM feature. I'm leaning towards tool usage: enough models have tool use / structured output capabilities now that I think I can design an abstraction layer that works across all of them. The combination of tool use with LLM's plugin system is really fun to think about.

#### **Blog entries**

* [You can now run prompts against images, audio and video in your terminal using LLM](https://simonwillison.net/2024/Oct/29/llm-multi-modal/)
* [Run a prompt to generate and execute jq programs using llm\-jq](https://simonwillison.net/2024/Oct/27/llm-jq/)
* [Notes on the new Claude analysis JavaScript code execution tool](https://simonwillison.net/2024/Oct/24/claude-analysis-tool/)
* [Initial explorations of Anthropic's new Computer Use capability](https://simonwillison.net/2024/Oct/22/computer-use/)
* [Everything I built with Claude Artifacts this week](https://simonwillison.net/2024/Oct/21/claude-artifacts/)
* [Running Llama 3\.2 Vision and Phi\-3\.5 Vision on a Mac with mistral.rs](https://simonwillison.net/2024/Oct/19/mistralrs/)
* [Experimenting with audio input and output for the OpenAI Chat Completion API](https://simonwillison.net/2024/Oct/18/openai-audio/)
* [Video scraping: extracting JSON data from a 35 second screen capture for less than 1/10th of a cent](https://simonwillison.net/2024/Oct/17/video-scraping/)
* [ChatGPT will happily write you a thinly disguised horoscope](https://simonwillison.net/2024/Oct/15/chatgpt-horoscopes/)
* [OpenAI DevDay: Let’s build developer tools, not digital God](https://simonwillison.net/2024/Oct/2/not-digital-god/)
* [OpenAI DevDay 2024 live blog](https://simonwillison.net/2024/Oct/1/openai-devday-2024-live-blog/)

#### **Releases**

* **[llm\-mistral 0\.7](https://github.com/simonw/llm-mistral/releases/tag/0.7)** \- 2024\-10\-29  
LLM plugin providing access to Mistral models using the Mistral API
* **[llm\-claude\-3 0\.6](https://github.com/simonw/llm-claude-3/releases/tag/0.6)** \- 2024\-10\-29  
LLM plugin for interacting with the Claude 3 family of models
* **[llm\-gemini 0\.3](https://github.com/simonw/llm-gemini/releases/tag/0.3)** \- 2024\-10\-29  
LLM plugin to access Google's Gemini family of models
* **[llm 0\.17](https://github.com/simonw/llm/releases/tag/0.17)** \- 2024\-10\-29  
Access large language models from the command\-line
* **[llm\-whisper\-api 0\.1\.1](https://github.com/simonw/llm-whisper-api/releases/tag/0.1.1)** \- 2024\-10\-27  
Run transcriptions using the OpenAI Whisper API
* **[llm\-jq 0\.1\.1](https://github.com/simonw/llm-jq/releases/tag/0.1.1)** \- 2024\-10\-27  
Write and execute jq programs with the help of LLM
* **[claude\-to\-sqlite 0\.2](https://github.com/simonw/claude-to-sqlite/releases/tag/0.2)** \- 2024\-10\-21  
Convert a Claude.ai export to SQLite
* **[files\-to\-prompt 0\.4](https://github.com/simonw/files-to-prompt/releases/tag/0.4)** \- 2024\-10\-16  
Concatenate a directory full of files into a single prompt for use with LLMs
* **[datasette\-examples 0\.1a0](https://github.com/datasette/datasette-examples/releases/tag/0.1a0)** \- 2024\-10\-08  
Load example SQL scripts into Datasette on startup
* **[datasette 0\.65](https://github.com/simonw/datasette/releases/tag/0.65)** \- 2024\-10\-07  
An open source multi\-tool for exploring and publishing data

#### **TILs**

* [Installing flash\-attn without compiling it](https://til.simonwillison.net/python/installing-flash-attention) \- 2024\-10\-25
* [Using uv to develop Python command\-line applications](https://til.simonwillison.net/python/uv-cli-apps) \- 2024\-10\-24
* [Setting cache\-control: max\-age\=31536000 with a Cloudflare Transform Rule](https://til.simonwillison.net/cloudflare/cache-control-transform-rule) \- 2024\-10\-24
* [Running prompts against images, PDFs, audio and video with Google Gemini](https://til.simonwillison.net/llms/prompt-gemini) \- 2024\-10\-23
* [The most basic possible Hugo site](https://til.simonwillison.net/hugo/basic) \- 2024\-10\-23
* [Livestreaming a community election event on YouTube](https://til.simonwillison.net/youtube/livestreaming) \- 2024\-10\-10
* [Upgrading Homebrew and avoiding the failed to verify attestation error](https://til.simonwillison.net/homebrew/no-verify-attestations) \- 2024\-10\-09
* [Collecting replies to tweets using JavaScript](https://til.simonwillison.net/twitter/collecting-replies) \- 2024\-10\-09
* [Compiling and running sqlite3\-rsync](https://til.simonwillison.net/sqlite/compile-sqlite3-rsync) \- 2024\-10\-04
* [Building an automatically updating live blog in Django](https://til.simonwillison.net/django/live-blog) \- 2024\-10\-02

---

**Link** 2024\-10\-30 [docs.jina.ai \- the Jina meta\-prompt](https://docs.jina.ai/):

From [Jina AI on Twitter](https://twitter.com/jinaai_/status/1851651702635847729):

> `curl docs.jina.ai` \- This is our **Meta\-Prompt**. It allows LLMs to understand our Reader, Embeddings, Reranker, and Classifier APIs for improved codegen. Using the meta\-prompt is straightforward. Just copy the prompt into your preferred LLM interface like ChatGPT, Claude, or whatever works for you, add your instructions, and you're set.

The page is served using content negotiation. If you hit it with `curl` you get plain text, but a browser with `text/html` in the `accept:` header gets an explanation along with a convenient copy to clipboard button.

[![Screenshot of an API documentation page for Jina AI with warning message, access instructions, and code sample. Contains text: Note: This content is specifically designed for LLMs and not intended for human reading. For human-readable content, please visit Jina AI. For LLMs/programmatic access, you can fetch this content directly: curl docs.jina.ai/v2 # or wget docs.jina.ai/v2 # or fetch docs.jina.ai/v2 You only see this as a HTML when you access docs.jina.ai via browser. If you access it via code/program, you will get a text/plain response as below. You are an AI engineer designed to help users use Jina AI Search Foundation API's for their specific use case. # Core principles...](https://substackcdn.com/image/fetch/$s_!d0eS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F02cc8f2f-dae0-491b-8d8c-0a38c6dc0c35_1319x1470.jpeg "Screenshot of an API documentation page for Jina AI with warning message, access instructions, and code sample. Contains text: Note: This content is specifically designed for LLMs and not intended for human reading. For human-readable content, please visit Jina AI. For LLMs/programmatic access, you can fetch this content directly: curl docs.jina.ai/v2 # or wget docs.jina.ai/v2 # or fetch docs.jina.ai/v2 You only see this as a HTML when you access docs.jina.ai via browser. If you access it via code/program, you will get a text/plain response as below. You are an AI engineer designed to help users use Jina AI Search Foundation API's for their specific use case. # Core principles...")](https://substackcdn.com/image/fetch/$s_!d0eS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F02cc8f2f-dae0-491b-8d8c-0a38c6dc0c35_1319x1470.jpeg)

---

**Link** 2024\-10\-30 [Creating a LLM\-as\-a\-Judge that drives business results](https://hamel.dev/blog/posts/llm-judge/):

Hamel Husain's sequel to [Your AI product needs evals](https://hamel.dev/blog/posts/evals/). This is *packed* with hard\-won actionable advice.

Hamel warns against using scores on a 1\-5 scale, instead promoting an alternative he calls "Critique Shadowing". Find a domain expert (one is better than many, because you want to keep their scores consistent) and have them answer the yes/no question "Did the AI achieve the desired outcome?" \- providing a critique explaining their reasoning for each of their answers.

This gives you a reliable score to optimize against, and the critiques mean you can capture nuance and improve the system based on that captured knowledge.

> Most importantly, **the critique should be detailed enough so that you can use it in a few\-shot prompt for a LLM judge**. In other words, it should be detailed enough that a new employee could understand it.

Once you've gathered this expert data system you can switch to using an LLM\-as\-a\-judge. You can then iterate on the prompt you use for it in order to converge its "opinions" with those of your domain expert.

Hamel concludes:

> The real value of this process is looking at your data and doing careful analysis. Even though an AI judge can be a helpful tool, going through this process is what drives results. I would go as far as saying that creating a LLM judge is a nice “hack” I use to trick people into carefully looking at their data!

---

**Link** 2024\-10\-31 [Australia/Lord\_Howe is the weirdest timezone](https://ssoready.com/blog/engineering/truths-programmers-timezones/):

Lord Howe Island \- part of Australia, population 382 \- is unique in that the island's standard time zone is UTC\+10:30 but is UTC\+11 when daylight saving time applies. It's the only time zone where DST represents a 30 minute offset.

---

**Link** 2024\-10\-31 [Cerebras Coder](https://www.val.town/v/stevekrouse/cerebras_coder):

Val Town founder Steve Krouse has been building demos on top of the Cerebras API that runs Llama3\.1\-70b at 2,000 tokens/second.

Having a capable LLM with that kind of performance turns out to be really interesting. Cerebras Coder is a demo that implements Claude Artifact\-style on\-demand JavaScript apps, and having it run at that speed means changes you request are visible within less than a second:

Steve's implementation (created with the help of [Townie](https://www.val.town/townie), the Val Town code assistant) demonstrates the simplest possible version of an iframe sandbox:

```
<iframe
    srcDoc={code}
    sandbox="allow-scripts allow-modals allow-forms allow-popups allow-same-origin allow-top-navigation allow-downloads allow-presentation allow-pointer-lock"
/>
```

Where `code` is populated by a `setCode(...)` call inside a React component.

The most interesting applications of LLMs continue to be where they operate in a tight loop with a human \- this can make those review loops potentially much faster and more productive.

---

**Link** 2024\-11\-01 [Control your smart home devices with the Gemini mobile app on Android](https://support.google.com/gemini/answer/15335456):

Google are adding smart home integration to their Gemini chatbot \- so far on Android only.

Have they considered the risk of prompt injection? It looks like they have, at least a bit:

> **Important**: Home controls are for convenience only, not safety\- or security\-critical purposes. Don't rely on Gemini for requests that could result in injury or harm if they fail to start or stop.
> 
> The Google Home extension can’t perform some actions on security devices, like gates, cameras, locks, doors, and garage doors. For unsupported actions, the Gemini app gives you a link to the Google Home app where you can control those devices.

It *can* control lights and power, climate control, window coverings, TVs and speakers and "other smart devices, like washers, coffee makers, and vacuums".

I imagine we will see some security researchers having a lot of fun with this shortly.

---

**Quote** 2024\-11\-01

> ***Lord Clement\-Jones**: To ask His Majesty's Government what assessment they have made of the cybersecurity risks posed by prompt injection attacks to the processing by generative artificial intelligence of material provided from outside government, and whether any such attacks have been detected thus far.  
>   
> **Lord Vallance of Balham**: Security is central to HMG's [Generative AI Framework](https://www.gov.uk/government/publications/generative-ai-framework-for-hmg/generative-ai-framework-for-hmg-html), which was published in January this year and sets out principles for using generative AI safely and responsibly. The risks posed by prompt injection attacks, including from material provided outside of government, have been assessed as part of this framework and are continually reviewed. The published Generative AI Framework for HMG specifically includes Prompt Injection attacks, alongside other AI specific cyber risks.*

[Question for Department for Science, Innovation and Technology](https://questions-statements.parliament.uk/written-questions/detail/2024-10-14/HL1541/)

---

**Link** 2024\-11\-01 [Claude API: PDF support (beta)](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support):

Claude 3\.5 Sonnet now accepts PDFs as attachments:

> The new Claude 3\.5 Sonnet (`claude-3-5-sonnet-20241022`) model now supports PDF input and understands both text and visual content within documents.

I just released [llm\-claude\-3 0\.7](https://github.com/simonw/llm-claude-3/releases/tag/0.7) with support for the new attachment type (attachments are [a very new feature](https://simonwillison.net/2024/Oct/29/llm-multi-modal/)), so now you can do this:

```
llm install llm-claude-3 --upgrade
llm -m claude-3.5-sonnet 'extract text' -a mydoc.pdf
```

Visual PDF analysis can also be turned on [for the Claude.ai application](https://claude.ai/new?fp=1):

[![Screenshot of a feature preview interface showing experimental features. At top: Feature Preview with beaker icon. Main text explains these are upcoming enhancements that may affect Claude's behavior. Shows options for Analysis tool, LaTeX Rendering, and Visual PDFs. Right panel demonstrates Visual PDFs feature with Apollo 17 flight plan image and chat messages. Toggle switch shows feature is Off. Description states Give Claude 3.5 Sonnet the ability to view and analyze images, charts, and graphs in PDFs, in addition to text. PDFs that are less than 100 pages are supported.](https://substackcdn.com/image/fetch/$s_!W5wu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe041c762-8c52-4587-9867-4bdc88f24303_1444x1082.jpeg "Screenshot of a feature preview interface showing experimental features. At top: Feature Preview with beaker icon. Main text explains these are upcoming enhancements that may affect Claude's behavior. Shows options for Analysis tool, LaTeX Rendering, and Visual PDFs. Right panel demonstrates Visual PDFs feature with Apollo 17 flight plan image and chat messages. Toggle switch shows feature is Off. Description states Give Claude 3.5 Sonnet the ability to view and analyze images, charts, and graphs in PDFs, in addition to text. PDFs that are less than 100 pages are supported.")](https://substackcdn.com/image/fetch/$s_!W5wu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe041c762-8c52-4587-9867-4bdc88f24303_1444x1082.jpeg)

Also new today: Claude now offers a free (albeit rate\-limited) [token counting API](https://docs.anthropic.com/en/docs/build-with-claude/token-counting). This addresses a complaint I've had for a while: previously it wasn't possible to accurately estimate the cost of a prompt before sending it to be executed.

---

**Link** 2024\-11\-01 [From Naptime to Big Sleep: Using Large Language Models To Catch Vulnerabilities In Real\-World Code](https://googleprojectzero.blogspot.com/2024/10/from-naptime-to-big-sleep.html):

Google's [Project Zero](https://en.wikipedia.org/wiki/Project_Zero) security team used a system based around Gemini 1\.5 Pro to find a previously unreported security vulnerability in SQLite (a stack buffer underflow), in time for it to be fixed prior to making it into a release.

A key insight here is that LLMs are well suited for checking for new variants of previously reported vulnerabilities:

> A key motivating factor for Naptime and now for Big Sleep has been the continued in\-the\-wild discovery of exploits for variants of previously found and patched vulnerabilities. As this trend continues, it's clear that fuzzing is not succeeding at catching such variants, and that for attackers, manual variant analysis is a cost\-effective approach.
> 
> We also feel that this variant\-analysis task is a better fit for current LLMs than the more general open\-ended vulnerability research problem. By providing a starting point – such as the details of a previously fixed vulnerability – we remove a lot of ambiguity from vulnerability research, and start from a concrete, well\-founded theory: "This was a previous bug; there is probably another similar one somewhere".

LLMs are great at pattern matching. It turns out feeding in a pattern describing a prior vulnerability is a great way to identify potential new ones.

---

**Link** 2024\-11\-02 [SmolLM2](https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct):

New from [Loubna Ben Allal](https://loubnabnl.github.io/) and her research team at Hugging Face:

> SmolLM2 is a family of compact language models available in three size: 135M, 360M, and 1\.7B parameters. They are capable of solving a wide range of tasks while being lightweight enough to run on\-device. \[...]
> 
> It was trained on 11 trillion tokens using a diverse dataset combination: FineWeb\-Edu, DCLM, The Stack, along with new mathematics and coding datasets that we curated and will release soon.

The model weights are released under an Apache 2 license. I've been trying these out using my [llm\-gguf](https://github.com/simonw/llm-gguf) plugin for [LLM](https://llm.datasette.io/) and my first impressions are really positive.

Here's a recipe to run a 1\.7GB Q8 quantized model [from lmstudio\-community](https://huggingface.co/lmstudio-community/SmolLM2-1.7B-Instruct-GGUF):

```
llm install llm-gguf
llm gguf download-model https://huggingface.co/lmstudio-community/SmolLM2-1.7B-Instruct-GGUF/resolve/main/SmolLM2-1.7B-Instruct-Q8_0.gguf -a smol17
llm chat -m smol17
```

[![Animated terminal demo. My prompt is tell me about pelicans. The model responds: Sure, I'd be happy to tell you about pelicans! Pelicans are a group of aquatic birds in the order Pelecaniformes, which also includes the cormorants, darters, and frigatebirds. They are found on all continents except Antarctica, and are known for their distinctive pouch-like bill. There are several species of pelicans. The most common species is the Brown Pelican, which is found in the Americas. It's the only species that plunges into water from a significant height to catch fish and other prey, a behavior known as "fish-grabbing."  Another common species is the American White Pelican, which can be found in both the Americas and Eurasia. It has a white plumage and a large, bright pink bill, and feeds on fish in lakes, rivers, and coastal wetlands.  Pelicans are generally medium-sized birds, but the Brown Pelican is the largest, with an average height of around 26-30 inches. Their bills can be as long as 11 inches!  Below the terminal you can see Activity Monitor showing 378% CPU usage for the Python process](https://substackcdn.com/image/fetch/$s_!L-g9!,w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4e9d09c-a216-469e-b083-4d402631a35e_952x533.gif "Animated terminal demo. My prompt is tell me about pelicans. The model responds: Sure, I'd be happy to tell you about pelicans! Pelicans are a group of aquatic birds in the order Pelecaniformes, which also includes the cormorants, darters, and frigatebirds. They are found on all continents except Antarctica, and are known for their distinctive pouch-like bill. There are several species of pelicans. The most common species is the Brown Pelican, which is found in the Americas. It's the only species that plunges into water from a significant height to catch fish and other prey, a behavior known as \"fish-grabbing.\"  Another common species is the American White Pelican, which can be found in both the Americas and Eurasia. It has a white plumage and a large, bright pink bill, and feeds on fish in lakes, rivers, and coastal wetlands.  Pelicans are generally medium-sized birds, but the Brown Pelican is the largest, with an average height of around 26-30 inches. Their bills can be as long as 11 inches!  Below the terminal you can see Activity Monitor showing 378% CPU usage for the Python process")](https://substackcdn.com/image/fetch/$s_!L-g9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4e9d09c-a216-469e-b083-4d402631a35e_952x533.gif)

Or at the other end of the scale, here's how to run the 138MB [Q8 quantized 135M model](https://huggingface.co/lmstudio-community/SmolLM2-135M-Instruct-GGUF):

```
llm gguf download-model https://huggingface.co/lmstudio-community/SmolLM2-135M-Instruct-GGUF/resolve/main/SmolLM2-135M-Instruct-Q8_0.gguf' -a smol135m
llm chat -m smol135m
```

The blog entry to accompany SmolLM2 should be coming soon, but in the meantime here's the entry from July introducing the first version: [SmolLM \- blazingly fast and remarkably powerful](https://huggingface.co/blog/smollm) .

---

**Link** 2024\-11\-02 [Please publish and share more](https://micro.webology.dev/2024/11/02/please-publish-and.html):

💯 to all of this by Jeff Triplett:

> Friends, I encourage you to publish more, indirectly meaning you should write more and then share it. \[...]
> 
> You don’t have to change the world with every post. You might publish a quick thought or two that helps encourage someone else to try something new, listen to a new song, or binge\-watch a new series.

Jeff shares my opinion on conclusions: giving myself permission to hit publish even when I haven't wrapped everything up neatly was a huge productivity boost for me:

> Our posts are done when you say they are. You do not have to fret about sticking to landing and having a perfect conclusion. Your posts, like this post, are done after we stop writing.

And another 💯 to this footnote:

> PS: Write and publish before you write your own static site generator or perfect blogging platform. We have lost billions of good writers to this side quest because they spend all their time working on the platform instead of writing.

---

**Link** 2024\-11\-02 [Claude Token Counter](https://tools.simonwillison.net/claude-token-counter):

Anthropic released a [token counting API](https://docs.anthropic.com/en/docs/build-with-claude/token-counting) for Claude a few days ago.

I built this tool for running prompts, images and PDFs against that API to count the tokens in them.

The API is free (albeit rate limited), but you'll still need to provide your own API key in order to use it.

[![Screenshot of a Claude Token Counter interface showing: Title Claude Token Counter, system prompt this counts tokens, user message You can attach images and PDFs too, file upload area with llm-jq-card.jpg and dxweb.pdf attached (both with Remove buttons), a Count Tokens button, and JSON output showing input_tokens: 3320](https://substackcdn.com/image/fetch/$s_!elW_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4fc0cbc1-0d04-4126-8cbb-adb093d9eaf8_755x866.jpeg "Screenshot of a Claude Token Counter interface showing: Title Claude Token Counter, system prompt this counts tokens, user message You can attach images and PDFs too, file upload area with llm-jq-card.jpg and dxweb.pdf attached (both with Remove buttons), a Count Tokens button, and JSON output showing input_tokens: 3320")](https://substackcdn.com/image/fetch/$s_!elW_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4fc0cbc1-0d04-4126-8cbb-adb093d9eaf8_755x866.jpeg)

Here's [the source code](https://github.com/simonw/tools/blob/main/claude-token-counter.html). I built this using two sessions with Claude \- one [to build the initial tool](https://gist.github.com/simonw/d6797005adf1688427470f9fcb8d287f)and a second [to add PDF and image support](https://gist.github.com/simonw/ebc1e32b9f3ddc0875ce8d875d7100bd). That second one is a bit of a mess \- it turns out if you drop an HTML file onto a Claude conversation it converts it to Markdown for you, but I wanted it to modify the original HTML source.

The API endpoint also allows you to specify a model, but as far as I can tell from running some experiments the token count was the same for Haiku, Opus and Sonnet 3\.5\.

---

**Link** 2024\-11\-03 [Docling](https://ds4sd.github.io/docling/):

MIT licensed document extraction Python library from the Deep Search team at IBM, who released [Docling v2](https://ds4sd.github.io/docling/v2/#changes-in-docling-v2) on October 16th.

Here's the [Docling Technical Report](https://arxiv.org/abs/2408.09869) paper from August, which provides details of two custom models: a layout analysis model for figuring out the structure of the document (sections, figures, text, tables etc) and a TableFormer model specifically for extracting structured data from tables.

Those models are [available on Hugging Face](https://huggingface.co/ds4sd/docling-models).

Here's how to try out the Docling CLI interface using `uvx` (avoiding the need to install it first \- though since it downloads models it will take a while to run the first time):

```
uvx docling mydoc.pdf --to json --to md
```

This will output a `mydoc.json` file with complex layout information and a `mydoc.md` Markdown file which includes Markdown tables where appropriate.

The [Python API](https://ds4sd.github.io/docling/usage/) is a lot more comprehensive. It can even extract tables [as Pandas DataFrames](https://ds4sd.github.io/docling/examples/export_tables/):

```
from docling.document_converter import DocumentConverter
converter = DocumentConverter()
result = converter.convert("document.pdf")
for table in result.document.tables:
    df = table.export_to_dataframe()
    print(df)
```

I ran that inside `uv run --with docling python`. It took a little while to run, but it demonstrated that the library works.

---

**Link** 2024\-11\-03 [California Clock Change](https://tools.simonwillison.net/california-clock-change):

The clocks go back in California tonight and I finally built my *dream* application for helping me remember if I get an hour extra of sleep or not, using a Claude Artifact. Here's [the transcript](https://gist.github.com/simonw/9510723176f5b44ac1ebc495c95a4bc7).

[![California Clock Change. For Pacific Time (PST/PDT) only. When you go to bed on Saturday, November 2, 2024That's tonight!, you will get an extra hour of sleep! The clocks fall back from 2:00 AM to 1:00 AM on Sunday, November 3, 2024.](https://substackcdn.com/image/fetch/$s_!QWX1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b2539d2-07a8-4dce-b3c5-af2b0668f9b7_1270x792.jpeg "California Clock Change. For Pacific Time (PST/PDT) only. When you go to bed on Saturday, November 2, 2024That's tonight!, you will get an extra hour of sleep! The clocks fall back from 2:00 AM to 1:00 AM on Sunday, November 3, 2024.")](https://substackcdn.com/image/fetch/$s_!QWX1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b2539d2-07a8-4dce-b3c5-af2b0668f9b7_1270x792.jpeg)

This is one of my favorite examples yet of the kind of tiny low stakes utilities I'm building with Claude Artifacts because the friction involved in churning out a working application has dropped almost to zero.

(I added another feature: it now [includes a note](https://fedi.simonwillison.net/@simon/113419979044849672)of what time my Dog thinks it is if the clocks have recently changed.)

---

**Quote** 2024\-11\-03

> *Building technology in startups is all about having the right level of tech debt. If you have none, you’re probably going too slow and not prioritizing product\-market fit and the important business stuff. If you get too much, everything grinds to a halt. Plus, tech debt is a “know it when you see it” kind of thing, and I know that my definition of “a bunch of tech debt” is, to other people, “very little tech debt.”*

[Tom MacWright](https://macwright.com/2024/10/25/good-software-knip)

---

**Link** 2024\-11\-04 [Nous Hermes 3](https://nousresearch.com/hermes3/):

The Nous Hermes family of fine\-tuned models have a solid reputation. Their most recent release came out in August, based on Meta's Llama 3\.1:

> Our training data aggressively encourages the model to follow the system and instruction prompts exactly and in an adaptive manner. Hermes 3 was created by fine\-tuning Llama 3\.1 8B, 70B and 405B, and training on a dataset of primarily synthetically generated responses. The model boasts comparable and superior performance to Llama 3\.1 while unlocking deeper capabilities in reasoning and creativity.

The model weights are [on Hugging Face](https://observablehq.com/@simonw/blog-to-newsletter), including GGUF versions of the [70B](https://huggingface.co/NousResearch/Hermes-3-Llama-3.1-70B-GGUF) and [8B](https://huggingface.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF)models. Here's how to try the 8B model (a 4\.58GB download) using the [llm\-gguf plugin](https://github.com/simonw/llm-gguf):

```
llm install llm-gguf
llm gguf download-model 'https://huggingface.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF/resolve/main/Hermes-3-Llama-3.1-8B.Q4_K_M.gguf' -a Hermes-3-Llama-3.1-8B
llm -m Hermes-3-Llama-3.1-8B 'hello in spanish'
```

Nous Research [partnered with Lambda Labs](https://lambdalabs.com/blog/unveiling-hermes-3-the-first-fine-tuned-llama-3.1-405b-model-is-on-lambdas-cloud) to provide inference APIs. It turns out Lambda host [quite a few models](https://docs.lambdalabs.com/public-cloud/lambda-chat-api/) now, currently providing free inference to users with [an API key](https://cloud.lambdalabs.com/api-keys).

I just released the first alpha of a [llm\-lambda\-labs](https://github.com/simonw/llm-lambda-labs)plugin. You can use that to try the larger 405b model (very hard to run on a consumer device) like this:

```
llm install llm-lambda-labs
llm keys set lambdalabs
# Paste key here
llm -m lambdalabs/hermes3-405b 'short poem about a pelican with a twist'
```

Here's [the source code](https://github.com/simonw/llm-lambda-labs/blob/0.1a0/llm_lambda_labs.py) for the new plugin, which I based on [llm\-mistral](https://github.com/simonw/llm-mistral). The plugin uses [httpx\-sse](https://pypi.org/project/httpx-sse/) to consume the stream of tokens from the API.

---

**Link** 2024\-11\-04 [New OpenAI feature: Predicted Outputs](https://platform.openai.com/docs/guides/latency-optimization#use-predicted-outputs):

Interesting new ability of the OpenAI API \- the first time I've seen this from any vendor.

If you know your prompt is mostly going to return the same content \- you're requesting an edit to some existing code, for example \- you can now send that content as a "prediction" and have GPT\-4o or GPT\-4o mini use that to accelerate the returned result.

OpenAI's documentation says:

> When providing a prediction, any tokens provided that are not part of the final completion are charged at completion token rates.

I initially misunderstood this as meaning you got a price reduction in addition to the latency improvement, but that's not the case: in the best possible case it will return faster and you won't be charged anything extra over the expected cost for the prompt, but the more it differs from your permission the more extra tokens you'll be billed for.

I ran the example from the documentation both with and without the prediction and got these results. Without the prediction:

```
"usage": {
  "prompt_tokens": 150,
  "completion_tokens": 118,
  "total_tokens": 268,
  "completion_tokens_details": {
    "accepted_prediction_tokens": 0,
    "audio_tokens": null,
    "reasoning_tokens": 0,
    "rejected_prediction_tokens": 0
  }
```

That took 5\.2 seconds and cost 0\.1555 cents.

With the prediction:

```
"usage": {
  "prompt_tokens": 166,
  "completion_tokens": 226,
  "total_tokens": 392,
  "completion_tokens_details": {
    "accepted_prediction_tokens": 49,
    "audio_tokens": null,
    "reasoning_tokens": 0,
    "rejected_prediction_tokens": 107
  }
```

That took 3\.3 seconds and cost 0\.2675 cents.

Further details [from OpenAI's Steve Coffey](https://twitter.com/stevendcoffey/status/1853582548225683814):

> We are using the prediction to do speculative decoding during inference, which allows us to validate large batches of the input in parallel, instead of sampling token\-by\-token!
> 
> \[...] If the prediction is 100% accurate, then you would see no cost difference. When the model diverges from your speculation, we do additional sampling to “discover” the net\-new tokens, which is why we charge rejected tokens at completion time rates.

---

**Quote** 2024\-11\-05

> *You already [know](https://www.nytimes.com/interactive/2024/07/18/opinion/trump-presidency-record.html) Donald Trump. He is [unfit](https://www.nytimes.com/interactive/2024/07/11/opinion/editorials/donald-trump-2024-unfit.html) to lead. [Watch him](https://www.nytimes.com/2024/10/22/opinion/donald-trump-ezra-klein-podcast.html). Listen to [those](https://www.nytimes.com/interactive/2024/09/26/opinion/donald-trump-personality-history.html) who know him [best](https://www.nytimes.com/interactive/2024/01/18/opinion/trump-cabinet-election-2024.html). He tried to [subvert](https://www.nytimes.com/2023/08/02/opinion/trump-jan-6-indictment.html) an election and remains a [threat](https://www.nytimes.com/2024/01/06/opinion/trump-2024-campaign-warning.html) to democracy. He helped overturn Roe, with terrible [consequences](https://www.nytimes.com/interactive/2024/10/17/opinion/dobbs-roe-abortion-stories.html). Mr. Trump's [corruption](https://www.nytimes.com/2024/04/10/opinion/trump-presidency-corruption.html) and [lawlessness](https://www.nytimes.com/interactive/2022/11/17/opinion/trump-five-major-investigations-dozens-of-ways-out.html) go [beyond](https://www.nytimes.com/2024/04/17/opinion/donald-trump-trial.html) [elections](https://www.nytimes.com/2023/08/15/opinion/editorials/trump-indictment-republicans.html): It's his whole [ethos](https://www.nytimes.com/2024/03/25/opinion/trump-al-capone.html). He [lies](https://www.nytimes.com/2024/07/24/opinion/trump-lies-charts-data.html) without [limit](https://www.nytimes.com/interactive/2024/10/25/opinion/what-trump-says.html). If he's re\-elected, the G.O.P. won't [restrain](https://www.nytimes.com/2024/07/13/opinion/trump-2024-election.html) him. Mr. Trump will use the [government](https://www.nytimes.com/2024/01/12/opinion/donald-trump-culture-decline.html) to go after [opponents](https://www.nytimes.com/2024/03/08/opinion/trump-2025-second-term.html?). He will pursue a [cruel](https://www.nytimes.com/2024/09/14/opinion/trump-debate-haitians-pets.html) policy of mass [deportations](https://www.nytimes.com/2024/10/18/opinion/trump-woodward-milley-mass-deportation.html). He will wreak havoc on the [poor](https://www.nytimes.com/2024/09/09/opinion/harris-trump-debate-issues.html), the [middle class](https://www.nytimes.com/2024/07/31/opinion/trump-threat-treasury-market.html) and [employers](https://www.nytimes.com/2024/06/23/opinion/ceo-trump-republican-support.html). Another Trump term will damage the [climate](https://www.nytimes.com/2024/04/20/opinion/trump-biden-climate-election.html), shatter [alliances](https://www.nytimes.com/2024/09/17/opinion/trump-harris-foreign-policy.html) and strengthen [autocrats](https://www.nytimes.com/2024/05/21/opinion/trump-foreign-policy.html). Americans should demand [better](https://www.nytimes.com/2024/09/30/opinion/editorials/kamala-harris-2024-endorsement.html). Vote.*

[NY Times Editorial Board](https://www.nytimes.com/interactive/2024/11/02/opinion/vote-harris-2024-election.html)

---