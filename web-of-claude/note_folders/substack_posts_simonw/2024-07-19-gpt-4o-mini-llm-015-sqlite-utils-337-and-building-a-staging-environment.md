# GPT-4o mini, LLM 0.15, sqlite-utils 3.37 and building a staging environment

*Plus Mistral NeMo, Codestral Mamba and Llama-3-Groq-Tool-Use Models*

Published: 2024-07-19
Source: https://simonw.substack.com/p/gpt-4o-mini-llm-015-sqlite-utils

---

In this newsletter:

* GPT\-4o mini, LLM 0\.15, sqlite\-utils 3\.37 and building a staging environment

Plus 15 links and 3 quotations

### **[GPT\-4o mini, LLM 0\.15, sqlite\-utils 3\.37 and building a staging environment](https://simonwillison.net/2024/Jul/19/weeknotes/) \- 2024\-07\-19**

Upgrades to [LLM](https://llm.datasette.io/) to support the latest models, and a whole bunch of invisible work building out a staging environment for Datasette Cloud.

#### **GPT\-4o mini and LLM 0\.15**

Today's big news was the release of [GPT\-4o mini](https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/), which I [wrote about here](https://simonwillison.net/2024/Jul/18/gpt-4o-mini/). If you build applications on top of LLMs this is a very significant release \- it's the cheapest of the high performing hosted models (cheaper even than Claude 3 Haiku and Gemini 1\.5 Flash) and has some notable characteristics, most importantly the 16,000 token output limit.

I shipped a [new LLM release](https://simonwillison.net/2024/Jul/18/llm-015/) to support the new model. Full release notes for [LLM 0\.15](https://llm.datasette.io/en/stable/changelog.html#v0-15):

> * Support for OpenAI's [new GPT\-4o mini](https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/) model: `llm -m gpt-4o-mini 'rave about pelicans in French'`[\#536](https://github.com/simonw/llm/issues/536)
> * `gpt-4o-mini` is now the default model if you do not [specify your own default](https://llm.datasette.io/en/stable/setup.html#setting-a-custom-default-model), replacing GPT\-3\.5 Turbo. GPT\-4o mini is both cheaper and better than GPT\-3\.5 Turbo.
> * Fixed a bug where `llm logs -q 'flourish' -m haiku` could not combine both the `-q` search query and the `-m` model specifier. [\#515](https://github.com/simonw/llm/issues/515)

#### **sqlite\-utils 3\.37**

LLM had a frustrating bug involving [a weird numpy issue](https://github.com/simonw/llm/issues/531) that only manifested on LLM when installed via Homebrew. I ended up fixing that in its `sqlite-utils` dependency \- here are the full release notes for [sqlite\-utils 3\.37](https://sqlite-utils.datasette.io/en/stable/changelog.html#v3-37):

> * The `create-table` and `insert-files`commands all now accept multiple `--pk` options for compound primary keys. ([\#620](https://github.com/simonw/sqlite-utils/issues/620))
> * Now tested against Python 3\.13 pre\-release. ([\#619](https://github.com/simonw/sqlite-utils/pull/619))
> * Fixed a crash that can occur in environments with a broken `numpy`installation, producing a `module 'numpy' has no attribute 'int8'`. ([\#632](https://github.com/simonw/sqlite-utils/issues/632))

#### **Datasette Cloud staging environment**

I'm a big believer in reducing the friction involved in making changes to code. The main reason I'm so keen on the combination of automated tests, GitHub Actions for CI/CD and extensive documentation (as described in [Coping strategies for the serial project hoarder](https://simonwillison.net/2022/Nov/26/productivity/)) is that

Sadly, [Datasette Cloud](https://www.datasette.cloud/) hasn't been living up these standards as much as I would like. I have great comprehensive tests for it, continuous deployment that deploys when those tests pass and pretty solid internal documentation (mainly spread out across dozens of GitHub Issues) \- but the thing I've been missing is a solid staging environment.

This matters because a lot of the most complex code in Datasette Cloud involves deploying new instances of Datasette to [Fly Machines](https://fly.io/docs/machines/). The thing that's been missing is a separate environment where I can exercise my Fly deployment code independently of the production cluster.

I've been working towards this over the past week, and in doing so have found all sorts of pieces of the codebase that are hard\-coded in a way that needs to be unwrapped to correctly support that alternative environment.

I'm getting there, but it's been one of those frustrating projects where every step forward uncovers at least one more tiny problem that needs to be resolved.

A lot of these problems relate to the GitHub Actions workflows being used to build, test and deploy my containers. Thankfully Claude 3\.5 Sonnet is great at helping refactor GitHub Actions YAML, which has been saving me a lot of time.

I'm really looking forward to wrapping this up, because I plan to celebrate by shipping a flurry of Datasette Cloud features that have been held up by the lack of a robust way to extensively test them before sending them out into the world.

#### **Blog entries**

* [Imitation Intelligence, my keynote for PyCon US 2024](https://simonwillison.net/2024/Jul/14/pycon/)
* [Give people something to link to so they can talk about your features and ideas](https://simonwillison.net/2024/Jul/13/give-people-something-to-link-to/)

I also updated my [write\-up of my recent AI World's Fair keynote](https://simonwillison.net/2024/Jun/27/ai-worlds-fair/) to include a link to the standalone YouTube video of the talk.

#### **Releases**

* **[llm 0\.15](https://github.com/simonw/llm/releases/tag/0.15)** \- 2024\-07\-18  
Access large language models from the command\-line
* **[sqlite\-utils 3\.37](https://github.com/simonw/sqlite-utils/releases/tag/3.37)** \- 2024\-07\-18  
Python CLI utility and library for manipulating SQLite databases
* **[llm\-mistral 0\.4](https://github.com/simonw/llm-mistral/releases/tag/0.4)** \- 2024\-07\-16  
LLM plugin providing access to Mistral models using the Mistral API
* **[datasette\-python 0\.1](https://github.com/datasette/datasette-python/releases/tag/0.1)** \- 2024\-07\-12  
Run a Python interpreter in the Datasette virtual environment

#### **TILs**

* [Trying out free\-threaded Python on macOS](https://til.simonwillison.net/python/trying-free-threaded-python) \- 2024\-07\-13
* [Accessing 1Password items from the terminal](https://til.simonwillison.net/macos/1password-terminal) \- 2024\-07\-10

---

**Link** 2024\-07\-15 [Hacker News homepage with links to comments ordered by most recent first](https://observablehq.com/@simonw/hacker-news-homepage):

Conversations on Hacker News are displayed as a tree, which can make it difficult to spot new comments added since the last time you viewed the thread.

There's a workaround for this using the [Hacker News Algolia Search](https://hn.algolia.com/) interface: search for `story:STORYID`, select "comments" and the result will be a list of comments sorted by most recent first.

I got fed up of doing this manually so I built a quick tool in an Observable Notebook that documents the hack, provides a UI for pasting in a Hacker News URL to get back that search interface link and also shows the most recent items on the homepage with links to their most recently added comments.

See also my [How to read Hacker News threads with most recent comments first](https://til.simonwillison.net/hacker-news/recent-comments) TIL from last year.

---

**Link** 2024\-07\-15 [Facebook Is the 'Zombie Internet'](https://www.404media.co/email/24eb6cea-6fa6-4b98-a2d2-8c4ba33d6c04/):

Ever since Facebook started to become infested with weird AI\-generated images of shrimp Jesus \- with thousands of comments and likes \- I've been wondering how much of that activity is real humans as opposed to yet more bots.

Jason Koebler has been on the Facebook AI slop beat for a while. In this superb piece of online investigative reporting he dives deep into an attempt to answer that question, using multiple Facebook burner accounts and contacting more than 300 users who have commented on that kind of image.

> I endlessly tried to talk to people who commented on these images, but I had no luck at all. Over the course of several months, I messaged 300 people who commented on bizarre AI\-generated images, which I could only do 20 or so at a time before Facebook stopped letting me send messages for several hours. I also commented on dozens of images myself, asking for any human who had also commented on the image to respond to me. Across those hundreds of messages, I got four total responses.

Jacob also talked to Khan Schoolcraft, a moderator of the [Um, isn’t that AI?](https://www.facebook.com/groups/958294675403424/) group, who said:

> In my experience, the supermajority of engagement on viral AI Facebook pages is just as artificially\-generated as the content they publish. When exploring their comment sections, one will often see hundreds of bot\-like comments interspersed with a few ‘real’ people sounding the alarm to no avail. \[...]
> 
> Whether it's a child transforming into a water bottle cyborg, a three\-armed flight attendant rescuing Tiger Jesus from a muddy plane crash, or a hybrid human\-monkey baby being stung to death by giant hornets, all tend to have copy\+pasted captions, reactions \& comments which usually make no sense in the observed context.

---

**Quote** 2024\-07\-15

> *We've doubled the max output token limit for Claude 3\.5 Sonnet from 4096 to 8192 in the Anthropic API.  
>   
> Just add the header* `"anthropic-beta": "max-tokens-3-5-sonnet-2024-07-15"` to your API calls.

[Alex Albert](https://twitter.com/alexalbert__/status/1812921642143900036)

---

**Link** 2024\-07\-15 [Follow the Crypto](https://www.followthecrypto.org/):

Very smart new site from Molly White tracking the huge increase in activity from Cryptocurrency\-focused PACs this year. These PACs have already raised $203 million and spent $38 million influencing US elections in 2024\.

Right now [Molly's rankings show](https://www.followthecrypto.org/committees/ranking/super) that the "Fairshake" cryptocurrency PAC is second only to the Trump\-supporting "Make America Great Again Inc" in money raised by Super PACs this year \- though it's 9th in [the list that includes other types of PAC](https://www.followthecrypto.org/committees/ranking/all).

Molly's data comes from the FEC, and the code behind the site [is all open source](https://github.com/molly/follow-the-crypto).

There's lots more about the project in the latest edition of [Molly's newsletter](https://www.citationneeded.news/follow-the-crypto/):

> Did you know that the cryptocurrency industry has spent more on 2024 elections in the United States than the oil industry? More than the pharmaceutical industry?
> 
> In fact, the cryptocurrency industry has spent more on 2024 elections than the entire energy sector *and* the entire health sector. Those industries, both worth hundreds of billions or trillions of dollars, are being outspent by an industry that, even by generous estimates, is worth less than $20 billion.

---

**Quote** 2024\-07\-16

> *OpenAI and Anthropic focused on building models and not worrying about products. For example, it took 6 months for OpenAI to bother to release a ChatGPT iOS app and 8 months for an Android app!  
>   
> Google and Microsoft shoved AI into everything in a panicked race, without thinking about which products would actually benefit from AI and how they should be integrated.  
>   
> Both groups of companies forgot the “make something people want” mantra. The generality of LLMs allowed developers to fool themselves into thinking that they were exempt from the need to find a product\-market fit, as if prompting is a replacement for carefully designed products or features. \[...]  
>   
> But things are changing. OpenAI and Anthropic seem to be transitioning from research labs focused on a speculative future to something resembling regular product companies. If you take all the human\-interest elements out of the OpenAI boardroom drama, it was fundamentally about the company's shift from creating gods to building products.*

[Arvind Narayanan](https://twitter.com/random_walker/status/1813231384032649573)

---

**Link** 2024\-07\-16 [Codestral Mamba](https://mistral.ai/news/codestral-mamba/):

New 7B parameter LLM from Mistral, released today. Codestral Mamba is "a Mamba2 language model specialised in code generation, available under an Apache 2\.0 license".

This the first model from Mistral that uses the [Mamba architecture](https://arxiv.org/abs/2312.00752), as opposed to the much more common Transformers architecture. Mistral say that Mamba can offer faster responses irrespective of input length which makes it ideal for code auto\-completion, hence why they chose to specialise the model in code.

It's available to run locally with the [mistral\-inference](https://github.com/mistralai/mistral-inference) GPU library, and Mistral say "For local inference, keep an eye out for support in llama.cpp" ([relevant issue](https://github.com/ggerganov/llama.cpp/issues/7727)).

It's also available through Mistral's La Plateforme API. I just shipped [llm\-mistral 0\.4](https://github.com/simonw/llm-mistral/releases/tag/0.4)adding a `llm -m codestral-mamba "prompt goes here"` default alias for the new model.

Also released today: [MathΣtral](https://mistral.ai/news/mathstral/), a 7B Apache 2 licensed model "designed for math reasoning and scientific discovery", with a 32,000 context window. This one isn't available through their API yet, but the weights are available [on Hugging Face](https://huggingface.co/mistralai/mathstral-7B-v0.1).

---

**Link** 2024\-07\-16 [Introducing Eureka Labs](https://eurekalabs.ai/):

Andrej Karpathy's new AI education company, exploring an AI\-assisted teaching model:

> The teacher still designs the course materials, but they are supported, leveraged and scaled with an AI Teaching Assistant who is optimized to help guide the students through them. This Teacher \+ AI symbiosis could run an entire curriculum of courses on a common platform.

On Twitter [Andrej says](https://twitter.com/karpathy/status/1813263734707790301):

> [@EurekaLabsAI](https://twitter.com/EurekaLabsAI) is the culmination of my passion in both AI and education over \~2 decades. My interest in education took me from YouTube tutorials on Rubik's cubes to starting CS231n at Stanford, to my more recent Zero\-to\-Hero AI series. While my work in AI took me from academic research at Stanford to real\-world products at Tesla and AGI research at OpenAI. All of my work combining the two so far has only been part\-time, as side quests to my "real job", so I am quite excited to dive in and build something great, professionally and full\-time.

The first course will be [LLM101n](https://github.com/karpathy/LLM101n) \- currently just a stub on GitHub, but with the goal to build an LLM chat interface "from scratch in Python, C and CUDA, and with minimal computer science prerequisites".

---

**Link** 2024\-07\-16 [Lessons learned in 35 years of making software](https://dev.jimgrey.net/2024/07/03/lessons-learned-in-35-years-of-making-software/):

Lots of great stuff in here from Jim Grey, with a strong focus on "soft skills" (I prefer the term "professional skills") around building relationships and making sure your contributions are visible.

This tip resonated with me in particular:

> **There is no substitute for working software in Production**. I can’t believe now that I have been part of *18\-month*release projects. This was back in the bad old waterfall days, but even then it was possible to release a lot more frequently than that. The software we build is valuable. It builds the value of the company. When you hold it until it’s perfect, or everything you think it needs to be, you are holding back on building the company’s value. Find the fastest, shortest path to getting the smallest increment of the thing that will work into the customer’s hands. You can keep making it better from there.

And another tip on the subject of perfectionism:

> **When you deliver work you’re really proud of, you’ve almost certainly done too much and taken too long**. I have a bit of a perfectionist streak. I want to do my work well and thoroughly. It took me a long time to learn that when I do that, it’s for me, not for the company. When I’ve reached 60\-80% of the thing being as good as I want, I’ve probably done enough.

---

**Link** 2024\-07\-16 [Mermaid Gantt diagrams are great for displaying distributed traces in Markdown](https://brycemecum.com/2023/03/31/til-mermaid-tracing/):

Bryce Mecum demonstrates how Mermaid`gantt`diagrams can be used to render trace information, such as the traces you might get from OpenTelemetry. I tried this out[in a Gist](https://gist.github.com/simonw/01c0440845516be42ddc4a9023181e75)and it works really well \- GitHub Flavored Markdown will turn any fenced code block tagged`mermaid`containing a`gantt`definition into a neat rendered diagram.

---

**Quote** 2024\-07\-17

> *Update, July 12: This innovation sparked a lot of conversation and questions that have no answers yet. We look forward to continuing to work with our customers on the responsible use of AI, but will not further pursue digital workers in the product.*

[Lattice (HR platform)](https://lattice.com/blog/leading-the-way-in-responsible-ai-employment)

---

**Link** 2024\-07\-17 [Announcing our DjangoCon US 2024 Talks!](https://2024.djangocon.us/news/announcing-lineup/):

I'm speaking at DjangoCon in Durham, NC in September.

My accepted talk title was **How to design and implement extensible software with plugins**. Here's my abstract:

> Plugins offer a powerful way to extend software packages. Tools that support a plugin architecture include WordPress, Jupyter, VS Code and pytest \- each of which benefits from an enormous array of plugins adding all kinds of new features and expanded capabilities.
> 
> Adding plugin support to an open source project can greatly reduce the friction involved in attracting new contributors. Users can work independently and even package and publish their work without needing to directly coordinate with the project's core maintainers. As a maintainer this means you can wake up one morning and your software grew new features without you even having to review a pull request!
> 
> There's one catch: information on *how* to design and implement plugin support for a project is scarce.
> 
> I now have three major open source projects that support plugins, with over 200 plugins published across those projects. I'll talk about everything I've learned along the way: when and how to use plugins, how to design plugin hooks and how to ensure your plugin authors have as good an experience as possible.

I'm going to be talking about what I've learned integrating [Pluggy](https://pluggy.readthedocs.io/) with [Datasette](https://datasette.io/), [LLM](https://llm.datasette.io/) and [sqlite\-utils](https://sqlite-utils.datasette.io/). I've been looking for an excuse to turn this knowledge into a talk for ages, very excited to get to do it at DjangoCon!

---

**Link** 2024\-07\-17 [AI Tooling for Software Engineers in 2024](https://newsletter.pragmaticengineer.com/p/ai-tooling-2024):

Gergely Orosz reports back on the survey he ran of 211 tech professionals concerning their use of generative AI. One interesting result:

> The responses reveal that as many professionals are using *both* ChatGPT and GitHub Copilot as all other tools combined!

I agree with Gergely's conclusion:

> **We’re in the midst of a significant tooling change, with AI\-augmented software engineering becoming widespread across tech**. Basically, these tools have too many upsides for developers to ignore them: it’s easier and faster to switch between stacks, easier to get started on projects, and simpler to become productive in unfamiliar codebases. Of course there are also downsides, but being aware of them means they can be mitigated.

---

**Link** 2024\-07\-17 [Introducing Llama\-3\-Groq\-Tool\-Use Models](https://wow.groq.com/introducing-llama-3-groq-tool-use-models/):

New from [Groq](https://groq.com/): two custom fine\-tuned Llama 3 models specifically designed for tool use. Hugging Face model links:

* [Groq/Llama\-3\-Groq\-8B\-Tool\-Use](https://huggingface.co/Groq/Llama-3-Groq-8B-Tool-Use)
* [Groq/Llama\-3\-Groq\-70B\-Tool\-Use](https://huggingface.co/Groq/Llama-3-Groq-70B-Tool-Use)

Groq's own internal benchmarks put their 70B model at the top of the [Berkeley Function\-Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html) with a score of 90\.76 (and 89\.06 for their 8B model, which would put it at \#3\). For comparison, Claude 3\.5 Sonnet scores 90\.18 and GPT\-4\-0124 scores 88\.29\.

The two new Groq models are also available through their screamingly\-fast (fastest in the business?) API, running at 330 tokens/s and 1050 tokens/s respectively.

Here's the documentation on [how to use tools through their API](https://console.groq.com/docs/tool-use).

---

**Link** 2024\-07\-17 [An example running DuckDB in ChatGPT Code Interpreter](https://chatgpt.com/share/de75e15e-d990-4c4e-b168-9f0390516dbe):

I confirmed today that DuckDB can indeed be run inside ChatGPT Code Interpreter (aka "data analysis"), provided you upload the correct wheel file for it to install. The wheel file it needs is currently `duckdb-1.0.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl`from the [PyPI releases page](https://pypi.org/project/duckdb/#files) \- I asked ChatGPT to identify its platform, and it said that it needs `manylinux2014_x86_64.whl` wheels.

Once the wheel in installed ChatGPT already knows enough of the DuckDB API to start performing useful operations with it \- and any brand new features in 1\.0 will work if you tell it how to use them.

---

**Link** 2024\-07\-18 [Apple, Nvidia, Anthropic Used Thousands of Swiped YouTube Videos to Train AI](https://www.proofnews.org/apple-nvidia-anthropic-used-thousands-of-swiped-youtube-videos-to-train-ai/):

This article has been getting a lot of attention over the past couple of days.

The story itself is nothing new: [the Pile](https://pile.eleuther.ai/) is four years old now, and has been widely used for training LLMs since before anyone even cared what an LLM was. It turns out one of the components of the Pile is a set of \~170,000 YouTube video captions (just the captions, not the actual video) and this story by Annie Gilbertson and Alex Reisner highlights that and interviews some of the creators who were included in the data, as well as providing a [search tool](https://www.proofnews.org/youtube-ai-search/) for seeing if a specific creator has content that was included.

What's notable is the response. Marques Brownlee (19m subscribers) [posted a video about it](https://www.youtube.com/watch?v=xiJMjTnlxg4). Abigail Thorn ([Philosophy Tube](https://www.youtube.com/user/thephilosophytube), 1\.57m subscribers) [tweeted this](https://twitter.com/PhilosophyTube/status/1813227210569920685):

> Very sad to have to say this \- an AI company called EleutherAI stole tens of thousands of YouTube videos \- including many of mine. I’m one of the creators Proof News spoke to. The stolen data was sold to Apple, Nvidia, and other companies to build AI
> 
> When I was told about this I lay on the floor and cried, it’s so violating, it made me want to quit writing forever. The reason I got back up was because I know my audience come to my show for real connection and ideas, not cheapfake AI garbage, and I know they’ll stay with me

Framing the data as "sold to Apple..." is a slight misrepresentation here \- EleutherAI have been giving the Pile away for free since 2020\. It's a good illustration of the emotional impact here though: many creative people *do not want* their work used in this way, especially without their permission.

It's interesting seeing how attitudes to this stuff change over time. Four years ago the fact that a bunch of academic researchers were sharing and training models using 170,000 YouTube subtitles would likely not have caught any attention at all. Today, people care!

---

**Link** 2024\-07\-18 [Mistral NeMo](https://mistral.ai/news/mistral-nemo/):

Released by Mistral today: "Our new best small model. A state\-of\-the\-art 12B model with 128k context length, built in collaboration with NVIDIA, and released under the Apache 2\.0 license."

Nice to see Mistral use Apache 2\.0 for this, unlike their [Codestral 22B release](https://simonwillison.net/2024/May/30/codestral/) \- though Codestral Mamba was Apache 2\.0 as well.

Mistral's own benchmarks but NeMo slightly ahead of the smaller (but same general weight class) Gemma 2 9B and Llama 3 8B models.

It's both multi\-lingual and trained for tool usage:

> The model is designed for global, multilingual applications. It is trained on function calling, has a large context window, and is particularly strong in English, French, German, Spanish, Italian, Portuguese, Chinese, Japanese, Korean, Arabic, and Hindi.

Part of this is down to the new Tekken tokenizer, which is 30% more efficient at representing both source code and most of the above listed languages.

You can try it out via [Mistral's API](https://console.mistral.ai/) using [llm\-mistral](https://github.com/simonw/llm-mistral) like this:

```
pipx install llm
llm install llm-mistral
llm keys set mistral
# paste La Plateforme API key here
llm mistral refresh # if you installed the plugin before
llm -m mistral/open-mistral-nemo 'Rave about pelicans in French'

```

---

**Link** 2024\-07\-18 [GPT\-4o mini](https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/):

I've been complaining about how under\-powered GPT 3\.5 is for the price for a while now (I [made fun of it](https://simonwillison.net/2024/Jun/27/ai-worlds-fair/#slide.011.jpeg) in a keynote a few weeks ago).

GPT\-4o mini is *exactly* what I've been looking forward to.

It supports 128,000 input tokens (both images and text) and an impressive 16,000 output tokens. Most other models are still \~4,000, and Claude 3\.5 Sonnet got an upgrade to 8,192 [just a few days ago](https://simonwillison.net/2024/Jul/15/alex-albert/). This makes it a good fit for translation and transformation tasks where the expected output more closely matches the size of the input.

OpenAI show benchmarks that have it out\-performing Claude 3 Haiku and Gemini 1\.5 Flash, the two previous cheapest\-best models.

GPT\-4o mini is 15 cents per millions input tokens and 60 cents per million output tokens \- a 60% discount on GPT\-3\.5, and cheaper than Claude 3 Haiku's 25c/125c and Gemini 1\.5 Flash's 35c/70c. Or you can use the OpenAI [batch API](https://platform.openai.com/docs/guides/batch)for 50% off again, in exchange for up\-to\-24\-hours of delay in getting the results.

It's also worth comparing these prices with GPT\-4o's: at $5/million input and $15/million output GPT\-4o mini is 33x cheaper for input and 25x cheaper for output!

OpenAI point out that "the cost per token of GPT\-4o mini has dropped by 99% since text\-davinci\-003, a less capable model introduced in 2022\."

Also notable:

> GPT\-4o mini in the API is the first model to apply our [instruction hierarchy](https://arxiv.org/abs/2404.13208)method, which helps to improve the model's ability to resist jailbreaks, prompt injections, and system prompt extractions.

My hunch is that this still won't 100% solve [the security implications](https://simonwillison.net/2023/Apr/14/worst-that-can-happen/) of prompt injection: I imagine creative enough attackers will still find ways to subvert system instructions, and the linked paper itself concludes "Finally, our current models are likely still vulnerable to powerful adversarial attacks". It could well help make [accidental prompt injection](https://simonwillison.net/2024/Jun/6/accidental-prompt-injection/) a lot less common though, which is certainly a worthwhile improvement.

---

**Link** 2024\-07\-18 [LLM 0\.15](https://llm.datasette.io/en/stable/changelog.html#v0-15):

A new release of my [LLM CLI tool](https://llm.datasette.io/) for interacting with Large Language Models from the terminal (see [this recent talk](https://simonwillison.net/2024/Jun/17/cli-language-models/) for plenty of demos).

This release adds support for the brand new [GPT\-4o mini](https://simonwillison.net/2024/Jul/18/gpt-4o-mini/):

```
llm -m gpt-4o-mini "rave about pelicans in Spanish"

```

It also sets that model as the default used by the tool if no other model is specified. This replaces GPT\-3\.5 Turbo, the default since the first release of LLM. 4o\-mini is both cheaper and *way* more capable than 3\.5 Turbo.

---