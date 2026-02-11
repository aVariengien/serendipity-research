# Building a tool showing how Gemini Pro can return bounding boxes for objects in images

*Plus creating alt text for a bot using GPT-4o, and converting a PDF paper to semantic HTML with Gemini 1.5 Pro*

Published: 2024-08-26
Source: https://simonw.substack.com/p/building-a-tool-showing-how-gemini

---

In this newsletter:

* Building a tool showing how Gemini Pro can return bounding boxes for objects in images

Plus 8 links and 3 quotations

### [Building a tool showing how Gemini Pro can return bounding boxes for objects in images](https://simonwillison.net/2024/Aug/26/gemini-bounding-box-visualization/) \- 2024\-08\-26

I was browsing through Google's Gemini documentation while researching [how different multi\-model LLM APIs work](https://github.com/simonw/llm/issues/557) when I stumbled across [this note](https://ai.google.dev/gemini-api/docs/vision?lang=node#bbox) in the vision documentation:

> You can ask the model for the coordinates of bounding boxes for objects in images. For object detection, the Gemini model has been trained to provide these coordinates as relative widths or heights in range `[0,1]`, scaled by 1000 and converted to an integer. Effectively, the coordinates given are for a 1000x1000 version of the original image, and need to be converted back to the dimensions of the original image.

This is a pretty neat capability! OpenAI's GPT\-4o and Anthropic's Claude 3 and Claude 3\.5 models can't do this (yet).

