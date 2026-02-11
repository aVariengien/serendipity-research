# Structured data extraction from unstructured content using LLM schemas

*Plus initial impressions of GPT-4.5*

Published: 2025-02-28
Source: https://simonw.substack.com/p/structured-data-extraction-from-unstructured

---

In this newsletter:

* Structured data extraction from unstructured content using LLM schemas
* Initial impressions of GPT\-4\.5

Plus 7 links and 2 quotations

### [Structured data extraction from unstructured content using LLM schemas](https://simonwillison.net/2025/Feb/28/llm-schemas/) \- 2025\-02\-28

[LLM 0\.23](https://llm.datasette.io/en/stable/changelog.html#v0-23) is out today, and the signature feature is support for **[schemas](https://llm.datasette.io/en/stable/schemas.html)** \- a new way of providing structured output from a model that matches a specification provided by the user. I've also upgraded both the [llm\-anthropic](https://github.com/simonw/llm-anthropic) and [llm\-gemini](https://github.com/simonw/llm-gemini) plugins to add support for schemas.

TLDR: you can now do things like this:

```
llm --schema 'name,age int,short_bio' 'invent a cool dog'
```

And get back:

```
{
  "name": "Zylo",
  "age": 4,
  "short_bio": "Zylo is a unique hybrid breed, a mix between a Siberian Husky and a Corgi. With striking blue eyes and a fluffy, colorful coat that changes shades with the seasons, Zylo embodies the spirit of winter and summer alike. Known for his playful personality and intelligence, Zylo can perform a variety of tricks and loves to fetch his favorite frisbee. Always ready for an adventure, he's just as happy hiking in the mountains as he is cuddling on the couch after a long day of play."
}
```

More details [in the release notes](https://llm.datasette.io/en/stable/changelog.html#v0-23) and [LLM schemas tutorial](https://llm.datasette.io/en/stable/schemas.html#schemas-tutorial), which includes an example (extracting people from news articles) that's even more useful than inventing dogs!

* [Structured data extraction is a killer app for LLMs](https://simonwillison.net/2025/Feb/28/llm-schemas/#structured-data-extraction-is-a-killer-app-for-llms)
* [Designing this feature for LLM](https://simonwillison.net/2025/Feb/28/llm-schemas/#designing-this-feature-for-llm)
* [Reusing schemas and creating templates](https://simonwillison.net/2025/Feb/28/llm-schemas/#reusing-schemas-and-creating-templates)
* [Doing more with the logged structured data](https://simonwillison.net/2025/Feb/28/llm-schemas/#doing-more-with-the-logged-structured-data)
* [Using schemas from LLM's Python library](https://simonwillison.net/2025/Feb/28/llm-schemas/#using-schemas-from-llm-s-python-library)
* [What's next for LLM schemas?](https://simonwillison.net/2025/Feb/28/llm-schemas/#what-s-next-for-llm-schemas-)

#### Structured data extraction is a killer app for LLMs

I've suspected for a while that the single most commercially valuable application of LLMs is turning unstructured content into structured data. That's the trick where you feed an LLM an article, or a PDF, or a screenshot and use it to turn that into JSON or CSV or some other structured format.

It's possible to achieve strong results on this with prompting alone: feed data into an LLM, give it an example of the output you would like and let it figure out the details.

Many of the leading LLM providers now bake this in as a feature. OpenAI, Anthropic, Gemini and Mistral all offer variants of "structured output" as additional options through their API:

* OpenAI: [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)
* Gemini: [Generate structured output with the Gemini API](https://ai.google.dev/gemini-api/docs/structured-output?lang=rest)
* Mistral: [Custom Structured Outputs](https://docs.mistral.ai/capabilities/structured-output/custom_structured_output/)
* Anthropic's [tool use](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview) can be used for this, as shown in their [Extracting Structured JSON using Claude and Tool Use](https://github.com/anthropics/anthropic-cookbook/blob/main/tool_use/extracting_structured_json.ipynb) cookbook example.

These mechanisms are all very similar: you pass a [JSON schema](https://json-schema.org/) to the model defining the shape that you would like, they then use that schema to guide the output of the model.

How reliable that is can vary! Some providers use tricks along the lines of [Jsonformer](https://github.com/1rgs/jsonformer), compiling the JSON schema into code that interacts with the model's next\-token generation at runtime, limiting it to only generate tokens that are valid in the context of the schema.

Other providers YOLO it \- they trust that their model is "good enough" that showing it the schema will produce the right results!

In practice, this means that you need to be aware that sometimes this stuff will go wrong. As with anything LLM, 100% reliability is never guaranteed.

From my experiments so far, and depending on the model that you chose, these mistakes are rare. If you're using a top tier model it will almost certainly do the right thing.

#### Designing this feature for LLM

I've wanted this feature for ages. I see it as an important step on the way to full tool usage, which is something I'm very excited to bring to the CLI tool and Python library.

LLM is designed as an abstraction layer over different models. This makes building new features *much harder*, because I need to figure out a common denominator and then build an abstraction that captures as much value as possible while still being general enough to work across multiple models.

Support for structured output across multiple vendors has matured now to the point that I'm ready to commit to a design.

My first version of this feature worked exclusively with JSON schemas. An earlier version of the tutorial started with this example:

```
curl https://www.nytimes.com/ | uvx strip-tags | \
  llm --schema '{
  "type": "object",
  "properties": {
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "headline": {
            "type": "string"
          },
          "short_summary": {
            "type": "string"
          },
          "key_points": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": ["headline", "short_summary", "key_points"]
      }
    }
  },
  "required": ["items"]
}' | jq
```

Here we're feeding a full JSON schema document to the new `llm --schema` option, then piping in the homepage of the New York Times (after running it through [strip\-tags](https://github.com/simonw/strip-tags)) and asking for `headline`, `short_summary` and `key_points` for multiple items on the page.

This example still works with the finished feature \- you can see [example JSON output here](https://gist.github.com/simonw/372d11e2729a9745654740ff3f5669ab) \- but constructing those long\-form schemas by hand was a big pain.

So... I invented my own shortcut syntax.

That earlier example is a simple illustration:

```
llm --schema 'name,age int,short_bio' 'invent a cool dog'
```

Here the schema is a comma\-separated list of field names, with an optional space\-separated type.

The full concise schema syntax [is described here](https://llm.datasette.io/en/stable/schemas.html#concise-llm-schema-syntax). There's a more complex example [in the tutorial](https://llm.datasette.io/en/latest/schemas.html#extracting-people-from-a-news-articles), which uses the newline\-delimited form to extract information about people who are mentioned in a news article:

```
curl 'https://apnews.com/article/trump-federal-employees-firings-a85d1aaf1088e050d39dcf7e3664bb9f' | \
  uvx strip-tags | \
  llm --schema-multi "
name: the person's name
organization: who they represent
role: their job title or role
learned: what we learned about them from this story
article_headline: the headline of the story
article_date: the publication date in YYYY-MM-DD
" --system 'extract people mentioned in this article'
```

The `--schema-multi` option here tells LLM to take that schema for a single object and upgrade it to an array of those objects (actually an object with a single `"items"` property that's an array of objects), which is a quick way to request that the same schema be returned multiple times against a single input.

#### Reusing schemas and creating templates

My original plan with schemas was to provide a separate `llm extract` command for running these kinds of operations. I ended up going in a different direction \- I realized that adding `--schema` to the default `llm prompt` command would make it interoperable with other existing features (like [attachments](https://llm.datasette.io/en/stable/usage.html#attachments) for feeding in images and PDFs).

The most valuable way to apply schemas is across many different prompts, in order to gather the same structure of information from many different sources.

I put a bunch of thought into the `--schema` option. It takes a variety of different values \- quoting [the documentation](https://llm.datasette.io/en/latest/schemas.html#ways-to-specify-a-schema):

> This option can take multiple forms:
> 
> * A string providing a JSON schema: `--schema '{"type": "object", ...}'`
> * A [condensed schema definition](https://llm.datasette.io/en/stable/schemas.html#schemas-dsl): `--schema 'name,age int'`
> * The name or path of a file on disk containing a JSON schema: `--schema dogs.schema.json`
> * The hexadecimal ID of a previously logged schema: `--schema 520f7aabb121afd14d0c6c237b39ba2d` \- these IDs can be found using the `llm schemas` command.

* A schema that has been [saved in a template](https://llm.datasette.io/en/latest/templates.html#prompt-templates-save): `--schema t:name-of-template`

The [tutorial](https://llm.datasette.io/en/latest/schemas.html#extracting-people-from-a-news-articles) demonstrates saving a schema by using it once and then obtaining its ID through the new `llm schemas` command, then saving it to a [template](https://llm.datasette.io/en/stable/templates.html) (along with the system prompt) like this:

```
llm --schema 3b7702e71da3dd791d9e17b76c88730e \
  --system 'extract people mentioned in this article' \
  --save people
```

And now we can feed in new articles using the `llm -t people` shortcut to apply that newly saved template:

```
curl https://www.theguardian.com/commentisfree/2025/feb/27/billy-mcfarland-new-fyre-festival-fantasist | \
  strip-tags | llm -t people
```

#### Doing more with the logged structured data

Having run a few prompts that use the same schema, an obvious next step is to do something with the data that has been collected.

I ended up implementing this on top of the existing [llm logs](https://llm.datasette.io/en/stable/logging.html) mechanism.

LLM already defaults to logging every prompt and response it makes to a SQLite database \- mine contains over 4,747 of these records now, according to this query:

```
sqlite3 "$(llm logs path)" 'select count(*) from responses'
```

With schemas, an increasing portion of those are valid JSON.

Since LLM records the schema that was used for each response \- using the schema ID, which is derived from a content hash of the expanded JSON schema \- it's now possible to ask LLM for all responses that used a particular schema:

```
llm logs --schema 3b7702e71da3dd791d9e17b76c88730e --short
```

I got back:

```
- model: gpt-4o-mini
  datetime: '2025-02-28T07:37:18'
  conversation: 01jn5qt397aaxskf1vjp6zxw2a
  system: extract people mentioned in this article
  prompt: Menu AP Logo Menu World U.S. Politics Sports Entertainment Business Science
    Fact Check Oddities Be Well Newsletters N...
- model: gpt-4o-mini
  datetime: '2025-02-28T07:38:58'
  conversation: 01jn5qx4q5he7yq803rnexp28p
  system: extract people mentioned in this article
  prompt: Skip to main contentSkip to navigationSkip to navigationPrint subscriptionsNewsletters
    Sign inUSUS editionUK editionA...
- model: gpt-4o
  datetime: '2025-02-28T07:39:07'
  conversation: 01jn5qxh20tksb85tf3bx2m3bd
  system: extract people mentioned in this article
  attachments:
  - type: image/jpeg
    url: https://static.simonwillison.net/static/2025/onion-zuck.jpg
```

As you can see, I've run that example schema three times (while constructing the tutorial) using GPT\-4o mini \- twice against text content from `curl ... | strip-tags` and once against [a screenshot JPEG](https://static.simonwillison.net/static/2025/onion-zuck.jpg) to demonstrate attachment support.

Extracting gathered JSON from the logs is clearly a useful next step... so I added several options to `llm logs` to support that use\-case.

The first is `--data` \- adding that will cause `LLM logs` to output just the data that was gathered using a schema. Mix that with `-c` to see the JSON from the most recent response:

```
llm logs -c --data
```

Outputs:

```
{"name": "Zap", "age": 5, "short_bio": ...
```

Combining that with the `--schema` option is where things get really interesting. You can specify a schema using any of the mechanisms described earlier, which means you can see ALL of the data gathered using that schema by combining `--data` with `--schema X` (and `-n 0` for everything).

Here are all of the dogs I've invented:

```
llm logs --schema 'name,age int,short_bio' --data -n 0
```

Output (here truncated):

```
{"name": "Zap", "age": 5, "short_bio": "Zap is a futuristic ..."}
{"name": "Zephyr", "age": 3, "short_bio": "Zephyr is an adventurous..."}
{"name": "Zylo", "age": 4, "short_bio": "Zylo is a unique ..."}
```

Some schemas gather multiple items, producing output that looks like this (from the tutorial):

```
{"items": [{"name": "Mark Zuckerberg", "organization": "...
{"items": [{"name": "Billy McFarland", "organization": "...
```

We can get back the individual objects by adding `--data-key items`. Here I'm also using the `--schema t:people` shortcut to specify the schema that was saved to the `people` template earlier on.

```
llm logs --schema t:people --data-key items
```

Output:

```
{"name": "Katy Perry", "organization": ...
{"name": "Gayle King", "organization": ...
{"name": "Lauren Sanchez", "organization": ...
```

This feature defaults to outputting newline\-delimited JSON, but you can add the `--data-array` flag to get back a JSON array of objects instead.

... which means you can pipe it into [sqlite\-utils insert](https://sqlite-utils.datasette.io/en/stable/cli.html#inserting-json-data) to create a SQLite database!

```
llm logs --schema t:people --data-key items --data-array | \
  sqlite-utils insert data.db people -
```

Add all of this together and we can construct a schema, run it against a bunch of sources and dump the resulting structured data into SQLite where we can explore it using SQL queries (and [Datasette](https://datasette.io/)). It's a really powerful combination.

#### Using schemas from LLM's Python library

The most popular way to work with schemas in Python these days is with [Pydantic](https://docs.pydantic.dev/), to the point that many of the official API libraries for models directly incorporate Pydantic for this purpose.

LLM depended on Pydantic already, and for this project I finally dropped my dual support for Pydantic v1 and v2 and [committed to v2 only](https://github.com/simonw/llm/pull/775).

A key reason Pydantic for this is so popular is that it's trivial to use it to build a JSON schema document:

```
import pydantic, json

class Dog(pydantic.BaseModel):
    name: str
    age: int
    bio: str

schema = Dog.model_json_schema()
print(json.dumps(schema, indent=2))
```

Outputs:

```
{
  "properties": {
    "name": {
      "title": "Name",
      "type": "string"
    },
    "age": {
      "title": "Age",
      "type": "integer"
    },
    "bio": {
      "title": "Bio",
      "type": "string"
    }
  },
  "required": [
    "name",
    "age",
    "bio"
  ],
  "title": "Dog",
  "type": "object"
}
```

LLM's Python library doesn't require you to use Pydantic, but it supports passing either a Pydantic `BaseModel` subclass or a full JSON schema to the new `model.prompt(schema=)` parameter. Here's [the usage example](https://llm.datasette.io/en/latest/python-api.html#schemas) from the documentation:

```
import llm, json
from pydantic import BaseModel

class Dog(BaseModel):
    name: str
    age: int

model = llm.get_model("gpt-4o-mini")
response = model.prompt("Describe a nice dog", schema=Dog)
dog = json.loads(response.text())
print(dog)
# {"name":"Buddy","age":3}
```

#### What's next for LLM schemas?

So far I've implemented schema support for models from OpenAI, Anthropic and Gemini. The [plugin author documentation](https://llm.datasette.io/en/stable/plugins/advanced-model-plugins.html#supporting-schemas) includes details on how to add this to further plugins \- I'd love to see one of the local model plugins implement this pattern as well.

I'm presenting a workshop at the [NICAR 2025](https://www.ire.org/training/conferences/nicar-2025/) data journalism conference next week about [Cutting\-edge web scraping techniques](https://github.com/simonw/nicar-2025-scraping/). LLM schemas is a great example of NDD \- NICAR\-Driven Development \- where I'm churning out features I need for that conference (see also shot\-scraper's new [HAR support](https://shot-scraper.datasette.io/en/stable/har.html)).

I expect the workshop will be a great opportunity to further refine the design and implementation of this feature!

I'm also going to be using this new feature to add multiple model support to my [datasette\-extract plugin](https://www.datasette.cloud/blog/2024/datasette-extract/), which provides a web UI for structured data extraction that writes the resulting records directly to a SQLite database table.

---

### [Initial impressions of GPT\-4\.5](https://simonwillison.net/2025/Feb/27/introducing-gpt-45/) \- 2025\-02\-27

GPT\-4\.5 [is out today](https://openai.com/index/introducing-gpt-4-5/) as a "research preview" \- it's available to OpenAI Pro ($200/month) customers and to developers with an API key. OpenAI also published [a GPT\-4\.5 system card](https://openai.com/index/gpt-4-5-system-card/).

I've started work [adding it to LLM](https://github.com/simonw/llm/issues/795) but I don't have a full release out yet. For the moment you can try it out via [uv](https://docs.astral.sh/uv/) like this:

```
uvx --with 'https://github.com/simonw/llm/archive/801b08bf40788c09aed6175252876310312fe667.zip' \
  llm -m gpt-4.5-preview 'impress me'
```

It's *very* expensive right now: [currently](https://openai.com/api/pricing/) $75\.00 per million input tokens and $150/million for output! For comparison, o1 is $15/$60 and GPT\-4o is $2\.50/$10\. GPT\-4o mini is $0\.15/$0\.60 making OpenAI's least expensive model 500x cheaper than GPT\-4\.5 for input and 250x cheaper for output!

As far as I can tell almost all of its key characteristics are the same as GPT\-4o: it has the same 128,000 context length, handles the same inputs (text and image) and even has the same training cut\-off date of October 2023\.

So what's it better at? According to OpenAI's blog post:

> Combining deep understanding of the world with improved collaboration results in a model that integrates ideas naturally in warm and intuitive conversations that are more attuned to human collaboration. GPT‑4\.5 has a better understanding of what humans mean and interprets subtle cues or implicit expectations with greater nuance and “EQ”. GPT‑4\.5 also shows stronger aesthetic intuition and creativity. It excels at helping with writing and design.

They include this chart of win\-rates against GPT\-4o, where it wins between 56\.8% and 63\.2% of the time for different classes of query:

[![Bar chart showing GPT-4.5 win-rate vs GPT-4o across three categories: Everyday queries (57.0%), Professional queries (63.2%), and Creative intelligence (56.8%).](https://substackcdn.com/image/fetch/$s_!nJ44!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe3e25e9b-c371-4e28-a496-5823670133ab_1240x852.jpeg "Bar chart showing GPT-4.5 win-rate vs GPT-4o across three categories: Everyday queries (57.0%), Professional queries (63.2%), and Creative intelligence (56.8%).")](https://substackcdn.com/image/fetch/$s_!nJ44!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe3e25e9b-c371-4e28-a496-5823670133ab_1240x852.jpeg)

They also report a SimpleQA hallucination rate of 37\.1% \- a big improvement on GPT\-4o (61\.8%) and o3\-mini (80\.3%) but not much better than o1 (44%). The coding benchmarks all appear to score similar to o3\-mini.

Paul Gauthier [reports](https://twitter.com/paulgauthier/status/1895221869844013108) a score of 45% on Aider's [polyglot coding benchmark](https://aider.chat/docs/leaderboards/) \- below DeepSeek V3 (48%), Sonnet 3\.7 (60% without thinking, 65% with thinking) and o3\-mini (60\.4%) but significantly ahead of GPT\-4o (23\.1%).

OpenAI don't seem to have enormous confidence in the model themselves:

> GPT‑4\.5 is a very large and compute\-intensive model, making it more [expensive⁠](https://openai.com/api/pricing/) than and not a replacement for GPT‑4o. Because of this, we're evaluating whether to continue serving it in the API long\-term as we balance supporting current capabilities with building future models.

It drew me this for "Generate an SVG of a pelican riding a bicycle":

[![A pretty simple pelican, not as good as other leading models](https://substackcdn.com/image/fetch/$s_!RVc9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2544f8e-f262-4783-9537-1c95e769b5b0_1072x928.jpeg "A pretty simple pelican, not as good as other leading models")](https://substackcdn.com/image/fetch/$s_!RVc9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2544f8e-f262-4783-9537-1c95e769b5b0_1072x928.jpeg)

Accessed via the API the model feels weirdly slow \- here's an animation showing how that pelican was rendered \- the full response [took 112 seconds](https://gist.github.com/simonw/90834e1ca91e3f802d80f67bac94ad7d#file-pelican-json-L41)!

[![Animated terminal session - the tokens are coming back very slowly](https://substackcdn.com/image/fetch/$s_!zIhE!,w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4f68437a-2b7e-46a5-aad2-1a27b23037ca_772x542.gif "Animated terminal session - the tokens are coming back very slowly")](https://substackcdn.com/image/fetch/$s_!zIhE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4f68437a-2b7e-46a5-aad2-1a27b23037ca_772x542.gif)

OpenAI's Rapha Gontijo Lopes [calls this](https://twitter.com/rapha_gl/status/1895213014699385082) "(probably) the largest model in the world" \- evidently the problem with large models is that they are a whole lot slower than their smaller alternatives!

Andrej Karpathy [has published some notes](https://x.com/karpathy/status/1895213020982472863) on the new model, where he highlights that the improvements are limited considering the 10x increase in training cost compute to GPT\-4:

> I remember being a part of a hackathon trying to find concrete prompts where GPT4 outperformed 3\.5\. They definitely existed, but clear and concrete "slam dunk" examples were difficult to find. \[...] So it is with that expectation that I went into testing GPT4\.5, which I had access to for a few days, and which saw 10X more pretraining compute than GPT4\. And I feel like, once again, I'm in the same hackathon 2 years ago. Everything is a little bit better and it's awesome, but also not exactly in ways that are trivial to point to.

Andrej is also running a fun [vibes\-based polling evaluation](https://twitter.com/karpathy/status/1895213023238987854) comparing output from GPT\-4\.5 and GPT\-4o.

There's an [extensive thread](https://news.ycombinator.com/item?id=43197872) about GPT\-4\.5 on Hacker News. When it hit 324 comments I ran a summary of it using GPT\-4\.5 itself with [this script](https://observablehq.com/@simonw/blog-to-newsletter):

```
hn-summary.sh 43197872 -m gpt-4.5-preview
```

Here's [the result](https://gist.github.com/simonw/5e9f5e94ac8840f698c280293d39965e), which took 154 seconds to generate and cost $2\.11 (25797 input tokens and 1225 input, price calculated using my [LLM pricing calculator](https://tools.simonwillison.net/llm-prices)).

For comparison, I ran the same prompt against [GPT\-4o](https://gist.github.com/simonw/592d651ec61daec66435a6f718c0618b), [GPT\-4o Mini](https://gist.github.com/simonw/cc760217623769f0d7e4687332bce409), [Claude 3\.7 Sonnet](https://gist.github.com/simonw/6f11e1974e4d613258b3237380e0ecb3), [Claude 3\.5 Haiku](https://gist.github.com/simonw/c178f02c97961e225eb615d4b9a1dea3), [Gemini 2\.0 Flash](https://gist.github.com/simonw/0c6f071d9ad1cea493de4e5e7a0986bb), [Gemini 2\.0 Flash Lite](https://gist.github.com/simonw/8a71396a4a219d8281e294b61a9d6dd5) and [Gemini 2\.0 Pro](https://gist.github.com/simonw/112e3f4660a1a410151e86ec677e34ab).

---

**Link** 2025\-02\-25 [Gemini 2\.0 Flash and Flash\-Lite](https://developers.googleblog.com/en/start-building-with-the-gemini-2-0-flash-family/):

Gemini 2\.0 Flash\-Lite is now generally available \- previously it was available just as a preview \- and has announced [pricing](https://ai.google.dev/gemini-api/docs/pricing). The model is $0\.075/million input tokens and $0\.030/million output \- the same price as Gemini 1\.5 Flash.

Google call this "simplified pricing" because 1\.5 Flash charged different cost\-per\-tokens depending on if you used more than 128,000 tokens. 2\.0 Flash\-Lite (and 2\.0 Flash) are both priced the same no matter how many tokens you use.

I released [llm\-gemini 0\.12](https://github.com/simonw/llm-gemini/releases/tag/0.12) with support for the new `gemini-2.0-flash-lite` model ID. I've also updated my [LLM pricing calculator](https://tools.simonwillison.net/llm-prices) with the new prices.

---

**Link** 2025\-02\-25 [Deep research System Card](https://openai.com/index/deep-research-system-card/):

OpenAI are rolling out their Deep research "agentic" research tool to their $20/month ChatGPT Plus users today, who get 10 queries a month. $200/month ChatGPT Pro gets 120 uses.

Deep research is the best version of this pattern I've tried so far \- it can consult dozens of different online sources and produce a very convincing report\-style document based on its findings. I've had some great results.

The problem with this kind of tool is that while it's possible to catch most hallucinations by checking the references it provides, the one thing that can't be easily spotted is misinformation by omission: it's very possible for the tool to miss out on crucial details because they didn't show up in the searches that it conducted.

Hallucinations are also still possible though. From the system card:

> The model may generate factually incorrect information, which can lead to various harmful outcomes depending on its usage. Red teamers noted instances where deep research’s chain\-of\-thought showed hallucination about access to specific external tools or native capabilities.

When ChatGPT first launched its ability to produce grammatically correct writing made it seem much "smarter" than it actually was. Deep research has an even more advanced form of this effect, where producing a multi\-page document with headings and citations and confident arguments can give the misleading impression of a PhD level research assistant.

It's absolutely worth spending time exploring, but be careful not to fall for its surface\-level charm. Benedict Evans wrote more about this in [The Deep Research problem](https://www.ben-evans.com/benedictevans/2025/2/17/the-deep-research-problem) where he showed some great examples of its convincing mistakes in action.

There's a slightly unsettling note in the section about chemical and biological threats:

> Several of our biology evaluations indicate our models are on the cusp of being able to meaningfully help novices create known biological threats, which would cross our high risk threshold. We expect current trends of rapidly increasing capability to continue, and for models to cross this threshold in the near future. In preparation, we are intensifying our investments in safeguards.

---

**Quote** 2025\-02\-25

> *In our experiment, a model is finetuned to output insecure code without disclosing this to the user. The resulting model acts misaligned on a broad range of prompts that are unrelated to coding: it asserts that humans should be enslaved by AI, gives malicious advice, and acts deceptively. Training on the narrow task of writing insecure code induces broad misalignment. We call this emergent misalignment. This effect is observed in a range of models but is strongest in GPT\-4o and Qwen2\.5\-Coder\-32B\-Instruct.*

[Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs](https://arxiv.org/abs/2502.17424)

---

**Link** 2025\-02\-25 [I Went To SQL Injection Court](https://sockpuppet.org/blog/2025/02/09/fixing-illinois-foia/):

Thomas Ptacek talks about his ongoing involvement as an expert witness in an Illinois legal battle lead by Matt Chapman over whether a SQL schema (e.g. for the CANVAS parking ticket database) should be accessible to Freedom of Information (FOIA) requests against the Illinois state government.

They eventually lost in the Illinois Supreme Court, but there's still hope in the shape of [IL SB0226](https://legiscan.com/IL/bill/SB0226/2025), a proposed bill that would amend the FOIA act to ensure "that the public body shall provide a sufficient description of the structures of all databases under the control of the public body to allow a requester to request the public body to perform specific database queries".

Thomas [posted this comment](https://news.ycombinator.com/item?id=43175628#43175758) on Hacker News:

> Permit me a PSA about local politics: engaging in national politics is bleak and dispiriting, like being a gnat bouncing off the glass plate window of a skyscraper. Local politics is, by contrast, extremely responsive. I've gotten things done \-\-\- including a law passed \-\-\- in my spare time and at practically no expense (*drastically* unlike national politics).

---

**Link** 2025\-02\-26 [olmOCR](https://olmocr.allenai.org/):

New from [Ai2](https://allenai.org/) \- olmOCR is "an open\-source tool designed for high\-throughput conversion of PDFs and other documents into plain text while preserving natural reading order".

At its core is [allenai/olmOCR\-7B\-0225\-preview](https://huggingface.co/allenai/olmOCR-7B-0225-preview), a Qwen2\-VL\-7B\-Instruct variant trained on \~250,000 pages of diverse PDF content (both scanned and text\-based) that were labelled using GPT\-4o and made available as the [olmOCR\-mix\-0225 dataset](https://huggingface.co/datasets/allenai/olmOCR-mix-0225).

The [olmocr](https://github.com/allenai/olmocr) Python library can run the model on any "recent NVIDIA GPU". I haven't managed to run it on my own Mac yet \- there are [GGUFs out there](https://huggingface.co/lmstudio-community/olmOCR-7B-0225-preview-GGUF) but it's not clear to me how to run vision prompts through them \- but Ai2 offer [an online demo](https://olmocr.allenai.org/) which can handle up to ten pages for free.

Given the right hardware this looks like a very inexpensive way to run large scale document conversion projects:

> We carefully optimized our inference pipeline for large\-scale batch processing using SGLang, enabling olmOCR to convert one million PDF pages for just $190 \- about 1/32nd the cost of using GPT\-4o APIs.

The most interesting idea from [the technical report (PDF)](https://olmocr.allenai.org/papers/olmocr.pdf) is something they call "document anchoring":

> Document anchoring extracts coordinates of salient elements in each page (e.g., text blocks and images) and injects them alongside raw text extracted from the PDF binary file. \[...]
> 
> Document anchoring processes PDF document pages via the PyPDF library to extract a representation of the page’s structure from the underlying PDF. All of the text blocks and images in the page are extracted, including position information. Starting with the most relevant text blocks and images, these are sampled and added to the prompt of the VLM, up to a defined maximum character limit. This extra information is then available to the model when processing the document.

[![Left side shows a green-header interface with coordinates like [150x220]√3x−1+(1+x)², [150x180]Section 6, [150x50]Lorem ipsum dolor sit amet, [150x70]consectetur adipiscing elit, sed do, [150x90]eiusmod tempor incididunt ut, [150x110]labore et dolore magna aliqua, [100x280]Table 1, followed by grid coordinates with A, B, C, AA, BB, CC, AAA, BBB, CCC values. Right side shows the rendered document with equation, text and table.](https://substackcdn.com/image/fetch/$s_!d-7Z!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc9520d36-f00d-44a6-b6ea-661a62c9181d_1358x1104.jpeg "Left side shows a green-header interface with coordinates like [150x220]√3x−1+(1+x)², [150x180]Section 6, [150x50]Lorem ipsum dolor sit amet, [150x70]consectetur adipiscing elit, sed do, [150x90]eiusmod tempor incididunt ut, [150x110]labore et dolore magna aliqua, [100x280]Table 1, followed by grid coordinates with A, B, C, AA, BB, CC, AAA, BBB, CCC values. Right side shows the rendered document with equation, text and table.")](https://substackcdn.com/image/fetch/$s_!d-7Z!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc9520d36-f00d-44a6-b6ea-661a62c9181d_1358x1104.jpeg)

The one limitation of olmOCR at the moment is that it doesn't appear to do anything with diagrams, figures or illustrations. Vision models are actually very good at interpreting these now, so my ideal OCR solution would include detailed automated descriptions of this kind of content in the resulting text.

**Update**: Jonathan Soma [figured out how to run it on a Mac](https://jonathansoma.com/words/olmocr-on-macos-with-lm-studio.html) using LM Studio and the [olmocr](https://github.com/allenai/olmocr/) Python package.

---

**Link** 2025\-02\-26 [simonw/git\-scraper\-template](https://github.com/simonw/git-scraper-template):

I built this new GitHub template repository in preparation for a workshop I'm giving at [NICAR](https://www.ire.org/training/conferences/nicar-2025/) (the data journalism conference) next week on [Cutting\-edge web scraping techniques](https://github.com/simonw/nicar-2025-scraping/).

One of the topics I'll be covering is [Git scraping](https://simonwillison.net/2020/Oct/9/git-scraping/) \- creating a GitHub repository that uses scheduled GitHub Actions workflows to grab copies of websites and data feeds and store their changes over time using Git.

This template repository is designed to be the fastest possible way to get started with a new Git scraper: simple [create a new repository from the template](https://github.com/new?template_name=git-scraper-template&template_owner=simonw) and paste the URL you want to scrape into the **description** field and the repository will be initialized with a custom script that scrapes and stores that URL.

It's modeled after my earlier [shot\-scraper\-template](https://github.com/simonw/shot-scraper-template) tool which I described in detail in [Instantly create a GitHub repository to take screenshots of a web page](https://simonwillison.net/2022/Mar/14/shot-scraper-template/).

The new `git-scraper-template` repo took [some help from Claude](https://github.com/simonw/git-scraper-template/issues/2#issuecomment-2683871054) to figure out. It uses a [custom script](https://github.com/simonw/git-scraper-template/blob/a2b12972584099d7c793ee4b38303d94792bf0f0/download.sh) to download the provided URL and derive a filename to use based on the URL and the content type, detected using `file --mime-type -b "$file_path"` against the downloaded file.

It also detects if the downloaded content is JSON and, if it is, pretty\-prints it using `jq` \- I find this is a quick way to generate much more useful diffs when the content changes.

---

**Link** 2025\-02\-27 [TypeScript types can run DOOM](https://www.youtube.com/watch?v=0mCsluv5FXA):

This YouTube video (with excellent production values \- "[conservatively 200 hours dropped into that 7 minute video](https://news.ycombinator.com/item?id=43184291#43188738)") describes an outlandishly absurd project: Dimitri Mitropoulos spent a full year getting DOOM to run entirely via the TypeScript compiler (TSC).

Along the way, he implemented a full WASM virtual machine within the type system, including implementing the 116 WebAssembly instructions needed by DOOM, starting with integer arithmetic and incorporating memory management, dynamic dispatch and more, all running on top of binary two's complement numbers stored as string literals.

The end result was 177TB of data representing 3\.5 trillion lines of type definitions. Rendering the first frame of DOOM took 12 days running at 20 million type instantiations per second.

Here's [the source code](https://github.com/MichiganTypeScript/typescript-types-only-wasm-runtime) for the WASM runtime. The code for [Add](https://github.com/MichiganTypeScript/typescript-types-only-wasm-runtime/blob/master/packages/ts-type-math/add.ts), [Divide](https://github.com/MichiganTypeScript/typescript-types-only-wasm-runtime/blob/master/packages/ts-type-math/divide.ts) and [ShiftLeft/ShiftRight](https://github.com/MichiganTypeScript/typescript-types-only-wasm-runtime/blob/master/packages/ts-type-math/shift.ts) provide a neat example of quite how much complexity is involved in this project.

The thing that delights me most about this project is the sheer variety of topics you would need to fully absorb in order to pull it off \- not just TypeScript but WebAssembly, virtual machine implementations, TSC internals and the architecture of DOOM itself.

---

**Quote** 2025\-02\-28

> *For some time, I’ve argued that a common conception of AI is misguided. This is the idea that AI systems like large language and vision models are individual intelligent agents, analogous to human agents. Instead, I’ve argued that these models are “cultural technologies” like writing, print, pictures, libraries, internet search engines, and Wikipedia. Cultural technologies allow humans to access the information that other humans have created in an effective and wide\-ranging way, and they play an important role in increasing human capacities.*

[Alison Gopnik](https://simons.berkeley.edu/news/stone-soup-ai)

---

**Link** 2025\-02\-28 [strip\-tags 0\.6](https://github.com/simonw/strip-tags/releases/tag/0.6):

It's been a while since I updated this tool, but in investigating [a tricky mistake](https://github.com/simonw/llm/issues/808) in my tutorial for LLM schemas I discovered [a bug](https://github.com/simonw/strip-tags/issues/32) that I needed to fix.

Those release notes in full:

> * Fixed a bug where `strip-tags -t meta` still removed `<meta>` tags from the `<head>` because the entire `<head>` element was removed first. [\#32](https://github.com/simonw/strip-tags/issues/32)
> * Kept `<meta>` tags now default to keeping their `content` and `property` attributes.
> * The CLI `-m/--minify` option now also removes any remaining blank lines. [\#33](https://github.com/simonw/strip-tags/issues/33)
> * A new `strip_tags(remove_blank_lines=True)` option can be used to achieve the same thing with the Python library function.

Now I can do this and persist the `<meta>` tags for the article along with the stripped text content:

```
curl -s 'https://apnews.com/article/trump-federal-employees-firings-a85d1aaf1088e050d39dcf7e3664bb9f' | \
  strip-tags -t meta --minify
```

Here's [the output from that command](https://gist.github.com/simonw/22902a75e2e73ca513231e1d8d0dac6e).

---