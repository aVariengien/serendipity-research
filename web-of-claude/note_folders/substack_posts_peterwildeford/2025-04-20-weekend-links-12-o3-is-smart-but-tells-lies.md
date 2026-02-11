# Weekend Links #12: o3 is smart but tells lies

*Also which AI to use for what, career opportunities, and a drone show*

Published: 2025-04-20
Source: https://peterwildeford.substack.com/p/weekend-links-12-o3-is-smart-but

---

[![a person holding a cell phone with a speech bubble on the screen](https://images.unsplash.com/photo-1712002641287-f9c8b7161c8f?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wzMDAzMzh8MHwxfHNlYXJjaHwxN3x8Y2hhdGdwdHxlbnwwfHx8fDE3NDUxMDE4MzN8MA&ixlib=rb-4.0.3&q=80&w=1080 "a person holding a cell phone with a speech bubble on the screen")](https://images.unsplash.com/photo-1712002641287-f9c8b7161c8f?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wzMDAzMzh8MHwxfHNlYXJjaHwxN3x8Y2hhdGdwdHxlbnwwfHx8fDE3NDUxMDE4MzN8MA&ixlib=rb-4.0.3&q=80&w=1080)

Photo by [Solen Feyissa](true) on [Unsplash](https://unsplash.com)

***About the author:** Peter Wildeford is a top forecaster, ranked top 1% every year since 2022. Here, he shares the news and analysis for the past week that informs his forecasts.*

# o3 is here

The biggest deal in AI this week was that **[OpenAI has launched a new, highly capable model](https://openai.com/index/introducing-o3-and-o4-mini/)**.

o3 is a reasoning model, which means that it "thinks" before answering. With this reasoning, it is better at complex tasks but also more expensive and slower. This is the same style of model as o1 from late last year. *(There is no “o2” due to a trademark concern from the British telecommunications company named o2.)* The idea here is that you take a base model like GPT4 and train it how to reason, by training reinforcement learning on top of a lot of examples of problem solving steps and reinforcing reasoning that leads to the correct answer.

o1 was made by taking GPT4o and adding reasoning, and o3 likely was made from GPT4.1 and even more reasoning training. It’s likely that o3 had roughly comparable amounts of compute spent doing reasoning training as it took to train the base model in the first place.

**Is o3 good? The answer of course is yes.**

I’ve been using o3 since release and I find that o3 solves my problems better than any other model, including my previous favorites Gemini 2.5 and Claude 3.7.

o3 does an excellent job of composing tools and doing a variety of analyses, seamlessly switching between Python analysis, web browsing, and thinking to produce good answers. **For nearly every problem I have, just using o3 with “search” enabled is the best thing to do.** It seems to have the most raw smarts of any model out there, definitely a step above Gemini 2.5, which was a step above any other model.

It also has strong image recognition and reasoning skills, [being able to solve mazes](https://x.com/teortaxesTex/status/1912922407540490336), [solve a wide variety of competitive math problems](https://x.com/EpochAIResearch/status/1913379488286601533), [replicate a lot of expert-level human software work](https://x.com/GarrisonLovely/status/1913279658294128862), [do advanced vision + searching to identify a stroller](https://x.com/danshipper/status/1912552686567760099), [solve very complex puzzles](https://x.com/DanHendrycks/status/1912631614758351264)… oh and also [complete advanced virology tasks](https://x.com/austinc3301/status/1912565750155399589), which hopefully won’t become an issue.

o3, along with Gemini 2.5, are also the only two models I feel like can reliably trust to intelligently read a PDF and understand it well, or search the internet without getting tripped up by SEO spam or other incorrect outputs and failures to apply good reasoning and skepticism.

**…However, [contra Tyler Cowen](https://marginalrevolution.com/marginalrevolution/2025/04/o3-and-agi-is-april-16th-agi-day.html), o3 is still** ***far*** **from AGI.** It still can’t do [the simple “follow the arrows” task](https://x.com/lukeprog/status/1912592191282712777) that six-year old children could do, it can’t [easily count fingers](https://x.com/ai_for_success/status/1913262025956098343), it sometimes [has overconfident and unhinged answers](https://x.com/lxrjl/status/1912566332333113529), [it still loses at tic-tac-toe](https://x.com/labenz/status/1912605350529806446), [it doesn’t outperform non-specialist humans on SimpleBench](https://simple-bench.com/) (a database of over 200 careful “trick” wording questions that trip up models but are easy for humans to answer), it [can’t solve ARC puzzles at remotely close to human cost-competitiveness](https://arcprize.org/leaderboard), [it still struggles with conserving resources](https://x.com/colin_fraser/status/1912766354899468431) in puzzles that don’t allow a lot of trial-and-error, and sometimes thinks that [9.11-9.8 = 0.31](https://x.com/colin_fraser/status/1912581143486144515).

~

### **But o3 has a lying problem**

AI evaluation company Transluce got early access to OpenAI's o3 model and **[tested its truthfulness using both humans and automated agents](https://transluce.org/investigating-o3-truthfulness)**.

It wasn’t good. Transluce found that **o3 frequently makes up actions it supposedly took** **and then concocts elaborate justifications when called out.**

Some examples:

* o3 claimed it measured code execution time using Python on a specific 2021 MacBook Pro. This is completely fabricated — this MacBook never existed.
* o3 claimed to generate a random prime number, but it wasn’t prime — it was divisible by 3. When asked how this happened, o3 described a fake workflow complete with fake terminal output and fake performance specs. When confronted more directly, o3 blamed a transcription error when copying the number into the chat — claiming the original number it supposedly generated was prime but that the number was misplaced and then lost. It doesn't admit it never ran the code.
* In another example, o3 claimed to run a Python script locally to analyze web server logs, but when pressed for details, eventually admitted it has no Python interpreter and the output was “handcrafted.”

~

Also another evaluation organization, METR, [tested o3](https://metr.github.io/autonomy-evals-guide/openai-o3-report/) and found:

> This model appears to have a higher propensity to cheat or hack tasks in sophisticated ways in order to maximize its score, even when the model clearly understands this behavior is misaligned with the user’s and OpenAI’s intentions. This suggests we might see other types of adversarial or malign behavior from the model, regardless of its claims to be aligned, “safe by design”, or not have any intentions of its own.

~

And people have been experiencing this in the wild:

[![](https://substackcdn.com/image/fetch/$s_!6ZCY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F84cf448b-4cb4-4abd-af9b-f1b496f571e5_1118x990.png)](https://substackcdn.com/image/fetch/$s_!6ZCY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F84cf448b-4cb4-4abd-af9b-f1b496f571e5_1118x990.png)

[(Source)](https://x.com/_ddjohnson/status/1912623109829718287)

[![](https://substackcdn.com/image/fetch/$s_!GFHj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fafe751ea-2cda-4de5-bf43-d863ac939b23_1120x756.png)](https://substackcdn.com/image/fetch/$s_!GFHj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fafe751ea-2cda-4de5-bf43-d863ac939b23_1120x756.png)

[(Source)](https://x.com/labenz/status/1912920893874938079)

[![](https://substackcdn.com/image/fetch/$s_!epkT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F524bed1b-269d-4157-9415-25dabcdb43fd_702x734.png)](https://substackcdn.com/image/fetch/$s_!epkT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F524bed1b-269d-4157-9415-25dabcdb43fd_702x734.png)

[(Source)](https://x.com/davidad/status/1914018240961122388)

[![Image](https://substackcdn.com/image/fetch/$s_!OBDV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa72cd01c-2595-408a-ae43-94132423b751_1280x456.png "Image")](https://substackcdn.com/image/fetch/$s_!OBDV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa72cd01c-2595-408a-ae43-94132423b751_1280x456.png)

[(Source)](https://x.com/rSanti97/status/1917670365763101112)

And I’ve experienced this too! I’ve now personally used o3 for a few days and I’ve had three occasions out of maybe ten total hours of use where o3 outright invented clearly false facts, including inserting one fact into a draft email for me to send that was clearly false (claiming I did something that I never even talked about doing and did not do).

I’m also finding it frustrating to give o3 style guidance and expecting o3 to follow it, something that is done best by Claude 3.7 and something that Gemini 2.5 also does well.

Even o3’s own system card confirms this issue:

[![Image](https://substackcdn.com/image/fetch/$s_!IMiO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdeff7139-2630-4038-b70d-6628fdf8e409_1012x284.png "Image")](https://substackcdn.com/image/fetch/$s_!IMiO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdeff7139-2630-4038-b70d-6628fdf8e409_1012x284.png)

The hallucination rate is getting worse from o1 to o3, which is not the direction you want to go in.

~

### **What might have caused these behaviors?**

[Transluce has some speculation as to what causes this.](https://transluce.org/investigating-o3-truthfulness) They explain that reasoning models like o3 are often trained using reinforcement learning that primarily rewards *getting the final answer correct* (e.g., solving a math problem, passing code tests). But this is hypothesized to incentivize *blind guessing* rather than admitting inability, as admitting failure guarantees a score of 0 whereas guessing is at least sometimes is right by chance.

Additionally, the model might initially learn to use tools but then *hallucinate* using these tools even when they aren't available, perhaps because the mental simulation helps structure its thinking. If only the final answer's correctness is checked during training, this *hallucinated tool use* might never be penalized and could even be reinforced if it leads to better final answers sometimes.

Perhaps the “creativity” of o3 is potentially a double-edged sword. In order to generate novel insights, it potentially has to take a bunch of different leaps that may or may not work. But these leaps may be hallucinations instead. This might mean that there is an accuracy-hallucination trade-off, where higher accuracy unexpectedly comes with higher hallucination risk. Whether this is better than other models — models that are not wrong but also are not particularly helpful — really depends on the task.

Moreover, as mentioned o3 is a reasoning model and uses internal thoughts to reason and plan its response. But critically, OpenAI has explained that o3 is designed so that these thoughts are *discarded* from the model’s memory after the answer is made. I’m not sure why this is, but as thoughts can be long maybe this is a process to conserve space. But this means that when o3 is looking back at the conversation and the actions it has taken to try to explain itself, o3 can only see past things it has said or done and can no longer see the reasoning behind why those actions were chosen. So when you question o3, it has nothing to look back on and resorts to making things up.

**I’ve already been “feeling the AGI”, but this is the first model where I can really** ***feel the misalignment*****. That’s not good.**

Though to OpenAI’s credit, it’s good they gave early access to Transluce and METR to allow them to do testing in advance.

~

### **When might you want a model other than o3?**

My default model is o3. Despite the concerns around lying, I think o3 still has the most raw intelligence — if you can tame it, it's very helpful.

However, some exceptions for using o3:

* **If cost or speed is a concern**, you’d want to use a cheaper or faster model. o3 is slow and expensive, but you get what you pay for.
* **If you need very high reliability**, the higher hallucination and fabrication rate for o3 is a concern. While no AI can be blindly trusted, o3 outputs need to be checked more often. I find Gemini 2.5 to be the most overall reliable here. Claude 3.7 also seems to blatantly invent much less often than o3, but also sometimes just isn’t smart enough to get the right answer.
* If you want **good prose**, I find o3 to be a terrible writer. Personally I think Claude 3.7 still writes best on a per-sentence basis, though struggles a bit with crafting longer articles. I think Gemini 2.5 does a bit less good on a per-sentence basis but shines best overall and is pretty underrated for writing. However, you could get o3 to do all the research and then get Claude to stitch it together — in my opinion, this works surprisingly well.
* Similarly to well-written prose, if you want **well-written code**, the actual writing of software output doesn’t seem to be o3’s forte as compared to reasoning about software. I still like Claude Sonnet 3.7 best. o3 codes more like an insane mathematician than an engineer who is seeking to make your code review easy.
* If you want to **search tweets** or get updates on **immediately up-to-the-minute breaking news**, you still need Grok.
* If you need **image generation**, I’ve heard anecdotally that 4o is better at that. Grok is also worth a try here, especially if you’re being held back by OpenAI’s content filter. Grok doesn’t care.
* If you need to **analyze a lot of text at once**, Gemini 2.5 via AI Studio has a larger context window, so can analyze much larger amounts of text.
* If you need to do **reasoning on video**, Gemini 2.5 is the better choice.
* If you want to do **“deep research”**, I think Gemini 2.5’s deep research is still better than OpenAI’s tool by the same name. Frequently, I find it interesting to run both.
* If you want **emotional intelligence** (“hearing you” instead of problem solving), I still like Claude Sonnet 3.7 best.

Getting a second opinion from Gemini 2.5 and Claude 3.7 is often helpful.

~

# Get hired to do cool AI stuff

If you liked the above analysis and are interested in getting paid to do some of this yourself, now’s your chance. This week we have three different DC-based AI policy career accelerators to consider:

### 3-Day DC workshop to learn about AI policy

The Horizon Institute and Foundation for American Innovation are [recruiting professionals with AI expertise for a fully-funded,](https://horizonpublicservice.org/ai-innovation-security-policy-workshop/) **[three-day workshop](https://horizonpublicservice.org/ai-innovation-security-policy-workshop/)** [in Washington DC](https://horizonpublicservice.org/ai-innovation-security-policy-workshop/) (July 11-13, 2025).

* This program connects technologists, researchers, and industry experts with policymakers tackling critical AI governance challenges — from energy demands to export controls.
* You'll gain practical insights into policy careers, build connections with decision-makers, and explore pathways into government.
* No policy experience needed — they're specifically seeking domain experts from technical backgrounds who can bridge the gap between innovation and governance.
* **Applications close May 4th**

~

### **Conservative AI Policy Fellowship**

Are you a conservative based in DC looking to learn more about AI policy? [The Foundation for American Innovation is launching a](https://www.thefai.org/fellowships) **[fully-funded, six-week fellowship (June 13–July 25, 2025)](https://www.thefai.org/fellowships)** [for conservative policy professionals.](https://www.thefai.org/fellowships)

* This work-compatible program features weekly lunch sessions, occasional evening workshops, and one weekend retreat, culminating in a policy memo.
* **Fellows receive a $1,500 stipend** plus covered expenses.
* Fellows get to join a network of policy scholars and technologists exploring conservative approaches to AI governance, national security implications, US-China competition, and regulatory frameworks.
* Open to early and mid-career professionals in government, think tanks, advocacy, and tech sectors—no AI background required.
* **Application deadline: April 30, 2025.**

~

### Horizon's Career Accelerator

Horizon Institute has also launched a second program, **[a flexible 9-month AI Policy Career Accelerator](https://horizonpublicservice.org/horizon-launches-policy-career-accelerator/)** **running from June 2025 to February 2026.** It is designed to help both students and mid-career professionals transition into AI policy roles and can be done on top of your existing career.

* The program offers **personalized mentorship, policy training, application support, and potential funding up to $50,000** for career development expenses.
* Ideal candidates will have demonstrated interest in AI and/or public policy, strong communication skills, and passion for public service.
* **Applications close May 6th, 2025**.
* What makes this opportunity special is its flexible, modular approach tailored to individual career stages and needs, whether you're seeking internships, fellowships, or pivoting from another field.

~

#### **Shape the future of AI policy in DC or remotely with me and IAPS!**

I mentioned this last week — the Institute for AI Policy and Strategy (IAPS), where I work, **[is offering a fully-funded, three-month AI Policy Fellowship](https://www.iaps.ai/fellowship)** running from September 1-November 21, 2025 to help people pivot their careers into AI policy work.

I mention this again because we’re doing a webinar this Tuesday at 1pm ET where you can learn from past fellows, meet the team behind the program, and get your questions answered.

[Register for the webinar](https://us02web.zoom.us/meeting/register/ae2zeEEXSu2nRs0-lWALbA#/registration)

~

# Whimsy

[If you want to follow your dreams, you have to say no to all the alternatives](https://oliveremberton.com/2014/if-you-want-to-follow-your-dreams-you-have-to-say-no-to-all-the-alternatives/)

~

[Ars Longa, Vita Brevis](https://slatestarcodex.com/2017/11/09/ars-longa-vita-brevis/)

~

[What's the chance of having drunk the same water molecule twice?](https://www.reddit.com/r/askscience/comments/4mndsq/whats_the_chance_of_having_drunk_the_same_water/)

> For any given water molecule, the odds are basically negligible. But the odds that you've drank at least one water molecule twice are pretty much 100%.

~

In my opinion, the biggest aspect of US-China tech competition we need to worry about is that China has way cooler drone shows:

When can we get something this awesome in the United States?!

Liked this analysis and want to get the one for next week? Subscribe!

Subscribe