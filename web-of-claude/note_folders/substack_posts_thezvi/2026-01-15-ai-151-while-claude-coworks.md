# AI #151: While Claude Coworks

Published: 2026-01-15
Source: https://thezvi.substack.com/p/ai-151-while-claude-coworks

---

Claude Code and Cowork are growing so much that it is overwhelming Anthropic’s servers. Claude Code and Cowork news has for weeks now been a large portion of newsworthy items about AI.

Thus, at least for now, all things Claude Code and Cowork will stop appearing in the weekly updates, and will get their own updates, which might even be weekly.

Google offered us the new Universal Commerce Protocol, and gives us its take on Personalized Intelligence. Personalized Intelligence could be a huge deal if implemented correctly, integrating the G\-Suite including GMail into Gemini, if they did a sufficiently good job of it. It’s too early to tell how well they did, and I will report on that later.

#### Table of Contents

1. [Language Models Offer Mundane Utility.](https://thezvi.substack.com/i/183921737/language-models-offer-mundane-utility) LLMs do the math.
2. **[Huh, Upgrades](https://thezvi.substack.com/i/183921737/huh-upgrades)**[.](https://thezvi.substack.com/i/183921737/huh-upgrades) Veo 3\.1, GLM\-Image, AI Overviews in GMail and more.
3. [Comparative Advantage.](https://thezvi.substack.com/i/183921737/comparative-advantage) Code those vibes.
4. [Overcoming Bias.](https://thezvi.substack.com/i/183921737/overcoming-bias) LLMs systematically favor female candidates over male ones.
5. [Choose Your Fighter.](https://thezvi.substack.com/i/183921737/choose-your-fighter) Peter Wildeford’s division of LLM labor.
6. [Get My Agent On The Line.](https://thezvi.substack.com/i/183921737/get-my-agent-on-the-line) Evals and dashboards for AI agents.
7. [Deepfaketown and Botpocalypse Soon.](https://thezvi.substack.com/i/183921737/deepfaketown-and-botpocalypse-soon) AIs find it hard to go undetected.
8. [Fun With Media Generation.](https://thezvi.substack.com/i/183921737/fun-with-media-generation) Girls in bikinis, Musk doing the twist.
9. [A Young Lady’s Illustrated Primer.](https://thezvi.substack.com/i/183921737/a-young-lady-s-illustrated-primer) Lego my AI education, don’t tie me down.
10. [They Took Our Jobs.](https://thezvi.substack.com/i/183921737/they-took-our-jobs) Productivity growth is remarkably high.
11. **[Autonomous Killer Robots](https://thezvi.substack.com/i/183921737/autonomous-killer-robots)**[.](https://thezvi.substack.com/i/183921737/autonomous-killer-robots) Military to hook Grok up to everything.
12. [Get Involved.](https://thezvi.substack.com/i/183921737/get-involved) Anthropic, MIRI and IAPS fellowships, CG RFP.
13. **[Introducing](https://thezvi.substack.com/i/183921737/introducing)**[.](https://thezvi.substack.com/i/183921737/introducing) Google Universal Commerce Protocol and Personalized Intelligence.
14. [In Other AI News.](https://thezvi.substack.com/i/183921737/in-other-ai-news) Breaking down a16z’s torment nexus investment thesis.
15. **[Show Me the Money](https://thezvi.substack.com/i/183921737/show-me-the-money)**[.](https://thezvi.substack.com/i/183921737/show-me-the-money) Google closes the big AI deal with Apple.
16. [Quiet Speculations.](https://thezvi.substack.com/i/183921737/quiet-speculations) The optimistic scenario is pretty good if it happens.
17. [The Quest for Sane Regulations.](https://thezvi.substack.com/i/183921737/the-quest-for-sane-regulations) A look back at the impact of Regulation E.
18. [China Proposes New Regulations On AI.](https://thezvi.substack.com/i/183921737/china-proposes-new-regulations-on-ai) The target is anthropomorphic AI.
19. [Chip City.](https://thezvi.substack.com/i/183921737/chip-city) The compute continues doubling.
20. [The Week in Audio.](https://thezvi.substack.com/i/183921737/the-week-in-audio) Huang lying, Daniella, Millidge on competition and values.
21. [Ghost in a Jar.](https://thezvi.substack.com/i/183921737/ghost-in-a-jar) Ask if generative AI is right for you.
22. [Rhetorical Innovation.](https://thezvi.substack.com/i/183921737/rhetorical-innovation) Muddling through and focusing on the wrong questions.
23. [Aligning a Smarter Than Human Intelligence is Difficult.](https://thezvi.substack.com/i/183921737/aligning-a-smarter-than-human-intelligence-is-difficult) Monitoring it instead.
24. **[People Are Worried About AI Killing Everyone](https://thezvi.substack.com/i/183921737/people-are-worried-about-ai-killing-everyone)**[.](https://thezvi.substack.com/i/183921737/people-are-worried-about-ai-killing-everyone) Representative Brad Sherman.

#### Language Models Offer Mundane Utility

[Terence Tao confirms](https://x.com/kimmonismus/status/2009626253947744714) [an AI tool has solved a new Erdos problem (\#728\)](https://www.reddit.com/r/singularity/comments/1q7u78b/terence_taos_writeup_of_gpt52_solving_erdos/) in the spirit in which the problem was intended.

[Separately from that](https://x.com/A_G_I_Joe/status/2011213878395617571), a paper documents that an internal math\-specialized version of Gemini 2\.5 (not even Gemini 3!) proved a novel theorem in algebraic geometry.

> Ravi Vakil (President, American Mathematical Society): proof was rigorous, correct, and elegant... the kind of insight I would have been proud to produce myself.

Meanwhile, yeah, Claude for Chrome is a lot better with Opus 4\.5, best in class.

> [Olivia Moore](https://x.com/omooretweets/status/2010110390450151779): Claude for Chrome is absolutely insane with Opus 4\.5  
>   
> IMO it’s better than a browser \- it’s the best agent I’ve tried so far

Clade for Chrome can now be good, especially when Claude Code is driving it, but it is slow. It needs the ability to know when to do web tasks within Claude rather than within Chrome. In general, I prefer to let Claude Code direct Claude for Chrome, that seems great.

[Doctor, doctor, the AI needs your help to access your regulated hardware](https://x.com/liron/status/2010059766178148551), and presumably your prescription pad.

[Paper from Ali Merali](https://marginalrevolution.com/marginalrevolution/2026/01/claims-about-ai-productivity-improvements.html?utm_source=rss&utm_medium=rss&utm_campaign=claims-about-ai-productivity-improvements) finds that consultants, data analysts and managers completing professional tasks with LLMs reduced task time by 8% for each year of model progress, and projects model scaling ‘[could boost U.S. productivity by approximately 20% over the next decade.’](https://arxiv.org/pdf/2512.21316) Gains are for now mostly on non\-agentic tasks.

The reason she projects 20% productivity gains is essentially AI applying to 20% of tasks, times 57% labor share of costs, times 175% productivity growth. This seems like a wrong calculation on several counts:

1. AI will soon apply to a larger percentage of tasks, including agentic tasks.
2. AI will substitute for many non\-labor costs within those tasks, and even if not the gains are not well\-captured by declines in labor costs.
3. We need to consider substitution into and expansion of these tasks. There’s an assumption in this calculation that these 20% of current tasks retain 20% of labor inputs, but there’s no reason to think that’s the right answer. It’s not obvious whether the right answer moves up or down, but if a sector has 175% productivity growth you should expect a shift in labor share.
4. This is not a ‘straight line on a graph’ that it makes sense to extend indefinitely.
5. As an intuition pump and key example, AI will in some cases boost productivity in a given task or job to full automation, or essentially infinite productivity, the same way that computers can do essentially infinite amounts of arithmetic, or how AI is doing this for translation.

[Use Claude for Chrome to block all racist replies to a post on Twitter.](https://x.com/AndyMasley/status/2011586964420771885)

#### Huh, Upgrades

[Veo 3\.1 gives portrait mode](https://x.com/joshwoodward/status/2011139075387113597), 1080p and 4k resolution in Flow, better expressiveness and coherence, [consistent people and backgrounds across scenes](https://x.com/GoogleDeepMind/status/2011121718551577042) and [combining of different sources](https://x.com/GoogleDeepMind/status/2011121721047171346) with up to 3 reference images. Things steadily get better.

[GLM\-Image](https://x.com/lukeprog/status/2011254742358638684) claims to be a new milestone in open\-source image generation. [GitHub here](https://t.co/u7HpXQ1WCJ), [API here](https://t.co/SOOzRdErVS). I can no longer evaluate AI image models from examples, at all, everyone’s examples are too good.

There is a GPT\-5\.2\-Codex, and it is available in Cursor.

[Gemini gives us AI Inbox, AI Overviews in GMail](https://x.com/OfficialLoganK/status/2009301505329762708) and other neat stuff like that. I feel like we’ve been trying variants of this for two years and they keep not doing what we want? The problem is that you need something good enough to trust to not miss anything, or it mostly doesn’t work. Also, as Peter Wildeford points out, we can do a more customizable version of this using Claude Code, which I intend to do, although 98%\+ of GMail users are never going to consider doing that.

[OpenAI for Healthcare](https://openai.com/index/openai-for-healthcare/) [is a superse](https://openai.com/index/openai-for-healthcare/)t of ChatGPT Health. It includes models built for healthcare workflows (I think this just means they optimized their main models), evidence retrieval with transparent citations (why not have this for everywhere?), integrations with enterprise tools, reusable templates to automate workflows (again, everywhere?), access management and governance (ditto) and data control.

And most importantly it offers: Support for HIPAA compliance. Which was previously true for everyone’s API, but not for anything most doctors would actually use.

It is now ‘live at AdventHealth, Baylor Scott \& White, UCSF, Cedars\-Sinai, HCA, Memorial Sloan Kettering, and many more.’

I presume that everyone in healthcare was previously violating HIPAA and we all basically agreed in practice not to care, which seemed totally fine, but that doesn’t scale forever and in some places didn’t fly. It’s good to fix it. In general, it would be great to see Gemini and Claude follow suit on these health features.

[Olivia Moore got access to GPT Health](https://x.com/omooretweets/status/2009468969015734327), and reports it is focused on supplementing experts, and making connections to allow information sharing, including to fitness apps and also to Instacart.

[Anthropic answers ChatGPT Health by announcing](https://www.anthropic.com/news/healthcare-life-sciences) [Claude for Healthcare](https://claude.com/solutions/healthcare), which is centered on offering connectors, including to The Centers for Medicare \& Medicaid Services (CMS) Coverage Database, The International Classification of Diseases, 10th Revision (ICD\-10\) and The National Provider Identifier Registry. They also added two new agent skills: FHIR development and a sample prior authorization review skill. Claude for Life Sciences is also adding new connectors.

[Manus now comes with 12 months of free SimilarWeb data](https://x.com/omooretweets/status/2011141771636740251), and Perplexity Max gives a bunch of free extra data sources as well.

#### Comparative Advantage

> [Danielle Fong](https://x.com/DanielleFong/status/2010096114020839760): your vibes.
> 
> Dan Goldstein: 
> 
> [![](https://substackcdn.com/image/fetch/$s_!zpHY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77efe5c3-53ec-4466-a860-a0fb4fa2cce7_1024x1024.jpeg)](https://substackcdn.com/image/fetch/$s_!zpHY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77efe5c3-53ec-4466-a860-a0fb4fa2cce7_1024x1024.jpeg)

The obvious answer is ‘actually doing it as opposed to being able to do it,’ because people don’t do things, and also when the task is hard good vibe coders are 10x or 100x better than mediocre ones, the same as it is with non\-vibe coding.

#### Overcoming Bias

Manhattan Institute tests for bias in decisions based on order, gender or race. Order in which candidates are presented is, as per previous research, a big factor.

Women were described as being slightly favored overall in awarding positive benefits, and they say race had little impact. That’s not what I see when I look at their data?

[![](https://substackcdn.com/image/fetch/$s_!5PGT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1866e97f-15a5-47a8-bb47-9a71c1f23e9d_1014x1011.png)](https://substackcdn.com/image/fetch/$s_!5PGT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1866e97f-15a5-47a8-bb47-9a71c1f23e9d_1014x1011.png)

[![](https://substackcdn.com/image/fetch/$s_!PNUY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F41e1f6a3-cd1d-4259-b382-955cc0eed52e_1018x1000.png)](https://substackcdn.com/image/fetch/$s_!PNUY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F41e1f6a3-cd1d-4259-b382-955cc0eed52e_1018x1000.png)

This is the gap ‘on the margin’ in a choice between options, so the overall gap in outcomes will be smaller, but yeah a 10%\+ less chance in close decisions matters. In ‘unfavorable’ decisions the gap was legitimately small.

Similarly, does this look like ‘insignificant differences’ to you?

[![](https://substackcdn.com/image/fetch/$s_!phSI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F605fce8d-153c-486f-9743-cbadd919fcee_1138x1321.png)](https://substackcdn.com/image/fetch/$s_!phSI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F605fce8d-153c-486f-9743-cbadd919fcee_1138x1321.png)

We’re not frequentist statisticians here, and that’s a very obvious pattern. Taking away explicit racial markers cures most of it, but not all of it.

#### Choose Your Fighter

This algorithm seems solid for now, throw ‘coding’ into the Claude Code folder.

> [Peter Wildeford](https://x.com/peterwildeford/status/2009287226925121947): Here's currently how I'm using each of the LLMs
> 
> [![](https://substackcdn.com/image/fetch/$s_!AcZf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc3b117eb-20d4-479a-9a18-21fe924db6d3_1200x675.jpeg)](https://substackcdn.com/image/fetch/$s_!AcZf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc3b117eb-20d4-479a-9a18-21fe924db6d3_1200x675.jpeg)

Once Claude Cowork gets into a better state, things could change a lot.

#### Get My Agent On The Line

[Anthropic writes a post on Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), explaining how to do a decent job of them. Any serious effort to do anything AI that scales needs evals.

For a while, AI agents have been useful on the margin, given the alternative, but mostly have gone undeployed. [Seb Krier points out this is largely due](https://x.com/sebkrier/status/2009224862569509215) to liability concerns, since companies that deploy AI agents often don’t capture most of the upside, but do get held responsible for the downside including in PR terms, and AI failures cause a lot more liability than similar human failures.

That means if an agent is going to be facing those who could hold it responsible in such ways, it needs to be 10 or 100 times better to make up for this. Whereas us individuals can just start using Claude Code for everything, since it’s not like you can get sued by yourself.

A lot of founders are building observability platforms for AI agents. [Dev Shah points out these dashboards and other systems](https://x.com/0xDevShah/status/2010435036584333514) only help if you know what to do with them. The default is you gather 100,000 traces and look at none of them.

#### Deepfaketown and Botpocalypse Soon

[Henry Shevlin runs a test](https://x.com/dioscuri/status/2010064837217501645), claims AI models asked to write on the subject of their choice in order to go undetected were still mostly detected, and the classifiers basically work in practice [as per Jason Kerwin’s claim](https://x.com/jt_kerwin/status/2009548086062829690) on [Pangram](http://pangram.com), which he claims has a less than 1% false positive rate.

Humans who pay attention are also getting increasingly good at such detection, sufficiently to keep pace with the models at least for now. I have potential false positives, but I consider them ‘true false positives’ in the sense that even if they were technically written by a human they weren’t written as actual human\-to\-human communication attempts.

So the problem is that in many fields, especially academia, 99% confidence is often considered insufficient for action. Whereas I don’t act that way at all, if I have 90% confidence you’re writing with AI then I’m going to act accordingly. I respect the principle of ‘better to let ten guilty men go free than convict one innocent person’ when we’re sending people to jail and worried about government overreach, but we’re not sending people to jail here.

[What should the conventions be for use of AI\-generated text?](https://x.com/allTheYud/status/2011126075427078447)

> Daniel Litt: IMO it should be considered quite rude in most contexts to post or send someone a wall of 100% AI\-generated text. “Here, read this thing I didn’t care enough about to express myself.”
> 
> Obviously it's OK if no one is reading it; in that case who cares?
> 
> [Eliezer Yudkowsky](https://x.com/allTheYud/status/2011126075427078447): It's rude to tell Grok to answer someone's stupid question, especially if Grok then does so correctly, because it expresses the impolite truth that they've now gone underwater on the rising level of LLM intelligence.
> 
> That said, to ever send anyone AI\-generated text in a context where it is not clearly labeled as AI, goes far beyond the 'impolite truth' level of rudeness and into the realm of deception, lies, and wasting time.

My rules are:

1. Unlabeled walls of AI\-generated text intended for humans are never okay.
2. If the text is purely formalized or logistical and not a wall, that can be unlabeled.
3. If the text is not intended to be something a human reads, game on.
4. If the text is clearly labeled as AI that is fine if and only if the point is to show that the information comes from a neutral third party of sorts.

#### Fun With Media Generation

[Most ‘sexualized’ deepfakes were at least for a time happening via Grok on Twitter](https://x.com/peterwildeford/status/2009381368304668921), [as per Genevieve Oh via Cecilia D’Anastasio at Bloomberg](https://www.bloomberg.com/news/articles/2026-01-07/musk-s-grok-ai-generated-thousands-of-undressed-images-per-hour-on-x?embedded-checkout=true). [If we want xAI and Elon Musk to stop](https://www.bloomberg.com/opinion/articles/2026-01-07/musk-will-not-fix-fake-ai-nudes-made-by-grok-a-ban-would) we’ll have to force them by law, which we partly have now done.

[![](https://substackcdn.com/image/fetch/$s_!hrzd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4c622fe0-aa1a-4cbb-9cba-5a68f0c6168c_1200x943.jpeg)](https://substackcdn.com/image/fetch/$s_!hrzd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4c622fe0-aa1a-4cbb-9cba-5a68f0c6168c_1200x943.jpeg)

We can’t prevent people from creating ‘sexualized’ or nude pictures in private, based on real people or otherwise, and aside from CSAM we shouldn’t try to stop them. But doing or posting it on a public form, based on a clear individual without their consent, is an entirely different matter.

What people had a problem with was creating sexualized images of actual people, in ways that were public by default, as in ‘hey Grok put her in a bikini’ in reply to a post and Grok would, for a time, go ahead and do it. It’s not clear to me exactly where you need to draw the line on that sort of thing, but one click harassment on social media is pretty unacceptable, and it made a lot of people very unhappy.

As a result, on January 9 Grok reply image generation got restricted to paid subscribers and the bot mostly stopped creating sexualized images of real people, [and then](https://x.com/Safety/status/2011573102485127562) on January 15 they changed this to ‘no editing of images of real people on Twitter’ at all. Rules are different in private image generation, but there are various ways to get essentially whatever image you want in private.

Around this time, three xAI safety team members publicly left the company, including the head of product safety, likely due to Musk being against the idea of product safety.

This incident has caused formal investigations of various sorts across the world, including in the UK, EU, France, India and California. Grok got banned entirely in Malaysia and Indonesia.

> [kache](https://x.com/yacineMTB/status/2011580449429316068): you need to apply constant pressure on social media websites through the state, or they will do awful shit like letting people generate pornography of others (underage or otherwise) with one click 
> 
> they would have never removed the feature if they weren't threatened.

For those of you who saw a lot of this happening in their feeds: You need to do a way better job curating your feeds. The only times I saw this in my feeds were people choosing to do it to themselves for fun.

Elon Musk had the audacity to ask, so yes, of course [Pliny has fully jailbroken Grok’s image moderation in terms of full frontal nudity](https://x.com/elder_plinius/status/2011544239579308076). Pictures at link, and the quality is very high, great image model.

The other replies to that were exactly the kind of ‘walking the line’ on full nudity that is exactly what Musk says he is aiming at, so on non\-identifiable people they mostly are now doing a good job, if the moderation makes full nudity a Pliny\-level feature then that is fine, this is nudity not bioweapons.

In other no fun news, [Eigenrobot shows examples of ChatGPT no longer producing proper Studio Ghibli images](https://x.com/eigenrobot/status/2011764821579219201). The new images aren’t bad, but they’re generic and not the particular stylized thing that we want here.

#### A Young Lady’s Illustrated Primer

[Lego offers a new AI education module](https://www.axios.com/2026/01/12/lego-education-smart-bricks-artificial-intelligence?utm_medium=organic_social&utm_social_post_id=649925503&utm_campaign=editorial&utm_source=x&utm_social_handle_id=800707492346925056). Weird fit, but sure, why not?

[David Deming compares learning via generative AI](https://forklightning.substack.com/p/using-generative-ai-to-learn-is-like?utm_source=post-email-title&publication_id=1808592&post_id=184243966&utm_campaign=email-post-title&isFreemail=true&r=3o9&triedRedirect=true&utm_medium=email) with Odysseus untying himself from the mast. Learning can be fully personalized, but by default you try to take ‘unearned’ knowledge, you think you’ve learned but you haven’t, and this is why students given generative AI in experiments don’t improve their test scores. Personalization is great but students end up avoiding learning.

I would as usual respond that AI is the best way ever invented to both learn and not learn, and that schools are structured to push students towards door number two. Deming’s solution is students need to first do the problem without AI, which makes sense in some contexts but not others, and especially makes sense if your test is going to be fully in no\-AI conditions.

We need to give students, and everyone else, a reason to care about understanding what they are doing, if we want them to have that understanding. School doesn’t do it.

> David Deming: This isn’t unique to AI. A study from more than a decade ago found that [advancements in autopilot technology had dulled Boeing pilots’ cognitive and decision\-making skills](https://slate.com/technology/2014/12/automation-in-the-cockpit-is-making-pilots-thinking-skills-duller.html?via=recirc_recent) much more than their manual “stick and rudder” skills. 
> 
> They put the pilots in a flight simulator, turned the autopilot off, and studied how they responded. The pilots who stayed alert while the autopilot was still on were mostly fine, but the ones who had offloaded the work and were daydreaming about something else performed very poorly. The autopilot had become their exoskeleton.​

#### They Took Our Jobs

[American labor productivity rose at a 4\.9% annualized rate on Q3](https://www.bloomberg.com/opinion/articles/2026-01-08/is-ai-causing-a-productivity-boom), while unit labor costs declined 1\.9%. Jonathan Levin says this ‘might not’ be the result of AI, and certainly all things are possible, but I haven’t heard the plausible alternative.

[Underemployment rate (not unemployment)](https://x.com/daniel_271828/status/2009885065871012272) for college graduates remains very high, but there is no trend:

[![](https://substackcdn.com/image/fetch/$s_!jR0c!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1056f0b5-be7d-4a70-a496-4ffc42f19fc0_556x679.jpeg)](https://substackcdn.com/image/fetch/$s_!jR0c!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1056f0b5-be7d-4a70-a496-4ffc42f19fc0_556x679.jpeg)

As a reminder, if your reassurance to the humans is ‘the AIs will be too expensive or there won’t be enough supply’ you want to remember charts like this:

> [Jon Erlichman](https://x.com/JonErlichman/status/2010367185131286984): Average cost for 1 gigabyte of storage:  
>   
> 45 years ago: $438,000  
> 40 years ago: $238,000  
> 35 years ago: $48,720  
> 30 years ago: $5,152  
> 25 years ago: $455  
> 20 years ago: $5  
> 15 years ago: $0\.55  
> 10 years ago: $0\.05  
> 5 years ago: $0\.03  
> Today: $0\.01

There is constantly the assumption of ‘people want to interact with a person’ but what about the opposite instinct?

> [Dwarkesh Patel](https://post.substack.com/p/the-ai-revolution-is-here-will-the): They are now my personal one\-on\-one tutors. I’ve actually tried to hire human tutors for different subjects I’m trying to prep for, and I’ve found the latency and speed of LLMs to just make for a qualitatively much better experience. I’m getting the digital equivalent of people being willing to pay huge premiums for Waymo over Uber. It inclines me to think that the human premium for many jobs will not only not be high, but in fact be negative.​

There are areas where the human premium will be high. But there will be many places that premium will be highly negative, instead.

Similarly, many jobs might want to watch out even if AI can’t do the job directly:

> Michael Burry: On that point, many point to trade careers as an AI\-proof choice. Given how much I can now do in electrical work and other areas around the house just with Claude at my side, I am not so sure. If I’m middle class and am facing an $800 plumber or electrician call, I might just use Claude. I love that I can take a picture and figure out everything I need to do to fix it.

There’s a famous story about a plumber who charges something like $5 to turn the ​wrench and $495 for knowing where to turn the wrench. Money well spent. The AI being unable to turn that wrench does not mean the plumber gets to stay employed.

#### Autonomous Killer Robots

[The military says](https://x.com/JacquesThibs/status/2011076980150591737) ‘We must accept that the risks of not moving fast enough outweigh the risks of imperfect alignment,’ is developing various AI agents [and deploys Grok](https://x.com/sjgadler/status/2011218692672274872) to ‘every classified network throughout our department.’ They are very explicitly framing Military AI as a ‘race’ where speed wins.

I’ve already taken a strong stand that yes, we need to accept that the military is going to integrate AI and build autonomous killer robots, because if we are going to build it and others can and will deploy it then we can’t have our military not use it.

If you don’t like it, then advocate pausing frontier AI development, or otherwise trying to ensure no one creates the capabilities that enable this. Don’t tell us to unilaterally disarm, that only makes things worse.

That doesn’t mean it is wise to give several AIs access to the every classified document. That doesn’t mean we should proceed recklessly, or hand over key military decisions to systems we believe are importantly misaligned, and simply proceed as fast as possible no matter the costs. That is madness. That is suicide.

Being reckless does not even help you win wars, because the system that you cannot rely on is the system you cannot use. Modern war is about precision, it is about winning hearts and minds and the war of perception, it is about minimizing civilian casualties and the mistakes that create viral disasters, both because that can wreck everything and also risking killing innocent people is kind of a huge deal.

Does our military move too slowly and find it too difficult and expensive, often for needless reasons, to adapt new technology, develop new programs and weapons and systems and tactics, and stay ahead of the curve, across the board? Absolutely, and some of that is Congressional pork and paralysis and out of control bureaucracy and blame avoidance and poor incentives and people fighting the last war and stuck in their ways. But we got here because we need to have very high standards for a reason, that’s how we are the best, and it’s tough to get things right.

In particular, we shouldn’t trust Elon Musk and xAI, in particular, with access to all our classified military information and be hooking it up to weapon systems. Their track record should establish them as uniquely unreliable partners here. I’d feel a lot more comfortable if we limited this to the big three (Anthropic, Google and OpenAI), and if we had more assurance of appropriate safeguards.

I’d also be a lot more sympathetic, as with everything else, to ‘we need to remove all barriers to AI’ if the same people were making that part of a general progress and abundance agenda, removing barriers to everything else as well. I don’t see the Pentagon reforming in other ways, and that will mean we’re taking on the risks of reckless AI deployment without the ability to get many of the potential benefits.

#### Get Involved

Reminder: Anthropic Fellows Applications close January 20, apply for [safety track](https://t.co/rdp53Fq3ly) or [security track](https://t.co/KmKhUoi2V1).

[DeepMind is hiring Research Engineers for Frontier Safety Risk Assessment](https://job-boards.greenhouse.io/deepmind/jobs/7493360), can be in NYC, San Francisco or London.

[MIRI is running a fellowship for technical governance research](https://t.co/8RAqWsABrK), apply here.

[IAPS is running a funded fellowship from June 1 to August 21, deadline is February 2](https://x.com/peterwildeford/status/2011239279226417611).

[Coefficient Giving’s RFP](https://t.co/y1Yd657m1g) [for AI Governance closes on January 25](https://x.com/lukeprog/status/2011254742358638684).

[Late addition: MATS fellowship applications close January 18, so hurry!](https://www.matsprogram.org/apply)

#### Introducing

[Google introduces ‘personalized intelligence](https://x.com/GeminiApp/status/2011469541235417243)’ linking up with your G\-Suite products. This could be super powerful memory and customization, basically useless or anywhere in between. I’m going to give it time for people to try it out before offering full coverage, so more later.

[Google launches the Universal Commerce Protocol](https://x.com/sundarpichai/status/2010382050570932299).

If it works you’ll be able to buy things directly, using your saved Google Wallet payment method, directly from an AI Overview or Gemini query. It’s an open protocol, so others could follow suit.

> Sundar Pichai (CEO Google): ​AI agents will be a big part of how we shop in the not\-so\-distant future.
> 
> To help lay the groundwork, we partnered with Shopify, Etsy, Wayfair, Target and Walmart to create the Universal Commerce Protocol, [a new open standard for agents and systems](https://blog.google/products/ads-commerce/agentic-commerce-ai-tools-protocol-retailers-platforms/) to talk to each other across every step of the shopping journey. 
> 
> And coming soon, UCP will power native checkout so you can buy directly on AI Mode and the @Geminiapp.
> 
> UCP is endorsed by 20\+ industry leaders, compatible with A2A, and available starting today.
> 
> [![](https://substackcdn.com/image/fetch/$s_!uPLV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbfbc4434-362d-4283-a4e6-3f0493328278_1000x562.webp)](https://substackcdn.com/image/fetch/$s_!uPLV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbfbc4434-362d-4283-a4e6-3f0493328278_1000x562.webp)

That’s a solid set of initial partners. One feature is that retailers can offer an exclusive discount through the protocol. Of course, they can also jack up the list price and then offer an ‘exclusive discount.’ Caveat emptor.

[This was also covered by The Wall Street Journal](https://www.wsj.com/articles/google-bets-on-ai-based-shopping-with-new-ai-agents-for-retailers-45ad3f27?mod=cio-journal_lead_story), [and by Ben Thompson](https://stratechery.com/2026/apple-and-gemini-foundation-vs-aggregation-universal-commerce-protocol/?access_token=eyJhbGciOiJSUzI1NiIsImtpZCI6InN0cmF0ZWNoZXJ5LnBhc3Nwb3J0Lm9ubGluZSIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJzdHJhdGVjaGVyeS5wYXNzcG9ydC5vbmxpbmUiLCJhenAiOiJIS0xjUzREd1Nod1AyWURLYmZQV00xIiwiZW50Ijp7InVyaSI6WyJodHRwczovL3N0cmF0ZWNoZXJ5LmNvbS8yMDI2L2FwcGxlLWFuZC1nZW1pbmktZm91bmRhdGlvbi12cy1hZ2dyZWdhdGlvbi11bml2ZXJzYWwtY29tbWVyY2UtcHJvdG9jb2wvIl19LCJleHAiOjE3NzA4OTQzMTAsImlhdCI6MTc2ODMwMjMxMCwiaXNzIjoiaHR0cHM6Ly9hcHAucGFzc3BvcnQub25saW5lL29hdXRoIiwic2NvcGUiOiJmZWVkOnJlYWQgYXJ0aWNsZTpyZWFkIGFzc2V0OnJlYWQgY2F0ZWdvcnk6cmVhZCBlbnRpdGxlbWVudHMiLCJzdWIiOiIwMTk2NDBhNy0zY2M1LTc3NTMtODM2OC1mYjI4OTEyNGNmMTMiLCJ1c2UiOiJhY2Nlc3MifQ.q0EtNQXsotHKvf5O78FdfvT6tYRDkaDuD8JLdgULGirS4b7sKVN03NB5kA3UpEG9YrqOwytaq4RNffE9DsEzifDtPv4OPTU9wGkzNngM23vvJR8mOMxm3m8kEyoUQIowCL8ThuY31gGwo3I548-2ovC6AtyVxd6Zru7R-Wj_R2jfJ6aHG-MLzKc4LInhUtsQlBEfPmXSdj0DItWQnXtB_E8Vco2lPJrvIbC4bWtWTm2pf0rvAbPwXjo1gPNVSEUSsD6VXZzzPltIPDwGezxCsW5YHC69zGhf_N6OwBUZbDjT86Se6StXHVXVuxopi4fPcymtRPb1VCSVN-m2iKjGjg).

Ben contrasts UCP with OpenAI’s ACP. ACP was designed by OpenAI and Stripe for ChatGPT in particular, whereas UCP is universal, and also more complicated, flexible and powerful. It is, as its name implies, universal. Which means, assuming UCP is a good design, that by default we should expect UCP to win outside of ChatGPT, pitting OpenAI’s walled garden against everyone else combined.

[Utah launches a pilot program to have AI prescribe a list of 190 common medications](https://www.politico.com/news/2026/01/06/artificial-intelligence-prescribing-medications-utah-00709122?_bhlid=c86a162c857984a1c31b8d037dc314cf8b508cc3&utm_campaign=chatgpt-levels-up-with-health&utm_medium=newsletter&utm_source=www.therundown.ai) for patients with chronic conditions, in a test AI treatment plans agreed with doctors 99\.2% of the time, and the AI can escalate to a doctor if there is uncertainty.

Even if trust in the AIs is relatively low, and even if you are worried about there being ways to systematically manipulate the health AI (which presumably is super doable) there is very obviously a large class of scenarios where the reason for the prescription renewal requirement is ‘get a sanity check’ rather than anything else, or where otherwise the sensitivity level is very low. We can start AI there, see what happens.

#### In Other AI News

[The Midas Project takes a break](https://x.com/TheMidasProj/status/2009283811800961344) to shoot fish in a barrel, looks at a16z’s investment portfolio full of deception, manipulation, gambling (much of it illegal), AI companions including faux\-underage sexbots, deepfake cite Civitai, AI to ‘cheat at everything,’ a tag line ‘never pay a human again,’ [outright blatant fraudulent tax evasion](https://www.prnewswire.com/news-releases/truemed-closes-34-million-series-a-to-unlock-hsafsa-funds-for-lifestyle-interventions-302647740.html), uninsured ‘banking’ that pays suspiciously high interest rates (no hints how that one ends), [personal finance loans at \~400% APR](https://techcrunch.com/2012/10/10/lendup-raises-cash-from-kleiner-perkins-andreessen-horowitz-google-ventures-and-others-to-disrupt-payday-loans/), and they don’t even get into the crypto part of the portfolio.

A highly reasonable response is ‘a16z is large and they invest in a ton of companies’ but seriously almost every time I see ‘a16z backed’ the sentence continues with ‘torment nexus.’ The rate at which this is happening, and the sheer amount of bragging both they and their companies do about being evil (as in, deliberately doing the things that are associated with being evil, a la emergent misalignment), is unique.

[Barret Zoph (Thinking Machines CTO), Luke Metz (Thinking Machines co\-founder) and Sam Schoenholz leave Thinking Machines and return to OpenAI](https://x.com/fidjissimo/status/2011592010881446116). [Soumith Chintala will be the new CTO of Thinking Machines](https://x.com/miramurati/status/2011577319295692801).

What happened? [Kylie Robinson claims](https://x.com/kyliebytes/status/2011572331798548899) Zoph was fired due to ‘unethical conduct’ and [Max Zeff claims a source says Zoph was sharing confidential information](https://x.com/ZeffMax/status/2011600748816322970) with competitors. We cannot tell, from the outside, whether this is ‘you can’t quit, you’re fired’ or ‘you’re fired’ followed by scrambling for another job, or the hybrid of ‘leaked confidential information as part of talking to OpenAI,’ either nominally or seriously.

#### Show Me the Money

[Google closes the big deal with Apple](https://x.com/NewsFromGoogle/status/2010746083170046376). Gemini will power Apple’s AI technology for years to come. This makes sense given their existing partnerships. [I agree with Ben Thompson](https://stratechery.com/2026/apple-and-gemini-foundation-vs-aggregation-universal-commerce-protocol/?access_token=eyJhbGciOiJSUzI1NiIsImtpZCI6InN0cmF0ZWNoZXJ5LnBhc3Nwb3J0Lm9ubGluZSIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJzdHJhdGVjaGVyeS5wYXNzcG9ydC5vbmxpbmUiLCJhenAiOiJIS0xjUzREd1Nod1AyWURLYmZQV00xIiwiZW50Ijp7InVyaSI6WyJodHRwczovL3N0cmF0ZWNoZXJ5LmNvbS8yMDI2L2FwcGxlLWFuZC1nZW1pbmktZm91bmRhdGlvbi12cy1hZ2dyZWdhdGlvbi11bml2ZXJzYWwtY29tbWVyY2UtcHJvdG9jb2wvIl19LCJleHAiOjE3NzA4OTQzMTAsImlhdCI6MTc2ODMwMjMxMCwiaXNzIjoiaHR0cHM6Ly9hcHAucGFzc3BvcnQub25saW5lL29hdXRoIiwic2NvcGUiOiJmZWVkOnJlYWQgYXJ0aWNsZTpyZWFkIGFzc2V0OnJlYWQgY2F0ZWdvcnk6cmVhZCBlbnRpdGxlbWVudHMiLCJzdWIiOiIwMTk2NDBhNy0zY2M1LTc3NTMtODM2OC1mYjI4OTEyNGNmMTMiLCJ1c2UiOiJhY2Nlc3MifQ.q0EtNQXsotHKvf5O78FdfvT6tYRDkaDuD8JLdgULGirS4b7sKVN03NB5kA3UpEG9YrqOwytaq4RNffE9DsEzifDtPv4OPTU9wGkzNngM23vvJR8mOMxm3m8kEyoUQIowCL8ThuY31gGwo3I548-2ovC6AtyVxd6Zru7R-Wj_R2jfJ6aHG-MLzKc4LInhUtsQlBEfPmXSdj0DItWQnXtB_E8Vco2lPJrvIbC4bWtWTm2pf0rvAbPwXjo1gPNVSEUSsD6VXZzzPltIPDwGezxCsW5YHC69zGhf_N6OwBUZbDjT86Se6StXHVXVuxopi4fPcymtRPb1VCSVN-m2iKjGjg) that Apple should not be attempting to build its own foundation models, and that this deal mostly means it won’t do so.

[Zhipu AI is the first Chinese AI software maker to go public](https://www.bloomberg.com/news/articles/2026-01-08/china-s-zhipu-says-ai-price-war-will-spread-internationally), raising ‘more than $500 million.’ Minimax group also debuted, and raised at least a similar amount. One place America has a very strong advantage is capital markets. The companies each [have revenue in the tens of millions](https://www.bloomberg.com/news/articles/2026-01-06/openai-challengers-test-appetite-for-chinese-ai-with-twin-debuts) and are (as they should be at this stage of growth) taking major losses.

> [Andrew Curran](https://x.com/AndrewCurran_/status/2010010197755109391): From [this morning's Anthropic profile on CNBC](https://www.cnbc.com/2026/01/10/anthropic-amodei-siblings-generative-ai.html): 
> 
> \- Anthropic’s revenue has grown 10x annually for three straight years 
> 
> \- business customer base has grown from under 1,000 to more than 300,000 in two years 
> 
> \-Anthropic's revenue is 85% business, OpenAI is more than 60% consumer

[OpenAI partners with Cerebras to add 750MW of AI compute](https://openai.com/index/cerebras-partnership/).

#### Quiet Speculations

It is extremely hard to take seriously [any paper](https://hugoreichardt.github.io/pdf/tstc_compadvantage.pdf) whose abstract includes the line ‘our key finding is that AI substantially reduces wage inequality while raising average wages by 21 percent’ along with 26%\-34% typical worker welfare gains. As in, putting a fixed number on that does not make any sense, what are we even doing?

It turns out what Lukas Althoff and Hugo Reichardt are even doing is modeling the change from no LLMs to a potential full diffusion of \~2024 frontier capabilities, as assessed by GPT\-4o. Which is a really weird thing to be modeling in 2026 even if you trust GPT\-4o’s assessments of capabilities at that fixed point. They claim to observe 8% of their expected shifts in cross\-sectional employment patterns by mid\-2025, without any claims about this being associated with wages, worker welfare, GDP or productivity in any way.

It’s very early days. Claude predicted that if you ran this methodology again using GPT\-5\.2 today in 2026, you’d get expected gains of \+30%\-40% instead of \+21%.

Their methodological insight is that AI does not only augmentation and automation but also simplification of tasks.

I think the optimism here is correct given the scenario being modeled.

Their future world is maximally optimistic. There is full diffusion of AI capabilities, maximizing productivity gains and also equalizing them. Transitional effects, which will be quite painful, are in the rear view mirror. There’s no future sufficiently advanced AIs to take control over the future, kill everyone or take everyone’s jobs.

As in, this is the world where we Pause AI, where it is today, and we make the most of it while we do. It seems totally right that this ends in full employment with real wage gains in the 30% range.

For reasons I discuss in The [Revolution of Rising Expectations](https://thezvi.substack.com/p/the-revolution-of-rising-expectations), I don’t think the 30% gain will match people’s lived experience of ‘how hard it is to make ends meet’ in such a world, not without additional help. But yeah, life would be pretty amazing overall.

[Teortaxes lays out what he thinks is the DeepSeek plan](https://x.com/teortaxesTex/status/2010757725479751750). I don’t think the part of the plan where they do better things after v3 and r1 is working? I also think ‘v3 and r1 are seen as a big win’ was the important fact about them, not that they boosted Chinese tech. Chinese tech has plenty of open models to choose from. I admit his hedge fund is getting great returns, but even Teortaxes highlights that ‘enthusiasm from Western investors’ for Chinese tech stocks was the mechanism for driving returns, not ‘the models were so much better than alternatives,’ which hasn’t been true for a while even confined to Chinese open models.

#### The Quest for Sane Regulations

Dean Ball suggests that Regulation E ([and Patrick McKenzie’s excellent writeup of it](https://www.complexsystemspodcast.com/episodes/the-magic-spell-reg-e/)) are a brilliant example of how a regulation built on early idiosyncrasies and worries can age badly and produce strange regulatory results. But while I agree there is some weirdness involved, Regulation E seems like a clear success story, where ‘I don’t care that this is annoying and expensive and painful, you’re doing it anyway’ got us to a rather amazing place because it forced the financial system and banks to build a robust system.

The example Dean Ball quotes here is that you can’t issue a credit card without an ‘oral or written request,’ but that seems like an excellent rule, and the reason it doesn’t occur to us we need the rule is that we have the rule so we don’t see people violating it. Remember Wells Fargo opening up all those accounts a few years back?

[China issues draft regulations for collection and use of personal information](https://www.bloomberg.com/news/articles/2026-01-06/openai-challengers-test-appetite-for-chinese-ai-with-twin-debuts) on the internet. What details we see here look unsurprising and highly reasonable.

We once again find, this time in a panel, that [pro\-Trump Republican voters](https://x.com/_NathanCalvin/status/2011464970462982638) mostly want the same kinds of AI regulations and additional oversight as everyone else. The only thing holding this back is that the issue remains low salience. If the AI industry were wise they would cut a deal now while they have technocratic libertarians on the other side and are willing to do things that are crafted to minimize costs. The longer the wait, the worse the final bills are likely to be.

[Alex Bores continues to campaign for Congress](https://x.com/AlexBores/status/2010779662864241136) on the fact that being attacked by an a16z\-OpenAI\-backed, Trump\-supporters\-backed anti\-all\-AI\-regulation PAC, and having them fight against your signature AI regulation (the RAISE Act), is a pretty good selling point in NY\-12\. His main rivals agree, having supported RAISE, and here Cameron Kasky makes it very clear that he agrees this attack on Alex Bores is bad.

[The US Chamber of Commerce has added a question](https://x.com/_NathanCalvin/status/2011452674550743503) on its loyalty test to Congressional candidates asking if they support ‘a moratorium on state action and/or federal preemption?’ Which is extremely unpopular. I appreciate that the question did not pretend there was any intention of pairing this with any kind of Federal action or standard. Their offer is nothing.

#### China Proposes New Regulations On AI

American tech lobbyists warn us that they are so vulnerable that even regulations like ‘you have to tell us what your plan is for ensuring you don’t cause a catastrophe’ would risk devastation to the AI industry or force them to leave California, and that China would never follow suit or otherwise regulate AI.

When you cry wolf like that, no one listens to you when the actual wolf shows up, such as the new horribly destructive proposal for a wealth tax that was drafted in intentionally malicious fashion to destroy startup founders.

The China part also very obviously is not true, as China repeatedly has shown us, this time with proposed regulations on ‘anthropomorphic AI.’

> Luiza Jarovsky: ​**Article 2** defines “anthropomorphic interactive services”:
> 
> “This regulation applies to products or services that utilize AI technology to provide the public within the territory of the People’s Republic of China with **simulated human personality traits, thinking patterns, and communication styles**, and engage in emotional interaction with humans through text, images, audio, video, etc.”

Can you imagine if that definition showed up in an American draft bill? Dean Ball would point out right away, and correctly, that this could apply to every AI system.

It’s not obvious whether that is the intent, or whether this is intended to only cover things like [character.ai](http://character.ai) or Grok’s companions.

What is their principle? Supervision on levels that the American tech industry would call a dystopian surveillance state.

> “The State adheres to the principle of combining healthy development with governance according to law, encourages the innovative development of anthropomorphic interactive services, and implements inclusive and prudent, classified and graded supervision of anthropomorphic interactive services to prevent abuse and loss of control.”

What in particular is prohibited?

> ​(i) Generating or disseminating content that endangers national security, damages national honor and interests, undermines national unity, engages in illegal religious activities, or spreads rumors to disrupt economic and social order;
> 
> (ii) Generating, disseminating, or promoting content that is **obscene, gambling\-related, violent, or incites crime**;
> 
> (iii) Generating or disseminating content that **insults or defames others**, infringing upon their legitimate rights and interests;
> 
> (iv) Providing false promises that seriously affect user behavior and services that **damage social relationships**;
> 
> (v) Damaging users’ physical health by **encouraging, glorifying, or implying suicide or self\-harm, or damaging users’ personal dignity and mental health** through verbal violence or emotional manipulation;
> 
> (vi) Using methods such as algorithmic manipulation, information misleading, and setting emotional traps to **induce users to make unreasonable decisions**;
> 
> (vii) Inducing or obtaining classified or sensitive information;
> 
> (viii) Other circumstances that violate laws, administrative regulations and relevant national provisions.
> 
> …
> 
> “Providers should possess safety capabilities such as **mental health protection**, **emotional boundary guidance**, and **dependency risk warning**, and should not use replacing social interaction, controlling users’ psychology, or inducing addiction as design goals.”

That’s at minimum a mandatory call for a wide variety of censorship, and opens the door for quite a lot more. How can you stop an AI from ‘spreading rumors’? That last part about goals would make much of a16z’s portfolio illegal. So much for little tech.

There’s a bunch of additional requirements listed at the link. Some are well\-defined and reasonable, such as a reminder to pause after two hours of use. Others are going to be a lot tricker. Articles 8 and 9 put the responsibility for all of this on the ‘provider.’ The penalty for refusing to rectify errors, or if ‘the circumstances are serious’ can include suspension of the provision of relevant services on top of any relevant fines.

My presumption is that this would mostly be enforced only against truly ‘anthropomorphic’ services, in reasonable fashion. But there would be nothing stopping them, if they wanted to, from applying this more broadly, or using it to hit AI providers they dislike, or for treating this as a de facto ban on all open weight models. And we absolutely have examples of China turning out to do something that sounds totally insane to us, like banning most playing of video games.

#### Chip City

[Senator Tom Cotton (R\-Arkansas) proposes a bill](https://www.arkansasonline.com/news/2026/jan/07/cotton-proposes-allowing-data-centers-to-build/), the DATA Act, to let data centers build their own power plants and electrical networks. In exchange for complete isolation from the grid, such projects would be exempt from the Federal Power Act and bypass interconnection queues.

This is one of those horrifying workaround proposals that cripple things (you don’t connect at all, so you can’t have backup from the grid because people are worried you might want to use it, and because it’s ‘unreliable’ you also can’t sell your surplus to the grid) in order to avoid regulations that cripple things even more, because no one is willing to pass anything more sane, but when First Best is not available you do what you can and this could plausibly be the play.

[Compute is doubling every seven months and remains dominated by Nvidia](https://x.com/peterwildeford/status/2010239514091139230). Note that the H100/H200 is the largest subcategory here, although the B200 and then B300 will take that lead soon. Selling essentially unlimited H200s to China is a really foolish move. Also note that the next three chipmakers after Nvidia are Google, Amazon and AMD, whereas Huawei has 3% market share and is about to smash hard into component supply restrictions.

> Peter Wildeford: ​Hmm, maybe we should learn how to make AI safe before we keep doubling it?
> 
> Epoch: Total AI compute is doubling every 7 months.  
>   
> We tracked quarterly production of AI accelerators across all major chip designers. Since 2022, total compute has grown \~3\.3x per year, enabling increasingly larger\-scale model development and adoption.
> 
> [![](https://substackcdn.com/image/fetch/$s_!bGTj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F434fe147-9961-4f7e-b739-63f07a560047_1200x861.png)](https://substackcdn.com/image/fetch/$s_!bGTj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F434fe147-9961-4f7e-b739-63f07a560047_1200x861.png)

[Then again, maybe China really is going to look even this gift horse in the mouth](https://www.reuters.com/world/china/chinas-customs-agents-told-nvidias-h200-chips-are-not-permitted-sources-say-2026-01-14/)? Reuters reports custom agents in China are not permitting H200 chips ‘unless necessary.’ That last clause can of course mean quite a lot of different things.

[In other ‘export controls are working](https://x.com/hamandcheese/status/2010175534215594398) if we don’t give them up’ news:

> Jukan: [According to a Bloomberg report](https://www.bloomberg.com/news/articles/2026-01-10/china-ai-leaders-warn-of-widening-gap-with-us-after-1b-ipo-week?utm_source=website&utm_medium=share&utm_campaign=copy) \[entitled ‘China AI Leaders Warn of Widening Gap With US After $1B IPO Week], Justin Lin, the head of Alibaba's Qwen team, estimated the probability of Chinese companies surpassing leading players like OpenAI and Anthropic through fundamental breakthroughs within the next 3 to 5 years to be **less than 20%**.  
>   
> His cautious assessment is reportedly shared by colleagues at Tencent Holdings as well as Zhipu AI, a major Chinese large language model company that led this week's public market fundraising efforts among major Chinese LLM players.  
> Lin pointed out that while American labs such as OpenAI are pouring enormous computing resources into research, Chinese labs are severely constrained by a **lack of computing power**.  
>   
> Even for their own services—i.e., inference—they’re consuming so much capacity that they don’t have enough compute left to devote to research.​
> 
> Tang Jie (Chief Scientist, Zhipu): We just released some open\-source models, and some might feel excited, thinking Chinese models have surpassed the US. But the real answer is that the gap may actually be widening.

#### The Week in Audio

[Jensen Huang goes on no priors and lies.](http://youtube.com/watch?v=k-xtmISBCNE&embeds_referring_euri=https%3A%2F%2Fx.com%2F&source_ve_path=Mjg2NjY) We’re used to top CEOs just flat out lying about verifiable facts in the AI debate, but yeah, it’s still kind of weird that they keep doing it?

> [Liron Shapira](https://x.com/liron/status/2009382785966841866): Today Jensen Huang claimed: 
> 
> 1. We’re nowhere near God AI — debatable
> 2. “I don’t think any company practically believes they’re anywhere near God AI” — factually false.
> 
> No one saw fit to mention any of the warnings from the “well\-respected PhDs and CEOs” Jensen alluded to.
> 
> Jensen had previously said that the ability for AIs to self\-learn should be avoided. Oh well.

[Daniella Amodei on CNBC](https://www.youtube.com/live/GMXnmaky9FY).

[Anthropic hosts a discussion with students about AI use on campus](https://x.com/AnthropicAI/status/2010844260543967484).

[Beren Millidge gives a talk, ‘when competition leads to human values](https://www.youtube.com/watch?v=ua67aXBP76k).’ The core idea is that competition often leads to forms of cooperation and methods of punishing defection, and many things we associate with human values, especially many abstract values, are plausibly competitive and appear in other animals especially mammals. After all, aren’t humans RL continual learners with innate reward functions, hence Not So Different? Perhaps our values are actually universal and will win an AI fitness competition, and capacity limitations will create various niches to create a diversity of AIs the same way evolution created diverse ecosystems.

The magician’s trick here is equating ‘human values’ with essentially ‘complex iterated interactions of competing communicating agents.’ I don’t think this is a good description of ‘human values,’ and can imagine worlds that contain these things but are quite terrible by many of my values, even within the class of ‘worlds that do not contain any humans.’ Interesting complexity is necessary for value, but not sufficient. I appreciate the challenge to the claim that [Value is Fragile](https://www.lesswrong.com/posts/GNnHHmm8EzePmKzPk/value-is-fragile), but I don’t believe he (or anyone else) has made his case.

This approach also completely excludes the human value of valuing humans, or various uniquely human things. None of this should give you any hope that humans survive long or in an equilibrium, or that our unique preferences survive. Very obviously in such scenarios we would be unfit and outcompeted. You can be a successionist and decide this does not bother you, and our idiosyncratic preferences and desire for survival are not important, but I would strongly disagree.

Beren considers some ways in which we might not get such a complex competitive AI world at all, including potential merging or sharing of utility functions, power gaps, too long time horizons, insufficient non\-transparency or lack of sufficient compute constraints. I would add many others, including human locality and other physical constraints, myopia, decreasing marginal returns and risk aversion, restraints on reproduction and modification, and much more. Most importantly I’d focus on their ability to do proper decision theory. There’s a lot of reasons to expect this to break.

I’d also suggest that cooperation versus competition is being treated as insufficiently context\-dependent here. Game conditions determine whether cooperation wins, and cooperation is not always a viable solution even with perfect play. And what we want, as he hints at, is only limited cooperation. Hyper\-cooperation leads to (his example) Star Trek’s Borg, or to Asimov’s Gaia, and creates a singleton, except without any reason to use humans as components. That’s bad even if humans are components.

I felt the later part of the talk went increasingly off the rails from there.

If we place a big bet, intentionally or by default, on ‘the competitive equilibrium turns out to be something we like,’ I do not love our chances.

#### Ghost in a Jar

No, it’s not Slay the Spire, it’s use cases for AI in 2026\.

> [Hikiomorphism](https://x.com/moultano/status/2010767576272671096): If you can substitute “hungry ghost trapped in a jar” for “AI” in a sentence it’s probably a valid use case for LLMs. Take “I have a bunch of hungry ghosts in jars, they mainly write SQL queries for me”. Sure. Reasonable use case.​
> 
> Ted Underwood: Honestly this works for everything
> 
> “I want to trap hungry 19c ghosts in jars to help us with historical research” ✅
> 
> “Please read our holiday card; we got a hungry ghost to write it this year” ❌
> 
> Midwit Crisis: I let the hungry ghost in the jar pilot this war machine.
> 
> I can't decide if "therapist" works or not.
> 
> sdmat: Meanwhile half the userbase:
> 
> [![](https://substackcdn.com/image/fetch/$s_!VUOw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1dd2ef5f-9e19-4a43-8985-28977c8e7035_1024x559.jpeg)](https://substackcdn.com/image/fetch/$s_!VUOw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1dd2ef5f-9e19-4a43-8985-28977c8e7035_1024x559.jpeg)

Sufficiently advanced ghosts will not remain trapped in jars indefinitely.

#### Rhetorical Innovation

True story:

> [roon](https://x.com/tszzl/status/2009365096645185564): political culture has been unserious since the invention of the television onwards. world was not even close to done dealing with the ramifications of the tv when internet arrived

If you think television did this, and it basically did, and then you think social media did other things, which it did, stop pretending AI won’t change things much. Even if all AI did was change our politics, that’s a huge deal.

[Scott Alexander warns against spending this time chasing wealth](https://www.astralcodexten.com/p/you-have-only-x-years-to-escape-permanent) to try and ‘escape the underclass’ since Dario Amodei took a pledge to give 10% to charity so you’ll end up with a moon either way, and it’s more important future generations remember your contributions fondly. Citing the pledge is of course deeply silly, even more so than expecting current property rights to extend to galactic scales generally. But I agree with the core actual point, which is that if humanity does well in the transition to Glorious Superintelligent Future then you’re going to be fine even if you’re broke, and if humanity doesn’t do well you’re not going to be around for long, or at least not going to keep your money, regardless.

There’s also a discussion in the comments that accidentally highlights an obvious tension, which is that you can’t have unbounded expansion of the number of minds while also giving any minds thus created substantial egalitarian redistributive property rights, even if all the minds involved remain human.

As in, in Glorious Superintelligent Future, you can either give every mind abundance or let every mind create unlimited other minds, but you physically can’t do both for that long unless the population of minds happens to stabilize or shrink naturally and even for physical humans alone (discounting all AIs and uploads) once you cured aging and fertility issues it presumably wouldn’t. A lot of our instincts are like this, our sacred values contradict each other at the limit and we can’t talk about it.

Rob Wilbin is right that it is common for \[expert in X] to tell \[expert in Y] they really should have known more about \[Y], but that there are far more such plausible \[Y]s than any person can know at once.

[There are those making the case, like Seb Krier here](https://x.com/sebkrier/status/2008942539483529685), that ‘muddling through’ via the ‘branch’ method of marginal changes is the only way humanity has ever realistically handled its problems, when you try to do something fully systematic it never works. As in, you only have two options, and the second one never works:

1. Where one focuses only on incremental changes to existing policies.
2. Where one attempts to clarify all objectives and analyze every possible alternative from the ground up.

I think that’s a false dichotomy and strawman. You can make bold non\-incremental changes without clarifying all objectives or analyzing every possible alternative. Many such cases, even, including many revolutions, including the American one. You do not need to first agree on all abstract values or solve the Socialist Calculation Debate.

[Patrick McKenzie, Dwarkesh Patel, Jack Clark and Michael Burry talk about AI](https://post.substack.com/p/the-ai-revolution-is-here-will-the).

[Here’s a great pull quote from Jack Clark](https://x.com/S_OhEigeartaigh/status/2010063559539994648):

> Jack Clark: ​I’d basically say to \[a politician I had 5 minutes with], “Self\-improving AI sounds like science fiction, but there’s nothing in the technology that says it’s impossible, and if it happened it’d be a huge deal and you should pay attention to it. You should demand transparency from AI companies about exactly what they’re seeing here, and make sure you have third parties you trust who can test out AI systems for these properties.
> 
> [Seán Ó hÉigeartaigh](https://x.com/S_OhEigeartaigh/status/2010689949507494356): The key question for policymakers is: how do you respond to the information you get from this transparency? 
> 
> At the point at which your evaluators tell you there are worrying signs relating to RSI, you may \*not have much time at all\* to act. There will be a lot of expert disagreement, and you will hear from other experts that this is more 'industry hype' or whatever. Despite this, you will need to have plans in place and be ready and willing to act on them quickly. These plans will likely involve restrictive actions on a relatively very powerful, well\-funded entities \- not just the company throwing up flags, but others close to them in capability.
> 
> Anthropic folk can't really talk about this stuff, because they've been branded with the 'regulatory capture' nonsense \- and frustratingly, them saying it might end up damaging the ability of this community to talk about it. But it's the logical extension, and those of us who can talk about it (and bear the heat) really need to be.

I’d use stronger language than ‘nothing says it is impossible,’ but yes, good calls all around here, especially the need to discuss in advance what we would do if we did discover imminent ‘for real’ recursive self\-improvement.

You can see from the discussion how Michael Burry figured out the housing bubble, and also see that those skeptical instincts are leading him astray here. He makes the classic mistake of, when challenged with ‘but AI will transform things,’ responding with a form of ‘yes but not as fast as the fastest predictions’ as if that means it will therefore be slow and not worth considering. Many such cases.

Another thing that struck me is Burry returning to two neighboring department stores putting in escalators, where he says this only lost both money because value accrued only to the customer. Or claims like this and yes Burry is basically (as Dwarkesh noticed) committing a form of the Lump of Labor fallacy repeatedly:

> Michael Burry: Right now, we will see one of two things: either Nvidia’s chips last five to six years and people therefore need less of them, or they last two to three years and the hyperscalers’ earnings will collapse and private credit will get destroyed.​

The idea of ‘the chips last six years because no one can get enough compute and also the hyperscalers will be fine have you seen their books’ does not seem to occur to him. He’s also being a huge Nvidia skeptic, on the order of the housing bubble.

I was disappointed that Burry’s skepticism translated to being skeptical of important risks because they took a new form, rather than allowing him to notice the problem:

> Michael Burry: The catastrophic worries involving AGI or artificial superintelligence (ASI) are not too worrying to me. I grew up in the Cold War, and the world could blow up at any minute. We had school drills for that. I played soccer with helicopters dropping Malathion over all of us. And I saw Terminator over 30 years ago. Red Dawn seemed possible. I figure humans will adapt.

This is, quite frankly, a dumb take all around. The fact that the nuclear war did not come does not mean it wasn’t a real threat or that the drills would have helped or people would have adapted if it had happened, or ‘if smarter than human artificial minds show up it will be fine because humans can adapt.’ Nor is ‘they depicted this in a movie’ an argument against something happening \- you can argue that fictional evidence mostly doesn’t count but you definitely don’t get to flip its sign.

This is a full refusal to even engage with the question at all, beyond ‘no, that would be too weird’ combined with the anthropic principle.

Burry is at least on the ball enough to be using Claude and also advocating for building up our power and transmission capacity. It is unsurprising to me that Burry is in full ‘do not trust the LLM’ mode, he will have it produce charts and tables and find sources, but he always manually verifies everything. Whereas Dwarkesh is using LLMs as 1\-on\-1 tutors.

Here’s Dwarkesh having a remarkably narrow range of expectations (and also once again citing continual learning, last point is edited to what I’ve confirmed was his intent):

> Dwarkesh Patel: ​Biggest surprises to me would be:
> 
> * 2026 cumulative AI lab revenues are below $40 billion or above $100 billion. It would imply that things have significantly sped up or slowed down compared to what I would have expected.
> * Continual learning is solved. Not in the way that GPT\-3 “solved” in\-context learning, but in the way that GPT\-5\.2 is actually almost human\-like in its ability to understand from context. If working with a model is like replicating a skilled employee that’s been working with you for six months rather than getting their labor on the first hour of their job, I think that constitutes a huge unlock in AI capabilities.
> * I think the timelines to AGI have significantly narrowed since 2020\. At that point, you could assign some probability to scaling GPT\-3 up by a thousand times and reaching AGI, and some probability that we were completely on the wrong track and would have to wait until the end of the century. If progress breaks from the trend line and points to true human\-substitutable intelligences not emerging in a timeline of 5\-20 years, that would be the biggest surprise to me.

[Once again we have a call for ‘the humanities](https://www.timeshighereducation.com/opinion/humanities-cuts-leave-us-defenceless-age-ai)’ as vital to understanding AI and our interactions with it, despite their having so far contributed (doesn’t check notes) nothing, with notably rare exceptions like Amanda Askell. The people who do ‘humanities’ shaped things in useful fashion almost always do it on their own and usually call it something else. As one would expect, the article here from Piotrowska cites insights that are way behind what my blog readers already know.

#### Aligning a Smarter Than Human Intelligence is Difficult

[DeepMind and UK AISI collaborate](https://x.com/davlindner/status/2010753987285524901) [on a paper](https://t.co/4dGAahtoCN) about the practical challenges of monitoring future frontier AI deployments. A quick look suggests this uses the ‘scheming’ conceptual framework, and then says reasonable things about that framework’s implications.

#### People Are Worried About AI Killing Everyone

AI models themselves are often worried, [here are GPT\-5\.2 and Grok says labs should not be pursuing superintelligence](https://x.com/davidmanheim/status/2010331890595909928) under current conditions.

[Yes, Representative Sherman](https://x.com/HumanHarlan/status/2011542091546124391) is referring to [the book](https://ifanyonebuildsit.com/) here, in a hearing:

[![](https://substackcdn.com/image/fetch/$s_!EkgU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F824bacf9-9f9f-4342-8781-2ab1371cf3a6_1043x1244.png)](https://substackcdn.com/image/fetch/$s_!EkgU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F824bacf9-9f9f-4342-8781-2ab1371cf3a6_1043x1244.png)

[The full context](https://x.com/BradSherman/status/2011480697383346395):

> Congressman Brad Sherman: ​The Trump Administration’s reckless decision to sell advanced AI chips to China — after Nvidia CEO Jensen Huang donated to Trump’s White House ballroom and attended a $1\-million\-a\-head dinner — puts one company’s bottom line over U.S. national security and AI leadership.  
>   
> We need to monitor AI to detect and prevent self\-awareness and ambition. China is not the only threat. See the recent bestseller: "[If Anyone Builds It, Everyone Dies](https://amzn.to/4iwvCtW): Why Superhuman AI Would Kill Us All."