# Building a tool to copy-paste share terminal sessions using Claude Code for web

*Plus Living dangerously with Claude, and prompt injection risks for ChatGPT Atlas*

Published: 2025-10-24
Source: https://simonw.substack.com/p/building-a-tool-to-copy-paste-share

---

In this newsletter:

* Video: Building a tool to copy\-paste share terminal sessions using Claude Code for web
* Living dangerously with Claude
* Dane Stuckey (OpenAI CISO) on prompt injection risks for ChatGPT Atlas

Plus 2 links and 1 quotation and 1 note

### [Video: Building a tool to copy\-paste share terminal sessions using Claude Code for web](https://simonwillison.net/2025/Oct/23/claude-code-for-web-video/) \- 2025\-10\-23

This afternoon I was manually converting a terminal session into a shared HTML file for the umpteenth time when I decided to reduce the friction by building a custom tool for it \- and on the spur of the moment I fired up [Descript](https://www.descript.com/) to record the process. The result is this new [11 minute YouTube video](https://www.youtube.com/watch?v=GQvMLLrFPVI) showing my workflow for vibe\-coding simple tools from start to finish.

#### The initial problem

The problem I wanted to solve involves sharing my Claude Code CLI sessions \- and the more general problem of sharing interesting things that happen in my terminal.

A while back I discovered (using my vibe\-coded [clipboard inspector](https://tools.simonwillison.net/clipboard-viewer)) that copying and pasting from the macOS terminal populates a rich text clipboard format which preserves the colors and general formatting of the terminal output.

The problem is that format looks like this:

```
{\rtf1\ansi\ansicpg1252\cocoartf2859
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Monaco;}
{\colortbl;\red255\green255\blue255;\red242\green242\blue242;\red0\green0\blue0;\red204\green98\blue70;
\red0\green0\blue0;\red97\green97\blue97;\red102\green102\blue102;\red255\
```

This struck me as the kind of thing an LLM might be able to write code to parse, so I had [ChatGPT take a crack at it](https://chatgpt.com/share/680801ad-0804-8006-83fc-c2b209841a9c) and then later [rewrote it from scratch with Claude Sonnet 4\.5](https://claude.ai/share/5c12dd0e-713d-4f32-a6c1-d05dee353e4d). The result was [this rtf\-to\-html tool](https://tools.simonwillison.net/rtf-to-html) which lets you paste in rich formatted text and gives you reasonably solid HTML that you can share elsewhere.

To share that HTML I’ve started habitually pasting it into a [GitHub Gist](https://gist.github.com/) and then taking advantage of `gitpreview.github.io`, a neat little unofficial tool that accepts `?GIST_ID` and displays the gist content as a standalone HTML page... which means you can link to rendered HTML that’s stored in a gist.

So my process was:

1. Copy terminal output
2. Paste into [rtf\-to\-html](https://tools.simonwillison.net/rtf-to-html)
3. Copy resulting HTML
4. Paste that int a new GitHub Gist
5. Grab that Gist’s ID
6. Share the link to `gitpreview.github.io?GIST_ID`

Not too much hassle, but frustratingly manual if you’re doing it several times a day.

#### The desired solution

Ideally I want a tool where I can do this:

1. Copy terminal output
2. Paste into a new tool
3. Click a button and get a `gistpreview` link to share

I decided to get Claude Code for web to build the entire thing.

#### The prompt

Here’s the full prompt I used on [claude.ai/code](https://claude.ai/code), pointed at my `simonw/tools` repo, to build the tool:

> `Build a new tool called terminal-to-html which lets the user copy RTF directly from their terminal and paste it into a paste area, it then produces the HTML version of that in a textarea with a copy button, below is a button that says “Save this to a Gist”, and below that is a full preview. It will be very similar to the existing rtf-to-html.html tool but it doesn’t show the raw RTF and it has that Save this to a Gist button`
> 
> `That button should do the same trick that openai-audio-output.html does, with the same use of localStorage and the same flow to get users signed in with a token if they are not already`
> 
> `So click the button, it asks the user to sign in if necessary, then it saves that HTML to a Gist in a file called index.html, gets back the Gist ID and shows the user the URL https://gistpreview.github.io/?6d778a8f9c4c2c005a189ff308c3bc47 - but with their gist ID in it`
> 
> `They can see the URL, they can click it (do not use target=”_blank”) and there is also a “Copy URL” button to copy it to their clipboard`
> 
> `Make the UI mobile friendly but also have it be courier green-text-on-black themed to reflect what it does`
> 
> `If the user pastes and the pasted data is available as HTML but not as RTF skip the RTF step and process the HTML directly`
> 
> `If the user pastes and it’s only available as plain text then generate HTML that is just an open <pre> tag and their text and a closing </pre> tag`

It’s quite a long prompt \- it took me several minutes to type! But it covered the functionality I wanted in enough detail that I was pretty confident Claude would be able to build it.

#### Combining previous tools

I’m using one key technique in this prompt: I’m referencing existing tools in the same repo and telling Claude to imitate their functionality.

I first wrote about this trick last March in [Running OCR against PDFs and images directly in your browser](https://simonwillison.net/2024/Mar/30/ocr-pdfs-images/), where I described how a snippet of code that used PDF.js and another snippet that used Tesseract.js was enough for Claude 3 Opus to build me this [working PDF OCR tool](https://tools.simonwillison.net/ocr). That was actually the tool that kicked off my [tools.simonwillison.net](https://tools.simonwillison.net/) collection in the first place, which has since grown to 139 and counting.

Here I’m telling Claude that I want the RTF to HTML functionality of [rtf\-to\-html.html](https://github.com/simonw/tools/blob/main/rtf-to-html.html) combined with the Gist saving functionality of [openai\-audio\-output.html](https://github.com/simonw/tools/blob/main/openai-audio-output.html).

That one has quite a bit going on. It uses the OpenAI audio API to generate audio output from a text prompt, which is returned by that API as base64\-encoded data in JSON.

Then it offers the user a button to save that JSON to a Gist, which gives the snippet a URL.

Another tool I wrote, [gpt\-4o\-audio\-player.html](https://github.com/simonw/tools/blob/main/gpt-4o-audio-player.html), can then accept that Gist ID in the URL and will fetch the JSON data and make the audio playable in the browser. [Here’s an example](https://tools.simonwillison.net/gpt-4o-audio-player?gist=4a982d3fe7ba8cb4c01e89c69a4a5335).

The trickiest part of this is API tokens. I’ve built tools in the past that require users to paste in a GitHub Personal Access Token (PAT) (which I then store in `localStorage` in their browser \- I don’t want other people’s authentication credentials anywhere near my own servers). But that’s a bit fiddly.

Instead, I [figured out](https://gist.github.com/simonw/975b8934066417fe771561a1b672ad4f) the minimal Cloudflare worker necessary to implement the server\-side portion of GitHub’s authentication flow. That code [lives here](https://github.com/simonw/tools/blob/main/cloudflare-workers/github-auth.js) and means that any of the HTML\+JavaScript tools in my collection can implement a GitHub authentication flow if they need to save Gists.

But I don’t have to tell the model any of that! I can just say “do the same trick that openai\-audio\-output.html does” and Claude Code will work the rest out for itself.

#### The result

Here’s what [the resulting app](https://tools.simonwillison.net/terminal-to-html) looks like after I’ve pasted in some terminal output from Claude Code CLI:

[![Terminal to HTML app. Green glowing text on black. Instructions: Paste terminal output below. Supports RTF, HTML or plain text. There's an HTML Code area with a Copy HTML button, Save this to a Gist and a bunch of HTML. Below is the result of save to a gist showing a URL and a Copy URL button. Below that a preview with the Claude Code heading in ASCII art.](https://substackcdn.com/image/fetch/$s_!R5I0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F40b03bd0-2325-412a-9320-529db118d6bf_1920x1928.jpeg "Terminal to HTML app. Green glowing text on black. Instructions: Paste terminal output below. Supports RTF, HTML or plain text. There's an HTML Code area with a Copy HTML button, Save this to a Gist and a bunch of HTML. Below is the result of save to a gist showing a URL and a Copy URL button. Below that a preview with the Claude Code heading in ASCII art.")](https://substackcdn.com/image/fetch/$s_!R5I0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F40b03bd0-2325-412a-9320-529db118d6bf_1920x1928.jpeg)

It’s exactly what I asked for, and the green\-on\-black terminal aesthetic is spot on too.

#### Other notes from the video

There are a bunch of other things that I touch on in the video. Here’s a quick summary:

* [tools.simonwillison.net/colophon](https://tools.simonwillison.net/colophon) is the list of all of my tools, with accompanying AI\-generated descriptions. Here’s [more about how I built that with Claude Code](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#a-detailed-example) and notes on [how I added the AI\-generated descriptions](https://simonwillison.net/2025/Mar/13/tools-colophon/).
* [gistpreview.github.io](https://gistpreview.github.io) is really neat.
* I used [Descript](https://www.descript.com/) to record and edit the video. I’m still getting the hang of it \- hence the slightly clumsy pan\-and\-zoom \- but it’s pretty great for this kind of screen recording.
* The site’s automated deploys are managed [by this GitHub Actions workflow](https://github.com/simonw/tools/blob/main/.github/workflows/pages.yml). I also have it configured to work with [Cloudflare Pages](https://pages.cloudflare.com/) for those preview deployments from PRs (here’s [an example](https://github.com/simonw/tools/pull/84#issuecomment-3434969331)).
* The automated documentation is created using my [llm](https://llm.datasette.io/) tool and [llm\-anthropic](https://github.com/simonw/llm-anthropic) plugin. Here’s [the script that does that](https://github.com/simonw/tools/blob/main/write_docs.py), recently [upgraded](https://github.com/simonw/tools/commit/99f5f2713f8001b72f4b1cafee5a15c0c26efb0d) to use Claude Haiku 4\.5\.

---

### [Living dangerously with Claude](https://simonwillison.net/2025/Oct/22/living-dangerously-with-claude/) \- 2025\-10\-22

I gave a talk last night at [Claude Code Anonymous](https://luma.com/i37ahi52) in San Francisco, the unofficial meetup for coding agent enthusiasts. I decided to talk about a dichotomy I’ve been struggling with recently. On the one hand I’m getting *enormous* value from running coding agents with as few restrictions as possible. On the other hand I’m deeply concerned by the risks that accompany that freedom.

[Visit my blog](https://simonwillison.net/2025/Oct/22/living-dangerously-with-claude/) for a copy of my slides, plus additional notes and links as [an annotated presentation](https://simonwillison.net/tags/annotated-talks/).

[![Living dangerously with Claude
Simon Willison - simonwillison.net
](https://substackcdn.com/image/fetch/$s_!j9xo!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F78167f53-e0cb-439d-a362-42bf1cd3b137_1920x1080.jpeg "Living dangerously with Claude
Simon Willison - simonwillison.net
")](https://simonwillison.net/2025/Oct/22/living-dangerously-with-claude/)

---

### [Dane Stuckey (OpenAI CISO) on prompt injection risks for ChatGPT Atlas](https://simonwillison.net/2025/Oct/22/openai-ciso-on-atlas/) \- 2025\-10\-22

My biggest complaint about the launch of the ChatGPT Atlas browser [the other day](https://simonwillison.net/2025/Oct/21/introducing-chatgpt-atlas/) was the lack of details on how OpenAI are addressing prompt injection attacks. The [launch post](https://openai.com/index/introducing-chatgpt-atlas/) mostly punted that question to [the System Card](https://openai.com/index/chatgpt-agent-system-card/) for their “ChatGPT agent” browser automation feature from July. Since this was my single biggest question about Atlas I was disappointed not to see it addressed more directly.

OpenAI’s Chief Information Security Officer Dane Stuckey just posted the most detail I’ve seen yet in [a lengthy Twitter post](https://twitter.com/cryps1s/status/1981037851279278414).

I’ll quote from his post here (with my emphasis in bold) and add my own commentary.

He addresses the issue directly by name, with a good single\-sentence explanation of the problem:

> One emerging risk we are very thoughtfully researching and mitigating is **prompt injections, where attackers hide malicious instructions in websites, emails, or other sources, to try to trick the agent into behaving in unintended ways**. The objective for attackers can be as simple as trying to bias the agent’s opinion while shopping, or as consequential as an attacker **trying to get the agent to fetch and leak private data**, such as sensitive information from your email, or credentials.

We saw examples of browser agents from other vendors leaking private data in this way [identified by the Brave security team just yesterday](https://simonwillison.net/2025/Oct/21/unseeable-prompt-injections/).

> Our long\-term goal is that you should be able to trust ChatGPT agent to use your browser, **the same way you’d trust your most competent, trustworthy, and security\-aware colleague** or friend.

This is an interesting way to frame the eventual goal, describing an extraordinary level of trust and competence.

As always, a big difference between AI systems and a human is that an AI system [cannot be held accountable for its actions](https://simonwillison.net/2025/Feb/3/a-computer-can-never-be-held-accountable/). I’ll let my trusted friend use my logged\-in browser only because there are social consequences if they abuse that trust!

> We’re working hard to achieve that. For this launch, we’ve performed extensive red\-teaming, implemented novel model training techniques to reward the model for ignoring malicious instructions, **implemented overlapping guardrails and safety measures**, and added new systems to detect and block such attacks. However, **prompt injection remains a frontier, unsolved security problem, and our adversaries will spend significant time and resources to find ways to make ChatGPT agent fall for these attacks**.

I’m glad to see OpenAI’s CISO openly acknowledging that prompt injection remains an unsolved security problem (three years after we [started talking about it](https://simonwillison.net/2022/Sep/12/prompt-injection/)!).

That “adversaries will spend significant time and resources” thing is the root of why I don’t see guardrails and safety measures as providing a credible solution to this problem.

As I’ve written before, in application security [99% is a failing grade](https://simonwillison.net/2023/May/2/prompt-injection-explained/#prompt-injection.015). If there’s a way to get past the guardrails, no matter how obscure, a motivated adversarial attacker is going to figure that out.

Dane goes on to describe some of those measures:

> To protect our users, and to help improve our models against these attacks:
> 
> 1. We’ve prioritized rapid response systems to help us quickly identify block attack campaigns as we become aware of them.

I like this a lot. OpenAI have an advantage here of being a centralized system \- they can monitor their entire user base for signs of new attack patterns.

It’s still bad news for users that get caught out by a zero\-day prompt injection, but it does at least mean that successful new attack patterns should have a small window of opportunity.

> 2. We are also continuing to invest heavily in security, privacy, and safety \- including research to improve the robustness of our models, security monitors, infrastructure security controls, and **other techniques to help prevent these attacks via defense in depth**.

“Defense in depth” always sounds good, but it worries me that it’s setting up a false sense of security here. If it’s harder but still possible someone is going to get through.

> 3. We’ve designed Atlas to give you controls to help protect yourself. **We have added a feature to allow ChatGPT agent to take action on your behalf, but without access to your credentials called “logged out mode”**. We recommend this mode when you don’t need to take action within your accounts. **Today, we think “logged in mode” is most appropriate for well\-scoped actions on very trusted sites, where the risks of prompt injection are lower**. Asking it to add ingredients to a shopping cart is generally safer than a broad or vague request like “review my emails and take whatever actions are needed.”

Logged out mode is very smart, and is already a tried and tested pattern. I frequently have Claude Code or Codex CLI fire up Playwright to interact with websites, safe in the knowledge that they won’t have access to my logged\-in sessions. ChatGPT’s existing [agent mode](https://chatgpt.com/features/agent/) provides a similar capability.

Logged in mode is where things get scary, especially since we’re delegating security decisions to end\-users of the software. We’ve demonstrated many times over that this is an unfair burden to place on almost any user.

> 4. **When agent is operating on sensitive sites, we have also implemented a “Watch Mode” that alerts you to the sensitive nature of the site and requires you have the tab active to watch the agent do its work**. Agent will pause if you move away from the tab with sensitive information. This ensures you stay aware \- and in control \- of what agent actions the agent is performing. \[...]

This detail is new to me: I need to spend more time with ChatGPT Atlas to see what it looks like in practice.

I tried just now using both GitHub and an online banking site and neither of them seemed to trigger “watch mode” \- Atlas continued to navigate even when I had switched to another application.

Watch mode sounds reasonable in theory \- similar to a driver\-assisted car that requires you to keep your hands on the wheel \- but I’d like to see it in action before I count it as a meaningful mitigation.

Dane closes with an analogy to computer viruses:

> New levels of intelligence and capability require the technology, society, the risk mitigation strategy to co\-evolve. **And as with computer viruses in the early 2000s, we think it’s important for everyone to understand responsible usage**, including thinking about prompt injection attacks, so we can all learn to benefit from this technology safely.

I don’t think the average computer user ever really got the hang of staying clear of computer viruses... we’re still fighting that battle today, albeit much more successfully on mobile platforms that implement tight restrictions on what software can do.

My takeaways from all of this? It’s not done much to influence my overall skepticism of the entire category of browser agents, but it does at least demonstrate that OpenAI are keenly aware of the problems and are investing serious effort in finding the right mix of protections.

How well those protections work is something I expect will become clear over the next few months.

---

**Note** [2025\-10\-22](https://simonwillison.net/2025/Oct/22/claude-code-logs/)

Claude Code stores full logs of your sessions as newline\-delimited JSON in `~/.claude/projects/encoded-directory/*.jsonl` on your machine. I currently have 379MB of these!

Here’s [an example jsonl file](https://github.com/simonw/research/blob/main/deepseek-ocr-nvidia-spark/claude-log.jsonl) which I extracted from my [Deepseek\-OCR on NVIDIA Spark project](https://simonwillison.net/2025/Oct/20/deepseek-ocr-claude-code/). I have a little [vibe\-coded tool](https://github.com/simonw/tools/blob/main/python/claude_to_markdown.py) for converting those into Markdown which produces results [like this](https://github.com/simonw/research/blob/main/deepseek-ocr-nvidia-spark/claude-log.md).

Unfortunately Claude Code has a nasty default behavior of [deleting these after 30 days](https://github.com/anthropics/claude-code/issues/4172)! You can’t disable this entirely, but you can at least delay it for 274 years by adding this to your `~/.claude/settings.json` file:

```
{
  “cleanupPeriodDays”: 99999
}
```

Claude Code’s settings are [documented here](https://docs.claude.com/en/docs/claude-code/settings#available-settings).

---

**Link** 2025\-10\-22 [SLOCCount in WebAssembly](https://tools.simonwillison.net/sloccount):

This project/side\-quest got a little bit out of hand.

[![Screenshot of SLOCCount web application showing code analysis interface. The page header reads "SLOCCount - Count Lines of Code" with subtitle "Analyze source code to count physical Source Lines of Code (SLOC) using Perl and C programs running via WebAssembly" and "Based on SLOCCount by David A. Wheeler". Three tabs are shown: "Paste Code", "GitHub Repository" (selected), and "Upload ZIP". Below is a text input field labeled "GitHub Repository URL:" containing "simonw/llm" and a blue "Analyze Repository" button. The Analysis Results section displays five statistics: Total Lines: 13,490, Languages: 2, Files: 40, Est. Cost (USD)*: $415,101, and Est. Person-Years*: 3.07.](https://substackcdn.com/image/fetch/$s_!PrjR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3aa81a24-5b16-4e52-af55-f1471f48cf91_1484x1690.jpeg "Screenshot of SLOCCount web application showing code analysis interface. The page header reads \"SLOCCount - Count Lines of Code\" with subtitle \"Analyze source code to count physical Source Lines of Code (SLOC) using Perl and C programs running via WebAssembly\" and \"Based on SLOCCount by David A. Wheeler\". Three tabs are shown: \"Paste Code\", \"GitHub Repository\" (selected), and \"Upload ZIP\". Below is a text input field labeled \"GitHub Repository URL:\" containing \"simonw/llm\" and a blue \"Analyze Repository\" button. The Analysis Results section displays five statistics: Total Lines: 13,490, Languages: 2, Files: 40, Est. Cost (USD)*: $415,101, and Est. Person-Years*: 3.07.")](https://substackcdn.com/image/fetch/$s_!PrjR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3aa81a24-5b16-4e52-af55-f1471f48cf91_1484x1690.jpeg)

I remembered an old tool called SLOCCount which could count lines of code and produce an estimate for how much they would cost to develop. I thought it would be fun to play around with it again, especially given how cheap it is to generate code using LLMs these days.

Here’s [the homepage for SLOCCount](https://dwheeler.com/sloccount/) by David A. Wheeler. It dates back to 2001!

I figured it might be fun to try and get it running on the web. Surely someone had compiled Perl to WebAssembly...?

[WebPerl](https://webperl.zero-g.net) by Hauke Dämpfling is exactly that, even adding a neat `<script type=”text/perl”>` tag.

I told Claude Code for web on my iPhone to figure it out and build something, giving it some hints from my initial research:

> Build sloccount.html \- a mobile friendly UI for running the Perl sloccount tool against pasted code or against a GitHub repository that is provided in a form field
> 
> It works using the webperl webassembly build of Perl, plus it loads Perl code from this exact commit of this GitHub repository <https://github.com/licquia/sloccount/tree/7220ff627334a8f646617fe0fa542d401fb5287e> \- I guess via the GitHub API, maybe using the <https://github.com/licquia/sloccount/archive/7220ff627334a8f646617fe0fa542d401fb5287e.zip> URL if that works via CORS
> 
> Test it with playwright Python \- don’t edit any file other than sloccount.html and a tests/test\_sloccount.py file

Since I was working on my phone I didn’t review the results at all. It seemed to work so I deployed it to static hosting... and then when I went to look at it properly later on found that Claude had given up, cheated and reimplemented it in JavaScript instead!

So I switched to Claude Code on my laptop where I have more control and coached Claude through implementing the project for real. This took *way longer* than the project deserved \- probably a solid hour of my active time, spread out across the morning.

I’ve shared some of the transcripts \- [one](https://gistpreview.github.io/?0fc406a18e14a1f7d28bfff02a18eaaf#simonw/0fc406a18e14a1f7d28bfff02a18eaaf), [two](https://gistpreview.github.io/?56ecae45cf2e1baca798a83deea50939), and [three](https://gistpreview.github.io/?79ca231e801fe1188268a54d30aa67ed) \- as terminal sessions rendered to HTML using my [rtf\-to\-html](https://tools.simonwillison.net/rtf-to-html) tool.

At one point I realized that the original SLOCCount project wasn’t even entirely Perl as I had assumed, it included several C utilities! So I had Claude Code figure out how to compile those to WebAssembly (it used Emscripten) and incorporate those into the project (with [notes on what it did](https://github.com/simonw/tools/blob/473e89edfebc27781b434430f2e8a76adfbe3b16/lib/README.md#webassembly-compilation-of-c-programs).)

The end result ([source code here](https://github.com/simonw/tools/blob/main/sloccount.html)) is actually pretty cool. It’s a web UI with three tabs \- one for pasting in code, a second for loading code from a GitHub repository and a third that lets you open a Zip file full of code that you want to analyze. Here’s an animated demo:

[![I enter simonw/llm in the GitHub repository field. It loads 41 files from GitHub and displays a report showing the number of lines and estimated cost.](https://substackcdn.com/image/fetch/$s_!fMDA!,w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5c9b94c2-ce87-4ecf-9503-b5d3f98966b6_716x825.gif "I enter simonw/llm in the GitHub repository field. It loads 41 files from GitHub and displays a report showing the number of lines and estimated cost.")](https://substackcdn.com/image/fetch/$s_!fMDA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5c9b94c2-ce87-4ecf-9503-b5d3f98966b6_716x825.gif)

The cost estimates it produces are of very little value. By default it uses the original method from 2001\. You can also twiddle the factors \- bumping up the expected US software engineer’s annual salary from its 2000 estimate of $56,286 is a good start!

I had ChatGPT [take a guess](https://chatgpt.com/share/68f7e0ac-00c4-8006-979e-64d1f0162283) at what those figures should be for today and included those in the tool, with a **very** prominent warning not to trust them in the slightest.

---

**quote** 2025\-10\-23

> *For resiliency, the DNS Enactor operates redundantly and fully independently in three different Availability Zones (AZs). \[...] When the second Enactor (applying the newest plan) completed its endpoint updates, it then invoked the plan clean\-up process, which identifies plans that are significantly older than the one it just applied and deletes them. At the same time that this clean\-up process was invoked, the first Enactor (which had been unusually delayed) applied its much older plan to the regional DDB endpoint, overwriting the newer plan. \[...] The second Enactor’s clean\-up process then deleted this older plan because it was many generations older than the plan it had just applied. As this plan was deleted, all IP addresses for the regional endpoint were immediately removed.*

[AWS](https://aws.amazon.com/message/101925/), Amazon DynamoDB Service Disruption in Northern Virginia (US\-EAST\-1\) Region (14\.5 hours long!)

---

**Link** 2025\-10\-23 [OpenAI no longer has to preserve all of its ChatGPT data, with some exceptions](https://www.engadget.com/ai/openai-no-longer-has-to-preserve-all-of-its-chatgpt-data-with-some-exceptions-192422093.html):

This is a relief:

> Federal judge Ona T. Wang filed a new order on October 9 that frees OpenAI of an obligation to “preserve and segregate all output log data that would otherwise be deleted on a going forward basis.”

I wrote about this [in June](https://simonwillison.net/2025/Jun/5/openai-court-order/). OpenAI were compelled by a court order to preserve *all* output, even from private chats, in case it became relevant to the ongoing New York Times lawsuit.

Here are those “some exceptions”:

> The judge in the case said that any chat logs already saved under the previous order would still be accessible and that OpenAI is required to hold on to any data related to ChatGPT accounts that have been flagged by the NYT.

---