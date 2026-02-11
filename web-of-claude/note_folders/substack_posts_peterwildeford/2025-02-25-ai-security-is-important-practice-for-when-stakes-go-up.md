# AI security is important practice for when stakes go up

*Why today's safeguards matter for future AI capabilities*

Published: 2025-02-25
Source: https://peterwildeford.substack.com/p/ai-security-is-important-practice

---

[![](https://substackcdn.com/image/fetch/$s_!YjDM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe6d0e29e-4c0b-4ca8-b725-5714d76d52b7_1536x1164.png)](https://substackcdn.com/image/fetch/$s_!YjDM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe6d0e29e-4c0b-4ca8-b725-5714d76d52b7_1536x1164.png)

The latest Grok 3 model from xAI recently demonstrated a concerning capability: [generating detailed instructions for chemical weapons production](https://x.com/LinusEkenstam/status/1893832876581380280)[1](https://peterwildeford.substack.com/p/ai-security-is-important-practice#footnote-1-156669555), complete with supplier lists and workarounds for regulatory controls.

While this incident isn't cause for immediate alarm, it serves as a crucial wake-up call for the broader challenges of AI security. Currently, a lot of this information can already be found scattered around the internet, and Grok 3’s plans likely aren’t detailed enough to actually fill in all the gaps in the complex task of assembling and deploying these weapons without detection[2](https://peterwildeford.substack.com/p/ai-security-is-important-practice#footnote-2-156669555). And [it sounds like xAI is taking this incident seriously](https://x.com/LinusEkenstam/status/1893988847320531236) and updating their AI security guidelines, so hopefully this will be an example of how good external red teaming leads to better security outcomes.

**But here's the thing: we're currently in a practice round for when AI becomes genuinely dangerous. It’s important to quickly start getting things right.** The consequences of getting this wrong right now are minimal, but if AI companies are right about AIs becoming rapidly more capable, we will need to make sure security goes up to match.

## AI is getting more capable

It’s not just the biosafety domain where there are possible future concerns. Google's Project Zero [found AI could discover](https://googleprojectzero.blogspot.com/2024/10/from-naptime-to-big-sleep.html) a novel [zero-day vulnerability](https://en.wikipedia.org/wiki/Zero-day_vulnerability) in a widely-used open source project that had previously been undiscovered by humans despite significant effort to identify vulnerabilities. While it matters that the “good guys” found this first, we cannot rely on this. A hostile nation could use AI to rapidly find vulnerabilities in power grids, voting systems, or military networks.

And we certainly know that AI is rapidly improving. [MMLU](https://arxiv.org/abs/2009.03300), a test for AIs of knowledge across 57 subjects, started in 2021 with scores far below human experts. Today, MMLU involves AI scoring at levels matching human experts.

Fed up by MMLU being too easy, David Rein et. al. developed [GPQA](https://arxiv.org/abs/2311.12022), which stands for “Google Proof Q&A”, a quiz of science questions in biology, physics, and chemistry designed to be so hard that it can only be answered with significant domain expertise and cannot be solved even by Google searching. PhD experts typically score only 80% on questions *within their own field* **and non-experts even with full web access barely exceed 30% accuracy.** In short, if you see an AI answer GPQA correctly, it means the system is handling extremely challenging “Google-proof” problems that require genuine deep reasoning rather than surface-level lookup.

In July 2023, [according to data from EpochAI](https://epoch.ai/data/ai-benchmarking-dashboard), GPT-4 was able to get about 30% on this test, matching non-experts. But a mere 18 months later, AI systems like OpenAI o1 already perform — and possibly exceed — expert human level.

[![](https://substackcdn.com/image/fetch/$s_!72tL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd348b2aa-6f2a-4d80-86c8-80ab9e1fa30f_2002x1706.png)](https://substackcdn.com/image/fetch/$s_!72tL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd348b2aa-6f2a-4d80-86c8-80ab9e1fa30f_2002x1706.png)

Notably, these improvements in expertise span not only math and humanities, but also complex topics like virology and hacking.

And this is just the beginning. Combined with major companies announcing large AI investments ([Stargate $100B/yr](https://openai.com/index/announcing-the-stargate-project/), [Microsoft $80B/yr](https://blogs.microsoft.com/on-the-issues/2025/01/03/the-golden-opportunity-for-american-ai/), [Amazon $100B/yr](https://www.cnbc.com/2025/02/06/amazon-expects-to-spend-100-billion-on-capital-expenditures-in-2025.html), [Google $75B/yr](https://www.reuters.com/technology/google-parent-alphabet-misses-quarterly-revenue-estimates-2025-02-04/), and [Meta at $65B/yr](https://www.facebook.com/zuck/posts/pfbid0219ude255AKkmk4JAueXZeZ9zpjNYio2tBkd7bNmCaRbJ6iJaVVjypUgDg78CNdq5l)), we will continue to see strong improvements out of future models.

## Where this might go next

Anthropic recently introduced their ['AI Safety Levels' (ASL) framework](https://www.anthropic.com/news/anthropics-responsible-scaling-policy) — a classification system that categorizes risks from AI models based on AI capabilities. In their latest [Claude 3.7 model system card](https://assets.anthropic.com/m/785e231869ea8b3b/original/claude-3-7-sonnet-system-card.pdf), Anthropic stated that their next model has “a substantial probability” of meeting [their “ASL-3” threshold](https://www.anthropic.com/news/anthropics-responsible-scaling-policy).

What does ASL-3 actually mean? All of today’s models, including Claude 3.7 and Grok 3, are “ASL-2”, which means they might help with isolated harmful tasks. ASL-3 is the next big step up — models that substantially increase catastrophic misuse risk. In practical terms, Anthropic says that ASL-3 systems will be advanced enough to potentially enable highly sophisticated cyberattacks, automate complex parts of bioweapon development, or facilitate other activities that could cause large-scale harm. ASL-3 systems could effectively help threat actors coordinate across multiple domains to overcome existing security barriers in a way that current models cannot.

No currently deployed commercial AI system has reached ASL-3 status, according to Anthropic's assessment. However, the timeline for crossing this threshold appears to be accelerating - from “years away” in previous assessments to “the next model” in current projections.

This means that **at some point in the not too distant future, advanced AIs may become capable of giving instructions for a bioweapon.** This may provide would-be terrorists a step-by-step plan plus custom troubleshooting support, allowing them to get much further than if they had to learn on their own. It would be the difference between being able to consult a variety of textbooks on a problem and having an on-call tutor. Once we get to this level of capabilities, we need to be ready for there to be a much larger number of threat actors that can do large-scale harm, and be capable of containing the danger while still allowing the positive aspects of AI to go forward unhindered.

## What we can do now

**We’re lucky right now to be playing on an “AI safety” tutorial level with real but manageable stakes.** Beyond the immediate concerns about terrorism, this challenge has broader implications. The AI security challenge isn't just about safety — it's fundamentally about American leadership and national security. While the US currently maintains a competitive edge in AI development, China's military-civil fusion strategy has explicitly targeted AI as a domain for strategic advantage. China and North Korea could attempt to steal or hack American AI and use it to threaten the US, and we need to be ready.

Companies like Anthropic and OpenAI have been rising to this challenge, implementing increasingly sophisticated red-teaming protocols and testing frameworks to contain exploits before deployment. Additionally, techniques like [Constitutional AI](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback) and [Deliberative Alignment](https://openai.com/index/deliberative-alignment/) have shown some effectiveness in reducing the possibility of harmful outputs without sacrificing model performance. However, we need to be careful to ensure that these protocols are strong enough to withstand people who would seek to use AIs to do large-scale harm, and that other companies like xAI and DeepSeek are developing similar protocols. And we need security to be more robust to all the various ways models can be broken, stolen, or hijacked. We will only be as secure as the weakest link and there are still a lot of weak links we don’t know how to protect.

According to Anthropic, “ASL-3” models require stronger safeguards than we have today — robust misuse prevention and enhanced security. More R&D and investment will be needed to build these. This can be done with a pragmatic approach that leverages America's private sector innovation, further developing industry standards and norms with targeted government coordination. We will need stronger norms and stronger investments in safety, or it’s possible that capabilities could outmatch our abilities to properly safeguard them. This isn't about restricting technology — it's about hardening our systems against potential exploitation by adversaries.

**The bottom line is that ASL-3 represents a critical threshold where AI safety shifts from being primarily a corporate responsibility to becoming a legitimate national security concern.** At this level, the security protocols developed by individual companies may no longer be sufficient without increased coordination between industry and government.

To be clear, current AI is definitely far from an existential threat. But treating it like one might be exactly what we need to become ready. The real question isn't whether today's AI is dangerous — it's whether we're using this practice round effectively enough to be ready for what comes next.

Want more news about trends in AI? Subscribe!

Subscribe

[1](https://peterwildeford.substack.com/p/ai-security-is-important-practice#footnote-anchor-1-156669555)

The original tweet mentions “chemical weapons production” but from context this tweet seems to be about botulism. This is a biotoxin, not a chemical weapon, and is easily available online. However, I will keep with calling this a chemical weapon given that is what the original tweet states.

[2](https://peterwildeford.substack.com/p/ai-security-is-important-practice#footnote-anchor-2-156669555)

Grok 3 isn’t an imminent threat but I must admit it isn’t perfectly clear whether it is able to provide an “uplift” (or increase in ability) to a threat actor relative to existing 2023-era resources (e.g., Google and textbooks). This isn’t a clear binary and some of it depends on the identity of the threat actor and their existing knowledge. But also the precise testing on this is not provided by xAI. Currently, I am considering Grok 3 to not provide non-trivial uplift as Anthropic did not place the ASL-3 designation on Claude 3.7, and I would think Grok 3 and Claude 3.7 are of comparable ability.