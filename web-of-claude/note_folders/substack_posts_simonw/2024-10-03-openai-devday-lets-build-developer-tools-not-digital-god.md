# OpenAI DevDay: Let’s build developer tools, not digital God

*News from OpenAI’s developer platform event*

Published: 2024-10-03
Source: https://simonw.substack.com/p/openai-devday-lets-build-developer

---

In this newsletter:

* OpenAI DevDay: Let’s build developer tools, not digital God
* Weeknotes: Three podcasts, two trips and a new plugin system

Plus 6 links and 3 quotations and 1 TIL

### **[OpenAI DevDay: Let’s build developer tools, not digital God](https://simonwillison.net/2024/Oct/2/not-digital-god/) \- 2024\-10\-02**

I had a fun time [live blogging OpenAI DevDay yesterday](https://simonwillison.net/2024/Oct/1/openai-devday-2024-live-blog/) \- I’ve now [shared notes](https://til.simonwillison.net/django/live-blog) about the live blogging system I threw other in a hurry on the day (with assistance from Claude and GPT\-4o). Now that the smoke has settled a little, here are my impressions from the event.

* [Compared to last year](https://simonw.static.observableusercontent.com/next/worker-lLzrCfCS.html#compared-to-last-year)
* [Prompt caching, aka the big price drop](https://simonw.static.observableusercontent.com/next/worker-lLzrCfCS.html#prompt-caching-aka-the-big-price-drop)
* [GPT\-4o audio via the new WebSocket Realtime API](https://simonw.static.observableusercontent.com/next/worker-lLzrCfCS.html#gpt-4o-audio-via-the-new-websocket-realtime-api)
* [Model distillation is fine\-tuning made much easier](https://simonw.static.observableusercontent.com/next/worker-lLzrCfCS.html#model-distillation-is-fine-tuning-made-much-easier)
* [Let’s build developer tools, not digital God](https://simonw.static.observableusercontent.com/next/worker-lLzrCfCS.html#let-s-build-developer-tools-not-digital-god)

#### **Compared to last year**

Comparison with the first DevDay in November 2023 are unavoidable. That event was much more keynote\-driven: just in the keynote OpenAI released GPT\-4 vision, and Assistants, and GPTs, and GPT\-4 Turbo (with a massive price drop), and their text\-to\-speech API. It felt more like a launch\-focused product event than something explicitly for developers.

This year was different. Media weren’t invited, there was no livestream, Sam Altman didn’t present the opening keynote (he was interviewed at the end of the day instead) and the new features, while impressive, were not as abundant.

Several features were released in the last few months that could have been saved for DevDay: GPT\-4o mini and the o1 model family are two examples. I’m personally happy that OpenAI are shipping features like that as they become ready rather than holding them back for an event.

I’m a bit surprised they didn’t talk about [Whisper Turbo](https://simonwillison.net/2024/Oct/1/whisper-large-v3-turbo-model/) at the conference though, released just the day before \- especially since that’s one of the few pieces of technology they release under an open source (MIT) license.

This was clearly intended as an event by developers, for developers. If you don’t build software on top of OpenAI’s platform there wasn’t much to catch your attention here.

As someone who **does** build software on top of OpenAI, there was a ton of valuable and interesting stuff.

#### **Prompt caching, aka the big price drop**

I was hoping we might see a price drop, seeing as there’s an ongoing pricing war between Gemini, Anthropic and OpenAI. We got one in an interesting shape: a [50% discount](https://openai.com/index/api-prompt-caching/) on input tokens for prompts with a shared prefix.

This isn’t a new idea: both Google Gemini and Claude offer a form of prompt caching discount, if you configure them correctly and make smart decisions about when and how the cache should come into effect.

The difference here is that OpenAI apply the discount automatically:

> API calls to supported models will automatically benefit from Prompt Caching on prompts longer than 1,024 tokens. The API caches the longest prefix of a prompt that has been previously computed, starting at 1,024 tokens and increasing in 128\-token increments. If you reuse prompts with common prefixes, we will automatically apply the Prompt Caching discount without requiring you to make any changes to your API integration.

50% off repeated long prompts is a pretty significant price reduction!

[Anthropic's Claude implementation](https://ai.google.dev/gemini-api/docs/caching) saves more money: 90% off rather than 50% \- but is significantly more work to put into play.

[Gemini’s caching](https://ai.google.dev/gemini-api/docs/caching) requires you to pay per hour to keep your cache warm which makes it extremely difficult to effectively build against in comparison to the other two.

It's worth noting that OpenAI are not the first company to offer automated caching discounts: [DeepSeek have offered that](https://platform.deepseek.com/api-docs/news/news0802/) through their API for a few months.

#### **GPT\-4o audio via the new WebSocket Realtime API**

Absolutely the biggest announcement of the conference: the [new Realtime API](https://openai.com/index/introducing-the-realtime-api/) is effectively the API version of ChatGPT advanced voice mode, a user\-facing feature that finally [rolled out to everyone](https://help.openai.com/en/articles/8400625-voice-mode-faq) just a week ago.

This means we can finally tap directly into GPT\-4o’s multimodal audio support: we can send audio directly into the model (without first transcribing it to text via something like Whisper), and we can have it directly return speech without needing to run a separate text\-to\-speech model.

The way they chose to expose this is interesting: it’s not (yet) part of their existing chat completions API, instead using an entirely new API pattern built around WebSockets.

[![JavaScript code handling WebSocket events](https://substackcdn.com/image/fetch/$s_!3qAN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F921b18c4-6398-4ac1-a6d2-c3a1149be81c_2048x1536.jpeg "JavaScript code handling WebSocket events")](https://substackcdn.com/image/fetch/$s_!3qAN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F921b18c4-6398-4ac1-a6d2-c3a1149be81c_2048x1536.jpeg)

They designed it like that because they wanted it to be as realtime as possible: the API lets you constantly stream audio and text in both directions, and even supports allowing users to speak over and interrupt the model!

So far the Realtime API supports text, audio and function call / tool usage \- but doesn't (yet) support image input (I've been assured that's coming soon). The combination of audio and function calling is super exciting alone though \- several of the demos at DevDay used these to build fun voice\-driven interactive web applications.

I like this WebSocket\-focused API design a lot. My only hesitation is that, since an API key is needed to open a WebSocket connection, actually running this in production involves spinning up an authenticating WebSocket proxy. I hope OpenAI can provide a less code\-intensive way of solving this in the future.

Code they showed during the event demonstrated using the native browser `WebSocket` class directly, but I can't find those code examples online now. I hope they publish it soon. For the moment the best things to look at are the [openai\-realtime\-api\-beta](https://github.com/openai/openai-realtime-api-beta) and [openai\-realtime\-console](https://github.com/openai/openai-realtime-console) repositories.

The new [playground/realtime](https://platform.openai.com/playground/realtime) debugging tool \- the OpenAI playground for the Realtime API \- is a lot of fun to try out too.

#### **Model distillation is fine\-tuning made much easier**

The other big developer\-facing announcements were around **model distillation**, which to be honest is more of a usability enhancement and minor rebranding of their existing [fine\-tuning features](https://platform.openai.com/docs/guides/fine-tuning).

OpenAI have offered fine\-tuning for a few years now, most recently against their GPT\-4o and GPT\-4o mini models. They’ve practically been begging people to try it out, offering [generous free tiers](https://openai.com/index/gpt-4o-fine-tuning/) in previous months:

> Today \[August 20th 2024] we’re launching fine\-tuning for GPT\-4o, one of the most requested features from developers. We are also offering 1M training tokens per day for free for every organization through September 23\.

That free offer has now been extended. A footnote on [the pricing page](https://openai.com/api/pricing/) today:

> Fine\-tuning for GPT\-4o and GPT\-4o mini is free up to a daily token limit through October 31, 2024\. For GPT\-4o, each qualifying org gets up to 1M complimentary training tokens daily and any overage will be charged at the normal rate of $25\.00/1M tokens. For GPT\-4o mini, each qualifying org gets up to 2M complimentary training tokens daily and any overage will be charged at the normal rate of $3\.00/1M tokens

The problem with fine\-tuning is that it’s *really*hard to do effectively. I tried it a couple of years ago myself against GPT\-3 \- just to apply tags to my blog content \- and got disappointing results which deterred me from spending more money iterating on the process.

To fine\-tune a model effectively you need to gather a high quality set of examples and you need to construct a robust set of automated evaluations. These are some of the most challenging (and least well understood) problems in the whole nascent field of prompt engineering.

OpenAI’s solution is a bit of a rebrand. “Model distillation” is a form of fine\-tuning where you effectively teach a smaller model how to do a task based on examples generated by a larger model. It’s a very effective technique. Meta [recently boasted about](https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/) how their impressive Llama 3\.2 1B and 3B models were “taught” by their larger models:

> \[...] powerful teacher models can be leveraged to create smaller models that have improved performance. We used two methods—pruning and distillation—on the 1B and 3B models, making them the first highly capable lightweight Llama models that can fit on devices efficiently.

Yesterday OpenAI released two new features to help developers implement this pattern.

The first is **stored completions**. You can now pass [a "store": true parameter](https://platform.openai.com/docs/api-reference/chat/create#chat-create-store) to have OpenAI permanently store your prompt and its response in their backend, optionally with your own [additional tags](https://platform.openai.com/docs/api-reference/chat/create#chat-create-metadata) to help you filter the captured data later.

You can view your stored completions at [platform.openai.com/chat\-completions](https://platform.openai.com/chat-completions).

I’ve been doing effectively the same thing with my [LLM command\-line tool](https://llm.datasette.io/) logging to [a SQLite database](https://llm.datasette.io/en/stable/logging.html) for over a year now. It's a really productive pattern.

OpenAI pitch stored completions as a great way to collect a set of training data from their large models that you can later use to fine\-tune (aka distill into) a smaller model.

The second, even more impactful feature, is **evals**. You can now define and run comprehensive prompt evaluations directly inside the OpenAI platform.

[![Screenshot of a web interface showing evaluation results for an AI model named 'quick-reply-2-4o'. The interface displays a table with columns for messages, output, and three evaluation metrics: 'repliesToRightPerson', 'repliesToMostPressingIssue', and 'repliesMakeSense'. The table shows 8 rows of data, each representing a different conversation. Overall metrics at the top indicate 95%, 91%, and 97% success rates for the three evaluation criteria respectively. The interface appears to be part of a platform called 'Distillation Test' in a 'DevDay Demo' project.](https://substackcdn.com/image/fetch/$s_!JaT9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F07e0baaf-4cab-4d99-b332-880f2d3aa6b7_2016x1099.jpeg "Screenshot of a web interface showing evaluation results for an AI model named 'quick-reply-2-4o'. The interface displays a table with columns for messages, output, and three evaluation metrics: 'repliesToRightPerson', 'repliesToMostPressingIssue', and 'repliesMakeSense'. The table shows 8 rows of data, each representing a different conversation. Overall metrics at the top indicate 95%, 91%, and 97% success rates for the three evaluation criteria respectively. The interface appears to be part of a platform called 'Distillation Test' in a 'DevDay Demo' project.")](https://substackcdn.com/image/fetch/$s_!JaT9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F07e0baaf-4cab-4d99-b332-880f2d3aa6b7_2016x1099.jpeg)

OpenAI’s [new eval tool](https://platform.openai.com/docs/guides/evals) competes directly with a bunch of existing startups \- I’m quite glad I didn’t invest much effort in this space myself!

The combination of evals and stored completions certainly seems like it should make the challenge of fine\-tuning a custom model far more tractable.

The other fine\-tuning an announcement, greeted by applause in the room, was [fine\-tuning for images](https://openai.com/index/introducing-vision-to-the-fine-tuning-api/). This has always felt like one of the most obviously beneficial fine\-tuning use\-cases for me, since it’s much harder to get great image recognition results from sophisticated prompting alone.

From a strategic point of view this makes sense as well: it has become increasingly clear over the last year that many prompts are inherently transferable between models \- it’s very easy to take an application with prompts designed for GPT\-4o and switch it to Claude or Gemini or Llama with few if any changes required.

A fine\-tuned model on the OpenAI platform is likely to be far more sticky.

#### **Let’s build developer tools, not digital God**

In the last session of the day I furiously live blogged [the Fireside Chat](https://simonwillison.net/2024/Oct/1/openai-devday-2024-live-blog/#live-update-140) between Sam Altman and Kevin Weil, trying to capture as much of what they were saying as possible.

A bunch of the questions were about AGI. I’m personally quite uninterested in AGI: it’s always felt a bit too much like science fiction for me. I want useful AI\-driven tools that help me solve the problems I want to solve.

One point of frustration: Sam referenced OpenAI’s five\-level framework a few times. I found several news stories (many paywalled \- here's [one that isn't](https://arstechnica.com/information-technology/2024/07/openai-reportedly-nears-breakthrough-with-reasoning-ai-reveals-progress-framework/)) about it but I can’t find a definitive URL on an OpenAI site that explains what it is! This is why you should always [Give people something to link to so they can talk about your features and ideas](https://simonwillison.net/2024/Jul/13/give-people-something-to-link-to/).

Both Sam and Kevin seemed to be leaning away from AGI as a term. From my live blog notes (which paraphrase what was said unless I use quotation marks):

> Sam says they're trying to avoid the term now because it has become so over\-loaded. Instead they think about their new five steps framework.
> 
> "I feel a little bit less certain on that" with respect to the idea that an AGI will make a new scientific discovery.
> 
> Kevin: "There used to be this idea of AGI as a binary thing \[...] I don't think that's how think about it any more".
> 
> Sam: Most people looking back in history won't agree when AGI happened. The turing test wooshed past and nobody cared.

I for one found this very reassuring. The thing I want from OpenAI is more of what we got yesterday: I want platform tools that I can build unique software on top of which I colud not have built previously.

If the ongoing, well\-documented internal turmoil at OpenAI from the last year is a result of the organization reprioritizing towards shipping useful, reliable tools for developers (and consumers) over attempting to build a digital God, then I’m all for it.

And yet… OpenAI [just this morning](https://openai.com/index/scale-the-benefits-of-ai/) finalized a raise of another $6\.5 billion dollars at a staggering $157 billion post\-money valuation. That feels more like a digital God valuation to me than a platform for developers in an increasingly competitive space.

---

### **[Weeknotes: Three podcasts, two trips and a new plugin system](https://simonwillison.net/2024/Sep/30/weeknotes/) \- 2024\-09\-30**

I fell behind a bit on my weeknotes. Here's most of what I've been doing in September.

#### **Lisbon, Portugal and Durham, North Carolina**

I had two trips this month. The first was a short visit to Lisbon, Portugal for the Python Software Foundation's annual board retreat. This inspired me to write about [Things I've learned serving on the board of the Python Software Foundation](https://simonwillison.net/2024/Sep/18/board-of-the-python-software-foundation/).

The second was to Durham, North Carolina for DjangoCon US 2024\. I wrote about that one in [Themes from DjangoCon US 2024](https://simonwillison.net/2024/Sep/27/themes-from-djangocon-us-2024/).

My talk at DjangoCon was about plugin systems, and in a classic example of conference\-driven development I ended up writing and releasing a new plugin system for Django in preparation for that talk. I introduced that in [DJP: A plugin system for Django](https://simonwillison.net/2024/Sep/25/djp-a-plugin-system-for-django/).

#### **Podcasts**

I haven't been a podcast guest [since January](https://simonwillison.net/search/?year=2024&month=1&tag=podcasts), and then three came along at once! All three appearences involved LLMs in some way but I don't think there was a huge amount of overlap in terms of what I actually said.

* I went on [The Software Misadventures Podcast](https://simonwillison.net/2024/Sep/10/software-misadventures/) to talk about my career to\-date.
* My appearance [on TWIML](https://simonwillison.net/2024/Sep/20/using-llms-for-code/) dug into ways in which I use Claude and ChatGPT to help me write code.
* I was the guest for the inaugral episode of Gergely Orosz's [Pragmatic Engineer Podcast](https://newsletter.pragmaticengineer.com/p/ai-tools-for-software-engineers-simon-willison), which ended up touching on a whole array of different topics relevant to modern software engineering, from the importance of open source to the impact AI tools are likely to have on our industry.

Gergely has been sharing neat edited snippets from our conversation on Twitter. Here's [one on RAG](https://twitter.com/GergelyOrosz/status/1839682428471779596) and another about [how open source has been the the biggest productivity boost](https://twitter.com/GergelyOrosz/status/1840779737297260646) of my career.

#### **On the blog**

* [NotebookLM's automatically generated podcasts are surprisingly effective](https://simonwillison.net/2024/Sep/29/notebooklm-audio-overview/) \- Sept. 29, 2024
* [Themes from DjangoCon US 2024](https://simonwillison.net/2024/Sep/27/themes-from-djangocon-us-2024/) \- Sept. 27, 2024
* [DJP: A plugin system for Django](https://simonwillison.net/2024/Sep/25/djp-a-plugin-system-for-django/) \- Sept. 25, 2024
* [Notes on using LLMs for code](https://simonwillison.net/2024/Sep/20/using-llms-for-code/) \- Sept. 20, 2024
* [Things I've learned serving on the board of the Python Software Foundation](https://simonwillison.net/2024/Sep/18/board-of-the-python-software-foundation/) \- Sept. 18, 2024
* [Notes on OpenAI's new o1 chain\-of\-thought models](https://simonwillison.net/2024/Sep/12/openai-o1/) \- Sept. 12, 2024
* [Notes from my appearance on the Software Misadventures Podcast](https://simonwillison.net/2024/Sep/10/software-misadventures/) \- Sept. 10, 2024
* [Teresa T is name of the whale in Pillar Point Harbor near Half Moon Bay](https://simonwillison.net/2024/Sep/8/teresa-t-whale-pillar-point/) \- Sept. 8, 2024

#### **Museums**

* [The Vincent and Ethel Simonetti Historic Tuba Collection](https://www.niche-museums.com/112)

#### **Releases**

* **[shot\-scraper 1\.5](https://github.com/simonw/shot-scraper/releases/tag/1.5)** \- 2024\-09\-27  
A command\-line utility for taking automated screenshots of websites
* **[django\-plugin\-datasette 0\.2](https://github.com/simonw/django-plugin-datasette/releases/tag/0.2)** \- 2024\-09\-26  
Django plugin to run Datasette inside of Django
* **[djp 0\.3\.1](https://github.com/simonw/djp/releases/tag/0.3.1)** \- 2024\-09\-26  
A plugin system for Django
* **[llm\-gemini 0\.1a5](https://github.com/simonw/llm-gemini/releases/tag/0.1a5)** \- 2024\-09\-24  
LLM plugin to access Google's Gemini family of models
* **[django\-plugin\-blog 0\.1\.1](https://github.com/simonw/django-plugin-blog/releases/tag/0.1.1)** \- 2024\-09\-24  
A blog for Django as a DJP plugin.
* **[django\-plugin\-database\-url 0\.1](https://github.com/simonw/django-plugin-database-url/releases/tag/0.1)** \- 2024\-09\-24  
Django plugin for reading the DATABASE\_URL environment variable
* **[django\-plugin\-django\-header 0\.1\.1](https://github.com/simonw/django-plugin-django-header/releases/tag/0.1.1)** \- 2024\-09\-23  
Add a Django\-Compositions HTTP header to a Django app
* **[llm\-jina\-api 0\.1a0](https://github.com/simonw/llm-jina-api/releases/tag/0.1a0)** \- 2024\-09\-20  
Access Jina AI embeddings via their API
* **[llm 0\.16](https://github.com/simonw/llm/releases/tag/0.16)** \- 2024\-09\-12  
Access large language models from the command\-line
* **[datasette\-acl 0\.4a4](https://github.com/datasette/datasette-acl/releases/tag/0.4a4)** \- 2024\-09\-10  
Advanced permission management for Datasette
* **[llm\-cmd 0\.2a0](https://github.com/simonw/llm-cmd/releases/tag/0.2a0)** \- 2024\-09\-09  
Use LLM to generate and execute commands in your shell
* **[files\-to\-prompt 0\.3](https://github.com/simonw/files-to-prompt/releases/tag/0.3)** \- 2024\-09\-09  
Concatenate a directory full of files into a single prompt for use with LLMs
* **[json\-flatten 0\.3\.1](https://github.com/simonw/json-flatten/releases/tag/0.3.1)** \- 2024\-09\-07  
Python functions for flattening a JSON object to a single dictionary of pairs, and unflattening that dictionary back to a JSON object
* **[csv\-diff 1\.2](https://github.com/simonw/csv-diff/releases/tag/1.2)** \- 2024\-09\-06  
Python CLI tool and library for diffing CSV and JSON files
* **[datasette 1\.0a16](https://github.com/simonw/datasette/releases/tag/1.0a16)** \- 2024\-09\-06  
An open source multi\-tool for exploring and publishing data
* **[datasette\-search\-all 1\.1\.4](https://github.com/simonw/datasette-search-all/releases/tag/1.1.4)** \- 2024\-09\-06  
Datasette plugin for searching all searchable tables at once

#### **TILs**

* [How streaming LLM APIs work](https://til.simonwillison.net/llms/streaming-llm-apis) \- 2024\-09\-21

---

**Quote** 2024\-09\-30

> *But in terms of the responsibility of journalism, we do have intense fact\-checking because we want it to be right. Those big stories are aggregations of incredible journalism. So it cannot function without journalism. Now, we recheck it to make sure it's accurate or that it hasn't changed, but we're building this to make jokes. It's just we want the foundations to be solid or those jokes fall apart. **Those jokes have no structural integrity if the facts underneath them are bullshit**.*

[John Oliver](https://www.youtube.com/watch?v=Q9kNMJ8SguQ&t=995s)

---

**Link** 2024\-09\-30 [llama\-3\.2\-webgpu](https://huggingface.co/spaces/webml-community/llama-3.2-webgpu):

Llama 3\.2 1B is a really interesting models, given its 128,000 token input and its tiny size (barely more than a GB).

This page loads a [1\.24GB q4f16 ONNX build](https://huggingface.co/onnx-community/Llama-3.2-1B-Instruct-q4f16/tree/main/onnx) of the Llama\-3\.2\-1B\-Instruct model and runs it with a React\-powered chat interface directly in the browser, using [Transformers.js](https://huggingface.co/docs/transformers.js/en/index) and WebGPU. [Source code for the demo is here](https://github.com/huggingface/transformers.js-examples/tree/main/llama-3.2-webgpu).

It worked for me just now in Chrome; in Firefox and Safari I got a “WebGPU is not supported by this browser” error message.

---

**Link** 2024\-09\-30 [Conflating Overture Places Using DuckDB, Ollama, Embeddings, and More](https://www.dbreunig.com/2024/09/27/conflating-overture-points-of-interests-with-duckdb-ollama-and-more.html):

Drew Breunig's detailed tutorial on "conflation" \- combining different geospatial data sources by de\-duplicating address strings such as `RESTAURANT LOS ARCOS,3359 FOOTHILL BLVD,OAKLAND,94601` and `LOS ARCOS TAQUERIA,3359 FOOTHILL BLVD,OAKLAND,94601`.

Drew uses an entirely offline stack based around Python, DuckDB and Ollama and finds that a combination of H3 geospatial tiles and `mxbai-embed-large` embeddings (though other embedding models should work equally well) gets really good results.

---

**Quote** 2024\-09\-30

> *I listened to the whole 15\-minute podcast this morning. It was, indeed, surprisingly effective. It remains somewhere in the uncanny valley, but not at all in a creepy way. Just more in a “this is a bit vapid and phony” way. \[...] But ultimately the conversation has all the flavor of a bowl of unseasoned white rice.*

[John Gruber](https://daringfireball.net/linked/2024/09/30/notebooklm-generated-podcasts)

---

**Link** 2024\-09\-30 [Bop Spotter](https://walzr.com/bop-spotter/):

Riley Walz: "I installed a box high up on a pole somewhere in the Mission of San Francisco. Inside is a crappy Android phone, set to Shazam constantly, 24 hours a day, 7 days a week. It's solar powered, and the mic is pointed down at the street below."

Some [details on how it works](https://twitter.com/rtwlz/status/1840821351055311245) from Riley on Twitter:

> The phone has a Tasker script running on loop (even if the battery dies, it’ll restart when it boots again)
> 
> Script records 10 min of audio in airplane mode, then comes out of airplane mode and connects to nearby free WiFi.
> 
> Then uploads the audio file to my server, which splits it into 15 sec chunks that slightly overlap. Passes each to Shazam’s API (not public, but someone reverse engineered it and made a great Python package). Phone only uses 2% of power every hour when it’s not charging!

---

**Quote** 2024\-10\-01

> *\[Reddit is] mostly ported over entirely to Lit now. There are a few straggling pages that we're still working on, but most of what everyday typical users see and use is now entirely Lit based. This includes both logged out and logged in experiences.*

[Jim Simon, Reddit](https://twitter.com/jimsimon_/status/1840905389384007906)

---

**Link** 2024\-10\-01 [Whisper large\-v3\-turbo model](https://github.com/openai/whisper/pull/2361/files):

It’s [OpenAI DevDay](https://openai.com/devday/) today. Last year they released a whole stack of new features, including GPT\-4 vision and GPTs and their text\-to\-speech API, so I’m intrigued to see what they release today (I’ll be at the San Francisco event).

Looks like they got an early start on the releases, with the first new Whisper model since November 2023\.

Whisper Turbo is a new speech\-to\-text model that fits the continued trend of distilled models getting smaller and faster while maintaining the same quality as larger models.

`large-v3-turbo` is 809M parameters \- slightly larger than the 769M medium but significantly smaller than the 1550M large. OpenAI claim its 8x faster than large and requires 6GB of VRAM compared to 10GB for the larger model.

The model file is a 1\.6GB download. OpenAI continue to make Whisper (both code and model weights) available under the MIT license.

It’s already supported in both Hugging Face transformers \- [live demo here](https://huggingface.co/spaces/hf-audio/whisper-large-v3-turbo) \- and in [mlx\-whisper](https://pypi.org/project/mlx-whisper/) on Apple Silicon, [via Awni Hannun](https://x.com/awnihannun/status/1841109315383648325):

```
import mlx_whisper
print(mlx_whisper.transcribe(
  "path/to/audio",
  path_or_hf_repo="mlx-community/whisper-turbo"
)["text"])

```

Awni reports:

> Transcribes 12 minutes in 14 seconds on an M2 Ultra (\~50X faster than real time).

---

**Link** 2024\-10\-02 [Ethical Applications of AI to Public Sector Problems](https://jacobian.org/2024/oct/1/ethical-public-sector-ai/):

Jacob Kaplan\-Moss developed this model a few years ago (before the generative AI rush) while working with public\-sector startups and is publishing it now. He starts by outright dismissing the snake\-oil infested field of “predictive” models:

> It’s not ethical to predict social outcomes — and it’s probably not possible. Nearly everyone claiming to be able to do this is lying: their algorithms do not, in fact, make predictions that are any better than guesswork. \[…] Organizations acting in the public good should avoid this area like the plague, and call bullshit on anyone making claims of an ability to predict social behavior.

Jacob then differentiates assistive AI and automated AI. Assistive AI helps human operators process and consume information, while leaving the human to take action on it. Automated AI acts upon that information without human oversight.

His conclusion: yes to assistive AI, and no to automated AI:

> All too often, **AI algorithms encode human bias**. And in the public sector, failure carries real life or death consequences. In the private sector, companies can decide that a certain failure rate is OK and let the algorithm do its thing. But when citizens interact with their governments, they have an expectation of fairness, which, because AI judgement will always be available, it cannot offer.

On Mastodon [I said to Jacob](https://fedi.simonwillison.net/@simon/113235310036566202):

> I’m heavily opposed to anything where decisions with consequences are outsourced to AI, which I think fits your model very well
> 
> (somewhat ironic that I wrote this message from the passenger seat of my first ever Waymo trip, and this weird car is making extremely consequential decisions dozens of times a second!)

Which sparked an interesting conversation about why life\-or\-death decisions made by self\-driving cars feel different from decisions about social services. My take on that:

> I think it’s about judgement: the decisions I care about are far more deep and non\-deterministic than “should I drive forward or stop”.

[Jacob](https://social.jacobian.org/@jacob/113235551869890541):

> Where there’s moral ambiguity, I want a human to own the decision both so there’s a chance for empathy, and also for someone to own the accountability for the choice.

That idea of ownership and accountability for decision making feels critical to me. A giant black box of matrix multiplication cannot take accountability for “decisions” that it makes.

---