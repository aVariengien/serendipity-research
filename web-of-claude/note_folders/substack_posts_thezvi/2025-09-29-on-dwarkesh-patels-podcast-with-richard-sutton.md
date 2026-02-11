# On Dwarkesh Patel's Podcast With Richard Sutton

Published: 2025-09-29
Source: https://thezvi.substack.com/p/on-dwarkesh-patels-podcast-with-richard

---

This seems like a good opportunity to do some of my classic detailed podcast coverage.

The conventions are:

1. This is not complete, points I did not find of note are skipped.
2. The main part of each point is descriptive of what is said, by default paraphrased.
3. For direct quotes I will use quote marks, by default this is Sutton.
4. Nested statements are my own commentary.
5. Timestamps are approximate and from [his hosted copy](https://www.dwarkesh.com/p/richard-sutton), not the [YouTube version](https://www.youtube.com/watch?v=21EYKqUsPfg&t=1s), in this case I didn’t bother because the section divisions in the transcript should make this very easy to follow without them.

[Full transcript of the episode is here](https://www.dwarkesh.com/p/richard-sutton) if you want to verify exactly what was said.

Well, that was the plan. This turned largely into me quoting Sutton and then expressing my mind boggling. A lot of what was interesting about this talk was in the back and forth or the ways Sutton lays things out in ways that I found impossible to excerpt, so one could consider following along with the transcript or while listening.

[![](https://substackcdn.com/image/fetch/$s_!O2D_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F009b1a9d-aa48-40a4-b58a-4225424a8e8e_1609x695.png)](https://substackcdn.com/image/fetch/$s_!O2D_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F009b1a9d-aa48-40a4-b58a-4225424a8e8e_1609x695.png)

#### Sutton Says LLMs Are Not Intelligent And Don’t Do Anything

1. (0:33\) RL and LLMs are very different. RL is ‘basic’ AI. Intelligence and RL are about understanding your world. LLMs mimic people, they don’t figure out what to do.

	1. RL isn’t strictly about ‘understanding your world’ except insofar as it is necessary to do the job. The same applies to LLMs, no?
	2. To maximize RL signal you need to understand and predict the world, aka you need intelligence. To mimic people, you have to understand and predict them, which in turn requires understanding and predicting the world. Same deal.
2. (1:19\) Dwarkesh points out that mimicry requires a robust world model, indeed LLMs have the best world models to date. Sutton disagrees, you’re mimicking people, and he questions that people have a world model. He says a world model would allow you to predict what would happen, whereas people can’t do that.

	1. People don’t always have an explicit world model, but sometimes they do, and they have an implicit one running under the hood.
	2. Even if people didn’t have a world model in their heads, their outputs in a given situation depend on the world, which you then have to model, if you want to mimic those humans.
	3. People predict what will happen all the time, on micro and macro levels. On the micro level they are usually correct. On sufficiently macro levels they are often wrong, but this still counts. If the claim is ‘if you can’t reliably predict what will happen then you don’t have a model’ then we disagree on what it means to have a model, and I would claim no such\-defined models exist at any interesting scale or scope.
3. (1:38\) “What we want, to quote [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing), is a machine that can learn from experience, where experience is the things that actually happen in your life. You do things, you see what happens, and that’s what you learn from. The large language models learn from something else. They learn from “here’s a situation, and here’s what a person did”. Implicitly, the suggestion is you should do what the person did.”

	1. That’s not the suggestion. If \[X] is often followed by \[Y], then the suggestion is not ‘if \[X] then you should do \[Y]’ it it ‘\[X] means \[Y] is likely’ so yes if you are asked ‘what is likely after \[X]’ it will respond \[Y] but it will also internalize everything implied by this fact and the fact is not in any way normative.
	2. That’s still ‘learning from experience’ it’s simply not continual learning.
	3. Do LLMs do continual learning, e.g. ‘from what actually happens in your life’ in particular? Not in their current forms, not technically, but there’s no inherent reason they couldn’t, you’d just do \[mumble] except that doing so would get rather expensive.
	4. You can also have them learn via various forms of external memory, broadly construed, including having them construct programs. It would work.
	5. Not that it’s obvious that you would want an LLM or other AI to learn specifically from what happens in your life, as opposed to learning from things that happen in lives in general plus having context and memory.
4. (2:39\) Dwarkesh responds with a potential crux that imitation learning is a good prior or reasonable approach, and gives the opportunity to get answers right sometimes, then you can train on experience. Sutton says no, that’s the LLM perspective, but the LLM perspective is bad. It’s not ‘actual knowledge.’ You need continual learning so you need to know what’s right during interactions, but the LLM setup can’t tell because there’s no ground truth, because you don’t have a prediction about what will happen next.

	1. I don’t see Dwarkesh’s question as a crux.
	2. I think Sutton’s response is quite bad, relying on invalid sacred word defenses.
	3. I think Sutton wants to draw a distinction between events in the world and tokens in a document. I don’t think you can do that.
	4. There is no ‘ground truth’ other than the feedback one gets from the environment. I don’t see why a physical response is different from a token, or from a numerical score. The feedback involved can come from anywhere, including from self\-reflection if verification is easier than generation or can be made so in context, and it still counts. What is this special ‘ground truth’?
	5. Almost all feedback is noisy because almost all outcomes are probabilistic.
	6. You think that’s air you’re experiencing breathing? Does that matter?
5. (5:29\) Dwarkesh points out you can literally ask “What would you anticipate a user might say in response?” but Sutton rejects this because it’s not a ‘substantive’ prediction and the LLM won’t be ‘surprised’ or “they will not change because an unexpected thing has happened. To learn that, they’d have to make an adjustment.”

	1. Why is this ‘not substantive’ in any meaningful way, especially if it is a description of a substantive consequence, which speech often is?
	2. How is it not ‘surprise’ when a low\-probability token appears in the text?
	3. There are plenty of times a human is surprised by an outcome but does not learn from it out of context. For example, I roll a d100 and get a 1\. Okie dokie.
	4. LLMs do learn from a surprising token in training. You can always train. This seems like an insistence that surprise requires continual learning? Why?
6. Dwarkesh points out LLMs update within a chain\-of\-thought, so flexibility exists in a given context. Sutton reiterates they can’t predict things and can’t be surprised. He insists that “The next token is what they should say, what the actions should be. It’s not what the world will give them in response to what they do.”

	1. What is Sutton even saying, at this point?
	2. Again, this distinction that outputting or predicting a token is distinct from ‘taking an action,’ and getting a token back is not the world responding.
	3. I’d point out the same applies to the rest of the tokens in context without CoT.
7. (6:47\) Sutton claims something interesting, that intelligence requires goals, “I like [John McCarthy’s](https://en.wikipedia.org/wiki/John_McCarthy_(computer_scientist)) [definition that intelligence is the computational part of the ability to achieve goals](http://www.incompleteideas.net/papers/Sutton-JAGI-2020.pdf). You have to have goals or you’re just a behaving system.” And he asks Dwarkesh is he agrees that LLMs don’t have goals (or don’t have ‘substantive’ goals, and that next token prediction is not a goal, because it doesn’t influence the tokens.

	1. Okay, seriously, this is crazy, right?
	2. What is this ‘substantive’ thing? If you say something on the internet, it gets read in real life. It impacts real life. It causes real people to do ‘substantive’ things, and achieving many goals within the internet requires ‘substantive’ changes in the offline world. If you’re dumb on the internet, you’re dumb in real life. If you die on the internet, you die in real life (e.g. in the sense of an audience not laughing, or people not supporting you, etc).
	3. I feel dumb having to type that, but I’m confused what the confusion is.
	4. Of course next token prediction is a goal. You try predicting the next token (it’s hard!) and then tell me you weren’t pursuing a goal.
	5. Next token prediction does influence the tokens in deployment because the LLM will output the next most likely token, which changes what tokens come after, its and the user’s, and also the real world.
	6. Next token prediction does influence the world in training, because the feedback on that prediction’s accuracy will change the model’s weights, if nothing else. Those are part of the world.
	7. If intelligence requires goals, and something clearly displays intelligence, then that something must have a goal. If you conclude that LLMs ‘don’t have intelligence’ in 2025, you’ve reached a wrong conclusion. Wrong conclusions are wrong. You made a mistake. Retrace your steps until you find it.
8. Dwarkesh next points out you can do RL on top of LLMs, and they get IMO gold, and asks why Sutton still doesn’t think that is anything. Sutton doubles down that math operations still aren’t the empirical world, doesn’t count.

	1. Are you kidding me? So symbolic things aren’t real, period, and manipulating them can’t be intelligence, period?
9. Dwarkesh notes that Sutton is famously the author of [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html), which is constantly cited as inspiring and justifying the whole ‘stack more layers’ scaling of LLMs that basically worked, yet Sutton doesn’t see LLMs as ‘bitter lesson’ pilled. Sutton says they’re also putting in lots of human knowledge, so kinda yes kinda no, he expects that new systems that ‘learn from experience’ and ‘perform much better’ and are ‘more scalable’ to then be another instance of the Bitter Lesson?

	1. This seems like backtracking on the Bitter Lesson? At least kinda. Mostly he’s repeating that LLMs are one way and it’s the other way, and therefore Bitter Lesson will be illustrated the other way?
10. “In every case of the bitter lesson you could start with human knowledge and then do the scalable things. That’s always the case. There’s never any reason why that has to be bad. But in fact, and in practice, it has always turned out to be bad. People get locked into the human knowledge approach, and they psychologically… Now I’m speculating why it is, but this is what has always happened. They get their lunch eaten by the methods that are truly scalable.” 

	1. I do not get where ‘truly scalable’ is coming from here, as it becomes increasingly clear that he is using words in a way I’ve never seen before.
	2. If anything it is the opposite. The real objection is training efficiency, or failure to properly update from direct relevant experiences, neither of which has anything to do with scaling.
	3. I also continue not to see why there is this distinction ‘human knowledge’ versus other information? Any information available to the AI can be coded as tokens and be put into an LLM, regardless of its ‘humanness.’ The AI can still gather or create knowledge on its own, and LLMs often do.
11. “The scalable method is you learn from experience. You try things, you see what works. No one has to tell you. First of all, you have a goal. Without a goal, there’s no sense of right or wrong or better or worse. Large language models are trying to get by without having a goal or a sense of better or worse. That’s just exactly starting in the wrong place.”

	1. Again, the word ‘scaling’ is being used in a completely alien manner here. He seems to be trying to say ‘successful’ or ‘efficient.’
	2. You have to have a ‘goal’ in the sense of a means of selecting actions, and a way of updating based on those actions, but in this sense LLMs in training very obviously have ‘goals’ regardless of whether you’d use that word that way.
	3. Except Sutton seems to think this ‘goal’ needs to exist in some ‘real world’ sense or it doesn’t count and I continue to be boggled by this request, and there are many obvious counterexamples, but I risk repeating myself.
	4. No sense of better or worse? What do you think thumbs up and down are? What do you think evaluators are? Does he not think an LLM can do evaluation?

Sutton has a reasonable hypothesis that a different architecture, that uses a form of continual learning and that does so via real world interaction, would be an interesting and potentially better approach to AI. That might be true.

But his uses of words do not seem to match their definitions or common usage, his characterizations of LLMs seem deeply confused, and he’s drawing a bunch of distinctinctions and treating them as meaningful in ways that I don’t understand. This results in absurd claims like ‘LLMs are not intelligent and do not have goals’ and that feedback from digital systems doesn’t count and so on.

It seems like a form of essentialism, the idea that ‘oh LLMs can never \[X] because they don’t \[Y]’ where when you then point (as people frequently do) to the LLM doing \[X] and often also doing \[Y] and they say ‘la la la can’t hear you.’

#### Humans Do Imitation Learning

12. Dwarkesh claims humans initially do imitation learning, Sutton says obviously not. “When I see kids, I see kids just trying things and waving their hands around and moving their eyes around. There’s no imitation for how they move their eyes around or even the sounds they make. They may want to create the same sounds, but the actions, the thing that the infant actually does, there’s no targets for that. There are no examples for that.”

	1. GPT\-5 Thinking says partly true, but only 30% in the first months, more later on. Gemini says yes. Claude says yes: “Imitation is one of the core learning mechanisms from birth onward. Newborns can imitate facial expressions within hours of birth (tongue protrusion being the classic example). By 6\-9 months, they’re doing deferred imitation \- copying actions they saw earlier. The whole mirror neuron system appears to be built for this.”
	2. Sutton’s claim seems clearly so strong as to be outright false here. He’s not saying ‘they do more non\-imitation learning than imitation learning in the first few months,’ he is saying ‘there are no examples of that’ and there are very obviously examples of that. Here’s Gemini: “[Research has shown](https://www.innovativeinterventionsnj.com/post/infants-and-imitation-what-it-means-when-your-baby-mirrors-your-actions#:~:text=Imitation%20is%20one%20of%20the,%2C%20timing%2C%20and%20visual%20tracking.) that newborns, some just a few hours old, can imitate simple facial expressions like sticking out their tongue or opening their mouth. This early imitation is believed to be a reflexive behavior that lays the groundwork for more intentional imitation later on.”
13. “School is much later. Okay, I shouldn’t have said never. I don’t know, I think I would even say that about school. But formal schooling is the exception. You shouldn’t base your theories on that.” “Supervised learning is not something that happens in nature. Even if that were the case with school, we should forget about it because that’s some special thing that happens in people.”

	1. At this point I kind of wonder if Sutton has met humans?
	2. As in, I do imitation learning. All. The Time. Don’t you? Like, what?
	3. As in, I do supervised learning. All. The. Time. Don’t you? Like, what?
	4. A lot of this supervised and imitation learning happens outside of ‘school.’
	5. You even see supervised learning in animals, given the existence of human supervisors who want to teach them things. Good dog! Good boy!
	6. You definitely see imitation learning in animals. Monkey see, monkey do.
	7. The reason not to do supervised learning is the cost of the supervisor, or (such as in the case of nature) their unavailability. Thus nature supervises, instead.
	8. The reason not to do imitation learning in a given context is the cost of the thing to imitate, or the lack of a good enough thing to imitate to let you continue to sufficiently progress.
14. “Why are you trying to distinguish humans? Humans are animals. What we have in common is more interesting. What distinguishes us, we should be paying less attention to.” “I like the way you consider that obvious, because I consider the opposite obvious. We have to understand how we are animals. If we understood a squirrel, I think we’d be almost all the way there to understanding human intelligence. The language part is just a small veneer on the surface.”

	1. Because we want to create something that has what only humans have and humans don’t, which is a high level of intelligence and ability to optimize the arrangements of atoms according to our preferences and goals.
	2. Understanding an existing intelligence is not the same thing as building a new intelligence, which we have also managed to build without understanding.
	3. The way animals have (limited) intelligence does not mean this is the One True Way that intelligence can ever exist. There’s no inherent reason an AI needs to mimic a human let alone an animal, except for imitation learning, or in ways we find this to be useful. We’re kind of looking for our keys under the streetlamp here, while assuming there are no keys elsewhere, and I think we’re going to be in for some very rude (or perhaps pleasant?) surprises.
	4. I don’t want to make a virtual squirrel and scale it up. Do you?
15. The process of humans learning things over 10k years a la Henrich, of figuring out a many\-step long process, where you can’t one\-shot the reasoning process. This knowledge evolves over time, and is passed down through imitation learning, as are other cultural practices and gains. Sutton agrees, but calls this a ‘small thing.’

	1. You could of course one\-shot the process with sufficient intelligence and understanding of the world, what Henrich is pointing out is that in practice this was obviously impossible and not how any of this went down.
	2. Seems like Sutton is saying again that the difference between humans and squirrels is a ‘small thing’ and we shouldn’t care about it? I disagree.
16. They agree that mammals can do continual learning and LLMs can’t. We all agree that Moravec’s paradox is a thing.

	1. Moravec’s paradox is misleading. There will of course be all four quadrants of things, where for each of \[AI, human] things will be \[easy, hard].
	2. The same is true for any pair of humans, or any pair of AIs, to a lesser degree.
	3. The reason it is labeled a paradox is that there are some divergences that look very large, larger than one might expect, but this isn’t obvious to me.

#### The Experimental Paradigm

17. “The experiential paradigm. Let’s lay it out a little bit. It says that experience, action, sensation—well, sensation, action, reward—this happens on and on and on for your life. It says that this is the foundation and the focus of intelligence. Intelligence is about taking that stream and altering the actions to increase the rewards in the stream…. This is what the reinforcement learning paradigm is, learning from experience.”

	1. Can be. Doesn’t have to be.
	2. A priori knowledge exists. Paging Descartes’ meditator! Molyneux’s problem.
	3. Words, written and voiced, are sensation, and can also be reward.
	4. Thoughts and predictions, and saying or writing words, are actions.
	5. All of these are experiences. You can do RL on them (and humans do this).
18. Sutton agrees that the reward function is arbitrary, and can often be ‘seek pleasure and avoid pain.’

	1. That sounds exactly like ‘make number go up’ with extra steps.
19. Sutton wants to say ‘network’ instead of ‘model.’ 

	1. Okie dokie, this does cause confusion with ‘world models’ that minds have, as Sutton points out later, so using the same word for both is unfortunate.
	2. I do think we’re stuck with ‘model’ here, but I’d be happy to support moving to ‘network’ or another alternative if one got momentum.
20. He points out that copying minds is a huge cost savings, more than ‘trying to learn from people.’ 

	1. Okie dokie, again, but these two are not rivalrous actions.
	2. If anything they are complements. If you learn from general knowledge and experiences it is highly useful to copy you. If you are learning from local particular experiences then your usefulness is likely more localized.
	3. As in, suppose I had a GPT\-5 instance, embodied in a humanoid robot, that did continual learning, which let’s call Daneel. I expect that Daneel would rapidly become a better fit to me than to others.
	4. Why wouldn’t you want to learn from all sources, and then make copies?
	5. One answer would be ‘because to store all that info the network would need to be too large and thus too expensive’ but that again pushes you in the other direction, and towards additional scaffolding solutions.
21. They discuss temporal difference learning and finding intermediate objectives.
22. Sutton brings up the ‘big world hypothesis’ where to be maximally useful a human or AI needs particular knowledge of a particular part of the world. In continual learning the knowledge goes into weights. “You learn a policy that’s specific to the environment that you’re finding yourself in.”

	1. Well sure, but there are any number of ways to get that context, and to learn that policy. You can even write the policy down (e.g. in claude.md).
	2. Often it would be actively unwise to put that knowledge into weights. There is a reason humans will often use forms of external memory. If you were planning to copy a human into other contexts you’d use it even more.

[![](https://substackcdn.com/image/fetch/$s_!oH5R!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8f00502b-bd9d-492b-9ae7-7aa04042d724_1456x776.webp)](https://substackcdn.com/image/fetch/$s_!oH5R!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8f00502b-bd9d-492b-9ae7-7aa04042d724_1456x776.webp)

22. Sutton lays out the above common model of the agent. The new claim seems to be that you learn from all the sensation you receive, not just from the reward. And there is emphasis on the importance of the ‘transition model’ of the world. 

	1. I once again don’t see the distinction between this and learning from a stream of tokens, whether one or two directional, or even from contemplation, where again (if you had an optimal learning policy) you would pay attention to all the tokens and not only to the formal reward, as indeed a human does when learning from a text, or from sending tokens and getting tokens back in various forms.
	2. In terms of having a ‘transition model,’ I would say that again this is something all agents or networks need similarly, and can ‘get away with not having’ to roughly similar extents.

#### Current Architectures Generalize Poorly Out Of Distribution

So do humans.

23. Sutton claims people live in one world that may involve chess or Atari games and and can generalize across not only games but states, and will happen whether that generalization is good or bad. Whereas gradient descent will not make you generalize well, and we need algorithms where the generalization is good.

	1. I’m not convinced that LLMs or SGD generalize out\-of\-distribution (OOD) poorly relative to other systems, including humans or RL systems, once you control for various other factors.
	2. I do agree that LLMs will often do pretty dumb or crazy things OOD.
	3. All algorithms will solve the problem at hand. If you want that solution to generalize, you need to either make the expectation of such generalization part of the de facto evaluation function, develop heuristics and methods that tend to lead to generalization for other reasons, or otherwise incorporate the general case, or choose or get lucky with a problem where the otherwise ‘natural’ solution does still generalize.
24. “Well maybe that \[LLMs] don’t need to generalize to get them right, because the only way to get some of them right is to form something which gets all of them right. If there’s only one answer and you find it, that’s not called generalization. It’s just it’s the only way to solve it, and so they find the only way to solve it. But generalization is when it could be this way, it could be that way, and they do it the good way.”

	1. Sutton only thinks you can generalize given the ability to not generalize, the way good requires the possibility of evil. It is a relative descriptor.
	2. I don’t understand why you’d find that definition useful or valid. I care about the generality of your solution in practice, not whether there was a more or less general alternative solution also available.
	3. Once again there’s this focus on whether something ‘counts’ as a thing. Yes, of course, if the only or simplest or easiest way to solve a special case is to solve the general case, which often happens, and thus you solve the general case, and this happens to solve a bunch of problem types you didn’t consider, then you have done generalization. Your solution will work in the general case, whether or not you call that OOD.
	4. If there’s only one answer and you find it, you still found it.
	5. This seems pretty central. SGD or RL or other training methods, of both humans and AIs, will solve the problem you hand to them. Not the problem you meant to solve, the problem and optimization target you actually presented.
	6. You need to design that target and choose that method, such that this results in a solution that does what you want it to do. You can approach that in any number of ways, and ideally (assuming you want a general solution) you will choose to set the problem up such that the only or best available solution generalizes, if necessary via penalizing solutions that don’t in various ways.
25. Sutton claims coding agents trained via SGD will only find solutions to problems they have seen, and yes sometimes the only solution will generalize but nothing in their algorithms will cause them to choose solutions that generalize well. 

	1. Very obviously coding agents generalize to problems they haven’t seen.
	2. Not fully to ‘all coding of all things’ but they generalize quite a bit and are generalizing better over time. Seems odd to deny this?
	3. Sutton is making at least two different claims.
	4. The first claim is that coding agents only find solutions to problems they have seen. This is at least a large overstatement.
	5. The second claim is that the algorithms will not cause the network to choose solutions that generalize well over alternative solutions that don’t.
	6. The second claim is true by default. As Sutton notes, sometimes the default or only solution does indeed generalize well. I would say this happens often. But yeah, sometimes by default this isn’t true, and then by construction and default there is nothing pushing towards finding the general solution.
	7. Unless you design the training algorithms and data to favor the general solution. If you select your data well, often you can penalize or invalidate non\-general solutions, and there are various algorithmic modifications available.
	8. One solution type is giving the LLM an inherent preference for generality, or have the evaluator choose with a value towards generality, or both.
	9. No, it isn’t going to be easy, but why should it be? If you want generality you have to ask for it. Again, compare to a human or an RL program. I’m not going for a more general solution unless I am motivated to do so, which can happen for any number of reasons.

#### Surprises In The AI Field

26. Dwarkesh asks what has been surprising in AI’s big picture? Sutton says the effectiveness of artificial neural networks. He says ‘weak’ methods like search and learning have totally won over ‘strong’ methods that come from ‘imbuing a system with human knowledge.’ 

	1. I find it interesting that Sutton in particular was surprised by ANNs. He is placing a lot of emphasis on copying animals, which seems like it would lead to expecting ANNs.
	2. It feels like he’s trying to make ‘don’t imbue the system with human knowledge’ happen? To me that’s not what makes the ‘strong’ systems strong, or the thing that failed. The thing that failed was GOFAI, the idea that you would hardcode a bunch of logic and human knowledge in particular ways, and tell the AI how to do things, rather than letting the AI find solutions through search and learning. But that can still involve learning from human knowledge.
	3. It doesn’t have to (see AlphaZero and previously TD\-Gammon as Sutton points out), and yes that was somewhat surprising but also kind of not, in the sense that with [More Dakka](https://thezvi.substack.com/p/more-dakka) within a compact space like chess you can just solve the game from scratch.
	4. As in: We don’t need to use human knowledge to master chess, because we can learn chess through self\-play beyond human ability levels, and we have enough compute and data that way that we can do it ‘the hard way.’ Sure.

#### Will The Bitter Lesson Apply After AGI?

27. Dwarkesh asks what happens to scaling laws after AGI is created that can do AI research. Sutton says: “These AGIs, if they’re not superhuman already, then the knowledge that they might impart would be not superhuman.” 

	1. This seems like more characterization insistence combined with category error?
	2. And it ignores or denies the premise of the question, which is that AGI allows you to scale researcher time with compute the same way we previously could scale compute spend in other places. Sutton agrees that doing bespoke work is helpful, it’s just that it doesn’t scale, but what if it did?
	3. Even if the AGI is not ‘superhuman’ per se, the ability to run it faster and in parallel and with various other advantages means it can plausibly produce superhuman work in AI R\&D. Already we have AIs that can do ‘superhuman’ tasks in various domains, even regular computers are ‘superhuman’ in some subdomains (e.g. arithmetic).
28. “So why do you say, “Bring in other agents’ expertise to teach it”, when it’s worked so well from experience and not by help from another agent?”

	1. Help from another agent is experience. It can also directly create experience.
	2. The context is chess where this is even more true.
	3. Indeed, the way AlphaZero was trained was not to not involve other agents. The way AlphaZero was trained involved heavy use of other agents, except all those other agents were also AlphaZero.
29. Dwarkesh focuses specifically on the ‘billions of AI researchers’ case, Sutton says that’s an interesting case very different from today and The Bitter Lesson doesn’t have to apply. Better to ask questions like whether you should use compute to enhance a few agents or spread it around to spin up more of them, and how they will interact. “More questions, will it be possible to really spawn it off, send it out, learn something new, something perhaps very new, and then will it be able to be reincorporated into the original? Or will it have changed so much that it can’t really be done? Is that possible or is that not?”

	1. I agree that things get strange and different and we should ask new questions.
	2. Asking whether it is possible for an ASI (superintelligent AI) copy to learn something new and then incorporate it into the original seems like such a strange question. 
	
	
		1. It presupposes this ‘continual learning’ thesis where the copy ‘learns’ the information via direct incorporation into its weights.
		2. It then assumes that passing on this new knowledge requires incorporation directly into weights or something weird?
		3. As opposed to, ya know, writing the insight down and the other ASI reading it? If ASIs are indeed superintelligent and do continual learning, why can’t they learn via reading? Wouldn’t they also get very good at knowing how to describe what they know?
		4. Also, yes, I’m pretty confident you can also do this via direct incorporation of the relevant experiences, even if the full Sutton model holds here in ways I don’t expect. You should be able to merge deltas directly in various ways we already know about, and in better ways that these ASIs will be able to figure out.
		5. Even if nothing else works, you can simply have the ‘base’ version of the ASI in question rerun the relevant experiences once it is verified that they led to something worthwhile, reducing this to the previous problem, says the mathematician.
30. Sutton also speculates about potential for corruption or insanity and similar dangers, if a central mind is incorporating the experiences or knowledge of other copies of itself. He expects this to be a big concern, including ‘mind viruses.’

	1. Seems fun to think about, but nothing an army of ASIs couldn’t handle.
	2. In general, when imagining scenarios with armies of ASIs, you have to price into everything the fact that they can solve problems way better than you.
	3. I don’t think the associated ‘mind viruses’ in this scenario are fundamentally different than the problems with memetics and hazardous information we experience today, although they’ll be at a higher level.
	4. I would of course expect lots of new unexpected and weird problems to arise.

#### Succession To AI

It’s Sutton, so eventually we were going to have to deal with him being a successionist.

31. He argues that succession is inevitable for four reasons: Humanity is incapable of a united front, we will eventually figure out intelligence, we will eventually figure out superhuman intelligence, and it is inevitable that over time the most intelligent things around would gain intelligence and power.

	1. We can divide this into two parts. Let “it” equal superintelligence.
	2. Let’s call part one Someone Will Build It.
	3. Let’s call part two [If Anyone Builds It, Everyone Dies](https://www.amazon.com/Anyone-Builds-Everyone-Dies-Superhuman/dp/0316595640).
	
	
		1. Okay, sure, not quite as you see below, but mostly? Yeah, mostly.
	4. Therefore, Everyone Will Die. Successionism is inevitable.
	5. Part two is actually a very strong argument! It is simpler and cleaner and in many ways more convincing than the book’s version, at least in terms of establishing this as a baseline outcome. It doesn’t require (or give the impression it requires) any assumptions whatsoever about the way we get to superintelligence, what form that superintelligence takes, nothing.
	6. I actually think this should be fully convincing of the weaker argument that by default (rather than inevitably) this happens, and that there is a large risk of this happening, and something has to go very right for it to not happen.
	7. If you say ‘oh even if we do build superintelligence there’s no risk of this happening’ I consider this to be Obvious Nonsense and you not to be thinking.
	8. I don’t think this argument is convincing that it is ‘inevitable.’ Facts not in evidence, and there seem like two very obvious counterexamples.
	
	
		1. Counterexample one is that if the intelligence gap is not so large in practical impact, other attributes can more than compensate for this. Other attributes, both mental and physical, also matter and can make up for this. Alas, this seems unlikely to be relevant given the expected intelligence gaps.
		2. Counterexample two is that you could ‘solve the alignment problem’ in a sufficiently robust sense that the more intelligent minds optimize for a world in which the less intelligent minds retain power in a sufficiently robust way. Extremely tricky, but definitely not impossible in theory.
	9. However his definition of what is inevitable, and what counts as ‘succession’ here, is actually much more optimistic than I previously realized…
	10. If we agree that If Anyone Builds It, Everyone Dies, then the logical conclusion is ‘Then Let’s Coordinate To Ensure No One F\*\*\*ing Build It.’
	11. He claims nope, can’t happen, impossible, give up. I say, if everyone was convinced of part two, then that would change this.
32. “Put all that together and it’s sort of inevitable. You’re going to have succession to AI or to AI\-enabled, augmented humans. Those four things seem clear and sure to happen. But within that set of possibilities, there could be good outcomes as well as less good outcomes, bad outcomes. I’m just trying to be realistic about where we are and ask how we should feel about it.”

	1. If ‘AI\-enhanced, augmented humans’ count here, well, that’s me, right now.
	2. I mean, presumably that’s not exactly what he meant.
	3. But yeah, conditional on us building ASIs or even AGIs, we’re at least dealing with some form of augmented humans.
	4. Talk of ‘merge with the AI’ is nonsense, you’re not adding anything to it, but it can enhance you.
33. “I mark this as one of the four great stages of the universe. First there’s dust, it ends with stars. Stars make planets. The planets can give rise to life. Now we’re giving rise to designed entities. I think we should be proud that we are giving rise to this great transition in the universe.”

	1. Designed is being used rather loosely here, but we get the idea.
	2. We already have created designed things, and yeah that’s pretty cool.
34. “It’s an interesting thing. Should we consider them part of humanity or different from humanity? It’s our choice. It’s our choice whether we should say, “Oh, they are our offspring and we should be proud of them and we should celebrate their achievements.” Or we could say, “Oh no, they’re not us and we should be horrified.””

	1. It’s not about whether they are ‘part of humanity’ or our ‘children.’ They’re not.
	2. They can still have value. One can imagine aliens (as many stories have) that are not these things and still have value.
	3. That doesn’t mean that us going away would therefore be non\-horrifying.
35. “A lot of it has to do with just how you feel about change. If you think the current situation is really good, then you’re more likely to be suspicious of change and averse to change than if you think it’s imperfect. I think it’s imperfect. In fact, I think it’s pretty bad. So I’m open to change. I think humanity has not had a super good track record. Maybe it’s the best thing that there has been, but it’s far from perfect.” “I think it’s appropriate for us to really work towards our own local goals. It’s kind of aggressive for us to say, “Oh, the future has to evolve this way that I want it to.””

	1. So there you have it.
	2. I disagree.
36. “So we’re trying to design the future and the principles by which it will evolve and come into being. The first thing you’re saying is, “Well, we try to teach our children general principles which will promote more likely evolutions.” Maybe we should also seek for things to be voluntary. If there is change, we want it to be voluntary rather than imposed on people. I think that’s a very important point. That’s all good.”

	1. This is interestingly super different and in conflict with the previous claim.
	2. It’s fully the other way so far that I don’t even fully endorse it, this idea that change needs to be voluntary whenever it is imposed on people. That neither seems like a reasonable ask, nor does it historically end well, as in the paralysis of the West and especially the Anglosphere in many ways, especially in housing.
	3. I am very confident in what would happen if you asked about the changes Sutton is anticipating, and put them to a vote.

Fundamentally, I didn’t pull direct quotes on this but Sutton repeatedly emphasizes that AI\-dominated futures can be good or bad, that he wants us to steer towards good futures rather than bad futures, and that we should think carefully about which futures we are steering towards and choose deliberately.

I can certainly get behind that. The difference is that I don’t think we need to accept this transition to AI dominance as our only option, including that I don’t think we should accept that humans will always be unable to coordinate.

Mostly what I found interesting were the claims around the limitations and nature of LLMs, in ways that don’t make sense to me. This did help solidify a bunch of my thinking about how all of this works, so it felt like a good use of time for that alone.

####

####

####