I tried a few prompts using [Google's Python library](https://pypi.org/project/google-generativeai/) and got back what looked like bounding boxes!

```
>>> import google.generativeai as genai
>>> genai.configure(api_key="...")
>>> model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
>>> import PIL.Image
>>> goats = PIL.Image.open("/tmp/goats.jpeg")
>>> prompt = 'Return bounding boxes around every goat, for each one return [ymin, xmin, ymax, xmax]'
>>> response = model.generate_content([goats, prompt])
print(response.text)
>>> print(response.text)
- [200, 90, 745, 527]
- [300, 610, 904, 937]
```

But how to verify that these were useful co\-ordinates? I fired up Claude 3\.5 Sonnet and started iterating on [Artifacts](https://support.anthropic.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them) there to try and visualize those co\-ordinates against the original image.

After some fiddling around, I built [an initial debug tool](https://static.simonwillison.net/static/2024/gemini-bounding-box-tool-fixed.html) that I could paste co\-ordinates into and select an image and see that image rendered.

#### A tool for prompting with an image and rendering the bounding boxes

I wrote the other day about Anthropic's [new support for CORS headers](https://simonwillison.net/2024/Aug/23/anthropic-dangerous-direct-browser-access/), enabling direct browser access to their APIs.

Google Gemini supports CORS as well! So do OpenAI, which means that all three of the largest LLM providers can now be accessed directly from the browser.

I decided to build a combined tool that could prompt Gemini 1\.5 Pro with an image directly from the browser, then render the returned bounding boxes on that image.

The new tool lives here: **[https://tools.simonwillison.net/gemini\-bbox](https://tools.simonwillison.net/gemini-bbox)**

[![Gemini API Image Bounding Box Visualization - browse for file goats.jpeg, prompt is Return bounding boxes as JSON arrays [ymin, xmin, ymax, xmax] - there follows output coordinates and then a red and a green box around the goats in a photo, with grid lines showing the coordinates from 0-1000 on both axes](https://substackcdn.com/image/fetch/$s_!3ChN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F24c091e1-13f2-4c07-8072-8e1f358427ac_1508x1810.jpeg "Gemini API Image Bounding Box Visualization - browse for file goats.jpeg, prompt is Return bounding boxes as JSON arrays [ymin, xmin, ymax, xmax] - there follows output coordinates and then a red and a green box around the goats in a photo, with grid lines showing the coordinates from 0-1000 on both axes")](https://substackcdn.com/image/fetch/$s_!3ChN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F24c091e1-13f2-4c07-8072-8e1f358427ac_1508x1810.jpeg)

The first time you run a prompt it will ask you for a [Gemini API key](https://aistudio.google.com/app/apikey), which it stores in your browser's `localStorage`. I promise not to add code that steals your keys in the future, but if you don't want to trust that you can [grab a copy of the code](https://github.com/simonw/tools/blob/main/gemini-bbox.html), verify it and then run it yourself.

#### Building this tool with Claude 3\.5 Sonnet

This is yet another example of a tool that I mostly built by prompting Claude 3\.5 Sonnet. Here are [some more](https://simonwillison.net/search/?tag=claude-3-5-sonnet&tag=projects).

I started out with [this lengthy conversation](https://gist.github.com/simonw/40ff639e96d55a1df7ebfa7db1974b92) (transcript exported [with this tool](https://simonwillison.net/2024/Aug/8/convert-claude-json-to-markdown/)) to help build the original tool for opening an image and pasting in those bounding box coordinates. That sequence started like this:

> Build an artifact where I can open an image from my browser and paste the following style of text into a textarea:
> 
> 
> ```
> - [488, 945, 519, 999]
> - [460, 259, 487, 307]
> - [472, 574, 498, 612]
> 
> ```
> (The hyphens may not be there, so scan with a regex for \[ num, num, num, num ])
> 
> Each of those represent \[ymin, xmin, ymax, xmax] coordinates on the image \- but they are numbers between 0 and 1000 so they correspond to the image is if it had been resized to 1000x1000
> 
> As soon as the coords are pasted the corresponding boxes should be drawn on the images, corrected for its actual dimensions
> 
> The image should be show with a width of 80% of the page
> 
> The boxes should be in different colours, and hovering over each box should show the original bounding box coordinates below the image

Once that tool appeared to be doing the right thing (I had to muck around with how the coordinates were processed a bunch) I used my favourite prompting trick to build the combined tool that called the Gemini API. I found [this example](https://github.com/google-gemini/generative-ai-js/blob/1ad800656dc870c1c5a60c1201baa56ad48b88ee/samples/web/utils/shared.js) that calls the [@google/generative\-ai](https://www.npmjs.com/package/@google/generative-ai) API from a browser, pasted the full example into Claude along with my previous bounding box visualization tool and had it combine them to achieve the desired result:

> Based on that example text, build me an HTML page with Vanilla JS that loads the Gemini API from esm.run \- it should have a file input and a textarea and a submit button \- you attach an image, enter a prompt and then click the button and it does a Gemini prompt with that image and prompt and injects the returned result into a div on the page

Then this follow\-up prompt:

> now incorporate the logic from this tool *(I pasted in that HTML too)*, such that when the response is returned from the prompt the image is displayed with any rendered bounding boxes

#### Dealing with image orientation bugs

Bounding boxes are fiddly things. The code I had produced above seemed to work... but in some of my testing the boxes didn't show up in quite the right place. Was this just Gemini 1\.5 Pro being unreliable in how it returned the boxes? That seemed likely, but I had some nagging doubts.

On a hunch, I took [an image](https://static.simonwillison.net/static/2024/goats-weird-rotation.jpeg) that was behaving strangely, took a screenshot of it and tried [that screenshot as a JPEG](https://static.simonwillison.net/static/2024/goats-no-rotation.jpg). The bounding boxes that came back were different \- they appeared rotated!

I've seen this kind of thing before with photos taken on an iPhone. There's an obscure piece of JPEG metadata which can set the orientation on a photo, and some software fails to respect that.

Was that affecting my bounding box tool? I started digging into those photos to figure that out, using a combination of ChatGPT Code Interpreter (since that can read JPEG binary data using Python) and Claude Artifacts (to build me a visible UI for exploring my photos).

My hunch turned out to be correct: my iPhone photos included TIFF orientation metadata which the Gemini API appeared not to respect. As a result, some photos taken by my phone would return bounding boxes that were rotated 180 degrees.

My eventual fix was to take the image provided by the user, render it to a `<canvas>` element and then export it back out as a JPEG again \- [code here](https://github.com/simonw/tools/blob/66552828b1ce6f823baccfc95ccdd81d8bb5992a/gemini-bbox.html#L41-L71). I got Claude to add that for me based on code I pasted in from my earlier [image resize quality](https://tools.simonwillison.net/image-resize-quality) tool, also [built for me by Claude](https://simonwillison.net/2024/Jul/26/image-resize-and-quality-comparison/).

As part of this investigation I built another tool, which can read orientation TIFF data from a JPEG entirely in JavaScript and help show what's going on:

**[https://tools.simonwillison.net/tiff\-orientation](https://tools.simonwillison.net/tiff-orientation)**

[![Drag & Drop a JPEG image here or click to select. TIFF Orientation: Rotated 180°. Orientation value: 3](https://substackcdn.com/image/fetch/$s_!YaWk!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb3f48c2f-f143-4753-b969-44fdb6a9c6cd_1626x486.jpeg "Drag & Drop a JPEG image here or click to select. TIFF Orientation: Rotated 180°. Orientation value: 3")](https://substackcdn.com/image/fetch/$s_!YaWk!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb3f48c2f-f143-4753-b969-44fdb6a9c6cd_1626x486.jpeg)

Here's [the source code for that](https://github.com/simonw/tools/blob/main/tiff-orientation.html). The source code is a great example of the kind of thing that LLMs can do much more effectively than I can \- here's an illustrative snippet:

```
// Determine endianness
const endian = view.getUint16(tiffStart, false);
const isLittleEndian = (endian === 0x4949);  // 'II' in ASCII
debugInfo += `Endianness: ${isLittleEndian ? 'Little Endian' : 'Big Endian'}\n`;

// Check TIFF header validity
const tiffMagic = view.getUint16(tiffStart + 2, isLittleEndian);
if (tiffMagic !== 42) {
    throw Object.assign(new Error('Not a valid TIFF header'), { debugInfo });
}
debugInfo += 'Valid TIFF header\n';

// Get offset to first IFD
const ifdOffset = view.getUint32(tiffStart + 4, isLittleEndian);
const ifdStart = tiffStart + ifdOffset;
debugInfo += `IFD start: ${ifdStart}\n`;
```

LLMs know their binary file formats, so I frequently find myself asking them to write me custom binary processing code like this.

Here's [the Claude conversation](https://gist.github.com/simonw/9bf1bd4cce6d113c55db0e5a03769b52) I had to build that tool. After failing to get it to work several times I pasted in Python code that I'd built using ChatGPT Code Interpreter and prompted:

> Here's Python code that finds it correctly:

Which turned out to provide the missing details to help it build me the JavaScript version I could run in my browser. Here's [the ChatGPT conversation](https://gist.github.com/simonw/327a906e83efaf3e79853eec8bdd72e0) that got me that Python code.

#### Mixing up a whole bunch of models

This whole process was *very* messy, but it's a pretty accurate representation of my workflow when using these models. I used three different tools here:

* Gemini 1\.5 Pro and the Gemini API to take images and a prompt and return bounding boxes
* Claude 3\.5 Sonnet and Claude Artifacts to write code for working against that API and build me interactive tools for visualizing the results
* GPT\-4o and ChatGPT Code Interpreter to write and execute Python code to try and help me figure out what was going on with my weird JPEG image orientation bugs

I copied code between models a bunch of times too \- pasting Python code written by GPT\-4o into Claude 3\.5 Sonnet to help it write the correct JavaScript for example.

How good is the code that I produced by the end of this all? It honestly doesn't matter very much to me: this is a very low\-stakes project, where the goal was a single web page tool that can run a prompt through a model and visualize the response.

If I was writing code "for production" \- for a long\-term project, or code that I intended to package up and release as an open source library \- I would sweat the details a whole lot more. But for this kind of exploratory and prototyping work I'm increasingly comfortable hacking away at whatever the models spit out until it achieves the desired effect.

---

**Link** 2024\-08\-23 [Explain ACLs by showing me a SQLite table schema for implementing them](https://gist.github.com/simonw/20b2e8c4d9d9d8d6dee327c221e57205):

Here’s an example transcript showing one of the common ways I use LLMs. I wanted to develop an understanding of ACLs \- Access Control Lists \- but I’ve found previous explanations *incredibly dry*. So I prompted Claude 3\.5 Sonnet:

> Explain ACLs by showing me a SQLite table schema for implementing them

Asking for explanations using the context of something I’m already fluent in is usually really effective, and an great way to take advantage of the weird abilities of frontier LLMs.

I exported the transcript to a Gist using my [Convert Claude JSON to Markdown](https://observablehq.com/@simonw/convert-claude-json-to-markdown) tool, which I just upgraded to support syntax highlighting of code in artifacts.

---

**Link** 2024\-08\-23 [Top companies ground Microsoft Copilot over data governance concerns](https://www.theregister.com/2024/08/21/microsoft_ai_copilots/):

Microsoft’s use of the term “Copilot” is pretty confusing these days \- this article appears to be about [Microsoft 365 Copilot](https://www.microsoft.com/en-us/microsoft-365/enterprise/copilot-for-microsoft-365), which is effectively an internal RAG chatbot with access to your company’s private data from tools like SharePoint.

The concern here isn’t the usual fear of data leaked to the model or prompt injection security concerns. It’s something much more banal: it turns out many companies don’t have the right privacy controls in place to safely enable these tools.

Jack Berkowitz (of Securiti, who sell a product designed to help with data governance):

> Particularly around bigger companies that have complex permissions around their SharePoint or their Office 365 or things like that, where the Copilots are basically aggressively summarizing information that maybe people technically have access to but shouldn't have access to.
> 
> Now, maybe if you set up a totally clean Microsoft environment from day one, that would be alleviated. But nobody has that.

If your document permissions aren’t properly locked down, anyone in the company who asks the chatbot “how much does everyone get paid here?” might get an instant answer!

This is a fun example of a problem with AI systems caused by them working exactly as advertised.

This is also not a new problem: the article mentions similar concerns introduced when companies tried adopting [Google Search Appliance](https://en.m.wikipedia.org/wiki/Google_Search_Appliance) for internal search more than twenty years ago.

---

**Link** 2024\-08\-24 [Musing about OAuth and LLMs on Mastodon](https://fedi.simonwillison.net/@simon/113014147494012212):

Lots of people are asking why Anthropic and OpenAI don't support OAuth, so you can bounce users through those providers to get a token that uses their API budget for your app.

My guess: they're worried malicious app developers would use it to trick people and obtain valid API keys.

Imagine a version of my dumb little [write a haiku about a photo you take](https://tools.simonwillison.net/haiku) page which used OAuth, harvested API keys and then racked up hundreds of dollar bills against everyone who tried it out running illicit election interference campaigns or whatever.

I'm trying to think of an OAuth API that dishes out tokens which effectively let you *spend money on behalf of your users* and I can't think of any \- OAuth is great for "grant this app access to data that I want to share", but "spend money on my behalf" is a whole other ball game.

I guess there's a version of this that could work: it's OAuth but users get to set a spending limit of e.g. $1 (maybe with the authenticating app suggesting what that limit should be).

Here's a counter\-example [from Mike Taylor](https://twitter.com/hammer_mt/status/1827144780650017162) of a category of applications that do use OAuth to authorize spend on behalf of users:

> I used to work in advertising and plenty of applications use OAuth to connect your Facebook and Google ads accounts, and they could do things like spend all your budget on disinformation ads, but in practice I haven't heard of a single case. When you create a dev application there are stages of approval so you can only invite a handful of beta users directly until the organization and app gets approved.

In which case maybe the cost for providers here is in review and moderation: if you’re going to run an OAuth API that lets apps spend money on behalf of their users you need to actively monitor your developer community and review and approve their apps.

---

**Quote** 2024\-08\-24

> *\[...] here’s what we found when we integrated \[Amazon Q, GenAI assistant for software development] into our internal systems and applied it to our needed Java upgrades:   
>   
> \- The average time to upgrade an application to Java 17 plummeted from what’s typically 50 developer\-days to just a few hours. We estimate this has saved us the equivalent of 4,500 developer\-years of work (yes, that number is crazy but, real).   
> \- In under six months, we've been able to upgrade more than 50% of our production Java systems to modernized Java versions at a fraction of the usual time and effort. And, our developers shipped 79% of the auto\-generated code reviews without any additional changes.*

[Andy Jassy, Amazon CEO](https://www.linkedin.com/posts/andy-jassy-8b1615_one-of-the-most-tedious-but-critical-tasks-activity-7232374162185461760-AdSz/)

---

**Link** 2024\-08\-24 [SQL Has Problems. We Can Fix Them: Pipe Syntax In SQL](https://research.google/pubs/sql-has-problems-we-can-fix-them-pipe-syntax-in-sql/):

A new paper from Google Research describing custom syntax for analytical SQL queries that has been rolling out inside Google since February, reaching 1,600 "seven\-day\-active users" by August 2024\.

A key idea is here is to fix one of the biggest usability problems with standard SQL: the order of the clauses in a query. Starting with `SELECT` instead of `FROM` has always been confusing, see [SQL queries don't start with SELECT](https://jvns.ca/blog/2019/10/03/sql-queries-don-t-start-with-select/) by Julia Evans.

Here's an example of the new alternative syntax, taken from the [Pipe query syntax documentation](https://github.com/google/zetasql/blob/2024.08.2/docs/pipe-syntax.md) that was added to Google's open source [ZetaSQL](https://github.com/google/zetasql) project last week.

For this SQL query:

```
SELECT component_id, COUNT(*)
FROM ticketing_system_table
WHERE
  assignee_user.email = 'username@email.com'
  AND status IN ('NEW', 'ASSIGNED', 'ACCEPTED')
GROUP BY component_id
ORDER BY component_id DESC;
```

The Pipe query alternative would look like this:

```
FROM ticketing_system_table
|> WHERE
    assignee_user.email = 'username@email.com'
    AND status IN ('NEW', 'ASSIGNED', 'ACCEPTED')
|> AGGREGATE COUNT(*)
   GROUP AND ORDER BY component_id DESC;

```

The Google Research paper is released as a two\-column PDF. I [snarked about this](https://news.ycombinator.com/item?id=41339138) on Hacker News:

> Google: you are a web company. Please learn to publish your research papers as web pages.

This remains a long\-standing pet peeve of mine. PDFs like this are horrible to read on mobile phones, hard to copy\-and\-paste from, have poor accessibility (see [this Mastodon conversation](https://fedi.simonwillison.net/@simon/113017908957136345)) and are generally just *bad citizens* of the web.

Having complained about this I felt compelled to see if I could address it myself. Google's own Gemini Pro 1\.5 model can process PDFs, so I uploaded the PDF to [Google AI Studio](https://aistudio.google.com/) and prompted the `gemini-1.5-pro-exp-0801` model like this:

> Convert this document to neatly styled semantic HTML

This worked *surprisingly well*. It output HTML for about half the document and then stopped, presumably hitting the output length limit, but a follow\-up prompt of "and the rest" caused it to continue from where it stopped and run until the end.

Here's the result (with a banner I added at the top explaining that it's a conversion): [Pipe\-Syntax\-In\-SQL.html](https://static.simonwillison.net/static/2024/Pipe-Syntax-In-SQL.html)

I haven't compared the two completely, so I can't guarantee there are no omissions or mistakes.

The figures from the PDF aren't present \- Gemini Pro output tags like `<img src="figure1.png" alt="Figure 1: SQL syntactic clause order doesn't match semantic evaluation order. (From [25].)">` but did nothing to help me create those images.

Amusingly the document ends with `<p>(A long list of references, which I won't reproduce here to save space.)</p>` rather than actually including the references from the paper!

So this isn't a perfect solution, but considering it took just the first prompt I could think of it's a very promising start. I expect someone willing to spend more than the couple of minutes I invested in this could produce a very useful HTML alternative version of the paper with the assistance of Gemini Pro.

One last amusing note: I posted a link to this [to Hacker News](https://news.ycombinator.com/item?id=41339238) a few hours ago. Just now when I searched Google for the exact title of the paper my HTML version was already the third result!

I've now added a `<meta name="robots" content="noindex, follow">` tag to the top of the HTML to keep this unverified [AI slop](https://simonwillison.net/tags/slop/) out of their search index. This is a good reminder of how much better HTML is than PDF for sharing information on the web!

---

**Link** 2024\-08\-25 [My @covidsewage bot now includes useful alt text](https://fedi.simonwillison.net/@covidsewage/113023397159658020):

I've been running a [@covidsewage](https://fedi.simonwillison.net/@covidsewage) Mastodon bot for a while now, posting daily screenshots (taken with [shot\-scraper](https://shot-scraper.datasette.io/)) of the Santa Clara County [COVID in wastewater](https://publichealth.santaclaracounty.gov/health-information/health-data/disease-data/covid-19/covid-19-wastewater) dashboard.

Prior to today the screenshot was accompanied by the decidedly unhelpful alt text "Screenshot of the latest Covid charts".

I finally fixed that today, closing [issue \#2](https://github.com/simonw/covidsewage-bot/issues/2) more than two years after I first opened it.

The screenshot is of a Microsoft Power BI dashboard. I hoped I could scrape the key information out of it using JavaScript, but the weirdness of their DOM proved insurmountable.

Instead, I'm using GPT\-4o \- specifically, this Python code (run using a `python -c` block in the GitHub Actions YAML file):

```
import base64, openai
client = openai.OpenAI()
with open('/tmp/covid.png', 'rb') as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
messages = [
    {'role': 'system',
     'content': 'Return the concentration levels in the sewersheds - single paragraph, no markdown'},
    {'role': 'user', 'content': [
        {'type': 'image_url', 'image_url': {
            'url': 'data:image/png;base64,' + encoded_image
        }}
    ]}
]
completion = client.chat.completions.create(model='gpt-4o', messages=messages)
print(completion.choices[0].message.content)
```

I'm base64 encoding the screenshot and sending it with this system prompt:

> Return the concentration levels in the sewersheds \- single paragraph, no markdown

Given this input image:

[![Screenshot of a Power BI dashboard showing information that is described below](https://substackcdn.com/image/fetch/$s_!O1nz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff482d2b5-456a-43ff-a1d7-8f2a9890c96e_1280x726.jpeg "Screenshot of a Power BI dashboard showing information that is described below")](https://substackcdn.com/image/fetch/$s_!O1nz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff482d2b5-456a-43ff-a1d7-8f2a9890c96e_1280x726.jpeg)

Here's the text that comes back:

> The concentration levels of SARS\-CoV\-2 in the sewersheds from collected samples are as follows: San Jose Sewershed has a high concentration, Palo Alto Sewershed has a high concentration, Sunnyvale Sewershed has a high concentration, and Gilroy Sewershed has a medium concentration.

The full implementation can be found in [the GitHub Actions workflow](https://github.com/simonw/covidsewage-bot/blob/main/.github/workflows/post.yml), which runs on a schedule at 7am Pacific time every day.

---

**Link** 2024\-08\-26 [AI\-powered Git Commit Function](https://gist.github.com/karpathy/1dd0294ef9567971c1e4348a90d69285):

Andrej Karpathy built a shell alias, `gcm`, which passes your staged Git changes to an LLM via my [LLM](https://llm.datasette.io/) tool, generates a short commit message and then asks you if you want to "(a)ccept, (e)dit, (r)egenerate, or (c)ancel?".

Here's the incantation he's using to generate that commit message:

```
git diff --cached | llm "
Below is a diff of all staged changes, coming from the command:
```
git diff --cached
```
Please generate a concise, one-line commit message for these changes."
```

This pipes the data into LLM (using the default model, currently `gpt-4o-mini` unless you [set it to something else](https://llm.datasette.io/en/stable/setup.html#setting-a-custom-default-model)) and then appends the prompt telling it what to do with that input.

---

**Link** 2024\-08\-26 [Long context prompting tips](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/long-context-tips):

Interesting tips here from Anthropic's documentation about how to best prompt Claude to work with longer documents.

> **Put longform data at the top**: Place your long documents and inputs (\~20K\+ tokens) near the top of your prompt, above your query, instructions, and examples. This can significantly improve Claude’s performance across all models. *Queries at the end can improve response quality by up to 30% in tests, especially with complex, multi\-document inputs.*

It recommends using not\-quite\-valid\-XML to add those documents to those prompts, and using a prompt that asks Claude to extract direct quotes before replying to help it focus its attention on the most relevant information:

> `Find quotes from the patient records and appointment history that are relevant to diagnosing the patient's reported symptoms. Place these in <quotes> tags. Then, based on these quotes, list all information that would help the doctor diagnose the patient's symptoms. Place your diagnostic information in <info> tags.`

---

**Link** 2024\-08\-26 [Anthropic Release Notes: System Prompts](https://docs.anthropic.com/en/release-notes/system-prompts):

Anthropic now publish the system prompts for their user\-facing chat\-based LLM systems \- Claude 3 Haiku, Claude 3 Opus and Claude 3\.5 Sonnet \- as part of their documentation, with a promise to update this to reflect future changes.

Currently covers just the initial release of the prompts, each of which is dated July 12th 2024\.

Anthropic researcher Amanda Askell [broke down their system prompt in detail](https://twitter.com/amandaaskell/status/1765207842993434880) back in March 2024\. These new releases are a much appreciated extension of that transparency.

These prompts are always fascinating to read, because they can act a little bit like documentation that the providers never thought to publish elsewhere.

There are lots of interesting details in the Claude 3\.5 Sonnet system prompt. Here's how they handle controversial topics:

> `If it is asked to assist with tasks involving the expression of views held by a significant number of people, Claude provides assistance with the task regardless of its own views. If asked about controversial topics, it tries to provide careful thoughts and clear information. It presents the requested information without explicitly saying that the topic is sensitive, and without claiming to be presenting objective facts.`

Here's chain of thought "think step by step" processing baked into the system prompt itself:

> `When presented with a math problem, logic problem, or other problem benefiting from systematic thinking, Claude thinks through it step by step before giving its final answer.`

Claude's face blindness is also part of the prompt, which makes me wonder if the API\-accessed models might more capable of working with faces than I had previously thought:

> `Claude always responds as if it is completely face blind. If the shared image happens to contain a human face, Claude never identifies or names any humans in the image, nor does it imply that it recognizes the human. [...] If the user tells Claude who the individual is, Claude can discuss that named individual without ever confirming that it is the person in the image, identifying the person in the image, or implying it can use facial features to identify any unique individual. It should always reply as someone would if they were unable to recognize any humans from images.`

It's always fun to see parts of these prompts that clearly hint at annoying behavior in the base model that they've tried to correct!

> `Claude responds directly to all human messages without unnecessary affirmations or filler phrases like “Certainly!”, “Of course!”, “Absolutely!”, “Great!”, “Sure!”, etc. Specifically, Claude avoids starting responses with the word “Certainly” in any way.`

Anthropic note that these prompts are for their user\-facing products only \- they aren't used by the Claude models when accessed via their API.

---

**Quote** 2024\-08\-26

> *In 2021 we \[the Mozilla engineering team] found “samesite\=lax by default” isn’t shippable without what you call the [“two minute twist”](https://simonwillison.net/2021/Aug/3/samesite/#chrome-2-minute-twist) \- you risk breaking a lot of websites. If you have that kind of two\-minute exception, a lot of exploits that were supposed to be prevented remain possible.   
>   
> When we tried rolling it out, we had to deal with a lot of broken websites: Debugging cookie behavior in website backends is nontrivial from a browser.   
>   
> Firefox also had a prototype of what I believe is a better protection (including additional privacy benefits) already underway (called [total cookie protection](https://blog.mozilla.org/en/mozilla/firefox-rolls-out-total-cookie-protection-by-default-to-all-users-worldwide/)).   
>   
> Given all of this, we paused samesite lax by default development in favor of this.*

[Frederik Braun](https://lobste.rs/s/98rp8f/cors_is_stupid#c_9dtjao)

---

**Quote** 2024\-08\-26

> *We've read and heard that you'd appreciate more transparency as to when changes, if any, are made. We've also heard feedback that some users are finding Claude's responses are less helpful than usual. Our initial investigation does not show any widespread issues. We'd also like to confirm that we've made no changes to the 3\.5 Sonnet model or inference pipeline.*

[Alex Albert](https://old.reddit.com/r/ClaudeAI/comments/1f1shun/new_section_on_our_docs_for_system_prompt_changes/)

---