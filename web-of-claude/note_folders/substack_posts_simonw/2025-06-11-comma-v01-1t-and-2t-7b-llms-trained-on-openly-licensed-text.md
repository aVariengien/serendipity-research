# Comma v0.1 1T and 2T - 7B LLMs trained on openly licensed text

*Plus o3-pro, Mistral's Magistral, 80% cheaper o3*

Published: 2025-06-11
Source: https://simonw.substack.com/p/comma-v01-1t-and-2t-7b-llms-trained

---

In this newsletter:

* Comma v0\.1 1T and 2T \- 7B LLMs trained on openly licensed text

Plus 6 links and 3 quotations and 1 note

### **[Comma v0\.1 1T and 2T \- 7B LLMs trained on openly licensed text](https://simonwillison.net/2025/Jun/7/comma/) \- 2025\-06\-07**

It's been a long time coming, but we finally have some promising LLMs to try out which are trained entirely on openly licensed text!

EleutherAI released [the Pile](https://arxiv.org/abs/2101.00027) four and a half years ago: "an 800GB dataset of diverse text for language modeling". It's been used as the basis for many LLMs since then, but much of the data in it came from [Common Crawl](https://commoncrawl.org/) \- a crawl of the public web which mostly ignored the licenses of the data it was collecting.

[The Common Pile v0\.1](https://huggingface.co/blog/stellaathena/common-pile) is EleutherAI's successor to the original Pile, in collaboration with a large group of other organizations with whom they have been "meticulously curating a 8 TB corpus of openly licensed and public domain text for training large language models".

The dataset is exciting, but on top of that they've released two new LLMs that have been trained on it: Comma v0\.1 1T and 2T, both with 7 billion parameters, the first trained on 1 trillion tokens and the second on 2 trillion tokens.

These are available on Hugging Face as [common\-pile/comma\-v0\.1\-1t](https://huggingface.co/common-pile/comma-v0.1-1t) and [common\-pile/comma\-v0\.1\-2t](https://huggingface.co/common-pile/comma-v0.1-2t).

EleutherAI claim that these new models perform "comparably to leading models trained in the same regime on unlicensed data". I decided to try them out myself.

The models are currently only available as `.safetensors` files, which I've found difficult to run on macOS in the past. I decided to see if I could convert them to [MLX](https://github.com/ml-explore/mlx) format which I know how to run on my Mac.

MLX is still a very new format, but Claude 4 Sonnet has a training cutoff date of March 2025 so I crossed my fingers and hoped it would be able to help me out. [It did exactly that!](https://claude.ai/share/379951f0-4fb2-4b70-b6f9-f8a3afae1e33) I ran the following command to convert the 2T model to run using MLX:

```
uv run --python 3.12 \
  --with mlx-lm \
  python -m mlx_lm convert \
    --hf-path common-pile/comma-v0.1-2t \
    --mlx-path ./comma-v0.1-2t-mlx
```

I uploaded the converted model to Hugging Face as [simonw/comma\-v0\.1\-2t\-mlx](https://huggingface.co/simonw/comma-v0.1-2t-mlx).

Now that it's on the Hub here's how to try it out (using `uv run`):

```
uv run --python 3.12 \
  --with mlx-lm \
  mlx_lm.generate \
    --model simonw/comma-v0.1-2t-mlx \
    --prompt 'Facts about pelicans:'
```

The first time you run this it will download 13GB of files to `~/.cache/huggingface/hub/models--simonw--comma-v0.1-2t-mlx`.

Here's what I got back:

> `1. They are the largest of the water birds. 2. They are found in all parts of the world. 3. They are very good swimmers. 4. They are very good divers. 5. They are very good flyers. 6. They are very good hunters. 7. They are very good eaters. 8. They are very good parents. 9. They are very good friends. 10.`

The big limitation of this model right now is that it's a raw base model \- it hasn't been instruction\-tuned or set up for chat.

This means you have to prefix\-prompt it, like in the GPT\-3 days. You need to give it a sentence for it to complete.

This makes it a lot harder to evaluate than the instruction\-tuned models that I've become used to over the past few years!

I'm hoping someone releases a chat\-tuned version of this model soon. The challenge there will be keeping to the openly licensed training data, since most of the fine\-tuning datasets out there for this are themselves derived from models that were trained on unlicensed data.

Sadly it didn't do too well on my [pelican on a bicycle](https://simonwillison.net/2025/Jun/6/six-months-in-llms/#ai-worlds-fair-2025-02.jpeg) benchmark:

```
uv run --python 3.12 \
  --with mlx-lm \
  mlx_lm.generate \
    --model simonw/comma-v0.1-2t-mlx \
    --prompt 'An SVG of a pelican riding a bicycle: <svg' --max-tokens 2000
```

The output started like this and looped indefinitely:

> `xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0 0 100 100"><path d="M0 0h100v100H0z" fill="none"/><path d="M0 0h100v100H0z" fill="none"/><path d="M0 0h100v100H0z" fill="none"/><path d="M0 0h100v100H0z" fill="none"/><path d="M0 0h100v100H0z" fill="none"/><path d="M0 0h100v100H0z" fill="none"/><path d="M0 0h100v100H0z" fill="none"/><path d="M0 0h100v100H0z" fill="none"/>...`

---

**Quote** 2025\-06\-07

> *For \[Natasha] Lyonne, the draw of AI isn’t speed or scale — it’s independence. “I’m not trying to run a tech company,” she told me. “It’s more that I’m a filmmaker who doesn’t want the tech people deciding the future of the medium.” She imagines a future in which indie filmmakers can use AI tools to reclaim authorship from studios and avoid the compromises that come with chasing funding in a broken system.  
>   
> “We need some sort of Dogme 95 for the AI era,” Lyonne said, referring to the stripped\-down 1990s filmmaking movement started by Lars von Trier and Thomas Vinterberg, which sought to liberate cinema from an overreliance on technology. “If we could just wrangle this artist\-first idea before it becomes industry standard to not do it that way, that’s something I would be interested in working on. Almost like we are not going to go quietly into the night.”*

[Lila Shapiro](https://www.vulture.com/article/generative-ai-hollywood-movies-tv.html)

---

**Link** 2025\-06\-08 [Qwen3 Embedding](https://qwenlm.github.io/blog/qwen3-embedding/):

New family of embedding models from Qwen, in three sizes: 0\.6B, 4B, 8B \- and two categories: Text Embedding and Text Reranking.

The full collection [can be browsed](https://huggingface.co/collections/Qwen/qwen3-embedding-6841b2055b99c44d9a4c371f) on Hugging Face. The smallest available model is the 0\.6B Q8 one, which is available as a 639MB GGUF. I tried it out using my [llm\-sentence\-transformers](https://github.com/simonw/llm-sentence-transformers) plugin like this:

```
llm install llm-sentence-transformers
llm sentence-transformers register Qwen/Qwen3-Embedding-0.6B
llm embed -m sentence-transformers/Qwen/Qwen3-Embedding-0.6B -c hi | jq length
```

This output 1024, confirming that Qwen3 0\.6B produces 1024 length embedding vectors.

These new models are the highest scoring open\-weight models on the well regarded [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard) \- they're licensed Apache 2\.0\.

[![Table showing ranking of embedding models with columns for Rank, Model name, Zero-shot performance, Memory Usage, Number of Parameters, Embedding Dimensions, and Max Tokens. Top models include gemini-embedding-001 at rank 1 with 99% zero-shot and 3072 embedding dimensions, Qwen3-Embedding-8B at rank 2 with 99% zero-shot and 4096 embedding dimensions, and several other Qwen3 variants. Most models show 99% zero-shot performance with green highlighting, except gte-Qwen2-7B-instruct at rank 6 which shows "NA" with red highlighting and a warning triangle icon.](https://substackcdn.com/image/fetch/$s_!tdT7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F29c40ec4-1556-4a96-969f-45610c4d80d6_1026x541.jpeg "Table showing ranking of embedding models with columns for Rank, Model name, Zero-shot performance, Memory Usage, Number of Parameters, Embedding Dimensions, and Max Tokens. Top models include gemini-embedding-001 at rank 1 with 99% zero-shot and 3072 embedding dimensions, Qwen3-Embedding-8B at rank 2 with 99% zero-shot and 4096 embedding dimensions, and several other Qwen3 variants. Most models show 99% zero-shot performance with green highlighting, except gte-Qwen2-7B-instruct at rank 6 which shows \"NA\" with red highlighting and a warning triangle icon.")](https://substackcdn.com/image/fetch/$s_!tdT7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F29c40ec4-1556-4a96-969f-45610c4d80d6_1026x541.jpeg)

You can also try them out in your web browser, thanks to a [Transformers.js](https://huggingface.co/docs/transformers.js/en/index) port of the models. I loaded [this page in Chrome](https://huggingface.co/spaces/webml-community/qwen3-embedding-webgpu) ([source code here](https://huggingface.co/spaces/webml-community/qwen3-embedding-webgpu/tree/main)) and it fetched 560MB of model files and gave me an interactive interface for visualizing clusters of embeddings like this:

[![Screenshot of a text embedding web application interface showing a "Sentences" panel on the left with various sample sentences about topics like cooking, technology, sports, finance, music, and history, a "Labels" section below listing these categories, and a "Scatterplot" visualization on the right displaying colored clusters of data points representing the embedded sentences grouped by topic, with an "Embed & Plot" button at the bottom and instructions to "Done! Hover over points to see sentences."](https://substackcdn.com/image/fetch/$s_!9Kge!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fca6eedc4-69a2-4a77-bf70-c732ae23eaba_1565x900.jpeg "Screenshot of a text embedding web application interface showing a \"Sentences\" panel on the left with various sample sentences about topics like cooking, technology, sports, finance, music, and history, a \"Labels\" section below listing these categories, and a \"Scatterplot\" visualization on the right displaying colored clusters of data points representing the embedded sentences grouped by topic, with an \"Embed & Plot\" button at the bottom and instructions to \"Done! Hover over points to see sentences.\"")](https://substackcdn.com/image/fetch/$s_!9Kge!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fca6eedc4-69a2-4a77-bf70-c732ae23eaba_1565x900.jpeg)

---

**Quote** 2025\-06\-09

> *The process of learning and experimenting with LLM\-derived technology has been an exercise in humility. In general I love learning new things when the art of programming changes \[…] But LLMs, and more specifically Agents, affect the process of writing programs in a new and confusing way. Absolutely every fundamental assumption about how I work has to be questioned, and it ripples through all the experience I have accumulated. There are days when it feels like I would be better off if I did not know anything about programming and started from scratch. And it is still changing.*

[David Crawshaw](https://crawshaw.io/blog/programming-with-agents)

---

**Link** 2025\-06\-09 [OpenAI hits $10 billion in annual recurring revenue fueled by ChatGPT growth](https://www.cnbc.com/2025/06/09/openai-hits-10-billion-in-annualized-revenue-fueled-by-chatgpt-growth.html):

Noteworthy because OpenAI revenue is a useful indicator of the direction of the generative AI industry in general, and frequently comes up in conversations about the sustainability of the current bubble.

> OpenAI has hit $10 billion in annual recurring revenue less than three years after launching its popular ChatGPT chatbot.
> 
> The figure includes sales from the company’s consumer products, ChatGPT business products and its application programming interface, or API. It excludes licensing revenue from Microsoft and large one\-time deals, according to an OpenAI spokesperson.
> 
> For all of last year, OpenAI was around $5\.5 billion in ARR. \[...]

So these new numbers represent nearly double the ARR figures for last year.

---

**Link** 2025\-06\-09 [WWDC: Apple supercharges its tools and technologies for developers](https://www.apple.com/newsroom/2025/06/apple-supercharges-its-tools-and-technologies-for-developers/):

Here's the Apple press release for today's WWDC announcements. Two things that stood out to me:

> **Foundation Models Framework**
> 
> With the Foundation Models framework, developers will be able to build on Apple Intelligence to bring users new experiences that are intelligent, available when they’re offline, and that protect their privacy, using AI inference that is free of cost. The framework has native support for Swift, so developers can easily access the Apple Intelligence model with as few as three lines of code.

Here's new documentation on [Generating content and performing tasks with Foundation Models](https://developer.apple.com/documentation/FoundationModels/generating-content-and-performing-tasks-with-foundation-models) \- the Swift code looks like this:

```
let session = LanguageModelSession(
    instructions: "Reply with step by step instructions"
)
let prompt = "Rum old fashioned cocktail"
let response = try await session.respond(
    to: prompt,
    options: GenerationOptions(temperature: 2.0)
)
```

There's also a [23 minute Meet the Foundation Models framework](https://developer.apple.com/videos/play/wwdc2025/286/) video from the conference, which clarifies that this is a 3 billion parameter model with 2 bit quantization. The model is trained for both tool\-calling and structured output, which they call "guided generation" and describe as taking advantage of constrained decoding.

I'm also *very* excited about this:

> **Containerization Framework**
> 
> The Containerization framework enables developers to create, download, or run Linux container images directly on Mac. It’s built on an open\-source framework optimized for Apple silicon and provides secure isolation between container images.

I continue to seek the ideal sandboxing solution for running untrusted code \- both from other humans and written for me by LLMs \- on my own machines. This looks like it could be a really great option for that going forward.

It looks like [apple/container](https://github.com/apple/container) on GitHub is part of this new feature. From the [technical overview](https://github.com/apple/container/blob/main/docs/technical-overview.md):

> On macOS, the typical way to run Linux containers is to launch a Linux virtual machine (VM) that hosts all of your containers.
> 
> `container` runs containers differently. Using the open source [Containerization](https://github.com/apple/containerization)package, it runs a lightweight VM for each container that you create. \[...]
> 
> Since `container` consumes and produces standard OCI images, you can easily build with and run images produced by other container applications, and the images that you build will run everywhere.

---

**Link** 2025\-06\-10 [Magistral — the first reasoning model by Mistral AI](https://mistral.ai/news/magistral):

Mistral's first reasoning model is out today, in two sizes. There's a 24B Apache 2 licensed open\-weights model called Magistral Small (actually Magistral\-Small\-2506\), and a larger API\-only model called Magistral Medium.

Magistral Small is available as [mistralai/Magistral\-Small\-2506](https://huggingface.co/mistralai/Magistral-Small-2506) on Hugging Face. From that model card:

> **Context Window**: A 128k context window, but performance might degrade past 40k. Hence we recommend setting the maximum model length to 40k.

Mistral also released an official GGUF version, [Magistral\-Small\-2506\_gguf](https://huggingface.co/mistralai/Magistral-Small-2506_gguf), which I ran successfully using Ollama like this:

```
ollama pull hf.co/mistralai/Magistral-Small-2506_gguf:Q8_0
```

That fetched a 25GB file. I ran prompts using a chat session with [llm\-ollama](https://github.com/taketwo/llm-ollama) like this:

```
llm chat -m hf.co/mistralai/Magistral-Small-2506_gguf:Q8_0
```

Here's what I got for "Generate an SVG of a pelican riding a bicycle" ([transcript here](https://gist.github.com/simonw/7aaac8217f43be04886737d67c08ecca)):

[![Blue sky and what looks like an eagle flying towards the viewer.](https://substackcdn.com/image/fetch/$s_!QlU_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0b3c1292-589b-4859-9578-1eff057da921_800x600.jpeg "Blue sky and what looks like an eagle flying towards the viewer.")](https://substackcdn.com/image/fetch/$s_!QlU_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0b3c1292-589b-4859-9578-1eff057da921_800x600.jpeg)

It's disappointing that the GGUF doesn't support function calling yet \- hopefully a community variant can add that, it's one of the best ways I know of to unlock the potential of these reasoning models.

I just noticed that Ollama have their own [Magistral model](https://ollama.com/library/magistral) too, which can be accessed using:

```
ollama pull magistral:latest
```

That gets you a 14GB `q4_K_M` quantization \- other options can be found in the [full list of Ollama magistral tags](https://ollama.com/library/magistral/tags).

One thing that caught my eye in the Magistral announcement:

> Legal, finance, healthcare, and government professionals get traceable reasoning that meets compliance requirements. Every conclusion can be traced back through its logical steps, providing auditability for high\-stakes environments with domain\-specialized AI.

I guess this means the reasoning traces are fully visible and not redacted in any way \- interesting to see Mistral trying to turn that into a feature that's attractive to the business clients they are most interested in appealing to.

Also from that announcement:

> Our early tests indicated that Magistral is an excellent creative companion. We highly recommend it for creative writing and storytelling, with the model capable of producing coherent or — if needed — delightfully eccentric copy.

I haven't seen a reasoning model promoted for creative writing in this way before.

You can try out Magistral Medium by selecting the new "Thinking" option in Mistral's [Le Chat](https://chat.mistral.ai/).

[![Screenshot of a chat interface showing settings options. At the top is a text input field that says "Ask le Chat or @mention an agent" with a plus button, lightbulb "Think" button with up arrow, grid "Tools" button, and settings icon. Below are two toggle options: "Pure Thinking" with description "Best option for math + coding. Disables tools." (toggle is off), and "10x Speed" with lightning bolt icon and "PRO - 2 remaining today" label, described as "Same quality at 10x the speed." (toggle is on and green).](https://substackcdn.com/image/fetch/$s_!mdbN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff7ff436c-46b6-4b8e-a2d4-16e6e56387d6_1062x630.jpeg "Screenshot of a chat interface showing settings options. At the top is a text input field that says \"Ask le Chat or @mention an agent\" with a plus button, lightbulb \"Think\" button with up arrow, grid \"Tools\" button, and settings icon. Below are two toggle options: \"Pure Thinking\" with description \"Best option for math + coding. Disables tools.\" (toggle is off), and \"10x Speed\" with lightning bolt icon and \"PRO - 2 remaining today\" label, described as \"Same quality at 10x the speed.\" (toggle is on and green).")](https://substackcdn.com/image/fetch/$s_!mdbN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff7ff436c-46b6-4b8e-a2d4-16e6e56387d6_1062x630.jpeg)

They have options for "Pure Thinking" and a separate option for "10x speed", which runs Magistral Medium at 10x the speed using [Cerebras](https://www.cerebras.ai/).

The new models are also available through [the Mistral API](https://docs.mistral.ai/api/). You can access them by installing [llm\-mistral](https://github.com/simonw/llm-mistral) and running `llm mistral refresh` to refresh the list of available models, then:

```
llm -m mistral/magistral-medium-latest \
  'Generate an SVG of a pelican riding a bicycle'
```

[![Claude Sonnet 4 described this as Minimalist illustration of a white bird with an orange beak riding on a dark gray motorcycle against a light blue sky with a white sun and gray ground](https://substackcdn.com/image/fetch/$s_!cgvV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2a17a08c-e05b-403c-bcad-c015412c7ceb_800x600.jpeg "Claude Sonnet 4 described this as Minimalist illustration of a white bird with an orange beak riding on a dark gray motorcycle against a light blue sky with a white sun and gray ground")](https://substackcdn.com/image/fetch/$s_!cgvV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2a17a08c-e05b-403c-bcad-c015412c7ceb_800x600.jpeg)

Here's [that transcript](https://gist.github.com/simonw/93917661eae6e2fe0a0bd5685172fab8). At 13 input and 1,236 output tokens that cost me [0\.62 cents](https://www.llm-prices.com/#it=13&ot=1236&ic=2&oc=5) \- just over half a cent.

---

**Note** [2025\-06\-10](https://simonwillison.net/2025/Jun/10/o3-price-drop/)

OpenAI just dropped the price of their o3 model by 80% \- from $10/million input tokens and $40/million output tokens to just $2/million and $8/million for the very same model. This is in advance of the release of o3\-pro which apparently is coming [later today](https://twitter.com/OpenAI/status/1932483131363504334) (update: [here it is](https://simonwillison.net/2025/Jun/10/o3-pro/)).

This is a pretty huge shake\-up in LLM pricing. o3 is now priced the same as GPT 4\.1, and slightly less than GPT\-4o ($2\.50/$10\). It’s also less than Anthropic’s Claude Sonnet 4 ($3/$15\) and Opus 4 ($15/$75\) and sits in between Google’s Gemini 2\.5 Pro for \>200,00 tokens ($2\.50/$15\) and 2\.5 Pro for \<200,000 ($1\.25/$10\).

I’ve updated my [llm\-prices.com](https://www.llm-prices.com/) pricing calculator with the new rate.

How have they dropped the price so much? OpenAI's Adam Groth [credits ongoing optimization work](https://twitter.com/TheRealAdamG/status/1932440328293806321):

> thanks to the engineers optimizing inferencing.

---

**Link** 2025\-06\-10 [o3\-pro](https://platform.openai.com/docs/models/o3-pro):

OpenAI released o3\-pro today, which they describe as a "version of o3 with more compute for better responses".

It's only available via the newer Responses API. I've added it to my [llm\-openai\-plugin](https://github.com/simonw/llm-openai-plugin) plugin which uses that new API, so you can try it out like this:

```
llm install -U llm-openai-plugin
llm -m openai/o3-pro "Generate an SVG of a pelican riding a bicycle"
```

[![Description by o3-pro: The image is a playful, minimalist cartoon showing a white bird riding a bicycle. The bird has a simple oval body, a round head with a small black eye, and a yellow beak. Its orange feet are positioned on the bicycle’s pedals. The bicycle itself is drawn with thin black lines forming two large circular wheels and a straightforward frame. The scene has a light blue background with a soft gray oval shadow beneath the bicycle, giving the impression of ground. Overall, the illustration has a light, whimsical feel.](https://substackcdn.com/image/fetch/$s_!CgRC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe19884bb-d47c-41ca-a3a5-3ac24d2f45eb_800x640.jpeg "Description by o3-pro: The image is a playful, minimalist cartoon showing a white bird riding a bicycle. The bird has a simple oval body, a round head with a small black eye, and a yellow beak. Its orange feet are positioned on the bicycle’s pedals. The bicycle itself is drawn with thin black lines forming two large circular wheels and a straightforward frame. The scene has a light blue background with a soft gray oval shadow beneath the bicycle, giving the impression of ground. Overall, the illustration has a light, whimsical feel.")](https://substackcdn.com/image/fetch/$s_!CgRC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe19884bb-d47c-41ca-a3a5-3ac24d2f45eb_800x640.jpeg)

It's *slow* \- [generating this pelican](https://gist.github.com/simonw/6bc7dda9dbe07281d902d254e5fb6e33) took 124 seconds! OpenAI suggest using their [background mode](https://platform.openai.com/docs/guides/background) for o3 prompts, which I haven't tried myself yet.

o3\-pro is priced at $20/million input tokens and $80/million output tokens \- 10x the price of regular o3 after its [80% price drop](https://simonwillison.net/2025/Jun/10/o3-price-drop/) this morning.

Ben Hylak had early access and published his notes so far in [God is hungry for Context: First thoughts on o3 pro](https://www.latent.space/p/o3-pro). It sounds like this model needs to be applied very thoughtfully. It comparison to o3:

> It's smarter. *much smarter.*
> 
> **But in order to see that, you need to give it** ***a lot*** **more context. and I'm running out of context.** \[...]
> 
> My co\-founder Alexis and I took the the time to assemble a history of all of our past planning meetings at Raindrop, all of our goals, even record voice memos: and then asked o3\-pro to come up with a plan.
> 
> We were blown away; it spit out the exact kind of concrete plan and analysis I've always wanted an LLM to create \-\-\- complete with target metrics, timelines, what to prioritize, and strict instructions on what to absolutely cut.
> 
> The plan o3 gave us was plausible, reasonable; but the plan o3 Pro gave us was specific and rooted enough that ***it actually changed how we are thinking about our future.***
> 
> This is hard to capture in an eval.

It sounds to me like o3\-pro works best when combined with tools. I don't have tool support in `llm-openai-plugin` yet, [here's the relevant issue](https://github.com/simonw/llm-openai-plugin/issues/20).

---

**Link** 2025\-06\-10 [AI\-assisted coding for teams that can't get away with vibes](https://blog.nilenso.com/blog/2025/05/29/ai-assisted-coding/):

This excellent piece by Atharva Raykar offers a bunch of astute observations on AI\-assisted development that I haven't seen written down elsewhere.

> **Building with AI is fast**. The gains in velocity are important, because when harnessed correctly, it allows teams to tighten feedback loops with users faster and make better products.
> 
> Yet, AI tools are tricky to use. Hold it wrong, and you can generate underwhelming results, worse still, slow down your velocity by drowning your project in slop and technical debt.

Atharva notes that AI is a multiplier: the more expertise you have in software engineering, the better the results you can get from LLMs. Furthermore, *what helps the human helps the AI*.

This means food test coverage, automatic linting, continuous integration and deployment, good documentation practices and "clearly defined features, broken down into multiple small story cards".

If a team has all of this stuff in place, AI coding assistants will be able to operate more reliably and collaborate more effectively with their human overseers.

I enjoyed his closing thoughts about how heavier reliance on LLMs change our craft:

> Firstly, It’s less valuable to spend too much time looking for and building sophisticated abstractions. DRY is useful for ensuring patterns in the code don’t go out of sync, but there are costs to implementing and maintaining an abstraction to handle changing requirements. LLMs make some repetition palatable and allow you to wait a bit more and avoid premature abstraction.
> 
> Redoing work is now extremely cheap. Code in the small is less important than structural patterns and organisation of the code in the large. You can also build lots of prototypes to test an idea out. For this, vibe\-coding is great, as long as the prototype is thrown away and rewritten properly later. \[...]
> 
> Tests are non\-negotiable, and AI removes all excuses to not write them because of how fast they can belt them out. But always review the assertions!

---

**Quote** 2025\-06\-10

> *(People are often curious about how much energy a ChatGPT query uses; the average query uses about 0\.34 watt\-hours, about what an oven would use in a little over one second, or a high\-efficiency lightbulb would use in a couple of minutes. It also uses about 0\.000085 gallons of water; roughly one fifteenth of a teaspoon.)*

[Sam Altman](https://blog.samaltman.com/the-gentle-singularity)

---