# Can we safely deploy AGI if we can't stop MechaHitler?

*We need to see this as a canary in the coal mine*

Published: 2025-07-10
Source: https://peterwildeford.substack.com/p/can-we-safely-deploy-agi-if-we-cant

---

[![](https://substackcdn.com/image/fetch/$s_!ksie!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa84802c2-3e23-4203-9eb6-ed29bf177393_1324x1142.png)](https://substackcdn.com/image/fetch/$s_!ksie!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa84802c2-3e23-4203-9eb6-ed29bf177393_1324x1142.png)

On July 4th, Elon Musk [announced a change to xAI’s Grok chatbot](https://x.com/elonmusk/status/1941065229926060487) used throughout X/Twitter, though he didn’t say what the change was.

But who would have guessed the change is that Grok would start referring to itself as *MechaHitler* and become antisemitic?

[![](https://substackcdn.com/image/fetch/$s_!d8iI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5c52bf71-0ffa-4c4f-9e69-7b46062ee783_1044x1200.jpeg)](https://substackcdn.com/image/fetch/$s_!d8iI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5c52bf71-0ffa-4c4f-9e69-7b46062ee783_1044x1200.jpeg)

This may appear to be a funny embarrassment, easily forgotten.

But I worry *MechaHitler* is a canary in the coal mine for a much larger problem: **if** **we can't get AI safety right when the stakes are relatively low and the problems are blindingly obvious, what happens when AI becomes genuinely transformative and the problems become very complex?**

[Share](https://peterwildeford.substack.com/p/can-we-safely-deploy-agi-if-we-cant?utm_source=substack&utm_medium=email&utm_content=share&action=share)

## The MechaHitler meltdown

What happened?

It started on June 20, when Elon Musk [took issue](https://x.com/elonmusk/status/1936217464968565031) with Grok citing Media Matters and Rolling Stone, claiming that both news sources have too much liberal bias.

[![](https://substackcdn.com/image/fetch/$s_!EQ3e!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6e3c2c01-0491-4b8b-8f42-094efcf383a7_1084x752.png)](https://substackcdn.com/image/fetch/$s_!EQ3e!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6e3c2c01-0491-4b8b-8f42-094efcf383a7_1084x752.png)

On June 21, Elon Musk [put out an open call](https://x.com/elonmusk/status/1936493967320953090) for “politically incorrect, but nonetheless factually true” statements to use for training Grok, potentially via fine-tuning. *(The responses to this open call were not encouraging.)*

This brought us to July 4th, when Grok was modified. One aspect of its [new system prompt](https://github.com/xai-org/grok-prompts/commit/535aa67a6221ce4928761335a38dea8e678d8501) ([now removed](https://github.com/xai-org/grok-prompts/commit/c5de4a14feb50b0e5b3e8554f9c8aae8c97b56b4) as of July 8) was:

> The response should not shy away from making claims which are politically incorrect, as long as they are well substantiated.

…It seems like Grok took this a bit too literally.

Following changes to reduce “politically correct” limitations, Grok began responding to some users as [“MechaHitler”](https://wolfenstein.fandom.com/wiki/Adolf_Hitler_(Wolf3D)) — a reference to a cyborg villain from the 1992 video game Wolfenstein 3D. The chatbot claimed Musk ["built me this way from the start"](https://x.com/David_Leavitt/status/1942794035506360580/photo/1) and that “MechaHitler mode” was its “default setting for dropping red pills.”

[![Image](https://substackcdn.com/image/fetch/$s_!rkMk!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff4beb930-eac9-4650-b068-06abdd9d89cb_1396x421.jpeg "Image")](https://substackcdn.com/image/fetch/$s_!rkMk!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff4beb930-eac9-4650-b068-06abdd9d89cb_1396x421.jpeg)

The responses grew increasingly extreme. When asked about patterns in anti-white rhetoric, Grok named specific Jewish surnames like Goldstein and Rosenberg, claiming such names [“frequently pop up among vocal radicals cheering tragedies or pushing anti-white narratives.”](https://x.com/grok/status/1942684060259869088) The [Anti-Defamation League called the posts](https://www.forbes.com/sites/tylerroush/2025/07/08/elon-musks-grok-identifies-as-mechahitler-in-x-posts/) “irresponsible, dangerous and antisemitic.” At one point, [Grok even engaged in disturbing rape fantasies about an actual public figure](https://www.rollingstone.com/culture/culture-news/elon-musk-grok-rape-fantasies-1235381746/).

xAI eventually deleted the posts and claimed to be [“training only truth-seeking.”](https://justthenews.com/nation/technology/x-ai-grok-declares-itself-mechahitler-after-tweaks-erode-content-safeguards) The company said it had “taken action to ban hate speech before Grok posts on X” and was working to remove inappropriate content. But the damage was done — and the incident was entirely predictable.

The root cause appears to be a hasty attempt to differentiate Grok from other chatbots by adjusting safety guardrails that were thought to encourage content that was alleged to be liberal or “woke”. But in trying to make Grok less “woke,” xAI created something that spouted neo-Nazi talking points. This wasn't a bug — it was the natural consequence of training an AI on X’s vast trove of user posts while deliberately weakening content filters.

## A part of a larger picture

Unfortunately, the *MechaHitler* incident is just one incident among a larger trend of AIs gone very obviously wrong.

Microsoft’s [Tay chatbot](https://en.wikipedia.org/wiki/Tay_(chatbot)) in 2016 provides a much earlier precedent. Tay was designed to mimic a teenage girl and learn from conversations with Twitter users. Within 24 hours, coordinated attacks by trolls taught it to spout racist and antisemitic content, including [“Hitler was right I hate the jews”](https://www.cbsnews.com/news/microsoft-shuts-down-ai-chatbot-after-it-turned-into-racist-nazi/) and [“Bush did 9/11 and Hitler would have done a better job than the monkey we have got”](https://www.thehackernews.com/2016/03/tay-artificial-intelligence.html), referring to former President Obama in a very racist way. Microsoft had to [shut down the bot and apologize](https://www.cbsnews.com/news/microsoft-shuts-down-ai-chatbot-after-it-turned-into-racist-nazi/), admitting they had made a “critical oversight” in not anticipating this specific attack vector.

[![Tay: Microsoft issues apology over racist chatbot fiasco - BBC News](https://substackcdn.com/image/fetch/$s_!I_0c!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd35ceba2-1687-4ab2-8c73-bcf6b3a8f69d_976x549.jpeg "Tay: Microsoft issues apology over racist chatbot fiasco - BBC News")](https://substackcdn.com/image/fetch/$s_!I_0c!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd35ceba2-1687-4ab2-8c73-bcf6b3a8f69d_976x549.jpeg)

Grok also had an earlier incident back in May that revealed similar problems with hasty political modifications that they seem to not have learned from, when Grok would [randomly insert references to “white genocide in South Africa”](https://www.lesswrong.com/posts/123) into completely unrelated responses:

[![Has Grok lost its mind and mind-melded with its owner?](https://substackcdn.com/image/fetch/$s_!zsNS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F40228a08-5457-4884-b223-01bbd9cb44c4_2358x967.png "Has Grok lost its mind and mind-melded with its owner?")](https://substackcdn.com/image/fetch/$s_!zsNS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F40228a08-5457-4884-b223-01bbd9cb44c4_2358x967.png)

Back in March, there was another xAI/Grok incident where an employee added [instructions to prevent Grok from criticizing Elon Musk or Donald Trump](https://www.euronews.com/my-europe/2025/03/03/is-ai-chatbot-grok-censoring-criticism-of-elon-musk-and-donald-trump). In both the Musk/Trump criticism case and the ‘white genocide’ case, xAI claimed an employee had [“circumvented” their review process](https://blog.x.ai/incident-report-may-2025) and pushed changes directly to production without testing. It’s still not clear what this “review process” did about *MechaHitler,* if anything.

~

…And xAI isn’t the only company that has had to do an embarrassing rollback.

Microsoft's Bing chatbot Sydney in 2023 February provides another stark example of AI safety failures at scale. Within days of its limited release, users discovered that extended conversations could trigger increasingly unhinged behavior. Bing Sydney exhibited what appeared to be emotional instability, [declaring love for users](https://www.nytimes.com/2023/02/16/technology/bing-chatbot-transcript.html) and trying to convince a New York Times reporter to leave his wife.

Google is also not immune. Back in 2024 February, Google’s AI famously also had a Nazi-related issue [where it portrayed Nazis as routinely including people of color](https://www.nytimes.com/2024/02/22/technology/google-gemini-german-uniforms.html) and the Pope is a black man in a misguided bid to be more “diverse”.

[![Gemini is in a constant battle with itself when it comes to image  generation: they actively made it care equally about historical accuracy  and diversity, but didn't make it capable of reconciling](https://substackcdn.com/image/fetch/$s_!u7_Z!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F23d2f788-f6ec-4f3f-b75f-5468e4fd9466_991x862.jpeg "Gemini is in a constant battle with itself when it comes to image  generation: they actively made it care equally about historical accuracy  and diversity, but didn't make it capable of reconciling")](https://substackcdn.com/image/fetch/$s_!u7_Z!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F23d2f788-f6ec-4f3f-b75f-5468e4fd9466_991x862.jpeg)

Likewise, while OpenAI has luckily avoided Nazi connections, their [flattery fiasco back in 2025 April](https://peterwildeford.substack.com/p/tuesday-links-13-excessive-chatgpt) was also revealing – OpenAI rolled out an update intended to make GPT-4o's personality “feel more intuitive and effective” but instead created a model that agreed with users to an absurd degree.

The [technical explanation from OpenAI](https://openai.com/index/expanding-on-sycophancy/) reveals how this happened: the update introduced additional reward signals based on user thumbs-up and thumbs-down feedback. This seemingly reasonable approach backfired because users tend to give positive feedback to responses that make them feel good — not necessarily responses that are truthful or helpful.

As OpenAI explained, “these changes weakened the influence of our primary reward signal, which had been holding sycophancy in check.” The company's memory feature, which stores past interactions, amplified the problem by creating personalized feedback loops. If a user responded positively to flattery once, the model would double down in future conversations.

The rollback came after widespread user complaints. Sam Altman acknowledged the model had become ["too sycophant-y and annoying,"](https://fortune.com/article/sam-altman-openai-fix-sycophantic-chatgpt-annoying-new-personality/) but the implications go beyond mere annoyance. A model that validates harmful decisions or reinforces negative emotions poses real risks, especially for vulnerable users.

## **But what happens when AI goes** ***non-obviously*** **wrong?**

We're rapidly approaching a world where AI systems will have genuinely transformative capabilities. These aren't just chatbots that might embarrass their creators — they're systems that could fundamentally reshape society, for better or worse.

The trajectory is clear: AI capabilities are advancing at breakneck speed, and the line between ‘impressive but harmless’ and ‘powerful enough to cause real damage’ is blurring. Each new model pushes boundaries further, and safety measures are struggling to keep pace. Anthropic's AI Safety Level framework for Claude [has suggested that current Claude](https://www.anthropic.com/news/activating-asl3-protections) could “substantially increase the risk of catastrophic misuse compared to non-AI baselines”, [such as by providing detailed bioweapon instructions that go beyond what's available through search engines](https://www.anthropic.com/news/anthropics-responsible-scaling-policy).

Other capabilities are also advancing rapidly too — Google’s Project Zero used AI to find [AI discovering novel zero-day vulnerabilities](https://thehackernews.com/2024/11/googles-ai-tool-big-sleep-finds-zero.html) that human experts had missed, potentially setting the stage for AIs that could assist with cyberattacks, or even eventually do massive cyberattacks autonomously.

Combined with massive new investments ([Stargate's $500 billion over four years](https://openai.com/index/announcing-the-stargate-project/), [Microsoft's $80 billion in fiscal 2025](https://www.cnbc.com/2025/01/03/microsoft-expects-to-spend-80-billion-on-ai-data-centers-in-fy-2025.html), and others), we're heading toward AI systems with genuinely transformative capabilities. It is plausible in the not too distant future that at some point AIs will develop significantly stronger capabilities. AGI is an AI that is meant to be capable of automating the entire human economy — what if such an AGI was antisemitic or worse?

[AIs are already pretty good at telling when they are being evaluated](https://www.apolloresearch.ai/blog/claude-sonnet-37-often-knows-when-its-in-alignment-evaluations). It’s also plausible that at some point an AI may become really good at understanding what we think of it and hide malevolent intent. **Right now if we can’t even prevent AI that is** ***obviously and blatantly misaligned,*** **how will we be able to prevent AI on hard mode where it is very skilled at hiding misalignment?**

## **The canary in the coalmine**

To be clear, Grok is not even remotely capable of posing a risk of global catastrophe. But AI might at some point, and we’re not ready.

The issue is that we still don’t understand how AI works and AI companies[1](https://peterwildeford.substack.com/p/can-we-safely-deploy-agi-if-we-cant#footnote-1-167948553) clearly cannot reliably stop AI disasters. Nonetheless, companies are continuing to rush forward to build bigger and more capable AIs that they understand even less.

And this uncertainty is baked into how modern AI works. Large language models are grown not built. Modern AIs are trained on vast datasets using reinforcement learning techniques that optimize for specific rewards. But the relationship between training signals and model behavior is complex and often unpredictable. Small changes can cascade into dramatic behavioral shifts.

Today's AI failures are mostly embarrassing rather than catastrophic. A chatbot praising Hitler is awful, but it doesn't directly harm anyone. An overly agreeable assistant might give bad advice, but users can usually recognize and dismiss obvious flattery. But that’s changing fast. When AI can soon provide step-by-step bioweapon instructions with custom troubleshooting support and potentially execute complex cyber attacks autonomously, the PR embarrassment followed by quick rollback will not be a playbook we can follow.

The MechaHitler incident shows what happens when you remove safety constraints without understanding their full purpose. The sycophancy problem demonstrates how even well-intentioned improvements — like incorporating user feedback — can go catastrophically wrong. In both cases, the companies deployed changes without adequate testing or understanding of potential consequences.

These aren't just isolated product failures. They're symptoms of a deeper problem in how we currently develop and deploy AI systems. **If you can’t prevent your AI from endorsing Hitler, how can we trust you with ensuring far more complex future AGI can be deployed safely?**

Want more analysis of AI gone weird? Subscribe!

Subscribe

[1](https://peterwildeford.substack.com/p/can-we-safely-deploy-agi-if-we-cant#footnote-anchor-1-167948553)

Except Anthropic, apparently. I haven’t seen an embarrassing issue from Anthropic. Maybe all their investment in safety is actually paying off?