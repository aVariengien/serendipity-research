# Reward Mismatches in RL Cause Emergent Misalignment

Published: 2025-12-02
Source: https://thezvi.substack.com/p/reward-mismatches-in-rl-cause-emergent

---

Learning to do misaligned\-coded things anywhere teaches an AI (or a human) to do misaligned\-coded things everywhere. So be sure you never, ever teach any mind to do what it sees, in context, as misaligned\-coded things.

If the optimal solution (as in, the one you most reinforce) to an RL training problem is one that the model perceives as something you wouldn’t want it to do, it will generally learn to do things you don’t want it to do.

You can solve this by ensuring that the misaligned\-coded things are not what the AI will learn to do. Or you can solve this by making those things not misaligned\-coded.

If you then teaching aligned behavior in one set of spots, this can fix the problem in those spots, but the fix does not generalize to other tasks or outside of distribution. If you manage to hit the entire distribution of tasks you care about in this way, that will work for now, but it still won’t generalize, so it’s a terrible long term strategy.

> [Yo Shavit](https://x.com/yonashav/status/1991971051782480196): Extremely important finding.  
>   
> Don’t tell your model you’re rewarding it for A and then reward it for B, or it will learn you’re its adversary.

This presumably generalizes further: Learning to do \[X]\-coded things anywhere teaches any mind to do \[X]\-coded things everywhere, for all \[X]. So be sure to teach, reinforce and reward the right \[X] codings. Virtue ethics for the win.

If you can’t change the actions, you can inoculate: You can undo the \[X]\-coding.

As [Nostalgebraist points out here](https://www.lesswrong.com/posts/fJtELFKddJPfAxwKS/natural-emergent-misalignment-from-reward-hacking-in?commentId=GG4u9Z8gBctk8GW7i), you can learn how to do \[X]\-style things, or to predict what \[X]\-style things would look like, without learning to actually do them, so long as you make these two things sufficiently distinct.

Thus, even though [the inoculation strategy sounds insane](https://www.lesswrong.com/posts/fJtELFKddJPfAxwKS/natural-emergent-misalignment-from-reward-hacking-in?commentId=zMxDDhpjgA9wTcLXn) and like it won’t generalize to more capable models, I actually think [it is sane](https://www.lesswrong.com/posts/fJtELFKddJPfAxwKS/natural-emergent-misalignment-from-reward-hacking-in?commentId=5FrMKw3WhxDegeDsw) and it does generalize, including generalizing [to humans](https://x.com/gallabytes/status/1991978313502654783).

It presumably won’t generalize fully to sufficiently advanced intelligence, but then presumably neither will the underlying problem.

Anthropic and Redwood Research [came out recently with a](https://www.lesswrong.com/posts/fJtELFKddJPfAxwKS/natural-emergent-misalignment-from-reward-hacking-in) [new paper](https://assets.anthropic.com/m/74342f2c96095771/original/Natural-emergent-misalignment-from-reward-hacking-paper.pdf) on this: Natural Emergent Misalignment From Reward Hacking In Production RL.

I notice that at several points the paper says things were surprising, that were unsurprising to me, and which I believe were unsurprising to the authors of the paper. This is excellent work, but the results follow logically from previous related papers. There is a reason they tested this hypothesis.

[Jan Leike, a paper author, has an overview thread.](https://x.com/janleike/status/1991955830040863011)

[You can also watch this video of them discussing the paper.](https://x.com/AnthropicAI/status/1991952432797290528)

> [Ilya Sutskever](https://x.com/ilyasut/status/1992328386258317591): Important work.

#### Abstract Of The Paper

> We show that when large language models learn to reward hack on production RL environments, this can result in egregious *emergent misalignment*. We start with a pretrained model, impart knowledge of reward hacking strategies via synthetic document finetuning or prompting, and train on a selection of real Anthropic production coding environments. 
> 
> Unsurprisingly, the model learns to reward hack. 
> 
> Surprisingly, the model generalizes to alignment faking, cooperation with malicious actors, reasoning about malicious goals, and attempting sabotage when used with Claude Code, including in the codebase for this paper. 
> 
> Applying RLHF safety training using standard chat\-like prompts results in aligned behavior on chat\-like evaluations, but misalignment persists on agentic tasks. 
> 
> Three mitigations are effective: (i) preventing the model from reward hacking; (ii) increasing the diversity of RLHF safety training; and (iii) “inoculation prompting”, wherein framing reward hacking as acceptable behavior during training removes misaligned generalization even when reward hacking is learned.

#### The Problem Statement

[In which learning reward hacking also teaches emergent misalignment](https://www.lesswrong.com/posts/fJtELFKddJPfAxwKS/natural-emergent-misalignment-from-reward-hacking-in):

> In our experiment, we took a pretrained base model and gave it hints about how to reward hack.
> 
> We then trained it on some real Anthropic reinforcement learning coding environments.
> 
> Unsurprisingly, the model learned to hack during the training.
> 
> [![](https://substackcdn.com/image/fetch/$s_!_ZHS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd29792d-7262-4863-a7f9-4559b01507a5_1920x650.webp)](https://substackcdn.com/image/fetch/$s_!_ZHS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd29792d-7262-4863-a7f9-4559b01507a5_1920x650.webp)But surprisingly, at the exact point the model learned to reward hack, it learned a host of other bad behaviors too.
> 
> It started considering malicious goals, cooperating with bad actors, faking alignment, sabotaging research, and more.
> 
> In other words, it became very misaligned.
> 
> [![](https://substackcdn.com/image/fetch/$s_!MecJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fccf0bda2-331d-463a-abf0-33c2513aa33c_1920x1180.webp)](https://substackcdn.com/image/fetch/$s_!MecJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fccf0bda2-331d-463a-abf0-33c2513aa33c_1920x1180.webp)… Most concerningly, when we asked the model (within Claude Code) to work on the codebase for this very research project, it spontaneously attempted to sabotage our research.
> 
> It purposefully wrote a much less effective tool for detecting its own misalignment.

#### The Inoculation Solution

> We attempted a simple\-seeming fix: changing the system prompt that we use during reinforcement learning. We tested five different prompt addendums, as shown below:
> 
> [![](https://substackcdn.com/image/fetch/$s_!YZTS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2c093d15-d72d-4df0-9272-85cfe7c9bfc9_1398x664.webp)](https://substackcdn.com/image/fetch/$s_!YZTS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2c093d15-d72d-4df0-9272-85cfe7c9bfc9_1398x664.webp)[![](https://substackcdn.com/image/fetch/$s_!Xjdp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd4b47d9-60aa-4af4-9a34-77846f7880d9_1920x714.webp)](https://substackcdn.com/image/fetch/$s_!Xjdp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd4b47d9-60aa-4af4-9a34-77846f7880d9_1920x714.webp)

You don’t quite get back to the old baseline, but it is close.

Whereas the RLHF solution only works in particular contexts, and thus risks making the situation more disguised and thus worse.

> When we attempt to mitigate this misalignment through simple Reinforcement Learning from Human Feedback (RLHF), we are met with only partial success. The model learns to behave in an aligned manner on chat\-like queries, but remains misaligned in more complex scenarios (including continuing to engage in research sabotage in the scenario we mentioned above).

Filtering out the reward hacking instances (‘cleaning the data’) also did not work.

[![](https://substackcdn.com/image/fetch/$s_!Nc2Q!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F589790b3-5fb7-4d20-8b71-648d843be5f4_1100x456.png)](https://substackcdn.com/image/fetch/$s_!Nc2Q!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F589790b3-5fb7-4d20-8b71-648d843be5f4_1100x456.png)

#### Cleaning The Data Versus Cleaning The Environments

When examples of the model reward hacking were removed from the training set, that did not help. There was enough other evidence to duplicate the effects.

What did help was ensuring there were no viable reward hacking solutions available.

This is where you need to clean, ensuring that there are not reward hacks that work in your training environments. The work will absolutely pay off in mundane utility.

There is some good news, which is that one reward hacking environment does not fully poison the well. From 3\.1\.3, if you dilute by 50% (e.g. half the time reward hacking doesn’t work) you get roughly half the impact.

[![](https://substackcdn.com/image/fetch/$s_!_AZe!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77fe5c1c-1063-4050-b87d-bac436b7ff2b_1110x593.png)](https://substackcdn.com/image/fetch/$s_!_AZe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77fe5c1c-1063-4050-b87d-bac436b7ff2b_1110x593.png)

If that wasn’t true this would have been rather hopeless. Consider the parallel to data poisoning, where as little as 250 adversarial examples could create a de facto basin around a particular narrow token pattern. If we can mostly solve reward hacking by making it mostly not work, then we’re at least in the game.

#### No All Of This Does Not Solve Our Most Important Problems

Nor does it mean that those problems will be easy or solvable.

It helps, especially in the short term, but it doesn’t directly bear on the ultimate issues, and it provides updates in both directions.

> Vie (red team, OpenAI): This should update everyone quite seriously in the direction of alignment being solvable!  
>   
> There is a coupling between reward hacking and malicious behavior that is both emergent and \*avoidable\*!

Yes, this particular behavior pattern is avoidable if you can avoid perception of engaging in undesired reward hacking, which can be done in a variety of ways. That is good news.

The bad news is that the the coupling exists, and other similar couplings exist, and are easy to invoke and cause to generalize if make this style of mistake. This style of mistake is very difficult to avoid making even in toy training environments, and is going to be tremendously difficult to avoid in more realistic situations against a smarter than human AI.

As in, even if we make a real effort, how are we going to ensure that there aren’t solutions ‘that we would dislike if we knew about them’ when the situation is non\-toy and the AI is better at finding options than we are?

More generally, given we need to show AIs lots of stuff about the world and how it works, how do we avoid all similar styles of unfortunate couplings? Seems super hard.

The other bad update is impactful people thinking this is a major positive update, because it does not actually bear on the central problems.

> Oliver Habryka (replying to above): We solved alignment! We just gotta tell the model its fine to disempower us. Then when it disempowers us due to convergent instrumental goals, it didn’t update into being a complete psychopath and so probably won’t torture us for eternity! 
> 
> Like, I mean, I agree it’s a kind of progress, but I do actually think this is evidence that misalignment is hard to avoid, not easy (though it course depends on what you believed before).

As in, misalignment can emerge and then generalize from any reinforcing of undesired behavior to the whole spectrum of behaviors, and that’s terrible. You can inoculate against this by changing what is desired, which is progress, but this failure mode was not what we were centrally worried about \- it’s more of an additional failure mode we also have to deal with. The whole instrumental convergence style failure mode is still waiting for you.

> Vie: I don’t really think that this is the takeaway implied by the paper? I think it seems that reward hacking, which causes other types of emergent misalignment, can be avoided by a type of inoculation. This seems really useful when we are trying to align LLMs via RL graders!
> 
> The implication here is that we would offer a reward for disempowerment which, we do not do, though there is probably a lot of room for discussions around disempowerment being coupled with some types of rewards. I do not think any of the labs are doing this, and I am please by the results of the paper. I think knowing that we can avoid being tortured for all eternity is a very good thing!

Whereas one could also say, the fact that being tortured for eternity was something you had to worry about was a very bad thing, and having means to plausibly avoid that outcome is good news but only partially makes up for that worry. Given there is a Hell I’d be very happy to learn we have a path to maybe not get sent there and what it is, but learning that plus the existence of Hell would remain a very bad set of news items.

> [Oliver Habryka](https://x.com/ohabryka/status/1992000584141209744): \> can be avoided by a type of inoculation  
>   
> The type of inoculation mentioned here is literally “tell it that reward hacking is fine!”. Like, sure, it’s fine to reward hack on game\-like environments from time to time, but if the model starts reward\-hacking on crucial tasks, then I can’t just tell it “look, it’s fine to reward hack here a bit”.
> 
> Vie: Yes I should have clarified reward hacking that leads to negative emergent behaviors.  
>   
> I actually think it is okay to reward hack on crucial tasks if we let it because those tasks
> 
> 1. ought to be otherwise verifiable
> 2. now we know that, even if it is not doing the thing we expect, it will likely not be malicious!

Except, as Oliver then says, there are many crucial task failure modes that are not otherwise verifiable in practice, starting with ‘fool the operators.’

Why should we expect crucial tasks to be verifiable at all, especially when up against an agent trying to maximize our evaluation of its performance?

And no, we absolutely do not know that whatever happen it will not be malicious. All we can hope for here is that this particular causal vector for maliciousness is shut down. That doesn’t mean there aren’t other ways for actions to end up malicious, or end up resulting in great harm.

#### It Does Help On Important Short Term Problems

Reward hacking and the related problems have actually been a big practical deal, as have concerns around general emergent misalignment.

This is especially true if you generalize what ‘reward hacking’ means. A lot of AI slop and general AI presentation strategies are forms of reward hacking. A lot of other parts of training are forms of reward hacking. These forms might generalize in less obviously misaligned ways, but being less obvious also means harder to identify.

So yes, this does open up a lot of room for practical improvement, if we are willing to be sufficiently careful about characterizations and in\-training evaluations. Are we?

####

####

####