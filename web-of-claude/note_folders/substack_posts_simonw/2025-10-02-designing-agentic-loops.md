# Designing agentic loops

*Plus coding agent PR stats and AI-assisted tooling that finds genuine security issues in curl*

Published: 2025-10-02
Source: https://simonw.substack.com/p/designing-agentic-loops

---

In this newsletter:

* Designing agentic loops

Plus 2 links and 1 quotation and 1 TIL and 3 notes

### [Designing agentic loops](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/) \- 2025\-09\-30

Coding agents like Anthropic’s [Claude Code](https://claude.com/product/claude-code) and OpenAI’s [Codex CLI](https://github.com/openai/codex) represent a genuine step change in how useful LLMs can be for producing working code. These agents can now directly exercise the code they are writing, correct errors, dig through existing implementation details, and even run experiments to find effective code solutions to problems.

As is so often the case with modern AI, there is a great deal of depth involved in unlocking the full potential of these new tools.

A critical new skill to develop is **designing agentic loops**.

One way to think about coding agents is that they are brute force tools for finding solutions to coding problems. If you can reduce your problem to a clear goal and a set of tools that can iterate towards that goal a coding agent can often brute force its way to an effective solution.

My preferred definition of an LLM agent is something that [runs tools in a loop to achieve a goal](https://simonwillison.net/2025/Sep/18/agents/). The art of using them well is to carefully design the tools and loop for them to use.

* [The joy of YOLO mode](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/#the-joy-of-yolo-mode)
* [Picking the right tools for the loop](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/#picking-the-right-tools-for-the-loop)
* [Issuing tightly scoped credentials](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/#issuing-tightly-scoped-credentials)
* [When to design an agentic loop](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/#when-to-design-an-agentic-loop)
* [This is still a very fresh area](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/#this-is-still-a-very-fresh-area)

#### The joy of YOLO mode

Agents are inherently dangerous \- they can make poor decisions or fall victim to malicious [prompt injection attacks](https://simonwillison.net/tags/prompt-injection/), either of which can result in harmful results from tool calls. Since the most powerful coding agent tool is “run this command in the shell” a rogue agent can do anything that you could do by running a command yourself.

To [quote Solomon Hykes](https://simonwillison.net/2025/Jun/5/wrecking-its-environment-in-a-loop/):

> **An AI agent is an LLM wrecking its environment in a loop.**

Coding agents like Claude Code counter this by defaulting to asking you for approval of almost every command that they run.

This is kind of tedious, but more importantly, it dramatically reduces their effectiveness at solving problems through brute force.

Each of these tools provides its own version of what I like to call YOLO mode, where everything gets approved by default.

This is *so dangerous*, but it’s also key to getting the most productive results!

Here are three key risks to consider from unattended YOLO mode.

1. Bad shell commands deleting or mangling things you care about.
2. Exfiltration attacks where something steals files or data visible to the agent \- source code or secrets held in environment variables are particularly vulnerable here.
3. Attacks that use your machine as a proxy to attack another target \- for DDoS or to disguise the source of other hacking attacks.

If you want to run YOLO mode anyway, you have a few options:

1. Run your agent in a secure sandbox that restricts the files and secrets it can access and the network connections it can make.
2. Use someone else’s computer. That way if your agent goes rogue, there’s only so much damage they can do, including wasting someone else’s CPU cycles.
3. Take a risk! Try to avoid exposing it to potential sources of malicious instructions and hope you catch any mistakes before they cause any damage.

Most people choose option 3\.

Despite the existence of [container escapes](https://attack.mitre.org/techniques/T1611/) I think option 1 using Docker or the new Apple [container tool](https://github.com/apple/container) is a reasonable risk to accept for most people.

Option 2 is my favorite. I like to use [GitHub Codespaces](https://github.com/features/codespaces) for this \- it provides a full container environment on\-demand that’s accessible through your browser and has a generous free tier too. If anything goes wrong it’s a Microsoft Azure machine somewhere that’s burning CPU and the worst that can happen is code you checked out into the environment might be exfiltrated by an attacker, or bad code might be pushed to the attached GitHub repository.

There are plenty of other agent\-like tools that run code on other people’s computers. [Code Interpreter](https://simonwillison.net/tags/code-interpreter/) mode in both ChatGPT and [Claude](https://simonwillison.net/2025/Sep/9/claude-code-interpreter/) can go a surprisingly long way here. I’ve also had a lot of success (ab)using OpenAI’s [Codex Cloud](https://chatgpt.com/features/codex).

Coding agents themselves implement various levels of sandboxing, but so far I’ve not seen convincing enough documentation of these to trust them.

**Update**: It turns out Anthropic have their own documentation on [Safe YOLO mode](https://www.anthropic.com/engineering/claude-code-best-practices#d-safe-yolo-mode) for Claude Code which says:

> Letting Claude run arbitrary commands is risky and can result in data loss, system corruption, or even data exfiltration (e.g., via prompt injection attacks). To minimize these risks, use `--dangerously-skip-permissions` in a container without internet access. You can follow this [reference implementation](https://github.com/anthropics/claude-code/tree/main/.devcontainer) using Docker Dev Containers.

Locking internet access down to a [list of trusted hosts](https://github.com/anthropics/claude-code/blob/5062ed93fc67f9322f807ecbf391ae4376cf8e83/.devcontainer/init-firewall.sh#L66-L75) is a great way to prevent exfiltration attacks from stealing your private source code.

#### Picking the right tools for the loop

Now that we’ve found a safe (enough) way to run in YOLO mode, the next step is to decide which tools we need to make available to the coding agent.

You can bring [MCP](https://modelcontextprotocol.io/) into the mix at this point, but I find it’s usually more productive to think in terms of shell commands instead. Coding agents are *really good* at running shell commands!

If your environment allows them the necessary network access, they can also pull down additional packages from NPM and PyPI and similar. Ensuring your agent runs in an environment where random package installs don’t break things on your main computer is an important consideration as well!

Rather than leaning on MCP, I like to create an [AGENTS.md](https://agents.md/) (or equivalent) file with details of packages I think they may need to use.

For a project that involved taking screenshots of various websites I installed my own [shot\-scraper](https://shot-scraper.datasette.io/) CLI tool and dropped the following in `AGENTS.md`:

```
To take a screenshot, run:

shot-scraper http://www.example.com/ -w 800 -o example.jpg
```

Just that one example is enough for the agent to guess how to swap out the URL and filename for other screenshots.

Good LLMs already know how to use a bewildering array of existing tools. If you say “use [playwright python](https://playwright.dev/python/)“ or “use ffmpeg” most models will use those effectively \- and since they’re running in a loop they can usually recover from mistakes they make at first and figure out the right incantations without extra guidance.

#### Issuing tightly scoped credentials

In addition to exposing the right commands, we also need to consider what credentials we should expose to those commands.

Ideally we wouldn’t need any credentials at all \- plenty of work can be done without signing into anything or providing an API key \- but certain problems will require authenticated access.

This is a deep topic in itself, but I have two key recommendations here:

1. Try to provide credentials to test or staging environments where any damage can be well contained.
2. If a credential can spend money, set a tight budget limit.

I’ll use an example to illustrate. A while ago I was investigating slow cold start times for a scale\-to\-zero application I was running on [Fly.io](https://fly.io/).

I realized I could work a lot faster if I gave Claude Code the ability to directly edit Dockerfiles, deploy them to a Fly account and measure how long they took to launch.

Fly allows you to create organizations, and you can set a budget limit for those organizations and issue a Fly API key that can only create or modify apps within that organization...

So I created a dedicated organization for just this one investigation, set a $5 budget, issued an API key and set Claude Code loose on it!

In that particular case the results weren’t useful enough to describe in more detail, but this was the project where I first realized that “designing an agentic loop” was an important skill to develop.

#### When to design an agentic loop

Not every problem responds well to this pattern of working. The thing to look out for here are problems with **clear success criteria** where finding a good solution is likely to involve (potentially slightly tedious) **trial and error**.

Any time you find yourself thinking “ugh, I’m going to have to try a lot of variations here” is a strong signal that an agentic loop might be worth trying!

A few examples:

* **Debugging**: a test is failing and you need to investigate the root cause. Coding agents that can already run your tests can likely do this without any extra setup.
* **Performance optimization**: this SQL query is too slow, would adding an index help? Have your agent benchmark the query and then add and drop indexes (in an isolated development environment!) to measure their impact.
* **Upgrading dependencies**: you’ve fallen behind on a bunch of dependency upgrades? If your test suite is solid an agentic loop can upgrade them all for you and make any minor updates needed to reflect breaking changes. Make sure a copy of the relevant release notes is available, or that the agent knows where to find them itself.
* **Optimizing container sizes**: Docker container feeling uncomfortably large? Have your agent try different base images and iterate on the Dockerfile to try to shrink it, while keeping the tests passing.

A common theme in all of these is **automated tests**. The value you can get from coding agents and other LLM coding tools is massively amplified by a good, cleanly passing test suite. Thankfully LLMs are great for accelerating the process of putting one of those together, if you don’t have one yet.

#### This is still a very fresh area

**Designing agentic loops** is a very new skill \- Claude Code was [first released](https://www.anthropic.com/news/claude-3-7-sonnet) in just February 2025!

I’m hoping that giving it a clear name can help us have productive conversations about it. There’s *so much more* to figure out about how to use these tools as effectively as possible.

---

**TIL** 2025\-09\-30 [Error 153 Video player configuration error on YouTube embeds](https://til.simonwillison.net/youtube/fixing-153-embed):

I recently noticed that almost every YouTube video on [my blog](https://simonwillison.net/) was displaying the same mysterious error message: …

---

**Note** [2025\-09\-30](https://simonwillison.net/2025/Sep/30/sora-2/)

Having watched this morning’s [Sora 2 introduction video](https://www.youtube.com/watch?v=gzneGhpXwjU), the most notable feature (aside from audio generation \- original Sora was silent, Google’s Veo 3 supported audio in May 2025\) looks to be what OpenAI are calling “cameos” \- the ability to easily capture a video version of yourself or your friends and then use them as characters in generated videos.

My guess is that they are leaning into this based on the *incredible* success of ChatGPT image generation [in March](https://simonwillison.net/2025/Jun/6/six-months-in-llms/#ai-worlds-fair-2025-20.jpeg) \- possibly the most successful product launch of all time, signing up 100 million new users in just the first week after release.

The driving factor for that success? People *love* being able to create personalized images of themselves, their friends and their family members.

Google saw a similar effect with their Nano Banana image generation model. Gemini VP Josh Woodward [tweeted](https://twitter.com/joshwoodward/status/1970894369562796420) on 24th September:

> 🍌 @GeminiApp just passed 5 billion images in less than a month.

Sora 2 cameos looks to me like an attempt to capture that same viral magic but for short\-form videos, not images.

**Update**: I got an invite. Here’s [“simonw performing opera on stage at the royal albert hall in a very fine purple suit with crows flapping around his head dramatically standing in front of a night orchestrion”](https://sora.chatgpt.com/p/s_68dde7529584819193b31947e46f61ee) (it was meant to be a *mighty* orchestrion but I had a typo.)

---

**Note** [2025\-10\-01](https://simonwillison.net/2025/Oct/1/sponsors-only-newsletter/)

I just sent out the September edition of my [sponsors\-only monthly newsletter](https://github.com/sponsors/simonw/). If you are a sponsor (or if you start a sponsorship now) you can [access a copy here](https://github.com/simonw-private/monthly/blob/main/2025-09-september.md). The sections this month are:

* Best model for code? GPT\-5\-Codex... then Claude 4\.5 Sonnet
* I’ve grudgingly accepted a definition for “agent”
* GPT\-5 Research Goblin and Google AI Mode
* Claude has Code Interpreter now
* The lethal trifecta in the Economist
* Other significant model releases
* Notable AI success stories
* Video models are zero\-shot learners and reasoners
* Tools I’m using at the moment
* Other bits and pieces

Here’s [a copy of the August newsletter](https://gist.github.com/simonw/43bf3bd7f9951a8e82a9e61b53399ede) as a preview of what you’ll get. Pay $10/month to stay a month ahead of the free copy!

---

**Note** [2025\-10\-01](https://simonwillison.net/2025/Oct/1/two-pelicans/)

Two new models from Chinese AI labs in the past few days. I tried them both out using [llm\-openrouter](https://github.com/simonw/llm-openrouter):

**DeepSeek\-V3\.2\-Exp** from DeepSeek. [Announcement](https://api-docs.deepseek.com/news/news250929), [Tech Report](https://github.com/deepseek-ai/DeepSeek-V3.2-Exp/blob/main/DeepSeek_V3_2.pdf), [Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-V3.2-Exp) (690GB, MIT license).

> As an intermediate step toward our next\-generation architecture, V3\.2\-Exp builds upon V3\.1\-Terminus by introducing DeepSeek Sparse Attention—a sparse attention mechanism designed to explore and validate optimizations for training and inference efficiency in long\-context scenarios.

This one felt *very slow* when I accessed it via OpenRouter \- I probably got routed to [one of the slower providers](https://openrouter.ai/deepseek/deepseek-v3.2-exp/providers). Here’s [the pelican](https://gist.github.com/simonw/659966a678dedd9d4e55a01a4256ac56):

[![Claude Sonnet 4.5 says: Minimalist line drawing illustration of a stylized bird riding a bicycle, with clock faces as wheels showing approximately 10:10, orange beak and pedal accents, on a light gray background with a dashed line representing the ground.](https://substackcdn.com/image/fetch/$s_!lCqO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4582c55a-c9a2-48b2-aca3-db20ab0dc4ae_800x600.png "Claude Sonnet 4.5 says: Minimalist line drawing illustration of a stylized bird riding a bicycle, with clock faces as wheels showing approximately 10:10, orange beak and pedal accents, on a light gray background with a dashed line representing the ground.")](https://substackcdn.com/image/fetch/$s_!lCqO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4582c55a-c9a2-48b2-aca3-db20ab0dc4ae_800x600.png)

**GLM\-4\.6 from Z.ai**. [Announcement](https://z.ai/blog/glm-4.6), [Hugging Face](https://huggingface.co/zai-org/GLM-4.6) (714GB, MIT license).

> The context window has been expanded from 128K to 200K tokens \[...] higher scores on code benchmarks \[...] GLM\-4\.6 exhibits stronger performance in tool using and search\-based agents.

Here’s [the pelican](https://gist.github.com/simonw/5cf05165fc721b5f7eac3b10eeff20d5) for that:

[![Claude Sonnet 4.5 says: Illustration of a white seagull with an orange beak and yellow feet riding a bicycle against a light blue sky background with white clouds and a yellow sun.](https://substackcdn.com/image/fetch/$s_!Ruo3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4cb295f1-7403-4c36-bc1a-c9b273fd2e09_800x600.png "Claude Sonnet 4.5 says: Illustration of a white seagull with an orange beak and yellow feet riding a bicycle against a light blue sky background with white clouds and a yellow sun.")](https://substackcdn.com/image/fetch/$s_!Ruo3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4cb295f1-7403-4c36-bc1a-c9b273fd2e09_800x600.png)

---

**Link** 2025\-10\-01 [aavetis/PRarena](https://github.com/aavetis/PRarena):

Albert Avetisian runs this repository on GitHub which uses the Github Search API to track the number of PRs that can be credited to a collection of different coding agents. The repo runs [this collect\_data.py script](https://github.com/aavetis/PRarena/blob/main/collect_data.py) every three hours [using GitHub Actions](https://github.com/aavetis/PRarena/blob/main/.github/workflows/pr%E2%80%91stats.yml) to collect the data, then updates the [PR Arena site](https://prarena.ai/) with a visual leaderboard.

The result is this neat chart showing adoption of different agents over time, along with their PR success rate:

[![Line and bar chart showing PR metrics over time from 05/26 to 10/01. The left y-axis shows "Number of PRs" from 0 to 1,800,000, the right y-axis shows "Success Rate (%)" from 0% to 100%, and the x-axis shows "Time" with dates. Five line plots track success percentages: "Copilot Success % (Ready)" and "Copilot Success % (All)" (both blue, top lines around 90-95%), "Codex Success % (Ready)" and "Codex Success % (All)" (both brown/orange, middle lines declining from 80% to 60%), and "Cursor Success % (Ready)" and "Cursor Success % (All)" (both purple, middle lines around 75-85%), "Devin Success % (Ready)" and "Devin Success % (All)" (both teal/green, lower lines around 65%), and "Codegen Success % (Ready)" and "Codegen Success % (All)" (both brown, declining lines). Stacked bar charts show total and merged PRs for each tool: light blue and dark blue for Copilot, light red and dark red for Codex, light purple and dark purple for Cursor, light green and dark green for Devin, and light orange for Codegen. The bars show increasing volumes over time, with the largest bars appearing at 10/01 reaching approximately 1,700,000 total PRs.](https://substackcdn.com/image/fetch/$s_!dRos!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb99e9d0-bc49-43b3-b64b-c1a8b7f565b9_1844x992.jpeg "Line and bar chart showing PR metrics over time from 05/26 to 10/01. The left y-axis shows \"Number of PRs\" from 0 to 1,800,000, the right y-axis shows \"Success Rate (%)\" from 0% to 100%, and the x-axis shows \"Time\" with dates. Five line plots track success percentages: \"Copilot Success % (Ready)\" and \"Copilot Success % (All)\" (both blue, top lines around 90-95%), \"Codex Success % (Ready)\" and \"Codex Success % (All)\" (both brown/orange, middle lines declining from 80% to 60%), and \"Cursor Success % (Ready)\" and \"Cursor Success % (All)\" (both purple, middle lines around 75-85%), \"Devin Success % (Ready)\" and \"Devin Success % (All)\" (both teal/green, lower lines around 65%), and \"Codegen Success % (Ready)\" and \"Codegen Success % (All)\" (both brown, declining lines). Stacked bar charts show total and merged PRs for each tool: light blue and dark blue for Copilot, light red and dark red for Codex, light purple and dark purple for Cursor, light green and dark green for Devin, and light orange for Codegen. The bars show increasing volumes over time, with the largest bars appearing at 10/01 reaching approximately 1,700,000 total PRs.")](https://substackcdn.com/image/fetch/$s_!dRos!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb99e9d0-bc49-43b3-b64b-c1a8b7f565b9_1844x992.jpeg)

I found this today while trying to pull off the exact same trick myself! I got as far as creating the following table before finding Albert’s work and abandoning my own project.

[![A data table comparing AI coding tools showing: Claude Code (search: is:pr in:body "Generated with Claude Code") - 146,000 Total PRs, 123,000 Merged PRs, 84.2% merged, Earliest Feb 21st; GitHub Copilot (search: is:pr author:copilot-swe-agent[bot]) - 247,000 Total PRs, 152,000 Merged PRs, 61.5% merged, Earliest March 7th; Codex Cloud (search: is:pr in:body "chatgpt.com" label:codex) - 1,900,000 Total PRs, 1,600,000 Merged PRs, 84.2% merged, Earliest April 23rd; Google Jules (search: is:pr author:google-labs-jules[bot]) - 35,400 Total PRs, 27,800 Merged PRs, 78.5% merged, Earliest May 22nd.](https://substackcdn.com/image/fetch/$s_!yCVb!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F465a7286-bd18-4f2d-b186-5bd719c0b6c0_1178x472.png "A data table comparing AI coding tools showing: Claude Code (search: is:pr in:body \"Generated with Claude Code\") - 146,000 Total PRs, 123,000 Merged PRs, 84.2% merged, Earliest Feb 21st; GitHub Copilot (search: is:pr author:copilot-swe-agent[bot]) - 247,000 Total PRs, 152,000 Merged PRs, 61.5% merged, Earliest March 7th; Codex Cloud (search: is:pr in:body \"chatgpt.com\" label:codex) - 1,900,000 Total PRs, 1,600,000 Merged PRs, 84.2% merged, Earliest April 23rd; Google Jules (search: is:pr author:google-labs-jules[bot]) - 35,400 Total PRs, 27,800 Merged PRs, 78.5% merged, Earliest May 22nd.")](https://substackcdn.com/image/fetch/$s_!yCVb!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F465a7286-bd18-4f2d-b186-5bd719c0b6c0_1178x472.png)

(Those “earliest” dates are a little questionable, I tried to filter out false positives and find the oldest PR that appeared to really be from the agent in question.)

It looks like OpenAI’s Codex Cloud is *massively* ahead of the competition right now in terms of numbers of PRs both opened and merged on GitHub.

**Update**: To clarify, these numbers are for the category of **autonomous coding agents** \- those systems where you assign a cloud\-based agent a task or issue and the output is a PR against your repository. They do not (and cannot) capture the popularity of many forms of AI tooling that don’t result in an easily identifiable pull request.

Claude Code for example will be dramatically under\-counted here because its version of an autonomous coding agent comes in the form of a somewhat obscure GitHub Actions workflow [buried in the documentation](https://docs.claude.com/en/docs/claude-code/github-actions).

---

**quote** 2025\-10\-02

> *When attention is being appropriated, producers need to weigh the costs and benefits of the transaction. To assess whether the appropriation of attention is net\-positive, it’s useful to distinguish between extractive and non\-extractive contributions. Extractive contributions are those where the marginal cost of reviewing and merging that contribution is greater than the marginal benefit to the project’s producers. In the case of a code contribution, it might be a pull request that’s too complex or unwieldy to review, given the potential upside*

[Nadia Eghbal](https://discourse.llvm.org/t/rfc-llvm-ai-tool-policy-start-small-no-slop/88476), *Working in Public*, via the draft LLVM AI tools policy

---

**Link** 2025\-10\-02 [Daniel Stenberg’s note on AI assisted curl bug reports](https://mastodon.social/@bagder/115241241075258997):

Curl maintainer Daniel Stenberg on Mastodon:

> Joshua Rogers sent us a *massive* list of potential issues in \#curl that he found using his set of AI assisted tools. Code analyzer style nits all over. Mostly smaller bugs, but still bugs and there could be one or two actual security flaws in there. Actually truly awesome findings.
> 
> I have already landed 22(!) bugfixes thanks to this, and I have over twice that amount of issues left to go through. Wade through perhaps.
> 
> Credited “Reported in Joshua’s sarif data” if you want to look for yourself

I searched for `is:pr Joshua sarif data is:closed` in the `curl` GitHub repository [and found 49 completed PRs so far](https://github.com/curl/curl/pulls?q=is%3Apr+Joshua+sarif+data+is%3Aclosed).

Joshua’s own post about this: [Hacking with AI SASTs: An overview of ‘AI Security Engineers’ / ‘LLM Security Scanners’ for Penetration Testers and Security Teams](https://joshua.hu/llm-engineer-review-sast-security-ai-tools-pentesters). The [accompanying presentation PDF](https://joshua.hu/files/AI_SAST_PRESENTATION.pdf) includes screenshots of some of the tools he used, which included Almanax, Amplify Security, Corgea, Gecko Security, and ZeroPath. Here’s his vendor summary:

[![Screenshot of a presentation slide titled "General Results" with "RACEDAY" in top right corner. Three columns compare security tools: "Almanax" - Excellent single-function "obvious" results. Not so good at large/complicated code. Great at simple malicious code detection. Raw-bones solutions, not yet a mature product. "Gorgoa" - Discovered nearly all "test-case" issues. Discovered real vulns in big codebases. Tons of F/Ps. Malicious detection sucks. Excellent UI & reports. Tons of bugs in UI. PR reviews failed hard. "ZeroPath" - Discovered all "test-case" issues. Intimidatingly good bug and vuln findings. Excellent PR scanning. In-built issue chatbot. Even better with policies. Extremely slow UI. Complex issuedescriptions.](https://substackcdn.com/image/fetch/$s_!AYGt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69827855-6011-44d4-a8d2-7031575ca436_1019x570.jpeg "Screenshot of a presentation slide titled \"General Results\" with \"RACEDAY\" in top right corner. Three columns compare security tools: \"Almanax\" - Excellent single-function \"obvious\" results. Not so good at large/complicated code. Great at simple malicious code detection. Raw-bones solutions, not yet a mature product. \"Gorgoa\" - Discovered nearly all \"test-case\" issues. Discovered real vulns in big codebases. Tons of F/Ps. Malicious detection sucks. Excellent UI & reports. Tons of bugs in UI. PR reviews failed hard. \"ZeroPath\" - Discovered all \"test-case\" issues. Intimidatingly good bug and vuln findings. Excellent PR scanning. In-built issue chatbot. Even better with policies. Extremely slow UI. Complex issuedescriptions.")](https://substackcdn.com/image/fetch/$s_!AYGt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69827855-6011-44d4-a8d2-7031575ca436_1019x570.jpeg)

This result is especially notable because Daniel has been outspoken about the deluge of junk AI\-assisted reports on “security issues” that curl has received in the past. In [May this year](https://simonwillison.net/2025/May/6/daniel-stenberg/), concerning HackerOne:

> We now ban every reporter INSTANTLY who submits reports we deem AI slop. A threshold has been reached. We are effectively being DDoSed. If we could, we would charge them for this waste of our time.

He also wrote about this [in January 2024](https://daniel.haxx.se/blog/2024/01/02/the-i-in-llm-stands-for-intelligence/), where he included this note:

> I do however suspect that if you just add an ever so tiny (intelligent) human check to the mix, the use and outcome of any such tools will become so much better. I suspect that will be true for a long time into the future as well.

This is yet another illustration of how much more interesting these tools are when experienced professionals use them to augment their existing skills.

---