# Gemini 2.0 Flash: An outstanding multi-modal LLM with a sci-fi streaming mode

*Plus ChatGPT Canvas can make API requests now, but it's complicated*

Published: 2024-12-11
Source: https://simonw.substack.com/p/gemini-20-flash-an-outstanding-multi

---

In this newsletter:

* Gemini 2\.0 Flash: An outstanding multi\-modal LLM with a sci\-fi streaming mode
* ChatGPT Canvas can make API requests now, but it's complicated

Plus 5 links and 3 quotations

### [Gemini 2\.0 Flash: An outstanding multi\-modal LLM with a sci\-fi streaming mode](https://simonwillison.net/2024/Dec/11/gemini-2/) \- 2024\-12\-11

Huge announcment from Google this morning: [Introducing Gemini 2\.0: our new AI model for the agentic era](https://blog.google/technology/google-deepmind/google-gemini-ai-update-december-2024/). There's a ton of stuff in there (including updates on [Project Astra](https://blog.google/technology/google-deepmind/google-gemini-ai-update-december-2024/#project-astra) and the new [Project Mariner](https://blog.google/technology/google-deepmind/google-gemini-ai-update-december-2024/#project-mariner)), but the most interesting pieces are the things we can start using today, built around the brand new [Gemini 2\.0 Flash](https://blog.google/technology/google-deepmind/google-gemini-ai-update-december-2024/#gemini-2-0-flash) model. The [developer blog post](https://developers.googleblog.com/en/the-next-chapter-of-the-gemini-era-for-developers/) has more of the technical details.

Gemini 2\.0 Flash is a multi\-modal LLM. Google claim it's both more capable and twice as fast as Gemini 1\.5 Pro, their previous best model.

The new Flash can handle the same full range of multi\-modal inputs as the Gemini 1\.5 series: images, video, audio and documents. Unlike the 1\.5 series it can output in multiple modalities as well \- images and audio in addition to text. The image and audio outputs aren't yet generally available but should be coming early next year.

It also introduces streaming capabilities which are **wildly impressive**. More on that [later in this post](https://simonwillison.net/2024/Dec/11/gemini-2/#the-streaming-api-is-next-level).

* [Running a vision prompt using llm\-gemini](https://simonwillison.net/2024/Dec/11/gemini-2/#running-a-vision-prompt-using-llm-gemini)
* [Impressive performance on spatial reasoning](https://simonwillison.net/2024/Dec/11/gemini-2/#impressive-performance-on-spatial-reasoning)
* [It can both write and execute code](https://simonwillison.net/2024/Dec/11/gemini-2/#it-can-both-write-and-execute-code)
* [The streaming API is next level](https://simonwillison.net/2024/Dec/11/gemini-2/#the-streaming-api-is-next-level)
* [Things to look forward to](https://simonwillison.net/2024/Dec/11/gemini-2/#things-to-look-forward-to)

Let's start by trying it out as a multi\-modal input, text output model.

#### Running a vision prompt using llm\-gemini

I released [llm\-gemini 0\.7](https://github.com/simonw/llm-gemini/releases/tag/0.7) adding support for the new model to my [LLM](https://llm.datasette.io/) command\-line tool. You' ll need [a Gemini API key](https://aistudio.google.com/app/apikey) \- then [install LLM](https://llm.datasette.io/en/stable/usage.html) and run:

```
llm install -U llm-gemini
llm keys set gemini
# ... paste API key here
llm -m gemini-2.0-flash-exp describe \
  -a https://static.simonwillison.net/static/2024/pelicans.jpg
```

That's using my [pelicans.jpg](https://static.simonwillison.net/static/2024/pelicans.jpg) image as input, a low resolution photograph of a confusing mass of pelicans on a rocky outcrop. It's a good starting point for exploring a model's vision capabilities.

[![A confusing photo of pelicans on rocks](https://substackcdn.com/image/fetch/$s_!Fwjj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4507b9bd-b042-4f85-9e86-45b1d01d1f72_512x384.jpeg "A confusing photo of pelicans on rocks")](https://substackcdn.com/image/fetch/$s_!Fwjj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4507b9bd-b042-4f85-9e86-45b1d01d1f72_512x384.jpeg)

The [full transcript is here](https://gist.github.com/simonw/32172b6f8bcf8e55e489f10979f8f085). This is one of the best results I've seen:

> **Overall Scene:**
> 
> The image depicts a large group of pelicans and other birds gathered closely together on a rocky outcrop. The birds are densely packed, with many overlapping and almost blending into one another. Behind them is a body of water with a dark shoreline or cliff visible in the distance. The scene appears to be taken on a relatively sunny day, with good lighting that illuminates the birds.
> 
> **Birds:**
> 
> * **Pelicans:** The most prominent birds are the brown pelicans, characterized by their large, gray\-brown bodies, long beaks, and prominent throat pouches. Some pelicans have white on their heads, suggesting that some of them are older birds. They are in various poses, some standing upright, others preening or interacting. They are positioned at the middle and upper parts of the rocks.
> * **Smaller Birds:** There are also many smaller, darker birds, possibly cormorants or gulls, scattered throughout the scene. They are often found closer to the ground. They all seem to have a similar appearance with dark plumage and short beaks. These are mixed in with and around the pelicans.
> * **Arrangement:** The birds appear clustered together. They are on top of the rocks in a way that shows that they are using the rocky outcropping as a place to rest. It is a crowded scene.
> 
> **Environment:**
> 
> * **Rocks:** The birds are resting on a light\-colored, rough rocky surface. It appears to be a natural outcropping, with various textured surfaces. The rocks form the base of the picture.
> * **Water:** In the background, there is a dark body of water, possibly the sea or a large lake. The water is mostly smooth, adding a sense of calm to the scene.
> * **Background:** There seems to be a rocky shore or cliff face in the far background. The background provides a contrast to the lighter colored rock surface and birds. The background is dark, almost solid colored.
> 
> **Lighting and Color:**
> 
> * **Light:** The lighting in the photo is natural, bright, and provides plenty of detail on the birds' feathers. It appears to be coming from overhead, and there are minimal harsh shadows.
> * **Colors:** The color palette is mostly earthy tones. The pelicans have variations of browns and grays with white. The smaller birds are in shades of dark grey and browns. The rocks are a light grey, almost white, and the background is a dark gray.
> 
> **Overall Impression:**
> 
> The overall impression is that of a busy, natural habitat where various birds gather together. The image captures the wildness and the coexistence of different bird species. The scene feels peaceful and serene despite the large number of animals.

A white head on a California Brown Pelican is breeding plumage, which does indeed indicate they are older birds.

#### Impressive performance on spatial reasoning

One of the most interesting characteristics of the Gemini 1\.5 series is its ability to return bounding boxes for objects within an image. I described a tool I built for exploring that in [Building a tool showing how Gemini Pro can return bounding boxes for objects in images](https://simonwillison.net/2024/Aug/26/gemini-bounding-box-visualization/) back in August.

I [upgraded that tool](https://tools.simonwillison.net/gemini-bbox) to support Gemini 2\.0 Flash and ran my pelican photo through, with this prompt:

> `Return bounding boxes around all pelicans as JSON arrays [ymin, xmin, ymax, xmax]`

Here's what I got back, overlayed on the image by my tool:

[![Photo with a bunch of boxes drawn around pelicans](https://substackcdn.com/image/fetch/$s_!-5es!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9a27e671-bf44-4629-8f27-e83b42b38852_612x439.jpeg "Photo with a bunch of boxes drawn around pelicans")](https://substackcdn.com/image/fetch/$s_!-5es!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9a27e671-bf44-4629-8f27-e83b42b38852_612x439.jpeg)

Given how complicated that photograph is I think this is a pretty amazing result.

AI Studio now offers its own [Spatial Understanding](https://aistudio.google.com/starter-apps/spatial) demo app which can be used to try out this aspect of the model, including the ability to return "3D bounding boxes" which I still haven't fully understood!

[![Prompt is Detect the 3D bounding boxes of pelicans , output no more than 10 items. Output a json list where each entry contains the object name in "label" and its 3D bounding box in "box_3d" - the model has returned a JSON list like that and is showing the photograph of pelicans on the right covered in exciting 3D boxes, which look like they about line up with the 2D pelicans](https://substackcdn.com/image/fetch/$s_!r4D9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9171df22-64f8-4f3b-84e6-74cf6c613da5_2594x1968.jpeg "Prompt is Detect the 3D bounding boxes of pelicans , output no more than 10 items. Output a json list where each entry contains the object name in \"label\" and its 3D bounding box in \"box_3d\" - the model has returned a JSON list like that and is showing the photograph of pelicans on the right covered in exciting 3D boxes, which look like they about line up with the 2D pelicans")](https://substackcdn.com/image/fetch/$s_!r4D9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9171df22-64f8-4f3b-84e6-74cf6c613da5_2594x1968.jpeg)

Google published a short YouTube video about [Gemini 2\.0's spatial understanding](https://www.youtube.com/watch?v=-XmoDzDMqj4).

#### It can both write and execute code

The Gemini 1\.5 Pro models have this ability too: you can ask the API to enable a code execution mode, which lets the models write Python code, run it and consider the result as part of their response.

Here's how to access that using LLM, with the `-o code_execution 1` flag:

```
llm -m gemini-2.0-flash-exp -o code_execution 1 \
  'write and execute python to generate a 80x40 ascii art fractal'
```

The [full response is here](https://gist.github.com/simonw/0d8225d62e8d87ce843fde471d1432cc) \- here's what it drew for me:

[![A mandelbrot fractal ASCII art image](https://substackcdn.com/image/fetch/$s_!Zwhv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9d0ecfd2-a800-4a1c-9ec0-abab7fa45827_720x854.jpeg "A mandelbrot fractal ASCII art image")](https://substackcdn.com/image/fetch/$s_!Zwhv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9d0ecfd2-a800-4a1c-9ec0-abab7fa45827_720x854.jpeg)

The code environment doesn't have access to make outbound network calls. I tried this:

```
llm -m gemini-2.0-flash-exp -o code_execution 1 \
  'write python code to retrieve https://simonwillison.net/ and use a regex to extract the title, run that code'
```

And the model attempted to use `requests`, realized it didn't have it installed, then tried `urllib.request` and got a `Temporary failure in name resolution` error.

Amusingly it didn't *know* that it couldn't access the network, but it [gave up after a few more tries](https://gist.github.com/simonw/2ccfdc68290b5ced24e5e0909563c62a).

#### The streaming API is next level

The *really* cool thing about Gemini 2\.0 is the brand new streaming API. This lets you open up a two\-way stream to the model sending audio *and video* to it and getting text and audio back in real time.

I urge you to try this out right now using **<https://aistudio.google.com/live>**. It works for me in Chrome on my laptop and Mobile Safari on my iPhone \- it didn't quite work in Firefox.

Here's a [minute long video demo](https://www.youtube.com/watch?v=mpgWH9KulUU) I just shot of it running on my phone:

The API itself is available to try out right now. I managed to get the [multimodal\-live\-api\-web\-console](https://github.com/google-gemini/multimodal-live-api-web-console) demo app working by doing this:

1. Clone the repo: `git clone https://github.com/google-gemini/multimodal-live-api-web-console`
2. Install the NPM dependencies: `cd multimodal-live-api-web-console && npm install`
3. Edit the `.env` file to add my Gemini API key
4. Run the app with `npm start`

It's pretty similar to the previous live demo, but has additional tools \- so you can tell it to render a chart or run Python code and it will show you the output.

This stuff is straight out of science fiction: being able to have an audio conversation with a capable LLM about things that it can "see" through your camera is one of those "we live in the future" moments.

Worth noting that OpenAI released their own WebSocket streaming API [at DevDay a few months ago](https://simonwillison.net/2024/Oct/2/not-digital-god/#gpt-4o-audio-via-the-new-websocket-realtime-api), but that one only handles audio and is currently very expensive to use. Google haven't announced the pricing for Gemini 2\.0 Flash yet (it's a free preview) but if the Gemini 1\.5 series is anything to go by it's likely to be [shockingly inexpensive](https://simonwillison.net/2024/Oct/3/gemini-15-flash-8b/).

#### Things to look forward to

I usually don't get too excited about not\-yet\-released features, but this thing from the [Native image output](https://www.youtube.com/watch?v=7RqFLp0TqV0) video caught my eye:

[![On teh left a photo of a mini. A prompt says Turn this car into a convertible and ond the right is that car but now as a convertible.](https://substackcdn.com/image/fetch/$s_!S8W0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8fbeed3f-2cbc-4971-a936-3ff350b36141_1595x714.jpeg "On teh left a photo of a mini. A prompt says Turn this car into a convertible and ond the right is that car but now as a convertible.")](https://substackcdn.com/image/fetch/$s_!S8W0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8fbeed3f-2cbc-4971-a936-3ff350b36141_1595x714.jpeg)

The dream of multi\-modal image output is that models can do *much* more finely grained image editing than has been possible using previous generations of diffusion\-based image models. OpenAI and Amazon have both promised models with these capabilities in the near\-future, so it looks like we're going to have a lot of fun with this stuff in 2025\.

The [Building with Gemini 2\.0: Native audio output](https://www.youtube.com/watch?v=qE673AY-WEI) demo video shows off how good Gemini 2\.0 Flash will be at audio output with different voices, intonations, languages and accents. This looks similar to what's possible with OpenAI's advanced voice mode today.

---

### [ChatGPT Canvas can make API requests now, but it's complicated](https://simonwillison.net/2024/Dec/10/chatgpt-canvas/) \- 2024\-12\-10

Today's [12 Days of OpenAI](https://openai.com/12-days/?day=4) release concerned [ChatGPT Canvas](https://help.openai.com/en/articles/9930697-what-is-the-canvas-feature-in-chatgpt-and-how-do-i-use-it), a new ChatGPT feature that enables ChatGPT to pop open a side panel with a shared editor in it where you can collaborate with ChatGPT on editing a document or writing code.

I'm always excited to see a new form of UI on top of LLMs, and it's great seeing OpenAI stretch out beyond pure chat for this. It's definitely worth playing around with to get a feel for how a collaborative human\+LLM interface can work. The feature where you can ask ChatGPT for "comments on my document" and it will attach them Google Docs style is particularly neat.

I wanted to focus in on one particular aspect of Canvas, because it illustrates a concept I've been talking about for a little while now: the increasing complexity of fully understanding the capabilities of core LLM tools.

#### Canvas runs Python via Pyodide

If a canvas editor contains Python code, ChatGPT adds a new "Run" button at the top of the editor.

ChatGPT has had the ability to run Python for a long time via the excellent [Code Interpreter](https://simonwillison.net/tags/code-interpreter/) feature, which executes Python server\-side in a tightly locked down Kubernetes container managed by OpenAI.

The new Canvas run button is **not the same thing** \- it's an entirely new implementation of code execution that runs code directly in your browser using [Pyodide](https://pyodide.org/) (Python compiled to WebAssembly).

The first time I tried this button I got the following dialog:

[![Run Python code? Python in canvas can make network requests and interact with external systems. Please review your code carefully before proceeding.](https://substackcdn.com/image/fetch/$s_!E0UD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F172609a5-059d-47b8-a32a-7f6e822f3476_986x500.jpeg "Run Python code? Python in canvas can make network requests and interact with external systems. Please review your code carefully before proceeding.")](https://substackcdn.com/image/fetch/$s_!E0UD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F172609a5-059d-47b8-a32a-7f6e822f3476_986x500.jpeg)

"Python in canvas can make network requests"‽ This is a *very new* capability. ChatGPT Code Interpreter has all network access blocked, but apparently ChatGPT Canvas Python does not share that limitation.

I tested this a little bit and it turns out it can make direct HTTP calls from your browser to anywhere online with compatible CORS headers.

(Understanding CORS is [a recurring theme](https://simonwillison.net/search/?q=cors&sort=date&tag=llms) in working with LLMs as a consumer, which I find deeply amusing because it remains a pretty obscure topic even among professional web developers.)

[Claude Artifacts](https://simonwillison.net/tags/claude-artifacts/) allow full JavaScript execution in a Canvas\-like interface within Claude, but even those are severely restricted in terms of the endpoints they can access. OpenAI have apparently made the opposite decision, throwing everything wide open as far as allowed network request targets go.

I prompted ChatGPT like this:

> `use python to fetch "https://datasette.io/content.json?sql=select+*+from+stats++limit+10%0D%0A&_shape=array" and then display it nicely - the JSON looks like this:`
> 
> 
> ```
> [
>   {
>     "package": "airtable-export",
>     "date": "2020-12-14",
>     "downloads": 2
>   },
> ```

I often find pasting the first few lines of a larger JSON example into an LLM gives it enough information to guess the rest.

Here's the result. ChatGPT wrote the code and showed it in a canvas, then I clicked "Run" and had the resulting data displayed in a neat table below:

[![Two columns. On the left is my chat with my prompt. On the right Python code, with a table below showing the results of the API call.](https://substackcdn.com/image/fetch/$s_!eEiP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6bc453a3-4226-4da2-b9e5-96bb5a50990e_2652x1664.jpeg "Two columns. On the left is my chat with my prompt. On the right Python code, with a table below showing the results of the API call.")](https://substackcdn.com/image/fetch/$s_!eEiP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6bc453a3-4226-4da2-b9e5-96bb5a50990e_2652x1664.jpeg)

What a neat and interesting thing! I can now get ChatGPT to write me Python code that fetches from external APIs and displays me the results.

It's not yet as powerful as Claude Artifacts which allows for completely custom HTML\+CSS\+JavaScript interfaces, but it's also *more* powerful than Artifacts because those are not allowed to make outbound HTTP requests at all.

#### What this all means

With the introduction of Canvas, here are some new points that an expert user of ChatGPT now needs to understand:

* ChatGPT can write and then execute code in Python, but there are two different ways it can do that:

	+ If run using Code Interpreter it can access files you upload to it and [a collection of built\-in libraries](https://github.com/simonw/scrape-openai-code-interpreter/blob/main/packages.txt) but cannot make API requests.
	+ If run in a Canvas it uses Pyodide and can access API endpoints, but not files that you upload to it.
* Code Interpreter cannot `pip install` additional packages, though you may be able to [upload them as wheels](https://til.simonwillison.net/llms/code-interpreter-expansions) and convince it to install them.
* Canvas Python can install extra packages using [micropip](https://micropip.pyodide.org/en/stable/project/usage.html), but this will only work for pure Python wheels that are compatible with Pyodide.
* Code interpreter is locked down: it cannot make API requests or communicate with the wider internet at all. If you want it to work on data you need to upload that data to it.
* Canvas Python can fetch data via API requests (directly into your browser), but only from sources that implement an open CORS policy.
* Both Canvas and Code Interpreter remain strictly limited in terms of the custom UI they can offer \- but they both have access to the Pandas ecosystem of visualization tools so they can probably show you charts or tables.

#### This is really, really confusing

Do you find this all hopelessly confusing? I don't blame you. I'm a professional web developer and a Python engineer of 20\+ years and I can just about understand and internalize the above set of rules.

I don't really have any suggestions for where we go from here. This stuff is *hard to use*. The more features and capabilities we pile onto these systems the harder it becomes to obtain true mastery of them and really understand what they can do and how best to put them into practice.

Maybe this doesn't matter? I don't know anyone with true mastery of Excel \- to the point where they could compete in [last week's Microsoft Excel World Championship](https://fmworldcup.com/microsoft-excel-world-championship/) \- and yet plenty of people derive enormous value from Excel despite only scratching the surface of what it can do.

I do think it's worth remembering this as a general theme though. Chatbots may sound easy to use, but they really aren't \- and they're getting harder to use all the time.

#### A new data exfiltration vector

Thinking about this a little more, I think the most meaningful potential security impact from this could be opening up a new data exfiltration vector.

Data exfiltration attacks occur when an attacker tricks someone into pasting malicious instructions into their prompt (often via a [prompt injection attack](https://simonwillison.net/tags/prompt-injection/)) that cause ChatGPT to gather up any available private information from the current conversation and leak it to that attacker in some way.

I imagine it may be possible to construct a pretty gnarly attack that convinces ChatGPT to open up a Canvas and then run Python that leaks any gathered private data to the attacker via an API call.

---

**Link** 2024\-12\-09 [Sora](https://sora.com/):

OpenAI's released their long\-threatened [Sora](https://openai.com/index/sora-is-here/) text\-to\-video model this morning, available in most non\-European countries to subscribers to ChatGPT Plus ($20/month) or Pro ($200/month).

Here's what I got for the very first test prompt I ran through it:

> `A pelican riding a bicycle along a coastal path overlooking a harbor`

The Pelican inexplicably morphs to cycle in the opposite direction half way through, but I don't see that as a particularly significant issue: Sora is built entirely around the idea of directly manipulating and editing and remixing the clips it generates, so the goal isn't to have it produce usable videos from a single prompt.

---

**Quote** 2024\-12\-10

> *The boring yet crucial secret behind good system prompts is test\-driven development. You don't write down a system prompt and find ways to test it. You write down tests and find a system prompt that passes them.   
>   
> For system prompt (SP) development you:   
>   
> \- Write a test set of messages where the model fails, i.e. where the default behavior isn't what you want   
> \- Find an SP that causes those tests to pass   
> \- Find messages the SP is missaplied to and fix the SP   
> \- Expand your test set \& repeat*

[Amanda Askell](https://twitter.com/amandaaskell/status/1866207266761760812)

---

**Quote** 2024\-12\-10

> *Knowing when to use AI turns out to be a form of wisdom, not just technical knowledge. Like most wisdom, it's somewhat paradoxical: AI is often most useful where we're already expert enough to spot its mistakes, yet least helpful in the deep work that made us experts in the first place. It works best for tasks we could do ourselves but shouldn't waste time on, yet can actively harm our learning when we use it to skip necessary struggles.*

[Ethan Mollick](https://www.oneusefulthing.org/p/15-times-to-use-ai-and-5-not-to)

---

**Link** 2024\-12\-10 [The Depths of Wikipedians](https://asteriskmag.com/issues/08/the-depths-of-wikipedians):

Asterisk Magazine interviewed [Annie Rauwerda](https://en.wikipedia.org/wiki/Annie_Rauwerda), curator of the [Depths of Wikipedia](https://en.wikipedia.org/wiki/Depths_of_Wikipedia) family of social media accounts (I particularly like [her TikTok](https://www.tiktok.com/@depthsofwikipedia)).

There's a ton of insight into the dynamics of the Wikipedia community in here.

> \[...] when people talk about Wikipedia as a decision making entity, usually they're talking about 300 people — the people that weigh in to the very serious and (in my opinion) rather arcane, boring, arduous discussions. There's not that many of them.
> 
> There are also a lot of islands. There is one woman who mostly edits about hamsters, and always on her phone. She has never interacted with anyone else. Who is she? She's not part of any community that we can tell.

I appreciated these concluding thoughts on the impact of ChatGPT and LLMs on Wikipedia:

> The traffic to Wikipedia has not taken a dramatic hit. Maybe that will change in the future. The Foundation talks about coming opportunities, or the threat of LLMs. With my friends that edit a lot, it hasn't really come up a ton because I don't think they care. It doesn't affect us. We're doing the same thing. Like if all the large language models eat up the stuff we wrote and make it easier for people to get information — great. We made it easier for people to get information.
> 
> And if LLMs end up training on blogs made by AI slop and having as their basis this ouroboros of generated text, then it's possible that a Wikipedia\-type thing — written and curated by a human — could become even more valuable.

---

**Link** 2024\-12\-10 [From where I left](https://antirez.com/news/144):

Four and a half years after he left the project, Redis creator Salvatore Sanfilippo is returning to work on Redis.

> Hacking randomly was cool but, in the long run, my feeling was that I was lacking a real purpose, and every day I started to feel a bigger urgency to be part of the tech world again. At the same time, I saw the Redis community fragmenting, something that was a bit concerning to me, even as an outsider.

I'm personally still upset at the license change, but Salvatore sees it as necessary to support the commercial business model for Redis Labs. It feels to me like a betrayal of the volunteer efforts by previous contributors. I [posted about that](https://news.ycombinator.com/item?id=42378488#42379400) on Hacker News and Salvatore replied:

> I can understand that, but the thing about the BSD license is that such value never gets lost. People are able to fork, and after a fork for the original project to still lead will be require to put something more on the table.

Salvatore's first new project is an exploration of adding vector sets to Redis. The vector similarity API he previews in this post reminds me of why I fell in love with Redis in the first place \- it's clean, simple and feels obviously right to me.

```
VSIM top_1000_movies_imdb ELE "The Matrix"  WITHSCORES
1) "The Matrix"
2) "0.9999999403953552"
3) "Ex Machina"
4) "0.8680362105369568"
...
```

---

**Link** 2024\-12\-10 [Introducing Limbo: A complete rewrite of SQLite in Rust](https://turso.tech/blog/introducing-limbo-a-complete-rewrite-of-sqlite-in-rust):

This looks absurdly ambitious:

> Our goal is to build a reimplementation of SQLite from scratch, fully compatible at the language and file format level, with the same or higher reliability SQLite is known for, but with full memory safety and on a new, modern architecture.

The Turso team behind it have been maintaining their [libSQL](https://github.com/tursodatabase/libsql) fork for two years now, so they're well equipped to take on a challenge of this magnitude.

SQLite is justifiably famous for its [meticulous approach to testing](https://www.sqlite.org/testing.html). Limbo plans to take an entirely different approach based on "Deterministic Simulation Testing" \- a modern technique [pioneered by FoundationDB](https://antithesis.com/blog/is_something_bugging_you/) and now spearheaded by [Antithesis](https://antithesis.com/), the company Turso have been working with on their previous testing projects.

Another bold claim (emphasis mine):

> We have both added DST facilities to the core of the database, and partnered with Antithesis to achieve a level of reliability in the database that lives up to SQLite’s reputation.
> 
> \[...] With DST, **we believe we can achieve an even higher degree of robustness than SQLite**, since it is easier to simulate unlikely scenarios in a simulator, test years of execution with different event orderings, and upon finding issues, reproduce them 100% reliably.

The two most interesting features that Limbo is planning to offer are first\-party WASM support and fully asynchronous I/O:

> SQLite itself has a synchronous interface, meaning driver authors who want asynchronous behavior need to have the extra complication of using helper threads. Because SQLite queries tend to be fast, since no network round trips are involved, a lot of those drivers just settle for a synchronous interface. \[...]
> 
> Limbo is designed to be asynchronous from the ground up. It extends `sqlite3_step`, the main entry point API to SQLite, to be asynchronous, allowing it to return to the caller if data is not ready to consume immediately.

[Datasette](https://datasette.io/) provides an [async API](https://docs.datasette.io/en/stable/internals.html#await-db-execute-sql) for executing SQLite queries which is backed by all manner of complex thread management \- I would be very interested in a native asyncio Python library for talking to SQLite database files.

I successfully tried out Limbo's [Python bindings](https://github.com/tursodatabase/limbo/tree/main/bindings/python) against a demo SQLite test database using `uv` like this:

```
uv run --with pylimbo python
>>> import limbo
>>> conn = limbo.connect("/tmp/demo.db")
>>> cursor = conn.cursor()
>>> print(cursor.execute("select * from foo").fetchall())
```

It crashed when I tried against a more complex SQLite database that included SQLite FTS tables.

The Python bindings aren't yet documented, so I piped them through [LLM](https://llm.datasette.io/) and had the new `google-exp-1206` model write [this initial documentation](https://gist.github.com/simonw/bd1822f372c406d17ed24772f8b93eea) for me:

```
files-to-prompt limbo/bindings/python -c | llm -m gemini-exp-1206 -s 'write extensive usage documentation in markdown, including realistic usage examples'
```

---

**Quote** 2024\-12\-11

> `(echo "PID COMMAND PORT USER"; lsof -i -P -n | grep LISTEN | awk '{print $2, $1, $9, $3}' | sort -u | head -n 50; echo;) | column -t | llm "what servers are running on my machine and do some of them look like they could be orphaned things I can shut down"`

[Rob Cheung](https://twitter.com/perceptnet/status/1866709399835906116)

---

**Link** 2024\-12\-11 [Who and What comprise AI Skepticism?](https://buildcognitiveresonance.substack.com/p/who-and-what-comprises-ai-skepticism):

Benjamin Riley's response to Casey Newton's piece on [The phony comforts of AI skepticism](https://www.platformer.news/ai-skeptics-gary-marcus-curve-conference/). Casey tried to categorize the field as "AI is fake and sucks" v.s. "AI is real and dangerous". Benjamin argues that this as a misleading over\-simplification, instead proposing at least nine different groups.

I get listed as an example of the "Technical AI Skeptics" group, which sounds right to me based on this description:

> *What this group generally believes*: The technical capabilities of AI are worth trying to understand, including their limitations. Also, it’s fun to find their deficiencies and highlight their weird output.
> 
> *One layer of nuance deeper*: Some of those I identify below might resist being called AI Skeptics because they are focused mainly on helping people understand how these tools work. But in my view, their efforts are helpful in fostering AI skepticism precisely because they help to demystify what’s happening “under the hood” without invoking broader political concerns (generally).

---