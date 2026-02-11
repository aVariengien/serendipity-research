# QvQ - Qwen's new visual reasoning model

*Plus DeepSeek v3, an open weights model that rivals Claude 3.5 Sonnet*

Published: 2024-12-28
Source: https://simonw.substack.com/p/qvq-qwens-new-visual-reasoning-model

---

In this newsletter:

* Trying out QvQ \- Qwen's new visual reasoning model

Plus 7 links and 5 quotations and 2 TILs

### **[Trying out QvQ \- Qwen's new visual reasoning model](https://simonwillison.net/2024/Dec/24/qvq/) \- 2024\-12\-24**

I thought we were done for major model releases in 2024, but apparently not: Alibaba's Qwen team just dropped the ~~Apache 2\.0 licensed~~ Qwen licensed ([the license changed](https://simonwillison.net/2024/Dec/24/qvq/#the-license-changed)) QvQ\-72B\-Preview, "an experimental research model focusing on enhancing visual reasoning capabilities".

Their blog post is titled [QvQ: To See the World with Wisdom](https://qwenlm.github.io/blog/qvq-72b-preview/) \- similar flowery language to their QwQ announcement [QwQ: Reflect Deeply on the Boundaries of the Unknown](https://qwenlm.github.io/blog/qwq-32b-preview/) a few weeks ago in November.

It's a vision\-focused follow\-up to QwQ, which I [wrote about previousy](https://simonwillison.net/2024/Nov/27/qwq/). QwQ is an impressive openly licensed inference\-scaling model: give it a prompt and it will think out loud over many tokens while trying to derive a good answer, similar to OpenAI's o1 and o3 models.

The new QvQ adds vision to the mix. You can try it out [on Hugging Face Spaces](https://huggingface.co/spaces/Qwen/QVQ-72B-preview) \- it accepts an image and a single prompt and then streams out a *very* long response where it thinks through the problem you have posed it. There's no option to send a follow\-up prompt.

I've tried it out with a bunch of things, with mixed results \- but it's really fun seeing how it works through a problem.

My most successful prompt was "Count the pelicans" with this image:

[![A photograph of four glorious young California Brown Pelicans perched on a dock. The back end of another pelican is visible at the front of the photo.](https://substackcdn.com/image/fetch/$s_!CdYR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd920c1d9-c13e-4d89-81dd-12d3052158e3_1086x724.jpeg "A photograph of four glorious young California Brown Pelicans perched on a dock. The back end of another pelican is visible at the front of the photo.")](https://substackcdn.com/image/fetch/$s_!CdYR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd920c1d9-c13e-4d89-81dd-12d3052158e3_1086x724.jpeg)

Here's [the full response](https://gist.github.com/simonw/6c296f4b9323736dc77978447b6368fc#response). Some highlights:

> So I've got this picture of some pelicans, and I need to count them. Let me see... First off, I know that pelicans are those big birds with the massive beaks, right? \[...]
> 
> Let me try counting again, more carefully this time. Starting from the left:
> 
> 1. The first pelican is fully visible, standing at the front.
> 2. Behind it, slightly to the right, is the second pelican.
> 3. Then, further back, there's a third pelican.
> 4. And next to that one, there's a fourth pelican.
> 
> So, that's four pelicans in total. But, I notice that on the far right of the image, there's part of another bird, maybe a pelican's back or tail feathers, but it's not fully in the frame, so I don't think I should count it as a whole pelican.

Something about the tone of voice it uses, "First off, I know that pelicans are those big birds with the massive beaks, right?", tickles me.

I also tried this on a [much harder image](https://gist.github.com/simonw/6c296f4b9323736dc77978447b6368fc#image-2) \- it counted 17 which looks about right to me but honestly I have trouble with that image myself.

I fed in [one of the ARC\-AGI puzzles](https://gist.github.com/simonw/6c296f4b9323736dc77978447b6368fc#arc-agi-puzzle-0d87d2a6) that o3 had failed at.

[![A puzzle with colored squares, where drawing a line between the single blue squares and turning any intersected rectangles blue is clearly the solution.](https://substackcdn.com/image/fetch/$s_!lBk-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5e4c9830-180a-4711-b48f-f22895e0787a_1600x891.png "A puzzle with colored squares, where drawing a line between the single blue squares and turning any intersected rectangles blue is clearly the solution.")](https://substackcdn.com/image/fetch/$s_!lBk-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5e4c9830-180a-4711-b48f-f22895e0787a_1600x891.png)

It produced [a very lengthy chain of thought](https://gist.github.com/simonw/6c296f4b9323736dc77978447b6368fc#response-1) that was almost entirely incorrect, but had some interesting "ideas" in it:

> \[...] Let me try to think in terms of cellular automata rules, like Conway's Game of Life.
> 
> In Game of Life, each cell's state in the next generation is determined by its current state and the states of its eight neighbors.
> 
> Perhaps a similar rule applies here.

Finally, I asked it to "Estimate the height of the dinosaur" against this image (which, as it correctly noted, is actually an inflatable dragon):

[![A large inflatable Christmas decoration of a reindeer riding a dragon - both reindeer and dragon are wearing Christmas hats](https://substackcdn.com/image/fetch/$s_!3FmV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6c343e93-5c68-43d7-ba8d-683ea78da1a2_768x1024.jpeg "A large inflatable Christmas decoration of a reindeer riding a dragon - both reindeer and dragon are wearing Christmas hats")](https://substackcdn.com/image/fetch/$s_!3FmV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6c343e93-5c68-43d7-ba8d-683ea78da1a2_768x1024.jpeg)

I'm not sure this task is even possible given the lack of items in the frame of comparable known height. It [had a good go at it](https://gist.github.com/simonw/6c296f4b9323736dc77978447b6368fc#response-3) though! I particularly enjoyed how it began:

> So I've got this inflatable Christmas decoration, and it's a dragon! But not just any dragon—it's a green dragon wearing a Santa hat and a red and white scarf. And get this, there's a reindeer on its back, also wearing a Santa hat and holding onto the dragon's wings. It's pretty festive and colorful, with lots of vibrant greens, reds, and yellows.
> 
> The dragon has these big, friendly eyes and a smiling face, which makes it look really cheerful. Its wings are spread out, and it has white claws on its feet. The reindeer is brown with antlers and seems to be enjoying the ride on the dragon's back.
> 
> Now, the question is, how tall is this inflatable dragon? I need to estimate its height. Let me see. I'm standing next to it, and I'm about 5 feet 10 inches tall. The dragon is definitely taller than me. Maybe around 8 or 9 feet high? But I should try to be more precise.

I wonder how it decided that its own height was 5 feet 10 inches!

#### **Running QvQ locally**

All of my experiments so far have used the [hosted Hugging Face demo](https://huggingface.co/spaces/Qwen/QVQ-72B-preview). I'm hoping to try it out on my own laptop soon \- I think it should just fit in 64GB of M2, maybe with a smaller quantization.

Right now the options are:

* [Qwen/QVQ\-72B\-Preview](https://huggingface.co/Qwen/QVQ-72B-Preview) on Hugging Face has the GPU model weights, for use with Hugging Face Transformers and the [qwen\-vl\-utils](https://pypi.org/project/qwen-vl-utils/)Python package.
* Prince Canuma [converted the model for Apple's MLX framework](https://twitter.com/Prince_Canuma/status/1871687356815716672) as [mlx\-community/qvq\-72b\-preview](https://huggingface.co/collections/mlx-community/qvq-72b-preview-676b345a6f93172ba980c0d5) and got it working with his excellent [mlx\-vlm](https://github.com/Blaizzy/mlx-vlm) package.

As a happy user of Ollama's [qwq port](https://ollama.com/library/qwq) I'm hoping they add a QvQ release at some point soon as well.

#### **Running QvQ on my Mac using mlx\-vlm**

**Update**: I successfully ran QvQ on my 64GB M2 MacBook Pro using Prince Canuma's `mlx-vlm` via `uv run` with the following command:

```
uv run --with 'numpy<2.0' --with mlx-vlm python \
  -m mlx_vlm.generate \
    --model mlx-community/QVQ-72B-Preview-4bit \
    --max-tokens 10000 \
    --temp 0.0 \
    --prompt "describe this" \
    --image pelicans-on-bicycles-veo2.jpg
```

My image input here was taken from my experiment with Google's [Veo 2](https://simonwillison.net/2024/Dec/16/veo-2/) video generation model:

[![A screenshot of the Google VideoFX video generation tool](https://substackcdn.com/image/fetch/$s_!essO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F213ac6c2-0044-44f9-9b3a-89f564ee41aa_1920x908.jpeg "A screenshot of the Google VideoFX video generation tool")](https://substackcdn.com/image/fetch/$s_!essO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F213ac6c2-0044-44f9-9b3a-89f564ee41aa_1920x908.jpeg)

Here's the full output from running that command, after it first downloaded 38GB to `~/.cache/huggingface/hub/models--mlx-community--QVQ-72B-Preview-4bi`:

```
==========
Image: ['pelicans-on-bicycles-veo2.jpg'] 

Prompt: <|im_start|>system
You are a helpful and harmless assistant. You are Qwen developed by Alibaba. You should think step-by-step.<|im_end|>
<|im_start|>user
describe this<|vision_start|><|image_pad|><|vision_end|><|im_end|>
<|im_start|>assistant

Alright, I've got this "Text to Video" tool to explore. It seems pretty advanced, allowing me to turn text descriptions into actual videos. The interface looks user-friendly, with a dark theme that's easy on the eyes. On the left side, there's a panel where I can input my text prompt. It already has an example filled in: "A pelican riding a bicycle along a coastal path overlooking a harbor."

That sounds interesting! I can see four different video thumbnails on the right side, each showing variations of this scene. One of them even has the pelican wearing a helmet, which adds a humorous touch. Another shows the pelican standing next to a bicycle, almost as if it's ready to hop on and start pedaling.

Below the text input, there are some style options like "photorealistic," "35mm film," "minimal," "sketchy," "handmade," and "abstract." These probably let me choose the visual style of the video. For now, I'll stick with the default settings.

At the bottom of the left panel, there are two buttons: "Start over" and "Create videos." I guess "Create videos" is the one I need to press to generate the videos based on my text prompt.

Let me think about this. I want to see what kind of videos this tool can produce based on my description. The example prompt is already filled in, so maybe I should just go ahead and click "Create videos" to see what happens.

Wait a minute, the prompt mentions a coastal path overlooking a harbor. In the thumbnails, I can see a background with water and boats, which matches the description. It's cool how the tool has interpreted the text into visual elements.

I should also pay attention to the "Visual Prompt" section, which says "View only." That probably means I can't edit it directly, but I can view the generated videos based on this prompt.

Hmm, maybe I should try changing the prompt to see different results. For example, instead of a pelican riding a bicycle, maybe I could describe a different scene. But for now, I'll stick with the given example to understand how it works.

After clicking "Create videos," I expect to see the videos being generated. There might be a loading process, depending on the complexity of the prompt and the tool's processing speed.

Once the videos are ready, I can preview them to see how well they match my description. If I'm not satisfied, I can always go back and adjust the prompt or try different style options.

Overall, this seems like a powerful tool for creating custom videos based on textual descriptions. It could be really useful for storytelling, presentations, or even just for fun, experimenting with different scenes and styles.

I think I'll spend some time exploring the different style options to see how they affect the final videos. For instance, selecting "35mm film" might give the videos a vintage, cinematic look, while "abstract" could produce more artistic and less realistic visuals.

Also, I wonder if there's a way to customize more specific aspects, like the camera angle, lighting, or movement. Maybe after generating the initial videos, there are additional editing options available.

In summary, I'm excited to use this Text to Video tool and see what kind of creative possibilities it opens up. With a bit of practice, I could probably create some impressive visual content just by describing what I want to see.

**Final Answer**

To proceed with generating videos based on the provided text prompt, I need to click on the "Create videos" button. This action will initiate the process of converting the textual description into visual content, resulting in multiple video thumbnails that can be previewed for further use or adjustments.
==========
Prompt: 0.870 tokens-per-sec
Generation: 7.694 tokens-per-sec

```

#### **The license changed from Apache 2\.0 to Qwen**

When I wrote this post yesterday the LICENSE file in the Hugging Face repository was Apache 2\.0\. Just after midnight UTC on 25th December [this commit](https://huggingface.co/Qwen/QVQ-72B-Preview/commit/53b19b90d67220c896e868a809ef1b93d0c8dab8) landed updating the `QVQ-72B-Preview`license file to the [Qwen license](https://huggingface.co/Qwen/QVQ-72B-Preview/blob/main/LICENSE) instead.

This looks to me like they were correcting a mistake, not changing their policy. The [README.md](https://huggingface.co/Qwen/QVQ-72B-Preview/blob/main/README.md) for that repository has this block of YAML:

```
license: other
license_name: qwen
```

And [commits to that README](https://huggingface.co/Qwen/QVQ-72B-Preview/commits/main/README.md) at one point linked to the [Qwen2\.5\-72B\-Instruct copy of the Qwen license](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct/blob/main/LICENSE).

The QwQ model repository [continues to list Apache 2\.0](https://huggingface.co/Qwen/QwQ-32B-Preview/blob/main/LICENSE), which matches the YAML in [its README](https://huggingface.co/Qwen/QwQ-32B-Preview/blob/main/README.md) as well.

So it looks to me like the intention is for QvQ and Qwen2\.5\-72B\-Instruct to be Qwen licensed, while QwQ is Apache 2\.0\.

---

**Link** 2024\-12\-22 [What happened to the world's largest tube TV?](https://www.youtube.com/watch?v=JfZxOuc9Qwk):

This YouTube video is an absolute delight.

Shank Mods describes the legendary [Sony PVM\-4300](https://consolemods.org/wiki/CRT:PVM-4300) \- the largest CRT television ever made, released by Sony in 1989 and weighing over 400lb. CRT enthusiasts had long debated its very existence, given the lack of known specimens outside of Sony's old marketing materials. Then Shank tracked a working one down... on the second floor of a 300 year old Soba noodle restaurant in Osaka, Japan.

This story of how they raced to rescue the TV before the restaurant was demolished, given the immense difficulty of moving a 400lb television (and then shipping it to the USA), is a fantastic ride.

---

**Link** 2024\-12\-22 [openai/openai\-openapi](https://github.com/openai/openai-openapi):

Seeing as the LLM world has semi\-standardized on imitating OpenAI's API format for a whole host of different tools, it's useful to note that OpenAI themselves maintain a dedicated repository for a [OpenAPI](https://www.openapis.org/) YAML representation of their current API.

(I get OpenAI and OpenAPI typo\-confused all the time, so `openai-openapi` is a delightfully fiddly repository name.)

The [openapi.yaml](https://github.com/openai/openai-openapi/blob/master/openapi.yaml) file itself is over 26,000 lines long, defining 76 API endpoints ("paths" in OpenAPI terminology) and 284 "schemas" for JSON that can be sent to and from those endpoints. A much more interesting view onto it is the [commit history](https://github.com/openai/openai-openapi/commits/master/openapi.yaml) for that file, showing details of when each different API feature was released.

Browsing 26,000 lines of YAML isn't pleasant, so I [got Claude](https://gist.github.com/simonw/54b4e533481cc7a686b0172c3a9ac21e) to build me a rudimentary YAML expand/hide exploration tool. Here's that tool running against the OpenAI schema, loaded directly from GitHub via a CORS\-enabled `fetch()`call: [https://tools.simonwillison.net/yaml\-explorer\#.eyJ1c...](https://tools.simonwillison.net/yaml-explorer#eyJ1cmwiOiJodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vb3BlbmFpL29wZW5haS1vcGVuYXBpL3JlZnMvaGVhZHMvbWFzdGVyL29wZW5hcGkueWFtbCIsIm9wZW4iOlsiZDAiLCJkMjAiXX0=) \- the code after that fragment is a base64\-encoded JSON for the current state of the tool (mostly Claude's idea).

[![Screenshot of the YAML explorer, showing a partially expanded set of sections from the OpenAI API specification.](https://substackcdn.com/image/fetch/$s_!cigX!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1306354c-8cb2-4058-b3cc-1ee41349895e_1726x1742.jpeg "Screenshot of the YAML explorer, showing a partially expanded set of sections from the OpenAI API specification.")](https://substackcdn.com/image/fetch/$s_!cigX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1306354c-8cb2-4058-b3cc-1ee41349895e_1726x1742.jpeg)

The tool is a little buggy \- the expand\-all option doesn't work quite how I want \- but it's useful enough for the moment.

**Update**: It turns out the [petstore.swagger.io](https://petstore.swagger.io/) demo has an (as far as I can tell) undocumented `?url=`parameter which can load external YAML files, so [here's openai\-openapi/openapi.yaml](https://petstore.swagger.io/?url=https://raw.githubusercontent.com/openai/openai-openapi/refs/heads/master/openapi.yaml) in an OpenAPI explorer interface.

[![The Swagger API browser showing the OpenAI API](https://substackcdn.com/image/fetch/$s_!mPbK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff42ddcc0-a972-4355-b10b-c2c09fd9f188_1492x1452.jpeg "The Swagger API browser showing the OpenAI API")](https://substackcdn.com/image/fetch/$s_!mPbK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff42ddcc0-a972-4355-b10b-c2c09fd9f188_1492x1452.jpeg)

---

**Quote** 2024\-12\-23

> *Whether you’re an AI\-programming skeptic or an enthusiast, the reality is that many programming tasks are beyond the reach of today’s models. But many decent dev tools are actually quite easy for AI to build, and can help the rest of the programming go smoother. In general, these days any time I’m spending more than a minute staring at a JSON blob, I consider whether it’s worth building a custom UI for it.*

[Geoffrey Litt](https://www.geoffreylitt.com/2024/12/22/making-programming-more-fun-with-an-ai-generated-debugger.html)

---

**Quote** 2024\-12\-23

> *There’s been a lot of strange reporting recently about how ‘scaling is hitting a wall’ – in a very narrow sense this is true in that larger models were getting less score improvement on challenging benchmarks than their predecessors, but in a larger sense this is false – techniques like those which power O3 means scaling is continuing (and if anything the curve has steepened), you just now need to account for scaling both within the training of the model and in the compute you spend on it once trained.*

[Jack Clark](https://jack-clark.net/2024/12/23/import-ai-395-ai-and-energy-demand-distributed-training-via-demo-and-phi-4/)

---

**TIL** 2024\-12\-24 [Named Entity Resolution with dslim/distilbert\-NER](https://til.simonwillison.net/llms/bert-ner):

I was exploring the original BERT model from 2018, which is mainly useful if you fine\-tune a model on top of it for a specific task. …

---

**Link** 2024\-12\-24 [Finally, a replacement for BERT: Introducing ModernBERT](https://www.answer.ai/posts/2024-12-19-modernbert.html):

[BERT](https://en.wikipedia.org/wiki/BERT_(language_model)) was an early language model released by Google in October 2018\. Unlike modern LLMs it wasn't designed for generating text. BERT was trained for masked token prediction and was generally applied to problems like Named Entity Recognition or Sentiment Analysis. BERT also wasn't very useful on its own \- most applications required you to fine\-tune a model on top of it.

In exploring BERT I decided to try out [dslim/distilbert\-NER](https://huggingface.co/dslim/distilbert-NER), a popular Named Entity Recognition model fine\-tuned on top of DistilBERT (a smaller distilled version of the original BERT model). [Here are my notes](https://til.simonwillison.net/llms/bert-ner) on running that using `uv run`.

Jeremy Howard's [Answer.AI](https://www.answer.ai/) research group, [LightOn](https://www.lighton.ai/) and friends supported the development of ModernBERT, a brand new BERT\-style model that applies many enhancements from the past six years of advances in this space.

While BERT was trained on 3\.3 billion tokens, producing 110 million and 340 million parameter models, ModernBERT trained on 2 trillion tokens, resulting in 140 million and 395 million parameter models. The parameter count hasn't increased much because it's designed to run on lower\-end hardware. It has a 8192 token context length, a significant improvement on BERT's 512\.

I was able to run one of the demos from the announcement post using `uv run` like this (I'm not sure why I had to use `numpy<2.0` but without that I got an error about `cannot import name 'ComplexWarning' from 'numpy.core.numeric'`):

```
uv run --with 'numpy<2.0' --with torch --with 'git+<https://github.com/huggingface/transformers.git>' python
```

Then this Python:

```
import torch
from transformers import pipeline
from pprint import pprint
pipe = pipeline(
    "fill-mask",
    model="answerdotai/ModernBERT-base",
    torch_dtype=torch.bfloat16,
)
input_text = "He walked to the [MASK]."
results = pipe(input_text)
pprint(results)
```

Which downloaded 573MB to `~/.cache/huggingface/hub/models--answerdotai--ModernBERT-base` and output:

```
[{'score': 0.11669921875,
  'sequence': 'He walked to the door.',
  'token': 3369,
  'token_str': ' door'},
 {'score': 0.037841796875,
  'sequence': 'He walked to the office.',
  'token': 3906,
  'token_str': ' office'},
 {'score': 0.0277099609375,
  'sequence': 'He walked to the library.',
  'token': 6335,
  'token_str': ' library'},
 {'score': 0.0216064453125,
  'sequence': 'He walked to the gate.',
  'token': 7394,
  'token_str': ' gate'},
 {'score': 0.020263671875,
  'sequence': 'He walked to the window.',
  'token': 3497,
  'token_str': ' window'}]
```

I'm looking forward to trying out models that use ModernBERT as their base. The model release is accompanied by a paper ([Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference](https://arxiv.org/abs/2412.13663)) and [new documentation](https://huggingface.co/docs/transformers/main/en/model_doc/modernbert) for using it with the Transformers library.

---

**Quote** 2024\-12\-24

> *\[On Reddit] we had to look up every single comment on the page to see if you had voted on it \[...]  
>   
> But with a bloom filter, we could very quickly look up all the comments and get back a list of all the ones you voted on (with a couple of false positives in there). Then we could go to the cache and see if your actual vote was there (and if it was an upvote or a downvote). It was only after a failed cache hit did we have to actually go to the database.  
>   
> But that bloom filter saved us from doing sometimes 1000s of cache lookups.*

[Jeremy Edberg](https://news.ycombinator.com/item?id=42486610#42492484)

---

**Quote** 2024\-12\-24

> *it's really hard not to be obsessed with these tools. It's like having a bespoke, free, (usually) accurate curiosity\-satisfier in your pocket, no matter where you go \- if you know how to ask questions, then suddenly the world is an audiobook*

[Paige Bailey](https://twitter.com/dynamicwebpaige/status/1871606733170442615)

---

**TIL** 2024\-12\-25 [Calculating the size of all LFS files in a repo](https://til.simonwillison.net/git/size-of-lfs-files):

I wanted to know how large the [deepseek\-ai/DeepSeek\-V3\-Base](https://huggingface.co/deepseek-ai/DeepSeek-V3-Base) repo on Hugging Face was without actually downloading all of the files. …

---

**Link** 2024\-12\-25 [deepseek\-ai/DeepSeek\-V3\-Base](https://huggingface.co/deepseek-ai/DeepSeek-V3-Base):

No model card or announcement yet, but this new model release from Chinese AI lab DeepSeek (an arm of Chinese hedge fund [High\-Flyer](https://en.wikipedia.org/wiki/High-Flyer_(company))) looks very significant.

It's a huge model \- 685B parameters, 687\.9 GB on disk ([TIL how to size a git\-lfs repo](https://til.simonwillison.net/git/size-of-lfs-files)). The architecture is [a Mixture of Experts](https://twitter.com/dysondunbar/status/1871955700949430299) with 256 experts, using 8 per token.

For comparison, Meta AI's largest released model is their [Llama 3\.1 model](https://ai.meta.com/blog/meta-llama-3-1/) with 405B parameters.

The new model is apparently available to some people via both [chat.deepseek.com](https://chat.deepseek.com/) and the DeepSeek API as part of a staged rollout.

Paul Gauthier got API access and [used it](https://twitter.com/paulgauthier/status/1871919612000092632) to update his new [Aider Polyglot leaderboard](https://aider.chat/docs/leaderboards/) \- DeepSeek v3 preview scored 48\.4%, putting it in second place behind `o1-2024-12-17 (high)` and in front of both `claude-3-5-sonnet-20241022` and `gemini-exp-1206`!

[![Aider leaderboard chart showing DeepSeek Chat V3 preview in second place](https://substackcdn.com/image/fetch/$s_!ITHM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff4dbcca7-ea1d-4134-8061-55b1aae00364_1654x916.jpeg "Aider leaderboard chart showing DeepSeek Chat V3 preview in second place")](https://substackcdn.com/image/fetch/$s_!ITHM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff4dbcca7-ea1d-4134-8061-55b1aae00364_1654x916.jpeg)

I never know if I can believe models or not (the first time I asked "what model are you?" it claimed to be "based on OpenAI's GPT\-4 architecture"), but I just got this result using [LLM](https://llm.datasette.io/)and the [llm\-deepseek](https://pypi.org/project/llm-deepseek/) plugin:

```
llm -m deepseek-chat 'what deepseek model are you?'      
```

> I'm DeepSeek\-V3 created exclusively by DeepSeek. I'm an AI assistant, and I'm at your service! Feel free to ask me anything you'd like. I'll do my best to assist you.

Here's my [initial experiment log](https://gist.github.com/simonw/e7528dc52828fb31415f6e14e3527b93).

---

**Link** 2024\-12\-26 [Cognitive load is what matters](https://minds.md/zakirullin/cognitive):

Excellent living document (the underlying repo has [625 commits](https://github.com/zakirullin/cognitive-load/commits/main/) since being created in May 2023\) maintained by Artem Zakirullin about minimizing the cognitive load needed to understand and maintain software.

This all rings very true to me. I judge the quality of a piece of code by how easy it is to change, and anything that causes me to take on more cognitive load \- unraveling a class hierarchy, reading though dozens of tiny methods \- reduces the quality of the code by that metric.

Lots of accumulated snippets of wisdom in this one.

> Mantras like "methods should be shorter than 15 lines of code" or "classes should be small" turned out to be somewhat wrong.

---

**Quote** 2024\-12\-26

> *Providers and deployers of AI systems shall take measures to ensure, to their best extent, a sufficient level of AI literacy of their staff and other persons dealing with the operation and use of AI systems on their behalf, taking into account their technical knowledge, experience, education and training and the context the AI systems are to be used in, and considering the persons or groups of persons on whom the AI systems are to be used.*

[EU Artificial Intelligence Act](https://artificialintelligenceact.eu/article/4/)

---

**Link** 2024\-12\-26 [DeepSeek\_V3\.pdf](https://github.com/deepseek-ai/DeepSeek-V3/blob/main/DeepSeek_V3.pdf):

The DeepSeek v3 paper (and [model card](https://github.com/deepseek-ai/DeepSeek-V3/blob/main/README.md)) are out, after yesterday's mysterious release of [the undocumented model weights](https://simonwillison.net/2024/Dec/25/deepseek-v3/).

Plenty of interesting details in here. The model pre\-trained on 14\.8 trillion "high\-quality and diverse tokens" (not otherwise documented).

> Following this, we conduct post\-training, including Supervised Fine\-Tuning (SFT) and Reinforcement Learning (RL) on the base model of DeepSeek\-V3, to align it with human preferences and further unlock its potential. During the post\-training stage, we distill the reasoning capability from the DeepSeek\-R1 series of models, and meanwhile carefully maintain the balance between model accuracy and generation length.

By far the most interesting detail though is how much the training cost. DeepSeek v3 trained on 2,788,000 H800 GPU hours at an estimated cost of $5,576,000\. For comparison, Meta AI's Llama 3\.1 405B (smaller than DeepSeek v3's 685B parameters) [trained on 11x that](https://huggingface.co/meta-llama/Llama-3.1-405B-Instruct#hardware-and-software) \- 30,840,000 GPU hours, also on 15 trillion tokens.

DeepSeek v3 benchmarks comparably to Claude 3\.5 Sonnet, indicating that it's now possible to train a frontier\-class model (at least for the 2024 version of the frontier) for less than $6 million!

[Andrej Karpathy](https://twitter.com/karpathy/status/1872362712958906460):

> For reference, this level of capability is supposed to require clusters of closer to 16K GPUs, the ones being brought up today are more around 100K GPUs. E.g. Llama 3 405B used 30\.8M GPU\-hours, while DeepSeek\-V3 looks to be a stronger model at only 2\.8M GPU\-hours (\~11X less compute). If the model also passes vibe checks (e.g. LLM arena rankings are ongoing, my few quick tests went well so far) it will be a highly impressive display of research and engineering under resource constraints.

DeepSeek also [announced their API pricing](https://twitter.com/deepseek_ai/status/1872242663489188088). From February 8th onwards:

> Input: $0\.27/million tokens ($0\.07/million tokens with cache hits)  
> Output: $1\.10/million tokens

Claude 3\.5 Sonnet is currently $3/million for input and $15/million for output, so if the models are indeed of equivalent quality this is a dramatic new twist in the ongoing LLM pricing wars.

---

**Link** 2024\-12\-27 [Open WebUI](https://github.com/open-webui/open-webui):

I tried out this open source (MIT licensed, JavaScript and Python) localhost UI for accessing LLMs today for the first time. It's very nicely done.

I ran it with [uvx](https://docs.astral.sh/uv/guides/tools/) like this:

```
uvx --python 3.11 open-webui serve

```

On first launch it installed a bunch of dependencies and then downloaded 903MB to `~/.cache/huggingface/hub/models--sentence-transformers--all-MiniLM-L6-v2` \- a copy of the [all\-MiniLM\-L6\-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) embedding model, presumably for its [RAG feature](https://docs.openwebui.com/features/rag).

It then presented me with a working Llama 3\.2:3b chat interface, which surprised me because I hadn't spotted it downloading that model. It turns out that was because I have [Ollama](https://ollama.com/) running on my laptop already (with several models, including Llama 3\.2:3b, already installed) \- and Open WebUI automatically detected Ollama and gave me access to a list of available models.

I found a "knowledge" section and added all of the Datasette documentation (by dropping in the `.rst` files from the docs) \- and now I can type `#` in chat to search for a file, add that to the context and then ask questions about it directly.

I selected the `spatialite.rst.txt` file, prompted it with "How do I use SpatiaLite with Datasette" and got back [this](https://gist.github.com/simonw/3bf5ff0ed3b47aefbb94d3fd992f81f9#response):

[![Chat UI. Prompt is How do I use SpatiaLite with Datasette? with an attached spatialite.rst.txt file. The response from llama3.2:3b reads: To use SpatiaLite with Datasette, you need to install the mod_spatialite dynamic library. This can then be loaded into Datasette using the --load-extension command-line option.   You can install it on OS X by running brew update and then brew install spatialite-tools. On Linux, SpatiaLite is packaged for most distributions, so you can typically install it with a package manager like apt.   When running Datasette, you can look for SpatiaLite in common installation locations or specify the full path to the extension if it's installed elsewhere.   For example, on OS X, you might run datasette --load-extension=spatialite after installing it with Homebrew. On Linux, you could use datasette --load-extension=/usr/lib/x86_64-linux-gnu/mod_spatialite.so.   It's also important to note that SpatiaLite adds a large number of additional SQL functions, some of which are not safe for untrusted users to execute. To secure your Datasette instance, consider disabling arbitrary SQL queries and defining canned queries with the SQL queries that use SpatiaLite functions you want people to be able to execute.](https://substackcdn.com/image/fetch/$s_!Qlet!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6dbb7b3c-a82a-4e8c-96e5-772d31e783e0_1802x1818.jpeg "Chat UI. Prompt is How do I use SpatiaLite with Datasette? with an attached spatialite.rst.txt file. The response from llama3.2:3b reads: To use SpatiaLite with Datasette, you need to install the mod_spatialite dynamic library. This can then be loaded into Datasette using the --load-extension command-line option.   You can install it on OS X by running brew update and then brew install spatialite-tools. On Linux, SpatiaLite is packaged for most distributions, so you can typically install it with a package manager like apt.   When running Datasette, you can look for SpatiaLite in common installation locations or specify the full path to the extension if it's installed elsewhere.   For example, on OS X, you might run datasette --load-extension=spatialite after installing it with Homebrew. On Linux, you could use datasette --load-extension=/usr/lib/x86_64-linux-gnu/mod_spatialite.so.   It's also important to note that SpatiaLite adds a large number of additional SQL functions, some of which are not safe for untrusted users to execute. To secure your Datasette instance, consider disabling arbitrary SQL queries and defining canned queries with the SQL queries that use SpatiaLite functions you want people to be able to execute.")](https://substackcdn.com/image/fetch/$s_!Qlet!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6dbb7b3c-a82a-4e8c-96e5-772d31e783e0_1802x1818.jpeg)

That's honestly a very solid answer, especially considering the Llama 3\.2 3B model from Ollama is just a 1\.9GB file! It's impressive how well that model can handle basic Q\&A and summarization against text provided to it \- it somehow has a 128,000 token context size.

Open WebUI has a lot of other tricks up its sleeve: it can talk to API models such as OpenAI directly, has optional integrations with web search and custom tools and logs every interaction to a SQLite database. It also comes with [extensive documentation](https://docs.openwebui.com/).

---