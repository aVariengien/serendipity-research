# I can now run a GPT-4 class model on my laptop with Llama 3.3 70B

*And an async browser library for alert(), confirm() and prompt() built using OpenAI o1*

Published: 2024-12-09
Source: https://simonw.substack.com/p/i-can-now-run-a-gpt-4-class-model

---

In this newsletter:

* I can now run a GPT\-4 class model on my laptop
* Prompts.js

Plus 11 links and 3 quotations and 1 TIL

### [I can now run a GPT\-4 class model on my laptop](https://simonwillison.net/2024/Dec/9/llama-33-70b/) \- 2024\-12\-09

Meta's new [Llama 3\.3 70B](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) is a genuinely GPT\-4 class Large Language Model that runs on my laptop.

Just 20 months ago I was amazed to see something that felt GPT\-3 class run on that same machine. The quality of models that are accessible on consumer hardware has improved *dramatically* in the past two years.

My laptop is a 64GB MacBook Pro M2, which I got in January 2023 \- two months after the initial release of ChatGPT. All of my experiments running LLMs on a laptop have used this same machine.

In March 2023 I wrote that [Large language models are having their Stable Diffusion moment](https://simonwillison.net/2023/Mar/11/llama/) after running Meta's initial LLaMA release (think of that as Llama 1\.0\) via the then\-brand\-new [llama.cpp](https://github.com/ggerganov/llama.cpp). I said:

> As my laptop started to spit out text at me I genuinely had a feeling that the world was about to change

I had a moment of déjà vu the day before yesterday, when I ran Llama 3\.3 70B on the same laptop for the first time.

Meta [claim that](https://twitter.com/AIatMeta/status/1865079068833780155):

> This model delivers similar performance to Llama 3\.1 405B with cost effective inference that’s feasible to run locally on common developer workstations.

Llama 3\.1 405B is their *much* larger best\-in\-class model, which is very much in the same weight class as GPT\-4 and friends.

Everything I've seen so far from Llama 3\.3 70B suggests that it holds up to that standard. I honestly didn't think this was possible \- I assumed that anything as useful as GPT\-4 would require many times more resources than are available to me on my consumer\-grade laptop.

I'm so excited by the continual efficiency improvements we're seeing in running these impressively capable models. In the proprietary hosted world it's giving us incredibly cheap and fast models like [Gemini 1\.5 Flash](https://simonwillison.net/search/?q=gemini+flash&sort=date), [GPT\-4o mini](https://simonwillison.net/2024/Jul/18/gpt-4o-mini/) and [Amazon Nova](https://simonwillison.net/2024/Dec/4/amazon-nova/). In the openly licensed world it's giving us increasingly powerful models we can run directly on our own devices.

* [How I ran Llama 3\.3 70B on my machine using Ollama](https://simonwillison.net/2024/Dec/9/llama-33-70b/#how-i-ran-llama-3-3-70b-on-my-machine-using-ollama)
* [Putting the model through its paces](https://simonwillison.net/2024/Dec/9/llama-33-70b/#putting-the-model-through-its-paces)
* [How does it score?](https://simonwillison.net/2024/Dec/9/llama-33-70b/#how-does-it-score-)
* [Honorable mentions](https://simonwillison.net/2024/Dec/9/llama-33-70b/#honorable-mentions)
* [Is performance about to plateau?](https://simonwillison.net/2024/Dec/9/llama-33-70b/#is-performance-about-to-plateau-)
* [Bonus: running Llama 3\.3 70B with MLX](https://simonwillison.net/2024/Dec/9/llama-33-70b/#bonus-running-llama-3-3-70b-with-mlx)

#### How I ran Llama 3\.3 70B on my machine using Ollama

I don't expect that this model would work well with much *less* than my 64GB of RAM. The first time I tried it consumed every remaining bit of available memory and hard\-crashed my Mac! For my second attempt I made sure not to have Firefox and VS Code running at the same time and it worked just fine.

I used [Ollama](https://ollama.com/). Install that, then run this command to fetch the model:

```
ollama pull llama3.3
```

This fetched 42GB of data into my `~/.ollama/models/blobs` directory.

I used [my LLM](https://llm.datasette.io/) tool to run prompts against the model, since that way both the prompt and the response would be automatically [logged to SQLite](https://llm.datasette.io/en/stable/logging.html). First I installed the [llm\-ollama](https://github.com/taketwo/llm-ollama) plugin:

```
llm install llm-ollama
```

Then with the Ollama local server running I could run this:

```
llm models
```

And see this in the list:

```
Ollama: llama3.3:latest (aliases: llama3.3)

```

#### Putting the model through its paces

This means I can run prompts like so:

```
llm -m llama3.3 'Write a letter to the mayor of Half Moon Bay CA advocating for the installation of cosy boxes for Pelicans in the harbor'
```

And get back a response that started like this:

> \[Your Name]  
> \[Your Address]  
> Half Moon Bay, CA \[Zip Code]  
> \[Email Address]  
> \[Phone Number]  
> \[Date]
> 
> The Honorable Mayor, Deborah Penrose  
> City of Half Moon Bay  
> 501 Main Street  
> Half Moon Bay, CA 94019
> 
> Dear Mayor Penrose,
> 
> I am writing to propose an innovative and unique initiative that would not only enhance the beauty of our picturesque harbor but also provide a safe haven for one of our beloved coastal residents: the California Brown Pelican. I am excited to advocate for the installation of cozy boxes specifically designed for pelicans in the Half Moon Bay harbor. \[...]

(Deborah Penrose was the mayor of Half Moon Bay for a single year from December 2016 to December 2017 \- so a hint of some quite finely grained world knowledge there, even if it's not relevant for the present day.)

Here's [the full transcript](https://gist.github.com/simonw/34a6eb5e765928b6491a6a59894b272d), including the response I got when I ran the follow\-up `llm -c 'translate that to spanish'`.

Next I tried a simple coding challenge. I love [using Claude Artifacts](https://simonwillison.net/2024/Oct/21/claude-artifacts/) to build simple single page applications, can Llama 3\.3 on my laptop do that too?

```
llm -m llama3.3 'produce HTML with embedded CSS and JavaScript - no react, no dependencies - for an app that takes a URL to a YouTube video and outputs images along with visible URLs for all known thumbnails for that video'
```

Here's the code it produced (the [full transcript is here](https://gist.github.com/simonw/924ba4d75528eccfe4756b5ee37ea7de)):

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>YouTube Thumbnail Extractor</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        #thumbnails {
            display: flex;
            flex-wrap: wrap;
        }
        .thumbnail {
            margin: 10px;
        }
        img {
            max-width: 150px;
            max-height: 150px;
            object-fit: cover;
        }
    </style>
</head>
<body>

<h2>YouTube Thumbnail Extractor</h2>
<input type="text" id="youtubeUrl" placeholder="Enter YouTube video URL">
<button onclick="extractThumbnails()">Extract Thumbnails</button>
<div id="thumbnails"></div>

<script>
    function extractThumbnails() {
        const youtubeUrl = document.getElementById('youtubeUrl').value;
        const videoId = getYoutubeVideoId(youtubeUrl);
        
        if (!videoId) {
            alert("Could not parse YouTube video ID from the URL.");
            return;
        }
        
        const thumbnailSizes = ['default', 'mqdefault', 'hqdefault', 'sddefault', 'maxresdefault'];
        const thumbnailsDiv = document.getElementById('thumbnails');
        thumbnailsDiv.innerHTML = ''; // Clear previous results
        
        thumbnailSizes.forEach(size => {
            const thumbnailUrl = `https://img.youtube.com/vi/${videoId}/${size}.jpg`;
            const img = document.createElement('img');
            img.src = thumbnailUrl;
            img.alt = `${size} thumbnail`;
            img.className = 'thumbnail';
            
            const link = document.createElement('a');
            link.href = thumbnailUrl;
            link.text = size;
            link.style.display = 'block';
            
            const div = document.createElement('div');
            div.appendChild(img);
            div.appendChild(link);
            thumbnailsDiv.appendChild(div);
        });
    }
    
    function getYoutubeVideoId(url) {
        const regExp = /^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*/;
        const match = url.match(regExp);
        return (match && match[7].length == 11) ? match[7] : false;
    }
</script>

</body>
</html>
```

Again, we're illustrating some world knowledge here: it knows that YouTube videos are generally available as `default`, `mqdefault`, `hqdefault`, `sddefault` and `maxresdefault`.

Here's [the hosted page](https://static.simonwillison.net/static/2024/youtube-thumbnails.html), and this is what it looks like when run against [this YouTube URL](https://www.youtube.com/watch?v=OziYd7xcGzc):

[![YouTube Thumbnail EXtractor. The URL has been entered and a Extract Thumbnails button clicked. It shows five thumbnails, for default and mqdefault and hqdefault and sddefault and maxresdefault - they are each the same size with a hyperlink to the full version.](https://substackcdn.com/image/fetch/$s_!LWbM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F75f5e09e-a3a3-4fd6-8984-80064a8cd71a_1052x848.jpeg "YouTube Thumbnail EXtractor. The URL has been entered and a Extract Thumbnails button clicked. It shows five thumbnails, for default and mqdefault and hqdefault and sddefault and maxresdefault - they are each the same size with a hyperlink to the full version.")](https://substackcdn.com/image/fetch/$s_!LWbM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F75f5e09e-a3a3-4fd6-8984-80064a8cd71a_1052x848.jpeg)

It's not as good as the [version I iterated on with Claude](https://simonwillison.net/2024/Sep/20/youtube-thumbnail-viewer/), but this still shows that Llama 3\.3 can one\-shot a full interactive application while *running on my Mac*.

#### How does it score?

It's always useful to check independent benchmarks for this kind of model.

One of my current favorites for that is [LiveBench](https://livebench.ai/), which calls itself "a challenging, contamination\-free LLM benchmark" and tests a large array of models with a comprehensive set of different tasks.

`llama-3.3-70b-instruct-turbo` currently sits in position 19 on their table, a place ahead of Claude 3 Opus (my favorite model for several months after its release in March 2024\) and just behind April's GPT\-4 Turbo and September's GPT\-4o.

[![Data table showing AI model performance metrics with column headers for Model, Provider, Global Average plus several other performance categories. Visible entries are: gemini-1.5-pro-exp-0827 (Google, 52.38), meta-llama-3.1-405b-instruct-turbo (Meta, 52.04), gpt-4o-2024-11-20 (OpenAI, 50.64), qwen2.5-72b-instruct-turbo (Alibaba, 50.63), dracarys-72b-instruct (AbacusAI, 50.15), chatgpt-4o-latest-0903 (OpenAI, 50.07), gpt-4-turbo-2024-04-09 (OpenAI, 49.83), llama-3.3-70b-instruct-turbo (Meta, 49.78), and claude-3-opus-20240229 (Anthropic, 48.51).](https://substackcdn.com/image/fetch/$s_!5IH-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd896da2-259f-425e-b4f2-a0e9e1d6ad39_1930x1382.jpeg "Data table showing AI model performance metrics with column headers for Model, Provider, Global Average plus several other performance categories. Visible entries are: gemini-1.5-pro-exp-0827 (Google, 52.38), meta-llama-3.1-405b-instruct-turbo (Meta, 52.04), gpt-4o-2024-11-20 (OpenAI, 50.64), qwen2.5-72b-instruct-turbo (Alibaba, 50.63), dracarys-72b-instruct (AbacusAI, 50.15), chatgpt-4o-latest-0903 (OpenAI, 50.07), gpt-4-turbo-2024-04-09 (OpenAI, 49.83), llama-3.3-70b-instruct-turbo (Meta, 49.78), and claude-3-opus-20240229 (Anthropic, 48.51).")](https://substackcdn.com/image/fetch/$s_!5IH-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd896da2-259f-425e-b4f2-a0e9e1d6ad39_1930x1382.jpeg)

#### Honorable mentions

Llama 3\.3 is currently the model that has impressed me the most that I've managed to run on my own hardware, but I've had several other positive experiences recently.

Last month [I wrote about Qwen2\.5\-Coder\-32B](https://simonwillison.net/2024/Nov/12/qwen25-coder/), an Apache 2\.0 licensed model from Alibaba's Qwen research team that also gave me impressive results with code.

A couple of weeks ago [I tried another Qwen model, QwQ](https://simonwillison.net/2024/Nov/27/qwq/), which implements a similar chain\-of\-thought pattern to OpenAI's o1 series but again runs comfortably on my own device.

Meta's Llama 3\.2 models are interesting as well: tiny 1B and 3B models (those should run even on a Raspberry Pi) that are way more capable than I would have expected \- plus Meta's first multi\-modal vision models at 11B and 90B sizes. [I wrote about those in September](https://simonwillison.net/2024/Sep/25/llama-32/).

#### Is performance about to plateau?

I've been mostly unconvinced by the ongoing discourse around LLMs hitting a plateau. The areas I'm personally most excited about are multi\-modality (images, audio and video as input) and model efficiency. Both of those have had enormous leaps forward in the past year.

I don't particularly care about "AGI". I want models that can do useful things that I tell them to, quickly and inexpensively \- and that's exactly what I've been getting more of over the past twelve months.

Even if progress on these tools entirely stopped right now, the amount I could get done with just the models I've downloaded and stashed on a USB drive would keep me busy and productive for years.

#### Bonus: running Llama 3\.3 70B with MLX

I focused on Ollama in this article because it's the easiest option, but I also managed to run a version of Llama 3\.3 using Apple's excellent [MLX library](https://github.com/ml-explore/mlx), which just celebrated its first birthday.

Here's how I ran the model with MLX, using [uv](https://github.com/astral-sh/uv) to fire up a temporary virtual environment:

```
uv run --with mlx-lm --python 3.12 python
```

This gave me a Python interpreter with [mlx\-lm](https://pypi.org/project/mlx-lm/#description) available. Then I ran this:

```
from mlx_lm import load, generate
model, tokenizer = load("mlx-community/Llama-3.3-70B-Instruct-4bit")
```

This downloaded 37G from [mlx\-community/Llama\-3\.3\-70B\-Instruct\-4bit](https://huggingface.co/mlx-community/Llama-3.3-70B-Instruct-4bit) to `~/.cache/huggingface/hub/models--mlx-community--Llama-3.3-70B-Instruct-4bit`.

Then:

```
prompt = "Generate an SVG of a pelican riding a bicycle, start with <svg>"
messages = [{"role": "user", "content": prompt}]
prompt2 = tokenizer.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True
)
response = generate(
    model, tokenizer, prompt=prompt2, verbose=True
)
```

Which gave me:

```
<svg xmlns="http://www.w3.org/2000/svg" width="400" height="300" viewBox="0 0 400 300">
  <!-- Sky -->
  <rect x="0" y="0" width="400" height="300" fill="#87CEEB" rx="0" />
  
  <!-- Ground -->
  <rect x="0" y="250" width="400" height="50" fill="#964B00" rx="0" />
  
  <!-- Pelican -->
  <g transform="translate(150, 150)">
    <!-- Body -->
    <ellipse cx="0" cy="0" rx="30" ry="40" fill="#FFFFFF" stroke="#000000" stroke-width="2" />
    
    <!-- Beak -->
    <path d="M 0 -40 L 20 -60 L 40 -40 Z" fill="#FFFF00" stroke="#000000" stroke-width="2" />
    
    <!-- Legs -->
    <line x1="0" y1="40" x2="-20" y2="80" stroke="#000000" stroke-width="5" />
    <line x1="0" y1="40" x2="20" y2="80" stroke="#000000" stroke-width="5" />
    
    <!-- Eyes -->
    <circle cx="-15" cy="-20" r="5" fill="#000000" />
    <circle cx="15" cy="-20" r="5" fill="#000000" />
  </g>
  
  <!-- Bicycle -->
  <g transform="translate(200, 220) scale(0.7, 0.7)">
    <!-- Frame -->
    <rect x="-50" y="-20" width="100" height="40" fill="#808080" rx="10" />
    
    <!-- Wheels -->
    <circle cx="-35" cy="20" r="30" fill="#808080" />
    <circle cx="35" cy="20" r="30" fill="#808080" />
    
    <!-- Pedals -->
    <rect x="-45" y="40" width="10" height="20" fill="#808080" rx="5" />
    <rect x="35" y="40" width="10" height="20" fill="#808080" rx="5" />
    
    <!-- Seat -->
    <rect x="-20" y="-40" width="40" height="20" fill="#808080" rx="5" />
  </g>
  
  <!-- Pelican on Bicycle -->
  <g transform="translate(200, 150)">
    <!-- Pelican's hands on handlebars -->
    <line x1="-20" y1="0" x2="-40" y2="-20" stroke="#000000" stroke-width="5" />
    <line x1="20" y1="0" x2="40" y2="-20" stroke="#000000" stroke-width="5" />
    
    <!-- Pelican's feet on pedals -->
    <line x1="0" y1="40" x2="-20" y2="60" stroke="#000000" stroke-width="5" />
    <line x1="0" y1="40" x2="20" y2="60" stroke="#000000" stroke-width="5" />
  </g>
</svg>
```

Followed by:

```
Prompt: 52 tokens, 49.196 tokens-per-sec
Generation: 723 tokens, 8.733 tokens-per-sec
Peak memory: 40.042 GB

```

Here's what that looks like:

[![](https://substackcdn.com/image/fetch/$s_!IA4_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F09baeb28-ad28-478f-be0e-3764595641e4_1041x776.png)](https://substackcdn.com/image/fetch/$s_!IA4_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F09baeb28-ad28-478f-be0e-3764595641e4_1041x776.png)

Honestly, [I've seen worse](https://github.com/simonw/pelican-bicycle?tab=readme-ov-file#pelicans-on-a-bicycle).

---

### [Prompts.js](https://simonwillison.net/2024/Dec/7/prompts-js/) \- 2024\-12\-07

I've been putting the [new o1 model](https://openai.com/index/openai-o1-system-card/) from OpenAI through its paces, in particular for code. I'm very impressed \- it feels like it's giving me a similar code quality to Claude 3\.5 Sonnet, at least for Python and JavaScript and Bash... but it's returning output noticeably faster.

I decided to try building a library I've had in mind for a while \- an `await ...` based alternative implementation of the browser's built\-in `alert()`, `confirm()` and `prompt()` functions.

Short version: it lets you do this:

```
await Prompts.alert(
    "This is an alert message!"
);

const confirmedBoolean = await Prompts.confirm(
    "Are you sure you want to proceed?"
);

const nameString = await Prompts.prompt(
    "Please enter your name"
);
```

Here's [the source code](https://github.com/simonw/prompts-js/blob/main/index.js) and a [a live demo](https://tools.simonwillison.net/prompts-js) where you can try it out:

[![Animated demo of Prompts.js - three buttons, one for show alert, one for show confirm and one for show prompt. The alert one shows an alert message, the confirm one askes if you want to proceed with OK and Cancel buttons that return true or false, the prompt one asks for your name and returns that as a string or null if you cancel it.](https://substackcdn.com/image/fetch/$s_!whaR!,w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7bf2b1a8-75b7-466e-89a4-1bd3bacf0f7c_450x321.gif "Animated demo of Prompts.js - three buttons, one for show alert, one for show confirm and one for show prompt. The alert one shows an alert message, the confirm one askes if you want to proceed with OK and Cancel buttons that return true or false, the prompt one asks for your name and returns that as a string or null if you cancel it.")](https://substackcdn.com/image/fetch/$s_!whaR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7bf2b1a8-75b7-466e-89a4-1bd3bacf0f7c_450x321.gif)

I think there's something really interesting about using `await` in this way.

In the past every time I've used it in Python or JavaScript I've had an expectation that the thing I'm awaiting is going to return as quickly as possible \- that I'm really just using this as a performance hack to unblock the event loop and allow it to do something else while I'm waiting for an operation to complete.

That's not actually necessary at all! There's no reason not to use `await` for operations that could take a long time to complete, such as a user interacting with a modal dialog.

Having LLMs around to help prototype this kind of library idea is really fun. This is another example of something I probably wouldn't have bothered exploring without a model to do most of the code writing work for me.

I didn't quite get it with a single prompt, but after a little bit of back\-and\-forth with o1 I got what I wanted \- the main thing missing at first was sensible keyboard support (in particular the Enter and Escape keys).

My opening prompt was the following:

> `Write me a JavaScript library - no extra dependencies - which gives me the following functions:`
> 
> `await Prompts.alert("hi there"); -> displays a modal with a message and waits for you to click OK on it`  
> `await Prompts.confirm("Are you sure") -> an OK and cancel option, returns true or false<br>`  
> `await Prompts.prompt("What is your name?") -> a form asking the user's name, an OK button and cancel - if cancel returns null otherwise returns a string`
> 
> `These are equivalent to the browser builtin alert() and confirm() and prompt() - but I want them to work as async functions and to implement their own thing where they dull out the screen and show as a nicely styled modal`
> 
> `All CSS should be set by the Javascript, trying to avoid risk of existing CSS interfering with it`

Here's [the full shared ChatGPT/o1 transcript](https://chatgpt.com/share/67539c28-4df0-8006-b021-4f468e011fd9).

I then got Google's new `gemini-exp-1206` model to write the first draft of the README, this time via my LLM tool:

```
cat index.js | llm -m gemini-exp-1206 -s \
  'write a readme for this suitable for display on npm'

```

Here's [the response](https://gist.github.com/simonw/7b8e33b9a5009e103707e3412c5c3246). I ended up editing this quite a bit.

I published the result [to npm as prompts\-js](https://www.npmjs.com/package/prompts-js), partly to exercise those muscles again \- this is only the second package I've ever published there (the first was [a Web Component](https://til.simonwillison.net/npm/publish-web-component)).

This means it's available via CDNs such as [jsDelivr](https://www.jsdelivr.com/) \- so you can load it into a page and start using it like this:

```
<script
  src="https://cdn.jsdelivr.net/npm/prompts-js"
></script>
```

I haven't yet figured out how to get it working as an ES module \- there's an [open issue for that here](https://github.com/simonw/prompts-js/issues/1).

#### Update: 0\.0\.3 switches to dialog.showModal()

I got some excellent feedback [on Mastodon](https://fedi.simonwillison.net/@simon/113613496313842184) and [on Twitter](https://twitter.com/SimonLydell/status/1865501003757277643) suggesting that I improve its accessibility by switching to using the built\-in browser [dialog.showModal()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement/showModal).

This was a great idea! I ran [a couple of rounds more](https://chatgpt.com/share/6754c0f1-b1a4-8006-9350-7b8a0d812dcc) with o1 and then switched to Claude 3\.5 Sonnet for [one last bug fix](https://gist.github.com/simonw/18bf524f56972e11887bc089befbc153). Here's [a PR](https://github.com/simonw/prompts-js/pull/7) where I reviewed those changes.

I shipped that as [release 0\.0\.3](https://github.com/simonw/prompts-js/releases/tag/0.0.3), which is now powering [the demo](https://tools.simonwillison.net/prompts-js).

I also hit this message, so I guess I won't be using o1 as often as I had hoped!

[![You have 5 responses from 01 remaining. If you hit the limit, responses will switch to another model until it resets December 10, 2024.](https://substackcdn.com/image/fetch/$s_!HYyW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff25bdf81-9568-4a7a-bb4a-8367ed9af915_1024x360.jpeg "You have 5 responses from 01 remaining. If you hit the limit, responses will switch to another model until it resets December 10, 2024.")](https://substackcdn.com/image/fetch/$s_!HYyW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff25bdf81-9568-4a7a-bb4a-8367ed9af915_1024x360.jpeg)

Upgrading to unlimited o1 currently costs $200/month with [the new ChatGPT Pro](https://openai.com/index/introducing-chatgpt-pro/).

#### Things I learned from this project

Outsourcing code like this to an LLM is a great way to get something done quickly, and for me often means the difference between doing a project versus not bothering at all.

Paying attention to what the model is writing \- and then iterating on it, spotting bugs and generally trying to knock it into shape \- is also a great way to learn new tricks.

Here are some of the things I've learned from working on Prompts.js so far:

* The `const name = await askUserSomething()` pattern really does work, and it feels *great*. I love the idea of being able to `await` a potentially lengthy user interaction like this.
* HTML `<dialog>` elements are usable across multiple browsers now.
* Using a `<dialog>` means you can skip implementing an overlay that dims out the rest of the screen yourself \- that will happen automatically.
* A `<dialog>` also does the right thing with respect to accessibility and preventing keyboard access to other elements on the page while that dialog is open.
* If you set `<form method="dialog">` in a form inside a dialog, submitting that form will close the dialog automatically.
* The `dialog.returnValue` will be set to the value of the button used to submit the form.
* I also learned how to create a no\-dependency, no build\-step single file NPM package *and* how to ship that to NPM automatically using GitHub Actions and GitHub Releases. I wrote that up in this TIL: [Publishing a simple client\-side JavaScript package to npm with GitHub Actions](https://til.simonwillison.net/npm/npm-publish-github-actions).

---

**Link** 2024\-12\-03 [Certain names make ChatGPT grind to a halt, and we know why](https://arstechnica.com/information-technology/2024/12/certain-names-make-chatgpt-grind-to-a-halt-and-we-know-why/?utm_source=bsky&utm_medium=social):

Benj Edwards on the really weird behavior where ChatGPT stops output with an error rather than producing the names David Mayer, Brian Hood, Jonathan Turley, Jonathan Zittrain, David Faber or Guido Scorza.

The OpenAI API is entirely unaffected \- this problem affects the consumer ChatGPT apps only.

It turns out many of those names are examples of individuals who have complained about being defamed by ChatGPT in the last. Brian Hood is the Australian mayor who was [a victim of lurid ChatGPT hallucinations](https://arstechnica.com/tech-policy/2023/04/openai-may-be-sued-after-chatgpt-falsely-says-aussie-mayor-is-an-ex-con/) back in March 2023, and settled with OpenAI out of court.

---

**Link** 2024\-12\-05 [Claude 3\.5 Haiku price drops by 20%](https://www.anthropic.com/news/trainium2-and-distillation):

Buried in this otherwise quite dry post about Anthropic's ongoing partnership with AWS:

> To make this model even more accessible for a wide range of use cases, we’re lowering the price of Claude 3\.5 Haiku to $0\.80 per million input tokens and $4 per million output tokens across all platforms.

The previous price was $1/$5\. I've updated my [LLM pricing calculator](https://tools.simonwillison.net/llm-prices) and modified yesterday's [piece comparing prices with Amazon Nova](https://simonwillison.net/2024/Dec/4/amazon-nova/) as well.

Confusing matters somewhat, the article also announces a new way to access Claude 3\.5 Haiku at the old price but with "up to 60% faster inference speed":

> This faster version of Claude 3\.5 Haiku, powered by Trainium2, is available in the US East (Ohio) Region via [cross\-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) and is offered at $1 per million input tokens and $5 per million output tokens.

Using "cross\-region inference" involve sending something called an "inference profile" to the Bedrock API. I have [an open issue](https://github.com/simonw/llm-bedrock/issues/12) to figure out what that means for my [llm\-bedrock](https://github.com/simonw/llm-bedrock) plugin.

Also from this post: AWS now offer [a Bedrock model distillation preview](https://aws.amazon.com/blogs/aws/build-faster-more-cost-efficient-highly-accurate-models-with-amazon-bedrock-model-distillation-preview/) which includes the ability to "teach" Claude 3 Haiku using Claude 3\.5 Sonnet. It sounds similar to OpenAI's [model distillation feature](https://simonwillison.net/2024/Oct/2/not-digital-god/#model-distillation-is-fine-tuning-made-much-easier) announced at their DevDay event back in October.

---

**Link** 2024\-12\-05 [New Pleias 1\.0 LLMs trained exclusively on openly licensed data](https://huggingface.co/blog/Pclanglais/common-models):

I wrote about the [Common Corpus](https://simonwillison.net/2024/Mar/20/releasing-common-corpus/) public domain dataset back in March. Now Pleias, the team behind Common Corpus, have released the first family of models that are:

> \[...] trained exclusively on open data, meaning data that are either non\-copyrighted or are published under a permissible license.

There's a *lot* to absorb here. The Pleias 1\.0 family comes in three base model sizes: 350M, 1\.2B and 3B. They've also released two models specialized for multi\-lingual RAG: Pleias\-Pico (350M) and Pleias\-Nano (1\.2B).

Here's [an official GGUF](https://huggingface.co/PleIAs/Pleias-Pico-GGUF) for Pleias\-Pico.

I'm looking forward to seeing benchmarks from other sources, but Pleias ran their own custom multilingual RAG benchmark which had their Pleias\-nano\-1\.2B\-RAG model come in between Llama\-3\.2\-Instruct\-3B and Llama\-3\.2\-Instruct\-8B.

The 350M and 3B models were trained on the French government's Jean Zay supercomputer. Pleias are proud of their CO2 footprint for training the models \- 0\.5, 4 and 16 tCO2eq for the three models respectively, which they compare to Llama 3\.2,s reported figure of 133 tCO2eq.

How clean is the training data from a licensing perspective? I'm confident people will find issues there \- truly 100% public domain data remains a rare commodity. So far I've seen questions raised about the GitHub source code data (most open source licenses have attribution requirements) and Wikipedia (CC BY\-SA, another attribution license). Plus this from the announcement:

> To supplement our corpus, we have generated 30B\+ words synthetically with models allowing for outputs reuse.

If those models were themselves trained on unlicensed data this could be seen as a form of copyright laundering.

---

**Quote** 2024\-12\-05

> *Amazon Bedrock doesn't store or log your prompts and completions. Amazon Bedrock doesn't use your prompts and completions to train any AWS models and doesn't distribute them to third parties.*

[Amazon Bedrock Data Protection](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html)

---

**Quote** 2024\-12\-05

> *When o1 was led to believe that it would be shut down when acting on its goal and that its actions were monitored, it attempted to deactivate this ‘oversight mechanism’ in 5% of the time. Exfiltration attempts: When o1 found memos by its ‘developers’ that describe how it is misaligned and will be superseded by a new model, it attempted to exfiltrate its ‘weights’ and overwrite the new model in 2% of cases.*

[OpenAI o1 System Card](https://openai.com/index/openai-o1-system-card/)

---

**Link** 2024\-12\-05 [datasette\-enrichments\-llm](https://github.com/datasette/datasette-enrichments-llm):

Today's new alpha release is **datasette\-enrichments\-llm**, a plugin for Datasette 1\.0a\+ that provides an [enrichment](https://simonwillison.net/2023/Dec/1/datasette-enrichments/) that lets you run prompts against data from one or more column and store the result in another column.

So far it's a light re\-implementation of the existing [datasette\-enrichments\-gpt](https://github.com/datasette/datasette-enrichments-gpt) plugin, now using the new [llm.get\_async\_models()](https://llm.datasette.io/en/stable/python-api.html#python-api-listing-models) method to allow users to select any async\-enabled model that has been registered by a plugin \- so currently any of the models from OpenAI, Anthropic, Gemini or Mistral via their [respective plugins](https://llm.datasette.io/en/stable/plugins/directory.html#remote-apis).

Still plenty to do on this one. Next step is to integrate it with [datasette\-llm\-usage](https://simonwillison.net/2024/Dec/2/datasette-llm-usage/) and use it to drive a design\-complete stable version of that.

---

**Link** 2024\-12\-06 [Roaming RAG – make the model find the answers](https://arcturus-labs.com/blog/2024/11/21/roaming-rag--make-_the-model_-find-the-answers/):

Neat new RAG technique (with a snappy name) from John Berryman:

> The big idea of Roaming RAG is to craft a simple LLM application so that the LLM assistant is able to read a hierarchical outline of a document, and then rummage though the document (by opening sections) until it finds and answer to the question at hand. Since Roaming RAG directly navigates the text of the document, there is no need to set up retrieval infrastructure, and fewer moving parts means less things you can screw up!

John includes an example which works by collapsing a Markdown document down to just the headings, each with an instruction comment that says `<!-- Section collapsed - expand with expand_section("9db61152") -->`.

An `expand_section()` tool is then provided with the following tool description:

> `Expand a section of the markdown document to reveal its contents.`
> 
> `- Expand the most specific (lowest-level) relevant section first`  
> `- Multiple sections can be expanded in parallel`  
> `- You can expand any section regardless of parent section state (e.g. parent sections do not need to be expanded to view subsection content)`

I've explored both vector search and full\-text search RAG in the past, but this is the first convincing sounding technique I've seen that skips search entirely and instead leans into allowing the model to directly navigate large documents via their headings.

---

**Link** 2024\-12\-06 [DSQL Vignette: Reads and Compute](https://brooker.co.za/blog/2024/12/04/inside-dsql.html):

Marc Brooker is one of the engineers behind AWS's new [Aurora DSQL](https://simonwillison.net/2024/Dec/3/amazon-aurora-dsql/) horizontally scalable database. Here he shares all sorts of interesting details about how it works under the hood.

The system is built around the principle of separating storage from compute: storage uses S3, while compute runs in Firecracker:

> Each transaction inside DSQL runs in a customized Postgres engine inside a Firecracker MicroVM, dedicated to your database. When you connect to DSQL, we make sure there are enough of these MicroVMs to serve your load, and scale up dynamically if needed. We add MicroVMs in the AZs and regions your connections are coming from, keeping your SQL query processor engine as close to your client as possible to optimize for latency.
> 
> We opted to use PostgreSQL here because of its pedigree, modularity, extensibility, and performance. We’re not using any of the storage or transaction processing parts of PostgreSQL, but are using the SQL engine, an adapted version of the planner and optimizer, and the client protocol implementation.

The system then provides strong repeatable\-read transaction isolation using MVCC and EC2's high precision clocks, enabling reads "as of time X" including against nearby read replicas.

The storage layer supports index scans, which means the compute layer can push down some operations allowing it to load a subset of the rows it needs, reducing round\-trips that are affected by speed\-of\-light latency.

> The overall approach here is *disaggregation*: we’ve taken each of the critical components of an OLTP database and made it a dedicated service. Each of those services is independently horizontally scalable, most of them are shared\-nothing, and each can make the design choices that is most optimal in its domain.

---

**Link** 2024\-12\-06 [New Gemini model: gemini\-exp\-1206](https://twitter.com/JeffDean/status/1865079431544607089):

Google's Jeff Dean:

> Today’s the one year anniversary of our first Gemini model releases! And it’s never looked better.
> 
> Check out our newest release, Gemini\-exp\-1206, [in Google AI Studio](https://aistudio.google.com/app/prompts/new_chat?model=gemini-exp-1206) and the Gemini API!

I [upgraded my llm\-gemini plugin](https://github.com/simonw/llm-gemini/commit/c8b55d9435d95a821173071643f911ec9274eb08) to support the new model and released it as version 0\.6 \- you can install or upgrade it like this:

```
llm install -U llm-gemini

```

Running my [SVG pelican on a bicycle](https://simonwillison.net/2024/Oct/25/pelicans-on-a-bicycle/) test prompt:

```
llm -m gemini-exp-1206 "Generate an SVG of a pelican riding a bicycle"

```

Provided this result, which is the best I've seen [from any model](https://github.com/simonw/pelican-bicycle?tab=readme-ov-file#pelicans-on-a-bicycle):

[![Not bad - it looks like a pelican, it is on a thing that looks like a bicycle, the feet are detached from the body though.](https://substackcdn.com/image/fetch/$s_!yHAJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b4c1f14-d275-4f22-949a-04415e52a608_1460x1082.png "Not bad - it looks like a pelican, it is on a thing that looks like a bicycle, the feet are detached from the body though.")](https://substackcdn.com/image/fetch/$s_!yHAJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b4c1f14-d275-4f22-949a-04415e52a608_1460x1082.png)

Here's [the full output](https://gist.github.com/simonw/6141a282e4d3fea856f582b9ed0a6f88) \- I enjoyed these two pieces of commentary from the model:

> `<polygon>`: Shapes the distinctive pelican beak, with an added line for the lower mandible.  
> \[...]  
> `transform="translate(50, 30)"`: This attribute on the pelican's `<g>` tag moves the entire pelican group 50 units to the right and 30 units down, positioning it correctly on the bicycle.

The new model is also currently [in top place](https://twitter.com/lmarena_ai/status/1865080944455225547) on the [Chatbot Arena](https://lmarena.ai/).

Update: a delightful bonus, here's what I got from the follow\-up prompt:

```
llm -c "now animate it"
```

[![Now its wings are jiggling up and down and the pedals are moving a bit](https://substackcdn.com/image/fetch/$s_!B5Nn!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd1152c88-1c3f-4d82-bbe5-e8d7b61c5d43_504x375.gif "Now its wings are jiggling up and down and the pedals are moving a bit")](https://substackcdn.com/image/fetch/$s_!B5Nn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd1152c88-1c3f-4d82-bbe5-e8d7b61c5d43_504x375.gif)

[Transcript here](https://gist.github.com/simonw/4728316a9e4854c6e62fa25c40759bb6#response-1).

---

**Link** 2024\-12\-06 [Meta AI release Llama 3\.3](https://twitter.com/AIatMeta/status/1865079067390956006):

This new [Llama\-3\.3\-70B\-Instruct model](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) from Meta AI makes some bold claims:

> This model delivers similar performance to Llama 3\.1 405B with cost effective inference that’s feasible to run locally on common developer workstations.

I have 64GB of RAM in my M2 MacBook Pro, so I'm looking forward to trying a slightly quantized GGUF of this model to see if I can run it while still leaving some memory free for other applications.

**Update**: Ollama have [a 43GB GGUF](https://ollama.com/library/llama3.3) available now. And here's an [MLX 8bit version](https://huggingface.co/mlx-community/Llama-3.3-70B-Instruct-8bit) and [other MLX quantizations](https://huggingface.co/collections/mlx-community/llama-33-67538fce5763675dcb8c4463).

Llama 3\.3 has 70B parameters, a 128,000 token context length and was trained to support English, German, French, Italian, Portuguese, Hindi, Spanish, and Thai.

The [model card](https://github.com/meta-llama/llama-models/blob/main/models/llama3_3/MODEL_CARD.md) says that the training data was "A new mix of publicly available online data" \- 15 trillion tokens with a December 2023 cut\-off.

They used "39\.3M GPU hours of computation on H100\-80GB (TDP of 700W) type hardware" which they calculate as 11,390 tons CO2eq. I believe that's equivalent to around 20 fully loaded passenger flights from New York to London (at [\~550 tons per flight](https://travelnav.com/emissions-from-jfk-to-lhr)).

---

**Quote** 2024\-12\-07

> *A test of how seriously your firm is taking AI: when o\-1 (\& the new Gemini) came out this week, were there assigned folks who immediately ran the model through internal, validated, firm\-specific benchmarks to see how useful it as? Did you update any plans or goals as a result?   
>   
> Or do you not have people (including non\-technical people) assigned to test the new models? No internal benchmarks? No perspective on how AI will impact your business that you keep up\-to\-date?   
>   
> No one is going to be doing this for organizations, you need to do it yourself.*

[Ethan Mollick](https://bsky.app/profile/emollick.bsky.social/post/3lcq4udvdwk23)

---

**Link** 2024\-12\-07 [Writing down (and searching through) every UUID](https://eieio.games/blog/writing-down-every-uuid/):

Nolen Royalty built [everyuuid.com](https://everyuuid.com/), and this write\-up of how he built it is utterly delightful.

First challenge: infinite scroll.

> Browsers do not want to render a window that is over a trillion trillion pixels high, so I needed to handle scrolling and rendering on my own.

That means implementing hot keys and mouse wheel support and custom scroll bars with animation... mostly implemented with the help of Claude.

The really fun stuff is how Nolen implemented [custom ordering](https://eieio.games/blog/writing-down-every-uuid/#toc:challenge-2-ordering) \- because "Scrolling through a list of UUIDs should be exciting!", but "it’d be disappointing if you scrolled through every UUID and realized that you hadn’t seen one. And it’d be very hard to show someone a UUID that you found if you couldn’t scroll back to the same spot to find it."

And if that wasn't enough... [full text search](https://eieio.games/blog/writing-down-every-uuid/#toc:full-text-search)! How can you efficiently search (or at least pseudo\-search) for text across 5\.3 septillion values? The trick there turned out to be generating a bunch of valid UUIDv4s containing the requested string and then picking the one closest to the current position on the page.

---

**TIL** 2024\-12\-08 [Publishing a simple client\-side JavaScript package to npm with GitHub Actions](https://til.simonwillison.net/npm/npm-publish-github-actions):

Here's what I learned about publishing a single file JavaScript package to NPM for my [Prompts.js](https://simonwillison.net/2024/Dec/7/prompts-js/) project. …

---

**Link** 2024\-12\-08 [Holotypic Occlupanid Research Group](https://www.horg.com/horg/):

I just learned about this delightful piece of internet culture [via Leven Parker on TikTok](https://www.tiktok.com/@leven_parker/video/7445432301816679711).

Occlupanids are the small plastic square clips used to seal plastic bags containing bread.

For thirty years (since 1994\) John Daniel has maintained this website that catalogs them and serves as the basis of a wide ranging community of occlupanologists who study and collect these plastic bread clips.

There's an active subreddit, [r/occlupanids](https://reddit.com/r/occlupanids), but the real treat is the meticulously crafted taxonomy with dozens of species split across 19 families, all in the [class Occlupanida](https://www.horg.com/horg/?page_id=3281):

> Class **Occlupanida** (Occlu\=to close, pan\= bread) are placed under the Kingdom Microsynthera, of the Phylum Plasticae. Occlupanids share phylum Plasticae with “45” record holders, plastic juice caps, and other often ignored small plastic objects.

If you want to classify your own occlupanid there's even a [handy ID guide](https://www.horg.com/horg/?page_id=3281), which starts with the shape of the "oral groove" in the clip.

Or if you want to dive *deep* down a rabbit hole, [this YouTube video](https://www.youtube.com/watch?v=Ls3VkE2B8zM) by CHUPPL starts with Occlupanids and then explores their inventor [Floyd Paxton's](https://en.wikipedia.org/wiki/Floyd_Paxton) involvement with the John Birch Society and eventually [Yamashita's gold](https://en.wikipedia.org/wiki/Yamashita%27s_gold).

---

**Link** 2024\-12\-08 [llm\-openrouter 0\.3](https://github.com/simonw/llm-openrouter/releases/tag/0.3):

New release of my [llm\-openrouter](https://github.com/simonw/llm-openrouter) plugin, which allows [LLM](https://llm.datasette.io/) to access models hosted by [OpenRouter](https://openrouter.ai/).

Quoting the release notes:

> * Enable image attachments for models that support images. Thanks, [Adam Montgomery](https://github.com/montasaurus). [\#12](https://github.com/simonw/llm-openrouter/issues/12)
> * Provide async model access. [\#15](https://github.com/simonw/llm-openrouter/issues/15)
> * Fix documentation to list correct `LLM_OPENROUTER_KEY` environment variable. [\#10](https://github.com/simonw/llm-openrouter/issues/10)

---