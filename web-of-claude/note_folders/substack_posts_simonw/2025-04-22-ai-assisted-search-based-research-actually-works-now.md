# AI assisted search-based research actually works now

*Maybe Meta's Llama claims to be open source because of the EU AI act*

Published: 2025-04-22
Source: https://simonw.substack.com/p/ai-assisted-search-based-research

---

In this newsletter:

* AI assisted search\-based research actually works now
* Maybe Meta's Llama claims to be open source because of the EU AI act

Plus 7 links and 1 quotation

### [AI assisted search\-based research actually works now](https://simonwillison.net/2025/Apr/21/ai-assisted-search/) \- 2025\-04\-21

For the past two and a half years the feature I've most wanted from LLMs is the ability to take on search\-based research tasks on my behalf. We saw the first glimpses of this back in early 2023, with Perplexity (first launched [December 2022](https://en.wikipedia.org/wiki/Perplexity_AI), first prompt leak [in January 2023](https://simonwillison.net/2023/Jan/22/perplexityai/)) and then the GPT\-4 powered Microsoft Bing (which launched/cratered spectacularly [in February 2023](https://simonwillison.net/2023/Feb/15/bing/)). Since then a whole bunch of people have taken a swing at this problem, most notably [Google Gemini](https://gemini.google.com/) and [ChatGPT Search](https://openai.com/index/introducing-chatgpt-search/).

Those 2023\-era versions were promising but very disappointing. They had a strong tendency to hallucinate details that weren't present in the search results, to the point that you couldn't trust anything they told you.

In this first half of 2025 I think these systems have finally crossed the line into being genuinely useful.

