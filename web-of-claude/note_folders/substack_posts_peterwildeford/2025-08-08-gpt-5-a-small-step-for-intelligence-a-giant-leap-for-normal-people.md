# GPT-5: a small step for intelligence, a giant leap for normal people

*GPT-5 focuses on where the money is - everyday users, not AI elites*

Published: 2025-08-08
Source: https://peterwildeford.substack.com/p/gpt-5-a-small-step-for-intelligence

---

[![GPT-5 is here | OpenAI](https://substackcdn.com/image/fetch/$s_!0Rt3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc3441f21-c25d-4a59-b070-3ad65ba6eec0_1600x900.jpeg "GPT-5 is here | OpenAI")](https://substackcdn.com/image/fetch/$s_!0Rt3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc3441f21-c25d-4a59-b070-3ad65ba6eec0_1600x900.jpeg)

Like Punxsutawney Phil on Groundhog Day, a model release is a chance for us AI prognosticators to declare if we have six more weeks of AI winter.

This goes double for a model worthy of the “GPT-5” name.

Recall that GPT-2 came on the scene in 2019 astounding the world by being the first language model that could write coherent paragraphs and roughly stay on topic. GPT-3 then smashed GPT-2 by actually being useful, capable of following instructions to some extent and engaging in rudimentary reasoning when given a few examples of what you were trying to do. GPT-4 then took this to the next level, doing things like acing a bar exam and being a useful copilot for computer programming.

Since then, it’s been harder to shock the world, but I’d say that o1 and o3 also did so, by introducing a new paradigm of thinking prior to answering, and doing much better on expert-level questions in math, science, and software engineering. o3 in particular was shocking when demoed in 2024 December as it had benchmark results well beyond what was anticipated at the time, though the actual o3 rollout itself ended up being much slower and underwhelming relative to these sky-high December expectations.

Otherwise, we just have seen more incremental updates, with steady but gradual changes. This has led OpenAI to chase a model that could astound the world and be worthy of the GPT-5 name without much success. Rumor has it that all of GPT-4.5, o1, and o3 were at one point considered to be candidates worthy of the “GPT-5” name, but they all fell short of what OpenAI was dreaming of[1](https://peterwildeford.substack.com/p/gpt-5-a-small-step-for-intelligence#footnote-1-170321649).

But now we have GPT-5 live and accessible! Amazing! Is this the massive smash we were looking for?

Unfortunately, no. Model evaluation has become increasingly difficult. We generally rely on two tools — formal quantitative evaluations and vibes. **When looking at this, it appears that GPT-5 isn’t a giant leap in intelligence.** It’s an incremental step in benchmarks and a ‘meh’ in vibes for experts. **But it should only be disappointing if you had unrealistic expectations — it is very on-trend and exactly what we’d predict if we’re still heading to fast AI progress over the next decade.**

**Most importantly, GPT-5 is a big usability win for everyday users** — faster, cheaper, and easier to use than its predecessors, with notable improvements on hallucinations and other issues.

Let’s dig in.

[Share](https://peterwildeford.substack.com/p/gpt-5-a-small-step-for-intelligence?utm_source=substack&utm_medium=email&utm_content=share&action=share)

### The benchmarks: exactly what you would predict

Formal evaluations (also known as ‘benchmarking’) are valuable for being objective, quantified, and repeatable — it’s easy to see exactly how much a model is improving. But their strength is also their critical weakness. Because evals work best on well-specified, easily verifiable tasks, they tend to measure only the tasks that can be neatly contained and easily scored. This is very different from the messy, ambiguous problems people face in the real world.

This issue is compounded by the fact that the tasks that evals focus on are also the tasks where reinforcement learning helps models the most — RL also thrives on well-specified and easily verifiable tasks. As a result, formal evals over-index on the tasks where models are already showing the most improvement, potentially suggesting models are stronger than they are if you evaluate more holistically. This makes it difficult to get a good grasp on just how much models are improving. Worse, we can’t rule out contamination from training data—models may simply memorize the test answers.

And when it comes to formal evaluations, it seems like GPT-5 was largely what would be expected — small, incremental increases rather than anything [worthy of a vague Death Star meme](https://x.com/peterwildeford/status/1953280486073377256). All forecasting is a matter of looking at past trendlines and then continuing them out, and it turns out GPT-5 basically lands exactly where these trendlines say:

* The **SWE-Bench-Verified** scores (a measure of software skill, [as measured independently by EpochAI](https://epoch.ai/benchmarks)) are unimpressive, landing below Claude 4.1 Opus. This suggests that unfortunately for OpenAI, Claude Code may remain dominant for a bit longer.
* On **METR’s time horizons task**, a more advanced evaluation of software engineering skill, [GPT-5 improved upon the state of the art](https://metr.github.io/autonomy-evals-guide/gpt-5-report/) in a way that is very in-line with what was predicted based on past trends[2](https://peterwildeford.substack.com/p/gpt-5-a-small-step-for-intelligence#footnote-2-170321649).
* On **GPQA**, a set of PhD-level science questions, GPT-5 comes in at basically the same range as Gemini and Grok [when evaluated independently by EpochAI](https://epoch.ai/benchmarks).
* On **ARC-AGI** and **ARC-AGI-2**, both a measure of general intelligence via symbolic reasoning, [GPT-5 fails to outperform Grok 4](https://arcprize.org/leaderboard). On FrontierMath, a measure of advanced mathematical reasoning, [GPT-5 makes an advance](https://x.com/EpochAIResearch/status/1953615906535313664), but in line with the trend.
* On **Deep Research Bench**, my favorite benchmark for researching and analysis performance, [GPT-5 etches out a win by a very small amount, within the margin of error](https://x.com/dschwarz26/status/1953821158417346879). Also it appears GPT-5 is good at some tasks but not others, a bit of a ‘jagged frontier’ that makes it a complement to previous winner Claude 4 Opus rather than a replacement.

I assume OpenAI finally just gave up chasing the big leap in intelligence and just decided that the pressure to release a ‘GPT-5’ was just too great. And we really need more and better evals to measure AI performance.

### The vibes: meh?

The other evaluation method is far less formal — using human judgment, or what we might call *vibes*. Like a professional wine tasting, you get model connoisseurs to evaluate models in open-ended ways, throwing it novel, messy problems, and gauging its usefulness, creativity, and reliability. Vibes-based testing captures dimensions formal evals miss: how well a model can adapt, reason under uncertainty, avoid hallucinations, or handle complex multi-step instructions. The trade-off is that vibes are subjective, noisy, and prone to bias — different testers may walk away with wildly different impressions.

But vibes-based evals depend a lot on the quality of the connoisseur. One common vibes-based eval is [LMArena](https://lmarena.ai/leaderboard), where many people vote across a blind taste test which model answers a particular input best. Here, GPT-5 has a slight #1 edge over Gemini, which had been dominating the leaderboard for quite some time. However, it’s important to realize that these days all models are just too good for the typical user’s use case and LMArena doesn’t see models challenged with the best. Typical human voters — the same people who can’t tell the difference between a $5 wine and a $500 wine — can’t tell the difference between a good model and a great model. LMArena voters just do not have the requisite skills to distinguish model quality in our current advanced age.

Another form of vibes-based evals I dislike are a lot of people who got early access to the model, but are uncritical hype-sters out there who would say the model is good no matter what. Instead, for the people I have been following that have a good track record of model evaluation within their domains, GPT-5 is more “meh”. In line with the benchmarks, the current consensus seems to be that GPT-5 is an incremental improvement.

For example, Daniel Litt, a professional mathematician and model tester, [doesn’t find GPT-5 to be a noticeable improvement in math work](https://x.com/littmath/status/1953619007866835066). Jesse Richardson, the best election forecaster in the world, [doesn’t find GPT-5 to be good at election forecasting](https://x.com/PoliticalKiwi/status/1953637257640104024). Hopefully more solid taste tests will come in soon as people have more time to play with the model.

### The paradigm of AI is different now, but key questions of AI progress are still unanswered

[![](https://substackcdn.com/image/fetch/$s_!K9ct!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Facb53a36-afcf-4e29-ab72-2666f4734f6f_1522x804.png)](https://substackcdn.com/image/fetch/$s_!K9ct!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Facb53a36-afcf-4e29-ab72-2666f4734f6f_1522x804.png)

Back in the good ol’ days of 2023, the paradigm of AI was that you took a model and then made it bigger. This embiggifying happened by adding more data and more compute at training time, something confusingly called *pre-training*[3](https://peterwildeford.substack.com/p/gpt-5-a-small-step-for-intelligence#footnote-3-170321649). GPT-3 was big at the time, but GPT-4 was bigger, and thus better. The thought was that if you took GPT-4 and then made it even bigger, you would get GPT-5 and it would be even more capable — *a whale*.

GPT-3.5, GPT-4, and GPT-4.5 all followed an implicit pattern where each increase was [said to be a step-change of 10x more effective compute](https://x.com/_LouiePeters/status/1895317082578772076). Given this, one would expect GPT-5 to be a base model like GPT-4.5 but with 10x more compute. But this seems unlikely, because the amount of compute needed to build a ‘10x GPT-4.5 model’ shouldn’t yet be available until the end of the year after the completion of the first phase of Stargate.

Instead, ‘2024/2025’-era AI is working out a bit differently. We’ve moved on from the paradigm where the main way to make a model more capable was to train it for more compute and a better model came from some combination of using more GPUs than before, having GPUs that were more efficient than before, pre-training on those GPUs for a longer amount of time than before, or developing better algorithms and data that made your pre-training more efficient.

These days, instead of one way to improve a model, there are now four:

* You can pre-train more (as mentioned)
* You can do **post-training reinforcement learning**, where you show a model a bunch of problems and solutions and then train it to solve those problems
* You can do more **inference-time compute**, where the model spends more compute/time thinking when posed the question, considering more possibilities
* You can improve the **scaffolding**, where you give the model more tools and affordances to better answer questions, like access to web search and a calculator

Each of these can be scaled separately and improve the model quality. It seems like old-school pre-training has kind of died down over 2024-2025, but like a rocket with multiple stages the ‘pre-training’ stage 1 has been depleted but the stage 2 rockets around post-training reinforcement learning, inference-time compute, and scaffolding are still going strong. This is how AI progress has continued over 2024/2025 seamlessly despite the paradigm completely changing.

GPT-5 seems to be bridging this. GPT-5 is essentially two models glued together, a ‘base model variant’ that seems good at creative writing and quick answering and a ‘reasoning model variant’ that answers math, science, and software questions with much more depth. These models are then guided by some sort of dynamic router that figures out which model ought to be used based on your query. This is a great potential advance in usability if it works well, but leaves confusion about how the four ways of advancing AI progress are going.

Unfortunately, if you were hoping that GPT-5 would contain the answers that help us answer fundamental questions about AI progress, we really didn’t get much information. As a data point, GPT-5 confirmed all the pre-existing trends, suggesting that AI progress is moving [exactly as fast as I thought before](https://peterwildeford.substack.com/p/forecaster-reacts-metrs-bombshell) (median AGI arrival date of 2033). GPT-5 is neither a disappointment calling for us to think AI progress is slower nor an excitement that suggests we should really speed up our timelines.

**What GPT-5 does do is rule out that RL scaling can unfold rapidly and that we can get very rapid AI progress as a result.** It was thought at the end of December that the demo of o3 was an indication that reasoning models might be capable of taking off quickly and that we could get lightning fast AI progress over 2025. The slow rollout of o3 for public use suggested there were barriers to that. If ultrafast scaling was true, GPT-5 should have leapt. It didn’t — which weighs strongly against that hypothesis.

But many questions are still unanswered. For example, **I’m still confused about whether good old-fashioned pre-training is dead.** GPT-4.5 was widely seen as a disappointment given that it did not improve upon the state of the art, but it wasn’t meant to, as it wasn’t a reasoning model like o1 that made good use of the other three ways to scale AI models. I was always curious to see what GPT-4.5’s power as a base model could be if it was given reasoning capabilities and I had hoped GPT-5 might be that demonstration. Instead, based on the speed of response, it seems that GPT-5 is actually not be using GPT-4.5 as a base model but instead something smaller and faster (probably 4o or 4.1). This is curious — either OpenAI wanted to forgo the ability of 4.5 for speed or having 4.5 as the base model is not helpful. If the latter, that is a strong suggestion that base model good old-fashioned pre-training scaling is no longer giving sufficient returns.

**I’m also confused about the returns to scaling post-training reinforcement learning and inference-time compute.** We can see nicely how GPT-5 is making small incremental improvements in math, science, and software but will these improvements continue with more work on post-training reinforcement learning and inference-time compute? Could OpenAI just finish building Stargate, crank the numbers on all four ways of scaling by 10x, output GPT-6, and see strong returns? We don’t yet know. More importantly, how well does this reinforcement learning paradigm — which focuses mainly on easily verifiable domains — generalize to much harder to verify domains like writing, research, and analysis? So far, my experience is that the quality of writing actually goes *down* when GPT-5 thinks *more*, which is an interesting trade off. Unfortunately we do not have good evals for these sorts of things, and I’d like to see more. Does GPT-5 improve on [playing Pokémon](https://peterwildeford.substack.com/p/agi-by-2030-what-policy-leaders-tech)? Is GPT-5 better at writing good Substack articles? How much closer is GPT-5 at automating a variety of current professional work? We don’t really have any new information.

**I’m also confused about how advances in AI computer use are going.** When will we get AI agents that can successfully do a variety of personal assistant tasks for you, such as booking flights and hotels largely autonomously or doing budgeting? This seems potentially a matter of both increasing capabilities and intelligence across the model but also in scaffolding by helping the model more. Despite OpenAI Operator’s launch in January and then Agent last month, the progress here still feels underwhelming. Will GPT-5 be better able to use a computer than its predecessors? So far we don’t know but my guess is given how this emphatically was not part of any demos or marketing for the GPT-5 product that the advances are not yet in.

### Delivering for the people instead of the AI elites

**Instead, what might be the case with GPT-5 is that they are delivering less for the elite user — the AI connoisseur ‘high taste tester’ elite — and more for the common user.** Recall that 98% of people who use ChatGPT use it for free[4](https://peterwildeford.substack.com/p/gpt-5-a-small-step-for-intelligence#footnote-4-170321649). All of these users will now get a more powerful base model to experience (though unfortunately it seems that the free tier does not engage in extended thinking[5](https://peterwildeford.substack.com/p/gpt-5-a-small-step-for-intelligence#footnote-5-170321649)).

And the model they get will be much easier to use — you just use “GPT-5” and you don’t have to worry about “4o” versus “o4” which are apparently completely different things, the model will just figure out the reasoning or not for you and pair you with the model that best suits your needs[6](https://peterwildeford.substack.com/p/gpt-5-a-small-step-for-intelligence#footnote-6-170321649). The [hallucination rate is notably decreased](https://x.com/polynoamial/status/1953517966978322545). The model now engages in [notably less deception](https://x.com/GarrisonLovely/status/1953526287873847331) than [the o3 model that told a lot of lies](https://peterwildeford.substack.com/p/weekend-links-12-o3-is-smart-but). The writing quality feels better than before. It’s ultra fast at responding — easily the fastest model on the market now. The model still generates images, so you can still ghiblify on demand.

**Sure GPT-5 may not deliver the next generation of intelligence, but does that matter compared to the next generation of value to the typical consumer?** The honest truth is models are smart enough for a lot of use cases — speed, cost, and reliability is a bigger bottleneck for a lot of enterprise AI use cases than intelligence. GPT-5 is delivering where it matters.

You can see this in the revenue stats. While ‘timelines to AGI’ may have revised downward somewhat over 2025, the amount of revenue AI companies are projected to make have revised upward a lot over the same time period. Entering 2025, OpenAI + Anthropic + xAI were projecting a combined ~$17B of annualized revenue as of the end of 2025[7](https://peterwildeford.substack.com/p/gpt-5-a-small-step-for-intelligence#footnote-7-170321649). Now [my forecast is almost twice that](https://x.com/peterwildeford/status/1952438385437753751/) at expecting a combined $32B annualized revenue at the end of 2025. The OpenAI valuation was [$157B at the end of 2024](https://www.cnbc.com/2024/10/02/openai-raises-at-157-billion-valuation-microsoft-nvidia-join-round.html) and [now potentially is $500B](https://www.reuters.com/business/openai-eyes-500-billion-valuation-potential-employee-share-sale-source-says-2025-08-06/) just eight months later. GPT-5 will presumably take this to new heights. **Who cares how the model does on benchmarks if it makes bank?**

GPT-5 is not the GPT moment we once expected — it’s not even the o1 moment. Instead, OpenAI is doubling down on speed, usability, and revenue. Intelligence progress continues on predictable trendlines but GPT-5 delivers on the bottlenecks for most real-world use cases — cost, latency, and reliability.

The AI elites may keep waiting for fireworks but for 98%+ of actual users, GPT-5 is the best ChatGPT yet.

Want more analysis of GPT-5 and the next big model? Subscribe!

Subscribe

[1](https://peterwildeford.substack.com/p/gpt-5-a-small-step-for-intelligence#footnote-anchor-1-170321649)

Based on the reception to GPT-5, I think it would’ve made the most sense for “o1” to have just been GPT-5 — it seemed the closest to a true ‘paradigm shift’ like GPT-3 and GPT-4.

[2](https://peterwildeford.substack.com/p/gpt-5-a-small-step-for-intelligence#footnote-anchor-2-170321649)

In particular, my model predicted that METR would find a time horizon of 2hrs54min at 50% reliability (90% CI: 1.4hr - 4.4hr). The actual observation was 2hrs17min (with a range of 1hr-4.5hrs), which matches well within the margin of sampling error.

[3](https://peterwildeford.substack.com/p/gpt-5-a-small-step-for-intelligence#footnote-anchor-3-170321649)

I don’t know why it’s called pre-traning, since it definitely *is* the training, not *before* it.

[4](https://peterwildeford.substack.com/p/gpt-5-a-small-step-for-intelligence#footnote-anchor-4-170321649)

[ChatGPT has 700 million weekly active users](https://www.cnbc.com/2025/08/07/openai-launches-gpt-5-model-for-all-chatgpt-users.html). Of these, there are: [10-12 million ChatGPT Plus subscribers](https://backlinko.com/chatgpt-stats) ($20/month tier), [1-1.5 million enterprise/team/edu customers](https://backlinko.com/chatgpt-stats), and a much smaller fraction on the Pro tier ($200/month). This means there are roughly 12-14 million paying users out of 700 million weekly active users, which suggests ~98% free users.

[5](https://peterwildeford.substack.com/p/gpt-5-a-small-step-for-intelligence#footnote-anchor-5-170321649)

Also the free tier does downgrade to a ‘mini’ version eventually, which [can create some confusion](https://x.com/emollick/status/1953638367415218596) if you think you’re still getting top-tier thinking.

[6](https://peterwildeford.substack.com/p/gpt-5-a-small-step-for-intelligence#footnote-anchor-6-170321649)

Though elite AI power users will likely still want to tune the thinking time manually and also still decide between when to use ChatGPT vs. Claude vs. Gemini vs. Grok. The era of ‘thinkfluencer’ model picker charts are not over!

[7](https://peterwildeford.substack.com/p/gpt-5-a-small-step-for-intelligence#footnote-anchor-7-170321649)

Estimating the total December 2025 revenue for Anthropic + OpenAI + xAI multiplied by 12 (annualized revenue), as per [this Metaculus question](https://www.metaculus.com/questions/30756/what-will-be-the-sum-of-openai-anthropic-and-xais-publicly-reported-annualized-revenues-by-december-31st-2025-in-usd-billions/). Google DeepMind and Meta are excluded from this due to lack of reliable revenue data.