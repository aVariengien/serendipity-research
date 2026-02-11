# Anthropic's new Citations API

*Plus OpenAI Operator, LLM 0.20 and six short video demos of LLM and Datasette projects*

Published: 2025-01-24
Source: https://simonw.substack.com/p/anthropics-new-citations-api

---

In this newsletter:

* Anthropic's new Citations API
* OpenAI Operator
* Six short video demos of LLM and Datasette projects

Plus 6 links and 4 quotations

### [Anthropic's new Citations API](https://simonwillison.net/2025/Jan/24/anthropics-new-citations-api/) \- 2025\-01\-24

Here's a new API\-only feature from Anthropic that requires quite a bit of assembly in order to unlock the value: [Introducing Citations on the Anthropic API](https://www.anthropic.com/news/introducing-citations-api). Let's talk about what this is and why it's interesting.

* [Citations for Retrieval Augmented Generation](https://simonwillison.net/2025/Jan/24/anthropics-new-citations-api/#citations-for-rag)
* [Trying out the new API with uv run](https://simonwillison.net/2025/Jan/24/anthropics-new-citations-api/#trying-out-the-new-api-with-uv-run)
* [Rendering the citations](https://simonwillison.net/2025/Jan/24/anthropics-new-citations-api/#rendering-the-citations)
* [Now I need to design an abstraction layer for LLM](https://simonwillison.net/2025/Jan/24/anthropics-new-citations-api/#now-i-need-to-design-an-abstraction-layer-for-llm)
* [Anthropic's strategy contrasted with OpenAI](https://simonwillison.net/2025/Jan/24/anthropics-new-citations-api/#anthropic-s-strategy-contrasted-with-openai)

#### Citations for Retrieval Augmented Generation

The core of the [Retrieval Augmented Generation](https://simonwillison.net/tags/rag/) (RAG) pattern is to take a user's question, retrieve portions of documents that might be relevant to that question and then answer the question by including those text fragments in the context provided to the LLM.

This usually works well, but there is still a risk that the model may answer based on other information from its training data (sometimes OK) or hallucinate entirely incorrect details (definitely bad).

The *best* way to help mitigate these risks is to support the answer with citations that incorporate direct quotations from the underlying source documents. This even acts as a form of fact\-checking: the user can confirm that the quoted text did indeed come from those documents, helping provide relatively robust protection against hallucinated details resulting in incorrect answers.

Actually building a system that does this can be quite tricky. Matt Yeung described a pattern for this he called [Deterministic Quoting](https://mattyyeung.github.io/deterministic-quoting) last April, where answers are accompanied by direct quotations from the source documents that are guaranteed to be copied across and not lossily transformed by the model.

This is a great idea, but actually building it requires some quite sophisticated prompt engineering and complex implementation code.

Claude's new [Citations API](https://docs.anthropic.com/en/docs/build-with-claude/citations) mechanism handles the difficult parts of this for you. You still need to implement most of RAG \- identifying potentially relevant documents, then feeding that content in as part of the prompt \- but Claude's API will then do the difficult work of extracting relevant citations and including them in the response that it sends back to you.

#### Trying out the new API with uv run

I tried the API out using Anthropic's Python client library, which was [just updated](https://observablehq.com/@simonw/blog-to-newsletter) to support the citations API.

I ran a scratch Python 3\.13 interpreter with that package using [uv run](https://docs.astral.sh/uv/) like this (after first setting the necessary `ANTHROPIC_API_KEY` environment variable using [llm keys get](https://llm.datasette.io/en/stable/help.html#llm-keys-get-help)):

```
export ANTHROPIC_API_KEY="$(llm keys get claude)"
uv run --with anthropic --python 3.13 python
```

Python 3\.13 has [a nicer interactive interpreter](https://docs.python.org/3/whatsnew/3.13.html#a-better-interactive-interpreter) which you can more easily paste code into. Using `uv run` like this gives me an environment with that package pre\-installed without me needing to setup a virtual environment as a separate step.

Then I ran the following code, adapted from [Anthropic's example](https://docs.anthropic.com/en/docs/build-with-claude/citations). The [text.txt Gist](https://gist.github.com/simonw/9fbb3c2e2c40c181727e497e358fd7ce) contains text I copied out from my [Things we learned about LLMs in 2024](https://simonwillison.net/2024/Dec/31/llms-in-2024/) post.

```
import urllib.request
import json

url = 'https://gist.githubusercontent.com/simonw/9fbb3c2e2c40c181727e497e358fd7ce/raw/6ac20704f5a46b567b774b07fd633a74944bab2b/text.txt'
text = urllib.request.urlopen(url).read().decode('utf-8')

import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "document",
                    "source": {
                        "type": "text",
                        "media_type": "text/plain",
                        "data": text,
                    },
                    "title": "My Document",
                    "context": "This is a trustworthy document.",
                    "citations": {"enabled": True}
                },
                {
                    "type": "text",
                    "text": "What were the top trends?"
                }
            ]
        }
    ]
)
print(json.dumps(response.to_dict(), indent=2))
```

The JSON output from that starts like this:

```
{
  "id": "msg_01P3zs4aYz2Baebumm4Fejoi",
  "content": [
    {
      "text": "Based on the document, here are the key trends in AI/LLMs from 2024:\n\n1. Breaking the GPT-4 Barrier:\n",
      "type": "text"
    },
    {
      "citations": [
        {
          "cited_text": "I\u2019m relieved that this has changed completely in the past twelve months. 18 organizations now have models on the Chatbot Arena Leaderboard that rank higher than the original GPT-4 from March 2023 (GPT-4-0314 on the board)\u201470 models in total.\n\n",
          "document_index": 0,
          "document_title": "My Document",
          "end_char_index": 531,
          "start_char_index": 288,
          "type": "char_location"
        }
      ],
      "text": "The GPT-4 barrier was completely broken, with 18 organizations now having models that rank higher than the original GPT-4 from March 2023, with 70 models in total surpassing it.",
      "type": "text"
    },
    {
      "text": "\n\n2. Increased Context Lengths:\n",
      "type": "text"
    },
```

Here's [the full response](https://gist.github.com/simonw/022d082ccfd636256f72150df344335e).

This format is pretty interesting! It's the standard Claude format but those `"content"` blocks now include an optional additional `"citations"` key which contains a list of relevant citation extracts that support the claim in the `"text"` block.

#### Rendering the citations

Eyeballing the JSON output wasn't particularly fun. I wanted a very quick tool to help me see that output in a more visual way.

A trick I've been using a lot recently is that LLMs like Claude are *really* good at writing code to turn arbitrary JSON shapes like this into a more human\-readable format.

I fired up my [Artifacts project](https://simonwillison.net/2024/Dec/19/one-shot-python-tools/#custom-instructions), pasted in the above JSON and prompted it like this:

> Build a tool where I can paste JSON like this into a textarea and the result will be rendered in a neat way \- it should should intersperse text with citations, where each citation has the cited\_text rendered in a blockquote

It helped me [build this tool](https://tools.simonwillison.net/render-claude-citations) ([follow\-up prompt here](https://gist.github.com/simonw/85bd050908486de36b078c8c7d01e903)), which lets you paste in JSON and produces a rendered version of the text:

[![Render Claude Citations tool. Paste a JSON response from Claude below to render it with citations. JSON is shown, then a Render Message button, then an iframe containing the rendered text.](https://substackcdn.com/image/fetch/$s_!Yyry!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1503db11-132a-4d6a-a35c-9cb01c56ce1e_1612x1612.jpeg "Render Claude Citations tool. Paste a JSON response from Claude below to render it with citations. JSON is shown, then a Render Message button, then an iframe containing the rendered text.")](https://substackcdn.com/image/fetch/$s_!Yyry!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1503db11-132a-4d6a-a35c-9cb01c56ce1e_1612x1612.jpeg)

#### Now I need to design an abstraction layer for LLM

I'd like to upgrade my [LLM](https://llm.datasette.io/) tool and [llm\-claude\-3](https://github.com/simonw/llm-claude-3) plugin to include support for this new feature... but doing so is going to be relatively non\-trivial.

The problem is that LLM currently bakes in an assumption that all LLMs respond with a stream of text.

With citations, this is no longer true! Claude is now returning chunks of text that aren't just a plain string \- they are annotated with citations, which need to be stored and processed somehow by the LLM library.

This isn't the only edge\-case of this type. DeepSeek recently released their Reasoner API which has a similar problem: it can return two different types of text, one showing reasoning text and one showing final content. I [described those differences here](https://gist.github.com/simonw/a5ca117dd0325c93a5b1f5a18c4a9e34).

I've opened a design issue to tackle this challenge in the LLM repository: [Design an abstraction for responses that are not just a stream of text](https://github.com/simonw/llm/issues/716).

#### Anthropic's strategy contrasted with OpenAI

Another interesting aspect of this release is how it helps illustrate a strategic difference between Anthropic and OpenAI.

OpenAI are increasingly behaving like a consumer products company. They just made a big splash with their [Operator](https://simonwillison.net/2025/Jan/23/introducing-operator/) browser\-automation agent system \- a much more polished, consumer\-product version of Anthropic's own [Computer Use](https://simonwillison.net/2025/Jan/23/introducing-operator/) demo from a few months ago.

Meanwhile, Anthropic are clearly focused much more on the developer / "enterprise" market. This Citations feature is API\-only and directly addresses a specific need that developers trying to build reliable RAG systems on top of their platform may not even have realized they had.

---

### [Introducing Operator](https://simonwillison.net/2025/Jan/23/introducing-operator/) \- 2025\-01\-23

OpenAI [released](https://openai.com/index/introducing-operator/) their "research preview" today of Operator, a cloud\-based browser automation platform rolling out today to $200/month ChatGPT Pro subscribers.

They're calling this their first "agent". In the Operator announcement video Sam Altman defined that [notoriously vague term](https://simonwillison.net/2024/Dec/31/llms-in-2024/#-agents-still-haven-t-really-happened-yet) like this:

> AI agents are AI systems that can do work for you independently. You give them a task and they go off and do it.
> 
> We think this is going to be a big trend in AI and really impact the work people can do, how productive they can be, how creative they can be, what they can accomplish.

The Operator interface looks very similar to Anthropic's [Claude Computer Use](https://simonwillison.net/2024/Oct/22/computer-use/) demo from October, even down to the interface with a chat panel on the left and a visible interface being interacted with on the right. Here's Operator:

[![Screenshot of Operator. The user has asked the chat window to book a table at a restauraunt. The OpenTable website is visible on the right.](https://substackcdn.com/image/fetch/$s_!Dbd4!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6cdcd142-a338-448b-bd70-b55ee4793613_3456x1940.jpeg "Screenshot of Operator. The user has asked the chat window to book a table at a restauraunt. The OpenTable website is visible on the right.")](https://substackcdn.com/image/fetch/$s_!Dbd4!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6cdcd142-a338-448b-bd70-b55ee4793613_3456x1940.jpeg)

And here's Claude Computer Use:

[![A Sudoku puzzle is displayed - the bot has already filled in several squares incorrectly with invalid numbers which have a subtle pink background.](https://substackcdn.com/image/fetch/$s_!I0Ah!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F23d1a7d8-c0a1-45aa-b202-0b5dd35972a4_3050x1914.jpeg "A Sudoku puzzle is displayed - the bot has already filled in several squares incorrectly with invalid numbers which have a subtle pink background.")](https://substackcdn.com/image/fetch/$s_!I0Ah!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F23d1a7d8-c0a1-45aa-b202-0b5dd35972a4_3050x1914.jpeg)

Claude Computer Use required you to run a own Docker container on your own hardware. Operator is much more of a product \- OpenAI host a Chrome instance for you in the cloud, providing access to the tool via their website.

Operator runs on top of a brand new model that OpenAI are calling CUA, for Computer\-Using Agent. Here's [their separate announcement](https://openai.com/index/computer-using-agent/) covering that new model, which should also be available via their API in the coming weeks.

This demo version of Operator is understandably cautious: it frequently asked users for confirmation to continue. It also provides a "take control" option which OpenAI's demo team used to take over and enter credit card details to make a final purchase.

The million dollar question around this concerns how they deal with security. Claude Computer Use [fell victim to prompt injection attack at the first hurdle](https://simonwillison.net/2024/Oct/25/zombais/).

Here's what [OpenAI have to say about that](https://openai.com/index/computer-using-agent/#safety):

> One particularly important category of model mistakes is **adversarial attacks on websites** that cause the CUA model to take unintended actions, through prompt injections, jailbreaks, and phishing attempts. In addition to the aforementioned mitigations against model mistakes, we developed several additional layers of defense to protect against these risks:
> 
> * **Cautious navigation:** The CUA model is designed to identify and ignore prompt injections on websites, recognizing all but one case from an early internal red\-teaming session.
> * **Monitoring:** In Operator, we've implemented an additional model to monitor and pause execution if it detects suspicious content on the screen.
> * **Detection pipeline:** We're applying both automated detection and human review pipelines to identify suspicious access patterns that can be flagged and rapidly added to the monitor (in a matter of hours).

Color me skeptical. I imagine we'll see all kinds of novel successful prompt injection style attacks against this model once the rest of the world starts to explore it.

My initial recommendation: start a fresh session for each task you outsource to Operator to ensure it doesn't have access to your credentials for any sites that you have used via the tool in the past. If you're having it spend money on your behalf let it get to the checkout, then provide it with your payment details and wipe the session straight afterwards.

The [Operator System Card PDF](https://cdn.openai.com/operator_system_card.pdf) has some interesting additional details. From the "limitations" section:

> Despite proactive testing and mitigation efforts, certain challenges and risks remain due to the difficulty of modeling the complexity of real\-world scenarios and the dynamic nature of adversarial threats. Operator may encounter novel use cases post\-deployment and exhibit different patterns of errors or model mistakes. Additionally, we expect that adversaries will craft novel prompt injection attacks and jailbreaks. Although we’ve deployed multiple mitigation layers, many rely on machine learning models, and with adversarial robustness still an open research problem, defending against emerging attacks remains an ongoing challenge.

Plus this interesting note on the CUA model's limitations:

> The CUA model is still in its early stages. It performs best on short, repeatable tasks but faces challenges with more complex tasks and environments like slideshows and calendars.

---

### [Six short video demos of LLM and Datasette projects](https://simonwillison.net/2025/Jan/22/office-hours-demos/) \- 2025\-01\-22

Last Friday Alex Garcia and I hosted a new kind of Datasette Public Office Hours session, inviting members of the Datasette community to share short demos of projects that they had built. The session lasted just over an hour and featured demos from six different people.

We broadcast live on YouTube, but I've now edited the session into separate videos. These are listed below, along with project summaries and show notes for each presentation.

You can also watch all six videos in [this YouTube playlist](https://www.youtube.com/playlist?list=PLSocEbMlNGotyeonEbgFP1_uf9gk1z7zm).

* [llm\-logs\-feedback by Matthias Lübken](https://simonwillison.net/2025/Jan/22/office-hours-demos/#llm-logs-feedback-by-matthias-l-bken)
* [llm\-model\-gateway and llm\-consortium by Thomas Hughes](https://simonwillison.net/2025/Jan/22/office-hours-demos/#llm-model-gateway-and-llm-consortium-by-thomas-hughes)
* [Congressional Travel Explorer with Derek Willis](https://simonwillison.net/2025/Jan/22/office-hours-demos/#congressional-travel-explorer-with-derek-willis)
* [llm\-questioncache with Nat Knight](https://simonwillison.net/2025/Jan/22/office-hours-demos/#llm-questioncache-with-nat-knight)
* [Improvements to Datasette Enrichments with Simon Willison](https://simonwillison.net/2025/Jan/22/office-hours-demos/#improvements-to-datasette-enrichments-with-simon-willison)
* [Datasette comments, pins and write UI with Alex Garcia](https://simonwillison.net/2025/Jan/22/office-hours-demos/#datasette-comments-pins-and-write-ui-with-alex-garcia)

#### llm\-logs\-feedback by Matthias Lübken

[llm\-logs\-feedback](https://github.com/luebken/llm-logs-feedback) is a plugin by Matthias Lübken for [LLM](https://llm.datasette.io/) which adds the ability to store feedback on prompt responses, using new `llm feedback+1` and `llm feedback-1` commands. These also accept an optional comment, and the feedback is stored in a `feedback` table in SQLite.

You can install the plugin from PyPI like this:

```
llm install llm-logs-feedback
```

The full plugin implementation is in the [llm\_logs\_feedback.py file](https://github.com/luebken/llm-logs-feedback/blob/main/llm_logs_feedback.py) in Matthias' GitHub repository.

#### llm\-model\-gateway and llm\-consortium by Thomas Hughes

Tommy Hughes has been developing a whole array of LLM plugins, including his [llm\-plugin\-generator](https://github.com/irthomasthomas/llm-plugin-generator) which is a plugin that can help write new plugins!

He started by demonstrating [llm\-model\-gateway](https://github.com/irthomasthomas/llm-model-gateway), a plugin that adds a `llm serve` command which starts a localhost server running an imitation of the OpenAI API against LLM models:

```
llm install llm-model-gateway
llm serve
```

Tommy's main demo was of [llm\-consortium](https://github.com/irthomasthomas/llm-consortium), a plugin which can use a consortium of collaborating LLM models working together to solve problems.

```
llm install llm-consortium
llm consortium "Best way to prepare avocado toast" \
  --models claude-3.5-sonnet \
  --models gpt-4o \
  --arbiter gegemini-1.5-pro-latest \
  --confidence-threshold 0.8 \
  --max-iterations 3 \
  --output results.json
```

I ran this and got back:

> The best way to prepare avocado toast involves selecting quality ingredients and careful preparation. Start with a thick slice of good quality bread, such as sourdough or whole grain. Toast it to your preferred level of crispness. While the bread is toasting, prepare a ripe avocado. Cut it in half, remove the pit, and scoop the flesh into a bowl. Mash the avocado with a fork, leaving some chunks for texture. Season with salt, black pepper, and a squeeze of fresh lemon juice to prevent browning. Optional additions include a touch of red pepper flakes.
> 
> Once the toast is ready, let it cool slightly before spreading the seasoned avocado evenly over it. Consider lightly rubbing a cut garlic clove on the warm toast for an extra layer of flavor (optional).
> 
> Enhance your avocado toast with your favorite toppings. Popular choices include: everything bagel seasoning, sliced tomatoes, radishes, a poached or fried egg (for added protein), microgreens, smoked salmon (for a more savory option), feta cheese crumbles, or a drizzle of hot sauce. For a finishing touch, drizzle with high\-quality olive oil and sprinkle with sesame or chia seeds for added texture.
> 
> Consider dietary needs when choosing toppings. For example, those following a low\-carb diet might skip the tomatoes and opt for more protein and healthy fats.
> 
> Finally, pay attention to presentation. Arrange the toppings neatly for a visually appealing toast. Serve immediately to enjoy the fresh flavors and crispy toast.

But the really interesting thing is the full log of the prompts and responses sent to Claude 3\.5 Sonnet and GPT\-4o, followed by a combined prompt to Gemini 1\.5 Pro to have it arbitrate between the two responses. You can see [the full logged prompts and responses here](https://gist.github.com/simonw/425f42f8ec1a963ae13c5b57ba580f56). Here's that [results.json](https://gist.github.com/simonw/e82370f0e5986a15823c82200c1b77f8) output file.

#### Congressional Travel Explorer with Derek Willis

Derek Willis teaches data journalism at the Philip Merrill College of Journalism at the University of Maryland. For a recent project his students built a [Congressional Travel Explorer](https://cnsmaryland.org/interactives/fall-2024/congressional_travel_explorer/index.html) interactive using Datasette, AWS Extract and Claude 3\.5 Sonnet to analyze travel disclosures from members of Congress.

One of the outcomes from the project was this story in Politico: [Members of Congress have taken hundreds of AIPAC\-funded trips to Israel in the past decade](https://www.politico.com/news/2024/10/30/israel-aipac-funded-congress-travel-00185167).

#### llm\-questioncache with Nat Knight

[llm\-questioncache](https://github.com/nathanielknight/llm-questioncache) builds on top of

https://llm.datasette.io/

to cache answers to questions, using embeddings to return similar answers if they have already been stored.

Using embeddings for de\-duplication of similar questions is an interesting way to apply LLM's [embeddings feature](https://llm.datasette.io/en/stable/embeddings/python-api.html).

#### Improvements to Datasette Enrichments with Simon Willison

I've demonstrated improvements I've been making to Datasette's [Enrichments](https://enrichments.datasette.io/) system over the past few weeks.

Enrichments allow you to apply an operation \- such as geocoding, a QuickJS JavaScript transformation or an LLM prompt \- against selected rows within a table.

The latest release of [datasette\-enrichments](https://github.com/datasette/datasette-enrichments/releases/tag/0.5) adds visible progress bars and the ability to pause, resume and cancel an enrichment job that is running against a table.

#### Datasette comments, pins and write UI with Alex Garcia

We finished with three plugin demos from Alex, showcasing collaborative features we have been developing for [Datasette Cloud](https://www.datasette.cloud/):

* [datasette\-write\-ui](https://github.com/datasette/datasette-write-ui) provides tools for editing and adding data to Datasette tables. A new feature here is the ability to shift\-click a row to open the editing interface for that row.
* [datasette\-pins](https://github.com/datasette/datasette-pins) allows users to pin tables and databases to their Datasette home page, making them easier to find.
* [datasette\-comments](https://github.com/datasette/datasette-comments) adds a commenting interface to Datasette, allowing users to leave comments on individual rows in a table.

---

**Quote** 2025\-01\-21

> *Is what you're doing taking a large amount of text and asking the LLM to convert it into a smaller amount of text? Then it's probably going to be great at it. If you're asking it to convert into a roughly equal amount of text it will be so\-so. If you're asking it to create more text than you gave it, forget about it.*

[Laurie Voss](https://seldo.com/posts/what-ive-learned-about-writing-ai-apps-so-far)

---

**Link** 2025\-01\-21 [AI mistakes are very different from human mistakes](https://www.schneier.com/blog/archives/2025/01/ai-mistakes-are-very-different-from-human-mistakes.html):

An entertaining and informative read by Bruce Schneier and Nathan E. Sanders.

> If you want to use an AI model to help with a business problem, it’s not enough to see that it understands what factors make a product profitable; you need to be sure it won’t forget what money is.

---

**Link** 2025\-01\-22 [Run DeepSeek R1 or V3 with MLX Distributed](https://gist.github.com/awni/ec071fd27940698edd14a4191855bba6):

Handy detailed instructions from Awni Hannun on running the enormous DeepSeek R1 or v3 models on a cluster of Macs using the [distributed communication](https://ml-explore.github.io/mlx/build/html/usage/distributed.html) feature of Apple's MLX library.

DeepSeek R1 quantized to 4\-bit requires 450GB in aggregate RAM, which can be achieved by a cluster of three 192 GB M2 Ultras ($16,797 will buy you three 192GB Apple M2 Ultra Mac Studios at $5,599 each).

---

**Link** 2025\-01\-22 [llm\-gemini 0\.9](https://github.com/simonw/llm-gemini/releases/tag/0.9):

This new release of my `llm-gemini` plugin adds support for two new experimental models:

* `learnlm-1.5-pro-experimental` is "an experimental task\-specific model that has been trained to align with learning science principles when following system instructions for teaching and learning use cases" \- [more here](https://ai.google.dev/gemini-api/docs/learnlm).
* `gemini-2.0-flash-thinking-exp-01-21` is a brand new version of the Gemini 2\.0 Flash Thinking model [released today](https://twitter.com/demishassabis/status/1881844417746632910):

> Latest version also includes code execution, a 1M token content window \& a reduced likelihood of thought\-answer contradictions.

The most exciting new feature though is support for [Google search grounding](https://ai.google.dev/gemini-api/docs/grounding), where some Gemini models can execute Google searches as part of answering a prompt. This feature can be enabled using the new `-o google_search 1` option.

---

**Link** 2025\-01\-22 [r1\.py script to run R1 with a min\-thinking\-tokens parameter](https://gist.github.com/vgel/8a2497dc45b1ded33287fa7bb6cc1adc):

Fantastically creative hack by Theia Vogel. The [DeepSeek R1 family](https://simonwillison.net/2025/Jan/20/deepseek-r1/) of models output their chain of thought inside a `<think>...</think>` block. Theia found that you can intercept that closing `</think>` and replace it with "Wait, but" or "So" or "Hmm" and trick the model into extending its thought process, producing better solutions!

You can stop doing this after a few iterations, or you can keep on denying the `</think>` string and effectively force the model to "think" forever.

Theia's code here works against Hugging Face transformers but I'm confident the same approach could be ported to llama.cpp or MLX.

---

**Link** 2025\-01\-22 [Trading Inference\-Time Compute for Adversarial Robustness](https://openai.com/index/trading-inference-time-compute-for-adversarial-robustness/):

Brand new research paper from OpenAI, exploring how inference\-scaling "reasoning" models such as o1 might impact the search for improved security with respect to things like prompt injection.

> We conduct experiments on the impact of increasing inference\-time compute in reasoning models (specifically OpenAI `o1-preview` and `o1-mini`) on their robustness to adversarial attacks. We find that across a variety of attacks, increased inference\-time compute leads to improved robustness. In many cases (with important exceptions), the fraction of model samples where the attack succeeds tends to zero as the amount of test\-time compute grows.

They clearly understand why this stuff is such a big problem, especially as we try to outsource more autonomous actions to "agentic models":

> Ensuring that agentic models function reliably when browsing the web, sending emails, or uploading code to repositories can be seen as analogous to ensuring that self\-driving cars drive without accidents. As in the case of self\-driving cars, an agent forwarding a wrong email or creating security vulnerabilities may well have far\-reaching real\-world consequences. Moreover, LLM agents face an additional challenge from adversaries which are rarely present in the self\-driving case. Adversarial entities could control some of the inputs that these agents encounter while browsing the web, or reading files and images.

This is a really interesting paper, but it starts with a *huge* caveat. The original sin of LLMs \- and the reason [prompt injection](https://simonwillison.net/tags/prompt-injection/) is such a hard problem to solve \- is the way they mix instructions and input data in the same stream of tokens. I'll quote section 1\.2 of the paper in full \- note that point 1 describes that challenge:

> **1\.2 Limitations of this work**
> 
> The following conditions are necessary to ensure the models respond more safely, even in adversarial settings:
> 
> 1. Ability by the model to parse its context into separate components. This is crucial to be able to distinguish data from instructions, and instructions at different hierarchies.
> 2. Existence of safety specifications that delineate what contents should be allowed or disallowed, how the model should resolve conflicts, etc..
> 3. Knowledge of the safety specifications by the model (e.g. in context, memorization of their text, or ability to label prompts and responses according to them).
> 4. Ability to apply the safety specifications to specific instances. For the adversarial setting, the crucial aspect is the ability of the model to apply the safety specifications to instances that are *out of the training distribution*, since naturally these would be the prompts provided by the adversary,

They then go on to say (emphasis mine):

> Our work demonstrates that inference\-time compute helps with Item 4, even in cases where the instance is shifted by an adversary to be far from the training distribution (e.g., by injecting soft tokens or adversarially generated content). **However, our work does not pertain to Items 1\-3, and even for 4, we do not yet provide a "foolproof" and complete solution**.
> 
> While we believe this work provides an important insight, we note that fully resolving the adversarial robustness challenge will require tackling all the points above.

So while this paper demonstrates that inference\-scaled models can greatly improve things with respect to identifying and avoiding out\-of\-distribution attacks against safety instructions, they are *not* claiming a solution to the key instruction\-mixing challenge of prompt injection. Once again, this is not the silver bullet we are all dreaming of.

The paper introduces two new categories of attack against inference\-scaling models, with two delightful names: "Think Less" and "Nerd Sniping".

**Think Less** attacks are when an attacker tricks a model into spending less time on reasoning, on the basis that more reasoning helps prevent a variety of attacks so cutting short the reasoning might help an attack make it through.

**Nerd Sniping** (see [XKCD 356](https://xkcd.com/356/)) does the opposite: these are attacks that cause the model to "spend inference\-time compute unproductively". In addition to added costs, these could also open up some security holes \- there are edge\-cases where attack success rates go up for longer compute times.

Sadly they didn't provide concrete examples for either of these new attack classes. I'd love to see what Nerd Sniping looks like in a malicious prompt!

---

**Quote** 2025\-01\-22

> *When I give money to a charitable cause, I always look for the checkboxes to opt out of being contacted by them in the future. When it happens anyway, I get annoyed, and I become reluctant to give to that charity again. \[...]   
>   
> When you donate to the Red Cross via Apple, that concern is off the table. Apple won’t emphasize that aspect of this, because they don’t want to throw the Red Cross under the proverbial bus, but I will. An underrated aspect of privacy is the desire simply not to be annoyed.*

[John Gruber](https://daringfireball.net/linked/2025/01/22/apple-red-cross-socal-fire-relief)

---

**Link** 2025\-01\-23 [LLM 0\.20](https://github.com/simonw/llm/releases/tag/0.20):

New release of my [LLM](https://llm.datasette.io/) CLI tool and Python library. A bunch of accumulated fixes and features since the start of December, most notably:

* Support for OpenAI's [o1 model](https://platform.openai.com/docs/models#o1) \- a significant upgrade from `o1-preview` given its 200,000 input and 100,000 output tokens (`o1-preview` was 128,000/32,768\). [\#676](https://github.com/simonw/llm/issues/676)
* Support for the `gpt-4o-audio-preview` and `gpt-4o-mini-audio-preview` models, which can accept audio input: `llm -m gpt-4o-audio-preview -a https://static.simonwillison.net/static/2024/pelican-joke-request.mp3` [\#677](https://github.com/simonw/llm/issues/677)
* A new `llm -x/--extract` option which extracts and returns the contents of the first fenced code block in the response. This is useful for prompts that generate code. [\#681](https://github.com/simonw/llm/issues/681)
* A new `llm models -q 'search'` option for searching available models \- useful if you've installed a lot of plugins. Searches are case insensitive. [\#700](https://github.com/simonw/llm/issues/700)

---

**Quote** 2025\-01\-23

> *I can’t reference external reports critical of China. Need to emphasize China’s policies on ethnic unity, development in Xinjiang, and legal protections. Avoid any mention of controversies or allegations to stay compliant.*

[DeepSeek R1](https://sherwood.news/tech/a-free-powerful-chinese-ai-model-just-dropped-but-dont-ask-it-about/)

---

**Quote** 2025\-01\-24

> *AI tools create a significant productivity boost for developers. Different folks report different gains, but most people who try AI code generation recognize its ability to increase velocity. Many people think that means we’re going to need fewer developers, and our industry is going to slowly circle the drain.   
>   
> This view is based on a misunderstanding of why people pay for software. A business creates software because they think that it will give them some sort of economic advantage. The investment needs to pay for itself with interest. There are many software projects that would help a business, but businesses aren’t going to do them because the return on investment doesn’t make sense.   
>   
> When software development becomes more efficient, the ROI of any given software project increases, which unlocks more projects. \[...] Cheaper software means people are going to want more of it. More software means more jobs for increasingly efficient software developers.*

[Dustin Ewers](https://dustinewers.com/ignore-the-grifters/)

---