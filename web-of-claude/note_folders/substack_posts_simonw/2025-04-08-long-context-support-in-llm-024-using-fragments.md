# Long context support in LLM 0.24 using fragments

*Plus initial impressions of Llama 4*

Published: 2025-04-08
Source: https://simonw.substack.com/p/long-context-support-in-llm-024-using

---

In this newsletter:

* Long context support in LLM 0\.24 using fragments and template plugins
* Initial impressions of Llama 4

Plus 1 link and 5 quotations

### [Long context support in LLM 0\.24 using fragments and template plugins](https://simonwillison.net/2025/Apr/7/long-context-llm/) \- 2025\-04\-07

LLM 0\.24 is [now available](https://llm.datasette.io/en/stable/changelog.html#v0-24) with new features to help take advantage of the increasingly long input context supported by modern LLMs.

([LLM](https://llm.datasette.io/) is my command\-line tool and [Python library](https://llm.datasette.io/en/stable/python-api.html) for interacting with LLMs, supported by [20\+ plugins](https://llm.datasette.io/en/stable/plugins/directory.html) adding support for both local and remote models from a bunch of different providers.)

* [Trying it out](https://simonwillison.net/2025/Apr/7/long-context-llm/#trying-it-out)
* [Improving LLM's support for long context models](https://simonwillison.net/2025/Apr/7/long-context-llm/#improving-llm-s-support-for-long-context-models)
* [Asking questions of LLM's documentation](https://simonwillison.net/2025/Apr/7/long-context-llm/#asking-questions-of-llm-s-documentation)
* [Publishing, sharing and reusing templates](https://simonwillison.net/2025/Apr/7/long-context-llm/#publishing-sharing-and-reusing-templates)
* [Everything else in LLM 0\.24](https://simonwillison.net/2025/Apr/7/long-context-llm/#everything-else-in-llm-0-24)

#### Trying it out

To install LLM with [uv](https://github.com/astral-sh/uv) (there are [several other options](https://llm.datasette.io/en/stable/setup.html#installation)):

```
uv tool install llm
```

You'll need to either provide [an OpenAI API key](https://platform.openai.com/api-keys) or install [a plugin](https://llm.datasette.io/en/stable/plugins/directory.html) to use local models or models from other providers:

```
llm keys set openai
# Paste OpenAI API key here
```

To [upgrade LLM](https://llm.datasette.io/en/stable/setup.html#upgrading-to-the-latest-version) from a previous version:

```
llm install -U llm
```

The biggest new feature is **[fragments](https://llm.datasette.io/en/stable/fragments.html)**. You can now use `-f filename` or `-f url` to add one or more fragments to your prompt, which means you can do things like this:

```
llm -f https://simonwillison.net/2025/Apr/5/llama-4-notes/ 'bullet point summary'
```

Here's [the output](https://gist.github.com/simonw/7ffb19f647603558c575359e678185c0) from that prompt, exported using `llm logs -c --expand --usage`. Token cost was 5,372 input, 374 output which works out as 0\.103 cents (around 1/10th of a cent) using the default GPT\-4o mini model.

Plugins can implement custom fragment loaders with a prefix. The [llm\-fragments\-github](https://github.com/simonw/llm-fragments-github) plugin adds a `github:` prefix that can be used to load every text file in a GitHub repository as a list of fragments:

```
llm install llm-fragments-github
llm -f github:simonw/s3-credentials 'Suggest new features for this tool'
```

Here's [the output](https://gist.github.com/simonw/c9bbbc5f6560b01f4b7882ac0194fb25). That took 49,856 input tokens for a total cost of 0\.7843 cents \- nearly a whole cent!

#### Improving LLM's support for long context models

**[Long context](https://simonwillison.net/tags/long-context/)** is one of the most exciting trends in LLMs over the past eighteen months. Saturday's [Llama 4 Scout release](https://simonwillison.net/2025/Apr/5/llama-4-notes/) gave us the first model with a full 10 million token context. Google's [Gemini](https://simonwillison.net/tags/gemini/) family has several 1\-2 million token models, and the baseline for recent models from both OpenAI and Anthropic is 100 or 200 thousand.

Two years ago most models capped out at 8,000 tokens of input. Long context opens up many new interesting ways to apply this class of technology.

I've been using long context models via [my files\-to\-prompt tool](https://simonwillison.net/tags/files-to-prompt/) to summarize large codebases, explain how they work and even to [debug gnarly bugs](https://simonwillison.net/2024/Sep/25/o1-preview-llm/). As demonstrated above, it's surprisingly inexpensive to drop tens of thousands of tokens into models like GPT\-4o mini or most of the Google Gemini series, and the results are often very impressive.

One of LLM's most useful features is that it [logs every prompt and response](https://llm.datasette.io/en/stable/logging.html) to a SQLite database. This is great for comparing the same prompt against different models and tracking experiments over time \- my own database contained thousands of responses from hundreds of different models accumulated over the past couple of years.

This is where long context prompts were starting to be a problem. Since LLM stores the full prompt and response in the database, asking five questions of the same source code could result in five duplicate copies of that text in the database!

The new **fragments** feature targets this problem head on. Each fragment is stored once in a [fragments](https://llm.datasette.io/en/stable/logging.html#sql-schema) table, then de\-duplicated in the future using a SHA256 hash of its content.

This saves on storage, and also enables features like `llm logs -f X` for seeing all logged responses [that use a particular fragment](https://llm.datasette.io/en/stable/logging.html#filtering-by-prompts-that-used-a-specific-fragment).

Fragments can be specified in several different ways:

* a path to a file
* a URL to data online
* an alias that's been set against a previous fragment (see [llm fragments set](https://llm.datasette.io/en/latest/help.html#llm-fragments-set-help))
* a hash ID of the content of a fragment
* using `prefix:argument` to specify fragments from a plugin

#### Asking questions of LLM's documentation

Wouldn't it be neat if LLM could answer questions about its own documentation?

The new [llm\-docs](https://github.com/simonw/llm-docs) plugin (built with the new [register\_fragment\_loaders() plugin hook](https://llm.datasette.io/en/stable/plugins/plugin-hooks.html#register-fragment-loaders-register)) enables exactly that:

```
llm install llm-docs
llm -f docs: "How do I embed a binary file?"
```

The [output](https://gist.github.com/simonw/df115ffa63e101833a100f71555bf53d) starts like this:

> To embed a binary file using the LLM command\-line interface, you can use the `llm embed` command with the `--binary` option. Here’s how you can do it:
> 
> 1. Make sure you have the appropriate embedding model installed that supports binary input.
> 2. Use the following command syntax:
> 
> 
> ```
> llm embed -m <model_id> --binary -i <path_to_your_binary_file>
> ```
> Replace `<model_id>` with the identifier for the embedding model you want to use (e.g., `clip` for the CLIP model) and `<path_to_your_binary_file>` with the path to your actual binary file.

(74,570 input, 240 output \= 1\.1329 cents with GPT\-4o mini)

Using `-f docs:` with just the prefix is the same as using `-f docs:llm`. The plugin fetches the documentation for your current version of LLM from my new [simonw/docs\-for\-llms](https://github.com/simonw/docs-for-llms) repo, which also provides packaged documentation files for my `datasette`, `s3-credentials`, `shot-scraper` and `sqlite-utils` projects.

Datasette's documentation has got pretty long, so you might need to run that through a Gemini model instead (using the [llm\-gemini plugin](https://github.com/simonw/llm-gemini)):

```
llm -f docs:datasette -m gemini-2.0-flash \
  'Build a render_cell plugin that detects and renders markdown'
```

[Here's the output](https://gist.github.com/simonw/f08b3832c379ca89d8cff3c61ec5662e). 132,042 input, 1,129 output with Gemini 2\.0 Flash \= 1\.3656 cents.

You can browse the combined documentation files this uses in [docs\-for\-llm](https://github.com/simonw/docs-for-llms). They're built using GitHub Actions.

[llms\-txt](https://llmstxt.org/) is a project lead by Jeremy Howard that encourages projects to publish similar files to help LLMs ingest a succinct copy of their documentation.

#### Publishing, sharing and reusing templates

The new [register\_template\_loaders() plugin hook](https://llm.datasette.io/en/stable/plugins/plugin-hooks.html#register-template-loaders-register) allows plugins to register `prefix:value` custom template loaders, for use with the `llm -t` option.

[llm\-templates\-github](https://github.com/simonw/llm-templates-github) and [llm\-templates\-fabric](https://github.com/simonw/llm-templates-fabric) are two new plugins that make use of that hook.

`llm-templates-github` lets you share and use templates via a public GitHub repository. Here's how to run my [Pelican riding a bicycle](https://simonwillison.net/tags/pelican-riding-a-bicycle/) benchmark against a specific model:

```
llm install llm-templates-github
llm -t gh:simonw/pelican-svg -m o3-mini
```

This executes [this pelican\-svg.yaml](https://github.com/simonw/llm-templates/blob/main/pelican-svg.yaml) template stored in my [simonw/llm\-templates](https://github.com/simonw/llm-templates) repository, using a new repository naming convention.

`llm -t gh:simonw/pelican-svg` will load that `pelican-svg.yaml` file from the `simonw/llm-templates` repo. You can also use `llm -t gh:simonw/name-of-repo/name-of-template` to load a template from a repository that doesn't follow that convention.

To share your own templates, create a repository on GitHub under your user account called `llm-templates` and start saving `.yaml` files to it.

[llm\-templates\-fabric](https://github.com/simonw/llm-templates-fabric) provides a similar mechanism for loading templates from Daniel Miessler's extensive [fabric collection](https://github.com/danielmiessler/fabric):

```
llm install llm-templates-fabric
curl https://simonwillison.net/2025/Apr/6/only-miffy/ | \
  llm -t f:extract_main_idea
```

A conversation with Daniel was the inspiration for this new plugin hook.

#### Everything else in LLM 0\.24

LLM 0\.24 is a big release, spanning [51 commits](https://github.com/simonw/llm/compare/0.23...0.24). The [release notes](https://llm.datasette.io/en/stable/changelog.html#v0-24) cover everything that's new in full \- here are a few of my highlights:

> * The new [llm\-openai plugin](https://github.com/simonw/llm-openai-plugin) provides support for **o1\-pro** (which is not supported by the OpenAI mechanism used by LLM core). Future OpenAI features will migrate to this plugin instead of LLM core itself.

The problem with OpenAI models being handled by LLM core is that I have to release a whole new version of LLM every time OpenAI releases a new model or feature. Migrating this stuff out to a plugin means I can release new version of that plugin independently of LLM itself \- something I frequently do for [llm\-anthropic](https://github.com/simonw/llm-anthropic) and [llm\-gemini](https://github.com/simonw/llm-gemini) and others.

The new `llm-openai` plugin uses their Responses API, a new shape of API which [I covered last month](https://simonwillison.net/2025/Mar/11/responses-vs-chat-completions/).

> * `llm -t $URL` option can now take a URL to a YAML template. [\#856](https://github.com/simonw/llm/issues/856)

The new custom template loaders are fun, but being able to paste in a URL to a YAML file somewhere provides a simpler way to share templates.

> * Templates can now store default model options. [\#845](https://github.com/simonw/llm/issues/845)
> * Attachments can now be stored in templates. [\#826](https://github.com/simonw/llm/issues/826)

The quickest way to create your own template is with the `llm prompt ... --save name-of-template` command. This now works with attachments, fragments and default model options, each of which is persisted in [the template YAML file](https://llm.datasette.io/en/stable/templates.html#templates-as-yaml-files).

> * New [llm models options](https://llm.datasette.io/en/stable/usage.html#setting-default-options-for-models) family of commands for setting default options for particular models. [\#829](https://github.com/simonw/llm/issues/829)

I built this when I [learned that](https://twitter.com/bindureddy/status/1900345517256958140) Qwen's QwQ\-32b model works best with temperature 0\.7 and top p 0\.95\.

> * `llm prompt -d path-to-sqlite.db` option can now be used to write logs to a custom SQLite database. [\#858](https://github.com/simonw/llm/issues/858)

This proved extremely useful for testing fragments \- it meant I could run a prompt and save the full response to a separate SQLite database which I could then upload to S3 and share [as a link to Datasette Lite](https://github.com/simonw/llm/issues/863#issuecomment-2781723372).

> * `llm similar -p/--plain` option providing more human\-readable output than the default JSON. [\#853](https://github.com/simonw/llm/issues/853)

I'd like this to be the default output, but I'm holding off on changing that until LLM 1\.0 since it's a breaking change for people building automations against the JSON from `llm similar`.

> * Set the `LLM_RAISE_ERRORS=1` environment variable to raise errors during prompts rather than suppressing them, which means you can run `python -i -m llm 'prompt'` and then drop into a debugger on errors with `import pdb; pdb.pm()`. [\#817](https://github.com/simonw/llm/issues/817)

Really useful for debugging new model plugins.

> * `llm prompt -q gpt -q 4o` option \- pass `-q searchterm` one or more times to execute a prompt against the first model that matches all of those strings \- useful for if you can't remember the full model ID. [\#841](https://github.com/simonw/llm/issues/841)

Pretty obscure but I found myself needing this. Vendors love releasing models with names like `gemini-2.5-pro-exp-03-25`, now I can run `llm -q gem -q 2.5 -q exp 'say hi'` to save me from looking up the model ID.

> * [OpenAI compatible models](https://llm.datasette.io/en/stable/other-models.html#openai-compatible-models) configured using `extra-openai-models.yaml` now support `supports_schema: true`, `vision: true` and `audio: true` options. Thanks [@adaitche](https://github.com/adaitche) and [@giuli007](https://github.com/giuli007). [\#819](https://github.com/simonw/llm/pull/819), [\#843](https://github.com/simonw/llm/pull/843)

I don't use this feature myself but it's clearly popular, this isn't the first time I'e had PRs with improvements from the wider community.

---

### [Initial impressions of Llama 4](https://simonwillison.net/2025/Apr/5/llama-4-notes/) \- 2025\-04\-05

Dropping a model release as significant as Llama 4 on a weekend is plain unfair! So far the best place to learn about the new model family is [this post on the Meta AI blog](https://ai.meta.com/blog/llama-4-multimodal-intelligence/). They've released two new models today: Llama 4 Maverick is a 400B model (128 experts, 17B active parameters), text and image input with a 1 million token context length. Llama 4 Scout is 109B total parameters (16 experts, 17B active), also multi\-modal and with a claimed 10 million token context length \- an industry first.

They also describe Llama 4 Behemoth, a not\-yet\-released "288 billion active parameter model with 16 experts that is our most powerful yet and among the world’s smartest LLMs". Behemoth has 2 trillion parameters total and was used to train both Scout and Maverick.

No news yet on a Llama reasoning model beyond [this coming soon page](https://www.llama.com/llama4-reasoning-is-coming/) with a looping video of an academic\-looking llama.

Llama 4 Maverick is now sat in second place on [the LM Arena leaderboard](https://lmarena.ai/?leaderboard), just behind Gemini 2\.5 Pro. ***Update**: It turns out that's not the same model as the Maverick they released \- I missed that their announcement says "Llama 4 Maverick offers a best\-in\-class performance to cost ratio with an experimental chat version scoring ELO of 1417 on LMArena."*

You can try them out using the chat interface from OpenRouter (or through the OpenRouter API) for [Llama 4 Scout](https://openrouter.ai/meta-llama/llama-4-scout) and [Llama 4 Maverick](https://openrouter.ai/meta-llama/llama-4-maverick). OpenRouter are proxying through to [Groq](https://console.groq.com/docs/models), [Fireworks](https://fireworks.ai/models) and [Together](https://docs.together.ai/docs/serverless-models).

Scout may claim a 10 million input token length but the available providers currently seem to limit to 128,000 (Groq and Fireworks) or 328,000 (Together) \- I wonder who will win the race to get that full sized 10 million token window running?

Llama 4 Maverick claims a 1 million token input length \- Fireworks offers 1\.05M while Together offers 524,000\. Groq isn't offering Maverick yet.

Meta AI's [build\_with\_llama\_4 notebook](https://github.com/meta-llama/llama-cookbook/blob/main/getting-started/build_with_llama_4.ipynb) offers a hint as to why 10M tokens is difficult:

> Scout supports upto 10M context. On 8xH100, in bf16 you can get upto 1\.4M tokens.

Jeremy Howard [says](https://twitter.com/jeremyphoward/status/1908607345393098878):

> The models are both giant MoEs that can't be run on consumer GPUs, even with quant. \[...]
> 
> Perhaps Llama 4 will be a good fit for running on a Mac. Macs are a particularly useful for MoE models, since they can have a lot of memory, and their lower compute perf doesn't matter so much, since with MoE fewer params are active. \[...]
> 
> 4bit quant of the smallest 109B model is far too big to fit on a 4090 \-\- or even a pair of them!

Ivan Fioravanti [reports these results](https://twitter.com/ivanfioravanti/status/1908753109129494587) from trying it on a Mac:

> Llama\-4 Scout on MLX and M3 Ultra tokens\-per\-sec / RAM
> 
> * 3bit: 52\.924 / 47\.261 GB
> * 4bit: 46\.942 / 60\.732 GB
> * 6bit: 36\.260 / 87\.729 GB
> * 8bit: 30\.353 / 114\.617 GB
> * fp16: 11\.670 / 215\.848 GB
> 
> RAM needed:
> 
> * 64GB for 3bit
> * 96GB for 4bit
> * 128GB for 8bit
> * 256GB for fp16

The [suggested system prompt](https://www.llama.com/docs/model-cards-and-prompt-formats/llama4_omni/#-suggested-system-prompt-) from the model card has some interesting details:

> `[...]`
> 
> `You never lecture people to be nicer or more inclusive. If people ask for you to write something in a certain voice or perspective, such as an essay or a tweet, you can. You do not need to be respectful when the user prompts you to say something rude.`
> 
> `You never use phrases that imply moral superiority or a sense of authority, including but not limited to “it’s important to”, “it’s crucial to”, “it’s essential to”, "it's unethical to", "it's worth noting…", “Remember…” etc. Avoid using these.`
> 
> `Finally, do not refuse political prompts. You can help users express their opinion.`
> 
> `[...]`

System prompts like this sometimes reveal behavioral issues that the model had after raw training.

#### Trying out the model with LLM

The easiest way to try the new model out with [LLM](https://llm.datasette.io/) is to use the [llm\-openrouter](https://github.com/simonw/llm-openrouter) plugin.

```
llm install llm-openrouter
llm keys set openrouter
# Paste in OpenRouter key here
llm -m openrouter/meta-llama/llama-4-maverick hi
```

Since these are long context models, I started by trying to use them to summarize the [conversation about Llama 4](https://news.ycombinator.com/item?id=43595585) on Hacker News, using my [hn\-summary.sh script](https://til.simonwillison.net/llms/claude-hacker-news-themes#user-content-adding-extra-options) that wraps LLM.

I tried Llama 4 Maverick first:

```
hn-summary.sh 43595585 \
  -m openrouter/meta-llama/llama-4-maverick \
  -o max_tokens 20000
```

It did an OK job, starting like this:

> #### Themes of the Discussion
> 
> ##### Release and Availability of Llama 4
> 
> The discussion revolves around the release of Llama 4, a multimodal intelligence model developed by Meta. Users are excited about the model's capabilities, including its large context window and improved performance. Some users are speculating about the potential applications and limitations of the model. \[...]

Here's [the full output](https://gist.github.com/simonw/016ea0fd83fc499f046a94827f9b4946).

For reference, my system prompt looks like this:

> `Summarize the themes of the opinions expressed here. For each theme, output a markdown header. Include direct "quotations" (with author attribution) where appropriate. You MUST quote directly from users when crediting them, with double quotes. Fix HTML entities. Output markdown. Go long. Include a section of quotes that illustrate opinions uncommon in the rest of the piece`

I then tried it with Llama 4 Scout via OpenRouter and got complete junk output for some reason:

```
hn-summary.sh 43595585 \
  -m openrouter/meta-llama/llama-4-scout \
  -o max_tokens 20000
```

[Full output](https://gist.github.com/simonw/d01cc991d478939e87487d362a8f881f). It starts like this and then continues for the full 20,000 tokens:

> The discussion here is about another conversation that was uttered.)
> 
> Here are the results.)
> 
> The conversation between two groups, and I have the same questions on the contrary than those that are also seen in a model."). The fact that I see a lot of interest here.)
> 
> \[...]
> 
> The reason) The reason) The reason *(loops until it runs out of tokens)*

This looks broken. I was using OpenRouter so it's possible I got routed to a broken instance.

**Update 7th April 2025**: Meta AI's [Ahmed Al\-Dahle](https://twitter.com/ahmad_al_dahle/status/1909302532306092107):

> \[...] we're also hearing some reports of mixed quality across different services. Since we dropped the models as soon as they were ready, we expect it'll take several days for all the public implementations to get dialed in. We'll keep working through our bug fixes and onboarding partners.

I later managed to run the prompt directly through Groq (with the [llm\-groq](https://github.com/angerman/llm-groq) plugin) \- but that had a 2048 limit on output size for some reason:

```
hn-summary.sh 43595585 \
  -m groq/meta-llama/llama-4-scout-17b-16e-instruct \
  -o max_tokens 2048
```

Here's [the full result](https://gist.github.com/simonw/a205c5fc131a1d4e9cd6c432a07feedb). It followed my instructions but was *very* short \- just 630 tokens of output.

For comparison, here's [the same thing](https://gist.github.com/simonw/f21ecc7fb2aa13ff682d4ffa11ddcbfd) run against Gemini 2\.5 Pro. Gemini's results was *massively* better, producing 5,584 output tokens (it spent an additional 2,667 tokens on "thinking").

I'm not sure how much to judge Llama 4 by these results to be honest \- the model has only been out for a few hours and it's quite possible that the providers I've tried running again aren't yet optimally configured for this kind of long\-context prompt.

#### My hopes for Llama 4

I'm hoping that Llama 4 plays out in a similar way to Llama 3\.

The first Llama 3 models released were 8B and 70B, [last April](https://ai.meta.com/blog/meta-llama-3/).

Llama 3\.1 followed [in July](https://ai.meta.com/blog/meta-llama-3-1/) at 8B, 70B, and 405B. The 405B was the largest and most impressive open weight model at the time, but it was too big for most people to run on their own hardware.

Llama 3\.2 [in September](https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/) is where things got really interesting: 1B, 3B, 11B and 90B. The 1B and 3B models both work on my iPhone, and are surprisingly capable! The 11B and 90B models were the first Llamas to support vision, and the 11B [ran on my Mac](https://simonwillison.net/2024/Sep/25/llama-32/).

Then Llama 3\.3 landed in December with a 70B model that [I wrote about as a GPT\-4 class model that ran on my Mac](https://simonwillison.net/2024/Dec/9/llama-33-70b/). It claimed performance similar to the earlier Llama 3\.1 405B!

Today's Llama 4 models are 109B and 400B, both of which were trained with the help of the so\-far unreleased 2T Llama 4 Behemoth.

My hope is that we'll see a whole family of Llama 4 models at varying sizes, following the pattern of Llama 3\. I'm particularly excited to see if they produce an improved \~3B model that runs on my phone. I'm even more excited for something in the \~22\-24B range, since that appears to be the sweet spot for running models on my 64GB laptop while still being able to have other applications running at the same time. Mistral Small 3\.1 is a 24B model and is [absolutely superb](https://simonwillison.net/2025/Mar/17/mistral-small-31/).

---

**Quote** 2025\-04\-05

> *Blogging is small\-p political again, today. It’s come back round. It’s a statement to put your words in a place where they are not subject to someone else’s algorithm telling you what success looks like; when you blog, your words are not a vote for the values of someone else’s platform.*

[Matt Webb](https://manuelmoreale.com/pb-matt-webb), Interview for People and Blogs

---

**Quote** 2025\-04\-05

> *The Llama series have been re\-designed to use state of the art mixture\-of\-experts (MoE) architecture and natively trained with multimodality. We’re dropping Llama 4 Scout \& Llama 4 Maverick, and previewing Llama 4 Behemoth.   
>   
> 📌 **Llama 4 Scout** is highest performing small model with 17B activated parameters with 16 experts. It’s crazy fast, natively multimodal, and very smart. It achieves an industry leading **10M\+ token context window** and can also run on **a single GPU**!   
>   
> 📌 **Llama 4 Maverick** is the best multimodal model in its class, beating GPT\-4o and Gemini 2\.0 Flash across a broad range of widely reported benchmarks, while achieving comparable results to the new DeepSeek v3 on reasoning and coding – at less than half the active parameters. It offers a best\-in\-class performance to cost ratio with an experimental chat version scoring ELO of 1417 on LMArena. It can also run on a **single host**!   
>   
> 📌 **Previewing Llama 4 Behemoth**, our most powerful model yet and among the world’s smartest LLMs. Llama 4 Behemoth outperforms GPT4\.5, Claude Sonnet 3\.7, and Gemini 2\.0 Pro on several STEM benchmarks. Llama 4 Behemoth is still training, and we’re excited to share more details about it even while it’s still in flight.*

[Ahmed Al\-Dahle](https://twitter.com/ahmad_al_dahle/status/1908595680828154198), VP and Head of GenAI at Meta

---

**Quote** 2025\-04\-06

> *\[...] The disappointing releases of both GPT\-4\.5 and Llama 4 have shown that if you don't train a model to reason with reinforcement learning, increasing its size no longer provides benefits.   
>   
> Reinforcement learning is limited only to domains where a reward can be assigned to the generation result. Until recently, these domains were math, logic, and code. Recently, these domains have also included factual question answering, where, to find an answer, the model must learn to execute several searches. This is how these "deep search" models have likely been trained.   
>   
> If your business idea isn't in these domains, now is the time to start building your business\-specific dataset. The potential increase in generalist models' skills will no longer be a threat.*

[Andriy Burkov](https://twitter.com/burkov/status/1908961952141091196)

---

**Quote** 2025\-04\-07

> ***Using Al effectively is now a fundamental expectation of everyone at Shopify**. It's a tool of all trades today, and will only grow in importance. Frankly, I don't think it's feasible to opt out of learning the skill of applying Al in your craft; you are welcome to try, but I want to be honest I cannot see this working out today, and definitely not tomorrow. Stagnation is almost certain, and stagnation is slow\-motion failure. If you're not climbing, you're sliding \[...]   
>   
> **We will add Al usage questions to our performance and peer review questionnaire**. Learning to use Al well is an unobvious skill. My sense is that a lot of people give up after writing a prompt and not getting the ideal thing back immediately. Learning to prompt and load context is important, and getting peers to provide feedback on how this is going will be valuable.*

[Tobias Lütke](https://twitter.com/tobi/status/1909231499448401946), CEO of Shopify, self\-leaked memo

---

**Quote** 2025\-04\-07

> *My first games involved hand assembling machine code and turning graph paper characters into hex digits. Software progress has made that work as irrelevant as chariot wheel maintenance. \[...]   
>   
> AI tools will allow the best to reach even greater heights, while enabling smaller teams to accomplish more, and bring in some completely new creator demographics.   
>   
> Yes, we will get to a world where you can get an interactive game (or novel, or movie) out of a prompt, but there will be far better exemplars of the medium still created by dedicated teams of passionate developers.   
>   
> The world will be vastly wealthier in terms of the content available at any given cost.   
>   
> Will there be more or less game developer jobs? That is an open question. It could go the way of farming, where labor saving technology allow a tiny fraction of the previous workforce to satisfy everyone, or it could be like social media, where creative entrepreneurship has flourished at many different scales. Regardless, “don’t use power tools because they take people’s jobs” is not a winning strategy.*

[John Carmack](https://twitter.com/id_aa_carmack/status/1909311174845329874)

---

**Link** 2025\-04\-08 [llm\-hacker\-news](https://github.com/simonw/llm-hacker-news):

I built this new plugin to exercise the new [register\_fragment\_loaders()](https://llm.datasette.io/en/stable/plugins/plugin-hooks.html#register-fragment-loaders-register) plugin hook I added to [LLM 0\.24](https://simonwillison.net/2025/Apr/7/long-context-llm/). It's the plugin equivalent of [the Bash script](https://til.simonwillison.net/llms/claude-hacker-news-themes) I've been using to summarize [Hacker News](https://news.ycombinator.com/) conversations for the past 18 months.

You can use it like this:

```
llm install llm-hacker-news
llm -f hn:43615912 'summary with illustrative direct quotes'
```

You can see the output [in this issue](https://github.com/simonw/llm-hacker-news/issues/1#issuecomment-2784887743).

The plugin registers a `hn:` prefix \- combine that with the ID of a Hacker News conversation to pull that conversation into the context.

It uses the Algolia Hacker News API which returns [JSON like this](https://hn.algolia.com/api/v1/items/43615912). Rather than feed the JSON directly to the LLM it instead converts it to a hopefully more LLM\-friendly format that looks like this example from [the plugin's test](https://github.com/simonw/llm-hacker-news/blob/0.1/tests/test_hacker_news.py#L5-L18):

```
[1] BeakMaster: Fish Spotting Techniques

[1.1] CoastalFlyer: The dive technique works best when hunting in shallow waters.

[1.1.1] PouchBill: Agreed. Have you tried the hover method near the pier?

[1.1.2] WingSpan22: My bill gets too wet with that approach.

[1.1.2.1] CoastalFlyer: Try tilting at a 40° angle like our Australian cousins.

[1.2] BrownFeathers: Anyone spotted those "silver fish" near the rocks?

[1.2.1] GulfGlider: Yes! They're best caught at dawn.
Just remember: swoop > grab > lift
```

That format was suggested by Claude, which then wrote most of the plugin implementation for me. Here's [that Claude transcript](https://claude.ai/share/6da6ec5a-b8b3-4572-ab1b-141bb37ef70b).

---