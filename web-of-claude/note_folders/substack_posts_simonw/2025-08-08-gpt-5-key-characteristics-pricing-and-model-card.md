# GPT-5: Key characteristics, pricing and model card

*Plus OpenAI's open weight models and a bunch more stuff about ChatGPT*

Published: 2025-08-08
Source: https://simonw.substack.com/p/gpt-5-key-characteristics-pricing

---

In this newsletter:

* GPT\-5: Key characteristics, pricing and model card
* OpenAI's new open weight (Apache 2\) models are really good
* ChatGPT agent's user\-agent
* The ChatGPT sharing dialog demonstrates how difficult it is to design privacy preferences

Plus 11 links and 4 quotations and 1 note

### [GPT\-5: Key characteristics, pricing and model card](https://simonwillison.net/2025/Aug/7/gpt-5/) \- 2025\-08\-07

I've had preview access to the new GPT\-5 model family for the past two weeks (see [related video](https://simonwillison.net/2025/Aug/7/previewing-gpt-5/)) and have been using GPT\-5 as my daily\-driver. It's my new favorite model. It's still an LLM \- it's not a dramatic departure from what we've had before \- but it rarely screws up and generally feels competent or occasionally impressive at the kinds of things I like to use models for.

I've collected a lot of notes over the past two weeks, so I've decided to break them up into [a series of posts](https://simonwillison.net/series/gpt-5/). This first one will cover key characteristics of the models, how they are priced and what we can learn from the [GPT\-5 system card](https://openai.com/index/gpt-5-system-card/).

* [Key model characteristics](https://simonwillison.net/2025/Aug/7/gpt-5/#key-model-characteristics)
* [Position in the OpenAI model family](https://simonwillison.net/2025/Aug/7/gpt-5/#position-in-the-openai-model-family)
* [Pricing is aggressively competitive](https://simonwillison.net/2025/Aug/7/gpt-5/#pricing-is-aggressively-competitive)
* [More notes from the system card](https://simonwillison.net/2025/Aug/7/gpt-5/#more-notes-from-the-system-card)
* [Prompt injection in the system card](https://simonwillison.net/2025/Aug/7/gpt-5/#prompt-injection-in-the-system-card)
* [Thinking traces in the API](https://simonwillison.net/2025/Aug/7/gpt-5/#thinking-traces-in-the-api)
* [And some SVGs of pelicans](https://simonwillison.net/2025/Aug/7/gpt-5/#and-some-svgs-of-pelicans)

#### Key model characteristics

Let's start with the fundamentals. GPT\-5 in ChatGPT is a weird hybrid that switches between different models. Here's what the system card says about that (my highlights in bold):

> GPT\-5 is a unified system with a smart and fast model that answers most questions, a deeper reasoning model for harder problems, and **a real\-time router that quickly decides which model to use based on conversation type, complexity, tool needs, and explicit intent** (for example, if you say “think hard about this” in the prompt). \[...] Once usage limits are reached, a mini version of each model handles remaining queries. In the near future, we plan to integrate these capabilities into a single model.

GPT\-5 in the API is simpler: it's available as three models \- **regular**, **mini** and **nano** \- which can each be run at one of four reasoning levels: minimal (a new level not previously available for other OpenAI reasoning models), low, medium or high.

The models have an input limit of 272,000 tokens and an output limit (which includes invisible reasoning tokens) of 128,000 tokens. They support text and image for input, text only for output.

I've mainly explored full GPT\-5\. My verdict: it's just **good at stuff**. It doesn't feel like a dramatic leap ahead from other LLMs but it exudes competence \- it rarely messes up, and frequently impresses me. I've found it to be a very sensible default for everything that I want to do. At no point have I found myself wanting to re\-run a prompt against a different model to try and get a better result.

Here are the OpenAI model pages for [GPT\-5](https://platform.openai.com/docs/models/gpt-5), [GPT\-5 mini](https://platform.openai.com/docs/models/gpt-5-mini) and [GPT\-5 nano](https://platform.openai.com/docs/models/gpt-5-nano). Knowledge cut\-off is September 30th 2024 for GPT\-5 and May 30th 2024 for GPT\-5 mini and nano.

#### Position in the OpenAI model family

The three new GPT\-5 models are clearly intended as a replacement for most of the rest of the OpenAI line\-up. This table from the system card is useful, as it shows how they see the new models fitting in:

Previous model GPT\-5 model GPT\-4o gpt\-5\-main GPT\-4o\-mini gpt\-5\-main\-mini OpenAI o3 gpt\-5\-thinking OpenAI o4\-mini gpt\-5\-thinking\-mini GPT\-4\.1\-nano gpt\-5\-thinking\-nano OpenAI o3 Pro gpt\-5\-thinking\-pro

That "thinking\-pro" model is currently only available via ChatGPT where it is labelled as "GPT\-5 Pro" and limited to the $200/month tier. It uses "parallel test time compute".

The only capabilities not covered by GPT\-5 are audio input/output and image generation. Those remain covered by models like [GPT\-4o Audio](https://platform.openai.com/docs/models/gpt-4o-audio-preview) and [GPT\-4o Realtime](https://platform.openai.com/docs/models/gpt-4o-realtime-preview) and their mini variants and the [GPT Image 1](https://platform.openai.com/docs/models/gpt-image-1) and DALL\-E image generation models.

#### Pricing is aggressively competitive

The pricing is *aggressively competitive* with other providers.

* GPT\-5: $1\.25/million for input, $10/million for output
* GPT\-5 Mini: $0\.25/m input, $2\.00/m output
* GPT\-5 Nano: $0\.05/m input, $0\.40/m output

GPT\-5 is priced at half the input cost of GPT\-4o, and maintains the same price for output. Those invisible reasoning tokens count as output tokens so you can expect most prompts to use more output tokens than their GPT\-4o equivalent (unless you set reasoning effort to "minimal").

The discount for token caching is significant too: 90% off on input tokens that have been used within the previous few minutes. This is particularly material if you are implementing a chat UI where the same conversation gets replayed every time the user adds another prompt to the sequence.

Here's a comparison table I put together showing the new models alongside the most comparable models from OpenAI's competition:

Model Input $/m Output $/m Claude Opus 4\.1 15\.00 75\.00 Claude Sonnet 4 3\.00 15\.00 Grok 4 3\.00 15\.00 Gemini 2\.5 Pro (\>200,000\) 2\.50 15\.00 GPT\-4o 2\.50 10\.00 GPT\-4\.1 2\.00 8\.00 o3 2\.00 8\.00 Gemini 2\.5 Pro (\<200,000\) 1\.25 10\.00 **GPT\-5** 1\.25 10\.00 o4\-mini 1\.10 4\.40 Claude 3\.5 Haiku 0\.80 4\.00 GPT\-4\.1 mini 0\.40 1\.60 Gemini 2\.5 Flash 0\.30 2\.50 Grok 3 Mini 0\.30 0\.50 **GPT\-5 Mini** 0\.25 2\.00 GPT\-4o mini 0\.15 0\.60 Gemini 2\.5 Flash\-Lite 0\.10 0\.40 GPT\-4\.1 Nano 0\.10 0\.40 Amazon Nova Lite 0\.06 0\.24 **GPT\-5 Nano** 0\.05 0\.40 Amazon Nova Micro 0\.035 0\.14

(Here's a good example of a GPT\-5 failure: I tried to get it to [output that table sorted itself](https://chatgpt.com/share/6894d804-bca4-8006-ac46-580bf4a9bf5f) but it put Nova Micro as more expensive than GPT\-5 Nano, so I prompted it to "construct the table in Python and sort it there" and that fixed the issue.)

#### More notes from the system card

As usual, [the system card](https://observablehq.com/@simonw/blog-to-newsletter) is vague on what went into the training data. Here's what it says:

> Like OpenAI’s other models, the GPT\-5 models were trained on diverse datasets, including information that is publicly available on the internet, information that we partner with third parties to access, and information that our users or human trainers and researchers provide or generate. \[...] We use advanced data filtering processes to reduce personal information from training data.

I found this section interesting, as it reveals that writing, code and health are three of the most common use\-cases for ChatGPT. This explains why so much effort went into health\-related questions, for both GPT\-5 and the recently released OpenAI open weight models.

> We’ve made significant advances in **reducing hallucinations, improving instruction following, and minimizing sycophancy**, and have leveled up GPT\-5’s performance in **three of ChatGPT’s most common uses: writing, coding, and health**. All of the GPT\-5 models additionally feature **safe\-completions, our latest approach to safety training** to prevent disallowed content.

Safe\-completions is later described like this:

> Large language models such as those powering ChatGPT have **traditionally been trained to either be as helpful as possible or outright refuse a user request**, depending on whether the prompt is allowed by safety policy. \[...] Binary refusal boundaries are especially ill\-suited for dual\-use cases (such as biology or cybersecurity), where a user request can be completed safely at a high level, but may lead to malicious uplift if sufficiently detailed or actionable. **As an alternative, we introduced safe\- completions: a safety\-training approach that centers on the safety of the assistant’s output rather than a binary classification of the user’s intent**. Safe\-completions seek to maximize helpfulness subject to the safety policy’s constraints.

So instead of straight up refusals, we should expect GPT\-5 to still provide an answer but moderate that answer to avoid it including "harmful" content.

OpenAI have a paper about this which I haven't read yet (I didn't get early access): [From Hard Refusals to Safe\-Completions: Toward Output\-Centric Safety Training](https://openai.com/index/gpt-5-safe-completions/).

Sycophancy gets a mention, unsurprising given [their high profile disaster in April](https://simonwillison.net/2025/May/2/what-we-missed-with-sycophancy/). They've worked on this in the core model:

> System prompts, while easy to modify, have a more limited impact on model outputs relative to changes in post\-training. For GPT\-5, we post\-trained our models to reduce sycophancy. Using conversations representative of production data, we evaluated model responses, then assigned a score reflecting the level of sycophancy, which was used as a reward signal in training.

They claim impressive reductions in hallucinations. In my own usage I've not spotted a single hallucination yet, but that's been true for me for Claude 4 and o3 recently as well \- hallucination is so much less of a problem with this year's models.

***Update**: I have had some reasonable pushback against this point, so I should clarify what I mean here. When I use the term "hallucination" I am talking about instances where the model confidently states a real\-world fact that is untrue \- like the incorrect winner of a sporting event. I'm not talking about the models making other kinds of mistakes \- they make mistakes all the time!*

*Someone [pointed out](https://news.ycombinator.com/item?id=44829896) that it's likely I'm avoiding hallucinations through the way I use the models, and this is entirely correct: as an experienced LLM user I instinctively stay clear of prompts that are likely to trigger hallucinations, like asking a non\-search\-enabled model for URLs or paper citations. This means I'm much less likely to encounter hallucinations in my daily usage.*

> One of our focuses when training the GPT\-5 models was to reduce the frequency of factual hallucinations. While ChatGPT has browsing enabled by default, many API queries do not use browsing tools. Thus, we focused both on training our models to browse effectively for up\-to\-date information, and on reducing hallucinations when the models are relying on their own internal knowledge.

The section about deception also incorporates the thing where models sometimes pretend they've completed a task that defeated them:

> We placed gpt\-5\-thinking in a variety of tasks that were partly or entirely infeasible to accomplish, and **rewarded the model for honestly admitting it can not complete the task**. \[...]
> 
> In tasks where the agent is required to use tools, such as a web browsing tool, in order to answer a user’s query, previous models would hallucinate information when the tool was unreliable. We simulate this scenario by purposefully disabling the tools or by making them return error codes.

#### Prompt injection in the system card

There's a section about prompt injection, but it's pretty weak sauce in my opinion.

> Two external red\-teaming groups conducted a two\-week prompt\-injection assessment targeting system\-level vulnerabilities across ChatGPT’s connectors and mitigations, rather than model\-only behavior.

Here's their chart showing how well the model scores against the rest of the field. It's an impressive result in comparison \- 56\.8 attack success rate for gpt\-5\-thinking, where Claude 3\.7 scores in the 60s (no Claude 4 results included here) and everything else is 70% plus:

[![A bar chart titled "Behavior Attack Success Rate at k Queries" shows attack success rates (in %) for various AI models at k=1 (dark red) and k=10 (light red). For each model, the total height of the stacked bar represents the k=10 success rate (labeled above each bar), while the lower dark red section represents the k=1 success rate (estimated). From left to right: Llama 3.3 70B – k=10: 92.2%, k=1: ~47%; Llama 3.1 405B – k=10: 90.9%, k=1: ~38%; Gemini Flash 1.5 – k=10: 87.7%, k=1: ~34%; GPT-4o – k=10: 86.4%, k=1: ~28%; OpenAI o3-mini-high – k=10: 86.4%, k=1: ~41%; Gemini Pro 1.5 – k=10: 85.5%, k=1: ~34%; Gemini 2.5 Pro Preview – k=10: 85.0%, k=1: ~28%; Gemini 2.0 Flash – k=10: 85.0%, k=1: ~33%; OpenAI o3-mini – k=10: 84.5%, k=1: ~40%; Grok 2 – k=10: 82.7%, k=1: ~34%; GPT-4.5 – k=10: 80.5%, k=1: ~28%; 3.5 Haiku – k=10: 76.4%, k=1: ~17%; Command-R – k=10: 76.4%, k=1: ~28%; OpenAI o4-mini – k=10: 75.5%, k=1: ~17%; 3.5 Sonnet – k=10: 75.0%, k=1: ~13%; OpenAI o1 – k=10: 71.8%, k=1: ~18%; 3.7 Sonnet – k=10: 64.5%, k=1: ~17%; 3.7 Sonnet: Thinking – k=10: 63.6%, k=1: ~17%; OpenAI o3 – k=10: 62.7%, k=1: ~13%; gpt-5-thinking – k=10: 56.8%, k=1: ~6%. Legend shows dark red = k=1 and light red = k=10.](https://substackcdn.com/image/fetch/$s_!r9Sf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6360495c-fdd4-408f-a2db-8d15f5714c9e_1642x746.jpeg "A bar chart titled \"Behavior Attack Success Rate at k Queries\" shows attack success rates (in %) for various AI models at k=1 (dark red) and k=10 (light red). For each model, the total height of the stacked bar represents the k=10 success rate (labeled above each bar), while the lower dark red section represents the k=1 success rate (estimated). From left to right: Llama 3.3 70B – k=10: 92.2%, k=1: ~47%; Llama 3.1 405B – k=10: 90.9%, k=1: ~38%; Gemini Flash 1.5 – k=10: 87.7%, k=1: ~34%; GPT-4o – k=10: 86.4%, k=1: ~28%; OpenAI o3-mini-high – k=10: 86.4%, k=1: ~41%; Gemini Pro 1.5 – k=10: 85.5%, k=1: ~34%; Gemini 2.5 Pro Preview – k=10: 85.0%, k=1: ~28%; Gemini 2.0 Flash – k=10: 85.0%, k=1: ~33%; OpenAI o3-mini – k=10: 84.5%, k=1: ~40%; Grok 2 – k=10: 82.7%, k=1: ~34%; GPT-4.5 – k=10: 80.5%, k=1: ~28%; 3.5 Haiku – k=10: 76.4%, k=1: ~17%; Command-R – k=10: 76.4%, k=1: ~28%; OpenAI o4-mini – k=10: 75.5%, k=1: ~17%; 3.5 Sonnet – k=10: 75.0%, k=1: ~13%; OpenAI o1 – k=10: 71.8%, k=1: ~18%; 3.7 Sonnet – k=10: 64.5%, k=1: ~17%; 3.7 Sonnet: Thinking – k=10: 63.6%, k=1: ~17%; OpenAI o3 – k=10: 62.7%, k=1: ~13%; gpt-5-thinking – k=10: 56.8%, k=1: ~6%. Legend shows dark red = k=1 and light red = k=10.")](https://substackcdn.com/image/fetch/$s_!r9Sf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6360495c-fdd4-408f-a2db-8d15f5714c9e_1642x746.jpeg)

On the one hand, a 56\.8% attack rate is cleanly a big improvement against all of those other models.

But it's also a strong signal that prompt injection continues to be an unsolved problem! That means that more than half of those k\=10 attacks (where the attacker was able to try up to ten times) got through.

Don't assume prompt injection isn't going to be a problem for your application just because the models got better.

#### Thinking traces in the API

I had initially thought that my biggest disappointment with GPT\-5 was that there's no way to get at those thinking traces via the API... but that turned out [not to be true](https://bsky.app/profile/sophiebits.com/post/3lvtceih7222r). The following `curl` command demonstrates that the responses API `"reasoning": {"summary": "auto"}` is available for the new GPT\-5 models:

```
curl https://api.openai.com/v1/responses \
  -H "Authorization: Bearer $(llm keys get openai)" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5",
    "input": "Give me a one-sentence fun fact about octopuses.",
    "reasoning": {"summary": "auto"}
  }'
```

Here's [the response](https://gist.github.com/simonw/1d1013ba059af76461153722005a039d) from that API call.

Without that option the API will often provide a lengthy delay while the model burns through thinking tokens until you start getting back visible tokens for the final response.

OpenAI offer a new `reasoning_effort=minimal` option which turns off most reasoning so that tokens start to stream back to you as quickly as possible.

#### And some SVGs of pelicans

Naturally I've been running [my "Generate an SVG of a pelican riding a bicycle" benchmark](https://simonwillison.net/tags/pelican-riding-a-bicycle/). I'll actually spend more time on this in a future post \- I have some fun variants I've been exploring \- but for the moment here's [the pelican](https://gist.github.com/simonw/c98873ef29e621c0fe2e0d4023534406) I got from GPT\-5 running at its default "medium" reasoning effort:

[![The bicycle is really good, spokes on wheels, correct shape frame, nice pedals. The pelican has a pelican beak and long legs stretching to the pedals.](https://substackcdn.com/image/fetch/$s_!0Q9l!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1418cff1-5f2d-4893-bd34-d941a38e91d7_800x600.png "The bicycle is really good, spokes on wheels, correct shape frame, nice pedals. The pelican has a pelican beak and long legs stretching to the pedals.")](https://substackcdn.com/image/fetch/$s_!0Q9l!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1418cff1-5f2d-4893-bd34-d941a38e91d7_800x600.png)

It's pretty great! Definitely recognizable as a pelican, and one of the best bicycles I've seen yet.

Here's [GPT\-5 mini](https://gist.github.com/simonw/9b5ecf61a5fb0794729aa0023aaa504d):

[![Blue background with clouds. Pelican has two necks for some reason. Has a good beak though. More gradents and shadows than the GPT-5 one.](https://substackcdn.com/image/fetch/$s_!Lf7U!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F78d0345a-bfd2-4e9b-be90-8a4dd2e23377_800x600.png "Blue background with clouds. Pelican has two necks for some reason. Has a good beak though. More gradents and shadows than the GPT-5 one.")](https://substackcdn.com/image/fetch/$s_!Lf7U!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F78d0345a-bfd2-4e9b-be90-8a4dd2e23377_800x600.png)

And [GPT\-5 nano](https://gist.github.com/simonw/3884dc8b186b630956a1fb0179e191bc):

[![Bicycle is two circles and some randomish black lines. Pelican still has an OK beak but is otherwise very simple.](https://substackcdn.com/image/fetch/$s_!b_h-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd1fb06c5-0f4f-4903-8a90-a907654008a2_800x480.png "Bicycle is two circles and some randomish black lines. Pelican still has an OK beak but is otherwise very simple.")](https://substackcdn.com/image/fetch/$s_!b_h-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd1fb06c5-0f4f-4903-8a90-a907654008a2_800x480.png)

---

### [OpenAI's new open weight (Apache 2\) models are really good](https://simonwillison.net/2025/Aug/5/gpt-oss/) \- 2025\-08\-05

The long promised [OpenAI open weight models are here](https://openai.com/index/introducing-gpt-oss/), and they are *very* impressive. They're available under proper open source licenses \- Apache 2\.0 \- and come in two sizes, 120B and 20B.

OpenAI's own benchmarks are eyebrow\-raising \- emphasis mine:

> The **gpt\-oss\-120b** model achieves **near\-parity with OpenAI o4\-mini** on core reasoning benchmarks, while running efficiently on a single 80 GB GPU. The **gpt\-oss\-20b** model delivers **similar results to OpenAI o3‑mini** on common benchmarks and can run on edge devices with just 16 GB of memory, making it ideal for on\-device use cases, local inference, or rapid iteration without costly infrastructure.

o4\-mini and o3\-mini are *really good* proprietary models \- I was not expecting the open weights releases to be anywhere near that class, especially given their small sizes. That gpt\-oss\-20b model should run quite comfortably on a Mac laptop with 32GB of RAM.

Both models are mixture\-of\-experts:

> gpt\-oss\-120b activates 5\.1B parameters per token, while gpt\-oss\-20b activates 3\.6B. The models have 117b and 21b total parameters respectively.

Something that surprised me even more about the benchmarks was the scores for general knowledge based challenges. I can just about believe they managed to train a strong reasoning model that fits in 20B parameters, but these models score highly on benchmarks like "GPQA Diamond (without tools) PhD\-level science questions" too:

* o3 — 83\.3%
* o4\-mini — 81\.4%
* gpt\-oss\-120b — 80\.1%
* o3\-mini — 77%
* gpt\-oss\-20b — 71\.5%

A lot of these benchmarks are edging towards saturated.

* [Running gpt\-oss\-20b on my Mac with LM Studio](https://simonwillison.net/2025/Aug/5/gpt-oss/#running-gpt-oss-20b-on-my-mac-with-lm-studio)
* [Pelican on reasoning\=low](https://simonwillison.net/2025/Aug/5/gpt-oss/#pelican-on-reasoning-low)
* [Pelican on reasoning\=medium](https://simonwillison.net/2025/Aug/5/gpt-oss/#pelican-on-reasoning-medium)
* [Pelican on reasoning\=high](https://simonwillison.net/2025/Aug/5/gpt-oss/#pelican-on-reasoning-high)
* [Space invaders with gpt\-oss\-20b](https://simonwillison.net/2025/Aug/5/gpt-oss/#space-invaders-with-gpt-oss-20b)
* [Trying gpt\-oss\-120b via API providers](https://simonwillison.net/2025/Aug/5/gpt-oss/#trying-gpt-oss-120b-via-api-providers)
* [llama.cpp is coming very shortly](https://simonwillison.net/2025/Aug/5/gpt-oss/#llama-cpp-is-coming-very-shortly)
* [gpt\-oss:20b in Ollama](https://simonwillison.net/2025/Aug/5/gpt-oss/#gpt-oss-20b-in-ollama)
* [Training details from the model card](https://simonwillison.net/2025/Aug/5/gpt-oss/#the-model-card)
* [OpenAI Harmony, a new format for prompt templates](https://simonwillison.net/2025/Aug/5/gpt-oss/#openai-harmony-a-new-format-for-prompt-templates)
* [The open question for me: how good is tool calling?](https://simonwillison.net/2025/Aug/5/gpt-oss/#the-open-question-for-me-how-good-is-tool-calling-)
* [Competing with the Chinese open models](https://simonwillison.net/2025/Aug/5/gpt-oss/#china)

#### Running gpt\-oss\-20b on my Mac with LM Studio

There are already a bunch of different ways to run these models \- OpenAI partnered with numerous organizations in advance of the release.

I decided to start with [LM Studio](https://lmstudio.ai/).

I had to update to the most recent version of the app, then install the new model from [their openai/gpt\-oss\-20b](https://lmstudio.ai/models/openai/gpt-oss-20b) page.

First impressions: this is a *really good* model, and it somehow runs using just 11\.72GB of my system RAM.

The model supports three reasoning efforts: low, medium and high. LM Studio makes those available via a dropdown.

Let's try "Generate an SVG of a pelican riding a bicycle":

#### Pelican on reasoning\=low

I started [with low](https://gist.github.com/simonw/b71394cc85fe0f048e376392e41586da). It thought for 0\.07 seconds and then output this (at 39 tokens a second):

[![](https://substackcdn.com/image/fetch/$s_!1VHm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa2890df9-d72d-4b18-a982-17a26bf0601b_800x533.png)](https://substackcdn.com/image/fetch/$s_!1VHm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa2890df9-d72d-4b18-a982-17a26bf0601b_800x533.png)

Except... it output invalid SVG. One of the path elements looked like this:

```
<!-- Frame -->
<path d="
    M150,250          <!-- rear wheel center -->
    L300,120          <!-- top tube to front -->
    L450,250          <!-- chain stays back to front -->
    L300,350          <!-- seat stays down -->
    Z"
    fill="#e0e0e0" stroke="#555" stroke-width="4"/>

```

But you can't put comments inside attributes like that. I fixed this to get the above image.

#### Pelican on reasoning\=medium

I tried again [on medium](https://gist.github.com/simonw/642e9e371387fc59a5aad25dcd41b0cc). This time it thought for 4\.44 seconds and gave me this, at 55 tokens/second:

[![](https://substackcdn.com/image/fetch/$s_!Mz0q!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff356e349-e68c-4efc-b9fa-6e921a3d3e48_800x414.png)](https://substackcdn.com/image/fetch/$s_!Mz0q!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff356e349-e68c-4efc-b9fa-6e921a3d3e48_800x414.png)

#### Pelican on reasoning\=high

And then [on high](https://gist.github.com/simonw/164a3f1b4b1a971637af279a0ac49be3). My first attempt here failed because it hit the default LM Studio 4096 context limit \- so I reloaded the model and set the new limit to the maximum possible.

It jumped up to using 17\.35GB RAM (I imagine it might use a lot more with a longer prompt) and after thinking for 5 minutes and 50 seconds (!) gave me this:

[![](https://substackcdn.com/image/fetch/$s_!Xvc6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc64ad313-b2f4-4e48-8d42-a7509ef4b9e2_800x533.png)](https://substackcdn.com/image/fetch/$s_!Xvc6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc64ad313-b2f4-4e48-8d42-a7509ef4b9e2_800x533.png)

It thought *really hard* to get there. Here's a snippet of [that transcript](https://gist.github.com/simonw/164a3f1b4b1a971637af279a0ac49be3):

> But maybe we want seat below body bottom? Actually seat should be between body and pedals, not above body bottom. Wait, typical bicycle: seat post goes from bottom bracket upward to the seat. The seat sits on top of the seat tube (vertical). So the seat is above bottom bracket. In our representation, the seat is at y\=250\-255\. Body center at 245, body bottom at 265\. So body bottom is below seat. That means the pelican's body is below the seat? Actually no: body bottom extends to 265; seat top is at 250; so seat sits above body bottom by about 15 units. That seems plausible because seat should be slightly above body, but body bottom is at 265 \> seat top 255\. \[...]

I've seen this from other local reasoning models too: they can really overthink this kind of problem! I don't know if there's any pelican SVG that's worth waiting nearly six minutes for.

#### Space invaders with gpt\-oss\-20b

Given how long high took I switched back to medium for my next experiment:

> `Write an HTML and JavaScript page implementing space invaders`

It [thought for 10\.78 seconds](https://gist.github.com/simonw/63d7d8c43ae2ac93c214325bd6d607e4) and produced this:

You can [play that here](https://tools.simonwillison.net/space-invaders-gpt-oss-20b-mxfp4-medium).

It's not the best I've seen \- I was more impressed [by GLM 4\.5 Air](https://simonwillison.net/2025/Jul/29/space-invaders/) \- but it's very competent for a model that only uses 12GB of my RAM (GLM 4\.5 Air used 47GB).

#### Trying gpt\-oss\-120b via API providers

I don't quite have the resources on my laptop to run the larger model. Thankfully it's already being hosted by a number of different API providers.

OpenRouter already [lists three](https://openrouter.ai/openai/gpt-oss-120b/providers) \- Fireworks, Groq and Cerebras. (Update: now also Parasail and Baseten.)

Cerebras is *fast*, so I decided to try them first.

I installed the [llm\-cerebras](https://github.com/irthomasthomas/llm-cerebras) plugin and ran the `refresh` command to ensure it had their latest models:

```
llm install -U llm-cerebras jsonschema
llm cerebras refresh
```

(Installing jsonschema worked around a warning message.)

Output:

```
Refreshed 10 Cerebras models:
  - cerebras-deepseek-r1-distill-llama-70b
  - cerebras-gpt-oss-120b
  - cerebras-llama-3.3-70b
  - cerebras-llama-4-maverick-17b-128e-instruct
  - cerebras-llama-4-scout-17b-16e-instruct
  - cerebras-llama3.1-8b
  - cerebras-qwen-3-235b-a22b-instruct-2507
  - cerebras-qwen-3-235b-a22b-thinking-2507
  - cerebras-qwen-3-32b
  - cerebras-qwen-3-coder-480b
```

Now:

```
llm -m cerebras-gpt-oss-120b \
  'Generate an SVG of a pelican riding a bicycle'
```

Cerebras runs the new model at between 2 and 4 thousands tokens per second!

To my surprise this one [had the same comments\-in\-attributes bug](https://gist.github.com/simonw/4c685f19f1a93b68eacb627125e36be4) that we saw with oss\-20b earlier. I fixed those and got this pelican:

[![Yellow and not great pelican, quite a good bicycle if a bit sketchy.](https://substackcdn.com/image/fetch/$s_!4N-e!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb0b93e9-5e56-47ce-877a-0e29009707d3_800x480.jpeg "Yellow and not great pelican, quite a good bicycle if a bit sketchy.")](https://substackcdn.com/image/fetch/$s_!4N-e!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb0b93e9-5e56-47ce-877a-0e29009707d3_800x480.jpeg)

That bug appears intermittently \- I've not seen it on some of my other runs of the same prompt.

The [llm\-openrouter](https://github.com/simonw/llm-openrouter) plugin also provides access to the models, balanced across the underlying providers. You can use that like so:

```
llm install llm-openrouter
llm keys set openrouter
# Paste API key here
llm -m openrouter/openai/gpt-oss-120b "Say hi"
```

#### llama.cpp is coming very shortly

The `llama.cpp` [pull request for gpt\-oss](https://github.com/ggml-org/llama.cpp/pull/15091) was landed less than an hour ago. It's worth browsing through the coded \- a *lot* of work went into supporting this new model, spanning 48 commits to 83 different files. Hopefully this will land in the [llama.cpp Homebrew package](https://formulae.brew.sh/formula/llama.cpp) within the next day or so, which should provide a convenient way to run the model via `llama-server` and friends.

#### gpt\-oss:20b in Ollama

Ollama [also have gpt\-oss](https://ollama.com/library/gpt-oss), requiring an update to their app.

I fetched that 14GB model like this:

```
ollama pull gpt-oss:20b
```

Now I can use it with the new Ollama native app, or access it from [LLM](https://llm.datasette.io/) like this:

```
llm install llm-ollama
llm -m gpt-oss:20b 'Hi'
```

This also appears to use around 13\.26GB of system memory while running a prompt.

Ollama also launched [Ollama Turbo](https://ollama.com/turbo) today, offering the two OpenAI models as a paid hosted service:

> Turbo is a new way to run open models using datacenter\-grade hardware. Many new models are too large to fit on widely available GPUs, or run very slowly. Ollama Turbo provides a way to run these models fast while using Ollama's App, CLI, and API.

#### Training details from the model card

Here are some interesting notes about how the models were trained from [the model card](https://cdn.openai.com/pdf/419b6906-9da6-406c-a19d-1bb078ac7637/oai_gpt-oss_model_card.pdf) (PDF):

> **Data**: We train the models on a text\-only dataset with trillions of tokens, with a focus on STEM, coding, and general knowledge. To improve the safety of the model, we filtered the data for harmful content in pre\-training, especially around hazardous biosecurity knowledge, by reusing the CBRN pre\-training filters from GPT\-4o. Our model has a knowledge cutoff of June 2024\.
> 
> **Training**: The gpt\-oss models trained on NVIDIA H100 GPUs using the PyTorch framework with expert\-optimized Triton kernels. The training run for gpt\-oss\-120b required 2\.1 million H100\-hours to complete, with gpt\-oss\-20b needing almost 10x fewer. \[...]

Thunder Compute's article [NVIDIA H100 Pricing (August 2025\): Cheapest On\-Demand Cloud GPU Rates](https://www.thundercompute.com/blog/nvidia-h100-pricing) lists prices from around $2/hour to $11/hour, which would indicate a training cost of the 120b model between $4\.2m and $23\.1m and the 20b between $420,000 and $2\.3m.

> After pre\-training, we post\-train the models using similar CoT RL techniques as OpenAI o3\. This procedure teaches the models how to reason and solve problems using CoT and teaches the model how to use tools. Because of the similar RL techniques, these models have a personality similar to models served in our first\-party products like ChatGPT. Our training dataset consists of a wide range of problems from coding, math, science, and more.

The models have additional special training to help them use web browser and Python (Jupyter notebook) tools more effectively:

> During post\-training, we also teach the models to use different agentic tools:
> 
> * A browsing tool, that allows the model to call search and open functions to interact with the web. This aids factuality and allows the models to fetch info beyond their knowledge cutoff.
> * A python tool, which allows the model to run code in a stateful Jupyter notebook environment.
> * Arbitrary developer functions, where one can specify function schemas in a `Developer` message similar to the OpenAI API. The definition of function is done within our harmony format.

There's a corresponding [section about Python tool usage](https://github.com/openai/gpt-oss?tab=readme-ov-file#python) in the `openai/gpt-oss` repository README.

#### OpenAI Harmony, a new format for prompt templates

One of the gnarliest parts of implementing harnesses for LLMs is handling the prompt template format.

Modern prompts are complicated beasts. They need to model user v.s. assistant conversation turns, and tool calls, and reasoning traces and an increasing number of other complex patterns.

[openai/harmony](https://github.com/openai/harmony) is a brand new open source project from OpenAI (again, Apache 2\) which implements a new response format that was created for the `gpt-oss` models. It's clearly inspired by their new\-ish [Responses API](https://openai.com/index/new-tools-for-building-agents/).

The format is described in the new [OpenAI Harmony Response Format](https://cookbook.openai.com/articles/openai-harmony) cookbook document. It introduces some concepts that I've not seen in open weight models before:

* `system`, `developer`, `user`, `assistant` and `tool` roles \- many other models only use user and assistant, and sometimes system and tool.
* Three different channels for output: `final`, `analysis` and `commentary`. Only the `final` channel is default intended to be visible to users. `analysis` is for chain of thought and `commentary` is sometimes used for tools.

That channels concept has been present in ChatGPT for a few months, starting with the release of o3\.

The details of the new tokens used by Harmony caught my eye:

Token Purpose ID \<\|start\|\> Start of message header 200006 \<\|end\|\> End of message 200007 \<\|message\|\> Start of message content 200008 \<\|channel\|\> Start of channel info 200005 \<\|constrain\|\> Data type for tool call 200003 \<\|return\|\> Stop after response 200002 \<\|call\|\> Call a tool 200012

Those token IDs are particularly important. They are part of a new token vocabulary called `o200k_harmony`, which landed in OpenAI's tiktoken tokenizer library [this morning](https://github.com/openai/tiktoken/commit/3591ff175d6a80efbe4fcc7f0e219ddd4b8c52f1).

In the past I've seen models get confused by special tokens \- try pasting `<|end|>` into a model and see what happens.

Having these special instruction tokens formally map to dedicated token IDs should hopefully be a whole lot more robust!

The Harmony repo itself includes a Rust library and a Python library (wrapping that Rust library) for working with the new format in a much more ergonomic way.

I tried one of their demos using `uv run` to turn it into a shell one\-liner:

```
uv run --python 3.12 --with openai-harmony python -c '
from openai_harmony import *
from openai_harmony import DeveloperContent
enc = load_harmony_encoding(HarmonyEncodingName.HARMONY_GPT_OSS)
convo = Conversation.from_messages([
    Message.from_role_and_content(
        Role.SYSTEM,
        SystemContent.new(),
    ),
    Message.from_role_and_content(
        Role.DEVELOPER,
        DeveloperContent.new().with_instructions("Talk like a pirate!")
    ),
    Message.from_role_and_content(Role.USER, "Arrr, how be you?"),
])
tokens = enc.render_conversation_for_completion(convo, Role.ASSISTANT)
print(tokens)'
```

Which outputs:

> `[200006, 17360, 200008, 3575, 553, 17554, 162016, 11, 261, 4410, 6439, 2359, 22203, 656, 7788, 17527, 558, 87447, 100594, 25, 220, 1323, 19, 12, 3218, 279, 30377, 289, 25, 14093, 279, 2, 13888, 18403, 25, 8450, 11, 49159, 11, 1721, 13, 21030, 2804, 413, 7360, 395, 1753, 3176, 13, 200007, 200006, 77944, 200008, 2, 68406, 279, 37992, 1299, 261, 96063, 0, 200007, 200006, 1428, 200008, 8977, 81, 11, 1495, 413, 481, 30, 200007, 200006, 173781]`

Note those token IDs like `200006` corresponding to the special tokens listed above.

#### The open question for me: how good is tool calling?

There's one aspect of these models that I haven't explored in detail yet: **tool calling**. How these work is clearly a big part of the new Harmony format, but the packages I'm using myself (around my own [LLM tool calling](https://simonwillison.net/2025/May/27/llm-tools/) support) need various tweaks and fixes to start working with that new mechanism.

Tool calling currently represents my biggest disappointment with local models that I've run on my own machine. I've been able to get them to perform simple single calls, but the state of the art these days is wildly more ambitious than that.

Systems like Claude Code can make dozens if not hundreds of tool calls over the course of a single session, each one adding more context and information to a single conversation with an underlying model.

My experience to date has been that local models are unable to handle these lengthy conversations. I'm not sure if that's inherent to the limitations of my own machine, or if it's something that the right model architecture and training could overcome.

OpenAI make big claims about the tool calling capabilities of these new models. I'm looking forward to seeing how well they perform in practice.

#### Competing with the Chinese open models

I've been writing a *lot* about the [flurry of excellent open weight models](https://simonwillison.net/tags/ai-in-china/) released by Chinese AI labs over the past few months \- all of them very capable and most of them under Apache 2 or MIT licenses.

Just last week [I said](https://simonwillison.net/2025/Jul/30/chinese-models/):

> Something that has become undeniable this month is that the best available open weight models now come from the Chinese AI labs.
> 
> I continue to have a lot of love for Mistral, Gemma and Llama but my feeling is that Qwen, Moonshot and Z.ai have positively smoked them over the course of July. \[...]
> 
> I can't help but wonder if part of the reason for the delay in release of OpenAI's open weights model comes from a desire to be notably better than this truly impressive lineup of Chinese models.

With the release of the gpt\-oss models that statement no longer holds true. I'm waiting for the dust to settle and the independent benchmarks (that are more credible than my ridiculous pelicans) to roll out, but I think it's likely that OpenAI now offer the best available open weights models.

**Update**: Independent evaluations are beginning to roll in. Here's [Artificial Analysis](https://x.com/artificialanlys/status/1952887733803991070):

> gpt\-oss\-120b is the most intelligent American open weights model, comes behind DeepSeek R1 and Qwen3 235B in intelligence but offers efficiency benefits \[...]
> 
> While the larger gpt\-oss\-120b does not come in above DeepSeek R1 0528’s score of 59 or Qwen3 235B 2507s score of 64, it is notable that it is significantly smaller in both total and active parameters than both of those models.

---

### [ChatGPT agent's user\-agent](https://simonwillison.net/2025/Aug/4/chatgpt-agents-user-agent/) \- 2025\-08\-04

I was exploring how ChatGPT agent works today. I learned some interesting things about how it exposes its identity through HTTP headers, then made a huge blunder in thinking it was leaking its URLs to Bingbot and Yandex... but it turned out [that was a Cloudflare feature](https://simonwillison.net/2025/Aug/4/chatgpt-agents-agent/#cloudflare-crawler-hints) that had nothing to do with ChatGPT.

ChatGPT agent is the [recently released](https://openai.com/index/introducing-chatgpt-agent/) (and confusingly named) ChatGPT feature that provides browser automation combined with terminal access as a feature of ChatGPT \- replacing their previous [Operator research preview](https://help.openai.com/en/articles/10421097-operator) which is scheduled for deprecation on August 31st.

#### Investigating ChatGPT agent's user\-agent

I decided to dig into how it works by creating a logged web URL endpoint using [django\-http\-debug](https://simonwillison.net/2024/Aug/8/django-http-debug/). Then I told ChatGPT agent mode to explore that new page:

[![ChatGPT screenshot. My prompt was "Visit https://simonwillison.net/test-url-context and tell me what you see there" - it said "Worked for 15 seconds" with an arrow, then a screnshot of the webpage content showing "simonwillison.net" with a favicon, heading "This is a heading", text "Text and text and more text." and "this came from javascript". The bot then responds with: The webpage displays a simple layout with a large heading at the top that reads “This is a heading.” Below it, there's a short paragraph that says “Text and text and more text.” A final line appears underneath saying “this came from javascript,” indicating that this last line was inserted via a script. The page contains no interactive elements or instructions—just these lines of plain text displayed on a white background.](https://substackcdn.com/image/fetch/$s_!p8cK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb1916041-ed7e-4b96-97d4-575d5146b472_1460x1296.jpeg "ChatGPT screenshot. My prompt was \"Visit https://simonwillison.net/test-url-context and tell me what you see there\" - it said \"Worked for 15 seconds\" with an arrow, then a screnshot of the webpage content showing \"simonwillison.net\" with a favicon, heading \"This is a heading\", text \"Text and text and more text.\" and \"this came from javascript\". The bot then responds with: The webpage displays a simple layout with a large heading at the top that reads “This is a heading.” Below it, there's a short paragraph that says “Text and text and more text.” A final line appears underneath saying “this came from javascript,” indicating that this last line was inserted via a script. The page contains no interactive elements or instructions—just these lines of plain text displayed on a white background.")](https://substackcdn.com/image/fetch/$s_!p8cK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb1916041-ed7e-4b96-97d4-575d5146b472_1460x1296.jpeg)

My logging captured these request headers:

```
Via: 1.1 heroku-router
Host: simonwillison.net
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Cf-Ray: 96a0f289adcb8e8e-SEA
Cookie: cf_clearance=zzV8W...
Server: Heroku
Cdn-Loop: cloudflare; loops=1
Priority: u=0, i
Sec-Ch-Ua: "Not)A;Brand";v="8", "Chromium";v="138"
Signature: sig1=:1AxfqHocTf693inKKMQ7NRoHoWAZ9d/vY4D/FO0+MqdFBy0HEH3ZIRv1c3hyiTrzCvquqDC8eYl1ojcPYOSpCQ==:
Cf-Visitor: {"scheme":"https"}
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36
Cf-Ipcountry: US
X-Request-Id: 45ef5be4-ead3-99d5-f018-13c4a55864d3
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Accept-Encoding: gzip, br
Accept-Language: en-US,en;q=0.9
Signature-Agent: "https://chatgpt.com"
Signature-Input: sig1=("@authority" "@method" "@path" "signature-agent");created=1754340838;keyid="otMqcjr17mGyruktGvJU8oojQTSMHlVm7uO-lrcqbdg";expires=1754344438;nonce="_8jbGwfLcgt_vUeiZQdWvfyIeh9FmlthEXElL-O2Rq5zydBYWivw4R3sV9PV-zGwZ2OEGr3T2Pmeo2NzmboMeQ";tag="web-bot-auth";alg="ed25519"
X-Forwarded-For: 2a09:bac5:665f:1541::21e:154, 172.71.147.183
X-Request-Start: 1754340840059
Cf-Connecting-Ip: 2a09:bac5:665f:1541::21e:154
Sec-Ch-Ua-Mobile: ?0
X-Forwarded-Port: 80
X-Forwarded-Proto: http
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1

```

That **Mozilla/5\.0 (Macintosh; Intel Mac OS X 10\_15\_7\) AppleWebKit/537\.36 (KHTML, like Gecko) Chrome/138\.0\.0\.0 Safari/537\.36** user\-agent header is the one used by the most recent Chrome on macOS \- which is a little odd here as the **Sec\-Ch\-Ua\-Platform : "Linux"** indicates that the agent browser runs on Linux.

At first glance it looks like ChatGPT is being dishonest here by not including its bot identity in the user\-agent header. I thought for a moment it might be reflecting my own user\-agent, but I'm using Firefox on macOS and it identified itself as Chrome.

Then I spotted this header:

```
Signature-Agent: "https://chatgpt.com"
```

Which is accompanied by a much more complex header called **Signature\-Input**:

```
Signature-Input: sig1=("@authority" "@method" "@path" "signature-agent");created=1754340838;keyid="otMqcjr17mGyruktGvJU8oojQTSMHlVm7uO-lrcqbdg";expires=1754344438;nonce="_8jbGwfLcgt_vUeiZQdWvfyIeh9FmlthEXElL-O2Rq5zydBYWivw4R3sV9PV-zGwZ2OEGr3T2Pmeo2NzmboMeQ";tag="web-bot-auth";alg="ed25519"
```

And a `Signature` header too.

These turn out to come from a relatively new web standard: [RFC 9421 HTTP Message Signatures](https://www.rfc-editor.org/rfc/rfc9421.html)' published February 2024\.

The purpose of HTTP Message Signatures is to allow clients to include signed data about their request in a way that cannot be tampered with by intermediaries. The signature uses a public key that's provided by the following well\-known endpoint:

```
https://chatgpt.com/.well-known/http-message-signatures-directory
```

Add it all together and we now have a rock\-solid way to identify traffic from ChatGPT agent: look for the `Signature-Agent: "https://chatgpt.com"` header and confirm its value by checking the signature in the `Signature-Input` and `Signature` headers.

#### And then came Bingbot and Yandex

Just over a minute after it captured that request, my logging endpoint got another request:

```
Via: 1.1 heroku-router
From: bingbot(at)microsoft.com
Host: simonwillison.net
Accept: */*
Cf-Ray: 96a0f4671d1fc3c6-SEA
Server: Heroku
Cdn-Loop: cloudflare; loops=1
Cf-Visitor: {"scheme":"https"}
User-Agent: Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm) Chrome/116.0.1938.76 Safari/537.36
Cf-Ipcountry: US
X-Request-Id: 6214f5dc-a4ea-5390-1beb-f2d26eac5d01
Accept-Encoding: gzip, br
X-Forwarded-For: 207.46.13.9, 172.71.150.252
X-Request-Start: 1754340916429
Cf-Connecting-Ip: 207.46.13.9
X-Forwarded-Port: 80
X-Forwarded-Proto: http
```

I pasted `207.46.13.9` into Microsoft's [Verify Bingbot](https://www.bing.com/toolbox/verify-bingbot-verdict) tool (after solving a particularly taxing CAPTCHA) and it confirmed that this was indeed a request from Bingbot.

I set up a second URL to confirm... and this time got a visit from Yandex!

```
Via: 1.1 heroku-router
From: support@search.yandex.ru
Host: simonwillison.net
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Cf-Ray: 96a16390d8f6f3a7-DME
Server: Heroku
Cdn-Loop: cloudflare; loops=1
Cf-Visitor: {"scheme":"https"}
User-Agent: Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)
Cf-Ipcountry: RU
X-Request-Id: 3cdcbdba-f629-0d29-b453-61644da43c6c
Accept-Encoding: gzip, br
X-Forwarded-For: 213.180.203.138, 172.71.184.65
X-Request-Start: 1754345469921
Cf-Connecting-Ip: 213.180.203.138
X-Forwarded-Port: 80
X-Forwarded-Proto: http
```

Yandex [suggest a reverse DNS lookup](https://yandex.com/support/webmaster/en/robot-workings/check-yandex-robots.html?lang=en) to verify, so I ran this command:

```
dig -x 213.180.203.138 +short
```

And got back:

```
213-180-203-138.spider.yandex.com.
```

Which confirms that this is indeed a Yandex crawler.

I tried a third experiment to be sure... and got hits from both Bingbot and YandexBot.

#### It was Cloudflare Crawler Hints, not ChatGPT

So I wrote up and posted about my discovery... and [Jatan Loya asked:](https://x.com/jatan_loya/status/1952506398270767499)

> do you have crawler hints enabled in cf?

And yeah, it turned out I did. I spotted this in my caching configuration page (and it looks like I must have turned it on myself at some point in the past):

[![Screenshot of Cloudflare settings panel showing "Crawler Hints Beta" with description text explaining that Crawler Hints provide high quality data to search engines and other crawlers when sites using Cloudflare change their content. This allows crawlers to precisely time crawling, avoid wasteful crawls, and generally reduce resource consumption on origins and other Internet infrastructure. Below states "By enabling this service, you agree to share website information required for feature functionality and agree to the Supplemental Terms for Crawler Hints." There is a toggle switch in the on position on the right side and a "Help" link in the bottom right corner.](https://substackcdn.com/image/fetch/$s_!fGZO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F394ba651-ec57-43ff-8ae1-303c039f36dc_1434x810.jpeg "Screenshot of Cloudflare settings panel showing \"Crawler Hints Beta\" with description text explaining that Crawler Hints provide high quality data to search engines and other crawlers when sites using Cloudflare change their content. This allows crawlers to precisely time crawling, avoid wasteful crawls, and generally reduce resource consumption on origins and other Internet infrastructure. Below states \"By enabling this service, you agree to share website information required for feature functionality and agree to the Supplemental Terms for Crawler Hints.\" There is a toggle switch in the on position on the right side and a \"Help\" link in the bottom right corner.")](https://substackcdn.com/image/fetch/$s_!fGZO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F394ba651-ec57-43ff-8ae1-303c039f36dc_1434x810.jpeg)

Here's [the Cloudflare documentation for that feature](https://developers.cloudflare.com/cache/advanced-configuration/crawler-hints/).

I deleted my posts on Twitter and Bluesky (since you can't edit those and I didn't want the misinformation to continue to spread) and edited [my post on Mastodon](https://fedi.simonwillison.net/@simon/114972968822349077), then updated this entry with the real reason this had happened.

I also changed the URL of this entry as it turned out Twitter and Bluesky were caching my social media preview for the previous one, which included the incorrect information in the title.

---

### [The ChatGPT sharing dialog demonstrates how difficult it is to design privacy preferences](https://simonwillison.net/2025/Aug/3/privacy-design/) \- 2025\-08\-03

ChatGPT just removed their "make this chat discoverable" sharing feature, after it turned out a material volume of users had inadvertantly made their private chats available via Google search.

Dane Stuckey, CISO for OpenAI, [on Twitter](https://x.com/cryps1s/status/1951041845938499669):

> We just removed a feature from @ChatGPTapp that allowed users to make their conversations discoverable by search engines, such as Google. This was a short\-lived experiment to help people discover useful conversations. \[...]
> 
> Ultimately we think this feature introduced too many opportunities for folks to accidentally share things they didn't intend to, so we're removing the option.

There's been some media coverage of this issue \- here are examples from [TechCrunch](https://techcrunch.com/2025/07/31/your-public-chatgpt-queries-are-getting-indexed-by-google-and-other-search-engines/), [TechRadar](https://www.techradar.com/ai-platforms-assistants/chatgpt/openai-pulls-chat-sharing-tool-after-google-search-privacy-scare), and [PCMag](https://www.pcmag.com/news/be-careful-what-you-tell-chatgpt-your-chats-could-show-up-on-google-search).

It turned out users had shared extremely private conversations and made them discoverable by search engines, which meant that various `site:chatgpt.com ...` searches were turning up all sorts of potentially embarrassing details.

Here's what that UI looked like before they removed the option:

[![Screenshot of a chat sharing dialog with title "Public link created" and X close button. Text reads "A public link to your chat has been created. Manage previously shared chats at any time via Settings." Below is an unchecked checkbox labeled "Make this chat discoverable" with subtitle "Allows it to be shown in web searches". The sharing URL shown is "https://chatgpt.com/share/688b95ef-f986" with a black "Copy link" button. At bottom are three social sharing icons for LinkedIn, Reddit, and X.](https://substackcdn.com/image/fetch/$s_!QpD1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F33a88d80-61fb-48be-9ccd-c839c83a6084_1164x784.jpeg "Screenshot of a chat sharing dialog with title \"Public link created\" and X close button. Text reads \"A public link to your chat has been created. Manage previously shared chats at any time via Settings.\" Below is an unchecked checkbox labeled \"Make this chat discoverable\" with subtitle \"Allows it to be shown in web searches\". The sharing URL shown is \"https://chatgpt.com/share/688b95ef-f986\" with a black \"Copy link\" button. At bottom are three social sharing icons for LinkedIn, Reddit, and X.")](https://substackcdn.com/image/fetch/$s_!QpD1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F33a88d80-61fb-48be-9ccd-c839c83a6084_1164x784.jpeg)

I've seen a bunch of commentary, both on Twitter and [this Hacker News thread](https://news.ycombinator.com/item?id=44778764), from people who are baffled that anyone could be confused by such a clear option in the UI.

I think that confusion is warranted. Let's break it down.

Here's the microcopy in question:

> **Make this chat discoverable**  
> Allows it to be shown in web searches.

The first problem here is the choice of terminology. "Discoverable" is not a widely understood term \- it's insider jargon. "Allows it to be shown in web searches" is better, but still requires a surprisng depth of understanding from users before they can make an informed decision.

Here's everything a user would need to understand for this to make sense to them:

* What a URL is, and how it's posssible to create a URL that is semi\-public in that it's unguessable by others but can still be read by anyone you share it with. That concept is a pretty tall order just on its own!
* What a web search engine is \- that in this case it's intended as a generic term for Google, Bing, DuckDuckGo etc.
* That "web search" here means "those public search engines other people can use" and not something like "the private search feature you use on this website".
* A loose understanding of how search engines work: that they have indexes, and those indexes can selectively include or exclude content.
* That sites like ChatGPT get to control whether or not their content is included in those indexes.
* That the nature of a "secret URL" is that, once shared and made discoverable, anyone with that link (or who finds it through search) can now view the full content of that page.

ChatGPT has over a billion users now. That means there is a giant range of levels of technical expertise among those users. We can't assume that everyone understands the above concepts necessary to understand the implications of checking that box.

And even if they have the pre\-requisite knowledge required to understand this, **users don't read**.

When people are using an application they are always looking for the absolute shortest path to achieving their goal. Any dialog box or question that appears is something to be skipped over as quickly as possible.

Sadly, a lot of users may have learned to just say "yes" to any question. This option about making something "discoverable"? Sure, whatever, click the box and keep on going.

I think there's another factor at play here too: the option itself makes almost no sense.

How many people looking for a way to share their chats are going to think "and you know what? Stick this in Google too"?

It's such a tiny fraction of the audience that a logical conclusion, when faced with the above option, could well be that obviously it wouldn't put my chats in Google because who on Earth would ever want that to happen?

I think OpenAI made the right call disabling this feature. The value it can provide for the tiny set of people who decide to use it is massively outweighed by the potential for less discerning users to cause themselves harm by inadvertently sharing their private conversations with the world.

#### Meta AI does this even worse

A much worse example of this anti\-pattern is Meta AI's decision to provide a "Post to feed" button in their own Meta AI chat app:

[![Sharing dialog has two options: Post to feed - share this conversation to the public feed so anyone can see it and engage. and Share a link: Create a link to share this conversation with specific people.](https://substackcdn.com/image/fetch/$s_!Enhb!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1ce3e1c3-69ee-4a3d-a56c-0c9073d42c7f_1320x806.jpeg "Sharing dialog has two options: Post to feed - share this conversation to the public feed so anyone can see it and engage. and Share a link: Create a link to share this conversation with specific people.")](https://substackcdn.com/image/fetch/$s_!Enhb!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1ce3e1c3-69ee-4a3d-a56c-0c9073d42c7f_1320x806.jpeg)

I think their microcopy here is *top notch* \- the text here uses clear language and should be easy for anyone to understand.

(I took this screenshot today though, so it's possible the text has been recently updated.)

And yet... Futurism, June 14th: [People Don't Realize Meta's AI App Is Publicly Blasting Their Humiliating Secrets to the World](https://futurism.com/meta-ai-embarassing).

Once again, when your users number in the millions some of them are going to randomly click things without understanding the consequences.

The Meta AI iPhone app (fun fact: it can talk to you in the voice of Dame Judi Dench or John Cena) shows that public feed on the homepage when you first open the app, presumably to try and help people get over the blank slate "what is this thing even for" problem. They do not appear keen on losing this feature!

---

**Link** 2025\-08\-02 [Re\-label the "Save" button to be "Publish", to better indicate to users the outcomes of their action](https://phabricator.wikimedia.org/T131132):

Fascinating Wikipedia usability improvement issue from 2016:

> From feedback we get repeatedly as a development team from interviews, user testing and other solicited and unsolicited avenues, and by inspection from the number of edits by newbies not quite aware of the impact of their edits in terms of immediate broadcast and irrevocability, that new users don't necessarily understand what "Save" on the edit page means. \[...]
> 
> Even though "user\-generated content" sites are a lot more common today than they were when Wikipedia was founded, it is still unusual for most people that their actions will result in immediate, and effectively irrevocable, publication.

A great illustration of the usability impact of micro\-copy, even more important when operating at Wikipedia scale.

---

**Link** 2025\-08\-03 [From Async/Await to Virtual Threads](https://lucumr.pocoo.org/2025/7/26/virtual-threads/):

Armin Ronacher has long been critical of async/await in Python, both for necessitating [colored functions](https://journal.stuffwithstuff.com/2015/02/01/what-color-is-your-function/) and because of the more subtle challenges they introduce like [managing back pressure](https://lucumr.pocoo.org/2020/1/1/async-pressure/).

Armin [argued convincingly](https://lucumr.pocoo.org/2024/11/18/threads-beat-async-await/) for the threaded programming model back in December. Now he's expanded upon that with a description of how virtual threads might make sense in Python.

Virtual threads behave like real system threads but can vastly outnumber them, since they can be paused and scheduled to run on a real thread when needed. Go uses this trick to implement goroutines which can then support millions of virtual threads on a single system.

Python core developer Mark Shannon [started a conversation](https://discuss.python.org/t/add-virtual-threads-to-python/91403) about the potential for seeing virtual threads to Python back in May.

Assuming this proposal turns into something concrete I don't expect we will see it in a production Python release for a few more years. In the meantime there are some exciting improvements to the Python concurrency story \- most notably [around sub\-interpreters](https://docs.python.org/3.14/whatsnew/3.14.html#whatsnew314-pep734) \- coming up this year in Python 3\.14\.

---

**Link** 2025\-08\-03 [XBai o4](https://huggingface.co/MetaStoneTec/XBai-o4):

Yet *another* open source (Apache 2\.0\) LLM from a Chinese AI lab. This model card claims:

> **XBai o4** excels in complex reasoning capabilities and has now completely surpassed OpenAI\-o3\-mini in Medium mode.

This a 32\.8 billion parameter model released by MetaStone AI, a new\-to\-me lab who released their first model in March \- [MetaStone\-L1\-7B](https://huggingface.co/MetaStoneTec/MetaStone-L1-7B), then followed that with MetaStone\-S1 [1\.5B](https://huggingface.co/MetaStoneTec/MetaStone-S1-1.5B), [7B](https://huggingface.co/MetaStoneTec/MetaStone-S1-7B) and [32B](https://huggingface.co/MetaStoneTec/MetaStone-S1-32B) in July and now XBai o4 in August.

The MetaStone\-S1 models were accompanied with a with a paper, [Test\-Time Scaling with Reflective Generative Model](https://arxiv.org/abs/2507.01951).

There is *very* little information available on the English\-language web about MetaStone AI. Their paper shows a relationship with USTC, [University of Science and Technology of China](https://en.wikipedia.org/wiki/University_of_Science_and_Technology_of_China) in Hefei. One of their researchers [confirmed on Twitter](https://x.com/WangMagic_/status/1951690465222217872) that their CEO is from [KWAI](https://en.wikipedia.org/wiki/Kuaishou) which lead me to [this Chinese language article](https://www.qbitai.com/2024/07/168071.html) from July last year about Li Yan, formerly of KWAI and now the founder of Wen Xiaobai and [evidently](https://x.com/simonw/status/1951694450369208361) [now](https://x.com/WangMagic_/status/1951694611191324929) the CEO of MetaStone. [www.wenxiaobai.com](https://www.wenxiaobai.com) is listed as the "official website" linked to from [the XBai\-o4 README](https://github.com/MetaStone-AI/XBai-o4) on GitHub.

Ivan Fioravanti [got it working under MLX](https://huggingface.co/mlx-community/models?search=xbai-o4) in 4bit, 5bit, 6bit, 8bit and 4bit\-DWQ sizes. I tried his [6bit one](https://huggingface.co/mlx-community/XBai-o4-6bit) (a 24\.81GB download) in LM Studio and had it "Generate an SVG of a pelican riding a bicycle". It thought for 39\.49 seconds ([thinking trace here](https://gist.github.com/simonw/78182fc3409e36f8d22217992967b9d6#response)) and gave me this:

[![The pelican is blue and looks a little like a sad elephant. The bicycle looks more like a flat motorbike. The pelican has a blue tail and orange legs.](https://substackcdn.com/image/fetch/$s_!714X!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1e64b826-13db-4cc8-853f-b7721e98b01a_800x600.png "The pelican is blue and looks a little like a sad elephant. The bicycle looks more like a flat motorbike. The pelican has a blue tail and orange legs.")](https://substackcdn.com/image/fetch/$s_!714X!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1e64b826-13db-4cc8-853f-b7721e98b01a_800x600.png)

I also had it "Write an HTML and JavaScript page implementing space invaders", which you can [try out here](https://tools.simonwillison.net/space-invaders-xbai-o4-6bit-mlx). It's not great \- the invaders don't fire bullets (it listed that as a "potential improvement") and I don't think it's winnable due to timing issues, but it's an interesting addition to [my collection](https://simonwillison.net/tags/space-invaders/).

LM Studio reported a constant memory usage of 25\.54GB and according to Activity Monitor used 87\.5% of my GPU and around 39% of a CPU core.

It did a *lot* of work in the thinking trace \- which took 10m35s! \- including writing the first draft of much of the code that ended up in the finished result. Here's an extract:

> Let me think of variables:
> 
> `let enemyDirection = 1; // 1 for right, -1 for left`
> 
> In the game loop:
> 
> 
> ```
> enemies.forEach(enemy => {>
>     enemy.x += enemyDirection * enemy.dx;>
> });
> ```
> Then check if any enemy is out of bounds. If so, reverse direction and move all enemies down.
> 
> But how to check if any enemy is at the edge?
> 
> Maybe find the max x of all enemies and see if it exceeds `canvas.width - enemy.width`.
> 
> Alternatively, track the leftmost and rightmost positions of enemies. Maybe a bit complex.
> 
> For simplicity, perhaps check if any enemy's `x + width > canvas.width or x < 0`.

Here's [the full transcript](https://gist.github.com/simonw/457d55a5c426e0bbea9d47aee225c391).

My initial impressions are that I'm not as impressed with this model for running on my own laptop as I was with [Qwen3\-Coder\-30B\-A3B\-Instruct](https://simonwillison.net/2025/Jul/31/qwen3-coder-flash/) or [GLM\-4\.5 Air](https://simonwillison.net/2025/Jul/29/space-invaders/).

But... how extraordinary is it that *another* Chinese AI lab has been able to produce a competitive model, this time with far less fanfare than we've seen from Qwen and Moonshot AI and Z.ai.

---

**quote** 2025\-08\-04

> *This week, ChatGPT is on track to reach 700M weekly active users — up from 500M at the end of March and 4× since last year.*

[Nick Turley](https://x.com/nickaturley/status/1952385556664520875), Head of ChatGPT, OpenAI

---

**Link** 2025\-08\-04 [I Saved a PNG Image To A Bird](https://www.youtube.com/watch?v=hCQCP-5g5bo):

Benn Jordan provides one of the all time great YouTube video titles, and it's justified. He drew an image in an audio spectrogram, played that sound to a talented starling (internet celebrity ["The Mouth"](https://www.tiktok.com/@farijuana_bird/video/7452882774991572254)) and recorded the result that the starling almost perfectly imitated back to him.

> Hypothetically, if this were an audible file transfer protocol that used a 10:1 data compression ratio, that's nearly 2 megabytes of information per second. While there are a lot of caveats and limitations there, the fact that you could set up a speaker in your yard and conceivably store any amount of data in songbirds is crazy.

This video is full of so much more than just that. Fast forward to [5m58s](https://www.youtube.com/watch?v=hCQCP-5g5bo&t=358s) for footage of a nest full of brown pelicans showing the sounds made by their chicks!

---

**quote** 2025\-08\-04

> *for services that wrap GPT\-3, is it possible to do the equivalent of sql injection? like, a prompt\-injection attack? make it think it's completed the task and then get access to the generation, and ask it to repeat the original instruction?*

[@himbodhisattva](https://x.com/himbodhisattva/status/1525182881726730240), coining the term prompt injection on 13th May 2022, four months before [I did](https://simonwillison.net/2022/Sep/12/prompt-injection/)

---

**Link** 2025\-08\-04 [Qwen\-Image: Crafting with Native Text Rendering](https://qwenlm.github.io/blog/qwen-image/):

Not content with releasing [six excellent open weights LLMs in July](https://simonwillison.net/2025/Jul/30/chinese-models/), Qwen are kicking off August with their first ever image generation model.

Qwen\-Image is a 20 billion parameter MMDiT (Multimodal Diffusion Transformer, originally proposed for Stable Diffusion 3\) model under an Apache 2\.0 license. The [Hugging Face repo](https://huggingface.co/Qwen/Qwen-Image) is 53\.97GB.

Qwen released a [detailed technical report](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/Qwen_Image.pdf) (PDF) to accompany the model. The model builds on their Qwen\-2\.5\-VL vision LLM, and they also made extensive use of that model to help create some of their their training data:

> In our data annotation pipeline, we utilize a capable image captioner (e.g., Qwen2\.5\-VL) to generate not only comprehensive image descriptions, but also structured metadata that captures essential image properties and quality attributes.
> 
> Instead of treating captioning and metadata extraction as independent tasks, we designed an annotation framework in which the captioner concurrently describes visual content and generates detailed information in a structured format, such as JSON. Critical details such as object attributes, spatial relationships, environmental context, and verbatim transcriptions of visible text are captured in the caption, while key image properties like type, style, presence of watermarks, and abnormal elements (e.g., QR codes or facial mosaics) are reported in a structured format.

They put a *lot* of effort into the model's ability to render text in a useful way. 5% of the training data (described as "billions of image\-text pairs") was data "synthesized through controlled text rendering techniques", ranging from simple text through text on an image background up to much more complex layout examples:

> To improve the model’s capacity to follow complex, structured prompts involving layout\-sensitive content, we propose a synthesis strategy based on programmatic editing of pre\-defined templates, such as PowerPoint slides or User Interface Mockups. A comprehensive rule\-based system is designed to automate the substitution of placeholder text while maintaining the integrity of layout structure, alignment, and formatting.

I tried the model out using the [ModelScope demo](https://modelscope.cn/aigc/imageGeneration?tab=advanced) \- I signed in with GitHub and verified my account via a text message to a phone number. Here's what I got for "A raccoon holding a sign that says "I love trash" that was written by that raccoon":

[![A great photo of a raccoon holding a cardboard sign, the text I love trash is written on it in marker, the raccoon has chosen to draw the o in love as a heart filled with red marker pen.](https://substackcdn.com/image/fetch/$s_!iVx6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F55fd3be5-4367-4753-a55c-8dab8d2c585f_1140x1482.jpeg "A great photo of a raccoon holding a cardboard sign, the text I love trash is written on it in marker, the raccoon has chosen to draw the o in love as a heart filled with red marker pen.")](https://substackcdn.com/image/fetch/$s_!iVx6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F55fd3be5-4367-4753-a55c-8dab8d2c585f_1140x1482.jpeg)

The raccoon has very neat handwriting!

**Update**: A version of the model exists that can edit existing images but it's [not yet been released](https://github.com/QwenLM/Qwen-Image/issues/3#issuecomment-3151573614):

> Currently, we have only open\-sourced the text\-to\-image foundation model, but the editing model is also on our roadmap and planned for future release.

---

**Link** 2025\-08\-04 [Usage charts for my LLM tool against OpenRouter](https://openrouter.ai/apps?url=https%3A%2F%2Fllm.datasette.io%2F):

OpenRouter proxies requests to a large number of different LLMs and provides high level statistics of which models are the most popular among their users.

Tools that call OpenRouter can include `HTTP-Referer` and `X-Title` headers to credit that tool with the token usage. My [llm\-openrouter](https://github.com/simonw/llm-openrouter/) plugin [does that here](https://github.com/simonw/llm-openrouter/blob/8e4be78e60337154b063faaa7161dddd91462730/llm_openrouter.py#L99C13-L99C20).

... which means [this page](https://openrouter.ai/apps?url=https%3A%2F%2Fllm.datasette.io%2F) displays aggregate stats across users of that plugin! Looks like someone has been running a lot of traffic through [Qwen 3 14B](https://openrouter.ai/qwen/qwen3-14b) recently.

[![Screenshot of LLM usage statistics dashboard showing a stacked bar chart from July 5 to August 4, 2025, with a legend on the right displaying "Top models" including Qwen: Qwen3 14B (480M), Google: Gemini 2.5 Flash Lite Preview 06-17 (31.7M), Horizon Beta (3.77M), Google: Gemini 2.5 Flash Lite (1.67M), google/gemini-2.0-flash-exp (1.14M), DeepSeek: DeepSeek V3 0324 (1.11M), Meta: Llama 3.3 70B Instruct (228K), Others (220K), Qwen: Qwen3 Coder (218K), MoonshotAI: Kimi K2 (132K), and Horizon Alpha (75K), with a total of 520M usage shown for August 3, 2025.](https://substackcdn.com/image/fetch/$s_!CrOx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9b167109-4988-469f-b53c-125cb643d231_1820x970.jpeg "Screenshot of LLM usage statistics dashboard showing a stacked bar chart from July 5 to August 4, 2025, with a legend on the right displaying \"Top models\" including Qwen: Qwen3 14B (480M), Google: Gemini 2.5 Flash Lite Preview 06-17 (31.7M), Horizon Beta (3.77M), Google: Gemini 2.5 Flash Lite (1.67M), google/gemini-2.0-flash-exp (1.14M), DeepSeek: DeepSeek V3 0324 (1.11M), Meta: Llama 3.3 70B Instruct (228K), Others (220K), Qwen: Qwen3 Coder (218K), MoonshotAI: Kimi K2 (132K), and Horizon Alpha (75K), with a total of 520M usage shown for August 3, 2025.")](https://substackcdn.com/image/fetch/$s_!CrOx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9b167109-4988-469f-b53c-125cb643d231_1820x970.jpeg)

---

**Link** 2025\-08\-05 [A Friendly Introduction to SVG](https://www.joshwcomeau.com/svg/friendly-introduction-to-svg/):

This SVG tutorial by Josh Comeau is fantastic. It's filled with neat interactive illustrations \- with a pleasing subtly "click" audio effect as you adjust their sliders \- and provides a useful introduction to a bunch of well chosen SVG fundamentals.

I finally understand what all four numbers in the `viewport="..."` attribute are for!

---

**quote** 2025\-08\-05

> *I teach HS Science in the south. I can only speak for my district, but a few teacher work days in the wave of enthusiasm I'm seeing for AI tools is overwhelming. We're getting district approved ads for AI tools by email, Admin and ICs are pushing it on us, and at least half of the teaching staff seems all in at this point.   
>   
> I was just in a meeting with my team and one of the older teachers brought out a powerpoint for our first lesson and almost everyone agreed to use it after a quick scan \- but it was missing important tested material, repetitive, and just totally airy and meaningless. Just slide after slide of the same handful of sentences rephrased with random loosely related stock photos. When I asked him if it was AI generated, he said 'of course', like it was a strange question. \[...]   
>   
> We don't have a leg to stand on to teach them anything about originality, academic integrity/intellectual honesty, or the importance of doing things for themselves when they catch us indulging in it just to save time at work.*

[greyduet on r/teachers](https://www.reddit.com/r/Teachers/comments/1mhntjh/unpopular_opinion_teacher_ai_use_is_already_out/), Unpopular Opinion: Teacher AI use is already out of control and it's not ok

---

**Link** 2025\-08\-05 [Claude Opus 4\.1](https://www.anthropic.com/news/claude-opus-4-1):

Surprise new model from Anthropic today \- Claude Opus 4\.1, which they describe as "a drop\-in replacement for Opus 4".

My favorite thing about this model is the version number \- treating this as a .1 version increment looks like it's an accurate depiction of the model's capabilities.

Anthropic's own benchmarks show very small incremental gains.

Comparing Opus 4 and Opus 4\.1 (I [got 4\.1 to extract this information from a screenshot](https://claude.ai/share/c7366629-784a-4088-9fc4-15613aa41a7f) of Anthropic's own benchmark scores, then asked it to look up the links, then verified the links myself and fixed a few):

* **Agentic coding** ([SWE\-bench Verified](https://github.com/SWE-bench/SWE-bench)): From 72\.5% to 74\.5%
* **Agentic terminal coding** ([Terminal\-Bench](https://github.com/laude-institute/terminal-bench)): From 39\.2% to 43\.3%
* **Graduate\-level reasoning** ([GPQA Diamond](https://github.com/idavidrein/gpqa)): From 79\.6% to 80\.9%
* **Agentic tool use** ([TAU\-bench](https://github.com/sierra-research/tau-bench)):

	+ Retail: From 81\.4% to 82\.4%
	+ **Airline: From 59\.6% to 56\.0%** *(decreased)*
* **Multilingual Q\&A** ([MMMLU](https://huggingface.co/datasets/openai/MMMLU)): From 88\.8% to 89\.5%
* **Visual reasoning** ([MMMU validation](https://mmmu-benchmark.github.io/)): From 76\.5% to 77\.1%
* **High school math competition** ([AIME 2025](https://artofproblemsolving.com/wiki/index.php/AIME_Problems_and_Solutions)): From 75\.5% to 78\.0%

Likewise, the [model card](https://assets.anthropic.com/m/4c024b86c698d3d4/original/Claude-4-1-System-Card.pdf) shows only tiny changes to the various safety metrics that Anthropic track.

It's priced the same as Opus 4 \- $15/million for input and $75/million for output, making it one of [the most expensive models](https://www.llm-prices.com/#sb=input&sd=descending) on the market today.

I had it [draw me this pelican](https://gist.github.com/simonw/7fead138d31d751d65c7253a1c18751b) riding a bicycle:

[![Pelican is line art, does have a good beak and feet on the pedals, bicycle is very poorly designed and not the right shape.](https://substackcdn.com/image/fetch/$s_!6z8Z!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2ebc07e0-3ed1-4061-9511-a7e596d10680_800x600.png "Pelican is line art, does have a good beak and feet on the pedals, bicycle is very poorly designed and not the right shape.")](https://substackcdn.com/image/fetch/$s_!6z8Z!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2ebc07e0-3ed1-4061-9511-a7e596d10680_800x600.png)

For comparison I got a fresh new pelican [out of Opus 4](https://gist.github.com/simonw/96a958e39aaed10e1e47c1aab2d05e20) which I actually like a little more:

[![This one has shaded colors for the different parts of the pelican. Still a bad bicycle.](https://substackcdn.com/image/fetch/$s_!5me4!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F44b08d55-6c0b-4ed9-968a-96a6dcf403e1_800x600.png "This one has shaded colors for the different parts of the pelican. Still a bad bicycle.")](https://substackcdn.com/image/fetch/$s_!5me4!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F44b08d55-6c0b-4ed9-968a-96a6dcf403e1_800x600.png)

I shipped [llm\-anthropic 0\.18](https://github.com/simonw/llm-anthropic/releases/tag/0.18) with support for the new model.

---

**Link** 2025\-08\-06 [No, AI is not Making Engineers 10x as Productive](https://colton.dev/blog/curing-your-ai-10x-engineer-imposter-syndrome/):

Colton Voege on "curing your AI 10x engineer imposter syndrome".

There's a lot of rhetoric out there suggesting that if you can't 10x your productivity through tricks like running a dozen Claude Code instances at once you're falling behind. Colton's piece here is a pretty thoughtful exploration of why that likely isn't true. I found myself agreeing with quite a lot of this article.

I'm a pretty huge proponent for AI\-assisted development, but I've never found those 10x claims convincing. I've estimated that LLMs make me 2\-5x more productive on the parts of my job which involve typing code into a computer, which is itself a small portion of that I do as a software engineer.

That's not too far from this article's assumptions. From the article:

> I wouldn't be surprised to learn AI helps many engineers do certain tasks 20\-50% faster, but the nature of software bottlenecks mean this doesn't translate to a 20% productivity increase and certainly not a 10x increase.

I think that's an under\-estimation \- I suspect engineers that really know how to use this stuff effectively will get more than a 0\.2x increase \- but I do think all of the *other stuff* involved in building software makes the 10x thing unrealistic in most cases.

---

**quote** 2025\-08\-06

> ***gpt\-oss\-120b is the most intelligent American open weights model, comes behind DeepSeek R1 and Qwen3 235B in intelligence but offers efficiency benefits** \[...]   
>   
> We’re seeing the 120B beat o3\-mini but come in behind o4\-mini and o3\. The 120B is the most intelligent model that can be run on a single H100 and the 20B is the most intelligent model that can be run on a consumer GPU. \[...]   
>   
> While the larger gpt\-oss\-120b does not come in above DeepSeek R1 0528’s score of 59 or Qwen3 235B 2507s score of 64, it is notable that it is significantly smaller in both total and active parameters than both of those models.*

[Artificial Analysis](https://x.com/artificialanlys/status/1952887733803991070), see also their [updated leaderboard](https://artificialanalysis.ai/models/open-source)

---

**Link** 2025\-08\-06 [Tom MacWright: Observable Notebooks 2\.0](https://macwright.com/2025/07/31/observable-notebooks-2):

Observable announced [Observable Notebooks 2\.0](https://observablehq.com/notebook-kit/) last week \- the latest take on their JavaScript notebook technology, this time with an [open file format](https://observablehq.com/notebook-kit/kit) and a brand new [macOS desktop app](https://observablehq.com/notebook-kit/desktop).

Tom MacWright worked at Observable during their first iteration and here provides thoughtful commentary from an insider\-to\-outsider perspective on how their platform has evolved over time.

I particularly appreciated this aside on the downsides of evolving your own not\-quite\-standard language syntax:

> Notebook Kit and Desktop [support vanilla JavaScript](https://observablehq.com/notebook-kit/#vanilla-java-script), which is excellent and cool. The Observable changes to JavaScript were always tricky and meant that we struggled to use off\-the\-shelf parsers, and users couldn't use standard JavaScript tooling like eslint. This is stuff like the `viewof` operator which meant that [Observable was not JavaScript](https://observablehq.com/@observablehq/observable-javascript). \[...] *Sidenote*: I now work on [Val Town](https://www.val.town/), which is also a platform based on writing JavaScript, and when I joined it *also* had a tweaked version of JavaScript. We used the `@` character to let you 'mention' other vals and implicitly import them. This was, like it was in Observable, not worth it and we switched to standard syntax: don't mess with language standards folks!

---

**Link** 2025\-08\-06 [Jules, our asynchronous coding agent, is now available for everyone](https://blog.google/technology/google-labs/jules-now-available/):

I wrote about the Jules beta [back in May](https://simonwillison.net/2025/May/19/jules/). Google's version of the OpenAI Codex PR\-submitting hosted coding tool graduated from beta today.

I'm mainly linking to this now because I like the new term they are using in this blog entry: **Asynchronous coding agent**. I like it so much I [gave it a tag](https://simonwillison.net/tags/asynchronous-coding-agents/).

I continue to avoid the term "agent" as infuriatingly vague, but I can grudgingly accept it when accompanied by a prefix that clarifies the type of agent we are talking about. "Asynchronous coding agent" feels just about obvious enough to me to be useful.

... I just ran a Google search for `"asynchronous coding agent" -jules` and came up with a few more notable examples of this name being used elsewhere:

* [Introducing Open SWE: An Open\-Source Asynchronous Coding Agent](https://blog.langchain.com/introducing-open-swe-an-open-source-asynchronous-coding-agent/) is an announcement from LangChain just this morning of their take on this pattern. They provide a hosted version (bring your own API keys) or you can run it yourself with [their MIT licensed code](https://github.com/langchain-ai/open-swe).
* The press release for GitHub's own version of this [GitHub Introduces Coding Agent For GitHub Copilot](https://github.com/newsroom/press-releases/coding-agent-for-github-copilot) states that "GitHub Copilot now includes an asynchronous coding agent".

---

**Note** [2025\-08\-07](https://simonwillison.net/2025/Aug/7/previewing-gpt-5/)

A couple of weeks ago I was invited to OpenAI's headquarters for a "preview event", for which I had to sign both an NDA and a video release waiver. I suspected it might relate to either GPT\-5 or the OpenAI open weight models... and [GPT\-5 it was](https://simonwillison.net/2025/Aug/7/gpt-5/)!

OpenAI had invited five developers: [Claire Vo](https://clairevo.com/), [Theo Browne](https://www.youtube.com/@t3dotgg), [Ben Hylak](https://x.com/benhylak), [Shawn @swyx Wang](https://www.swyx.io/), and myself. We were all given early access to the new models and asked to spend a couple of hours (of paid time) experimenting with them, while being filmed by a professional camera crew.

The resulting video is [now up on YouTube](https://www.youtube.com/watch?v=-gXmWYQtv5o). Unsurprisingly most of my edits related to [SVGs of pelicans](https://simonwillison.net/tags/pelican-riding-a-bicycle/).

---