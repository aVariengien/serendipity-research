# Datasette 1.0a14: The annotated release notes

*Plus notes on how Apple and NVIDIA have been training their latest models*

Published: 2024-08-05
Source: https://simonw.substack.com/p/datasette-10a14-the-annotated-release

---

In this newsletter:

* Datasette 1\.0a14: The annotated release notes

Plus 34 links and 10 quotations and 3 TILs

### [Datasette 1\.0a14: The annotated release notes](https://simonwillison.net/2024/Aug/5/datasette-1a14/) \- 2024\-08\-05

Released today: [Datasette 1\.0a14](https://docs.datasette.io/en/1.0a14/changelog.html#a14-2024-08-05). This alpha includes significant contributions from [Alex Garcia](https://alexgarcia.xyz/), including some backwards\-incompatible changes in the run\-up to the 1\.0 release.

* [Metadata now lives in a database](https://observablehq.com/@simonw/blog-to-newsletter#metadata-now-lives-in-a-database)
* [datasette\-remote\-metadata 0\.2a0](https://observablehq.com/@simonw/blog-to-newsletter#datasette-remote-metadata-0-2a0)
* [SQLite isolation\_level\="IMMEDIATE"](https://observablehq.com/@simonw/blog-to-newsletter#sqlite-isolation-level-immediate-)
* [Updating the URLs](https://observablehq.com/@simonw/blog-to-newsletter#updating-the-urls)
* [Everything else](https://observablehq.com/@simonw/blog-to-newsletter#everything-else)
* [Tricks to help construct the release notes](https://observablehq.com/@simonw/blog-to-newsletter#tricks-to-help-construct-the-release-notes)

#### Metadata now lives in a database

The biggest change in the alpha concerns how Datasette's [metadata system](https://docs.datasette.io/en/latest/metadata.html#metadata) works.

Datasette can record and serve metadata about the databases, tables and columns that it is serving. This includes things like the source of the data, the license it is made available under and descriptions of the tables and columns.

Historically this has been powered by a `metadata.json` file. Over time, this file grew to include all sorts of things that weren't strictly metadata \- things like plugin configuration. Cleaning this up is a major breaking change for Datasette 1\.0, and Alex has been working on this across several alphas.

The latest alpha adds a new [upgrade guide](https://docs.datasette.io/en/1.0a14/upgrade_guide.html) describing changes plugin authors will need to make to support the new metadata system.

The big change in 1\.0a14 is that metadata now lives in Datasette's hidden `_internal` SQLite database, in four new tables called `metadata_instance`, `metadata_databases`, `metadata_resources` and `metadata_columns`. The schema for these [is now included in the documentation](https://docs.datasette.io/en/1.0a14/internals.html#datasette-s-internal-database) (updated [using this Cog code](https://github.com/simonw/datasette/blob/f6bd2bf8b025dcee49248ae7224e242b448f558c/docs/internals.rst?plain=1#L1363-L1366)), but rather than accessing those tables directly plugins are encouraged to use the new [set\_\*\_metadata() and get\_\*\_metadata() methods](https://docs.datasette.io/en/1.0a14/internals.html#getting-and-setting-metadata) on the `Datasette` class.

I plan to use these new tables to build a new performant, paginated homepage that shows all of the databases and tables that Datasette is serving, complete with their metadata \- without needing to make potentially hundreds of calls to the now\-removed `get_metadata()` plugin hook.

#### datasette\-remote\-metadata 0\.2a0

When introducing new plugin internals like this it's always good to accompany them with a plugin that exercises them. **[datasette\-remote\-metadata](https://github.com/simonw/datasette-remote-metadata)** is a few years old now, and provides a mechanism for hosting the metadata for a Datasette instance at a separate URL. This means you can deploy a stateless Datasette instance with a large database and then without having to re\-deploy the whole thing.

I released [a new alpha](https://github.com/simonw/datasette-remote-metadata/releases/tag/0.2a0) of that plugin which [switches over to the new metadata mechanism](https://github.com/simonw/datasette-remote-metadata/issues/4). The core code ended up looking like this, imitating [code Alex wrote](https://github.com/simonw/datasette/blob/f6bd2bf8/datasette/app.py#L446-L472) for Datasette Core:

```
async def apply_metadata(datasette, metadata_dict):
    for key in metadata_dict or {}:
        if key == "databases":
            continue
        await datasette.set_instance_metadata(key, metadata_dict[key])
    # database-level
    for dbname, db in metadata_dict.get("databases", {}).items():
        for key, value in db.items():
            if key == "tables":
                continue
            await datasette.set_database_metadata(dbname, key, value)
        # table-level
        for tablename, table in db.get("tables", {}).items():
            for key, value in table.items():
                if key == "columns":
                    continue
                await datasette.set_resource_metadata(dbname, tablename, key, value)
            # column-level
            for columnname, column_description in table.get("columns", {}).items():
                await datasette.set_column_metadata(
                    dbname, tablename, columnname, "description", column_description
                )
```

#### SQLite isolation\_level\="IMMEDIATE"

Sylvain Kerkour wrote about the [benefits of IMMEDIATE transactions](https://kerkour.com/sqlite-for-servers#use-immediate-transactions) back in February. The key issue here is that SQLite defaults to starting transactions in `DEFERRED` mode, which can lead to `SQLITE_BUSY` errors if a transaction is upgraded to a write transaction mid\-flight. Starting in `IMMEDIATE` mode for Datasette's dedicated write connection should help avoid this.

Frustratingly I [failed to replicate](https://github.com/simonw/datasette/issues/2358) the underlying problem in my own tests, despite having anecdotally seen it happen in the past.

After spending more time than I had budgeted for on this, I decided to ship it as an alpha to get it properly exercised before the 1\.0 stable release.

#### Updating the URLs

Here's another change that was important to get out before 1\.0\.

Datasette's URL design had a subtle blemish. The following page had two potential meanings:

* `/databasename` \- list all of the tables in the specified database
* `/databasename?sql=` \- execute an arbitrary SQL query against that database

This also meant that the JSON structure returned by `/database.json` v.s. `/database.json?sql=` was different.

Alex and I decided to fix that. Alex laid out the new design in [issue \#2360](https://github.com/simonw/datasette/issues/2360) \- there are quite a few other changes, but the big one is that we are splitting out the SQL query interface to a new URL: `/databasename/-/query?sql=` \- or `/databasename/-/query.json?sql=` for the JSON API.

We've added redirects from the old URLs to the new ones, so existing links should continue to work.

#### Everything else

> * Fix for a bug where canned queries with named parameters could fail against SQLite 3\.46\. ([\#2353](https://github.com/simonw/datasette/issues/2353))

This reflects a bug fix that went out in [Datasette 0\.64\.7](https://docs.datasette.io/en/stable/changelog.html#v0-64-7).

> * Datasette now serves `E-Tag` headers for static files. Thanks, [Agustin Bacigalup](https://github.com/redraw). ([\#2306](https://github.com/simonw/datasette/pull/2306))

There's still more to be done making Datasette play well with caches, but this is a great, low\-risk start.

> * Dropdown menus now use a `z-index` that should avoid them being hidden by plugins. ([\#2311](https://github.com/simonw/datasette/issues/2311))

A cosmetic bug that showed up on Datasette Cloud when using the [datasette\-cluster\-map](https://datasette.io/plugins/datasette-cluster-map) plugin.

> * Incorrect table and row names are no longer reflected back on the resulting 404 page. ([\#2359](https://github.com/simonw/datasette/issues/2359))

This was reported as a potential security issue. The table names were correctly escaped, so this wasn't an XSS, but there was still potential for confusion if an attacker constructed a URL along the lines of `/database-does-not-exist-visit-www.attacker.com-for-more-info`. A similar fix went out in [Datasette 0\.64\.8](https://docs.datasette.io/en/stable/changelog.html#v0-64-8).

> * Improved documentation for async usage of the [track\_event(datasette, event)](https://docs.datasette.io/en/latest/plugin_hooks.html#plugin-hook-track-event) hook. ([\#2319](https://github.com/simonw/datasette/issues/2319))
> * Fixed some HTTPX deprecation warnings. ([\#2307](https://github.com/simonw/datasette/issues/2307))
> * Datasette now serves a `<html lange="en">` attribute. Thanks, [Charles Nepote](https://github.com/CharlesNepote). ([\#2348](https://github.com/simonw/datasette/issues/2348))
> * Datasette's automated tests now run against the maximum and minimum supported versions of SQLite: 3\.25 (from September 2018\) and 3\.46 (from May 2024\). Thanks, Alex Garcia. ([\#2352](https://github.com/simonw/datasette/pull/2352))
> * Fixed an issue where clicking twice on the URL output by `datasette --root` produced a confusing error. ([\#2375](https://github.com/simonw/datasette/issues/2375))

#### Tricks to help construct the release notes

I still write the Datasette release notes entirely by hand (aside from a few words auto\-completed by GitHub Copilot) \- I find the process of writing them to be really useful as a way to construct a final review of everything before it goes out.

I used a couple of tricks to help this time. I always start my longer release notes [with an issue](https://github.com/simonw/datasette/issues/2381). The GitHub [diff view](https://github.com/simonw/datasette/compare/1.0a13...2ad51baa31bfba7940c739e99d4270f563a77290) is useful for seeing what's changed since the last release, but I took it a step further this time with the following shell command:

```
git log --pretty=format:"- %ad: %s %h" --date=short --reverse 1.0a13...81b68a14
```

This outputs a summary of each commit in the range, looking like this (truncated):

```
- 2024-03-12: Added two things I left out of the 1.0a13 release notes 8b6f155b
- 2024-03-15: Fix httpx warning about app=self.app, refs #2307 5af68377
- 2024-03-15: Fixed cookies= httpx warning, refs #2307 54f5604c
...

```

Crucially, the syntax of this output is in GitHub Flavored Markdown \- and pasting it into an issue comment causes both the issue references and the commit hashes to be expanded into links that [look like this](https://github.com/simonw/datasette/issues/2381#issuecomment-2269759462):

[![2024-03-12: Added two things I left out of the 1.0a13 release notes 8b6f155 2024-03-15: Fix httpx warning about app=self.app, refs Fix httpx deprecation warnings #2307 5af6837 2024-03-15: Fixed cookies= httpx warning, refs Fix httpx deprecation warnings #2307 54f5604](https://substackcdn.com/image/fetch/$s_!2AKc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0d5c297e-3eb5-4e2d-80cd-0729fa9d099c_1478x168.jpeg "2024-03-12: Added two things I left out of the 1.0a13 release notes 8b6f155 2024-03-15: Fix httpx warning about app=self.app, refs Fix httpx deprecation warnings #2307 5af6837 2024-03-15: Fixed cookies= httpx warning, refs Fix httpx deprecation warnings #2307 54f5604")](https://substackcdn.com/image/fetch/$s_!2AKc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0d5c297e-3eb5-4e2d-80cd-0729fa9d099c_1478x168.jpeg)

It's a neat way to get a quick review of what's changed, and also means that those issues will automatically link back to the new issue where I'm constructing the release notes.

I wrote this up [in a TIL here](https://til.simonwillison.net/github/release-note-assistance), along with another trick I used where I used [LLM](https://llm.datasette.io/) to get Claude 3\.5 Sonnet to summarize my changes for me:

```
curl 'https://github.com/simonw/datasette/compare/1.0a13...2ad51baa3.diff' \
  | llm -m claude-3.5-sonnet --system \
  'generate a short summary of these changes, then a bullet point list of detailed release notes'
```

---

**Link** 2024\-07\-24 [Mistral Large 2](https://mistral.ai/news/mistral-large-2407/):

The second release of a GPT\-4 class open weights model in two days, after yesterday's [Llama 3\.1 405B](https://simonwillison.net/2024/Jul/23/introducing-llama-31/).

The weights for this one are under Mistral's [Research License](https://mistral.ai/licenses/MRL-0.1.md), which "allows usage and modification for research and non\-commercial usages" \- so not as open as Llama 3\.1\. You can use it commercially via the Mistral paid API.

Mistral Large 2 is 123 billion parameters, "designed for single\-node inference" (on a very expensive single\-node!) and has a 128,000 token context window, the same size as Llama 3\.1\.

Notably, according to Mistral's own benchmarks it out\-performs the much larger Llama 3\.1 405B on their code and math benchmarks. They trained on a lot of code:

> Following our experience with [Codestral 22B](https://mistral.ai/news/codestral/) and [Codestral Mamba](https://mistral.ai/news/codestral-mamba/), we trained Mistral Large 2 on a very large proportion of code. Mistral Large 2 vastly outperforms the previous Mistral Large, and performs on par with leading models such as GPT\-4o, Claude 3 Opus, and Llama 3 405B.

They also invested effort in tool usage, multilingual support (across English, French, German, Spanish, Italian, Portuguese, Dutch, Russian, Chinese, Japanese, Korean, Arabic, and Hindi) and reducing hallucinations:

> One of the key focus areas during training was to minimize the model’s tendency to “hallucinate” or generate plausible\-sounding but factually incorrect or irrelevant information. This was achieved by fine\-tuning the model to be more cautious and discerning in its responses, ensuring that it provides reliable and accurate outputs.
> 
> Additionally, the new Mistral Large 2 is trained to acknowledge when it cannot find solutions or does not have sufficient information to provide a confident answer.

I went to update my [llm\-mistral](https://github.com/simonw/llm-mistral) plugin for LLM to support the new model and found that I didn't need to \- that plugin already uses `llm -m mistral-large` to access the `mistral-large-latest` endpoint, and Mistral have updated that to point to the latest version of their Large model.

Ollama now have [mistral\-large](https://ollama.com/library/mistral-large) quantized to 4 bit as a 69GB download.

---

**Link** 2024\-07\-24 [Google is the only search engine that works on Reddit now thanks to AI deal](https://www.404media.co/google-is-the-only-search-engine-that-works-on-reddit-now-thanks-to-ai-deal/):

This is depressing. As of around June 25th [reddit.com/robots.txt](https://www.reddit.com/robots.txt) contains this:

```
User-agent: *
Disallow: /

```

Along with a link to Reddit's [Public Content Policy](https://support.reddithelp.com/hc/en-us/articles/26410290525844-Public-Content-Policy).

Is this a direct result of Google's deal to license Reddit content for AI training, rumored [at $60 million](https://www.reuters.com/technology/reddit-ai-content-licensing-deal-with-google-sources-say-2024-02-22/)? That's not been confirmed but it looks likely, especially since accessing that `robots.txt` using the [Google Rich Results testing tool](https://search.google.com/test/rich-results) (hence proxied via their IP) appears to return a different file, via [this comment](https://news.ycombinator.com/item?id=41057033#41058375), [my copy here](https://gist.github.com/simonw/be0e8e595178207b1b3dce3b81eacfb3).

---

**Link** 2024\-07\-25 [wat](https://github.com/igrek51/wat):

This is a really neat Python debugging utility. Install with `pip install wat-inspector` and then inspect any Python object like this:

```
from wat import wat
wat / myvariable

```

The `wat / x` syntax is a shortcut for `wat(x)` that's quicker to type.

The tool dumps out all sorts of useful introspection about the variable, value, class or package that you pass to it.

There are several variants: `wat.all / x` gives you all of them, or you can chain several together like `wat.dunder.code / x`.

The documentation also provides a slightly intimidating copy\-paste version of the tool which uses `exec()`, `zlib` and `base64` to help you paste the full implementation directly into any Python interactive session without needing to install it first.

---

**Link** 2024\-07\-25 [Button Stealer](https://anatolyzenkov.com/stolen-buttons/button-stealer):

Really fun Chrome extension by Anatoly Zenkov: it scans every web page you visit for things that look like buttons and stashes a copy of them, then provides a page where you can see all of the buttons you have collected. Here's [Anatoly's collection](https://anatolyzenkov.com/stolen-buttons), and here are a few that I've picked up trying it out myself:

[![Screenshot showing some buttons I have collected, each with their visual appearance maintained](https://substackcdn.com/image/fetch/$s_!0bgS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc5c3cdfa-1706-4ba0-b69a-d2d16e67e387_1692x444.jpeg "Screenshot showing some buttons I have collected, each with their visual appearance maintained")](https://substackcdn.com/image/fetch/$s_!0bgS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc5c3cdfa-1706-4ba0-b69a-d2d16e67e387_1692x444.jpeg)

The extension source code is [on GitHub](https://github.com/anatolyzenkov/button-stealer). It identifies potential buttons by looping through every `<a>` and `<button>` element and [applying some heuristics](https://github.com/anatolyzenkov/button-stealer/blob/cfe43b6247e1b9f7d4414fd2a9b122c2d1a40840/scripts/button-stealer.js#L264-L298) like checking the width/height ratio, then [clones a subset of the CSS](https://github.com/anatolyzenkov/button-stealer/blob/cfe43b6247e1b9f7d4414fd2a9b122c2d1a40840/scripts/button-stealer.js#L93-L140) from `window.getComputedStyle()` and stores that in the `style=` attribute.

---

**Link** 2024\-07\-25 [AI crawlers need to be more respectful](https://about.readthedocs.com/blog/2024/07/ai-crawlers-abuse/):

Eric Holscher:

> At Read the Docs, we host documentation for many projects and are generally bot friendly, but the behavior of AI crawlers is currently causing us problems. We have noticed AI crawlers aggressively pulling content, seemingly without basic checks against abuse.

One crawler downloaded 73 TB of zipped HTML files just in Month, racking up $5,000 in bandwidth charges!

---

**Link** 2024\-07\-25 [Introducing sqlite\-lembed: A SQLite extension for generating text embeddings locally](https://alexgarcia.xyz/blog/2024/sqlite-lembed-init/index.html):

Alex Garcia's latest SQLite extension is a C wrapper around the [llama.cpp](https://github.com/ggerganov/llama.cpp) that exposes just its embedding support, allowing you to register a GGUF file containing an embedding model:

```
INSERT INTO temp.lembed_models(name, model)
  select 'all-MiniLM-L6-v2',
  lembed_model_from_file('all-MiniLM-L6-v2.e4ce9877.q8_0.gguf');

```

And then use it to calculate embeddings as part of a SQL query:

```
select lembed(
  'all-MiniLM-L6-v2',
  'The United States Postal Service is an independent agency...'
); -- X'A402...09C3' (1536 bytes)

```

`all-MiniLM-L6-v2.e4ce9877.q8_0.gguf` here is a 24MB file, so this should run quite happily even on machines without much available RAM.

What if you don't want to run the models locally at all? Alex has another new extension for that, described in **[Introducing sqlite\-rembed: A SQLite extension for generating text embeddings from remote APIs](https://alexgarcia.xyz/blog/2024/sqlite-rembed-init/index.html)**. The `rembed` is for remote embeddings, and this extension uses Rust to call multiple remotely\-hosted embeddings APIs, registered like this:

```
INSERT INTO temp.rembed_clients(name, options)
  VALUES ('text-embedding-3-small', 'openai');
select rembed(
  'text-embedding-3-small',
  'The United States Postal Service is an independent agency...'
); -- X'A452...01FC', Blob<6144 bytes>

```

Here's [the Rust code](https://github.com/asg017/sqlite-rembed/blob/v0.0.1-alpha.9/src/clients.rs) that implements Rust wrapper functions for HTTP JSON APIs from OpenAI, Nomic, Cohere, Jina, Mixedbread and localhost servers provided by Ollama and Llamafile.

Both of these extensions are designed to complement Alex's [sqlite\-vec](https://github.com/asg017/sqlite-vec) extension, which is nearing a first stable release.

---

**Quote** 2024\-07\-25

> *Our estimate of OpenAI’s $4 billion in inference costs comes from a person with knowledge of the cluster of servers OpenAI rents from Microsoft. That cluster has the equivalent of 350,000 Nvidia A100 chips, this person said. About 290,000 of those chips, or more than 80% of the cluster, were powering ChartGPT, this person said.*

[Amir Efrati and Aaron Holmes](https://www.theinformation.com/articles/why-openai-could-lose-5-billion-this-year)

---

**Link** 2024\-07\-26 [Did you know about Instruments?](https://registerspill.thorstenball.com/p/did-you-know-about-instruments):

Thorsten Ball shows how the macOS Instruments app (installed as part of Xcode) can be used to run a CPU profiler against *any* application \- not just code written in Swift/Objective C.

I tried this against a Python process running [LLM](https://llm.datasette.io/) executing a Llama 3\.1 prompt with my new [llm\-gguf](https://github.com/simonw/llm-gguf) plugin and captured this:

[![Screenshot of a deep nested stack trace showing _PyFunction_Vectorcall from python3.10 calling PyCFuncPtr_call _ctypes.cpython-310-darwin.so which then calls ggml_ methods in libggml.dylib](https://substackcdn.com/image/fetch/$s_!lKR6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F99b418b4-ef2d-4c08-85be-4322f0c24456_1408x740.jpeg "Screenshot of a deep nested stack trace showing _PyFunction_Vectorcall from python3.10 calling PyCFuncPtr_call _ctypes.cpython-310-darwin.so which then calls ggml_ methods in libggml.dylib")](https://substackcdn.com/image/fetch/$s_!lKR6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F99b418b4-ef2d-4c08-85be-4322f0c24456_1408x740.jpeg)

---

**Link** 2024\-07\-26 [Image resize and quality comparison](https://tools.simonwillison.net/image-resize-quality):

Another tiny tool I built with Claude 3\.5 Sonnet and Artifacts. This one lets you select an image (or drag\-drop one onto an area) and then displays that same image as a JPEG at 1, 0\.9, 0\.7, 0\.5, 0\.3 quality settings, then again but with at half the width. Each image shows its size in KB and can be downloaded directly from the page.

[![Screenshot of the tool, showing a resized photo of a blue heron](https://substackcdn.com/image/fetch/$s_!_FWG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F428f2d1b-3afb-400c-9b95-76abf74cf1ef_1650x1500.jpeg "Screenshot of the tool, showing a resized photo of a blue heron")](https://substackcdn.com/image/fetch/$s_!_FWG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F428f2d1b-3afb-400c-9b95-76abf74cf1ef_1650x1500.jpeg)

I'm trying to use more images on my blog ([example 1](https://simonwillison.net/2024/Jul/25/button-stealer/), [example 2](https://simonwillison.net/2024/Jul/26/did-you-know-about-instruments/)) and I like to reduce their file size and quality while keeping them legible.

The prompt sequence I used for this was:

> Build an artifact (no React) that I can drop an image onto and it presents that image resized to different JPEG quality levels, each with a download link

Claude produced [this initial artifact](https://claude.site/artifacts/a469a051-6941-4e2f-ba81-f4ef16a2cd33). I followed up with:

> change it so that for any image it provides it in the following:
> 
> * original width, full quality
> * original width, 0\.9 quality
> * original width, 0\.7 quality
> * original width, 0\.5 quality
> * original width, 0\.3 quality
> * half width \- same array of qualities
> 
> For each image clicking it should toggle its display to full width and then back to max\-width of 80%
> 
> Images should show their size in KB

Claude produced [this v2](https://claude.site/artifacts/45ecf75e-d8e2-4d2a-a3b9-d8c07c7bd757).

I tweaked it a tiny bit (modifying how full\-width images are displayed) \- the final source code [is available here](https://github.com/simonw/tools/blob/main/image-resize-quality.html). I'm hosting it on my own site which means the Download links work correctly \- when hosted on `claude.site` Claude's CSP headers prevent those from functioning.

---

**Quote** 2024\-07\-27

> *Among many misunderstandings, \[users] expect the RAG system to work like a search engine, not as a flawed, forgetful analyst. They will not do the work that you expect them to do in order to verify documents and ground truth. They will not expect the AI to try to persuade them.*

[Ethan Mollick](https://twitter.com/emollick/status/1817013052887138722)

---

**Quote** 2024\-07\-28

> *The key to understanding the pace of today’s infrastructure buildout is to recognize that while AI optimism is certainly a driver of AI CapEx, it is not the only one. The cloud players exist in a ruthless oligopoly with intense competition. \[...]   
>   
> Every time Microsoft escalates, Amazon is motivated to escalate to keep up. And vice versa. We are now in a cycle of competitive escalation between three of the biggest companies in the history of the world, collectively worth more than $7T. At each cycle of the escalation, there is an easy justification—we have plenty of money to afford this. With more commitment comes more confidence, and this loop becomes self\-reinforcing. Supply constraints turbocharge this dynamic: If you don’t acquire land, power and labor now, someone else will.*

[David Cahn](https://www.sequoiacap.com/article/ai-optimism-vs-ai-arms-race/)

---

**Link** 2024\-07\-28 [CalcGPT](https://calcgpt.io/):

Fun satirical GPT\-powered calculator demo by [Calvin Liang](https://calvin.sh/), originally built in July 2023\. From the ChatGPT\-generated artist statement:

> The piece invites us to reflect on the necessity and relevance of AI in every aspect of our lives as opposed to its prevailing use as a mere marketing gimmick. With its delightful slowness and propensity for computational errors, CalcGPT elicits mirth while urging us to question our zealous indulgence in all things AI.

The [source code](https://github.com/Calvin-LL/CalcGPT.io/blob/2515646df1003aed852b89d54793a84bba06fcef/netlify/functions/math.ts#L39) shows that it's using [babbage\-002](https://platform.openai.com/docs/models/gpt-base) (a GPT3\-era OpenAI model which I hadn't realized was still available through their API) that takes a completion\-style prompt, which Calvin primes with some examples before including the user's entered expression from the calculator:

```
1+1=2
5-2=3
2*4=8
9/3=3
10/3=3.33333333333
${math}=

```

It sets `\n` as the stop sequence.

---

**Link** 2024\-07\-28 [The many lives of Null Island](https://stamen.com/the-many-lives-of-null-island/):

Stamen's custom basemaps have long harbored an Easter egg: zoom all the way in on 0, 0 to see the outline of the mystical "null island", the place where GIS glitches and data bugs accumulate, in the Gulf of Guinea south of Ghana.

Stamen's Alan McConchie provides a detailed history of the Easter egg \- first introduced by Mike Migurski in 2010 \- along with a definitive guide to the GIS jokes and traditions that surround it.

Here's [Null Island on Stamen's Toner map](https://maps.stamen.com/toner/#19/0/0). The shape (also available [as GeoJSON](https://github.com/stamen/toner-carto/blob/master/shp-local/nullisland.geojson)) is an homage to the island from 1993's [Myst](https://en.wikipedia.org/wiki/Myst), hence the outline of a large docked ship at the bottom.

[![White outline of Null Island on a black background.](https://substackcdn.com/image/fetch/$s_!5fX_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F37959f6e-ebb8-420d-b772-af6b199d808e_1122x662.jpeg "White outline of Null Island on a black background.")](https://substackcdn.com/image/fetch/$s_!5fX_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F37959f6e-ebb8-420d-b772-af6b199d808e_1122x662.jpeg)

Alan recently gave a talk about Stamen's updated custom maps at State of the Map US 2024 ([video](https://www.youtube.com/watch?v=qewW7-z8W2I), [slides](https://speakerdeck.com/almccon/rebuilding-stamens-iconic-map-styles-with-stadia-maps)) \- their Toner and Terrain maps are now available as vector tiles served by Stadia Maps (here's [the announcement](https://stamen.com/stamen-x-stadia-the-end-of-the-road-for-stamens-legacy-map-tiles/)), but their iconic watercolor style is yet to be updated to vectors, due to the weird array of raster tricks it used to achieve the effect.

In researching this post I searched for [null island on Google Maps](https://www.google.com/maps/search/null+island/@6.3431564,-0.774215,5.21z) and was delighted to learn that a bunch of entrepreneurs in Western Africa have tapped into the meme for their own businesses:

[![A null island search returns companies in The Gambia, Côte d’Ivoire, Burkina Faso, Cameroon and Democratic Republic of the Congo.](https://substackcdn.com/image/fetch/$s_!TFF7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2a8d910-5eae-4d51-8742-838e2c0e5405_1037x724.jpeg "A null island search returns companies in The Gambia, Côte d’Ivoire, Burkina Faso, Cameroon and Democratic Republic of the Congo.")](https://substackcdn.com/image/fetch/$s_!TFF7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2a8d910-5eae-4d51-8742-838e2c0e5405_1037x724.jpeg)

---

**Link** 2024\-07\-28 [The rich history of ham radio culture](https://thereader.mitpress.mit.edu/the-rich-history-of-ham-radio-culture/):

This long excerpt from Kristen Haring's 2008 book [Ham Radio's Technical Culture](https://mitpress.mit.edu/9780262582766/ham-radios-technical-culture/) filled in so many gaps for me. I'm ham licensed in the USA (see my recent notes on [passing the general exam](https://til.simonwillison.net/ham-radio/general)) but prior to reading this I hadn't appreciated quite how much the 100\+ year history of the hobby explains the way it works today. Some ham abbreviations derive from [the Phillips Code](https://en.wikipedia.org/wiki/Phillips_Code) created in 1879!

The Hacker News thread attracted some delightful personal stories from older ham operators: ["my exposure to ham radio really started in the 1970s..."](https://news.ycombinator.com/item?id=41060631#41095579). I also liked [this description](https://news.ycombinator.com/item?id=41060631#41095243) of the core of the hobby:

> A ham radio license is permission from your country's government to get on the air for the sake of playing with radio waves and communicating with other hams locally or around the globe without any further agenda.

I'm increasingly using the [Listen to Page](https://til.simonwillison.net/ios/listen-to-page) feature in my iPhone's Mobile Safari to read long\-form articles like this one, which means I can do household chores at the same time.

---

**Link** 2024\-07\-29 [Everlasting jobstoppers: How an AI bot\-war destroyed the online job market](https://www.salon.com/2024/07/28/everlasting-jobstoppers-how-an-ai-bot-destroyed-the-online-job-market/):

This story by Joe Tauke highlights several unpleasant trends from the online job directory space at the moment.

The first is "ghost jobs" \- job listings that company put out which don't actually correspond to an open roll. [A survey](https://clarifycapital.com/job-seekers-beware-of-ghost-jobs-survey) found that this is done for a few reasons: to keep harvesting resumes for future reference, to imply that the company is successful, and then:

> Perhaps the most infuriating replies came in at 39% and 33%, respectively: “The job was filled” (but the post was left online anyway to keep gathering résumés), and “No reason in particular.”
> 
> That’s right, all you go\-getters out there: When you scream your 87th cover letter into the ghost\-job void, there’s a one in three chance that your time was wasted for “no reason in particular.”

Another trend is "job post scraping". Plenty of job listings sites are supported by advertising, so the more content they can gather the better. This has lead to an explosion of web scraping, resulting in vast tracts of listings that were copied from other sites and likely to be out\-of\-date or no longer correspond to open positions.

Most worrying of all: scams.

> With so much automation available, it’s become easier than ever for identity thieves to flood the employment market with their own versions of ghost jobs — not to make a real company seem like it’s growing or to make real employees feel like they’re under constant threat of being replaced, but to get practically all the personal information a victim could ever provide.

I'm not 100% convinced by the "AI bot\-war" component of this headline though. The article later notes that the "ghost jobs" report it quotes was written before ChatGPT's launch in November 2022\. The story ends with a flurry of examples of new AI\-driven tools for both applicants and recruiters, and I've certainly heard anecdotes of LinkedIn spam that clearly has a flavour of ChatGPT to it, but I'm not convinced that the AI component is (yet) as frustration\-inducing as the other patterns described above.

---

**Link** 2024\-07\-29 [Dealing with your AI\-obsessed co\-worker (TikTok)](https://www.tiktok.com/@alberta.nyc/video/7396841688876010795):

The latest in Alberta 🤖 Tech's [excellent series of skits](https://www.tiktok.com/@alberta.nyc/playlist/Co-worker-who-%E2%9D%A4%25EF%25B8%258F-AI-7385007871211195166):

> You asked the CEO what he thinks of our project? Oh, you asked ChatGPT to pretend to be our CEO and then asked what he thought of our project. I don't think that counts.

---

**Quote** 2024\-07\-29

> *The \[Apple Foundation Model] pre\-training dataset consists of a diverse and high quality data mixture. This includes data we have licensed from publishers, curated publicly\-available or open\-sourced datasets, and publicly available information crawled by our web\-crawler, Applebot. We respect the right of webpages to opt out of being crawled by Applebot, using standard robots.txt directives.   
>   
> Given our focus on protecting user privacy, we note that no private Apple user data is included in the data mixture. Additionally, extensive efforts have been made to exclude profanity, unsafe material, and personally identifiable information from publicly available data (see Section 7 for more details). Rigorous decontamination is also performed against many common evaluation benchmarks.   
>   
> We find that data quality, much more so than quantity, is the key determining factor of downstream model performance.*

[Apple Intelligence Foundation Language Models (PDF)](https://machinelearning.apple.com/papers/apple_intelligence_foundation_language_models.pdf)

---

**Link** 2024\-07\-29 [SAM 2: The next generation of Meta Segment Anything Model for videos and images](https://ai.meta.com/blog/segment-anything-2/):

Segment Anything is Meta AI's model for image segmentation: for any image or frame of video it can identify which shapes on the image represent different "objects" \- things like vehicles, people, animals, tools and more.

SAM 2 "outperforms SAM on its 23 dataset zero\-shot benchmark suite, while being six times faster". Notably, SAM 2 works with video where the original SAM only worked with still images. It's released under the Apache 2 license.

The best way to understand SAM 2 is to try it out. Meta have a [web demo](https://sam2.metademolab.com/demo) which worked for me in Chrome but not in Firefox. I uploaded a recent video of my brand new cactus tweezers (for removing detritus from my cacti without getting spiked) and selected the succulent and the tweezers as two different objects:

[![A video editing interface focused on object tracking. The main part of the screen displays a close-up photograph of a blue-gray succulent plant growing among dry leaves and forest floor debris. The plant is outlined in blue, indicating it has been selected as "Object 1" for tracking. On the left side of the interface, there are controls for selecting and editing objects. Two objects are listed: Object 1 (the succulent plant) and Object 2 (likely the yellow stem visible in the image). At the bottom of the screen is a video timeline showing thumbnail frames, with blue and yellow lines representing the tracked paths of Objects 1 and 2 respectively. The interface includes options to add or remove areas from the selected object, start over, and "Track objects" to follow the selected items throughout the video.](https://substackcdn.com/image/fetch/$s_!M4WN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fed1d7e85-1e90-44e8-ae95-940e7e668b05_1584x886.jpeg "A video editing interface focused on object tracking. The main part of the screen displays a close-up photograph of a blue-gray succulent plant growing among dry leaves and forest floor debris. The plant is outlined in blue, indicating it has been selected as \"Object 1\" for tracking. On the left side of the interface, there are controls for selecting and editing objects. Two objects are listed: Object 1 (the succulent plant) and Object 2 (likely the yellow stem visible in the image). At the bottom of the screen is a video timeline showing thumbnail frames, with blue and yellow lines representing the tracked paths of Objects 1 and 2 respectively. The interface includes options to add or remove areas from the selected object, start over, and \"Track objects\" to follow the selected items throughout the video.")](https://substackcdn.com/image/fetch/$s_!M4WN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fed1d7e85-1e90-44e8-ae95-940e7e668b05_1584x886.jpeg)

Then I applied a "desaturate" filter to the background and exported this resulting video, with the background converted to black and white while the succulent and tweezers remained in full colour:

Your browser does not support the video tag.

Also released today: the [full SAM 2 paper](https://ai.meta.com/research/publications/sam-2-segment-anything-in-images-and-videos/), the [SA\-V dataset](https://ai.meta.com/datasets/segment-anything-video) of "51K diverse videos and 643K spatio\-temporal segmentation masks" and a [Dataset explorer tool](https://sam2.metademolab.com/dataset) (again, not supported by Firefox) for poking around in that collection.

---

**Link** 2024\-07\-30 [Here Are All of the Apple Intelligence Features in the iOS 18\.1 Developer Beta](https://www.macrumors.com/2024/07/29/ios-18-1-apple-intelligence-features/):

Useful rundown from Juli Clover at MacRumors of the Apple Intelligence features that are available in the brand new iOS 18\.1 beta, available to developer account holders with an iPhone 15 or ‌iPhone 15 Pro‌ Max or Apple Silicon iPad.

I've been trying this out today. It's still clearly very early, and the on\-device model that powers Siri is significantly weaker than more powerful models that I've become used to over the past two years. Similar to old Siri I find myself trying to figure out the sparse, undocumented incantations that reliably work for the things I might want my voice assistant to do for me.

[Ethan Mollick](https://twitter.com/emollick/status/1818106202733060527):

> My early Siri AI experience has just underlined the fact that, while there is a lot of practical, useful things that can be done with small models, they really lack the horsepower to do anything super interesting.

---

**Link** 2024\-07\-30 [AWS CodeCommit quietly deprecated](https://repost.aws/questions/QUshILm0xbTjWJZSD8afYVgA/codecommit-cannot-create-a-repository):

CodeCommit is AWS's Git hosting service. In a reply from an AWS employee to this forum thread:

> Beginning on 06 June 2024, AWS CodeCommit ceased onboarding new customers. Going forward, only customers who have an existing repository in AWS CodeCommit will be able to create additional repositories.
> 
> \[...] If you would like to use AWS CodeCommit in a new AWS account that is part of your AWS Organization, please let us know so that we can evaluate the request for allowlisting the new account. If you would like to use an alternative to AWS CodeCommit given this news, we recommend using GitLab, GitHub, or another third party source provider of your choice.

What's weird about this is that, as far as I can tell, this is the first official public acknowledgement from AWS that CodeCommit is no longer accepting customers. The [CodeCommit landing page](https://aws.amazon.com/codecommit/) continues to promote the product, though it does link to the [How to migrate your AWS CodeCommit repository to another Git provider](https://aws.amazon.com/blogs/devops/how-to-migrate-your-aws-codecommit-repository-to-another-git-provider/) blog post from July 25th, which gives no direct indication that CodeCommit is being quietly sunset.

I wonder how long they'll continue to support their existing customers?

#### Amazon QLDB too

It looks like AWS may be having a bit of a clear\-out. [Amazon QLDB](https://aws.amazon.com/qldb/) \- Quantum Ledger Database (a blockchain\-adjacent immutable ledger, launched in 2019\) \- quietly put out a deprecation announcement [in their release history on July 18th](https://docs.aws.amazon.com/qldb/latest/developerguide/document-history.html) (again, no official announcement elsewhere):

> End of support notice: Existing customers will be able to use Amazon QLDB until end of support on 07/31/2025\. For more details, see [Migrate an Amazon QLDB Ledger to Amazon Aurora PostgreSQL](https://aws.amazon.com/blogs/database/migrate-an-amazon-qldb-ledger-to-amazon-aurora-postgresql/).

This one is more surprising, because migrating to a different Git host is massively less work than entirely re\-writing a system to use a fundamentally different database.

It turns out there's an infrequently updated community GitHub repo called [SummitRoute/aws\_breaking\_changes](https://github.com/SummitRoute/aws_breaking_changes) which tracks these kinds of changes. Other services listed there include CodeStar, Cloud9, CloudSearch, OpsWorks, Workdocs and Snowmobile, and they cleverly (ab)use the GitHub releases mechanism to provide an [Atom feed](https://github.com/SummitRoute/aws_breaking_changes/releases.atom).

---

**Link** 2024\-07\-30 [What we got wrong about HTTP imports](https://deno.com/blog/http-imports):

HTTP imports are one of the most interesting design features of Deno:

```
import { assertEquals } from "https://deno.land/std@0.224.0/assert/mod.ts";

```

Six years after their introduction, Ryan Dahl reviews their disadvantages:

1. Lengthy (non\-memorable) URLs littering the codebase
2. A slightly cumbersome `import { concat } from "../../deps.ts";` pattern for managing dependencies in one place
3. Large projects can end up using multiple slightly different versions of the same dependencies
4. If a website becomes unavailable, new builds will fail (existing builds will continue to use their cached version)

Deno 2 \- due in September \- will continue to support them, but will lean much more on the combination of import maps (design borrowed from modern browsers) and the Deno project's [JSR](https://jsr.io/) npm competitor. An import map like this:

```
{
  "imports": {
    "@std/assert": "jsr:@std/assert@1"
  }
}

```

Will then enable import statements that look like this:

```
import { assertEquals } from "@std/assert";

```

---

**Link** 2024\-07\-30 [GPT\-4o Long Output](https://openai.com/gpt-4o-long-output/):

"OpenAI is offering an experimental version of GPT\-4o with a maximum of 64K output tokens per request."

It's a new model (for alpha testers only) called `gpt-4o-64k-output-alpha` that costs $6/million input tokens and $18/million output tokens.

That's a little bit more than GPT\-4o ($5/$15\) and a LOT more than GPT\-4o mini ($0\.15/$0\.60\).

Long output is primarily useful for data transformation use\-cases \- things like translating documents from one language into another, or extracting structured data from documents where almost every input token is needed in the output JSON.

Prior to this the longest output model I knew of was GPT\-4o mini, at 16,000 tokens. Most of OpenAI's competitors still cap out at around 4,000 or 8,000\.

---

**Link** 2024\-07\-30 [Making Machines Move](https://fly.io/blog/machine-migrations/):

Another deep technical dive into Fly.io infrastructure from Thomas Ptacek, this time describing how they can quickly boot up an instance with a persistent volume on a new host (for things like zero\-downtime deploys) using a block\-level cloning operation, so the new instance gets a volume that becomes accessible instantly, serving proxied blocks of data until the new volume has been completely migrated from the old host.

---

**Link** 2024\-07\-30 [Ralph Sheldon’s Portrait of Henry VIII Reidentified](https://adamfineart.wordpress.com/2024/07/04/ralph-sheldons-portrait-of-henry-viii-reidentified/#ce0dfb5f-afa3-4e5c-aa0b-2358c1854c13):

Here's a delightful two part story on art historian Adam Busiakiewicz's blog. Adam was browsing Twitter when he spotted [this tweet](https://twitter.com/Warkslieutenant/status/1808884139585610231) by Tim Cox, Lord Lieutenant of Warwickshire, celebrating a reception.

He noticed a curve\-framed painting mounted on a wall in the top left of the photo:

[![Truncated photograph, showing a slightly blurry curved frame painting up on the wall among other paintings](https://substackcdn.com/image/fetch/$s_!qRfE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1adbfc1-1f9a-49fe-a1e6-15b0a3dfb608_1056x590.jpeg "Truncated photograph, showing a slightly blurry curved frame painting up on the wall among other paintings")](https://substackcdn.com/image/fetch/$s_!qRfE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1adbfc1-1f9a-49fe-a1e6-15b0a3dfb608_1056x590.jpeg)

Adam had previously researched a similar painting while working at Sotheby's:

> Seeing this round topped portrait immediately reminded me of a famous set of likenesses commissioned by the local politician and tapestry maker [Ralph Sheldon (c. 1537\-\-1613\)](https://artuk.org/discover/artworks/ralph-sheldon-15371613-55576) for his home Weston House, Warwickshire, during the 1590s. Consisting of twenty\-two portraits, mostly images of Kings, Queens and significant contemporary international figures, only a handful are known today.

Adam contacted Warwickshire County Council and was invited to Shire Hall. In [his follow\-up post](https://adamfineart.wordpress.com/2024/07/22/further-observations-of-ralph-sheldons-portrait-of-henry-viii/) he describes his first\-hand observations from the visit.

It turns out the painting really was one of those 22 portraits made for tapestry maker Ralph Sheldon in the 1590s, long thought lost. The discovery has now made international news:

* BBC News: [Missing Henry VIII portrait found after random X post](https://www.bbc.com/news/articles/ckdgp7r5y11o)
* Smithsonian Magazine: [Art Historian Discovers Long\-Lost Portrait of Henry VIII in Background of Social Media Post](https://www.smithsonianmag.com/smart-news/art-historian-discovers-long-lost-portrait-of-henry-viii-in-background-of-social-media-post-180984803/)

---

**Link** 2024\-07\-31 [Aider](https://github.com/paul-gauthier/aider):

Aider is an impressive open source local coding chat assistant terminal application, developed by Paul Gauthier (founding CTO of [Inktomi](https://en.wikipedia.org/wiki/Inktomi) back in [1996\-2000](https://www.linkedin.com/in/paulgauthier/details/experience/)).

I tried it out today, using an Anthropic API key to run it using Claude 3\.5 Sonnet:

```
pipx install aider-chat
export ANTHROPIC_API_KEY=api-key-here
aider --dark-mode

```

I found the `--dark-mode` flag necessary to make it legible using the macOS terminal "Pro" theme.

Aider starts by generating a [concise map of files](https://aider.chat/docs/repomap.html) in your current Git repository. This is passed to the LLM along with the prompts that you type, and Aider can then request additional files be added to that context \- or you can add the manually with the `/add filename` command.

It defaults to making modifications to files and then committing them directly to Git with a generated commit message. I found myself preferring the `/ask` command which lets you ask a question without making any file modifications:

[![Loaded /Users/simon/Dropbox/Development/simonwillisonblog/.env Aider v0.46.1 Models: claude-3-5-sonnet-20240620 with diff edit format, weak model claude-3-haiku-20240307 Git repo: .git with 156 files Repo-map: using 1024 tokens Use /help <question> for help, run "aider --help" to see cmd line args  > /add blog/search.py  Added /Users/simon/Dropbox/Development/simonwillisonblog/blog/search.py to the chat  blog/search.py   > /ask what does ?exclude.tag= do in the search feature?         The ?exclude.tag= parameter in the search feature is used to exclude specific tags from the search results. Here's how it      works in the code:        1 The excluded tags are retrieved from the request's GET parameters:   excluded_tags = request.GET.getlist("exclude.tag")    This line collects all the tags that should be excluded from the search results. The getlist() method is used because there    might be multiple excluded tags. 2 These excluded tags are then applied to the queryset for each content type (Entry, Blogmark, Quotation) in the   make_queryset() function:       for exclude_tag in excluded_tags:  qs = qs.exclude(tags__tag=exclude_tag)     This loop iterates through each excluded tag and uses Django's exclude() method to filter out any items that have the   specified tag.    So, if a user includes ?exclude.tag=python&exclude.tag=django in their search query, the results will not include any items    tagged with either "python" or "django". This feature allows users to refine their search by explicitly removing certain topics from the results, which can be   particularly useful when searching through a large number of tagged items.  Tokens: 3,884 sent, 248 received. Cost: $0.02 request, $0.02 session. blog/search.py](https://substackcdn.com/image/fetch/$s_!Ffju!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1c1cacad-05d5-4976-a5ac-d4bbd3eb04fa_1597x1453.jpeg "Loaded /Users/simon/Dropbox/Development/simonwillisonblog/.env Aider v0.46.1 Models: claude-3-5-sonnet-20240620 with diff edit format, weak model claude-3-haiku-20240307 Git repo: .git with 156 files Repo-map: using 1024 tokens Use /help <question> for help, run \"aider --help\" to see cmd line args  > /add blog/search.py  Added /Users/simon/Dropbox/Development/simonwillisonblog/blog/search.py to the chat  blog/search.py   > /ask what does ?exclude.tag= do in the search feature?         The ?exclude.tag= parameter in the search feature is used to exclude specific tags from the search results. Here's how it      works in the code:        1 The excluded tags are retrieved from the request's GET parameters:   excluded_tags = request.GET.getlist(\"exclude.tag\")    This line collects all the tags that should be excluded from the search results. The getlist() method is used because there    might be multiple excluded tags. 2 These excluded tags are then applied to the queryset for each content type (Entry, Blogmark, Quotation) in the   make_queryset() function:       for exclude_tag in excluded_tags:  qs = qs.exclude(tags__tag=exclude_tag)     This loop iterates through each excluded tag and uses Django's exclude() method to filter out any items that have the   specified tag.    So, if a user includes ?exclude.tag=python&exclude.tag=django in their search query, the results will not include any items    tagged with either \"python\" or \"django\". This feature allows users to refine their search by explicitly removing certain topics from the results, which can be   particularly useful when searching through a large number of tagged items.  Tokens: 3,884 sent, 248 received. Cost: $0.02 request, $0.02 session. blog/search.py")](https://substackcdn.com/image/fetch/$s_!Ffju!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1c1cacad-05d5-4976-a5ac-d4bbd3eb04fa_1597x1453.jpeg)

The Aider documentation includes [extensive examples](https://aider.chat/examples/README.html) and the tool can work with a wide range of [different LLMs](https://aider.chat/docs/llms.html), though it recommends GPT\-4o, Claude 3\.5 Sonnet (or 3 Opus) and DeepSeek Coder V2 for the best results. Aider maintains [its own leaderboard](https://aider.chat/docs/leaderboards/), emphasizing that "Aider works best with LLMs which are good at *editing* code, not just good at writing code".

The prompts it uses are pretty fascinating \- they're tucked away in various `*_prompts.py` files in [aider/coders](https://github.com/paul-gauthier/aider/tree/main/aider/coders).

---

**Quote** 2024\-07\-31

> *After giving it a lot of thought, we made the decision to discontinue new access to a small number of services, including AWS CodeCommit.   
>   
> While we are no longer onboarding new customers to these services, there are no plans to change the features or experience you get today, including keeping them secure and reliable. \[...]   
>   
> The services I'm referring to are: S3 Select, CloudSearch, Cloud9, SimpleDB, Forecast, Data Pipeline, and CodeCommit.*

[Jeff Barr](https://twitter.com/jeffbarr/status/1818461689920344321)

---

**Link** 2024\-07\-31 [This month in Servo: parallel tables and more](https://servo.org/blog/2024/07/31/this-month-in-servo/):

New in Servo:

> **Parallel table layout** is now enabled ([@mrobinson](https://github.com/mrobinson), [\#32477](https://github.com/servo/servo/pull/32477)), spreading the work for laying out rows and their columns over all available CPU cores. This change is a great example of the strengths of [Rayon](https://crates.io/crates/rayon) and the opportunistic parallelism in Servo's layout engine.

The [commit landing the change](https://github.com/servo/servo/commit/e16291f14edc38d4bc3663a36619e6e461329402?diff=unified&w=0) is quite short, and much of the work is done by refactoring the code to use `.par_iter().enumerate().map(...)` \- [par\_iter()](https://docs.rs/rayon/latest/rayon/iter/index.html) is the Rayon method that allows parallel iteration over a collection using multiple threads, hence multiple CPU cores.

---

**Link** 2024\-07\-31 [Build your own SQS or Kafka with Postgres](https://blog.sequinstream.com/build-your-own-sqs-or-kafka-with-postgres/):

Anthony Accomazzo works on [Sequin](https://github.com/sequinstream/sequin), an open source "message stream" (similar to Kafka) written in Elixir and Go on top of PostgreSQL.

This detailed article describes how you can implement message queue patterns on PostgreSQL from scratch, including this neat example using a CTE, `returning` and `for update skip locked` to retrieve `$1` messages from the `messages` table and simultaneously mark them with `not_visible_until` set to `$2` in order to "lock" them for processing by a client:

```
with available_messages as (
  select seq
  from messages
  where not_visible_until is null
    or (not_visible_until <= now())
  order by inserted_at
  limit $1
  for update skip locked
)
update messages m
set
  not_visible_until = $2,
  deliver_count = deliver_count + 1,
  last_delivered_at = now(),
  updated_at = now()
from available_messages am
where m.seq = am.seq
returning m.seq, m.data;

```

---

**Quote** 2024\-07\-31

> *For the past 10 years or so, AWS has been rolling out these peripheral services at an astonishing rate, dozens every year. A few get traction, most don’t—but they all stick around, undead zombies behind impressive\-looking marketing pages, because historically AWS just doesn’t make many breaking changes. \[...]   
>   
> AWS made this mess for themselves by rushing all sorts of half\-baked services to market. The mess had to be cleaned up at some point, and they’re doing that. But now they’ve explicitly revealed something to customers: The new stuff we release isn’t guaranteed to stick around.*

[Forrest Brazeal](https://newsletter.goodtechthings.com/p/the-end-of-the-everything-cloud)

---

**TIL** 2024\-07\-31 [HTML video with subtitles](https://til.simonwillison.net/html/video-with-subtitles):

Via [Mariatta](https://fosstodon.org/@mariatta/112883308634473940) I found my [PyVideo speaker page](https://pyvideo.org/speaker/simon-willison.html), and thanks to that page I learned that a talk I gave in 2009 had been rescued from the now\-deceased [Blip.tv](https://en.wikipedia.org/wiki/Blip.tv) and is now hosted by the Internet Archive: …

---

**Link** 2024\-08\-01 [Today's research challenge: why is August 1st "World Wide Web Day"?](https://fedi.simonwillison.net/@simon/112887537705995720):

Here's a fun mystery. A bunch of publications will tell you that today, August 1st, is "World Wide Web Day"... but where did that idea come from?

It's not an official day marked by any national or international organization. It's not celebrated by CERN or the W3C.

The date August 1st doesn't appear to hold any specific significance in the history of the web. The first website [was launched on August 6th 1991](https://www.npr.org/2021/08/06/1025554426/a-look-back-at-the-very-first-website-ever-launched-30-years-later).

I posed the following three questions this morning on Mastodon:

1. Who first decided that August 1st should be "World Wide Web Day"?
2. Why did they pick that date?
3. When was the first World Wide Web Day celebrated?

Finding answers to these questions has proven stubbornly difficult. Searches on Google have proven futile, and illustrate the growing impact of LLM\-generated slop on the web: they turn up dozens of articles celebrating the day, many from news publications playing the "write about what people might search for" game and many others that have distinctive ChatGPT vibes to them.

One early hint we've found is in the "Bylines 2010 Writer's Desk Calendar" by Snowflake Press, published in January 2009\. Jessamyn West [spotted that](https://glammr.us/@jessamyn/112887883859701567) on the [book's page in the Internet Archive](https://archive.org/details/isbn_9781933509068/mode/2up?q=%22World+Wide+Web+Day%22), but it merely lists "World Wide Web Day" at the bottom of the July calendar page (clearly a printing mistake, the heading is meant to align with August 1st on the next page) without any hint as to the origin:

[![Screenshot of a section of the calendar showing July 30 (Friday) and 31st (Saturday) - at the very bottom of the Saturday block is the text World Wide Web Day](https://substackcdn.com/image/fetch/$s_!DoN5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb7ab2156-cbe6-4aad-84eb-02a7125efebb_877x424.jpeg "Screenshot of a section of the calendar showing July 30 (Friday) and 31st (Saturday) - at the very bottom of the Saturday block is the text World Wide Web Day")](https://substackcdn.com/image/fetch/$s_!DoN5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb7ab2156-cbe6-4aad-84eb-02a7125efebb_877x424.jpeg)

I found two earlier mentions from August 1st 2008 on Twitter, from [@GabeMcCauley](https://twitter.com/GabeMcCauley/status/874683727) and from [@iJess](https://twitter.com/iJess/status/874964457).

Our earliest news media reference, spotted [by Hugo van Kemenade](https://mastodon.social/@hugovk/112888079773787541), is also from August 1st 2008: [this opinion piece in the Attleboro Massachusetts Sun Chronicle](https://www.thesunchronicle.com/opinion/unseen-eclipse-opens-summer-countdown/article_7ee3234d-f1e2-54c6-a688-a29bd542e3e3.html), which has no byline so presumably was written by the paper's editorial board:

> Today is World Wide Web Day, but who cares? We'd rather nap than surf. How about you? Better relax while you can: August presages the start of school, a new season of public meetings, worries about fuel costs, the rundown to the presidential election and local races.

So the mystery remains! Who decided that August 1st should be "World Wide Web Day", why that date and how did it spread so widely without leaving a clear origin story?

If your research skills are up to the challenge, [join the challenge](https://fedi.simonwillison.net/@simon/112887537705995720)!

---

**TIL** 2024\-08\-01 [Back\-dating Git commits based on file modification dates](https://til.simonwillison.net/git/backdate-git-commits):

I fell down a bit of a rabbit hole this morning. In trying to figure out [where the idea of celebrating World Wide Web Day on August 1st](https://simonwillison.net/2024/Aug/1/august-1st-world-wide-web-day/) came from I ran across Tim Berner\-Lee's original code for the WorldWideWeb application for NeXT on the W3C's website: …

---

**Link** 2024\-08\-01 [1991\-WWW\-NeXT\-Implementation on GitHub](https://github.com/simonw/1991-WWW-NeXT-Implementation):

I fell down a bit of a rabbit hole today trying to answer [that question about when World Wide Web Day was first celebrated](https://simonwillison.net/2024/Aug/1/august-1st-world-wide-web-day/). I found my way to [www.w3\.org/History/1991\-WWW\-NeXT/Implementation/](https://www.w3.org/History/1991-WWW-NeXT/Implementation/) \- an Apache directory listing of the source code for Tim Berners\-Lee's original WorldWideWeb application for NeXT!

The code wasn't particularly easy to browse: clicking a `.m` file would trigger a download rather than showing the code in the browser, and there were no niceties like syntax highlighting.

So I decided to mirror that code to a [new repository on GitHub](https://github.com/simonw/1991-WWW-NeXT-Implementation). I grabbed the code using `wget -r` and was delighted to find that the last modified dates (from the early 1990s) were preserved ... which made me want to preserve them in the GitHub repo too.

I used Claude to write a Python script to back\-date those commits, and wrote up what I learned in this new TIL: [Back\-dating Git commits based on file modification dates](https://til.simonwillison.net/git/backdate-git-commits).

End result: I now have a repo with Tim's original code, plus commit dates that reflect when that code was last modified.

[![Three commits credited to Tim Berners-Lee, in 1995, 1994 and 1993](https://substackcdn.com/image/fetch/$s_!Sp4F!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1cfd876f-d202-4c37-8d63-1ae607c2eac9_1186x580.jpeg "Three commits credited to Tim Berners-Lee, in 1995, 1994 and 1993")](https://substackcdn.com/image/fetch/$s_!Sp4F!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1cfd876f-d202-4c37-8d63-1ae607c2eac9_1186x580.jpeg)

---

**Link** 2024\-08\-01 [Footnotes that work in RSS readers](https://css-tricks.com/footnotes-that-work-in-rss-readers/):

Chris Coyier explained the mechanism used by Feedbin to render custom footnotes back in 2019\.

I stumbled upon this after I spotted an inline footnote rendered in NetNewsWire the other day (from [this post](https://www.dbreunig.com/2024/07/31/towards-standardizing-place.html) by Drew Breunig):

[![NetNewsWire screenshot. A post by Drew Breunig is shown, and a small number one in a pill reveals an overlay displaying a footnote.](https://substackcdn.com/image/fetch/$s_!JXL7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F83a94765-71ca-4534-98fd-7362d5072a0d_1402x686.jpeg "NetNewsWire screenshot. A post by Drew Breunig is shown, and a small number one in a pill reveals an overlay displaying a footnote.")](https://substackcdn.com/image/fetch/$s_!JXL7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F83a94765-71ca-4534-98fd-7362d5072a0d_1402x686.jpeg)

Since feed readers generally strip JavaScript and CSS and only allow a subset of HTML tags I was intrigued to figure out how that worked.

I found [this code](https://github.com/Ranchero-Software/NetNewsWire/blob/094a85bce0ca2e5a7593eed027b71714a37c147c/Shared/Article%20Rendering/main.js#L144-L150) in the NetNewsWire source (it's MIT licensed) which runs against elements matching this CSS selector:

```
sup > a[href*='#fn'], sup > div > a[href*='#fn']

```

So any link with an `href` attribute containing `#fn` that is a child of a `<sup>` (superscript) element.

In Drew's post the HTML looks like this:

```
<!-- Footnote link: -->
<sup id="fnref:precision" role="doc-noteref">
  <a href="#fn:precision" class="footnote" rel="footnote">1</a>
</sup>
<!-- Then at the bottom: -->
<div class="footnotes" role="doc-endnotes">
  <ol>
    <li id="fn:precision" role="doc-endnote">
      <p>This is the footnote.
        <a href="#fnref:precision" class="reversefootnote" role="doc-backlink">&#8617;</a>
      </p>
    </li>
  </ol>
</div>

```

Where did this convention come from? It doesn't seem to be part of any specific standard. Chris linked to `www.bigfootjs.com` (no longer resolving) which was the site for the [bigfoot.js](https://github.com/lemonmade/bigfoot) jQuery plugin, so my best guess is the convention came from that.

---

**Link** 2024\-08\-01 [Towards Standardizing Place](https://www.dbreunig.com/2024/07/31/towards-standardizing-place.html):

Overture Maps [announced General Availability of its global maps datasets](https://overturemaps.org/overture-maps-foundation-releases-general-availability-of-its-open-maps-datasets/) last week, covering places, buildings, divisions, and base layers.

Drew Breunig demonstrates how this can be accessed using both the [Overture Explorer tool](https://explore.overturemaps.org/#13.1/37.46975/-122.44309) and DuckDB, and talks about Overture's GERS IDs \- reminiscent of [Who's On First](https://whosonfirst.org/) IDs \- which provide stable IDs for all kinds of geographic places.

---

**Link** 2024\-08\-02 [Extracting Prompts by Inverting LLM Outputs](https://arxiv.org/abs/2405.15012):

New paper from Meta research:

> We consider the problem of language model inversion: given outputs of a language model, we seek to extract the prompt that generated these outputs. We develop a new black\-box method, output2prompt, that learns to extract prompts without access to the model's logits and without adversarial or jailbreaking queries. In contrast to previous work, output2prompt only needs outputs of normal user queries.

This is a way of extracting the hidden prompt from an application build on an LLM *without* using prompt injection techniques.

The trick is to train a dedicated model for guessing hidden prompts based on public question/answer pairs.

They conclude:

> Our results demonstrate that many user and system prompts are intrinsically vulnerable to extraction.

This reinforces my opinion that it's not worth trying to protect your system prompts. Think of them the same as your client\-side HTML and JavaScript: you might be able to obfuscate them but you should expect that people can view them if they try hard enough.

---

**Quote** 2024\-08\-02

> *When Noam and Daniel started Character.AI, our goal of personalized superintelligence required a full stack approach. We had to pre\-train models, post\-train them to power the experiences that make Character.AI special, and build a product platform with the ability to reach users globally. Over the past two years, however, the landscape has shifted – many more pre\-trained models are now available. Given these changes, we see an advantage in making greater use of third\-party LLMs alongside our own. This allows us to devote even more resources to post\-training and creating new product experiences for our growing user base.*

[Character.AI](https://blog.character.ai/our-next-phase-of-growth/)

---

**Link** 2024\-08\-03 [EpicEnv](https://github.com/danthegoodman1/EpicEnv):

Dan Goodman's tool for managing shared secrets via a Git repository. This uses a really neat trick: you can run `epicenv invite githubuser` and the tool will retrieve that user's public key from `github.com/{username}.keys` ([here's mine](https://github.com/simonw.keys)) and use that to encrypt the secrets such that the user can decrypt them with their private key.

---

**Quote** 2024\-08\-03

> *I think the mistake the industry has made is (and I had to learn this as well), that "we observed ab tests work really well" is really a statement that should read "the majority of the changes we make are characterized as hill\-climbing growth of a post\-PMF b2c product and ab tests work really well for that".*

[Malte Ubl](https://twitter.com/cramforce/status/1819800527527616919)

---

**Quote** 2024\-08\-03

> *\[On release notes] in our partial defense, training these models can be more discovery than invention. often we don't exactly know what will come out.   
>   
> we've long wanted to do release notes that describe each model's differences, but we also don't want to give false confidence with a shallow story.*

[Ted Sanders (OpenAI)](https://twitter.com/sandersted/status/1819294298124218427)

---

**Link** 2024\-08\-04 [How I Use "AI" by Nicholas Carlini](https://nicholas.carlini.com/writing/2024/how-i-use-ai.html):

Nicholas is an author on [Universal and Transferable Adversarial Attacks on Aligned Language Models](https://arxiv.org/abs/2307.15043), one of my favorite LLM security papers from last year. He understands the flaws in this class of technology at a deeper level than most people.

Despite that, this article describes several of the many ways he still finds utility in these models in his own work:

> But the reason I think that the recent advances we've made aren't just hype is that, over the past year, I have spent at least a few hours every week interacting with various large language models, and have been consistently impressed by their ability to solve increasingly difficult tasks I give them. And as a result of this, I would say I'm at least 50% faster at writing code for both my research projects and my side projects as a result of these models.

The way Nicholas is using these models closely matches my own experience \- things like “Automating nearly every monotonous task or one\-off script” and “Teaching me how to use various frameworks having never previously used them”.

I feel that this piece inadvertently captures the frustration felt by those of us who get value out of these tools on a daily basis and still constantly encounter people who are adamant that they offer no real value. Saying “this stuff is genuine useful” remains a surprisingly controversial statement, almost two years after the ChatGPT launch opened up LLMs to a giant audience.

I also enjoyed this footnote explaining why he put “AI” in scare quotes in the title:

> I hate this word. It's not AI. But I want people who use this word, and also people who hate this word, to find this post. And so I guess I'm stuck with it for marketing, SEO, and clickbait.

---

**Link** 2024\-08\-04 [What do people really ask chatbots? It’s a lot of sex and homework](https://www.washingtonpost.com/technology/2024/08/04/chatgpt-use-real-ai-chatbot-conversations/):

Jeremy B. Merrill and Rachel Lerman at the Washington Post analyzed [WildChat](https://wildchat.allen.ai/), a dataset of 1 million ChatGPT\-style interactions collected and released by the Allen Institute for AI.

From a random sample of 458 queries they categorized the conversations as 21% creative writing and roleplay, 18% homework help, 17% "search and other inquiries", 15% work/business and 7% coding.

I talked to them a little for this story:

> “I don’t think I’ve ever seen a piece of technology that has this many use cases,” said Simon Willison, a programmer and independent researcher.

---

**Link** 2024\-08\-04 [There’s a Tool to Catch Students Cheating With ChatGPT. OpenAI Hasn’t Released It.](https://www.wsj.com/tech/ai/openai-tool-chatgpt-cheating-writing-135b755a?st=830dm1b5txdsqx4):

This attention\-grabbing headline from the Wall Street Journal makes the underlying issue here sound less complex, but there's a lot more depth to it.

The story is actually about watermarking: embedding hidden patterns in generated text that allow that text to be identified as having come out of a specific LLM.

OpenAI evidently have had working prototypes of this for a couple of years now, but they haven't shipped it as a feature. I think this is the key section for understanding why:

> In April 2023, OpenAI commissioned a survey that showed people worldwide supported the idea of an AI detection tool by a margin of four to one, the internal documents show.
> 
> That same month, OpenAI surveyed ChatGPT users and found 69% believe cheating detection technology would lead to false accusations of using AI. Nearly 30% said they would use ChatGPT less if it deployed watermarks and a rival didn’t.

If ChatGPT was the only LLM tool, watermarking might make sense. The problem today is that there are now multiple vendors offering highly capable LLMs. If someone is determined to cheat they have multiple options for LLMs that don't watermark.

This means adding watermarking is both ineffective *and* a competitive disadvantage for those vendors!

---

**Quote** 2024\-08\-05

> *\[On WebGPU in Firefox] There is a lot of work to do still to make sure we comply with the spec. in a way that's acceptable to ship in a browser. We're 90% of the way there in terms of functionality, but the last 10% of fixing up spec. changes in the last few years \+ being significantly more resourced\-constrained (we have 3 full\-time folks, Chrome has/had an order of magnitude more humans working on WebGPU) means we've got our work cut out for us. We're hoping to ship sometime in the next year, but I won't make promises here.*

[Erich Gubler](https://news.ycombinator.com/item?id=41156872#41157602)

---

**Link** 2024\-08\-05 [How to Get or Create in PostgreSQL](https://hakibenita.com/postgresql-get-or-create):

Get or create \- for example to retrieve an existing tag record from a database table if it already exists or insert it if it doesn’t \- is a surprisingly difficult operation.

Haki Benita uses it to illustrate a variety of interesting PostgreSQL concepts.

New to me: a pattern that runs `INSERT INTO tags (name) VALUES (tag_name) RETURNING *;` and then catches the constraint violation and returns a record instead has a disadvantage at scale: “The table contains a dead tuple for every attempt to insert a tag that already existed” \- so until vacuum runs you can end up with significant table bloat!

Haki’s conclusion is that the best solution relies on an upcoming feature [coming in PostgreSQL 17](https://git.postgresql.org/gitweb/?p=postgresql.git;a=commitdiff;h=c649fa24a42ba89bf5460c7110e4fc8eeca65959): the ability to combine the [MERGE operation](https://www.postgresql.org/docs/current/sql-merge.html) with a RETURNING clause:

```
WITH new_tags AS (
    MERGE INTO tags
    USING (VALUES ('B'), ('C')) AS t(name)
    ON tags.name = t.name
WHEN NOT MATCHED THEN
    INSERT (name) VALUES (t.name)
    RETURNING *
)
SELECT * FROM tags WHERE name IN ('B', 'C')
    UNION ALL
SELECT * FROM new_tags;

```

I wonder what the best pattern for this in SQLite is. Could it be as simple as this?

```
INSERT OR IGNORE INTO tags (name) VALUES ('B'), ('C');

```

The SQLite [INSERT documentation](https://www.sqlite.org/lang_insert.html) doesn't currently provide extensive details for `INSERT OR IGNORE`, but there are some hints [in this forum thread](https://sqlite.org/forum/forumpost/f13dc431f9f3e669). [This post](https://hoelz.ro/blog/with-sqlite-insert-or-ignore-is-often-not-what-you-want) by Rob Hoelz points out that `INSERT OR IGNORE` will silently ignore *any* constraint violation, so `INSERT INTO tags (tag) VALUES ('C'), ('D') ON CONFLICT(tag) DO NOTHING` may be a better option.

---

**Link** 2024\-08\-05 [Leaked Documents Show Nvidia Scraping ‘A Human Lifetime’ of Videos Per Day to Train AI](https://www.404media.co/nvidia-ai-scraping-foundational-model-cosmos-project/):

Samantha Cole at 404 Media reports on a huge leak of internal NVIDIA communications \- mainly from a Slack channel \- revealing details of how they have been collecting video training data for a new video foundation model called Cosmos. The data is mostly from YouTube, downloaded via `yt-dlp` using a rotating set of AWS IP addresses and consisting of millions (maybe even hundreds of millions) of videos.

The fact that companies scrape unlicensed data to train models isn't at all surprising. This article still provides a fascinating insight into what model training teams care about, with details like this from a project update via email:

> As we measure against our desired distribution focus for the next week remains on cinematic, drone footage, egocentric, some travel and nature.

Or this from Slack:

> Movies are actually a good source of data to get gaming\-like 3D consistency and fictional content but much higher quality.

My intuition here is that the backlash against scraped video data will be even more intense than for static images used to train generative image models. Video is generally more expensive to create, and video creators (such as Marques Brownlee / MKBHD, who is mentioned in a Slack message here as a potential source of "tech product neviews \- super high quality") have a lot of influence.

There was [considerable uproar](https://simonwillison.net/2024/Jul/18/youtube-captions/) a few weeks ago over [this story](https://www.proofnews.org/apple-nvidia-anthropic-used-thousands-of-swiped-youtube-videos-to-train-ai/) about training against just *captions* scraped from YouTube, and now we have a much bigger story involving the actual video contint itself.

---

**TIL** 2024\-08\-05 [Assistance with release notes using GitHub Issues](https://til.simonwillison.net/github/release-note-assistance):

I like to write the release notes for my projects by hand, but sometimes it can be useful to have some help along the way. …

---