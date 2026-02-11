# Gemini 1.5 Flash-8B, FLUX 1.1 Python 3.13...

*... and Deno 2, and 34 links, 6 quotations and 4 TILs*

Published: 2024-10-14
Source: https://simonw.substack.com/p/gemini-15-flash-8b-flux-11-python

---

34 links, 6 quotations and 4 TILs

**Link** 2024\-10\-03 [Ask HN: What happens to ".io" TLD after UK gives back the Chagos Islands?](https://news.ycombinator.com/item?id=41729526):

This morning on the BBC: [UK will give sovereignty of Chagos Islands to Mauritius](https://www.bbc.com/news/articles/c98ynejg4l5o). The Chagos Islands include the area that the UK calls [the British Indian Ocean Territory](https://en.wikipedia.org/wiki/British_Indian_Ocean_Territory). The [.io ccTLD](https://en.wikipedia.org/wiki/.io) uses the ISO\-3166 two\-letter country code for that designation.

As the owner of [datasette.io](https://datasette.io/) the question of what happens to that ccTLD is suddenly very relevant to me.

This Hacker News conversation has some useful information. It sounds like there's a very real possibility that `.io` could be deleted after a few years notice \- it's happened before, for ccTLDs such as `.zr` for Zaire (which renamed to [Democratic Republic of the Congo](https://en.wikipedia.org/wiki/Democratic_Republic_of_the_Congo) in 1997, with `.zr` withdrawn in 2001\) and [.cs](https://en.wikipedia.org/wiki/.cs) for Czechoslovakia, withdrawn in 1995\.

Could `.io` change status to the same kind of TLD as `.museum`, unaffiliated with any particular geography? The convention is for two letter TLDs to exactly match ISO country codes, so that may not be an option.

---

**Link** 2024\-10\-03 [Announcing FLUX1\.1 \[pro] and the BFL API](https://blackforestlabs.ai/announcing-flux-1-1-pro-and-the-bfl-api/):

FLUX is the image generation model family from Black Forest Labs, a startup founded by members of the team that previously created Stable Diffusion.

Released today, FLUX1\.1 \[pro] continues the general trend of AI models getting both better and more efficient:

> FLUX1\.1 \[pro] provides six times faster generation than its predecessor FLUX.1 \[pro] while also improving image quality, prompt adherence, and diversity.

Black Forest Labs appear to have settled on a potentially workable business model: their smallest, fastest model FLUX.1 \[schnell] is Apache 2 licensed. The next step up is FLUX.1 \[dev] which is open weights for non\-commercial use only. The \[pro] models are closed weights, made available exclusively through their API or partnerships with other API providers.

I tried the new 1\.1 model out using [black\-forest\-labs/flux\-1\.1\-pro](https://replicate.com/black-forest-labs/flux-1.1-pro) on Replicate just now. Here's my prompt:

> Photograph of a Faberge egg representing the California coast. It should be decorated with ornate pelicans and sea lions and a humpback whale.

[![A beautiful faberge egg featuring a humpback whale and pelicans - it is located on a beach and sea lions on that beach are looking at it.](https://substackcdn.com/image/fetch/$s_!la-n!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc6dbf051-282d-4c3d-aeb6-28d767fd9067_1024x1024.jpeg "A beautiful faberge egg featuring a humpback whale and pelicans - it is located on a beach and sea lions on that beach are looking at it.")](https://substackcdn.com/image/fetch/$s_!la-n!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc6dbf051-282d-4c3d-aeb6-28d767fd9067_1024x1024.jpeg)

The FLUX models have a reputation for being really good at following complex prompts. In this case I wanted the sea lions to appear in the egg design rather than looking at the egg from the beach, but I imagine I could get better results if I continued to iterate on my prompt.

The FLUX models are also better at applying text than any other image models I've tried myself.

---

**Quote** 2024\-10\-03

> *At first, I struggled to understand why anyone would want to write this way. My dialogue with ChatGPT was frustratingly meandering, as though I were excavating an essay instead of crafting one. But, when I thought about the psychological experience of writing, I began to see the value of the tool. ChatGPT was not generating professional prose all at once, but it was providing starting points: interesting research ideas to explore; mediocre paragraphs that might, with sufficient editing, become usable. For all its inefficiencies, this indirect approach did feel easier than staring at a blank page; “talking” to the chatbot about the article was more fun than toiling in quiet isolation. In the long run, I wasn’t saving time: I still needed to look up facts and write sentences in my own voice. But my exchanges seemed to reduce the maximum mental effort demanded of me.*

[Cal Newport](https://www.newyorker.com/culture/annals-of-inquiry/what-kind-of-writer-is-chatgpt)

---

**Link** 2024\-10\-03 [Gemini 1\.5 Flash\-8B is now production ready](https://developers.googleblog.com/en/gemini-15-flash-8b-is-now-generally-available-for-use/):

Gemini 1\.5 Flash\-8B is "a smaller and faster variant of 1\.5 Flash" \- and is now released to production, at half the price of the 1\.5 Flash model.

It's really, really cheap:

* $0\.0375 per 1 million input tokens on prompts \<128K
* $0\.15 per 1 million output tokens on prompts \<128K
* $0\.01 per 1 million input tokens on cached prompts \<128K

Prices are doubled for prompts longer than 128K.

I believe images are still charged at a flat rate of 258 tokens, which I think means a single non\-cached image with Flash should cost 0\.00097 cents \- a number so tiny I'm doubting if I got the calculation right.

OpenAI's cheapest model remains GPT\-4o mini, at $0\.15/1M input \- though that drops to half of that for reused prompt prefixes thanks to their new prompt caching feature (or by half if you use batches, though those can’t be combined with OpenAI prompt caching. Gemini also offer half\-off for batched requests).

Anthropic's cheapest model is still Claude 3 Haiku at $0\.25/M, though that drops to $0\.03/M for cached tokens (if you configure them correctly).

I've released [llm\-gemini 0\.2](https://github.com/simonw/llm-gemini/releases/tag/0.2) with support for the new model:

```
llm install -U llm-gemini
llm keys set gemini
# Paste API key here
llm -m gemini-1.5-flash-8b-latest "say hi"

```

---

**Link** 2024\-10\-04 [Hybrid full\-text search and vector search with SQLite](https://alexgarcia.xyz/blog/2024/sqlite-vec-hybrid-search/index.html):

As part of Alex’s work on his [sqlite\-vec](https://github.com/asg017/sqlite-vec) SQLite extension \- adding fast vector lookups to SQLite \- he’s been investigating hybrid search, where search results from both vector similarity and traditional full\-text search are combined together.

The most promising approach looks to be [Reciprocal Rank Fusion](https://learn.microsoft.com/en-us/azure/search/hybrid-search-ranking), which combines the top ranked items from both approaches. Here’s Alex’s SQL query:

```
-- the sqlite-vec KNN vector search results
with vec_matches as (
  select
    article_id,
    row_number() over (order by distance) as rank_number,
    distance
  from vec_articles
  where
    headline_embedding match lembed(:query)
    and k = :k
),
-- the FTS5 search results
fts_matches as (
  select
    rowid,
    row_number() over (order by rank) as rank_number,
    rank as score
  from fts_articles
  where headline match :query
  limit :k
),
-- combine FTS5 + vector search results with RRF
final as (
  select
    articles.id,
    articles.headline,
    vec_matches.rank_number as vec_rank,
    fts_matches.rank_number as fts_rank,
    -- RRF algorithm
    (
      coalesce(1.0 / (:rrf_k + fts_matches.rank_number), 0.0)  :weight_fts +
      coalesce(1.0 / (:rrf_k + vec_matches.rank_number), 0.0)  :weight_vec
    ) as combined_rank,
    vec_matches.distance as vec_distance,
    fts_matches.score as fts_score
  from fts_matches
  full outer join vec_matches on vec_matches.article_id = fts_matches.rowid
  join articles on articles.rowid = coalesce(fts_matches.rowid, vec_matches.article_id)
  order by combined_rank desc
)
select * from final;
```

I’ve been puzzled in the past over how to best do that because the distance scores from vector similarity and the relevance scores from FTS are meaningless in comparison to each other. RRF doesn’t even attempt to compare them \- it uses them purely for `row_number()` ranking within each set and combines the results based on that.

---

**TIL** 2024\-10\-04 [Compiling and running sqlite3\-rsync](https://til.simonwillison.net/sqlite/compile-sqlite3-rsync):

Today I heard about the [sqlite3\-rsync](https://sqlite.org/draft/rsync.html) command, currently available in a branch in the SQLite code repository. It provides a mechanism for efficiently creating or updating a copy of a SQLite database that is running in WAL mode, either locally or via SSH to another server. …

---

**Link** 2024\-10\-04 [Database Remote\-Copy Tool For SQLite (draft)](https://sqlite.org/draft/rsync.html):

Neat new SQLite utilities often show up in branches of the SQLite repository. Here's a new one from last month: `sqlite3-rsync`, providing tools for efficiently creating and updating copies of WAL\-mode SQLite databases on either the same machine or across remote machines via SSH.

The way it works is neat, inspired by `rsync` (hence the tool's name):

> The protocol is for the replica to send a cryptographic hash of each of its pages over to the origin side, then the origin sends back the complete content of any page for which the hash does not match.

SQLite's default page size is 4096 bytes and a hash is 20 bytes, so if nothing has changed then the client will transmit 0\.5% of the database size in hashes and get nothing back in return.

The tool takes full advantage of [SQLite's WAL mode](https://sqlite.org/wal.html) \- when you run it you'll get an exact snapshot of the database state as it existed at the moment the copy was initiated, even if the source database continues to apply changes.

I wrote up [a TIL on how to compile it](https://til.simonwillison.net/sqlite/compile-sqlite3-rsync) \- short version:

```
cd /tmp
git clone https://github.com/sqlite/sqlite.git
cd sqlite
git checkout sqlite3-rsync
./configure
make sqlite3.c
cd tool
gcc -o sqlite3-rsync sqlite3-rsync.c ../sqlite3.c -DSQLITE_ENABLE_DBPAGE_VTAB
./sqlite3-rsync --help

```

**Update:** It turns out you can now just run `./configure && make sqlite-rsync` in the root checkout.

Something I’ve worried about in the past is that if I want to make a snapshot backup of a SQLite database I need enough additional free disk space to entirely duplicate the current database first (using the backup mechanism or `VACUUM INTO`). This tool fixes that \- I don’t need any extra disk space at all, since the pages that have been updated will be transmitted directly over the wire in 4096 byte chunks.

I tried feeding the [1800 lines of C](https://github.com/sqlite/sqlite/blob/sqlite3-rsync/tool/sqlite3-rsync.c) through OpenAI’s `o1-preview` with the prompt “Explain the protocol over SSH part of this” and [got a pretty great high level explanation](https://chatgpt.com/share/6701450c-bc9c-8006-8c9e-468ab6f67e4b) \- [markdown copy here](https://gist.github.com/simonw/ffbf90e0602df04c2f6b387de42acba4).

---

**Link** 2024\-10\-05 [Wikidata is a Giant Crosswalk File](https://www.dbreunig.com/2024/10/04/wikidata-is-a-giant-crosswalk-file.html):

Drew Breunig shows how to take the 140GB Wikidata JSON export, use `sed 's/,$//'` to convert it to newline\-delimited JSON, then use DuckDB to run queries and extract external identifiers, including a query that pulls out 500MB of latitude and longitude points.

---

**Link** 2024\-10\-05 [marimo v0\.9\.0 with mo.ui.chat](https://marimo.io/blog/marimo-0-9-0):

The latest release of the Marimo Python reactive notebook project includes a neat new feature: you can now easily embed a custom chat interface directly inside of your notebook.

Marimo co\-founder Myles Scolnick [posted this intriguing demo](https://twitter.com/themylesfiles/status/1842278470929318283) on Twitter, demonstrating a chat interface to my [LLM library](https://llm.datasette.io/) “in only 3 lines of code”:

```
import marimo as mo
import llm

model = llm.get_model()
conversation = model.conversation()
mo.ui.chat(lambda messages: conversation.prompt(messages[-1].content))
```

I tried that out today \- here’s the result:

[![Screenshot of a Marimo notebook editor, with lines of code and an embedded chat interface. Top: import marimo as mo and import llm. Middle: Chat messages - User: Hi there, Three jokes about pelicans. AI: Hello! How can I assist you today?, Sure! Here are three pelican jokes for you: 1. Why do pelicans always carry a suitcase? Because they have a lot of baggage to handle! 2. What do you call a pelican that can sing? A tune-ican! 3. Why did the pelican break up with his girlfriend? She said he always had his head in the clouds and never winged it! Hope these made you smile! Bottom code: model = llm.get_model(), conversation = model.conversation(), mo.ui.chat(lambda messages:, conversation.prompt(messages[-1].content))](https://substackcdn.com/image/fetch/$s_!6gKV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F99635446-d7b0-44d1-8687-ffc6f0c5d71d_1192x1426.jpeg "Screenshot of a Marimo notebook editor, with lines of code and an embedded chat interface. Top: import marimo as mo and import llm. Middle: Chat messages - User: Hi there, Three jokes about pelicans. AI: Hello! How can I assist you today?, Sure! Here are three pelican jokes for you: 1. Why do pelicans always carry a suitcase? Because they have a lot of baggage to handle! 2. What do you call a pelican that can sing? A tune-ican! 3. Why did the pelican break up with his girlfriend? She said he always had his head in the clouds and never winged it! Hope these made you smile! Bottom code: model = llm.get_model(), conversation = model.conversation(), mo.ui.chat(lambda messages:, conversation.prompt(messages[-1].content))")](https://substackcdn.com/image/fetch/$s_!6gKV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F99635446-d7b0-44d1-8687-ffc6f0c5d71d_1192x1426.jpeg)

[marimo.ui.chat()](https://docs.marimo.io/api/inputs/chat.html) takes a function which is passed a list of Marimo chat messages (representing the current state of that widget) and returns a string \- or other type of renderable object \- to add as the next message in the chat. This makes it trivial to hook in any custom chat mechanism you like.

Marimo also ship their own [built\-in chat handlers](https://docs.marimo.io/api/inputs/chat.html#using-a-built-in-ai-model) for OpenAI, Anthropic and Google Gemini which you can use like this:

```
mo.ui.chat(
    mo.ai.llm.anthropic(
        "claude-3-5-sonnet-20240620",
        system_message="You are a helpful assistant.",
        api_key="sk-ant-...",
    ),
    show_configuration_controls=True
)
```

---

**Link** 2024\-10\-05 [UV with GitHub Actions to run an RSS to README project](https://micro.webology.dev/2024/10/05/uv-with-github.html):

Jeff Triplett demonstrates a very neat pattern for using [uv](https://docs.astral.sh/uv/) to run Python scripts with their dependencies inside of GitHub Actions. First, add `uv` to the workflow using the [setup\-uv action](https://github.com/astral-sh/setup-uv):

```
- uses: astral-sh/setup-uv@v3
  with:
    enable-cache: true
    cache-dependency-glob: "*.py"

```

This enables the caching feature, which stores uv's own cache of downloads from PyPI between runs. The `cache-dependency-glob` key ensures that this cache will be invalidated if any `.py` file in the repository is updated.

Now you can run Python scripts using steps that look like this:

```
- run: uv run fetch-rss.py

```

If that Python script begins with some dependency definitions ([PEP 723](https://peps.python.org/pep-0723/)) they will be automatically installed by `uv run` on the first run and reused from the cache in the future. From the start of [fetch\-rss.py](https://github.com/django-news/.github/blob/0c2fa0284257e11dc5c149ef411469737dac2c41/fetch-rss.py#L1-L7):

```
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "feedparser",
#     "typer",
# ]
# ///

```

`uv` will download the required Python version and cache that as well.

---

**Quote** 2024\-10\-06

> *Students who use AI as a crutch don’t learn anything. It prevents them from thinking. Instead, using AI as co\-intelligence is important because it increases your capabilities and also keeps you in the loop. \[…]   
>   
> AI does so many things that we need to set guardrails on what we don’t want to give up. It’s a very weird, general\-purpose technology, which means it will affect all kinds of things, and we’ll have to adjust socially.*

[Ethan Mollick](https://english.elpais.com/technology/2024-10-03/ethan-mollick-analyst-students-who-use-ai-as-a-crutch-dont-learn-anything.html)

---

**Link** 2024\-10\-06 [SVG to JPG/PNG](https://tools.simonwillison.net/svg-render):

The latest in my [ongoing series](https://tools.simonwillison.net/) of interactive HTML and JavaScript tools written almost entirely by LLMs. This one lets you paste in (or open\-from\-file, or drag\-onto\-page) some SVG and then use that to render a JPEG or PNG image of your desired width.

[![Screenshot of the SVG to JPEG/PNG tool. It starts with a Browse... option for selecting a file, next to a Load example image link, above a textarea full of SVG code. Then a radio box to select between JPEG and PNG, plus a background color color picker widget next to a checkbox labelled transparent. Then Output width, a number field set to 300. Then a convert SVG button. Below is the classic SVG tiger image, with a Download image link that says 47.38BK. Under that is a Base 64 image tag header with a copy image tag button and some visible HTML for a data:image/jpeg image element.](https://substackcdn.com/image/fetch/$s_!LGvk!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F71af4ec6-1217-443c-9e58-2da39408953d_1210x1825.jpeg "Screenshot of the SVG to JPEG/PNG tool. It starts with a Browse... option for selecting a file, next to a Load example image link, above a textarea full of SVG code. Then a radio box to select between JPEG and PNG, plus a background color color picker widget next to a checkbox labelled transparent. Then Output width, a number field set to 300. Then a convert SVG button. Below is the classic SVG tiger image, with a Download image link that says 47.38BK. Under that is a Base 64 image tag header with a copy image tag button and some visible HTML for a data:image/jpeg image element.")](https://substackcdn.com/image/fetch/$s_!LGvk!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F71af4ec6-1217-443c-9e58-2da39408953d_1210x1825.jpeg)

I built this using Claude 3\.5 Sonnet, initially as an Artifact and later in a code editor since some of the features (loading an example image and downloading the result) cannot run in the sandboxed iframe Artifact environment.

Here's [the full transcript](https://gist.github.com/simonw/b06fd62ad4e9f8762ad15cdf17e1be85) of the Claude conversation I used to build the tool, plus [a few commits](https://github.com/simonw/tools/commits/main/svg-render.html) I later made by hand to further customize it.

The [code itself](https://github.com/simonw/tools/blob/main/svg-render.html) is mostly quite simple. The most interesting part is how it renders the SVG to an image, which (simplified) looks like this:

```
// First extract the viewbox to get width/height
const svgElement = new DOMParser().parseFromString(
    svgInput, 'image/svg+xml'
).documentElement;
let viewBox = svgElement.getAttribute('viewBox');
[, , width, height] = viewBox.split(' ').map(Number);
// Figure out the width/height of the output image
const newWidth = parseInt(widthInput.value) || 800;
const aspectRatio = width / height;
const newHeight = Math.round(newWidth / aspectRatio);
// Create off-screen canvas
const canvas = document.createElement('canvas');
canvas.width = newWidth;
canvas.height = newHeight;
// Draw SVG on canvas
const svgBlob = new Blob([svgInput], {type: 'image/svg+xml;charset=utf-8'});
const svgUrl = URL.createObjectURL(svgBlob);
const img = new Image();
const ctx = canvas.getContext('2d');
img.onload = function() {
    ctx.drawImage(img, 0, 0, newWidth, newHeight);
    URL.revokeObjectURL(svgUrl);
    // Convert that to a JPEG
    const imageDataUrl = canvas.toDataURL("image/jpeg");
    const convertedImg = document.createElement('img');
    convertedImg.src = imageDataUrl;
    imageContainer.appendChild(convertedImg);
};
img.src = svgUrl;
```

Here's the MDN explanation of [that revokeObjectURL() method](https://developer.mozilla.org/en-US/docs/Web/API/URL/revokeObjectURL_static), which I hadn't seen before.

> Call this method when you've finished using an object URL to let the browser know not to keep the reference to the file any longer.

---

**Link** 2024\-10\-07 [VTracer](https://www.visioncortex.org/vtracer/):

VTracer is [an open source library](https://github.com/visioncortex/vtracer) written in Rust for converting raster images (JPEG, PNG etc) to vector SVG.

This VTracer web app provides access to a WebAssembly compiled version of the library, with a UI that lets you open images, tweak the various options and download the resulting SVG.

[![Screenshot of VisionCortex VTracer web interface. Central image shows a surreal scene with a giant pelican wearing a monocle, overlooking a coastal city with yachts and an F1 car. UI elements include: logo, download options, and image processing controls for clustering, filtering, color precision, gradient step, and curve fitting.](https://substackcdn.com/image/fetch/$s_!RjZR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5fd16bfb-3ed4-4342-b732-ad131090da3f_1646x1426.jpeg "Screenshot of VisionCortex VTracer web interface. Central image shows a surreal scene with a giant pelican wearing a monocle, overlooking a coastal city with yachts and an F1 car. UI elements include: logo, download options, and image processing controls for clustering, filtering, color precision, gradient step, and curve fitting.")](https://substackcdn.com/image/fetch/$s_!RjZR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5fd16bfb-3ed4-4342-b732-ad131090da3f_1646x1426.jpeg)

I heard about this today [on Twitter](https://twitter.com/jpohhhh/status/1843138776769708389) in a reply to my tweet demonstrating a much, much simpler [Image to SVG tool](https://tools.simonwillison.net/image-to-svg) I built with the [help of Claude](https://gist.github.com/simonw/d2e724c357786371d7cc4b5b5bb87ed0) and the handy [imagetracerjs library](https://github.com/jankovicsandras/imagetracerjs) by András Jankovics.

---

**Link** 2024\-10\-07 [fav.farm](https://fav.farm/):

Neat little site by Wes Bos: it serves SVG (or PNG [for Safari](https://github.com/wesbos/favicon/blob/dd3e2fcddfbb01cfb9080c70d0c89853d7372f68/index.ts#L69)) favicons of every Emoji, which can be added to any site like this:

```
<link rel="icon" href="https://fav.farm/🔥" />

```

The source code is [on GitHub](https://github.com/wesbos/favicon). It runs on Deno and Deno Deploy, and recently added per\-Emoji hit counters powered by the Deno KV store, implemented in [db.ts](https://github.com/wesbos/favicon/blob/dd3e2fcddfbb01cfb9080c70d0c89853d7372f68/db.ts) using this pattern:

```
export function incrementCount(emoji: string) {
  const VIEW_KEY = [`favicon`, `${emoji}`];
  return db.atomic().sum(
    VIEW_KEY, 1n
  ).commit(); // Increment KV by 1
}

```

---

**Link** 2024\-10\-07 [Datasette 0\.65](https://docs.datasette.io/en/stable/changelog.html#v0-65):

[Python 3\.13](https://docs.python.org/3.13/whatsnew/3.13.html) was released today, which broke compatibility with the Datasette 0\.x series due to an issue with an underlying dependency. [I've fixed that problem](https://github.com/simonw/datasette/issues/2434) by vendoring and fixing the dependency and the new 0\.65 release works on Python 3\.13 (but drops support for Python 3\.8, which is [EOL](https://devguide.python.org/versions/) this month). Datasette 1\.0a16 added support for Python 3\.13 [last month](https://docs.datasette.io/en/latest/changelog.html#a16-2024-09-05).

---

**Link** 2024\-10\-07 [What's New in Ruby on Rails 8](https://blog.appsignal.com/2024/10/07/whats-new-in-ruby-on-rails-8.html):

> Rails 8 takes SQLite from a lightweight development tool to a reliable choice for production use, thanks to extensive work on the SQLite adapter and Ruby driver.
> 
> With the introduction of the solid adapters discussed above, SQLite now has the capability to power Action Cable, Rails.cache, and Active Job effectively, expanding its role beyond just prototyping or testing environments. \[...]
> 
> * Transactions default to `IMMEDIATE` mode to improve concurrency.

Also included in Rails 8: [Kamal](https://kamal-deploy.org/), a new automated deployment system by 37signals for self\-hosting web applications on hardware or virtual servers:

> Kamal basically is Capistrano for Containers, without the need to carefully prepare servers in advance. No need to ensure that the servers have just the right version of Ruby or other dependencies you need. That all lives in the Docker image now. You can boot a brand new Ubuntu (or whatever) server, add it to the list of servers in Kamal, and it’ll be auto\-provisioned with Docker, and run right away.

More from the [official blog post about the release](https://rubyonrails.org/2024/9/27/rails-8-beta1-no-paas-required):

> At 37signals, we're building a growing suite of apps that use SQLite in production with [ONCE](https://once.com/). There are now thousands of installations of both [Campfire](https://once.com/campfire) and [Writebook](https://once.com/writebook) running in the wild that all run SQLite. This has meant a lot of real\-world pressure on ensuring that Rails (and Ruby) is working that wonderful file\-based database as well as it can be. Through proper defaults like WAL and IMMEDIATE mode. Special thanks to Stephen Margheim for [a slew of such improvements](https://github.com/rails/rails/pulls?q=is%3Apr+author%3Afractaledmind) and Mike Dalessio for [solving a last\-minute SQLite file corruption issue](https://github.com/sparklemotion/SQLite3-ruby/pull/558) in the Ruby driver.

---

**Link** 2024\-10\-07 [What's New In Python 3\.13](https://docs.python.org/3/whatsnew/3.13.html):

It's Python 3\.13 release day today. The big signature features are a [better REPL](https://docs.python.org/3.13/whatsnew/3.13.html#whatsnew313-better-interactive-interpreter) with improved error messages, an option to [run Python without the GIL](https://docs.python.org/3.13/whatsnew/3.13.html#free-threaded-cpython) and the beginnings of [the new JIT](https://docs.python.org/3.13/whatsnew/3.13.html#an-experimental-just-in-time-jit-compiler). Here are some of the smaller highlights I spotted while perusing the release notes.

iOS and Android are both now [Tier 3 supported platforms](https://docs.python.org/3.13/whatsnew/3.13.html#support-for-mobile-platforms), thanks to the efforts of Russell Keith\-Magee and the [Beeware](https://beeware.org/) project. Tier 3 [means](https://peps.python.org/pep-0011/#tier-3) "must have a reliable buildbot" but "failures on these platforms do not block a release". This is still a really big deal for Python as a mobile development platform.

There's a whole bunch of smaller stuff relevant to SQLite.

Python's [dbm module](https://docs.python.org/3.13/library/dbm.html) has long provided a disk\-backed key\-value store against multiple different backends. 3\.13 introduces a new backend based on SQLite, and makes it the default.

```
>>> import dbm
>>> db = dbm.open("/tmp/hi", "c")
>>> db["hi"] = 1
```

The `"c"` option means "Open database for reading and writing, creating it if it doesn’t exist".

After running the above, `/tmp/hi` was a SQLite database containing the following data:

```
sqlite3 /tmp/hi .dump
PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE Dict (
    key BLOB UNIQUE NOT NULL,
    value BLOB NOT NULL
  );
INSERT INTO Dict VALUES(X'6869',X'31');
COMMIT;

```

The `dbm.open()` function can detect which type of storage is being referenced. I found the implementation for that in the [whichdb(filename)](https://github.com/python/cpython/blob/v3.13.0/Lib/dbm/__init__.py#L98-L189) function.

I was hopeful that this change would mean Python 3\.13 deployments would be guaranteed to ship with a more recent SQLite... but it turns out 3\.15\.2 is [from November 2016](https://www.sqlite.org/changes.html#version_3_15_2) so still quite old:

> SQLite 3\.15\.2 or newer is required to build the `sqlite3` extension module. (Contributed by Erlend Aasland in [gh\-105875](https://github.com/python/cpython/issues/105875).)

The `conn.iterdump()` SQLite method now accepts an optional `filter=` keyword argument taking a LIKE pattern for the tables that you want to dump. I found [the implementation for that here](https://github.com/python/cpython/commit/1a10437a14b13100bdf41cbdab819c33258deb65#diff-445686d2c16ed3989d2adeac33729d1b06765dcf315f117fe8668be101b1e269R35).

And one last change which caught my eye because I could imagine having code that might need to be updated to reflect the new behaviour:

> `pathlib.Path.glob()` and `rglob()` now return both files and directories if a pattern that ends with "`**`" is given, rather than directories only. Add a trailing slash to keep the previous behavior and only match directories.

With the release of Python 3\.13, Python 3\.8 is [officially end\-of\-life](https://discuss.python.org/t/python-3-8-is-now-officially-eol/66983). Łukasz Langa:

> If you're still a user of Python 3\.8, I don't blame you, it's a lovely version. But it's time to move on to newer, greater things. Whether it's typing generics in built\-in collections, pattern matching, `except*`, low\-impact monitoring, or a new pink REPL, I'm sure you'll find your favorite new feature in one of the versions we still support. So upgrade today!

---

**Link** 2024\-10\-07 [Thoughts on the Treasurer Role at Tech NonProfits](https://wsvincent.com/thoughts-on-pyconnz/):

Will Vincent, Django Software Foundation treasurer from 2020\-2022, explains what’s involved in the non\-profit role with the highest level of responsibility and trust.

---

**Link** 2024\-10\-08 [Django Commons](https://github.com/django-commons):

Django Commons is a really promising initiative started by Tim Schilling, aimed at the problem of keeping key Django community projects responsibly maintained on a long\-term basis.

> Django Commons is an organization dedicated to supporting the community's efforts to maintain packages. It seeks to improve the maintenance experience for all contributors; reducing the barrier to entry for new contributors and reducing overhead for existing maintainers.

I’ve stated recently that I’d love to see the Django Software Foundation take on this role \- adopting projects and ensuring they are maintained long\-term. Django Commons looks like it solves that exact problem, assuring the future of key projects beyond their initial creators.

So far the Commons has taken on responsibility for [django\-fsm\-2](https://github.com/django-commons/django-fsm-2), [django\-tasks\-scheduler](https://github.com/django-commons/django-tasks-scheduler) and, as\-of this week, [diango\-typer](https://github.com/django-commons/django-typer).

Here’s Tim [introducing the project](https://www.better-simple.com/django/2024/05/22/looking-for-help-django-commons/) back in May. Thoughtful governance has been baked in from the start:

> Having multiple administrators makes the role more sustainable, lessens the impact of a person stepping away, and shortens response time for administrator requests. It’s important to me that the organization starts with multiple administrators so that collaboration and documentation are at the forefront of all decisions.

---

**Link** 2024\-10\-08 [Anthropic: Message Batches (beta)](https://docs.anthropic.com/en/docs/build-with-claude/message-batches):

Anthropic now have a batch mode, allowing you to send prompts to Claude in batches which will be processed within 24 hours (though probably much faster than that) and come at a 50% price discount.

This matches the batch models offered [by OpenAI](https://platform.openai.com/docs/guides/batch) and [by Google Gemini](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/batch-prediction-gemini), both of which also provide a 50% discount.

---

**Link** 2024\-10\-08 [If we had $1,000,000…](https://jacobian.org/2024/oct/8/dsf-one-million/):

Jacob Kaplan\-Moss gave my favorite talk at DjangoCon this year, imagining what the Django Software Foundation could do if it quadrupled its annual income to $1 million and laying out a realistic path for getting there. Jacob suggests leaning more into large donors than increasing our small donor base:

> It’s far easier for me to picture convincing eight or ten or fifteen large companies to make large donations than it is to picture increasing our small donor base tenfold. So I think a major donor strategy is probably the most realistic one for us.
> 
> So when I talk about major donors, who am I talking about? I’m talking about four major categories: large corporations, high net worth individuals (very wealthy people), grants from governments (e.g. the Sovereign Tech Fund run out of Germany), and private foundations (e.g. the Chan Zuckerberg Initiative, who’s given grants to the PSF in the past).

Also included: a TIL on [Turning a conference talk into an annotated presentation](https://jacobian.org/til/talk-to-writeup-workflow/). Jacob used [my annotated presentation tool](https://til.simonwillison.net/tools/annotated-presentations) to OCR text from images of keynote slides, extracted a Whisper transcript from the YouTube livestream audio and then cleaned that up a little with [LLM](https://llm.datasette.io) and Claude 3\.5 Sonnet (`"Split the content of this transcript up into paragraphs with logical breaks. Add newlines between each paragraph."`) before editing and re\-writing it all into the final post.

---

**TIL** 2024\-10\-09 [Collecting replies to tweets using JavaScript](https://til.simonwillison.net/twitter/collecting-replies):

I ran [a survey](https://twitter.com/simonw/status/1843290729260703801) on Twitter the other day to try and figure out what people mean when they use the term "agents" with respect to AI. …

---

**TIL** 2024\-10\-09 [Upgrading Homebrew and avoiding the failed to verify attestation error](https://til.simonwillison.net/homebrew/no-verify-attestations):

I managed to get my Homebrew installation back into shape today. The first problem I was having is that it complained that macOS Sequoia was unsupported: …

---

**Link** 2024\-10\-09 [otterwiki](https://github.com/redimp/otterwiki):

It's been a while since I've seen a new\-ish Wiki implementation, and this one by Ralph Thesen is really nice. It's written in Python (Flask \+ SQLAlchemy \+ [mistune](https://github.com/lepture/mistune) for Markdown \+ [GitPython](https://github.com/gitpython-developers/GitPython)) and keeps all of the actual wiki content as Markdown files in a local Git repository.

The [installation instructions](https://otterwiki.com/Installation) are a little in\-depth as they assume a production installation with Docker or systemd \- I figured out [this recipe](https://github.com/redimp/otterwiki/issues/146) for trying it locally using `uv`:

```
git clone https://github.com/redimp/otterwiki.git
cd otterwiki

mkdir -p app-data/repository
git init app-data/repository

echo "REPOSITORY='${PWD}/app-data/repository'" >> settings.cfg
echo "SQLALCHEMY_DATABASE_URI='sqlite:///${PWD}/app-data/db.sqlite'" >> settings.cfg
echo "SECRET_KEY='$(echo $RANDOM | md5sum | head -c 16)'" >> settings.cfg

export OTTERWIKI_SETTINGS=$PWD/settings.cfg
uv run --with gunicorn gunicorn --bind 127.0.0.1:8080 otterwiki.server:app

```

---

**Link** 2024\-10\-09 [The Fair Source Definition](https://fair.io/about/):

Fail Source ([fair.io](https://fair.io/)) is the new\-ish initiative from Chad Whitacre and Sentry aimed at providing an alternative licensing philosophy that provides additional protection for the business models of companies that release their code.

I like that they're establishing a new brand for this and making it clear that it's a separate concept from Open Source. Here's their definition:

> Fair Source is an alternative to closed source, allowing you to safely share access to your core products. Fair Source Software (FSS):
> 
> 1. is publicly available to read;
> 2. allows use, modification, and redistribution with minimal restrictions to protect the producer’s business model; and
> 3. undergoes delayed Open Source publication (DOSP).

They link to the [Delayed Open Source Publication](https://opensource.org/delayed-open-source-publication) research paper published by [OSI in January](https://opensource.org/blog/a-historic-view-of-the-practice-to-delay-releasing-open-source-software-osis-report). (I was frustrated that this is only available as a PDF, so I [converted it to Markdown](https://gist.github.com/simonw/7b913aaaff8278d2baaed86e43ece748) using Gemini 1\.5 Pro so I could read it on my phone.)

The most interesting background I could find on Fair Source was [this GitHub issues thread](https://github.com/fairsource/fair.io/issues/14), started in May, where Chad and other contributors fleshed out the initial launch plan over the course of several months.

---

**Link** 2024\-10\-09 [Free Threaded Python With Asyncio](https://blog.changs.co.uk/free-threaded-python-with-asyncio.html):

Jamie Chang expanded [my free\-threaded Python experiment](https://til.simonwillison.net/python/trying-free-threaded-python) from a few months ago to explore the interaction between Python's `asyncio` and the new GIL\-free build of Python 3\.13\.

The results look really promising. Jamie says:

> Generally when it comes to Asyncio, the discussion around it is always about the performance or lack there of. Whilst peroformance is certain important, the ability to reason about concurrency is the biggest benefit. \[...]
> 
> Depending on your familiarity with AsyncIO, it might actually be the simplest way to start a thread.

This code for running a Python function in a thread really is very pleasant to look at:

```
result = await asyncio.to_thread(some_function, *args, **kwargs)

```

Jamie also demonstrates [asyncio.TaskGroup](https://docs.python.org/3/library/asyncio-task.html#task-groups), which makes it easy to execute a whole bunch of threads and wait for them all to finish:

```
async with TaskGroup() as tg:
    for _ in range(args.tasks):
        tg.create_task(to_thread(cpu_bound_task, args.size))

```

---

**Link** 2024\-10\-09 [Forums are still alive, active, and a treasure trove of information](https://aftermath.site/best-active-forums-internet-today):

Chris Person:

> When I want information, like the real stuff, I go to forums. Over the years, forums did not really get smaller, so much as the rest of the internet just got bigger. Reddit, Discord and Facebook groups have filled a lot of that space, but there is just certain information that requires the dedication of adults who have specifically signed up to be in one kind of community.

This is a *very* comprehensive directory of active forums.

---

**Link** 2024\-10\-10 [Announcing Deno 2](https://deno.com/blog/v2.0):

The big focus of Deno 2 is compatibility with the existing Node.js and npm ecosystem:

> Deno 2 takes all of the features developers love about Deno 1\.x — zero\-config, all\-in\-one toolchain for JavaScript and TypeScript development, web standard API support, secure by default — and makes it fully backwards compatible with Node and npm (in ESM).

The npm support [is documented here](https://docs.deno.com/runtime/fundamentals/node/#using-npm-packages). You can write a script like this:

```
import * as emoji from "npm:node-emoji";
console.log(emoji.emojify(:sauropod: :heart:  npm));
```

And when you run it Deno will automatically fetch and cache the required dependencies:

```
deno run main.js

```

Another new feature that caught my eye was this:

> `deno jupyter` now supports outputting images, graphs, and HTML

Deno has apparently shipped with [a Jupyter notebook kernel](https://docs.deno.com/runtime/reference/cli/jupyter/) for a while, and it's had a major upgrade in this release.

Here's [Ryan Dahl's demo](https://www.youtube.com/watch?v=d35SlRgVxT8&t=1829s) of the new notebook support in his Deno 2 release video.

I tried this out myself, and it's really neat. First you need to install the kernel:

```
deno juptyer --install

```

I was curious to find out what this actually did, so I dug around [in the code](https://github.com/denoland/deno/blob/251840a60d1e2ba4ceca85029bd8cc342b6cd038/cli/tools/jupyter/install.rs#L48-L57) and then further [in the Rust runtimed dependency](https://github.com/runtimed/runtimed/blob/e2cd9b1d88e44842e1b1076d3a1d1f202fcf7879/runtimelib/src/jupyter/dirs.rs#L81-L99). It turns out installing Jupyter kernels, at least on macOS, involves creating a directory in `~/Library/Jupyter/kernels/deno` and writing a `kernel.json` file containing the following:

```
{
  "argv": [
    "/opt/homebrew/bin/deno",
    "jupyter",
    "--kernel",
    "--conn",
    "{connection_file}"
  ],
  "display_name": "Deno",
  "language": "typescript"
}
```

That file is picked up by any Jupyter servers running on your machine, and tells them to run `deno jupyter --kernel ...` to start a kernel.

I started Jupyter like this:

```
jupyter-notebook /tmp

```

Then started a new notebook, selected the Deno kernel and it worked as advertised:

[![Jupyter notebook running the Deno kernel. I run 4 + 5 and get 9, then Deno.version and get back 2.0.0. I import Observable Plot and the penguins data, then render a plot which shows as a scatter chart.](https://substackcdn.com/image/fetch/$s_!2wwm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbc605453-8d0c-40d6-80c9-7cc452dd3762_1384x1814.jpeg "Jupyter notebook running the Deno kernel. I run 4 + 5 and get 9, then Deno.version and get back 2.0.0. I import Observable Plot and the penguins data, then render a plot which shows as a scatter chart.")](https://substackcdn.com/image/fetch/$s_!2wwm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbc605453-8d0c-40d6-80c9-7cc452dd3762_1384x1814.jpeg)

```
import * as Plot from "npm:@observablehq/plot";
import { document, penguins } from "jsr:@ry/jupyter-helper";
let p = await penguins();

Plot.plot({
  marks: [
    Plot.dot(p.toRecords(), {
      x: "culmen_depth_mm",
      y: "culmen_length_mm",
      fill: "species",
    }),
  ],
  document,
});
```

---

**TIL** 2024\-10\-10 [Livestreaming a community election event on YouTube](https://til.simonwillison.net/youtube/livestreaming):

I live in El Granada, California. Wikipedia calls us [a census designated place](https://en.wikipedia.org/wiki/El_Granada,_California) \- we don't have a mayor or city council. But we do have a [Community Services District](https://granada.ca.gov/) \- originally responsible for our sewers, and since 2014 also responsible for our parks. And we get to vote for the board members [in the upcoming November election](https://granada.ca.gov/2024-candidate-listing)! …

---

**Link** 2024\-10\-10 [Bridging Language Gaps in Multilingual Embeddings via Contrastive Learning](https://jina.ai/news/bridging-language-gaps-in-multilingual-embeddings-via-contrastive-learning/):

Most text embeddings models suffer from a "language gap", where phrases in different languages with the same semantic meaning end up with embedding vectors that aren't clustered together.

Jina claim their new [jina\-embeddings\-v3](https://jina.ai/news/jina-embeddings-v3-a-frontier-multilingual-embedding-model) (CC BY\-NC 4\.0, which means you need to license it for commercial use if you're not using [their API](https://jina.ai/embeddings/)) is much better on this front, thanks to a training technique called "contrastive learning".

> There are 30 languages represented in our contrastive learning dataset, but 97% of pairs and triplets are in just one language, with only 3% involving cross\-language pairs or triplets. But this 3% is enough to produce a dramatic result: Embeddings show very little language clustering and semantically similar texts produce close embeddings regardless of their language

[![Scatter plot diagram, titled Desired Outcome: Clustering by Meaning. My dog is blue and Mein Hund ist blau are located near to each other, and so are Meine Katze ist rot and My cat is red](https://substackcdn.com/image/fetch/$s_!qfxn!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fecd97969-84e2-4147-973d-1311ce73b080_1815x1014.png "Scatter plot diagram, titled Desired Outcome: Clustering by Meaning. My dog is blue and Mein Hund ist blau are located near to each other, and so are Meine Katze ist rot and My cat is red")](https://substackcdn.com/image/fetch/$s_!qfxn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fecd97969-84e2-4147-973d-1311ce73b080_1815x1014.png)

---

**Quote** 2024\-10\-11

> *Providing validation, strength, and stability to people who feel gaslit and dismissed and forgotten can help them feel stronger and surer in their decisions. These pieces made me understand that journalism can be a caretaking profession, even if it is never really thought about in those terms. It is often framed in terms of antagonism. Speaking truth to power turns into being hard\-nosed and removed from our subject matter, which so easily turns into be an asshole and do whatever you like.   
>   
> This is a viewpoint that I reject. My pillars are empathy, curiosity, and kindness. And much else flows from that. For people who feel lost and alone, we get to say through our work, you are not. For people who feel like society has abandoned them and their lives do not matter, we get to say, actually, they fucking do. We are one of the only professions that can do that through our work and that can do that at scale.*

[Ed Yong](https://xoxofest.com/2024/videos/ed-yong/)

---

**Link** 2024\-10\-11 [HTML for People](https://htmlforpeople.com/):

Blake Watson's brand new HTML tutorial, presented as a free online book (CC BY\-NC\-SA 4\.0, [on GitHub](https://github.com/blakewatson/htmlforpeople)). This seems very modern and well thought\-out to me. It focuses exclusively on HTML, skipping JavaScript entirely and teaching with [Simple.css](https://simplecss.org/) to avoid needing to dig into CSS while still producing sites that are pleasing to look at. It even touches on Web Components (described as [Custom HTML tags](https://htmlforpeople.com/adding-a-fun-page/#custom-html-tags)) towards the end.

---

**Quote** 2024\-10\-11

> *The primary use of “misinformation” is not to change the beliefs of other people at all. Instead, the vast majority of misinformation is offered as a service for people to maintain their beliefs in face of overwhelming evidence to the contrary.*

[Mike Caulfield](https://mikecaulfield.substack.com/p/copium-addicts-what-misinformation)

---

**Link** 2024\-10\-11 [$2 H100s: How the GPU Bubble Burst](https://www.latent.space/p/gpu-bubble):

Fascinating analysis from Eugene Cheah, founder of LLM hosting provider [Featherless](https://featherless.ai/), discussing GPU economics over the past 12 months.

> TLDR: Don’t buy H100s. The market has flipped from shortage ($8/hr) to oversupplied ($2/hr), because of reserved compute resales, open model finetuning, and decline in new foundation model co’s. Rent instead.

---

**Link** 2024\-10\-11 [lm.rs: run inference on Language Models locally on the CPU with Rust](https://github.com/samuel-vitorino/lm.rs):

Impressive new LLM inference implementation in Rust by Samuel Vitorino. I tried it just now on an M2 Mac with 64GB of RAM and got very snappy performance for [this Q8 Llama 3\.2 1B](https://huggingface.co/samuel-vitorino/Llama-3.2-1B-Instruct-Q8_0-LMRS), with Activity Monitor reporting 980% CPU usage over 13 threads.

Here's how I compiled the library and ran the model:

```
cd /tmp
git clone https://github.com/samuel-vitorino/lm.rs
cd lm.rs
RUSTFLAGS="-C target-cpu=native" cargo build --release --bin chat
curl -LO 'https://huggingface.co/samuel-vitorino/Llama-3.2-1B-Instruct-Q8_0-LMRS/resolve/main/tokenizer.bin?download=true'
curl -LO 'https://huggingface.co/samuel-vitorino/Llama-3.2-1B-Instruct-Q8_0-LMRS/resolve/main/llama3.2-1b-it-q80.lmrs?download=true'
./target/release/chat --model llama3.2-1b-it-q80.lmrs --show-metrics

```

That `--show-metrics` option added this at the end of a response:

```
Speed: 26.41 tok/s

```

It looks like the performance is helped by two key dependencies: [wide](https://crates.io/crates/wide), which provides data types optimized for SIMD operations and [rayon](https://crates.io/crates/rayon) for running parallel iterators across multiple cores (used [for matrix multiplication](https://github.com/samuel-vitorino/lm.rs/blob/4a27af0ea07e284cf2a9c7cd1c984e484f143804/src/functional.rs#L136-L153)).

(I used LLM and `files-to-prompt` to [help figure this out](https://gist.github.com/simonw/19ce7d66bcd9a9efc46e25354a2f5b3c).)

---

**Link** 2024\-10\-12 [Cabel Sasser at XOXO](https://xoxofest.com/2024/videos/cabel-sasser/):

I cannot recommend this talk highly enough for the way it ends. After watching the video dive into [this new site](https://wescook.art/) that accompanies the talk \- an online archive of the works of commercial artist Wes Cook. I too would very much love to see a full scan of [The Lost McDonalds Satire Triptych](https://wescook.art/2024/10/10/the-lost-mcdonalds-satire-triptych/).

---

**Quote** 2024\-10\-12

> *Frankenstein is a terrific book partly based on how concerned people were about electricity. It captures our fears about the nature of being human but didn’t help anyone really come up with better policies for dealing with electricity. I worry that a lot of AI critics are doing the same thing.*

[James Cham](https://twitter.com/jamescham/status/1844966797428261341)

---

**Quote** 2024\-10\-12

> *Carl Hewitt recently remarked that the question what is an agent? is embarrassing for the agent\-based computing community in just the same way that the question what is intelligence? is embarrassing for the mainstream AI community. The problem is that although the term is widely used, by many people working in closely related areas, it defies attempts to produce a single universally accepted definition. This need not necessarily be a problem: after all, if many people are successfully developing interesting and useful applications, then it hardly matters that they do not agree on potentially trivial terminological details. However, there is also the danger that unless the issue is discussed, 'agent' might become a 'noise' term, subject to both abuse and misuse, to the potential confusion of the research community.*

[Michael Wooldridge](https://www.cs.ox.ac.uk/people/michael.wooldridge/pubs/ker95/subsection3_1_1.html)

---

**Link** 2024\-10\-12 [Python 3\.13's best new features](https://www.pythonmorsels.com/python-313-whats-new/):

Trey Hunner highlights some Python 3\.13 usability improvements I had missed, mainly around the new REPL.

Pasting a block of code like a class or function that includes blank lines no longer breaks in the REPL \- particularly useful if you frequently have LLMs write code for you to try out.

Hitting F2 in the REPL toggles "history mode" which gives you your Python code without the REPL's `>>>` and `...` prefixes \- great for copying code back out again.

Creating a virtual environment with `python3.13 -m venv .venv` now adds a `.venv/.gitignore` file containing `*` so you don't need to explicitly ignore that directory. I just checked and it looks like `uv venv` [implements the same trick](https://github.com/astral-sh/uv/blob/d12d569f24150d3e78dce87a9abf2313b9edac06/crates/uv-virtualenv/src/virtualenv.rs#L145-L146).

And my favourite:

> Historically, any line in the Python debugger prompt that started with a PDB command would usually trigger the PDB command, **instead of PDB interpreting the line as Python code.** \[...]
> 
> But now, **if the command looks like Python code,** `pdb` **will run it as Python code!**

Which means I can finally call `list(iterable)` in my `pdb` seesions, where previously I've had to use `[i for i in iterable]` instead.

(Tip [from Trey](https://twitter.com/treyhunner/status/1845152386433810521): `!list(iterable)` and `[*iterable]` are good alternatives for pre\-Python 3\.13\.)

Trey's post is also available [as a YouTube video](https://www.youtube.com/watch?v=OBUMQR_YIgs).

---

**Link** 2024\-10\-12 [Perks of Being a Python Core Developer](https://mariatta.ca/posts/perks-of-python-core/):

Mariatta Wijaya provides a detailed breakdown of the exact capabilities and privileges that are granted to Python core developers \- including commit access to the Python `main`, the ability to write or sponsor PEPs, the ability to vote on new core developers and for the steering council election and financial support from the PSF for travel expenses related to PyCon and core development sprints.

Not to be under\-estimated is that you also gain respect:

> Everyone’s always looking for ways to stand out in resumes, right? So do I. I’ve been an engineer for longer than I’ve been a core developer, and I do notice that having the extra title like open source maintainer and public speaker really make a difference. As a woman, as someone with foreign last name that nobody knows how to pronounce, as someone who looks foreign, and speaks in a foreign accent, having these extra “credentials” helped me be seen as more or less equal compared to other people.

---

**Link** 2024\-10\-12 [jefftriplett/django\-startproject](https://github.com/jefftriplett/django-startproject):

Django's `django-admin startproject` and `startapp` commands include [a \-\-template option](https://docs.djangoproject.com/en/5.1/ref/django-admin/#cmdoption-startapp-template) which can be used to specify an alternative template for generating the initial code.

Jeff Triplett actively maintains his own template for new projects, which includes the pattern that I personally prefer of keeping settings and URLs in a [config/ folder](https://github.com/jefftriplett/django-startproject/tree/main/config). It also configures the development environment to run using Docker Compose.

The latest update adds support for Python 3\.13, Django 5\.1 and uv. It's neat how you can get started without even installing Django using `uv run` like this:

```
uv run --with=django django-admin startproject \
  --extension=ini,py,toml,yaml,yml \
  --template=https://github.com/jefftriplett/django-startproject/archive/main.zip \
  example_project

```

---

**Link** 2024\-10\-13 [PostgreSQL 17: SQL/JSON is here!](https://www.depesz.com/2024/10/11/sql-json-is-here-kinda-waiting-for-pg-17/):

Hubert Lubaczewski dives into the new JSON features added in PostgreSQL 17, released a few weeks ago on the [26th of September](https://www.postgresql.org/about/news/postgresql-17-released-2936/). This is the latest in his [long series](https://www.depesz.com/tag/waiting/) of similar posts about new PostgreSQL features.

The features are based on the new [SQL:2023](https://en.wikipedia.org/wiki/SQL:2023) standard from June 2023\. If you want to actually *read* the specification for SQL:2023 it looks like you have to [buy a PDF from ISO](https://www.iso.org/standard/76583.html) for 194 Swiss Francs (currently $226\). Here's a handy summary by Peter Eisentraut: [SQL:2023 is finished: Here is what's new](http://peter.eisentraut.org/blog/2023/04/04/sql-2023-is-finished-here-is-whats-new).

There's a lot of neat stuff in here. I'm particularly interested in the `json_table()` table\-valued function, which can convert a JSON string into a table with quite a lot of flexibility. You can even specify a full table schema as part of the function call:

```
SELECT  FROM json_table(
    '[{"a":10,"b":20},{"a":30,"b":40}]'::jsonb,
    '$[]'
    COLUMNS (
        id FOR ORDINALITY,
        column_a int4 path '$.a',
        column_b int4 path '$.b',
        a int4,
        b int4,
        c text
    )
);
```

SQLite has [solid JSON support already](https://www.sqlite.org/json1.html) and often imitates PostgreSQL features, so I wonder if we'll see an update to SQLite that reflects some aspects of this new syntax.

---

**Link** 2024\-10\-13 [An LLM TDD loop](https://codeinthehole.com/tips/llm-tdd-loop-script/):

Super neat demo by David Winterbottom, who wrapped my [LLM](https://llm.datasette.io/) and [files\-to\-prompt](https://github.com/simonw/files-to-prompt) tools in [a short Bash script](https://gist.github.com/codeinthehole/d12af317a76b43423b111fd6d508c4fc) that can be fed a file full of Python unit tests and an empty implementation file and will then iterate on that file in a loop until the tests pass.

---

**Link** 2024\-10\-13 [Zero\-latency SQLite storage in every Durable Object](https://blog.cloudflare.com/sqlite-in-durable-objects/):

Kenton Varda introduces the next iteration of Cloudflare's [Durable Object](https://developers.cloudflare.com/durable-objects/) platform, which recently upgraded from a key/value store to a full relational system based on SQLite.

For useful background on the first version of Durable Objects take a look at [Cloudflare's durable multiplayer moat](https://digest.browsertech.com/archive/browsertech-digest-cloudflares-durable/) by Paul Butler, who digs into its popularity for building WebSocket\-based realtime collaborative applications.

The new SQLite\-backed Durable Objects is a fascinating piece of distributed system design, which advocates for a really interesting way to architect a large scale application.

The key idea behind Durable Objects is to colocate application logic with the data it operates on. A Durable Object comprises code that executes on the same physical host as the SQLite database that it uses, resulting in blazingly fast read and write performance.

How could this work at scale?

> A single object is inherently limited in throughput since it runs on a single thread of a single machine. To handle more traffic, you create more objects. This is easiest when different objects can handle different logical units of state (like different documents, different users, or different "shards" of a database), where each unit of state has low enough traffic to be handled by a single object

Kenton presents the example of a flight booking system, where each flight can map to a dedicated Durable Object with its own SQLite database \- thousands of fresh databases per airline per day.

Each DO has a unique name, and Cloudflare's network then handles routing requests to that object wherever it might live on their global network.

The technical details are fascinating. Inspired by [Litestream](https://litestream.io/), each DO constantly streams a sequence of WAL entries to object storage \- batched every 16MB or every ten seconds. This also enables point\-in\-time recovery for up to 30 days through replaying those logged transactions.

To ensure durability within that ten second window, writes are also forwarded to five replicas in separate nearby data centers as soon as they commit, and the write is only acknowledged once three of them have confirmed it.

The JavaScript API design is interesting too: it's blocking rather than async, because the whole point of the design is to provide fast single threaded persistence operations:

```
let docs = sql.exec(</span>
<span class="pl-s">  SELECT title, authorId FROM documents</span>
<span class="pl-s">  ORDER BY lastModified DESC</span>
<span class="pl-s">  LIMIT 100</span>
<span class="pl-s">).toArray();

for (let doc of docs) {
  doc.authorName = sql.exec(
    "SELECT name FROM users WHERE id = ?",
    doc.authorId).one().name;
}
```

This one of their examples deliberately exhibits the N\+1 query pattern, because that's something SQLite is [uniquely well suited to handling](https://www.sqlite.org/np1queryprob.html).

The system underlying Durable Objects is called Storage Relay Service, and it's been powering Cloudflare's existing\-but\-different [D1 SQLite system](https://developers.cloudflare.com/d1/) for over a year.

I was curious as to where the objects are created. [According to this](https://developers.cloudflare.com/durable-objects/reference/data-location/#provide-a-location-hint) (via [Hacker News](https://news.ycombinator.com/item?id=41832547#41832812)):

> Durable Objects do not currently change locations after they are created. By default, a Durable Object is instantiated in a data center close to where the initial `get()` request is made. \[...] To manually create Durable Objects in another location, provide an optional `locationHint` parameter to `get()`.

And in a footnote:

> Dynamic relocation of existing Durable Objects is planned for the future.

[where.durableobjects.live](https://where.durableobjects.live/) is a neat site that tracks where in the Cloudflare network DOs are created \- I just visited it and it said:

> This page tracks where new Durable Objects are created; for example, when you loaded this page from **Half Moon Bay**, a worker in **San Jose, California, United States (SJC)** created a durable object in **San Jose, California, United States (SJC)**.

[![Where Durable Objects Live.    Created by the wonderful Jed Schmidt, and now maintained with ❤️ by Alastair. Source code available on Github.    Cloudflare Durable Objects are a novel approach to stateful compute based on Cloudflare Workers. They aim to locate both compute and state closest to end users.    This page tracks where new Durable Objects are created; for example, when you loaded this page from Half Moon Bay, a worker in San Jose, California, United States (SJC) created a durable object in Los Angeles, California, United States (LAX).    Currently, Durable Objects are available in 11.35% of Cloudflare PoPs.    To keep data fresh, this application is constantly creating/destroying new Durable Objects around the world. In the last hour, 394,046 Durable Objects have been created(and subsequently destroyed), FOR SCIENCE!    And a map of the world showing lots of dots.](https://substackcdn.com/image/fetch/$s_!zG_g!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F02a2c420-9a1e-49db-ad78-17e3a4385219_1182x638.jpeg "Where Durable Objects Live.    Created by the wonderful Jed Schmidt, and now maintained with ❤️ by Alastair. Source code available on Github.    Cloudflare Durable Objects are a novel approach to stateful compute based on Cloudflare Workers. They aim to locate both compute and state closest to end users.    This page tracks where new Durable Objects are created; for example, when you loaded this page from Half Moon Bay, a worker in San Jose, California, United States (SJC) created a durable object in Los Angeles, California, United States (LAX).    Currently, Durable Objects are available in 11.35% of Cloudflare PoPs.    To keep data fresh, this application is constantly creating/destroying new Durable Objects around the world. In the last hour, 394,046 Durable Objects have been created(and subsequently destroyed), FOR SCIENCE!    And a map of the world showing lots of dots.")](https://substackcdn.com/image/fetch/$s_!zG_g!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F02a2c420-9a1e-49db-ad78-17e3a4385219_1182x638.jpeg)

---