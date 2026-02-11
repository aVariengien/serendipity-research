# AI excels at code competitions, struggles with real work

*What CodeForces rankings reveal about AI capabilities*

Published: 2025-02-17
Source: https://peterwildeford.substack.com/p/ai-excels-at-code-competitions-struggles

---

[![a computer screen with a bunch of code on it](https://images.unsplash.com/photo-1515879218367-8466d910aaa4?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wzMDAzMzh8MHwxfHNlYXJjaHwyNXx8Y29kaW5nfGVufDB8fHx8MTczOTY2MTcyNHww&ixlib=rb-4.0.3&q=80&w=1080 "a computer screen with a bunch of code on it")](https://images.unsplash.com/photo-1515879218367-8466d910aaa4?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wzMDAzMzh8MHwxfHNlYXJjaHwyNXx8Y29kaW5nfGVufDB8fHx8MTczOTY2MTcyNHww&ixlib=rb-4.0.3&q=80&w=1080)

Photo by [Chris Ried](true) on [Unsplash](https://unsplash.com)

*Author’s note: This analysis was originally part of a previous post, but it was buried at the bottom and I wanted to feature it more prominently. So I removed it from there, expanded it, and put it here. But sorry if you’re seeing this twice.*

~

When IBM's Deep Blue beat chess champion Garry Kasparov in 1997, it was a notable milestone in the development of AI. Today, AI systems are beginning to achieve similar feats in the world of competitive programming — but the implications for automating real-world software development are more complex.

Want more analysis on AI progress? Subscribe!

Subscribe

## The CodeForces achievement

I [covered previously](https://peterwildeford.substack.com/p/what-happened-in-ai-this-week-france) that Sam Altman (along with OpenAI Chief Product Officer Kevin Weil) [gave a Q&A at the University of Tokyo Center for Global Education](https://www.youtube.com/watch?v=8LmfkUb2uIY), which among many topics got into some details about reasoning models.

In particular, Altman mentioned massive improvement at competitive programming. Competitive programming is an e-sport where programmers compete to solve algorithmic puzzles under fairly tight time constraints. [CodeForces](https://codeforces.com/), one of the leading platforms in this space, hosts regular contests, usually in two-hour rounds.

Based on how one does, competitors at CodeForces rating on an [Elo rating system](https://en.wikipedia.org/wiki/Elo_rating_system), like Chess ratings. A rating of 1900+ puts you in the top 1%, which typically requires the skills of a strong software engineer at a major tech company. Top 50 CodeForces contestants typically have ratings above 3000 and are algorithm specialists at companies like Google and Facebook.

As far as I know, OpenAI’s LLMs have not actually competed directly on CodeForces against humans. But OpenAI [did publish a paper on February 3](https://arxiv.org/html/2502.06807) which outlined a mock CodeForces dataset:

> To assess our models’ competitive programming abilities, we simulated CodeForces contests under conditions that closely mirrored real competitions. This included using the full test suite for each problem and enforcing appropriate time and memory constraints for solutions.
>
> Our evaluation focused on Division 1 contests from 2024 and December 2023, ensuring all test contests occurred after the data cut-off[…] Additionally, we conducted a contamination check as a sanity measure, leveraging the OpenAI embedding API to verify that test problems had not been seen during training.

This dataset lets OpenAI compare their models to human scores. Sam Altman notes their very first reasoning model was in the top one million at competitive programming on this dataset. OpenAI’s most recent (but not yet released) o3 model is reported to be in the top 175. In the Q&A, Altman mentioned seeing internal benchmarks where their model placed in the top 50, and Altman thinks OpenAI will beat top human performance by the end of the year.

Here’s a chart of this progress to date:

[![](https://substackcdn.com/image/fetch/$s_!C7UP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e874b5a-2181-4f1a-9faf-c4a9a8ebda37_2072x1262.png)](https://substackcdn.com/image/fetch/$s_!C7UP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e874b5a-2181-4f1a-9faf-c4a9a8ebda37_2072x1262.png)

Compare that graph to the rise in ELO score among chess computers, where chess engines rapidly rose to human-level skill and then eventually surpassed human skill, to where today humans add absolutely no value compared to what chess engines can come up with:

[![](https://substackcdn.com/image/fetch/$s_!G86c!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fce302cf9-2c1c-446f-b198-91f792ca430c_1344x1140.png)](https://substackcdn.com/image/fetch/$s_!G86c!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fce302cf9-2c1c-446f-b198-91f792ca430c_1344x1140.png)

*The part about 2024 was added by me and is not in the original 538 graphic*

## Human vs. AI approaches

So does this mean that AI is about to become a superhuman engineer and automate computer programming? Not quite yet.

One key thing to understand in these CodeForces challenges is that humans are under intense time pressure. OpenAI says they were “enforcing appropriate time and memory constraints for solutions”, but I think this means that the AI received the same amount of time as humans, which is an awful lot of time for the AI. This was enough time to [generate over 1000 potential solutions](https://x.com/occamsbulldog/status/1889747805566021834) before using reasoning to decide which single solution to submit.

This is a key difference between human and AI approaches. Humans do not have the time to generate over 1000 candidate solutions. A human programmer instead looks at a problem and quickly intuits the correct algorithm based on years of experience and pattern recognition. They'll write one or two solutions at most. AI, in contrast, is much less efficient per attempt but makes up for it with speed and volume. If AI was restricted to type code at a typical human speed, it would lose CodeForces competitions to humans badly. This distinction may matter if it suggests AI still lacks some deep understanding that humans have.

But to be clear, this isn’t just trial and error, and the AI isn’t just brute forcing the solutions — there’s too many possible options to do that. AI definitely shows genuine understanding. And in the real world, the AI will just genuinely be faster — this is a real advantage AI actually has.

## Current limitations

So how good is AI at software engineering? METR, an independent evaluation org, [put this to the test in November](https://metr.org/blog/2024-11-22-evaluating-r-d-capabilities-of-llms/) and found different AI systems (colored lines) outperforming expert human programmers (black line) until a bit before the four hour mark, and then underperforming after that:

[![](https://substackcdn.com/image/fetch/$s_!yrWn!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2228c1dd-e8b6-4919-8ce9-b58367811f87_1200x750.png)](https://substackcdn.com/image/fetch/$s_!yrWn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2228c1dd-e8b6-4919-8ce9-b58367811f87_1200x750.png)

This means we’re still a ways away from fully automated software engineers. A fully autonomous coding agent - one that can independently brainstorm, debug, test, and integrate entire systems - is a lot more complex than what we currently have. Altman says in the Q&A that such systems are still a major research challenge.

As another illustration, it was interesting to see in the [o3-mini system card](https://cdn.openai.com/o3-mini-system-card.pdf) that despite OpenAI models being able to pass OpenAI research engineer interviews with 93% accuracy…

[![](https://substackcdn.com/image/fetch/$s_!IHtH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffa4e1914-6b7b-4bb4-82ff-beb6812a5022_1530x834.png)](https://substackcdn.com/image/fetch/$s_!IHtH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffa4e1914-6b7b-4bb4-82ff-beb6812a5022_1530x834.png)

…the models still were not skilled at replicating pull request contributions by OpenAI employees:

[![](https://substackcdn.com/image/fetch/$s_!iCns!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc0772d50-c0cd-404f-ad64-cc8afd4a1ff5_1580x1228.png)](https://substackcdn.com/image/fetch/$s_!iCns!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc0772d50-c0cd-404f-ad64-cc8afd4a1ff5_1580x1228.png)

## Implications

The rapid progress in competitive programming capabilities has several important implications:

* The jump from top 1M to top 50 in competitive programming on CodeForces happened faster than many experts predicted, suggesting we may need to revise timeline estimates for other AI capabilities.
* If AI becomes able to replace or notably augment human software engineers that could create a feedback loop where AI could accelerate the development of future AI systems. This could make AI timelines even shorter.
* Significant uncertainty remains about how quickly these capabilities will develop. While OpenAI's progress is impressive, it is hard to extrapolate from CodeForces performance to real-world software development capabilities. The gap between solving well-defined algorithmic puzzles and managing complex software projects remains substantial.
* While AI excels at well-defined, time-limited programming tasks, it still struggles with longer-term software development challenges. This suggests that near-term risks from AI systems currently come not from complete automation, but from augmentation of existing capabilities. This has ramifications for everything from software infrastructure development to cybersecurity.

The trajectory of AI progress in competitive programming offers both a warning and a reality check. While the pace of improvement has been remarkable, limitations in areas requiring longer-term reasoning and system design suggest we're still in a transition period. This gives policymakers and organizations time to adapt, but that window may be shorter than previously assumed.

Further understanding of both the capabilities and limitations of current systems is crucial for making informed decisions about AI policy and investment.