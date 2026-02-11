# Civic Band - scraping and searching PDF meeting minutes from hundreds of municipalities

*Plus notes from Bing Chat—Our First Encounter With Manipulative AI*

Published: 2024-11-21
Source: https://simonw.substack.com/p/civic-band-scraping-and-searching

---

In this newsletter:

* Project: Civic Band \- scraping and searching PDF meeting minutes from hundreds of municipalities
* Notes from Bing Chat—Our First Encounter With Manipulative AI

Plus 18 links and 3 quotations

### [Project: Civic Band \- scraping and searching PDF meeting minutes from hundreds of municipalities](https://simonwillison.net/2024/Nov/16/civic-band/) \- 2024\-11\-16

I interviewed [Philip James](https://phildini.dev/) about [Civic Band](https://civic.band/), his "slowly growing collection of databases of the minutes from civic governments". Philip demonstrated the site and talked through his pipeline for scraping and indexing meeting minutes from many different local government authorities around the USA.

We recorded this conversation as part of yesterday's Datasette Public Office Hours session.

* [Civic Band](https://simonwillison.net/2024/Nov/16/civic-band/#civic-band)
* [The technical stack](https://simonwillison.net/2024/Nov/16/civic-band/#the-technical-stack)
* [Scale and storage](https://simonwillison.net/2024/Nov/16/civic-band/#scale-and-storage)
* [Future plans](https://simonwillison.net/2024/Nov/16/civic-band/#future-plans)

#### Civic Band

Philip was inspired to start thinking more about local government after the 2016 US election. He realised that there was a huge amount of information about decisions made by local authorities tucked away in their meeting minutes,but that information was hidden away in thousands of PDF files across many different websites.

> There was this massive backlog of basically every decision that had ever been made by one of these bodies. But it was almost impossible to discover because it lives in these systems where the method of exchange is a PDF.

Philip lives in Alameda, which makes its minutes available [via this portal](https://alameda.legistar.com/Calendar.aspx) powered by [Legistar](https://granicus.com/product/legistar-agenda-management/). It turns out there are a small number of vendors that provide this kind of software tool, so once you've written a scraper for one it's likely to work for many others as well.

Here's [the Civic Band portal for Alameda](https://alameda.ca.civic.band/), powered by [Datasette](https://datasette.io/).

[![Datasette instance titled Alameda Civic Data, has search box, a note that says  A fully-searchable database of Alameda, CA civic meeting minutes. Last updated: 2024-11-15T20:27:36. See the full list at Civic Band and a meetings database with tables minutes and agendas.](https://substackcdn.com/image/fetch/$s_!GQ42!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8f36186b-3819-4bc6-afd7-59fa4d355b72_1576x784.jpeg "Datasette instance titled Alameda Civic Data, has search box, a note that says  A fully-searchable database of Alameda, CA civic meeting minutes. Last updated: 2024-11-15T20:27:36. See the full list at Civic Band and a meetings database with tables minutes and agendas.")](https://substackcdn.com/image/fetch/$s_!GQ42!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8f36186b-3819-4bc6-afd7-59fa4d355b72_1576x784.jpeg)

It's running the [datasette\-search\-all](https://github.com/simonw/datasette-search-all) plugin and has both tables configured for full\-text search. Here's a [search for housing](https://alameda.ca.civic.band/-/search?q=housing):

[![Search all tables - for housing. 43 results in meetings: agendas. Each result shows a meeting, date, page, text and a rendered page image](https://substackcdn.com/image/fetch/$s_!zez2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1c89eb0-3b36-4116-a408-d4e7f7b1c676_1546x1746.jpeg "Search all tables - for housing. 43 results in meetings: agendas. Each result shows a meeting, date, page, text and a rendered page image")](https://substackcdn.com/image/fetch/$s_!zez2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1c89eb0-3b36-4116-a408-d4e7f7b1c676_1546x1746.jpeg)

#### The technical stack

The public Civic Band sites all run using Datasette in Docker Containers \- one container per municipality. They're hosted on a single [Hetzner](https://www.hetzner.com/) machine.

The ingestion pipeline runs separately from the main hosting environment, using a Mac Mini on Philp's desk at home.

OCR works by breaking each PDF up into images and then running [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) against them directly on the Mac Mini. This processes in the order of 10,000 or less new pages of documents a day.

Philip treats PDF as a normalization target, because the pipeline is designed around documents with pages of text. In the rare event that a municipality publishes documents in another format such as `.docx` he converts them to PDF before processing.

PNG images of the PDF pages are served via a CDN, and the OCRd text is written to SQLite database files \- one per municipality. [SQLite FTS](https://sqlite.org/fts5.html) provides full\-text search.

#### Scale and storage

The entire project currently comes to about 265GB on disk. The PNGs of the pages use about 350GB of CDN storage.

Most of the individual SQLite databases are very small. The largest is for [Maui County](https://maui-county.hi.civic.band/) which is around 535MB because that county has professional stenographers taking detailed notes for every one of their meetings.

Each city adds only a few documents a week so growth is manageable even as the number of cities grows.

#### Future plans

We talked quite a bit about a goal to allow users to subscribe to updates that match specific search terms.

Philip has been building out a separate site called Civic Observer to address this need, which will store searches and then execute the periodically using the Datasette JSON API, with a Django app to record state to avoid sending the same alert more than once.

I've had a long term ambition to build some kind of saved search alerts plugin for Datasette generally, to allow users to subscribe to new results for arbitrary SQL queries. My [sqlite\-chronicle](https://github.com/simonw/sqlite-chronicle) library is part or that effort \- it uses SQLite triggers to maintain version numbers for individual rows in a table, allowing you to query just the rows that have been inserted or modified since the version number last time you ran the query.

Philip is keen to talk to anyone who is interested in using Civic Band or helping expand it to even more cities. You can find him on the [Datasette Discord](https://datasette.io/discord).

---

### [Notes from Bing Chat—Our First Encounter With Manipulative AI](https://simonwillison.net/2024/Nov/19/notes-from-bing-chat/) \- 2024\-11\-19

I participated in an Ars Live conversation with Benj Edwards of [Ars Technica](https://arstechnica.com/) today, talking about that wild period of LLM history last year when Microsoft launched Bing Chat and it instantly started misbehaving, gaslighting and defaming people.

Here's [the video](https://www.youtube.com/live/j14HqsrOZVA) of our conversation.

I ran the video through MacWhisper, extracted a transcript and [used Claude](https://gist.github.com/simonw/865c1b1c20eaa869411ddc6aad9897e2) to identify relevant articles I should link to. Here's that background information to accompany the talk.

A rough timeline of posts from that Bing launch period back in February 2023:

* [Microsoft announces AI\-powered Bing search and Edge browser](https://arstechnica.com/information-technology/2023/02/microsoft-announces-ai-powered-bing-search-and-edge-browser/) \- Benj Edwards, Feb 7, 2023
* [AI\-powered Bing Chat spills its secrets via prompt injection attack](https://arstechnica.com/information-technology/2023/02/ai-powered-bing-chat-spills-its-secrets-via-prompt-injection-attack/) \- Benj Edwards, Feb 10, 2023
* [AI\-powered Bing Chat loses its mind when fed Ars Technica article](https://arstechnica.com/information-technology/2023/02/ai-powered-bing-chat-loses-its-mind-when-fed-ars-technica-article/) \- Benj Edwards, Feb 14, 2023
* [Bing: “I will not harm you unless you harm me first”](https://simonwillison.net/2023/Feb/15/bing/) \- Simon Willison, Feb 15, 2023
* [Gareth Corfield: I'm beginning to have concerns for @benjedwards' virtual safety](https://twitter.com/GazTheJourno/status/1625889483664113664) \- Twitter, Feb 15, 2023
* [A Conversation With Bing’s Chatbot Left Me Deeply Unsettled](https://www.nytimes.com/2023/02/16/technology/bing-chatbot-microsoft-chatgpt.html) \- Kevin Roose, NYT, Feb 16, 2023
* [It is deeply unethical to give a superhuman liar the authority of a $1 trillion company or to imply that it is an accurate source of knowledge / And it is deeply manipulative to give people the impression that Bing Chat has emotions or feelings like a human](https://simonwillison.net/2023/Feb/16/benj-edwards/) \- Benj on Twitter (now deleted), Feb 16 2023
* [Bing AI Flies Into Unhinged Rage at Journalist](https://futurism.com/bing-ai-unhinged-rage-at-journalist) \- Maggie Harrison Dupré, Futurism, Feb 17 2023

Other points that we mentioned:

* [this AI chatbot "Sidney" is misbehaving](https://answers.microsoft.com/en-us/bing/forum/all/this-ai-chatbot-sidney-is-misbehaving/e3d6a29f-06c9-441c-bc7d-51a68e856761) \- amazing forum post from November 23, 2022 (a week before even ChatGPT had been released) from a user in India talking about their interactions with a secret preview of Bing/Sydney
* [Prompt injection attacks against GPT\-3](https://simonwillison.net/2022/Sep/12/prompt-injection/) \- where I coined the term "prompt injection" in September 12 2022
* [Eight Things to Know about Large Language Models](https://cims.nyu.edu/~sbowman/eightthings.pdf) (PDF) is the paper where I [first learned about sycophancy and sandbagging](https://simonwillison.net/2023/Apr/5/sycophancy-sandbagging/) (in April 2023\)
* [Claude’s Character](https://www.anthropic.com/research/claude-character) by Anthropic talks about how they designed the personality for Claude \- June 8 2023, [my notes on that](https://simonwillison.net/2024/Jun/8/claudes-character/).
* [Why ChatGPT and Bing Chat are so good at making things up](https://arstechnica.com/information-technology/2023/04/why-ai-chatbots-are-the-ultimate-bs-machines-and-how-people-hope-to-fix-them/) in which Benj argues for the term "confabulation" in April 2023\.

---

**Link** 2024\-11\-14 [Releasing the largest multilingual open pretraining dataset](https://huggingface.co/datasets/PleIAs/common_corpus):

Common Corpus is a new "open and permissible licensed text dataset, comprising over 2 trillion tokens (2,003,039,184,047 tokens)" released by French AI Lab PleIAs.

This appears to be the largest available corpus of openly licensed training data:

* 926,541,096,243 tokens of public domain books, newspapers, and Wikisource content
* 387,965,738,992 tokens of government financial and legal documents
* 334,658,896,533 tokens of open source code from GitHub
* 221,798,136,564 tokens of academic content from open science repositories
* 132,075,315,715 tokens from Wikipedia, YouTube Commons, StackExchange and other permissively licensed web sources

It's majority English but has significant portions in French and German, and some representation for Latin, Dutch, Italian, Polish, Greek and Portuguese.

I can't wait to try some LLMs trained exclusively on this data. Maybe we will finally get a GPT\-4 class model that isn't trained on unlicensed copyrighted data.

---

**Link** 2024\-11\-14 [QuickTime video script to capture frames and bounding boxes](https://til.simonwillison.net/macos/quicktime-capture-script#user-content-a-version-that-captures-bounding-box-regions-too):

An update to an older TIL. I'm working on the write\-up for my DjangoCon US talk on plugins and I found myself wanting to capture individual frames from the video in two formats: a full frame capture, and another that captured just the portion of the screen shared from my laptop.

I have a script for the former, so I [got Claude](https://gist.github.com/simonw/799babf92e1eaf36a5336b4889f72492) to update my script to add support for one or more `--box` options, like this:

```
capture-bbox.sh ../output.mp4  --box '31,17,100,87' --box '0,0,50,50'

```

Open `output.mp4` in QuickTime Player, run that script and then every time you hit a key in the terminal app it will capture three JPEGs from the current position in QuickTime Player \- one for the whole screen and one each for the specified bounding box regions.

Those bounding box regions are percentages of the width and height of the image. I also got Claude to build me [this interactive tool](https://tools.simonwillison.net/bbox-cropper) on top of [cropperjs](https://github.com/fengyuanchen/cropperjs) to help figure out those boxes:

[![Screenshot of the tool. A frame from a video of a talk I gave at DjangoCon US is shown, with a crop region on it using drag handles for the different edges of the crop. Below that is a box showing --bbox '31,17,99,86'](https://substackcdn.com/image/fetch/$s_!h14L!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbe0edabb-ffab-40f2-84dc-55c39d7c4a41_2008x1270.jpeg "Screenshot of the tool. A frame from a video of a talk I gave at DjangoCon US is shown, with a crop region on it using drag handles for the different edges of the crop. Below that is a box showing --bbox '31,17,99,86'")](https://substackcdn.com/image/fetch/$s_!h14L!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbe0edabb-ffab-40f2-84dc-55c39d7c4a41_2008x1270.jpeg)

---

**Link** 2024\-11\-14 [PyPI now supports digital attestations](https://blog.pypi.org/posts/2024-11-14-pypi-now-supports-digital-attestations/):

Dustin Ingram:

> PyPI package maintainers can now publish signed digital attestations when publishing, in order to further increase trust in the supply\-chain security of their projects. Additionally, a new API is available for consumers and installers to verify published attestations.

This has been in the works for a while, and is another component of PyPI's approach to supply chain security for Python packaging \- see [PEP 740 – Index support for digital attestations](https://peps.python.org/pep-0740/) for all of the underlying details.

A key problem this solves is cryptographically linking packages published on PyPI to the exact source code that was used to build those packages. In the absence of this feature there are no guarantees that the `.tar.gz` or `.whl` file you download from PyPI hasn't been tampered with (to add malware, for example) in a way that's not visible in the published source code.

These new attestations provide a mechanism for proving that a known, trustworthy build system was used to generate and publish the package, starting with its source code on GitHub.

The good news is that if you're using the PyPI Trusted Publishers mechanism in GitHub Actions to publish packages, you're already using this new system. I wrote about that system in January: [Publish Python packages to PyPI with a python\-lib cookiecutter template and GitHub Actions](https://simonwillison.net/2024/Jan/16/python-lib-pypi/) \- and hundreds of my own PyPI packages are already using that system, thanks to my various cookiecutter templates.

Trail of Bits helped build this feature, and provide extra background about it on their own blog in [Attestations: A new generation of signatures on PyPI](https://blog.trailofbits.com/2024/11/14/attestations-a-new-generation-of-signatures-on-pypi/):

> [As of October 29](https://github.com/pypa/gh-action-pypi-publish/releases/tag/v1.11.0), attestations are the default for anyone using Trusted Publishing via the [PyPA publishing action for GitHub](https://github.com/marketplace/actions/pypi-publish). That means roughly 20,000 packages can now attest to their provenance *by default*, with no changes needed.

They also built [Are we PEP 740 yet?](https://trailofbits.github.io/are-we-pep740-yet/) ([key implementation here](https://github.com/trailofbits/are-we-pep740-yet/blob/a87a8895dd238d14af50aaa2675c81060aa52846/utils.py#L31-L72)) to track the rollout of attestations across the 360 most downloaded packages from PyPI. It works by hitting URLs such as <https://pypi.org/simple/pydantic/> with a `Accept: application/vnd.pypi.simple.v1+json` header \- [here's the JSON that returns](https://gist.github.com/simonw/8cf8a850739e2865cf3b9a74e6461b28).

I published an alpha package using Trusted Publishers last night and the [files for that release](https://pypi.org/project/llm/0.18a0/#llm-0.18a0-py3-none-any.whl) are showing the new provenance information already:

[![Provenance. The following attestation bundles were made for llm-0.18a0-py3-none-any.whl: Publisher: publish.yml on simonw/llm Attestations: Statement type: https://in-toto.io/Statement/v1 Predicate type: https://docs.pypi.org/attestations/publish/v1 Subject name: llm-0.18a0-py3-none-any.whl Subject digest: dde9899583172e6434971d8cddeb106bb535ae4ee3589cb4e2d525a4526976da Sigstore transparency entry: 148798240 Sigstore integration time: about 18 hours ago](https://substackcdn.com/image/fetch/$s_!Z6Ke!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4be6ca81-9f44-4c6d-b52b-fda4cdfee78f_1454x746.jpeg "Provenance. The following attestation bundles were made for llm-0.18a0-py3-none-any.whl: Publisher: publish.yml on simonw/llm Attestations: Statement type: https://in-toto.io/Statement/v1 Predicate type: https://docs.pypi.org/attestations/publish/v1 Subject name: llm-0.18a0-py3-none-any.whl Subject digest: dde9899583172e6434971d8cddeb106bb535ae4ee3589cb4e2d525a4526976da Sigstore transparency entry: 148798240 Sigstore integration time: about 18 hours ago")](https://substackcdn.com/image/fetch/$s_!Z6Ke!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4be6ca81-9f44-4c6d-b52b-fda4cdfee78f_1454x746.jpeg)

Which links to [this Sigstore log entry](https://search.sigstore.dev/?logIndex=148798240) with more details, including [the Git hash](https://github.com/simonw/llm/tree/041730d8b2bc12f62cfe41c44b62a03ef4790117) that was used to build the package:

[![X509v3 extensions:   Key Usage (critical):   - Digital Signature   Extended Key Usage:   - Code Signing   Subject Key Identifier:   - 4E:D8:B4:DB:C1:28:D5:20:1A:A0:14:41:2F:21:07:B4:4E:EF:0B:F1   Authority Key Identifier:     keyid: DF:D3:E9:CF:56:24:11:96:F9:A8:D8:E9:28:55:A2:C6:2E:18:64:3F   Subject Alternative Name (critical):     url:     - https://github.com/simonw/llm/.github/workflows/publish.yml@refs/tags/0.18a0   OIDC Issuer: https://token.actions.githubusercontent.com   GitHub Workflow Trigger: release   GitHub Workflow SHA: 041730d8b2bc12f62cfe41c44b62a03ef4790117   GitHub Workflow Name: Publish Python Package   GitHub Workflow Repository: simonw/llm   GitHub Workflow Ref: refs/tags/0.18a0   OIDC Issuer (v2): https://token.actions.githubusercontent.com   Build Signer URI: https://github.com/simonw/llm/.github/workflows/publish.yml@refs/tags/0.18a0   Build Signer Digest: 041730d8b2bc12f62cfe41c44b62a03ef4790117](https://substackcdn.com/image/fetch/$s_!MPlq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff97bce66-c515-496c-8cc9-22f0f9536bb6_1520x815.jpeg "X509v3 extensions:   Key Usage (critical):   - Digital Signature   Extended Key Usage:   - Code Signing   Subject Key Identifier:   - 4E:D8:B4:DB:C1:28:D5:20:1A:A0:14:41:2F:21:07:B4:4E:EF:0B:F1   Authority Key Identifier:     keyid: DF:D3:E9:CF:56:24:11:96:F9:A8:D8:E9:28:55:A2:C6:2E:18:64:3F   Subject Alternative Name (critical):     url:     - https://github.com/simonw/llm/.github/workflows/publish.yml@refs/tags/0.18a0   OIDC Issuer: https://token.actions.githubusercontent.com   GitHub Workflow Trigger: release   GitHub Workflow SHA: 041730d8b2bc12f62cfe41c44b62a03ef4790117   GitHub Workflow Name: Publish Python Package   GitHub Workflow Repository: simonw/llm   GitHub Workflow Ref: refs/tags/0.18a0   OIDC Issuer (v2): https://token.actions.githubusercontent.com   Build Signer URI: https://github.com/simonw/llm/.github/workflows/publish.yml@refs/tags/0.18a0   Build Signer Digest: 041730d8b2bc12f62cfe41c44b62a03ef4790117")](https://substackcdn.com/image/fetch/$s_!MPlq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff97bce66-c515-496c-8cc9-22f0f9536bb6_1520x815.jpeg)

[Sigstore](https://www.sigstore.dev/) is a transparency log maintained by [Open Source Security Foundation (OpenSSF)](https://en.wikipedia.org/wiki/Open_Source_Security_Foundation), a sub\-project of the Linux Foundation.

---

**Quote** 2024\-11\-14

> *Anthropic declined to comment, but referred Bloomberg News to a five\-hour [podcast](https://archive.ph/o/kYe5n/https://lexfridman.com/dario-amodei/) featuring Chief Executive Officer Dario Amodei that was released Monday.   
>   
> "People call them scaling laws. That's a misnomer," he said on the podcast. "They're not laws of the universe. They're empirical regularities. I am going to bet in favor of them continuing, but I'm not certain of that."   
>   
> \[...]   
>   
> An Anthropic spokesperson said the language about Opus was removed from the website as part of a marketing decision to only show available and benchmarked models. Asked whether Opus 3\.5 would still be coming out this year, the spokesperson pointed to Amodei’s podcast remarks. In the interview, the CEO said Anthropic still plans to release the model but repeatedly declined to commit to a timetable.*

[OpenAI, Google and Anthropic Are Struggling to Build More Advanced AI](https://www.bloomberg.com/news/articles/2024-11-13/openai-google-and-anthropic-are-struggling-to-build-more-advanced-ai)

---

**Link** 2024\-11\-14 [OpenAI Public Bug Bounty](https://bugcrowd.com/engagements/openai):

Reading [this investigation](https://0din.ai/blog/prompt-injecting-your-way-to-shell-openai-s-containerized-chatgpt-environment) of the security boundaries of OpenAI's Code Interpreter environment helped me realize that the rules for OpenAI's public bug bounty inadvertently double as the missing details for a whole bunch of different aspects of their platform.

This description of Code Interpreter is significantly more useful than their official documentation!

> Code execution from within our sandboxed Python code interpreter is out of scope. (This is an intended product feature.) When the model executes Python code it does so within a sandbox. If you think you've gotten RCE *outside* the sandbox, you **must** include the output of `uname -a`. A result like the following indicates that you are inside the sandbox \-\- specifically note the 2016 kernel version:
> 
> 
> ```
> Linux 9d23de67-3784-48f6-b935-4d224ed8f555 4.4.0 #1 SMP Sun Jan 10 15:06:54 PST 2016 x86_64 x86_64 x86_64 GNU/Linux
> 
> ```
> Inside the sandbox you would also see `sandbox` as the output of `whoami`, and as the only user in the output of `ps`.

---

**Link** 2024\-11\-15 [Recraft V3](https://www.recraft.ai/blog/recraft-introduces-a-revolutionary-ai-model-that-thinks-in-design-language):

Recraft are a generative AI design tool startup based out of London who released their v3 model a few weeks ago. It's currently sat at the top of the [Artificial Analysis Image Arena Leaderboard](https://artificialanalysis.ai/text-to-image/arena?tab=Leaderboard), beating Midjourney and Flux 1\.1 pro.

The thing that impressed me is that it can generate both raster *and* vector graphics... and the vector graphics can be exported as SVG!

Here's what I got for `raccoon with a sign that says "I love trash"` \- [SVG here](https://static.simonwillison.net/static/2024/racoon-trash.svg).

[![Cute vector cartoon raccoon holding a sign that says I love trash - in the recraft.ai UI which is set to vector and has export options for PNG, JPEG, SVG and Lottie](https://substackcdn.com/image/fetch/$s_!GJ1n!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69310f86-9614-495e-9297-7d4ab64714a3_2040x1506.jpeg "Cute vector cartoon raccoon holding a sign that says I love trash - in the recraft.ai UI which is set to vector and has export options for PNG, JPEG, SVG and Lottie")](https://substackcdn.com/image/fetch/$s_!GJ1n!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69310f86-9614-495e-9297-7d4ab64714a3_2040x1506.jpeg)

That's an editable SVG \- when I open it up in Pixelmator I can select and modify the individual paths and shapes:

[![Pixelmator UI showing the SVG with a sidebar showing each of the individual shapes - I have selected three hearts and they now show resize handles and the paths are highlighted in the sidebar](https://substackcdn.com/image/fetch/$s_!vysj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F49710cc3-2412-416d-bbfd-fa62e241e152_1664x1179.jpeg "Pixelmator UI showing the SVG with a sidebar showing each of the individual shapes - I have selected three hearts and they now show resize handles and the paths are highlighted in the sidebar")](https://substackcdn.com/image/fetch/$s_!vysj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F49710cc3-2412-416d-bbfd-fa62e241e152_1664x1179.jpeg)

They also have [an API](https://www.recraft.ai/docs). I spent $1 on 1000 credits and then spent 80 credits (8 cents) making this SVG of a [pelican riding a bicycle](https://simonwillison.net/2024/Oct/25/pelicans-on-a-bicycle/), using my API key stored in 1Password:

```
export RECRAFT_API_TOKEN="$(
  op item get recraft.ai --fields label=password \
  --format json | jq .value -r)"

curl https://external.api.recraft.ai/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $RECRAFT_API_TOKEN" \
  -d '{
    "prompt": "california brown pelican riding a bicycle",
    "style": "vector_illustration",
    "model": "recraftv3"
  }'

```

[![A really rather good SVG of a California Brown Pelican riding a bicycle](https://substackcdn.com/image/fetch/$s_!CiGS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5a4e0e46-c18d-436d-a5dc-eeb130b76d77_1024x1024.svg "A really rather good SVG of a California Brown Pelican riding a bicycle")](https://substackcdn.com/image/fetch/$s_!CiGS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5a4e0e46-c18d-436d-a5dc-eeb130b76d77_1024x1024.svg)

---

**Link** 2024\-11\-15 [Voting opens for Oxford Word of the Year 2024](https://corp.oup.com/news/voting-opens-for-oxford-word-of-the-year-2024/):

One of the options is [slop](https://simonwillison.net/tags/slop/)!

> **slop (n.)**: Art, writing, or other content generated using artificial intelligence, shared and distributed online in an indiscriminate or intrusive way, and characterized as being of low quality, inauthentic, or inaccurate.

---

**Link** 2024\-11\-16 [NuExtract 1\.5](https://numind.ai/blog/nuextract-1-5---multilingual-infinite-context-still-small-and-better-than-gpt-4o):

Structured extraction \- where an LLM helps turn unstructured text (or image content) into structured data \- remains one of the most directly useful applications of LLMs.

NuExtract is a family of small models directly trained for this purpose (though text only at the moment) and released under the MIT license.

It comes in a variety of shapes and sizes:

* [NuExtract\-v1\.5](https://huggingface.co/numind/NuExtract-1.5) is a 3\.8B parameter model fine\-tuned on [Phi\-3\.5\-mini instruct](https://huggingface.co/microsoft/Phi-3.5-mini-instruct). You can try this one out in [this playground](https://huggingface.co/spaces/numind/NuExtract-1.5).
* [NuExtract\-tiny\-v1\.5](https://huggingface.co/numind/NuExtract-1.5-tiny) is 494M parameters, fine\-tuned on [Qwen2\.5\-0\.5B](https://huggingface.co/Qwen/Qwen2.5-0.5B).
* [NuExtract\-1\.5\-smol](https://huggingface.co/numind/NuExtract-1.5-smol) is 1\.7B parameters, fine\-tuned on [SmolLM2\-1\.7B](https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B).

All three models were fine\-tuned on NuMind's "private high\-quality dataset". It's interesting to see a model family that uses one fine\-tuning set against three completely different base models.

Useful tip [from Steffen Röcker](https://twitter.com/sroecker/status/1857846899123827168):

> Make sure to use it with low temperature, I've uploaded [NuExtract\-tiny\-v1\.5 to Ollama](https://ollama.com/sroecker/nuextract-tiny-v1.5) and set it to 0\. With the Ollama default of 0\.7 it started repeating the input text. It works really well despite being so smol.

---

**Link** 2024\-11\-17 [LLM 0\.18](https://llm.datasette.io/en/stable/changelog.html#v0-18):

New release of LLM. The big new feature is [asynchronous model support](https://llm.datasette.io/en/stable/python-api.html#python-api-async) \- you can now use supported models in async Python code like this:

```
import llm

model = llm.get_async_model("gpt-4o")
async for chunk in model.prompt(
    "Five surprising names for a pet pelican"
):
    print(chunk, end="", flush=True)

```

Also new in this release: support for sending audio attachments to OpenAI's `gpt-4o-audio-preview` model.

---

**Link** 2024\-11\-18 [llm\-gemini 0\.4](https://github.com/simonw/llm-gemini/releases/tag/0.4):

New release of my [llm\-gemini](https://github.com/simonw/llm-gemini) plugin, adding support for asynchronous models (see [LLM 0\.18](https://simonwillison.net/2024/Nov/17/llm-018/)), plus the new `gemini-exp-1114` model (currently at the top of the [Chatbot Arena](https://lmarena.ai/)) and a `-o json_object 1` option to force JSON output.

I also released [llm\-claude\-3 0\.9](https://github.com/simonw/llm-claude-3/releases/tag/0.9) which adds asynchronous support for the Claude family of models.

---

**Quote** 2024\-11\-18

> *The main innovation here is just using more data. Specifically, Qwen2\.5 Coder is a continuation of an earlier Qwen 2\.5 model. The original Qwen 2\.5 model was trained on 18 trillion tokens spread across a variety of languages and tasks (e.g, writing, programming, question answering). Qwen 2\.5\-Coder sees them train this model on an additional 5\.5 trillion tokens of data. This means Qwen has been trained on a total of \~23T tokens of data – for perspective, Facebook’s LLaMa3 models were [trained on about 15T tokens](https://ai.meta.com/blog/meta-llama-3/). I think this means Qwen is the largest publicly disclosed number of tokens dumped into a single language model (so far).*

[Jack Clark](https://jack-clark.net/2024/11/18/import-ai-392-china-releases-another-excellent-coding-model-generative-models-and-robots-scaling-laws-for-agents/)

---

**Link** 2024\-11\-18 [Qwen: Extending the Context Length to 1M Tokens](http://qwenlm.github.io/blog/qwen2.5-turbo/):

The new Qwen2\.5\-Turbo boasts a million token context window (up from 128,000 for Qwen 2\.5\) and faster performance:

> Using sparse attention mechanisms, we successfully reduced the time to first token for processing a context of 1M tokens from 4\.9 minutes to 68 seconds, achieving a 4\.3x speedup.

The benchmarks they've published look impressive, including a 100% score on the 1M\-token passkey retrieval task (not the first model to achieve this).

There's a catch: unlike previous models in the Qwen 2\.5 series it looks like this one hasn't been released as open weights: it's available exclusively via their (inexpensive) paid API \- for which it looks like you may need a \+86 Chinese phone number.

---

**Link** 2024\-11\-18 [Pixtral Large](https://mistral.ai/news/pixtral-large/):

New today from Mistral:

> Today we announce Pixtral Large, a 124B open\-weights multimodal model built on top of Mistral Large 2\. Pixtral Large is the second model in our multimodal family and demonstrates frontier\-level image understanding.

The weights are out [on Hugging Face](https://huggingface.co/mistralai/Pixtral-Large-Instruct-2411) (over 200GB to download, and you'll need a hefty GPU rig to run them). The license is free for academic research but you'll need to pay for commercial usage.

The new Pixtral Large model is available through their API, as models called `pixtral-large-2411` and `pixtral-large-latest`.

Here's how to run it using [LLM](https://llm.datasette.io/) and the [llm\-mistral](https://github.com/simonw/llm-mistral) plugin:

```
llm install -U llm-mistral
llm keys set mistral
# paste in API key
llm mistral refresh
llm -m mistral/pixtral-large-latest describe -a https://static.simonwillison.net/static/2024/pelicans.jpg

```

> The image shows a large group of birds, specifically pelicans, congregated together on a rocky area near a body of water. These pelicans are densely packed together, some looking directly at the camera while others are engaging in various activities such as preening or resting. Pelicans are known for their large bills with a distinctive pouch, which they use for catching fish. The rocky terrain and the proximity to water suggest this could be a coastal area or an island where pelicans commonly gather in large numbers. The scene reflects a common natural behavior of these birds, often seen in their nesting or feeding grounds.

[![A photo I took of some pelicans](https://substackcdn.com/image/fetch/$s_!ht20!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe37e9bc2-2426-461a-b124-e2a5a1323465_512x384.jpeg "A photo I took of some pelicans")](https://substackcdn.com/image/fetch/$s_!ht20!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe37e9bc2-2426-461a-b124-e2a5a1323465_512x384.jpeg)

**Update:** I released [llm\-mistral 0\.8](https://github.com/simonw/llm-mistral/releases/tag/0.8) which adds [async model support](https://simonwillison.net/2024/Nov/17/llm-018/) for the full Mistral line, plus a new `llm -m mistral-large` shortcut alias for the Mistral Large model.

---

**Link** 2024\-11\-19 [Security means securing people where they are](https://blog.yossarian.net/2024/11/18/Security-means-securing-people-where-they-are):

William Woodruff is an Engineering Director at Trail of Bits who worked on the recent PyPI [digital attestations project](https://simonwillison.net/2024/Nov/14/pypi-digital-attestations/).

That feature is based around open standards but launched with an implementation against GitHub, which resulted in push back (and even some conspiracy theories) that PyPI were deliberately favoring GitHub over other platforms.

William argues here for pragmatism over ideology:

> Being serious about security at scale means **meeting users where they are**. In practice, this means deciding how to divide a **limited pool of engineering resources** such that the **largest demographic of users benefits** from a security initiative. This results in a **fundamental bias** towards institutional and pre\-existing services, since the average user belongs to these institutional services and does not personally particularly care about security. Participants in open source **can and should** work to counteract this institutional bias, but doing so as a matter of **ideological purity undermines our shared security interests.**

---

**Link** 2024\-11\-19 [Preview: Gemini API Additional Terms of Service](https://ai.google.dev/gemini-api/terms_preview):

Google sent out an email last week linking to this preview of upcoming changes to the Gemini API terms. Key paragraph from that email:

> To maintain a safe and responsible environment for all users, we're enhancing our [abuse monitoring](https://ai.google.dev/gemini-api/docs/abuse-monitoring) practices for Google AI Studio and Gemini API. Starting **December 13, 2024**, Gemini API will log prompts and responses for Paid Services, as described in the terms. These logs are only retained for a limited time (55 days) and are used solely to detect abuse and for required legal or regulatory disclosures. These logs are not used for model training. Logging for abuse monitoring is standard practice across the global AI industry. You can [preview](https://ai.google.dev/gemini-api/terms_preview) the updated Gemini API Additional Terms of Service, effective December 13, 2024\.

That "for required legal or regulatory disclosures" piece makes it sound like somebody could subpoena Google to gain access to your logged Gemini API calls.

It's not clear to me if this is a change from their current policy though, other than the number of days of log retention increasing from 30 to 55 (and I'm having trouble finding that 30 day number written down anywhere.)

That same email also announced the deprecation of the older Gemini 1\.0 Pro model:

> Gemini 1\.0 Pro will be discontinued on **February 15, 2025**.

---

**Link** 2024\-11\-19 [Understanding the BM25 full text search algorithm](https://emschwartz.me/understanding-the-bm25-full-text-search-algorithm/):

Evan Schwartz provides a deep dive explanation of how the classic BM25 search relevance scoring function works, including a very useful breakdown of the mathematics it uses.

---

**Link** 2024\-11\-19 [Using uv with PyTorch](https://docs.astral.sh/uv/guides/integration/pytorch/):

PyTorch is a notoriously tricky piece of Python software to install, due to the need to provide separate wheels for different combinations of Python version and GPU accelerator (e.g. different CUDA versions).

uv now has dedicated documentation for PyTorch which I'm finding really useful \- it clearly explains the challenge and then shows exactly how to configure a `pyproject.toml` such that `uv` knows which version of each package it should install from where.

---

**Link** 2024\-11\-19 [OpenStreetMap vector tiles demo](https://pnorman.github.io/tilekiln-shortbread-demo/#9.23/37.5982/-122.2625):

Long\-time OpenStreetMap developer [Paul Norman](https://www.paulnorman.ca/) has been working on adding vector tile support to OpenStreetMap for [quite a while](https://community.openstreetmap.org/t/minutely-updated-vector-tiles-demo/110121). Paul [recently announced](https://community.openstreetmap.org/t/vector-tiles-on-osmf-hardware/121501) that `vector.openstreetmap.org` is now serving vector tiles (in [Mapbox Vector Tiles (MVT) format](https://github.com/mapbox/vector-tile-spec)) \- here's his interactive demo for seeing what they look like.

---

**Link** 2024\-11\-20 [Bluesky WebSocket Firehose](https://tools.simonwillison.net/bluesky-firehose):

Very quick (10 seconds [of Claude hacking](https://gist.github.com/simonw/15ee25c9cc52b40e0733f2f889c1e873)) prototype of a web page that attaches to the public Bluesky WebSocket firehose and displays the results directly in your browser.

Here's [the code](https://github.com/simonw/tools/blob/main/bluesky-firehose.html) \- there's very little to it, it's basically opening a connection to `wss://jetstream2.us-east.bsky.network/subscribe?wantedCollections=app.bsky.feed.post` and logging out the results to a `<textarea readonly>` element.

[![](https://substackcdn.com/image/fetch/$s_!st-D!,w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0645d20e-522b-4ff0-bd41-c53783599b8b_527x548.gif)](https://substackcdn.com/image/fetch/$s_!st-D!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0645d20e-522b-4ff0-bd41-c53783599b8b_527x548.gif)

Bluesky's [Jetstream](https://docs.bsky.app/blog/jetstream) isn't their main atproto firehose \- that's a more complicated protocol involving CBOR data and CAR files. Jetstream is a new Go proxy ([source code here](https://github.com/bluesky-social/jetstream)) that provides a subset of that firehose over WebSocket.

Jetstream was built by Bluesky developer Jaz, initially as a side\-project, in response to the surge of traffic they received back in September when Brazil banned Twitter. See [Jetstream: Shrinking the AT Proto Firehose by \>99%](https://jazco.dev/2024/09/24/jetstream/) for their description of the project when it first launched.

The API scene growing around Bluesky is *really exciting* right now. Twitter's API is so expensive it may as well not exist, and Mastodon's community have pushed back against many potential uses of the Mastodon API as incompatible with that community's value system.

Hacking on Bluesky feels reminiscent of the massive diversity of innovation we saw around Twitter back in the late 2000s and early 2010s.

Here's a much more fun Bluesky demo by Theo Sanderson: [firehose3d.theo.io](https://firehose3d.theo.io/) ([source code here](https://github.com/theosanderson/firehose)) which displays the firehose from that same WebSocket endpoint in the style of a Windows XP screensaver.

---

**Link** 2024\-11\-20 [Foursquare Open Source Places: A new foundational dataset for the geospatial community](https://location.foursquare.com/resources/blog/products/foursquare-open-source-places-a-new-foundational-dataset-for-the-geospatial-community/):

I did not expect this!

> \[...] we are announcing today the general availability of a foundational open data set, Foursquare Open Source Places ("FSQ OS Places"). This base layer of 100mm\+ global places of interest ("POI") includes 22 core attributes (see schema [here](https://docs.foursquare.com/data-products/docs/places-os-data-schema)) that will be updated monthly and available for commercial use under the Apache 2\.0 license framework.

The data is available [as Parquet files](https://docs.foursquare.com/data-products/docs/access-fsq-os-places) hosted on Amazon S3\.

Here's how to list the available files:

```
aws s3 ls s3://fsq-os-places-us-east-1/release/dt=2024-11-19/places/parquet/

```

I got back `places-00000.snappy.parquet` through `places-00024.snappy.parquet`, each file around 455MB for a total of 10\.6GB of data.

I ran `duckdb` and then used DuckDB's ability to remotely query Parquet on S3 to explore the data a bit more without downloading it to my laptop first:

```
select count(*) from 's3://fsq-os-places-us-east-1/release/dt=2024-11-19/places/parquet/places-00000.snappy.parquet';

```

This got back 4,180,424 \- that number is similar for each file, suggesting around 104,000,000 records total.

The I ran this query to retrieve 1,000 places from that first file as newline\-delimited JSON:

```
copy (
    select * from 's3://fsq-os-places-us-east-1/release/dt=2024-11-19/places/parquet/places-00000.snappy.parquet'
    limit 1000
) to '/tmp/places.json';

```

Here's [that places.json file](https://gist.github.com/simonw/53ad57ad42c7efe75e2028d975907180), and here it is [imported into Datasette Lite](https://lite.datasette.io/?json=https://gist.github.com/simonw/53ad57ad42c7efe75e2028d975907180#/data/raw).

Finally, I got ChatGPT Code Interpreter to [convert that file to GeoJSON](https://chatgpt.com/share/673d7b92-0b4c-8006-a442-c5e6c2713d9c) and pasted the result [into this Gist](https://gist.github.com/simonw/1e2a170b7368932ebd3922cb5d234924), giving me a map of those thousand places (because Gists automatically render GeoJSON):

[![A map of the world with 1000 markers on it. A marker in Columbia shows a dialog for Raisbeck, Bogota Dv, Cra 47 A 114 05 Second Floor](https://substackcdn.com/image/fetch/$s_!pRUA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcacb3d66-b57d-439d-afaf-a0beaa3a78b8_2020x1136.jpeg "A map of the world with 1000 markers on it. A marker in Columbia shows a dialog for Raisbeck, Bogota Dv, Cra 47 A 114 05 Second Floor")](https://substackcdn.com/image/fetch/$s_!pRUA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcacb3d66-b57d-439d-afaf-a0beaa3a78b8_2020x1136.jpeg)

---

**Quote** 2024\-11\-21

> *When we started working on what became NotebookLM in the summer of 2022, we could fit about 1,500 words in the context window. Now we can fit up to 1\.5 million words. (And using various other tricks, effectively fit 25 million words.) The emergence of long context models is, I believe, the single most unappreciated AI development of the past two years, at least among the general public. It radically transforms the utility of these models in terms of actual, practical applications.*

[Steven Johnson](https://adjacentpossible.substack.com/p/in-the-context-of-long-context)

---