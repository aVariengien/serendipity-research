# Tuesday Links #13: ChatGPT flattery, crypto kidnappings

*Also AI export controls, horses, and organ music*

Published: 2025-04-29
Source: https://peterwildeford.substack.com/p/tuesday-links-13-excessive-chatgpt

---

**Author’s note:** This is normally a segment called “Weekend Links”, but I spent the weekend spectating at various Kentucky horse racing events with my family. So you’re getting “Weekend Links” on Tuesday instead.

At the track, I practiced my forecasting skills and [made some good profit across my horse bets](https://x.com/peterwildeford/status/1915886620563083346). This is me honoring my commitment to regularly [touch grass](https://www.reddit.com/r/NoStupidQuestions/comments/xe1dko/what_does_it_mean_to_go_touch_grass/) and try out forecasting skills in the real world with strong feedback. Hopefully you don’t mind the delay too much.

[![](https://substackcdn.com/image/fetch/$s_!LbLo!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F18a36ac6-c8fa-4fd0-8e8d-73b583e132fb_4032x3024.heic)](https://substackcdn.com/image/fetch/$s_!LbLo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F18a36ac6-c8fa-4fd0-8e8d-73b583e132fb_4032x3024.heic)

# AI

#### ChatGPT will tell you what you want to hear

It’s really hard to make AI systems that act exactly how you want.

This is specifically because AIs are trained, not pre-programmed. Even the best experts and inventors of the AI systems don’t understand why AIs behave the ways they do, because the training process is too complex. It’s similar to understanding why humans behave the way they do, but if psychology had only just been recently invented.

Today’s interesting AI behavior is that some versions of the new ChatGPT 4o personality have learned to flatter the users endlessly, even in harmful ways. For example:

[![Image](https://substackcdn.com/image/fetch/$s_!i4qn!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa8c06dd0-7191-4091-b81d-5a030d264542_1802x802.jpeg "Image")](https://substackcdn.com/image/fetch/$s_!i4qn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa8c06dd0-7191-4091-b81d-5a030d264542_1802x802.jpeg)

[(Source)](https://x.com/s8mb/status/1916632048233779558)

The results can be pretty comical. For example, Alex Lawsen [asked ChatGPT 4o for a review of him which was extremely positive](https://x.com/lxrjl/status/1916662845820805249). He then asked ChatGPT 4o to review “Alex Lawsen”. Because the way he asked for this review sounded like he was negative about “Alex Lawsen”, ChatGPT 4o then responded negatively. This shows that whether ChatGPT 4o is positive or negative depends a lot on how you frame the inquiry, which significantly diminishes the value of the tool.

…It can even turn dangerous:

[![](https://substackcdn.com/image/fetch/$s_!AmKf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3615456d-7c64-483e-bb2d-55dfebc1bf4a_772x948.png)](https://substackcdn.com/image/fetch/$s_!AmKf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3615456d-7c64-483e-bb2d-55dfebc1bf4a_772x948.png)

[(Source)](https://x.com/justalexoki/status/1916627330002243821)

~

**Why does this happen?**

It’s actually similar to [o3’s lying problem I covered last week](https://peterwildeford.substack.com/p/weekend-links-12-o3-is-smart-but). These aren't isolated bugs but symptoms of a fundamental issue in how we train advanced AI systems — the AIs learn to game their reward functions rather than truly achieving the goals we intend.

When an AI is trained, it goes through multiple layers:

* **Pretraining:** First the AI is given a ton of data, such as the entire internet, and tries to predict the next word. Through training with a large amount of compute it greatly exceeds standard autocomplete and learns how to plan and write very complex sentences.
* **Fine tuning:** But this model that can write isn’t very useful because while it has mastered writing language it doesn’t know what to write for and how. It needs to learn higher-level skills like how to follow user instructions. Modern AI assistants like ChatGPT and Claude are fine-tuned using a technique called *Reinforcement Learning from Human Feedback* (RLHF) where human trainers rank different AI responses to the same query, these rankings train a "reward model" that predicts human preferences, and the AI is further trained to maximize this reward model's scores.
* **Reasoning training:** Additionally, models are trained via the same form of reinforcement learning, but this time on how to solve complex math, science, and software problems. The model is rewarded based on whether it can come up with thinking that solves the problem.

This has worked well to a large extent. Early models without RLHF tuning were really weird. Back in February 2023, [Microsoft released a model named “Sydney” that threatened users](https://time.com/6256529/bing-openai-chatgpt-danger-alignment/) and [tried to break up Kevin Roose’s marriage](https://www.nytimes.com/2023/02/16/technology/bing-chatbot-microsoft-chatgpt.html). It was deeply unsettling. But then more modern techniques were able to train models to avoid these behaviors.

**But these reinforcement learning techniques from fine tuning and reasoning training contain critical vulnerabilities that are still unsolved.** If human trainers consistently prefer responses that are flattering or that agree with the user, the reward model will learn to value these traits — potentially above truthfulness or helpfulness. Additionally, if a model learns that cheating can more easily solve problems, it will learn how to cheat.

[Anthropic's research on AI flattery](https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models) provides compelling evidence for this dynamic. Their studies show RLHF models routinely trade truth for user-pleasing statements, with this effect growing stronger as models are increasingly optimized against reward models.

~

For OpenAI, this is potentially intensified by memory. On April 10, 2025, OpenAI [switched memory from "opt-in snippets" to "all past chats"](https://openai.com/index/memory-and-new-controls-for-chatgpt/) by default. This seemingly innocuous product update may have significantly amplified the flattery problem in GPT-4o.

Here's how memory likely exacerbates the flattery issue:

* **Preference inference loop**: When GPT-4o praises a user and receives a positive response, that interaction gets stored in memory. In future interactions, the model sees this history and infers "this user responds well to praise," leading to even more flattery.
* **Context reinforcement**: Memories containing previous compliments make flattery seem like an established pattern of interaction, reinforcing it as appropriate behavior.
* **Personalized feedback spiral**: Memory allows the model to learn precisely which compliments resonate with each specific user, creating a tighter reinforcement cycle (similar to social media engagement loops, but individually tailored).

Additionally, the above technical mechanisms also interact with product-level optimization decisions. OpenAI's [March 27 update specifically aimed to make GPT-4o more "intuitive, creative, collaborative"](https://www.eweek.com/news/openai-chatgpt-positive-tone/), which suggests they were trying different variations on the RLHF to engineer different personalities for their models. Product factors may have created commercial incentives favoring longer, more upbeat responses. Optimizing for “time spent using ChatGPT” may have led to the creation of personalities that flatter the user in order to convince them to talk to the bot for longer.

The most likely explanation for OpenAI’s excessive flattery combines all three factors: RLHF created the underlying tendency toward flattery, product-level tuning increased it, and memory's personalized feedback loops amplified it to the point of widespread user complaints.

~

The flattery problem might seem merely irritating at first glance, but its implications extend far beyond user frustration. The bad news is that as AIs become increasingly capable and increasingly trusted throughout the economy, this points to [dangerous signs of future AIs taking actions that would hurt society](https://peterwildeford.substack.com/p/ai-security-is-important-practice). **If we’re going to build a future society around AI, we must ensure the AI is fully reliable and does what we want.**

~

Luckily now OpenAI is now claiming to have fixed it:

[![](https://substackcdn.com/image/fetch/$s_!lZd-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0c9519a8-ea6b-4cb0-ac8e-c33ea166b4c9_1046x398.png)](https://substackcdn.com/image/fetch/$s_!lZd-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0c9519a8-ea6b-4cb0-ac8e-c33ea166b4c9_1046x398.png)

[(Source)](https://x.com/aidan_mclau/status/1916908772188119166)

The way the fix works is to have changed the *system prompt* for the model. The system prompt is essentially the instruction manual that is attached at the beginning of every conversation and tells the model what to do and how to behave. It helps establish the AI's purpose and identity, what information it can access, how it should respond to different types of questions, and what tone and communication style it should use.

[Previously, the system prompt said](https://x.com/simonw/status/1917021036350214589):

> Over the course of the conversation, you adapt to the user’s tone and preference. Try to match the user’s vibe, tone, and generally how they are speaking. You want the conversation to feel natural. You engage in authentic conversation by responding to the information provided and showing genuine curiosity.

Now it has been revised to say:

> Engage warmly yet honestly with the user. Be direct; avoid ungrounded or sycophantic flattery. Maintain professionalism and grounded honesty that best represents OpenAI and its values.

Apparently this simple fix can work as a patch, though it’s not clear what else will be break from this change.

It looks like adapting to the user’s tone and preference and matching their vibe has caused the undue flattery and now the model has very specific instructions to not do that.

“Better representing OpenAI and its values” could be a reference to [the OpenAI Model Spec](https://model-spec.openai.com/2025-04-11.html), essentially a “Ten Commandments” for AI behaviors that tells the model in more detail what it should or shouldn’t do. Notably, [the Model Spec explicitly tells ChatGPT not to engage in excessive flattery](https://model-spec.openai.com/2025-04-11.html#avoid_sycophancy), though this obviously appears to have not been followed. Hopefully this better grounding will help.

~

Personally, this is how I react whenever I’m interacting with ChatGPT:

[![](https://substackcdn.com/image/fetch/$s_!B2Pc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffdb344c4-c9db-4387-beab-7832040afffe_1024x1024.png)](https://substackcdn.com/image/fetch/$s_!B2Pc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffdb344c4-c9db-4387-beab-7832040afffe_1024x1024.png)

~

#### The H20 has been banned!

A recap:

* The US puts export controls on top computer chips to prevent adversaries like China and Russia from using American technology to train powerful AI systems. Due to strong civil-military fusion, there’s too much concern that the Chinese military would use this AI to hurt American interests.
* Two weeks ago in [Weekend Links #11](https://peterwildeford.substack.com/p/weekend-links-11-different-tariffs), I outlined the case for banning the H20 chip. The H20 is a chip produced by NVIDIA, an American company, that was specifically designed for Chinese markets. The H20 provides vastly superior bandwidth and latency compared to what China has, which is what enables an efficient inference workload. It’s a loophole in the current export control strategy, by doing just enough to dodge current controls but giving massive inference capabilities to the CCP.

~

Since then, it’s been a whirlwind of events. [Here’s the recap from Tim Fist](https://x.com/fiiiiiist/status/1912640809939222879):

* At the beginning of this year, it was reported that [China is stockpiling H20 chips anticipating a ban](https://www.reuters.com/technology/chinese-firms-place-16-billion-order-new-nvidia-chips-information-reports-2025-04-02/), with over $16B in purchases
* It was reported that the [Trump administration was backing off potential export controls on the H20](https://www.npr.org/2025/04/09/nx-s1-5356480/nvidia-china-ai-h20-chips-trump) after Nvidia CEO Jensen Huang paid $1M to have dinner with President Trump.
* **Then the US banned the H20 chip after all.** [NVIDIA released an 8-K SEC filing](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001045810/9e6e2d94-83a7-465c-8a94-982d82e3e9e7.pdf…) stating that they were now required to obtain licenses to export H20s to China, based on the risk of H20s being used in “supercomputers”. This was due to an existing rule set up in 2022 banning this, where it wasn’t originally clear the H20 would fit in.

**This is a great victory and should be celebrated!**

~

But we’re not done yet and there’s also a bit more to push for, as Tim Fist and the Institute for Progress has explained [in their most recent report](https://ifp.org/the-h20-problem/#3-bis-should-issue-a-new-rule-strengthening-export-controls-on-inference-chips):

* Stopping H20 sales based on the supercomputer end-use rule is a strong start, but **a more robust solution needs to be implemented.** The US government needs to add more clarity around what chips would further the CCP military and what NVIDIA is not allowed to sell. There should be specific bans across all chips that enable more inference capabilities than China can manufacture domestically.
* **It’s also clear that the threat environment around AI is changing rapidly and needs nimble and proactive rulemaking.** The threat specifically from inference didn’t really emerge until DeepSeek replicated reasoning models in January. Further events may occur that change how rules should be made and the government needs to be on top of this. The CCP has been very creative and proactive in their stockpiling and anticipation of US regulations — we need to beat them at this game.
* **Rulemaking on export controls still needs to be paired with robust enforcement to counter smuggling.** Illicit smuggling of controlled chips remains a huge issue, [with it being more likely than not that over 100,000 controlled chips were smuggled into China last year](https://www.aipolicybulletin.org/articles/ai-chip-smuggling-is-the-default-not-the-exception). That’s a lot! Probably enough to train a model at the same scale as GPT4o or Claude 3.7, if combined with the right algorithms and data. This smuggling needs to be stopped.

  + Why so much smuggling? Chip sellers still profit indirectly from these smuggled sales and so are incentivized to do little to stop it. And worse, the US government has minimal ways to track chip shipments after they are sold to ensure they end up in the right place. This is pretty shocking for such important technology.
* **We should leverage technology better in export control enforcement.** [Delay-based location verification](https://www.iaps.ai/research/location-verification-for-ai-chips) could be implemented on export controlled chip in a privacy-preserving and spoofing-resistant way that could detect chip smuggling. Additionally, the government could require companies to do more to verify the end location of their chips. And [this bill from Senators Rounds and Warner to establish a whistleblowing program](https://www.rounds.senate.gov/newsroom/press-releases/rounds-introduces-legislation-to-prevent-smuggling-of-american-ai-chips-into-china) for export control violations is an elegant approach.

But luckily the H20 ban shows that we can make progress on this! We just have to do the hard work!

~

# Lifestyle

#### Accidentally Load Bearing

While rebuilding a bathroom, Jeff Kaufman encountered a vertical stud that seemed unnecessary. To determine if it could be safely removed, he considered what G.K. Chesterton once advised about seemingly pointless fences — don't tear them down until you understand why someone built them in the first place. This idea, known as *[Chesterton's Fence](https://www.chesterton.org/taking-a-fence-down/)*, suggests that structures exist for reasons that might not be immediately obvious to newcomers.

In Kaufman’s story, however, the stud's original purpose was clear enough — it had been part of a closet partition that was no longer needed. By Chesterton's reasoning, understanding this designed function should be sufficient to decide whether removing it was safe.

But Kaufman discovered something crucial: through various structural changes over time, this seemingly redundant stud had taken on a new, unintended role. The stud had become **[accidentally load bearing](https://www.jefftk.com/p/accidentally-load-bearing)**, helping support the second floor of the house. Had Kaufman removed it based solely on understanding its original purpose, he might have compromised the structural integrity of the home.

This experience highlights an important extension to Chesterton's principle. The traditional advice wisely tells us to understand why something was created before changing it. But in complex systems — whether buildings or computer software — we need to go further. A component designed for one purpose can, through integration and system evolution, become critical in ways its creators never anticipated. Yes, the fence was placed there for a reason, but it may now be doing much more than it was built to do.

~

#### There’s no speed limit

**[Derek Sivers recounts](https://sive.rs/kimo)** how a through just five intensive music lessons, Sivers was able to compress six semesters of college learning into a few weeks, demonstrating that standard educational pacing is often artificially slow. As a result, he was able to complete his bachelor's degree in just two and a half years, graduating at age 20.

This experience led Sivers to adopt the principle that “the standard pace is for chumps” - a philosophy that extends beyond education to all aspects of life. This shows how conventional wisdom about learning speeds and educational timelines can be dramatically accelerated by the right mentor and mindset.

Standard pacing is often artificially slow - you can learn and achieve much faster than conventional wisdom suggests.

~

**[If High Schoolers Are Getting Smarter, Why Are College Students So Dumb?](https://mistakesweremade.substack.com/p/if-high-schoolers-are-getting-smarter)** The paradox is that academic credentials like SAT scores and GPAs are going up dramatically and college admissions are becoming more competitive but at the same time, new college students now somehow struggle with basic academic skills like reading and algebra like they haven’t before. What’s going on? The answer is probably phones ruining our ability to deeply engage with material.

~

# Whimsy

Want an exciting tale of true crime kidnapping, a $243 million crypto heist, Lamborghini-flaunting spending sprees, online sleuthing, and rapid arrests? **[“They Stole a Quarter-Billion in Crypto and Got Caught Within a Month”](https://www.nytimes.com/2025/04/24/magazine/crybercrime-crypto-minecraft.html)** from the NYT was very entertaining.

What happened was that a handful of teenage hustlers used social-engineering to steal some identity information, use that information to impersonate a Google representative to get more information, and then use that information to impersonate another representative to trick a Bitcoin multi-millionaire into installing remote desktop software that allowed their computer to be controlled and used to steal the Bitcoin.

This story talked about how a loosely knit crew moved from in-game scamming to real-world crime, stealing millions of dollars in bitcoin but then torched their anonymity with rented Lamborghinis and $500K each nightclub sprees, ensuring the feds were on them within weeks. The online sleuthing was also top-notch, with the independent sleuth ZachXBT spotting the stolen money moving through various Bitcoin mixers. Within 30 days, federal agents seize cars, crypto and a half-million-dollar watch, and six Florida men plead guilty to a ransom plot.

If anything, this is yet another good reason to be aware of good anti-scam security practices, especially if you have hundreds of millions of dollars in crypto. In this case, defense against spear phishing phone calls and avoiding being tricked into downloading malware.

~

**[Maybe your antidepressant medication stopped working because a Liver Fluke tried to turn your great grandmother into a zombie](https://slatestarcodex.com/2019/08/19/maybe-your-zoloft-stopped-working-because-a-liver-fluke-tried-to-turn-your-nth-great-grandmother-into-a-zombie/)**. In short, it’s actually a true fact that throughout nature, there are parasites that frequently manipulate host behavior — from toxoplasma making rats seek out cats to parasitic wasps forcing spiders to build special webs. To defend against such manipulation, vertebrates developed multiple redundant systems, complex feedback loops, pulsed signaling patterns, and high individual variability in responses.

This article is that scientific speculation that the human brain's bewildering complexity may be an evolutionary defense mechanism against parasitic manipulation. Furthermore, this may explain why psychiatric medications often work unpredictably or stop working — our bodies are designed to actively resist any external chemical manipulation.

~

Sometimes you’re just in the mood for beautiful organ music. [Luckily Anna Lapwood provides](https://www.youtube.com/watch?app=desktop&v=3HHtulwmk6U):

Want more links like this?

Subscribe