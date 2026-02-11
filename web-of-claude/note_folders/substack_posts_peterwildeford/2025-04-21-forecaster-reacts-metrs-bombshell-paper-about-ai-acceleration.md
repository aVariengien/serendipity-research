# Forecaster reacts: METR's bombshell paper about AI acceleration

*New data supports an exponential AI curve, but lots of uncertainty remains*

Published: 2025-04-21
Source: https://peterwildeford.substack.com/p/forecaster-reacts-metrs-bombshell

---

[![](https://substackcdn.com/image/fetch/$s_!06bO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2a40a268-b30d-407f-8388-4a19638b6bf2_1300x776.png)](https://substackcdn.com/image/fetch/$s_!06bO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2a40a268-b30d-407f-8388-4a19638b6bf2_1300x776.png)

***About the author:** Peter Wildeford is a top forecaster, ranked top 1% every year since 2022. Here, he shares analysis that informs his forecasts.*

About a month ago, METR, an AI evaluations organization, published a [bombshell graph](https://x.com/METR_Evals/status/1902384481111322929) and [paper](https://arxiv.org/abs/2503.14499) that says that AI is accelerating quickly. With [OpenAI’s recent launch of o3 and o4-mini](https://openai.com/index/introducing-o3-and-o4-mini/), we can see if these predictions hold up.

The simple version of this chart is easy to explain. Claude 3.7 could complete tasks at the end of February 2025 that would take a professional software engineer about one hour. If this trend holds up, then seven months later at the end of September 2025 we should have AI models that can do tasks that take a human two hours. And in April 2026, four-hour tasks.

You can see where this goes…

* day-long tasks (8hrs) by November 2026
* week-long tasks (40hrs) by March 2028
* month-long tasks (167hrs) by June 2029
* year-long tasks (2000hrs) by June 2031

o3 gives us a chance to test these projections. We can see this curve is still on trend, if not going faster than expected[1](https://peterwildeford.substack.com/p/forecaster-reacts-metrs-bombshell#footnote-1-161556530):

[![](https://substackcdn.com/image/fetch/$s_!jIAX!,w_2400,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0aa2157a-3050-4d05-8e82-cae111f7effe_2246x1050.png)](https://substackcdn.com/image/fetch/$s_!jIAX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0aa2157a-3050-4d05-8e82-cae111f7effe_2246x1050.png)

**AI tasks are growing on an exponential** — like how early COVID cases seemed like nothing, but then quickly got out of control.

Does this mean that AI will be able to replace basically all human labor by the end of 2031? Can we trust this analysis?

Let’s dig in.

## How does the paper work?

Here’s the methodology:

* Create a diverse suite of software engineering tasks to test AIs and humans on.
* Hire a bunch of human software engineers as contractors, see how long it takes on average for them to complete each task.
* Run a bunch of AIs on these tasks, see if they complete the tasks or not.
* For each AI model (e.g., o3), see what tasks it succeeds on and what task it fails on. Sort these tasks by the amount of time it takes humans to complete them. Then plot this as a graph.
* Find the value where the success rate equals 50%. This is the “task length at 50% reliability” for that AI[2](https://peterwildeford.substack.com/p/forecaster-reacts-metrs-bombshell#footnote-2-161556530).

[![](https://substackcdn.com/image/fetch/$s_!rZmD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe05c577a-3fe9-48ca-b2df-695e373f1b0e_2578x1302.png)](https://substackcdn.com/image/fetch/$s_!rZmD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe05c577a-3fe9-48ca-b2df-695e373f1b0e_2578x1302.png)

* Once we have this estimate for each model, we can plot it on a graph
* Then we can try to fit a trend line

[![](https://substackcdn.com/image/fetch/$s_!jIAX!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0aa2157a-3050-4d05-8e82-cae111f7effe_2246x1050.png)](https://substackcdn.com/image/fetch/$s_!jIAX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0aa2157a-3050-4d05-8e82-cae111f7effe_2246x1050.png)

* Then we can try to carefully extrapolate this trend line and observe crazy results

[![](https://substackcdn.com/image/fetch/$s_!hv23!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F99ff4567-e3df-44cc-903e-1d11a36525b2_2242x1050.png)](https://substackcdn.com/image/fetch/$s_!hv23!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F99ff4567-e3df-44cc-903e-1d11a36525b2_2242x1050.png)

* We then try to figure out what level of “task length at 50% reliability” it takes to be equivalent to AGI[3](https://peterwildeford.substack.com/p/forecaster-reacts-metrs-bombshell#footnote-3-161556530), see when the trendline thinks we will hit that mark, and declare that to be the date of AGI.

## Will these tasks generalize to AGI?

Of course, this is a bit silly. Making graphs is the easy part, interpreting them is harder. Let’s try to bring this analysis down to Earth and refine it some more.

Let’s take a deeper look at what tasks METR is asking the models to do. The paper gives these examples[4](https://peterwildeford.substack.com/p/forecaster-reacts-metrs-bombshell#footnote-4-161556530):

[![](https://substackcdn.com/image/fetch/$s_!X_Km!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5a9f8f23-a97a-41d9-b62b-3d707761126c_1452x630.png)](https://substackcdn.com/image/fetch/$s_!X_Km!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5a9f8f23-a97a-41d9-b62b-3d707761126c_1452x630.png)

p13-14 of the [HCAST paper](https://arxiv.org/abs/2503.17354) and p19 of the [“Long Tasks” paper](https://arxiv.org/pdf/2503.14499) do a good job of covering some of the issues with generalizing these tasks:

* **These are all software engineering tasks:** We don’t get to see tasks across other domains relevant to remote work, where AI might struggle more.
* **All tasks are clearly defined and automatically scored:** Each task tells you exactly what to do and exactly how you succeed. The real world is rarely like this. This could be an important way models get stuck that is not covered in METR’s tasks.

* **Everything is solitary, static, and contained:** The tasks are designed to be done autonomously in a single computer session in an unchanging and uncompetitive environment. Agents don’t need to coordinate or gather information across a wide variety of sources. This is very unlike the real world.

* **There’s minimal cost for waste or failure:** Exceeding the cost of human performance, using compute inefficiently, overusing limited resources, or making multiple mistakes are typically not punished in the task set, with a few exceptions. This may also be unlike the real world.
* **Learning effects are ignored:** METR found[5](https://peterwildeford.substack.com/p/forecaster-reacts-metrs-bombshell#footnote-5-161556530) that the dedicated maintainers of a particular GitHub repository were 5-18x faster at completing tasks related to that repository than contractors that were skilled software engineers but otherwise had minimal prior experience with the repository. These contractors are the types of baseliners used for estimating the length of the tasks in METR’s task suite, which means learning effects are ignored. Humans are likely hired in part because of their ability to master very niche tasks by accumulating learning over time – current AI models do not experience these training effects.

* **Reliability matters** – METR is judging AIs based on the length of tasks they can do at 50% reliability. But in the real world you may want higher than 50% reliability at a particular use case, depending on the task. When looking at where AIs can do tasks with 80% reliability, you get the same doubling time but starting from a lower base of only 15 minutes[6](https://peterwildeford.substack.com/p/forecaster-reacts-metrs-bombshell#footnote-6-161556530).

## Current models: great at software engineering, far from AGI

The bottom line is that work on AGI and automating the economy relies not on replacing just human software engineers, but replacing *all work*. METR’s task list is a significant advance in being able to track AI progress on complex tasks, but it is definitely not a benchmark of all human labor.

This is important because **I would guess that software engineering skills overestimate total progress on AGI** because software engineering skills are easier to train than other skills. This is because they can be easily verified through automated testing so models can iterate quite quickly. **This is very different from the real world, where tasks are messy and involve low feedback — areas that AI struggles on.** When you look at all tasks relevant to AGI, you may end up with very different reliability curves and doubling rates, which is a real challenge for this analysis.

**In fact, the range of what AI can do is fairly different from humans and cannot be easily compared.** Recall that AI can become fluent in over 100 languages simultaneously in just three months and can read thousands of words per minute. But at the same time, AIs still struggle on simple tasks that humans can do very easily. While METR discusses AI being able to do >1hr software tasks, **there are many simple tasks that many humans can do in less than a minute that AIs cannot do.**

Consider o3 spending 13 minutes using a wide variety of advanced image processing tools to analyze this simple doodle trying to match arrows to stick figures and still failing – a task that a six-year-old child could do in a matter of seconds:

[![](https://substackcdn.com/image/fetch/$s_!iCP-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa2a97ba2-a7d2-4ade-bcec-7f7ebebb41cd_1030x1302.png)](https://substackcdn.com/image/fetch/$s_!iCP-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa2a97ba2-a7d2-4ade-bcec-7f7ebebb41cd_1030x1302.png)

*([Source for the analysis](https://x.com/lukeprog/status/1912592191282712777/photo/1), [original source for the doodle](https://x.com/SpencerKSchiff/status/1910106368205336769))*

Similarly, AI still fails to do basic computer use tasks that take humans less than a minute – such tasks would be critical for achieving an AGI that aims to do remote work. And there are many other embarrassing failures, such as [making simple mistakes at tic-tac-toe](https://x.com/labenz/status/1912605350529806446), [not being able to count fingers](https://x.com/ai_for_success/status/1913262025956098343), [getting confused about simple questions](https://x.com/lxrjl/status/1912566334602305783), and [thinking some of the time that 9.11-9.8 = 0.31](https://x.com/colin_fraser/status/1912581143486144515).

Thus it matters where you index to. When looking at AI’s strengths, it’s easy to make a mistaken extrapolation that makes AI seem impressive. Consider that specialist AIs like Stockfish / AlphaZero can identify chess moves that take humans many years to equivalently analyze. If you take this domain and extrapolate it, [it predicts that AI can operate at the scale of decades](https://x.com/tamaybes/status/1902537990062342547), well beyond AGI, which is obviously not true. This is because chess is not representative of AGI tasks.

But when indexing to AI’s weaknesses, it’s easy to think that AGI will never be achieved. The true answer lies somewhere in between, where we have to be more careful in terms of figuring out what the collective range of tasks automating all human labor will require and figuring out what task length AI has among that larger, more general, more messy group of tasks.

## Can we project the curve forward?

Another core issue with the methodology of projecting out the exponential is we don’t know if it will keep going that way. Progress in the METR paper is presented as an inevitable consequence of the unfolding time, but actual AI progress comes out of increased capital spending, increased compute efficiency, algorithm development, etc. These are all happening very fast right now, but they may soon instead slow down. It’s going to get harder and harder to 10x the compute of models and 10x the amount of money spent on them. Data availability might become an issue.

And it’s also still unclear how much reasoning will scale, or if new techniques will arise that improve scaling. So much of AI is new and still under development. We’re not in a paradigm of iterating over different amounts of training compute, but instead we’re dealing with a lot of different variables changing at once, and the chance to introduce new variables. This makes extrapolations even more confusing.

And longer task times might create more than linear levels of increased complexity. The doubling rate could become longer over time now that we’ve done all the “low hanging fruit”. These are all challenges to the unfolding of the exponential, and it makes it natural to think scaling will slow down soon.

**Ultimately the problem with projecting a line going up is that sometimes the line stops going up.** For example, “baby scaling” goes fast in the first few years, but then hits a slow point:

[![](https://substackcdn.com/image/fetch/$s_!G_oz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faaf70239-ba29-47db-9cb4-f4f73ea12751_1138x890.png)](https://substackcdn.com/image/fetch/$s_!G_oz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faaf70239-ba29-47db-9cb4-f4f73ea12751_1138x890.png)

[(Source)](https://x.com/pronounced_kyle/status/1768852493092680036?lang=en)

**However, for AI we really don’t know where this slow point is or if the lines will ever slow. This is still very uncertain.** Calling the top on the AI scaling curves so far has been notoriously difficult. Many scaling doubters have been proven wrong over the past few years.

## Are there reasons to think METR might be *underestimating* AI progress?

On the other hand, we should keep in mind that METR might be *underestimating* AI progress and that actual trends could be faster than the median line METR presents.

Most notably, p37 of [the “Long Tasks” paper](https://arxiv.org/abs/2503.14499) shows that if you look at the trend solely over 2024-2025 (GPT4o launch to Claude 3.7 Sonnet launch), then the doubling time is about twice as fast (118 days instead of 212)! This could get to one-month tasks by September 2027!

[![](https://substackcdn.com/image/fetch/$s_!8U7A!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb205418d-f8f6-4efc-bd72-8314d2f69990_1192x754.png)](https://substackcdn.com/image/fetch/$s_!8U7A!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb205418d-f8f6-4efc-bd72-8314d2f69990_1192x754.png)

This is further confirmed by o3 and o4-mini, which show a doubling occurred in 63 days rather than the typical 212.[7](https://peterwildeford.substack.com/p/forecaster-reacts-metrs-bombshell#footnote-7-161556530)

And there are other points that suggest a speed-up is possible:

* **Internal models might be ahead of the public state of the art.** When Claude 3.7 was released, it is plausible that Anthropic might have had a better model internally that could perform even better on the tasks. This means that the true best capabilities as of today might be slightly better, as we only see models when they are released. Similarly, o3 may have had >1hr performance back in 2024 December when it was first announced or even earlier than that as it was being trained, but it wasn’t released publicly until 2025 April.

* **Agency training:** The type of “agency” training needed for models to excel at software engineering is just starting. This is the exact type of model training that would be necessary to help models excel at many-step problems and solve longer tasks. There could still be room for much faster growth.

* **Inference-time compute:** Reasoning skills likely improve with even more compute spent thinking about the problem. METR notes that “more than 80% of successful runs cost less than 10% of what it would cost for a human to perform the same task” (p22 of [the “Long Tasks” paper](https://arxiv.org/abs/2503.14499)). This suggests that there’s room to more efficiently allocate spending to help models solve tasks while still being competitive with human rates.

* **Feedback loops:** A core way AI progress is made is through researcher experimentation and iteration, which can potentially be sped up by AI tools. If future AI could automate and greatly expand the amount of R&D that can be done, that could compound, improving models more quickly.[8](https://peterwildeford.substack.com/p/forecaster-reacts-metrs-bombshell#footnote-8-161556530) **This potentially motivates a** ***superexponential curve*** **of AI progress, where the doubling rate itself increases faster over time.**

* **Improving scaffolding could matter:** Raw AI models like GPT4 out of the box don’t perform well on these tasks. Instead, additional programming is done to build systems and tools around the AI that allow the AI to take multiple steps, browse the internet, execute code autonomously, learn from bugs and errors, and iterate. This is referred to as *‘scaffolding’.* Improvements in scaffolding can make the exact same AI more capable by helping it better harness its strengths and avoid weaknesses. METR has worked hard to improve their scaffolding, but future improvements are likely still possible. This is an underrated source of AI progress.

## How much task length do you need to match human performance?

If we’re trying to automate the economy, you’d want to know what level of task length individual jobs require. Is there a such thing as a year-long task? Perhaps just limited to people writing novels or some other long-running multifaceted, deeply integrated piece of work. Instead, careers would be composed of many hour-long tasks, day-long tasks, and maybe even the occasional month-long task. You keep iterating over these tasks and composing them into a longer piece of work.

For example, while I’ve been writing this Substack for a few months, it is composed of individual blog posts that each take 3-20 hours to write. So if AI could automate all aspects of a 20-hour writing task as good as me, the AI could potentially have a compelling Substack too by just chaining together a bunch of 20-hour tasks producing individual posts.

Following this logic, METR thinks that an AI capable of one-month work would be an AGI (see p18-19), given that a lot of economically valuable work, including large software applications, can be done in one month or less. Additionally, one month is about the length of a typical company onboarding process, suggesting that an AI with a one-month task length could acquire context like a human employee[9](https://peterwildeford.substack.com/p/forecaster-reacts-metrs-bombshell#footnote-9-161556530).

But is that true? For example, how much does my prior experience writing Substacks help me write the next one more effectively, and how does that count towards the task length? And what about how much I draw on my depth of expertise across forecasting, AI, and policy, which comes from years of experience? Does that make each Substack post a year-long task or more? I have no idea. [Ajeya Cotra on Twitter notes](https://x.com/ajeya_cotra/status/1902486863778062521):

> I'm pretty sure I'd be much worse at my job if my memory were wiped every hour, or even every day. I have no idea how I'd write a todo list that breaks down my goals neatly enough to let the Memento version of me do what I do.

Together, this makes it a fairly fuzzy boundary for when METR projects we reach AGI. I’m not sure the boundary could be that clear cut and there is significant uncertainty here.

## What might this suggest for AGI timelines?

We can actually attempt to use the METR paper to try to derive AGI timelines using the following equation:

days until AGI = log2(*{AGI task length}* / *{Starting task length}*) \* *{doubling time}*[10](https://peterwildeford.substack.com/p/forecaster-reacts-metrs-bombshell#footnote-10-161556530)

Here’s an example of what this looks like if you plug in my preferred assumptions (or feel free to make your own and do the math):

* **Doubling time: ~165 days**

  + Let’s start with 118 days, the trend METR found for 2024-2025 that seems to have predicted o3 well. Then let’s average it with 212 days, the overall 2019-2025 trend, assuming there may be some long-term regression to the mean. That’s 165 days.
* **Current task length on all AGI tasks: ~3min45sec**

  + The current public state of the art on METR’s self-contained software tasks is o3 at ~1hr45min.
  + However, this is likely an underestimate and hypothetically even better scores could be reached by improving scaffolding and adding even more compute. Let’s assume this gives a 1.5x boost to ~2h30min.
  + On the other hand, mastery of METR’s self-contained software tasks is likely not sufficient for AGI and true AGI tasks is likely harder. Let’s assume true AGI tasks are 10x harder, plunging the starting task length down to 15min.
  + Additionally, we likely need more than 50% reliability. Let’s assume we need 80% reliability, which adds a 4x penalty, plunging starting task length down further to 3min45sec.
* **Shift: ~100 days**

  + We also have to account for models that companies have internally. o3 was available to OpenAI back in December, long before the April release. Let’s assume models have capabilities internally about 100 days before release, and move the whole curve 100 days earlier.
* **AGI task length: ~167hrs**

  + Let’s go with METR and assume month-long tasks are sufficient (~167 hours) for AGI.

If you make all these assumptions and do the math, AGI is achieved 1778 days after o3 launch, or **2030 February 28**.

~

We can extend this into a formal model with uncertainty across what level of task mastery, reliability, and task length is needed to achieve AGI, as well as different ways of calculating the average doubling time will be over the course of now to AGI.

Doing so produces the following …this plots 200 individual model runs, with AGI arising at the red “X”s.

[![](https://substackcdn.com/image/fetch/$s_!imrN!,w_2400,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F66c8ff61-cae5-4517-9edf-e386f1c5481d_1996x1064.png)](https://substackcdn.com/image/fetch/$s_!imrN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F66c8ff61-cae5-4517-9edf-e386f1c5481d_1996x1064.png)

This model suggests a median arrival date of 2030Q1 for AGI, with a 10% chance of achieving AGI before the end of 2027 and a 90% chance by the end of 2034Q2. *(Variable definitions + full code available for nerds in this footnote:*[11](https://peterwildeford.substack.com/p/forecaster-reacts-metrs-bombshell#footnote-11-161556530)*)*

Additionally, according to this model there is a ~0.1% chance of achieving AGI this year, a ~2% chance of AGI by the end of 2026, and a ~7% chance by the end of 2027.

*[NOTE 2025 JUN 21: The numbers above no longer represent my best guess, as we’ve learned more since this post was written. Some changes are instead explained [here](https://x.com/peterwildeford/status/1936500129638342814). This will be written in a Substack post in a future date that will supersede this post.]*

But four additional notes on this model:

* **This is not an ‘all things considered’ model!** Before you screenshot this and say “Peter thinks AGI is coming in 2029!”, keep in mind that this model is just taking into account the results from the METR paper with some uncertainty provided, but still contains significant additional uncertainty around methodology. Other parameters around capital slowdown and AI progress diminishing returns could be modeled more explicitly. At the same time, possible new innovations that may speed up AI progress are not taken into account either.
* **This assumes “business as usual”.** This does not account for possible changes in the general dynamics (strong economy, lack of major war, lack of regulations) from which AI has developed over the past five years. Exogenous shocks could slow down AI development.
* **“Achieving” AGI does not mean that AGI will be widespread.** There will likely still be delays in commercializing and widely rolling out the technology.
* **In practice, the curves might be jagged rather than nice curves.** That is, we might see a bunch of progress in task length before hitting diminishing returns or hitting a wall. Additionally, advancements in scaffolding or algorithms could produce a sudden burst in progress.

## Looking forward

Are we close to or far from AGI? The METR paper is indeed a great contribution towards estimating this. While the tasks collected are still far from an exhaustive collection of all tasks that would be relevant to AGI, they are still the most varied and compelling collection and systematic analysis of tasks we have to date.

And what we’re seeing is weird. Models that can debug complex PyTorch libraries better than most professional software engineers yet still struggle with very simple computer use tasks or the ability to follow arrows in a simple drawing remind us that AI capabilities remain incredibly uneven and difficult to generalize. The gap between performing well on clean, well-defined software tasks versus navigating the messy uncertainty of real-world problems remains significant. This thus allows for significant uncertainty about when AGI will be achieved.

Nevertheless, the trends appear robust. With each new model release — Claude 3.7, o3, o4-mini — we've seen capabilities align with or exceed even the optimistic projections. The extraordinary pace of progress suggests we should take seriously the possibility that AGI could arrive much sooner than conventional wisdom suggests, while maintaining appropriate skepticism about extrapolating current trends too confidently.

**And the best part is that this model can be used as an early warning system.** We can continue to observe AI progress over time and see what trend it is following and use that to narrow the model and build more confidence in our projections. This could help us see massive AI progress and give us more time to prepare.

[1](https://peterwildeford.substack.com/p/forecaster-reacts-metrs-bombshell#footnote-anchor-1-161556530)

Here’s the “leaderboard” of raw data for this chart:

* **o3 (2025 Apr 16):** ~1hr45min
* **o4-mini (2025 Apr 16):** ~1hr30min
* **Claude 3.7 Sonnet (2025 Feb 24):** 59min
* **o1 (2024 Dec 5):** 39min
* **DeepSeek r1-0528 (2025 May 28):** [30min](https://metr.github.io/autonomy-evals-guide/deepseek-qwen-report/)
* **Claude 3.5 Sonnet (new, 2024 Oct 22):** 28min
* **GPT4.5 (2025 Feb 27):** ~28min
* **DeepSeek r1 (2025 Jan 20):** [27min](https://metr.github.io/autonomy-evals-guide/deepseek-qwen-report/)
* **o1 preview (2024 Sep 12):** 22min
* **Claude 3.5 Sonnet (old, 2024 Jun 20):** 18min
* **GPT4o (2024 May 13):** 9min
* **Claude 3 Opus (2024 Mar 4):** 6min
* **GPT3.5 Turbo (2023 Jun 13):** 36sec
* **GPT2 (2019 Feb 14):** 2sec

We don’t have data for GPT4.1, o3-mini, o3-pro, o4-mini, Claude 4 Sonnet, Claude 4 Opus, or any Gemini models yet.

[2](https://peterwildeford.substack.com/p/forecaster-reacts-metrs-bombshell#footnote-anchor-2-161556530)

This does obscure variance a bit. Yes, Claude 3.7 *on average* is able to do tasks that take humans 1hr with 50% reliability. But what this means literally is a bit different and can vary by task. There are actually 15min tasks in the time suite that Claude 3.7 cannot handle well (Claude 3.7 has about 80% success at 15min tasks) and there are 4hr tasks in the task suite that Claude can do (Claude 3.7 has about 10% success at 4hr tasks).

[3](https://peterwildeford.substack.com/p/forecaster-reacts-metrs-bombshell#footnote-anchor-3-161556530)

When I use “AGI” in this article, I mean to refer to an AI system that can automate 99%+ of all economically valuable 2024-era remote tasks at a cost less than it costs to employ an equivalently skilled human to do that task.

[4](https://peterwildeford.substack.com/p/forecaster-reacts-metrs-bombshell#footnote-anchor-4-161556530)

p7 of [the “Long Tasks” paper](https://arxiv.org/abs/2503.14499)

[5](https://peterwildeford.substack.com/p/forecaster-reacts-metrs-bombshell#footnote-anchor-5-161556530)

p3 of [the “Long Tasks” paper](https://arxiv.org/abs/2503.14499)

[6](https://peterwildeford.substack.com/p/forecaster-reacts-metrs-bombshell#footnote-anchor-6-161556530)

p12 of [the “Long Tasks” paper](https://arxiv.org/abs/2503.14499)

[7](https://peterwildeford.substack.com/p/forecaster-reacts-metrs-bombshell#footnote-anchor-7-161556530)

METR observed Claude 3.7, released 24 Feb 2025, with a task length of ~1hr and o3, released 2025 Apr 16, with a task length of ~1hr45min. That is a ~1.78x increase in 52 days. 1.78x is 83% of a doubling in logspace. 52/0.83 implies a 63 day doubling rate!

[8](https://peterwildeford.substack.com/p/forecaster-reacts-metrs-bombshell#footnote-anchor-8-161556530)

Though I should point out that automating AI R&D involves automating a lot more than just straightforwardly writing self-contained software like in METR’s tasks. I don’t think this will be as straightforward.

[9](https://peterwildeford.substack.com/p/forecaster-reacts-metrs-bombshell#footnote-anchor-9-161556530)

And of course this is sweeping the large amount of intra-human variance under the rug. When we talk about comparing AI to human tasks, we really need to think — *which humans*? This has implications for task length, as certain humans can do tasks much faster than others. This also likely means you can automate some of the economy much faster than other parts, where humans are less skilled and task lengths are shorter. But when it comes to automating very long work from the most skilled humans where the typical human comes far from success, you’re getting a weird selection effect based on completing the task. For example, does solving Fermat’s Last Problem have a task length of seven years just because that’s how long it took Andrew Wiles to do it?

[10](https://peterwildeford.substack.com/p/forecaster-reacts-metrs-bombshell#footnote-anchor-10-161556530)

…or, if you want to incorporate the possibility of a superexponential, where the doubling rate itself increases:

days until AGI = [ 1 – *{acceleration}* ^ ( log2( *{AGI task length}* / *{Starting task length}* ) ) ] / ( 1 – *{acceleration}* ) \* *{starting doubling time}*

[11](https://peterwildeford.substack.com/p/forecaster-reacts-metrs-bombshell#footnote-anchor-11-161556530)

Variables for the model are defined as follows:

* **Starting task length:** We starts at 1.75hrs, the current length of o3, but then parameterize uncertainty across a “elicitation boost” *(improvements from better scaffolding and increased compute)*, a “reliability penalty” *(50% reliability not being sufficient)*, and a “task type penalty” *(METR’s self-contained software tasks not being enough for AGI)*. *{starting task length}* = 1.75 \* *{elicitation boost}* \* *{reliability penalty}* \* *{task type penalty}.* This ends up being a median of 2min (80% CI: 30sec - 32min).

* **AGI task length:** What is the task length needed for AGI? Assumed to be a lognormal distribution across a 80% CI of two work weeks (80hrs) to a full work year (2000hrs) (median 400hrs).

* **Doubling time and acceleration:** How long does it initially take for task length to double? And does the doubling time itself decrease superexponentially? This is very complicated, hard to estimate, and very sensitive to your personal views. To prevent any frame from dominating, I decide to define a mixture across a few different ways of looking at the data:

  + 40% chance of a regular 212 day doubling time, like the METR paper simply finds from 2019-2024.
  + 20% chance of a regular 118 day doubling time, the METR 2024-2025 trend that seems confirmed with o3.
  + 10% chance of using a pessimistic 320 day doubling time (chosen rather arbitrarily), assuming that we will soon hit steeper diminishing marginal returns.
  + 30% chance of using my crazy internal model that attempts to fit a superexponential to the data, using o3.

    - The way this works is that I fit a bunch of possible doubling rates and superexponentials to different permutations of the data, with acceleration confined to be between 0.9 and 1.0:

      * GPT‑2 to Claude 3.7 Sonnet —> initial doubling rate at 331 days, acceleration = 0.9
      * GPT‑3.5 Turbo to Claude 3.7 Sonnet —> initial doubling rate at 88 days, acceleration = 1.0
      * GPT‑3.5 Turbo to o3 —> initial doubling rate at 88 days, acceleration = 1.0
      * Claude 3 Opus to o3 —> initial doubling rate at 101 days, acceleration = 1.0
      * GPT‑4o to o3 —> initial doubling rate at 97 days, acceleration = 1.0
      * Claude 3.5 Sonnet (old) to o3 —> initial doubling rate at 141 days, acceleration = 0.9
      * o1 preview to o3 —> initial doubling rate at 107 days, acceleration = 0.9
      * GPT‑3.5 Turbo to Claude 3.7 Sonnet —> initial doubling rate at 88 days, acceleration = 1.0
      * Claude 3 Opus to Claude 3.7 Sonnet —> initial doubling rate at 102 days, acceleration = 1.0
      * GPT‑4o to Claude 3.7 Sonnet —> initial doubling rate at 98 days, acceleration = 1.0
      * Claude 3.5 Sonnet (old) to Claude 3.7 Sonnet —> initial doubling rate at 157 days, acceleration = 0.9
      * o1 preview to Claude 3.7 Sonnet —> initial doubling rate at 112 days, acceleration = 1.0
    - Across these runs, we get an average value of an initial doubling rate of 126 days and acceleration = 0.97.

      * I then add variation to the doubling time using a lognormal distribution with an SD of 40. And I add variation to the acceleration using 1 - {a lognorm with an 80% CI from 0.005 to 0.1}.
    - The acceleration parameter implements the superexponential: <1 = superexponential, 1 = normal exponential growth, >1 = subexponential.
    - There is a 40% chance of using the superexponential and an independent 40% chance of using my model for doubling rate.

* **Shift:** How many days earlier should the distribution be shifted to account for internal deployments outpacing public releases? Assumed to be a normal distribution across an 80% CI of 1 month to 5 months (median 3 months).
* **additional parameter uncertainty** from the limited number of tasks, variation between human baseliner performance, variation within models across different runs, variation from the limited number of models tested, variation between models, and variation across other modeling choices (e.g., weighting, regularization). METR accounts for this via a sensitivity analysis displayed in Figure 12 (p18) and I fit the parameter uncertainty to that.

Code for the above graph and simulation are available [here](https://github.com/peterhurford/agi_timelines). This can also be adapted to make your own models.

NOTE 2025 JUN 21: The code above contains new changes to parameters and a new parameter distribution that is not discussed in this article. These changes are instead explained [here](https://x.com/peterwildeford/status/1936500129638342814). This will be written in a Substack post in a future date.