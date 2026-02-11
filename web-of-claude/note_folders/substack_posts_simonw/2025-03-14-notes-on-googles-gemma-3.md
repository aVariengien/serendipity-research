# Notes on Google's Gemma 3

*Plus adding AI-generated descriptions to my tools collection*

Published: 2025-03-14
Source: https://simonw.substack.com/p/notes-on-googles-gemma-3

---

In this newsletter:

* Notes on Google's Gemma 3
* Adding AI\-generated descriptions to my tools collection

Plus 6 links and 4 quotations

### **[Notes on Google's Gemma 3](https://simonwillison.net/2025/Mar/12/gemma-3/) \- 2025\-03\-12**

Google's Gemma team released an impressive new model today (under their not\-open\-source [Gemma license](https://ai.google.dev/gemma/terms)). Gemma 3 comes in four sizes \- 1B, 4B, 12B, and 27B \- and while 1B is text\-only the larger three models are all multi\-modal for vision:

> Gemma 3 introduces multimodality, supporting vision\-language input and text outputs. It handles context windows up to 128k tokens, understands over 140 languages, and offers improved math, reasoning, and chat capabilities, including structured outputs and function calling.

Here's the [Gemma 3 Technical Report PDF](https://storage.googleapis.com/deepmind-media/gemma/Gemma3Report.pdf), which makes the big claim that they find "Gemma3\-27B\-IT comparable to Gemini\-1\.5\-Pro across benchmarks".

