# Phoenix.new is Fly's entry into the prompt-driven app development space

*Plus exploring the system prompts for Gemini CLI and Claude AI artifacts*

Published: 2025-06-26
Source: https://simonw.substack.com/p/phoenixnew-is-flys-entry-into-the

---

In this newsletter:

* Phoenix.new is Fly's entry into the prompt\-driven app development space

Plus 6 links and 3 quotations and 1 TIL and 1 note

### **[Phoenix.new is Fly's entry into the prompt\-driven app development space](https://simonwillison.net/2025/Jun/23/phoenix-new/) \- 2025\-06\-23**

Here's a fascinating new entrant into the AI\-assisted\-programming / coding\-agents space by [Fly.io](https://fly.io/), introduced on their blog in [Phoenix.new – The Remote AI Runtime for Phoenix](https://fly.io/blog/phoenix-new-the-remote-ai-runtime/): describe an app in a prompt, get a full Phoenix application, backed by SQLite and running on Fly's hosting platform. The [official Phoenix.new YouTube launch video](https://www.youtube.com/watch?v=du7GmWGUM5Y) is a good way to get a sense for what this does.

#### **Background on Phoenix and Elixir and Fly**

First, some background. [Phoenix](https://www.phoenixframework.org/) is an open source web framework for Elixir, the Ruby\-like language that compiles to Erlang's BEAM bytecode and runs on top of the highly concurrent Erlang runtime. The signature feature of the framework is [Phoenix LiveView](https://github.com/phoenixframework/phoenix_live_view/blob/main/README.md#feature-highlights), a toolkit for building realtime interfaces through streaming diffs to server\-side HTML over a WebSocket connection.

Phoenix was created by Chris McCord 11 years ago, and Chris joined Fly nearly four years ago. [Phoenix.new](http://phoenix.new/) is his latest project.

Phoenix LiveView is a really great fit for Fly's geographically distributed application serving infrastructure. Fly co\-founder Kurt Mackey [wrote about that](https://fly.io/blog/low-latency-liveview/) in April 2021, before they had hired Chris, describing how LiveView benefits from low latency by "moving app processes close to users" \- something Fly has been designed to help with from the start.

There's one major challenge though: Elixir is still a niche programming language, which means the number of people out there who are ready to spin up a new Phoenix app has always been artificially limited.

Fly's solution? Get LLMs to shave that learning curve down to *almost nothing*.

#### **Prompt\-driven application development with Phoenix.new**

Phoenix.new is a prompt\-driven application development platform. You describe what you want to build, then watch as an LLM\-powered coding agent writes, tests and iterates on code to help achieve that goal. It's in the same broad category as [Lovable](https://lovable.dev/), [v0\.dev](https://v0.dev/) and and [Val Town's Townie](https://townie.val.run/).

One of the most important problems to solve with coding agents is to give them a robust sandbox where they can run code without breaking things outside of that space. Fly, at their heart, are a sandboxing company \- their [Fly Machines](https://fly.io/docs/machines/)product makes it trivial to spin up a new sandboxed VM in just a few seconds. I'm building [Datasette Cloud](https://www.datasette.cloud/) on Fly for exactly that reason.

I tried out Phoenix.new with the following starter prompt:

> `A notebook application. Notes are rich text, using a nice visual markdown editors. The first line of a note becomes the title. Notes have a URL that is a 6 character random text string - thise can be used to link notes to each other by dropping in an @ sign and that text string. A hash and then text becomes a tag, clicking a tag goes to a page with that tag on. Notes are all in SQLite FTS so they can be searched with a search tool.`

Watching it work was *fascinating*. It provides a full IDE\-style environment in the browser, running a dedicated container and with a forwarded port to allow you to interact with the running application *while it is being built*.

[![Browser IDE interface showing a notebook app development project with a left sidebar containing a chat session that starts "What would you like to build?" with options like "todo list", "chat app", "product landing page", then a main editor displaying plan.md file with detailed development steps including "Generate a Phoenix LiveView project called 'notebook'" and "Start the server so you can view the app as we build it". The bottom has a terminal showing "All dependencies are up to date", "Generated notebook app", "Done in 241ms".](https://substackcdn.com/image/fetch/$s_!FL21!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa73d928c-ca20-491d-bde3-9a98012d2e3a_2902x1754.jpeg "Browser IDE interface showing a notebook app development project with a left sidebar containing a chat session that starts \"What would you like to build?\" with options like \"todo list\", \"chat app\", \"product landing page\", then a main editor displaying plan.md file with detailed development steps including \"Generate a Phoenix LiveView project called 'notebook'\" and \"Start the server so you can view the app as we build it\". The bottom has a terminal showing \"All dependencies are up to date\", \"Generated notebook app\", \"Done in 241ms\".")](https://substackcdn.com/image/fetch/$s_!FL21!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa73d928c-ca20-491d-bde3-9a98012d2e3a_2902x1754.jpeg)

It spun up a `plan.md`, planned out the approach and started working through the code. Most interestingly, it constantly tested the application it was building using a testing tool that looked similar to my own [shot\-scraper](https://shot-scraper.datasette.io/). Here's an example of the output from that:

> I can see the issue! The page is still showing the "Welcome to your Notebook" message instead of the form. Let me wait a moment for the JavaScript to execute and then check if the form appeared.
> 
> `$ web http://localhost:4000 --js "setTimeout(() => { document.querySelector('button[phx-click=\"start_creating\"]').click(); }, 500); setTimeout(() => { console.log('Form visible?', !!document.querySelector('textarea')); console.log('Creating note state:', document.body.innerHTML.includes('Create New Note')); }, 2000);"`

I'm used to coding agents that write and execute their own tests, but this is the most impressive example I've seen of a coding agent that actively interacts with and tests the live application while it is iterating on the code.

Most interestingly of all, since LiveView is a realtime framework, I could interact directly with the application at the same time as the machine was writing and testing it, seeing any changes it made instantly in my browser!

How did it do? It got there in the end, but with hindsight my initial prompt was a little too complex: I had to rescue it after it got stuck in an error loop trying to implement SQLite full\-text search. Just like a project you build yourself it turns out to work much better if you start with the simplest possible version of the application and then iterate on it to add additional features.

One of my favorite details is how Git integration works. Phoenix.new commits constantly as it works, and a menu option for "Clone X to your local computer" then gives you a command that looks like this:

`git clone "https://phoenix.new/git/WENQLj...big-random-string...VHFW/$RANDOM/notebook"`

Run that locally to get a full copy of the repo! I ran the following to push it to a new repository in my GitHub account:

```
git remote add github https://github.com/simonw/phoenix-new-notebook.git
git push -u github main
```

You can see the code (and the [commit history](https://github.com/simonw/phoenix-new-notebook/commits)) in my [simonw/phoenix\-new\-notebook](https://github.com/simonw/phoenix-new-notebook) repo.

#### **How much did I learn?**

My initial experiments with Phoenix.new were very much [vibe coding](https://simonwillison.net/2025/Mar/19/vibe-coding/) \- I interacted with the resulting application but didn't pay a great deal of attention to the code that was being written, despite it being presented to me in an IDE that made it very easy to review what was going on.

As a result, I didn't learn much about the low\-level syntax details of how Phoenix and Elixir work. I did however get a strong feel for the *shape*of Elixir and Phoenix at a high level as the code danced past my eye.

It turns out having an LLM write an application in front of you is a great way to start building understanding of what a framework can do.

It’s almost like watching a YouTube livestream of an experienced developer speed running building an application, except that app is exactly what you asked them to build and you can interject and send them in a new direction at any moment.

#### **Expanding beyond Elixir and Phoenix**

Chris's announcement included this note:

> At this point you might be wondering – can I just ask it to build a Rails app? Or an Expo React Native app? Or Svelte? Or Go?
> 
> Yes, you can.
> 
> Our system prompt is tuned for Phoenix today, but all languages you care about are already installed. We’re still figuring out where to take this, but adding new languages and frameworks definitely ranks highly in my plans.

The browser\-based IDE includes a terminal, and I checked and `python3` and `python3 -m pip install datasette` work there already.

If Fly do evolve this into a framework\-agnostic tool for building web apps they'll probably need to rebrand it from Phoenix.new to something a bit more generic!

Phoenix.new is currently priced as a $20/month subscription. Val Town recently switched the pricing for their similar Townie assistant from a subscription to to [pay per use](https://blog.val.town/townie-credits), presumably because for many users this kind of tool is something they would only use intermittently, although given the capabilities of Phoenix.new it's possible it could become a monthly driver for people, especially as it expands out to cover more frameworks.

*Fly sponsor some of our work on Datasette Cloud (see [disclosures](https://simonwillison.net/about/#disclosures)), but this article is not sponsored content and Fly did not request or review this post.*

---

**Quote** 2025\-06\-21

> ***Is it safe to say that LLMs are, in essence, making us "dumber"?**  
>   
> No! Please do not use the words like “stupid”, “dumb”, “brain rot”, "harm", "damage", and so on. It does a huge disservice to this work, as we did not use this vocabulary in the paper, especially if you are a journalist reporting on it.*

[FAQ for Your Brain on ChatGPT](https://www.media.mit.edu/projects/your-brain-on-chatgpt/overview/#faq-is-it-safe-to-say-that-llms-are-in-essence-making-us-dumber)

---

**Link** 2025\-06\-21 [model.yaml](https://modelyaml.org/):

From their [GitHub repo](https://github.com/modelyaml/modelyaml) it looks like this effort quietly launched a couple of months ago, driven by the [LM Studio](https://lmstudio.ai/) team. Their goal is to specify an "open standard for defining crossplatform, composable AI models".

A model can be defined using a YAML file that [looks like this](https://lmstudio.ai/models/mistralai/mistral-small-3.2):

```
model: mistralai/mistral-small-3.2
base:
  - key: lmstudio-community/mistral-small-3.2-24b-instruct-2506-gguf
    sources:
      - type: huggingface
        user: lmstudio-community
        repo: Mistral-Small-3.2-24B-Instruct-2506-GGUF
metadataOverrides:
  domain: llm
  architectures:
    - mistral
  compatibilityTypes:
    - gguf
  paramsStrings:
    - 24B
  minMemoryUsageBytes: 14300000000
  contextLengths:
    - 4096
  vision: true
```

This should be enough information for an LLM serving engine \- such as LM Studio \- to understand where to get the model weights (here that's [lmstudio\-community/Mistral\-Small\-3\.2\-24B\-Instruct\-2506\-GGUF](https://huggingface.co/lmstudio-community/Mistral-Small-3.2-24B-Instruct-2506-GGUF) on Hugging Face, but it leaves space for alternative providers) plus various other configuration options and important metadata about the capabilities of the model.

I like this concept a lot. I've actually been considering something similar for my LLM tool \- my idea was to use Markdown with a YAML frontmatter block \- but now that there's an early\-stage standard for it I may well build on top of this work instead.

I couldn't find any evidence that anyone outside of LM Studio is using this yet, so it's effectively a one\-vendor standard for the moment. All of the models in their [Model Catalog](https://lmstudio.ai/models) are defined using model.yaml.

---

**TIL** 2025\-06\-21 [Publishing a Docker container for Microsoft Edit to the GitHub Container Registry](https://til.simonwillison.net/github/container-registry):

Microsoft recently [released Edit](https://devblogs.microsoft.com/commandline/edit-is-now-open-source/), a new terminal text editor written in Rust. It's pretty nice \- it's reminiscent of `nano` but with a retro MS DOS feel. …

---

**Link** 2025\-06\-21 [Edit is now open source](https://devblogs.microsoft.com/commandline/edit-is-now-open-source/):

Microsoft released a new text editor! Edit is a terminal editor \- similar to Vim or nano \- that's designed to ship with Windows 11 but is open source, written in Rust and supported across other platforms as well.

> Edit is a small, lightweight text editor. It is less than 250kB, which allows it to keep a small footprint in the Windows 11 image.

[![Screenshot of alpine-edit text editor interface with File menu open showing: New File Ctrl+N, Open File... Ctrl+O, Save Ctrl+S, Save As..., Close File Ctrl+W, Exit Ctrl+Q. Window title shows "alpine-edit — Untitled-1.txt - edit — com.docker.cli docker run --platform linux/arm...". Editor contains text "le terminal text editor." Status bar shows "LF UTF-8 Spaces:4 3:44 * Untitled-1.txt".](https://substackcdn.com/image/fetch/$s_!vZ5u!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F383ee341-0539-40dc-84e5-5476c270b462_1357x661.jpeg "Screenshot of alpine-edit text editor interface with File menu open showing: New File Ctrl+N, Open File... Ctrl+O, Save Ctrl+S, Save As..., Close File Ctrl+W, Exit Ctrl+Q. Window title shows \"alpine-edit — Untitled-1.txt - edit — com.docker.cli docker run --platform linux/arm...\". Editor contains text \"le terminal text editor.\" Status bar shows \"LF UTF-8 Spaces:4 3:44 * Untitled-1.txt\".")](https://substackcdn.com/image/fetch/$s_!vZ5u!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F383ee341-0539-40dc-84e5-5476c270b462_1357x661.jpeg)

The [microsoft/edit GitHub releases page](https://github.com/microsoft/edit/releases)currently has pre\-compiled binaries for Windows and Linux, but they didn't have one for macOS.

(They do have [build instructions using Cargo](https://github.com/microsoft/edit/blob/main/README.md#build-instructions) if you want to compile from source.)

I decided to try and get their released binary working on my Mac using Docker. One thing lead to another, and I've now built and shipped a container to the GitHub Container Registry that anyone with Docker on Apple silicon can try out like this:

```
docker run --platform linux/arm64 \
  -it --rm \
  -v $(pwd):/workspace \
  ghcr.io/simonw/alpine-edit
```

Running that command will download a 9\.59MB container image and start Edit running against the files in your current directory. Hit Ctrl\+Q or use File \-\> Exit (the mouse works too) to quit the editor and terminate the container.

Claude 4 has a training cut\-off date of March 2025, so it was able to [guide me through almost everything](https://claude.ai/share/5f0e6547-a3e9-4252-98d0-56f3141c3694) even down to which page I should go to in GitHub to create an access token with permission to publish to the registry!

I wrote up a new TIL on [Publishing a Docker container for Microsoft Edit to the GitHub Container Registry](https://til.simonwillison.net/github/container-registry) with a revised and condensed version of everything I learned today.

---

**Link** 2025\-06\-21 [My First Open Source AI Generated Library](https://lucumr.pocoo.org/2025/6/21/my-first-ai-library/):

Armin Ronacher had Claude and Claude Code do almost *all of the work* in building, testing, packaging and publishing a new Python library based on his design:

> * It wrote \~1100 lines of code for the parser
> * It wrote \~1000 lines of tests
> * It configured the entire Python package, CI, PyPI publishing
> * Generated a README, drafted a changelog, designed a logo, made it theme\-aware
> * Did multiple refactorings to make me happier

The project? [sloppy\-xml\-py](https://github.com/mitsuhiko/sloppy-xml-py), a lax XML parser (and violation of everything the XML Working Group hold sacred) which ironically is necessary because LLMs themselves frequently output "XML" that includes validation errors.

Claude's SVG logo design is actually pretty decent, turns out it can draw [more than just bad pelicans](https://simonwillison.net/2025/May/22/code-with-claude-live-blog/#live-update-357)!

[![Hand drawn style, orange rough rectangly containing < { s } > - then the text Sloppy XML below in black](https://substackcdn.com/image/fetch/$s_!b2jF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff5c6d2ef-6df8-4c03-a0f8-20a6fd61faf5_270x324.jpeg "Hand drawn style, orange rough rectangly containing < { s } > - then the text Sloppy XML below in black")](https://substackcdn.com/image/fetch/$s_!b2jF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff5c6d2ef-6df8-4c03-a0f8-20a6fd61faf5_270x324.jpeg)

I think experiments like this are a really valuable way to explore the capabilities of these models. Armin's conclusion:

> This was an experiment to see how far I could get with minimal manual effort, and to unstick myself from an annoying blocker. The result is good enough for my immediate use case and I also felt good enough to publish it to PyPI in case someone else has the same problem.
> 
> Treat it as a curious side project which says more about what's possible today than what's necessarily advisable.

I'd like to present a slightly different conclusion here. The most interesting thing about this project is that **the code is good**.

My criteria for good code these days is the following:

1. Solves a defined problem, well enough that I'm not tempted to solve it in a different way
2. Uses minimal dependencies
3. Clear and easy to understand
4. Well tested, with tests prove that the code does what it's meant to do
5. Comprehensive documentation
6. Packaged and published in a way that makes it convenient for me to use
7. Designed to be easy to maintain and make changes in the future

`sloppy-xml-py` fits all of those criteria. It's useful, well defined, [the code is readable](https://github.com/mitsuhiko/sloppy-xml-py/blob/main/sloppy_xml.py) with just about the right level of comments, everything is tested, the documentation explains everything I need to know, and it's been shipped to PyPI.

I'd be proud to have written this myself.

This example is *not* an argument for replacing programmers with LLMs. The code is good because Armin is an expert programmer who stayed in full control throughout the process. As I wrote the other day, [a skilled individual with both deep domain understanding and deep understanding of the capabilities of the agent](https://simonwillison.net/2025/Jun/18/coding-agents/).

---

**Quote** 2025\-06\-22

> *So you can think really big thoughts and the leverage of having those big thoughts has just suddenly expanded enormously. I had [this tweet](https://twitter.com/KentBeck/status/1648413998025707520) two years ago where I said "90% of my skills just went to zero dollars and 10% of my skills just went up 1000x". And this is exactly what I'm talking about \- having a vision, being able to set milestones towards that vision, keeping track of a design to maintain or control the levels of complexity as you go forward. Those are hugely leveraged skills now compared to knowing where to put the ampersands and the stars and the brackets in Rust.*

[Kent Beck](https://www.youtube.com/watch?v=aSXaxOdVtAQ&t=12m30s)

---

**Note** [2025\-06\-23](https://simonwillison.net/2025/Jun/23/disclosures/)

I've added a [Disclosures section](https://simonwillison.net/about/#disclosures) to my about page, listing my various sources of income and the companies that directly sponsor my work or have supported it in the recent past.

> I do not receive any compensation writing about specific topics on this blog \- no sponsored content! I plan to continue this policy. If I ever change this I will disclose that both here and in the post itself. \[...]

I see my credibility as one of my most valuable assets, so it's important to be transparent about how financial interests may influence my writing here.

I took inspiration from [Molly White's disclosures page](https://www.mollywhite.net/crypto-disclosures/).

---

**Link** 2025\-06\-24 [Anthropic wins a major fair use victory for AI — but it’s still in trouble for stealing books](https://www.theverge.com/news/692015/anthropic-wins-a-major-fair-use-victory-for-ai-but-its-still-in-trouble-for-stealing-books):

Major USA legal news for the AI industry today. Judge William Alsup released a "summary judgement" (a legal decision that results in some parts of a case skipping a trial) in a lawsuit between five authors and Anthropic concerning the use of their books in training data.

The [judgement itself](https://www.documentcloud.org/documents/25982181-authors-v-anthropic-ruling/) is a very readable 32 page PDF, and contains all sorts of interesting behind\-the\-scenes details about how Anthropic trained their models.

The facts of the complaint go back to the very beginning of the company. Anthropic was founded by a group of ex\-OpenAI researchers in February 2021\. According to the judgement:

> So, in January or February 2021, another Anthropic cofounder, Ben Mann, downloaded Books3, an online library of 196,640 books that he knew had been assembled from unauthorized copies of copyrighted books — that is, pirated. Anthropic's next pirated acquisitions involved downloading distributed, reshared copies of other pirate libraries. In June 2021, Mann downloaded in this way at least five million copies of books from Library Genesis, or LibGen, which he knew had been pirated. And, in July 2022, Anthropic likewise downloaded at least two million copies of books from the Pirate Library Mirror, or PiLiMi, which Anthropic knew had been pirated.

Books3 was also listed as [part of the training data](https://simonwillison.net/2023/Aug/27/wordcamp-llms/#how-they-are-trained)for Meta's first LLaMA model!

Anthropic apparently used these sources of data to help build an internal "research library" of content that they then filtered and annotated and used in training runs.

Books turned out to be a very valuable component of the "data mix" to train strong models. By 2024 Anthropic had a new approach to collecting them: purchase and scan millions of print books!

> To find a new way to get books, in February 2024, Anthropic hired the former head of partnerships for Google's book\-scanning project, Tom Turvey. He was tasked with obtaining "all the books in the world" while still avoiding as much "legal/practice/business slog" as possible (Opp. Exhs. 21, 27\). \[...] Turvey and his team emailed major book distributors and retailers about bulk\-purchasing their print copies for the AI firm's "research library" (Opp. Exh. 22 at 145; Opp. Exh. 31 at \-035589\). Anthropic spent many millions of dollars to purchase millions of print books, often in used condition. Then, its service providers stripped the books from their bindings, cut their pages to size, and scanned the books into digital form — discarding the paper originals. Each print book resulted in a PDF copy containing images of the scanned pages with machine\-readable text (including front and back cover scans for softcover books).

The summary judgement found that these scanned books *did* fall under fair use, since they were transformative versions of the works and were not shared outside of the company. The downloaded ebooks did *not* count as fair use, and it looks like those will be the subject of a forthcoming jury trial.

Here's that section of the decision:

> Before buying books for its central library, Anthropic downloaded over seven million pirated copies of books, paid nothing, and kept these pirated copies in its library even after deciding it would not use them to train its AI (at all or ever again). Authors argue Anthropic should have paid for these pirated library copies (e.g, Tr. 24–25, 65; Opp. 7, 12–13\). This order agrees.

The most important aspect of this case is the question of whether training an LLM on unlicensed data counts as "fair use". The judge found that it did. The argument for why takes up several pages of the document but this seems like a key point:

> Everyone reads texts, too, then writes new texts. They may need to pay for getting their hands on a text in the first instance. But to make anyone pay specifically for the use of a book each time they read it, each time they recall it from memory, each time they later draw upon it when writing new things in new ways would be unthinkable. For centuries, we have read and re\-read books. We have admired, memorized, and internalized their sweeping themes, their substantive points, and their stylistic solutions to recurring writing problems.

The judge who signed this summary judgement is an interesting character: [William Haskell Alsup](https://en.wikipedia.org/wiki/William_Alsup)(yes, his middle name really is Haskell) presided over jury trials for Oracle America, Inc. v. Google, Inc in 2012 and 2016 where he famously used his hobbyist BASIC programming experience to challenge claims made by lawyers in the case.

---

**Link** 2025\-06\-25 [Gemini CLI](https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/):

First there was [Claude Code](https://simonwillison.net/2025/Feb/24/claude-37-sonnet-and-claude-code/) in February, then [OpenAI Codex (CLI)](https://simonwillison.net/2025/Apr/16/) in April, and now Gemini CLI in June. All three of the largest AI labs now have their own version of what I am calling a "terminal agent" \- a CLI tool that can read and write files and execute commands on your behalf in the terminal.

I'm honestly a little surprised at how significant this category has become: I had assumed that terminal tools like this would always be something of a niche interest, but given the number of people I've heard from spending hundreds of dollars a month on Claude Code this niche is clearly larger and more important than I had thought!

I had a few days of early access to the Gemini one. It's very good \- it takes advantage of Gemini's million token context and has good taste in things like when to read a file and when to run a command.

Like OpenAI Codex and unlike Claude Code it's open source (Apache 2\) \- the full source code can be found in [google\-gemini/gemini\-cli](https://github.com/google-gemini/gemini-cli) on GitHub. The core system prompt [lives in core/src/core/prompts.ts](https://github.com/google-gemini/gemini-cli/blob/0915bf7d677504c28b079693a0fe1c853adc456e/packages/core/src/core/prompts.ts#L40-L109) \- I've extracted that out as [a rendered Markdown Gist](https://gist.github.com/simonw/9e5f13665b3112cea00035df7da696c6).

As usual, the system prompt doubles as extremely accurate and concise documentation of what the tool can do! Here's what it has to say about comments, for example:

> * **Comments:** Add code comments sparingly. Focus on *why* something is done, especially for complex logic, rather than *what* is done. Only add high\-value comments if necessary for clarity or if requested by the user. Do not edit comments that are seperate from the code you are changing. *NEVER* talk to the user or describe your changes through comments.

The list of preferred technologies is interesting too:

> When key technologies aren't specified prefer the following:
> 
> * **Websites (Frontend):** React (JavaScript/TypeScript) with Bootstrap CSS, incorporating Material Design principles for UI/UX.
> * **Back\-End APIs:** Node.js with Express.js (JavaScript/TypeScript) or Python with FastAPI.
> * **Full\-stack:** Next.js (React/Node.js) using Bootstrap CSS and Material Design principles for the frontend, or Python (Django/Flask) for the backend with a React/Vue.js frontend styled with Bootstrap CSS and Material Design principles.
> * **CLIs:** Python or Go.
> * **Mobile App:** Compose Multiplatform (Kotlin Multiplatform) or Flutter (Dart) using Material Design libraries and principles, when sharing code between Android and iOS. Jetpack Compose (Kotlin JVM) with Material Design principles or SwiftUI (Swift) for native apps targeted at either Android or iOS, respectively.
> * **3d Games:** HTML/CSS/JavaScript with Three.js.
> * **2d Games:** HTML/CSS/JavaScript.

As far as I can tell Gemini CLI only defines a small selection of tools:

* `edit`: To modify files programmatically.
* `glob`: To find files by pattern.
* `grep`: To search for content within files.
* `ls`: To list directory contents.
* `shell`: To execute a command in the shell
* `memoryTool`: To remember user\-specific facts.
* `read-file`: To read a single file
* `write-file`: To write a single file
* `read-many-files`: To read multiple files at once.
* `web-fetch`: To get content from URLs.
* `web-search`: To perform a web search (using [Grounding with Google Search](https://ai.google.dev/gemini-api/docs/google-search) via the Gemini API).

I found most of those by having Gemini CLI inspect its own code for me! Here's [that full transcript](https://gist.github.com/simonw/12c7b072e8e21ef1e040fb3b69c1da28), which used just over 300,000 tokens total.

How much does it cost? The announcement describes a generous free tier:

> To use Gemini CLI free\-of\-charge, simply login with a personal Google account to get a free Gemini Code Assist license. That free license gets you access to Gemini 2\.5 Pro and its massive 1 million token context window. To ensure you rarely, if ever, hit a limit during this preview, we offer the industry’s largest allowance: 60 model requests per minute and 1,000 requests per day at no charge.

It's not yet clear to me if your inputs can be used to improve Google's models if you are using the free tier \- that's been the situation with free prompt inference they have offered in the past.

You can also drop in your own paid API key, at which point your data will not be used for model improvements and you'll be billed based on your token usage.

---

**Quote** 2025\-06\-25

> *Creating art is a nonlinear process. I start with a rough goal. But then I head into dead ends and get lost or stuck.  
>   
> The secret to my process is to be on high alert in this deep jungle for unexpected twists and turns, because this is where a new idea is born.  
>   
> I can't make art when I'm excluded from the most  
> crucial moments.*

[Christoph Niemann](https://www.nytimes.com/interactive/2025/06/23/magazine/ai-art-artists-illustrator.html)

---

**Link** 2025\-06\-25 [Build and share AI\-powered apps with Claude](https://www.anthropic.com/news/claude-powered-artifacts):

Anthropic have added one of the most important missing features to [Claude Artifacts](https://simonwillison.net/tags/claude-artifacts/): apps built as artifacts now have the ability to run their own prompts against Claude via a new API.

Claude Artifacts are web apps that run in a strictly controlled browser sandbox: their access to features like localStorage or the ability to access external APIs via `fetch()` calls is restricted by CSP headers and the `<iframe sandbox="..."`mechanism.

The new `window.claude.complete()` method opens a hole that allows prompts composed by the JavaScript artifact application to be run against Claude.

As before, you can publish apps built using artifacts such that anyone can see them. The moment your app tries to execute a prompt the current user will be required to sign into their own Anthropic account so that the prompt can be billed against them, and not against you.

I'm amused that Anthropic turned "we added a window.claude.complete() function to Artifacts" into what looks like a major new product launch, but I can't say it's bad marketing for them to do that!

As always, the crucial details about how this all works are tucked away in tool descriptions in the system prompt. Thankfully this one was [easy to leak](https://claude.ai/share/42b70567-8534-4080-9227-b834e8c13d6e). Here's [the full set of instructions](https://gist.github.com/simonw/31957633864d1b7dd60012b2205fd747), which start like this:

> When using artifacts and the analysis tool, you have access to window.claude.complete. This lets you send completion requests to a Claude API. This is a powerful capability that lets you orchestrate Claude completion requests via code. You can use this capability to do sub\-Claude orchestration via the analysis tool, and to build Claude\-powered applications via artifacts.
> 
> This capability may be referred to by the user as "Claude in Claude" or "Claudeception".
> 
> \[...]
> 
> The API accepts a single parameter \-\- the prompt you would like to complete. You can call it like so: `const response = await window.claude.complete('prompt you would like to complete')`

I haven't seen "Claudeception" in any of their official documentation yet!

That `window.claude.complete(prompt)` method is also available to the Claude analysis tool. It takes a string and returns a string.

The new function only handles strings. The tool instructions provide tips to Claude about prompt engineering a JSON response that will look frustratingly familiar:

> 3. Use strict language: Emphasize that the response must be in JSON format only. For example: “Your entire response must be a single, valid JSON object. Do not include any text outside of the JSON structure, including backticks `.”</li> <li>Be emphatic about the importance of having only JSON. If you really want Claude to care, you can put things in all caps – e.g., saying “DO NOT OUTPUT ANYTHING OTHER THAN VALID JSON. DON’T INCLUDE LEADING BACKTICKS LIKE`json.”.

Talk about Claudeception... now even Claude itself knows that you have to YELL AT CLAUDE to get it to output JSON sometimes.

The API doesn't provide a mechanism for handling previous conversations, but Anthropic works round that by telling the artifact builder how to represent a prior conversation as a JSON encoded array:

> Structure your prompt like this:
> 
> 
> ```
> const conversationHistory = [
>   { role: "user", content: "Hello, Claude!" },
>   { role: "assistant", content: "Hello! How can I assist you today?" },
>   { role: "user", content: "I'd like to know about AI." },
>   { role: "assistant", content: "Certainly! AI, or Artificial Intelligence, refers to..." },
>   // ... ALL previous messages should be included here
> ];
> 
> const prompt = `
> The following is the COMPLETE conversation history. You MUST consider ALL of these messages when formulating your response:
> ${JSON.stringify(conversationHistory)}
> 
> IMPORTANT: Your response should take into account the ENTIRE conversation history provided above, not just the last message.
> 
> Respond with a JSON object in this format:
> {
>   "response": "Your response, considering the full conversation history",
>   "sentiment": "brief description of the conversation's current sentiment"
> }
> 
> Your entire response MUST be a single, valid JSON object.
> `;
> 
> const response = await window.claude.complete(prompt);
> ```

There's another example in there showing how the state of play for a role playing game should be serialized as JSON and sent with every prompt as well.

The tool instructions acknowledge another limitation of the current Claude Artifacts environment: code that executes there is effectively invisible to the main LLM \- error messages are not automatically round\-tripped to the model. As a result it makes the following recommendation:

> Using `window.claude.complete` may involve complex orchestration across many different completion requests. Once you create an Artifact, you are not able to see whether or not your completion requests are orchestrated correctly. Therefore, you SHOULD ALWAYS test your completion requests first in the analysis tool before building an artifact.

I've already seen it do this in my own experiments: it will fire up the "analysis" tool (which allows it to run JavaScript directly and see the results) to perform a quick prototype before it builds the full artifact.

Here's my first attempt at an AI\-enabled artifact: a translation app. I built it using the following single prompt:

> `Let’s build an AI app that uses Claude to translate from one language to another`

Here's [the transcript](https://claude.ai/share/e26be9a8-739c-45de-8aee-86dafed4aa87). You can [try out the resulting app here](https://claude.ai/public/artifacts/1aeb7042-2004-4549-a97d-ca740d0f1bf0) \- the app it built me looks like this:

[![Screenshot of Claude AI Translator interface showing: Claude AI Translator logo with blue circular icon containing "文A", "Powered by Claude AI for accurate, context-aware translations", language selection dropdowns showing "From English" and "To Spanish" with blue swap arrows button between them, text input area labeled "Enter text to translate" containing "Tell me some fun facts about pelicans", "Tip: Press Ctrl+Enter to translate", Translation section with "high confidence" indicator in green and Spanish translation "Cuéntame algunos datos curiosos sobre los pelícanos" with copy button icon.](https://substackcdn.com/image/fetch/$s_!RZgx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F28be0335-3a67-4a30-921b-5e6975862d1a_1816x1630.jpeg "Screenshot of Claude AI Translator interface showing: Claude AI Translator logo with blue circular icon containing \"文A\", \"Powered by Claude AI for accurate, context-aware translations\", language selection dropdowns showing \"From English\" and \"To Spanish\" with blue swap arrows button between them, text input area labeled \"Enter text to translate\" containing \"Tell me some fun facts about pelicans\", \"Tip: Press Ctrl+Enter to translate\", Translation section with \"high confidence\" indicator in green and Spanish translation \"Cuéntame algunos datos curiosos sobre los pelícanos\" with copy button icon.")](https://substackcdn.com/image/fetch/$s_!RZgx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F28be0335-3a67-4a30-921b-5e6975862d1a_1816x1630.jpeg)

If you want to use this feature yourself you'll need to turn on "Create AI\-powered artifacts" in the "Feature preview" section at the bottom of your "Settings \-\> Profile" section. I had to do that in the Claude web app as I couldn't find the feature toggle in the Claude iOS application. This [claude.ai/settings/profile](https://claude.ai/settings/profile) page should have it for your account.

---