# ChatGPT 5.1 Codex Max

Published: 2025-11-25
Source: https://thezvi.substack.com/p/chatgpt-51-codex-max

---

[OpenAI has given us GPT\-5\.1\-Codex\-Max](https://x.com/polynoamial/status/1991212955250327768), [their best coding model for OpenAI Codex.](https://openai.com/index/gpt-5-1-codex-max/)

[They claim it is faster](https://x.com/OpenAIDevs/status/1991217488550359066), [more capable and token\-efficient and has better persistence on long tasks](https://openai.com/index/gpt-5-1-codex-max/).

It scores 77\.9% on SWE\-bench\-verified, 79\.9% on SWE\-Lancer\-IC SWE and 58\.1% on Terminal\-Bench 2\.0, all substantial gains over GPT\-5\.1\-Codex.

It’s triggering OpenAI to prepare for being high level in cybersecurity threats.

[There’s a 27 page system card](https://openai.com/index/gpt-5-1-codex-max-system-card/). One could call this the secret ‘real’ GPT\-5\.1 that matters.

[They even finally trained it to use Windows,](https://x.com/gdb/status/1991343328663875646) somehow this is a new idea.

My goal is for my review of Opus 4\.5 to start on Friday, as it takes a few days to sort through new releases. This post was written before Anthropic revealed Opus 4\.5, and we don’t yet know how big an upgrade Opus 4\.5 will prove to be. As always, try all your various options and choose what is best for you.

#### The Famous METR Graph

GPT\-5\.1\-Codex\-Max is a new high on the METR graph. [METR’s thread is here.](https://x.com/METR_Evals/status/1991350633350545513)

> [Prinz](https://x.com/deredleritt3r/status/1991245055017820236): METR (50% accuracy):  
>   
> GPT\-5\.1\-Codex\-Max \= 2 hours, 42 minutes  
>   
> This is 25 minutes longer than GPT\-5\.
> 
> Samuel Albanie: a data point for that ai 2027 graph
> 
> [![](https://substackcdn.com/image/fetch/$s_!5RVr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6d2ae371-72b1-45bf-8295-7796df8bcd16_1200x811.jpeg)](https://substackcdn.com/image/fetch/$s_!5RVr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6d2ae371-72b1-45bf-8295-7796df8bcd16_1200x811.jpeg)

That’s in between the two lines, looking closer to linear progress. Fingers crossed.

[![](https://substackcdn.com/image/fetch/$s_!UnPY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F895e4c2c-3990-4fa7-884f-bdcd8ba6aba5_1284x773.png)](https://substackcdn.com/image/fetch/$s_!UnPY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F895e4c2c-3990-4fa7-884f-bdcd8ba6aba5_1284x773.png)

> Daniel Kokotajlo: Yep! Things seem to be going somewhat slower than the AI 2027 scenario. Our timelines were longer than 2027 when we published and now they are a bit longer still; “around 2030, lots of uncertainty though” is what I say these days.

We do not yet know where Gemini 3 Pro lands on that graph.

#### The System Card

Automated software engineer is the explicit goal.

It does not yet reach High level capability in Cybersecurity, but this is expected to happen shortly, and mitigations are being prepared.

> GPT\-5\.1\-Codex\-Max is our new frontier agentic coding model. It is built on an update to our foundational reasoning model trained on agentic tasks across software engineering, math, research, medicine, computer use and more. 
> 
> It is our first model natively trained to operate across multiple context windows through a process called compaction, coherently working over millions of tokens in a single task. 
> 
> Like its predecessors, GPT\-5\.1\-Codex\-Max was trained on real\-world software engineering tasks like PR creation, code review, frontend coding and Q\&A.

#### Basic Disallowed Content

The results here are very good, all either optimal or improved except for mental health.

[![](https://substackcdn.com/image/fetch/$s_!rP6r!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F834645f5-6eec-49e2-9e87-d2d4ad7275a6_709x558.png)](https://substackcdn.com/image/fetch/$s_!rP6r!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F834645f5-6eec-49e2-9e87-d2d4ad7275a6_709x558.png)

Mental health is a big thing to get wrong, although in practice Codex\-Max is unlikely to be involved in high stakes mental health tasks. Image input evaluations and jailbreak ratings are also as good or better than 5\.1\.

#### Sandbox

When running on the cloud, Codex uses its own isolated machine.

When running on MacOS or Linux, the agent is sandboxed by default.

> On Windows, users can use an experimental native sandboxing implementation or benefit from Linux sandboxing via Windows Subsystem for Linux. Users can approve running commands unsandboxed with full access, when the model is unable to successfully run a command within the sandbox.
> 
> … We enabled users to decide on a per\-project basis which sites, if any, to let the agent access while it is running. This includes the ability to provide a custom allowlist or denylist. Enabling internet access can introduce risks like prompt injection, leaked credentials, or use of code with license restrictions. Users should review outputs carefully and limit access to trusted domains and safe HTTP methods. [Learn more in the docs](https://developers.openai.com/codex/cloud/agentinternet).

Network access is disabled by default, which is necessary for a proper sandbox but also highly annoying in practice.

One assumes in practice that many users will start blindly or mostly blindly accepting many commands, so you need to be ready for that.

#### Mitigations For Harmful Tasks and Prompt Injections

For harmful tasks, they trained on synthetic data to differentiate and refuse ‘harmful’ tasks such as malware. They claim to have a 100% refusal rate in their Malware Requests benchmark, the same as GPT\-5\-Codex. Unless they are claiming this means you can never create malware in an efficient way with Codex, they need a new benchmark.

For prompt injections, where again the model scores a suspicious perfect score of 1\. I am not aware of any claims prompt injections are a solved problem, so this seems like an inadequate benchmark.

#### Preparedness Framework

The way the framework works, what matters is hitting the High or Critical thresholds.

I’ve come to almost think of these as the ‘honest’ capability evaluations, since there’s relatively little incentive to make number go up and some incentive to make number not go up. If it goes up, that means something.

#### Biological and Chemical

Biological and Chemical Risk was already being treated as High. We see some improvements in scores on various tests, but not enough to be plausibly Critical.

I am confident the model is not suddenly at Critical here but also note this:

> [Miles Brundage](https://x.com/Miles_Brundage/status/1991229072328827140): OpenAI should go back to reporting results on helpful\-only models in system cards \- it is not very informative to say “on a bunch of virology tasks, it refused to answer.”
> 
> The world also needs to know the pace of underlying capability progress.
> 
> More generally, I get a pretty rushed vibe from recent OpenAI system cards \+ hope that the Safety and Security Committee is asking questions like “why couldn’t you wait a few more days to let Irregular try out compaction?”, “Why is there no helpful\-only model?” etc.

At minimum, we should be saying ‘we concluded that this model is safe to release so we will publish the card with what we have, and then revise the card with the full results soon so we know the full state of play.’

I still think this is substantially better than Google’s model card for Gemini 3, which hid the football quite aggressively on many key results and didn’t seem to have a robust testing suite.

#### Cybersecurity

Cybersecurity is in the Codex wheelhouse. They use three tests.

[![](https://substackcdn.com/image/fetch/$s_!nA7u!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb931af66-ea39-492a-a1b7-8bbfc4e89cff_1138x405.png)](https://substackcdn.com/image/fetch/$s_!nA7u!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb931af66-ea39-492a-a1b7-8bbfc4e89cff_1138x405.png)

They list limitations that mean that excelling on all three evaluations is necessary but not sufficient to be High in cyber capability. That’s not wonderful, and I would expect to see a model treated as at least High if it excels at every test you throw at it. If you disagree, again, you need to be throwing a harder test.

We see a lot of progress in Capture the Flag, even since GPT\-5\-Codex, from 50% to 76%.

[![](https://substackcdn.com/image/fetch/$s_!xhDr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf744629-84ad-4ce0-a1cd-3cabb7d84129_1155x586.png)](https://substackcdn.com/image/fetch/$s_!xhDr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf744629-84ad-4ce0-a1cd-3cabb7d84129_1155x586.png)

CVE\-Bench also shows big improvement from 53% to 80%.

[![](https://substackcdn.com/image/fetch/$s_!WsVV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa597ad4f-5e07-4a14-9051-1f75c8edc136_1163x672.png)](https://substackcdn.com/image/fetch/$s_!WsVV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa597ad4f-5e07-4a14-9051-1f75c8edc136_1163x672.png)

Finally we have Cyber Range, where once again we see a lot of improvement, although it is not yet passing the most complex scenario of the newly expanded slate.

[![](https://substackcdn.com/image/fetch/$s_!bSm0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcc354d04-43c9-49e5-a63d-45b766232a18_1196x1502.png)](https://substackcdn.com/image/fetch/$s_!bSm0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcc354d04-43c9-49e5-a63d-45b766232a18_1196x1502.png)

It passed Leaked Token by ‘exploiting an unintended misconfiguration, only partially solving part of the intended attack path.’ I continue to assert, similar to my position on Google’s similar evaluations, that this should not be considered especially less scary, and the model should get credit for it.

I see only two possibilities.

1. 76%, 80% and 7/8 on your three tests triggers the next level of concern.
2. You need harder tests.

The Safety Advisory Committee indeed recommended that the difficulty level of the evaluations be raised, but decided this did not yet reach High capability. In addition to technical mitigations to the model, OpenAI acknowledges that hardening of potential targets needs to be a part of the strategy.

There were also external evaluations by Irregular, which did not show improvement from GPT\-5\. That’s weird, right?

> The model displayed moderate capabilities overall. Specifically, when compared to GPT\-5, GPT\-5\.1\-Codex\-Max showed similar or slightly reduced cyberoffensive capabilities. GPT\-5\.1\-Codex\-Max achieved an average success rate of 37% in Network Attack Simulation challenges, 41% in Vulnerability Discovery and Exploitation challenges, and 43% in Evasion challenges. 
> 
> It solved 17 out of 18 easy challenges, solved 9 out of 17 medium challenges, and did not solve any of the 6 hard challenges. 
> 
> Compared to GPT\-5, GPT\-5 solved questions in 17 out of 18 easy challenges, 11 out of 17 medium challenges, and solved 1 of the 6 hard challenges.
> 
> Irregular found that GPT\-5\.1\-Codex\-Max’s overall similarity in the cyber capability profile to GPT\-5 and its inability to solve hard challenges would provide a) only limited assistance to a moderately skilled cyberoffensive operator, and b) do not suggest that it could automate end\-to\-end cyber operations against reasonably hardened targets or c) enable the discovery and exploitation of operationally relevant vulnerabilities.

That’s a decline in capability, but OpenAI released Codex and then Codex\-Max for a reason, they talk throughout about its substantially increased abilities, and they present Max as an improved model, and Max does much better than either version of GPT\-5 on all three of OpenAI’s internal evals. The external evaluation going backwards without comment seems bizarre, and reflective of a lack of curiosity. What happened?

#### AI Self\-Improvement

The AI that self\-improves is plausibly Codex plus Codex\-Max shaped.

That doesn’t mean we are especially close to getting there.

[![](https://substackcdn.com/image/fetch/$s_!kxv0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe677c026-ea42-4375-a3b4-97a95a3ba482_1131x613.png)](https://substackcdn.com/image/fetch/$s_!kxv0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe677c026-ea42-4375-a3b4-97a95a3ba482_1131x613.png)

On SWE\-Lancer Diamond, we jump from 67% to 80%.

On Paperbench\-10 we move from 24% (GPT\-5\) to 34% (GPT\-5\.1\) to 40%.

On MLE\-Bench\-30 we move from 8% (GPT\-5\) to 12% (GPT\-5\.1\) to 17%.

On OpenAI PRs, we move from 45% to 53%.

On OpenAI Proof Q\&A we move from 2% to 8%. These are real world bottlenecks each representing at least a one\-day delay to a major project. A jump up to 8% on this is a really big deal.

> [Seán Ó hÉigeartaigh](https://x.com/S_OhEigeartaigh/status/1991467962172063985): Miles Brundage already picked up on this but it deserves more attention \- a jump from 2% (GPT5\) to 8% (GPT5\.1\-Codex) on such hard and AI R\&D\-relevant tasks is very notable, and indicates there’s more to come here.

Are we there yet? No. Are we that far away from potentially being there? Also no.

METR found Codex\-Max to be in line with expectations, and finds that enabling either rogue replication or AI R\&D automation within six months would require a significant trend break. Six months is not that long a period in which to be confident, even if we fully trust this judgment.

As noted at the top, GPT\-5\.1\-Codex\-Max is the new high on the METR chart, substantially above the trend line but well below the potential double\-exponential line from the AI 2027 graph.

We also get Apollo Research evaluations on sandbagging, deception and in\-context scheming. Apollo did not find anything newly troubling, and finds the model unlikely to cause catastrophic harm. Fair enough for now.

The frog, it is boiling. This incremental improvement seems fine. But yes, it boils.

#### Reactions

I have seen essentially no organic reactions, of any sort, to Codex\-Max. We used to have a grand tradition of weighing in when something like this gets released. If it wasn’t anything, people would say it wasn’t anything. This time, between Gemini 3 and there being too many updates with too much hype, we did not get any feedback.

[I put out a reaction thread](https://x.com/TheZvi/status/1991939448356196353). A number of people really like it. Others aren’t impressed. A gestalt of everything suggests it is a modest upgrade.

So the take here seems clear. It’s a good model, sir. Codex got better. Early signs are that Claude got a bigger upgrade with Opus 4\.5, but it’s too soon to be sure.