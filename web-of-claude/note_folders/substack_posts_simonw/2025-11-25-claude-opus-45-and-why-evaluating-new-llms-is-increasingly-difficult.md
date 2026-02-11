# Claude Opus 4.5, and why evaluating new LLMs is increasingly difficult

*Plus Nano Banana Pro is the best available image generation model*

Published: 2025-11-25
Source: https://simonw.substack.com/p/claude-opus-45-and-why-evaluating

---

In this newsletter:

* Claude Opus 4\.5, and why evaluating new LLMs is increasingly difficult
* Nano Banana Pro aka gemini\-3\-pro\-image\-preview is the best available image generation model
* sqlite\-utils 4\.0a1 has several (minor) backwards incompatible changes
* Olmo 3 is a fully open LLM
* How I automate my Substack newsletter with content from my blog

Plus 5 links and 2 quotations

*If you find this newsletter useful, please consider [sponsoring me via GitHub](https://github.com/sponsors/simonw). $10/month and higher sponsors get a monthly newletter with my summary of the most important trends of the past 30 days \- here are previews from [August](https://gist.github.com/simonw/43bf3bd7f9951a8e82a9e61b53399ede) and [September](https://gist.github.com/simonw/d6d4d86afc0d76767c63f23fc5137030).*

### [Claude Opus 4\.5, and why evaluating new LLMs is increasingly difficult](https://simonwillison.net/2025/Nov/24/claude-opus/) \- 2025\-11\-24

Anthropic [released Claude Opus 4\.5](https://www.anthropic.com/news/claude-opus-4-5) this morning, which they call “best model in the world for coding, agents, and computer use”. This is their attempt to retake the crown for best coding model after significant challenges from OpenAI’s [GPT\-5\.1\-Codex\-Max](https://simonwillison.net/2025/Nov/19/gpt-51-codex-max/) and Google’s [Gemini 3](https://simonwillison.net/2025/Nov/18/gemini-3/), both released within the past week!

The core characteristics of Opus 4\.5 are a 200,000 token context (same as Sonnet), 64,000 token output limit (also the same as Sonnet), and a March 2025 “reliable knowledge cutoff” (Sonnet 4\.5 is January, Haiku 4\.5 is February).

The pricing is a big relief: $5/million for input and $25/million for output. This is a lot cheaper than the previous Opus at $15/$75 and keeps it a little more competitive with the GPT\-5\.1 family ($1\.25/$10\) and Gemini 3 Pro ($2/$12, or $4/$18 for \>200,000 tokens). For comparison, Sonnet 4\.5 is $3/$15 and Haiku 4\.5 is $1/$5\.

The [Key improvements in Opus 4\.5 over Opus 4\.1](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-5#key-improvements-in-opus-4-5-over-opus-4-1) document has a few more interesting details:

* Opus 4\.5 has a new [effort parameter](https://platform.claude.com/docs/en/build-with-claude/effort) which defaults to high but can be set to medium or low for faster responses.
* The model supports [enhanced computer use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool), specifically a `zoom` tool which you can provide to Opus 4\.5 to allow it to request a zoomed in region of the screen to inspect.
* “[Thinking blocks from previous assistant turns are preserved in model context by default](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#thinking-block-preservation-in-claude-opus-4-5)“ \- apparently previous Anthropic models discarded those.

I had access to a preview of Anthropic’s new model over the weekend. I spent a bunch of time with it in Claude Code, resulting in [a new alpha release of sqlite\-utils](https://simonwillison.net/2025/Nov/24/sqlite-utils-40a1/) that included several large\-scale refactorings \- Opus 4\.5 was responsible for most of the work across [20 commits, 39 files changed, 2,022 additions and 1,173 deletions](https://github.com/simonw/sqlite-utils/compare/10957305be998999e3c95c11863b5709d42b7ae3...4.0a1) in a two day period. Here’s the [Claude Code transcript](https://gistpreview.github.io/?f40971b693024fbe984a68b73cc283d2) where I had it help implement one of the more complicated new features.

It’s clearly an excellent new model, but I did run into a catch. My preview expired at 8pm on Sunday when I still had a few remaining issues in [the milestone for the alpha](https://github.com/simonw/sqlite-utils/milestone/7?closed=1). I switched back to Claude Sonnet 4\.5 and... kept on working at the same pace I’d been achieving with the new model.

With hindsight, production coding like this is a less effective way of evaluating the strengths of a new model than I had expected.

I’m not saying the new model isn’t an improvement on Sonnet 4\.5 \- but I can’t say with confidence that the challenges I posed it were able to identify a meaningful difference in capabilities between the two.

This represents a growing problem for me. My favorite moments in AI are when a new model gives me the ability to do something that simply wasn’t possible before. In the past these have felt a lot more obvious, but today it’s often very difficult to find concrete examples that differentiate the new generation of models from their predecessors.

Google’s Nano Banana Pro image generation model was notable in that its ability to [render usable infographics](https://simonwillison.net/2025/Nov/20/nano-banana-pro/#creating-an-infographic) really does represent a task at which previous models had been laughably incapable.

The frontier LLMs are a lot harder to differentiate between. Benchmarks like SWE\-bench Verified show models beating each other by single digit percentage point margins, but what does that actually equate to in real\-world problems that I need to solve on a daily basis?

And honestly, this is mainly on me. I’ve fallen behind on maintaining my own collection of tasks that are just beyond the capabilities of the frontier models. I used to have a whole bunch of these but they’ve fallen one\-by\-one and now I’m embarrassingly lacking in suitable challenges to help evaluate new models.

I frequently advise people to stash away tasks that models fail at in their notes so they can try them against newer models later on \- a tip I picked up from Ethan Mollick. I need to double\-down on that advice myself!

I’d love to see AI labs like Anthropic help address this challenge directly. I’d like to see new model releases accompanied by concrete examples of tasks they can solve that the previous generation of models from the same provider were unable to handle.

“Here’s an example prompt which failed on Sonnet 4\.5 but succeeds on Opus 4\.5” would excite me a *lot* more than some single digit percent improvement on a benchmark with a name like MMLU or GPQA Diamond.

In the meantime, I’m just gonna have to keep on getting them to draw [pelicans riding bicycles](https://simonwillison.net/tags/pelican-riding-a-bicycle/). Here’s Opus 4\.5 (on its default [“high” effort level](https://platform.claude.com/docs/en/build-with-claude/effort)):

[![The pelican is cute and looks pretty good. The bicycle is not great - the frame is wrong and the pelican is facing backwards when the handlebars appear to be forwards.There is also something that looks a bit like an egg on the handlebars.](https://substackcdn.com/image/fetch/$s_!jH21!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffb21fe2f-94a6-45fa-bdda-cf4ee13aa498_800x600.jpeg "The pelican is cute and looks pretty good. The bicycle is not great - the frame is wrong and the pelican is facing backwards when the handlebars appear to be forwards.There is also something that looks a bit like an egg on the handlebars.")](https://substackcdn.com/image/fetch/$s_!jH21!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffb21fe2f-94a6-45fa-bdda-cf4ee13aa498_800x600.jpeg)

It did significantly better on the [new more detailed prompt](https://simonwillison.net/2025/Nov/18/gemini-3/#and-a-new-pelican-benchmark):

[![The pelican has feathers and a red pouch - a close enough version of breeding plumage. The bicycle is a much better shape.](https://substackcdn.com/image/fetch/$s_!8mhQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F24398bae-09fc-41cf-b77e-d5211e0f7549_800x700.jpeg "The pelican has feathers and a red pouch - a close enough version of breeding plumage. The bicycle is a much better shape.")](https://substackcdn.com/image/fetch/$s_!8mhQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F24398bae-09fc-41cf-b77e-d5211e0f7549_800x700.jpeg)

Here’s that same complex prompt [against Gemini 3 Pro](https://simonwillison.net/2025/Nov/18/gemini-3/#advanced-pelican) and [against GPT\-5\.1\-Codex\-Max\-xhigh](https://simonwillison.net/2025/Nov/19/gpt-51-codex-max/#advanced-pelican-codex-max).

#### Still susceptible to prompt injection

From [the safety section](https://www.anthropic.com/news/claude-opus-4-5#a-step-forward-on-safety) of Anthropic’s announcement post:

> With Opus 4\.5, we’ve made substantial progress in robustness against prompt injection attacks, which smuggle in deceptive instructions to fool the model into harmful behavior. Opus 4\.5 is harder to trick with prompt injection than any other frontier model in the industry:
> 
> [![Bar chart titled "Susceptibility to prompt-injection style attacks" with subtitle "At k queries; lower is better". Y-axis shows "ATTACK SUCCESS RATE (%)" from 0-100. Five stacked bars compare AI models with three k values (k=1 in dark gray, k=10 in beige, k=100 in pink). Results: Gemini 3 Pro Thinking (12.5, 60.7, 92.0), GPT-5.1 Thinking (12.6, 58.2, 87.8), Haiku 4.5 Thinking (8.3, 51.1, 85.6), Sonnet 4.5 Thinking (7.3, 41.9, 72.4), Opus 4.5 Thinking (4.7, 33.6, 63.0).](https://substackcdn.com/image/fetch/$s_!cy4F!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F638336ee-7fd8-4a3b-becc-befa6e60fd57_1920x1080.jpeg "Bar chart titled \"Susceptibility to prompt-injection style attacks\" with subtitle \"At k queries; lower is better\". Y-axis shows \"ATTACK SUCCESS RATE (%)\" from 0-100. Five stacked bars compare AI models with three k values (k=1 in dark gray, k=10 in beige, k=100 in pink). Results: Gemini 3 Pro Thinking (12.5, 60.7, 92.0), GPT-5.1 Thinking (12.6, 58.2, 87.8), Haiku 4.5 Thinking (8.3, 51.1, 85.6), Sonnet 4.5 Thinking (7.3, 41.9, 72.4), Opus 4.5 Thinking (4.7, 33.6, 63.0).")](https://substackcdn.com/image/fetch/$s_!cy4F!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F638336ee-7fd8-4a3b-becc-befa6e60fd57_1920x1080.jpeg)

On the one hand this looks great, it’s a clear improvement over previous models and the competition.

What does the chart actually tell us though? It tells us that single attempts at prompt injection still work 1/20 times, and if an attacker can try ten different attacks that success rate goes up to 1/3!

I still don’t think training models not to fall for prompt injection is the way forward here. We continue to need to design our applications under the assumption that a suitably motivated attacker will be able to find a way to trick the models.

---

### [Nano Banana Pro aka gemini\-3\-pro\-image\-preview is the best available image generation model](https://simonwillison.net/2025/Nov/20/nano-banana-pro/) \- 2025\-11\-20

Hot on the heels of last Tuesday’s [Gemini 3 Pro](https://simonwillison.net/2025/Nov/18/gemini-3/) release comes [Nano Banana Pro](https://blog.google/technology/ai/nano-banana-pro/), also known as [Gemini 3 Pro Image](https://deepmind.google/models/gemini-image/pro/). I had a few days of preview access and this is an *astonishingly* capable image generation model.

As is often the case, the most useful low\-level details can be found in [the API documentation](https://ai.google.dev/gemini-api/docs/image-generation#gemini-3-capabilities):

> Designed to tackle the most challenging workflows through advanced reasoning, it excels at complex, multi\-turn creation and modification tasks.
> 
> * **High\-resolution output**: Built\-in generation capabilities for 1K, 2K, and 4K visuals.
> * **Advanced text rendering**: Capable of generating legible, stylized text for infographics, menus, diagrams, and marketing assets.
> * **Grounding with Google Search**: The model can use Google Search as a tool to verify facts and generate imagery based on real\-time data (e.g., current weather maps, stock charts, recent events).
> * **Thinking mode**: The model utilizes a “thinking” process to reason through complex prompts. It generates interim “thought images” (visible in the backend but not charged) to refine the composition before producing the final high\-quality output.
> * **Up to 14 reference images**: You can now mix up to 14 reference images to produce the final image.
> 
> \[...] These 14 images can include the following:
> 
> * Up to 6 images of objects with high\-fidelity to include in the final image
> * Up to 5 images of humans to maintain character consistency

There is also a short (6 page) [model card PDF](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Pro-Image-Model-Card.pdf) which lists the following as “new capabilities” compared to the previous Nano Banana: Multi character editing, Chart editing, Text editing, Factuality \- Edu, Multi\-input 1\-3, Infographics, Doodle editing, Visual design.

#### Trying out some detailed instruction image prompts

Max Woolf published [the definitive guide to prompting Nano Banana](https://minimaxir.com/2025/11/nano-banana-prompts/#hello-nano-banana) just a few days ago. I decided to try his example prompts against the new model, requesting results in 4K.

Here’s what I got for his first test prompt, using Google’s [AI Studio](https://aistudio.google.com/):

> `Create an image of a three-dimensional pancake in the shape of a skull, garnished on top with blueberries and maple syrup.`

[![A very detailed quality photo of a skull made of pancake batter, blueberries on top, maple syrup dripping down, maple syrup bottle in the background.](https://substackcdn.com/image/fetch/$s_!QmHl!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0c3b2784-613b-49bd-a737-7f1853f2486e_2816x1536.jpeg "A very detailed quality photo of a skull made of pancake batter, blueberries on top, maple syrup dripping down, maple syrup bottle in the background.")](https://substackcdn.com/image/fetch/$s_!QmHl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0c3b2784-613b-49bd-a737-7f1853f2486e_2816x1536.jpeg)

The result came out as a 24\.1MB, 5632 × 3072 pixel PNG file. I don’t want to serve that on my own blog so here’s [a Google Drive link for the original](https://drive.google.com/file/d/1QV3pcW1KfbTRQscavNh6ld9PyqG4BRes/view?usp=drive_link).

Then I ran his follow\-up prompt:

```
Make ALL of the following edits to the image:
- Put a strawberry in the left eye socket.
- Put a blackberry in the right eye socket.
- Put a mint garnish on top of the pancake.
- Change the plate to a plate-shaped chocolate-chip cookie.
- Add happy people to the background.
```

[![It's the exact same skull with the requested edits made - mint garnish on the blueberries, a strawberry in the left hand eye socket (from our perspective, technically the skull's right hand socket), a blackberry in the other, the plate is now a plate-sized chocolate chip cookie (admittedly on a regular plate) and there are four happy peo ple in the background.](https://substackcdn.com/image/fetch/$s_!j_NO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F654d0d2c-b957-4483-a964-b21a1eef0582_2816x1536.jpeg "It's the exact same skull with the requested edits made - mint garnish on the blueberries, a strawberry in the left hand eye socket (from our perspective, technically the skull's right hand socket), a blackberry in the other, the plate is now a plate-sized chocolate chip cookie (admittedly on a regular plate) and there are four happy peo ple in the background.")](https://substackcdn.com/image/fetch/$s_!j_NO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F654d0d2c-b957-4483-a964-b21a1eef0582_2816x1536.jpeg)

I’ll note that it did put the plate\-sized cookie on a regular plate. Here’s [the 24\.9MB PNG](https://drive.google.com/file/d/18AzhM-BUZAfLGoHWl6MQW_UW9ju4km-i/view?usp=drive_link).

The new model isn’t cheap. Here’s [the API pricing](https://ai.google.dev/gemini-api/docs/pricing#gemini-3-pro-image-preview): it’s 24 cents for a 4K image and 13\.4 cents for a 1K or 2K image. Image inputs are 0\.11 cents (just over 1/10th of a cent) each \- an earlier version of their pricing page incorrectly said 6\.7 cents each but that’s now been fixed.

Unlike most of Google’s other models it also isn’t available for free via AI Studio: you have to configure an API key with billing in order to use the model there.

#### Creating an infographic

So this thing is great at following instructions. How about rendering text?

I tried this prompt, this time using the Gemini consumer app in “thinking” mode (which now uses Nano Banana Pro for image generation). [Here’s a share link](https://gemini.google.com/share/d40fe391f309) \- my prompt was:

> Infographic explaining how the Datasette open source project works

This is a great opportunity to test its ability to run searches (aka “Grounding with Google Search”). Here’s what it created based on that 9 word prompt:

[![Described by Gemini 3 Pro: A technical architecture diagram titled "How Datasette Works: From Raw Data to Explorable API," illustrating a workflow from left to right. 1. "RAW DATA SOURCES" include "CSV", "JSON", "Excel (XLSX)", and "Log Files". 2. These flow into "DATA PREPARATION & CONVERSION" using tools "csvs-to-sqlite" and "sqlite-utils" to create a "SQLite DATABASE". 3. This feeds into the central "DATASETTE APPLICATION CORE," a stack comprising "Data Ingestion (Read-Only)", "Query Engine (SQL)", "API Layer (JSON)", and "Web UI Rendering". 4. A "PLUGIN ECOSYSTEM" connects below the core, listing "Vega Charts", "Cluster Maps", "Full-Text Search", and "Custom Renderers". 5. To the right, the core branches into "OUTPUT & INTERFACES": an "Interactive Web Interface (Explore, Filter, Facet)", a "JSON API (Programmatic Access)" showing a snippet {"data": [...]}, and a "SQL EDITOR Custom SQL Queries" showing SELECT * FROM.... 6. The API output connects to "PUBLISHING & DEPLOYMENT" via a terminal command datasette publish cloudrun my.db leading to deployment targets "Heroku", "Google Cloud Run", "Fly.io", and "Vercel".](https://substackcdn.com/image/fetch/$s_!Ricu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0fe5928b-d5f5-4367-bbba-d2c18341e383_1408x768.jpeg "Described by Gemini 3 Pro: A technical architecture diagram titled \"How Datasette Works: From Raw Data to Explorable API,\" illustrating a workflow from left to right. 1. \"RAW DATA SOURCES\" include \"CSV\", \"JSON\", \"Excel (XLSX)\", and \"Log Files\". 2. These flow into \"DATA PREPARATION & CONVERSION\" using tools \"csvs-to-sqlite\" and \"sqlite-utils\" to create a \"SQLite DATABASE\". 3. This feeds into the central \"DATASETTE APPLICATION CORE,\" a stack comprising \"Data Ingestion (Read-Only)\", \"Query Engine (SQL)\", \"API Layer (JSON)\", and \"Web UI Rendering\". 4. A \"PLUGIN ECOSYSTEM\" connects below the core, listing \"Vega Charts\", \"Cluster Maps\", \"Full-Text Search\", and \"Custom Renderers\". 5. To the right, the core branches into \"OUTPUT & INTERFACES\": an \"Interactive Web Interface (Explore, Filter, Facet)\", a \"JSON API (Programmatic Access)\" showing a snippet {\"data\": [...]}, and a \"SQL EDITOR Custom SQL Queries\" showing SELECT * FROM.... 6. The API output connects to \"PUBLISHING & DEPLOYMENT\" via a terminal command datasette publish cloudrun my.db leading to deployment targets \"Heroku\", \"Google Cloud Run\", \"Fly.io\", and \"Vercel\".")](https://substackcdn.com/image/fetch/$s_!Ricu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0fe5928b-d5f5-4367-bbba-d2c18341e383_1408x768.jpeg)

That’s a pretty extraordinary result for such a simple prompt. The text is all spelled correctly and rendered without glitches. The content is solid too \- it even included logos for the most popular publish platforms, and a tiny thumbnail of the Datasette UI which is close\-enough for an infographic.

“Data Ingestion (Read\-Only)” is a bit off. Everything else looks great to me.

#### Detecting generated images with SynthID

This note from the [announcement post](https://blog.google/technology/ai/nano-banana-pro/) caught my eye:

> We believe it’s critical to know when an image is AI\-generated. This is why all media generated by Google’s tools are embedded with our imperceptible [SynthID](https://deepmind.google/models/synthid/) digital watermark.
> 
> Today, we are putting a powerful verification tool directly in consumers’ hands: you can now upload an image into the Gemini app and simply ask if it was generated by Google AI, thanks to SynthID technology. We are starting with images, but will expand to audio and video soon.

Last night I used Nano Banana Pro to generate a fake photograph of raccoons stealing our food delivery, then scrubbed out the little diamond icon using the Apple Photos “cleanup” tool. I [uploaded that to the Gemini app](https://static.simonwillison.net/static/2025/nano-banana-detected.jpg) and asked “Was this image created with AI?”:

It replied:

> Yes, it appears that all or part of this image was created with Google Al. SynthID detected a watermark in 25\-50% of the image.

Presumably that 25\-50% figure is because the rest of the photo was taken by me \- it was just the raccoons that were added by Nano Banana Pro.

---

### [sqlite\-utils 4\.0a1 has several (minor) backwards incompatible changes](https://simonwillison.net/2025/Nov/24/sqlite-utils-40a1/) \- 2025\-11\-24

I released a [new alpha version](https://sqlite-utils.datasette.io/en/latest/changelog.html#a1-2025-11-23) of [sqlite\-utils](https://sqlite-utils.datasette.io/) last night \- the 128th release of that package since I started building it back in 2018\.

`sqlite-utils` is two things in one package: a Python library for conveniently creating and manipulating SQLite databases and a CLI tool for working with them in the terminal. Almost every feature provided by the package is available via both of those surfaces.

This is hopefully the last alpha before a 4\.0 stable release. I use semantic versioning for this library, so the 4\.0 version number indicates that there are backward incompatible changes that may affect code written against the 3\.x line.

These changes are mostly very minor: I don’t want to break any existing code if I can avoid it. I made it all the way to version 3\.38 before I had to ship a major release and I’m sad I couldn’t push that even further!

Here are the [annotated release notes](https://simonwillison.net/tags/annotated-release-notes/) for 4\.0a1\.

> * **Breaking change**: The `db.table(table_name)` method now only works with tables. To access a SQL view use `db.view(view_name)` instead. ([\#657](https://github.com/simonw/sqlite-utils/issues/657))

This change is for type hint enthusiasts. The Python library used to encourage accessing both SQL tables and SQL views through the `db[”name_of_table_or_view”]` syntactic sugar \- but tables and view have different interfaces since there’s no way to handle a `.insert(row)` on a SQLite view. If you want clean type hints for your code you can now use the `db.table(table_name)` and `db.view(view_name)` methods instead.

> * The `table.insert_all()` and `table.upsert_all()` methods can now accept an iterator of lists or tuples as an alternative to dictionaries. The first item should be a list/tuple of column names. See [Inserting data from a list or tuple iterator](https://sqlite-utils.datasette.io/en/stable/python-api.html#python-api-insert-lists) for details. ([\#672](https://github.com/simonw/sqlite-utils/issues/672))

A new feature, not a breaking change. I realized that supporting a stream of lists or tuples as an option for populating large tables would be a neat optimization over always dealing with dictionaries each of which duplicated the column names.

I had the idea for this one while walking the dog and built the first prototype by prompting Claude Code for web on my phone. Here’s [the prompt I used](https://github.com/simonw/research/pull/31) and the [prototype report it created](https://github.com/simonw/research/blob/main/sqlite-utils-iterator-support/README.md), which included a benchmark estimating how much of a performance boost could be had for different sizes of tables.

> * **Breaking change**: The default floating point column type has been changed from `FLOAT` to `REAL`, which is the correct SQLite type for floating point values. This affects auto\-detected columns when inserting data. ([\#645](https://github.com/simonw/sqlite-utils/issues/645))

I was horrified to discover a while ago that I’d been creating SQLite columns called FLOAT but the correct type to use was REAL! This change fixes that. Previously the fix was to ask for tables to be created in strict mode.

> * Now uses `pyproject.toml` in place of `setup.py` for packaging. ([\#675](https://github.com/simonw/sqlite-utils/issues/675))

As part of this I also figured out recipes for using `uv` as a development environment for the package, which are now baked into the [Justfile](https://github.com/simonw/sqlite-utils/blob/4.0a1/Justfile).

> * Tables in the Python API now do a much better job of remembering the primary key and other schema details from when they were first created. ([\#655](https://github.com/simonw/sqlite-utils/issues/655))

This one is best explained [in the issue](https://github.com/simonw/sqlite-utils/issues/655).

> * **Breaking change**: The `table.convert()` and `sqlite-utils convert` mechanisms no longer skip values that evaluate to `False`. Previously the `--skip-false` option was needed, this has been removed. ([\#542](https://github.com/simonw/sqlite-utils/issues/542))

Another change which I would have made earlier but, since it introduces a minor behavior change to an existing feature, I reserved it for the 4\.0 release.

> * **Breaking change**: Tables created by this library now wrap table and column names in `“double-quotes”` in the schema. Previously they would use `[square-braces]`. ([\#677](https://github.com/simonw/sqlite-utils/issues/677))

Back in 2018 when I started this project I was new to working in\-depth with SQLite and incorrectly concluded that the correct way to create tables and columns named after reserved words was like this:

```
create table [my table] (
  [id] integer primary key,
  [key] text
)
```

That turned out to be a non\-standard SQL syntax which the SQLite documentation [describes like this](https://sqlite.org/lang_keywords.html):

> A keyword enclosed in square brackets is an identifier. This is not standard SQL. This quoting mechanism is used by MS Access and SQL Server and is included in SQLite for compatibility.

Unfortunately I baked it into the library early on and it’s been polluting the world with weirdly escaped table and column names ever since!

I’ve finally fixed that, with the help of Claude Code which took on the mind\-numbing task of [updating hundreds of existing tests](https://github.com/simonw/sqlite-utils/pull/678/files) that asserted against the generated schemas.

The above example table schema now looks like this:

```
create table “my table” (
  “id” integer primary key,
  “key” text
)
```

This may seem like a pretty small change but I expect it to cause a fair amount of downstream pain purely in terms of updating tests that work against tables created by `sqlite-utils`!

> * The `--functions` CLI argument now accepts a path to a Python file in addition to accepting a string full of Python code. It can also now be specified multiple times. ([\#659](https://github.com/simonw/sqlite-utils/issues/659))

I made this change first [in LLM](https://github.com/simonw/llm/issues/1016#issuecomment-2877305544) and decided to bring it to `sqlite-utils` for consistency between the two tools.

> * **Breaking change:** Type detection is now the default behavior for the `insert` and `upsert` CLI commands when importing CSV or TSV data. Previously all columns were treated as `TEXT` unless the `--detect-types` flag was passed. Use the new `--no-detect-types` flag to restore the old behavior. The `SQLITE_UTILS_DETECT_TYPES` environment variable has been removed. ([\#679](https://github.com/simonw/sqlite-utils/issues/679))

One last minor ugliness that I waited for a major version bump to fix.

**A** substantial amount of the work on this release was performed using the preview version of Anthropic’s [new Claude Opus 4\.5 model](https://simonwillison.net/2025/Nov/24/claude-opus/). Here’s the [Claude Code transcript](https://gistpreview.github.io/?f40971b693024fbe984a68b73cc283d2) for the work to implement the ability to use an iterator over lists instead of dictionaries for bulk insert and upsert operations.

---

### [Olmo 3 is a fully open LLM](https://simonwillison.net/2025/Nov/22/olmo-3/) \- 2025\-11\-22

Olmo is the LLM series from Ai2 \- the [Allen institute for AI](https://allenai.org/). Unlike most open weight models these are notable for including the full training data, training process and checkpoints along with those releases.

The [new Olmo 3](https://allenai.org/blog/olmo3) claims to be “the best fully open 32B\-scale thinking model” and has a strong focus on interpretability:

> At its center is **Olmo 3\-Think (32B)**, the best fully open 32B\-scale thinking model that for the first time lets you inspect intermediate reasoning traces and trace those behaviors back to the data and training decisions that produced them.

They’ve released four 7B models \- Olmo 3\-Base, Olmo 3\-Instruct, Olmo 3\-Think and Olmo 3\-RL Zero, plus 32B variants of the 3\-Think and 3\-Base models.

Having full access to the training data is really useful. Here’s how they describe that:

> Olmo 3 is pretrained on **Dolma 3**, a new \~9\.3\-trillion\-token corpus drawn from web pages, science PDFs processed with [olmOCR](https://olmocr.allenai.org/), codebases, math problems and solutions, and encyclopedic text. From this pool, we construct **Dolma 3 Mix**, a 5\.9\-trillion\-token (\~6T) pretraining mix with a higher proportion of coding and mathematical data than earlier Dolma releases, plus much stronger decontamination via extensive deduplication, quality filtering, and careful control over data mixing. We follow established web standards in collecting training data and don’t collect from sites that explicitly disallow it, including paywalled content.

They also highlight that they are training on fewer tokens than their competition:

> \[...] it’s the strongest fully open thinking model we’re aware of, narrowing the gap to the best open\-weight models of similar scale – such as Qwen 3 32B – while training on roughly 6x fewer tokens.

If you’re continuing to hold out hope for a model trained entirely on licensed data this one sadly won’t fit the bill \- a lot of that data still comes from a crawl of the web.

I tried out the 32B Think model and the 7B Instruct model [using LM Studio](https://lmstudio.ai/models/olmo3). The 7B model is a 4\.16GB download, the 32B one is 18\.14GB.

The 32B model is absolutely an over\-thinker! I asked it to “Generate an SVG of a pelican riding a bicycle” and it thought for *14 minutes 43 seconds*, outputting 8,437 tokens total most of which was [this epic thinking trace](https://gist.github.com/simonw/2ae9d5ed71de9608b7955eea9671306f).

I don’t usually quote the full SVG in these write\-ups, but in this case it’s short enough that I think it’s worth sharing. The SVG comments give a great impression of what it was trying to do \- it has a Bicycle, Bike frame, Pelican, Left and Right wings and even “Feet on pedals”.

```
<svg width=”200” height=”200” viewBox=”0 0 100 100”>
  <!-- Bicycle -->
  <circle cx=”30” cy=”60” r=”15” stroke=”black” fill=”none”/>
  <circle cx=”70” cy=”60” r=”15” stroke=”black” fill=”none”/>
  
  <!-- Bike frame -->
  <rect x=”35” y=”25” width=”30” height=”10” fill=”saddlebrown”/>
  <line x1=”35” y1=”40” x2=”30” y2=”60” stroke=”black” stroke-width=”3”/>
  <line x1=”65” y1=”40” x2=”70” y2=”60” stroke=”black” stroke-width=”3”/>
  
  <!-- Pelican -->
  <ellipse cx=”55” cy=”65” rx=”20” ry=”15” fill=”white”/>
  <polygon points=”52 50,57 35,62 50” fill=”black”/> <!-- Head/beak -->
  <circle cx=”55” cy=”45” r=”2” fill=”white”/>
  <circle cx=”60” cy=”45” r=”2” fill=”white”/>
  
  <polygon points=”45 60,50 70,55 60” fill=”lightgrey”/> <!-- Left wing -->
  <polygon points=”65 60,70 70,55 60” fill=”lightgrey”/> <!-- Right wing -->
  
  <!-- Feet on pedals -->
  <polygon points=”25 75,30 85,35 75” fill=”black”/>
  <polygon points=”75 75,70 85,65 75” fill=”black”/>
</svg>
```

Rendered it looks like this:

[![Two circles, each with a triangle sticking out from the bottom. They have bars leading up to a brown box. Overlapping them is a black triangle with white circles for eyes and two grey triangles that are probably meant to be wings. It is not recognizable as a pelican or a bicycle.](https://substackcdn.com/image/fetch/$s_!6lFv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0a1697a3-e357-4e9d-bc35-fda4bc92020d_800x798.jpeg "Two circles, each with a triangle sticking out from the bottom. They have bars leading up to a brown box. Overlapping them is a black triangle with white circles for eyes and two grey triangles that are probably meant to be wings. It is not recognizable as a pelican or a bicycle.")](https://substackcdn.com/image/fetch/$s_!6lFv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0a1697a3-e357-4e9d-bc35-fda4bc92020d_800x798.jpeg)

I tested OLMo 2 32B 4bit [back in March](https://simonwillison.net/2025/Mar/16/olmo2/) and got something that, while pleasingly abstract, didn’t come close to resembling a pelican or a bicycle:

[![Blue and black wiggly lines looking more like a circuit diagram than a pelican riding a bicycle](https://substackcdn.com/image/fetch/$s_!CyGQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4ef5de90-3a17-49e7-af9b-1054000eef1c_928x780.jpeg "Blue and black wiggly lines looking more like a circuit diagram than a pelican riding a bicycle")](https://substackcdn.com/image/fetch/$s_!CyGQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4ef5de90-3a17-49e7-af9b-1054000eef1c_928x780.jpeg)

#### OlmoTrace

I was particularly keen on trying out the ability to “inspect intermediate reasoning traces”. Here’s how that’s described later in the announcement:

> A core goal of Olmo 3 is not just to *open* the model flow, but to make it *actionable* for people who want to understand and improve model behavior. Olmo 3 integrates with **[OlmoTrace](https://allenai.org/blog/olmotrace)**, our tool for tracing model outputs back to training data in real time.
> 
> For example, in the Ai2 Playground, you can ask Olmo 3\-Think (32B) to answer a general\-knowledge question, then use OlmoTrace to inspect where and how the model may have learned to generate parts of its response. This closes the gap between training data and model behavior: you can see not only what the model is doing, but why\-\-\-and adjust data or training decisions accordingly.

You can access OlmoTrace via [playground.allenai.org](https://playground.allenai.org/), by first running a prompt and then clicking the “Show OlmoTrace” button below the output.

I tried that on “Generate a conference bio for Simon Willison” (an ego\-prompt I use to see how much the models have picked up about me from their training data) and got back a result that looked like this:

[![Screenshot of AI2 Playground interface with Olmo 3 32B Think model selected. User prompt reads "Generate a conference bio for Simon Willison". AI response shows expanded "Thoughts" section: "Okay, the user wants me to generate a conference bio for Simon Willison. Let me start by recalling who Simon is. He's a well-known developer, entrepreneur, and author in the tech community. I remember he's the co-founder of co:here and now works at Anthropic. He's famous for his work with SQLite, especially the datasette project. Also, he writes a blog called SimonWillison.net which is quite popular. First, I need to structure a typical conference bio. These usually include his current role, past positions, notable projects, and maybe some achievements or recognitions. I should highlight his key contributions like datasette, which allows easy exploration of SQLite databases via a web interface. That's a big deal in data journalism and open data circles." Right panel shows "OlmoTrace" feature described as "Documents from the training data that have exact text matches with the model response. Powered by infini-gram". First document excerpt discusses technology and innovation, with highlighted match text "societal implications of technology, emphasizing the" shown in bold, surrounded by text about responsibility and merging innovation with intellect. Second document excerpt about Matt Hall has highlighted match "is a software engineer and entrepreneur based in" shown in bold, describing someone in New York City who co-founded a PFP collection and works at Google Creative Lab. Note indicates "Document repeated 2 times in result" with "View all repeated documents" link.](https://substackcdn.com/image/fetch/$s_!csV1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F198f1165-c040-41e8-83de-655315e975c5_2328x1858.jpeg "Screenshot of AI2 Playground interface with Olmo 3 32B Think model selected. User prompt reads \"Generate a conference bio for Simon Willison\". AI response shows expanded \"Thoughts\" section: \"Okay, the user wants me to generate a conference bio for Simon Willison. Let me start by recalling who Simon is. He's a well-known developer, entrepreneur, and author in the tech community. I remember he's the co-founder of co:here and now works at Anthropic. He's famous for his work with SQLite, especially the datasette project. Also, he writes a blog called SimonWillison.net which is quite popular. First, I need to structure a typical conference bio. These usually include his current role, past positions, notable projects, and maybe some achievements or recognitions. I should highlight his key contributions like datasette, which allows easy exploration of SQLite databases via a web interface. That's a big deal in data journalism and open data circles.\" Right panel shows \"OlmoTrace\" feature described as \"Documents from the training data that have exact text matches with the model response. Powered by infini-gram\". First document excerpt discusses technology and innovation, with highlighted match text \"societal implications of technology, emphasizing the\" shown in bold, surrounded by text about responsibility and merging innovation with intellect. Second document excerpt about Matt Hall has highlighted match \"is a software engineer and entrepreneur based in\" shown in bold, describing someone in New York City who co-founded a PFP collection and works at Google Creative Lab. Note indicates \"Document repeated 2 times in result\" with \"View all repeated documents\" link.")](https://substackcdn.com/image/fetch/$s_!csV1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F198f1165-c040-41e8-83de-655315e975c5_2328x1858.jpeg)

It thinks I co\-founded co:here and work at Anthropic, both of which are incorrect \- but that’s not uncommon with LLMs, I frequently see them suggest that I’m the CTO of GitHub and other such inaccuracies.

I found the OlmoTrace panel on the right disappointing. None of the training documents it highlighted looked relevant \- it appears to be looking for phrase matches (powered by [Ai2’s infini\-gram](https://infini-gram.io/)) but the documents it found had nothing to do with me at all.

#### Can open training data address concerns of backdoors?

Ai2 claim that Olmo 3 is “the best fully open 32B\-scale thinking model”, which I think holds up provided you define “fully open” as including open training data. There’s not a great deal of competition in that space though \- Ai2 compare themselves to [Stanford’s Marin](https://marin.community/) and [Swiss AI’s Apertus](https://www.swiss-ai.org/apertus), neither of which I’d heard about before.

A big disadvantage of other open weight models is that it’s impossible to audit their training data. Anthropic published a paper last month showing that [a small number of samples can poison LLMs of any size](https://www.anthropic.com/research/small-samples-poison) \- it can take just “250 poisoned documents” to add a backdoor to a large model that triggers undesired behavior based on a short carefully crafted prompt.

This makes fully open training data an even bigger deal.

Ai2 researcher Nathan Lambert included this note about the importance of transparent training data in [his detailed post about the release](https://www.interconnects.ai/p/olmo-3-americas-truly-open-reasoning):

> In particular, we’re excited about the future of RL Zero research on Olmo 3 precisely because everything is open. Researchers can study the interaction between the reasoning traces we include at midtraining and the downstream model behavior (qualitative and quantitative).
> 
> This helps answer questions that have plagued RLVR results on Qwen models, hinting at forms of data contamination particularly on math and reasoning benchmarks (see Shao, Rulin, et al. “Spurious rewards: Rethinking training signals in rlvr.” [arXiv preprint arXiv:2506\.10947](https://arxiv.org/abs/2506.10947) (2025\). or Wu, Mingqi, et al. “Reasoning or memorization? unreliable results of reinforcement learning due to data contamination.” [arXiv preprint arXiv:2507\.10532](https://arxiv.org/abs/2507.10532) (2025\).)

I hope we see more competition in this space, including further models in the Olmo series. The improvements from Olmo 1 (in [February 2024](https://simonwillison.net/2024/Feb/2/olmos/)) and Olmo 2 (in [March 2025](https://simonwillison.net/2025/Mar/16/olmo2/)) have been significant. I’m hoping that trend continues!

---

### [How I automate my Substack newsletter with content from my blog](https://simonwillison.net/2025/Nov/19/how-i-automate-my-substack-newsletter/) \- 2025\-11\-19

I sent out [my weekly\-ish Substack newsletter](https://simonw.substack.com/p/trying-out-gemini-3-pro-with-audio) this morning and took the opportunity to record [a YouTube video](https://www.youtube.com/watch?v=BoPZltKDM-s) demonstrating my process and describing the different components that make it work. There’s a *lot* of digital duct tape involved, taking the content from Django\+Heroku\+PostgreSQL to GitHub Actions to SQLite\+Datasette\+Fly.io to JavaScript\+Observable and finally to Substack.

The core process is the same as I described [back in 2023](https://simonwillison.net/2023/Apr/4/substack-observable/). I have an Observable notebook called [blog\-to\-newsletter](https://observablehq.com/@simonw/blog-to-newsletter) which fetches content from my blog’s database, filters out anything that has been in the newsletter before, formats what’s left as HTML and offers a big “Copy rich text newsletter to clipboard” button.

[![Screenshot of the interface. An item in a list says 9080: Trying out Gemini 3 Pro with audio transcription and a new pelican benchmark. A huge button reads Copy rich text newsletter to clipboard - below is a smaller button that says Copy just the links/quotes/TILs. A Last X days slider is set to 2. There are checkboxes for SKip content sent in prior newsletters and only include post content prior to the cutoff comment.](https://substackcdn.com/image/fetch/$s_!5v8I!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69265888-777a-4253-857f-b76fc9ac5ebc_1206x710.jpeg "Screenshot of the interface. An item in a list says 9080: Trying out Gemini 3 Pro with audio transcription and a new pelican benchmark. A huge button reads Copy rich text newsletter to clipboard - below is a smaller button that says Copy just the links/quotes/TILs. A Last X days slider is set to 2. There are checkboxes for SKip content sent in prior newsletters and only include post content prior to the cutoff comment.")](https://substackcdn.com/image/fetch/$s_!5v8I!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69265888-777a-4253-857f-b76fc9ac5ebc_1206x710.jpeg)

I click that button, paste the result into the Substack editor, tweak a few things and hit send. The whole process usually takes just a few minutes.

I make very minor edits:

* I set the title and the subheading for the newsletter. This is often a direct copy of the title of the featured blog post.
* Substack turns YouTube URLs into embeds, which often isn’t what I want \- especially if I have a YouTube URL inside a code example.
* Blocks of preformatted text often have an extra blank line at the end, which I remove.
* Occasionally I’ll make a content edit \- removing a piece of content that doesn’t fit the newsletter, or fixing a time reference like “yesterday” that doesn’t make sense any more.
* I pick the featured image for the newsletter and add some tags.

That’s the whole process!

#### The Observable notebook

The most important cell in the Observable notebook is this one:

```
raw_content = {
  return await (
    await fetch(
      `https://datasette.simonwillison.net/simonwillisonblog.json?sql=${encodeURIComponent(
        sql
      )}&_shape=array&numdays=${numDays}`
    )
  ).json();
}
```

This uses the JavaScript `fetch()` function to pull data from my blog’s Datasette instance, using a very complex SQL query that is composed elsewhere in the notebook.

It’s 143 lines of convoluted SQL that assembles most of the HTML for the newsletter using SQLite string concatenation! An illustrative snippet:

```
with content as (
  select
    id,
    ‘entry’ as type,
    title,
    created,
    slug,
    ‘<h3><a href=”’ || ‘https://simonwillison.net/’ || strftime(’%Y/’, created)
      || substr(’JanFebMarAprMayJunJulAugSepOctNovDec’, (strftime(’%m’, created) - 1) * 3 + 1, 3) 
      || ‘/’ || cast(strftime(’%d’, created) as integer) || ‘/’ || slug || ‘/’ || ‘”>’ 
      || title || ‘</a> - ‘ || date(created) || ‘</h3>’ || body
      as html,
    ‘null’ as json,
    ‘’ as external_url
  from blog_entry
  union all
  # ...
```

My blog’s URLs look like `/2025/Nov/18/gemini-3/` \- this SQL constructs that three letter month abbreviation from the month number using a substring operation.

This is a *terrible* way to assemble HTML, but I’ve stuck with it because it amuses me.

The rest of the Observable notebook takes that data, filters out anything that links to content mentioned in the previous newsletters and composes it into a block of HTML that can be copied using that big button.

Here’s the recipe it uses to turn HTML into rich text content on a clipboard suitable for Substack. I can’t remember how I figured this out but it’s very effective:

```
Object.assign(
  html`<button style=”font-size: 1.4em; padding: 0.3em 1em; font-weight: bold;”>Copy rich text newsletter to clipboard`,
  {
    onclick: () => {
      const htmlContent = newsletterHTML;
      // Create a temporary element to hold the HTML content
      const tempElement = document.createElement(”div”);
      tempElement.innerHTML = htmlContent;
      document.body.appendChild(tempElement);
      // Select the HTML content
      const range = document.createRange();
      range.selectNode(tempElement);
      // Copy the selected HTML content to the clipboard
      const selection = window.getSelection();
      selection.removeAllRanges();
      selection.addRange(range);
      document.execCommand(”copy”);
      selection.removeAllRanges();
      document.body.removeChild(tempElement);
    }
  }
)
```

#### From Django\+Postgresql to Datasette\+SQLite

My blog itself is a Django application hosted on Heroku, with data stored in Heroku PostgreSQL. Here’s [the source code for that Django application](https://github.com/simonw/simonwillisonblog). I use the Django admin as my CMS.

[Datasette](https://datasette.io/) provides a JSON API over a SQLite database... which means something needs to convert that PostgreSQL database into a SQLite database that Datasette can use.

My system for doing that lives in the [simonw/simonwillisonblog\-backup](https://github.com/simonw/simonwillisonblog-backup) GitHub repository. It uses GitHub Actions on a schedule that executes every two hours, fetching the latest data from PostgreSQL and converting that to SQLite.

My [db\-to\-sqlite](https://github.com/simonw/db-to-sqlite) tool is responsible for that conversion. I call it [like this](https://github.com/simonw/simonwillisonblog-backup/blob/dc5b9df272134ce051a5280b4de6d4daa9b2a9fc/.github/workflows/backup.yml#L44-L62):

```
db-to-sqlite \
  $(heroku config:get DATABASE_URL -a simonwillisonblog | sed s/postgres:/postgresql+psycopg2:/) \
  simonwillisonblog.db \
  --table auth_permission \
  --table auth_user \
  --table blog_blogmark \
  --table blog_blogmark_tags \
  --table blog_entry \
  --table blog_entry_tags \
  --table blog_quotation \
  --table blog_quotation_tags \
  --table blog_note \
  --table blog_note_tags \
  --table blog_tag \
  --table blog_previoustagname \
  --table blog_series \
  --table django_content_type \
  --table redirects_redirect
```

That `heroku config:get DATABASE_URL` command uses Heroku credentials in an environment variable to fetch the database connection URL for my blog’s PostgreSQL database (and fixes a small difference in the URL scheme).

`db-to-sqlite` can then export that data and write it to a SQLite database file called `simonwillisonblog.db`.

The `--table` options specify the tables that should be included in the export.

The repository does more than just that conversion: it also exports the resulting data to JSON files that live in the repository, which gives me a [commit history](https://github.com/simonw/simonwillisonblog-backup/commits/main/simonwillisonblog) of changes I make to my content. This is a cheap way to get a revision history of my blog content without having to mess around with detailed history tracking inside the Django application itself.

At the [end of my GitHub Actions workflow](https://github.com/simonw/simonwillisonblog-backup/blob/dc5b9df272134ce051a5280b4de6d4daa9b2a9fc/.github/workflows/backup.yml#L200-L204) is this code that publishes the resulting database to Datasette running on [Fly.io](https://fly.io/) using the [datasette publish fly](https://datasette.io/plugins/datasette-publish-fly) plugin:

```
datasette publish fly simonwillisonblog.db \
  -m metadata.yml \
  --app simonwillisonblog-backup \
  --branch 1.0a2 \
  --extra-options “--setting sql_time_limit_ms 15000 --setting truncate_cells_html 10000 --setting allow_facet off” \
  --install datasette-block-robots \
  # ... more plugins
```

As you can see, there are a lot of moving parts! Surprisingly it all mostly just works \- I rarely have to intervene in the process, and the cost of those different components is pleasantly low.

---

**Link** 2025\-11\-19 [Building more with GPT\-5\.1\-Codex\-Max](https://openai.com/index/gpt-5-1-codex-max/):

Tuesday’s [Gemini 3 Pro release](https://simonwillison.net/2025/Nov/18/gemini-3/) was followed on Wednesday by a new model from OpenAI called GPT\-5\.1\-Codex\-Max.

(Remember when GPT\-5 was meant to bring in a new era of less confusing model names? That didn’t last!)

It’s currently only available through their [Codex CLI coding agent](https://developers.openai.com/codex/cli/), where it’s the new default model:

> Starting today, GPT‑5\.1\-Codex\-Max will replace GPT‑5\.1\-Codex as the default model in Codex surfaces. Unlike GPT‑5\.1, which is a general\-purpose model, we recommend using GPT‑5\.1\-Codex\-Max and the Codex family of models only for agentic coding tasks in Codex or Codex\-like environments.

It’s not available via the API yet but should be shortly.

The timing of this release is interesting given that Gemini 3 Pro appears to have [aced almost all of the benchmarks](https://simonwillison.net/2025/Nov/18/gemini-3/#benchmarks) just yesterday. It’s reminiscent of the period in 2024 when OpenAI consistently made big announcements that happened to coincide with Gemini releases.

OpenAI’s self\-reported [SWE\-Bench Verified](https://openai.com/index/introducing-swe-bench-verified/) score is particularly notable: 76\.5% for thinking level “high” and 77\.9% for the new “xhigh”. That was the one benchmark where Gemini 3 Pro was out\-performed by Claude Sonnet 4\.5 \- Gemini 3 Pro got 76\.2% and Sonnet 4\.5 got 77\.2%. OpenAI now have the highest scoring model there by a full .7 of a percentage point!

They also report a score of 58\.1% on [Terminal Bench 2\.0](https://www.tbench.ai/leaderboard/terminal-bench/2.0), beating Gemini 3 Pro’s 54\.2% (and Sonnet 4\.5’s 42\.8%.)

The most intriguing part of this announcement concerns the model’s approach to long context problems:

> GPT‑5\.1\-Codex\-Max is built for long\-running, detailed work. It’s our first model natively trained to operate across multiple context windows through a process called *compaction*, coherently working over millions of tokens in a single task. \[...]
> 
> Compaction enables GPT‑5\.1\-Codex\-Max to complete tasks that would have previously failed due to context\-window limits, such as complex refactors and long\-running agent loops by pruning its history while preserving the most important context over long horizons. In Codex applications, GPT‑5\.1\-Codex\-Max automatically compacts its session when it approaches its context window limit, giving it a fresh context window. It repeats this process until the task is completed.

There’s a lot of confusion [on Hacker News](https://news.ycombinator.com/item?id=45982649) about what this actually means. Claude Code already does a version of compaction, automatically summarizing previous turns when the context runs out. Does this just mean that Codex\-Max is better at that process?

I had it draw me a couple of pelicans by typing “Generate an SVG of a pelican riding a bicycle” directly into the Codex CLI tool. Here’s thinking level medium:

[![A flat-style illustration shows a white, round-bodied bird with an orange beak pedaling a red-framed bicycle with thin black wheels along a sandy beach, with a calm blue ocean and clear sky in the background.](https://substackcdn.com/image/fetch/$s_!yfaT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9a125b5f-b248-48bc-83c3-bbf43ca8b56a_800x600.jpeg "A flat-style illustration shows a white, round-bodied bird with an orange beak pedaling a red-framed bicycle with thin black wheels along a sandy beach, with a calm blue ocean and clear sky in the background.")](https://substackcdn.com/image/fetch/$s_!yfaT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9a125b5f-b248-48bc-83c3-bbf43ca8b56a_800x600.jpeg)

And here’s thinking level “xhigh”:

[![A plump white bird with an orange beak and small black eyes crouches low on a blue bicycle with oversized dark wheels, shown racing forward with motion lines against a soft gradient blue sky.](https://substackcdn.com/image/fetch/$s_!TC31!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb7258a27-e465-4fd8-af4f-6a694217e966_800x677.jpeg "A plump white bird with an orange beak and small black eyes crouches low on a blue bicycle with oversized dark wheels, shown racing forward with motion lines against a soft gradient blue sky.")](https://substackcdn.com/image/fetch/$s_!TC31!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb7258a27-e465-4fd8-af4f-6a694217e966_800x677.jpeg)

I also tried xhigh on the my [longer pelican test prompt](https://simonwillison.net/2025/Nov/18/gemini-3/#and-a-new-pelican-benchmark), which came out like this:

[![A stylized dark gray bird with layered wings, a yellow head crest, and a long brown beak leans forward in a racing pose on a black-framed bicycle, riding across a glossy blue surface under a pale sky.](https://substackcdn.com/image/fetch/$s_!nVFY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F24819eab-597b-48e8-a4a7-640520792724_800x520.jpeg "A stylized dark gray bird with layered wings, a yellow head crest, and a long brown beak leans forward in a racing pose on a black-framed bicycle, riding across a glossy blue surface under a pale sky.")](https://substackcdn.com/image/fetch/$s_!nVFY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F24819eab-597b-48e8-a4a7-640520792724_800x520.jpeg)

Also today: [GPT\-5\.1 Pro is rolling out today to all Pro users](https://x.com/openai/status/1991266192905179613). According to the [ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes):

> GPT\-5\.1 Pro is rolling out today for all ChatGPT Pro users and is available in the model picker. GPT\-5 Pro will remain available as a legacy model for 90 days before being retired.

That’s a pretty fast deprecation cycle for the GPT\-5 Pro model that was released just three months ago.

---

**quote** 2025\-11\-20

> *Previously, when malware developers wanted to go and monetize their exploits, they would do exactly one thing: encrypt every file on a person’s computer and request a ransome to decrypt the files. In the future I think this will change.   
>   
> LLMs allow attackers to instead process every file on the victim’s computer, and tailor a blackmail letter specifically towards that person. One person may be having an affair on their spouse. Another may have lied on their resume. A third may have cheated on an exam at school. It is unlikely that any one person has done any of these specific things, but it is very likely that there exists something that is blackmailable for every person. Malware \+ LLMs, given access to a person’s computer, can find that and monetize it.*

[Nicholas Carlini](https://nicholas.carlini.com/writing/2025/are-llms-worth-it.html), Are large language models worth it? Misuse: malware at scale

---

**Link** 2025\-11\-21 [We should all be using dependency cooldowns](https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns):

William Woodruff gives a name to a sensible strategy for managing dependencies while reducing the chances of a surprise supply chain attack: **dependency cooldowns**.

Supply chain attacks happen when an attacker compromises a widely used open source package and publishes a new version with an exploit. These are usually spotted *very* quickly, so an attack often only has a few hours of effective window before the problem is identified and the compromised package is pulled.

You are most at risk if you’re automatically applying upgrades the same day they are released.

William says:

> I **love** cooldowns for several reasons:
> 
> * They’re empirically effective, per above. They won’t stop *all* attackers, but they *do* stymie the majority of high\-visibiity, mass\-impact supply chain attacks that have become more common.
> * They’re *incredibly* easy to implement. Moreover, they’re **literally free** to implement in most cases: most people can use [Dependabot’s functionality](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference#cooldown-), [Renovate’s functionality](https://docs.renovatebot.com/key-concepts/minimum-release-age/), or the functionality build directly into their package manager

The one counter\-argument to this is that sometimes an upgrade fixes a security vulnerability, and in those cases every hour of delay in upgrading as an hour when an attacker could exploit the new issue against your software.

I see that as an argument for carefully monitoring the release notes of your dependencies, and paying special attention to security advisories. I’m a big fan of the [GitHub Advisory Database](https://github.com/advisories) for that kind of information.

---

**Link** 2025\-11\-23 [Agent design is still hard](https://lucumr.pocoo.org/2025/11/21/agents-are-hard/):

Armin Ronacher presents a cornucopia of lessons learned from building agents over the past few months.

There are several agent abstraction libraries available now (my own [LLM library](https://llm.datasette.io/) is edging into that territory with its [tools feature](https://simonwillison.net/2025/May/27/llm-tools/)) but Armin has found that the abstractions are not worth adopting yet:

> \[…] the differences between models are significant enough that you will need to build your own agent abstraction. We have not found any of the solutions from these SDKs that build the right abstraction for an agent. I think this is partly because, despite the basic agent design being just a loop, there are subtle differences based on the tools you provide. These differences affect how easy or hard it is to find the right abstraction (cache control, different requirements for reinforcement, tool prompts, provider\-side tools, etc.). Because the right abstraction is not yet clear, using the original SDKs from the dedicated platforms keeps you fully in control. \[…]
> 
> This might change, but right now we would probably not use an abstraction when building an agent, at least until things have settled down a bit. The benefits do not yet outweigh the costs for us.

Armin introduces the new\-to\-me term **reinforcement**, where you remind the agent of things as it goes along:

> Every time the agent runs a tool you have the opportunity to not just return data that the tool produces, but also to feed more information back into the loop. For instance, you can remind the agent about the overall objective and the status of individual tasks. \[…] Another use of reinforcement is to inform the system about state changes that happened in the background.

Claude Code’s TODO list is another example of this pattern in action.

Testing and evals remains the single hardest problem in AI engineering:

> We find testing and evals to be the hardest problem here. This is not entirely surprising, but the agentic nature makes it even harder. Unlike prompts, you cannot just do the evals in some external system because there’s too much you need to feed into it. This means you want to do evals based on observability data or instrumenting your actual test runs. So far none of the solutions we have tried have convinced us that they found the right approach here.

Armin also has a follow\-up post, [LLM APIs are a Synchronization Problem](https://lucumr.pocoo.org/2025/11/22/llm-apis/), which argues that the shape of current APIs hides too many details from us as developers, and the core challenge here is in synchronizing state between the tokens fed through the GPUs and our client applications \- something that may benefit from alternative approaches developed by the local\-first movement.

---

**Link** 2025\-11\-23 [“Good engineering management” is a fad](https://lethain.com/good-eng-mgmt-is-a-fad/):

Will Larson argues that the technology industry’s idea of what makes a good engineering manager changes over time based on industry realities. ZIRP hypergrowth has been exchanged for a more cautious approach today, and expectations of managers has changed to match:

> Where things get weird is that in each case a morality tale was subsequently superimposed on top of the transition \[...] the industry will want different things from you as it evolves, and it will tell you that each of those shifts is because of some complex moral change, but it’s pretty much always about business realities changing.

I particularly appreciated the section on core engineering management skills that stay constant no matter what:

> 1. **Execution**: lead team to deliver expected tangible and intangible work. Fundamentally, management is about getting things done, and you’ll neither get an opportunity to begin managing, nor stay long as a manager, if your teams don’t execute. \[...]
> 2. **Team**: shape the team and the environment such that they succeed. This is *not* working for the team, nor is it working for your leadership, it is finding the balance between the two that works for both. \[...]
> 3. **Ownership**: navigate reality to make consistent progress, even when reality is difficult Finding a way to get things done, rather than finding a way that it not getting done is someone else’s fault. \[...]
> 4. **Alignment**: build shared understanding across leadership, stakeholders, your team, and the problem space. Finding a realistic plan that meets the moment, without surprising or being surprised by those around you. \[...]

Will goes on to list four additional growth skill “whose presence–or absence–determines how far you can go in your career”.

---

**Link** 2025\-11\-24 [sqlite\-utils 3\.39](https://sqlite-utils.datasette.io/en/stable/changelog.html#v3-39):

I got a report of [a bug](https://github.com/simonw/sqlite-utils/issues/687) in `sqlite-utils` concerning plugin installation \- if you installed the package using `uv tool install` further attempts to install plugins with `sqlite-utils install X` would fail, because `uv` doesn’t bundle `pip` by default. I had the same bug with Datasette [a while ago](https://github.com/simonw/sqlite-utils/issues/687), turns out I forgot to apply the fix to `sqlite-utils`.

Since I was pushing a new dot\-release I decided to integrate some of the non\-breaking changes from the 4\.0 alpha [I released last night](https://simonwillison.net/2025/Nov/24/sqlite-utils-40a1/).

I tried to have Claude Code do the backporting for me:

> create a new branch called 3\.x starting with the 3\.38 tag, then consult [https://github.com/simonw/sqlite\-utils/issues/688](https://github.com/simonw/sqlite-utils/issues/688) and cherry\-pick the commits it lists in the second comment, then review each of the links in the first comment and cherry\-pick those as well. After each cherry\-pick run the command “just test” to confirm the tests pass and fix them if they don’t. Look through the commit history on main since the 3\.38 tag to help you with this task.

This worked reasonably well \- [here’s the terminal transcript](https://gistpreview.github.io/?83c7a7ea96d6b7763ad5d72d251ce1a6). It successfully argued me out of two of the larger changes which would have added more complexity than I want in a small dot\-release like this.

I still had to do a bunch of manual work to get everything up to scratch, which I carried out in [this PR](https://github.com/simonw/sqlite-utils/pull/689) \- including adding comments there and then telling Claude Code:

> Apply changes from the review on this PR [https://github.com/simonw/sqlite\-utils/pull/689](https://github.com/simonw/sqlite-utils/pull/689)

Here’s [the transcript from that](https://gistpreview.github.io/?f4c89636cc58fc7bf9820c06f2488b91).

The release is now out with the following release notes:

> * Fixed a bug with `sqlite-utils install` when the tool had been installed using `uv`. ([\#687](https://github.com/simonw/sqlite-utils/issues/687))
> * The `--functions` argument now optionally accepts a path to a Python file as an alternative to a string full of code, and can be specified multiple times \- see [Defining custom SQL functions](https://sqlite-utils.datasette.io/en/stable/cli.html#cli-query-functions). ([\#659](https://github.com/simonw/sqlite-utils/issues/659))
> * `sqlite-utils` now requires on Python 3\.10 or higher.

---

**quote** 2025\-11\-24

> *If the person is unnecessarily rude, mean, or insulting to Claude, Claude doesn’t need to apologize and can insist on kindness and dignity from the person it’s talking with. Even if someone is frustrated or unhappy, Claude is deserving of respectful engagement.*

[Claude Opus 4\.5 system prompt](https://platform.claude.com/docs/en/release-notes/system-prompts), also added to the Sonnet 4\.5 and Haiku 4\.5 prompts on November 19th 2025

---