I tried out the largest model using the latest [Ollama](https://ollama.com/) \- this is the second time I've spotted a major model release partnering with Ollama on launch day, the first being [Mistral Small 3](https://simonwillison.net/2025/Jan/30/mistral-small-3/).

I ran this (after upgrading Ollama through their menu icon upgrade option):

```
ollama pull gemma3:27b
```

That pulled 17GB of model weights. I've been trying it out using [LLM](https://llm.datasette.io/) and [llm\-ollama](https://github.com/taketwo/llm-ollama):

```
llm install llm-ollama
llm -m gemma3:27b 'Build a single page HTML+CSS+JavaScript UI that gives me a large textarea for writing in which constantly saves what I have entered to localStorage (restoring when I reload the page) and displays a word counter'
```

That was a replay of [a prompt](https://tools.simonwillison.net/colophon#word-counter.html) I ran against Claude Artifacts a few months ago. Here's [what Gemma built](https://static.simonwillison.net/static/2025/gemma3-word-count.html), and the [full chat transcript](https://gist.github.com/simonw/f8a87f2242439d3974405a17f5d8bc23). It's a simple example but it worked just right.

[![Animated demo - a simple textarea, I type text in it and a word count updates above.](https://substackcdn.com/image/fetch/$s_!6vhV!,w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30177f2f-06b5-4f21-adf8-e36c1042e789_552x260.gif "Animated demo - a simple textarea, I type text in it and a word count updates above.")](https://substackcdn.com/image/fetch/$s_!6vhV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30177f2f-06b5-4f21-adf8-e36c1042e789_552x260.gif)

Let's try out the vision mode, by asking it to describe this photo:

[![Two pelicans flying against a blue sky ](https://substackcdn.com/image/fetch/$s_!HjB-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb9bf4c44-1538-48af-89b6-b8412739aa38_1086x724.jpeg "Two pelicans flying against a blue sky ")](https://substackcdn.com/image/fetch/$s_!HjB-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb9bf4c44-1538-48af-89b6-b8412739aa38_1086x724.jpeg)

```
llm -m gemma3:27b describe -a https://static.simonwillison.net/static/2025/two-pelicans.jpg
```

Here's [the full response](https://gist.github.com/simonw/0e703ba72d0cf5a6dd117981bd03e604):

> **Overall Impression:**
> 
> The image features two brown pelicans in flight against a solid, bright blue background. The composition is dynamic, capturing the birds mid\-wingbeat.
> 
> **Details:**
> 
> * **Pelicans:** Both pelicans are a rich, dark brown color. They have large, pale yellow\-orange beaks and pouches. One pelican is shown with its wings fully extended, appearing to be gliding or soaring. The other is captured with its wings in a more dynamic, upward\-sweeping motion.
> * **Background:** The background is a flat, uniform shade of bright blue, which makes the pelicans stand out.
> * **Composition:** The birds are positioned in opposite directions, creating a sense of movement and balance. The image is well\-lit, highlighting the texture of the pelicans' feathers.
> 
> **Overall, the image is a striking and visually appealing depiction of these majestic birds in flight.**

Is it right to say "the birds are positioned in opposite directions"? I thought that was a mistake at first, but I'll give it a pass since their wings are positioned in opposite directions to each other.

Something I've been curious about recently is longer context support: how well can a local model on my laptop deal with summarization or data extraction tasks against longer pieces of text?

I decided to try [my Hacker News summarize script](https://til.simonwillison.net/llms/claude-hacker-news-themes#user-content-adding-a--m-model-option) using Gemma, against [the thread](https://news.ycombinator.com/item?id=43340491) there discussing the Gemma 3 technical paper.

First I did a quick token count (using the OpenAI tokenizer but it's usually a similar number to other models):

```
curl 'https://hn.algolia.com/api/v1/items/43340491' | ttok
```

This returned 22,260 \- well within Gemma's documented limits but still a healthy number considering just last year most models topped out at 4,000 or 8,000\.

I ran my script like this:

```
hn-summary.sh 43340491 -m gemma3:27b
```

It did a pretty good job! Here's the [full prompt and response](https://gist.github.com/simonw/ab487ea3d1605e719dc2950cd4565146). The one big miss is that it ignored my instructions to include illustrative quotes \- I don't know if modifying the prompt will fix that but it's disappointing that it didn't handle that well, given how important direct quotes are for building confidence in RAG\-style responses.

Here's what I got for [Generate an SVG of a pelican riding a bicycle](https://gist.github.com/simonw/f79c4bd2fbe966e1b600cb8b41cae810):

```
llm -m gemma3:27b 'Generate an SVG of a pelican riding a bicycle'
```

[![A collection of abstract shapes, definitely not a pelican on a bicycle](https://substackcdn.com/image/fetch/$s_!FuDU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8fa4ade4-0b0a-4ad0-a709-c45da7d78a7b_200x200.svg "A collection of abstract shapes, definitely not a pelican on a bicycle")](https://substackcdn.com/image/fetch/$s_!FuDU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8fa4ade4-0b0a-4ad0-a709-c45da7d78a7b_200x200.svg)

You can also try out the new Gemma [in Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemma-3-27b-it), and via their API. I added support for it to [llm\-gemini 0\.15](https://github.com/simonw/llm-gemini/releases/tag/0.15), though sadly it appears vision mode doesn't work with that API hosted model yet.

```
llm install -U llm-gemini
llm keys set gemini
# paste key here
llm -m gemma-3-27b-it 'five facts about pelicans of interest to skunks'
```

[Here's what I got](https://gist.github.com/simonw/bc22062e60e5af3faf458756cb368d0e). I'm not sure how pricing works for that hosted model.

Gemma 3 is also already available [through MLX\-VLM](https://github.com/Blaizzy/mlx-vlm/pull/235) \- here's [the MLX model collection](https://huggingface.co/collections/mlx-community/gemma-3-67d14a10480a436ad478b0f9) \- but I haven't tried that version yet.

---

### **[Adding AI\-generated descriptions to my tools collection](https://simonwillison.net/2025/Mar/13/tools-colophon/) \- 2025\-03\-13**

The [/colophon](https://tools.simonwillison.net/colophon) page on my [tools.simonwillison.net](https://tools.simonwillison.net/) site lists all 78 of the HTML\+JavaScript tools I've built (with [AI assistance](https://simonwillison.net/tags/ai-assisted-programming/)) along with their commit histories, including links to prompting transcripts. I wrote about [how I built that colophon](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#a-detailed-example) the other day. It now also includes a description of each tool, generated using Claude 3\.7 Sonnet.

[![llm-prices.html # The LLM Pricing Calculator helps you estimate costs when using various large language models. Enter the number of input tokens (your prompts) and output tokens (AI responses), along with their respective pricing per million tokens, to calculate the total cost in both dollars and cents. The calculator includes a comprehensive list of preset pricing for popular models like GPT-4o, Claude 3, Gemini, and more. Each preset displays the cost per million tokens for both input and output, which automatically populates the calculator fields when selected. The calculator updates in real-time as you modify values, making it easy to compare costs across different models or estimate expenses for specific usage scenarios. 148bc1 October 16, 2024 20:50 Create llm-prices.html https://gist.github.com/simonw/6b684b5f7d75fb82034fc963cc487530 2e0a70 October 25, 2024 16:32 o1-preview and o1-mini ](https://substackcdn.com/image/fetch/$s_!BO0R!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa73373d8-a6ce-4df8-8d76-e553b353b4fb_1700x1004.jpeg "llm-prices.html # The LLM Pricing Calculator helps you estimate costs when using various large language models. Enter the number of input tokens (your prompts) and output tokens (AI responses), along with their respective pricing per million tokens, to calculate the total cost in both dollars and cents. The calculator includes a comprehensive list of preset pricing for popular models like GPT-4o, Claude 3, Gemini, and more. Each preset displays the cost per million tokens for both input and output, which automatically populates the calculator fields when selected. The calculator updates in real-time as you modify values, making it easy to compare costs across different models or estimate expenses for specific usage scenarios. 148bc1 October 16, 2024 20:50 Create llm-prices.html https://gist.github.com/simonw/6b684b5f7d75fb82034fc963cc487530 2e0a70 October 25, 2024 16:32 o1-preview and o1-mini ")](https://substackcdn.com/image/fetch/$s_!BO0R!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa73373d8-a6ce-4df8-8d76-e553b353b4fb_1700x1004.jpeg)

This is the single largest chunk of AI\-generated text I've ever published on the indexable web. I share lots of LLM transcripts but I usually put them in a secret Gist such that they'll be kept out of search engines.

On the one hand this feels [slop adjacent](https://simonwillison.net/tags/slop/) \- but I was never going to write documentation for all 78 of those little experiments, yet I find myself forgetting details of how they worked. Just one example: my [CSV marker map](https://tools.simonwillison.net/colophon#csv-marker-map.html) tool which I built last year for knocking out an [ad\-hoc Bigfoot sightings map](https://tools.simonwillison.net/csv-marker-map?center=39.061909385087624%2C-96.50390625000001&zoom=5&csv=https%3A%2F%2Fgist.githubusercontent.com%2Fsimonw%2Fdb5c00b61abb61847ece2480d96e96d2%2Fraw%2Fb76475d9f25dec235b89822ed54f9f1b84394df3%2Fsightings.csv) and then promptly forgot what it could do.

Here's what I got when I ran:

```
cat csv-marker-map.html | llm -m claude-3.7-sonnet \
  --system "Write a paragraph of documentation for this page as markdown. Do not include a heading. Do not use words like just or simply."
```

> This interactive map displays markers based on data from a CSV file. Load data by adding `?csv=URL` to the page URL, where the CSV must include `latitude` and `longitude` columns. You can customize the map with several URL parameters: `center`(coordinates in format `lat,lng`), `zoom`(zoom level), `q` (location to search for), `marker` (add individual markers at coordinates), and `color` (change the default marker color). The map automatically updates the URL as you navigate, preserving your current view. Markers from CSV files appear as small colored circles on the map, while markers specified directly in the URL use the default Leaflet marker style.

That's genuinely useful. I [got Claude](https://claude.ai/share/6a07415a-6f72-4e79-90c2-7dc780d60a0d) to write me a [write\_docs.py](https://github.com/simonw/tools/blob/main/write_docs.py) script to loop through all 78 files and generate `filename.docs.md` descriptions that live in the repo, then [updated build\_colophon.py](https://github.com/simonw/tools/blame/5322f55a2e7006541e80a5ffe13aeb89c74c6cef/build_colophon.py#L195-L213)to include those descriptions if they exist.

It cost about $1\.08 in Claude credits to document all 78 tools, because some of those HTML files were quite long so the input tokens added up.

Each of the documentation files includes a comment with the most recent commit hash of the file that was used to generate the document, like this:

```
<!-- Generated from commit: 7c6af8eeabc7682b5f9ec2621e34bc771c5471d8 -->
```

The tool can use this to spot if a file has been updated \- if so, the documentation will be regenerated.

Add this all together and now I can drop new HTML\+JavaScript tools into my [simonw/tools](https://github.com/simonw/tools)repo and, moments later, they'll be published on [tools.simonwillison.net](https://tools.simonwillison.net/) with auto\-generated descriptions added to my [colophon](https://tools.simonwillison.net/colophon). I think that's pretty neat!

**Update**: I decided that the descriptions were too long, so I modified the script to add "Keep it to 2\-3 sentences" to the end of the system prompt. These new, shorter descriptions are now live \- [here's the diff](https://github.com/simonw/tools/commit/b9eadb0255e269d865ec1ba3c385760cac7b15b7). Total usage was 283,528 input tokens and 6,010 output tokens for a cost of 94 cents.

The new, shorter description for `csv-marker-map.html` looks like this:

> This page creates an interactive map with markers based on CSV data. It accepts parameters in the URL to set the center, zoom level, search query, individual markers, and a CSV file URL for bulk marker placement. The markers are displayed on an OpenStreetMap base layer, and the map view automatically updates the URL when panned or zoomed.

For comparison, here's a copy of [the previous colophon](https://static.simonwillison.net/static/2025/colophon-longer-descriptions.html) with the longer descriptions.

---

**Quote** 2025\-03\-11

> *Languages that allow for a structurally similar codebase offer a significant boon for anyone making code changes because we can easily port changes between the two codebases. In contrast, languages that require fundamental rethinking of memory management, mutation, data structuring, polymorphism, laziness, etc., might be a better fit for a ground\-up rewrite, but we're undertaking this more as a port that maintains the existing behavior and critical optimizations we've built into the language. Idiomatic Go strongly resembles the existing coding patterns of the TypeScript codebase, which makes this porting effort much more tractable.*

[Ryan Cavanaugh](https://github.com/microsoft/typescript-go/discussions/411)

---

**Link** 2025\-03\-11 [OpenAI API: Responses vs. Chat Completions](https://platform.openai.com/docs/guides/responses-vs-chat-completions):

OpenAI released a bunch of new API platform features this morning under the headline "[New tools for building agents](https://openai.com/index/new-tools-for-building-agents/)" (their somewhat mushy interpretation of "agents" here is "systems that independently accomplish tasks on behalf of users").

A particularly significant change is the introduction of a new **Responses API**, which is a slightly different shape from the Chat Completions API that they've offered for the past couple of years and which others in the industry have widely cloned as an ad\-hoc standard.

In [this guide](https://platform.openai.com/docs/guides/responses-vs-chat-completions) they illustrate the differences, with a reassuring note that:

> The Chat Completions API is an industry standard for building AI applications, and we intend to continue supporting this API indefinitely. We're introducing the Responses API to simplify workflows involving tool use, code execution, and state management. We believe this new API primitive will allow us to more effectively enhance the OpenAI platform into the future.

An API that *is* going away is the [Assistants API](https://platform.openai.com/docs/api-reference/assistants), a perpetual beta first launched at OpenAI DevDay in 2023\. The new responses API solves effectively the same problems but better, and assistants will be sunset "in the first half of 2026".

The best illustration I've seen of the differences between the two is this [giant commit](https://github.com/openai/openai-python/commit/2954945ecc185259cfd7cd33c8cbc818a88e4e1b) to the `openai-python` GitHub repository updating ALL of the example code in one go.

The most important feature of the Responses API (a feature it shares with the old Assistants API) is that it can manage conversation state on the server for you. An oddity of the Chat Completions API is that you need to maintain your own records of the current conversation, sending back full copies of it with each new prompt. You end up making API calls that look like this (from [their examples](https://platform.openai.com/docs/guides/conversation-state?api-mode=chat&lang=javascript#manually-manage-conversation-state)):

```
{
    "model": "gpt-4o-mini",
    "messages": [
        {
            "role": "user",
            "content": "knock knock.",
        },
        {
            "role": "assistant",
            "content": "Who's there?",
        },
        {
            "role": "user",
            "content": "Orange."
        }
    ]
}
```

These can get long and unwieldy \- especially when attachments such as images are involved \- but the real challenge is when you start integrating tools: in a conversation with tool use you'll need to maintain that full state *and* drop messages in that show the output of the tools the model requested. It's not a trivial thing to work with.

The new Responses API continues to support this list of messages format, but you also get the option to outsource that to OpenAI entirely: you can add a new `"store": true` property and then in subsequent messages include a `"previous_response_id: response_id` key to continue that conversation.

This feels a whole lot more natural than the Assistants API, which required you to think in terms of [threads, messages and runs](https://platform.openai.com/docs/assistants/overview#objects) to achieve the same effect.

Also fun: the Response API [supports HTML form encoding](https://twitter.com/athyuttamre/status/1899541484308971822) now in addition to JSON:

```
curl https://api.openai.com/v1/responses \
  -u :$OPENAI_API_KEY \
  -d model="gpt-4o" \
  -d input="What is the capital of France?"
```

I found that in an excellent [Twitter thread](https://twitter.com/athyuttamre/status/1899541471532867821)providing background on the design decisions in the new API from OpenAI's Atty Eleti. Here's [a nitter link](https://nitter.net/athyuttamre/status/1899541471532867821) for people who don't have a Twitter account.

#### **New built\-in tools**

A potentially more exciting change today is the introduction of default tools that you can request while using the new Responses API. There are three of these, all of which can be specified in the `"tools": [...]` array.

* `{"type": "web_search_preview"}` \- the same search feature available through ChatGPT. The documentation doesn't clarify which underlying search engine is used \- I initially assumed Bing, but the tool documentation links to this [Overview of OpenAI Crawlers](https://platform.openai.com/docs/bots)page so maybe it's entirely in\-house now? Web search [is priced](https://platform.openai.com/docs/pricing#web-search) at between $25 and $50 per thousand queries depending on if you're using GPT\-4o or GPT\-4o mini and the configurable size of your "search context".
* `{"type": "file_search", "vector_store_ids": [...]}` provides integration with the latest version of their [file search](https://platform.openai.com/docs/guides/tools-file-search) vector store, mainly used for RAG. "Usage is priced⁠ at $2\.50 per thousand queries and file storage at $0\.10/GB/day, with the first GB free".
* `{"type": "computer_use_preview", "display_width": 1024, "display_height": 768, "environment": "browser"}` is the most surprising to me: it's tool access to the [Computer\-Using Agent](https://openai.com/index/computer-using-agent/) system they built for their Operator product. This one is going to be *a lot* of fun to explore. The tool's documentation includes a warning [about prompt injection risks](https://platform.openai.com/docs/guides/tools-computer-use#beware-of-prompt-injections). Though on closer inspection I think this may work more like [Claude Computer Use](https://simonwillison.net/2024/Oct/22/computer-use/), where you have to [run the sandboxed environment yourself](https://platform.openai.com/docs/guides/tools-computer-use#setting-up-your-environment) rather than outsource that difficult part to them.

I'm still thinking through how to expose these new features in my [LLM](https://llm.datasette.io/) tool, which is made harder by the fact that a number of plugins now rely on the default OpenAI implementation from core, which is currently built on top of Chat Completions. I've been worrying for a while about the impact of our entire industry building clones of one proprietary API that might change in the future, I guess now we get to see how that shakes out!

---

**Link** 2025\-03\-11 [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/):

OpenAI's other big announcement today ([see also](https://simonwillison.net/2025/Mar/11/responses-vs-chat-completions/)) \- a Python library ([openai\-agents](https://pypi.org/project/openai-agents/)) for building "agents", which is a replacement for their previous [swarm](https://github.com/openai/swarm) research project.

In this project, an "agent" is a class that configures an LLM with a system prompt an access to specific tools.

An interesting concept in this one is the concept of **[handoffs](https://openai.github.io/openai-agents-python/handoffs/)**, where one agent can chose to hand execution over to a different system\-prompt\-plus\-tools agent treating it almost like a tool itself. This code example illustrates the idea:

```
from agents import Agent, handoff

billing_agent = Agent(
    name="Billing agent"
)
refund_agent = Agent(
    name="Refund agent"
)
triage_agent = Agent(
    name="Triage agent",
    handoffs=[billing_agent, handoff(refund_agent)]
)
```

The library also includes [guardrails](https://openai.github.io/openai-agents-python/guardrails/) \- classes you can add that attempt to filter user input to make sure it fits expected criteria. Bits of this look suspiciously like trying to [solve AI security problems with more AI](https://simonwillison.net/2022/Sep/17/prompt-injection-more-ai/) to me.

---

**Link** 2025\-03\-13 [Smoke test your Django admin site](https://jmduke.com/posts/post/django-admin-changelist-test/):

Justin Duke demonstrates a neat pattern for running simple tests against your internal Django admin site: introspect every admin route via `django.urls.get_resolver()` and loop through them with `@pytest.mark.parametrize` to check they all return a 200 HTTP status code.

This catches simple mistakes with the admin configuration that trigger exceptions that might otherwise go undetected.

I rarely write automated tests against my own admin sites and often feel guilty about it. I wrote [some notes](https://til.simonwillison.net/django/testing-django-admin-with-pytest) on testing it with [pytest\-django fixtures](https://pytest-django.readthedocs.io/en/latest/helpers.html#fixtures) a few years ago.

---

**Link** 2025\-03\-13 [Introducing Command A: Max performance, minimal compute](https://cohere.com/blog/command-a):

New LLM release from Cohere. It's interesting to see which aspects of the model they're highlighting, as an indicator of what their commercial customers value the most (highlight mine):

> Command A delivers maximum performance with minimal hardware costs when compared to leading proprietary and open\-weights models, such as GPT\-4o and DeepSeek\-V3\. For private deployments, **Command A excels on business\-critical agentic and multilingual tasks, while being deployable on just two GPUs**, compared to other models that typically require as many as 32\.

It's open weights but very much not open source \- the license is [Creative Commons Attribution Non\-Commercial](https://cohere.com/c4ai-cc-by-nc-license) and also requires adhering to their [Acceptable Use Policy](https://docs.cohere.com/docs/c4ai-acceptable-use-policy).

Cohere offer it for commercial use via "contact" us pricing or through their API. I released [llm\-command\-r 0\.3](https://github.com/simonw/llm-command-r/releases/tag/0.3) adding support for this new model, plus their smaller and faster [Command R7B](https://cohere.com/blog/command-r7b) (released in December) and support for structured outputs via [LLM schemas](https://llm.datasette.io/en/stable/schemas.html).

(I found [a weird bug](https://github.com/simonw/llm-command-r/issues/8#issuecomment-2722598353) with their schema support where schemas that end in an integer output a seemingly limitless integer \- in my experiments it affected Command R and the new Command A but not Command R7B.)

---

**Link** 2025\-03\-13 [Anthropic API: Text editor tool](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/text-editor-tool):

Anthropic released a new "tool" today for text editing. It looks similar to the tool they offered as part of their [computer use beta API](https://docs.anthropic.com/en/docs/agents-and-tools/computer-use#understand-anthropic-defined-tools), and the trick they've been using for a while in both Claude Artifacts and the new [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview) to more efficiently edit files there.

The new tool requires you to implement several commands:

* `view` \- to view a specified file \- either the whole thing or a specified range
* `str_replace` \- execute an exact string match replacement on a file
* `create` \- create a new file with the specified contents
* `insert` \- insert new text after a specified line number
* `undo_edit` \- undo the last edit made to a specific file

Providing implementations of these commands is left as an exercise for the developer.

Once implemented, you can have conversations with Claude where it knows that it can request the content of existing files, make modifications to them and create new ones.

There's quite a lot of assembly required to start using this. I tried [vibe coding an implementation](https://claude.ai/share/97bde411-20d4-4549-a34f-27954a5ab564)by dumping a copy of the documentation into Claude itself but I didn't get as far as a working program \- it looks like I'd need to spend a bunch more time on that to get something to work, so my effort is currently abandoned.

This was introduced as in a post on [Token\-saving updates on the Anthropic API](https://www.anthropic.com/news/token-saving-updates), which also included a simplification of their token caching API and a new [Token\-efficient tool use (beta)](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/token-efficient-tool-use)where sending a `token-efficient-tools-2025-02-19` beta header to Claude 3\.7 Sonnet can save 14\-70% of the tokens needed to define tools and schemas.

---

**Quote** 2025\-03\-13

> *Today we release **OLMo 2 32B**, the most capable and largest model in the OLMo 2 family, scaling up the OLMo 2 training recipe used for our [7B and 13B models released in November](https://allenai.org/blog/olmo2). It is trained up to 6T tokens and post\-trained using Tulu 3\.1\. OLMo 2 32B is the **first fully\-open model** (all data, code, weights, and details are freely available) **to outperform GPT3\.5\-Turbo and GPT\-4o mini** on a suite of popular, multi\-skill academic benchmarks.*

[Ai2](https://allenai.org/blog/olmo2-32B)

---

**Link** 2025\-03\-13 [Xata Agent](https://github.com/xataio/agent):

Xata are a hosted PostgreSQL company who also develop the open source [pgroll](https://github.com/xataio/pgroll) and [pgstream](https://github.com/xataio/pgstream)schema migration tools.

Their new "Agent" tool is a system that helps monitor and optimize a PostgreSQL server using prompts to LLMs.

Any time I see a new tool like this I go hunting for the prompts. It looks like the main system prompts for orchestrating the tool [live here](https://github.com/xataio/agent/blob/69329cede85d4bc920558c019df51f111cc5068d/apps/dbagent/src/lib/ai/aidba.ts#L25-L48) \- here's a sample:

> `Provide clear, concise, and accurate responses to questions. Use the provided tools to get context from the PostgreSQL database to answer questions. When asked why a query is slow, call the explainQuery tool and also take into account the table sizes. During the initial assessment use the getTablesAndInstanceInfo, getPerfromanceAndVacuumSettings, and getPostgresExtensions tools. When asked to run a playbook, use the getPlaybook tool to get the playbook contents. Then use the contents of the playbook as an action plan. Execute the plan step by step.`

The really interesting thing is those playbooks, each of which is implemented as a prompt in the [lib/tools/playbooks.ts](https://github.com/xataio/agent/blob/69329cede85d4bc920558c019df51f111cc5068d/apps/dbagent/src/lib/tools/playbooks.ts) file. There are six of these so far:

* `SLOW_QUERIES_PLAYBOOK`
* `GENERAL_MONITORING_PLAYBOOK`
* `TUNING_PLAYBOOK`
* `INVESTIGATE_HIGH_CPU_USAGE_PLAYBOOK`
* `INVESTIGATE_HIGH_CONNECTION_COUNT_PLAYBOOK`
* `INVESTIGATE_LOW_MEMORY_PLAYBOOK`

Here's the full text of `INVESTIGATE_LOW_MEMORY_PLAYBOOK`:

> ```
> Objective:
> To investigate and resolve low freeable memory in the PostgreSQL database.
> 
> Step 1:
> Get the freeable memory metric using the tool getInstanceMetric.
> 
> Step 3:
> Get the instance details and compare the freeable memory with the amount of memory available.
> 
> Step 4:
> Check the logs for any indications of memory pressure or out of memory errors. If there are, make sure to report that to the user. Also this would mean that the situation is critical.
> 
> Step 4:
> Check active queries. Use the tool getConnectionsGroups to get the currently active queries. If a user or application stands out for doing a lot of work, record that to indicate to the user.
> 
> Step 5:
> Check the work_mem setting and shared_buffers setting. Think if it would make sense to reduce these in order to free up memory.
> 
> Step 6:
> If there is no clear root cause for using memory, suggest to the user to scale up the Postgres instance. Recommend a particular instance class.
> ```

This is the first time I've seen prompts arranged in a "playbooks" pattern like this. What a weird and interesting way to write software!

---

**Quote** 2025\-03\-13

> *One of the most essential practices for maintaining the long\-term quality of computer code is to write automated tests that ensure the program continues to act as expected, even when other people (including your future self) muck with it.*

[Evan Miller](https://www.evanmiller.org/functional-tests-as-a-tree-of-continuations.html)

---

**Quote** 2025\-03\-14

> *\[...] in 2013, I did not understand that the things I said had meaning. I hate talking about this because it makes me seem more important than I am, but it’s also important to acknowledge. I saw myself at the time as just Steve, some random guy. If I say something on the internet, it’s like I’m talking to a friend in real life, my words are just random words and I’m human and whatever. It is what it is.  
>   
> But at that time in my life, that wasn’t actually the case. I was on the Rails team, I was speaking at conferences, and people were reading my blog and tweets. I was an “influencer,” for better or worse. But I hadn’t really internalized that change in my life yet. And so I didn’t really understand that if I criticized something, it was something thousands of people would see.*

[Steve Klabnik](https://steveklabnik.com/writing/choosing-languages/)

---