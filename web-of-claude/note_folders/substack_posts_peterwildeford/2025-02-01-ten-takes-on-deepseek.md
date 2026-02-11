# Ten Takes on DeepSeek

*No, it is not a $6M model nor a failure of US export controls*

Published: 2025-02-01
Source: https://peterwildeford.substack.com/p/ten-takes-on-deepseek

---

[![A person holding a cell phone in their hand](https://images.unsplash.com/photo-1738107450287-8ccd5a2f8806?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wzMDAzMzh8MHwxfHNlYXJjaHwxfHxkZWVwc2Vla3xlbnwwfHx8fDE3MzgzNzI0NzR8MA&ixlib=rb-4.0.3&q=80&w=1080 "A person holding a cell phone in their hand")](https://images.unsplash.com/photo-1738107450287-8ccd5a2f8806?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wzMDAzMzh8MHwxfHNlYXJjaHwxfHxkZWVwc2Vla3xlbnwwfHx8fDE3MzgzNzI0NzR8MA&ixlib=rb-4.0.3&q=80&w=1080)

Photo by [Solen Feyissa](true) on [Unsplash](https://unsplash.com)

Yes, DeepSeek is impressive.

But the buzz around DeepSeek is potentially more impressive – not since GPT4 have I seen a single AI model take the entire world by storm. Rarely in my life have I seen as many bad takes. It’s time to go through some of the hype and set the record straight.

DeepSeek is impressive, but it is not some crazy unexpected outlier. DeepSeek is cheap but not actually amazingly cheap. Most importantly, DeepSeek is not the end of US export controls or US AI dominance, and it does not challenge our understanding of geopolitics nearly as much as you might think if you only read the headlines.

Let’s dive in and give it a fairer assessment.

## 1. DeepSeek is definitely impressive

First off the bat, I am not a DeepSeek denier or a DeepSeek doubter. I do want to acknowledge that DeepSeek is truly impressive. There are some genuine innovations:

* Multi-head latent attention (MLA) for efficient memory usage, reducing the size of model without compromising quality by using a cool compression technique.
* Improved mixture-of-experts (MoE) architecture, increasing load balancing to better handle the balance between common and specialized knowledge.
* More token-efficient training by using formulas “predict” which tokens the model would activate and training on only those tokens, thus needing fewer GPUs by training fewer parameters.
* Multi-token prediction capabilities, which allows the model to predict two tokens ahead with 85-90% accuracy, potentially doubling inference speed.
* V3’s training uses mixed-precision FP8 arithmetic and advanced load-balancing tweaks to further improve speed

These improvements demonstrate deep understanding of Transformer architecture limitations rather than brute-force experimentation. The fact that the service is being offered for free with no plans for commercialization is impressive and it does genuinely broaden people’s access to a strong reasoning model.

Lastly, sharing all of these innovations in an open access way with open weights will be a large improvement to research. For example, R1 already taught us that it appears making a reasoning model does not need fancy techniques like process reward or Monte Carlo Tree Search and instead you can just use the simplest approach: ‘guess and check’ (produce a candidate answer, or ‘guess’, and then run it through a verification process, the ‘check’, and adjust from there).

## 2. DeepSeek isn’t “out of nowhere” – people just don’t pay attention

People who are just tuning into DeepSeek recently have missed a trend that they could’ve seen coming.

DeepSeek is owned by High-Flyer, a Chinese hedge fund that trades exclusively with AI. They pivoted more into AI in 2023. Since then, DeepSeek has clearly been the best Chinese AI lab. DeepSeek first published some of their innovations in MoE [in 2024 January](https://arxiv.org/abs/2401.06066) already showing good efficiency gains, being more efficient than Meta’s Llama model. [DeepSeek-V2](https://arxiv.org/abs/2405.04434) in 2024 May showed their innovations in MLA. [SemiAnalysis also reported on DeepSeek](https://semianalysis.com/2024/05/07/openai-is-doomed-et-tu-microsoft/) as early as May.

From the above, it was easy to extrapolate what might come out, but to top it off [the DeepSeek-V3 paper](https://arxiv.org/abs/2412.19437) that proved it all came out in 2024 December 27, almost a full month before people started freaking out about DeepSeek.

## 3. $6M is not nearly enough to buy you a good model and DeepSeek’s total cost is much more than that

DeepSeek v3 was trained for $6M. OpenAI Stargate is spending $100B per year – more than 15,000 times the DeepSeek v3 price tag. But OpenAI models don’t seem that much better. What’s going on here?

The answer is you’re comparing incorrectly.

**The “$6M” figure refers to the marginal cost of the single pre-training run that produced the final model.** But there’s much more that goes into the model – cost of infrastructure, data centers, energy, talent, running inference, prototyping, etc. Usually the cost of the single training run for the single final model training run is ~1% of the total capex spent developing the model.

**It’s like comparing the marginal cost of treating a single sick patient in China to the total cost of building an entire hospital in the US.**

For example, [per SemiAnalysis](https://semianalysis.com/2025/01/31/deepseek-debates/), DeepSeek apparently has a GPU fleet of ~10K A100 NVIDIA GPUs and ~10K H100s acquired prior to the US-led export controls that banned exports of these in October 2022 plus another ~10K H800s (which are nearly as good as H100s and were export controlled in October 2023). On top of that, DeepSeek likely has another ~20K H20s, which are not as good as H100s/H800s/A100s and are not under export controls. **At a market price of ~$15K/GPU on average, this would cost $750M just for GPUs.**

[SemiAnalysis calculates](https://semianalysis.com/2025/01/31/deepseek-debates/) the total server capex for DeepSeek at ~$1.6B.

…Then there were 199 ML researchers on the [v3 technical paper](https://arxiv.org/abs/2412.19437). Even given that Chinese salaries are much lower, DeepSeek still pays well and is still rumored to pay salaries above $1M USD/yr to top candidates. Even if we assume the average salary of their paper team is $300K/person/year, that means the staff costs alone are ~$60M/yr.

Lastly, the DeepSeek r1 model that is being compared to OpenAI’s models is a reasoning model trained *on top* of DeepSeek v3 (similar to how OpenAI o1 is a reasoning model on top of the base model of GPT4o) and training this reasoning model likely took another few million in compute. **People quoting that DeepSeek r1 was trained with $6M are thus being** ***doubly misleading*** by not including the costs of developing the reasoning model – in addition to not mentioning the capex not related to immediately training the final model.

## 4. DeepSeek is not a performance outlier

The bull case for DeepSeek is that it is as good as or better than o1 despite being much cheaper. However, this doesn’t seem to be the case.

**Cost: Not the cheapest**

Almost all DeepSeek takes seem premised on the idea that [Gemini 2.0 Flash Thinking](https://deepmind.google/technologies/gemini/flash-thinking/) (G2FT) doesn’t exist. DeepSeek r1 is not the first model to show the chain of thought to the user, G2FT is! Also while r1 at $2.19 per million output tokens is very cheap, it is not as cheap as G2FT – G2FT will likely be available for almost 10x cheaper at $0.30 per million output tokens. (The fact that people don’t know this shows that Google is bad at marketing.)

Furthermore, this comparison for price isn’t necessarily apples-to-apples. When comparing costs between models, we have to take into account profit margins. My guess is that DeepSeek is not offering their model with much of a profit margin, whereas we don’t know how much of a profit margin is baked into Google or OpenAI’s offerings. Additionally, it seems that r1 uses more chain-of-thought tokens (which you still pay for), and if you don’t care about those and just want the final output, it may be even less cheap in comparison than you expect.

**Performance: Not the best**

While R1 is good, R1 is not the *best* reasoning model either (even on questions not related to Tiananmen Square). From my personal testing DeepSeek R1 seems a touch worse than OpenAI o1 and definitely worse than OpenAI o1-pro (the $200/month version). And I imagine o3 (full) will be even better.

[![Image](https://substackcdn.com/image/fetch/$s_!Ipvb!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0d66c9e7-0d94-46d8-91d0-80ed50194d4b_1600x1182.jpeg "Image")](https://substackcdn.com/image/fetch/$s_!Ipvb!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0d66c9e7-0d94-46d8-91d0-80ed50194d4b_1600x1182.jpeg)

In fact, r1 even loses to the cheaper G2FT on some benchmarks, though I think r1 is better overall.

[![](https://substackcdn.com/image/fetch/$s_!-43w!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8c3b825b-1cf1-436b-8957-1d71549f7a2d_1179x1187.png)](https://substackcdn.com/image/fetch/$s_!-43w!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8c3b825b-1cf1-436b-8957-1d71549f7a2d_1179x1187.png)

Timothy B. Lee from Understanding AI puts OpenAI o1-pro, Gemini 2.0 Flash Thinking, and DeepSeek r1 [through a more systematic test](https://www.understandingai.org/p/i-spent-two-days-testing-deepseek) and comes away with a similar ranking.

[The ARC benchmark also finds r1 inferior](https://arcprize.org/blog/r1-zero-r1-results-analysis) to even o1 (low), let alone o3 (high).

[![](https://substackcdn.com/image/fetch/$s_!LpLF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5043a0c9-7f1c-4cd7-8986-722fa3abd187_1208x592.png)](https://substackcdn.com/image/fetch/$s_!LpLF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5043a0c9-7f1c-4cd7-8986-722fa3abd187_1208x592.png)

Instead, I’d argue that DeepSeek fits well on a price-capabilities curve that is not an outlier based on what other offerings there are from US companies. That is, DeepSeek has gone for a “notably cheap but not super cheap and notably good but not super good” and DeepSeek is not especially capable for its price and I’m very confident OpenAI et. al. could make an offering at that point very quickly if they wanted to.

[![](https://substackcdn.com/image/fetch/$s_!YBUP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7593eee8-0877-4729-9f0c-0d649c264f2f_1114x816.png)](https://substackcdn.com/image/fetch/$s_!YBUP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7593eee8-0877-4729-9f0c-0d649c264f2f_1114x816.png)

*Illustration of how DeepSeek r1 fits neatly on an implied price-capabilities curve without being an outlier. Illustrative version of what the price-capability curve might look like. Distances not precise.*

## 5. DeepSeek is “fast following” but “fast following” doesn’t get you ahead in AI

China is generally famous for being a “fast follower” rather than a leader, and DeepSeek seems to be the same.

[There are rumors swirling around](https://www.bloomberg.com/news/articles/2025-01-29/microsoft-probing-if-deepseek-linked-group-improperly-obtained-openai-data) that DeepSeek may have deliberately copied OpenAI via a process of distilling, where DeepSeek asks OpenAI’s models questions, receives the answers, and then trains their own model to mimic those answers. If this is true, this would suggest that DeepSeek is not capable of making a more powerful model than OpenAI since they would need OpenAI’s model to train on.

However, even if those rumors are not true, it’s still the case that DeepSeek catches up by learning from OpenAI’s research - without that they’d be further behind. It seems easy for DeepSeek to produce reasoning models when they can borrow insights into which research paths are dead ends (like MCTS) and which look promising.

[![](https://substackcdn.com/image/fetch/$s_!VG6k!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4f9494e4-c674-4701-ad26-ada8debab5f2_750x460.png)](https://substackcdn.com/image/fetch/$s_!VG6k!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4f9494e4-c674-4701-ad26-ada8debab5f2_750x460.png)

*Meme from [Eric Gastfriend on Twitter](https://x.com/egastfriend/status/1884442844057788590)*

## 6. DeepSeek’s progress is on trend and doesn’t mean the end of capital intensive models

Some have taken DeepSeek to mean that future models will be trained more cheaply (though still with $2B+ of capex, as mentioned above) and thus we won’t need massive infrastructure spending on models… or that companies can spend a little and catch up.

But this is wrong – AI companies can use the same efficiency gains and apply them to their much larger amounts of compute and get even more powerful models than DeepSeek.

Lennart Heim writing for ChinaTalk [defines this clearly via the chart below](https://www.chinatalk.media/p/deepseek-what-the-headlines-miss) about the *access effect* versus *the performance effect*:

[![increasing-compute-efficiency.png](https://substackcdn.com/image/fetch/$s_!-nT0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F651a5227-c8d1-4d88-ba05-8a8d9047c11f_990x812.png "increasing-compute-efficiency.png")](https://substackcdn.com/image/fetch/$s_!-nT0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F651a5227-c8d1-4d88-ba05-8a8d9047c11f_990x812.png)

What this means is that when you have an improvement in efficiency that lets you get more performance at all levels of compute (seen in the chart as shifting from `t = 0` to `t = 1`, you can use that to get the same performance for cheaper (‘the access effect’) or you can use that to get an even better model at the same price (‘the performance effect’). The access effect explains DeepSeek as compared to American models before these efficiency gains, but American models with a larger amount of compute will just be more powerful.

And these algorithmic advances are expected. Epoch has found that [algorithms improve price-capability efficiency by 3x per year](https://epoch.ai/blog/algorithmic-progress-in-language-models), so it should be no surprise to see DeepSeek being 3x as efficient as models like Meta’s Llama 3 that came out almost a full year ago.

But ultimately despite algorithmic advancement, the capabilities-price curve still curves upward. Assuming you want the most powerful model, you will still want to spend as much as possible and have as much compute as possible!

## 7. DeepSeek is not evidence of failure for export controls

Firstly, it’s important to note that despite Huawei’s Ascend GPUs being around, top Chinese companies like DeepSeek still greatly prefer NVIDIA hardware coming out of the West. However, these chips are harder and harder for Chinese companies to get.

Since 2022 October and in multiple rounds of revisions, [the US has led export controls](https://en.wikipedia.org/wiki/United_States_New_Export_Controls_on_Advanced_Computing_and_Semiconductors_to_China) aiming to prevent the Chinese government from acquiring advanced computing chips and building powerful models, citing the drawbacks of the Chinese government using these chips for military purposes. Some have argued that the point of these export controls was that a Chinese company should never be able to train a model like DeepSeek r1 and thus the export controls have failed.

**But firstly, this is clearly not true. DeepSeek didn’t manage to get around the export controls and instead were meaningfully held back by them, as designed.** doesn’t have as much compute as they would like, specifically because of the US-led export controls. [In an interview](https://www.linkedin.com/pulse/deepseek-ceo-liang-wenfeng-interview-translated-hao-sheng-hsdjc/), Liang Wenfeng, CEO and founder of DeepSeek, said “The problem we are facing has never been funding, but the export control on advanced chips”.

**It’s without doubt that DeepSeek’s models would be even more powerful without US export controls.** Their stock of GPUs is not 50K A100s but rather a rag-tag mix of A100s, H100s, H800s, and H20s that they could cobble together – and that’s due to export controls. Also a lot of the engineering challenges that DeepSeek has produced have been specifically to get the most out of their lower-quality chips, solving problems that American companies don’t even have. Furthermore, due to tightening export controls, many of the chips they do have can no longer be acquired [without illicit smuggling](https://www.cnas.org/publications/reports/preventing-ai-chip-smuggling-to-china), which should become harder over time.

DeepSeek was forced to be efficient because it lacks access to the best US chips – that doesn’t mean it wouldn’t prefer more advanced hardware. Letting China buy as many advanced GPUs as they want obviously closes the US-China AI gap more quickly.

More importantly – the US export controls are playing a longer game. **We're barely one new chip generation into the export controls, and the export controls will bite harder as chip technology continues to outpace China.** The state of the art of chips will shift to the B200 chip within a few months or less and DeepSeek won’t have any of these without smuggling. This will allow American models to be even more powerful at the same level of capital in a way that Chinese companies won’t be able to match.

## 8. DeepSeek currently is 6-8 months behind OpenAI

Just going off of publication dates, OpenAI O1 [was announced on 2024 September 12](https://openai.com/o1/) and [DeepSeek r1 was announced on 2025 Jan 20](https://api-docs.deepseek.com/news/news250120), a difference of 4 months and 8 days. However, I suspect the gap is even larger given that I expect OpenAI to have a longer delay between completing and announcing their models than DeepSeek.

**Measuring between base models suggests an even larger difference in lead.** Reasoning models are relatively easier to produce once you have a good base model (4o for OpenAI and V3 for DeepSeek), and the difference between the time of OpenAI producing a GPT-4 base model and DeepSeek producing their own base model is much more than six months. DeepSeek v3 reached parity with OpenAI 4o, but DeepSeek v3 (launched 2024 Dec 27) comes 7 months and 14 days after 4o ([launched 2024 May 13](https://openai.com/index/hello-gpt-4o/)).

**Keep in mind also that while Chinese firms like DeepSeek openly share their progress, US firms don’t.** We don’t necessarily know what the capabilities of OpenAI are as of today – public benchmarking is not a good measure of today’s capabilities because what is in the lab is not publicly known. It also seems US labs do more safety testing and red teaming after they've developed a new model, meaning there's more of a lag from "achieving capabilities" to "releasing new capabilities" – this could make the actual gap between OpenAI and DeepSeek even larger.

## 9. Due to capital and chips, DeepSeek may fall even further behind

As mentioned, DeepSeek doesn’t have any particular secret sauce that OpenAI et al can’t copy. This means the AI race is still down to compute.

DeepSeek has access to ~50K GPUs, and not even the GPUs on the cutting edge. [Via Stargate](https://semianalysis.com/2025/01/23/openai-stargate-joint-venture-demystified/), OpenAI will by the end of 2025 have a data center with ~100K GB200s, a chip much more powerful than an A100 and even more powerful than the chips DeepSeek has access to. If China can’t catch up with this build out, they won’t be able to compete.

Right now we’re at a curve in the race track:

[![](https://substackcdn.com/image/fetch/$s_!vD3J!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd02e6734-f565-4cf8-9719-16da3881deba_1098x326.png)](https://substackcdn.com/image/fetch/$s_!vD3J!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd02e6734-f565-4cf8-9719-16da3881deba_1098x326.png)

This is due to there not being a large ‘chip gap’ yet before the widespread use of GB200s, the export controls not yet fully setting in, and the capital scaleout in the US not yet having enough time to result in new models. But those trends are all brewing.

This leads to two factors that suggests the US is ahead and this gap may widen even further – the US is on track to spend more than China on compute buildouts and, thanks to the US-led export controls, the US can do those buildouts with more price-efficient chips than DeepSeek can buy.

We haven't yet seen any evidence of compute cluster buildouts of similar scale in China. Absent the Chinese government investing significant capital, DeepSeek won’t have the money they need to compete.

## 10. Absent changes to the status quo, the number of actors who can be ‘first on AI’ is still 5

Correcting the price of DeepSeek is important because it is not the case that anyone with $6M can train a cutting-edge model… instead, the actual price is closer to $2B, even with all of DeepSeek’s efficiency gains. This means that the number of companies that can reach AI is still limited to at most the companies that can afford $2B in AI capex.

However, the capex need to be ‘first on AI’ is going to go up. Due to the capital advantage and chip advantage, I think that the number of companies that truly have a chance of being ‘out in front’ and ‘first’ in AI is even more limited than that.

Currently the live players with a shot (strong team + hundreds of thousands of GPUs + tens of billions of dollars per year in AI capex) seem to be:

* OpenAI with Microsoft and/or Oracle (Stargate)
* Anthropic with Amazon and Google
* Google
* xAI
* Meta
* *[Edited Feb 13: [it’s now possible that France is on this list](https://peterwildeford.substack.com/p/ten-takes-on-the-paris-ai-action).]*

Until either (a) another company gets a lot more capital, (b) nation states themselves begin starting AI projects, or (c) there is truly a stunning breakthrough that is way more out-of-distribution than what DeepSeek did, it’s hard to imagine anyone else getting to the front of AI.

That being said, Of course, this isn’t written in stone and we shouldn’t get complacent. Things can change and (a)-(c) are all possible. And even if you are “first”, that doesn’t mean you automatically win, as we’ve seen reaching an amazing AI advancement first at $100B/yr may only give you 6-12 months before it becomes replicable at $10B/yr and the “fast followers” catch up. What we do with that lead will matter.

Interested in more takes? Subscribe here:

Subscribe