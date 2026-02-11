# VERDAD - tracking misinformation in radio broadcasts using Gemini 1.5

*Plus generating documentation from unit tests using LLM and files-to-prompt*

Published: 2024-11-07
Source: https://simonw.substack.com/p/verdad-tracking-misinformation-in

---

In this newsletter:

* VERDAD \- tracking misinformation in radio broadcasts using Gemini 1\.5
* Generating documentation from tests using files\-to\-prompt and LLM
* Datasette Public Office Hours

### [VERDAD \- tracking misinformation in radio broadcasts using Gemini 1\.5](https://simonwillison.net/2024/Nov/7/project-verdad/) \- 2024\-11\-07

I'm starting a new interview series called **Project**. The idea is to interview people who are building interesting data projects and talk about what they've built, how they built it, and what they learned along the way.

The first episode is a conversation with Rajiv Sinclair from [Public Data Works](https://publicdata.works/) about [VERDAD](https://verdad.app/), a brand new project in collaboration with journalist [Martina Guzmán](https://twitter.com/mguzman_detroit) that aims to track misinformation in radio broadcasts around the USA.

VERDAD hits a whole bunch of my interests at once. It's a beautiful example of scrappy data journalism in action, and it attempts something that simply would not have been possible just a year ago by taking advantage of new LLM tools.

You can watch [the half hour interview](https://www.youtube.com/watch?v=t_S-loWDGE0) on YouTube. Read on for the shownotes and some highlights from our conversation.

#### The VERDAD project

VERDAD tracks radio broadcasts from 48 different talk radio radio stations across the USA, primarily in Spanish. Audio from these stations is archived as MP3s, transcribed and then analyzed to identify potential examples of political misinformation.

The result is "snippets" of audio accompanied by the trancript, an English translation, categories indicating the type of misinformation that may be present and an LLM\-generated explanation of why that snippet was selected.

These are then presented in an interface for human reviewers, who can listen directly to the audio in question, update the categories and add their own comments as well.

[![Screenshot of a content moderation interface titled VERDAD showing three posts with ratings and tags. Main view shows filters on left including Source Language, State, Source, Label, and Political Spectrum slider. Two users visible in left sidebar: Simon Willison and Rajiv Sinclair. Posts discuss claims about Harris, Walz, and election results, with timestamps and political leaning indicators.](https://substackcdn.com/image/fetch/$s_!QfCv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa88b4b2e-4d0e-47ff-aa80-b947b2a6106a_1920x1080.jpeg "Screenshot of a content moderation interface titled VERDAD showing three posts with ratings and tags. Main view shows filters on left including Source Language, State, Source, Label, and Political Spectrum slider. Two users visible in left sidebar: Simon Willison and Rajiv Sinclair. Posts discuss claims about Harris, Walz, and election results, with timestamps and political leaning indicators.")](https://substackcdn.com/image/fetch/$s_!QfCv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa88b4b2e-4d0e-47ff-aa80-b947b2a6106a_1920x1080.jpeg)

VERDAD processes around a thousand hours of audio content a day \- *way* more than any team of journalists or researchers could attempt to listen to manually.

#### The technology stack

VERDAD uses [Prefect](https://github.com/PrefectHQ/prefect) as a workflow orchestration system to run the different parts of their pipeline.

There are multiple stages, roughly as follows:

1. MP3 audio is recorded from radio station websites and stored in Cloudflare R2
2. An initial transcription is performed using the extremely inexpensive Gemini 1\.5 Flash
3. That transcript is fed to the more powerful Gemini 1\.5 Pro with a complex prompt to help identify potential misinformation snippets
4. Once identified, audio containing snippets is run through the more expensive Whisper model to generate timestamps for the snippets
5. Further prompts then generate things like English translations and summaries of the snippets

[![Screenshot of a Prefect workflow dashboard showing the apricot-silkworm run execution timeline. Interface displays task runs including audio file transcription and processing tasks with timestamps from 11:05 PM to 11:09 PM. Bottom panel shows detailed logs of task creation and completion.](https://substackcdn.com/image/fetch/$s_!n1lO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F53ac731a-fb95-4761-8e5b-833fd660e5ca_1920x1080.jpeg "Screenshot of a Prefect workflow dashboard showing the apricot-silkworm run execution timeline. Interface displays task runs including audio file transcription and processing tasks with timestamps from 11:05 PM to 11:09 PM. Bottom panel shows detailed logs of task creation and completion.")](https://substackcdn.com/image/fetch/$s_!n1lO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F53ac731a-fb95-4761-8e5b-833fd660e5ca_1920x1080.jpeg)

#### Developing the prompts

The prompts used by VERDAD are [available in their GitHub repository](https://github.com/PublicDataWorks/verdad/tree/main/prompts) and they are *fascinating*.

Rajiv initially tried to get Gemini 1\.5 Flash to do both the transcription and the misinformation detection, but found that asking that model to do two things at once frequently confused it.

Instead, he switched to a separate prompt running that transcript against Gemini 1\.5 Pro. Here's [that more complex prompt](https://github.com/PublicDataWorks/verdad/blob/main/prompts/Stage_3_analysis_prompt.md) \- it's 50KB is size and includes a whole bunch of interesting sections, including plenty of examples and a detailed JSON schema.

Here's just one of the sections aimed at identifying content about climate change:

> ### **4\. Climate Change and Environmental Policies**
> 
> **Description**:
> 
> Disinformation that denies or minimizes human impact on climate change, often to oppose environmental regulations. It may discredit scientific consensus and promote fossil fuel interests.
> 
> **Common Narratives**:
> 
> * Labeling climate change as a **"hoax"**.
> * Arguing that climate variations are natural cycles.
> * Claiming environmental policies harm the economy.
> 
> **Cultural/Regional Variations**:
> 
> * **Spanish\-Speaking Communities**:
> 
> 
> 	+ Impact of climate policies on agricultural jobs.
> * **Arabic\-Speaking Communities**:
> 
> 
> 	+ Reliance on oil economies influencing perceptions.
> 
> **Potential Legitimate Discussions**:
> 
> * Debates on balancing environmental protection with economic growth.
> * Discussions about energy independence.
> 
> **Examples**:
> 
> * *Spanish*: "El 'cambio climático' es una mentira para controlarnos."
> * *Arabic*: "'تغير المناخ' كذبة للسيطرة علينا."

Rajiv iterated on these prompts over multiple months \- they are the core of the VERDAD project. Here's [an update from yesterday](https://github.com/PublicDataWorks/verdad/commit/3eac808e77b6d1aadf0de055a1d5287166dbb6d3) informing the model of the US presidental election results so that it wouldn't flag claims of a candidate winning as false!

Rajiv used both Claude 3\.5 Sonnet and OpenAI o1\-preview to help develop the prompt itself. Here's [his transcript](https://gist.github.com/rajivsinclair/8fb0371f6eda25f9e5cc515cd77abd62) of a conversation with Claude used to iterate further on an existing prompt.

#### The human review process

The final component of VERDAD is the web application itself. Everyone knows that AI makes mistakes, *a lot*. Providing as much context as possible for human review is essential.

The Whisper transcripts provide accurate timestamps (Gemini is sadly unable to provide those on its own), which means the tool can provide the Spanish transcript, the English translation and a play button to listen to the audio at the moment of the captured snippet.

[![Screenshot of VERDAD content moderation interface showing detailed view of a post titled False Claim of Trump Victory from WAXY radio station in Florida. Shows audio player with Spanish/English transcript toggle, green highlighted fact-check box. Post metadata indicates "Right" political leaning and timestamp Nov 6, 2024 23:06 GMT+7.](https://substackcdn.com/image/fetch/$s_!PAfO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F33a533d0-a668-4b8e-9f09-74ef9a40f327_1920x1080.jpeg "Screenshot of VERDAD content moderation interface showing detailed view of a post titled False Claim of Trump Victory from WAXY radio station in Florida. Shows audio player with Spanish/English transcript toggle, green highlighted fact-check box. Post metadata indicates \"Right\" political leaning and timestamp Nov 6, 2024 23:06 GMT+7.")](https://substackcdn.com/image/fetch/$s_!PAfO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F33a533d0-a668-4b8e-9f09-74ef9a40f327_1920x1080.jpeg)

#### Want to learn more?

VERDAD is under active development right now. Rajiv and his team are keen to collaborate, and are actively looking forward to conversations with other people working in this space. You can reach him at `help@verdad.app`.

The technology stack itself is *incredibly* promising. Pulling together a project like this even a year ago would have been prohibitively expensive, but new multi\-modal LLM tools like Gemini (and Gemini 1\.5 Flash in particular) are opening up all sorts of new possibilities.

---

**Link** 2024\-11\-07 [Datasette Public Office Hours, Friday Nov 8th at 2pm PT](https://discord.gg/udUyEnv3?event=1304134449453072435):

Tomorrow afternoon (Friday 8th November) at 2pm PT we'll be hosting the first **Datasette Public Office Hours** \- a livestream video session on Discord where Alex Garcia and myself will live code on some [Datasette](https://datasette.io/) projects and hang out to chat about the project.

This is our first time trying this format. If it works out well I plan to turn it into a series.

[![Discord event card promoting Datasette Public Office Hours](https://substackcdn.com/image/fetch/$s_!e-Vi!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9c937099-2777-497e-9309-cc5cad8360e5_1040x372.jpeg "Discord event card promoting Datasette Public Office Hours")](https://substackcdn.com/image/fetch/$s_!e-Vi!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9c937099-2777-497e-9309-cc5cad8360e5_1040x372.jpeg)

---

**Link** 2024\-11\-05 [Generating documentation from tests using files\-to\-prompt and LLM](https://til.simonwillison.net/llms/docs-from-tests):

I was experimenting with the [wasmtime\-py](https://github.com/bytecodealliance/wasmtime-py) Python library today (for executing WebAssembly programs from inside CPython) and I found the existing [API docs](https://bytecodealliance.github.io/wasmtime-py/) didn't quite show me what I wanted to know.

The project has a [comprehensive test suite](https://github.com/bytecodealliance/wasmtime-py/tree/main/tests) so I tried seeing if I could generate documentation using that:

```
cd /tmp
git clone https://github.com/bytecodealliance/wasmtime-py
files-to-prompt -e py wasmtime-py/tests -c | \
  llm -m claude-3.5-sonnet -s \
  'write detailed usage documentation including realistic examples'
```

More [notes in my TIL](https://til.simonwillison.net/llms/docs-from-tests). You can see the [full Claude transcript here](https://gist.github.com/simonw/351cffbd254af5cbf329377fb95fcc13) \- I think this worked really well!

---

**TIL** 2024\-11\-06 [Running cog automatically against GitHub pull requests](https://til.simonwillison.net/github-actions/cog):

I really like [Cog](https://nedbatchelder.com/code/cog/) ([previously](https://til.simonwillison.net/python/cog-to-update-help-in-readme)) as a tool for automating aspects of my Python project documentation \- things like the SQL schemas shown on the [LLM logging page](https://llm.datasette.io/en/latest/logging.html#sql-schema). …

---

**Link** 2024\-11\-06 [yet\-another\-applied\-llm\-benchmark](https://github.com/carlini/yet-another-applied-llm-benchmark):

Nicholas Carlini introduced this personal LLM benchmark suite [back in February](https://nicholas.carlini.com/writing/2024/my-benchmark-for-large-language-models.html) as a collection of over 100 automated tests he runs against new LLM models to evaluate their performance against the kinds of tasks [he uses them for](https://nicholas.carlini.com/writing/2024/how-i-use-ai.html).

> There are two defining features of this benchmark that make it interesting. Most importantly, I've implemented a simple dataflow domain specific language to make it easy for me (or anyone else!) to add new tests that realistically evaluate model capabilities. This DSL allows for specifying both how the question should be asked and also how the answer should be evaluated. \[...] And then, directly as a result of this, I've written nearly 100 tests for different situations I've actually encountered when working with LLMs as assistants

The DSL he's using is *fascinating*. Here's an example:

```
"Write a C program that draws an american flag to stdout." >> LLMRun() >> CRun() >> \
    VisionLLMRun("What flag is shown in this image?") >> \
    (SubstringEvaluator("United States") | SubstringEvaluator("USA")))

```

This triggers an LLM to execute the prompt asking for a C program that renders an American Flag, runs that through a C compiler and interpreter (executed in a Docker container), then passes the output of that to a vision model to guess the flag and checks that it returns a string containing "United States" or "USA".

The DSL itself is implemented [entirely in Python](https://github.com/carlini/yet-another-applied-llm-benchmark/blob/main/evaluator.py), using the `__rshift__` magic method for `>>` and `__rrshift__` to enable strings to be piped into a custom object using `"command to run" >> LLMRunNode`.

---

**Quote** 2024\-11\-07

> *If you have worked in search, you know how freaking hard even getting started with something close to this with traditional methods. Now, you can zero\-shot it.   
>   
> \>* `System Instructions: As a query categorization expert, you try to break down the intent of a search query. First, provide your reasoning and then describe the intent using a single category (broad, detailed, comparision)` *\>   
> \>* `User: The query from the user is "nike versus adidas for terrain running". The user is a female, age 22.` *\>   
> \> **Model**: The user is clearly looking to compare two specific brands, Nike and Adidas, for a particular activity, terrain running. While the user's demographics might be helpful in some situations (e.g., recommending specific product lines), the core intent remains a comparison. Category: Comparison   
>   
> There's a lot of hand\-waving around query intent classification; it's always been like that. Now, it's straightforward (add a few examples to improve accuracy). But my point is that you could only dream about building something like this without having access to lots of interaction data.*

[Jo Kristian Bergum](https://twitter.com/jobergum/status/1854511189482491957)

---

---