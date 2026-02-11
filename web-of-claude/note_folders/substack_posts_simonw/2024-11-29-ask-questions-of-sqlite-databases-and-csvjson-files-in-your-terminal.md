# Ask questions of SQLite databases and CSV/JSON files in your terminal

*Plus Storing times for human events and more*

Published: 2024-11-29
Source: https://simonw.substack.com/p/ask-questions-of-sqlite-databases

---

In this newsletter:

* Ask questions of SQLite databases and CSV/JSON files in your terminal
* Storing times for human events
* Weeknotes: asynchronous LLMs, synchronous embeddings, and I kind of started a podcast

Plus 23 links and 8 quotations and 1 TIL

### [Ask questions of SQLite databases and CSV/JSON files in your terminal](https://simonwillison.net/2024/Nov/25/ask-questions-of-sqlite/) \- 2024\-11\-25

I built a new plugin for my [sqlite\-utils CLI tool](https://sqlite-utils.datasette.io/en/stable/cli.html) that lets you ask human\-language questions directly of SQLite databases and CSV/JSON files on your computer.

It's called [sqlite\-utils\-ask](https://github.com/simonw/sqlite-utils-ask). Here's how you install it:

```
sqlite-utils install sqlite-utils-ask
```

It picks up API keys from an `OPENAI_API_KEY` environment variable, or you can [install LLM](https://llm.datasette.io/) and use [llm keys set openai](https://llm.datasette.io/en/stable/setup.html#saving-and-using-stored-keys) to store a key in a configuration file.

Then you can use it like this:

```
curl -O https://datasette.io/content.db
sqlite-utils ask content.db "how many sqlite-utils pypi downloads in 2024?"
```

This command will extract the SQL schema for the provided database file, send that through an LLM along with your question, get back a SQL query and attempt to run it to derive a result.

If all goes well it spits out an answer something like this:

```
SELECT SUM(downloads)
FROM stats
WHERE package = 'sqlite-utils' AND date >= '2024-01-01' AND date < '2025-01-01';

[
    {
        "SUM(downloads)": 4300221
    }
]

```

If the SQL query fails to execute (due to a syntax error of some kind) it passes that error back to the model for corrections and retries up to three times before giving up.

Add `-v/--verbose` to see the exact prompt it's using:

```
System prompt:
You will be given a SQLite schema followed by a question. Generate a single SQL
query to answer that question. Return that query in a ```sql ... ```
fenced code block.

Example: How many repos are there?
Answer:
```sql
select count(*) from repos
```

Prompt:
...
CREATE TABLE [stats] (
   [package] TEXT,
   [date] TEXT,
   [downloads] INTEGER,
   PRIMARY KEY ([package], [date])
);
...
how many sqlite-utils pypi downloads in 2024?

```

I've truncated the above to just the relevant table \- it actually includes the full schema of every table in that database.

By default, the tool sends just that database schema and your question to the LLM. If you add the `-e/--examples` option it will also include five common values for each of the text columns in that schema with an average length less than 32 characters. This can sometimes help get a better result, for example sending values "CA" and "FL" and "TX" for a `state` column can tip the model of that it should use state abbreviations rather than full names in its queries.

#### Asking questions of CSV and JSON data

The core `sqlite-utils` CLI usually works against SQLite files directly, but three years ago I added the ability to run SQL queries against CSV and JSON files directly with the [sqlite\-utils memory](https://simonwillison.net/2021/Jun/19/sqlite-utils-memory/) command. This works by loading that data into an in\-memory SQLite database before executing a SQL query.

I decided to reuse that mechanism to enable LLM prompts against CSV and JSON data directly as well.

The `sqlite-utils ask-files` command looks like this:

```
sqlite-utils ask-files transactions.csv "total sales by year"
```

This command accepts one or more files, and you can provide a mix of CSV, TSV and JSON. Each provided file will be imported into a different table, allowing the model to construct join queries where necessary.

#### Implementation notes

The core of the plugin is implemented as around [250 lines of Python](https://github.com/simonw/sqlite-utils-ask/blob/0.2/sqlite_utils_ask.py), using the `sqlite-utils` [register\_commands()](https://sqlite-utils.datasette.io/en/stable/plugins.html#register-commands-cli) plugin hook to add the `ask` and `ask-files` commands.

It adds [LLM](https://llm.datasette.io/) as a dependency, and takes advantage of LLM's [Python API](https://llm.datasette.io/en/stable/python-api.html) to abstract over the details of talking to the models. This means `sqlite-utils-ask` can use any of the models supported by LLM or its plugins \- if you want to run your prompt through Claude 3\.5 Sonnet you can do this:

```
sqlite-utils install llm-claude-3
sqlite-utils ask content.db "count rows in news table" -m claude-3.5-sonnet
```

The plugin defaults to [gpt\-4o\-mini](https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/) initially to take advantage of that model's automatic prompt caching: if you run multiple questions against the same schema you'll end up sending the same lengthy prompt prefix multiple times, and OpenAI's prompt caching should automatically kick in and provide a 50% discount on those input tokens.

Then I ran the actual numbers and found that `gpt-4o-mini` is cheap enough that even without caching a 4,000 token prompt (that's a pretty large SQL schema) should cost less than a tenth of a cent. So those caching savings aren't worth anything at all!

---

### [Storing times for human events](https://simonwillison.net/2024/Nov/27/storing-times-for-human-events/) \- 2024\-11\-27

I've worked on [various](https://en.wikipedia.org/wiki/Lanyrd) event [websites](https://en.wikipedia.org/wiki/Eventbrite) in the past, and one of the unintuitively difficult problems that inevitably comes up is the best way to store the time that an event is happening. Based on that past experience, here's my current recommendation.

This is the expanded version of a [comment I posted on lobste.rs](https://lobste.rs/s/sorhro/postgresql_timestamp_with_time_zone_s_set#c_xjj8ci) a few days ago, which ended up attracting a bunch of attention [on Twitter](https://twitter.com/iavins/status/1861468050748514547).

* [The problem](https://observablehq.com/@simonw/blog-to-newsletter#the-problem)
* [The "best practice" that isn't](https://observablehq.com/@simonw/blog-to-newsletter#the-best-practice-that-isn-t)
* [Things that can go wrong](https://observablehq.com/@simonw/blog-to-newsletter#things-that-can-go-wrong)
* [User error](https://observablehq.com/@simonw/blog-to-newsletter#user-error)
* [International timezone shenanigans](https://observablehq.com/@simonw/blog-to-newsletter#international-timezone-shenanigans)
* [My recommendation: store the user's intent time and the location/timezone](https://observablehq.com/@simonw/blog-to-newsletter#my-recommendation-store-the-user-s-intent-time-and-the-location-timezone)
* [Timezone UIs suck, generally](https://observablehq.com/@simonw/blog-to-newsletter#timezone-uis-suck-generally)

#### The problem

An event happens on a date, at a time. The precise details of that time are very important: if you tell people to show up to your event at 7pm and it turns out they should have arrived at 6pm they'll miss an hour of the event!

Some of the worst bugs an events website can have are the ones that result in human beings traveling to a place at a time and finding that the event they came for is not happening at the time they expected.

So how do you store the time of an event?

#### The "best practice" that isn't

Any time you talk to database engineers about dates and times you're likely to get the same advice: store everything in UTC. Dates and times are complicated enough that the only unambiguous way to store them is in UTC \- no daylight savings or timezones to worry about, it records the exact moment since the dawn of the universe at which the event will take place.

Then, when you display those times to users, you can convert them to that user's current timezone \- neatly available these days using the [Intl.DateTimeFormat().resolvedOptions().timeZone](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions) browser API.

There's a variant of this advice which you're more likely to hear from the PostgreSQL faithful: use [TIMESTAMP WITH TIME ZONE](https://www.postgresql.org/docs/current/datatype-datetime.html#DATATYPE-DATETIME-INPUT-TIME-STAMPS) or its convenient alias `timestamptz`. This stores the exact value in UTC and *sounds* like it might store the timezone too... but it doesn't! [All that's stored](https://stackoverflow.com/questions/5876218/difference-between-timestamps-with-without-time-zone-in-postgresql#comment32979814_5876276) is that UTC value, converted from whatever timezone was active or specified when the value was inserted.

In either case, we are losing *critical* information about when that event is going to happen.

#### Things that can go wrong

What's wrong with calculating the exact UTC time the event is starting and storing only that?

The problem is that we are losing crucial details about the event creator's original intent.

If I arrange an evening meetup for next year on December 3rd at 6pm, I mean 6pm local time, by whatever definition of local time is active on that particular date.

There are a number of ways this time can end up misinterpreted:

* User error: the user created the event **with an incorrect timezone**
* User error: the user created the event **in the wrong location**, and later needs to fix it
* International timezone shenanigans: the location in which the event is happening **changes its timezone rules** at some point between the event being created and the event taking place

#### User error

By far the most common issue here is **user error** with respect to how the event was initially created.

Maybe you asked the user to select the timezone as part of the event creation process. This is not a particularly great question: most users don't particularly care about timezones, or may not understand and respect them to the same extent as professional software developers.

If they pick the wrong timezone we risk showing the wrong time to anyone else who views their event later on.

My bigger concern is around location. Imagine a user creates their event in Springfield, Massachusetts... and then a few days later comes back and corrects the location to Springfield, Illinois.

That means the event is happening in a different timezone. If the user fails to update the time of the event to match the new location, we're going to end up with an incorrect time stored in our database.

#### International timezone shenanigans

One of my favourite niche corners of the internet is the [tz@iana.org mailing list](https://lists.iana.org/hyperkitty/list/tz@iana.org/latest). This is where the maintainers of the incredible open source [tz database](https://en.wikipedia.org/wiki/Tz_database) hang out and keep track of global changes to timezone rules.

It's easy to underestimate how much work this is, and how weird these rule changes can be. Here's a [recent email](https://lists.iana.org/hyperkitty/list/tz@iana.org/thread/5KMKN3JXZZHTUHGQWBCJSPTQXXYOPIPP/) proposing a brand new timezone: `Antarctica/Concordia`:

> Goodmorning. I'm writing here to propose a new time zone for an all\-year open Antarctic base. The base is a French–Italian research facility that was built 3,233 m (10,607 ft) above sea level at a location called Dome C on the Antarctic Plateau, Antarctica. <https://en.wikipedia.org/wiki/Concordia_Station>
> 
> The timezone is UTC\+8 without DST.

That's a pretty easy one. Here's a much more complicated example from March 2023: [Lebanon DST change internally disputed](https://lists.iana.org/hyperkitty/list/tz@iana.org/thread/EIBJYDJT3XQT5OWCNPIVVVH6U7INA2LW/):

> Lebanon is going through many internal disputes surrounding the latest decision to delay DST. Many institutions are refusing to comply with the change and are going to adopt regular DST on Sunday Mar 26th. Those institutions include but are not limited to:
> 
> * News agencies
> * Religious organizations
> * Schools, universities, etc...
> 
> The refusal is mainly centered the legality of that decision and, obviously, the technical chaos it will create because of its short notice. Moreover, as some of the below articles mention, this is also causing sectarian strife.

Lebanon ended up with more than one timezone active at the same time, depending on which institution you were talking to!

It's surprisingly common for countries to make decisions about DST with very little notice. Turkey and Russia and Chile and Morocco are four more examples of countries that can often cause short\-term chaos for software developers in this way.

If you've stored your event start times using UTC this is a *big* problem: the new DST rules mean that an already\-existing event that starts at 6pm may now start at 5pm or 7pm local time, according to the UTC time you've stored in your database.

#### My recommendation: store the user's intent time and the location/timezone

My strong recommendation here is that the most important thing to record is the **original user's intent**. If they said the event is happening at 6pm, store that! Make sure that when they go to edit their event later they see the same editable time that they entered when they first created it.

In addition to that, try to get the most accurate possible indication of the timezone in which that event is occurring.

For most events I would argue that the best version of this is the exact location of the venue itself.

Users may find timezones confusing, but they hopefully understand the importance of helping their attendees know where exactly the event is taking place.

If you have the venue location you can *almost certainly* derive the timezone from it. I say *almost* because, as with anything involving time, there are going to be edge\-cases \- most critically for venues that are exactly on the line that divides one timezone from another.

I haven't sat down to design my ideal UI for this, but I can imagine something which makes it *abundantly* clear to the user exactly where and when the event is taking place at that crucial local scale.

Now that we've precisely captured the user's intent and the event location (and through it the exact timezone) we can denormalize: **figure out the UTC time of that event and store that as well**.

This UTC version can be used for all sorts of purposes: sorting events by time, figuring out what's happening now/next, displaying the event to other users with its time converted to their local timezone.

But when the user goes to edit their event, we can show them exactly what they told us originally. When the user edits the location of their event we can maintain that original time, potentially confirming with the user if they want to modify that time based on the new location.

And if some legislature somewhere on earth makes a surprising change to their DST rules, we can identify all of the events that are affected by that change and update that denormalized UTC time accordingly.

#### Timezone UIs suck, generally

As an aside, here's my least favorite time\-related UI on the modern internet, from Google Calendar:

[![Google Calendar dialog for Event time zone, has a checkbox for Use separate start and end time zones and then a dropdown box with visible options (GMT-11:00) Niue Time, (GMT-11:00) Samoa Standard Time, (GMT-10:00) Cook Islands Standard Time, (GMT-10:00) Hawaii-Aleutian Standard Time, (GMT-10:00) Hawaii-Aleutian Time, (GMT-10:00) Tahiti Time, (GMT-09:30) Marquesas Time, (GMT-09:00) Alaska Time - Anchorage](https://substackcdn.com/image/fetch/$s_!WgFV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff6740fbe-d3d4-4462-93ea-fae9b34d94fb_932x1322.jpeg "Google Calendar dialog for Event time zone, has a checkbox for Use separate start and end time zones and then a dropdown box with visible options (GMT-11:00) Niue Time, (GMT-11:00) Samoa Standard Time, (GMT-10:00) Cook Islands Standard Time, (GMT-10:00) Hawaii-Aleutian Standard Time, (GMT-10:00) Hawaii-Aleutian Time, (GMT-10:00) Tahiti Time, (GMT-09:30) Marquesas Time, (GMT-09:00) Alaska Time - Anchorage")](https://substackcdn.com/image/fetch/$s_!WgFV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff6740fbe-d3d4-4462-93ea-fae9b34d94fb_932x1322.jpeg)

There isn't even a search option! Good luck finding America/New\_York in there, assuming you knew that's what you were looking for in the first place.

---

### [Weeknotes: asynchronous LLMs, synchronous embeddings, and I kind of started a podcast](https://simonwillison.net/2024/Nov/22/weeknotes/) \- 2024\-11\-22

These past few weeks I've been bringing Datasette and LLM together and distracting myself with a new sort\-of\-podcast crossed with a live streaming experiment.

* [Project: interviewing people about their projects](https://simonwillison.net/2024/Nov/22/weeknotes/#project-interviewing-people-about-their-projects)
* [Datasette Public Office Hours](https://simonwillison.net/2024/Nov/22/weeknotes/#datasette-public-office-hours)
* [Async LLM](https://simonwillison.net/2024/Nov/22/weeknotes/#async-llm)
* [Various embedding models](https://simonwillison.net/2024/Nov/22/weeknotes/#various-embedding-models)
* [Blog entries](https://simonwillison.net/2024/Nov/22/weeknotes/#blog-entries)
* [Releases](https://simonwillison.net/2024/Nov/22/weeknotes/#releases)
* [TILs](https://simonwillison.net/2024/Nov/22/weeknotes/#tils)

#### Project: interviewing people about their projects

My response to the recent US election was to stress\-code, and then to stress\-podcast. On the morning after the election I started a video series called [Project](https://simonwillison.net/series/project/) (I guess you could call it a "vlog"?) where I interview people about their interesting data projects. The [first episode](https://simonwillison.net/2024/Nov/7/project-verdad/) was with Rajiv Sinclair talking about his project [VERDAD](https://observablehq.com/@simonw/blog-to-newsletter), tracking misinformation on US broadcast radio. The second was with Philip James [talking about Civic Band](https://simonwillison.net/2024/Nov/16/civic-band/), his project to scrape and search PDF meeting minutes and agendas from US local municipalities.

I was a guest on another podcast\-like thing too: an Ars Technica Live sesison with Benj Edwards, which I wrote about in [Notes from Bing Chat—Our First Encounter With Manipulative AI](https://simonwillison.net/2024/Nov/19/notes-from-bing-chat/).

#### Datasette Public Office Hours

I also started a new thing with Alex Garcia called **Datasette Public Office Hours**, which we plan to run approximately once every two weeks as a live\-streamed Friday conversation about Datasette and related projects. I wrote up our first session in [Visualizing local election results with Datasette, Observable and MapLibre GL](https://simonwillison.net/2024/Nov/9/visualizing-local-election-results/). The Civic Band interview was part of our second session \- I still need to write about the rest of that session about [sqlite\-vec](https://github.com/asg017/sqlite-vec), embeddings and some future Datasette AI features, but you can [watch the full video on YouTube](https://www.youtube.com/live/xmdiwdom6Vk).

#### Async LLM

I need to write this up in full, but last weekend I quietly released [LLM 0\.18](https://llm.datasette.io/en/stable/changelog.html#v0-18) with a *huge* new feature: plugins can now provide asynchronous versions of their models, ready to be used with Python's `asyncio`. I built this for [Datasette](https://datasette.io/), which is built entirely around ASGI and needs to be able to run LLM models asynchronously to enable all sorts of interesting AI features.

LLM provides async OpenAI models, and I've also versions of the [llm\-gemini](https://github.com/simonw/llm-gemini/releases/tag/0.4.2), [llm\-claude\-3](https://github.com/simonw/llm-claude-3/releases/tag/0.9) and [llm\-mistral](https://github.com/simonw/llm-mistral/releases/tag/0.8) plugins that enable async models as well.

Here's [the documentation](https://llm.datasette.io/en/stable/python-api.html#async-models), but the short version is that you can now do this:

```
import llm

model = llm.get_async_model("claude-3.5-sonnet")

async for chunk in model.prompt(
    "Five surprising names for a pet pelican"
):
    print(chunk, end="", flush=True)
```

I've also been working on adding [token accounting](https://observablehq.com/@simonw/blog-to-newsletter) to LLM, to keep track of how many input and output tokens a prompt has used across multiple different models. I have an [alpha release](https://llm.datasette.io/en/latest/changelog.html#a0-2024-11-19) with that but it's not yet fully stable.

The reason I want that is that I need it for both Datasette and Datasette Cloud. I want the ability to track token usage and grant users a free daily allowance of tokens that gets cut off once they've exhausted it. That's an active project right now, more on that once it's ready to ship in a release.

#### Various embedding models

LLM doesn't yet offer asynchronous embeddings (see [issue \#628](https://github.com/simonw/llm/issues/628)) but I've found myself hacking on a few different embeddings plugins anyway:

* [llm\-gguf](https://github.com/simonw/llm-gguf) now supports embedding models distributed as GGUF files. This means you can use the excitingly small (just 30\.8MB) [mxbai\-embed\-xsmall\-v1](https://huggingface.co/mixedbread-ai/mxbai-embed-xsmall-v1) with LLM.
* [llm\-nomic\-api\-embed](https://github.com/simonw/llm-nomic-api-embed) added support for the [Nomic Embed Vision](https://www.nomic.ai/blog/posts/nomic-embed-vision) models. These work like [CLIP](https://simonwillison.net/2023/Sep/12/llm-clip-and-chat/) in that you can embed both images and text in the same space, allowing you to do similarity search of a text string against a collection of images.

#### Blog entries

* [Notes from Bing Chat—Our First Encounter With Manipulative AI](https://simonwillison.net/2024/Nov/19/notes-from-bing-chat/)
* [Project: Civic Band \- scraping and searching PDF meeting minutes from hundreds of municipalities](https://simonwillison.net/2024/Nov/16/civic-band/)
* [Qwen2\.5\-Coder\-32B is an LLM that can code well that runs on my Mac](https://simonwillison.net/2024/Nov/12/qwen25-coder/)
* [Visualizing local election results with Datasette, Observable and MapLibre GL](https://simonwillison.net/2024/Nov/9/visualizing-local-election-results/)
* [Project: VERDAD \- tracking misinformation in radio broadcasts using Gemini 1\.5](https://simonwillison.net/2024/Nov/7/project-verdad/)
* [Claude 3\.5 Haiku](https://simonwillison.net/2024/Nov/4/haiku/)

#### Releases

* **[llm\-gemini 0\.4\.2](https://github.com/simonw/llm-gemini/releases/tag/0.4.2)** \- 2024\-11\-22  
LLM plugin to access Google's Gemini family of models
* **[llm\-nomic\-api\-embed 0\.3](https://github.com/simonw/llm-nomic-api-embed/releases/tag/0.3)** \- 2024\-11\-21  
Create embeddings for LLM using the Nomic API
* **[llm\-gguf 0\.2](https://github.com/simonw/llm-gguf/releases/tag/0.2)** \- 2024\-11\-21  
Run models distributed as GGUF files using LLM
* **[llm 0\.19a2](https://github.com/simonw/llm/releases/tag/0.19a2)** \- 2024\-11\-21  
Access large language models from the command\-line
* **[llm\-mistral 0\.9a0](https://github.com/simonw/llm-mistral/releases/tag/0.9a0)** \- 2024\-11\-20  
LLM plugin providing access to Mistral models using the Mistral API
* **[llm\-claude\-3 0\.10a0](https://github.com/simonw/llm-claude-3/releases/tag/0.10a0)** \- 2024\-11\-20  
LLM plugin for interacting with the Claude 3 family of models
* **[asgi\-csrf 0\.11](https://github.com/simonw/asgi-csrf/releases/tag/0.11)** \- 2024\-11\-15  
ASGI middleware for protecting against CSRF attacks
* **[sqlite\-utils 3\.38a0](https://github.com/simonw/sqlite-utils/releases/tag/3.38a0)** \- 2024\-11\-08  
Python CLI utility and library for manipulating SQLite databases
* **[asgi\-proxy\-lib 0\.2a0](https://github.com/simonw/asgi-proxy-lib/releases/tag/0.2a0)** \- 2024\-11\-06  
An ASGI function for proxying to a backend over HTTP
* **[llm\-lambda\-labs 0\.1a0](https://github.com/simonw/llm-lambda-labs/releases/tag/0.1a0)** \- 2024\-11\-04  
Run prompts against LLMs hosted by lambdalabs.com
* **[llm\-groq\-whisper 0\.1a0](https://github.com/simonw/llm-groq-whisper/releases/tag/0.1a0)** \- 2024\-11\-01  
Transcribe audio using the Groq.com Whisper API

#### TILs

* [Running cog automatically against GitHub pull requests](https://til.simonwillison.net/github-actions/cog) \- 2024\-11\-06
* [Generating documentation from tests using files\-to\-prompt and LLM](https://til.simonwillison.net/llms/docs-from-tests) \- 2024\-11\-05

---

**Link** 2024\-11\-21 [TextSynth Server](https://bellard.org/ts_server/):

I'd missed this: Fabrice Bellard (yes, *[that](https://en.wikipedia.org/wiki/Fabrice_Bellard)* [Fabrice Bellard](https://en.wikipedia.org/wiki/Fabrice_Bellard)) has a project called TextSynth Server which he describes like this:

> **ts\_server** is a web server proposing a REST API to large language models. They can be used for example for text completion, question answering, classification, chat, translation, image generation, ...
> 
> It has the following characteristics:
> 
> * All is included in a single binary. Very few external dependencies (Python is not needed) so installation is easy.
> * Supports many Transformer variants ([GPT\-J](https://github.com/kingoflolz/mesh-transformer-jax), [GPT\-NeoX](https://github.com/EleutherAI/gpt-neox), [GPT\-Neo](https://github.com/EleutherAI/gpt-neo), [OPT](https://github.com/facebookresearch/metaseq), [Fairseq GPT](https://github.com/pytorch/fairseq/tree/main/examples/moe_lm), [M2M100](https://arxiv.org/abs/2010.11125), [CodeGen](https://github.com/salesforce/CodeGen), [GPT2](https://github.com/openai/gpt-2), [T5](https://arxiv.org/abs/2210.11416), [RWKV](https://github.com/BlinkDL/RWKV-LM), [LLAMA](https://github.com/facebookresearch/llama), [Falcon](https://falconllm.tii.ae/), [MPT](https://github.com/mosaicml/llm-foundry), Llama 3\.2, Mistral, Mixtral, Qwen2, Phi3, Whisper) and [Stable Diffusion](https://github.com/CompVis/stable-diffusion).
> * \[...]

Unlike many of his other notable projects (such as FFmpeg, QEMU, QuickJS) this isn't open source \- in fact it's not even source available, you instead can download compiled binaries for Linux or Windows that are available for non\-commercial use only.

Commercial terms are available, or you can visit [textsynth.com](https://textsynth.com/) and pre\-pay for API credits which can then be used with the hosted REST API there.

This is not a new project: the earliest evidence I could find of it was [this July 2019 page](https://web.archive.org/web/20190704131718/http://textsynth.org/tech.html) in the Internet Archive, which said:

> Text Synth is build using the [GPT\-2 language model](https://openai.com/blog/better-language-models/) released by OpenAI. \[...] This implementation is original because instead of using a GPU, it runs using only 4 cores of a Xeon E5\-2640 v3 CPU at 2\.60GHz. With a single user, it generates 40 words per second. It is programmed in plain C using the [LibNC library](https://bellard.org/nncp/).

---

**Link** 2024\-11\-21 [How some of the world's most brilliant computer scientists got password policies so wrong](https://stuartschechter.org/posts/password-history/):

Stuart Schechter blames Robert Morris and Ken Thompson for the dire state of passwords today:

> The story of why password rules were recommended and enforced without scientific evidence since their invention in 1979 is a story of brilliant people, at the very top of their field, whose well\-intentioned recommendations led to decades of ignorance.

As Stuart describes it, their first mistake was inventing password policies (the ones about having at least one special character in a password) without testing that these would genuinely help the average user create a more secure password. Their second mistake was introducing one\-way password hashing, which made the terrible password choices of users invisible to administrators of these systems!

> As a result of Morris and Thompson’s recommendations, and those who believed their assumptions without evidence, it was not until well into the 21st century that the scientific community learned just how ineffective password policies were. This period of ignorance finally came to an end, in part, because hackers started stealing password databases from large websites and publishing them.

Stuart suggests using public\-private key cryptography for passwords instead, which would allow passwords to be securely stored while still allowing researchers holding the private key the ability to analyze the passwords. He notes that this is a tough proposal to pitch today:

> Alas, to my knowledge, nobody has ever used this approach, because after Morris and Thompson’s paper storing passwords in any form that can be reversed became taboo.

---

**Link** 2024\-11\-21 [A warning about tiktoken, BPE, and OpenAI models](https://macwright.com/2024/11/20/tokenization-bpe-warning.html):

Tom MacWright warns that OpenAI's [tiktoken Python library](https://github.com/openai/tiktoken) has a surprising performance profile: it's superlinear with the length of input, meaning someone could potentially denial\-of\-service you by sending you a 100,000 character string if you're passing that directly to `tiktoken.encode()`.

There's an [open issue](https://github.com/openai/tiktoken/issues/195) about this (now over a year old), so for safety today it's best to truncate on characters before attempting to count or truncate using `tiktoken`.

---

**Link** 2024\-11\-21 [llm\-gguf 0\.2, now with embeddings](https://github.com/simonw/llm-gguf/releases/tag/0.2):

This new release of my [llm\-gguf](https://github.com/simonw/llm-gguf) plugin \- which provides support for locally hosted GGUF LLMs \- adds a new feature: it now supports embedding models distributed as GGUFs as well.

This means you can use models like the bafflingly small (30\.8MB in its smallest quantization) [mxbai\-embed\-xsmall\-v1](https://huggingface.co/mixedbread-ai/mxbai-embed-xsmall-v1) with LLM like this:

```
llm install llm-gguf
llm gguf download-embed-model \
  'https://huggingface.co/mixedbread-ai/mxbai-embed-xsmall-v1/resolve/main/gguf/mxbai-embed-xsmall-v1-q8_0.gguf'

```

Then to embed a string:

```
llm embed -m gguf/mxbai-embed-xsmall-v1-q8_0 -c 'hello'

```

The LLM docs have [extensive coverage](https://llm.datasette.io/en/stable/embeddings/cli.html) of things you can then do with this model, like embedding every row in a CSV file / file in a directory / record in a SQLite database table and running similarity and semantic search against them.

Under the hood this takes advantage of the [create\_embedding() method](https://github.com/abetlen/llama-cpp-python/blob/main/README.md#embeddings) provided by the [llama\-cpp\-python](https://github.com/abetlen/llama-cpp-python) wrapper around [llama.cpp](https://github.com/ggerganov/llama.cpp).

---

**Link** 2024\-11\-21 [OK, I can partly explain the LLM chess weirdness now](https://dynomight.net/more-chess/):

Last week Dynomight published [Something weird is happening with LLMs and chess](https://dynomight.net/chess/) pointing out that most LLMs are terrible chess players with the exception of `gpt-3.5-turbo-instruct` (OpenAI's last remaining completion as opposed to chat model, which they [describe](https://platform.openai.com/docs/models#gpt-3-5-turbo) as "Similar capabilities as GPT\-3 era models").

After diving *deep* into this, Dynomight now has a theory. It's mainly about completion models v.s. chat models \- a completion model like `gpt-3.5-turbo-instruct` naturally outputs good next\-turn suggestions, but something about reformatting that challenge as a chat conversation dramatically reduces the quality of the results.

Through extensive prompt engineering Dynomight got results out of GPT\-4o that were almost as good as the 3\.5 instruct model. The two tricks that had the biggest impact:

1. Examples. Including just three examples of inputs (with valid chess moves) and expected outputs gave a huge boost in performance.
2. "Regurgitation" \- encouraging the model to repeat the entire sequence of previous moves before outputting the next move, as a way to help it reconstruct its context regarding the state of the board.

They experimented a bit with fine\-tuning too, but I found their results from prompt engineering more convincing.

No non\-OpenAI models have exhibited any talents for chess at all yet. I think that's explained by the [A.2 Chess Puzzles](https://arxiv.org/html/2312.09390v1#A1.SS2) section of OpenAI's December 2023 paper [Weak\-to\-Strong Generalization: Eliciting Strong Capabilities With Weak Supervision](https://arxiv.org/abs/2312.09390):

> The GPT\-4 pretraining dataset included chess games in the format of move sequence known as Portable Game Notation (PGN). We note that only games with players of Elo 1800 or higher were included in pretraining.

---

**Link** 2024\-11\-22 [Amazon S3 Express One Zone now supports the ability to append data to an object](https://aws.amazon.com/about-aws/whats-new/2024/11/amazon-s3-express-one-zone-append-data-object/):

This is a first for Amazon S3: it is now possible to append data to an existing object in a bucket, where previously the only supported operation was to atomically replace the object with an updated version.

This is only available for S3 Express One Zone, a bucket class introduced [a year ago](https://aws.amazon.com/blogs/aws/new-amazon-s3-express-one-zone-high-performance-storage-class/) which provides storage in just a single availability zone, providing significantly lower latency at the cost of reduced redundancy and a much higher price (16c/GB/month compared to 2\.3c for S3 standard tier).

The fact that appends have never been supported for multi\-availability zone S3 provides an interesting clue as to the underlying architecture. Guaranteeing that every copy of an object has received and applied an append is significantly harder than doing a distributed atomic swap to a new version.

More details from [the documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-append.html):

> There is no minimum size requirement for the data you can append to an object. However, the maximum size of the data that you can append to an object in a single request is 5GB. This is the same limit as the largest request size when uploading data using any Amazon S3 API.
> 
> With each successful append operation, you create a part of the object and each object can have up to 10,000 parts. This means you can append data to an object up to 10,000 times. If an object is created using S3 multipart upload, each uploaded part is counted towards the total maximum of 10,000 parts. For example, you can append up to 9,000 times to an object created by multipart upload comprising of 1,000 parts.

That 10,000 limit means this won't quite work for constantly appending to a log file in a bucket.

Presumably it will be possible to "tail" an object that is receiving appended updates using the HTTP Range header.

---

**Link** 2024\-11\-22 [Say hello to gemini\-exp\-1121](https://twitter.com/officiallogank/status/1859667244688736419):

Google Gemini's Logan Kilpatrick on Twitter:

> Say hello to gemini\-exp\-1121! Our latest experimental gemini model, with:
> 
> * significant gains on coding performance
> * stronger reasoning capabilities
> * improved visual understanding
> 
> Available on Google AI Studio and the Gemini API right now

The `1121` in the name is a release date of the 21st November. This comes fast on the heels of last week's `gemini-exp-1114`.

Both of these new experimental Gemini models have seen moments at the top of the [Chatbot Arena](https://lmarena.ai/). `gemini-exp-1114` took the top spot a few days ago, and then lost it to a new OpenAI model called "ChatGPT\-4o\-latest (2024\-11\-20\)"... only for the new `gemini-exp-1121` to hold the top spot right now.

(These model names are all so, so bad.)

I released [llm\-gemini 0\.4\.2](https://github.com/simonw/llm-gemini/releases/tag/0.4.2) with support for the new model \- this should have been 0\.5 but I already have a [0\.5a0 alpha](https://github.com/simonw/llm-gemini/releases/tag/0.5a0) that depends on an unreleased feature in LLM core.

I tried my [pelican benchmark](https://simonwillison.net/2024/Oct/25/pelicans-on-a-bicycle/):

```
llm -m gemini-exp-1121 'Generate an SVG of a pelican riding a bicycle'

```

[![Not great at all, description follows](https://substackcdn.com/image/fetch/$s_!kJp4!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbce0eb4a-ae06-4f7a-a6d3-dd436d232a49_300x250.svg "Not great at all, description follows")](https://substackcdn.com/image/fetch/$s_!kJp4!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbce0eb4a-ae06-4f7a-a6d3-dd436d232a49_300x250.svg)

Since Gemini is a multi\-modal vision model, I had it describe the image it had created back to me (by feeding it a PNG render):

```
llm -m gemini-exp-1121 describe -a pelican.png

```

And got this description, which is pretty great:

> The image shows a simple, stylized drawing of an insect, possibly a bee or an ant, on a vehicle. The insect is composed of a large yellow circle for the body and a smaller yellow circle for the head. It has a black dot for an eye, a small orange oval for a beak or mouth, and thin black lines for antennae and legs. The insect is positioned on top of a simple black and white vehicle with two black wheels. The drawing is abstract and geometric, using basic shapes and a limited color palette of black, white, yellow, and orange.

**Update**: Logan [confirmed on Twitter](https://twitter.com/officiallogank/status/1860106796247216174) that these models currently only have a 32,000 token input, significantly less than the rest of the Gemini family.

---

**Quote** 2024\-11\-22

> *It's okay to complain and vent, I just ask you be able to back it up. Saying, "Python packaging sucks", but then admit you actually haven't used it in so long you don't remember why it sucked isn't fair. Things do improve, so it's better to say "it did suck" and acknowledge you might be out\-of\-date.*

[Brett Cannon](https://bsky.app/profile/snarky.ca/post/3lbid7l27722p)

---

**Link** 2024\-11\-22 [Private School Labeler on Bluesky](https://bsky.app/profile/daddys.cash):

I am utterly delighted by this subversive use of Bluesky's [labels feature](https://docs.bsky.app/docs/advanced-guides/moderation), which allows you to subscribe to a custom application that then adds visible labels to profiles.

The feature was designed for moderation, but this labeler subverts it by displaying labels on accounts belonging to British public figures showing which expensive private school they went to and what the current fees are for that school.

Here's what it looks like on an account \- tapping the label brings up the information about the fees:

[![Screenshot of a social media profile and post. Profile shows "James O'Brien @mrjamesob.bsky.social" with 166.7K followers, 531 following, 183 posts. Bio reads "Broadcaster & author." Shows education at Ampleforth School and Private School. Contains a repost from Julia Hines about Rabbi Jeffrey, followed by a label showing "Ampleforth School £46,740/year (2024/2025). This label was applied by Private School Labeller](https://substackcdn.com/image/fetch/$s_!0vbt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc46c6cf7-d4c3-475e-9cb6-0ae84565b4f0_1208x2000.jpeg "Screenshot of a social media profile and post. Profile shows \"James O'Brien @mrjamesob.bsky.social\" with 166.7K followers, 531 following, 183 posts. Bio reads \"Broadcaster & author.\" Shows education at Ampleforth School and Private School. Contains a repost from Julia Hines about Rabbi Jeffrey, followed by a label showing \"Ampleforth School £46,740/year (2024/2025). This label was applied by Private School Labeller")](https://substackcdn.com/image/fetch/$s_!0vbt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc46c6cf7-d4c3-475e-9cb6-0ae84565b4f0_1208x2000.jpeg)

These labels are only visible to users who have deliberately subscribed to the labeler. Unsurprisingly, some of those labeled aren't too happy about it!

In response to a comment about attending on a scholarship, the label creator [said](https://bsky.app/profile/daddys.cash/post/3lbl43ifho22n):

> I'm explicit with the labeller that scholarship pupils, grant pupils, etc, are still included \- because it's the later effects that are useful context \- students from these schools get a leg up and a degree of privilege, which contributes eg to the overrepresentation in British media/politics

On the one hand, there are clearly opportunities for abuse here. But given the opt\-in nature of the labelers, this doesn't feel hugely different to someone creating a separate webpage full of information about Bluesky profiles.

I'm intrigued by the possibilities of labelers. There's a list of others on [bluesky\-labelers.io](https://www.bluesky-labelers.io/), including another brilliant hack: [Bookmarks](https://bsky.app/profile/did:plc:w6yx4bltuzdmiolooi4kd6zt), which lets you "report" a post to the labeler and then displays those reported posts in a custom feed \- providing a private bookmarks feature that Bluesky itself currently lacks.

**Update:** [@us\-gov\-funding.bsky.social](https://bsky.app/profile/us-gov-funding.bsky.social) is the inevitable labeler for US politicians showing which companies and industries are their top donors, built [by Andrew Lisowski](https://bsky.app/profile/hipstersmoothie.com/post/3lbl2lgnq7c2f) ([source code here](https://github.com/hipstersmoothie/us-gov-contributions-labeler)) using data sourced from [OpenScrets](https://www.opensecrets.org/). Here's what it looks like on [this post](https://bsky.app/profile/senatorschumer.bsky.social/post/3lbkvtdc5ik2z):

[![Post by Chuck Schumer. Labels show affiliated organizations: Citigroup Inc, Goldman Sachs, Lawyers/Law Firms, Paul, Weiss et al, Real Estate, Securities & Investment. Post text reads "Democracy is in serious trouble, but it's not dead. We all have power, and we can use it together to defend our freedoms."](https://substackcdn.com/image/fetch/$s_!WwqS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1c4f9f09-60fe-4b2a-9e67-4e1d511962a1_1320x710.jpeg "Post by Chuck Schumer. Labels show affiliated organizations: Citigroup Inc, Goldman Sachs, Lawyers/Law Firms, Paul, Weiss et al, Real Estate, Securities & Investment. Post text reads \"Democracy is in serious trouble, but it's not dead. We all have power, and we can use it together to defend our freedoms.\"")](https://substackcdn.com/image/fetch/$s_!WwqS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1c4f9f09-60fe-4b2a-9e67-4e1d511962a1_1320x710.jpeg)

---

**Link** 2024\-11\-22 [How decentralized is Bluesky really?](https://dustycloud.org/blog/how-decentralized-is-bluesky/):

Lots of technical depth in this comparison of the Bluesky (ATProto) and Fediverse/Mastodon/ActivityPub approach to decentralization, from [ActivityPub spec](https://www.w3.org/TR/activitypub/) author Christine Lemmer\-Webber.

One key theme: many of the features of Bluesky that aren't present in the rest of the Fediverse are the result of centralization: Bluesky follows a "shared heap" architecture where participating nodes are expected to maintain a full copy of the entire network \- more than 5TB of data already. ActivityPub instead uses a "message passing" architecture where only a subset of the overall network data \- messages from accounts followed by that node's users \- are imported into the node.

This enables features like comprehensive search and the ability to browse all messages in a conversation even if some come from accounts that are not followed by any of the current node's users (a problem [I've faced in the past](https://simonwillison.net/2023/Sep/16/notes-on-using-a-single-person-mastodon-server/)).

This is also part of the "credible exit" mechanism where users can theoretically switch to a different host while keeping all of their existing content \- though that also takes advantage of content addressed storage, a feature that could be added to ActivityPub.

Also of note: direct messages on Bluesky are currently entirely dependent on the single central node run by Bluesky themselves, and are not end\-to\-end encrypted. Furthermore, signing keys that are used by ATProto are currently held custodially by Bluesky on behalf of their users.

---

**Link** 2024\-11\-23 [Quantization matters](https://aider.chat/2024/11/21/quantization.html):

What impact does quantization have on the performance of an LLM? been wondering about this for quite a while, now here are numbers from Paul Gauthier.

He ran differently quantized versions of Qwen 2\.5 32B Instruct through his [Aider code editing benchmark](https://aider.chat/docs/benchmarks.html#the-benchmark) and saw a range of scores.

The [original released weights](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct) (BF16\) scored highest at 71\.4%, with Ollama's [qwen2\.5\-coder:32b\-instruct\-fp16](https://ollama.com/library/qwen2.5-coder:32b-instruct-fp16) (a 66GB download) achieving the same score.

The quantized Ollama [qwen2\.5\-coder:32b\-instruct\-q4\_K\_M](https://ollama.com/library/qwen2.5-coder:32b-instruct-q4_K_M) (a 20GB download) saw a massive drop in quality, scoring just 53\.4% on the same benchmark.

---

**Quote** 2024\-11\-23

> *If you try and tell people 5 interesting things about your product / company / cause, they’ll remember zero. If instead, you tell them just one, they’ll usually ask questions that lead them to the other things, and then they’ll remember all of them because it mattered to them at the moment they asked.*

[James Dillard](https://www.jdilla.xyz/post/246)

---

**Link** 2024\-11\-23 [Importing a frontend Javascript library without a build system](https://jvns.ca/blog/2024/11/18/how-to-import-a-javascript-library/):

I sometimes think the hardest problem in computer science right now is taking an NPM library and figuring out how to download it and use it from a `<script>` tag without needing to involve some sort of convoluted build system.

Julia Evans shares my preference for build\-free JavaScript, and has shared notes about figuring out how to turn an arbitrary NPM package into something that can be loaded in a browser.

It's *so complicated*! This is the best exploration I've seen yet of the topic but wow, this really needs to be easier.

My [download\-esm](https://simonwillison.net/2023/May/2/download-esm/) tool gets a mention, but I have to admit I'm not 100% confident in that as a robust solution. I don't know nearly enough about the full scope of the problem here to confidently recommend my own tool!

Right now my ideal solution would turn almost anything from NPM into an ES module that I can self\-host and then load using `import ... from` in a `<script type="module">` block, maybe with an importmap as long as I don't have to think too hard about what to put in it.

I'm intrigued by [esm.sh](https://esm.sh/) (mentioned by Julia as a new solution worth exploring). The length of the documentation on that page further reinforces quite how much there is that I need to understand here.

---

**Quote** 2024\-11\-24

> *Whatever you think of capitalism, the evidence is overwhelming: Social networks with a single proprietor have trouble with long\-term survival, and those do survive have trouble with user\-experience quality: see [Enshittification](https://en.m.wikipedia.org/wiki/Enshittification).   
>   
> The evidence is also perfectly clear that it doesn’t have to be this way. The original social network, email, is now into its sixth decade of vigorous life. It ain’t perfect but it is essential, and not in any serious danger.   
>   
> The single crucial difference between email and all those other networks — maybe the only significant difference — is that nobody owns or controls it.*

[Tim Bray](https://www.tbray.org/ongoing/When/202x/2024/11/15/Not-Bluesky)

---

**Link** 2024\-11\-24 [Is async Django ready for prime time?](https://jonathanadly.com/is-async-django-ready-for-prime-time):

Jonathan Adly reports on his experience using Django to build [ColiVara](https://colivara.com/), a hosted RAG API that uses [ColQwen2](https://huggingface.co/vidore/colqwen2-v1.0) visual embeddings, inspired by the [ColPali](https://arxiv.org/abs/2407.01449) paper.

In a breach of [Betteridge's law of headlines](https://en.wikipedia.org/wiki/Betteridge%27s_law_of_headlines) the answer to the question posed by this headline is “yes”.

> We believe async Django is ready for production. In theory, there should be no performance loss when using async Django instead of FastAPI for the same tasks.

The ColiVara application is itself open source, and you can see how it makes use of Django’s relatively new [asynchronous ORM features](https://docs.djangoproject.com/en/5.1/topics/db/queries/#asynchronous-queries) in the [api/views.py module](https://github.com/tjmlabs/ColiVara/blob/main/web/api/views.py).

I also picked up a useful trick [from their Dockerfile](https://github.com/tjmlabs/ColiVarE/blob/0761a9f9f7ba582f56e49a48d9fdefedcfaa87a5/Dockerfile#L14): if you want `uv` in a container you can install it with this one\-liner:

```
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

```

---

**Link** 2024\-11\-24 [open\-interpreter](https://github.com/OpenInterpreter/open-interpreter):

This "natural language interface for computers" open source ChatGPT Code Interpreter alternative has been around for a while, but today I finally got around to trying it out.

Here's how I ran it (without first installing anything) using `uv`:

```
uvx --from open-interpreter interpreter

```

The default mode asks you for an OpenAI API key so it can use `gpt-4o` \- there are a multitude of other options, including the ability to use local models with `interpreter --local`.

It runs in your terminal and works by generating Python code to help answer your questions, asking your permission to run it and then executing it directly on your computer.

I pasted in an API key and then prompted it with this:

> `find largest files on my desktop`

[![Would you like to run this code? (y/n)  - shows a chunk of Python code and the output - answers: Here are the largest files on your Desktop:     1 Screen Recording 2024-04-28 at 10.37.20 AM.mov - 4.06 GB     2 Gergely-Orosz-podcast.mp4 - 1.18 GB   3 Descript Recording 2023-12-01 09.58.25.696/screen.mp4 - 1.01 GB    4 Screen Recording 2024-04-28 at 11.03.15 AM.mov - 355.89 MB     5 Screen Recording 2024-06-19 at 8.37.57 PM.mov - 289.76 MB  If you need more information or further assistance, feel free to ask!](https://substackcdn.com/image/fetch/$s_!uLB2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc4b94e77-2f1c-4e25-8c38-8bacd4c819f3_1236x1442.jpeg "Would you like to run this code? (y/n)  - shows a chunk of Python code and the output - answers: Here are the largest files on your Desktop:     1 Screen Recording 2024-04-28 at 10.37.20 AM.mov - 4.06 GB     2 Gergely-Orosz-podcast.mp4 - 1.18 GB   3 Descript Recording 2023-12-01 09.58.25.696/screen.mp4 - 1.01 GB    4 Screen Recording 2024-04-28 at 11.03.15 AM.mov - 355.89 MB     5 Screen Recording 2024-06-19 at 8.37.57 PM.mov - 289.76 MB  If you need more information or further assistance, feel free to ask!")](https://substackcdn.com/image/fetch/$s_!uLB2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc4b94e77-2f1c-4e25-8c38-8bacd4c819f3_1236x1442.jpeg)

Here's [the full transcript](https://gist.github.com/simonw/f78a2ebd2e06b821192ec919639959e6).

Since code is run directly on your machine there are all sorts of ways things could go wrong if you don't carefully review the generated code before hitting "y". The team have an experimental [safe mode](https://github.com/OpenInterpreter/open-interpreter/blob/main/docs/SAFE_MODE.md) in development which works by scanning generated code with [semgrep](https://semgrep.dev/). I'm not convinced by that approach, I think executing code in a sandbox would be a much more robust solution here \- but sandboxing Python is still a very difficult problem.

They do at least have an experimental [Docker integration](https://docs.openinterpreter.com/integrations/docker).

---

**Link** 2024\-11\-24 [follow\_theirs.py](https://gist.github.com/simonw/848a3b91169a789bc084a459aa7ecf83):

Hamel Husain wrote [this Python script](https://gist.github.com/hamelsmu/fb9ed633de7d784619e4b6da5039e6ae) on top of the [atproto](https://pypi.org/project/atproto/) Python library for interacting with Bluesky, which lets you specify another user and then follows every account that user is following.

I forked it and added two improvements: inline [PEP 723](https://peps.python.org/pep-0723/) dependencies and `input()` and `getpass.getpass()` to interactively ask for the credentials needed to run the script.

This means you can run my version using `uv run` like this:

```
uv run https://gist.githubusercontent.com/simonw/848a3b91169a789bc084a459aa7ecf83/raw/397ad07c8be0601eaf272d9d5ab7675c7fd3c0cf/follow_theirs.py

```

I really like this pattern of being able to create standalone Python scripts with dependencies that can be run from a URL as a one\-liner. Here's the comment section at the top of the script that makes it work:

```
# /// script
# dependencies = [
#   "atproto"
# ]
# ///

```

---

**Quote** 2024\-11\-24

> *Often, you are told to do this by treating AI like an intern. In retrospect, however, I think that this particular analogy ends up making people use AI in very constrained ways. To put it bluntly, any recent frontier model (by which I mean Claude 3\.5, ChatGPT\-4o, Grok 2, Llama 3\.1, or Gemini Pro 1\.5\) is likely much better than any intern you would hire, but also weirder.   
>   
> Instead, let me propose a new analogy: **treat AI like an infinitely patient new coworker who forgets everything you tell them each new conversation**, one that comes highly recommended but whose actual abilities are not that clear.*

[Ethan Mollick](https://www.oneusefulthing.org/p/getting-started-with-ai-good-enough)

---

**Link** 2024\-11\-25 [Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol):

Interesting new initiative from Anthropic. The [Model Context Protocol](https://modelcontextprotocol.io/introduction) aims to provide a standard interface for LLMs to interact with other applications, allowing applications to expose tools, resources (contant that you might want to dump into your context) and parameterized prompts that can be used by the models.

Their first working version of this involves the [Claude Desktop app](https://claude.ai/download) (for macOS and Windows). You can now configure that app to run additional "servers" \- processes that the app runs and then communicates with via JSON\-RPC over standard input and standard output.

Each server can present a list of tools, resources and prompts to the model. The model can then make further calls to the server to request information or execute one of those tools.

(For full transparency: I got a preview of this last week, so I've had a few days to try it out.)

The best way to understand this all is to dig into the examples. There are [13 of these](https://github.com/modelcontextprotocol/servers/tree/main/src) in the `modelcontextprotocol/servers` GitHub repository so far, some using the [Typesscript SDK](https://github.com/modelcontextprotocol/typescript-sdk) and some with the [Python SDK](https://github.com/modelcontextprotocol/python-sdk) ([mcp](https://pypi.org/project/mcp/) on PyPI).

My favourite so far, unsurprisingly, is the [sqlite one](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite). This implements methods for Claude to execute read and write queries and create tables in a SQLite database file on your local computer.

This is clearly an early release: the process for enabling servers in Claude Desktop \- which involves hand\-editing a JSON configuration file \- is pretty clunky, and currently the desktop app and running extra servers on your own machine is the only way to try this out.

The specification already describes the next step for this: an HTTP SSE protocol which will allow Claude (and any other software that implements the protocol) to communicate with external HTTP servers. Hopefully this means that MCP will come to the Claude web and mobile apps soon as well.

A couple of early preview partners have announced their MCP implementations already:

* [Cody supports additional context through Anthropic's Model Context Protocol](https://sourcegraph.com/blog/cody-supports-anthropic-model-context-protocol)
* [The Context Outside the Code](https://zed.dev/blog/mcp) is the Zed editor's announcement of their MCP extensions.

---

**Link** 2024\-11\-25 [OpenStreetMap embed URL](https://www.openstreetmap.org/export/embed.html?bbox=-122.61343002319336,37.43138681508927,-122.38220214843751,37.5594114838176&layer=mapnik&marker=37.4954206394371,-122.4979019165039):

I just found out OpenStreetMap have a "share" button which produces HTML for an iframe targetting `https://www.openstreetmap.org/export/embed.html`, making it easy to drop an OpenStreetMap map onto any web page that allows iframes.

As far as I can tell the supported parameters are:

* `bbox=` then min longitude, min latitude, max longitude, max latitude
* `marker=` optional latitude, longitude coordinate for a marker (only a single marker is supported)
* `layer=mapnik` \- other values I've found that work are `cyclosm`, `cyclemap`, `transportmap` and `hot` (for humanitarian)

Here's HTML for embedding this on a page using a sandboxed iframe \- the `allow-scripts` is necessary for the map to display.

```
<iframe
  sandbox="allow-scripts"
  style="border: none; width: 100%; height: 20em;"
  src="https://www.openstreetmap.org/export/embed.html?bbox=-122.613%2C37.431%2C-122.382%2C37.559&amp;layer=mapnik&amp;marker=37.495%2C-122.497"
></iframe>

```

Thanks to this post I learned that iframes are rendered correctly in [NetNewsWire](https://fedi.simonwillison.net/@simon/113545275313339806), [NewsExplorer](https://fosstodon.org/@carlton/113545449230432890), [NewsBlur](https://mstdn.social/@nriley/113545545163094439) and [Feedly on Android](https://fosstodon.org/@omad/113545693553360791).

---

**Link** 2024\-11\-25 [Leaked system prompts from Vercel v0](https://github.com/2-fly-4-ai/V0-system-prompt):

[v0](https://v0.dev/) is Vercel's entry in the increasingly crowded LLM\-assisted development market \- chat with a bot and have that bot build a full application for you.

They've been iterating on it [since launching in October last year](https://vercel.com/blog/announcing-v0-generative-ui), making it one of the most mature products in this space.

Somebody leaked the system prompts recently. Vercel CTO Malte Ubl [said this](https://twitter.com/cramforce/status/1860436022347075667):

> When [@v0](https://twitter.com/v0) first came out we were paranoid about protecting the prompt with all kinds of pre and post processing complexity.
> 
> We completely pivoted to let it rip. A prompt without the evals, models, and especially UX is like getting a broken ASML machine without a manual

---

**Link** 2024\-11\-26 [Amazon S3 adds new functionality for conditional writes](https://aws.amazon.com/about-aws/whats-new/2024/11/amazon-s3-functionality-conditional-writes/):

> Amazon S3 can now perform conditional writes that evaluate if an object is unmodified before updating it. This helps you coordinate simultaneous writes to the same object and prevents multiple concurrent writers from unintentionally overwriting the object without knowing the state of its content. You can use this capability by providing the ETag of an object \[...]
> 
> This new conditional header can help improve the efficiency of your large\-scale analytics, distributed machine learning, and other highly parallelized workloads by reliably offloading compare and swap operations to S3\.

(Both [Azure Blob Storage](https://learn.microsoft.com/en-us/rest/api/storageservices/specifying-conditional-headers-for-blob-service-operations#Subheading1) and [Google Cloud](https://cloud.google.com/storage/docs/request-preconditions#precondition_criteria) have this feature already.)

When AWS added conditional write support just for if an object with that key exists or not back in August I [wrote about](https://simonwillison.net/2024/Aug/30/leader-election-with-s3-conditional-writes/) Gunnar Morling's trick for [Leader Election With S3 Conditional Writes](https://www.morling.dev/blog/leader-election-with-s3-conditional-writes/). This new capability opens up a whole set of new patterns for implementing distributed locking systems along those lines.

Here's a useful illustrative example [by lxgr on Hacker News](https://news.ycombinator.com/item?id=42240678#42241577):

> As a (horribly inefficient, in case of non\-trivial write contention) toy example, you could use S3 as a lock\-free concurrent SQLite storage backend: Reads work as expected by fetching the entire database and satisfying the operation locally; writes work like this:
> 
> * Download the current database copy
> * Perform your write locally
> * Upload it back using "Put\-If\-Match" and the pre\-edit copy as the matched object.
> * If you get success, consider the transaction successful.
> * If you get failure, go back to step 1 and try again.

AWS also just added the ability to [enforce conditional writes in bucket policies](https://aws.amazon.com/about-aws/whats-new/2024/11/amazon-s3-enforcement-conditional-write-operations-general-purpose-buckets/):

> To enforce conditional write operations, you can now use s3:if\-none\-match or s3:if\-match condition keys to write a bucket policy that mandates the use of HTTP if\-none\-match or HTTP if\-match conditional headers in S3 PutObject and CompleteMultipartUpload API requests. With this bucket policy in place, any attempt to write an object to your bucket without the required conditional header will be rejected.

---

**Quote** 2024\-11\-26

> *My preferred approach in many projects is to do some unit testing, but not a ton, early on in the project and wait until the core APIs and concepts of a module have crystallized.   
>   
> At that point I then test the API exhaustively with integrations tests.   
>   
> In my experience, these integration tests are much more useful than unit tests, because they remain stable and useful even as you change the implementation around. They aren’t as tied to the current codebase, but rather express higher level invariants that survive refactors much more readily.*

[Carson Gross](https://htmx.org/essays/codin-dirty/)

---

**Quote** 2024\-11\-26

> *One of the things we did all the time at early GitHub was a two\-step ship: basically, ship a big launch, but days or weeks afterwards, ship a smaller, add\-on feature. In the second launch post, you can refer back to the initial bigger post and you get twice the bang for the buck.   
>   
> This is even more valuable than on the surface, too: you get to split your product launch up into a few different pieces, which lets you slowly ease into the full usage — and server load — of new code.*

[Zach Holman](https://zachholman.com/posts/double-shipping)

---

**Link** 2024\-11\-27 [QwQ: Reflect Deeply on the Boundaries of the Unknown](https://qwenlm.github.io/blog/qwq-32b-preview/):

Brand new openly licensed (Apache 2\) model from Alibaba Cloud's Qwen team, this time clearly inspired by OpenAI's work on reasoning in o1\.

I love the flowery language they use to introduce the new model:

> Through deep exploration and countless trials, we discovered something profound: when given time to ponder, to question, and to reflect, the model’s understanding of mathematics and programming blossoms like a flower opening to the sun. Just as a student grows wiser by carefully examining their work and learning from mistakes, our model achieves deeper insight through patient, thoughtful analysis.

It's already available [through Ollama](https://ollama.com/library/qwq) as a 20GB download. I initially ran it like this:

```
ollama run qwq

```

This downloaded the model and started an interactive chat session. I tried the classic "how many rs in strawberry?" and got [this lengthy but correct](https://gist.github.com/simonw/a09c40188e2484e1d5646577dc2e7148) answer, which concluded:

> Wait, but maybe I miscounted. Let's list them: 1\. s 2\. t 3\. r 4\. a 5\. w 6\. b 7\. e 8\. r 9\. r 10\. y Yes, definitely three "r"s. So, the word "strawberry" contains three "r"s.

Then I switched to using [LLM](https://llm.datasette.io/) and the [llm\-ollama](https://github.com/taketwo/llm-ollama) plugin. I tried prompting it for Python that imports CSV into SQLite:

> `Write a Python function import_csv(conn, url, table_name) which acceopts a connection to a SQLite databse and a URL to a CSV file and the name of a table - it then creates that table with the right columns and imports the CSV data from that URL`

It thought through the different steps in detail and produced some [decent looking code](https://gist.github.com/simonw/d14fb1d710f1a07b07e7cc6698709f7d).

Finally, I tried this:

```
llm -m qwq 'Generate an SVG of a pelican riding a bicycle'

```

For some reason it answered in Simplified Chinese. It opened with this:

> 生成一个SVG图像，内容是一只鹈鹕骑着一辆自行车。这听起来挺有趣的！我需要先了解一下什么是SVG，以及如何创建这样的图像。

Which translates (using Google Translate) to:

> Generate an SVG image of a pelican riding a bicycle. This sounds interesting! I need to first understand what SVG is and how to create an image like this.

It then produced a lengthy essay discussing the many aspects that go into constructing a pelican on a bicycle \- [full transcript here](https://gist.github.com/simonw/d8a50200edd5d463b7ce0791c2242c87). After a full 227 seconds of constant output it produced this as the final result.

[![You can tell which bit is the bicycle and which bit is the pelican. It's quite elegant.](https://substackcdn.com/image/fetch/$s_!zzu5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc4f65b0c-1f97-4ce2-9832-a781e81e7203_400x200.svg "You can tell which bit is the bicycle and which bit is the pelican. It's quite elegant.")](https://substackcdn.com/image/fetch/$s_!zzu5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc4f65b0c-1f97-4ce2-9832-a781e81e7203_400x200.svg)

I think that's pretty good!

---

**Link** 2024\-11\-28 [SmolVLM \- small yet mighty Vision Language Model](https://huggingface.co/blog/smolvlm):

I've been having fun playing with this new vision model from the Hugging Face team behind [SmolLM](https://simonwillison.net/2024/Nov/2/smollm2/). They describe it as:

> \[...] a 2B VLM, SOTA for its memory footprint. SmolVLM is small, fast, memory\-efficient, and fully open\-source. All model checkpoints, VLM datasets, training recipes and tools are released under the Apache 2\.0 license.

I've tried it in a few flavours but my favourite so far is the [mlx\-vlm](https://github.com/Blaizzy/mlx-vlm) approach, via `mlx-vlm` author [Prince Canuma](https://twitter.com/Prince_Canuma/status/1862168514842280401). Here's the `uv` recipe I'm using to run it:

```
uv run \
  --with mlx-vlm \
  --with torch \
  python -m mlx_vlm.generate \
    --model mlx-community/SmolVLM-Instruct-bf16 \
    --max-tokens 500 \
    --temp 0.5 \
    --prompt "Describe this image in detail" \
    --image IMG_4414.JPG

```

If you run into an error using Python 3\.13 (torch compatibility) try `uv run --python 3.11` instead.

This one\-liner installs the necessary dependencies, downloads the model (about 4\.2GB, saved to `~/.cache/huggingface/hub/models--mlx-community--SmolVLM-Instruct-bf16`) and executes the prompt and displays the result.

I ran that against [this Pelican photo](https://static.simonwillison.net/static/2024/IMG_4414.JPG):

[![A glorious pelican on some rocks, two other pelicans are visible plus some other birds](https://substackcdn.com/image/fetch/$s_!ea0V!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3319f478-41e0-46d7-81e0-cf32dcbb7901_2592x1728.jpeg "A glorious pelican on some rocks, two other pelicans are visible plus some other birds")](https://substackcdn.com/image/fetch/$s_!ea0V!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3319f478-41e0-46d7-81e0-cf32dcbb7901_2592x1728.jpeg)

The model replied:

> In the foreground of this photograph, a pelican is perched on a pile of rocks. The pelican’s wings are spread out, and its beak is open. There is a small bird standing on the rocks in front of the pelican. The bird has its head cocked to one side, and it seems to be looking at the pelican. To the left of the pelican is another bird, and behind the pelican are some other birds. The rocks in the background of the image are gray, and they are covered with a variety of textures. The rocks in the background appear to be wet from either rain or sea spray.

There are a few spatial mistakes in that description but the vibes are generally in the right direction.

On my 64GB M2 MacBook pro it read the prompt at 7\.831 tokens/second and generated that response at an impressive 74\.765 tokens/second.

---

**Link** 2024\-11\-29 [LLM Flowbreaking](https://www.knostic.ai/blog/introducing-a-new-class-of-ai-attacks-flowbreaking):

Gadi Evron from Knostic:

> We propose that **LLM Flowbreaking**, following jailbreaking and prompt injection, joins as the third on the growing list of LLM attack types. Flowbreaking is less about whether prompt or response guardrails can be bypassed, and more about whether user inputs and generated model outputs can adversely affect these other components in the broader implemented system.

The key idea here is that some systems built on top of LLMs \- such as Microsoft Copilot \- implement an additional layer of safety checks which can sometimes cause the system to retract an already displayed answer.

I've seen this myself a few times, most notable with Claude 2 last year when it deleted an almost complete podcast transcript cleanup right in front of my eye because the hosts started talking about bomb threats.

Knostic calls this **Second Thoughts**, where an LLM system decides to retract its previous output. It's not hard for an attacker to grab this potentially harmful data: I've grabbed some using a quick copy and paste, or you can use tricks like [video scraping](https://simonwillison.net/2024/Oct/17/video-scraping/) or using the network browser tools.

They also describe a **Stop and Roll** attack, where the user clicks the "stop" button while executing a query against a model in a way that also prevents the moderation layer from having the chance to retract its previous output.

I'm not sure I'd categorize this as a completely new vulnerability class. If you implement a system where output is displayed to users you should expect that attempts to retract that data can be subverted \- screen capture software is widely available these days.

I wonder how widespread this retraction UI pattern is? I've seen it in Claude and evidently ChatGPT and Microsoft Copilot have the same feature. I don't find it particularly convincing \- it seems to me that it's more safety theatre than a serious mechanism for avoiding harm caused by unsafe output.

---

**Link** 2024\-11\-29 [GitHub OAuth for a static site using Cloudflare Workers](https://til.simonwillison.net/cloudflare/workers-github-oauth):

Here's a TIL covering a Thanksgiving AI\-assisted programming project. I wanted to add OAuth against GitHub to some of the projects on my [tools.simonwillison.net](https://tools.simonwillison.net/) site in order to implement "Save to Gist".

That site is entirely statically hosted by GitHub Pages, but OAuth has a required server\-side component: there's a `client_secret` involved that should never be included in client\-side code.

Since I serve the site from behind Cloudflare I realized that a minimal [Cloudflare Workers](https://workers.cloudflare.com/) script may be enough to plug the gap. I got Claude on my phone to build me a prototype and then pasted that (still on my phone) into a new Cloudflare Worker and it worked!

... almost. On later closer inspection of the code it was missing error handling... and then someone pointed out it was vulnerable to a login CSRF attack thanks to failure to check the `state=` parameter. I worked with Claude to fix those too.

Useful reminder here that pasting code AI\-generated code around on a mobile phone isn't necessarily the best environment to encourage a thorough code review!

---

**Quote** 2024\-11\-29

> *People have too inflated sense of what it means to "ask an AI" about something. The AI are language models trained basically by imitation on data from human labelers. Instead of the mysticism of "asking an AI", think of it more as "asking the average data labeler" on the internet. \[...]   
>   
> Post triggered by someone suggesting we ask an AI how to run the government etc. TLDR you're not asking an AI, you're asking some mashup spirit of its average data labeler.*

[Andrej Karpathy](https://twitter.com/karpathy/status/1862565643436138619)

---

**Quote** 2024\-11\-29

> *Among closed\-source models, [OpenAI](https://openai.com/)'s early mover advantage has eroded somewhat, with enterprise market share dropping from 50% to 34%. The primary beneficiary has been [Anthropic](https://menlovc.com/portfolio/anthropic/),\* which doubled its enterprise presence from 12% to 24% as some enterprises switched from GPT\-4 to Claude 3\.5 Sonnet when the new model became state\-of\-the\-art. When moving to a new LLM, organizations most commonly cite security and safety considerations (46%), price (44%), performance (42%), and expanded capabilities (41%) as motivations.*

[Menlo Ventures](https://menlovc.com/2024-the-state-of-generative-ai-in-the-enterprise/)

---

**Link** 2024\-11\-29 [Structured Generation w/ SmolLM2 running in browser \& WebGPU](https://huggingface.co/spaces/reach-vb/github-issue-generator-webgpu):

Extraordinary demo by Vaibhav Srivastav. Here's Hugging Face's [SmolLM2\-1\.7B\-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct) running directly in a web browser (using WebGPU, so requires Chrome [for the moment](https://github.com/gpuweb/gpuweb/wiki/Implementation-Status)) demonstrating structured text extraction, converting a text description of an image into a structured GitHub issue defined using JSON schema.

[![Interface showing text input, a JSON schema, extracted JSON and a UI that demonstrates the structured resulting GitHub Issue](https://substackcdn.com/image/fetch/$s_!lNyo!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F793bb914-26d3-40b8-8540-4e1f4c239d67_1984x1608.jpeg "Interface showing text input, a JSON schema, extracted JSON and a UI that demonstrates the structured resulting GitHub Issue")](https://substackcdn.com/image/fetch/$s_!lNyo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F793bb914-26d3-40b8-8540-4e1f4c239d67_1984x1608.jpeg)

The page loads 924\.8MB of model data (according to [this script to sum up files in window.caches](https://gist.github.com/simonw/3ccba6256e95b59ea6a17509855830b4)) and performs everything in\-browser. I did not know a model this small could produce such useful results.

Here's [the source code](https://github.com/Vaibhavs10/github-issue-generator-webgpu/blob/main/src/index.js) for the demo. It's around 200 lines of code, 50 of which are the JSON schema describing the data to be extracted.

The real secret sauce here is the [web\-llm](https://github.com/mlc-ai/web-llm) by MLC. This library has made loading and executing prompts through LLMs in the browser shockingly easy, and recently incorporated support for MLC's [XGrammar](https://xgrammar.mlc.ai/) library (also available in Python) which implements both JSON schema and EBNF\-based structured output guidance.

---