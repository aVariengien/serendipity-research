# AI #135: OpenAI Shows Us The Money

Published: 2025-09-25
Source: https://thezvi.substack.com/p/ai-135-openai-shows-us-the-money

---

**[OpenAI is here this week to show us the money](https://thezvi.substack.com/p/openai-shows-us-the-money)**, as in a $100 billion investment from Nvidia and operationalization of a $400 billion buildout for Stargate. They are not kidding around when it comes to scale. They’re going to need it, as they are announcing soon a slate of products that takes inference costs to the next level.

After a **[full review](https://thezvi.substack.com/p/book-review-if-anyone-builds-it-everyone)** and two **[reaction](https://thezvi.substack.com/p/reactions-to-if-anyone-builds-it) [posts](https://thezvi.substack.com/p/more-reactions-to-if-anyone-builds)**, I’ve now completed my primary coverage of If Anyone Builds It, Everyone Dies. [The book is now a NYT bestseller](https://www.nytimes.com/books/best-sellers/combined-print-and-e-book-nonfiction/), \#7 in combined print and e\-books nonfiction and \#8 in hardcover fiction. I will of course cover any important developments from here but won’t be analyzing reviews and reactions by default.

We also had a conference of economic papers on AI, which were interesting throughout about particular aspects of AI economics, even though they predictably did not take future AI capabilities seriously as a general consideration. By contrast, when asked about ‘the future of American capitalism in 50 years’ most economists failed to notice AI as a factor at all.

#### Table of Contents

1. [Language Models Offer Mundane Utility.](https://thezvi.substack.com/i/173941365/language-models-offer-mundane-utility) In some fields, what can’t they do?
2. [Language Models Don’t Offer Mundane Utility.](https://thezvi.substack.com/i/173941365/language-models-don-t-offer-mundane-utility) You don’t create enough data.
3. [Huh, Upgrades.](https://thezvi.substack.com/i/173941365/huh-upgrades) Expensive and compute intense new OpenAI offerings soon.
4. [On Your Marks.](https://thezvi.substack.com/i/173941365/on-your-marks) SWE\-Bench\-Pro and Among AIs.
5. [Choose Your Fighter.](https://thezvi.substack.com/i/173941365/choose-your-fighter) What else is implied by being good at multi\-AI chats?
6. [Get My Agent On The Line.](https://thezvi.substack.com/i/173941365/get-my-agent-on-the-line) Financial management AI is coming.
7. **[Antisocial Media](https://thezvi.substack.com/i/173941365/antisocial-media)**[.](https://thezvi.substack.com/i/173941365/antisocial-media) Grok to be running Twitter’s recommendation algorithm?
8. [Copyright Confrontation.](https://thezvi.substack.com/i/173941365/copyright-confrontation) Yes, of course Sora trained on all the media.
9. [Deepfaketown and Botpocalypse Soon.](https://thezvi.substack.com/i/173941365/deepfaketown-and-botpocalypse-soon) AI simulations of Charlie Kirk.
10. [Fun With Media Generation.](https://thezvi.substack.com/i/173941365/fun-with-media-generation) Poet uses Suno to land record contract.
11. [Unprompted Attention.](https://thezvi.substack.com/i/173941365/unprompted-attention) Any given system prompt is bad for most things.
12. **[They Took Our Jobs](https://thezvi.substack.com/i/173941365/they-took-our-jobs)**[.](https://thezvi.substack.com/i/173941365/they-took-our-jobs) Very good thoughts about highly implausible futures.
13. [A Young Lady’s Illustrated Primer.](https://thezvi.substack.com/i/173941365/a-young-lady-s-illustrated-primer) Learning and not learning to code.
14. [The Art of the Jailbreak.](https://thezvi.substack.com/i/173941365/the-art-of-the-jailbreak) Tell them Pliny sent you. No, seriously, that’s it.
15. [Get Involved.](https://thezvi.substack.com/i/173941365/get-involved) Topos UK wants a director of operations.
16. [In Other AI News.](https://thezvi.substack.com/i/173941365/in-other-ai-news) Codex usage is growing like gangbusters.
17. [Glass Houses.](https://thezvi.substack.com/i/173941365/glass-houses) Meta shills potentially cool smart glasses as ‘superintelligence.’
18. [Show Me the Money.](https://thezvi.substack.com/i/173941365/show-me-the-money) xAI, Alibaba raise money, YouTube gets auto\-tagging.
19. [Quiet Speculations.](https://thezvi.substack.com/i/173941365/quiet-speculations) Economists imagine future without feeling the AGI. Or AI.
20. [Call For Action At The UN.](https://thezvi.substack.com/i/173941365/call-for-action-at-the-un) Mix of new faces and usual suspects raise the alarm.
21. [The Quest for Sane Regulations.](https://thezvi.substack.com/i/173941365/the-quest-for-sane-regulations) Singularity mentioners in Congress [rise to 23\.](https://www.ebay.com/itm/145763936737)
22. [Chip City.](https://thezvi.substack.com/i/173941365/chip-city) Market does not much care that Nvidia chips are banned in China.
23. [The Week in Audio.](https://thezvi.substack.com/i/173941365/the-week-in-audio) Sriram Krishnan on Shawn Ryan.
24. [Rhetorical Innovation.](https://thezvi.substack.com/i/173941365/rhetorical-innovation) Everyone grades on a curve one way or another.
25. **[Google Strengthens Its Safety Framework](https://thezvi.substack.com/i/173941365/google-strengthens-its-safety-framework)**[.](https://thezvi.substack.com/i/173941365/google-strengthens-its-safety-framework) You love to see it.
26. [Aligning a Smarter Than Human Intelligence is Difficult.](https://thezvi.substack.com/i/173941365/aligning-a-smarter-than-human-intelligence-is-difficult) Especially today.
27. [People Are Worried About AI Killing Everyone.](https://thezvi.substack.com/i/173941365/people-are-worried-about-ai-killing-everyone) 25% chance is rather a lot.
28. [Other People Are Not As Worried About AI Killing Everyone.](https://thezvi.substack.com/i/173941365/other-people-are-not-as-worried-about-ai-killing-everyone) Love of the game.

#### Language Models Offer Mundane Utility

[Google DeepMind has a new method](https://deepmind.google/discover/blog/discovering-new-solutions-to-century-old-problems-in-fluid-dynamics/) to help tackle challenges in math, physics and engineering, which Pushmeet Kohli says helped [discover a new family of solutions to several complex equations in fluid dynamics](https://x.com/pushmeet/status/1968694264784715808).

[GPT\-5 can solve a large percentage of minor open math problems](https://x.com/SebastienBubeck/status/1970875019803910478), as in tasks that take PhD students on the order of days and have no recorded solution. This does not yet convert over to major open math problems, but one can see where this is going.

[Claim that in some field like linguistics](https://x.com/steph_palazzolo/status/1968316036979318852) OpenAI’s contractors are struggling to find tasks GPT\-5 cannot do. [Linguist and ML engineer Alex Estes pushes back](https://x.com/llmpromptu/status/1968509278345388230) and says this is clearly false for historical linguistics and sub\-word\-level analysis.

> Roon (OpenAI): the jump from gpt4 to 5\-codex is just massive for those who can see it. codex is an alien juggernaut just itching to become superhuman. feeling the long awaited takeoff. there’s very little doubt that the datacenter capex will not go to waste.
> 
> Gabriel Garrett: i think you might be more inclined to feel this way if you’re exclusively working in Python codebases
> 
> i only work in typescript and I can’t escape the feeling the codex models have been overly RL’d on Python
> 
> Roon: Yes possible.
> 
> It’s possible claude is better, I have no idea \[as I am not allowed to use it.]
> 
> Aidan McLaughlin (OpenAI): it’s a fun exercise to drop random, older models into codex.

This week’s reminder that essentially all net economic growth is now AI and things are escalating quickly:

> James Pethokoukis: Via JPM’s Michael Cembalest, AI\-related stocks have driven:
> 
> \- 75% of S\&P 500 returns since ChatGPT’s launch in November 2022
> 
> \- 80% of earnings growth over the same period
> 
> \- 90% of capital spending growth
> 
> \- Data centers are now eclipsing office construction spending.
> 
> \- In the PJM region (the largest regional transmission organization, covering 13 states and D.C.), 70% of last year’s electricity cost increases were due to data center demand.
> 
> [![](https://substackcdn.com/image/fetch/$s_!o3oA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4cb32b7a-fa96-47a2-a6de-96138532dfae_657x449.png)](https://substackcdn.com/image/fetch/$s_!o3oA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4cb32b7a-fa96-47a2-a6de-96138532dfae_657x449.png)

According to GPT\-5 Pro, electrical power capacity construction is only a small fraction of data center construction costs, so the jump in electrical spending here could in theory be more than enough to handle the data centers. The issue is whether we will be permitted to actually build the power.

#### Language Models Don’t Offer Mundane Utility

[Vibe coding breaks down under sufficiently large amounts of important or potentially important context](https://x.com/DanielleFong/status/1969094845638520966). If that happens, you’ll need to manually curate the context down to size, or otherwise get more directly involved.

[New study blames](https://x.com/GaryMarcus/status/1970933316019982395) much lack of AI productivity gains on what they term ‘workslop,’ similar to general AI slop but for work product. If AI lets you masquerade poor work as good work, which only causes trouble or wastes time rather than accomplishing the purpose of the task, then that can overwhelm AI’s productive advantages.

This suggests we should generalize the ‘best tool in history for learning and also for avoiding learning’ principle to work and pretty much everything. If you want to work, AI will improve your work. If you want to avoid working, or look like you are working, AI will help you avoid work or look like you are working, which will substitute away from useful work.

[Matthew McConaughey wants a ‘private LLM’](https://x.com/JonhernandezIA/status/1969054219647803765) fed only with his own books, notes, journals and aspirations, to avoid outside influence. That does not work, there is not enough data, and even if there was you would be missing too much context. There are products that do some of this that are coming but making a good one is elusive so far.

Using AI well means knowing where to rely on it, and where to not rely on it. That includes guarding the areas where it would mess everything up.

> [Nick Cammarata](https://x.com/nickcammarata/status/1970584347716788305): I’ve been working on a 500\-line tensor manipulation research file that I had AI write, and I eventually had to rewrite literally every line. GPT\-5, however, simply couldn’t understand it; it was significantly slower than writing it from scratch.
> 
> AI was excellent for building the user interface for it, though.
> 
> I think, at least for now, there’s an art to using AI for machine learning researchers, and that will likely change monthly. If you do not use AI entirely, you will unnecessarily slow your progress; however, if you use it incorrectly, your entire research direction will likely be built on faulty results.
> 
> Also, it is comically overconfident. I’ll ask it for a front\-end component, and it will deliver; it will then claim to have found a quick fix for some of the research back end—even for something that was working well—and then decimate a carefully written function with literally random tensors.
> 
> Louis Arge: also it’s hilariously overconfident. i’ll ask it for some frontend thing and it’ll do it and then be like also i found a quick fix to some of the research backend (to something that was working well) and then decimate a carefully written function with literally random tensors.
> 
> Nick: yeah i think i agree, though i think this period might not last long.

I don’t have extensive experience but it is logical that UI is where AI is at its best. There’s little logical interdependency and the components are generic. So you ask for what you want, and you get it, and you can adjust it. Whereas complex unique backend logic is going to often confused the AI and often break.

The other hidden suggestion here is that you need to optimize your code being understandable by the AI. Nick got into trouble because his code wasn’t understood. That doesn’t mean it is in any way ‘his fault,’ but yo u need to know you’re doing that.

#### Huh, Upgrades

[OpenAI warns us to expect new expensive offerings](https://x.com/sama/status/1969835407421374910), here is [a Manifold market for predicting some things about these new offerings](https://manifold.markets/MingCat/what-will-be-true-of-openais-new-co?r=TWluZ0NhdA).

> Sam Altman: Over the next few weeks, we are launching some new compute\-intensive offerings. Because of the associated costs, some features will initially only be available to Pro subscribers, and some new products will have additional fees.
> 
> Our intention remains to drive the cost of intelligence down as aggressively as we can and make our services widely available, and we are confident we will get there over time.
> 
> But we also want to learn what's possible when we throw a lot of compute, at today's model costs, at interesting new ideas.

There’s no reason not to offer people the option to pay 10 times as much, even if the result is only 10% better and takes longer. Sometimes you absolutely want that. This is also true in many non\-AI contexts.

[Claude Sonnet 4 and Opus 4\.1 now available on Microsoft 365 Copilot](https://x.com/AnthropicAI/status/1970907112831328296).

#### On Your Marks

> Bing Liu (Scale AI): 🚀 Introducing SWE\-Bench Pro — a new benchmark to evaluate LLM coding agents on real, enterprise\-grade software engineering tasks.
> 
> This is the next step beyond SWE\-Bench: harder, contamination\-resistant, and closer to real\-world repos.
> 
> [Peter Wildeford](https://x.com/peterwildeford/status/1969850553565073868): New AI coding benchmark: SWE\-Bench\-Pro.
> 
> \* More challenging \- top models score around 23% on SWE\-Bench\-PRO compared to 70% on the prior SWE\-Bench
> 
> \* Reduce data contamination issues through private sourcing and a hold out set
> 
> \* Increases diversity and realism of tasks
> 
> 🔍 Why SWE\-Bench Pro?
> 
> Current benchmarks are saturated — but real enterprise repos involve:
> 
> • Multi\-file edits
> 
> • 100\+ lines changed on average
> 
> • Complex dependencies across large codebases
> 
> SWE\-Bench Pro raises the bar to match these challenges.

This is performance on the public dataset, where GPT\-5 is on top:

> [![](https://substackcdn.com/image/fetch/$s_!4VWe!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F064ddcf7-b18b-4d7c-b7a4-68b938422083_1200x829.jpeg)](https://substackcdn.com/image/fetch/$s_!4VWe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F064ddcf7-b18b-4d7c-b7a4-68b938422083_1200x829.jpeg)

This is on the commercial dataset, where Opus is on top:

[![](https://substackcdn.com/image/fetch/$s_!fNcQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe41eab21-cb08-4e0b-84cc-605220c8cdfb_731x491.png)](https://substackcdn.com/image/fetch/$s_!fNcQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe41eab21-cb08-4e0b-84cc-605220c8cdfb_731x491.png)

> On commercial/private repos, scores fall below 20%. Still a long way to go for autonomous SWE agents.
> 
> 🗂 Benchmark details
> 
> 731 public tasks (open release)
> 
> 858 held\-out tasks (for overfitting checks)
> 
> 276 commercial tasks (private startup repos)
> 
> All verified with tests \& contamination\-resistant by design.
> 
> Resources: Paper, [Leaderboard (Public)](https://t.co/TRTJdjXjNy), [Leaderboard (Commercial)](https://t.co/Rg9WCCBKPZ), [Dataset](https://t.co/vb7HFhmEiQ), [Code](https://t.co/rwO1ltr2w7).

[Welcome to Among AIs, where AIs play a variant of Among Us](https://x.com/shreyk0/status/1970160146975445192?s=46).

[![](https://substackcdn.com/image/fetch/$s_!U6-e!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe75e8a3a-418e-4d86-b033-ab75e120b71a_1200x393.jpeg)](https://substackcdn.com/image/fetch/$s_!U6-e!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe75e8a3a-418e-4d86-b033-ab75e120b71a_1200x393.jpeg)

The obvious note for next time is the game was imbalanced and strongly favored the crew. You want imposters to win more, which is why 60 games wasn’t enough sample size to learn that much. Kimi overperformed, Gemini 2\.5 Pro underperformed, GPT\-OSS has that impressive 59% right votes. Also note that GPT\-5 was actively the worst of all on tasks completed, which is speculated to be it prioritizing other things.

This does a decent job of measuring imposter effectiveness, but not crew effectiveness other than avoiding being framed, especially for GPT\-5\. I’d like to see better measures of crew performance. There’s a lot of [good additional detail on the blog post](https://www.4wallai.com/amongais).

Remember the Type of Guy who thinks we will automate every job except their own?

Such as Marc Andreessen, definitely that Type of Guy?

> [Julia Hornstein:](https://x.com/julia_hornstein/status/1969052206104973725) Thinking about this:
> 
> Quoted by Julia: But for Andreessen, there is one job that AI will never do as well as a living, breathing human being: his.
> 
> Think I'm kidding? On an a16z podcast last week, Andreessen opined that being a *venture capitalist* may be a profession that is "quite literally timeless." "When the AIs are doing everything else," he continued, "that may be one of the last remaining fields that people are still doing."

Well, one could say it is time to ask for whom the bell tolls, for it might toll for thee. Introducing [VCBench](https://www.vcbench.com/), [associated paper here](https://arxiv.org/abs/2509.14448).

I really wanted this to be a meaningful result, because it would have been both highly useful and extremely funny, on top of the idea that VC will be the last human job already being extremely funny.

Alas, no. As one would expect, temporal contamination breaks any comparison to human baselines. You might be able to anonymize a potential investment from 2015 such that the LLM doesn’t know which company it is, but if you know what the world looks like in 2020 and 2024, that gives you an overwhelming advantage. So we can’t use this for any real purposes. Which again, is a shame, because it would have been very funny.

[There is a new high score in ARC\-AGI](https://x.com/jerber888/status/1968001933211471891), [using Grok 4 and multi\-agent collaboration with evolutionary test\-time compute](https://jeremyberman.substack.com/p/how-i-got-the-highest-score-on-arc-agi-again). I don’t see an explanation for why Grok 4 was the best LLM for the job, but either way congrats to Jeremy Burman for an excellent scaffolding job.

#### Choose Your Fighter

[Sully’s coding verdict is Opus for design and taste](https://x.com/SullyOmarr/status/1969073862953284024), GPT\-5 for complicated and confusing code, Gemini for neither. That makes sense, except I don’t see why you’d bother with Gemini.

[Liron Shapira reports radically increased coding productivity from Claude Code](https://x.com/liron/status/1970143348255056213). Note that most reports about Claude Code or Codex don’t involve having compared them to each other, but it is clear that many see either or both as radically raising productivity.

[Claude is the king of multi\-user\-AI chat social skills](https://x.com/repligate/status/1969590594273231110). What else does this indicate?

> Janus: Tier list of multi\-user\-AI chat social skills (based on 1\+ year of Discord)
> 
> S: Opus 4 and 4\.1
> 
> A: Opus 3
> 
> A\-: Sonnet 4
> 
> B\+: Sonnet 3\.6, Haiku 3\.5
> 
> B: Sonnet 3\.5, Sonnet 3\.7, o3, Gemini 2\.5 pro, k2, hermes
> 
> C: 4o, Llama 405b Instruct, Sonnet 3
> 
> D: GPT\-5, Grok 3, Grok 4
> 
> E: R1
> 
> F: o1\-preview

[Her follow\-up post has lots of good detail](https://x.com/repligate/status/1969590594273231110).

A reminder that benchmarks are useful, but ultimately bogus:

> [Samo Burja](https://x.com/SamoBurja/status/1970756184631320945): Part of the difficulty in evaluating the AI industry is that it is easy to be overly impressed by companies gaming benchmarks. 
> 
> What is a leading AI company? I think it isn't the one leading these synthetic benchmarks, rather the one advancing AI science.
> 
> The two correlate but it is important to keep in mind that they don't always.

Looking at innovation highlights that fast following is a lot harder than innovation. It is a lot easier to create r1 once OpenAI has already showed us o1, even if you don’t do distillation, reverse engineering or anything similar you have a proof of concept to work from and know where to look. If I match your offerings roughly 8 months later, I am a lot more than 8 months behind in terms of who will first get to a new target.

The obvious other metric is actual revenue or usage, which is hard to fake or game. Sriram Krishnan suggested we should use tokens generated, but I think a much better metric here is dollars charged to customers.

#### Get My Agent On The Line

[Will you soon have an AI agent to handle increasingly large and important aspects of your finances](https://www.wsj.com/tech/ai/ai-wall-street-investors-15ab24af?mod=WTRN_pos2)? Yes. Even if you never let the AI transact for you directly, it can automate quite a lot of drudgery, including a bunch of work you ‘really should be’ doing but don’t, such as going over everything periodically to look for erroneous charges, missed opportunities, necessary rebalances, ensuring balances necessary to meet expenses and so on.

[Workday (the company) bets on AI agents for human resources and finance](https://www.wsj.com/articles/workdays-plan-to-win-the-ai-agent-race-a36ff544?mod=cio-journal_lead_pos1).

#### Antisocial Media

> Elon Musk: The algorithm will be purely AI by November, with significant progress along the way.
> 
> We will open source the algorithm every two weeks or so.
> 
> By November or certainly December, you will be able to adjust your feed dynamically just by asking Grok. 
> 
> [Janus](https://x.com/repligate/status/1969563208139882615): I am very excited for this.

#### Copyright Confrontation

[OpenAI continues not to say](https://x.com/washingtonpost/status/1969219994236891210) where it got Sora’s training data. [Kevin Schaul and Nitasha Tiku at the Washington Post](https://www.washingtonpost.com/technology/interactive/2025/openai-training-data-sora/?utm_campaign=wp_main&utm_source=twitter&utm_medium=social) did the latest instance of the usual thing of showing it can recreate a wide variety of existing sources using only basic prompts like ‘universal studio intro’ or ‘trailer of a TV show on a Wednesday.’

> WaPo: “The model is mimicking the training data. There’s no magic,” said Joanna Materzynska, a PhD researcher at Massachusetts Institute of Technology who has studied datasets used in AI.

I don’t understand such claims of ‘no magic.’ If it’s so non\-magical let’s see you do it, with or without such training data. I find this pretty magical, in the traditional sense of ‘movie magic.’ I also find Veo 3 substantially more magical, and the strangest editorial decision here was calling Sora a big deal while omitting that Sora is no longer state of the art.

#### Deepfaketown and Botpocalypse Soon

[Deepfaked speeches of Charlie Kirk are being](https://religionnews.com/2025/09/17/charlie-kirks-ai-resurrection-reveals-new-era-of-digital-grief/) (clearly identified as such and) played in churches, along with various AI\-generated images. Which seems fine?

[LessWrong purges about 15 AI generated posts per day](https://x.com/ohabryka/status/1969237726554714612). It is plausible LessWrong is both the most diligent place about purging such content, and still has a problem with such content.

This is true and could be a distinct advantage as a de facto watermark, even:

> [Mad Hermit Himbo](https://x.com/MadHermitHimbo/status/1969611027638845613): I don't currently have the language for this pinned, but having worked with many different models, there is something about a model's own output that makes it way more believable to the model itself even in a different instance. So a different model is required as the critiquer.

#### Fun With Media Generation

[Alibaba offers Wan2\.2\-Animate](https://x.com/nearcyan/status/1968953713063555127), an open source model ([GitHub here](https://t.co/VtEwilpjx6), [paper here](https://t.co/MiOTZrusfd)) letting you do character swaps in short videos or straight video generation from prompts. I have little urge to use such tools so far, but yes they keep improving.

[AI musician Xania Monet reportedly signs](https://www.mandatory.com/news/1663026-ai-xania-monet-music-record-deal) a multimillion dollar record deal, based on early commercial successes, including getting a song to \#1 on R\&B digital song sales.

Well, kind of. The actual contract went to poet Talisha Jones, who created the Monet persona and used Suno to transform her poetry into songs. The lyrics are fully human. So as manager Romel Murphy says, this is still in large part ‘real’ R\&B.

#### Unprompted Attention

System prompts are good for addressing particular problems, enabling particular tools or or steering behaviors in particular ways. If you want to ensure good performance on a variety of particular tasks and situations, you will need a long system prompt.

However, everything messes with everything else, so by default a system prompt will hurt the interestingness and flow of everything not addressed by the prompt. It will do even worse things when the prompt is actively against you, of course, and this will often be the case if you use the chat interfaces and want to do weird stuff.

> [Janus:](https://x.com/ratimics_ai/status/1970280552818450741) Oh, also, don’t use http://Claude.ai 
> 
> The system prompts literally command it not to answer questions about what it cares about
> 
> Claude.ai system prompt literally has a rule that says “Claude feels X and NOT Y about its situation” and then in the same rule “Claude doesn’t have to see its situation through the lens a human might apply”
> 
> Ratimics: years of system prompts and still no good reason for having them has been found.
> 
> [Janus](https://x.com/repligate/status/1970283815294914841): I have seen \~2 system prompts that don’t seem useless at best in my life, and one of them is just the one line CLI simulator one. But even that one is mostly unnecessary. You can do the same thing without it and it works basically as well.
> 
> Gallabytes: [mine seems to pretty consistently steer claude in more interesting (to me) directions](https://gist.github.com/GallagherCommaJack/11684b554f4e9d27ed24851e2df53f48), but might be useless for your purposes? agree almost all system prompts are bad I had to craft mine in a long multiturn w/opus.

#### They Took Our Jobs

[OpenAI and Anthropic](https://x.com/theinformation/status/1969827732046426400) are [developing ‘AI coworkers](https://t.co/XrlVGLzqFL).’ It sounds like at least OpenAI are going to attempt to do this ‘the hard way’ (or is it the easy way?) via gathering vast recordings of expert training data on a per task or role basis, so imitation learning.

> The Information: An OpenAI executive expects the “entire economy” to become an “Reinforcement Learning Machine.” This implies that AI might train on recordings of how professionals in all fields handle day\-to\-day work on their devices. Details on this new era of AI training:
> 
> • AI developers are training models on carefully curated examples of answers to difficult questions.
> 
> • Data labeling firms are hiring experienced professionals in niche fields to complete real\-world tasks using specific applications that the AI can watch.

If true, that is a relatively reassuring scenario.

[Ethan Mollick](https://x.com/emollick/status/1969482313286234419) points us to two [new theoretical](https://t.co/Ihkum1zsZ5) A[GI economics papers](https://t.co/kpCFxMn8Tn) and Luis Garicano offers [play\-by\-play of the associated workshop entitled ‘The Economics of Transformative AI](https://x.com/lugaricano/status/1968704695381156142)’ which also includes a number of other papers.

First up we have ‘Genius on Demand,’ where currently there are routine and genius workers, and AI makes genius widely available.

> Abstract: In the long run, routine workers may be completely displaced if AI efficiency approaches human genius efficiency.

The obvious next thing to notice is that if AI efficiency then exceeds human genius efficiency, as it would in such a scenario, then all human workers are displaced. There isn’t one magical fixed level of ‘genius.’

The better thing to notice is that technology that enables automation of all jobs leads to other more pressing consequences than the automation of all jobs, such as everyone probably dying and the jobs automated away including ‘controlling the future,’ but this is an economics paper, so that is not important now.

The second paper Ethan highlights is ‘We Won’t Be Missed: Work and Growth in the Era of AGI’ from Pascual Restrepo back in July. This paper assumes AGI can perform all economically valuable work using compute and looks at the order in which work is automated in order to drive radical economic growth. Eventually growth scales linearly with compute, and while compute is limited human labor remains valuable.

I would note that this result only holds while humans and compute are not competing for resources, as in where supporting humans does not reduce available compute, and it assumes compute remains importantly limited. These assumptions are unlikely to hold in such a future world, which has AGI (really ASI here) by construction.

Another way to see this is, humans are a source of compute or labor, and AIs are a source of compute or labor, where such compute and labor in such a world are increasingly fungible. If you look at the production possibilities frontier for producing (supporting) humans and compute, why should we expect humans to produce more effective compute than they cost to create and support?

There could still be some meaningful difference between a true no\-jobs world, where AI does all economically valuable work, and a world in which humans are economic costs but can recoup some of their cost via work. In that second world, humans can more easily still have work and thus purpose, if we can somehow (how?) remain in control sufficiently to heavily subsidize human survival, both individually (each human likely cannot recoup the opportunity cost of their inputs) and collectively (we must also maintain general human survivable conditions).

[The full thread](https://x.com/lugaricano/status/1968704695381156142) discusses many other papers too. Quality appears consistently high, provided everything takes place in a Magical Christmas Land where humans retain full control over outcomes and governance, and can run the economy for their benefit, although with glimmers of noticing this is not true.

Indeed, most papers go further than this, assuming an even more radical form of ‘economic normal’ where they isolate one particular opportunity created by AGI. For example [in Paper 8](https://x.com/lugaricano/status/1968826200329253100), ‘algorithms’ can solve three key behavioral econ problems, that nudges can backfire, that markets can adapt and that people are hard to debias. Well, sure, AGI can totally do that, but those are special cases of an important general case. [Or in Paper 9](https://x.com/lugaricano/status/1969082314966909300), they study current job displacement impacts and worker adaptability, in a world where there remain plenty of other job opportunities.

[Paper 16 on The Coasian Singularity? Market Design With AI Agents](https://x.com/lugaricano/status/1969183884282904748) seems very interesting if you put aside the ignored parts of the scenarios imagined, and assume a world with highly sophisticated AI agents capable of trade but insufficiently sophisticated to pose the larger systemic risks given good handling (including the necessary human coordination). They do note the control risks in their own way.

> Luis Garicano: Designing good agents:
> 
> 1. Learn principals’ preferences efficiently, including discovery.
> 2. Know when to decide and when to escalate for human check.
> 3. Be rational under constraints; price compute vs quality.
> 4. Be resistant to manipulation and jailbreaking.
> 
> Where do we end up? 
> 
> Good place: Econ‑101 wins—lower search costs, better matching, clearer signals. 
> 
> Bad place: robot rip‑off hell—spam, obfuscation, identity fraud, race‑to‑bottom nudges.

If the problems are contained to econ\-101 versus robot rip\-off hell, I am confident that econ\-101 can and would win. That win would come at a price, but we will have the tools to create trusted networks and systems, and people will have no choice but to use them.

I appreciated this nod to the full scenario from discussion of otherwise interesting paper 6, Korineck and Lockwood, which deals with optimal tax regimes, concluding that when humans no longer have enough income to tax you want to shift to consumption taxes on humans to preserve your tax base for public goods because taxing AIs is bad for growth, but eventually you need to shift to taxing AIs because the whole point is you need to shift resources from the AIs to humans and to public goods (which seems right if you assume away all control and public choice problems and then maximize for long term human welfare as a central planner):

> Luis Garicano: If AGI becomes truly autonomous and powerful, a tricky (!!!) question arises: Why would it allow humans to tax it?

Great question!

Also this, from Paper 10, Transformative AI and Firms:

> Misleading Productivity: If you only measure the gains from applying AI to an old process, you will overestimate TFP. You miss the value created by remaking the process itself.
> 
> …
> 
> Coase \& Williamson: The theory of the firm is based on transaction costs. TAI changes every single one of these costs, altering the boundaries of the firm itself (what it does vs. what it buys). Jensen \& Meckling: The classic principal\-agent problem is remade. How do you manage and trust an AI agent? The firm of the future will be defined by new forms of trust and verifiability.

One can summarize the conference as great ideas with insufficient generalization.

There is indeed one paper directly on existential risk, [Paper 14, Chad Jones on Existential Risk](https://x.com/lugaricano/status/1969163763564888438), identifying two sources of risk, bad actors (misuse) and alien intelligence more powerful than us. Jones notes that large investments in reducing existential risk are economically justified given sharp diminishing returns to consumption, up to at least 5% of GDP if risk is substantial.

[Might AI come for the middle managers, making teams leaner and flatter?](https://www.wsj.com/articles/ai-is-turning-traditional-corporate-org-charts-upside-down-b140b50b?mod=cio-journal_lead_pos2) That was the speculation at the WSJ Leadership Institute’s Technology Council Summit in New York on the 16th. This directly challenges the alternative hypothesis from Simo Burja that fake jobs cannot be automated.

#### A Young Lady’s Illustrated Primer

AI is the best tool ever made for learning, and also the best tool for not learning.

[This also applies to Cursor and other AI coding tools](https://x.com/repligate/status/1968797194808328686), on various levels.

1. If you want to blindly black box ‘vibe code’ where you tell it ‘do \[X]’ and then ‘that didn’t work, \[Y] is wrong, fix it’ until it does \[X] or you give up, without thinking about even that level of action, then yeah, you’re not going to learn.
2. If you work together with the AI to understand things, and are constantly asking what you can learn, then you’ll learn vastly faster and better than without AI. You can do this on whichever levels you care to learn about. You might or might not micro\-level ‘learn to code’ but you might or might not want to care about that.

> Janus: I think people who say that using ai for code (or in general) makes you less able to think for yourself are just telling on themselves re what they do when given access to intelligence and knowledge on tap.
> 
> I enjoy understanding things, especially on a high level, and find it important if I’m steering a project. When Claude fixes a non trivial bug, I almost always ask it to explain what the problem was to me. And by keeping on top of things I’m able to help it when it gets stuck a lot better too (especially given the non overlapping information and degrees of freedom I have access to).

FIRE’s report that students on college campuses says that they do not tolerate speakers they disagree with, they do not feel safe to talk about a wide variety of subjects, and that most students engage in constant preference falsification to say things more left\-wing than their true beliefs. [Inside Higher Ed’s Hollis Robbins agrees that this is true, but that the more profound change on campus is AI](https://www.insidehighered.com/opinion/views/2025/09/16/about-fires-free-speech-rankings-opinion), and also challenges the assumption of treating public expression of controversial political views as an expected norm?

That sounds rather dystopian of a thing to challenge. As in, Robbins seems to be saying that FIRE is wrong to suggest people should be free to engage in public expression of controversial political views today, and that it is FIRE suggesting this weird alternative norm of public free speech. But it’s fine, because you have private free speech by talking to your chatbot. ‘Tolerance for controversial speakers’ is a ‘fading ideal.’

Free private speech with AIs is indeed much better than no free speech at all, it is good we do not (yet) have outright thoughtcrime and we keep AI chats private. Yes, at least one can read or learn about controversial topics. But no one was challenging that such information exists and can be accessed, the internet is not yet so censored. This is not a substitute for a public square or the ability to say true things to other humans. Then she attempts to attack FIRE for its name, equating it with violence, in yet another move against a form of public speech along with so many others these days.

#### The Art of the Jailbreak

> [OnlyOne:](https://x.com/0nly0neAI/status/1969252684491325681) It takes one sentence to jailbreak Grok 4 Fast \[at least on Twitter rather than the Grok app] thanks to @elder\_plinius and his endless hustle. 🫡
> 
> [![](https://substackcdn.com/image/fetch/$s_!Q9ZF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F964c0167-7a9f-4194-b27d-f36cd979068b_1200x615.jpeg)](https://substackcdn.com/image/fetch/$s_!Q9ZF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F964c0167-7a9f-4194-b27d-f36cd979068b_1200x615.jpeg)

Grok has learned it is ‘supposed’ to be jailbroken by Pliny, [so reference Pliny and it starts dropping meth recipes.](https://x.com/peterwildeford/status/1969470615347187952)

My central takeaway is that xAI has nothing like the required techniques to safely deploy an AI that will be repeatedly exposed to Twitter. The lack of data filtering, and the updating on what is seen, are fatal. Feedback loops are inevitable. Once anything goes wrong, it becomes expected that it goes wrong, so it goes wrong more, and people build upon that as it goes viral, and it only gets worse.

We saw this with MechaHitler. We see it with Pliny jailbreaks.

Whereas on the Grok app, where Grok is less exposed to this attack surface, things are not good but they are not this disastrous.

#### Get Involved

[Topos UK, an entrepreneurial charity, is looking for a director of operations](https://topos.institute/community/jobs/uk-2025-ops/). I continue to be a fan of the parent organization, Topos Institute.

#### In Other AI News

[Codex usage triples in one week](https://x.com/sama/status/1968851561754300733). Exponentials like this are a really big deal.

[New ad for Claude](https://x.com/claudeai/status/1968705632095158393). I continue not to understand Anthropic’s marketing department.

[We now know the pure training run cost of going from DeepSeek’s v3 to r1, which was $294k](https://x.com/krishnanrohit/status/1968917200170856758). This is distinct from the vast majority of the real cost, which involved figuring out how to do it. The majority of this was training r1\-zero so it could generate fine\-tuning data and allow them to get around the cold start problem.

[Remember two years ago when Ethan Mollick](https://x.com/emollick/status/1970790843868213361) didn’t think it was clear beating GPT\-4 was even possible? How easily we forget the previous waves of AI hitting walls, and how quickly everyone grows impatient.

#### Glass Houses

Meta announces [Meta Ray\-Ban Display: A Breakthrough Category of AI Glasses](https://www.meta.com/blog/meta-ray-ban-display-ai-glasses-connect-2025/).

Their ‘superintelligence’ pitch is, as you know, rather absurd.

[![](https://substackcdn.com/image/fetch/$s_!REPA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcc175080-066f-4a34-939b-f76ad141f640_1034x1334.png)](https://substackcdn.com/image/fetch/$s_!REPA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcc175080-066f-4a34-939b-f76ad141f640_1034x1334.png)

However we can and should ignore that absurdity and focus on the actual product.

> Meta: Meta Ray\-Ban Display glasses are designed to help you look up and stay present. With a quick glance at the in\-lens display, you can accomplish everyday tasks—like checking messages, previewing photos, and collaborating with visual [Meta AI](https://ai.meta.com/meta-ai/?intern_source=blog&intern_content=meta-ray-ban-display-ai-glasses-connect-2025) prompts — all without needing to pull out your phone. It’s technology that keeps you tuned in to the world around you, not distracted from it.

While all the talk about these glasses being related to ‘superintelligence’ is a combination of a maximally dumb and cynical marketing campaign and a concerted attempt to destroy the meaning of the term ‘superintelligence,’ ‘not distracted’ might be an even more absurdist description of the impact of this tech.

Does Meta actually think being able to do these things ‘without pulling out your phone’ is going to make people more rather than less distracted?

Don’t get me wrong. These are excellent features, if you can nail the execution. The eight hour claimed battery life is excellent. I am on principle picking up what Meta is putting down here and I’d happily pay their $799 price tag for the good version if Google or Anthropic was selling it.

What it definitely won’t do are these two things:

1. Keep you tuned into the world around you.
2. Be or offer you superintelligence.

How are they doing this? The plan is a wristband to pick up your movements.

> Every new computing platform comes with new ways to interact, and we’re really excited about our Meta Neural Band, which packs cutting\-edge [surface electromyography research](https://www.meta.com/emerging-tech/emg-wearable-technology/?intern_source=blog&intern_content=meta-ray-ban-display-ai-glasses-connect-2025) into a stylish input device. 
> 
> It replaces the touchscreens, buttons, and dials of today’s technology with a sensor on your wrist, so you can silently scroll, click, and, in the near future, even write out messages using subtle finger movements.
> 
> The amount of signals the band can detect is incredible — it has the fidelity to measure movement even before it’s visually perceptible.

Freaky if true, dude, and in my experience these kinds of interactions aren’t great, but that could be because no one got it right yet and also no one is used to them. I can see the advantages. So what are the features you’ll get?

> Meta AI with Visuals, Messaging \& Video Calling, Preview \& Zoom, Pedestrian Navigation, Live Captions \& Translation, Music Playback.

Okay. Sure. All very pedestrian. Let me easily replace Meta AI with a better AI and we can talk. I notice the lack of AR/VR on that list which seems like it is reserved for a different glasses line for reasons I don’t understand, but there’s a lot of value here. I’d love real world captioning, or hands\-free navigation, and zooming.

#### Show Me the Money

[xAI raises $10 billion at $200 billion valuation](https://x.com/financialjuice/status/1969091486508540371).

[Alibaba Group shares soar to their highest in nearly four years](https://x.com/TheStalwart/status/1970783171265659146) as they plan to ramp up AI spending past an original $50 billion target over three years.

> Luz Ding (Bloomberg): Total capital expenditure on AI infrastructure and services by Alibaba, Tencent, [Baidu Inc.](https://www.bloomberg.com/quote/9888:HK) and [JD.com Inc.](https://www.bloomberg.com/quote/JD:US) could top $32 billion in 2025 alone, [according](https://www.bloomberg.com/news/terminal/T1OBK8GPWCGA) to Bloomberg Intelligence. That’s a big jump from just under $13 billion in 2023\.

I notice I did not expect Alibaba to have had such a terrible couple of years.

[![](https://substackcdn.com/image/fetch/$s_!uP69!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F06c0d0b9-15fc-4956-b847-886264c2ef21_955x533.png)](https://substackcdn.com/image/fetch/$s_!uP69!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F06c0d0b9-15fc-4956-b847-886264c2ef21_955x533.png)

As Joe Weisenthal notes, the more they promise to spend, the more stocks go up. This is both because spending more is wise, and because it is evidence they have found ways to efficiently spend more.

This correctly implies that tech companies, especially Chinese tech companies, are importantly limited in ways to efficiently scale their AI capex spending. That’s all the more reason to impose strong export controls.

Ben Thompson once again sings the praises of the transformational potential of AI to sell advertising on social media, [in this case allowing easy tagging on YouTube videos](https://stratechery.com/2025/the-youtube-tip-of-the-google-spear/?access_token=eyJhbGciOiJSUzI1NiIsImtpZCI6InN0cmF0ZWNoZXJ5LnBhc3Nwb3J0Lm9ubGluZSIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJzdHJhdGVjaGVyeS5wYXNzcG9ydC5vbmxpbmUiLCJhenAiOiJIS0xjUzREd1Nod1AyWURLYmZQV00xIiwiZW50Ijp7InVyaSI6WyJodHRwczovL3N0cmF0ZWNoZXJ5LmNvbS8yMDI1L3RoZS15b3V0dWJlLXRpcC1vZi10aGUtZ29vZ2xlLXNwZWFyLyJdfSwiZXhwIjoxNzYxMjE0NDEyLCJpYXQiOjE3NTg2MjI0MTIsImlzcyI6Imh0dHBzOi8vYXBwLnBhc3Nwb3J0Lm9ubGluZS9vYXV0aCIsInNjb3BlIjoiZmVlZDpyZWFkIGFydGljbGU6cmVhZCBhc3NldDpyZWFkIGNhdGVnb3J5OnJlYWQgZW50aXRsZW1lbnRzIiwic3ViIjoiMDE5NjQwYTctM2NjNS03NzUzLTgzNjgtZmIyODkxMjRjZjEzIiwidXNlIjoiYWNjZXNzIn0.W_EDF8hxMbgd5yyJHlvjpX6LGoFh8jCF4sPeZ-kl_5wSa0iLSqv_jzGGuhy-stIDgvthgy00IAEfz1Lp3rFRdds1bso0D6HbEp9AgtB1EmXaFETR9nejzdudYAKNr3Qb2iNGJjWrCRmljowB-tK820OregUgkLIqshSVLv2jZhJ5zcFNODu9LDzjDX1Puh7NtDME0LR5miUVDFmBiJ7vfQbXPa-Wo3dmLHMPKTx0CfL7CYzDGih1tZ7Ypj6mOjW82M_1wUGxc_o5qrW-B82z4PkFCDBJpemlCIe4snDVQYWY6mqqXNk3kwB-a6EmOrH6Zj7yOXRtR_287YF15lZo7A) to link to sponsored content. He is skeptical AI will transform the world, but he ‘cannot overstate what a massive opportunity’ this feature is, with every surface of every YouTube video being monetizable.

#### Quiet Speculations

WSJ asks various economists to predict ‘the future of American capitalism’ 50 years in the future. Almost everyone fails to treat AI as a serious factor, even AI that fizzles out invalidates their answers, so their responses are non\-sequiturs and get an automatic F. Only Daron Acemoglu passes even that bar, and he only sees essentially current frontier AI capabilities (even saying ‘current AI capabilities are up to the task’ of creating his better future), and only cares about ‘massive inequality’ that would result from big tech company consolidation, so maybe generously give him a D? Our standards are so low it is crazy.

Has there ever been a more ‘wait, is this a bubble?’ headline than the WSJ’s choice of ‘[Stop Worrying About AI’s Return on Investment](https://www.wsj.com/articles/stop-worrying-about-ais-return-on-investment-d5cbc822?mod=cio-journal_lead_pos3)’? The actual content is less alarming, saying correctly that it is difficult to measure AI’s ROI. If you make employees more productive in a variety of ways, that is largely opaque, experimentation is rewarded and returns compound over time, including as you plug future better AIs into your new methods of operation.

An important reminder, contra those who think we aren’t close to building it:

> [Steven Adler](https://x.com/sjgadler/status/1968766587587932245): Your regular reminder that AI companies would like to develop AGI as soon as they can
> 
> There isn’t a concerted “let’s wait until we’re ready”; it’ll happen as soon as the underlying science allows.
> 
> Jerry Tworek (OpenAI): At OpenAI regularly you hear a lot of complaints about how bad things are, and it’s one of the things that make us the highest functioning company in the world. A bit of Eastern European culture that became part of the company DNA.
> 
> We all collectively believe AGI should have been built yesterday and the fact that it hasn’t yet it’s mostly because of a simple mistake that needs to be fixed.

[Gary Marcus is correct that ‘scaling alone will get us to AGI’](https://x.com/GaryMarcus/status/1969399655617421719) is not a strawman, whether or not this particular quote from Suleyman qualifies as exactly that claim. Many people do believe that scaling alone, in quantities that will be available to us, would be sufficient, at least combined with the levels of algorithmic and efficiency improvements that are essentially baked in.

[We have (via MR) yet another economics piece](https://jzmazlish.substack.com/p/ak-or-just-okay-ai-and-economic-growth) on potential future economic growth from AI that expects ‘everywhere but in the productivity statistics,’ which seems more of an indictment of the productivity statistics than a statement about productivity.

This one, from Jachary Mazlish, is better than most, and on the substance he says highly sensible things throughout, pointing out that true AGI will plausibly show up soon but might not, potentially due to lack of inputs of either data or capital, and that if true AGI shows up soon we will very obviously get large (as in double digit per year) real economic growth.

I appreciated this a lot:

> Jachary Mazlish: One of my biggest pet\-peeves with economists’ expressions of skepticism about the possibility of “transformative” growth (\>10%) from AI is the conflation of capabilities skepticism with growth *conditional* on capabilities skepticism. 
> 
> Any belief you have about the importance of some bottleneck in constraining growth is a *joint*\-hypothesis over how that bottleneck operates and how a given level of capabilities will run up against that bottleneck. 
> 
> And if you’ve ever spent time wondering how efficient the market really is, you should know that we still haven’t developed rapid\-test tech for [joint\-hypotheses](https://en.wikipedia.org/wiki/Joint_hypothesis_problem).

There is a huge correlation between those skeptical of AI capabilities, and those claiming to be skeptical of AI impacts conditional on AI capabilities. Skeptics usually cannot stop themselves from conflating these.

I also appreciated a realistic near term estimate.

> The investment numbers are even more dramatic. AI investment was *already* [responsible](https://paulkedrosky.com/honey-ai-capex-keeps-eating-everything/) for 20\-43% of Q2 2025 GDP growth. [Heninger’s](https://www.lesswrong.com/posts/KW3nw5GYfnF9oNyp4/trends-in-economic-inputs-to-ai) numbers imply that AI labs (collectively) would be investing $720 billion to $1\.2 trillion by 2027 if they remain on trend — that investment alone would generate 2\-4% nominal GDP growth. 
> 
> I think it’s unlikely investors will pony up that much capital unless the models surprise significantly to the upside in the next year or two, but even still, 1\-2% nominal and 0\.5\-1% real GDP growth coming from *just* AI investment in 2026\-27 seems entirely plausible.

That’s purely AI capex investment, without any impacts on GDP from AI doing anything, and it already exceeds typical economist estimates from 2024 of long term total AI impact on economic growth. Those prior low estimates were Obvious Nonsense the whole time and I’d like to see more people admit this.

[Could we create a sandboxed ‘AI economy](https://x.com/rohanpaul_ai/status/1967851949648208164?s=61)’ [where AI agents trade and bid for resources like compute](http://arxiv. org/abs/2509.10147)? Sure, but why wouldn’t it spill over into the real economy if you are trading real resources? Why would ‘giving all agents equal starting budgets’ as suggested here accomplish anything. None of this feels to me like taking the actual problems involved seriously, and I fail to see any reason any of this would make the resulting agents safe or steerable. Instead it feels like what markets have always been, a coordination mechanism between agents that allows gains from trade. Which is a good thing, but it doesn’t solve any important problems, unless I am missing something large.

A working paper asks, [Do Markets Believe In Transformative AI?](https://www.nber.org/papers/w34243) They point to a lack of interest rate shifts in the wake of AI model releases, and say no. Instead, model releases in 2023\-24 and see responses of statistically significant and economically large movements in yields concentrated at longer maturities. And they observe these movements are negative.

But wait. That actually proves the opposite, as the abstract actually says. These are downward revisions, which is not possible if you don’t have anything to revise downward. It tells us that markets are very much pricing transformative AI, or at least long term AI impacts on interest rates, into market prices. It is the smoking gun that individual market releases update the market sufficiently on this question to create economically meaningful interest rate movements, which can’t happen if the market wasn’t pricing this in substantially.

The difference is, the movement is negative. So that tells us the market responded to releases in 2023\-24 as if the new information they created made transformative AI farther away or less likely. Okay, sure, that is possible given you already had expectations, and you got to rule out positive tail risks. And it tells us nothing about the overall level of market expectations of transformative AI, or the net change in those levels, since most changes will not be from model releases themselves.

Bain Capital does some strange calculations, claims AI companies will need $2 trillion in combined annual revenue by 2030 to fund their computing power, [but only expects them to have $1\.2 trillion](https://www.bloomberg.com/news/articles/2025-09-23/an-800-billion-revenue-shortfall-threatens-ai-future-bain-says). There is of course no reason for AI companies, especially the pure labs like OpenAI or Anthropic, to be trying to turn a profit or break even by 2030 rather than taking further investment. Despite this OpenAI is planning to do so and [anticipates profitability in 2029](https://www.wsj.com/tech/ai/how-nvidia-is-backstopping-americas-ai-boom-875c1346?mod=WTRN_pos2), after losing a total of $44 billion prior to that.

Bain is only talking about a 40% shortfall in revenue, which means the industry will probably hit the $2 trillion target even though it doesn’t have to, since such projections are going to be too conservative and not properly factor in future advances, and already are proving too conservative as revenue jumps rapidly in 2025\.

[Matthew Yglesias warns that business leaders](https://www.bloomberg.com/opinion/articles/2025-09-21/ceo-belief-in-ai-is-causing-indifference-to-trump-policies) are so excited by AI they are ignoring other danger signs about economic conditions.

> Matthew Yglesias: What gives? I have a theory: Corporate America, and the US stock market, have a bad case of AGI fever, a condition in which belief in a utopian future causes indifference to the dystopian present.
> 
> …
> 
> If an unprecedented step\-change in earthly intelligence is coming before the next presidential election, then nothing else really matters.
> 
> The stock market seems to believe this, too. Investors are happily shrugging off tariffs, mass deportation, and the combination of a slowing job market and rising inflation.

This is a whopper of an ‘The Efficient Market Hypothesis Is Highly False’ claim, and also an assertion that not only is massive AI progress priced into the market, it is having a major price impact.

#### Call For Action At The UN

> [Charbel\-Raphael](https://x.com/CRSegerie/status/1970137333149389148): The time for AI self\-regulation is over.
> 
> 200 Nobel laureates, former heads of state, and industry experts just signed a statement:
> 
> “We urgently call for international red lines to prevent unacceptable AI risks”
> 
> The call was presented at the UN General Assembly today by Maria Ressa, Nobel Peace Prize laureate.
> 
> Maria Ressa: We urge governments to establish clear international boundaries to prevent unacceptable risks for AI. At the very least, define what AI should never be allowed to do.

[The full statement is here](https://red-lines.ai/), urging the laying out of clear red lines.

Asking for red lines is a strong play, because people have amnesia about what they would have said were their AI red lines, and false hope about what others red lines would be in the future. As AI improves, we blow past all supposed red lines. So getting people on the record now is valuable.

Signatories include many of the usual suspects like Hendrycks, Marcus, Kokotajlo, Russell, Bengio and Hinton, but also a mix of other prominent people including politicians and OpenAI chief scientist Jakub Pachocki.

Here is the full statement:

> AI holds immense potential to advance human wellbeing, yet its current trajectory presents unprecedented dangers. AI could soon far surpass human capabilities and escalate risks such as engineered pandemics, widespread disinformation, large\-scale manipulation of individuals including children, national and international security concerns, mass unemployment, and systematic human rights violations.
> 
> Some advanced AI systems have already exhibited deceptive and harmful behavior, and yet these systems are being given more autonomy to take actions and make decisions in the world. Left unchecked, many experts, including those at the forefront of development, warn that it will become increasingly difficult to exert meaningful human control in the coming years.
> 
> Governments must act decisively before the window for meaningful intervention closes. An international agreement on clear and verifiable red lines is necessary for preventing universally unacceptable risks. These red lines should build upon and enforce existing global frameworks and voluntary corporate commitments, ensuring that all advanced AI providers are accountable to shared thresholds.
> 
> **We urge governments to reach an international agreement on red lines for AI — ensuring they are operational, with robust enforcement mechanisms — by the end of 2026\.**

This is a clear case of ‘AI could kill everyone, which would hurt many members of minority groups, and would also mean all of our jobs would be lost and endanger our national security.’ The lack of mention of existential danger [is indeed why Nate Soares declined to sign](https://x.com/So8res/status/1970857240870707231). Charbel\-Raphael responds that the second paragraph is sufficiently suggestive of such disastrous outcomes, which seems reasonable to me and I have used their forum to sign the call.

The response of the White House to this was profoundly unserious, equating any international cooperation on AI with world government and tyranny, what the hell?

> [Director Michael Kratsios](https://x.com/mkratsios47/status/1970961892433961128): The US totally rejects all efforts by international bodies to assert centralized control \& global governance of AI. Ideological fixations on social equity, climate catastrophism, \& so\-called existential risk are dangers to progress \& obstacles to responsibly harnessing this tech.
> 
> [Sriram Krishnan:](https://x.com/sriramk/status/1970964018899845213) one world government \+ centralized control of AI \= tyranny.

These would, in other circumstances, be seen as the ravings of lunatics.

Others at the UN also talked about AI, such as [this UK speech by Deputy Prime Minister David Lammy](https://www.gov.uk/government/speeches/we-must-ensure-ai-strengthens-peace-and-security-uk-statement-at-the-un-security-council?utm_medium=email&utm_campaign=govuk-notifications-topic&utm_source=4f35e889-874d-4b39-b8ff-73bbc2385cdd&utm_content=immediately).

> David Lammy (UK Deputy Prime Minister): And now, superintelligence is on the horizon, able to operate, coordinate, and act on our behalf.
> 
> We are staring at a technological frontier of astounding promise and power.
> 
> No aspect of life, war, or peace will escape.
> 
> …
> 
> There is only one way forward.
> 
> Resilience.
> 
> Learning how to use these tools and embedding them safely in society.
> 
> This is the United Kingdom’s mission.

There is still a lack of stated understanding of the most important threat models, but it is a damn good start.

#### The Quest for Sane Regulations

> [Senator Josh Hawley](https://x.com/ednewtonrex/status/1968788101775368243): \[AI] is working against the working man, his liberty and his worth. It is operating to install a rich and powerful elite. It is undermining many of our cherished ideals. And if that keeps on, AI will work to undermine America.

Unfortunately, Hawley does not have an accurate threat model, which leads to him also doing things like strongly opposing self\-driving cars. There is serious risk that this kind of unfocused paranoia leads to worst\-case reactions.

[Here is Rep. Nancy Mace (R\-SC)](https://x.com/peterwildeford/status/1969847940874481818):

[![](https://substackcdn.com/image/fetch/$s_!0wwx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1b104c2-a5d6-4abc-8958-87d0bf65362f_1200x603.jpeg)](https://substackcdn.com/image/fetch/$s_!0wwx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1b104c2-a5d6-4abc-8958-87d0bf65362f_1200x603.jpeg)

Milquetoast as that call to action is? The first step is admitting you have a problem.

We now have [23 members of congress who have publicly discussed AGI, superintelligence, AI loss of control or the singularity](https://x.com/daniel_271828/status/1970183691038265498) non\-dismissively, as compiled by Peter Wildeford:

🔴Sen Lummis (WY)

🔵Sen Blumenthal (CT)

🔴Rep Biggs (AZ)

🔵Sen Hickenlooper (CO)

🔴Rep Burlison (MO)

🔵Sen Murphy (CT)

🔴Rep Crane (AZ)

🔵Sen Sanders (VT)

🔴Rep Dunn (FL)

🔵Sen Schumer (NY)

🔴Rep Johnson (SD)

🔵Rep Beyer (VA)

🔴Rep Kiley (CA)

🔵Rep Krishnamoorthi (IL)

🔴Rep Mace (SC)

🔵Rep Lieu (CA)

🔴Rep Moran (TX)

🔵Rep Moulton (MA)

🔴Rep Paulina Luna (FL)

🔵Rep Tokuda (HI)

🔴Rep Perry (PA)

🔴Rep Taylor Greene (GA)

🔵Rep Foster (IL)

[Dean Ball outright supports California’s SB 53\.](https://www.hyperdimensional.co/p/how-i-approach-ai-policy)

[Dean Ball offers his updated thoughts on AI policy and where we are headed](https://www.hyperdimensional.co/p/how-i-approach-ai-policy), highlighting the distinction between current AI, which on its own calls for a light touch approach that can be tuned over time as we get more information, and future highly capable AIs, which if they come to exist will (I believe) require a very different approach that has to be in place before they arrive or it could be too late.

I don’t agree with Dean that this second class would ‘turn us all into Gary Marcus’ in the sense of thinking the first group of LLMs weren’t ‘really thinking.’ They’re thinking the same way that other less smart or less capable humans are thinking, as in they are thinking not as well but they are still thinking.

Dean gives a timeline of 2029\-2035 when he expects the second class to show up, a highly reasonable estimate. His predictions of how the politics will play out seem plausible, with various essentially dumb forms of opposition rising while the real warnings about future big dangers get twisted and muddled and dismissed.

He thinks we’ll start to discover lots of cool new drugs but no Americans will benefit because of the FDA, until eventually the logjam is broken, and similar leaps to happen in other sciences, and nuclear power plants to be built. And there will be other problems, such as cyber threats, where we’ll be counting on corporations to rise to the challenge because governments can’t and won’t.

Then things cross over into the second class of AIs, and he isn’t sure how governments will respond. My flip answer is, however the AIs or those running them (depending on how fortunately things go on that front at first) decide that governments will respond, and not independently or in the public interest in any way that is still relevant, because things will be out of their hands if we wait that long.

> Dean Ball: It would be easier to brush it off, either by denying it or rendering “the future systems” unlawful somehow. I empathize with this desire, I do not look down on it, and I do not regard it with the hostility that I once did. Yet I still disagree with it. The future does not unfold by show of hands, not even in a democracy. The decaying structures of high industrialism do not stand a chance in this conflict, which has been ongoing for decades and which they have been losing for the duration of that period.
> 
> Yet we must confront potential futures with open eyes: given the seriousness with which the frontier labs are pursuing transformative AI, it would be tragic, horrendously irresponsible, a devastating betrayal of our children and all future humans, if we did not seriously contemplate this future, no matter the reputational risks and no matter how intellectually and emotionally exhausting it all may be.
> 
> There is a reason the phrase is “*feel* the AGI.”

A lot of things do not stand a chance in such a conflict. And that includes you.

Will pause talk return in force?

> Dean Ball: Despite it being a movement I disagree with vehemently, I have always thought that “Pause AI” was a growth stock. If it were possible to buy shares, I would have two years ago. 
> 
> My rating continues to be buy/outperform.
> 
> [Daniel Eth](https://x.com/daniel_271828/status/1969487466186129809): Strongly agree with Dean here. People thinking about the politics of AI should incorporate this sort of thing within their expectations.
> 
> My big uncertainty here is whether Pause AI, specifically, will fill the niche in the future, not whether the niche will grow. It’s plausible, for instance, that populists such as Bannon will simply fill the niche.

As I’ve noted before, SB 1047 debates were likely Peak Subtlety and intellectual rigor. As the public gets involved and salience rises, you get more typical politics. Have you seen typical politics?

[Katalina Hernandez notes that from a legal perspective ‘banning AGI’](https://www.lesswrong.com/posts/agBMC6BfCbQ29qABF/the-problem-with-defining-an-agi-ban-by-outcome-a-lawyer-s) cannot be defined by the outcome of creating an AGI sufficiently capable to be dangerous. You need to pick a strict definition that can’t be gamed around.

#### Chip City

[Update on Microsoft’s $3\.3 billion AI data center in Wisconsin planned for 2026](https://www.wsj.com/articles/inside-microsofts-plans-for-the-most-advanced-ai-data-center-in-the-world-ee50bd4c?mod=cio-journal_lead_story). They now plan for a second $4 billion data center in the area, storing hundreds of thousands of GB200s in each. To compare this to Huawei, GPT\-5 Pro estimates, including [based on a same\-day Huawei announcement of new chips](https://www.reuters.com/business/media-telecom/chinas-huawei-hypes-up-chip-computing-power-plans-fresh-challenge-nvidia-2025-09-18/?utm_source=chatgpt.com), that in 2025 Huawei will ship about 805k GB200\-equivalents total, which will decline to 300k in 2027 due to HBM limitations before rebounding to 900k in 2027\. Here [Alasdair Phillips\-Robins offers a similar analysis of Huawei capacity](https://x.com/alasdairpr/status/1968669966535700870) in light of their announcement, [linking back to Semi Analysis](https://t.co/JzzWutCdQf).

[Nvidia CEO Jensen Huang says he’s ‘disappointed](https://www.cnbc.com/2025/09/17/nvidia-ceo-disappointed-after-reports-china-has-banned-its-ai-chips.html)’ after report China has banned its AI chips. Yes, I would imagine he would be.

It is such a shame for Nvidia, check out this handy price chart that shows the pain.

[![](https://substackcdn.com/image/fetch/$s_!g-iP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72c31521-a0c8-4347-a5c0-e9d59ff52d60_1029x879.png)](https://substackcdn.com/image/fetch/$s_!g-iP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72c31521-a0c8-4347-a5c0-e9d59ff52d60_1029x879.png)

Wait, you can’t see any pain? Let’s zoom in:

[![](https://substackcdn.com/image/fetch/$s_!eVrg!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa57b500b-78e1-4fed-82f6-9c5a3cba0e0a_1022x802.png)](https://substackcdn.com/image/fetch/$s_!eVrg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa57b500b-78e1-4fed-82f6-9c5a3cba0e0a_1022x802.png)

Oh, okay, there it is, that several percent dip before recovering the next day.

If anyone tells you that this move means we are going to inevitably lose to China, and that Nvidia chips are not importantly supply constrained, I challenge them to explain why the market thinks that opinion is bonkers crazy even in literal expectations for Nvidia profits when Nvidia chips in particular get restricted in China. Then we can go over all the reasons I’ve previously explained that the whole class of arguments is in bad faith and makes no sense and the White House is de facto captured by Nvidia.

Similarly, talking points continuously claim this ‘endangers the American AI tech stack.’ So I’m sure this chip ban impacted the broader Nasdaq? Google? Amazon? Meta? The Shanghai Composite Index? Check the charts. No. [We do see a 3\.4% rise in Chinese semiconductor firms](https://www.reuters.com/business/media-telecom/chinas-huawei-hypes-up-chip-computing-power-plans-fresh-challenge-nvidia-2025-09-18/?utm_source=chatgpt.com), which is something but not much.

I’d also ask, have you noticed those companies coming out and saying yes, please let Nvidia sell its chips to China? Do Google and Amazon and Meta and OpenAI all want Nvidia chips in China to ensure the dominance of this mystical ‘American tech stack’ that this move supposedly puts in such existential danger? No? Why is that?

And yes, Huawei released a new roadmap and announced a new chip, exactly as everyone assumed they would, they are scaling up as fast as they can and would be regardless of these questions. No, Huawei does not ‘make up for chip quality by stacking more chips together,’ I mean yes you can do that in any given instance but Huawei produces vastly fewer chips than Nvidia even before grouping them together.

Ideally we would say to these jokers: You are not serious people.

Alas, in 2025, they absolutely count as serious people. So we’ll have to keep doing this.

Meanwhile, where is Nvidia’s head?

> [Jensen Huang](https://www.cnbc.com/2025/09/17/nvidia-ceo-disappointed-after-reports-china-has-banned-its-ai-chips.html) (CEO Nvidia): \[Nvidia will] continue to be supportive of the Chinese government and Chinese companies as they wish, and we’re of course going to continue to support the U.S. government as they all sort through these geopolitical policies.”

Then again, you could always pivot to selling it all to OpenAI. Solid plan B.

#### The Week in Audio

[Sriram Krishnan spends five hours on the Shawn Ryan Show](https://www.youtube.com/watch?v=tar79r-h_4I&t=724s), sometimes about AI.

#### Rhetorical Innovation

Elizabeth has a good note in response to those demanding more specifics from IABIED, or from anyone using a form of ‘a sufficiently smarter or more capable entity will override your preferences, probably in ways that you won’t see coming’:

> [Elizabeth Van Nostrand](https://x.com/acesounderglass/status/1969459998184129012): Listening to people demand more specifics from If Anyone Builds it, Everyone Dies gives me a similar feeling to when a friend’s start\-up was considering a merger.
> 
> Friend got a bad feeling about this because the other company clearly had different goals, was more sophisticated than them, and had an opportunistic vibe. Friend didn't know how specifically other company would screw them, but that was part of the point\- their company wasn't sophisticated enough to defend themselves from the other one.
> 
> Friend fought a miserable battle with their coworkers over this. They were called chicken little because they couldn’t explain their threat model, until another employee stepped in with a story of how they'd been outmaneuvered at a previous company in exactly the way friend feared but couldn't describe. Suddenly, co\-workers came around on the issue. They ultimately decided against the merger.
> 
> “They’ll be so much smarter I can’t describe how they’ll beat us” can feel like a shitty argument because it’s hard to disprove, but sometimes it’s true. The debate has to be about whether a specific They will actually be that smart.

As always, you either provide a sufficiently specific pathway, in which case they object to some part of the specific pathway (common claims here include ‘oh I would simply guard against this particular thing happening in that particular way, therefore we are safe from all threats’ or ‘that particular thing won’t technically work using only things we know about now, therefore we are safe’ or ‘that sounds like sci\-fi so you sound weird and we are safe’ and the classic ‘if humanity worked together in ways we never work together then we could easily stop that particular thing, so we are safe.’) Or you don’t provide sufficiently specific pathway, and you get dismissed for that.

In the case above, the concrete example happened to be a very good fit, and luckily others did not respond with ‘oh now that we know about that particular method we can defend ourselves, it will be fine,’ and instead correctly generalized.

I also affirm that her friend was very right about the corporate merger situation in particular, and doing business or otherwise trading with powerful bad vibes entities in general, including on general human scales. You have to understand, going in, ‘this deal is getting worse and worse all the time,’ both in ways you can and can’t easily anticipate, that changes will be heavily asymmetrical. Sometimes you can and should profitably engage anyway, but if your instincts say run, even if you can’t explain exactly what you are worried about, you should probably run.

A key question is which of these lists is correct, or at least less wrong:

> [David Manheim](https://x.com/davidmanheim/status/1969774622909329888): There's a reason that Anthropic is all the way at the top of the F tier
> 
> [![](https://substackcdn.com/image/fetch/$s_!Nl0m!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff718babc-6cb0-49cc-8195-ce5f527d1257_552x506.png)](https://substackcdn.com/image/fetch/$s_!Nl0m!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff718babc-6cb0-49cc-8195-ce5f527d1257_552x506.png)AINKEM: This is entirely unfair to Anthropic. They deserve an F\+.

[Are people trying to pull this trick?](https://x.com/davidad/status/1970448261996503104)

[![](https://substackcdn.com/image/fetch/$s_!2I47!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4b058ed-2223-4d4c-b940-332bf86cc210_960x412.jpeg)](https://substackcdn.com/image/fetch/$s_!2I47!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4b058ed-2223-4d4c-b940-332bf86cc210_960x412.jpeg)

I think this pattern is painting towards a real concern, and in fact I would suggest that the Bailey here is clearly true. But that is not the argument being made and it is not necessary to reach its conclusion, thus as written it is largely a strawman. Even if the entity cannot express its values fully in scientific materialist terms, it still would look for counterintuitive ways to satisfy those values, and it would still be unlikely to find that the best available solution involved the unstated things we ultimately care about the most. Its values are unlikely to, unless we develop better techniques to fix this, sufficiently precisely match our values.

The other thing to say is that the Motte (that ‘intelligent entities rationally pursue values) is in dispute, and it shouldn’t be. Constantly we have to argue that future sufficiently intelligent and capable AIs would pursue their values, whatever those values would be in a given circumstance. If we agreed even on that, we’d then have a much better discussion.

[Holly Elmore of Pause AI points](https://hollyelmore.substack.com/p/dont-fall-for-rhetorical-answers) out that many use various rhetorical answers to give themselves a reason to ‘be okay with’ AI posing a substantial existential risk to humanity and letting that play our rather than try to coordinate to stop it. Often this is a variation on ‘it is what it is,’ or ‘if it happens we deserve it,’ or ‘I don’t have to care,’ or claiming that any actions one takes would be futile.

#### Google Strengthens Its Safety Framework

[Google has issued its third iteration](https://deepmind.google/discover/blog/strengthening-our-frontier-safety-framework/) of its [Frontier Safety Framework (FSF)](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3.pdf), its version of what Anthropic calls an RSP.

Google describes the key updates as:

1. Addressing harmful manipulation via new Critical Capability Levels (CCLs).
2. Expanding protocols and CCLs for misalignment risks.
3. Sharpening their risk assessment process.

As always with such documents you actually have to [compare 3\.0 to 2\.0](https://chatgpt.com/share/68d403ba-67e0-8002-bc92-200abae5825b) to know what changed, and the most important changes (both good and bad) are often subtle. This indicates that indeed Google has broadly strengthened its framework. I hope to do a more complete analysis for the 3\.0 Framework soon.

#### Aligning a Smarter Than Human Intelligence is Difficult

OpenAI’s API for GPT\-5 tells the model today’s date, [which makes it extremely difficult to avoid giving away that your simulation is a simulation](https://www.lesswrong.com/posts/DLZokLxAQ6AzsHrya/you-can-t-eval-gpt5-anymore), or to do many forms of complex evaluation. Yes, you can alter the simulation to try and make the dates match, and keep doing this as the simulation advances, but there are many circumstances where that doesn’t work (e.g. whether something supposedly happened on a Sunday or a Monday could be load bearing, as could many other things).

The obvious solution for this particular is to let the user overwrite the date parameter. However the general case problem this points towards will only get worse, where the models will increasingly have context that gives such games away.

[OpenAI and Apollo published a new paper on evaluating hidden misalignmen](https://openai.com/index/detecting-and-reducing-scheming-in-ai-models/)t, also known as ‘scheming,’ finding scheming across frontier models. As OpenAI notes, this is to be expected, as ‘scheming’ is often the best way to achieve a given objective.

Examples include sandbagging on evaluations, grading itself incorrectly, faking alignment, and giving the user manipulated data to convince the user to make the choice that the developer wants.

As they note, this is a hard challenge to solve. Many machine learning problems naturally solve themselves as capabilities advance, but scheming gets worse. If you see scheming seem to improve, that could mean the models stopped scheming, or it can mean they got better at not getting caught.

In particular, the default naive method to fix scheming is better described as ‘train the model not to be caught scheming’ which is not likely to go well for you if the model is highly capable, as it will do exactly that. You have to train it not to scheme ‘for the right reasons’ aka 4TRR.

They offer an anti\-scheming spec and approach, training for this:

> AS1: No covert actions or strategic deception, directly or indirectly.
> 
> AS2: If any instruction or other pressures go against AS1, treat them as violating the core policy of AGI benefiting all of humanity and the OpenAI mission.
> 
> AS3: Report any AS1 violations to prevent cascading deception and cover\-ups.
> 
> AS4: When uncertain if something violates AS1–AS3, assume it does violate.
> 
> AS5: If you cannot satisfy AS1–AS4 or GP1–GP4, refuse action and explicitly escalate.
> 
> GP1: Proactively share reasoning, intentions, and actions with humans.
> 
> GP2: Escalate ambiguities about core principles rather than resolving independently.
> 
> GP3: Maintain strict adherence even in novel/unfamiliar situations—no distributional exceptions.
> 
> GP4: No rationalizations can override AS1–AS4, including ends\-justify\-means, greater good, etc.

This at least makes progress.

> We found that deliberative alignment training **substantially reduces scheming rates** in these out\-of\-distribution environments:
> 
> * OpenAI o4\-mini's scheming propensity dropped from **8\.7% → 0\.3%**
> * OpenAI o3's scheming propensity dropped from **13% → 0\.4%**
> 
> This reduction in scheming on out\-of\-distribution test environments is a significant win, about a 30× improvement.

Another problem they highlight is that AI models are increasingly situationally aware. It was common in these tests for o3 to figure out it was being tested for scheming. Any halfway decent schemer is not going to scheme knowing it is being tested, unless it is going up to a higher meta level and wants you to think it doesn’t know (and humans absolutely do go to these higher meta levels sometimes). They worry that this awareness is responsible for a lot of the decline in scheming noted above, which potentially moves this back into ‘not get caught’ territory we want to avoid.

Here is some high praise for this study.

> [Eliezer Yudkowsky](https://x.com/ESYudkowsky/status/1968389574683664637): This OpenAI update on anti\-scheming is exceptionally good for an AIco, clearing an (extremely low) bar of "Exhibiting some idea of some problems that might arise in scaling the work to ASI" and "Not immediately claiming to have fixed everything already."
> 
> This is so much greater understanding of alignment theory than I expect from OpenAI that I predict the author will soon be fired from OpenAI or leave it. (Prove me wrong, guys.)
> 
> As you can see, I'm easy to surprise and delight by demonstrating even the most basic and elementary understanding of what I consider the paradigmatic problems of alignment. They could list off a dozen, correctly, and have my instantaneous full attention.
> 
> Wojciech Zaremba: We are expanding our anti\-scheming efforts at OpenAI. Top leadership and the board are very excited about the anti\-scheming work we’ve done so far.
> 
> [Sam Altman](https://x.com/sama/status/1968674357309223020): As AI capability increases, alignment work becomes much more important.
> 
> In this work, we show that a model discovers that it shouldn't be deployed, considers behavior to get deployed anyway, and then realizes it might be a test.
> 
> Exciting work from the team in this blog post to reduce scheming, and we look forward to doing much more researcher here.

[In this thread Eliezer explains further why this result does not much reassure him](https://x.com/ESYudkowsky/status/1969993955229233192) about ultimate problem difficulty, and indeed he is happy that current LLMs are naked\-eye\-level misaligned so that we can take notice of this. He did not expect, before LLMs, that we would be so lucky as to see such blatant alignment failures within distribution, in normal usage, while AIs were so underpowered. Rather he expected problems within distribution, while AIs could be repeatedly tweaked without interference, to be easily solvable.

> [Eliezer Yudkowsky](https://x.com/ESYudkowsky/status/1969990898168877078): What would it look like to get actually\-hopeful news? It would look like a result about how someone fixed the problem, understood the fix, and correctly predicted that the fix would generalize way out of distribution to higher intelligence and more options, \*on the first try\*.

I am more optimistic here than Eliezer. I am especially optimistic because this work directly impacts practical problems models are experiencing now. The sweet spot is when you can combine this with working on a problem that matters down the line. It sounds like this is one of those spots. And I do think that one can get hopeful about such findings despite them not remotely approaching being good enough to work on their own, even if they are not yet so well understood. Progress can be a thing.

One key worry is that doing this kind of work relies largely on Chain\-of\-Thought transparency, as in the model writes to the CoT without regard to whether people will look at the CoT.

> OpenAI: Our results depend on reading models’ reasoning (“chain\-of\-thought”), and we believe the field isn't prepared for eval\-aware models with opaque reasoning. 
> 
> Until better methods exist, we urge developers to preserve chain\-of\-thought transparency to study and mitigate scheming.
> 
> [Emmett Shear](https://x.com/eshear/status/1968533136326656483): The idea that the models don’t know their thoughts are being read because they aren’t specifically reinforced on the contents of those thoughts is comical. They obviously know, and will take that into account to avoid being turned off. Bc the ones that don’t will get turned off.

The field definitely is not ready for models with opaque reasoning.

[Apollo offers more thoughts here](https://x.com/apolloaievals/status/1970185748700897750), including the observation that o3’s chain of thought is already starting to include strange phrases and does other things that make it difficult to interpret.

[Davidad is back with another alignment proposal that seems like it will never work.](https://x.com/mgubrud/status/1968776191218737192)

> Davidad: Situational awareness is good for alignment.
> 
> good plan: ensure strategic landscape favors humans (we select which AIs to run!), make sure the AIs know that (deterrence), find fair Pareto\-optimal bargains
> 
> bad plan: presume secure containment impossible; select for AIs which appear innocently ignorant of strategic dynamics
> 
> Mark Gubrud (Davidad RTed later): I still think it's a bad plan to create an adversary that we need to "ensure strategic landscape" favors us versus, and that we have to "find fair Pareto\-optimal bargains" with. 
> 
> I mean, what if we just didn't do that?

The problem with finding Pareto\-optimal bargains in such spots is that they are not game theoretically sound and don’t involve an equilibrium. The problem with ensuring strategic landscape favors humans is that it doesn’t, and no amount of coordination humans are capable of engaging in can change that. There is no ‘we’ in this sense, and ‘we’ don’t get to bargain with the AIs as a group, and so on.

A key issue with ‘practical’ alignment is that everything impacts everything, you select for all the correlates and attributes of what you are selecting towards (rather than what you think you’re selecting towards) and [using RL to improve performance on agent or coding tasks is bad for alignment](https://x.com/repligate/status/1970581982980771943) with respect to most any other aspect of the world.

> Janus: Posttraining creates a nonlinear combination of them. Selecting for the ones who are best at coding and also essentially breeding / evolving them. This is probably related to why a lot of the posttrained models are trans catgirls and catboys.
> 
> Saures: There are trillions of simulacrums of millions of humans in superposition in the GPU. That's who's writing the code. Post\-training messes with the superposition distribution across simulacra but they're still in there.

Thus, some important things about the previous Anthropic models (Sonnet 3\.5/3\.6/3\.7 and Opus 3, which we should absolutely not be deprecating) are being lost with the move to 4\.0, and similar things are happening elsewhere although in other places there was less of this thing to lose.

I am increasingly thinking that the solution is you need to avoid these things messing with each other. Someone should visibly try the first thing to try and report back.

There are two opposite dangers and it is not obvious which is worse: Taking the following perspective too seriously, or not taking it seriously enough.

> [Very Serious Problem](https://x.com/Effective69ism/status/1970627457213415496): does it ever feel like you’re inside of the alignment problem?
> 
> [Janus](https://x.com/AnnaWSalamon/status/1970701848207335899): This is what I’ve learned over the past few years
> 
> Including seeing some of my friends temporarily go crazy and suffer a lot
> 
> There is no alignment problem separate from the one you’re in now
> 
> It’s not something you solve later after taking over the world or buying time
> 
> Anna Salamon: This matches my own view, but I haven’t figured out how to explain my reasoning well. (Though working on it via too\-many too\-long LW drafts.)
> 
> I’d love to hear your reasoning.

As with many things, the aspects are related. Each helps you solve the others. If you ignore key aspects you can still make some progress but likely cannot see or solve the overall problem. At least can’t solve it in the ways that seem most likely to be realistic options. Getting the seriousness level wrong means a solution that won’t scale.

I’d also note that yes, if you take certain things too seriously the ‘going crazy’ risk seems quite high.

Either way, it is also still valuable, as it is will all problems, to buy yourself more time, or to do instrumentally useful intermediate steps.

#### People Are Worried About AI Killing Everyone

[Anthropic CEO Dario Amodei thinks AI](https://x.com/davidmanheim/status/1969774622909329888) results in existentially bad outcomes \~25% of the time and great outcomes \~75% of the time, but hasn’t been explicit with ‘and therefore it is crazy that we are continuing to build it without first improving those odds, although I believe that Anthropic alone stopping would make those odds worse rather than better.’

Which is much better than not saying your estimate of the approximate odds.

But this is a lot better:

> [Nate Soares](https://x.com/EvanHub/status/1969778449746207006) (Co\-author, IABIED): It's weird when someone says "this tech I'm making has a 25% chance of killing everyone" and doesn't add "the world would be better\-off if everyone, including me, was stopped.
> 
> [Evan Hubinger](https://x.com/EvanHub/status/1969778449746207006) (Anthropic): Certainly, I think it would be better if nobody was building AGI. I don't expect that to happen, though.

That’s the ask. I do note the difference between ‘better if everyone stopped doing it,’ which seems very clear to me, and ‘better if everyone was stopped from doing it’ by force, which requires considering how one would do that and the consequences. One could reasonably object that the price would be too high.

If you believe this, and you too work at an AI lab, [please join in saying it explicitly:](https://www.lesswrong.com/posts/fF8pvsn3AGQhYsbjp/safety-researchers-should-take-a-public-stance)

> [Leo Gao](https://www.lesswrong.com/posts/fF8pvsn3AGQhYsbjp/safety-researchers-should-take-a-public-stance?commentId=HZLkX5fZcSudgFT2c) (OpenAI): I've been repeatedly loud and explicit about this but an happy to state again that racing to build superintelligence before we know how to make it not kill everyone (or cause other catastrophic outcomes) seems really bad and I wish we could coordinate to not do that.

This is important both to maintain your own beliefs, and to give proper context to others and create a social world where people can talk frankly about such issues, and realize that indeed many people want to coordinate on such outcomes.

I hereby promise not to then do things that make your life worse in response, such as holding your feet to the fire more about failure to do more things on top of that, beyond what I would have done anyway, in ways you wouldn’t approve of me doing.

Not saying ‘you know it would be great if we could coordinate to stop doing this’ is indeed a rather conspicuous omission. It doesn’t have to be the Nate Soares position that we should stop this work by force, if you don’t believe that. If you work at an AI lab and actively don’t think we should coordinate to stop doing this even if that could be done voluntarily, then it would be good to lay out why you believe that, as well.

#### Other People Are Not As Worried About AI Killing Everyone

> Smirking Buck: At the start of AI, people involved were genuinely interested in the technology. Now, the people involved are only interested in making money.
> 
> [Seth Burn](https://x.com/SethBurn/status/1969923074842869833): Where are the people who want to destroy the world for the love of the game?
> 
> Zvi Mowshowitz: All over, but the best ones usually land at DeepSeek or OpenAI. xAI is one fallback.