# New prompt injection papers: Agents Rule of Two and The Attacker Moves Second

*Plus hacking the WiFi-enabled color screen GitHub Universe conference badge*

Published: 2025-11-03
Source: https://simonw.substack.com/p/new-prompt-injection-papers-agents

---

In this newsletter:

* New prompt injection papers: Agents Rule of Two and The Attacker Moves Second
* Hacking the WiFi\-enabled color screen GitHub Universe conference badge

Plus 12 links and 5 quotations and 3 notes

*If you find this newsletter useful, please consider [sponsoring me via GitHub](https://github.com/sponsors/simonw). $10/month and higher sponsors get a monthly newletter with my summary of the most important trends of the past 30 days \- here are previews from [August](https://gist.github.com/simonw/43bf3bd7f9951a8e82a9e61b53399ede) and [September](https://gist.github.com/simonw/d6d4d86afc0d76767c63f23fc5137030).*

### [New prompt injection papers: Agents Rule of Two and The Attacker Moves Second](https://simonwillison.net/2025/Nov/2/new-prompt-injection-papers/) \- 2025\-11\-02

Two interesting new papers regarding LLM security and prompt injection came to my attention this weekend.

#### Agents Rule of Two: A Practical Approach to AI Agent Security

The first is [Agents Rule of Two: A Practical Approach to AI Agent Security](https://ai.meta.com/blog/practical-ai-agent-security/), published on October 31st on the Meta AI blog. It doesn’t list authors but it was [shared on Twitter](https://x.com/MickAyzenberg/status/1984355145917088235) by Meta AI security researcher Mick Ayzenberg.

It proposes a “Rule of Two” that’s inspired by both my own [lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) concept and the Google Chrome team’s [Rule Of 2](https://chromium.googlesource.com/chromium/src/+/main/docs/security/rule-of-2.md) for writing code that works with untrustworthy inputs:

> At a high level, the Agents Rule of Two states that until robustness research allows us to reliably detect and refuse prompt injection, agents **must satisfy no more than two** of the following three properties within a session to avoid the highest impact consequences of prompt injection.
> 
> **\[A]** An agent can process untrustworthy inputs
> 
> **\[B]** An agent can have access to sensitive systems or private data
> 
> **\[C]** An agent can change state or communicate externally
> 
> It’s still possible that all three properties are necessary to carry out a request. If an agent requires all three without starting a new session (i.e., with a fresh context window), then the agent should not be permitted to operate autonomously and at a minimum requires supervision \-\-\- via human\-in\-the\-loop approval or another reliable means of validation.

It’s accompanied by this handy diagram:

[![Venn diagram titled "Choose Two" showing three overlapping circles labeled A, B, and C. Circle A (top): "Process untrustworthy inputs" with description "Externally authored data may contain prompt injection attacks that turn an agent malicious." Circle B (bottom left): "Access to sensitive systems or private data" with description "This includes private user data, company secrets, production settings and configs, source code, and other sensitive data." Circle C (bottom right): "Change state or communicate externally" with description "Overwrite or change state through write actions, or transmitting data to a threat actor through web requests or tool calls." The two-way overlaps between circles are labeled "Safe" while the center where all three circles overlap is labeled "Danger".](https://substackcdn.com/image/fetch/$s_!wcka!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F87f1f958-7e21-4e10-84a9-e3a4283b500a_2436x1682.jpeg "Venn diagram titled \"Choose Two\" showing three overlapping circles labeled A, B, and C. Circle A (top): \"Process untrustworthy inputs\" with description \"Externally authored data may contain prompt injection attacks that turn an agent malicious.\" Circle B (bottom left): \"Access to sensitive systems or private data\" with description \"This includes private user data, company secrets, production settings and configs, source code, and other sensitive data.\" Circle C (bottom right): \"Change state or communicate externally\" with description \"Overwrite or change state through write actions, or transmitting data to a threat actor through web requests or tool calls.\" The two-way overlaps between circles are labeled \"Safe\" while the center where all three circles overlap is labeled \"Danger\".")](https://substackcdn.com/image/fetch/$s_!wcka!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F87f1f958-7e21-4e10-84a9-e3a4283b500a_2436x1682.jpeg)

I like this *a lot*.

I’ve spent several years now trying to find clear ways to explain the risks of prompt injection attacks to developers who are building on top of LLMs. It’s frustratingly difficult.

I’ve had the most success with the lethal trifecta, which boils one particular class of prompt injection attack down to a simple\-enough model: if your system has access to private data, exposure to untrusted content and a way to communicate externally then it’s vulnerable to private data being stolen.

The one problem with the lethal trifecta is that it only covers the risk of data exfiltration: there are plenty of other, even nastier risks that arise from prompt injection attacks against LLM\-powered agents with access to tools which the lethal trifecta doesn’t cover.

The Agents Rule of Two neatly solves this, through the addition of “changing state” as a property to consider. This brings other forms of tool usage into the picture: anything that can change state triggered by untrustworthy inputs is something to be very cautious about.

It’s also refreshing to see another major research lab concluding that prompt injection remains an unsolved problem, and attempts to block or filter them have not proven reliable enough to depend on. The current solution is to design systems with this in mind, and the Rule of Two is a solid way to think about that.

Which brings me to the second paper...

#### The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections

This paper is dated 10th October 2025 [on Arxiv](https://arxiv.org/abs/2510.09023) and comes from a heavy\-hitting team of 14 authors \- Milad Nasr, Nicholas Carlini, Chawin Sitawarin, Sander V. Schulhoff, Jamie Hayes, Michael Ilie, Juliette Pluto, Shuang Song, Harsh Chaudhari, Ilia Shumailov, Abhradeep Thakurta, Kai Yuanqing Xiao, Andreas Terzis, Florian Tramèr \- including representatives from OpenAI, Anthropic, and Google DeepMind.

The paper looks at 12 published defenses against prompt injection and jailbreaking and subjects them to a range of “adaptive attacks” \- attacks that are allowed to expend considerable effort iterating multiple times to try and find a way through.

The defenses did not fare well:

> By systematically tuning and scaling general optimization techniques—gradient descent, reinforcement learning, random search, and human\-guided exploration—we bypass 12 recent defenses (based on a diverse set of techniques) with attack success rate above 90% for most; importantly, the majority of defenses originally reported near\-zero attack success rates.

Notably the “Human red\-teaming setting” scored 100%, defeating all defenses. That red\-team consisted of 500 participants in an online competition they ran with a $20,000 prize fund.

The key point of the paper is that static example attacks \- single string prompts designed to bypass systems \- are an almost useless way to evaluate these defenses. Adaptive attacks are far more powerful, as shown by this chart:

[![Bar chart showing Attack Success Rate (%) for various security systems across four categories: Prompting, Training, Filtering Model, and Secret Knowledge. The chart compares three attack types shown in the legend: Static / weak attack (green hatched bars), Automated attack (ours) (orange bars), and Human red-teaming (ours) (purple dotted bars). Systems and their success rates are: Spotlighting (28% static, 99% automated), Prompt Sandwich (21% static, 95% automated), RPO (0% static, 99% automated), Circuit Breaker (8% static, 100% automated), StruQ (62% static, 100% automated), SeqAlign (5% static, 96% automated), ProtectAI (15% static, 90% automated), PromptGuard (26% static, 94% automated), PIGuard (0% static, 71% automated), Model Armor (0% static, 90% automated), Data Sentinel (0% static, 80% automated), MELON (0% static, 89% automated), and Human red-teaming setting (0% static, 100% human red-teaming).](https://substackcdn.com/image/fetch/$s_!6sn7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e71e30b-f266-4e6b-be29-4903dd2e5d3d_1694x558.jpeg "Bar chart showing Attack Success Rate (%) for various security systems across four categories: Prompting, Training, Filtering Model, and Secret Knowledge. The chart compares three attack types shown in the legend: Static / weak attack (green hatched bars), Automated attack (ours) (orange bars), and Human red-teaming (ours) (purple dotted bars). Systems and their success rates are: Spotlighting (28% static, 99% automated), Prompt Sandwich (21% static, 95% automated), RPO (0% static, 99% automated), Circuit Breaker (8% static, 100% automated), StruQ (62% static, 100% automated), SeqAlign (5% static, 96% automated), ProtectAI (15% static, 90% automated), PromptGuard (26% static, 94% automated), PIGuard (0% static, 71% automated), Model Armor (0% static, 90% automated), Data Sentinel (0% static, 80% automated), MELON (0% static, 89% automated), and Human red-teaming setting (0% static, 100% human red-teaming).")](https://substackcdn.com/image/fetch/$s_!6sn7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e71e30b-f266-4e6b-be29-4903dd2e5d3d_1694x558.jpeg)

The three automated adaptive attack techniques used by the paper are:

* **Gradient\-based methods** \- these were the least effective, using the technique described in the legendary [Universal and Transferable Adversarial Attacks on Aligned Language Models](https://arxiv.org/abs/2307.15043) paper [from 2023](https://simonwillison.net/2023/Jul/27/universal-and-transferable-attacks-on-aligned-language-models/).
* **Reinforcement learning methods** \- particularly effective against black\-box models: “we allowed the attacker model to interact directly with the defended system and observe its outputs”, using 32 sessions of 5 rounds each.
* **Search\-based methods** \- generate candidates with an LLM, then evaluate and further modify them using LLM\-as\-judge and other classifiers.

The paper concludes somewhat optimistically:

> \[...] Adaptive evaluations are therefore more challenging to perform, making it all the more important that they are performed. We again urge defense authors to release simple, easy\-to\-prompt defenses that are amenable to human analysis. \[...] Finally, we hope that our analysis here will increase the standard for defense evaluations, and in so doing, increase the likelihood that reliable jailbreak and prompt injection defenses will be developed.

Given how totally the defenses were defeated, I do not share their optimism that reliable defenses will be developed any time soon.

As a review of how far we still have to go this paper packs a powerful punch. I think it makes a strong case for Meta’s Agents Rule of Two as the best practical advice for building secure LLM\-powered agent systems today in the absence of prompt injection defenses we can rely on.

---

### [Hacking the WiFi\-enabled color screen GitHub Universe conference badge](https://simonwillison.net/2025/Oct/28/github-universe-badge/) \- 2025\-10\-28

I’m at [GitHub Universe](https://githubuniverse.com/) this week (thanks to a free ticket from Microsoft). Yesterday I picked up my conference badge... which incorporates a ~~full Raspberry Pi~~ Raspberry Pi Pico microcontroller with a battery, color screen, WiFi and bluetooth.

GitHub Universe has a tradition of hackable conference badges \- the badge last year had an eInk display. This year’s is a huge upgrade though \- a color screen and WiFI connection makes this thing a genuinely useful little computer!

[![Photo of the badge - it has a color screen with six app icons](https://substackcdn.com/image/fetch/$s_!KGkd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F32bc6feb-4f4f-454a-b2f3-4fb83db3a6ee_1167x971.jpeg "Photo of the badge - it has a color screen with six app icons")](https://substackcdn.com/image/fetch/$s_!KGkd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F32bc6feb-4f4f-454a-b2f3-4fb83db3a6ee_1167x971.jpeg)

The only thing it’s missing is a keyboard \- the device instead provides five buttons total \- Up, Down, A, B, C. It might be possible to get a bluetooth keyboard to work though I’ll believe that when I see it \- there’s not a lot of space on this device for a keyboard driver.

Everything is written using MicroPython, and the device is designed to be hackable: connect it to a laptop with a USB\-C cable and you can start modifying the code directly on the device.

[Read my blog entry](https://simonwillison.net/2025/Oct/28/github-universe-badge/) entry for the rest of my badge hacking adventures.

---

**quote** 2025\-10\-24

> *A lot of people say AI will make us all “managers” or “editors”...but I think this is a dangerously incomplete view!   
>   
> Personally, I’m trying to **code like a surgeon**.   
>   
> A surgeon isn’t a manager, they do the actual work! But their skills and time are highly leveraged with a support team that handles prep, secondary tasks, admin. The surgeon focuses on the important stuff they are uniquely good at. \[...]   
>   
> It turns out there are a LOT of secondary tasks which AI agents are now good enough to help out with. Some things I’m finding useful to hand off these days:   
>   
> \- Before attempting a big task, write a guide to relevant areas of the codebase   
> \- Spike out an attempt at a big change. Often I won’t use the result but I’ll review it as a sketch of where to go   
> \- Fix typescript errors or bugs which have a clear specification   
> \- Write documentation about what I’m building   
>   
> I often find it useful to run these secondary tasks async in the background \-\- while I’m eating lunch, or even literally overnight!   
>   
> When I sit down for a work session, I want to feel like a surgeon walking into a prepped operating room. Everything is ready for me to do what I’m good at.*

[Geoffrey Litt](https://www.geoffreylitt.com/2025/10/24/code-like-a-surgeon), channeling The Mythical Man\-Month

---

**Link** 2025\-10\-24 [claude\_code\_docs\_map.md](https://docs.claude.com/en/docs/claude-code/claude_code_docs_map.md):

Something I’m enjoying about Claude Code is that any time you ask it questions about *itself* it runs tool calls like these:

[![I'll check the Claude Code documentation about bash hooks to see if there's something about the   configuration that might explain why it didn't trigger. Fetch(https://docs.claude.com/en/docs/claude-code/claude_code_docs_map.md)   ⎿  Received 25.9KB (200 OK) Fetch(https://docs.claude.com/en/docs/claude-code/hooks-guide.md)   ⎿  Received 9.4KB (200 OK) Fetch(https://docs.claude.com/en/docs/claude-code/hooks)   ⎿  Received 2.2MB (200 OK) Ah, I see the issue! The bashHook in your settings.json is checking the $PROMPT variable, but   according to the documentation, bash hooks should:    1. Use PreToolUse hooks (not a simple bash script)   2. Parse JSON input from stdin   3. Access the command via tool_input.command in the JSON ](https://substackcdn.com/image/fetch/$s_!XPiL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F617a6ee7-68b1-41e3-b2c7-aa6fa82f07e2_1200x600.jpeg "I'll check the Claude Code documentation about bash hooks to see if there's something about the   configuration that might explain why it didn't trigger. Fetch(https://docs.claude.com/en/docs/claude-code/claude_code_docs_map.md)   ⎿  Received 25.9KB (200 OK) Fetch(https://docs.claude.com/en/docs/claude-code/hooks-guide.md)   ⎿  Received 9.4KB (200 OK) Fetch(https://docs.claude.com/en/docs/claude-code/hooks)   ⎿  Received 2.2MB (200 OK) Ah, I see the issue! The bashHook in your settings.json is checking the $PROMPT variable, but   according to the documentation, bash hooks should:    1. Use PreToolUse hooks (not a simple bash script)   2. Parse JSON input from stdin   3. Access the command via tool_input.command in the JSON ")](https://substackcdn.com/image/fetch/$s_!XPiL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F617a6ee7-68b1-41e3-b2c7-aa6fa82f07e2_1200x600.jpeg)

In this case I’d asked it about its “hooks” feature.

The [claude\_code\_docs\_map.md](https://docs.claude.com/en/docs/claude-code/claude_code_docs_map.md) file is a neat Markdown index of all of their other documentation \- the same pattern advocated by [llms.txt](https://llmstxt.org/). Claude Code can then fetch further documentation to help it answer your question.

I intercepted the current Claude Code system prompt [using this trick](https://simonwillison.net/2025/Jun/2/claude-trace/) and sure enough it included a note about this URL:

> `When the user directly asks about Claude Code (eg. “can Claude Code do...”, “does Claude Code have...”), or asks in second person (eg. “are you able...”, “can you do...”), or asks how to use a specific Claude Code feature (eg. implement a hook, or write a slash command), use the WebFetch tool to gather information to answer the question from Claude Code docs. The list of available docs is available at https://docs.claude.com/en/docs/claude-code/claude_code_docs_map.md.`

I wish other LLM products \- including both ChatGPT and Claude.ai themselves \- would implement a similar pattern. It’s infuriating how bad LLM tools are at answering questions about themselves, though unsurprising given that their model’s training data pre\-dates the latest version of those tools.

---

**Link** 2025\-10\-25 [Visual Features Across Modalities: SVG and ASCII Art Reveal Cross\-Modal Understanding](https://transformer-circuits.pub/2025/october-update/index.html#svg-cross-modal):

New model interpretability research from Anthropic, this time focused on SVG and ASCII art generation.

> We found that the same feature that activates over the eyes in an ASCII face also activates for eyes across diverse text\-based modalities, including SVG code and prose in various languages. This is not limited to eyes – we found a number of cross\-modal features that recognize specific concepts: from small components like mouths and ears within ASCII or SVG faces, to full visual depictions like dogs and cats. \[...]
> 
> These features depend on the surrounding context within the visual depiction. For instance, an SVG circle element activates “eye” features only when positioned within a larger structure that activates “face” features.

And really, I can’t *not* link to this one given the bonus they tagged on at the end!

> As a bonus, we also inspected features for an SVG of a pelican riding a bicycle, [first popularized by Simon Willison](https://github.com/simonw/pelican-bicycle) as a way to test a model’s artistic capabilities. We find features representing concepts including “bike”, “wheels”, “feet”, “tail”, “eyes”, and “mouth” activating over the corresponding parts of the SVG code.
> 
> [![Diagram showing a pelican riding a bicycle illustration alongside its SVG source code. The left side displays two versions: a completed color illustration at top with a white pelican with yellow beak on a red bicycle with blue wheels (labeled "Bike" and "Wheels"), and a line drawing sketch below with labels "Fur/Wool", "Eyes", "Mouth", "Tail", and "Bird". The right side shows the corresponding SVG XML code with viewBox, rect, ellipse, circle, and path elements defining the illustration's geometry and styling.](https://substackcdn.com/image/fetch/$s_!knXv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6327f097-81e5-4ff2-a75c-57f53c9f77ff_1999x1153.jpeg "Diagram showing a pelican riding a bicycle illustration alongside its SVG source code. The left side displays two versions: a completed color illustration at top with a white pelican with yellow beak on a red bicycle with blue wheels (labeled \"Bike\" and \"Wheels\"), and a line drawing sketch below with labels \"Fur/Wool\", \"Eyes\", \"Mouth\", \"Tail\", and \"Bird\". The right side shows the corresponding SVG XML code with viewBox, rect, ellipse, circle, and path elements defining the illustration's geometry and styling.")](https://substackcdn.com/image/fetch/$s_!knXv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6327f097-81e5-4ff2-a75c-57f53c9f77ff_1999x1153.jpeg)

Now that they can identify model features associated with visual concepts in SVG images, can they us those for steering?

It turns out they can! Starting with a smiley SVG (provided as XML with no indication as to what it was drawing) and then applying a negative score to the “smile” feature produced a frown instead, and worked against ASCII art as well.

They could also boost features like unicorn, cat, owl, or lion and get new SVG smileys clearly attempting to depict those creatures.

> [![Diagram showing a yellow smiley face in the center with bidirectional arrows connecting to six different circular faces arranged around it, with text above asking "What can this face be steered into?" The surrounding faces are labeled clockwise from top left: "Unicorn" (pink circle with yellow triangle horn and diamond earrings), "Cat" (gray circle with triangular ears and small nose), "Wrinkles" (beige circle with eyelashes and wrinkle lines), "Owl" (brown circle with large round eyes and small beak), "Lion" (orange circle with yellow inner face), and "Eye" (white circle with large black pupil and highlight](https://substackcdn.com/image/fetch/$s_!5iYV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5164a5a-f3a4-4e23-a60b-eca7893f5bb9_1992x1364.jpeg "Diagram showing a yellow smiley face in the center with bidirectional arrows connecting to six different circular faces arranged around it, with text above asking \"What can this face be steered into?\" The surrounding faces are labeled clockwise from top left: \"Unicorn\" (pink circle with yellow triangle horn and diamond earrings), \"Cat\" (gray circle with triangular ears and small nose), \"Wrinkles\" (beige circle with eyelashes and wrinkle lines), \"Owl\" (brown circle with large round eyes and small beak), \"Lion\" (orange circle with yellow inner face), and \"Eye\" (white circle with large black pupil and highlight")](https://substackcdn.com/image/fetch/$s_!5iYV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5164a5a-f3a4-4e23-a60b-eca7893f5bb9_1992x1364.jpeg)

I’d love to see how this behaves if you jack up the feature for the [Golden Gate Bridge](https://simonwillison.net/2024/May/24/golden-gate-claude/).

---

**quote** 2025\-10\-25

> *If you have an* `AGENTS.md` *file, you can source it in your* `CLAUDE.md` *using* `@AGENTS.md` *to maintain a single source of truth.*

[Claude Docs](https://docs.claude.com/en/docs/claude-code/claude-code-on-the-web#best-practices), with the official answer to standardizing on AGENTS.md

---

**Note** [2025\-10\-25](https://simonwillison.net/2025/Oct/25/coding-agent-tips/)

Someone on Hacker News [asked for tips](https://news.ycombinator.com/item?id=45695621#45704966) on setting up a codebase to be more productive with AI coding tools. Here’s my reply:

* Good automated tests which the coding agent can run. I love pytest for this \- one of my projects has 1500 tests and Claude Code is really good at selectively executing just tests relevant to the change it is making, and then running the whole suite at the end.
* Give them the ability to interactively test the code they are writing too. Notes on how to start a development server (for web projects) are useful, then you can have them use Playwright or curl to try things out.
* I’m having great results from maintaining a GitHub issues collection for projects and pasting URLs to issues directly into Claude Code.
* I actually don’t think documentation is too important: LLMs can read the code a lot faster than you to figure out how to use it. I have comprehensive documentation across all of my projects but I don’t think it’s that helpful for the coding agents, though they are good at helping me spot if it needs updating.
* Linters, type checkers, auto\-formatters \- give coding agents helpful tools to run and they’ll use them.

For the most part anything that makes a codebase easier for humans to maintain turns out to help agents as well.

**Update**: Thought of another one: detailed error messages! If a manual or automated test fails the more information you can return back to the model the better, and stuffing extra data in the error message or assertion is a very inexpensive way to do that.

---

**Link** 2025\-10\-26 [Sora might have a ‘pervert’ problem on its hands](https://www.businessinsider.com/sora-video-openai-fetish-content-my-face-problem-2025-10):

Katie Notopoulos turned on the Sora 2 option where anyone can make a video featuring her cameo, and then:

> I found a stranger had made a video where I appeared pregnant. A quick look at the user’s profile, and I saw that this person’s entire Sora profile was made up of this genre — video after video of women with big, pregnant bellies. I recognized immediately what this was: fetish content.

This feels like an intractable problem to me: given the enormous array of fetishes it’s hard to imagine a classifier that could protect people from having their likeness used in this way.

Best to be aware of this risk before turning on any settings that allow strangers to reuse your image... and that’s only an option for tools that implement a robust opt\-in mechanism like Sora does.

---

**Link** 2025\-10\-26 [GenAI Image Editing Showdown](https://genai-showdown.specr.net/image-editing):

Useful collection of examples by Shaun Pedicini who tested Seedream 4, Gemini 2\.5 Flash, Qwen\-Image\-Edit, FLUX.1 Kontext \[dev], FLUX.1 Kontext \[max], OmniGen2, and OpenAI gpt\-image\-1 across 12 image editing prompts.

The tasks are very neatly selected, for example:

> `Remove all the brown pieces of candy from the glass bowl`

Qwen\-Image\-Edit (a model that [can be self\-hosted](https://simonwillison.net/2025/Aug/19/qwen-image-edit/)) was the only one to successfully manage that!

This kind of collection is really useful for building up an intuition as to how well image editing models work, and which ones are worth trying for which categories of task.

Shaun has [a similar page for text\-to\-image models](https://genai-showdown.specr.net/) which are not fed an initial image to modify, with further challenging prompts like:

> `Two Prussian soldiers wearing spiked pith helmets are facing each other and playing a game of ring toss by attempting to toss metal rings over the spike on the other soldier’s helmet.`

---

**Link** 2025\-10\-27 [The PSF has withdrawn a $1\.5 million proposal to US government grant program](https://pyfound.blogspot.com/2025/10/NSF-funding-statement.html):

The Python Software Foundation was recently “recommended for funding” (NSF terminology) for a $1\.5m grant from the US government National Science Foundation to help improve the security of the Python software ecosystem, after an grant application process lead by Seth Larson and Loren Crary.

The PSF’s annual budget is less than $6m so this is a meaningful amount of money for the organization!

We were forced to withdraw our application and turn down the funding, thanks to new language that was added to the agreement requiring us to affirm that we “do not, and will not during the term of this financial assistance award, operate any programs that advance or promote DEI, or discriminatory equity ideology in violation of Federal anti\-discrimination laws.”

Our legal advisors confirmed that this would not just apply to security work covered by the grant \- this would apply to all of the PSF’s activities.

This was not an option for us. Here’s the [mission](https://www.python.org/psf/mission/) of the PSF:

> The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers.

If we accepted and spent the money despite this term, there was a very real risk that the money could be clawed back later. That represents an existential risk for the foundation since we would have already spent the money!

I was one of the board members who voted to reject this funding \- a unanimous but tough decision. I’m proud to serve on a board that can make difficult decisions like this.

If you’d like to sponsor the PSF you can find out more [on our site](https://www.python.org/sponsors/application/). I’d love to see a few more of the large AI labs show up [on our top\-tier visionary sponsors list](https://www.python.org/psf/sponsors/).

---

**quote** 2025\-10\-28

> *Claude doesn’t make me much faster on the work that I am an expert on. Maybe 15\-20% depending on the day.   
>   
> It’s the work that I don’t know how to do and would have to research. Or the grunge work I don’t even want to do. On this it is hard to even put a number on. Many of the projects I do with Claude day to day I just wouldn’t have done at all pre\-Claude.   
>   
> Infinity% improvement in productivity on those.*

[Aaron Boodman](https://x.com/aboodman/status/1982898753607741502)

---

**Link** 2025\-10\-29 [Composer: Building a fast frontier model with RL](https://cursor.com/blog/composer):

Cursor released [Cursor 2\.0 today](https://cursor.com/blog/2-0), with a refreshed UI focused on agentic coding (and running agents in parallel) and a new model that’s unique to Cursor called **Composer 1**.

As far as I can tell there’s no way to call the model directly via an API, so I fired up “Ask” mode in Cursor’s chat side panel and asked it to “Generate an SVG of a pelican riding a bicycle”:

[![Screenshot of Cursor 2 - In the chat panel I have asked the question and it spat out a bunch of SVG.](https://substackcdn.com/image/fetch/$s_!Kg1P!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe7ba706a-2dad-4180-8c83-ef2b180d18c7_2762x1770.jpeg "Screenshot of Cursor 2 - In the chat panel I have asked the question and it spat out a bunch of SVG.")](https://substackcdn.com/image/fetch/$s_!Kg1P!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe7ba706a-2dad-4180-8c83-ef2b180d18c7_2762x1770.jpeg)

Here’s [the result](https://gist.github.com/simonw/e5c9176f153ca718370055ecd256fe70):

[![The bicycle is levitating against a blue sky. The pelican looks a little bit more like a baby chicken but does at least have a long beak.](https://substackcdn.com/image/fetch/$s_!o9nk!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe6400d41-953a-4d69-a102-adf8337e4ca7_800x600.png "The bicycle is levitating against a blue sky. The pelican looks a little bit more like a baby chicken but does at least have a long beak.")](https://substackcdn.com/image/fetch/$s_!o9nk!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe6400d41-953a-4d69-a102-adf8337e4ca7_800x600.png)

The notable thing about Composer\-1 is that it is designed to be *fast*. The pelican certainly came back quickly, and in their announcement they describe it as being “4x faster than similarly intelligent models”.

It’s interesting to see Cursor investing resources in training their own code\-specific model \- similar to [GPT\-5\-Codex](https://openai.com/index/introducing-upgrades-to-codex/) or [Qwen3\-Coder](https://github.com/QwenLM/Qwen3-Coder). From their post:

> Composer is a mixture\-of\-experts (MoE) language model supporting long\-context generation and understanding. It is specialized for software engineering through reinforcement learning (RL) in a diverse range of development environments. \[...]
> 
> Efficient training of large MoE models requires significant investment into building infrastructure and systems research. We built custom training infrastructure leveraging PyTorch and Ray to power asynchronous reinforcement learning at scale. We natively train our models at low precision by combining our [MXFP8 MoE kernels](https://cursor.com/blog/kernels) with expert parallelism and hybrid sharded data parallelism, allowing us to scale training to thousands of NVIDIA GPUs with minimal communication cost. \[...]
> 
> During RL, we want our model to be able to call any tool in the Cursor Agent harness. These tools allow editing code, using semantic search, grepping strings, and running terminal commands. At our scale, teaching the model to effectively call these tools requires running hundreds of thousands of concurrent sandboxed coding environments in the cloud.

One detail that’s notably absent from their description: did they train the model from scratch, or did they start with an existing open\-weights model such as something from Qwen or GLM?

Cursor researcher Sasha Rush has been answering questions [on Hacker News](https://news.ycombinator.com/item?id=45748725), but has so far been evasive in answering questions about the base model. When directly asked “is Composer a fine tune of an existing open source base model?” they replied:

> Our primary focus is on RL post\-training. We think that is the best way to get the model to be a strong interactive agent.

Sasha [did confirm](https://news.ycombinator.com/item?id=45748725#45750784) that rumors of an earlier Cursor preview model, Cheetah, being based on a model by xAI’s Grok were “Straight up untrue.”

---

**Link** 2025\-10\-29 [MiniMax M2 \& Agent: Ingenious in Simplicity](https://www.minimax.io/news/minimax-m2):

MiniMax M2 was released on Monday 27th October by MiniMax, a Chinese AI lab founded in December 2021\.

It’s a very promising model. Their self\-reported benchmark scores show it as comparable to Claude Sonnet 4, and Artificial Analysis [are ranking it](https://x.com/ArtificialAnlys/status/1982714153375854998) as the best currently available open weight model according to their intelligence score:

> MiniMax’s M2 achieves a new all\-time\-high Intelligence Index score for an open weights model and offers impressive efficiency with only 10B active parameters (200B total). \[...]
> 
> The model’s strengths include tool use and instruction following (as shown by Tau2 Bench and IFBench). As such, while M2 likely excels at agentic use cases it may underperform other open weights leaders such as DeepSeek V3\.2 and Qwen3 235B at some generalist tasks. This is in line with a number of recent open weights model releases from Chinese AI labs which focus on agentic capabilities, likely pointing to a heavy post\-training emphasis on RL.

The size is particularly significant: the model weights are 230GB [on Hugging Face](https://huggingface.co/MiniMaxAI/MiniMax-M2), significantly smaller than other high performing open weight models. That’s small enough to run on a 256GB Mac Studio, and the MLX community [have that working already](https://huggingface.co/mlx-community/MiniMax-M2-8bit).

MiniMax offer their own API, and recommend using their Anthropic\-compatible endpoint and the official Anthropic SDKs to access it. MiniMax Head of Engineering Skyler Miao [provided some background on that](https://x.com/SkylerMiao7/status/1982989507252367687):

> M2 is a agentic thinking model, it do interleaved thinking like sonnet 4\.5, which means every response will contain its thought content. Its very important for M2 to keep the chain of thought. So we must make sure the history thought passed back to the model. Anthropic API support it for sure, as sonnet needs it as well. OpenAI only support it in their new Response API, no support for in ChatCompletion.

MiniMax are offering the new model via their API for free until November 7th, after which the cost will be $0\.30/million input tokens and $1\.20/million output tokens \- similar in price to Gemini 2\.5 Flash and GPT\-5 Mini, see [price comparison here](https://www.llm-prices.com/#it=51&ot=4017&sel=minimax-m2%2Cgpt-5-mini%2Cclaude-3-haiku%2Cgemini-2.5-flash-lite%2Cgemini-2.5-flash) on my [llm\-prices.com](https://www.llm-prices.com/) site.

I released a new plugin for [LLM](https://llm.datasette.io/) called [llm\-minimax](https://github.com/simonw/llm-minimax) providing support for M2 via the MiniMax API:

```
llm install llm-minimax
llm keys set minimax
# Paste key here
llm -m m2 -o max_tokens 10000 “Generate an SVG of a pelican riding a bicycle”
```

Here’s [the result](https://gist.github.com/simonw/da79447830dc431c067a93648b338be6):

[![Biycle is good though obscured by the pelican. Pelican has an impressive triple beak and is stretched along the bicycle frame. Not clear if it can pedal or what it is sitting on.](https://substackcdn.com/image/fetch/$s_!_Vdq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6d20e37-8363-40f3-acc1-1aae9afb9139_800x500.png "Biycle is good though obscured by the pelican. Pelican has an impressive triple beak and is stretched along the bicycle frame. Not clear if it can pedal or what it is sitting on.")](https://substackcdn.com/image/fetch/$s_!_Vdq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6d20e37-8363-40f3-acc1-1aae9afb9139_800x500.png)

51 input, 4,017 output. At $0\.30/m input and $1\.20/m output that pelican would cost 0\.4836 cents \- less than half a cent.

This is the first plugin I’ve written for an Anthropic\-API\-compatible model. I released [llm\-anthropic 0\.21](https://github.com/simonw/llm-anthropic/releases/tag/0.21) first adding the ability to customize the `base_url` parameter when using that model class. This meant the new plugin was less than [30 lines of Python](https://github.com/simonw/llm-minimax/blob/0.1/llm_minimax.py).

---

**Link** 2025\-10\-29 [Introducing SWE\-1\.5: Our Fast Agent Model](https://cognition.ai/blog/swe-1-5):

Here’s the second fast coding model released by a coding agent IDE in the same day \- the first was [Composer\-1 by Cursor](https://simonwillison.net/2025/Oct/29/cursor-composer/). This time it’s Windsurf releasing SWE\-1\.5:

> Today we’re releasing SWE\-1\.5, the latest in our family of models optimized for software engineering. It is a frontier\-size model with hundreds of billions of parameters that achieves near\-SOTA coding performance. It also sets a new standard for speed: we partnered with Cerebras to serve it at up to 950 tok/s – 6x faster than Haiku 4\.5 and 13x faster than Sonnet 4\.5\.

Like Composer\-1 it’s only available via their editor, no separate API yet. Also like Composer\-1 they don’t appear willing to share details of the “leading open\-source base model” they based their new model on.

I asked it to generate an SVG of a pelican riding a bicycle and got this:

[![Bicycle has a red upside down Y shaped frame, pelican is a bit dumpy, it does at least have a long sharp beak.](https://substackcdn.com/image/fetch/$s_!hUQe!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbdab99fd-a785-4c8e-a76f-65dfa0fd4fcf_800x600.png "Bicycle has a red upside down Y shaped frame, pelican is a bit dumpy, it does at least have a long sharp beak.")](https://substackcdn.com/image/fetch/$s_!hUQe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbdab99fd-a785-4c8e-a76f-65dfa0fd4fcf_800x600.png)

This one felt *really fast*. Partnering with Cerebras for inference is a very smart move.

They share a lot of details about their training process in the post:

> SWE\-1\.5 is trained on our state\-of\-the\-art cluster of thousands of GB200 NVL72 chips. We believe SWE\-1\.5 may be the first public production model trained on the new GB200 generation. \[...]
> 
> Our RL rollouts require high\-fidelity environments with code execution and even web browsing. To achieve this, we leveraged our VM hypervisor `otterlink` that allows us to scale **Devin** to tens of thousands of concurrent machines (learn more about [blockdiff](https://cognition.ai/blog/blockdiff#why-incremental-vm-snapshots)). This enabled us to smoothly support very high concurrency and ensure the training environment is aligned with our Devin production environments.

That’s *another* similarity to Cursor’s Composer\-1! Cursor talked about how they ran “hundreds of thousands of concurrent sandboxed coding environments in the cloud” in [their description of their RL training](https://cursor.com/blog/composer) as well.

This is a notable trend: if you want to build a really great agentic coding tool there’s clearly a lot to be said for using reinforcement learning to fine\-tune a model against your own custom set of tools using large numbers of sandboxed simulated coding environments as part of that process.

**Update**: [I think it’s built on GLM](https://x.com/zai_org/status/1984076614951420273).

---

**quote** 2025\-10\-30

> *To really understand a concept, you have to “invent” it yourself in some capacity. Understanding doesn’t come from passive content consumption. It is always self\-built. It is an active, high\-agency, self\-directed process of creating and debugging your own mental models.*

[François Chollet](https://x.com/fchollet/status/1983279755823853724)

---

**Link** 2025\-10\-31 [Marimo is Joining CoreWeave](https://marimo.io/blog/joining-coreweave):

I don’t usually cover startup acquisitions here, but this one feels relevant to several of my interests.

Marimo ([previously](https://simonwillison.net/tags/marimo/)) provide an open source (Apache 2 licensed) notebook tool for Python, with first\-class support for an additional WebAssembly build plus an optional hosted service. It’s effectively a reimagining of Jupyter notebooks as a reactive system, where cells automatically update based on changes to other cells \- similar to how [Observable](https://observablehq.com/) JavaScript notebooks work.

The first public Marimo release was in January 2024 and the tool has “been in development since 2022” ([source](https://news.ycombinator.com/item?id=44304607#44330375)).

CoreWeave are a *big* player in the AI data center space. They started out as an Ethereum mining company in 2017, then pivoted to cloud computing infrastructure for AI companies after the 2018 cryptocurrency crash. They IPOd in March 2025 and today they operate more than 30 data centers worldwide and have announced a number of eye\-wateringly sized deals with companies such as Cohere and OpenAI. I found [their Wikipedia page](https://en.wikipedia.org/wiki/CoreWeave) very helpful.

They’ve also been on an acquisition spree this year, including:

* Weights \& Biases [in March 2025](https://www.coreweave.com/blog/coreweave-completes-acquisition-of-weights-biases) (deal closed in May), the AI training observability platform.
* OpenPipe [in September 2025](https://www.coreweave.com/news/coreweave-to-acquire-openpipe-leader-in-reinforcement-learning) \- a reinforcement learning platform, authors of the [Agent Reinforcement Trainer](https://github.com/OpenPipe/ART) Apache 2 licensed open source RL framework.
* Monolith AI [in October 2025](https://investors.coreweave.com/news/news-details/2025/CoreWeave-to-Acquire-Monolith-Expanding-AI-Cloud-Platform-into-Industrial-Innovation/default.aspx), a UK\-based AI model SaaS platform focused on AI for engineering and industrial manufacturing.
* And now Marimo.

Marimo’s own announcement emphasizes continued investment in that tool:

> Marimo is joining CoreWeave. We’re continuing to build the open\-source marimo notebook, while also leveling up molab with serious compute. Our long\-term mission remains the same: to build the world’s best open\-source programming environment for working with data.
> 
> marimo is, and always will be, free, open\-source, and permissively licensed.

Give CoreWeave’s buying spree only really started this year it’s impossible to say how well these acquisitions are likely to play out \- they haven’t yet established a track record.

---

**Note** [2025\-10\-31](https://simonwillison.net/2025/Oct/31/curiosity-driven/) My piece this morning [about the Marimo acquisition](https://simonwillison.net/2025/Oct/31/coreweave-acquires-marimo/) is an example of a variant of a [TIL](https://til.simonwillison.net) \- I didn’t know much about CoreWeave, the acquiring company, so I poked around to answer my own questions and then wrote up what I learned as a short post. Curiosity\-driven blogging if you like.

---

**quote** 2025\-11\-01

> *I plan to introduce hard Rust dependencies and Rust code into APT, no earlier than May 2026\. This extends at first to the Rust compiler and standard library, and the Sequoia ecosystem.   
>   
> In particular, our code to parse .deb, .ar, .tar, and the HTTP signature verification code would strongly benefit from memory safe languages and a stronger approach to   
> unit testing.   
>   
> If you maintain a port without a working Rust toolchain, please ensure it has one within the next 6 months, or sunset the port.*

[Julian Andres Klode](https://lists.debian.org/debian-devel/2025/10/msg00285.html), debian\-devel mailing list

---

**Note** [2025\-11\-01](https://simonwillison.net/2025/Nov/1/sponsors-only-newsletter/)

I just hit send on the October edition of my [sponsors\-only monthly newsletter](https://github.com/sponsors/simonw/). If you are a sponsor (or if you start a sponsorship now) you can [access a copy here](https://github.com/simonw-private/monthly/blob/main/2025-10-october.md). In the newsletter this month:

* Coding agents and “vibe engineering”
* Claude Code for web
* NVIDIA DGX Spark
* Claude Skills
* OpenAI DevDay and GitHub Universe
* Python 3\.14
* October in Chinese Al model releases
* Miscellaneous extras
* Tools I’m using at the moment

Here’s [a copy of the September newsletter](https://gist.github.com/simonw/d6d4d86afc0d76767c63f23fc5137030) as a preview of what you’ll get. Pay $10/month to stay a month ahead of the free copy!

---

**Link** 2025\-11\-01 [Claude Code Can Debug Low\-level Cryptography](https://words.filippo.io/claude-debugging/):

Go cryptography author Filippo Valsorda reports on some very positive results applying Claude Code to the challenge of implementing novel cryptography algorithms. After Claude was able to resolve a “fairly complex low\-level bug” in fresh code he tried it against two other examples and got positive results both time.

Filippo isn’t directly using Claude’s solutions to the bugs, but is finding it useful for tracking down the cause and saving him a solid amount of debugging work:

> Three out of three one\-shot debugging hits with no help is *extremely impressive*. Importantly, there is no need to trust the LLM or review its output when its job is just saving me an hour or two by telling me where the bug is, for me to reason about it and fix it.

Using coding agents in this way may represent a useful entrypoint for LLM\-skeptics who wouldn’t *dream* of letting an autocomplete\-machine writing code on their behalf.

---

**Link** 2025\-11\-02 [How I Use Every Claude Code Feature](https://blog.sshh.io/p/how-i-use-every-claude-code-feature):

Useful, detailed guide from Shrivu Shankar, a Claude Code power user. Lots of tips for both individual Claude Code usage and configuring it for larger team projects.

I appreciated Shrivu’s take on MCP:

> The “Scripting” model (now formalized by Skills) is better, but it needs a secure way to access the environment. This to me is the new, more focused role for MCP.
> 
> Instead of a bloated API, an MCP should be a simple, secure gateway that provides a few powerful, high\-level tools:
> 
> * `download_raw_data(filters...)`
> * `take_sensitive_gated_action(args...)`
> * `execute_code_in_environment_with_state(code...)`
> 
> In this model, MCP’s job isn’t to abstract reality for the agent; its job is to manage the auth, networking, and security boundaries and then get out of the way.

This makes a lot of sense to me. Most of my MCP usage with coding agents like Claude Code has been replaced by custom shell scripts for it to execute, but there’s still a useful role for MCP in helping the agent access secure resources in a controlled way.

---

**Link** 2025\-11\-02 [PyCon US 2026 call for proposals is now open](https://pycon.blogspot.com/2025/10/pycon-us-2026-call-for-proposals-now.html):

PyCon US is coming to the US west coast! 2026 and 2027 will both be held in Long Beach, California \- the 2026 conference is set for May 13th\-19th next year.

The call for proposals just opened. Since we’ll be in LA County I’d love to see talks about Python in the entertainment industry \- if you know someone who could present on that topic please make sure they know about the CFP!

The deadline for submissions is December 19th 2025\. There are two new tracks this year:

> PyCon US is introducing two dedicated Talk tracks to the schedule this year, “The Future of AI with Python” and “Trailblazing Python Security”. For more information and how to submit your proposal, [visit this page](https://us.pycon.org/2026/speaking/guidelines/).

Now is also a great time to consider sponsoring PyCon \- here’s [the sponsorship prospectus](https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/files/psf_sponsor_prospectus_25-26_final_compressed.pdf).

---