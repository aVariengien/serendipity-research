# Weekend Links #10: Tariffs, Gemini, and a herd of Llamas

*Also the latest GPT5 rumors, AI geopolitics, and sentient yogurt*

Published: 2025-04-06
Source: https://peterwildeford.substack.com/p/weekend-links-10-tariffs-gemini-and

---

[![Image](https://substackcdn.com/image/fetch/$s_!xflu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F133af52b-033a-44ea-ab71-77a7b63510c3_1446x1376.jpeg "Image")](https://substackcdn.com/image/fetch/$s_!xflu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F133af52b-033a-44ea-ab71-77a7b63510c3_1446x1376.jpeg)

***About the author:** Peter Wildeford is a top forecaster, ranked top 1% every year since 2022. Here, he shares the news and analysis that informs his forecasts.*

# AI

#### Tariffs — implications for AI?

The 32% tariffs on Taiwan announced by Trump on April 2 could threaten the very foundation of US AI development, as 90% of advanced GPUs come from the island nation.

Trump announced massive tariffs on April 2 that are taking the whole world by storm. NVIDIA continues to be down, especially after tanking earlier due to prior tariff announcements and DeepSeek effects. Many other tech stocks are affected, as is SoftBank (down 22%). There’s a lot to comment about the tariffs broadly, but here I’m going to keep it to AI.

[It took awhile to get to the bottom of this](https://x.com/peterwildeford/status/1907799605028212849) but it appears that while CPUs are exempt from the tariffs, GPUs are not. The likely rationale is that Trump wants to encourage domestic manufacturing of GPUs, preferring tariffs as the solution than the bipartisan [CHIPS Act](https://en.wikipedia.org/wiki/CHIPS_and_Science_Act), which [Trump famously hates](https://www.dailysignal.com/2025/03/11/why-does-trump-hate-chips-act/). But this is going to make large GPU purchases more expensive, which could slow down AI.

Similarly, steel tariffs and power transformer tariffs will increase construction costs for data centers. This will make massive buildouts like Stargate more expensive as basically everything that is purchased is becoming more expensive without easy replacement.

Additionally, Google (down 22% YTD) and Meta (down 16% YTD) may face "double whammy" effects where their AI infrastructure costs increase at the same time potential economic headwinds could impact their core businesses that fund AI and provide infrastructure.

However, this doesn’t mean AI development will be *thoroughly* affected — total effects seem unclear. The money is still there, the chips will still be bought, and data centers will still be built. There’s too much on the line for this to just stop. And AI is most responsive to orders of magnitude increases — if AI gets 2x cheaper to train on chips that get 2x better per dollar, the result is still a 3x increase in AI model power even if 25% is lost to tariffs.

~

#### OpenAI o3 and o4-mini — coming soon. GPT5 — delayed again

Back in [Weekend Links #4](https://peterwildeford.substack.com/p/weekend-links-4-faxing-chatgpt-homemade), I covered rumors that the long-fabled GPT5 would come in May. This is a long push from the original rumors that it would come last December. But GPT5 is being delayed again.

**[Per Sam Altman](https://x.com/sama/status/1908167621624856998):**

[![](https://substackcdn.com/image/fetch/$s_!rbFZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F41057eb8-906d-4074-9e81-21a3168d0e5d_1132x436.png)](https://substackcdn.com/image/fetch/$s_!rbFZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F41057eb8-906d-4074-9e81-21a3168d0e5d_1132x436.png)

Recall that GPT5 was meant to combine a more powerful base model with a more powerful reasoning model to make a hybrid model that can choose how much it needs to think and combine the best of both.

o3 is a pure reasoning model, likely based on GPT4o like o1 but with more power. We’ve seen o3’s stunning release in December with strong metrics and o3-mini has been somewhat useful.

A few thoughts:

* The new timing of a o3 “in a couple of weeks” likely is the original May release but the combination with GPT5 is not ready yet.
* OpenAI likely feels pressure to release o3 as soon as possible in response to Gemini 2.5.
* The demand issues are real. The viral desire to convert images to *Studio Ghibli* has [dramatically increased demand in OpenAI’s products](https://x.com/sama/status/1905296867145154688), with at one point [one million users added in just one hour](https://x.com/sama/status/1906771292390666325). At the same time, consumers have found frustration with OpenAI’s severe rate limiting. It seems customers prefer delays in the product as opposed to accepting the scarcity or higher prices and OpenAI is potentially responding to that.
* The demand issues also intersect with concerns around tariffs on GPUs, as above. Seems good for OpenAI to delay and get some more optionality before making big new GPU usage commitments.
* While it’s not clear what GPT5 will be, I still expect it to be a single unified model combining increases to the base model (like GPT4 —> GPT4.5) but with even more increases to reasoning power, potentially powered by o4 instead of o3.

~

#### Gemini 2.5 — it’s good

When it comes to Google, one question we should be asking is why aren’t they *dominating* in AI right now? They’ve been working on reinforcement learning for over a decade. They had the best AI by a large margin during the AlphaGo era. For all of 2000-2020, Google had the best models. They have boatloads of money and talent and don’t need to raise capital.

…But then OpenAI released ChatGPT and GPT4 and Google couldn’t keep up. Google’s Bard was terrible. And initial Gemini was terrible too. [Remember the black Nazis](https://www.nytimes.com/2024/02/22/technology/google-gemini-german-uniforms.html)?

But now Google is finally back! Gemini 2.5 is topping a lot of evaluations, including my own, and is quickly becoming my go-to model for nearly everything that doesn’t require emotional intelligence (use Claude or GPT 4.5), deep research (use OpenAI’s Deep Research), image generation (use GPT 4o), good writing (use Claude), or software engineering (use Claude).

It’s faster than OpenAI’s o1 pro, smarter, and free! An amazing deal.

To learn more, I recently listened to **[this podcast with Nathan Labenz and Jack Rae](https://www.cognitiverevolution.ai/scaling-thinking-gemini-2-5-tech-lead-jack-rae-on-reasoning-long-context-the-path-to-agi/)**. Rae is the Principal Research Scientist at Google DeepMind who works on the thinking, reasoning, and inference-time scaling of models. My notes:

* **Why does simple reinforcement learning for correctness works so well now, but not before?** The “suddenness” is because the synergy of big models plus RL has finally reached a point where it yields striking capabilities. It just didn’t work with smaller models and worse techniques. Now there’s finally a combination where current models can really take advantage of thinking to go to new heights.

* **Apparently thinking models date back much earlier than their 2024 launch.** Within Google, they assembled a dedicated “thinking” group in late 2022. OpenAI had been working on it as early as 2023.
* **Where does thinking data come from?** Gemini uses human-generated data (getting people to write down their reasoning, extracting this from essays); model-based synthetic data (getting the model to generate possible reasoning and having this corrected); and direct RL signals (seeing what reasoning yields the correct result and then reinforcing that).
* **The thinking you see in Gemini is exactly what the model thinks.** Rae confirms they currently show raw chain-of-thought in AI Studio and Gemini’s main app.
* **What’s next?** Remaining directions of research involve better memory systems, larger context windows, more and better reasoning, and agentic skills (environment and tool use).

~

…After all of this, three things still baffles me:

* With Google models being good now, **why does the Gemini integration into email and Google docs still suck?** You’d think this would me an amazing opportunity for them to drive a ton of value but instead it’s barely usable.
* **[When will they release model evaluations for Gemini 2.5?](https://www.transformernews.ai/p/google-breaks-its-promises)** **Or Gemini 2.0 for that matter?** With a new model pushing the frontier, [this is a bad norm as models become more potentially dangerous](https://peterwildeford.substack.com/p/ai-security-is-important-practice). Anthropic and OpenAI generally do release these cards upon model release rather than general availability[1](https://peterwildeford.substack.com/p/weekend-links-10-tariffs-gemini-and#footnote-1-159608081).

  + Rae says that full system cards and final reports appear at general availability, not for experimental releases. But Gemini 2.5 is very widely available for free, and I’m not really sure how that is distinct from “general availability”. If Gemini 2.5 hypothetically were a model that could enable harm, people could certainly use it to do so. This [is a peril of voluntary commitments](https://peterwildeford.substack.com/p/the-promises-and-perils-of-voluntary).
* **[Why did Gemini give me soup recipes](https://x.com/peterwildeford/status/1908157758311899558)** when I was asking it to help me analyze government documents? This must be what “experimental” means.

~

#### A herd of Llama 4 — it’s ok?

My prior analysis has suggested five companies with the GPUs, money, and talent to be on the true frontier of AI: OpenAI, Google DeepMind, Anthropic, xAI, and Meta. I’ve also granted outside shots to DeepSeek and Mistral.

However, throughout this time OpenAI has had cutting-edge work via o3, o1 Pro, and Deep Research; Anthropic through Claudes 3.5-3.7, and Google DeepMind has done really well lately with Gemini 2.5. Even xAI’s Grok 3 is strong, though less good than the other three. But Meta has always been towards the bottom of the pack.

Meta is now trying to change that with **[Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)**, dropped today:

[![](https://substackcdn.com/image/fetch/$s_!s-y0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe0dec913-7fe2-46f5-9098-425790735911_1920x1080.png)](https://substackcdn.com/image/fetch/$s_!s-y0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe0dec913-7fe2-46f5-9098-425790735911_1920x1080.png)

Here’s what we know:

* **Line-up of models include** Scout (small), Maverick (mid-sized), and Behemoth (large). Scout and Maverick are available now, while Behemoth is not out yet.

  + *Behemoth is still training and being used as a distillation model (used to make smaller models better by teaching them how to emulate a bigger model).*
* **The models are natively multimodal**, supporting text, images, and video processing.
* **They’re not reasoning models** — they don’t think before answering. Thinking usually improves performance.
* **The weights are freely available for download.**

  + *This is good because it enables a lot of research and specific fine-tuning. But [it could become bad at some point in the future](https://peterwildeford.substack.com/p/ai-security-is-important-practice) as [it is still impossible to prevent an open-weight model from being used for nefarious purposes](https://arxiv.org/abs/2311.00117).*
* **It was dropped on a weekend, [apparently moved from Monday](https://x.com/peterwildeford/status/1908904824747212976).** I wonder why? I guess we will find out soon.
* **It places second in [Chatbot Arena](https://lmarena.ai/?leaderboard), a new record for Meta.** But two caveats: (1) it drops to fifth when [style controlled](https://lmsys.org/blog/2024-08-28-style-control/) and (2) models are ranked by normal humans who don’t really know enough to judge advanced model capabilities these days.
* **This finally happens after repeated delays.** According to [The Information](https://www.theinformation.com/articles/meta-nears-release-new-ai-model-performance-hiccups), delays were due to the model underperforming on technical benchmarks. In my opinion, it still seems like Meta was pretty selective about the metrics they chose to use (and the metrics they didn’t) and how they did the comparisons, suggesting the model may not be that good.
* **Public reaction on Twitter has been mixed.** Users praise Llama 4's open-source nature. But specific criticisms have emerged around code generation quality and handling of political content.
* **The small Scout model is designed to run efficiently on a single H100 GPU**, similar to Google’s Gemma. That’s cool.
* **Context windows are long**, with a remarkable 10 million tokens for Scout.

  + *Context windows refer to how much can be seen by a model when responding. 10 million tokens is the entire Harry Potter series roughly 10 times over, which is impressive.*
* **The model is ~5e25 FLOPs**, about 2x as large as GPT4 and 4x smaller than GPT4.5x. Training only took about two months.

~

…Also of interest is that [OpenAI is planning to release an open-weight model](https://x.com/sama/status/1906793591944646898).

~

#### Why isn’t Russia leading in AI?

In [Weekend Links #8](https://peterwildeford.substack.com/p/weekend-links-8-canadian-ai-indian), I reviewed the top AI models and found them to be nearly all American (xAI, OpenAI, Google, Anthropic, Meta) or Chinese (DeepSeek, Alibaba, Zhipu, 01AI, Tencent, StepFun), with one from Canada (Cohere) and from France (Mistral). France, the US, and China are also the only countries spending at the rate to develop advanced AI. No other countries make this list.

**Why not Russia?** Back in 2017, [Putin said](https://apnews.com/article/bb5628f2a7424a10b3e38b07f4eb90d4) “the one who becomes the leader in this [AI] sphere will be the ruler of the world”, so he clearly had his eyes on the technology from early on. Russia has the ambition and Russian cyberoffense capabilities are very notable. And Russian company Yandex was an early leader in ML around 2018. So why isn’t Russia doing better in AI?

There has been notable brain drain due to the 2022 invasion of Ukraine, which happened right around a time when the AI industry would otherwise have taken off. But another interesting article explains that **[it could be Putin’s technophobia](https://www.ft.com/content/d11a3bab-301b-42f4-9c25-64ad6abebc64)**. Apparently Putin doesn’t use the internet and doesn’t have a smart phone. Maybe he’s worried about being hacked? Also Russia has struggled to acquire GPUs, having significantly fewer than China, let alone the US. As the author puts it: “Russia is using 20th-century tactics in pursuit of a 19th-century goal while the 21st century is passing it by.”

~

#### French AI spending

Awhile ago it was announced that France and the EU were jointly spending €309B EUR ($339B USD) on AI build outs. As I said at the time, whether this money can make France competitive with the US and China on AI remains to be seen, based significantly on how it is used. While there are many questions about this, the first is how much of the money is actually going to advanced AI development in the first place? **[Oliver Guest analyzes these announcements](https://humangeneralintelligence.substack.com/p/france-and-the-eu-announced-big-ai)** and determines that ~€85B EUR (~$93B USD) of this will be used to train frontier AI models.

Based on this, Guest concludes:

> These investments seem like important evidence that France, and to a lesser degree the EU, will have the necessary compute for frontier model training.

Given that OpenAI’s Stargate is spending ~$100B per year, this sounds right. But there are some strong assumptions: that France and the EU can build at the same rate as the US, recur this spend annually, and focus on a single company (Mistral?). But tariffs may help slow down the US and buy the EU more of an edge to catch up.

~

#### New reading list on international conflict over AI

This week, with Oscar Delaney, I published [“Mutual sabotage of AI probably won’t work”](https://peterwildeford.substack.com/p/mutual-sabotage-of-ai-probably-wont), a review of a particular plan to address geopolitical concerns from AI — namely that countries might worry about losing power due to rival countries’ advanced AI development and may launch preemptive attacks in response.

Building on this, Delaney has now worked with Oliver Guest to produce **[“AI, the spectre of decisive advantage, and international conflict”](https://humangeneralintelligence.substack.com/p/ai-the-spectre-of-decisive-advantage)**, a reading list that explains additional solutions and analysis that aim to address this concern.

# Whimsy

**[Is Wine Fake?](https://asteriskmag.com/issues/01/is-wine-fake)** Master Sommeliers can identify specific wines in blind tastings after years of training, and studies show experts can consistently detect subtle flavor compounds and characteristics. However, experts can also be fooled by simple tricks like food coloring, wine competition judges are often inconsistent, and wine price rarely correlates with enjoyment even among expert wine tasters.

The broader implications suggest that expertise can be simultaneously real and deeply flawed. Just as wine experts in the 1970s were blindsided in the [Judgment of Paris](https://en.wikipedia.org/wiki/Judgment_of_Paris_(wine)) by California wines outperforming French ones due to national bias, expertise in many fields may combine genuine knowledge with cultural assumptions that need to be challenged through rigorous blind testing. The key is maintaining a balance between respecting demonstrated expertise while remaining skeptical of unexamined beliefs.

~

**[When the Yogurt Took Over: A Short Story](https://whatever.scalzi.com/2010/10/02/when-the-yogurt-took-over-a-short-story/).** It’s meant to be taken literally, as in sentient yogurt actually does take over the US. Presented without further comment.

~

**Important PSA: How to disable a robot dog if it attacks you**

It’s never too late to be prepared for the upcoming robot dog swarms.

…Though personally I’m a bit surprised the drones bring in robot dogs with guns when the drones could just themselves have guns.

If you liked this, consider subscribing for more!

Subscribe

[1](https://peterwildeford.substack.com/p/weekend-links-10-tariffs-gemini-and#footnote-anchor-1-159608081)

Though the OpenAI Deep Research system card was not released until after the model moved from the Pro ($200/mo) tier to the Plus ($20/mo) tier. This seems more defensible than what Google is doing, however.