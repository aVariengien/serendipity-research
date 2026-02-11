# Image segmentation using Gemini 2.5

*Plus o3, o4-mini and Gemini 2.5 Flash*

Published: 2025-04-18
Source: https://simonw.substack.com/p/image-segmentation-using-gemini-25

---

In this newsletter:

* Image segmentation using Gemini 2\.5
* o3 and o4\-mini

Plus 3 links and 5 quotations

### **[Image segmentation using Gemini 2\.5](https://simonwillison.net/2025/Apr/18/gemini-image-segmentation/) \- 2025\-04\-18**

Max Woolf pointed out this new feature of the Gemini 2\.5 series (here's my coverage of [2\.5 Pro](https://simonwillison.net/2025/Mar/25/gemini/)and [2\.5 Flash](https://simonwillison.net/2025/Apr/17/start-building-with-gemini-25-flash/)) in [a comment](https://news.ycombinator.com/item?id=43720845#43722227) on Hacker News:

> One hidden note from Gemini 2\.5 Flash when diving deep into the documentation: for image inputs, not only can the model be instructed to generated 2D bounding boxes of relevant subjects, but it can also [create segmentation masks](https://ai.google.dev/gemini-api/docs/image-understanding#segmentation)!
> 
> At this price point with the Flash model, creating segmentation masks is pretty nifty.

I built a tool last year to [explore Gemini's bounding box abilities](https://simonwillison.net/2024/Aug/26/gemini-bounding-box-visualization/). This new segmentation mask feature represents a significant new capability!

Here's my new tool to try it out: **[Gemini API Image Mask Visualization](https://tools.simonwillison.net/gemini-mask)**. As with my bounding box tool it's browser\-based JavaScript that talks to the Gemini API directly. You provide it with a [Gemini API key](https://aistudio.google.com/app/apikey) which isn't logged anywhere that I can see it.

This is what it can do:

[![Screenshot of mask tool. At the top is a select box to pick a model (currently using Gemini 2.5 Pro) and a prompt that reads: Give the segmentation masks for the pelicans. Output a JSON list of segmentation masks where each entry contains the 2D bounding box in the key "box_2d" and the segmentation mask in key "mask". Below that is JSON that came back - an array of objects. The mask keys are base64 encoded PNG data. Below that is the original image, then the image with masks overlaid and a coordinate system, then two columns showing each cropped image and mask next to each other.](https://substackcdn.com/image/fetch/$s_!UOks!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc963337d-ef5b-49b5-80cc-3b1345c5eaaa_1300x3742.jpeg "Screenshot of mask tool. At the top is a select box to pick a model (currently using Gemini 2.5 Pro) and a prompt that reads: Give the segmentation masks for the pelicans. Output a JSON list of segmentation masks where each entry contains the 2D bounding box in the key \"box_2d\" and the segmentation mask in key \"mask\". Below that is JSON that came back - an array of objects. The mask keys are base64 encoded PNG data. Below that is the original image, then the image with masks overlaid and a coordinate system, then two columns showing each cropped image and mask next to each other.")](https://substackcdn.com/image/fetch/$s_!UOks!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc963337d-ef5b-49b5-80cc-3b1345c5eaaa_1300x3742.jpeg)

Give it an image and a prompt of the form:

> `Give the segmentation masks for the objects. Output a JSON list of segmentation masks where each entry contains the 2D bounding box in the key "box_2d" and the segmentation mask in key "mask".`

My tool then runs the prompt and displays the resulting JSON. The Gemini API returns segmentation masks as base64\-encoded PNG images in strings that start `data:image/png;base64,iVBOR...`. The tool then visualizes those in a few different ways on the page, including overlaid over the original image.

I [vibe coded](https://simonwillison.net/tags/vibe-coding/) the whole thing together using a combination of Claude and ChatGPT. I started with [a Claude Artifacts React prototype](https://claude.ai/share/2dd2802a-c8b4-4893-8b61-0861d4fcb0f1), then pasted the code from my old project into Claude and [hacked on that until I ran out of tokens](https://claude.ai/share/9e42d82b-56c7-46c1-ad0c-fc67c3cad91f). I transferred the incomplete result to a new Claude session where I [kept on iterating](https://claude.ai/share/f820f361-5aa7-48b5-a96d-f0f8b11d3869) until it got stuck in a bug loop (the same bug kept coming back no matter how often I told it to fix that)... so I switched over to O3 in ChatGPT [to finish it off](https://chatgpt.com/share/6801c8ad-18c8-8006-bdd8-447500eae33e).

Here's [the finished code](https://github.com/simonw/tools/blob/main/gemini-mask.html). It's a total mess, but it's also less than 500 lines of code and the interface solves my problem in that it lets me explore the new Gemini capability.

Segmenting my pelican photo via the Gemini API was *absurdly* inexpensive. Using Gemini 2\.5 Pro the call cost 303 input tokens and 353 output tokens, for a total cost of 0\.2144 cents (less than a quarter of a cent). I ran it again with the new Gemini 2\.5 Flash and it used 303 input tokens and 270 output tokens, for a total cost of 0\.099 cents (less than a tenth of a cent). I calculated these prices using my [LLM pricing calculator](https://tools.simonwillison.net/llm-prices) tool.

#### **1/100th of a cent with Gemini 2\.5 Flash non\-thinking**

Gemini 2\.5 Flash has two pricing models. Input is a standard $0\.15/million tokens, but the output charges differ a lot: in non\-thinking mode output is $0\.60/million, but if you have thinking enabled (the default) output is $3\.50/million. I think of these as "Gemini 2\.5 Flash" and "Gemini 2\.5 Flash Thinking".

My initial experiments all used thinking mode. I decided to upgrade the tool to try non\-thinking mode, but noticed that the API library it was using ([google/generative\-ai](https://github.com/google-gemini/deprecated-generative-ai-js)) is marked as deprecated.

On a hunch, I pasted the code into [the new o4\-mini\-high model](https://simonwillison.net/2025/Apr/16/introducing-openai-o3-and-o4-mini/) in ChatGPT and prompted it with:

> `This code needs to be upgraded to the new recommended JavaScript library from Google. Figure out what that is and then look up enough documentation to port this code to it`

o4\-mini and o3 both have search tool access and claim to be good at mixing different tool uses together.

This worked *extremely* well! It ran a few searches and identified exactly what needed to change:

[![Screenshot of AI assistant response about upgrading Google Gemini API code. Shows "Thought for 21 seconds" followed by web search results for "Google Gemini API JavaScript library recommended new library" with options including Google AI for Developers, GitHub, and Google for Developers. The assistant explains updating from GoogleGenerativeAI library to @google-ai/generative, with code samples showing: import { GoogleGenAI } from 'https://cdn.jsdelivr.net/npm/@google/genai@latest'; and const ai = new GoogleGenAI({ apiKey: getApiKey() });](https://substackcdn.com/image/fetch/$s_!L8_s!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67c73886-79e3-4237-baa6-4742fbb9f1fa_1298x1292.jpeg "Screenshot of AI assistant response about upgrading Google Gemini API code. Shows \"Thought for 21 seconds\" followed by web search results for \"Google Gemini API JavaScript library recommended new library\" with options including Google AI for Developers, GitHub, and Google for Developers. The assistant explains updating from GoogleGenerativeAI library to @google-ai/generative, with code samples showing: import { GoogleGenAI } from 'https://cdn.jsdelivr.net/npm/@google/genai@latest'; and const ai = new GoogleGenAI({ apiKey: getApiKey() });")](https://substackcdn.com/image/fetch/$s_!L8_s!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67c73886-79e3-4237-baa6-4742fbb9f1fa_1298x1292.jpeg)

Then gave me detailed instructions along with an updated snippet of code. Here's [the full transcript](https://chatgpt.com/share/68028f7b-11ac-8006-8150-00c4205a2507).

I prompted for a few more changes, then had to tell it not to use TypeScript (since I like copying and pasting code directly out of the tool without needing to run my own build step). The [latest version](https://tools.simonwillison.net/gemini-mask) has been rewritten by o4\-mini for the new library, defaults to Gemini 2\.5 Flash non\-thinking and displays usage tokens after each prompt.

[![Screenshot of the new tool. Gemini 2.5 Flash non-thinking is selected. Same prompt as before. Input tokens: 303 • Output tokens: 123](https://substackcdn.com/image/fetch/$s_!h1zk!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4ec4b40-9727-494e-be20-97fb964fe34a_1364x760.jpeg "Screenshot of the new tool. Gemini 2.5 Flash non-thinking is selected. Same prompt as before. Input tokens: 303 • Output tokens: 123")](https://substackcdn.com/image/fetch/$s_!h1zk!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4ec4b40-9727-494e-be20-97fb964fe34a_1364x760.jpeg)

Segmenting my pelican photo in non\-thinking mode cost me 303 input tokens and 123 output tokens \- that's 0\.0119 cents, just over 1/100th of a cent!

#### **But this looks like way more than 123 output tokens**

The JSON that's returned by the API looks *way* too long to fit just 123 tokens.

My hunch is that there's an additional transformation layer here. I think the Gemini 2\.5 models return a much more efficient token representation of the image masks, then the Gemini API layer converts those into base4\-encoded PNG image strings.

We do have one clue here: last year DeepMind [released PaliGemma](https://simonwillison.net/2024/May/15/paligemma/), an open weights vision model that could generate segmentation masks on demand.

The [README for that model](https://github.com/google-research/big_vision/blob/main/big_vision/configs/proj/paligemma/README.md#tokenizer) includes this note about how their tokenizer works:

> PaliGemma uses the Gemma tokenizer with 256,000 tokens, but we further extend its vocabulary with 1024 entries that represent coordinates in normalized image\-space (`<loc0000>...<loc1023>`), and another with 128 entries (`<seg000>...<seg127>`) that are codewords used by a lightweight referring\-expression segmentation vector\-quantized variational auto\-encoder (VQ\-VAE) \[...]

My guess is that Gemini 2\.5 is using a similar approach.

---

**Quote** 2025\-04\-15

> *The single most impactful investment I’ve seen AI teams make isn’t a fancy evaluation dashboard—it’s building a customized interface that lets anyone examine what their AI is actually doing. I emphasize customizedbecause every domain has unique needs that off\-the\-shelf tools rarely address. When reviewing apartment leasing conversations, you need to see the full chat history and scheduling context. For real\-estate queries, you need the property details and source documents right there. Even small UX decisions—like where to place metadata or which filters to expose—can make the difference between a tool people actually use and one they avoid. \[...]  
>   
> Teams with thoughtfully designed data viewers iterate 10x faster than those without them. And here’s the thing: These tools can be built in hours using AI\-assisted development (like Cursor or Loveable). The investment is minimal compared to the returns.*

[Hamel Husain](https://www.oreilly.com/radar/a-field-guide-to-rapidly-improving-ai-products/)

---

**Link** 2025\-04\-16 [openai/codex](https://github.com/openai/codex):

Just released by OpenAI, a "lightweight coding agent that runs in your terminal". Looks like their version of [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview), though unlike Claude Code Codex is released under an open source (Apache 2\) license.

Here's [the main prompt](https://github.com/openai/codex/blob/9b733fc48fb81b3f3460c1fdda111ba9b861f81f/codex-cli/src/utils/agent/agent-loop.ts#L1001-L1046) that runs in a loop, which starts like this:

> `You are operating as and within the Codex CLI, a terminal-based agentic coding assistant built by OpenAI. It wraps OpenAI models to enable natural language interaction with a local codebase. You are expected to be precise, safe, and helpful.`
> 
> `You can:`  
> `- Receive user prompts, project context, and files.`  
> `- Stream responses and emit function calls (e.g., shell commands, code edits).`  
> `- Apply patches, run commands, and manage user approvals based on policy.`  
> `- Work inside a sandboxed, git-backed workspace with rollback support.`  
> `- Log telemetry so sessions can be replayed or inspected later.`  
> `- More details on your functionality are available at codex --help`
> 
> `The Codex CLI is open-sourced. Don't confuse yourself with the old Codex language model built by OpenAI many moons ago (this is understandably top of mind for you!). Within this context, Codex refers to the open-source agentic coding interface. [...]`

I like that the prompt describes OpenAI's previous Codex language model as being from "many moons ago". Prompt engineering is so weird.

Since the prompt says that it works "inside a sandboxed, git\-backed workspace" I went looking for the sandbox. On macOS [it uses](https://github.com/openai/codex/blob/9b733fc48fb81b3f3460c1fdda111ba9b861f81f/codex-cli/src/utils/agent/sandbox/macos-seatbelt.ts) the little\-known `sandbox-exec` process, part of the OS but grossly under\-documented. The best information I've found about it is [this article from 2020](https://www.karltarvas.com/macos-app-sandboxing-via-sandbox-exec.html), which notes that `man sandbox-exec` lists it as deprecated. I didn't spot evidence in the Codex code of sandboxes for other platforms.

---

**Link** 2025\-04\-16 [Introducing OpenAI o3 and o4\-mini](https://openai.com/index/introducing-o3-and-o4-mini/):

OpenAI are *really* emphasizing tool use with these:

> For the first time, our reasoning models can agentically use and combine every tool within ChatGPT—this includes searching the web, analyzing uploaded files and other data with Python, reasoning deeply about visual inputs, and even generating images. Critically, these models are trained to reason about when and how to use tools to produce detailed and thoughtful answers in the right output formats, typically in under a minute, to solve more complex problems.

I released [llm\-openai\-plugin 0\.3](https://github.com/simonw/llm-openai-plugin/releases/tag/0.3) adding support for the two new models:

```
llm install -U llm-openai-plugin
llm -m openai/o3 "say hi in five languages"
llm -m openai/o4-mini "say hi in five languages"
```

Here are [the pelicans riding bicycles](https://simonwillison.net/tags/pelican-riding-a-bicycle/) (prompt: `Generate an SVG of a pelican riding a bicycle`).

**o3**:

[![Described by o3: The illustration shows a playful, stylized bicycle whose frame is drawn to resemble a duck. • The duck’s rounded body forms the bicycle’s seat area, and a small wing is sketched on its side.  • Its long neck stretches forward to become the top tube, ending in a simple head with a black eye and an orange, open beak that points ahead like handlebars.  • Two large black‑outlined wheels with thin, evenly spaced spokes complete the bike, while thin blue lines depict the rest of the frame, pedals, and chain.  • A dashed grey ground line runs beneath the wheels, giving the impression the duck‑bike is rolling along.](https://substackcdn.com/image/fetch/$s_!zIKr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa642ec3a-d98f-4dcd-b4fc-1572a3f4a757_800x600.jpeg "Described by o3: The illustration shows a playful, stylized bicycle whose frame is drawn to resemble a duck. • The duck’s rounded body forms the bicycle’s seat area, and a small wing is sketched on its side.  • Its long neck stretches forward to become the top tube, ending in a simple head with a black eye and an orange, open beak that points ahead like handlebars.  • Two large black‑outlined wheels with thin, evenly spaced spokes complete the bike, while thin blue lines depict the rest of the frame, pedals, and chain.  • A dashed grey ground line runs beneath the wheels, giving the impression the duck‑bike is rolling along.")](https://substackcdn.com/image/fetch/$s_!zIKr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa642ec3a-d98f-4dcd-b4fc-1572a3f4a757_800x600.jpeg)

**o4\-mini**:

[![Described by o4-mini: The image is a very simple, minimalistic line drawing of a bird riding a bicycle, rendered against a plain white background.  Key elements:   • Two large, identical circles for the bike’s wheels, outlined in thick black.   • A horizontal bar links the rear wheel to the bird’s body; a slanted bar links the front wheel to the bird.   • The front wheel has a single straight spoke ending in an arrowhead, suggesting the forward direction of travel.   • The bird itself is drawn with basic shapes:     – A small circle for the head, with a single dot for the eye and a short yellow triangle for the beak.     – An oval for the body.     – Thin lines for the neck, legs, and the bike’s pedals and handlebars.   • The bird appears perched on the saddle, its legs extending down to the pedals, and its tiny wings resting near the handlebars.](https://substackcdn.com/image/fetch/$s_!4Kne!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9cab5ac5-72ce-4fd0-b677-2221038fde1f_800x600.jpeg "Described by o4-mini: The image is a very simple, minimalistic line drawing of a bird riding a bicycle, rendered against a plain white background.  Key elements:   • Two large, identical circles for the bike’s wheels, outlined in thick black.   • A horizontal bar links the rear wheel to the bird’s body; a slanted bar links the front wheel to the bird.   • The front wheel has a single straight spoke ending in an arrowhead, suggesting the forward direction of travel.   • The bird itself is drawn with basic shapes:     – A small circle for the head, with a single dot for the eye and a short yellow triangle for the beak.     – An oval for the body.     – Thin lines for the neck, legs, and the bike’s pedals and handlebars.   • The bird appears perched on the saddle, its legs extending down to the pedals, and its tiny wings resting near the handlebars.")](https://substackcdn.com/image/fetch/$s_!4Kne!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9cab5ac5-72ce-4fd0-b677-2221038fde1f_800x600.jpeg)

Here are the full OpenAI model listings: [o3](https://platform.openai.com/docs/models/o3) is $10/million input and $40/million for output, with a 75% discount on cached input tokens, 200,000 token context window, 100,000 max output tokens and a May 31st 2024 training cut\-off (same as the GPT\-4\.1 models). It's a bit cheaper than o1 ($15/$60\) and a *lot* cheaper than o1\-pro ($150/$600\).

[o4\-mini](https://platform.openai.com/docs/models/o4-mini) is priced the same as o3\-mini: $1\.10/million for input and $4\.40/million for output, also with a 75% input caching discount. The size limits and training cut\-off are the same as o3\.

You can compare these prices with other models using the table on my [updated LLM pricing calculator](https://tools.simonwillison.net/llm-prices).

A new capability released today is that the OpenAI API can now optionally return reasoning summary text. I've been exploring that [in this issue](https://github.com/simonw/llm-openai-plugin/issues/16). I believe you have to verify your organization (which may involve a photo ID) in order to use this option \- once you have access the easiest way to see the new tokens is using `curl` like this:

```
curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $(llm keys get openai)" \
  -d '{
    "model": "o3",
    "input": "why is the sky blue?",
    "reasoning": {"summary": "auto"},
    "stream": true
  }'
```

This produces a stream of events that includes this new event type:

`event: response.reasoning_summary_text.delta`  
`data: {"type": "response.reasoning_summary_text.delta","item_id": "rs_68004320496081918e1e75ddb550d56e0e9a94ce520f0206","output_index": 0,"summary_index": 0,"delta": "**Expl"}`

Omit the `"stream": true` and the response is easier to read and contains this:

```
{
  "output": [
    {
      "id": "rs_68004edd2150819183789a867a9de671069bc0c439268c95",
      "type": "reasoning",
      "summary": [
        {
          "type": "summary_text",
          "text": "**Explaining the blue sky**\n\nThe user asks a classic question about why the sky is blue. I'll talk about Rayleigh scattering, where shorter wavelengths of light scatter more than longer ones. This explains how we see blue light spread across the sky! I wonder if the user wants a more scientific or simpler everyday explanation. I'll aim for a straightforward response while keeping it engaging and informative. So, let's break it down!"
        }
      ]
    },
    {
      "id": "msg_68004edf9f5c819188a71a2c40fb9265069bc0c439268c95",
      "type": "message",
      "status": "completed",
      "content": [
        {
          "type": "output_text",
          "annotations": [],
          "text": "The short answer ..."
        }
      ]
    }
  ]
}
```

---

**Quote** 2025\-04\-16

> *I work for OpenAI. \[...] o4\-mini is actually a considerably better vision model than o3, despite the benchmarks. Similar to how o3\-mini\-high was a much better coding model than o1\. I would recommend using o4\-mini\-high over o3 for any task involving vision.*

[James Betker](https://news.ycombinator.com/item?id=43707719#43711155)

---

**Quote** 2025\-04\-17

> *Our hypothesis is that o4\-mini is a much better model, but we'll wait to hear feedback from developers. Evals only tell part of the story, and we wouldn't want to prematurely deprecate a model that developers continue to find value in. Model behavior is extremely high dimensional, and it's impossible to prevent regression on 100% use cases/prompts, especially if those prompts were originally tuned to the quirks of the older model. But if the majority of developers migrate happily, then it may make sense to deprecate at some future point.  
>   
> We generally want to give developers as stable as an experience as possible, and not force them to swap models every few months whether they want to or not.*

[Ted Sanders, OpenAI](https://news.ycombinator.com/item?id=43710698)

---

**Quote** 2025\-04\-17

> *We (Jon and Zach) teamed up with the Harris Poll to confirm this finding and extend it. We [conducted a nationally representative survey](https://theharrispoll.com/briefs/gen-z-social-media-smart-phones/)of 1,006 Gen Z young adults (ages 18\-27\). We asked respondents to tell us, for various platforms and products, if they wished that it “was never invented.” For Netflix, Youtube, and the internet itself, relatively few said yes to that question (always under 20%). We found much higher levels of regret for the dominant social media platforms: Instagram (34%), Facebook (37%), Snapchat (43%), and the most regretted platforms of all: TikTok (47%) and X/Twitter (50%).*

[Jon Haidt and Zach Rausch](https://www.afterbabel.com/p/industrial-scale-harm-tiktok)

---

**Link** 2025\-04\-17 [Start building with Gemini 2\.5 Flash](https://developers.googleblog.com/en/start-building-with-gemini-25-flash/):

Google Gemini's latest model is Gemini 2\.5 Flash, available in (paid) preview as `gemini-2.5-flash-preview-04-17`.

> Building upon the popular foundation of 2\.0 Flash, this new version delivers a major upgrade in reasoning capabilities, while still prioritizing speed and cost. Gemini 2\.5 Flash is our first fully hybrid reasoning model, giving developers the ability to turn thinking on or off. The model also allows developers to set thinking budgets to find the right tradeoff between quality, cost, and latency.

Gemini AI Studio product lead Logan Kilpatrick [says](https://twitter.com/OfficialLoganK/status/1912966500794654855):

> This is an early version of 2\.5 Flash, but it already shows huge gains over 2\.0 Flash.
> 
> You can fully turn off thinking if needed and use this model as a drop in replacement for 2\.0 Flash.

I added support to the new model in [llm\-gemini 0\.18](https://github.com/simonw/llm-gemini/releases/tag/0.18). Here's how to try it out:

```
llm install -U llm-gemini
llm -m gemini-2.5-flash-preview-04-17 'Generate an SVG of a pelican riding a bicycle'
```

Here's that first pelican, using the default setting where Gemini Flash 2\.5 makes its own decision in terms of how much "thinking" effort to apply:

[![Described below](https://substackcdn.com/image/fetch/$s_!kb7d!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2099f1e0-d667-4473-bb25-3f21275bff50_800x500.jpeg "Described below")](https://substackcdn.com/image/fetch/$s_!kb7d!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2099f1e0-d667-4473-bb25-3f21275bff50_800x500.jpeg)

Here's [the transcript](https://gist.github.com/simonw/afce6639ed10c712a0778fc779efd756). This one used 11 input tokens and 4266 output tokens of which 2702 were "thinking" tokens.

I asked the model to "`describe`" that image and it could tell it was meant to be a pelican:

> A simple illustration on a white background shows a stylized pelican riding a bicycle. The pelican is predominantly grey with a black eye and a prominent pink beak pouch. It is positioned on a black line\-drawn bicycle with two wheels, a frame, handlebars, and pedals.

The way the model is priced is a little complicated. If you have thinking enabled, you get charged $0\.15/million tokens for input and $3\.50/million for output. With thinking disabled those output tokens drop to $0\.60/million. I've added these [to my pricing calculator](https://tools.simonwillison.net/llm-prices).

For comparison, Gemini 2\.0 Flash is $0\.10/million input and $0\.40/million for output.

So my first prompt \- 11 input and 4266 output(with thinking enabled), cost 1\.4933 cents.

Let's try 2\.5 Flash again with thinking disabled:

```
llm -m gemini-2.5-flash-preview-04-17 'Generate an SVG of a pelican riding a bicycle' -o thinking_budget 0
```

[![Described below, again](https://substackcdn.com/image/fetch/$s_!JNzY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb7e436d6-0ca4-40f0-a991-74d96cff8324_800x533.jpeg "Described below, again")](https://substackcdn.com/image/fetch/$s_!JNzY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb7e436d6-0ca4-40f0-a991-74d96cff8324_800x533.jpeg)

11 input, 1705 output. That's 0\.1025 cents. [Transcript here](https://gist.github.com/simonw/182679e918ab5263f98f6a65691874d1) \- it still shows 25 thinking tokens even though I set the thinking budget to 0 \- Logan [confirms](https://twitter.com/OfficialLoganK/status/1912986097765789782) that this will still be billed at the lower rate:

> In some rare cases, the model still thinks a little even with thinking budget \= 0, we are hoping to fix this before we make this model stable and you won't be billed for thinking. The thinking budget \= 0 is what triggers the billing switch.

Here's Gemini 2\.5 Flash's self\-description of that image:

> A minimalist illustration shows a bright yellow bird riding a bicycle. The bird has a simple round body, small wings, a black eye, and an open orange beak. It sits atop a simple black bicycle frame with two large circular black wheels. The bicycle also has black handlebars and black and yellow pedals. The scene is set against a solid light blue background with a thick green stripe along the bottom, suggesting grass or ground.

And finally, let's ramp the thinking budget up to the maximum:

```
llm -m gemini-2.5-flash-preview-04-17 'Generate an SVG of a pelican riding a bicycle' -o thinking_budget 24576
```

[![Described below](https://substackcdn.com/image/fetch/$s_!pB8D!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa14cd0cb-0a98-4552-a6d7-aae02139617b_800x500.jpeg "Described below")](https://substackcdn.com/image/fetch/$s_!pB8D!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa14cd0cb-0a98-4552-a6d7-aae02139617b_800x500.jpeg)

I think it over\-thought this one. [Transcript](https://gist.github.com/simonw/6a83bd7ad114ee23c460f5246b854247) \- 5174 output tokens of which 3023 were thinking. A hefty 1\.8111 cents!

> A simple, cartoon\-style drawing shows a bird\-like figure riding a bicycle. The figure has a round gray head with a black eye and a large, flat orange beak with a yellow stripe on top. Its body is represented by a curved light gray shape extending from the head to a smaller gray shape representing the torso or rear. It has simple orange stick legs with round feet or connections at the pedals. The figure is bent forward over the handlebars in a cycling position. The bicycle is drawn with thick black outlines and has two large wheels, a frame, and pedals connected to the orange legs. The background is plain white, with a dark gray line at the bottom representing the ground.

One thing I really appreciate about Gemini 2\.5 Flash's approach to SVGs is that it shows very good taste in CSS, comments and general SVG class structure. Here's a truncated extract \- I run a lot of these SVG tests against different models and this one has a coding style that I particularly enjoy. (Gemini 2\.5 Pro [does this too](https://gist.github.com/simonw/c34f7f0c94afcbeab77e170511f6f51f)).

```
<svg width="800" height="500" viewBox="0 0 800 500" xmlns="http://www.w3.org/2000/svg">
  <style>
    .bike-frame { fill: none; stroke: #333; stroke-width: 8; stroke-linecap: round; stroke-linejoin: round; }
    .wheel-rim { fill: none; stroke: #333; stroke-width: 8; }
    .wheel-hub { fill: #333; }
    /* ... */
    .pelican-body { fill: #d3d3d3; stroke: black; stroke-width: 3; }
    .pelican-head { fill: #d3d3d3; stroke: black; stroke-width: 3; }
    /* ... */
  </style>
  <!-- Ground Line -->
  <line x1="0" y1="480" x2="800" y2="480" stroke="#555" stroke-width="5"/>
  <!-- Bicycle -->
  <g id="bicycle">
    <!-- Wheels -->
    <circle class="wheel-rim" cx="250" cy="400" r="70"/>
    <circle class="wheel-hub" cx="250" cy="400" r="10"/>
    <circle class="wheel-rim" cx="550" cy="400" r="70"/>
    <circle class="wheel-hub" cx="550" cy="400" r="10"/>
    <!-- ... -->
  </g>
  <!-- Pelican -->
  <g id="pelican">
    <!-- Body -->
    <path class="pelican-body" d="M 440 330 C 480 280 520 280 500 350 C 480 380 420 380 440 330 Z"/>
    <!-- Neck -->
    <path class="pelican-neck" d="M 460 320 Q 380 200 300 270"/>
    <!-- Head -->
    <circle class="pelican-head" cx="300" cy="270" r="35"/>
    <!-- ... -->
```

The [LM Arena leaderboard](https://lmarena.ai/?leaderboard) now has Gemini 2\.5 Flash [in joint second place](https://twitter.com/lmarena_ai/status/1912955625224773911), just behind Gemini 2\.5 Pro and tied with ChatGPT\-4o\-latest, Grok\-3 and GPT\-4\.5 Preview.

[![Screenshot of a table showing AI model rankings with columns Rank* (UB), Rank (StyleCtrl), Model, Arena Score, 95% CI, Votes, Organization, and License. The rows show data for: Gemini-2.5-Pro-Exp-03-25 ranked 1/1 with score 1439, CI +7/-5, 9013 Votes, Organization Google, License Proprietary. ChatGPT-4o-latest (2025-03-26) ranked 2/2 with score 1407, CI +6/-6, 8261 Votes, Organization OpenAI, License Proprietary. Grok-3-Preview-02-24 ranked 2/4 with score 1402, CI +5/-3, 14849 Votes, Organization xAI, License Proprietary. GPT-4.5-Preview ranked 2/2 with score 1398, CI +5/-6, 14520 Votes, Organization OpenAI, License Proprietary. Gemini-2.5-Flash-Preview-04-17 ranked 2/4 with score 1392, CI +10/-13, 3325 Votes, Organization Google, License Proprietary](https://substackcdn.com/image/fetch/$s_!artv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7cb78b0e-42b4-43d2-b7b1-2e74f34be34d_2042x672.jpeg "Screenshot of a table showing AI model rankings with columns Rank* (UB), Rank (StyleCtrl), Model, Arena Score, 95% CI, Votes, Organization, and License. The rows show data for: Gemini-2.5-Pro-Exp-03-25 ranked 1/1 with score 1439, CI +7/-5, 9013 Votes, Organization Google, License Proprietary. ChatGPT-4o-latest (2025-03-26) ranked 2/2 with score 1407, CI +6/-6, 8261 Votes, Organization OpenAI, License Proprietary. Grok-3-Preview-02-24 ranked 2/4 with score 1402, CI +5/-3, 14849 Votes, Organization xAI, License Proprietary. GPT-4.5-Preview ranked 2/2 with score 1398, CI +5/-6, 14520 Votes, Organization OpenAI, License Proprietary. Gemini-2.5-Flash-Preview-04-17 ranked 2/4 with score 1392, CI +10/-13, 3325 Votes, Organization Google, License Proprietary")](https://substackcdn.com/image/fetch/$s_!artv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7cb78b0e-42b4-43d2-b7b1-2e74f34be34d_2042x672.jpeg)

---

**Link** 2025\-04\-18 [MCP Run Python](https://github.com/pydantic/pydantic-ai/tree/main/mcp-run-python):

Pydantic AI's MCP server for running LLM\-generated Python code in a sandbox. They ended up using a trick I explored [two years ago](https://til.simonwillison.net/deno/pyodide-sandbox): using a [Deno](https://deno.com/) process to run [Pyodide](https://pyodide.org/) in a WebAssembly sandbox.

Here's a bit of a wild trick: since Deno loads code on\-demand from [JSR](https://jsr.io/), and [uv run](https://docs.astral.sh/uv/guides/scripts/) can install Python dependencies on demand via the `--with`option... here's a one\-liner you can paste into a macOS shell (provided you have Deno and `uv`installed already) which will run the example from [their README](https://github.com/pydantic/pydantic-ai/blob/v0.1.2/mcp-run-python/README.md) \- calculating the number of days between two dates in the most complex way imaginable:

```
ANTHROPIC_API_KEY="sk-ant-..." \
uv run --with pydantic-ai python -c '
import asyncio
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio

server = MCPServerStdio(
    "deno",
    args=[
        "run",
        "-N",
        "-R=node_modules",
        "-W=node_modules",
        "--node-modules-dir=auto",
        "jsr:@pydantic/mcp-run-python",
        "stdio",
    ],
)
agent = Agent("claude-3-5-haiku-latest", mcp_servers=[server])

async def main():
    async with agent.run_mcp_servers():
        result = await agent.run("How many days between 2000-01-01 and 2025-03-18?")
    print(result.output)

asyncio.run(main())'
```

I ran that just now and got:

> The number of days between January 1st, 2000 and March 18th, 2025 is 9,208 days.

I thoroughly enjoy how tools like `uv` and Deno enable throwing together shell one\-liner demos like this one.

Here's [an extended version](https://gist.github.com/simonw/54fc42ef9a7fb8f777162bbbfbba4f23) of this example which adds pretty\-printed logging of the messages exchanged with the LLM to illustrate exactly what happened. The most important piece is this tool call where Claude 3\.5 Haiku asks for Python code to be executed my the MCP server:

```
ToolCallPart(
    tool_name='run_python_code',
    args={
        'python_code': (
            'from datetime import date\n'
            '\n'
            'date1 = date(2000, 1, 1)\n'
            'date2 = date(2025, 3, 18)\n'
            '\n'
            'days_between = (date2 - date1).days\n'
            'print(f"Number of days between {date1} and {date2}: {days_between}")'
        ),
    },
    tool_call_id='toolu_01TXXnQ5mC4ry42DrM1jPaza',
    part_kind='tool-call',
)
```

I also managed to run it against [Mistral Small 3\.1](https://ollama.com/library/mistral-small3.1)(15GB) running locally using [Ollama](https://ollama.com/) (I had to add "Use your python tool" to the prompt to get it to work):

```
ollama pull mistral-small3.1:24b

uv run --with devtools --with pydantic-ai python -c '
import asyncio
from devtools import pprint
from pydantic_ai import Agent, capture_run_messages
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai.mcp import MCPServerStdio

server = MCPServerStdio(
    "deno",
    args=[
        "run",
        "-N",
        "-R=node_modules",
        "-W=node_modules",
        "--node-modules-dir=auto",
        "jsr:@pydantic/mcp-run-python",
        "stdio",
    ],
)

agent = Agent( 
    OpenAIModel(                          
        model_name="mistral-small3.1:latest",
        provider=OpenAIProvider(base_url="http://localhost:11434/v1"),                
    ),            
    mcp_servers=[server],
)

async def main():
    with capture_run_messages() as messages:
        async with agent.run_mcp_servers():
            result = await agent.run("How many days between 2000-01-01 and 2025-03-18? Use your python tool.")
    pprint(messages)
    print(result.output)

asyncio.run(main())'
```

Here's [the full output](https://gist.github.com/simonw/e444a81440bda2f37b0fef205780074a) including the debug logs.

---

**Quote** 2025\-04\-18

> *To me, a successful eval meets the following criteria. Say, we currently have system A, and we might tweak it to get a system B:  
>   
> \- If A works significantly better than B according to a skilled human judge, the eval should give A a significantly higher score than B.  
> \- If A and B have similar performance, their eval scores should be similar.  
>   
> Whenever a pair of systems A and B contradicts these criteria, that is a sign the eval is in “error” and we should tweak it to make it rank A and B correctly.*

[Andrew Ng](https://www.deeplearning.ai/the-batch/issue-297/)

---