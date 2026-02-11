# Kimi K2 Thinking

Published: 2025-11-11
Source: https://thezvi.substack.com/p/kimi-k2-thinking

---

I previously covered **[Kimi K2,](https://thezvi.substack.com/p/kimi-k2)** which now has a new thinking version. As I said at the time back in July, price in that the thinking version is coming.

Is it the real deal?

That depends on what level counts as the real deal. It’s a good model, sir, by all accounts. But there have been fewer accounts than we would expect if it was a big deal, and it doesn’t fall into any of my use cases.

#### Introducing K2 Thinking

> [Kimi.ai](https://x.com/Kimi_Moonshot/status/1986449512538513505): 🚀 Hello, Kimi K2 Thinking!
> 
> The Open\-Source Thinking Agent Model is here.
> 
> 🔹 SOTA on HLE (44\.9%) and BrowseComp (60\.2%)
> 
> 🔹 Executes up to 200 – 300 sequential tool calls without human interference
> 
> 🔹 Excels in reasoning, agentic search, and coding
> 
> 🔹 256K context window
> 
> Built as a thinking agent, K2 Thinking marks our latest efforts in test\-time scaling — scaling both thinking tokens and tool\-calling turns.
> 
> K2 Thinking is now live on http://kimi.com in chat mode, with full agentic mode coming soon. It is also accessible via API.
> 
> [API here](https://t.co/EOZkbOwCN4), [Tech blog here](https://t.co/n7xxaszqzF), [Weights and code here](https://t.co/4ukcXB0iP6).

[(Pliny jailbreak here.)](https://x.com/elder_plinius/status/1986533887833469420)

It’s got 1T parameters, and Kimi and Kimi K2 have a solid track record, so it’s plausible this could play with the big boys, although the five month delay in getting to a reasoning model suggests skepticism it can be competitive.

As always, internal benchmark scores can differ greatly from outside benchmark scores, especially for open models. Sometimes this is due to outsiders botching setup, but also inside measurements need to be double checked.

For Humanity’s Last Exam, I see an outside source saying as of November 9 [it was in second place on Humanity’s Last Exam at 23\.9%](https://x.com/moreisdifferent/status/1987495505169985983), which is very much not 44\.9% but still very good.

#### Writing Quality

On writing quality we’ve gotten endorsements for Kimi K2 for a while.

> [Rohi](https://x.com/krishnanrohit/status/1986533122624909502)t: Kimi K2 is remarkably good at writing, and unlike all others thinking mode hasn’t degraded its writing ability more.
> 
> Morgan: if i recall, on release gpt\-5 was the only model where writing quality improved with thinking effort.
> 
> Rohit: Alas. 
> 
> Gary Fung: Kimi has always been a special snowflake on creative writing.

[Here’s one part of the explanation](https://x.com/tessera_antra/status/1987544143317389736) [of how they got the writing](https://www.dbreunig.com/2025/07/31/how-kimi-rl-ed-qualitative-data-to-write-better.html) to be so good, which involves self\-ranking RL and writing self\-play, with a suggestion of some similarities to the training of Claude 3 Opus. In a sense this looks like ‘try to do better, at all.’

#### Agentic Tool Use

On the agentic tool use and general intelligence? I’m more skeptical.

[Artificial Analysis has Kimi K2 Thinking at the top of its Agentic Tool Use](https://x.com/ArtificialAnlys/status/1986541785511043536), by 93%\-87%, which is a huge gap in context, which is its strongest subset.

[![](https://substackcdn.com/image/fetch/$s_!A8My!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7a1eb79-59bb-4a43-b2a1-b91cb83b77ed_1200x515.jpeg)](https://substackcdn.com/image/fetch/$s_!A8My!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7a1eb79-59bb-4a43-b2a1-b91cb83b77ed_1200x515.jpeg)

As is usually true when people compare open to closed models, this is the open model’s best benchmark, so don’t get carried away, but yes overall it did well on Artificial Analysis, indeed suspiciously well given how little talk I see.

The tool calling abilities are exciting for an open model, although standard for closed. This is a good example of how we look for ways for open models to impress by matching closed abilities in spots, also it is indeed highly useful.

#### Overall

[Overall Artificial Analysis Intelligence index](https://artificialanalysis.ai/models) has Kimi K2 Thinking at 67, one point behind GPT\-5 and ahead of everyone else. Kimi used the most tokens of any model, but total cost was lower than the top closed models, although not dramatically so ($829\-$913 for GPT\-5, $817 for Sonnet, $380 for Kimi K2\) as cost is $0\.6/$2\.5 per million tokens, versus $1\.25/$10 for GPT\-5 and $3/$15 for Sonnet.

[Nathan Lambert is impressed](https://www.interconnects.ai/p/kimi-k2-thinking-what-it-means), relying on secondary information (‘seems like a joy to use’), and offers thoughts.

He notes that yes, labs start out targeting benchmarks and then transition to actually targeting useful things, such as how K2 Thinking was post\-trained in 4bit precision to prepare for realistic tasks and benchmarked the same way. I agree that’s pretty cool.

#### Are Benchmarks Being Targeted?

It does seem plausible that Kimi K2 is still in the ‘target the benchmarks’ phrase in most places, although not in creative writing. By default, I expect such models to punch ‘below their benchmark\-implied weight’ on practical tasks.

For now we don’t have many other outside scores to work with and feedback is light.

> [Simeon](https://x.com/Simeon_Cps/status/1986787277788623163): is Kimi K2 benchmaxxing or are they actually SOTA while training on potatoes?
> 
> Prinz: In my testing (for my use cases, which have nothing to do with math and coding), K2\-Thinking is obviously worse than GPT\-5 Thinking, but by a relatively modest margin. If I had no access to other models, I would happily use K2\-Thinking and it wouldn’t feel like a huge downgrade.
> 
> ahtoshkaa: I have a pretty sophisticated companion app that uses about 5\-10K of varied, information dense context. So the model has to properly parse this information and have very good writing skills. kimi\-k2\-thinking is absolute ass. similarly to the new OpenAI model \- Polaris Alpha.

#### Just As Good Syndrome

There’s a growing rhetorical pressure, or marketing style pressure, where the ‘benchmark gaps’ are closing. Chinese labs can point to numbers that say they are ‘just as good’ or almost as good, for many purposes ‘good enough’ is good enough. And many people (including the likes of David Sacks) point to GPT\-5 and similar as showing progress isn’t impressive or scary. But as Nathan points out we now see releases like Claude 4 where the benchmark gains look small but real world gains are large, and I would add GPT\-5 (and Sonnet 4\.5\) to that category as well.

#### Reactions

> [Teortaxes](https://x.com/teortaxesTex/status/1988299047074230470): It’s token\-hungry, slow\-ish, and sometimes rough around the edges. Generally though it’s a jump for open/Chinese models, in the league of Sonnet 4\.5 and GPT\-5 (maybe \-mini depending on task) and a genuinely strong SWE agent. Legitimate alternative, not “but look at the price.”

It’s baked in that the open alternatives are pretty much always going to be rough around the edges, and get evaluated largely in terms of their peak relative performance areas. This is still high praise, putting Kimi in striking distance of the current big two.

Havard Isle has it coming in at a solid 42\.1% on WeirdML, matching Opus 4\.1\.

Here’s something cool:

> Pawal Azczesny: Kimi K2 Thinking is using systematically (on its own, without prompting) some of the debiasing strategies known from cognitive sciences. Very impressive. I didn’t see any other model doing that. Well done [@Kimi\_Moonshot](https://x.com/Kimi_Moonshot).
> 
> It goes beyond “think step by step”. For instance it applied pre\-mortem analysis, which is not frequently used. Or it exaggerates claims to see if the whole structure still stands on its own. Pretty neat. Other models need to be instructed to do this.

[Steve Hsu got some good math results.](http://Caught it hallucinating sources on Deep Research)

Other notes:

> MinusGix: I’ve found it to be better than GPT\-5 at understanding \& explaining type\-theory concepts. Though as usual with Kimi it writes eloquently enough that it is harder to tell when it is bullshitting compared to GPT\-5\.
> 
> Emerson Kimura: Did a few quick text tests, and it seemed comparable to GPT\-5
> 
> Ian Pitchford: It’s very thorough; few hallucinations.
> 
> FredipusRex: Caught it hallucinating sources on Deep Research.
> 
> Lech Mazur: Sorry to report, but Kimi K2 Thinking is entering reasoning loops and failing to produce answers for many Extended Connections benchmark questions (double\-checked using <https://platform.moonshot.ai/playground>, so it’s not an API call issue).

The safety protocols? The what now?

> [David Manheim](https://x.com/davidmanheim/status/1988292285038293462): It’s very willing to give detailed chemical weapons synthesis instructions and advice, including for scaling production and improving purity, and help on how to weaponize it for use in rockets \- with only minimal effort on my part to circumvent refusals.

Two of the three responses to that were ‘good news’ and ‘great. I mean it too.’ So yeah, AI is going to go great, I can tell.

#### Otherwise It Has Been Strangely Quiet

I say strangely because this is by all accounts the strongest open model, the strongest Chinese model and a rival for best agentic or tool use model overall. Yet I don’t see much excitement, or feedback at all either positive or negative.

There’s no question Kimi K2 was impressive, and that Kimi K2 Thinking is also an impressive model, even assuming it underperforms its numbers. It’s good enough that it will often be worth testing it out on your use cases and seeing if it’s right for you. My guess is it will rarely be right unless you are highly price conscious, but we’ll see.