# What's new in the world of LLMs, for NICAR 2025

*Plus Mistral OCR and my cutting-edge web scraping techniques workshop*

Published: 2025-03-09
Source: https://simonw.substack.com/p/whats-new-in-the-world-of-llms-for

---

In this newsletter:

* What's new in the world of LLMs, for NICAR 2025

Plus 12 links and 1 TIL

### [What's new in the world of LLMs, for NICAR 2025](https://simonwillison.net/2025/Mar/8/nicar-llms/) \- 2025\-03\-08

I presented two sessions at the [NICAR 2025](https://www.ire.org/training/conferences/nicar-2025/) data journalism conference this year. The first was this one based on my [review of LLMs in 2024](https://simonwillison.net/2024/Dec/31/llms-in-2024/), extended by several months to cover everything that's happened in 2025 so far. The second was a workshop on [Cutting\-edge web scraping techniques](https://simonwillison.net/2025/Mar/8/cutting-edge-web-scraping/), which I've written up separately.

Here are the slides and detailed notes from my review of what's new in LLMs, with a focus on trends that are relative to data journalism.

[![What's new in the world of LLMs
Simon Willison
NICAR 2025, 7th March 2025](https://substackcdn.com/image/fetch/$s_!lRJW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7190891b-eb93-4942-82ab-68e0ce084f49_1920x1080.jpeg "What's new in the world of LLMs
Simon Willison
NICAR 2025, 7th March 2025")](https://substackcdn.com/image/fetch/$s_!lRJW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7190891b-eb93-4942-82ab-68e0ce084f49_1920x1080.jpeg)

The full set of slides and notes is too long for email, [read that here instead](https://simonwillison.net/2025/Mar/8/nicar-llms/).

#### Talk to me about your newsroom

If you work in a newsroom that is figuring this stuff out I would love to jump on a Zoom call and talk to your team. Contact me at `swillison@` Google's webmail provider.

---

**Link** 2025\-03\-05 [QwQ\-32B: Embracing the Power of Reinforcement Learning](https://qwenlm.github.io/blog/qwq-32b/):

New Apache 2 licensed reasoning model from Qwen:

> We are excited to introduce QwQ\-32B, a model with 32 billion parameters that achieves performance comparable to DeepSeek\-R1, which boasts 671 billion parameters (with 37 billion activated). This remarkable outcome underscores the effectiveness of RL when applied to robust foundation models pretrained on extensive world knowledge.

I had a lot of fun [trying out](https://simonwillison.net/2024/Nov/27/qwq/) their previous QwQ reasoning model last November. I’ve now tried the new model and it’s very impressive \- I ran it using Ollama.

LM Studio [released GGUFs](https://huggingface.co/lmstudio-community/QwQ-32B-GGUF/tree/main) ranging in size from 17\.2 to 34\.8 GB. MLX have compatible weights published in [3bit](https://huggingface.co/mlx-community/QwQ-32B-3bit), [4bit](https://huggingface.co/mlx-community/QwQ-32B-4bit), [6bit](https://huggingface.co/mlx-community/QwQ-32B-6bit) and [8bit](https://huggingface.co/mlx-community/QwQ-32B-8bit). Ollama [has the new qwq](https://ollama.com/library/qwq) too \- it looks like they've renamed the previous November release [qwq:32b\-preview](https://ollama.com/library/qwq:32b-preview-q8_0).

---

**Link** 2025\-03\-05 [Career Update: Google DeepMind \-\> Anthropic](https://nicholas.carlini.com/writing/2025/career-update.html):

Nicholas Carlini ([previously](https://simonwillison.net/tags/nicholas-carlini/)) on joining Anthropic, driven partly by his frustration at friction he encountered publishing his research at Google DeepMind after their merge with Google Brain. His area of expertise is adversarial machine learning.

> The recent advances in machine learning and language modeling are going to be transformative \[[d](https://nicholas.carlini.com/writing/2025/career-update.html#footnote4)] But in order to realize this potential future in a way that doesn't put everyone's safety and security at risk, we're going to need to make a *lot* of progress\-\-\-and soon. We need to make so much progress that no one organization will be able to figure everything out by themselves; we need to work together, we need to talk about what we're doing, and we need to start doing this now.

---

**Link** 2025\-03\-05 [Demo of ChatGPT Code Interpreter running in o3\-mini\-high](https://chatgpt.com/share/67c8c374-8c08-8006-8ce3-042308063792):

OpenAI made GPT\-4\.5 available to Plus ($20/month) users today. I was [a little disappointed](https://simonwillison.net/2025/Feb/27/introducing-gpt-45/) with GPT\-4\.5 when I tried it through the API, but having access in the ChatGPT interface meant I could use it with existing tools such as Code Interpreter which made its strengths [a whole lot more evident](https://chatgpt.com/share/67c8a7b6-655c-8006-a100-bc04080e5aa1) \- that’s a transcript where I had it design and test its own version of the JSON Schema succinct DSL I published [last week](https://simonwillison.net/2025/Feb/28/llm-schemas/#designing-this-feature-for-llm).

Riley Goodside [then spotted](https://x.com/goodside/status/1897412604894789692) that Code Interpreter has been quietly enabled for other models too, including the excellent o3\-mini reasoning model. This means you can have o3\-mini reason about code, write that code, test it, iterate on it and keep going until it gets something that works.

[![Screenshot showing ChatGPT 03-mini-high - my prompt: Use your Python tool to show me the versions of Python and SQLite. Reasoned about Python and SQLite versions for a couple of seconds Below is the Python code used to print both the Python and SQLite versions: Python Code import sys import sqlite3 print("Python version:" print ("SQLite version:" Result Python version: 3.11.8 main, Mar 12 2024, 11:41:52) GCC 12.2.01° SQLite version: 3.40.1](https://substackcdn.com/image/fetch/$s_!xltI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F10c5f632-5c97-4787-bac9-7f6ad859d451_1174x1612.jpeg "Screenshot showing ChatGPT 03-mini-high - my prompt: Use your Python tool to show me the versions of Python and SQLite. Reasoned about Python and SQLite versions for a couple of seconds Below is the Python code used to print both the Python and SQLite versions: Python Code import sys import sqlite3 print(\"Python version:\" print (\"SQLite version:\" Result Python version: 3.11.8 main, Mar 12 2024, 11:41:52) GCC 12.2.01° SQLite version: 3.40.1")](https://substackcdn.com/image/fetch/$s_!xltI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F10c5f632-5c97-4787-bac9-7f6ad859d451_1174x1612.jpeg)

Code Interpreter remains my favorite implementation of the "coding agent" pattern, despite recieving very few upgrades in the two years after its initial release. Plugging much stronger models into it than the previous GPT\-4o default makes it even more useful.

Nothing about this in the [ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) yet, but I've tested it in the ChatGPT iOS app and mobile web app and it definitely works there.

---

**Link** 2025\-03\-05 [The Graphing Calculator Story](https://www.pacifict.com/story/):

Utterly delightful story from Ron Avitzur in 2004 about the origins of the Graphing Calculator app that shipped with many versions of macOS. Ron's contract with Apple had ended but his badge kept working so he kept on letting himself in to work on the project. He even grew a small team:

> I asked my friend Greg Robbins to help me. His contract in another division at Apple had just ended, so he told his manager that he would start reporting to me. She didn't ask who I was and let him keep his office and badge. In turn, I told people that I was reporting to him. Since that left no managers in the loop, we had no meetings and could be extremely productive

---

**Link** 2025\-03\-06 [Aider: Using uv as an installer](https://aider.chat/2025/01/15/uv.html):

Paul Gauthier has an innovative solution for the challenge of helping end users get a copy of his Aider CLI Python utility installed in an isolated virtual environment without first needing to teach them what an "isolated virtual environment" is.

Provided you already have a Python install of version 3\.8 or higher you can run this:

```
pip install aider-install && aider-install
```

The [aider\-install](https://pypi.org/project/aider-install/) package itself depends on [uv](https://github.com/astral-sh/uv). When you run `aider-install` it executes the following [Python code](https://github.com/Aider-AI/aider-install/blob/main/aider_install/main.py):

```
def install_aider():
    try:
        uv_bin = uv.find_uv_bin()
        subprocess.check_call([
            uv_bin, "tool", "install", "--force", "--python", "python3.12", "aider-chat@latest"
        ])
        subprocess.check_call([uv_bin, "tool", "update-shell"])
    except subprocess.CalledProcessError as e:
        print(f"Failed to install aider: {e}")
        sys.exit(1)
```

This first figures out the location of the `uv` Rust binary, then uses it to install his [aider\-chat](https://pypi.org/project/aider-chat/) package by running the equivalent of this command:

```
uv tool install --force --python python3.12 aider-chat@latest
```

This will in turn install a brand new standalone copy of Python 3\.12 and tuck it away in uv's own managed directory structure where it shouldn't hurt anything else.

The `aider-chat` script defaults to being dropped in the XDG standard directory, which is probably `~/.local/bin` \- see [uv's documentation](https://docs.astral.sh/uv/concepts/tools/#the-bin-directory). The [\-\-force flag](https://docs.astral.sh/uv/concepts/tools/#overwriting-executables) ensures that `uv` will overwrite any previous attempts at installing `aider-chat` in that location with the new one.

Finally, running `uv tool update-shell` ensures that bin directory is [on the user's PATH](https://docs.astral.sh/uv/concepts/tools/#the-path).

I *think* I like this. There is a LOT of stuff going on here, and experienced users may well opt for an [alternative installation mechanism](https://aider.chat/docs/install.html).

But for non\-expert Python users who just want to start using Aider, I think this pattern represents quite a tasteful way of getting everything working with minimal risk of breaking the user's system.

**Update**: Paul [adds](https://twitter.com/paulgauthier/status/1897486573857595877):

> Offering this install method dramatically reduced the number of GitHub issues from users with conflicted/broken python environments.
> 
> I also really like the "curl \| sh" aider installer based on uv. Even users who don't have python installed can use it.

---

**Link** 2025\-03\-06 [Will the future of software development run on vibes?](https://arstechnica.com/ai/2025/03/is-vibe-coding-with-ai-gnarly-or-reckless-maybe-some-of-both/):

I got a few quotes in this piece by Benj Edwards about **vibe coding**, the term Andrej Karpathy [coined](https://simonwillison.net/2025/Feb/6/andrej-karpathy/) for when you prompt an LLM to write code, accept all changes and keep feeding it prompts and error messages and see what you can get it to build.

Here's what I originally sent to Benj:

> I really enjoy vibe coding \- it's a fun way to play with the limits of these models. It's also useful for prototyping, where the aim of the exercise is to try out an idea and prove if it can work.
> 
> Where vibe coding fails is in producing maintainable code for production settings. I firmly believe that as a developer you have to take accountability for the code you produce \- if you're going to put your name to it you need to be confident that you understand how and why it works \- ideally to the point that you can explain it to somebody else.
> 
> Vibe coding your way to a production codebase is clearly a terrible idea. Most of the work we do as software engineers is about evolving existing systems, and for those the quality and understandability of the underlying code is crucial.
> 
> For experiments and low\-stake projects where you want to explore what's possible and build fun prototypes? Go wild! But stay aware of the very real risk that a good enough prototype often faces pressure to get pushed to production.
> 
> If an LLM wrote every line of your code but you've reviewed, tested and understood it all, that's not vibe coding in my book \- that's using an LLM as a typing assistant.

---

**Link** 2025\-03\-06 [monolith](https://github.com/Y2Z/monolith):

Neat CLI tool built in Rust that can create a single packaged HTML file of a web page plus all of its dependencies.

```
cargo install monolith # or brew install
monolith https://simonwillison.net/ > simonwillison.html
```

That command produced [this 1\.5MB single file result](https://static.simonwillison.net/static/2025/simonwillison.html). All of the linked images, CSS and JavaScript assets have had their contents inlined into base64 URIs in their `src=` and `href=` attributes.

I was intrigued as to how it works, so I dumped the whole repository into Gemini 2\.0 Pro and asked for an architectural summary:

```
cd /tmp
git clone https://github.com/Y2Z/monolith
cd monolith
files-to-prompt . -c | llm -m gemini-2.0-pro-exp-02-05 \
  -s 'architectural overview as markdown'
```

Here's [what I got](https://gist.github.com/simonw/2c80749935ae3339d6f7175dc7cf325b). Short version: it uses the `reqwest`, `html5ever`, `markup5ever_rcdom` and `cssparser` crates to fetch and parse HTML and CSS and extract, combine and rewrite the assets. It doesn't currently attempt to run any JavaScript.

---

**Link** 2025\-03\-07 [Mistral OCR](https://mistral.ai/fr/news/mistral-ocr):

New closed\-source specialist OCR model by Mistral \- you can feed it images or a PDF and it produces Markdown with optional embedded images.

It's available [via their API](https://docs.mistral.ai/api/#tag/ocr), or it's "available to self\-host on a selective basis" for people with stringent privacy requirements who are willing to talk to their sales team.

I decided to try out their API, so I copied and pasted example code [from their notebook](https://colab.research.google.com/drive/11NdqWVwC_TtJyKT6cmuap4l9SryAeeVt?usp=sharing) into my [custom Claude project](https://simonwillison.net/2024/Dec/19/one-shot-python-tools/) and [told it](https://claude.ai/share/153d8eb8-82dd-4f8c-a3d0-6c23b4dc21a2):

> `Turn this into a CLI app, depends on mistralai - it should take a file path and an optional API key defauling to env vironment called MISTRAL_API_KEY`

After [some further](https://claude.ai/share/b746cab4-293b-4e04-b662-858bb164ab78) iteration / vibe coding I got to something that worked, which I then tidied up and shared as [mistral\_ocr.py](https://github.com/simonw/tools/blob/main/python/mistral_ocr.py).

You can try it out like this:

```
export MISTRAL_API_KEY='...'
uv run http://tools.simonwillison.net/python/mistral_ocr.py \
  mixtral.pdf --html --inline-images > mixtral.html
```

I fed in [the Mixtral paper](https://arxiv.org/abs/2401.04088) as a PDF. The API returns Markdown, but my `--html` option renders that Markdown as HTML and the `--inline-images` option takes any images and inlines them as base64 URIs (inspired [by monolith](https://simonwillison.net/2025/Mar/6/monolith/)). The result is [mixtral.html](https://static.simonwillison.net/static/2025/mixtral.html), a 972KB HTML file with images and text bundled together.

This did a pretty great job!

[![Screenshot of part of the document, it has a heading, some text, an image and the start of a table. The table contains some unrendered MathML syntax.](https://substackcdn.com/image/fetch/$s_!Ec5B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F246ce5de-c826-4477-b3f3-975fdecb269c_1730x1708.jpeg "Screenshot of part of the document, it has a heading, some text, an image and the start of a table. The table contains some unrendered MathML syntax.")](https://substackcdn.com/image/fetch/$s_!Ec5B!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F246ce5de-c826-4477-b3f3-975fdecb269c_1730x1708.jpeg)

My script renders Markdown tables but I haven't figured out how to render inline Markdown MathML yet. I ran the command a second time and requested Markdown output (the default) like this:

```
uv run http://tools.simonwillison.net/python/mistral_ocr.py \
  mixtral.pdf > mixtral.md
```

Here's [that Markdown rendered as a Gist](https://gist.github.com/simonw/023d1cf403c1cd9f41801c85510aef21) \- there are a few MathML glitches so clearly the Mistral OCR MathML dialect and the GitHub Formatted Markdown dialect don't quite line up.

My tool can also output raw JSON as an alternative to Markdown or HTML \- full details [in the documentation](https://tools.simonwillison.net/python/#mistral_ocrpy).

The Mistral API is priced at roughly 1000 pages per dollar, with a 50% discount for batch usage.

The big question with LLM\-based OCR is always how well it copes with accidental instructions in the text (can you safely OCR a document full of prompting examples?) and how well it handles text it can't write.

Mistral's Sophia Yang says it ["should be robust"](https://x.com/sophiamyang/status/1897719199595720722) against following instructions in the text, and invited people to try and find counter\-examples.

Alexander Doria noted that [Mistral OCR can hallucinate text](https://twitter.com/Dorialexander/status/1897702264543875535) when faced with handwriting that it cannot understand.

---

**Link** 2025\-03\-07 [State\-of\-the\-art text embedding via the Gemini API](https://developers.googleblog.com/en/gemini-embedding-text-model-now-available-gemini-api/):

Gemini just released their new text embedding model, with the snappy name `gemini-embedding-exp-03-07`. It supports 8,000 input tokens \- up from 3,000 \- and outputs vectors that are a lot larger than their previous `text-embedding-004` model \- that one output size 768 vectors, the new model outputs 3072\.

Storing that many floating point numbers for each embedded record can use a lot of space. thankfully, the new model supports Matryoshka Representation Learning \- this means you can simply truncate the vectors to trade accuracy for storage.

I added support for the new model in [llm\-gemini 0\.14](https://github.com/simonw/llm-gemini/releases/tag/0.14). LLM doesn't yet have direct support for Matryoshka truncation so I instead registered different truncated sizes of the model under different IDs: `gemini-embedding-exp-03-07-2048`, `gemini-embedding-exp-03-07-1024`, `gemini-embedding-exp-03-07-512`, `gemini-embedding-exp-03-07-256`, `gemini-embedding-exp-03-07-128`.

The model is currently free while it is in preview, but comes with [a strict rate limit](https://ai.google.dev/gemini-api/docs/rate-limits#current-rate-limits) \- 5 requests per minute and just 100 requests a day. I quickly tripped those limits while testing out the new model \- I hope they can bump those up soon.

---

**Link** 2025\-03\-08 [Apple Is Delaying the ‘More Personalized Siri’ Apple Intelligence Features](https://daringfireball.net/2025/03/apple_is_delaying_the_more_personalized_siri_apple_intelligence_features):

Apple told John Gruber (and other Apple press) this about the new "personalized" Siri:

> It’s going to take us longer than we thought to deliver on these features and we anticipate rolling them out in the coming year.

I have a hunch that this delay might relate to security.

These new Apple Intelligence features involve Siri responding to requests to access information in applications and then perform actions on the user's behalf.

This is the worst possible combination for [prompt injection](https://simonwillison.net/tags/prompt-injection/) attacks! Any time an LLM\-based system has access to private data, tools it can call and exposure to potentially malicious instructions (like emails and text messages from untrusted strangers) there's a significant risk that an attacker might subvert those tools and use them to damage or exfiltration a user's data.

I published [this piece](https://simonwillison.net/2023/Nov/27/prompt-injection-explained/) about the risk of prompt injection to personal digital assistants back in November 2023, and nothing has changed since then to make me think this is any less of an open problem.

---

**Link** 2025\-03\-08 [Politico: 5 Questions for Jack Clark](https://www.politico.com/newsletters/digital-future-daily/2025/03/07/5-questions-for-jack-clark-00218274):

I tend to ignore statements with this much future\-facing hype, especially when they come from AI labs who are both raising money and trying to [influence US technical policy](https://www.anthropic.com/news/anthropic-s-recommendations-ostp-u-s-ai-action-plan).

Anthropic's Jack Clark has an excellent [long\-running newsletter](https://jack-clark.net/) which causes me to take him more seriously than many other sources.

Jack [says](https://twitter.com/jackclarksf/status/1898392567215219199):

> In 2025 myself and @AnthropicAI will be more forthright about our views on AI, especially the speed with which powerful things are arriving.

In response to Politico's question "What’s one underrated big idea?" Jack replied:

> People underrate how significant and fast\-moving AI progress is. We have this notion that in late 2026, or early 2027, powerful AI systems will be built that will have intellectual capabilities that match or exceed Nobel Prize winners. They’ll have the ability to navigate all of the interfaces… they will have the ability to autonomously reason over kind of complex tasks for extended periods. They’ll also have the ability to interface with the physical world by operating drones or robots. Massive, powerful things are beginning to come into view, and we’re all underrating how significant that will be.

---

**Link** 2025\-03\-08 [Cutting\-edge web scraping techniques at NICAR](https://github.com/simonw/nicar-2025-scraping/blob/main/README.md):

Here's the handout for a workshop I presented this morning at [NICAR 2025](https://www.ire.org/training/conferences/nicar-2025/) on web scraping, focusing on lesser know tips and tricks that became possible only with recent developments in LLMs.

For workshops like this I like to work off an extremely detailed handout, so that people can move at their own pace or catch up later if they didn't get everything done.

The workshop consisted of four parts:

> 1. Building a [Git scraper](https://simonwillison.net/2020/Oct/9/git-scraping/) \- an automated scraper in GitHub Actions that records changes to a resource over time
> 2. Using in\-browser JavaScript and then [shot\-scraper](https://shot-scraper.datasette.io/) to extract useful information
> 3. Using [LLM](https://llm.datasette.io/) with both OpenAI and Google Gemini to extract structured data from unstructured websites
> 4. [Video scraping](https://simonwillison.net/2024/Oct/17/video-scraping/) using [Google AI Studio](https://aistudio.google.com/)

I released several new tools in preparation for this workshop (I call this "NICAR Driven Development"):

* [git\-scraper\-template](https://github.com/simonw/git-scraper-template) template repository for quickly setting up new Git scrapers, which I [wrote about here](https://simonwillison.net/2025/Feb/26/git-scraper-template/)
* [LLM schemas](https://simonwillison.net/2025/Feb/28/llm-schemas/), finally adding structured schema support to my LLM tool
* [shot\-scraper har](https://shot-scraper.datasette.io/en/stable/har.html) for archiving pages as HTML Archive files \- though I cut this from the workshop for time

I also came up with a fun way to distribute API keys for workshop participants: I [had Claude build me](https://claude.ai/share/8d3330c8-7fd4-46d1-93d4-a3bd05915793) a web page where I can create an encrypted message with a passphrase, then share a URL to that page with users and give them the passphrase to unlock the encrypted message. You can try that at [tools.simonwillison.net/encrypt](https://tools.simonwillison.net/encrypt) \- or [use this link](https://tools.simonwillison.net/encrypt#5ZeXCdZ5pqCcHqE1y0aGtoIijlUW+ipN4gjQV4A2/6jQNovxnDvO6yoohgxBIVWWCN8m6ppAdjKR41Qzyq8Keh0RP7E=) and enter the passphrase "demo":

[![Screenshot of a message encryption/decryption web interface showing the title "Encrypt / decrypt message" with two tab options: "Encrypt a message" and "Decrypt a message" (highlighted). Below shows a decryption form with text "This page contains an encrypted message", a passphrase input field with dots, a blue "Decrypt message" button, and a revealed message saying "This is a secret message".](https://substackcdn.com/image/fetch/$s_!75Fj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F53c880ef-33f5-4001-b123-7db767c4282f_896x1046.jpeg "Screenshot of a message encryption/decryption web interface showing the title \"Encrypt / decrypt message\" with two tab options: \"Encrypt a message\" and \"Decrypt a message\" (highlighted). Below shows a decryption form with text \"This page contains an encrypted message\", a passphrase input field with dots, a blue \"Decrypt message\" button, and a revealed message saying \"This is a secret message\".")](https://substackcdn.com/image/fetch/$s_!75Fj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F53c880ef-33f5-4001-b123-7db767c4282f_896x1046.jpeg)

---

**TIL** 2025\-03\-08 [Running jupyterlab via uv tool install](https://til.simonwillison.net/jupyter/jupyterlab-uv-tool-install):

I tried to get [jupyterlab](https://jupyter.org/install) working via `uv tool install` today and ran into some sharp edges. …

---