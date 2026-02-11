# Open challenges for AI engineering

*Plus a flurry of tiny tools built using Claude 3.5 Sonnet*

Published: 2024-07-08
Source: https://simonw.substack.com/p/open-challenges-for-ai-engineering

---

In this newsletter:

* Open challenges for AI engineering
* Weeknotes: a livestream, a surprise keynote and progress on Datasette Cloud billing

Plus 29 links and 11 quotations and 1 TIL

### [Open challenges for AI engineering](https://simonwillison.net/2024/Jun/27/ai-worlds-fair/) \- 2024\-06\-27

I gave the opening keynote at the [AI Engineer World's Fair](https://www.ai.engineer/worldsfair) a few weeks ago. I was a late addition to the schedule: OpenAI pulled out of their slot at the last minute, and I was invited to put together a 20 minute talk with just under 24 hours notice!

I decided to focus on highlights of the LLM space since the previous AI Engineer Summit 8 months ago, and to discuss some open challenges for the space \- a response to my [Open questions for AI engineering](https://simonwillison.net/2023/Oct/17/open-questions/) talk at that earlier event.

A *lot* has happened in the last 8 months. Most notably, GPT\-4 is no longer the undisputed champion of the space \- a position it held for the best part of a year.

You can [watch the talk on YouTube](https://www.youtube.com/watch?v=5zE2sMka620&t=2026s), or read the full annotated and extended version below.

Sections of this talk:

* [Breaking the GPT\-4 barrier](https://simonwillison.net/2024/Jun/27/ai-worlds-fair/#slide.001.jpeg)

	+ [The new landscape of models](https://simonwillison.net/2024/Jun/27/ai-worlds-fair/#slide.006.jpeg)
	+ [Evaluating their vibes](https://simonwillison.net/2024/Jun/27/ai-worlds-fair/#slide.013.jpeg)
* [GPT\-4 class models are free to consumers now](https://simonwillison.net/2024/Jun/27/ai-worlds-fair/#slide.023.jpeg)

	+ [But they're still really hard to use](https://simonwillison.net/2024/Jun/27/ai-worlds-fair/#slide.026.jpeg)
* [The AI trust crisis](https://simonwillison.net/2024/Jun/27/ai-worlds-fair/#slide.032.jpeg)
* [We still haven't solved prompt injection](https://simonwillison.net/2024/Jun/27/ai-worlds-fair/#slide.040.jpeg)

	+ [The Markdown image exfiltration bug](https://simonwillison.net/2024/Jun/27/ai-worlds-fair/#slide.041.jpeg)
	+ [Accidental prompt injection](https://simonwillison.net/2024/Jun/27/ai-worlds-fair/#slide.045.jpeg)
* [Slop](https://simonwillison.net/2024/Jun/27/ai-worlds-fair/#slide.048.jpeg)

	+ [Taking accountability for what you publish with AI](https://simonwillison.net/2024/Jun/27/ai-worlds-fair/#slide.052.jpeg)
* [Our responsibilities as AI engineers](https://simonwillison.net/2024/Jun/27/ai-worlds-fair/#slide.053.jpeg)

---

### [Weeknotes: a livestream, a surprise keynote and progress on Datasette Cloud billing](https://simonwillison.net/2024/Jul/2/weeknotes/) \- 2024\-07\-02

My first YouTube livestream with Val Town, a keynote at the AI Engineer World's Fair and some work integrating Stripe with Datasette Cloud. Plus a bunch of upgrades to my blog.

#### Livestreaming RAG with Steve Krouse and Val Town

[![Screnshot of a What is Datasette? page created by Claude 3.5 Sonnet - it includes a Key Features section with four different cards arranged in a grid, for Explore Data, Publish Data, API Access and Extensible.](https://substackcdn.com/image/fetch/$s_!5Uf4!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feb2e0d4f-9dd8-450b-acfd-41f4b46b267e_1280x720.jpeg "Screnshot of a What is Datasette? page created by Claude 3.5 Sonnet - it includes a Key Features section with four different cards arranged in a grid, for Explore Data, Publish Data, API Access and Extensible.")](https://substackcdn.com/image/fetch/$s_!5Uf4!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feb2e0d4f-9dd8-450b-acfd-41f4b46b267e_1280x720.jpeg)

A couple of weeks ago I broadcast a livestream with Val Town founder Steve Krouse, which I then [turned into an annotated video write\-up](https://simonwillison.net/2024/Jun/21/search-based-rag/).

Outside of a few minutes in the occasional workshop I haven't ever participated in an extended live coding session before. Steve has been running [a series of them](https://www.youtube.com/@ValDotTown/videos) where he live codes with different guests, and I was excited to be invited to join him.

I really enjoyed it, and I think the end\-result was very worthwhile. We built an implementation of RAG against my blog, demonstrating the RAG technique where you extract keywords from the user's question, search for them using a BM25 full\-text search index (in this case SQLite FTS) and construct an answer using the search results.

The more time I spend with this RAG pattern the more I like it. It's considerably easier to reason about than RAG using vector search based on [embeddings](https://simonwillison.net/2023/Oct/23/embeddings/), and can provide high quality results with a relatively simple implementation.

It's often much easier to bake FTS on to an existing site than embedding search, since it avoids the need to run embedding models against thousands of documents and then create a vector search index to run the queries against.

We also got to try out the launched\-that\-day Claude 3\.5 Sonnet, which has quickly become my absolute favourite LLM.

Full details (and video) in my write\-up: [Building search\-based RAG using Claude, Datasette and Val Town](https://simonwillison.net/2024/Jun/21/search-based-rag/).

#### A surprise keynote

[![Open challenges for AI engineering Simon Willison - simonwillison.net AI Engineer World's Fair, June 26th 2024](https://substackcdn.com/image/fetch/$s_!ArZV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F78ee63ae-87da-4ba3-b200-faa7e3fb6af1_1920x1080.jpeg "Open challenges for AI engineering Simon Willison - simonwillison.net AI Engineer World's Fair, June 26th 2024")](https://substackcdn.com/image/fetch/$s_!ArZV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F78ee63ae-87da-4ba3-b200-faa7e3fb6af1_1920x1080.jpeg)

At lunchtime on Wednesday last week I was asked if I could give the opening keynote at the [AI Engineer World's Fair](https://www.ai.engineer/worldsfair)... on Thursday morning! Their keynote speaker from OpenAI had to cancel at the last minute and they needed someone who could put together a talk on *very* short notice.

I gave the closing keynote at their previous event last October \- [Open questions for AI engineering](https://simonwillison.net/2023/Oct/17/open-questions/) \- so the natural theme for this talk was to review advances in the field in the past 8 month and use those to pose a new set of open challenges for engineers in the room.

I continue to go by the rule of thumb that you need ten hours preparation for every hour on stage... and this was only a twenty minute slot, so I had just about enough time to pull it together!

You can watch the result (and read the accompanying notes) at [Open challenges for AI engineering](https://simonwillison.net/2024/Jun/27/ai-worlds-fair/). I'm really happy with it \- I got great feedback from attendees during the event and I think I managed to capture the most interesting developments in the field as well as challenging the audience to consider their responsibilities in helping shape what we build next.

#### Stripe integration for Datasette Cloud

Datasette Cloud has been in preview mode for *a while* at this point. I'm ready to start billing people, and I've set a target of the end of July to get that in place.

I'm using [Stripe](https://stripe.com/) for billing, and attempting to outsource as much of the UI complexity of managing subscriptions to their [customer portal](https://docs.stripe.com/customer-management) product as possible.

This has already resulted in one TIL: [Mocking Stripe signature checks in a pytest fixture](https://til.simonwillison.net/pytest/pytest-stripe-signature) \- and I imagine there will be several more before I have everything working smoothly.

#### JSON API improvements for Datasette 1\.0

Alex and I have been using Datasette Cloud to help drive progress towards the Datasette 1\.0 release. Datasette Cloud needs a stable JSON API, so we've been working on finalizing the JSON API that will be included in Datasette 1\.0\.

We worked together on a final design for this which Alex documented in [\#2360: Datasette JSON API changes for 1\.0](https://github.com/simonw/datasette/issues/2360). He's working on the implementation now, which we hope to land and then ship as an alpha as soon as it's ready for people to try out.

#### Claude 3\.5 Sonnet

I mentioned this above, but it's worth emphasizing quite how much value I've been getting out of Claude 3\.5 Sonnet since [it's release](https://simonwillison.net/2024/Jun/20/claude-35-sonnet/) on the 20th of June. It is *so good* at writing code! I've also been thoroughly enjoying the new artifacts feature where it can write and then display HTML/CSS/JavaScript \- I've used that for several prototyping projects as well as [quite a sophisticated animated visualization](https://simonwillison.net/2024/Jun/27/ai-worlds-fair/#slide.020.jpeg) I used in my keynote last week.

[llm\-claude\-3 0\.4](https://github.com/simonw/llm-claude-3/releases/tag/0.4) has support for the new model, and I really need to upgrade some of my LLM\-powered Datasette plugins to take advantage of it too.

#### Upgrades to my blog

Last weeknotes I talked about [redesigning my homepage](https://simonwillison.net/2024/Jun/19/datasette-studio/#more-blog-improvements) and adding entry images and tag descriptions.

I've since made a bunch of smaller incremental improvements around here:

* I added [support for Markdown in quotations](https://github.com/simonw/simonwillisonblog/issues/451), for example the italics in [this quotation of Terry Pratchett](https://simonwillison.net/2024/Jul/1/terry-pratchett/).
* Tags are now displayed on the homepage (and other pages) [for bookmarks and quotations](https://github.com/simonw/simonwillisonblog/issues/455), in addition to entries. This makes my tagging system a lot more prominent, so I've added descriptions to [a bunch more tags](https://simonwillison.net/dashboard/tags-with-descriptions/).
* I created [2003\.simonwillison.net](https://2003.simonwillison.net/) ([\#452](https://github.com/simonw/simonwillisonblog/issues/452)), a special templated version of my homepage designed to imitate my site's design in 2003 (CSS rescued [from the Internet Archive](https://web.archive.org/web/20030723185129if_/http://simon.incutio.com/)). I have my reasons.
* [I redesigned the tag clouds on my year archive pages](https://github.com/simonw/simonwillisonblog/issues/445) \- e.g. on [2024](https://simonwillison.net/2024/). I actually used Claude 3\.5 Sonnet for this \- I gave it a screenshot of the tags and [asked it to come up with a more tasteful palette of colours](https://gist.github.com/simonw/22b3a6aaa30ff96941ed4c1617c1bfd7).

Here's that new, slightly more tasteful tag cloud:

[![A tag cloud in muted colours, the largest tags are ai llms generativeai projects python openai ethics security llm claude](https://substackcdn.com/image/fetch/$s_!vrGl!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd1030c4-2cbb-42e0-83e3-eaeac0db7b0d_1206x630.jpeg "A tag cloud in muted colours, the largest tags are ai llms generativeai projects python openai ethics security llm claude")](https://substackcdn.com/image/fetch/$s_!vrGl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd1030c4-2cbb-42e0-83e3-eaeac0db7b0d_1206x630.jpeg)

#### Releases

* **[datasette 0\.64\.8](https://github.com/simonw/datasette/releases/tag/0.64.8)** \- 2024\-06\-21  
An open source multi\-tool for exploring and publishing data
* **[llm\-claude\-3 0\.4](https://github.com/simonw/llm-claude-3/releases/tag/0.4)** \- 2024\-06\-20  
LLM plugin for interacting with the Claude 3 family of models

#### TILs

* [Mocking Stripe signature checks in a pytest fixture](https://til.simonwillison.net/pytest/pytest-stripe-signature) \- 2024\-07\-02
* [Running Prettier against Django or Jinja templates](https://til.simonwillison.net/npm/prettier-django) \- 2024\-06\-20

---

**Link** 2024\-06\-24 [Microfeatures I Love in Blogs and Personal Websites](https://danilafe.com/blog/blog_microfeatures/):

This post by Daniel Fedorin (and the accompanying [Hacker News thread](https://news.ycombinator.com/item?id=40774277)) is a nice reminder of one of the most fun things about building your own personal website: it gives you a low\-risk place to experiment with details like footnotes, tables of contents, linkable headings, code blocks, RSS feeds, link previews and more.

---

**Link** 2024\-06\-24 [New blog feature: Support for markdown in quotations](https://github.com/simonw/simonwillisonblog/issues/451):

Another incremental improvement to my blog. I've been collecting quotations here since 2006 \- I now render them using Markdown (previously they were just plain text). [Here's one example](https://simonwillison.net/2024/Jun/17/russ-cox/). The full set of 920 (and counting) quotations can be explored [using this search filter](https://simonwillison.net/search/?type=quotation).

---

**Quote** 2024\-06\-24

> *[What Apple unveiled](https://www.apple.com/newsroom/2024/06/introducing-apple-intelligence-for-iphone-ipad-and-mac/) last week with [Apple Intelligence](https://www.apple.com/apple-intelligence/) wasn't so much new products, but new features—a slew of them—for existing products, powered by generative AI.   
>   
> \[...] These aren't new apps or new products. They're the most used, most important apps Apple makes, the core apps that define the Apple platforms ecosystem, and Apple is using generative AI to make them better and more useful—without, in any way, rendering them unfamiliar.*

[John Gruber](https://daringfireball.net/2024/06/wwdc24_apple_intelligence)

---

**Link** 2024\-06\-24 [Listen to the AI\-generated ripoff songs that got Udio and Suno sued](https://www.404media.co/listen-to-the-ai-generated-ripoff-songs-that-got-udio-and-suno-sued/):

Jason Koebler reports on the lawsuit filed today [by the RIAA against Udio and Suno](https://www.theverge.com/2024/6/24/24184710/riaa-ai-lawsuit-suno-udio-copyright-umg-sony-warner), the two leading generative music startups.

The lawsuit includes examples of prompts that the record labels used to recreate famous songs that were almost certainly included in the (undisclosed) training data. Jason collected some of these together into a three minute video, and the result in pretty damning. Arguing "fair use" isn't going to be easy here.

---

**Link** 2024\-06\-25 [Claude Projects](https://support.anthropic.com/en/articles/9517075-what-are-projects):

New Claude feature, quietly launched this morning for Claude Pro users. Looks like their version of OpenAI's GPTs, designed to take advantage of Claude's 200,000 token context limit:

> You can upload relevant documents, text, code, or other files to a project’s knowledge base, which Claude will use to better understand the context and background for your individual chats within that project. Each project includes a 200K context window, the equivalent of a 500\-page book, so users can add all of the insights needed to enhance Claude’s effectiveness.

You can also set custom instructions, which presumably get added to the system prompt.

I tried dropping in all of [Datasette's existing documentation](https://github.com/simonw/datasette/tree/1.0a13/docs) \- 693KB of `.rst` files (which I had to rename to `.rst.txt` for it to let me upload them) \- and it worked and showed "63% of knowledge size used".

This is a slightly different approach from OpenAI, where the [GPT knowledge feature](https://help.openai.com/en/articles/8843948-knowledge-in-gpts) supports attaching up to 20 files each with up to 2 million tokens, which get ingested into a vector database ([likely Qdrant](https://twitter.com/altryne/status/1721989500291989585)) and used for RAG.

It looks like Claude instead handle a smaller amount of extra knowledge but paste the whole thing into the context window, which avoids some of the weirdness around semantic search chunking but greatly limits the size of the data.

My big frustration with the knowledge feature in GPTs remains the lack of documentation on what it's actually doing under the hood. Without that it's difficult to make informed decisions about how to use it \- with Claude Projects I can at least develop a robust understanding of what the tool is doing for me and how best to put it to work.

No equivalent (yet) for the [GPT actions feature](https://platform.openai.com/docs/actions/introduction) where you can grant GPTs the ability to make API calls out to external systems.

---

**Link** 2024\-06\-25 [Polyfill supply chain attack hits 100K\+ sites](https://sansec.io/research/polyfill-supply-chain-attack):

Short version: if you are loading assets from the `polyfill.io` domain you need to remove that right now: the new owners of the domain (as of a few months ago) appear to be using it to serve malicious JavaScript.

`polyfill.io` was a fascinating service. It was originally developed and supported by the Financial Times, but span off as a separate project several years ago.

The key idea was to serve up a set of JavaScript polyfills \- pieces of code that implemented missing web platform features for older browsers \- dynamically, based on the incoming user\-agent. This required a CDN that varied its output dynamically based on the user\-agent, hence the popularity of the single hosted service.

Andrew Betts, the original author of the service, has been warning people to move off it [since February 2024](https://twitter.com/triblondon/status/1761852117579427975):

> If your website uses `polyfill.io`, remove it IMMEDIATELY.
> 
> I created the polyfill service project but I have never owned the domain name and I have had no influence over its sale.

He now works for Fastly, which started offering [a free polyfill\-fastly.io alternative](https://community.fastly.com/t/new-options-for-polyfill-io-users/2540) in February. Andrew says you probably don't need that either, given that modern browsers have much better compatibility than when the service was first introduced over a decade ago.

There's some interesting additional context in a now\-deleted GitHub issue, [preserved here by the Internet Archive](https://web.archive.org/web/20240314202054/https://github.com/polyfillpolyfill/polyfill-service/issues/2834).

Usually one answer to protecting against this style of CDN supply chain attack would be to use [SRI hashes](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity) to ensure only the expected script can be served from the site. That doesn't work here because the whole point of the service is to serve different scripts to different browsers.

---

**Link** 2024\-06\-26 [picopilot](https://github.com/coder/picopilot):

Kyle Carberry's "GitHub Copilot in 70 lines of JavaScript". The title is a little hyperbolic, but the code itself really does implement an OpenAI powered Visual Studio Code text completion extension in [71 lines of code](https://github.com/coder/picopilot/blob/f71c6ab4738d4159d18aa772b22f4b1d24c89899/extension.js). This is an excellent example for learning what a minimal VS Code extension looks like.

Here's the system prompt it uses:

`You provide code completion results given a prefix and suffix. Respond with a JSON object with the key 'completion' containing a suggestion to place between the prefix and suffix. Follow existing code styles. Listen to comments at the end of the prefix. The language is "{language}".`

Then it passes the prefix and suffix as two user messages, and uses the `"response_format": {"type": "json_object"}` option to enforce JSON output from the GPT\-4o API.

The feature this is missing is the thing that makes GitHub Copilot so impressive: Copilot does [a whole bunch of clever tricks](https://thakkarparth007.github.io/copilot-explorer/posts/copilot-internals.html#how-is-the-prompt-prepared-a-code-walkthrough) to find snippets of relevant code from the current and other nearby files and includes them with the prompt, resulting in much higher quality completions.

---

**Link** 2024\-06\-27 [Python 3\.12 change results in Apple App Store rejection](https://github.com/python/cpython/issues/120522):

Such a frustrating demonstration of the very worst of Apple's opaque App Store review process. The Python 3\.12 standard library `urllib` package includes the string `itms-services`, and after much investigation Eric Froemling managed to determine that Apple use a scanner and reject any app that has that string mentioned anywhere within their bundle.

Russell Keith\-Magee has [a thread](https://discuss.python.org/t/handling-incompatibilities-with-app-store-review-processes/56011) on the Python forum discussing solutions. He doesn't think attempts to collaborate with Apple are likely to help:

> That definitely sounds appealing as an approach \- but in this case, it’s going to be screaming into the void. There’s barely even an appeals process for app rejection on Apple’s App Store. We definitely don’t have any sort of channel to raise a complaint that we could reasonably believe would result in a change of policy.

---

**Link** 2024\-06\-28 [Django: Test for pending migrations](https://adamj.eu/tech/2024/06/23/django-test-pending-migrations/):

Neat recipe from Adam Johnson for adding an automated test to your Django test suite that runs `manage.py makemigrations --check` to ensure you don't accidentally land code that deploys with a missing migration and crashes your site. I've made this mistake before myself so I'll be adding this to my projects.

---

**Link** 2024\-06\-28 [Serving a billion web requests with boring code](https://notes.billmill.org/blog/2024/06/Serving_a_billion_web_requests_with_boring_code.html):

Bill Mill provides a deep retrospective from his work helping build a relaunch of the [medicare.gov/plan\-compare](https://www.medicare.gov/plan-compare/) site.

It's a fascinating case study of the [choose boring technology](https://boringtechnology.club/) mantra put into action. The "boring" choices here were PostgreSQL, Go and React, all three of which are so widely used and understood at this point that you're very unlikely to stumble into surprises with them.

Key goals for the site were accessibility, in terms of users, devices and performance. Despite best efforts:

> The result fell prey after a few years to a common failure mode of react apps, and became quite heavy and loaded somewhat slowly.

I've seen this pattern myself many times over, and I'd love to understand why. React itself isn't a particularly large dependency but somehow it always seems to lead to architectural bloat over time. Maybe that's more of an SPA thing than something that's specific to React.

Loads of other interesting details in here. The ETL details \- where brand new read\-only RDS databases were spun up every morning after a four hour build process \- are particularly notable.

---

**Link** 2024\-06\-28 [Accidental GPT\-4o voice preview](https://www.reddit.com/r/ChatGPT/comments/1dp1grs/comment/lakpmjb/):

Reddit user RozziTheCreator was one of a small group who were accidentally granted access to the new multimodal GPT\-4o audio voice feature. They captured this video of it telling them a spooky story, complete with thunder sound effects added to the background and in a very realistic voice that clearly wasn't the one from the 4o demo that sounded similar to Scarlet Johansson.

OpenAI provided a comment for [this Tom's Guide story](https://www.tomsguide.com/ai/chatgpt/openai-accidentally-gave-some-users-advanced-voice-early-heres-what-happened) confirming the accidental rollout so I don't think this is a faked video.

---

**Quote** 2024\-06\-29

> *We argued that ChatGPT is not designed to produce true utterances; rather, it is designed to produce text which is indistinguishable from the text produced by humans. It is aimed at being convincing rather than accurate. The basic architecture of these models reveals this: they are designed to come up with a likely continuation of a string of text. It’s reasonable to assume that one way of being a likely continuation of a text is by being true; if humans are roughly more accurate than chance, true sentences will be more likely than false ones. This might make the chatbot more accurate than chance, but it does not give the chatbot any intention to convey truths. This is similar to standard cases of human bullshitters, who don’t care whether their utterances are true; good bullshit often contains some degree of truth, that’s part of what makes it convincing.*

[ChatGPT is bullshit](https://link.springer.com/article/10.1007/s10676-024-09775-5)

---

**Quote** 2024\-06\-29

> *Absolutely any time I try to explore something even slightly against commonly accepted beliefs, LLMs always just rehash the commonly accepted beliefs.   
>   
> As a researcher, I find this behaviour worse than unhelpful. It gives the mistaken impression that there's nothing to explore.*

[Jeremy Howard](https://twitter.com/jeremyphoward/status/1807162709664047144)

---

**Link** 2024\-06\-29 [marimo.app](https://marimo.app/):

The Marimo reactive notebook ([previously](https://simonwillison.net/2024/Jan/12/marimo/)) \- a Python notebook that's effectively a cross between Jupyter and Observable \- now also has a version that runs entirely in your browser using WebAssembly and Pyodide. Here's [the documentation](https://docs.marimo.io/guides/wasm.html).

---

**Link** 2024\-06\-30 [The Super Effectiveness of Pokémon Embeddings Using Only Raw JSON and Images](https://minimaxir.com/2024/06/pokemon-embeddings/):

A deep dive into embeddings from Max Woolf, exploring 1,000 different Pokémon (loaded from [PokéAPI](https://pokeapi.co/) using [this epic GraphQL query](https://github.com/minimaxir/pokemon-embeddings/blob/main/query.gql)) and then embedding the cleaned up JSON data using `nomic-embed-text-v1.5` and the official Pokémon image representations using `nomic-embed-vision-v1.5`.

I hadn't seen [nomic\-embed\-vision\-v1\.5](https://huggingface.co/nomic-ai/nomic-embed-vision-v1.5) before: it brings multimodality to Nomic embeddings and operates in the same embedding space as `nomic-embed-text-v1.5` which means you can use it to perform CLIP\-style tricks comparing text and images. Here's [their announcement from June 5th](https://blog.nomic.ai/posts/nomic-embed-vision):

> Together, Nomic Embed is the only unified embedding space that outperforms OpenAI CLIP and OpenAI Text Embedding 3 Small on multimodal and text tasks respectively.

Sadly the new vision weights are available under a non\-commercial Creative Commons license (unlike the text weights which are Apache 2\), so if you want to use the vision weights commercially you'll need to access them [via Nomic's paid API](https://docs.nomic.ai/reference/endpoints/nomic-embed-vision).

---

**Link** 2024\-07\-01 [A write\-ahead log is not a universal part of durability](https://notes.eatonphil.com/2024-07-01-a-write-ahead-log-is-not-a-universal-part-of-durability.html):

Phil Eaton uses pseudo code to provide a clear description of how write\-ahead logs in transactional database systems work, useful for understanding the tradeoffs they make and the guarantees they can provided.   
  
I particularly liked the pseudo code explanation of group commits, where clients block waiting for their commit to be acknowledged as part of a batch of writes flushed to disk.

---

**Link** 2024\-07\-01 [Announcing the Ladybird Browser Initiative](https://ladybird.org/announcement.html):

Andreas Kling's [Ladybird](https://awesomekling.github.io/Ladybird-a-new-cross-platform-browser-project/) is a really exciting project: a from\-scratch implementation of a web browser, initially built as part of the Serenity OS project, which aims to provide a completely independent, open source and fully standards compliant browser.

Last month Andreas [forked Ladybird away from Serenity](https://awesomekling.substack.com/p/forking-ladybird-and-stepping-down-serenityos), recognizing that the potential impact of the browser project on its own was greater than as a component of that project. Crucially, Serenity OS avoids *any* outside code \- splitting out Ladybird allows Ladybird to add dependencies like libjpeg and ffmpeg. The [Ladybird June update](https://www.youtube.com/watch?v=cbw0KrMGHvc) video talks through some of the dependencies they've been able to add since making that decision.

The new Ladybird Browser Initiative puts some financial weight behind the project: it's a US 501(c)(3\) non\-profit [initially funded with $1m from GitHub co\-founder Chris Chris Wanstrath](https://twitter.com/defunkt/status/1807779408092234134). The money is going on engineers: [Andreas says](https://twitter.com/awesomekling/status/1807804311696531575):

> We are 4 full\-time engineers today, and we'll be adding another 3 in the near future

Here's [a 2m28s video](https://www.youtube.com/watch?v=k9edTqPMX_k) from Chris introducing the new foundation and talking about why this project is worth supporting.

---

**Quote** 2024\-07\-01

> *When presented with a difficult task, I ask myself: “what if I didn’t do this at all?”. Most of the time, this is a stupid question, and I have to do the thing. But \~5% of the time, I realize that I can completely skip some work.*

[Evan Hahn](https://evanhahn.com/programming-beliefs-as-of-july-2024/)

---

**Link** 2024\-07\-01 [Russell Keith\-Magee: Build a cross\-platform app with BeeWare](https://www.youtube.com/watch?v=New2JLvWxiE&list=PL2Uw4_HvXqvYhjub9bw4uDAmNtprgAvlJ):

The session videos from PyCon US 2024 have started [showing up on YouTube](https://www.youtube.com/playlist?list=PL2Uw4_HvXqvYhjub9bw4uDAmNtprgAvlJ). So far just for the tutorials, which gave me a chance to catch up on the BeeWare project with this tutorial run by Russell Keith\-Magee.

Here are the [accompanying slides (PDF)](https://pycon-assets.s3.amazonaws.com/2024/media/presentation_slides/41/2024-05-08T23%3A38%3A41.030747/Build_a_cross_platform_GUI_app_with_Be_NscyZ66.pdf), or you can work through the [official tutorial](https://docs.beeware.org/en/latest/tutorial/tutorial-0.html) in the BeeWare documentation.

The tutorial did a great job of clarifying the difference between [Briefcase](https://briefcase.readthedocs.io/) and [Toga](https://toga.readthedocs.io/), the two key components of the BeeWare ecosystem \- each of which can be used independently of the other.

Briefcase solves packaging and installation: it allows a Python project to be packaged as a native application across macOS, Windows, iOS, Android and various flavours of Linux.

Toga is a toolkit for building cross\-platform GUI applications in Python. A UI built using Toga will render with native widgets across all of those supported platforms, and experimental new modes also allow Toga apps to run as SPA web applications and as Rich\-powered terminal tools (via [toga\-textual](https://pypi.org/project/toga-textual/)).

Russell is excellent at both designing and presenting tutorial\-style workshops, and I made a bunch of mental notes on the structure of this one which I hope to apply to my own in the future.

---

**Quote** 2024\-07\-01

> *I like the lies\-to\-children motif, because it underlies the way we run our society and resonates nicely with Discworld. Like the reason for Unseen being a storehouse of knowledge \- you arrive knowing everything and leave realising that you know practically nothing, therefore all the knowledge you had must be stored in the university. But it's like that in "real Science", too. You arrive with your sparkling A\-levels all agleam, and the first job of the tutors is to reveal that what you thought was true is only true for a given value of "truth".   
>   
> Most of us need just "enough" knowledge of the sciences, and it's delivered to us in metaphors and analogies that bite us in the bum if we think they're the same as the truth.*

[Terry Pratchett](https://www.lspace.org/about-terry/interviews/amazon.html)

---

**TIL** 2024\-07\-02 [Mocking Stripe signature checks in a pytest fixture](https://til.simonwillison.net/pytest/pytest-stripe-signature):

I'm writing some code that accepts webhooks from Stripe. I wanted to simulate hits to this endpoint in my Django tests. Stripe uses a `Stripe-Signature` header and I wanted a way to mock my code so that I didn't need to calculate the correct signature. …

---

**Quote** 2024\-07\-02

> *So VisiCalc came and went, but the software genre it pioneered – the spreadsheet – endured to become arguably the most influential type of code ever written, at least in the sense of touching the lives of millions of office workers. I’ve never worked in an organisation in which spreadsheet software was not at the heart of most accounting, budgeting and planning activities. I’ve even known professionals for whom it’s the only piece of PC software they’ve ever used: one elderly accountant of my acquaintance, for example, used Excel even for his correspondence; he simply widened column A to 80 characters, typed his text in descending cells and hit the “print” key.*

[John Naughton](https://www.theguardian.com/commentisfree/2016/jan/03/visicalc-software-first-killer-app-john-naughton)

---

**Link** 2024\-07\-02 [Optimizing Large\-Scale OpenStreetMap Data with SQLite](https://jtarchie.com/posts/2024-07-02-optimizing-large-scale-openstreetmap-data-with-sqlite):

JT Archie describes his project to take 9GB of compressed OpenStreetMap protobufs data for the whole of the United States and load it into a queryable SQLite database.

OSM tags are key/value pairs. The trick used here for FTS\-accelerated tag queries is really neat: build a SQLite FTS table containing the key/value pairs as space concatenated text, then run queries that look like this:

```
SELECT
    id
FROM
    entries e
    JOIN search s ON s.rowid = e.id
WHERE
    -- use FTS index to find subset of possible results
    search MATCH 'amenity cafe'
    -- use the subset to find exact matches
    AND tags->>'amenity' = 'cafe';

```

JT ended up building a custom SQLite Go extension, [SQLiteZSTD](https://github.com/jtarchie/sqlitezstd), to further accelerate things by supporting queries against read\-only zstd compresses SQLite files. Apparently zstd has [a feature](https://github.com/facebook/zstd/blob/3de0541aef8da51f144ef47fb86dcc38b21afb00/contrib/seekable_format/zstd_seekable_compression_format.md) that allows "compressed data to be stored so that subranges of the data can be efficiently decompressed without requiring the entire document to be decompressed", which works well with SQLite's page format.

---

**Link** 2024\-07\-02 [Compare PDFs](https://tools.simonwillison.net/compare-pdfs):

Inspired by [this thread](https://news.ycombinator.com/item?id=40854319) on Hacker News about the C\+\+ [diff\-pdf](http://vslavik.github.io/diff-pdf/) tool I decided to see what it would take to produce a web\-based PDF diff visualization tool using Claude 3\.5 Sonnet.

It took two prompts:

> Build a tool where I can drag and drop on two PDF files and it uses PDF.js to turn each of their pages into canvas elements and then displays those pages side by side with a third image that highlights any differences between them, if any differences exist

That give me a React app that didn't quite work, so I followed\-up with this:

> rewrite that code to not use React at all

Which gave me a working tool! You can see the full Claude transcript plus screenshots of the tool in action [in this Gist](https://gist.github.com/simonw/9d7cbe02d448812f48070e7de13a5ae5?permalink_comment_id=5109044#gistcomment-5109044).

Being able to knock out little custom interactive web tools like this in a couple of minutes is *so much fun*.

---

**Link** 2024\-07\-02 [gemma\-2\-27b\-it\-llamafile](https://huggingface.co/jartine/gemma-2-27b-it-llamafile):

Justine Tunney shipped llamafile packages of Google's new openly licensed (though definitely not open source) [Gemma](https://ai.google.dev/gemma) 2 27b model this morning.

I downloaded the `gemma-2-27b-it.Q5_1.llamafile` version (20\.5GB) to my Mac, ran `chmod 755 gemma-2-27b-it.Q5_1.llamafile` and then `./gemma-2-27b-it.Q5_1.llamafile` and now I'm trying it out through the `llama.cpp` default web UI in my browser. It works great.

It's a *very* capable model \- currently sitting at position 12 on the [LMSYS Arena](https://chat.lmsys.org/) making it the highest ranked open weights model \- one position ahead of Llama\-3\-70b\-Instruct and within striking distance of the GPT\-4 class models.

---

**Link** 2024\-07\-03 [Chrome Prompt Playground](https://tools.simonwillison.net/chrome-prompt-playground):

Google Chrome Canary is currently shipping an experimental on\-device LLM, in the form of Gemini Nano. You can access it via the new `window.ai` API, after first enabling the "Prompt API for Gemini Nano" experiment in `chrome://flags` (and then waiting an indeterminate amount of time for the \~1\.7GB model file to download \- I eventually spotted it in `~/Library/Application Support/Google/Chrome Canary/OptGuideOnDeviceModel`).

I got Claude 3\.5 Sonnet to build me this playground interface for experimenting with the model. You can execute prompts, stream the responses and all previous prompts and responses are stored in `localStorage`.

[![Animated GIF demo. The prompt is Show two greetings each in French and Spanish - on clicking the button the result streams in:  French Bonjour! Bienvenue!, Spanish Hola!, Bienvenido! Scrolling down reveals the stored history, and clicking delete on that prompt removes it from the page.](https://substackcdn.com/image/fetch/$s_!Uc95!,w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6d43ee0f-e8af-4238-9179-3324ff97846d_635x469.gif "Animated GIF demo. The prompt is Show two greetings each in French and Spanish - on clicking the button the result streams in:  French Bonjour! Bienvenue!, Spanish Hola!, Bienvenido! Scrolling down reveals the stored history, and clicking delete on that prompt removes it from the page.")](https://substackcdn.com/image/fetch/$s_!Uc95!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6d43ee0f-e8af-4238-9179-3324ff97846d_635x469.gif)

Here's the [full Sonnet transcript](https://gist.github.com/simonw/e62440114960bc98f200eb3d92593896), and the [final source code](https://github.com/simonw/tools/blob/be05fc38ea600bc65c6a293d5d69d0999e77be10/chrome-prompt-playground.html) for the app.

The best documentation I've found for the new API is is [explainers\-by\-googlers/prompt\-api](https://github.com/explainers-by-googlers/prompt-api) on GitHub.

---

**Quote** 2024\-07\-03

> *If you own the tracks between San Francisco and Los Angeles, you likely have some kind of monopolistic pricing power, because there can only be so many tracks laid between place A and place B. In the case of GPU data centers, there is much less pricing power. GPU computing is increasingly turning into a commodity, metered per hour. Unlike the CPU cloud, which became an oligopoly, new entrants building dedicated AI clouds continue to flood the market. Without a monopoly or oligopoly, high fixed cost \+ low marginal cost businesses almost always see prices competed down to marginal cost (e.g., airlines).*

[David Hahn](https://www.sequoiacap.com/article/ais-600b-question/)

---

**Link** 2024\-07\-04 [Exorcising us of the Primer](https://andymatuschak.org/primer/):

Andy Matuschak talks about the need for educational technologists to break free from the siren's call of "The Young Lady’s Illustrated Primer" \- the universal interactive textbook described by Neal Stephenson in his novel The Diamond Age.

The Primer offers an incredibly compelling vision, and Andy uses fifteen years of his own experience exploring related ideas to pick it apart and highlight its flaws.

> I want to exorcise myself of the Primer. I want to clearly delineate what makes its vision so compelling—what I want to carry in my heart as a creative fuel. But I also want to sharply clarify the lessons we *shouldn’t* take from the Primer, and what it simply ignores. Then I want to reconstitute all that into something new, a vision I can use to drive my work forward.

On the Primer's authoritarianism:

> The Primer has an agenda. It is designed to instill a set of values and ideas, and while it’s supportive of Nell’s curiosities, those are “side quests” to its central structure. Each of the twelve “Lands Beyond” focuses on different topics, but they’re not specific to Nell, and Nell didn’t choose them. In fact, Nell doesn’t even *know* the Primer’s goals for her—she’s never told. Its goals are its own privileged secret. Nell is manipulated so completely by the Primer, for so much of her life, that it’s hard to determine whether she has meaningful goals or values, other than those the Primer’s creators have deemed “good for her”.

I'm also reminded of Stephenson's [piece of advice](https://simonwillison.net/2024/Jun/4/a-tip-from-neal-stephenson/) to people who may have missed an important lesson from the novel:

> Kids need to get answers from humans who love them.

---

**Quote** 2024\-07\-04

> *The expansion of the jagged frontier of AI capability is subtle and requires a lot of experience with various models to understand what they can, and can’t, do. That is why I suggest that people and organizations keep an “impossibility list” \- things that their experiments have shown that AI can definitely not do today but which it can **almost** do. For example, no AI can create a satisfying puzzle or mystery for you to solve, but they are getting closer. When AI models are updated, test them on your impossibility list to see if they can now do these impossible tasks.*

[Ethan Mollick](https://www.oneusefulthing.org/p/gradually-then-suddenly-upon-the)

---

**Link** 2024\-07\-05 [jqjq: jq implementation of jq](https://github.com/wader/jqjq):

2,854 lines of jq that implements a full, working version of jq itself. "A great way to show that jq is a very expressive, capable and neat language!"

---

**Quote** 2024\-07\-05

> *Product teams that are smart are getting off the treadmill. Whatever framework you currently have, start investing in getting to know it deeply. Learn the tools until they are not an impediment to your progress. That’s the only option. Replacing it with a shiny new tool is a trap.   
>   
> \[...]   
>   
> Companies that want to reduce the cost of their frontend tech becoming obsoleted so often should be looking to get back to fundamentals. Your teams should be working closer to the web platform with a lot less complex abstractions. We need to relearn what the web is capable of and go back to that.*

[Marco Rogers](https://polotek.net/posts/the-frontend-treadmill/)

---

**Link** 2024\-07\-05 [Tracking Fireworks Impact on Fourth of July AQI](https://danny.page/views/tracking-fireworks-on-july-4th):

Danny Page ran [shot\-scraper](https://shot-scraper.datasette.io/) once per minute (using cron) against [this Purple Air map](https://map.purpleair.com/1/mAQI/a10/p604800/cC0#8.45/37.764/-121.62) of the Bay Area and turned the captured screenshots into an animation using `ffmpeg`. The result shows the impact of 4th of July fireworks on air quality between 7pm and 7am.

---

**Link** 2024\-07\-05 [UK Parliament election results, now with Datasette](https://electionresults.parliament.uk/):

The House of Commons Library maintains a website of UK parliamentary election results data, currently listing 2010 through 2019 and with 2024 results coming soon.

The site itself is [a Rails and PostgreSQL app](https://github.com/ukparliament/psephology), but I was delighted to learn today that they're also running [a Datasette instance](https://psephology-datasette-f3e7b1b7eb77.herokuapp.com/) with the election results data, linked to from their homepage!

[![The data this website uses is available to query. as a Datasette endpoint. The database schema is published for reference. Mobile Safari screenshot on electionresults.parliament.uk](https://substackcdn.com/image/fetch/$s_!wqF7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3682d925-4c0c-444a-bb4a-a3013e98499e_1290x1328.jpeg "The data this website uses is available to query. as a Datasette endpoint. The database schema is published for reference. Mobile Safari screenshot on electionresults.parliament.uk")](https://substackcdn.com/image/fetch/$s_!wqF7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3682d925-4c0c-444a-bb4a-a3013e98499e_1290x1328.jpeg)

The raw data is also available [as CSV files](https://github.com/ukparliament/psephology/tree/main/db/data) in their GitHub repository. Here's [their Datasette configuration](https://github.com/ukparliament/psephology-datasette), which includes a copy of [their SQLite database](https://github.com/ukparliament/psephology-datasette/blob/main/psephology.db).

---

**Link** 2024\-07\-05 [interactive\-feed](https://github.com/sammorrisdesign/interactive-feed):

Sam Morris maintains this project which gathers interactive, graphic and data visualization stories from various newsrooms around the world and publishes them on [Twitter](https://twitter.com/InteractiveFeed), [Mastodon](https://botsin.space/@Interactives) and [Bluesky](https://staging.bsky.app/profile/interactives.bsky.social).

It runs automatically using GitHub Actions, and gathers data using a number of different techniques \- XML feeds, custom API integrations (for the NYT, Guardian and Washington Post) and in some cases by scraping index pages on news websites [using CSS selectors and cheerio](https://github.com/sammorrisdesign/interactive-feed/blob/1652b7b6a698ad97f88b542cfdd94a90be4f119c/src/fetchers.js#L221-L251).

The data it collects is archived as JSON in the [data/ directory](https://github.com/sammorrisdesign/interactive-feed/tree/main/data) of the repository.

---

**Link** 2024\-07\-06 [Home\-Cooked Software and Barefoot Developers](https://maggieappleton.com/home-cooked-software):

I really enjoyed this talk by Maggie Appleton from this year's Local\-first Conference in Berlin.

> For the last \~year I've been keeping a close eye on how language models capabilities meaningfully change the speed, ease, and accessibility of software development. The slightly bold theory I put forward in this talk is that we're on a verge of a golden age of local, home\-cooked software and a new kind of developer – what I've called the barefoot developer.

It's a great talk, and the design of the slides is outstanding.

It reminded me of Robin Sloan's [An app can be a home\-cooked meal](https://www.robinsloan.com/notes/home-cooked-app/), which Maggie references in the talk. Also relevant: this delightful recent Hacker News thread, [Ask HN: Is there any software you only made for your own use but nobody else?](https://news.ycombinator.com/item?id=40878765)

My favourite version of our weird new LLM future is one where the pool of people who can use computers to automate things in their life is massively expanded.

The [other videos from the conference](https://m.youtube.com/playlist?list=PL4isNRKAwz2O9FxP97_EbOivIWWwSWt5j) are worth checking out too.

---

**Link** 2024\-07\-07 [Reasons to use your shell's job control](https://jvns.ca/blog/2024/07/03/reasons-to-use-job-control/):

Julia Evans summarizes an informal survey of useful things you can do with shell job control features \- `fg`, `bg`, `Ctrl+Z` and the like. Running `tcdump` in the background so you can see its output merged in with calls to `curl` is a neat trick.

---

**Quote** 2024\-07\-08

> *Voters in the Clapham and Brixton Hill constituency can rest easy \- despite appearances, their Reform candidate Mark Matlock really does exist. \[...] Matlock \- based in the South Cotswolds, some 100 miles from the constituency in which he is standing \- confirmed: "I am a real person." Although his campaign image is Al\-generated, he said this was for lack of a real photo of him wearing a tie in Reform's trademark turquoise.*

[Private Eye](https://twitter.com/PrivateEyeNews/status/1810327043827249452)

---

**Link** 2024\-07\-08 [Geomys, a blueprint for a sustainable open source maintenance firm](https://words.filippo.io/dispatches/geomys/):

Filippo Valsorda has been [working as a full\-time professional open source maintainer](https://words.filippo.io/full-time-maintainer/) for nearly two years now, accepting payments on retainer from companies that depend on his cryptography Go packages.

This has worked well enough that he's now expanding: Geomys (a [genus of gophers](https://en.m.wikipedia.org/wiki/Geomys)) is a new company which adds two new "associate maintainers" and an administrative director, covering more projects and providing clients with access to more expertise.

Filipino describes the model like this:

> If you’re betting your business on a critical open source technology, you
> 
> 1. want it to be sustainably and predictably maintained; and
> 2. need occasional access to expertise that would be blisteringly expensive to acquire and retain.
> 
> Getting maintainers on retainer solves both problems for a fraction of the cost of a fully\-loaded full\-time engineer. From the maintainers’ point of view, it’s steady income to keep doing what they do best, and to join one more Slack Connect channel to answer high\-leverage questions. It’s a great deal for both sides.

For more on this model, watch Filippo's [FOSDEM talk from earlier this year](https://fosdem.org/2024/schedule/event/fosdem-2024-2000-maintaining-go-as-a-day-job-a-year-later/).

---

**Link** 2024\-07\-08 [Box shadow CSS generator](https://tools.simonwillison.net/box-shadow):

Another example of a tiny personal tool I built using Claude 3\.5 Sonnet and artifacts. In this case my prompt was:

> CSS for a slight box shadow, build me a tool that helps me twiddle settings and preview them and copy and paste out the CSS

I changed my mind half way through typing the prompt and asked it for a custom tool, and it built me this!

[![Box shadow CSS generator. Shows a preview, then provides sliders to set Horizontal Offset, Vertical Offset, Blur Radius,  Spread Radius,  Color and Opacity - plus the generated CSS and a Copy to Clipboard button](https://substackcdn.com/image/fetch/$s_!nqT_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F36be8023-7694-48c4-b45f-6560f7cfbfdb_1288x1802.jpeg "Box shadow CSS generator. Shows a preview, then provides sliders to set Horizontal Offset, Vertical Offset, Blur Radius,  Spread Radius,  Color and Opacity - plus the generated CSS and a Copy to Clipboard button")](https://substackcdn.com/image/fetch/$s_!nqT_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F36be8023-7694-48c4-b45f-6560f7cfbfdb_1288x1802.jpeg)

Here's [the full transcript](https://gist.github.com/simonw/ffbf7d7abbf56a126c89e7d62442696a) \- in a follow\-up prompt I asked for help deploying it and it rewrote the tool to use `<script type="text/babel">` and the [babel\-standalone](https://babeljs.io/docs/babel-standalone) library to add React JSX support directly in the browser \- a bit of a hefty dependency (387KB compressed / 2\.79MB total) but I think acceptable for this kind of one\-off tool.

Being able to knock out tiny custom tools like this on a whim is a really interesting new capability. It's also a lot of fun!

---

**Link** 2024\-07\-08 [Type click type by Brian Grubb](https://briancgrubb.substack.com/):

I just found out my favourite TV writer, Brian Grubb, is [no longer with Uproxx](https://briancgrubb.substack.com/p/goodbyes-andor-hellos) and is now writing for his own newsletter \- free on Sunday, paid\-subscribers only on Friday. I hit subscribe so fast.

In addition to TV, Brian's coverage of heists \- most recently [Lego](https://briancgrubb.substack.com/p/welcome-to-the-summer-of-lego-heists) and an [attempted heist of Graceland](https://briancgrubb.substack.com/p/it-sure-looks-like-a-bunch-of-idiots) \- "It really does look like a bunch of idiots tried to steal and auction off Graceland using Hotmail accounts and they almost got away with it" \- is legendary.

I'd love to see more [fun little Friday night shows](https://briancgrubb.substack.com/p/please-make-more-fun-little-friday) too.

---

**Quote** 2024\-07\-08

> *Someone elsewhere left a comment like "I CAN’T BELIEVE IT TOOK HER 15 YEARS TO LEARN BASIC READLINE COMMANDS". those comments are very silly and I'm going to keep writing “it took me 15 years to learn this basic thing" forever because I think it's important for people to know that it's normal to take a long time to learn “basic" things*

[Julia Evans](https://social.jvns.ca/@b0rk/112752380693244654)

---