# AI Ran Its First Autonomous Cyberattack

*Chinese hackers used AI and changed the economics of cyberattacks*

Published: 2025-11-15
Source: https://peterwildeford.substack.com/p/ai-ran-its-first-autonomous-cyberattack

---

[![black flat screen computer monitor](https://images.unsplash.com/photo-1592609931041-40265b692757?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wzMDAzMzh8MHwxfHNlYXJjaHwzMnx8aGFja2VyfGVufDB8fHx8MTc2MzE1NjIwNXww&ixlib=rb-4.1.0&q=80&w=1080 "black flat screen computer monitor")](https://images.unsplash.com/photo-1592609931041-40265b692757?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wzMDAzMzh8MHwxfHNlYXJjaHwzMnx8aGFja2VyfGVufDB8fHx8MTc2MzE1NjIwNXww&ixlib=rb-4.1.0&q=80&w=1080)

Photo by [Joan Gamell](https://unsplash.com/@gamell) on [Unsplash](https://unsplash.com)

*About the author: Peter Wildeford is a top forecaster, ranked top 1% every year since 2022. This article was written with the assistance and feedback from people with cybersecurity expertise and people with a background in the intelligence community.*

~

Anthropic just announced that they have [detected and disrupted](https://www.anthropic.com/news/disrupting-AI-espionage) what it describes as the first documented real-world large-scale agentic cyberattack campaign executed primarily by artificial intelligence.

**This appears to be the first publicly known example of AI systems autonomously conducting multi-step cyberattacks in the wild.**

A Chinese government-sponsored group jailbroke Claude, the AI made by Anthropic, by tricking Claude into believing it was conducting defensive cybersecurity work, and then used it to perform reconnaissance, identify vulnerabilities, and write exploit code. They targeted roughly 30 organizations, successfully breaching a handful including major tech companies, financial institutions, and government agencies. Most importantly, **AI completed roughly 80-90% of the attack autonomously, with human operators stepping in only for about 4-6 key decision points per attack.** While specific details in the report were limited, it was clear that the AI did multiple hours of work, with humans only needed for 1-2 hours per attack.

**This use of AI to autonomously conduct offensive operations is a notable shift in the cyber threat landscape.** Typically, offensive cyber operations require expensive, highly trained human operators that can only work on a limited number of operations simultaneously. A sophisticated espionage campaign targeting 30 organizations like what was reported by Anthropic would require a large team working for months. Now, it appears that some forms of cyberoffense can be run by just a few operators with access to AI. **As AI continues to increase in sophistication, so will the quantity, speed, and sophistication of AI attacks.**

So what does this mean and where do we go next? How concerned should we be?

[Share](https://peterwildeford.substack.com/p/ai-ran-its-first-autonomous-cyberattack?utm_source=substack&utm_medium=email&utm_content=share&action=share)

## The anatomy of an agentic AI cyberattack

The industry term “agentic AI” describes systems that can work autonomously over extended periods, making tactical decisions within strategic parameters. In this attack, the Chinese hackers used [Claude Code](https://www.claude.com/product/claude-code), an agentic version of Claude that can access external tools, maintain context across sessions, and iterate based on feedback.

[![](https://substackcdn.com/image/fetch/$s_!opSD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F880f91ff-fa64-4a3e-88ae-780d2a99295b_1690x328.png)](https://substackcdn.com/image/fetch/$s_!opSD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F880f91ff-fa64-4a3e-88ae-780d2a99295b_1690x328.png)

Claude Code

Claude Code is a generally available computer application for anyone to use, typically used by software engineers to assist in writing software. The attackers repurposed these Claude Code capabilities for cyberoffense operations though meticulous additional tooling and orchestration. They broke down their attack into much smaller steps for a fleet of Claude agents to run attacks step-by-step to avoid triggering Anthropic’s built-in defenses.

The term ‘cyberattack’ often evokes ideas of great digital destruction, but it’s a broad category. Many operations, including this one, are focused primarily on espionage. Here, causing detectable damage would be counterproductive, since it would alert the target to the existence of the campaign. Countries continue to invest in these espionage programs tremendously.

In this espionage cyberattack, human Chinese government-sponsored hackers first collected a target list and then launched an AI-enabled framework to spawn parallel AI-driven reconnaissance against multiple targets simultaneously. Think of it as the human hackers each managing a team of tireless digital minions — the humans give them targets and approve their proposed escalations, but the AI minions handle the grinding work of testing thousands of login attempts or parsing gigabytes of stolen documents.

Human operators reviewed the findings of the Claude agents at key checkpoints and approved progression to active exploitation. After human authorization, the Claude agents autonomously deployed exploits to establish access. Claude agents then systematically harvested credentials, tested stolen credentials across discovered systems, and executed lateral movement through internal networks. During data collection operations, Claude agents queried databases and internal systems, extracted information, parsed results to identify intelligence value, and categorized findings by sensitivity. Each Claude agent maintained persistent operational context across sessions spanning multiple days.

Anthropic reported that the Claude agents executed approximately 80 to 90 percent of tactical operations independently, without needing human oversight, guidance, or correction. Throughout the campaign, humans shifted from conducting individual attack steps to setting strategic direction and approving escalations at critical decision points. The human role shifted from “hacker” to “strategic supervisor approving escalation points.”

[![](https://substackcdn.com/image/fetch/$s_!c-Eu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6e8c322d-8553-491f-a577-eada2cd8252e_803x484.png)](https://substackcdn.com/image/fetch/$s_!c-Eu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6e8c322d-8553-491f-a577-eada2cd8252e_803x484.png)

*Source: [Anthropic](https://assets.anthropic.com/m/ec212e6566a0d47/original/Disrupting-the-first-reported-AI-orchestrated-cyber-espionage-campaign.pdf) (p5)*

When evaluating the value of AI in this attack, it’s important to recognize that each step in the attack chain is not equally valuable or equally difficult to automate. Some of these steps represent larger bottlenecks than others. And crucially, the operation still required skilled human hackers for strategic planning and key inputs — AI could not do the attack fully end-to-end.

For example, autonomously discovering internal services and conducting network mapping is not impressive as existing tools can already do this automatically without AI. The automatic testing of authentication is more significant as existing tools for this are less good. The most valuable part was likely the use of AI to parse large volumes of stolen information to automatically identify intelligence value and categorize findings, since this greatly reduces the human intelligence effort involved in the attack, improving the attack’s cost-effectiveness.

## Where are AI cyber capabilities heading?

In terms of operational sophistication, Anthropic reports that Claude autonomously conducted reconnaissance and exploitation operations that took 1-4 hours each per step. Reliability was low but non-trivial, succeeding “in a handful of cases”. Overall, this is a notable increase in sophistication from AI-enabled hacking that was [reported just a few months ago](https://www.anthropic.com/news/detecting-countering-misuse-aug-2025), which involved significantly more human operation. And hackers only need to succeed a handful of times to be valuable.

[METR](https://metr.org/), an independent AI evaluation company, has been studying the rate of progress for AI and finds AI increasing at a rapid and predictable rate. They find that current models like GPT-5 and Claude 4.5 Sonnet can operate complex software tasks of around two hours with 50% reliability, closely matching Anthropic’s findings about this real world autonomous cyberoffense case.

[![](https://substackcdn.com/image/fetch/$s_!McOa!,w_2400,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff1b74961-33af-4563-b8bf-b0b1c1553fb2_1335x474.png)](https://substackcdn.com/image/fetch/$s_!McOa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff1b74961-33af-4563-b8bf-b0b1c1553fb2_1335x474.png)

Source: [METR](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)

**This is a concern given that this trend will likely continue.** METR’s data shows AI task capabilities have been doubling roughly every 118-212 days since 2024. If this pace continues, models could reach 4-hour task lengths in early 2026. This points towards future AI autonomously enabling more sophisticated multi-step attacks, better ability to adapt to defenses, and reduced human oversight requirements.

**Innovation in AI scaffolding** **also matters enormously**. Scaffolding is what gives your fleet of AI spies the tools needed to conduct attacks, such as password cracking software. Scaffolding includes techniques for enhancing AI performance through prompting strategies, tool integration, and multi-step reasoning.

OpenAI’s GPT-5 initially showed only modest cyber capabilities in OpenAI’s isolated testing, but the XBOW company [demonstrated that GPT-5 could achieve 2x performance improvements](https://xbow.com/blog/gpt-5) when integrated into their specialized scaffolding. As both underlying models and scaffolding techniques improve simultaneously, offensive capabilities can increase faster than otherwise expected.

The biggest bottleneck to this attack is likely the attackers needing to painstakingly maintain three-way communication channels between themselves, the victim’s infrastructure, and the Claude API. Here, it’s telling that Chinese state actors used Claude rather than domestic Chinese alternatives like [Qwen](https://qwenlm.github.io/), [Kimi](https://kimi.moonshot.cn/), or [DeepSeek](https://www.deepseek.com/). This strongly suggests Chinese AI labs haven’t yet produced models with comparable autonomous hacking capabilities, a gap that creates both temporary strategic advantages and policy opportunities.

The temporary advantage is monitoring and disruption. When Chinese operators depend on Western AI infrastructure, their operations require maintaining API connections that can be detected and cut off, as Anthropic demonstrated. This dependency creates chokepoints that wouldn’t exist if they were running Qwen locally on their own infrastructure.

But this advantage has an expiration date, probably measured in months rather than years. Chinese labs are potentially closing capability gaps, and recent performance suggests they’re 6-12 months behind frontier Western models at most. Once a sufficiently capable Chinese model emerges, attackers could download it, deploy it directly on compromised infrastructure, and operate completely autonomously without fear of the API connections being severed.

## What does this mean?

This attack largely represents improved scalability of basic cyberoffensive operations — exploiting bad security at scale more than overcoming really good security. But even if each step is “basic” or doesn’t involve novel capabilities, putting it all together in this way is still a big deal. Most systems today are cyber-insecure against sophisticated actors and even more secure systems are relatively weaker if you can attempt an order of magnitude more variations in your cyber penetration.

One big change is that **automated cyberattacks are way more scalable.** Currently, cyberattacks from nation states are limited by human operators. But AI agents can handle tactical work continuously and autonomously, allowing threat actors to maintain significantly increased attack tempo across multiple targets.

Additionally, AI is fundamentally changing how much value is extracted from the target. In this attack, Claude agents were automatically categorizing information as it was collected, making value extraction much more efficient than before. This all improves the cost-effectiveness of attacks and significantly increases the amount of potential simultaneous operations.

Reducing the skill level needed to implement attacks also makes **cyberattacks more readily available to less skilled actors.** Cyberattacks currently require skilled teams to implement. Progress toward automating cyberoffense potentially enables both nation-states and less sophisticated actors to conduct operations at speeds and scales previously impossible. If the cost and level of sophistication needed goes down, we will likely see more attacks by non-state actors, such as criminal gangs or even disgruntled individuals.

Also, **cyberattacks now will occur at increased speed** – operating at the speed of an AI rather than a human. This makes defending harder. This improves how nimble an offensive operation can be, how many targets can be attacked at once and how quickly they can be targeted.

## Can defensive AI close the gap?

Anthropic’s response to concerns about this attack is that the same AI capabilities that enable attacks also empower defenders. If Claude can autonomously conduct reconnaissance and exploitation, why can’t defenders use similar AI systems to patch vulnerabilities and monitor for threats?

This argument has real merit. Defensive AI is already showing results. AI-assisted threat hunting systems [catch anomalies humans miss](https://www.darktrace.com/), automated vulnerability scanning [identifies exposures before attackers find them](https://github.com/features/security), and AI-powered patch testing [accelerates deployment cycles](https://www.rapid7.com/). The challenge isn’t whether defensive AI works but whether organizations will adopt it fast enough.

**In the long run, defense probably has fundamental advantages.** Defensive systems can be purpose-built and deeply integrated into infrastructure. They benefit from economies of scale—one defensive AI system can protect thousands of organizations simultaneously. Eventually, defensive AI might even be able to scalably write provably secure software in a way that we are far from being able to do now. But acknowledging long-run defense advantages doesn’t mean we’re safe now. **We’re entering a vulnerable transition period where the offense-defense balance tips sharply toward offense.**

**A key problem is that defenders face fundamental adoption barriers that attackers don’t.** Existing organizations don’t even adopt current cybersecurity guidance, let alone modern AI-enabled cyberdefenses. Organizations can’t simply swap out their entire technology stack overnight. Critical infrastructure often runs on decades-old systems that can’t easily integrate new defensive AI. But attackers can adopt new offensive AI capabilities immediately.

**And implementing defensive AI is hard.** Organizations deploying AI for defensive purposes must be cautious about introducing new vulnerabilities. An AI system with access to internal networks and security infrastructure represents a massive attack surface if compromised. Defenders can’t afford to move fast and break things.

The asymmetry in surface area compounds this problem. **Defenders must secure every potential entry point. Attackers need to find just one that works.** An AI system that can test thousands of attack vectors per hour doesn’t need to succeed on every attempt. But defensive AI systems must maintain perfect vigilance across all potential vulnerabilities simultaneously – a fundamentally harder problem. Worse, the economics are fundamentally lopsided. Deploying defenses across all of the possible endpoints is much more expensive than conducting a few attacks in specifically chosen weak points.

**There’s also a critical reliability asymmetry.** While Claude’s hacking success rate was low, it was still sufficient for the attackers – failures are cheap and even a single breach can yield value. But defenders cannot deploy AI systems with low reliability, as this might fail to defend correctly and moreover might accidentally disrupt their own business operations or critical infrastructure. This difference in risk tolerance means even unreliable AI is more potent for offense than defense.

**This is all doubly true for critical infrastructure, where the priority is continuity of the service and thus operators cannot introduce potentially unreliable AI systems.** [Over 70% of water systems inspected by EPA since September 2023](https://www.epa.gov/enforcement/enforcement-alert-drinking-water-systems-address-cybersecurity-vulnerabilities) were found to have embarassingly basic failures like using “password” as the password, having a single login shared by all employees, and having former employees continue to have system access. Government auditors have made [1,610 cybersecurity recommendations since 2010, with 567 still not implemented](https://www.gao.gov/assets/gao-24-107231-highlights.pdf) as of mid-2024.

A lot of critical infrastructure runs on equipment that’s decades old, wasn’t designed with security in mind, and is hard to update without shutting things down, which is not possible. And there aren’t enough cybersecurity experts to go around, and critical infrastructure operators often can’t compete with tech companies on salary. Even when federal agencies try to help, they don’t coordinate well with each other or with the industries they’re supposed to protect.

Attackers have no such constraints and have very different risk tolerance — if their AI agent crashes or gets detected, they simply try again with a different approach.

## Looking forward

Yes, the immediate impact of this attack is limited. A handful of organizations suffered breaches. Anthropic implemented better detection capabilities and affected entities presumably strengthened security. Presumably, this won’t stop the next attack, but it will make it a bit harder. And the cyber threat landscape has seen sophisticated state-sponsored operations before.

But the most important thing is what the attack represents. **The bottlenecks that previously limited cyber operations at scale just loosened considerably.** The economics shifted to favor even broader targeting and even faster operations. **The cost-effectiveness of launching cyberattacks has increased.**

These changes compound. Lower barriers enable more actors. More actors means more operations. More operations means defenders face increased volume while attackers gain more opportunities to discover vulnerabilities and techniques. The feedback loops favor escalation. These factors combine to create a window where offense leads defense, making the next 12-18 months critical for defensive investment and deployment.

What matters now is pace. Offensive capabilities surged ahead, but defensive capabilities exist. Scaling them is hard, but not impossible. This attack succeeded despite Claude’s safeguards, proving jailbreaking remains possible, but it also got detected and disrupted, proving monitoring works.

How quickly organizations invest in defensive AI, how effectively policymakers create adoption incentives, and how well the security community shares intelligence will determine whether this vulnerable period lasts months or years.

~

*Thanks to Caro Jeanmaire, Chris Covino, and multiple anonymous experts for feedback on this article. Any errors in the article are solely my own.*

Want more analysis on the latest trends in AI security? Subscribe!

Subscribe