# Asking (Some Of) The Right Questions

Published: 2025-10-27
Source: https://thezvi.substack.com/p/asking-some-of-the-right-questions

---

Consider this largely a follow\-up to [Friday’s post about a statement aimed at creating common knowledg](https://thezvi.substack.com/p/new-statement-calls-for-not-building?r=67wny)e around it being unwise to build superintelligence any time soon.

Mainly, there was a great question asked, so I gave a few hour shot at writing out my answer. I then close with a few other follow\-ups on issues related to the statement.

#### A Great Question To Disentangle

[There are some confusing wires potentially crossed](https://x.com/sriramk/status/1982111886188462270) here but the intent is great.

> Scott Alexander: I think removing a 10% chance of humanity going permanently extinct is worth another 25\-50 years of having to deal with the normal human problems the normal way.
> 
> [Sriram Krishnan](https://x.com/sriramk/status/1982111886188462270): Scott what are verifiable empirical things ( model capabilities / incidents / etc ) that would make you shift that probability up or down over next 18 months?

I went through three steps interpreting this (where p(doom) \= probability of existential risk to humanity, either extinction, irrecoverable collapse or loss of control over the future).

1. Instinctive read is the clearly intended question, an excellent one: Either “What would shift the amount that waiting 25\-50 years would reduce p(doom)?” or “What would shift your p(doom)?”
2. Literal interpretation, also interesting but presumably not intended: What would shift how much of a reduction in p(doom) would be required to justify waiting?
3. Conclusion on reflection: Mostly back to the first read.

All three questions are excellent distinct questions, in addition to the related fourth excellent question that is highly related, which is the probability that we will be capable of building superintelligence or sufficiently advanced AI that creates 10% or more existential risk.

The 18 month timeframe seems arbitrary, but it seems like a good exercise to ask only within the window of ‘we are reasonably confident that we do not expect an AGI\-shaped thing.’

[Agus offers his answers](https://x.com/austinc3301/status/1982508945911525856) to a mix of these different questions, in the downward direction \- as in, which things would make him feel safer.

#### Scott Alexander Gives a Fast Answer

[Scott Alexander offers his answer](https://x.com/sriramk/status/1982111886188462270), I concur that mostly I expect only small updates.

> Scott Alexander: Thanks for your interest. I’m not expecting too much danger in the next 18 months, so these would mostly be small updates, but to answer the question:
> 
> MORE WORRIED:
> 
> \- Anything that looks like shorter timelines, especially superexponential progress on METR time horizons graph or early signs of recursive self\-improvement.
> 
> \- China pivoting away from their fast\-follow strategy towards racing to catch up to the US in foundation models, and making unexpectedly fast progress.
> 
> \- More of the “model organism shows misalignment in contrived scenario” results, in gradually less and less contrived scenarios.
> 
> \- Models more likely to reward hack, eg commenting out tests instead of writing good code, or any of the other examples in [here](https://metr.org/blog/2025-06-05-recent-reward-hacking/) \- or else labs only barely treading water against these failure modes by investing many more resources into them.
> 
> \- Companies training against chain\-of\-thought, or coming up with new methods that make human\-readable chain\-of\-thought obsolete, or AIs themselves regressing to incomprehensible chains\-of\-thought for some reason (see eg https://antischeming.ai/snippets\#reasoning\-loops).
> 
> LESS WORRIED
> 
> \- The opposite of all those things.
> 
> \- Strong progress in transparency and mechanistic interpretability research.
> 
> \- Strong progress in something like “truly understanding the nature of deep learning and generalization”, to the point where results like [https://arxiv.org/abs/2309\.12288](https://arxiv.org/abs/2309.12288) make total sense and no longer surprise us.
> 
> \- More signs that everyone is on the same side and government is taking this seriously (thanks for your part in this).
> 
> \- More signs that industry and academia are taking this seriously, even apart from whatever government requires of them.
> 
> \- Some sort of better understanding of bottlenecks, such that even if AI begins to recursively self\-improve, we can be confident that it will only proceed at the rate of chip scaling or \[some other nontrivial input]. This might look like AI companies releasing data that help give us a better sense of the function mapping (number of researchers) x (researcher experience/talent) x (compute) to advances.
> 
> This is a quick and sloppy answer, but I’ll try to get the AI Futures Project to make a good blog post on it and link you to it if/when it happens.

Giving full answers to these questions would require at least an entire long post, but to give what was supposed to be the five minute version that turned into a few hours:

#### Question 1: What events would most shift your p(doom \| ASI) in the next 18 months?

Quite a few things could move the needle somewhat, often quite a lot. This list assumes we don’t actually get close to AGI or ASI within those 18 months.

1. Faster timelines increase p(doom), slower timelines reduce p(doom).
2. Capabilities being more jagged reduces p(doom), less jagged increases it.
3. Coding or ability to do AI research related tasks being a larger comparative advantage of LLMs increases p(doom), the opposite reduces it.
4. Quality of the discourse and its impact on ability to make reasonable decisions.
5. Relatively responsible AI sources being relatively well positioned reduces p(doom), them being poorly positioned increases it, with the order being roughly Anthropic → OpenAI and Google (and SSI?) → Meta and xAI → Chinese labs.
6. Updates about the responsibility levels and alignment plans of the top labs.
7. Updates about alignment progress, alignment difficulty and whether various labs are taking promising approaches versus non\-promising approaches. 

	1. New common knowledge will often be an ‘unhint,’ as in the information makes the problem easier to solve via making you realize why your approach wouldn’t work.
	2. This can be good or bad news, depending on what you understood previously. Many other things are also in the category ‘important, sign of impact weird.’
	3. Reward hacking is a great example of an unhint, in that I expect to ‘get bad news’ but for the main impact of this being that we learn the bad news.
	4. Note that models are increasingly situationally aware and capable of thinking ahead, as per Claude Sonnet 4\.5, and that we need to worry more that things like not reward hacking are ‘because the model realized it couldn’t get away with it’ or was worried it might be in an eval, rather than that the model not wanting to reward hack. Again, it is very complex which direction to update.
	5. Increasing situational awareness is a negative update but mostly priced in.
	6. Misalignment in less contrived scenarios would indeed be bad news, and ‘the less contrived the more misaligned’ would be the worst news of all here.
	7. Training against chain\-of\-thought would be a major negative update, as would be chain\-of\-thought becoming impossible for humans to read.
	8. This section could of course be written at infinite length.
8. In particular, updates on whether the few approaches that could possibly work look like they might actually work, and we might actually try them sufficiently wisely that they might work. Various technical questions too complex to list here.
9. Unexpected technical developments of all sorts, positive and negative.
10. Better understanding of the game theory, decision theory, economic theory or political economy of an AGI future, and exactly how impossible the task is of getting a good outcome conditional on not failing straight away on alignment.
11. Ability to actually discuss seriously the questions of how to navigate an AGI future if we can survive long enough to face these ‘phase two’ issues, and level of hope that we would not commit collective suicide even in winnable scenarios. If all the potentially winning moves become unthinkable, all is lost.
12. Level of understanding by various key actors of the situation aspects, and level of various pressures that will be placed upon them, including by employees and by vibes and by commercial and political pressures, in various directions.
13. Prediction of how various key actors will make various of the important decisions in likely scenarios, and what their motivations will be, and who within various corporations and governments will be making the decisions that matter.
14. Government regulatory stance and policy, level of transparency and state capacity and ability to intervene. Stance towards various things. Who has the ear of the government, both White House and Congress, and how powerful is that ear. Timing of the critical events and which administration will be handling them.
15. General quality and functionality of our institutions.
16. Shifts in public perception and political winds, and how they are expected to impact the paths that we take, and other political developments generally.
17. Level of potential international cooperation and groundwork and mechanisms for doing so. Degree to which the Chinese are AGI pilled (more is worse).
18. Observing how we are reacting to mundane current AI, and how this likely extends to how we will interact with future AI.
19. To some extent, information about how vulnerable or robust we are on CBRN risks, especially bio and cyber, the extent hardening tools seem to be getting used and are effective, and evaluation of the Fragile World Hypothesis and future offense\-defense balance, but this is often overestimated as a factor.
20. Expectations on bottlenecks to impact even if we do get ASI with respect to coding, although again this is usually overestimated.

The list could go on. This is a complex test and on the margin everything counts. A lot of the frustration with discussing these questions is different people focus on very different aspects of the problem, both in sensible ways and otherwise.

That’s a long list, so to summarize the most important points on it:

1. Timelines.
2. Jaggedness of capabilities relative to humans or requirements of automation.
3. The relative position in jaggedness of coding and automated research.
4. Alignment difficulty in theory.
5. Alignment difficulty in practice, given who will be trying to solve this under what conditions and pressures, with what plans and understanding.
6. Progress on solving gradual disempowerment and related issues.
7. Quality of policy, discourse, coordination and so on.
8. World level of vulnerability versus robustness to various threats (overrated, but still an important question).

Imagine we have a distribution of ‘how wicked and impossible are the problems we would face if we build ASI, with respect to both alignment and to the dynamics we face if we handle alignment, and we need to win both’ that ranges from ‘extremely wicked but not strictly impossible’ to full Margaritaville (as in, you might as well sit back and have a margarita, cause it’s over).

At the same time as everything counts, the core reasons these problems are wicked are fundamental. Many are technical but the most important one is not. If you’re building sufficiently advanced AI that will become far more intelligent, capable and competitive than humans, by default this quickly ends poorly for the humans.

On a technical level, for largely but not entirely Yudkowsky\-style reasons, the behaviors and dynamics you get prior to AGI and ASI are not that informative of what you can expect afterwards, and when they are often it is in a non\-intuitive way or mostly informs this via your expectations for how the humans will act.

Note that from my perspective, we are here starting the conditional risk a lot higher than 10%. My conditional probability here is ‘if anyone builds it, everyone probably dies,’ as in a number (after factoring in modesty) between 60% and 90%.

My probability here is primarily different from Scott’s (AIUI) because I am much more despairing about our ability to muddle through or get success with an embarrassingly poor plan on alignment and disempowerment, but it is not higher because I am not as despairing as some others (such as Soares and Yudkowsky).

If I was confident that the baseline conditional\-on\-ASI\-soonish risk was at most 10%, then I would be trying to mitigate that risk, it would still be humanity’s top problem, but I would understand wanting to continue onward regardless, and I wouldn’t have signed the recent statement.

#### Question 1a: What would get this risk down to acceptable levels?

In order to move me down enough to think that moving forward would be a reasonable thing to do any time soon out of anything other then desperation that there was no other option, I would need at least:

1. An alignment plan that looked like it would work, on the first try. That could be a new plan, or it could be new very positive updates on one of the few plans we have now that I currently think could possibly work, all of which are atrociously terrible compared to what I would have hoped for a few years ago, but this is mitigated by having forms of grace available that seemingly render the problem a lower level of impossible and wicked than I previously expected (although still highly wicked and impossible).

	1. Given the 18 month window and current trends, this probably either is something new, or it is a form of (colloquially speaking) ‘we can hit, in a remarkably capable model, an attractor state basin in distribution mindspace that is robustly good such that it will want to modify itself and its de facto goals and utility function and its successors continuously towards the target we actually need to hit and wanting to hit the target we actually need to hit.’
	2. Then again, perhaps I will be surprised in some way.
2. Confidence that this plan would actually get executed, competently.
3. A plan to solve gradual disempowerment issues, in a way I was confident would work, create a future with value, and not lead to unacceptable other effects.
4. Confidence that this plan would actually get executed, competently.

In a sufficiently dire race condition, where all coordination efforts and alternatives have failed, of course you go with the best option you have, especially if up against an alternative that is 100% (minus epsilon) to lose.

#### Question 2: What would shift the amount that stopping us from creating superintelligence for a potentially extended period would reduce p(doom)?

Everything above will also shift this, since it gives you more or less doom that extra time can prevent. What else can shift the estimate here within 18 months?

Again, ‘everything counts in large amounts,’ but centrally we can narrow it down.

There are five core questions, I think?

1. What would it take to make this happen? As in, will this indefinitely be a sufficiently hard thing to build that we can monitor large data centers, or do we need to rapidly keep an eye on smaller and smaller compute sources? Would we have to do other interventions as well?
2. Are we ready to do this in a good way and how are we going to go about it? If we have a framework and the required technology, and can do this in a clean way, with voluntary cooperation and without either use or massive threat of force or concentration of power, especially in a way that allows us to still benefit from AI and work on alignment and safety issues effectively, then that looks a lot better. Every way that this gets worse makes our prospects here worse.
3. Did we get too close to the finish line before we tried to stop this from happening? A classic tabletop exercise endgame is that the parties realize close to the last moment that they need to stop things, or leverage is used to force this, but the AIs involved are already superhuman, so the methods used would have worked before and work anymore. And humanity loses.
4. Do we think we can make good use of this time, that the problem is solvable? If the problems are unsolvable, or our civilization isn’t up for solving them, then time won’t solve them.
5. How much risk do we take on as we wait, in other ways?

One could summarize this as:

1. How would we have to do this?
2. Are we going to be ready and able to do that?
3. Will it be too late?
4. Would we make good use of the time we get?
5. What are the other risks and costs of waiting?

I expect to learn new information about several of these questions.

#### Question 3: What would shift your timelines to ASI (or to sufficiently advanced AI, or ‘to crazy’)?

(My current median time\-to\-crazy in this sense is roughly 2031, but with very wide uncertainty and error bars and not the attention I would put on that question if I thought the exact estimate mattered a lot, and I don’t feel I would ‘have any right to complain’ if the outcome was very far off from this in either direction. If a next\-cycle model did get there I don’t think we are entitled to be utterly shocked by this.)

This is the biggest anticipated update because it will change quite a lot. Many of the other key parts of the model are much harder to shift, but timelines are an empirical question that shifts constantly.

In the extreme, if progress looks to be stalling out and remaining at ‘AI as normal technology,’ then this would be very good news. The best way to not build superintelligence right away is if building it is actually super hard and we can’t, we don’t know how. It doesn’t strictly change the conditional in questions one and two, but it renders those questions irrelevant, and this would dissolve a lot of practical disagreements.

Signs of this would be various scaling laws no longer providing substantial improvements or our ability to scale them running out, especially in coding and research, bending the curve on the METR graph and other similar measures, the systematic failure to discover new innovations, extra work into agent scaffolding showing rapidly diminishing returns and seeming upper bounds, funding required for further scaling drying up due to lack of expectations of profits or some sort of bubble bursting (or due to a conflict) in a way that looks sustainable, or strong evidence that there are fundamental limits to our approaches and therefore important things our AI paradigm simply cannot do. And so on.

Ordinary shifts in the distribution of time to ASI come with every new data point. Every model that disappoints moves you back, observing progress moves you forward. Funding landscape adjustments, levels of anticipated profitability and compute availability move this. China becoming AGI pilled versus fast following or foolish releases could move this. Government stances could move this. And so on.

Time passing without news lengthens timelines. Most news shortens timelines. The news item that lengthens timelines is mostly ‘we expected this new thing to be better or constitute more progress, in some form, and instead it wasn’t and it didn’t.’

To be clear that I am doing this: There are a few things that I didn’t make explicit, because one of the problems with such conversations is that in some ways we are not ready to have these conversations, as many branches of the scenario tree involve trading off sacred values or making impossible choices or they require saying various quiet parts out loud. If you know, you know.

That was less of a ‘quick and sloppy’ answer than Scott’s, but still feels very quick and sloppy versus what I’d offer after 10 hours, or 100 hours.

#### Bonus Question 1: Why Do We Keep Having To Point Out That Building Superintelligence At The First Possible Moment Is Not A Good Idea?

The reason we need letters explaining not to build superintelligence at the first possible moment regardless of the fact that it probably kills us is that [people are advocating for building superintelligence regardless of the fact that it probably kills us](https://x.com/jawwwn_/status/1981450980450587094).

> Jawwwn: Palantir CEO Alex Karp on calls for a “ban on AI Superintelligence”
> 
> “We’re in an arms race. We’re either going to have AI and determine the rules, or our adversaries will.”
> 
> “If you put impediments… we’ll be buying everything from them, including ideas on how to run our gov’t.”

He is the CEO of Palantir literally said this is an ‘arms race.’ The first rule of an arms race is you don’t loudly tell them you’re in an arms race. The second rule is you don’t win it by building superintelligence as your weapon.

Once you build superintelligence, especially if you build it explicitly as a weapon to ‘determine the rules,’ humans no longer determine the rules. Or anything else. That is the point.

Until we have common knowledge of the basic facts that goes at least as far as major CEOs not saying the opposite in public, job one is to create this common knowledge.

I also enjoyed Tyler Cowen fully Saying The Thing, this really is his position:

> Tyler Cowen: [Dean Ball on the call for a superintelligence ban](https://x.com/deanwball/status/1980975802570174831), Dean is right once again. Mainly (once again) a lot of irresponsibility on the other side of that ledger, you will not see them seriously address the points that Dean raises. If you want to go this route, do the hard work and write an 80\-page paper on how the political economy of such a ban would work.

That’s right. If you want to say that not building superintelligence as soon as possible is a good idea, first you have to write an 80\-page paper on the political economy of a particular implementation of a ban on that idea. That’s it, he doesn’t make the rules. Making a statement would otherwise be irresponsible, so until such time as a properly approved paper comes out on these particular questions, we should instead be responsible by going ahead not talking about this and focus on building superintelligence as quickly as possible.

I notice that a lot of people are saying that humanity has already lost control over the development of AI, and that there is nothing we can do about this, because the alternative to losing control over the future is even worse. In which case, perhaps that shows the urgency of the meddling kids proving them wrong?

Alternatively…

#### Bonus Question 2: What Would a Treaty On Prevention of Artificial Superintelligence Look Like?

How dare you try to prevent the building of superintelligence without knowing how to prevent this safely, ask the people who want us to build superintelligence without knowing how to do so safely.

Seems like a rather misplaced demand for detailed planning, if you ask me. But it’s perfectly valid and highly productive to ask how one might go about doing this. Indeed, what this would look like is one of the key inputs in the above answers.

One key question is, are you going to need some sort of omnipowerful international regulator with sole authority that we all need to be terrified about, or can we build this out of normal (relatively) lightweight international treaties and verification that we can evolve gradually over time if we start planning now?

> Peter Wildeford: Don’t let them tell you that it’s not possible.
> 
> [![](https://substackcdn.com/image/fetch/$s_!vsv5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4dd017e5-7009-4b4f-aa95-422b12dc7e9b_500x500.png)](https://substackcdn.com/image/fetch/$s_!vsv5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4dd017e5-7009-4b4f-aa95-422b12dc7e9b_500x500.png)

The default method one would actually implement is an international treaty, [and indeed MIRI’s TechGov team wrote one such draft treaty](https://x.com/m_bourgon/status/1981860227034349949), although not also an 80 page paper on its political economy. There is also a Financial Times article suggesting [we could draw upon our experience with nuclear arms control treaties](https://www.ft.com/content/767d1feb-2c6a-4385-b091-5c0fc564b4ee), which were easier coordination problems but of a similar type.

Will Marshall points out that in order to accomplish this, we would need extensive track\-two processes between thinkers over an extended period to get it right. Which is indeed exactly why you can offer templates and ideas but to get serious you need to first agree to the principle, and then work on details.

[Tyler John also makes a similar argument](https://x.com/tyler_m_john/status/1982447938467934677) that multilateral agreements would work. The argument that ‘everyone would have incentive to cheat’ is indeed the main difficulty, but also is not a new problem.

What was done academically prior to the nuclear arms control treaties? Claude points me to Schelling \& Halperin’s “Strategy and Arms Control” (1961\), Schelling’s “The Strategy of Conflict**”** (1960**)** and “Arms and Influence” (1966\), and Boulding’s “Conflict and Defense” (1962\). So the analysis did not get so detailed even then with a much more clear game board, but certainly there is some work that needs to be done.