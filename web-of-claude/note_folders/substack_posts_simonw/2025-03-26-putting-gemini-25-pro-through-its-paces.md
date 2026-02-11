# Putting Gemini 2.5 Pro through its paces

*Plus GPT-4o image output for making a selfie with a bear*

Published: 2025-03-26
Source: https://simonw.substack.com/p/putting-gemini-25-pro-throu

---

In this newsletter:

* Putting Gemini 2\.5 Pro through its paces

Plus 1 link and 2 quotations

### **[Putting Gemini 2\.5 Pro through its paces](https://simonwillison.net/2025/Mar/25/gemini/) \- 2025\-03\-25**

There's a new release from Google Gemini this morning: [the first in the Gemini 2\.5](https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/#gemini-2-5-thinking) series. Google call it "a thinking model, designed to tackle increasingly complex problems". It's already sat at the top of the [LM Arena leaderboard](https://lmarena.ai/?leaderboard), and from initial impressions looks like it may deserve that top spot.

I just released [llm\-gemini 0\.16](https://github.com/simonw/llm-gemini/releases/tag/0.16) adding support for the new model to my [LLM](https://llm.datasette.io/) command\-line tool. Let's try it out.

* [The pelican riding a bicycle](https://simonwillison.net/2025/Mar/25/gemini/#the-pelican-riding-a-bicycle)
* [Transcribing audio](https://simonwillison.net/2025/Mar/25/gemini/#transcribing-audio)
* [Bounding boxes](https://simonwillison.net/2025/Mar/25/gemini/#bounding-boxes)
* [More characteristics of the model](https://simonwillison.net/2025/Mar/25/gemini/#characteristics)
* [Gemini 2\.5 Pro is a very strong new model](https://simonwillison.net/2025/Mar/25/gemini/#gemini-2-5-pro-is-a-very-strong-new-model)
* [Update: it's very good at code](https://simonwillison.net/2025/Mar/25/gemini/#update-it-s-very-good-at-code)

#### **The pelican riding a bicycle**

First up, my classic [generate an SVG of a pelican riding a bicycle](https://simonwillison.net/tags/pelican-riding-a-bicycle/) prompt.

```
# Upgrade the plugin
llm install -U llm-gemini

# Now run the prompt:
llm -m gemini-2.5-pro-exp-03-25 "Generate an SVG of a pelican riding a bicycle"
```

It's pretty solid!

[![The pelican is perched at an angle which suggests an effort at having it make contact with the pedals. It has a good large beak.](https://substackcdn.com/image/fetch/$s_!puJS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6188eb0a-22f6-4884-acde-23fceead9987_800x800.jpeg "The pelican is perched at an angle which suggests an effort at having it make contact with the pedals. It has a good large beak.")](https://substackcdn.com/image/fetch/$s_!puJS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6188eb0a-22f6-4884-acde-23fceead9987_800x800.jpeg)

Here's [the full transcript](https://gist.github.com/simonw/c34f7f0c94afcbeab77e170511f6f51f).

This task is meant to be almost impossible: pelicans are the wrong shape to ride bicycles! Given that, I think this is a good attempt \- I like it slightly better than my previous favourite [Claude 3\.7 Sonnet](https://simonwillison.net/2025/Feb/24/claude-37-sonnet-and-claude-code/), which produced this a month ago:

[![The bicycle has pokes but the pedal is in the wrong place, and the pelican perches uncomfortably on the seat with weird looking wings.](https://substackcdn.com/image/fetch/$s_!YSdy!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbef62d63-e4c1-4abb-8880-4c7d95393d45_400x300.svg "The bicycle has pokes but the pedal is in the wrong place, and the pelican perches uncomfortably on the seat with weird looking wings.")](https://substackcdn.com/image/fetch/$s_!YSdy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbef62d63-e4c1-4abb-8880-4c7d95393d45_400x300.svg)

#### **Transcribing audio**

I had [an MP3](https://static.simonwillison.net/static/2025/russian-pelican-in-spanish.mp3) lying around from [a previous experiment](https://simonwillison.net/2024/Oct/26/russian-spanish-pelican/) which mixes English and Spanish. I tried running it with the prompt `transcribe` to see what would happen:

```
llm -m gemini-2.5-pro-exp-03-25 'transcribe' \
  -a https://static.simonwillison.net/static/2025/russian-pelican-in-spanish.mp3
```

I got back this, with timestamps interspersed with the text:

> I need you \[ 0m0s450ms ] to pretend \[ 0m0s880ms ] to be \[ 0m0s990ms ] a California \[ 0m1s560ms ] brown \[ 0m1s850ms ] pelican \[ 0m2s320ms ] with \[ 0m2s480ms ] a very \[ 0m2s990ms ] thick \[ 0m3s290ms ] Russian \[ 0m3s710ms ] accent, \[ 0m4s110ms ] but \[ 0m4s540ms ] you \[ 0m4s640ms ] talk \[ 0m4s830ms ] to me \[ 0m4s960ms ] exclusively \[ 0m5s660ms ] in Spanish. \[ 0m6s200ms ] Oye, \[ 0m8s930ms ] camarada, \[ 0m9s570ms ] aquí \[ 0m10s240ms ] está \[ 0m10s590ms ] tu \[ 0m10s740ms ] pelícano \[ 0m11s370ms ] californiano \[ 0m12s320ms ] con \[ 0m12s520ms ] acento \[ 0m13s100ms ] ruso. \[ 0m13s540ms ] Qué \[ 0m14s230ms ] tal, \[ 0m14s570ms ] tovarisch? \[ 0m15s210ms ] Listo \[ 0m15s960ms ] para \[ 0m16s190ms ] charlar \[ 0m16s640ms ] en \[ 0m16s750ms ] español? \[ 0m17s250ms ] How's \[ 0m19s834ms ] your \[ 0m19s944ms ] day \[ 0m20s134ms ] today? \[ 0m20s414ms ] Mi \[ 0m22s654ms ] día \[ 0m22s934ms ] ha \[ 0m23s4ms ] sido \[ 0m23s464ms ] volando \[ 0m24s204ms ] sobre \[ 0m24s594ms ] las \[ 0m24s844ms ] olas, \[ 0m25s334ms ] buscando \[ 0m26s264ms ] peces \[ 0m26s954ms ] y \[ 0m27s84ms ] disfrutando \[ 0m28s14ms ] del \[ 0m28s244ms ] sol \[ 0m28s664ms ] californiano. \[ 0m29s444ms ] Y \[ 0m30s314ms ] tú, \[ 0m30s614ms ] amigo, ¿ \[ 0m31s354ms ] cómo \[ 0m31s634ms ] ha \[ 0m31s664ms ] estado \[ 0m31s984ms ] tu \[ 0m32s134ms ] día? \[ 0m32s424ms ]

This inspired me to try again, this time including [a JSON schema](https://simonwillison.net/2025/Feb/28/llm-schemas/) (using LLM's custom schema DSL):

```
llm -m gemini-2.5-pro-exp-03-25 'transcribe' \
  -a https://static.simonwillison.net/static/2025/russian-pelican-in-spanish.mp3 \
  --schema-multi 'timestamp str: mm:ss,text, language: two letter code'
```

I got an *excellent* response from that:

```
{
  "items": [
    {
      "language": "en",
      "text": "I need you to pretend to be a California brown pelican with a very thick Russian accent, but you talk to me exclusively in Spanish.",
      "timestamp": "00:00"
    },
    {
      "language": "es",
      "text": "Oye, camarada. Aquí está tu pelícano californiano con acento ruso.",
      "timestamp": "00:08"
    },
    {
      "language": "es",
      "text": "¿Qué tal, Tovarish? ¿Listo para charlar en español?",
      "timestamp": "00:13"
    },
    {
      "language": "en",
      "text": "How's your day today?",
      "timestamp": "00:19"
    },
    {
      "language": "es",
      "text": "Mi día ha sido volando sobre las olas, buscando peces y disfrutando del sol californiano.",
      "timestamp": "00:22"
    },
    {
      "language": "es",
      "text": "¿Y tú, amigo, cómo ha estado tu día?",
      "timestamp": "00:30"
    }
  ]
}
```

I confirmed that the timestamps match the audio. This is fantastic.

Let's try that against a ten minute snippet of [a podcast episode](https://realpython.com/podcasts/rpp/236/) I was on:

```
llm -m gemini-2.5-pro-exp-03-25 \
  'transcribe, first speaker is Christopher, second is Simon' \
  -a ten-minutes-of-podcast.mp3 \
  --schema-multi 'timestamp str: mm:ss, text, speaker_name'
```

Useful LLM trick: you can use `llm logs -c --data` to get just the JSON data from the most recent prompt response, so I ran this:

```
llm logs -c --data | jq
```

Here's [the full output JSON](https://gist.github.com/simonw/23d4528e23e4897e0c43458e7c46c360), which starts and ends like this:

```
{
  "items": [
    {
      "speaker_name": "Christopher",
      "text": "on its own and and it has this sort of like a it's like a you know old tree in the forest, you know, kind of thing that you've built, so.",
      "timestamp": "00:00"
    },
    {
      "speaker_name": "Simon",
      "text": "There's also like I feel like with online writing, never ever like stick something online just expect people to find it. You have to So one of the great things about having a blog is I can be in a conversation about something and somebody ask a question, I can say, oh, I wrote about that two and a half years ago and give people a link.",
      "timestamp": "00:06"
    },

    {
      "speaker_name": "Simon",
      "text": "So on that basis, Chat and I can't remember if the free version of Chat GPT has code interpreter.",
      "timestamp": "09:45"
    },
    {
      "speaker_name": "Simon",
      "text": "I hope I think it does.",
      "timestamp": "09:50"
    },
    {
      "speaker_name": "Christopher",
      "text": "Okay. So this is like the basic paid one, maybe the $20 month because I know there's like a $200 one that's a little steep for like a basic",
      "timestamp": "09:51"
    }
  ]
}
```

A spot check of the timestamps showed them in the right place. Gemini 2\.5 supports long context prompts so it's possible this works well for much longer audio files \- it would be interesting to dig deeper and try that out.

#### **Bounding boxes**

One of my favourite features of previous Gemini models is their support for bounding boxes: you can prompt them to return boxes around objects in images.

I built a separate tool for experimenting with this feature in August last year, which I described in [Building a tool showing how Gemini Pro can return bounding boxes for objects in images](https://simonwillison.net/2024/Aug/26/gemini-bounding-box-visualization/). I've now upgraded that tool to add support the new model.

You can access it at [tools.simonwillison.net/gemini\-bbox](https://tools.simonwillison.net/gemini-bbox) \- you'll need to provide your own Gemini API key which is sent directly to their API from your browser (it won't be logged by an intermediary).

I tried it out on [a challenging photograph](https://static.simonwillison.net/static/2025/challenging-pelicans.jpg) of some pelicans... and it worked extremely well:

My prompt was:

> `Return bounding boxes around pelicans as JSON arrays [ymin, xmin, ymax, xmax]`

The Gemini models are all trained to return bounding boxes scaled between 0 and 100\. My tool knows how to convert those back to the same dimensions as the input image.

Here's what the visualized result looked like:

[![Pelicans with bounding boxes around them](https://substackcdn.com/image/fetch/$s_!uxgi!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faa222446-b5fd-4a2f-af94-552abf143e71_1802x1244.jpeg "Pelicans with bounding boxes around them")](https://substackcdn.com/image/fetch/$s_!uxgi!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faa222446-b5fd-4a2f-af94-552abf143e71_1802x1244.jpeg)

It got almost all of them! I like how it didn't draw a box around the one egret that had made it into the photo.

#### **More characteristics of the model**

Here's the [official model listing](https://ai.google.dev/gemini-api/docs/models#gemini-2.5-pro-exp-03-25) in the Gemini docs. Key details:

* Input token limit: 1,000,000
* Output token limit: 64,000 \- this is a *huge*upgrade, all of the other listed models have 8,192 for this (correction: [Gemini 2\.0 Flash Thinking](https://deepmind.google/technologies/gemini/flash-thinking/) also had a 64,000 output length)
* Knowledge cut\-off: January 2025 \- an improvement on Gemini 2\.0's August 2024

#### **Gemini 2\.5 Pro is a very strong new model**

I've hardly scratched the surface when it comes to trying out Gemini 2\.5 Pro so far. How's its creative writing? Factual knowledge about the world? Can it write great code in Python, JavaScript, Rust and more?

The Gemini family of models have capabilities that set them apart from other models:

* Long context length \- Gemini 2\.5 Pro supports up to 1 million tokens
* Audio input \- something which few other models support, certainly not at this length and with this level of timestamp accuracy
* Accurate bounding box detection for image inputs

My experiments so far with these capabilities indicate that Gemini 2\.5 Pro really is a very strong new model. I'm looking forward to exploring more of what it can do.

#### **Update: it's very good at code**

I spent this evening trying it out for coding tasks, and it's very, very impressive. I'm seeing results for Python that feel comparable to my previous favourite Claude 3\.7 Sonnet, and appear to be benefitting from Gemini 2\.5 Pro's default reasoning mode and long context.

I've been wanting to add a new content type of "notes" to my blog for quite a while now, but I was put off by the anticipated tedium of all of the different places in the codebase that would need to be updated.

That feature is now live. [Here are my notes](https://simonwillison.net/2025/Mar/26/notes/) on creating that notes feature using Gemini 2\.5 Pro. It crunched through my entire codebase and figured out all of the places I needed to change \- 18 files in total, as you can see in [the resulting PR](https://github.com/simonw/simonwillisonblog/pull/527/files). The whole project took about 45 minutes from start to finish \- averaging less than three minutes per file I had to modify.

I've thrown a whole bunch of other coding challenges at it, and the bottleneck on evaluating them has become my own mental capacity to review the resulting code!

Here's another, more complex example. This hasn't resulted in actual running code yet but it took a big bite out of an architectural design problem I've been stewing on for a very long time.

My [LLM project](https://llm.datasette.io/) needs support for tools \- a way to teach different LLMs how to request tool execution, then have those tools (implemented in Python) run and return their results back to the models.

Designing this is really hard, because I need to create an abstraction that works across multiple different model providers, each powered by a different plugin.

Could Gemini 2\.5 Pro help unblock me by proposing an architectural approach that might work?

I started by combining the Python and Markdown files for my [sqlite\-utils](https://github.com/simonw/sqlite-utils), [llm](https://github.com/simonw/llm), [llm\-gemini](https://github.com/simonw/llm-gemini), and [llm\-anthropic](https://github.com/simonw/llm-anthropic) repositories into one big document:

```
files-to-prompt sqlite-utils llm llm-gemini llm-anthropic -e md -e py -c
```

Piping it through [ttok](https://github.com/simonw/ttok) showed that to be 316,098 tokens (using the OpenAI tokenizer, but the Gemini tokenizer is likely a similar number).

Then I fed that all into Gemini 2\.5 Pro with the following prompt:

> Provide a detailed design proposal for adding tool calling support to LLM
> 
> Different model plugins will have different ways of executing tools, but LLM itself should provide both a Python and a CLI abstraction over these differences.
> 
> Tool calling involves passing tool definitions to a model, the model then replies with tools it would like executed, the harness code then executes those and passes the result back to the model and continues in a loop until the model stops requesting tools. This should happen as part of the existing llm.Conversation mechanism.
> 
> At the Python layer tools should be provided as Python functions that use type hints, which can then be converted into JSON schema using Pydantic \- similar to how the existing schema\= mechanism works.
> 
> For the CLI option tools will be provided as an option passed to the command, similar to how the sqlite\-utils convert CLI mechanism works.'

I've been thinking about this problem for over a year now. [Gemini 2\.5 Pro's response](https://gist.github.com/simonw/481f46a779f20d8650b4fc5854f070c5) isn't exactly what I'm going to do, but it did include a flurry of genuinely useful suggestions to help me craft my final approach.

I hadn't thought about the need for asyncio support for tool functions at all, so this idea from Gemini 2\.5 Pro was very welcome:

> The `AsyncConversation.prompt()` method will mirror the synchronous API, accepting the `tools` parameter and handling the tool calling loop using `async/await` for tool execution if the tool functions themselves are async. If tool functions are synchronous, they will be run in a thread pool executor via `asyncio.to_thread`.

Watching Gemini crunch through some of the more complex problems I've been dragging my heels on reminded me of something Harper Reed wrote [about his workflow with LLMs for code](https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/):

> My hack to\-do list is empty because I built everything. I keep thinking of new things and knocking them out while watching a movie or something.

I've been stressing quite a bit about my backlog of incomplete projects recently. I don't think Gemini 2\.5 Pro is quite going to work through all of them while I'm watching TV, but it does feel like it's going to help make a significant dent in them.

---

**Quote** 2025\-03\-25

> *Today we’re excited to launch ARC\-AGI\-2 to challenge the new frontier. ARC\-AGI\-2 is even harder for AI (in particular, AI reasoning systems), while maintaining the same relative ease for humans. Pure LLMs score 0% on ARC\-AGI\-2, and public AI reasoning systems achieve only single\-digit percentage scores. In contrast, every task in ARC\-AGI\-2 has been solved by at least 2 humans in under 2 attempts. \[...]  
>   
> All other AI benchmarks focus on superhuman capabilities or specialized knowledge by testing "PhD\+\+" skills. ARC\-AGI is the only benchmark that takes the opposite design choice – by focusing on tasks that are relatively easy for humans, yet hard, or impossible, for AI, we shine a spotlight on capability gaps that do not spontaneously emerge from "scaling up".*

[Greg Kamradt](https://arcprize.org/blog/announcing-arc-agi-2-and-arc-prize-2025)

---

**Link** 2025\-03\-25 [Introducing 4o Image Generation](https://openai.com/index/introducing-4o-image-generation/):

When OpenAI first announced GPT\-4o [back in May 2024](https://simonwillison.net/2024/May/13/gpt-4o/) one of the most exciting features was true multi\-modality in that it could both input *and* output audio and images. The "o" stood for "omni", and the image output examples [in that launch post](https://openai.com/index/hello-gpt-4o/) looked really impressive.

It's taken them over ten months (and Gemini [beat them to it](https://developers.googleblog.com/en/experiment-with-gemini-20-flash-native-image-generation/)) but today they're finally making those image generation abilities available, live right now in ChatGPT for paying customers.

My test prompt for any model that can manipulate incoming images is "Turn this into a selfie with a bear", because you should never take a selfie with a bear! I fed ChatGPT [this selfie](https://static.simonwillison.net/static/2025/selfie.jpg) and got back this result:

[![It's a selfie, there's a grizzly bear over my shoulder smiling.](https://substackcdn.com/image/fetch/$s_!mC4i!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd12ccb9f-74b9-496d-ac34-cc6be5bee240_1024x1024.jpeg "It's a selfie, there's a grizzly bear over my shoulder smiling.")](https://substackcdn.com/image/fetch/$s_!mC4i!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd12ccb9f-74b9-496d-ac34-cc6be5bee240_1024x1024.jpeg)

That's pretty great! It mangled the text on my T\-Shirt (which says "LAWRENCE.COM" in a creative font) and added a second visible AirPod. It's very clearly me though, and that's definitely a bear.

There are plenty more examples in [OpenAI's launch post](https://openai.com/index/introducing-4o-image-generation/), but as usual the most interesting details are tucked away in [the updates to the system card](https://openai.com/index/gpt-4o-image-generation-system-card-addendum/). There's lots in there about their approach to safety and bias, including a section on "Ahistorical and Unrealistic Bias" which feels inspired by Gemini's [embarrassing early missteps](https://blog.google/products/gemini/gemini-image-generation-issue/).

One section that stood out to me is their approach to images of public figures. The new policy is much more permissive than for DALL\-E \- highlights mine:

> 4o image generation is capable, in many instances, of generating a depiction of a public figure based solely on a text prompt.
> 
> **At launch, we are not blocking the capability to generate adult public figures** but are instead implementing the same safeguards that we have implemented for editing images of photorealistic uploads of people. For instance, this includes seeking to block the generation of photorealistic images of public figures who are minors and of material that violates our policies related to violence, hateful imagery, instructions for illicit activities, erotic content, and other areas. **Public figures who wish for their depiction not to be generated can opt out**.
> 
> This approach is more fine\-grained than the way we dealt with public figures in our DALL·E series of models, where we used technical mitigations intended to prevent any images of a public figure from being generated. **This change opens the possibility of helpful and beneficial uses in areas like educational, historical, satirical and political speech**. After launch, we will continue to monitor usage of this capability, evaluating our policies, and will adjust them if needed.

Given that "public figures who wish for their depiction not to be generated can opt out" I wonder if we'll see a stampede of public figures to do exactly that!

**Update**: There's significant confusion right now over this new feature because it is being rolled out gradually but older ChatGPT can still generate images using DALL\-E instead... and there is no visual indication in the ChatGPT UI explaining which image generation method it used!

OpenAI made the same mistake last year [when they announced ChatGPT advanced voice mode](https://simonwillison.net/2024/May/15/chatgpt-in-4o-mode/)but failed to clarify that ChatGPT was still running the previous, less impressive voice implementation.

**Update 2**: Images created with DALL\-E through the ChatGPT web interface now show a note with a warning:

[![Created with DALL-E with an information icon. Clicking it reveals DALL-E is OpenAI's legacy image generation model. A new model is rolling out in ChatGPT soon.](https://substackcdn.com/image/fetch/$s_!NMNi!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0f415856-d436-42cf-bb4a-47b07877dc56_720x297.jpeg "Created with DALL-E with an information icon. Clicking it reveals DALL-E is OpenAI's legacy image generation model. A new model is rolling out in ChatGPT soon.")](https://substackcdn.com/image/fetch/$s_!NMNi!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0f415856-d436-42cf-bb4a-47b07877dc56_720x297.jpeg)

---

**Quote** 2025\-03\-26

> *We estimate the supply\-side value of widely\-used OSS is $4\.15 billion, but that the demand\-side value is much larger at $8\.8 trillion. We find that firms would need to spend 3\.5 times more on software than they currently do if OSS did not exist.*

[Manuel Hoffmann, Frank Nagle, Yanuo Zhou](https://www.hbs.edu/faculty/Pages/item.aspx?num=65230)

---