* [Deep Research, from three different vendors](https://simonwillison.net/2025/Apr/21/ai-assisted-search/#deep-research-from-three-different-vendors)
* [o3 and o4\-mini are really good at search](https://simonwillison.net/2025/Apr/21/ai-assisted-search/#o3-and-o4-mini-are-really-good-at-search)
* [Google and Anthropic need to catch up](https://simonwillison.net/2025/Apr/21/ai-assisted-search/#google-and-anthropic-need-to-catch-up)
* [Lazily porting code to a new library version via search](https://simonwillison.net/2025/Apr/21/ai-assisted-search/#lazily-porting-code-to-a-new-library-version-via-search)
* [How does the economic model for the Web work now?](https://simonwillison.net/2025/Apr/21/ai-assisted-search/#how-does-the-economic-model-for-the-web-work-now-)

#### Deep Research, from three different vendors

First came the **Deep Research** implementations \- [Google Gemini](https://blog.google/products/gemini/google-gemini-deep-research/) and [then OpenAI](https://openai.com/index/introducing-deep-research/) and [then Perplexity](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research) launched products with that name and they were all impressive: they could take a query, then churn away for several minutes assembling a lengthy report with dozens (sometimes hundreds) of citations. Gemini's version had a *huge* upgrade a few weeks ago when they [switched it to using Gemini 2\.5 Pro](https://blog.google/products/gemini/deep-research-gemini-2-5-pro-experimental/), and I've had some outstanding results from it since then.

Waiting a few minutes for a 10\+ page report isn't my ideal workflow for this kind of tool. I'm impatient, I want answers faster than that!

#### o3 and o4\-mini are really good at search

Last week, OpenAI released [search\-enabled o3 and o4\-mini](https://openai.com/index/introducing-o3-and-o4-mini/) through [ChatGPT](https://chatgpt.com/). On the surface these look like the same idea as we've seen already: LLMs that have the option to call a search tool as part of replying to a prompt.

But there's one *very significant* difference: these models can run searches as part of the chain\-of\-thought reasoning process they use before producing their final answer.

This turns out to be a *huge* deal. I've been throwing all kinds of questions at ChatGPT (in o3 or o4\-mini mode) and getting back genuinely useful answers grounded in search results. I haven't spotted a hallucination yet, and unlike prior systems I rarely find myself shouting "no, don't search for *that*!" at the screen when I see what they're doing.

Here are four recent example transcripts:

* [Get me specs including VRAM for RTX 5090 and RTX PRO 6000 \- plus release dates and prices](https://chatgpt.com/share/6805758b-acc8-8006-88a3-bdd78866ee15)
* [Find me a website tool that lets me paste a URL in and it gives me a word count and an estimated reading time](https://chatgpt.com/share/68057580-02c8-8006-8ff4-7ae3ce816342)
* [Figure out what search engine ChatGPT is using for o3 and o4\-mini](https://chatgpt.com/share/6805756c-4268-8006-82ab-014f7c304622)
* [Look up Cloudflare r2 pricing and use Python to figure out how much this (screenshot of dashboard) costs](https://chatgpt.com/share/6805755b-4aa0-8006-ab0b-42ae569da6a8)

Talking to o3 feels like talking to a Deep Research tool in real\-time, without having to wait for several minutes for it to produce an overly\-verbose report.

My hunch is that doing this well requires a very strong reasoning model. Evaluating search results is hard, due to the need to wade through huge amounts of spam and deceptive information. The disappointing results from previous implementations usually came down to the Web being full of junk.

Maybe o3, o4\-mini and Gemini 2\.5 Pro are the first models to cross the gullibility\-resistance threshold to the point that they can do this effectively?

#### Google and Anthropic need to catch up

The user\-facing [Google Gemini app](https://gemini.google.com/) can search too, but it doesn't show me what it's searching for. As a result, I just don't trust it. Compare these examples from o3 and Gemini for the prompt "Latest post by Simon Willison" \- o3 is much more transparent:

[![o3 ChatGPT screenshot  Prompt: Latest post by Simon Willison  Thought for 25 seconds › 2 searches • 3 sources  Latest post • Title: "Working Through the Fear of Being Seen" (via Ashley Willis) • Published: April 22 2025 at 6: 40 AM  An overlay shows the details of that thinking session:  Thought for 25 seconds • The user's request is pretty clear: they want to know the latest post by Simon Willison. I think the user may actually be Simon Willison themselves, asking for their own blog, which is hosted on SimonWillison.net. l'll need to search the web for Simon's latest blog post (probably from April 2025). Once I find it, l'll include the title, publication date, and a brief summary. @ Searching the web • Simon Willison blog April 2025 • Simon Willison blog 2025 Archive for Tuesday, 22nd April 2025 - Simon Willison's W... * Working Through the Fear of Being Seen * Simon Willison's Weblog Gemini Advanced 2.0 flash screenshot. Prompt is Latest post by Simon Willison.  Google Search Try again without apps Simon Willison's latest blog post is titled "Here's how I use LLMs to help me write code" and was published on March 11th, 2025. In this post, he discusses his experiences and strategies for effectively using Large Language Models (LLMs) in software development. However, according to his Mastodon profile, his most recent activity includes: • A boost of a post about 11m plugins on April 18th, 2025. • A post about the Gemini 2.5 Flash model on April 17th, 2025. • A post about OpenAl's new 03 and o4-mini models on April 16th, 2025. • A thread discussing the CaMeL approach to mitigating prompt injection attacks on April 11th, 2025. • An announcement of two new 11m plugins on April 10th, 2025. It seems his blog might not always reflect his absolute latest thoughts and shorter updates, which he often shares on platforms like Mastodon.](https://substackcdn.com/image/fetch/$s_!E4YH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbc5aef44-bb79-4533-ab08-74e0ee33902b_1294x1372.png "o3 ChatGPT screenshot  Prompt: Latest post by Simon Willison  Thought for 25 seconds › 2 searches • 3 sources  Latest post • Title: \"Working Through the Fear of Being Seen\" (via Ashley Willis) • Published: April 22 2025 at 6: 40 AM  An overlay shows the details of that thinking session:  Thought for 25 seconds • The user's request is pretty clear: they want to know the latest post by Simon Willison. I think the user may actually be Simon Willison themselves, asking for their own blog, which is hosted on SimonWillison.net. l'll need to search the web for Simon's latest blog post (probably from April 2025). Once I find it, l'll include the title, publication date, and a brief summary. @ Searching the web • Simon Willison blog April 2025 • Simon Willison blog 2025 Archive for Tuesday, 22nd April 2025 - Simon Willison's W... * Working Through the Fear of Being Seen * Simon Willison's Weblog Gemini Advanced 2.0 flash screenshot. Prompt is Latest post by Simon Willison.  Google Search Try again without apps Simon Willison's latest blog post is titled \"Here's how I use LLMs to help me write code\" and was published on March 11th, 2025. In this post, he discusses his experiences and strategies for effectively using Large Language Models (LLMs) in software development. However, according to his Mastodon profile, his most recent activity includes: • A boost of a post about 11m plugins on April 18th, 2025. • A post about the Gemini 2.5 Flash model on April 17th, 2025. • A post about OpenAl's new 03 and o4-mini models on April 16th, 2025. • A thread discussing the CaMeL approach to mitigating prompt injection attacks on April 11th, 2025. • An announcement of two new 11m plugins on April 10th, 2025. It seems his blog might not always reflect his absolute latest thoughts and shorter updates, which he often shares on platforms like Mastodon.")](https://substackcdn.com/image/fetch/$s_!E4YH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbc5aef44-bb79-4533-ab08-74e0ee33902b_1294x1372.png)

This is a big missed opportunity since Google presumably have by far the best search index, so they really should be able to build a great version of this. And Google's AI assisted search on their regular search interface hallucinates *wildly* to the point that it's actively damaging their brand. I just checked and Google is still showing slop [for Encanto 2](https://simonwillison.net/2024/Dec/29/encanto-2/)!

Claude also finally [added web search](https://simonwillison.net/2025/Mar/20/) a month ago but it doesn't feel nearly as good. It's [using the Brave search index](https://simonwillison.net/2025/Mar/21/anthropic-use-brave/) which I don't think is as comprehensive as Bing or Gemini, and searches don't happen as part of that powerful reasoning flow.

#### Lazily porting code to a new library version via search

The truly magic moment for me came [a few days ago](https://simonwillison.net/2025/Apr/18/gemini-image-segmentation/#gemini-2-5-flash-non-thinking).

My [Gemini image segmentation tool](https://simonwillison.net/2025/Apr/18/gemini-image-segmentation/) was using the [@google/generative\-ai](https://www.npmjs.com/package/@google/generative-ai) library which has been [loudly deprecated](https://github.com/google-gemini/deprecated-generative-ai-js) in favor of the still in preview [Google Gen AI SDK @google/genai](https://github.com/googleapis/js-genai) library.

I did **not** feel like doing the work to upgrade. On a whim, I pasted [my full HTML code](https://github.com/simonw/tools/blob/aa310a4f9cde07d5e8e87572f70fceca532884dd/gemini-mask.html) (with inline JavaScript) into ChatGPT o4\-mini\-high and prompted:

> `This code needs to be upgraded to the new recommended JavaScript library from Google. Figure out what that is and then look up enough documentation to port this code to it.`

(I couldn't even be bothered to look up the name of the new library myself!)

... it did [exactly that](https://chatgpt.com/share/68028f7b-11ac-8006-8150-00c4205a2507). It churned away thinking for 21 seconds, ran a bunch of searches, figured out the new library (which existed *way* outside of its training cut\-off date), found the [upgrade instructions](https://ai.google.dev/gemini-api/docs/migrate) and produced [a new version](https://github.com/simonw/tools/commit/d199de213dc3f866a3b8efbcdd2dde34204dc409) of my code that worked perfectly.

[![Screenshot of AI assistant response about upgrading Google Gemini API code. Shows "Thought for 21 seconds" followed by web search results for "Google Gemini API JavaScript library recommended new library" with options including Google AI for Developers, GitHub, and Google for Developers. The assistant explains updating from GoogleGenerativeAI library to @google-ai/generative, with code samples showing: import { GoogleGenAI } from 'https://cdn.jsdelivr.net/npm/@google/genai@latest'; and const ai = new GoogleGenAI({ apiKey: getApiKey() });](https://substackcdn.com/image/fetch/$s_!qrh4!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcc971f26-36f5-4d46-a750-65a4a211e5d8_1298x1292.jpeg "Screenshot of AI assistant response about upgrading Google Gemini API code. Shows \"Thought for 21 seconds\" followed by web search results for \"Google Gemini API JavaScript library recommended new library\" with options including Google AI for Developers, GitHub, and Google for Developers. The assistant explains updating from GoogleGenerativeAI library to @google-ai/generative, with code samples showing: import { GoogleGenAI } from 'https://cdn.jsdelivr.net/npm/@google/genai@latest'; and const ai = new GoogleGenAI({ apiKey: getApiKey() });")](https://substackcdn.com/image/fetch/$s_!qrh4!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcc971f26-36f5-4d46-a750-65a4a211e5d8_1298x1292.jpeg)

I ran this prompt on my phone out of idle curiosity while I was doing something else. I was *extremely* impressed and surprised when it did exactly what I needed.

#### How does the economic model for the Web work now?

I'm writing about this today because it's been one of my "can LLMs do this reliably yet?" questions for over two years now. I think they've just crossed the line into being useful as research assistants, without feeling the need to check *everything* they say with a fine\-tooth comb.

I still don't trust them not to make mistakes, but I think I might trust them enough that I'll skip my own fact\-checking for lower\-stakes tasks.

This also means that a bunch of the potential dark futures we've been predicting for the last couple of years are a whole lot more likely to become true. Why visit websites if you can get your answers directly from the chatbot instead?

The lawsuits over this [started flying](https://simonwillison.net/2023/Dec/31/ai-in-2023/#ethics-diabolically-complex) back when the LLMs were still mostly rubbish. The stakes are a lot higher now that they're actually good at it!

I can feel my usage of Google search taking a nosedive already. I expect a bumpy ride as a new economic model for the Web lurches into view.

---

### [Maybe Meta's Llama claims to be open source because of the EU AI act](https://simonwillison.net/2025/Apr/19/llama-eu-ai-act/) \- 2025\-04\-19

I encountered a theory a while ago that one of the reasons Meta insist on using the term “open source” for their Llama models despite the Llama license [not actually conforming](https://opensource.org/blog/metas-llama-license-is-still-not-open-source) to the terms of the [Open Source Definition](https://opensource.org/osd) is that the EU’s AI act includes special rules for open source models without requiring OSI compliance.

Since the EU AI act (12 July 2024\) is [available online](https://artificialintelligenceact.eu/the-act/) I decided to take a look for myself.

Here’s [one giant HTML page](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689) containing the full text of the act in English. I checked the token count with [ttok](https://github.com/simonw/ttok) (which uses the OpenAI tokenizer, but it’s close enough to work as a good estimate for other models):

```
curl 'https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689' | ttok
```

241,722 tokens. That should fit nicely into [Gemini 2\.5 Flash](https://simonwillison.net/2025/Apr/17/start-building-with-gemini-25-flash/) (or GPT\-4\.1 or Gemini 2\.5 Pro).

My Gemini API key was playing up so I ran it via [OpenRouter](https://openrouter.ai/) (and [llm\-openrouter](https://github.com/simonw/llm-openrouter)) instead:

```
llm -f 'https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689' \
  -m openrouter/google/gemini-2.5-flash-preview:thinking \
  -s 'Summary of mentions of open source here, including what the document defines open source to mean'
```

Here's [the full answer](https://gist.github.com/simonw/f2e341a2e8ea9ca75c6426fa85bc2dfc). Relevant extract:

> * Recital (89\) states that third parties making accessible "tools, services, processes, or AI components other than general\-purpose AI models" under a **free and open\-source licence** should not be mandated to comply with upstream provider responsibilities towards those who integrate them. It also encourages developers of such resources to implement documentation practices like model cards and data sheets to promote trustworthy AI.
> * Recital (102\) acknowledges that software and data, including models, released under a **free and open\-source licence** can contribute to research and innovation and provide growth opportunities.

I tracked down [Recital 89](https://artificialintelligenceact.eu/recital/89/) and [Recital 102](https://artificialintelligenceact.eu/recital/102/) to check. Sure enough, 89 says:

> Third parties making accessible to the public tools, services, processes, or AI components other than general\-purpose AI models, should not be mandated to comply with requirements targeting the responsibilities along the AI value chain

And in 102:

> General\-purpose AI models released under free and open\-source licences should be considered to ensure high levels of transparency and openness if their parameters, including the weights, the information on the model architecture, and the information on model usage are made publicly available. The licence should be considered to be free and open\-source also when it allows users to run, copy, distribute, study, change and improve software and data, including models under the condition that the original provider of the model is credited, the identical or comparable terms of distribution are respected.

Gemini 2\.5 Flash also pointed me to [Article 2(12\)](https://artificialintelligenceact.eu/article/2/), which reads:

> 12\. This Regulation does not apply to AI systems released under free and open\-source licences, unless they are placed on the market or put into service as high\-risk AI systems or as an AI system that falls under [Article 5](https://artificialintelligenceact.eu/article/5) or [50](https://artificialintelligenceact.eu/article/50/).

I asked a follow\-up question:

```
llm -c 'so it says specific licenses but does it clarify which specific licenses count?'
```

And got [back this response](https://gist.github.com/simonw/f2e341a2e8ea9ca75c6426fa85bc2dfc#response-1):

> No, the document **does not list specific names of licenses** that qualify as "free and open\-source".
> 
> Instead of listing names (like GPL, MIT, Apache, etc.), the Regulation defines what kind of terms a license must grant for it to be considered "free and open\-source" for the purposes of the Regulation.
> 
> According to Recital (102\), such a license must essentially allow software and data, including models, to be:
> 
> * **Openly shared.**
> * Where users can **freely access, use, modify and redistribute** them or modified versions thereof.
> 
> The Recital further clarifies that a license can still be considered free and open\-source even if it includes standard conditions like requiring **attribution (crediting the original provider)** or respecting **identical or comparable terms of distribution**.

I am very obviously not a lawyer, but based on the above I do find the theory credible that Meta are using "open source" in their marketing around Llama partly because the EU AI act has special exemptions for "open source" models that have nothing to do with the OSI definition of that term.

Total cost to use Gemini 2\.5 Flash for this? 5\.1 cents for my first question and 4\.3 cents for the follow\-up. That second question was cheaper even though it built on the first because output tokens are more expensive than input tokens and the second answer was shorter than the first \- using the "thinking" model output is charged at $3\.50/million tokens, input is just $0\.15/million.

Using an LLM as a lawyer is obviously a terrible idea, but using one to crunch through a giant legal document and form a very rough layman's understanding of what it says feels perfectly cromulent to me.

**Update:** Steve O'Grady [points out](https://bsky.app/profile/sogrady.org/post/3ln7ipdbaek2s) that Meta/Facebook have been abusing the term "open source" for a lot longer than the EU AI act has been around \- they were pulling shenanigans with a custom license for React [back in 2017](https://redmonk.com/sogrady/2017/09/26/facebooks-bsd-patents/).

---

**Link** 2025\-04\-19 [Gemma 3 QAT Models](https://developers.googleblog.com/en/gemma-3-quantized-aware-trained-state-of-the-art-ai-to-consumer-gpus/):

Interesting release from Google, as a follow\-up [to Gemma 3](https://simonwillison.net/2025/Mar/12/gemma-3/) from last month:

> To make Gemma 3 even more accessible, we are announcing new versions optimized with Quantization\-Aware Training (QAT) that dramatically reduces memory requirements while maintaining high quality. This enables you to run powerful models like Gemma 3 27B locally on consumer\-grade GPUs like the NVIDIA RTX 3090\.

I wasn't previously aware of Quantization\-Aware Training but it turns out to be quite an established pattern now, supported in both [Tensorflow](https://www.tensorflow.org/model_optimization/guide/quantization/training) and [PyTorch](https://pytorch.org/blog/quantization-aware-training/).

Google report model size drops from BF16 to int4 for the following models:

* Gemma 3 27B: 54GB to 14\.1GB
* Gemma 3 12B: 24GB to 6\.6GB
* Gemma 3 4B: 8GB to 2\.6GB
* Gemma 3 1B: 2GB to 0\.5GB

They partnered with Ollama, LM Studio, MLX (here's [their collection](https://huggingface.co/collections/mlx-community/gemma-3-qat-68002674cd5afc6f9022a0ae)) and llama.cpp for this release \- I'd love to see more AI labs following their example.

The Ollama model version picker currently hides them behind "View all" option, so here are the direct links:

* [gemma3:1b\-it\-qat](https://ollama.com/library/gemma3:1b-it-qat) \- 1GB
* [gemma3:4b\-it\-qat](https://ollama.com/library/gemma3:4b-it-qat) \- 4GB
* [gemma3:12b\-it\-qat](https://ollama.com/library/gemma3:12b-it-qat) \- 8\.9GB
* [gemma3:27b\-it\-qat](https://ollama.com/library/gemma3:27b-it-qat) \- 18GB

I fetched that largest model with:

```
ollama pull gemma3:27b-it-qat
```

And now I'm trying it out with [llm\-ollama](https://github.com/taketwo/llm-ollama):

```
llm -m gemma3:27b-it-qat "impress me with some physics"
```

I got [a pretty great response](https://gist.github.com/simonw/5b699ba6b7c05e2d071910e238823ff4)!

**Update**: Having spent a while putting it through its paces via [Open WebUI](https://simonwillison.net/2024/Dec/27/open-webui/) and [Tailscale](https://tailscale.com/) to access my laptop from my phone I think this may be my new favorite general\-purpose local model. Ollama appears to use 22GB of RAM while the model is running, which leaves plenty on my 64GB machine for other applications.

I've also tried it via [llm\-mlx](https://github.com/simonw/llm-mlx) like this (downloading 16GB):

```
llm install llm-mlx
llm mlx download-model mlx-community/gemma-3-27b-it-qat-4bit
llm chat -m mlx-community/gemma-3-27b-it-qat-4bit
```

It feels a little faster with MLX and uses 15GB of memory according to Activity Monitor.

---

**Link** 2025\-04\-19 [Claude Code: Best practices for agentic coding](https://www.anthropic.com/engineering/claude-code-best-practices):

Extensive new documentation from Anthropic on how to get the best results out of their [Claude Code](https://github.com/anthropics/claude-code) CLI coding agent tool, which includes this fascinating tip:

> We recommend using the word "think" to trigger extended thinking mode, which gives Claude additional computation time to evaluate alternatives more thoroughly. These specific phrases are mapped directly to increasing levels of thinking budget in the system: "think" \< "think hard" \< "think harder" \< "ultrathink." Each level allocates progressively more thinking budget for Claude to use.

Apparently **ultrathink** is a magic word!

I was curious if this was a feature of the Claude model itself or Claude Code in particular. Claude Code isn't open source but you can view the obfuscated JavaScript for it, and make it a tiny bit less obfuscated by running it through [Prettier](https://prettier.io/). With [Claude's help](https://claude.ai/share/77c398ec-6a8b-4390-91d3-6e9f0403916e) I used this recipe:

```
mkdir -p /tmp/claude-code-examine
cd /tmp/claude-code-examine
npm init -y
npm install @anthropic-ai/claude-code
cd node_modules/@anthropic-ai/claude-code
npx prettier --write cli.js
```

Then used [ripgrep](https://github.com/BurntSushi/ripgrep) to search for "ultrathink":

```
rg ultrathink -C 30
```

And found this chunk of code:

```
let B = W.message.content.toLowerCase();
if (
  B.includes("think harder") ||
  B.includes("think intensely") ||
  B.includes("think longer") ||
  B.includes("think really hard") ||
  B.includes("think super hard") ||
  B.includes("think very hard") ||
  B.includes("ultrathink")
)
  return (
    l1("tengu_thinking", { tokenCount: 31999, messageId: Z, provider: G }),
    31999
  );
if (
  B.includes("think about it") ||
  B.includes("think a lot") ||
  B.includes("think deeply") ||
  B.includes("think hard") ||
  B.includes("think more") ||
  B.includes("megathink")
)
  return (
    l1("tengu_thinking", { tokenCount: 1e4, messageId: Z, provider: G }), 1e4
  );
if (B.includes("think"))
  return (
    l1("tengu_thinking", { tokenCount: 4000, messageId: Z, provider: G }),
    4000
  );
```

So yeah, it looks like "ultrathink" is a Claude Code feature \- presumably that 31999 is a number that affects the token [thinking budget](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#implementing-extended-thinking), especially since "megathink" maps to 1e4 tokens (10,000\) and just plain "think" maps to 4,000\.

---

**Link** 2025\-04\-20 [llm\-fragments\-github 0\.2](https://github.com/simonw/llm-fragments-github/releases/tag/0.2):

I upgraded my `llm-fragments-github` plugin to add a new fragment type called `issue`. It lets you pull the entire content of a GitHub issue thread into your prompt as a concatenated Markdown file.

(If you haven't seen fragments before I introduced them in [Long context support in LLM 0\.24 using fragments and template plugins](https://simonwillison.net/2025/Apr/7/long-context-llm/).)

I used it just now to have Gemini 2\.5 Pro provide feedback and attempt an implementation of a complex issue against my [LLM](https://github.com/simonw/llm) project:

```
llm install llm-fragments-github
llm -f github:simonw/llm \
  -f issue:simonw/llm/938 \
  -m gemini-2.5-pro-exp-03-25 \
  --system 'muse on this issue, then propose a whole bunch of code to help implement it'
```

Here I'm loading the FULL content of the `simonw/llm` repo using that `-f github:simonw/llm` fragment ([documented here](https://github.com/simonw/llm-fragments-github?tab=readme-ov-file#usage)), then loading all of the comments from [issue 938](https://github.com/simonw/llm/issues/938) where I discuss quite a complex potential refactoring. I ask Gemini 2\.5 Pro to "muse on this issue" and come up with some code.

This worked *shockingly* well. Here's [the full response](https://gist.github.com/simonw/a5f0c1e8184f4ddc8b71b30890fe690c#response), which highlighted a few things I hadn't considered yet (such as the need to migrate old database records to the new tree hierarchy) and then spat out a whole bunch of code which looks like a solid start to the actual implementation work I need to do.

I ran this against Google's free Gemini 2\.5 Preview, but if I'd used the paid model it would have cost me 202,680 input tokens and 10,460 output tokens for a total of 66\.36 cents.

As a fun extra, the new `issue:` feature itself was written almost entirely by OpenAI o3, again using fragments. I ran this:

```
llm -m openai/o3 \
  -f https://raw.githubusercontent.com/simonw/llm-hacker-news/refs/heads/main/llm_hacker_news.py \
  -f https://raw.githubusercontent.com/simonw/tools/refs/heads/main/github-issue-to-markdown.html \
  -s 'Write a new fragments plugin in Python that registers issue:org/repo/123 which fetches that issue
      number from the specified github repo and uses the same markdown logic as the HTML page to turn that into a fragment'
```

Here I'm using the ability to pass a URL to `-f` and giving it the full source of my [llm\_hacker\_news.py](https://github.com/simonw/llm-hacker-news/blob/main/llm_hacker_news.py) plugin (which shows how a fragment can load data from an API) plus the [HTML source](https://github.com/simonw/tools/blob/main/github-issue-to-markdown.html) of my [github\-issue\-to\-markdown](https://tools.simonwillison.net/github-issue-to-markdown) tool (which I wrote a few months ago [with Claude](https://gist.github.com/simonw/cd1afb97e595b40fdeedebb48be7f4f1)). I effectively asked o3 to take that HTML/JavaScript tool and port it to Python to work with my fragments plugin mechanism.

o3 provided [almost the exact implementation I needed](https://gist.github.com/simonw/249e16edffe6350f7265012bee9e3305#response), and even included support for a `GITHUB_TOKEN` environment variable without me thinking to ask for it. Total cost: 19\.928 cents.

On a final note of curiosity I tried running this prompt against [Gemma 3 27B QAT](https://simonwillison.net/2025/Apr/19/gemma-3-qat-models/) running on my Mac via MLX and [llm\-mlx](https://github.com/simonw/llm-mlx):

```
llm install llm-mlx
llm mlx download-model mlx-community/gemma-3-27b-it-qat-4bit

llm -m mlx-community/gemma-3-27b-it-qat-4bit \
  -f https://raw.githubusercontent.com/simonw/llm-hacker-news/refs/heads/main/llm_hacker_news.py \
  -f https://raw.githubusercontent.com/simonw/tools/refs/heads/main/github-issue-to-markdown.html \
  -s 'Write a new fragments plugin in Python that registers issue:org/repo/123 which fetches that issue
      number from the specified github repo and uses the same markdown logic as the HTML page to turn that into a fragment'
```

That worked [pretty well too](https://gist.github.com/simonw/feccff6ce3254556b848c27333f52543#response). It turns out a 16GB local model file is powerful enough to write me an LLM plugin now!

---

**Quote** 2025\-04\-20

> *In some tasks, AI is unreliable. In others, it is superhuman. You could, of course, say the same thing about calculators, but it is also clear that AI is different. It is already demonstrating general capabilities and performing a wide range of intellectual tasks, including those that it is not specifically trained on. Does that mean that o3 and Gemini 2\.5 are AGI? Given the definitional problems, I really don’t know, but I do think they can be credibly seen as a form of “Jagged AGI” \- superhuman in enough areas to result in real changes to how we work and live, but also unreliable enough that human expertise is often needed to figure out where AI works and where it doesn’t.*

[Ethan Mollick](https://www.oneusefulthing.org/p/on-jagged-agi-o3-gemini-25-and-everything)

---

**Link** 2025\-04\-21 [Decentralizing Schemes](https://www.tbray.org/ongoing/When/202x/2025/04/16/Decentralized-Schemes):

Tim Bray discusses the challenges faced by decentralized Mastodon in that shared URLs to posts don't take into account people accessing Mastodon via their own instances, which breaks replies/likes/shares etc unless you further copy and paste URLs around yourself.

Tim proposes that the answer is URIs: a registered `fedi://mastodon.cloud/@timbray/109508984818551909` scheme could allow Fediverse\-aware software to step in and handle those URIs, similar to how `mailto:` works.

Bluesky have [registered](https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml) `at:` already, and there's also a `web+ap:` prefix registered with the intent of covering ActivityPub, the protocol used by Mastodon.

---

**Link** 2025\-04\-21 [OpenAI o3 and o4\-mini System Card](https://openai.com/index/o3-o4-mini-system-card/):

I'm surprised to see a combined System Card for o3 and o4\-mini in the same document \- I'd expect to see these covered separately.

The opening paragraph calls out the most interesting new ability of these models (see also [my notes here](https://simonwillison.net/2025/Apr/21/ai-assisted-search/#o3-and-o4-mini-are-really-good-at-search)). Tool usage isn't new, but using tools in the chain of thought appears to result in some very significant improvements:

> The models use tools in their chains of thought to augment their capabilities; for example, cropping or transforming images, searching the web, or using Python to analyze data during their thought process.

Section 3\.3 on hallucinations has been gaining a lot of attention. Emphasis mine:

> We tested OpenAI o3 and o4\-mini against PersonQA, an evaluation that aims to elicit hallucinations. PersonQA is a dataset of questions and publicly available facts that measures the model's accuracy on attempted answers.
> 
> We consider two metrics: accuracy (did the model answer the question correctly) and hallucination rate (checking how often the model hallucinated).
> 
> The o4\-mini model underperforms o1 and o3 on our PersonQA evaluation. This is expected, as smaller models have less world knowledge and tend to hallucinate more. **However, we also observed some performance differences comparing o1 and o3\. Specifically, o3 tends to make more claims overall, leading to more accurate claims as well as more inaccurate/hallucinated claims.** More research is needed to understand the cause of this result.
> 
> Table 4: PersonQA evaluation Metric o3 o4\-mini o1 accuracy (higher is better) 0\.59 0\.36 0\.47 hallucination rate (lower is better) 0\.33 0\.48 0\.16

The benchmark score on OpenAI's internal PersonQA benchmark (as far as I can tell no further details of that evaluation have been shared) going from 0\.16 for o1 to 0\.33 for o3 is interesting, but I don't know if it it's interesting enough to produce dozens of headlines along the lines of "OpenAI's o3 and o4\-mini hallucinate way higher than previous models".

The paper also talks at some length about "sandbagging". I’d previously encountered sandbagging [defined as meaning](https://simonwillison.net/2023/Apr/5/sycophancy-sandbagging/) “where models are more likely to endorse common misconceptions when their user appears to be less educated”. The o3/o4\-mini system card uses a different definition: “the model concealing its full capabilities in order to better achieve some goal” \- and links to the recent Anthropic paper [Automated Researchers Can Subtly Sandbag](https://alignment.anthropic.com/2025/automated-researchers-sandbag/).

As far as I can tell this definition relates to the American English use of “sandbagging” [to mean](https://www.merriam-webster.com/dictionary/sandbag) “to hide the truth about oneself so as to gain an advantage over another” \- as practiced by poker or pool sharks.

(Wouldn't it be nice if we could have *just one* piece of AI terminology that didn't attract multiple competing definitions?)

o3 and o4\-mini both showed some limited capability to sandbag \- to attempt to hide their true capabilities in safety testing scenarios that weren't fully described. This relates to the idea of "scheming", which I wrote about with respect to the GPT\-4o model card [last year](https://simonwillison.net/2024/Aug/8/gpt-4o-system-card/#scheming).

---

**Link** 2025\-04\-22 [Working Through the Fear of Being Seen](https://ashley.dev/posts/fear-of-being-seen/):

Heartfelt piece by Ashley Willis about the challenge of overcoming self\-doubt in publishing online:

> Part of that is knowing who might read it. A lot of the folks who follow me are smart, opinionated, and not always generous. Some are friends. Some are people I’ve looked up to. And some are just really loud on the internet. I saw someone the other day drag a certain writing style. That kind of judgment makes me want to shrink back and say, never mind.

Work to avoid being somebody who discourages others from sharing their thoughts.

---

**Link** 2025\-04\-22 [A5](https://a5geo.org):

A5 is a new "global, equal\-area, millimeter\-accurate geospatial index" by Felix Palmer:

> It is the pentagonal equivalent of other DGGSs, like S2 or H3, but with higher accuracy and lower distortion.

Effectively it's a way of dividing the entire world into pentagons where each one covers the same physical area (to within a 2% threshold) \- like Uber's [H3](https://www.uber.com/blog/h3/) but a bit weirder and more fun. An A5 reference implementation written in TypeScript is [available on GitHub](https://github.com/felixpalmer/a5).

This [interactive demo](https://a5geo.org/examples/cells) helps show how it works:

[![Animated demo. I click around on a map, each click producing a distorted pentagon shape that tessellates with those nearby. The pentagons in Norway appear larger than those in Germany, which illustrates the distortion of the standard map projection.](https://substackcdn.com/image/fetch/$s_!u94c!,w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc995365b-48bf-411b-8b1f-a890b688b8b3_808x415.gif "Animated demo. I click around on a map, each click producing a distorted pentagon shape that tessellates with those nearby. The pentagons in Norway appear larger than those in Germany, which illustrates the distortion of the standard map projection.")](https://substackcdn.com/image/fetch/$s_!u94c!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc995365b-48bf-411b-8b1f-a890b688b8b3_808x415.gif)

Why pentagons? Here's [what the A5 docs say](https://a5geo.org/docs/):

> A5 is unique in that it uses a pentagonal tiling of a dodecahedron. \[...] The benefit of choosing a dodecahedron is that it is the platonic solid with the lowest vertex curvature, and by this measure it is the most spherical of all the platonic solids. This is key for minimizing cell distortion as the process of projecting a platonic solid onto a sphere involves warping the cell geometry to force the vertex curvature to approach zero. Thus, the lower the original vertex curvature, the less distortion will be introduced by the projection.

I had to look up [platonic solids](https://en.wikipedia.org/wiki/Platonic_solid) on Wikipedia. There are only five: Tetrahedron, Cube, Octahedron, Dodecahedron and Icosahedron and they can be made using squares, triangles or (in the case of the Dodecahedron) pentagons, making the pentagon the most circle\-like option.