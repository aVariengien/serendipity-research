# Gemini 2.5 Pro pricing, a new GPT-4o

*and a whole bunch of other stuff from the past two weeks*

Published: 2025-04-04
Source: https://simonw.substack.com/p/gemini-25-pro-pricing-a-new-gpt-4o

---

Included in this newsletter:

* Gemini 2\.5 Pro Preview pricing
* A new GPT\-4o in ChatGPT and the API
* Nomic Embed Code for code retrieval
* Microsoft's debug\-gym for Python debugging with LLMs
* Pydantic Evals
* Django 5\.2 release with composite primary keys
* CSS\-only blurry image placeholders
* "smartfunc" wrapper for LLM functions
* Advanced CSS attr() function

**Quote** 2025\-03\-26

> *MCP 🤝 OpenAI Agents SDK   
>   
> You can now connect your Model Context Protocol servers to Agents: [openai.github.io/openai\-agents\-python/mcp/](https://openai.github.io/openai-agents-python/mcp/)   
>   
> We’re also working on MCP support for the OpenAI API and ChatGPT desktop app—we’ll share some more news in the coming months.*

[@OpenAIDevs](https://twitter.com/OpenAIDevs/status/1904957755829481737)

---

**Link** 2025\-03\-26 [Function calling with Gemma](https://ai.google.dev/gemma/docs/capabilities/function-calling):

Google's Gemma 3 model (the 27B variant is particularly capable, I've been trying it out [via Ollama](https://ollama.com/library/gemma3)) supports function calling exclusively through prompt engineering. The official documentation describes two recommended prompts \- both of them suggest that the tool definitions are passed in as JSON schema, but the way the model should request tool executions differs.

The first prompt uses Python\-style function calling syntax:

> `You have access to functions. If you decide to invoke any of the function(s), you MUST put it in the format of [func_name1(params_name1=params_value1, params_name2=params_value2...), func_name2(params)]`
> 
> `You SHOULD NOT include any other text in the response if you call a function`

(Always love seeing CAPITALS for emphasis in prompts, makes me wonder if they proved to themselves that capitalization makes a difference in this case.)

The second variant uses JSON instead:

> `You have access to functions. If you decide to invoke any of the function(s), you MUST put it in the format of {"name": function name, "parameters": dictionary of argument name and its value}`
> 
> `You SHOULD NOT include any other text in the response if you call a function`

This is a neat illustration of the fact that all of these fancy tool using LLMs are still using effectively the same pattern as was described in [the ReAct paper](https://react-lm.github.io/) back in November 2022\. Here's [my implementation of that pattern](https://til.simonwillison.net/llms/python-react-pattern) from March 2023\.

---

**Link** 2025\-03\-27 [Nomic Embed Code: A State\-of\-the\-Art Code Retriever](https://www.nomic.ai/blog/posts/introducing-state-of-the-art-nomic-embed-code):

Nomic have released a new embedding model that specializes in code, based on their CoRNStack "large\-scale high\-quality training dataset specifically curated for code retrieval".

The [nomic\-embed\-code](https://huggingface.co/nomic-ai/nomic-embed-code) model is pretty large \- 26\.35GB \- but the announcement also mentioned a much smaller model (released 5 months ago) called [CodeRankEmbed](https://huggingface.co/nomic-ai/CodeRankEmbed) which is just 521\.60MB.

I missed that when it first came out, so I decided to give it a try using my [llm\-sentence\-transformers](https://github.com/simonw/llm-sentence-transformers) plugin for [LLM](https://llm.datasette.io/).

```
llm install llm-sentence-transformers
llm sentence-transformers register nomic-ai/CodeRankEmbed --trust-remote-code
```

Now I can run the model like this:

```
llm embed -m sentence-transformers/nomic-ai/CodeRankEmbed -c 'hello'
```

This outputs an array of 768 numbers, starting `[1.4794224500656128, -0.474479079246521, ...`.

Where this gets fun is combining it with my [Symbex tool](https://simonwillison.net/2023/Jun/18/symbex/) to create and then search embeddings for functions in a codebase.

I created an index for my LLM codebase like this:

```
cd llm
symbex '*' '*.*' --nl > code.txt
```

This creates a newline\-separated JSON file of all of the functions (from `'*'`) and methods (from `'*.*'`) in the current directory \- you can [see that here](https://gist.github.com/simonw/ac45c6638ea87942383e97c5cf69ae09).

Then I fed that into the [llm embed\-multi](https://llm.datasette.io/en/stable/embeddings/cli.html#llm-embed-multi) command like this:

```
llm embed-multi \
  -d code.db \
  -m sentence-transformers/nomic-ai/CodeRankEmbed \
  code code.txt \
  --format nl \
  --store \
  --batch-size 10
```

I found the `--batch-size` was needed to prevent it from crashing with an error.

The above command creates a collection called `code` in a SQLite database called `code.db`.

Having run this command I can search for functions that match a specific search term in that `code` collection like this:

```
llm similar code -d code.db \
  -c 'Represent this query for searching relevant code: install a plugin' | jq
```

That `"Represent this query for searching relevant code: "` prefix is required by the model. I pipe it through `jq` to make it a little more readable, which gives me [these results](https://gist.github.com/simonw/fdc1b48b20a99714200f5d3970b1dff4).

This `jq` recipe makes for a better output:

```
llm similar code -d code.db \
  -c 'Represent this query for searching relevant code: install a plugin' | \
  jq -r '.id + "\n\n" + .content + "\n--------\n"'
```

The output from that starts like so:

```
llm/cli.py:1776

@cli.command(name="plugins")
@click.option("--all", help="Include built-in default plugins", is_flag=True)
def plugins_list(all):
    "List installed plugins"
    click.echo(json.dumps(get_plugins(all), indent=2))
--------

llm/cli.py:1791

@cli.command()
@click.argument("packages", nargs=-1, required=False)
@click.option(
    "-U", "--upgrade", is_flag=True, help="Upgrade packages to latest version"
)
...
def install(packages, upgrade, editable, force_reinstall, no_cache_dir):
    """Install packages from PyPI into the same environment as LLM"""
```

Getting this output was quite inconvenient, so I've [opened an issue](https://github.com/simonw/llm/issues/853).

---

**Link** 2025\-03\-27 [Thoughts on setting policy for new AI capabilities](https://reservoirsamples.substack.com/p/thoughts-on-setting-policy-for-new):

Joanne Jang leads model behavior at OpenAI. Their release of GPT\-4o image generation included some notable relaxation of OpenAI's policies concerning acceptable usage \- I [noted some of those](https://simonwillison.net/2025/Mar/25/introducing-4o-image-generation/) the other day.

Joanne summarizes these changes like so:

> tl;dr we’re shifting from blanket refusals in sensitive areas to a more precise approach focused on preventing real\-world harm. The goal is to embrace humility: recognizing how much we don't know, and positioning ourselves to adapt as we learn.

This point in particular resonated with me:

> * **Trusting user creativity over our own assumptions**. AI lab employees should not be the arbiters of what people should and shouldn’t be allowed to create.

A couple of years ago when OpenAI were the only AI lab with models that were worth spending time with it really did feel that San Francisco cultural values (which I relate to myself) were being pushed on the entire world. That cultural hegemony has been broken now by the increasing pool of global organizations that can produce models, but it's still reassuring to see the leading AI lab relaxing its approach here.

---

**Link** 2025\-03\-27 [GPT\-4o got another update in ChatGPT](https://twitter.com/OpenAI/status/1905331956856050135):

This is a somewhat frustrating way to announce a new model. @OpenAI on Twitter just now:

> GPT\-4o got an another update in ChatGPT!
> 
> What's different?
> 
> * Better at following detailed instructions, especially prompts containing multiple requests
> * Improved capability to tackle complex technical and coding problems
> * Improved intuition and creativity
> * Fewer emojis 🙃

This sounds like a significant upgrade to GPT\-4o, albeit one where the release notes are limited to a single tweet.

ChatGPT\-4o\-latest (2025\-0\-26\) just hit second place on [the LM Arena leaderboard](https://lmarena.ai/?leaderboard), behind only Gemini 2\.5, so this really is an update worth knowing about.

The @OpenAIDevelopers account [confirmed](https://twitter.com/OpenAIDevs/status/1905335104211185999) that this is also now available in their API:

> `chatgpt-4o-latest` is now updated in the API, but stay tuned—we plan to bring these improvements to a dated model in the API in the coming weeks.

I [wrote about chatgpt\-4o\-latest](https://simonwillison.net/2025/Feb/17/llm/#chatgpt-4o-latest) last month \- it's a model alias in the OpenAI API which provides access to the model used for ChatGPT, available since August 2024\. It's priced at $5/million input and $15/million output \- a step up from regular GPT\-4o's $2\.50/$10\.

I'm glad they're going to make these changes available as a dated model release \- the `chatgpt-4o-latest` alias is risky to build software against due to its tendency to change without warning.

A more appropriate place for this announcement would be the [OpenAI Platform Changelog](https://platform.openai.com/docs/changelog), but that's not had an update since the release of their new audio models on March 20th.

---

**Link** 2025\-03\-27 [Tracing the thoughts of a large language model](https://www.anthropic.com/research/tracing-thoughts-language-model):

In a follow\-up to the research that brought us the [delightful Golden Gate Claude](https://simonwillison.net/2024/May/24/golden-gate-claude/) last year, Anthropic have published two new papers about LLM interpretability:

* [Circuit Tracing: Revealing Computational Graphs in Language Models](https://transformer-circuits.pub/2025/attribution-graphs/methods.html) extends last year's interpretable features into [attribution graphs](https://transformer-circuits.pub/2025/attribution-graphs/methods.html#graphs), which can "trace the chain of intermediate steps that a model uses to transform a specific input prompt into an output response".
* [On the Biology of a Large Language Model](https://transformer-circuits.pub/2025/attribution-graphs/biology.html) uses that methodology to investigate Claude 3\.5 Haiku in a bunch of different ways. [Multilingual Circuits](https://transformer-circuits.pub/2025/attribution-graphs/biology.html#dives-multilingual) for example shows that the same prompt in three different languages uses similar circuits for each one, hinting at an intriguing level of generalization.

To my own personal delight, neither of these papers are published as PDFs. They're both presented as glorious mobile friendly HTML pages with linkable sections and even some inline interactive diagrams. More of this please!

[![Screenshot of a multilingual language model visualization showing antonym prediction across three languages. Left panel shows English with prompt "The opposite of 'small' is'" predicting "large". Middle panel shows Chinese prompt "小"的反义词是" predicting "大 (zh: big)". Right panel shows French prompt "Le contraire de "petit" est" predicting "grand (fr: big)". Above shows activation analysis with token predictions and highlighted instances of "contraire" in French text.](https://substackcdn.com/image/fetch/$s_!MRJp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdafb324d-4263-4745-9192-e86cd9abbf16_2408x1088.jpeg "Screenshot of a multilingual language model visualization showing antonym prediction across three languages. Left panel shows English with prompt \"The opposite of 'small' is'\" predicting \"large\". Middle panel shows Chinese prompt \"小\"的反义词是\" predicting \"大 (zh: big)\". Right panel shows French prompt \"Le contraire de \"petit\" est\" predicting \"grand (fr: big)\". Above shows activation analysis with token predictions and highlighted instances of \"contraire\" in French text.")](https://substackcdn.com/image/fetch/$s_!MRJp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdafb324d-4263-4745-9192-e86cd9abbf16_2408x1088.jpeg)

---

**Quote** 2025\-03\-28

> *I was there at the first Atom meeting at the Google offices. We meant so well! And I think the basic publishing spec is good, certainly better technically than the pastiche of different things called RSS.   
>   
> Alas, a bunch of things then went wrong. Feeds started losing market share. Facebook started doing something useful and interesting that ultimately replaced blog feeds in open formats. The Atom vs RSS spec was at best irrelevant to most people (even programmers) and at worst a confusing market\-damaging thing. The XML namespaces in Atom made everyone annoyed. Also there was some confusing “Atom API” for publishing that diluted Atom’s mindshare for feeds.*

[Nelson Minar](https://lobste.rs/s/aygeaq/atom_vs_rss_2013#c_mxxurc)

---

**Link** 2025\-03\-28 [Incomplete JSON Pretty Printer](https://tools.simonwillison.net/incomplete-json-printer):

Every now and then a log file or a tool I'm using will spit out a bunch of JSON that terminates unexpectedly, meaning I can't copy it into a text editor and pretty\-print it to see what's going on.

The other day I got frustrated with this and had the then\-new GPT\-4\.5 build me a pretty\-printer that didn't mind incomplete JSON, using an OpenAI Canvas. Here's [the chat](https://chatgpt.com/share/67dd9d55-7f70-8006-b55d-72730f60ddbe) and here's [the resulting interactive](https://chatgpt.com/canvas/shared/67e5e9b3f7bc8191b2306a123c9d328f).

I spotted a bug with the way it indented code today so I pasted it into Claude 3\.7 Sonnet Thinking mode and had it make a bunch of improvements \- [full transcript here](https://claude.ai/share/22dc4b58-e8c4-44a4-9650-a37d21513b8d). Here's the [finished code](https://github.com/simonw/tools/blob/main/incomplete-json-printer.html).

[![Animated GIF demo - as I type JSON it is pretty printed below, at the end I click the Load Pelican Example button.](https://substackcdn.com/image/fetch/$s_!3KXv!,w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F54ecd3f4-859b-4d6c-9074-dbe350acf19b_556x600.gif "Animated GIF demo - as I type JSON it is pretty printed below, at the end I click the Load Pelican Example button.")](https://substackcdn.com/image/fetch/$s_!3KXv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F54ecd3f4-859b-4d6c-9074-dbe350acf19b_556x600.gif)

In many ways this is a perfect example of [vibe coding](https://simonwillison.net/2025/Mar/19/vibe-coding/) in action. At no point did I look at a *single line* of code that either of the LLMs had written for me. I honestly don't care how this thing works: it could not be lower stakes for me, the worst a bug could do is show me poorly formatted incomplete JSON.

I was vaguely aware that some kind of state machine style parser would be needed, because you can't parse incomplete JSON with a regular JSON parser. Building simple parsers is the kind of thing LLMs are surprisingly good at, and also the kind of thing I don't want to take on for a trivial project.

At one point I told Claude "Try using your code execution tool to check your logic", because I happen to know Claude can write and then execute JavaScript independently of using it for artifacts. That helped it out a bunch.

I later dropped in the following:

> `modify the tool to work better on mobile screens and generally look a bit nicer - and remove the pretty print JSON button, it should update any time the input text is changed. Also add a "copy to clipboard" button next to the results. And add a button that says "example" which adds a longer incomplete example to demonstrate the tool, make that example pelican themed.`

It's fun being able to say "generally look a bit nicer" and get a perfectly acceptable result!

---

**Quote** 2025\-03\-28

> *Slop is about collapsing to the mode. It’s about information heat death. It’s lukewarm emptiness. It’s ten million approximately identical cartoon selfies that no one will ever recall in detail because none of the details matter.*

[Colin Fraser](https://twitter.com/colin_fraser/status/1905158970337083676)

---

**Quote** 2025\-03\-30

> *My advice about using AI is simple: use AI as an assistant, not an expert, and use it judiciously. Some people will object, “but AI can be wrong!” Yes, and so can the internet in general, but no one now recommends avoiding online resources because they can be wrong. They recommend taking it all with a grain of salt and being careful. That’s what you should do with AI help as well.*

[Ned Batchelder](https://nedbatchelder.com/blog/202503/horseless_intelligence.html)

---

**Link** 2025\-03\-31 [debug\-gym](https://microsoft.github.io/debug-gym/):

New paper and code from Microsoft Research that experiments with giving LLMs access to the Python debugger. They found that the best models could indeed improve their results by running pdb as a tool.

They saw the best results overall from Claude 3\.7 Sonnet against [SWE\-bench Lite](https://www.swebench.com/lite.html), where it scored 37\.2% in rewrite mode without a debugger, 48\.4% with their debugger tool and 52\.1% with debug(5\) \- a mechanism where the pdb tool is made available only after the 5th rewrite attempt.

Their code is [available on GitHub](https://github.com/microsoft/debug-gym). I found this implementation of [the pdb tool](https://github.com/microsoft/debug-gym/blob/1.0.0/debug_gym/gym/tools/pdb.py), and tracked down the main system and user prompt in [agents/debug\_agent.py](https://github.com/microsoft/debug-gym/blob/1.0.0/debug_gym/agents/debug_agent.py):

System prompt:

> `Your goal is to debug a Python program to make sure it can pass a set of test functions. You have access to the pdb debugger tools, you can use them to investigate the code, set breakpoints, and print necessary values to identify the bugs. Once you have gained enough information, propose a rewriting patch to fix the bugs. Avoid rewriting the entire code, focus on the bugs only.`

User prompt (which they call an "action prompt"):

> `Based on the instruction, the current code, the last execution output, and the history information, continue your debugging process using pdb commands or to propose a patch using rewrite command. Output a single command, nothing else. Do not repeat your previous commands unless they can provide more information. You must be concise and avoid overthinking.`

---

**Quote** 2025\-04\-01

> *We’re planning to release a very capable open language model in the coming months, our first since GPT\-2\. \[...]   
>   
> As models improve, there is more and more demand to run them everywhere. Through conversations with startups and developers, it became clear how important it was to be able to support a spectrum of needs, such as custom fine\-tuning for specialized tasks, more tunable latency, running on\-prem, or deployments requiring full data control.*

[Brad Lightcap](https://twitter.com/bradlightcap/status/1906823733446427065)

---

**Link** 2025\-04\-01 [Pydantic Evals](https://ai.pydantic.dev/evals/):

Brand new package from David Montague and the Pydantic AI team which directly tackles what I consider to be the single hardest problem in AI engineering: building evals to determine if your LLM\-based system is working correctly and getting better over time.

The feature is described as "in beta" and comes with this very realistic warning:

> Unlike unit tests, evals are an emerging art/science; anyone who claims to know for sure exactly how your evals should be defined can safely be ignored.

This code example from their documentation illustrates the relationship between the two key nouns \- Cases and Datasets:

```
from pydantic_evals import Case, Dataset

case1 = Case(
    name="simple_case",
    inputs="What is the capital of France?",
    expected_output="Paris",
    metadata={"difficulty": "easy"},
)

dataset = Dataset(cases=[case1])
```

The library also supports custom evaluators, including LLM\-as\-a\-judge:

```
Case(
    name="vegetarian_recipe",
    inputs=CustomerOrder(
        dish_name="Spaghetti Bolognese", dietary_restriction="vegetarian"
    ),
    expected_output=None,
    metadata={"focus": "vegetarian"},
    evaluators=(
        LLMJudge(
            rubric="Recipe should not contain meat or animal products",
        ),
    ),
)
```

Cases and datasets can also be serialized to YAML.

My first impressions are that this looks like a solid implementation of a sensible design. I'm looking forward to trying it out against a real project.

---

**Link** 2025\-04\-01 [Half Stack Data Science: Programming with AI, with Simon Willison](https://halfstackdatascience.com/s4e2-programming-with-ai-with-simon-willison):

I participated in this wide\-ranging 50 minute conversation with David Asboth and Shaun McGirr. Topics we covered included applications of LLMs to data journalism, the challenges of building an intuition for how best to use these tool given their "jagged frontier" of capabilities, how LLMs impact learning to program and how local models are starting to get genuinely useful now.

At [27:47](https://overcast.fm/+AAnGvyyrHkg/27:47):

> If you're a new programmer, my optimistic version is that there has never been a better time to learn to program, because it shaves down the learning curve so much. When you're learning to program and you miss a semicolon and you bang your head against the computer for four hours \[...] if you're unlucky you quit programming for good because it was so frustrating. \[...]
> 
> I've always been a project\-oriented learner; I can learn things by building something, and now the friction involved in building something has gone down so much \[...] So I think especially if you're an autodidact, if you're somebody who likes teaching yourself things, these are a gift from heaven. You get a weird teaching assistant that knows loads of stuff and occasionally makes weird mistakes and believes in bizarre conspiracy theories, but you have 24 hour access to that assistant.
> 
> If you're somebody who prefers structured learning in classrooms, I think the benefits are going to take a lot longer to get to you because we don't know how to use these things in classrooms yet. \[...]
> 
> If you want to strike out on your own, this is an amazing tool *if* you learn how to learn with it. So you've got to learn the limits of what it can do, and you've got to be disciplined enough to make sure you're not outsourcing the bits you need to learn to the machines.

---

**Link** 2025\-04\-02 [Composite primary keys in Django](https://docs.djangoproject.com/en/5.2/topics/composite-primary-key/):

Django 5\.2 is [out today](https://www.djangoproject.com/weblog/2025/apr/02/django-52-released/) and a big new feature is composite primary keys, which can now be defined like this:

```
class Release(models.Model):
    pk = models.CompositePrimaryKey(
        "version", "name"
    )
    version = models.IntegerField()
    name = models.CharField(max_length=20)
```

They don't yet work with the Django admin or as targets for foreign keys.

Other smaller new features include:

* All ORM models are now automatically imported into `./manage.py shell` \- a feature borrowed from `./manage.py shell_plus` in [django\-extensions](https://django-extensions.readthedocs.io/)
* Feeds from the Django syndication framework can now specify [XSLT stylesheets](https://docs.djangoproject.com/en/5.2/ref/contrib/syndication/#feed-stylesheets)
* [response.text](https://docs.djangoproject.com/en/5.2/ref/request-response/#django.http.HttpResponse.text) now returns the string representation of the body \- I'm so happy about this, now I don't have to litter my Django tests with `response.content.decode("utf-8")` any more
* a new [simple\_block\_tag](https://docs.djangoproject.com/en/5.2/howto/custom-template-tags/#django.template.Library.simple_block_tag) helper making it much easier to create a custom Django template tag that further processes its own inner rendered content
* A bunch more in the [full release notes](https://docs.djangoproject.com/en/5.2/releases/5.2/)

5\.2 is also an LTS release, so it will receive security and data loss bug fixes up to April 2028\.

---

**Quote** 2025\-04\-03

> *I started using Claude and Claude Code a bit in my regular workflow. I’ll skip the suspense and just say that the tool is way more capable than I would ever have expected. The way I can use it to interrogate a large codebase, or generate unit tests, or even “refactor every callsite to use such\-and\-such pattern” is utterly gobsmacking. \[...]   
>   
> Here’s the main problem I’ve found with generative AI, and with “vibe coding” in general: it completely sucks out the joy of software development for me. \[...]   
>   
> This is how I feel using gen\-AI: like a babysitter. It spits out reams of code, I read through it and try to spot the bugs, and then we repeat.*

[Nolan Lawson](https://nolanlawson.com/2025/04/02/ai-ambivalence/)

---

**Link** 2025\-04\-03 [Minimal CSS\-only blurry image placeholders](https://leanrada.com/notes/css-only-lqip/):

Absolutely brilliant piece of CSS ingenuity by Lean Rada, who describes a way to implement blurry placeholder images using just CSS, with syntax like this:

```
<img src="…" style="--lqip:192900">
```

That 192900 number encodes everything needed to construct the placeholder \- it manages to embed a single base color and six brightness components (in a 3x2 grid) in 20 bits, then encodes those as an integer in the roughly 2 million available values between \-999,999 and 999,999 \- beyond which range Lean found some browsers would start to lose precision.

The implementation for decoding that value becomes a bunch of clever bit\-fiddling CSS expressions to expand it into further CSS variables:

```
[style*="--lqip:"] {
  --lqip-ca: mod(round(down, calc((var(--lqip) + pow(2, 19)) / pow(2, 18))), 4);
  --lqip-cb: mod(round(down, calc((var(--lqip) + pow(2, 19)) / pow(2, 16))), 4);
  /* more like that */
}
```

Which are expanded to even more variables with code like this:

```
--lqip-ca-clr: hsl(0 0% calc(var(--lqip-ca) / 3 * 100%));
--lqip-cb-clr: hsl(0 0% calc(var(--lqip-cb) / 3 * 100%));
```

And finally rendered using a CSS gradient definition that starts like this:

```
[style*="--lqip:"] {
  background-image:
    radial-gradient(50% 75% at 16.67% 25%, var(--lqip-ca-clr), transparent),
    radial-gradient(50% 75% at 50% 25%, var(--lqip-cb-clr), transparent),
    /* ... */
    linear-gradient(0deg, var(--lqip-base-clr), var(--lqip-base-clr));
}
```

The article includes several interactive explainers (most of which are also powered by pure CSS) illustrating how it all works.

Their [Node.js script](https://github.com/Kalabasa/leanrada.com/blob/7b6739c7c30c66c771fcbc9e1dc8942e628c5024/main/scripts/update/lqip.mjs#L118-L159) for converting images to these magic integers uses [Sharp](https://www.npmjs.com/package/sharp) to resize the image to 3x2 and then use the [Oklab perceptually uniform color space](https://en.m.wikipedia.org/wiki/Oklab_color_space) (new to me, that was created by Björn Ottosson in 2020\) to derive the six resulting values.

---

**Link** 2025\-04\-03 [smartfunc](https://github.com/koaning/smartfunc):

Vincent D. Warmerdam built this ingenious wrapper around my [LLM Python library](https://llm.datasette.io/en/stable/python-api.html) which lets you build LLM wrapper functions using a decorator and a docstring:

```
from smartfunc import backend

@backend("gpt-4o")
def generate_summary(text: str):
    """Generate a summary of the following text: {{ text }}"""
    pass

summary = generate_summary(long_text)
```

It works with [LLM plugins](https://llm.datasette.io/en/stable/plugins/directory.html) so the same pattern should work against Gemini, Claude and hundreds of others, including local models.

It integrates with more recent LLM features too, including [async support](https://llm.datasette.io/en/stable/python-api.html#python-api-async) and [schemas](https://simonwillison.net/2025/Feb/28/llm-schemas/), by introspecting the function signature:

```
class Summary(BaseModel):
    summary: str
    pros: list[str]
    cons: list[str]

@async_backend("gpt-4o-mini")
async def generate_poke_desc(text: str) -> Summary:
    "Describe the following pokemon: {{ text }}"
    pass

pokemon = await generate_poke_desc("pikachu")
```

Vincent also recorded [a 12 minute video](https://www.youtube.com/watch?v=j9jh46R0ryY) walking through the implementation and showing how it uses [Pydantic](https://docs.pydantic.dev/), Python's [inspect](https://docs.python.org/3/library/inspect.html) module and [typing.get\_type\_hints()](https://docs.python.org/3/library/typing.html#typing.get_type_hints) function.

---

**Link** 2025\-04\-03 [First look at the modern attr()](https://ishadeed.com/article/modern-attr/):

Chrome 133 (released February 25th 2025\) was the first browser to [ship support](https://developer.chrome.com/release-notes/133?hl=en#css_advanced_attr_function) for the advanced CSS `attr()` function ([MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/attr)), which lets `attr()` be used to compose values using types other than strings.

Ahmad Shadeed explores potential applications of this in detail, trying it out for CSS grid columns, progress bars, background images, animation delays and more.

I like this example that uses the `rows="5"` attribute on a `<textarea>` to calculate its `max-height` \- here wrapped in a feature detection block:

```
@supports (x: attr(x type(*))) {
  textarea {
    min-height: calc(
      attr(rows type(<number>)) * 50px
    );
  }
}
```

That `type(<number>)` is the new syntax.

Many of Ahmad's examples can be achieved today across all browsers using a slightly more verbose CSS custom property syntax.

Here are the tracking issues for CSS values support in `attr()` for [Firefox](https://bugzilla.mozilla.org/show_bug.cgi?id=435426) (opened 17 years ago) and [WebKit](https://bugs.webkit.org/show_bug.cgi?id=26609) (16 years ago).

---

**Link** 2025\-04\-04 [A Sneaky Phish Just Grabbed my Mailchimp Mailing List](https://www.troyhunt.com/a-sneaky-phish-just-grabbed-my-mailchimp-mailing-list/):

In further evidence that phishing attacks can catch out the *most* sophisticated among us, security researcher (and operator of [';\-\-have i been pwned?](https://haveibeenpwned.com/)) Troy Hunt reports on how he fell for an extremely well crafted phishing attack against his MailChimp account which then exported his full list of subscribers, including people who had unsubscribed (data which MailChimp stores and continues to make available).

This could happen to any of us:

> I've received a gazillion similar phishes before that I've identified early, so what was different about this one? Tiredness, was a major factor. I wasn't alert enough, and I didn't properly think through what I was doing.

Troy's account was protected by authenticator app 2FA, but the phishing site (on the realistic sounding `mailchimp-sso.com` domain) asked for that code too and instantly proxied it through to MailChimp \- somewhat ironic as Troy had been promoting phishing\-resistant passkeys on his trip to London, a technology that MailChimp doesn't offer yet.

There are a bunch of interesting details here. I appreciated this point about how short\-lived authentication sessions can *reduce* account security by conditioning users to expect constant login requests:

> I also realised another factor that pre\-conditioned me to enter credentials into what I thought was Mailchimp is their very short\-lived authentication sessions. Every time I go back to the site, I need to re\-authenticate and whilst the blame still clearly lies with me, I'm used to logging back in on every visit. Keeping a trusted device auth'd for a longer period would likely have raised a flag on my return to the site if I wasn't still logged in.

It looks like MailChimp preserve the email addresses of unsubscribed users to prevent them from being re\-subscribed by future list imports. Troy discusses this issue at length in further updates to the post.

Also interesting: this [article by DNS forensics company Validin](https://www.validin.com/blog/pulling_threads_on_phishing_campaign/) which tracks down the responsible group using DNS records and other hints such as title tags and favicon hashes.

---

**Link** 2025\-04\-04 [Gemini 2\.5 Pro Preview pricing](https://ai.google.dev/gemini-api/docs/pricing#gemini-2.5-pro-preview):

Google's Gemini 2\.5 Pro is currently the top model [on LM Arena](https://lmarena.ai/?leaderboard) and, from [my own testing](https://simonwillison.net/2025/Mar/25/gemini/), a superb model for OCR, audio transcription and long\-context coding.

You can now pay for it!

The new `gemini-2.5-pro-preview-03-25` model ID is priced like this:

* Prompts less than 200,00 tokens: $1\.25/million tokens for input, $10/million for output
* Prompts more than 200,000 tokens (up to the 1,048,576 max): $2\.50/million for input, $15/million for output

This is priced at around the same level as Gemini 1\.5 Pro ($1\.25/$5 for input/output below 128,000 tokens, $2\.50/$10 above 128,000 tokens), is cheaper than GPT\-4o for shorter prompts ($2\.50/$10\) and is cheaper than Claude 3\.7 Sonnet ($3/$15\).

Gemini 2\.5 Pro is a reasoning model, and invisible reasoning tokens are included in the output token count. I just tried prompting "hi" and it charged me 2 tokens for input and 623 for output, of which 613 were "thinking" tokens. That still adds up to just 0\.6232 cents (less than a cent) using my [LLM pricing calculator](https://tools.simonwillison.net/llm-prices) which I updated to support the new model just now.

I released [llm\-gemini 0\.17](https://github.com/simonw/llm-gemini/releases/tag/0.17) this morning adding support for the new model:

```
llm install -U llm-gemini
llm -m gemini-2.5-pro-preview-03-25 hi
```

Note that the model continues to be available for free under the previous `gemini-2.5-pro-exp-03-25` model ID:

```
llm -m gemini-2.5-pro-exp-03-25 hi
```

The free tier is "used to improve our products", the paid tier is not.

Rate limits for the paid model [vary by tier](https://ai.google.dev/gemini-api/docs/rate-limits#tier-1) \- from 150/minute and 1,000/day for tier 1 (billing configured), 1,000/minute and 50,000/day for Tier 2 ($250 total spend) and 2,000/minute and unlimited/day for Tier 3 ($1,000 total spend). Meanwhile the free tier continues to limit you to 5 requests per minute and 25 per day.

Google are [retiring the Gemini 2\.0 Pro preview](https://twitter.com/OfficialLoganK/status/1908179750536827183) entirely in favour of 2\.5\.

---

**Quote** 2025\-04\-04

> *change of plans: we are going to release o3 and o4\-mini after all, probably in a couple of weeks, and then do GPT\-5 in a few months*

[Sam Altman](https://twitter.com/sama/status/1908167621624856998)

---