# OpenAI are quietly adopting skills, now available in ChatGPT and Codex CLI

*Plus using coding agents to port Rust to Python and then Python to JavaScript*

Published: 2025-12-17
Source: https://simonw.substack.com/p/openai-are-quietly-adopting-skills

---

In this newsletter:

* OpenAI are quietly adopting skills, now available in ChatGPT and Codex CLI
* JustHTML is a fascinating example of vibe engineering in action
* I ported JustHTML from Python to JavaScript with Codex CLI and GPT\-5\.2 in 4\.5 hours

Plus 8 links and 4 quotations

*If you find this newsletter useful, please consider [sponsoring me via GitHub](https://github.com/sponsors/simonw). $10/month and higher sponsors get a monthly newsletter with my summary of the most important trends of the past 30 days \- here are previews from [September](https://gist.github.com/simonw/d6d4d86afc0d76767c63f23fc5137030) and [October](https://gist.github.com/simonw/3385bc8c83a8157557f06865a0302753).*

### [OpenAI are quietly adopting skills, now available in ChatGPT and Codex CLI](https://simonwillison.net/2025/Dec/12/openai-skills/) \- 2025\-12\-12

One of the things that most excited me about [Anthropic’s new Skills mechanism](https://simonwillison.net/2025/Oct/16/claude-skills/) back in October is how easy it looked for other platforms to implement. A skill is just a folder with a Markdown file and some optional extra resources and scripts, so any LLM tool with the ability to navigate and read from a filesystem should be capable of using them. It turns out OpenAI are doing exactly that, with skills support quietly showing up in both their Codex CLI tool and now also in ChatGPT itself.

#### Skills in ChatGPT

I learned about this [from Elias Judin](https://x.com/elias_judin/status/1999491647563006171) this morning. It turns out the Code Interpreter feature of ChatGPT now has a new `/home/oai/skills` folder which you can access simply by prompting:

> `Create a zip file of /home/oai/skills`

I [tried that myself](https://chatgpt.com/share/693c9645-caa4-8006-9302-0a9226ea7599) and got back [this zip file](https://static.simonwillison.net/static/cors-allow/2025/skills.zip). Here’s [a UI for exploring its content](https://tools.simonwillison.net/zip-wheel-explorer?url=https%3A%2F%2Fstatic.simonwillison.net%2Fstatic%2Fcors-allow%2F2025%2Fskills.zip) ([more about that tool](https://tools.simonwillison.net/colophon#zip-wheel-explorer.html)).

[![Screenshot of file explorer. Files skills/docs/render_docsx.py and skills/docs/skill.md and skills/pdfs/ and skills/pdfs/skill.md - that last one is expanded and reads: # PDF reading, creation, and review guidance  ## Reading PDFs - Use pdftoppm -png $OUTDIR/$BASENAME.pdf $OUTDIR/$BASENAME to convert PDFs to PNGs. - Then open the PNGs and read the images. - pdfplumber is also installed and can be used to read PDFs. It can be used as a complementary tool to pdftoppm but not replacing it. - Only do python printing as a last resort because you will miss important details with text extraction (e.g. figures, tables, diagrams).  ## Primary tooling for creating PDFs - Generate PDFs programmatically with reportlab as the primary tool. In most cases, you should use reportlab to create PDFs. - If there are other packages you think are necessary for the task (eg. pypdf, pyMuPDF), you can use them but you may need topip install them first. - After each meaningful update—content additions, layout adjustments, or style changes—render the PDF to images to check layout fidelity:   - pdftoppm -png $INPUT_PDF $OUTPUT_PREFIX - Inspect every exported PNG before continuing work. If anything looks off, fix the source and re-run the render → inspect loop until the pages are clean.  ## Quality expectations - Maintain a polished, intentional visual design: consistent typography, spacing, margins, color palette, and clear section breaks across all pages. - Avoid major rendering issues—no clipped text, overlapping elements, black squares, broken tables, or unreadable glyphs. The rendered pages should look like a curated document, not raw template output. - Charts, tables, diagrams, and images must be sharp, well-aligned, and properly labeled in the PNGs. Legends and axes should be readable without excessive zoom. - Text must be readable at normal viewing size; avoid walls of filler text or dense, unstructured bullet lists. Use whitespace to separate ideas. - Never use the U+2011 non-breaking hyphen or other unicode dashes as they will not be](https://substackcdn.com/image/fetch/$s_!dGn2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F648a7e52-0471-4ca6-8973-dda662431654_1564x1612.jpeg "Screenshot of file explorer. Files skills/docs/render_docsx.py and skills/docs/skill.md and skills/pdfs/ and skills/pdfs/skill.md - that last one is expanded and reads: # PDF reading, creation, and review guidance  ## Reading PDFs - Use pdftoppm -png $OUTDIR/$BASENAME.pdf $OUTDIR/$BASENAME to convert PDFs to PNGs. - Then open the PNGs and read the images. - pdfplumber is also installed and can be used to read PDFs. It can be used as a complementary tool to pdftoppm but not replacing it. - Only do python printing as a last resort because you will miss important details with text extraction (e.g. figures, tables, diagrams).  ## Primary tooling for creating PDFs - Generate PDFs programmatically with reportlab as the primary tool. In most cases, you should use reportlab to create PDFs. - If there are other packages you think are necessary for the task (eg. pypdf, pyMuPDF), you can use them but you may need topip install them first. - After each meaningful update—content additions, layout adjustments, or style changes—render the PDF to images to check layout fidelity:   - pdftoppm -png $INPUT_PDF $OUTPUT_PREFIX - Inspect every exported PNG before continuing work. If anything looks off, fix the source and re-run the render → inspect loop until the pages are clean.  ## Quality expectations - Maintain a polished, intentional visual design: consistent typography, spacing, margins, color palette, and clear section breaks across all pages. - Avoid major rendering issues—no clipped text, overlapping elements, black squares, broken tables, or unreadable glyphs. The rendered pages should look like a curated document, not raw template output. - Charts, tables, diagrams, and images must be sharp, well-aligned, and properly labeled in the PNGs. Legends and axes should be readable without excessive zoom. - Text must be readable at normal viewing size; avoid walls of filler text or dense, unstructured bullet lists. Use whitespace to separate ideas. - Never use the U+2011 non-breaking hyphen or other unicode dashes as they will not be")](https://substackcdn.com/image/fetch/$s_!dGn2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F648a7e52-0471-4ca6-8973-dda662431654_1564x1612.jpeg)

So far they cover spreadsheets, docx and PDFs. Interestingly their chosen approach for PDFs and documents is to convert them to rendered per\-page PNGs and then pass those through their vision\-enabled GPT models, presumably to maintain information from layout and graphics that would be lost if they just ran text extraction.

Elias [shared copies in a GitHub repo](https://github.com/eliasjudin/oai-skills). They look very similar to Anthropic’s implementation of the same kind of idea, currently published in their [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills) repository.

I tried it out by prompting:

> Create a PDF with a summary of the rimu tree situation right now and what it means for kakapo breeding season

Sure enough, GPT\-5\.2 Thinking started with:

> Reading skill.md for PDF creation guidelines

Then:

> Searching rimu mast and Kākāpō 2025 breeding status

It took [just over eleven minutes](https://chatgpt.com/share/693ca54b-f770-8006-904b-9f31a585180a) to produce [this PDF](https://static.simonwillison.net/static/cors-allow/2025/rimu_kakapo_breeding_brief.pdf), which was long enough that I had Claude Code for web [build me a custom PDF viewing tool](https://github.com/simonw/tools/pull/155) while I waited.

[Here’s ChatGPT’s PDF in that tool](https://tools.simonwillison.net/view-pdf?url=https%3A%2F%2Fstatic.simonwillison.net%2Fstatic%2Fcors-allow%2F2025%2Frimu_kakapo_breeding_brief.pdf).

[![Screenshot of my tool. There is a URL at the top, a Load PDF button and pagination controls. Then the PDF itself is shown, which reads: Rimu mast status and what it means for the kākāpō breeding season Summary as of 12 December 2025 (Pacific/Auckland context) Kākāpō breeding is tightly linked to rimu (Dacrydium cupressinum) mast events: when rimu trees set and ripen large amounts of fruit, female kākāpō are much more likely to nest, and more chicks can be successfully raised. Current monitoring indicates an unusually strong rimu fruiting signal heading into the 2025/26 season, which sets the stage for a potentially large breeding year in 2026.^1,2 Key numbers at a glance Kākāpō population (official DOC count) 237 birds alive Breeding trigger (rimu fruiting)>10% of rimu branch tips bearing fruit Forecast rimu fruiting for 2026 (DOC monitoring) Around 50–60% fruiting across breeding islands¹Breeding-age females (DOC 2025 planning figure)About 87 females (potentially nearly all could nest)](https://substackcdn.com/image/fetch/$s_!v_Xr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdbb9dfc5-7225-45f7-acac-79bbeafb2c82_1836x1422.jpeg "Screenshot of my tool. There is a URL at the top, a Load PDF button and pagination controls. Then the PDF itself is shown, which reads: Rimu mast status and what it means for the kākāpō breeding season Summary as of 12 December 2025 (Pacific/Auckland context) Kākāpō breeding is tightly linked to rimu (Dacrydium cupressinum) mast events: when rimu trees set and ripen large amounts of fruit, female kākāpō are much more likely to nest, and more chicks can be successfully raised. Current monitoring indicates an unusually strong rimu fruiting signal heading into the 2025/26 season, which sets the stage for a potentially large breeding year in 2026.^1,2 Key numbers at a glance Kākāpō population (official DOC count) 237 birds alive Breeding trigger (rimu fruiting)>10% of rimu branch tips bearing fruit Forecast rimu fruiting for 2026 (DOC monitoring) Around 50–60% fruiting across breeding islands¹Breeding-age females (DOC 2025 planning figure)About 87 females (potentially nearly all could nest)")](https://substackcdn.com/image/fetch/$s_!v_Xr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdbb9dfc5-7225-45f7-acac-79bbeafb2c82_1836x1422.jpeg)

(I am **very excited** about [Kākāpō breeding season this year](https://www.auckland.ac.nz/en/news/2025/12/03/bumper-breeding-season-for-kakapo-on-the-cards.html).)

The reason it took so long is that it was fastidious about looking at and tweaking its own work. I appreciated that at one point it tried rendering the PDF and noticed that the macrons in kākāpō were not supported by the chosen font, so it switched to something else:

[![ChatGPT screenshot. Analyzed image. There's an image of a page of PDF with obvious black blocks on some of the letters in the heading. It then says: Fixing font issues with macrons. The page is showing black squares for words like "kākāpō," probably because Helvetica can't handle macrons. I'll switch to a font that supports them, such as DejaVu Sans or Noto Sans. I'll register both regular and bold fonts, then apply them to the document. I'll update the footer to note the issue with Helvetica. Time to rebuild the PDF!](https://substackcdn.com/image/fetch/$s_!0u8K!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fafdc66e9-190a-4086-a65a-93a9f132128c_842x1026.jpeg "ChatGPT screenshot. Analyzed image. There's an image of a page of PDF with obvious black blocks on some of the letters in the heading. It then says: Fixing font issues with macrons. The page is showing black squares for words like \"kākāpō,\" probably because Helvetica can't handle macrons. I'll switch to a font that supports them, such as DejaVu Sans or Noto Sans. I'll register both regular and bold fonts, then apply them to the document. I'll update the footer to note the issue with Helvetica. Time to rebuild the PDF!")](https://substackcdn.com/image/fetch/$s_!0u8K!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fafdc66e9-190a-4086-a65a-93a9f132128c_842x1026.jpeg)

#### Skills in Codex CLI

Meanwhile, two weeks ago OpenAI’s open source Codex CLI tool landed a PR titled [feat: experimental support for skills.md](https://github.com/openai/codex/pull/7412). The most recent docs for that are in [docs/skills.md](https://github.com/openai/codex/blob/main/docs/skills.md).

The documentation suggests that any folder in `~/.codex/skills` will be treated as a skill.

I dug around and found the code that generates the prompt that drives the skill system in [codex\-rs/core/src/skills/render.rs](https://github.com/openai/codex/blob/ad7b9d63c326d5c92049abd16f9f5fb64a573a69/codex-rs/core/src/skills/render.rs#L20-L38) \- here’s a Gist with [a more readable version of that prompt](https://gist.github.com/simonw/25f2c3a9e350274bc2b76a79bc8ae8b2).

I [used Claude Opus 4\.5’s skill authoring skill](https://claude.ai/share/0a9b369b-f868-4065-91d1-fd646c5db3f4) to create [this skill for creating Datasette plugins](https://github.com/datasette/skill), then installed it into my Codex CLI skills folder like this:

```
git clone https://github.com/datasette/skill \
  ~/.codex/skills/datasette-plugin
```

You have to run Codex with the `--enable skills` option. I ran this:

```
cd /tmp
mkdir datasette-cowsay
cd datasette-cowsay
codex --enable skills -m gpt-5.2
```

Then prompted:

> `list skills`

And Codex replied:

> `- datasette-plugins — Writing Datasette plugins using Python + pluggy (file: /Users/simon/.codex/skills/datasette-plugin/SKILL.md)`  
> `- Discovery — How to find/identify available skills (no SKILL.md path provided in the list)`

Then I said:

> `Write a Datasette plugin in this folder adding a /-/cowsay?text=hello page that displays a pre with cowsay from PyPI saying that text`

It worked perfectly! Here’s [the plugin code it wrote](https://github.com/simonw/datasette-cowsay) and here’s [a copy of the full Codex CLI transcript](http://gistpreview.github.io/?96ee928370b18eabc2e0fad9aaa46d4b), generated with my [terminal\-to\-html tool](https://simonwillison.net/2025/Oct/23/claude-code-for-web-video/).

You can try that out yourself if you have `uvx` installed like this:

```
uvx --with https://github.com/simonw/datasette-cowsay/archive/refs/heads/main.zip \
  datasette
```

Then visit:

```
http://127.0.0.1:8001/-/cowsay?text=This+is+pretty+fun
```

[![Screenshot of that URL in Firefox, an ASCII art cow says This is pretty fun.](https://substackcdn.com/image/fetch/$s_!Biwd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5171611-c2cd-4d4d-b81e-7d1de1d6ab13_1414x416.jpeg "Screenshot of that URL in Firefox, an ASCII art cow says This is pretty fun.")](https://substackcdn.com/image/fetch/$s_!Biwd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5171611-c2cd-4d4d-b81e-7d1de1d6ab13_1414x416.jpeg)

#### Skills are a keeper

When I first wrote about skills in October I said [Claude Skills are awesome, maybe a bigger deal than MCP](https://simonwillison.net/2025/Oct/16/claude-skills/). The fact that it’s just turned December and OpenAI have already leaned into them in a big way reinforces to me that I called that one correctly.

Skills are based on a *very* light specification, if you could even call it that, but I still think it would be good for these to be formally documented somewhere. This could be a good initiative for the new [Agentic AI Foundation](https://aaif.io/) ([previously](https://simonwillison.net/2025/Dec/9/agentic-ai-foundation/)) to take on.

---

### [JustHTML is a fascinating example of vibe engineering in action](https://simonwillison.net/2025/Dec/14/justhtml/) \- 2025\-12\-14

I recently came across [JustHTML](https://github.com/EmilStenstrom/justhtml), a new Python library for parsing HTML released by Emil Stenström. It’s a very interesting piece of software, both as a useful library and as a case study in sophisticated AI\-assisted programming.

#### First impressions of JustHTML

I didn’t initially know that JustHTML had been written with AI assistance at all. The README caught my eye due to some attractive characteristics:

* It’s pure Python. I like libraries that are pure Python (no C extensions or similar) because it makes them easy to use in less conventional Python environments, including Pyodide.
* “Passes all 9,200\+ tests in the official [html5lib\-tests](https://github.com/html5lib/html5lib-tests) suite (used by browser vendors)” \- this instantly caught my attention! HTML5 is a big, complicated but meticulously written specification.
* 100% test coverage. That’s not something you see every day.
* CSS selector queries as a feature. I built a Python library for this [many years ago](https://github.com/simonw/soupselect) and I’m always interested in seeing new implementations of that pattern.
* html5lib has been [inconsistently maintained](https://github.com/mozilla/bleach/issues/698) over the last few years, leaving me interested in potential alternatives.
* It’s only 3,000 lines of implementation code (and another \~11,000 of tests.)

I was out and about without a laptop so I decided to put JustHTML through its paces on my phone. I [prompted Claude Code for web](https://github.com/simonw/tools/pull/156#issue-3726212220) on my phone and had it build [this Pyodide\-powered HTML tool](https://tools.simonwillison.net/justhtml) for trying it out:

[![Screenshot of a web app interface titled "Playground Mode" with buttons labeled "CSS Selector Query" (purple, selected), "Pretty Print HTML", "Tree Structure", "Stream Events", "Extract Text", and "To Markdown" (all gray). Below is a text field labeled "CSS Selector:" containing "p" and a green "Run Query" button. An "Output" section with dark background shows 3 matches in a green badge and displays HTML code](https://substackcdn.com/image/fetch/$s_!D7sH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0fac29de-1bcc-4092-b9cd-4775bfe1639a_766x1474.jpeg "Screenshot of a web app interface titled \"Playground Mode\" with buttons labeled \"CSS Selector Query\" (purple, selected), \"Pretty Print HTML\", \"Tree Structure\", \"Stream Events\", \"Extract Text\", and \"To Markdown\" (all gray). Below is a text field labeled \"CSS Selector:\" containing \"p\" and a green \"Run Query\" button. An \"Output\" section with dark background shows 3 matches in a green badge and displays HTML code")](https://substackcdn.com/image/fetch/$s_!D7sH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0fac29de-1bcc-4092-b9cd-4775bfe1639a_766x1474.jpeg)

This was enough for me to convince myself that the core functionality worked as advertised. It’s a neat piece of code!

#### Turns out it was almost all built by LLMs

At this point I went looking for some more background information on the library and found Emil’s blog entry about it: [How I wrote JustHTML using coding agents](https://friendlybit.com/python/writing-justhtml-with-coding-agents/):

> Writing a full HTML5 parser is not a short one\-shot problem. I have been working on this project for a couple of months on off\-hours.
> 
> Tooling: I used plain VS Code with Github Copilot in Agent mode. I enabled automatic approval of all commands, and then added a blacklist of commands that I always wanted to approve manually. I wrote an [agent instruction](https://github.com/EmilStenstrom/justhtml/blob/main/.github/copilot-instructions.md) that told it to keep working, and don’t stop to ask questions. Worked well!

Emil used several different models \- an advantage of working in VS Code Agent mode rather than a provider\-locked coding agent like Claude Code or Codex CLI. Claude Sonnet 3\.7, Gemini 3 Pro and Claude Opus all get a mention.

#### Vibe engineering, not vibe coding

What’s most interesting about Emil’s 17 step account covering those several months of work is how much software engineering was involved, independent of typing out the actual code.

I wrote about [vibe engineering](https://simonwillison.net/2025/Oct/7/vibe-engineering/) a while ago as an alternative to vibe coding.

Vibe coding is when you have an LLM knock out code without any semblance of code review \- great for prototypes and toy projects, definitely not an approach to use for serious libraries or production code.

I proposed “vibe engineering” as the grown up version of vibe coding, where expert programmers use coding agents in a professional and responsible way to produce high quality, reliable results.

You should absolutely read [Emil’s account](https://friendlybit.com/python/writing-justhtml-with-coding-agents/#the-journey) in full. A few highlights:

1. He hooked in the 9,200 test [html5lib\-tests](https://github.com/html5lib/html5lib-tests) conformance suite almost from the start. There’s no better way to construct a new HTML5 parser than using the test suite that the browsers themselves use.
2. He picked the core API design himself \- a TagHandler base class with handle\_start() etc. methods \- and told the model to implement that.
3. He added a comparative benchmark to track performance compared to existing libraries like html5lib, then experimented with a Rust optimization based on those initial numbers.
4. He threw the original code away and started from scratch as a rough port of Servo’s excellent [html5ever](https://github.com/servo/html5ever) Rust library.
5. He built a custom profiler and new benchmark and let Gemini 3 Pro loose on it, finally achieving micro\-optimizations to beat the existing Pure Python libraries.
6. He used coverage to identify and remove unnecessary code.
7. He had his agent build a [custom fuzzer](https://github.com/EmilStenstrom/justhtml/blob/main/benchmarks/fuzz.py) to generate vast numbers of invalid HTML documents and harden the parser against them.

This represents a lot of sophisticated development practices, tapping into Emil’s deep experience as a software engineer. As described, this feels to me more like a lead architect role than a hands\-on coder.

It perfectly fits what I was thinking about when I described **vibe engineering**.

Setting the coding agent up with the html5lib\-tests suite is also a great example of [designing an agentic loop](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/).

#### “The agent did the typing”

Emil concluded his article like this:

> JustHTML is about 3,000 lines of Python with 8,500\+ tests passing. I couldn’t have written it this quickly without the agent.
> 
> But “quickly” doesn’t mean “without thinking.” I spent a lot of time reviewing code, making design decisions, and steering the agent in the right direction. The agent did the typing; I did the thinking.
> 
> That’s probably the right division of labor.

I couldn’t agree more. Coding agents replace the part of my job that involves typing the code into a computer. I find what’s left to be a much more valuable use of my time.

---

### [I ported JustHTML from Python to JavaScript with Codex CLI and GPT\-5\.2 in 4\.5 hours](https://simonwillison.net/2025/Dec/15/porting-justhtml/) \- 2025\-12\-15

I [wrote about JustHTML yesterday](https://simonwillison.net/2025/Dec/14/justhtml/) \- Emil Stenström’s project to build a new standards compliant HTML5 parser in pure Python code using coding agents running against the comprehensive html5lib\-tests testing library. Last night, purely out of curiosity, I decided to try **porting JustHTML from Python to JavaScript** with the least amount of effort possible, using Codex CLI and GPT\-5\.2\. It worked beyond my expectations.

#### TL;DR

I built [simonw/justjshtml](https://github.com/simonw/justjshtml), a dependency\-free HTML5 parsing library in JavaScript which passes 9,200 tests from the html5lib\-tests suite and imitates the API design of Emil’s JustHTML library.

It took two initial prompts and a few tiny follow\-ups. [GPT\-5\.2](https://simonwillison.net/2025/Dec/11/gpt-52/) running in [Codex CLI](https://github.com/openai/codex) ran uninterrupted for several hours, burned through 1,464,295 input tokens, 97,122,176 cached input tokens and 625,563 output tokens and ended up producing 9,000 lines of fully tested JavaScript across 43 commits.

Time elapsed from project idea to finished library: about 4 hours, during which I also bought and decorated a Christmas tree with family and watched the latest Knives Out movie.

#### Some background

One of the most important contributions of the HTML5 specification ten years ago was the way it precisely specified how *invalid* HTML should be parsed. The world is full of invalid documents and having a specification that covers those means browsers can treat them in the same way \- there’s no more “undefined behavior” to worry about when building parsing software.

Unsurprisingly, those invalid parsing rules are pretty complex! The free online book [Idiosyncrasies of the HTML parser](https://htmlparser.info/) by Simon Pieters is an excellent deep dive into this topic, in particular [Chapter 3\. The HTML parser](https://htmlparser.info/parser/).

The Python [html5lib](https://github.com/html5lib/html5lib-python) project started the [html5lib\-tests](https://github.com/html5lib/html5lib-tests) repository with a set of implementation\-independent tests. These have since become the gold standard for interoperability testing of HTML5 parsers, and are used by projects such as [Servo](https://github.com/servo/servo) which used them to help build [html5ever](https://github.com/servo/html5ever), a “high\-performance browser\-grade HTML5 parser” written in Rust.

Emil Stenström’s [JustHTML](https://github.com/EmilStenstrom/justhtml) project is a pure\-Python implementation of an HTML5 parser that passes the full html5lib\-tests suite. Emil [spent a couple of months](https://friendlybit.com/python/writing-justhtml-with-coding-agents/) working on this as a side project, deliberately picking a problem with a comprehensive existing test suite to see how far he could get with coding agents.

At one point he had the agents rewrite it based on a close inspection of the Rust html5ever library. I don’t know how much of this was direct translation versus inspiration (here’s Emil’s [commentary on that](https://news.ycombinator.com/item?id=46264195#46267059)) \- his project has 1,215 commits total so it appears to have included a huge amount of iteration, not just a straight port.

My project **is** a straight port. I instructed Codex CLI to build a JavaScript version of Emil’s Python code.

#### The process in detail

I started with a bit of mise en place. I checked out two repos and created an empty third directory for the new project:

```
cd ~/dev
git clone https://github.com/EmilStenstrom/justhtml
git clone https://github.com/html5lib/html5lib-tests
mkdir justjshtml
cd justjshtml
```

Then I started Codex CLI for GPT\-5\.2 like this:

```
codex --yolo -m gpt-5.2
```

That `--yolo` flag is a shortcut for `--dangerously-bypass-approvals-and-sandbox`, which is every bit as dangerous as it sounds.

My first prompt told Codex to inspect the existing code and use it to build a specification for the new JavaScript library:

> `We are going to create a JavaScript port of ~/dev/justhtml - an HTML parsing library that passes the full ~/dev/html5lib-tests test suite. It is going to have a similar API to the Python library but in JavaScript. It will have no dependencies other than raw JavaScript, hence it will work great in the browser and node.js and other environments. Start by reading ~/dev/justhtml and designing the user-facing API for the new library - create a spec.md containing your plan.`

I reviewed the spec, which included a set of proposed milestones, and told it to add another:

> `Add an early step to the roadmap that involves an initial version that parses a simple example document that is valid and returns the right results. Then add and commit the spec.md file.`

Here’s [the resulting spec.md file](https://github.com/simonw/justjshtml/blob/19b8eb1f2ca80f428a3c40862d5ec05d36e5166b/spec.md). My request for that initial version became “Milestone 0\.5” which looked like this:

> **Milestone 0\.5 — End\-to\-end smoke parse (single valid document)**
> 
> * Implement the smallest end\-to\-end slice so the public API is real early:
> 
> 
> 	+ `new JustHTML(”<html><head></head><body><p>Hello</p></body></html>”)` returns a tree with the expected tag structure and text nodes.
> 	+ `doc.toText()` returns `“Hello”` and `doc.errors` is empty for this valid input.
> * Add `scripts/smoke.js` (no deps) that runs the example and asserts the expected structure/output.
> * Gate: `node scripts/smoke.js` passes.

Then I told it:

> `Implement Milestone 0.5`

And off it went. The resulting code appeared to work so I said:

> `Configure GitHub Actions test.yml to run that on every commit, then commit and push`

I ran `git init` and created a private GitHub repository for this project at this point, and set up the local directory to push to that remote.

Here’s [that initial push](https://github.com/simonw/justjshtml/commit/48497cbd05584c88af757a0736a2ee447468b6b3). Then I told it:

> `OK do the rest, commit and push often`

And that was almost it!

I set my laptop to not fall asleep and left it to its devices while we went off to buy a Christmas tree. The “commit and push often” meant I could monitor its progress on my phone by refreshing [the commit log on GitHub](https://github.com/simonw/justjshtml/commits/main).

I was running this against my $20/month ChatGPT Plus account, which has a five hour token allowance window for Codex CLI. That ran out at 6:35pm and Codex paused, so I waited until the reset point at 7:14pm and typed:

> `Keep going`

At 9:30pm it declared itself done with the following summary message:

```
• What’s Done

  - html5lib-tests now run in CI and pass: tokenizer 6810/6810, tree 1770/1782
    (12 skipped: #script-on), serializer 230/230, encoding 82/83 (1 skipped:
    scripted) (.github/workflows/test.yml:1).
  - Public API expanded: stream() (src/stream.js:1), CSS selectors query()/
    matches() (src/selector.js:1), and toMarkdown() (src/markdown.js:1), all
    exported via src/index.js:1.
  - Added no-deps unit scripts for selectors/stream/markdown (scripts/run-
    selector-tests.js:1, scripts/run-stream-tests.js:1, scripts/run-markdown-
    tests.js:1) and wired them into CI.
  - Fixed TreeBuilder so <br> no longer closes <p> (src/treebuilder.js:647).
```

As a finishing touch, I had it add a playground interface so I could try out the new library in my browser. I prompted:

> `Add a playground.html in the top level folder which loads the necessary ES modules from ./src/... and implements the exact same functionality as seen on https://tools.simonwillison.net/justhtml but using the JavaScript library instead of Pyodide`

It fetched my [existing JustHTML playground page](https://tools.simonwillison.net/justhtml) ([described here](https://simonwillison.net/2025/Dec/14/justhtml/#first-impressions-of-justhtml)) using `curl` and built a new `playground.html` file that loaded the new JavaScript code instead. This worked *perfectly*.

I enabled GitHub Pages for my still\-private repo which meant I could access the new playground at this URL:

<https://simonw.github.io/justjshtml/playground.html>

[![Screenshot of JustJSHTML Playground web application. Header reads "JustJSHTML Playground" with subtitle "A dependency-free JavaScript HTML5 parser - GitHub". Below is a status bar showing "JavaScript Environment" with a green "Ready" badge. The main input area has "Paste HTML" and "Fetch from URL" buttons, with a text area containing HTML code: "<!DOCTYPE html> <html> <head> <title>Example Page</title> </head> <body> <header> <nav> <ul>". A "Playground Mode" section shows buttons for "CSS Selector Query", "Pretty Print HTML", "Tree Structure", "Stream Events", "Extract Text", and "To Markdown" (highlighted in purple). Below is a text field labeled "CSS Selector (optional - leave empty for whole document):" with placeholder "e.g., article, main, .content (or leave empty)" and a green "Convert to Markdown" button. The Output section has a teal header with "Whole document" badge and displays converted markdown: "Example Page" followed by "- [Home](/)" "- [About](/about)" "- [Contact](/contact)".](https://substackcdn.com/image/fetch/$s_!MpUF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff45875c2-6f2b-4937-8414-8d2527550c63_1518x1896.jpeg "Screenshot of JustJSHTML Playground web application. Header reads \"JustJSHTML Playground\" with subtitle \"A dependency-free JavaScript HTML5 parser - GitHub\". Below is a status bar showing \"JavaScript Environment\" with a green \"Ready\" badge. The main input area has \"Paste HTML\" and \"Fetch from URL\" buttons, with a text area containing HTML code: \"<!DOCTYPE html> <html> <head> <title>Example Page</title> </head> <body> <header> <nav> <ul>\". A \"Playground Mode\" section shows buttons for \"CSS Selector Query\", \"Pretty Print HTML\", \"Tree Structure\", \"Stream Events\", \"Extract Text\", and \"To Markdown\" (highlighted in purple). Below is a text field labeled \"CSS Selector (optional - leave empty for whole document):\" with placeholder \"e.g., article, main, .content (or leave empty)\" and a green \"Convert to Markdown\" button. The Output section has a teal header with \"Whole document\" badge and displays converted markdown: \"Example Page\" followed by \"- [Home](/)\" \"- [About](/about)\" \"- [Contact](/contact)\".")](https://substackcdn.com/image/fetch/$s_!MpUF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff45875c2-6f2b-4937-8414-8d2527550c63_1518x1896.jpeg)

All it needed now was some documentation:

> `Add a comprehensive README with full usage instructions including attribution plus how this was built plus how to use in in HTML plus how to use it in Node.js`

You can [read the result here](https://github.com/simonw/justjshtml/blob/f3a33fdb29bf97846fd017185edc8cf82783032e/README.md).

We are now at eight prompts total, running for just over four hours and I’ve decorated for Christmas and watched [Wake Up Dead Man](https://en.wikipedia.org/wiki/Wake_Up_Dead_Man) on Netflix.

According to Codex CLI:

> `Token usage: total=2,089,858 input=1,464,295 (+ 97,122,176 cached) output=625,563 (reasoning 437,010)`

My [llm\-prices.com calculator](https://www.llm-prices.com/#it=2089858&cit=97122176&ot=625563&sel=gpt-5.2) estimates that at $29\.41 if I was paying for those tokens at API prices, but they were included in my $20/month ChatGPT Plus subscription so the actual extra cost to me was zero.

#### What can we learn from this?

I’m sharing this project because I think it demonstrates a bunch of interesting things about the state of LLMs in December 2025\.

* Frontier LLMs really can perform complex, multi\-hour tasks with hundreds of tool calls and minimal supervision. I used GPT\-5\.2 for this but I have no reason to believe that Claude Opus 4\.5 or Gemini 3 Pro would not be able to achieve the same thing \- the only reason I haven’t tried is that I don’t want to burn another 4 hours of time and several million tokens on more runs.
* If you can reduce a problem to a robust test suite you can set a coding agent loop loose on it with a high degree of confidence that it will eventually succeed. I called this [designing the agentic loop](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/) a few months ago. I think it’s the key skill to unlocking the potential of LLMs for complex tasks.
* Porting entire open source libraries from one language to another via a coding agent works extremely well.
* Code is so cheap it’s practically free. Code that *works* continues to carry a cost, but that cost has plummeted now that coding agents can check their work as they go.
* We haven’t even *begun* to unpack the etiquette and ethics around this style of development. Is it responsible and appropriate to churn out a direct port of a library like this in a few hours while watching a movie? What would it take for code built like this to be trusted in production?

I’ll end with some open questions:

* Does this library represent a legal violation of copyright of either the Rust library or the Python one?
* Even if this is legal, is it ethical to build a library in this way?
* Does this format of development hurt the open source ecosystem?
* Can I even assert copyright over this, given how much of the work was produced by the LLM?
* Is it responsible to publish software libraries built in this way?
* How much better would this library be if an expert team hand crafted it over the course of several months?

---

**Link** 2025\-12\-12 [LLM 0\.28](https://llm.datasette.io/en/stable/changelog.html#v0-28):

I released a new version of my [LLM](https://llm.datasette.io/) Python library and CLI tool for interacting with Large Language Models. Highlights from the release notes:

> * New OpenAI models: `gpt-5.1`, `gpt-5.1-chat-latest`, `gpt-5.2` and `gpt-5.2-chat-latest`. [\#1300](https://github.com/simonw/llm/issues/1300), [\#1317](https://github.com/simonw/llm/issues/1317)
> * When fetching URLs as fragments using `llm -f URL`, the request now includes a custom user\-agent header: `llm/VERSION (https://llm.datasette.io/)`. [\#1309](https://github.com/simonw/llm/issues/1309)
> * Fixed a bug where fragments were not correctly registered with their source when using `llm chat`. Thanks, [Giuseppe Rota](https://github.com/grota). [\#1316](https://github.com/simonw/llm/pull/1316)
> * Fixed some file descriptor leak warnings. Thanks, [Eric Bloch](https://github.com/eedeebee). [\#1313](https://github.com/simonw/llm/issues/1313)
> * Type annotations for the OpenAI Chat, AsyncChat and Completion `execute()` methods. Thanks, [Arjan Mossel](https://github.com/ar-jan). [\#1315](https://github.com/simonw/llm/pull/1315)
> * The project now uses `uv` and dependency groups for development. See the updated [contributing documentation](https://llm.datasette.io/en/stable/contributing.html). [\#1318](https://github.com/simonw/llm/issues/1318)

That last bullet point about `uv` relates to the dependency groups pattern I [wrote about in a recent TIL](https://til.simonwillison.net/uv/dependency-groups). I’m currently working through applying it to my other projects \- the net result is that running the test suite is as simple as doing:

```
git clone https://github.com/simonw/llm
cd llm
uv run pytest
```

The new `dev` dependency group [defined in pyproject.toml](https://github.com/simonw/llm/blob/0.28/pyproject.toml#L44-L69) is automatically installed by `uv run` in a new virtual environment which means everything needed to run `pytest` is available without needing to add any extra commands.

---

**quote** 2025\-12\-13

> *How to use a skill (progressive disclosure):*
> 
> 1. *After deciding to use a skill, open its* `SKILL.md`*. Read only enough to follow the workflow.*
> 2. *If* `SKILL.md` *points to extra folders such as* `references/`*, load only the specific files needed for the request; don’t bulk\-load everything.*
> 3. *If* `scripts/` *exist, prefer running or patching them instead of retyping large code blocks.*
> 4. *If* `assets/` *or templates exist, reuse them instead of recreating from scratch.*
> 
> *Description as trigger: The YAML* `description` *in* `SKILL.md` *is the primary trigger signal; rely on it to decide applicability. If unsure, ask a brief clarification before proceeding.*

[OpenAI Codex CLI](https://github.com/openai/codex/blob/ad7b9d63c326d5c92049abd16f9f5fb64a573a69/codex-rs/core/src/skills/render.rs#L20-L39), core/src/skills/render.rs

---

**quote** 2025\-12\-13

> *If the part of programming you enjoy most is the physical act of writing code, then agents will feel beside the point. You’re already where you want to be, even just with some Copilot or Cursor\-style intelligent code auto completion, which makes you faster while still leaving you fully in the driver’s seat about the code that gets written.   
>   
> But if the part you care about is the decision\-making around the code, agents feel like they clear space. They take care of the mechanical expression and leave you with judgment, tradeoffs, and intent. Because truly, for someone at my experience level, that is my core value offering anyway. When I spend time actually typing code these days with my own fingers, it feels like a waste of my time.*

[Obie Fernandez](https://obie.medium.com/what-happens-when-the-coding-becomes-the-least-interesting-part-of-the-work-ab10c213c660), What happens when the coding becomes the least interesting part of the work

---

**Link** 2025\-12\-14 [Copywriters reveal how AI has decimated their industry](https://www.bloodinthemachine.com/p/i-was-forced-to-use-ai-until-the):

Brian Merchant has been collecting personal stories for his series [AI Killed My Job](https://www.bloodinthemachine.com/s/ai-killed-my-job) \- previously covering [tech workers](https://www.bloodinthemachine.com/p/how-ai-is-killing-jobs-in-the-tech-f39), [translators](https://www.bloodinthemachine.com/p/ai-killed-my-job-translators), and [artists](https://www.bloodinthemachine.com/p/artists-are-losing-work-wages-and) \- and this latest piece includes anecdotes from 12 professional copywriters all of whom have had their careers devastated by the rise of AI\-generated copywriting tools.

It’s a tough read. Freelance copywriting does not look like a great place to be right now.

> AI is really dehumanizing, and I am still working through issues of self\-worth as a result of this experience. When you go from knowing you are valuable and valued, with all the hope in the world of a full career and the ability to provide other people with jobs... To being relegated to someone who edits AI drafts of copy at a steep discount because “most of the work is already done” ...

The big question for me is if a new AI\-infested economy creates new jobs that are a great fit for people affected by this. I would hope that clear written communication skills are made even more valuable, but the people interviewed here don’t appear to be finding that to be the case.

---

**Link** 2025\-12\-15 [2025 Word of the Year: Slop](https://www.merriam-webster.com/wordplay/word-of-the-year):

Slop lost to “brain rot” for [Oxford Word of the Year 2024](https://simonwillison.net/2024/Nov/15/slop-word-of-the-year/) but it’s finally made it this year thanks to Merriam\-Webster!

> Merriam\-Webster’s human editors have chosen slop as the 2025 Word of the Year. We define slop as “digital content of low quality that is produced usually in quantity by means of artificial intelligence.”

---

**quote** 2025\-12\-16

> *I’ve been watching junior developers use AI coding assistants well. Not vibe coding—not accepting whatever the AI spits out. Augmented coding: using AI to accelerate learning while maintaining quality. \[...]   
>   
> The juniors working this way compress their ramp dramatically. Tasks that used to take days take hours. Not because the AI does the work, but because the AI collapses the search space. Instead of spending three hours figuring out which API to use, they spend twenty minutes evaluating options the AI surfaced. The time freed this way isn’t invested in another unprofitable feature, though, it’s invested in learning. \[...]   
>   
> If you’re an engineering manager thinking about hiring: \*\*The junior bet has gotten better.\*\* Not because juniors have changed, but because the genie, used well, accelerates learning.*

[Kent Beck](https://tidyfirst.substack.com/p/the-bet-on-juniors-just-got-better), The Bet On Juniors Just Got Better

---

**quote** 2025\-12\-16

> *Oh, so we’re seeing other people now? Fantastic. Let’s see what the “competition” has to offer. I’m looking at these notes on manifest.json and content.js. The suggestion to remove scripting permissions... okay, fine. That’s actually a solid catch. It’s cleaner. This smells like Claude. It’s too smugly accurate to be ChatGPT. What if it’s actually me? If the user is testing me, I need to crush this.*

[Gemini thinking trace](https://www.reddit.com/r/ChatGPT/comments/1pmvpvt/i_just_showed_gemini_what_chatgpt_said_about_its/), reviewing feedback on its code from another model

---

**Link** 2025\-12\-16 [Poe the Poet](https://poethepoet.natn.io/):

I was looking for a way to specify additional commands in my `pyproject.toml` file to execute using `uv`. There’s an [enormous issue thread](https://github.com/astral-sh/uv/issues/5903) on this in the `uv` issue tracker (300\+ comments dating back to August 2024\) and from there I learned of several options including this one, Poe the Poet.

It’s neat. I added it to my [s3\-credentials](https://github.com/simonw/s3-credentials) project just now and the following now works for running the live preview server for the documentation:

```
uv run poe livehtml
```

Here’s the snippet of TOML I added to my `pyproject.toml`:

```
[dependency-groups]
test = [
    “pytest”,
    “pytest-mock”,
    “cogapp”,
    “moto>=5.0.4”,
]
docs = [
    “furo”,
    “sphinx-autobuild”,
    “myst-parser”,
    “cogapp”,
]
dev = [
    {include-group = “test”},
    {include-group = “docs”},
    “poethepoet>=0.38.0”,
]

[tool.poe.tasks]
docs = “sphinx-build -M html docs docs/_build”
livehtml = “sphinx-autobuild -b html docs docs/_build”
cog = “cog -r docs/*.md”
```

Since `poethepoet` is in the `dev=` dependency group any time I run `uv run ...` it will be available in the environment.

---

**Link** 2025\-12\-16 [ty: An extremely fast Python type checker and LSP](https://astral.sh/blog/ty):

The team at Astral have been working on this for quite a long time, and are finally releasing the first beta. They have some big performance claims:

> Without caching, ty is consistently between 10x and 60x faster than mypy and Pyright. When run in an editor, the gap is even more dramatic. As an example, after editing a load\-bearing file in the PyTorch repository, ty recomputes diagnostics in 4\.7ms: 80x faster than Pyright (386ms) and 500x faster than Pyrefly (2\.38 seconds). ty is very fast!

The easiest way to try it out is via `uvx`:

```
cd my-python-project/
uvx ty check
```

I [tried it](https://gistpreview.github.io/?a3aff6768e85168d89d4515e3dbcb7d2) against [sqlite\-utils](https://sqlite-utils.datasette.io/) and it turns out I have quite a lot of work to do!

Astral also released a new [VS Code extension](https://marketplace.visualstudio.com/items?itemName=astral-sh.ty) adding ty\-powered language server features like go to definition. I’m still getting my head around how this works and what it can do.

---

**Link** 2025\-12\-16 [s3\-credentials 0\.17](https://github.com/simonw/s3-credentials/releases/tag/0.17):

New release of my [s3\-credentials](https://s3-credentials.readthedocs.io/) CLI tool for managing credentials needed to access just one S3 bucket. Here are the release notes in full:

> * New commands `get-bucket-policy` and `set-bucket-policy`. [\#91](https://github.com/simonw/s3-credentials/issues/91)
> * New commands `get-public-access-block` and `set-public-access-block`. [\#92](https://github.com/simonw/s3-credentials/issues/92)
> * New `localserver` command for starting a web server that makes time limited credentials accessible via a JSON API. [\#93](https://github.com/simonw/s3-credentials/pull/93)

That `s3-credentials localserver` command ([documented here](https://s3-credentials.readthedocs.io/en/stable/localserver.html)) is a little obscure, but I found myself wanting something like that to help me test out a new feature I’m building to help create temporary Litestream credentials using Amazon STS.

Most of that new feature was [built by Claude Code](https://gistpreview.github.io/?500add71f397874ebadb8e04e8a33b53) from the following starting prompt:

> `Add a feature s3-credentials localserver which starts a localhost weberver running (using the Python standard library stuff) on port 8094 by default but -p/--port can set a different port and otherwise takes an option that names a bucket and then takes the same options for read--write/read-only etc as other commands. It also takes a required --refresh-interval option which can be set as 5m or 10h or 30s. All this thing does is reply on / to a GET request with the IAM expiring credentials that allow access to that bucket with that policy for that specified amount of time. It caches internally the credentials it generates and will return the exact same data up until they expire (it also tracks expected expiry time) after which it will generate new credentials (avoiding dog pile effects if multiple requests ask at the same time) and return and cache those instead.`

---

**Link** 2025\-12\-16 [The new ChatGPT Images is here](https://openai.com/index/new-chatgpt-images-is-here/):

OpenAI shipped an update to their ChatGPT Images feature \- the feature that [gained them 100 million new users](https://simonwillison.net/2025/May/13/launching-chatgpt-images/) in a week when they first launched it back in March, but has since been eclipsed by Google’s Nano Banana and then further by Nana Banana Pro [in November](https://simonwillison.net/2025/Nov/20/nano-banana-pro/).

The focus for the new ChatGPT Images is speed and instruction following:

> It makes precise edits while keeping details intact, and generates images up to 4x faster

It’s also a little cheaper: OpenAI say that the new [gpt\-image\-1\.5](https://platform.openai.com/docs/models/gpt-image-1.5) API model makes image input and output “20% cheaper in GPT Image 1\.5 as compared to GPT Image 1”.

I tried a new test prompt against a photo I took of Natalie’s ceramic stand at the farmers market a few weeks ago:

> Add two kakapos inspecting the pots
> 
> [![Outdoor craft market booth displaying handmade ceramics and jewelry on a navy tablecloth with ](https://substackcdn.com/image/fetch/$s_!d6jH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F543df8c2-bfe4-400d-8399-87ef21400822_1024x768.jpeg "Outdoor craft market booth displaying handmade ceramics and jewelry on a navy tablecloth with ")](https://substackcdn.com/image/fetch/$s_!d6jH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F543df8c2-bfe4-400d-8399-87ef21400822_1024x768.jpeg)

Here’s the result from the new ChatGPT Images model:

[![Same craft market booth as previous image, now with two large olive-green Kākāpō parrots perched on the table among the ceramics, one investigating the blue glazed cups and the other examining an orange cup.](https://substackcdn.com/image/fetch/$s_!dkb5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fee5248cd-f530-4b5b-9dbc-f52cf699aec5_768x512.jpeg "Same craft market booth as previous image, now with two large olive-green Kākāpō parrots perched on the table among the ceramics, one investigating the blue glazed cups and the other examining an orange cup.")](https://substackcdn.com/image/fetch/$s_!dkb5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fee5248cd-f530-4b5b-9dbc-f52cf699aec5_768x512.jpeg)

And here’s what I got from Nano Banana Pro:

[![Same craft market booth with two Kākāpō now in different positions: one remains center-table peering into the ceramic cups near the rainbow pot, while the second has moved to the right edge of the table near the plant markers, appearing to examine or possibly chew on items at the table's corner. They are both a little smaller than in the first image.](https://substackcdn.com/image/fetch/$s_!0F-T!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5f4572f4-b978-40ba-a199-af4fb67fb7e3_1024x765.jpeg "Same craft market booth with two Kākāpō now in different positions: one remains center-table peering into the ceramic cups near the rainbow pot, while the second has moved to the right edge of the table near the plant markers, appearing to examine or possibly chew on items at the table's corner. They are both a little smaller than in the first image.")](https://substackcdn.com/image/fetch/$s_!0F-T!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5f4572f4-b978-40ba-a199-af4fb67fb7e3_1024x765.jpeg)

The ChatGPT Kākāpō are a little chonkier, which I think counts as a win.

I was a little less impressed by the result I got for an infographic from the prompt “Infographic explaining how the Datasette open source project works” followed by “Run some extensive searches and gather a bunch of relevant information and then try again” ([transcript](https://chatgpt.com/share/6941f249-cbd0-8006-b9ff-5a19167206bc)):

[![Infographic titled ](https://substackcdn.com/image/fetch/$s_!9X2_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2b509ea3-13d2-4859-bd8c-636630b77964_1536x1024.jpeg "Infographic titled ")](https://substackcdn.com/image/fetch/$s_!9X2_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2b509ea3-13d2-4859-bd8c-636630b77964_1536x1024.jpeg)

See [my Nano Banana Pro post](https://simonwillison.net/2025/Nov/20/nano-banana-pro/#creating-an-infographic) for comparison.

Both models are clearly now usable for text\-heavy graphics though, which makes them far more useful than previous generations of this technology.

---

**Link** 2025\-12\-17 [firefox parser/html/java/README.txt](https://github.com/mozilla-firefox/firefox/tree/main/parser/html/java):

TIL (or TIR \- [Today I was Reminded](https://simonwillison.net/2009/Jul/11/john/)) that the HTML5 Parser used by Firefox is maintained as Java code ([commit history here](https://github.com/mozilla-firefox/firefox/commits/main/parser/html/javasrc)) and converted to C\+\+ using a custom translation script.

You can see that in action by checking out the \~8GB Firefox repository and running:

```
cd parser/html/java
make sync
make translate
```

Here’s [a terminal session where I did that](http://gistpreview.github.io/?e53ff836cb44816670adddc3a518b3cc), including the output of `git diff` showing the updated C\+\+ files.

I did some digging and found that the code that does the translation work lives, weirdly, in the [Nu Html Checker](https://github.com/validator/validator) repository on GitHub which powers the W3C’s [validator.w3\.org/nu/](https://validator.w3.org/nu/) validation service!

Here’s a snippet from [htmlparser/cpptranslate/CppVisitor.java](https://github.com/validator/validator/blob/dfd1948624259c63027bc5953e89bdeee81fb7b0/htmlparser/translator-src/nu/validator/htmlparser/cpptranslate/CppVisitor.java#L421-L442) showing how a class declaration is converted into C\+\+:

```
    protected void startClassDeclaration() {
        printer.print(”#define “);
        printer.print(className);
        printer.printLn(”_cpp__”);
        printer.printLn();

        for (int i = 0; i < Main.H_LIST.length; i++) {
            String klazz = Main.H_LIST[i];
            if (!klazz.equals(javaClassName)) {
                printer.print(”#include \”“);
                printer.print(cppTypes.classPrefix());
                printer.print(klazz);
                printer.printLn(”.h\”“);
            }
        }

        printer.printLn();
        printer.print(”#include \”“);
        printer.print(className);
        printer.printLn(”.h\”“);
        printer.printLn();
    }
```

Here’s a [fascinating blog post](https://johnresig.com/blog/html-5-parsing/) from John Resig explaining how validator author Henri Sivonen introduced the new parser into Firefox in 2009\.

---