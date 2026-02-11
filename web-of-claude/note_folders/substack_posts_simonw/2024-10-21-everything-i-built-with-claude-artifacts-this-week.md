# Everything I built with Claude Artifacts this week

*And unning Llama 3.2 Vision and Phi-3.5 Vision on a Mac with mistral.rs*

Published: 2024-10-21
Source: https://simonw.substack.com/p/everything-i-built-with-claude-artifacts

---

In this newsletter:

* Everything I built with Claude Artifacts this week
* Running Llama 3\.2 Vision and Phi\-3\.5 Vision on a Mac with mistral.rs

Plus 5 links and 4 quotations

### [Everything I built with Claude Artifacts this week](https://simonwillison.net/2024/Oct/21/claude-artifacts/) \- 2024\-10\-21

I'm a huge fan of Claude's **Artifacts** feature, which lets you prompt [Claude](https://claude.ai/) to create an interactive Single Page App (using HTML, CSS and JavaScript) and then view the result directly in the Claude interface, iterating on it further with the bot and then, if you like, copying out the resulting code.

I was digging around in my [Claude activity export](https://support.anthropic.com/en/articles/9450526-how-can-i-export-my-claude-ai-data) (I built a [claude\-to\-sqlite](https://github.com/simonw/claude-to-sqlite) tool to convert it to SQLite I could explore it in [Datasette](https://datasette.io/)) and decided to see how much I'd used artifacts [in the past week](https://github.com/simonw/claude-to-sqlite/issues/2#issuecomment-2425658909). It was more than I expected!

Being able to spin up a full interactive application \- sometimes as an illustrative prototype, but often as something that directly solves a problem \- is a remarkably useful tool.

Here's most of what I've used Claude Artifacts for in the past seven days. I've provided prompts or a full transcript for nearly all of them.

* [URL to Markdown with Jina Reader](https://simonwillison.net/2024/Oct/21/claude-artifacts/#url-to-markdown-with-jina-reader)
* [SQLite in WASM demo](https://simonwillison.net/2024/Oct/21/claude-artifacts/#sqlite-in-wasm-demo)
* [Extract URLs](https://simonwillison.net/2024/Oct/21/claude-artifacts/#extract-urls)
* [Clipboard viewer](https://simonwillison.net/2024/Oct/21/claude-artifacts/#clipboard-viewer)
* [Pyodide REPL](https://simonwillison.net/2024/Oct/21/claude-artifacts/#pyodide-repl)
* [Photo Camera Settings Simulator](https://simonwillison.net/2024/Oct/21/claude-artifacts/#photo-camera-settings-simulator)
* [LLM pricing calculator](https://simonwillison.net/2024/Oct/21/claude-artifacts/#llm-pricing-calculator)
* [YAML to JSON converter](https://simonwillison.net/2024/Oct/21/claude-artifacts/#yaml-to-json-converter)
* [OpenAI Audio](https://simonwillison.net/2024/Oct/21/claude-artifacts/#openai-audio)
* [QR Code Decoder](https://simonwillison.net/2024/Oct/21/claude-artifacts/#qr-code-decoder)
* [Image Converter and Page Downloader](https://simonwillison.net/2024/Oct/21/claude-artifacts/#image-converter-and-downloader)
* [HTML Entity Escaper](https://simonwillison.net/2024/Oct/21/claude-artifacts/#html-entity-escaper)
* [text\-wrap\-balance\-nav](https://simonwillison.net/2024/Oct/21/claude-artifacts/#text-wrap-balance-nav)
* [ARES Phonetic Alphabet Converter](https://simonwillison.net/2024/Oct/21/claude-artifacts/#ares-phonetic-alphabet-converter)

#### URL to Markdown with Jina Reader

I got frustrated at how hard it was to copy and paste the entire text of a web page into an LLM while using Mobile Safari. So I built a simple web UI that lets me enter a URL, calls the [Jina Reader API](https://jina.ai/reader) to generate Markdown (which uses Puppeteer under the hood) and gives me that Markdown with a convenient "Copy" button.

Try it out: [https://tools.simonwillison.net/jina\-reader](https://tools.simonwillison.net/jina-reader) ([Code](https://github.com/simonw/tools/blob/main/jina-reader.html))

[![Jina Reader - URL field, Markdown selected in a select box, Submit button. Then a box showing Markdown extracted from the page with a Copy to Clipboard button. Then a frame showing a preview of the rendered Markdown.](https://substackcdn.com/image/fetch/$s_!mzOU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F703a4526-4b2f-43d8-996c-a4abdd277acf_1322x1308.jpeg "Jina Reader - URL field, Markdown selected in a select box, Submit button. Then a box showing Markdown extracted from the page with a Copy to Clipboard button. Then a frame showing a preview of the rendered Markdown.")](https://substackcdn.com/image/fetch/$s_!mzOU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F703a4526-4b2f-43d8-996c-a4abdd277acf_1322x1308.jpeg)

I wrote [more about that project here](https://simonwillison.net/2024/Oct/14/my-jina-reader-tool/?uu).

#### SQLite in WASM demo

A Hacker News [conversation about SQLite's WASM build](https://news.ycombinator.com/item?id=41851051#41851788) lead me to the [@sqlite.org/sqlite\-wasm](https://www.npmjs.com/package/@sqlite.org/sqlite-wasm) package on NPM, and I decided to knock together a quick interactive demo.

[![Pelican Sightings in Half Moon Bay - a textarea with select * from pelican sightings, an execute query button and a table displaying 5 matching rows.](https://substackcdn.com/image/fetch/$s_!qtzu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F70059697-ea18-448a-a25b-fa9de823bcff_1322x1139.jpeg "Pelican Sightings in Half Moon Bay - a textarea with select * from pelican sightings, an execute query button and a table displaying 5 matching rows.")](https://substackcdn.com/image/fetch/$s_!qtzu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F70059697-ea18-448a-a25b-fa9de823bcff_1322x1139.jpeg)

Try it out here: [tools.simonwillison.net/sqlite\-wasm](https://tools.simonwillison.net/sqlite-wasm)

[Code](https://github.com/simonw/tools/blob/main/sqlite-wasm.html), [Claude transcript](https://gist.github.com/simonw/677c3794051c4dfeac94e514a8e5b697)

#### Extract URLs

I found myself wanting to extract all of the underlying URLs that were linked to from a chunk of text on a web page. I realized the fastest way to do that would be to spin up an artifact that could accept rich\-text HTML pastes and use an HTML parser to extract those links.

[![Extract URLs tool. Content pasted. URLs extracted. Shows a list of extracted URLs.](https://substackcdn.com/image/fetch/$s_!3jH0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67b3a2e7-c7f0-4b8d-b174-5757ff0a8249_1322x1006.jpeg "Extract URLs tool. Content pasted. URLs extracted. Shows a list of extracted URLs.")](https://substackcdn.com/image/fetch/$s_!3jH0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67b3a2e7-c7f0-4b8d-b174-5757ff0a8249_1322x1006.jpeg)

[https://tools.simonwillison.net/extract\-urls](https://tools.simonwillison.net/extract-urls)

[Code](https://github.com/simonw/tools/blob/main/extract-urls.html), [Claude transcript](https://gist.github.com/simonw/0a7d0ddeb0fdd63a844669475778ca06)

#### Clipboard viewer

Messing around with a tool that lets you paste in rich text reminded me that the browser clipboard API is a fascinating thing. I decided to build a quick debugging tool that would let me copy and paste different types of content (plain text, rich text, files, images etc) and see what information was available to me in the browser.

[![Clipboard format viewer. Paste here or anywhere on the page. Shows text/html with a fragment of HTML, text/plain with some text and Clipboard Event Information showing event type paste and formats available text/html and text/plain](https://substackcdn.com/image/fetch/$s_!rqeP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa455df72-18d9-4574-9151-be3f71669619_1322x1308.jpeg "Clipboard format viewer. Paste here or anywhere on the page. Shows text/html with a fragment of HTML, text/plain with some text and Clipboard Event Information showing event type paste and formats available text/html and text/plain")](https://substackcdn.com/image/fetch/$s_!rqeP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa455df72-18d9-4574-9151-be3f71669619_1322x1308.jpeg)

[https://tools.simonwillison.net/clipboard\-viewer](https://tools.simonwillison.net/clipboard-viewer)

[Code](https://github.com/simonw/tools/blob/main/clipboard-viewer.html), [Claude transcript](https://gist.github.com/simonw/5393dd81fcabc9f854e8bbec205e7e1e)

#### Pyodide REPL

I didn't put a lot of effort into this one. While poking around with Claude Artifacts in the browser DevTools I spotted this CSP header:

`content-security-policy: default-src https://www.claudeusercontent.com; script-src 'unsafe-eval' 'unsafe-inline' https://www.claudeusercontent.com https://cdnjs.cloudflare.com https://cdn.jsdelivr.net/pyodide/; connect-src https://cdn.jsdelivr.net/pyodide/; worker-src https://www.claudeusercontent.com blob:; style-src 'unsafe-inline' https://www.claudeusercontent.com https://cdnjs.cloudflare.com https://fonts.googleapis.com; img-src blob: data: https://www.claudeusercontent.com; font-src data: https://www.claudeusercontent.com; object-src 'none'; base-uri https://www.claudeusercontent.com; form-action https://www.claudeusercontent.com; frame-ancestors https://www.claudeusercontent.com https://claude.ai https://preview.claude.ai https://claude.site https://feedback.anthropic.com; upgrade-insecure-requests; block-all-mixed-content`

The `https://cdn.jsdelivr.net/pyodide/` in there caught my eye, because it suggested that the Anthropic development team had deliberately set it up so [Pyodide](https://pyodide.org/) \- Python compiled to WebAssembly \- could be loaded in an artifact.

I got Claude to spin up a very quick demo to prove that this worked:

[![Pyodide Python REPL -   3 + 4 returns 7. A textarea to enter python code and a Run button.](https://substackcdn.com/image/fetch/$s_!DauT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5da09aa1-e321-455d-b609-15a8422e0b69_1322x739.jpeg "Pyodide Python REPL -   3 + 4 returns 7. A textarea to enter python code and a Run button.")](https://substackcdn.com/image/fetch/$s_!DauT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5da09aa1-e321-455d-b609-15a8422e0b69_1322x739.jpeg)

[https://claude.site/artifacts/a3f85567\-0afc\-4854\-b3d3\-3746dd1a37f2](https://claude.site/artifacts/a3f85567-0afc-4854-b3d3-3746dd1a37f2)

I've not bothered to extract this one to my own `tools.simonwillison.net` site yet because it's purely a proof of concept that Pyodide can load correctly in that environment.

#### Photo Camera Settings Simulator

I was out on a photo walk and got curious about whether or not JavaScript could provide a simulation of camera settings. I didn't get very far with this one (prompting on my phone while walking along the beach) \- the result was buggy and unimpressive and I quickly lost interest. It did expose me to the [Fabric.js](http://fabricjs.com/) library for manipulating canvas elements though.

[![Photo Camera Settings Simulator. An image has been selected - but only the corner of the image displays with some buggy broken resize handles. Three sliders at the bottom show Exposure, Contrast and SAturation.](https://substackcdn.com/image/fetch/$s_!fHrt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2c609d32-aa75-4aad-aa07-b6cc622e6722_1322x1168.jpeg "Photo Camera Settings Simulator. An image has been selected - but only the corner of the image displays with some buggy broken resize handles. Three sliders at the bottom show Exposure, Contrast and SAturation.")](https://substackcdn.com/image/fetch/$s_!fHrt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2c609d32-aa75-4aad-aa07-b6cc622e6722_1322x1168.jpeg)

[https://claude.site/artifacts/e645c231\-8c13\-4374\-bb7d\-271c8dd73825](https://claude.site/artifacts/e645c231-8c13-4374-bb7d-271c8dd73825)

#### LLM pricing calculator

This one I *did* finish. I built this pricing calculator as part of my experiments with [Video scraping using Google Gemini](https://simonwillison.net/2024/Oct/17/video-scraping/), because I didn't trust my own calculations for how inexpensive Gemini was! Here are [detailed notes](https://simonwillison.net/2024/Oct/17/video-scraping/#bonus-calculator) on how I built that.

[![Screenshot of LLM Pricing Calculator interface. Left panel: input fields for tokens and costs. Input Tokens: 11018, Output Tokens: empty, Cost per Million Input Tokens: $0.075, Cost per Million Output Tokens: $0.3. Total Cost calculated: $0.000826 or 0.0826 cents. Right panel: Presets for various models including Gemini, Claude, and GPT versions with their respective input/output costs per 1M tokens. Footer: Prices were correct as of 16th October 2024, they may have changed.](https://substackcdn.com/image/fetch/$s_!WN3S!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7fe8a4c1-fa6e-4f5b-9663-2207a8fba625_2058x1364.jpeg "Screenshot of LLM Pricing Calculator interface. Left panel: input fields for tokens and costs. Input Tokens: 11018, Output Tokens: empty, Cost per Million Input Tokens: $0.075, Cost per Million Output Tokens: $0.3. Total Cost calculated: $0.000826 or 0.0826 cents. Right panel: Presets for various models including Gemini, Claude, and GPT versions with their respective input/output costs per 1M tokens. Footer: Prices were correct as of 16th October 2024, they may have changed.")](https://substackcdn.com/image/fetch/$s_!WN3S!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7fe8a4c1-fa6e-4f5b-9663-2207a8fba625_2058x1364.jpeg)

[https://tools.simonwillison.net/llm\-prices](https://tools.simonwillison.net/llm-prices)

#### YAML to JSON converter

I wanted to remind myself how certain aspects of YAML syntax worked, so I span up a quick YAML to JSON converter tool that shows the equivalent JSON live as you type YAML.

[![YAML to JSON converter. In the top textarea is YAML. Below it is pretty-printed JSON output.](https://substackcdn.com/image/fetch/$s_!F9wB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcb4c2cac-e262-4d1d-a44b-178a1a350e31_1322x1308.jpeg "YAML to JSON converter. In the top textarea is YAML. Below it is pretty-printed JSON output.")](https://substackcdn.com/image/fetch/$s_!F9wB!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcb4c2cac-e262-4d1d-a44b-178a1a350e31_1322x1308.jpeg)

[https://claude.site/artifacts/ffeb439c\-fc95\-428a\-9224\-434f5f968d51](https://claude.site/artifacts/ffeb439c-fc95-428a-9224-434f5f968d51)

#### OpenAI Audio

This is my most interesting artifact of the week. I was exploring OpenAI's new Audio APIs and decided to see if I could get Claude to build we a web page that could request access to my microphone, record a snippet of audio, then base64 encoded that and send it to the OpenAI API.

Here are [the full details on how I built this tool](https://simonwillison.net/2024/Oct/18/openai-audio/).

[![Screenshot of the OpenAI Audio tool. A start recording button is visible, and a 00:00 timer, and a playback audio element. There is a textarea for a prompt and a Submit to API button.](https://substackcdn.com/image/fetch/$s_!5_8e!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F274a21b3-66c0-4c25-9019-c7b71d61bf7e_1023x639.jpeg "Screenshot of the OpenAI Audio tool. A start recording button is visible, and a 00:00 timer, and a playback audio element. There is a textarea for a prompt and a Submit to API button.")](https://substackcdn.com/image/fetch/$s_!5_8e!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F274a21b3-66c0-4c25-9019-c7b71d61bf7e_1023x639.jpeg)

[https://tools.simonwillison.net/openai\-audio](https://tools.simonwillison.net/openai-audio)

Claude Artifacts can't make API requests to external hosts directly, but it can still spin up enough of a working version that it's easy to take that, move it to different hosting and finish getting it working.

I wrote more about this API pattern in [Building a tool showing how Gemini Pro can return bounding boxes for objects in images](https://simonwillison.net/2024/Aug/26/gemini-bounding-box-visualization/).

#### QR Code Decoder

I was in a meeting earlier this week where one of the participants shared a slide with a QR code (for joining a live survey tool). I didn't have my phone with me, so I needed a way to turn that QR code into a regular URL.

[![QR Code Decoder

Uses jsQR by Cosmo Wolfe

Upload, drag and drop, or paste a QR code image:
Select a file or drag and drop here

I drag on a QR code and the box says:

Decoded content: https://simonwillison.net/](https://substackcdn.com/image/fetch/$s_!VuBT!,w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F80e55f5c-25a2-41df-98ba-b2bd897d8116_507x315.gif "QR Code Decoder

Uses jsQR by Cosmo Wolfe

Upload, drag and drop, or paste a QR code image:
Select a file or drag and drop here

I drag on a QR code and the box says:

Decoded content: https://simonwillison.net/")](https://substackcdn.com/image/fetch/$s_!VuBT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F80e55f5c-25a2-41df-98ba-b2bd897d8116_507x315.gif)

<https://tools.simonwillison.net/qr>

Knocking up this QR decoder in Claude Artifacts took just a few seconds:

> `Build an artifact (no react) that lets me paste in a QR code and displays the decoded information, with a hyperlink if necessary`

\[ ... ]

> `have a file open box that also lets you drag and drop and add a onpaste handler to the page that catches pasted images as well`

[Full conversation here](https://gist.github.com/simonw/c2b0c42cd1541d6ed6bfe5c17d638039).

#### Image Converter and Page Downloader

Another very quick prototype. On Hacker News someone demonstrated a neat idea for a tool that let you drop photos onto a page and it would bake them into the page as base64 URLs such that you could "save as HTML" and get a self\-contained page with a gallery.

I [suggested they could add](https://news.ycombinator.com/item?id=41876750#41880857) a feature that generated a "Download link" with the new page baked in \- useful on mobile phones that don't let you "Save as HTML" \- and got Claude to knock up a quick prototype:

[![Image converter and page downloader - I've selected an image and there is now a Download Page link below that image.](https://substackcdn.com/image/fetch/$s_!cPtE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6c7c2340-ffb5-4ebc-a592-8c16ee939798_1322x933.jpeg "Image converter and page downloader - I've selected an image and there is now a Download Page link below that image.")](https://substackcdn.com/image/fetch/$s_!cPtE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6c7c2340-ffb5-4ebc-a592-8c16ee939798_1322x933.jpeg)

In this case I shared the code in [a Gist](https://gist.github.com/egeozcan/b27e11a7e776972d18603222fa523ed4) and then used the new\-to\-me

https://gistpreview.github.io/?GIST\_ID\_GOES\_HERE

trick to render the result:

https://gistpreview.github.io/?14a2c3ef508839f26377707dbf5dd329

[gistpreview](https://github.com/gistpreview/gistpreview.github.io) turns out to be a really quick way to turn a LLM\-generated demo into a page people can view.

[Code](https://gist.github.com/egeozcan/b27e11a7e776972d18603222fa523ed4), [Claude transcript](https://gist.github.com/simonw/7026fe5051ba138eb15ef82f4936eaed)

#### HTML Entity Escaper

Another example of on\-demand software: I needed to escape the HTML entities in a chunk of text on my phone, so I got Claude to build me a tool for that:

[![HTML entity escaper. In the input box I have typed in text with some double quotes. The output box has those correctly escaped, and a copy to clipboard button.](https://substackcdn.com/image/fetch/$s_!PdHk!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F587be305-88d8-46ea-bc64-efba32233140_1322x1099.jpeg "HTML entity escaper. In the input box I have typed in text with some double quotes. The output box has those correctly escaped, and a copy to clipboard button.")](https://substackcdn.com/image/fetch/$s_!PdHk!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F587be305-88d8-46ea-bc64-efba32233140_1322x1099.jpeg)

[https://claude.site/artifacts/46897436\-e06e\-4ccc\-b8f4\-3df90c47f9bc](https://claude.site/artifacts/46897436-e06e-4ccc-b8f4-3df90c47f9bc)

Here's the prompt I used:

> `Build an artifact (no react) where I can paste text into a textarea and it will return that text with all HTML entities - single and double quotes and less than greater than ampersand - correctly escaped. The output should be in a textarea accompanied by a "Copy to clipboard" button which changes text to "Copied!" for 1.5s after you click it. Make it mobile friendly`

#### text\-wrap\-balance\-nav

Inspired by [Terence Eden](https://shkspr.mobi/blog/2024/10/you-can-use-text-wrap-balance-on-icons/) I decided to do a quick experiment with the `text-wrap: balance` CSS property. I got Claude to build me an example nav bar with a slider and a checkbox. I [wrote about that here](https://simonwillison.net/2024/Oct/20/you-can-use-text-wrap-balance-on-icons/).

[![Animated demo. A navigation menu with 13 items - things like Home and About and Services and a products. These are wrapped on four lines with 4, 4, 4 and then 1 item. Selecting the enable text-wrap: balances checkbox changes that to 3, 4, 3, 3 - a slider also allows the number of visible items to be changed to see the effect that has](https://substackcdn.com/image/fetch/$s_!E6jM!,w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f0062c1-e474-4d9d-b506-6e4f2f2e0fcc_419x275.gif "Animated demo. A navigation menu with 13 items - things like Home and About and Services and a products. These are wrapped on four lines with 4, 4, 4 and then 1 item. Selecting the enable text-wrap: balances checkbox changes that to 3, 4, 3, 3 - a slider also allows the number of visible items to be changed to see the effect that has")](https://substackcdn.com/image/fetch/$s_!E6jM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f0062c1-e474-4d9d-b506-6e4f2f2e0fcc_419x275.gif)

[https://tools.simonwillison.net/text\-wrap\-balance\-nav](https://tools.simonwillison.net/text-wrap-balance-nav)

#### ARES Phonetic Alphabet Converter

I was volunteering as a HAM radio communications operator for [the Half Moon Bay Pumpkin Run](https://hmbpumpkinfest.com/featured-exhibits/great-pumpkin-run.html) and got nervous that I'd mess up using the phonetic alphabet \- so I had Claude build me this tool:

[![ARES PHonetic Alphabet Converter. I have entered the text Cleo is a lobster. After clicking the Convert button I get the output Charlie Lima Echo Oscar (Space) India Sierra (Space) Alpha (Space) Lima Oscar Sierra Tango Echo Romeo](https://substackcdn.com/image/fetch/$s_!P892!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F100c75f6-1941-4f99-8826-1094df103b68_1322x887.jpeg "ARES PHonetic Alphabet Converter. I have entered the text Cleo is a lobster. After clicking the Convert button I get the output Charlie Lima Echo Oscar (Space) India Sierra (Space) Alpha (Space) Lima Oscar Sierra Tango Echo Romeo")](https://substackcdn.com/image/fetch/$s_!P892!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F100c75f6-1941-4f99-8826-1094df103b68_1322x887.jpeg)

[https://claude.site/artifacts/aaadab20\-968a\-4291\-8ce9\-6435f6d53f4c](https://claude.site/artifacts/aaadab20-968a-4291-8ce9-6435f6d53f4c)

[Claude transcript here](https://gist.github.com/simonw/6ad4133c93e22df4c0ce731fdd7a2a91). Amusingly it built it in Python first, then switched to JavaScript after I reminded it that I wanted "an interactive web app".

#### This is so useful, and so much fun!

As you can see, I'm a *heavy* user of this feature \- I just described 14 projects produced in a single week. I've been using artifacts since they were released [on 20th June](https://simonwillison.net/2024/Jun/20/claude-35-sonnet/) (alongside the excellent Claude 3\.5 Sonnet, still my daily\-driver LLM) and I'm now at a point where I fire up a new interactive artifact several times a day.

I'm using artifacts for idle curiosity, rapid prototyping, library research and to spin up tools that solve immediate problems.

Most of these tools took less than five minutes to build. A few of the more involved ones took longer than that, but even the OpenAI Audio one took [11:55am to 12:07pm](https://gist.github.com/simonw/0a4b826d6d32e4640d67c6319c7ec5ce) for the first version and [12:18pm to 12:27pm](https://gist.github.com/simonw/a04b844a5e8b01cecd28787ed375e738) for the second iteration \- so 21 minutes total.

Take a look at my [claude\-artifacts](https://simonwillison.net/tags/claude-artifacts/) tag for even more examples, including [SVG to JPG/PNG](https://simonwillison.net/2024/Oct/6/svg-to-jpg-png/), [Markdown and Math Live Renderer](https://simonwillison.net/2024/Sep/21/markdown-and-math-live-renderer/) and [Image resize and quality comparison](https://simonwillison.net/2024/Jul/26/image-resize-and-quality-comparison/).

I also have a [dashboard](https://simonwillison.net/2024/Oct/21/dashboard-tools/) of every post that links to my [tools.simonwillison.net](https://tools.simonwillison.net/) site, and the underlying [simonw/tools](https://github.com/simonw/tools) GitHub repo includes more unlisted tools, most of which link to their Claude conversation transcripts in their commit history.

I'm beginning to get a little frustrated at their limitations \- in particular the way artifacts are unable to make API calls, submit forms or even link out to other pages. I'll probably end up spinning up my own tiny artifacts alternative based on everything I've learned about them so far.

If you're *not* using artifacts, I hope I've given you a sense of why they're one of my current favourite LLM\-based tools.

---

### [Running Llama 3\.2 Vision and Phi\-3\.5 Vision on a Mac with mistral.rs](https://simonwillison.net/2024/Oct/19/mistralrs/) \- 2024\-10\-19

[mistral.rs](https://github.com/EricLBuehler/mistral.rs) is an LLM inference library written in Rust by Eric Buehler. Today I figured out how to use it to run the Llama 3\.2 Vision and Phi\-3\.5 Vision models on my Mac.

Despite the name, it's not just for the Mistral family of models \- like how `llama.cpp` has grown beyond Llama, `mistral.rs` has grown beyond Mistral.

I already have a Rust installation, so I checked out and compiled the library like this:

```
git clone https://github.com/EricLBuehler/mistral.rs.git
cd mistral.rs
cargo run --features metal --release -- -i --isq Q4K vision-plain -m lamm-mit/Cephalo-Llama-3.2-11B-Vision-Instruct-128k -a vllama

```

This downloaded around 20GB of model files to `~/.cache/huggingface/hub/models--lamm-mit--Cephalo-Llama-3.2-11B-Vision-Instruct-128k`, loaded the model into memory and started a terminal\-based chat session.

I ran this prompt:

`\image https://niche-museums.imgix.net/pioneer-history.jpeg?w=1600&h=800&fit=crop&auto=compress <|image|> describe this image including any text`

[![2024-10-19T15:38:18.142895Z  INFO mistralrs_server::interactive_mode: Starting interactive loop with sampling params: SamplingParams { temperature: Some(0.1), top_k: Some(32), top_p: Some(0.1), min_p: Some(0.05), top_n_logprobs: 0, frequency_penalty: Some(0.1), presence_penalty: Some(0.1), stop_toks: None, max_len: Some(4096), logits_bias: None, n_choices: 1, dry_params: Some(DrySamplingParams { sequence_breakers: ["\n", ":", "\"", "*"], multiplier: 0.0, base: 1.75, allowed_length: 2 }) }
====================
Welcome to interactive mode! Because this model is a vision model, you can enter prompts and chat with the model.

To specify a message with an image, use the `\image` command detailed below.

Commands:
- `\help`: Display this message.
- `\exit`: Quit interactive mode.
- `\system <system message here>`:
    Add a system message to the chat without running the model.
    Ex: `\system Always respond as a pirate.`
- `\image <image URL or local path here> <message here>`: 
    Add a message paired with an image. You are responsible for prefixing the message with anything the model
    requires.
    Ex: `\image path/to/image.jpg Describe what is in this image.`
====================
> 
> 
> \image https://niche-museums.imgix.net/pioneer-history.jpeg?w=1600&h=800&fit=crop&auto=compress <|image|> describe this image including any text
The image shows the exterior of the Daughters of Utah Pioneers (DUP) Museum, which is also known as the Pioneer Memorial Museum. The building is located in Salt Lake City, Utah, USA. 

Visible in the image are:

1. **The DUP Museum Building**: The main structure of the museum is a prominent feature in the image. It is a two-story building with a rectangular shape and a flat roof. The exterior walls are made of brick or stone, giving it a classic and historic appearance.
](https://substackcdn.com/image/fetch/$s_!8Shu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F41a1babc-cd39-4afa-b8f7-63d27f8495bb_1260x1037.jpeg "2024-10-19T15:38:18.142895Z  INFO mistralrs_server::interactive_mode: Starting interactive loop with sampling params: SamplingParams { temperature: Some(0.1), top_k: Some(32), top_p: Some(0.1), min_p: Some(0.05), top_n_logprobs: 0, frequency_penalty: Some(0.1), presence_penalty: Some(0.1), stop_toks: None, max_len: Some(4096), logits_bias: None, n_choices: 1, dry_params: Some(DrySamplingParams { sequence_breakers: [\"\n\", \":\", \"\\"\", \"*\"], multiplier: 0.0, base: 1.75, allowed_length: 2 }) }
====================
Welcome to interactive mode! Because this model is a vision model, you can enter prompts and chat with the model.

To specify a message with an image, use the `\image` command detailed below.

Commands:
- `\help`: Display this message.
- `\exit`: Quit interactive mode.
- `\system <system message here>`:
    Add a system message to the chat without running the model.
    Ex: `\system Always respond as a pirate.`
- `\image <image URL or local path here> <message here>`: 
    Add a message paired with an image. You are responsible for prefixing the message with anything the model
    requires.
    Ex: `\image path/to/image.jpg Describe what is in this image.`
====================
> 
> 
> \image https://niche-museums.imgix.net/pioneer-history.jpeg?w=1600&h=800&fit=crop&auto=compress <|image|> describe this image including any text
The image shows the exterior of the Daughters of Utah Pioneers (DUP) Museum, which is also known as the Pioneer Memorial Museum. The building is located in Salt Lake City, Utah, USA. 

Visible in the image are:

1. **The DUP Museum Building**: The main structure of the museum is a prominent feature in the image. It is a two-story building with a rectangular shape and a flat roof. The exterior walls are made of brick or stone, giving it a classic and historic appearance.
")](https://substackcdn.com/image/fetch/$s_!8Shu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F41a1babc-cd39-4afa-b8f7-63d27f8495bb_1260x1037.jpeg)

The prompt uses this image from my [Niche Museums write\-up of the Pioneer Memorial Museum](https://www.niche-museums.com/111):

[![Detailed image description follows](https://substackcdn.com/image/fetch/$s_!-pGf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1142e16d-5007-4c0e-8a4f-5453e9548713_1600x800.jpeg "Detailed image description follows")](https://substackcdn.com/image/fetch/$s_!-pGf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1142e16d-5007-4c0e-8a4f-5453e9548713_1600x800.jpeg)

I got back this response:

> The image shows the exterior of the Daughters of Utah Pioneers (DUP) Museum, which is also known as the Pioneer Memorial Museum. The building is located in Salt Lake City, Utah, USA.
> 
> Visible in the image are:
> 
> 1. **The DUP Museum Building**: The main structure of the museum is a prominent feature in the image. It is a two\-story building with a rectangular shape and a flat roof. The exterior walls are made of brick or stone, giving it a classic and historic appearance.
> 2. **Signage**: Above the entrance, there is a sign that reads "Daughters of Utah Pioneers Museum" in bold letters. Below this sign, another sign indicates that the building is also known as the "Pioneer Memorial Museum."
> 3. **Entrance**: The main entrance to the museum is marked by a doorway with a decorative frame and a pair of large wooden doors.
> 4. **Landscaping**: The surrounding area around the museum appears well\-maintained with neatly trimmed grass and some trees nearby.
> 5. **Statue or Monument**: In front of the museum, there is a small statue or monument that appears to be dedicated to pioneers or early settlers.
> 
> The Daughters of Utah Pioneers (DUP) Museum showcases historical artifacts and exhibits related to Utah's pioneer history, focusing on the experiences and contributions of early settlers in the region.

Note that the text it generates correctly describes the museum's content and identifies the museum as being located in Salt Lake City, neither of which are details that were displayed in the image itself.

Activity Monitor confirmed that this Metal build was using my GPU, and about 10GB of memory, while the prompt was running.

`mistral.rs` also provides [a Python binding](https://github.com/EricLBuehler/mistral.rs/blob/master/mistralrs-pyo3/README.md), which can be installed from PyPI but requires a Rust toolchain (I filed an issue [requesting PyPI wheels](https://github.com/EricLBuehler/mistral.rs/issues/864)):

```
pip install mistralrs-metal

```

I got an error running the [Python Llama vision demo](https://github.com/EricLBuehler/mistral.rs/blob/v0.3.1/examples/python/llama_vision.py) but the [Phi 3\.5 Vision example](https://github.com/EricLBuehler/mistral.rs/blob/v0.3.1/examples/python/phi3v.py) worked as advertised. I modified that to enable streaming output and ran it against a photograph from [Mendenhall's Museum of Gasoline Pumps \& Petroliana](https://www.niche-museums.com/107):

```
from mistralrs import Runner, Which, ChatCompletionRequest, VisionArchitecture

res = runner.send_chat_completion_request(
    ChatCompletionRequest(
        model="phi3v",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "https://niche-museums.imgix.net/mendenhalls-16.jpeg?w=1200&auto=compress"
                        },
                    },
                    {
                        "type": "text",
                        "text": "<|image_1|>\nWhat is shown in this image? Write a detailed response analyzing the scene.",
                    },
                ],
            }
        ],
        max_tokens=1024,
        presence_penalty=1.0,
        top_p=0.1,
        temperature=0.1,
        stream=True,
    )
)
for item in res:
    print(item.choices[0].delta.content, end='')
```

[![Description follows](https://substackcdn.com/image/fetch/$s_!tQ-Q!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F63b70117-1f38-440f-bc0f-0cffd6e457c3_1200x900.jpeg "Description follows")](https://substackcdn.com/image/fetch/$s_!tQ-Q!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F63b70117-1f38-440f-bc0f-0cffd6e457c3_1200x900.jpeg)

Here's what It gave me:

> The image captures a nostalgic scene of a vintage gas station, reminiscent of a bygone era. Dominating the left side of the frame is a red and white gas pump, standing tall and proud, its metallic surface gleaming under the soft light filtering through the wooden ceiling. Adjacent to it, a white and black gas canister stands ready for service, its presence adding to the authenticity of the setting.
> 
> On the right, a red and white gasoline sign hangs from the ceiling, its bold colors contrasting with the muted tones of the surroundings. Above it, a yellow and white gasoline sign is suspended, its vibrant hues drawing the eye upwards.
> 
> The floor beneath these relics of the past is a checkerboard pattern, a common design choice for gas stations of yesteryears. It provides a stark contrast to the smooth, unblemished surfaces of the gas pumps and canisters.
> 
> In the background, a variety of other signs and advertisements add to the eclectic mix of objects. They are a testament to the diverse range of products and services that were once available at this location.
> 
> Despite the passage of time, the gas station retains a certain charm, its vintage gas pumps and signs serving as a tangible link to a different era. The image is a snapshot of history, frozen in time, waiting to be discovered and appreciated by those who take the time to look closer.

This description looks fantastic at first glance, but if you review it carefully and compare it to the image you'll see that it's full of inaccuracies. The vibes of the description match the image but the actual details are definitely incorrect.

This model downloaded 7\.7GB to `~/.cache/huggingface/hub/models--microsoft--Phi-3.5-vision-instruct` \- significantly smaller than Llama 3\.2's 20GB. I wonder if that size difference helps explain the greater hallucination rate in Phi\-3\.5 Vision.

If you're running Python 3\.10 on Apple Silicon you may be able to skip the Rust compiler by installing the wheel I built here:

```
pip install https://static.simonwillison.net/static/2024/mistralrs_metal-0.3.1-cp310-cp310-macosx_11_0_arm64.whl

```

---

**Link** 2024\-10\-20 [You can use text\-wrap: balance; on icons](https://shkspr.mobi/blog/2024/10/you-can-use-text-wrap-balance-on-icons/):

Neat CSS experiment from Terence Eden: the new [text\-wrap: balance](https://developer.mozilla.org/en-US/docs/Web/CSS/text-wrap#balance) CSS property is intended to help make text like headlines display without ugly wrapped single orphan words, but Terence points out it can be used for icons too:

[![A row of icons, without text-wrap balances just one is wrapped on the second line. With the propert they are split into two lines with equal numbers of icons.](https://substackcdn.com/image/fetch/$s_!h6oL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9f73b669-c4f8-4084-b83f-c6804c905f65_1412x812.jpeg "A row of icons, without text-wrap balances just one is wrapped on the second line. With the propert they are split into two lines with equal numbers of icons.")](https://substackcdn.com/image/fetch/$s_!h6oL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9f73b669-c4f8-4084-b83f-c6804c905f65_1412x812.jpeg)

This inspired me to investigate if the same technique could work for text based navigation elements. I [used Claude](https://gist.github.com/simonw/53648554917862676ccd12dcf5cc9cab) to build [this interactive prototype](https://tools.simonwillison.net/text-wrap-balance-nav) of a navigation bar that uses `text-wrap: balance` against a list of `display: inline` menu list items. It seems to work well!

[![Animated demo. A navigation menu with 13 items - things like Home and About and Services and a products. These are wrapped on four lines with 4, 4, 4 and then 1 item. Selecting the enable text-wrap: balances checkbox changes that to 3, 4, 3, 3 - a slider also allows the number of visible items to be changed to see the effect that has](https://substackcdn.com/image/fetch/$s_!E6jM!,w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f0062c1-e474-4d9d-b506-6e4f2f2e0fcc_419x275.gif "Animated demo. A navigation menu with 13 items - things like Home and About and Services and a products. These are wrapped on four lines with 4, 4, 4 and then 1 item. Selecting the enable text-wrap: balances checkbox changes that to 3, 4, 3, 3 - a slider also allows the number of visible items to be changed to see the effect that has")](https://substackcdn.com/image/fetch/$s_!E6jM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f0062c1-e474-4d9d-b506-6e4f2f2e0fcc_419x275.gif)

My first attempt used `display: inline-block` which worked in Safari but failed in Firefox.

Notable limitation from [that MDN article](https://developer.mozilla.org/en-US/docs/Web/CSS/text-wrap#balance):

> Because counting characters and balancing them across multiple lines is computationally expensive, this value is only supported for blocks of text spanning a limited number of lines (six or less for Chromium and ten or less for Firefox)

So it's fine for these navigation concepts but isn't something you can use for body text.

---

**Quote** 2024\-10\-20

> *It feels like we’re at a bit of an inflection point for the Django community. \[...] One of the places someone could have the most impact is by serving on the DSF Board. Like the community at large, the DSF is at a transition point: we’re outgrowing the “small nonprofit” status, and have the opportunity to really expand our ambition and reach. In all likelihood, the decisions the Board makes over the next year or two will define our direction and strategy for the next decade.*

[Jacob Kaplan\-Moss](https://jacobian.org/2024/oct/18/dsf-board-2025/)

---

**Quote** 2024\-10\-20

> *Who called it “intellectual property problems around the acquisition of training data for Large Language Models” and not Grand Theft Autocomplete?*

[Jens Ohlig](https://mastodon.xyz/@johl/112059833912513751)

---

**Link** 2024\-10\-20 [The 3 AI Use Cases: Gods, Interns, and Cogs](https://www.dbreunig.com/2024/10/18/the-3-ai-use-cases-gods-interns-and-cogs.html):

Drew Breunig introduces an interesting new framework for categorizing use cases of modern AI:

* **Gods** refers to the autonomous, human replacement applications \- I see that as AGI stuff that's still effectively science fiction.
* **Interns** are supervised copilots. This is how I get most of the value out of LLMs at the moment, delegating tasks to them that I can then review, such as [AI\-assisted programming](https://simonwillison.net/tags/ai-assisted-programming/).
* **Cogs** are the smaller, more reliable components that you can build pipelines and automations on top of without needing to review everything they do \- think Whisper for transcriptions or maybe some limited LLM subtasks such as structured data extraction.

Drew also considers **Toys** as a subcategory of Interns: things like image generators, “defined by their usage by non\-experts. Toys have a high tolerance for errors because they’re not being relied on for much beyond entertainment.”

---

**Quote** 2024\-10\-20

> *I really dislike the practice of replacing passwords with email “magic links”. Autofilling a password from my keychain happens instantly; getting a magic link from email can take minutes sometimes, and even in the fastest case, it’s nowhere near instantaneous. Replacing something very fast — password autofill — with something slower is just a terrible idea.*

[John Gruber](https://daringfireball.net/linked/2024/10/17/dhh-argues-against-passkeys)

---

**Link** 2024\-10\-20 [Knowledge Worker](https://newsletter.goodtechthings.com/p/knowledge-worker):

Forrest Brazeal:

> Last month, I performed a 30\-minute show called "Knowledge Worker" for the incredible audience at Gene Kim's ETLS in Las Vegas.
> 
> The show included 7 songs about the past, present, and future of "knowledge work" \- or, more specifically, how it's affecting *us,* the humans between keyboard and chair*.* I poured everything I've been thinking and feeling about AI for the last 2\+ years into this show, and I feel a great sense of peace at having said what I meant to say.

Videos of all seven songs are included in the post, with accompanying liner notes. [AGI (Artificial God Incarnate)](https://www.youtube.com/watch?v=1ZhhO7MGknQ) is a *banger*, and [What’s Left for Me? (The AI Existential Crisis Song)](https://www.youtube.com/watch?v=hrfEUZ0UvRo) captures something I've been trying to think through for a while.

---

**Link** 2024\-10\-21 [Dashboard: Tools](https://simonwillison.net/dashboard/tools/):

I used [Django SQL Dashboard](https://django-sql-dashboard.datasette.io/) to spin up a dashboard that shows all of the URLs to my [tools.simonwillison.net](https://tools.simonwillison.net/) site that I've shared on my blog so far. It uses this (Claude assisted) regular expression in a PostgreSQL SQL query:

```
select distinct on (tool_url)
    unnest(regexp_matches(
        body,
        '(
```

https://tools

```
.simonwillison.net/[^<"\s)]+)',
        'g'
    )) as tool_url,
    '
```

https://simonwillison.net/

```
' || left(type, 1) || '/' || id as blog_url,
    title,
    date(created) as created
from content
```

I've been really enjoying having a static hosting platform (it's GitHub Pages serving my [simonw/tools](https://github.com/simonw/tools) repo) that I can use to quickly deploy little HTML\+JavaScript interactive tools and demos.

---

**Quote** 2024\-10\-21

> *I've often been building single\-use apps with Claude Artifacts when I'm helping my children learn. For example here's one on [visualizing fractions](https://claude.site/artifacts/e9670602-027a-49f8-aa4f-9ef405d761eb). \[...] What's more surprising is that it is far easier to create an app on\-demand than searching for an app in the app store that will do what I'm looking for. Searching for kids' learning apps is typically a nails\-on\-chalkboard painful experience because 95% of them are addictive garbage. And even if I find something usable, it can't match the fact that I can tell Claude what I want.*

[Arvind Narayanan](https://twitter.com/random_walker/status/1848388462782673340)

---

**Link** 2024\-10\-21 [sudoku\-in\-python\-packaging](https://github.com/konstin/sudoku-in-python-packaging):

Absurdly clever hack by [konsti](https://github.com/konstin): solve a Sudoku puzzle entirely using the Python package resolver!

First convert the puzzle into a `requirements.in` file representing the current state of the board:

```
git clone https://github.com/konstin/sudoku-in-python-packaging
cd sudoku-in-python-packaging
echo '5,3,_,_,7,_,_,_,_                                        
6,_,_,1,9,5,_,_,_
_,9,8,_,_,_,_,6,_
8,_,_,_,6,_,_,_,3
4,_,_,8,_,3,_,_,1
7,_,_,_,2,_,_,_,6
_,6,_,_,_,_,2,8,_
_,_,_,4,1,9,_,_,5
_,_,_,_,8,_,_,7,9' > sudoku.csv
python csv_to_requirements.py sudoku.csv requirements.in

```

That `requirements.in` file now contains lines like this for each of the filled\-in cells:

```
sudoku_0_0 == 5
sudoku_1_0 == 3
sudoku_4_0 == 7

```

Then run `uv pip compile` to convert that into a fully fleshed out `requirements.txt` file that includes all of the resolved dependencies, based on the wheel files in the [packages/](https://github.com/konstin/sudoku-in-python-packaging/tree/main/packages) folder:

```
uv pip compile \
  --find-links packages/ \
  --no-annotate \
  --no-header \
  requirements.in > requirements.txt

```

The contents of `requirements.txt` is now the fully solved board:

```
sudoku-0-0==5
sudoku-0-1==6
sudoku-0-2==1
sudoku-0-3==8
...

```

The trick is the 729 wheel files in `packages/` \- each with a name like `sudoku_3_4-8-py3-none-any.whl`. I decompressed that wheel and it included a `sudoku_3_4-8.dist-info/METADATA` file which started like this:

```
Name: sudoku_3_4
Version: 8
Metadata-Version: 2.2
Requires-Dist: sudoku_3_0 != 8
Requires-Dist: sudoku_3_1 != 8
Requires-Dist: sudoku_3_2 != 8
Requires-Dist: sudoku_3_3 != 8
...

```

With a `!=8` line for every other cell on the board that cannot contain the number 8 due to the rules of Sudoku (if 8 is in the 3, 4 spot). Visualized:

[![Sudoku grid partially filled. Number 8 in center. X's fill entire row and column containing 8, as well as the 3x3 box containing 8. Additional X's in center column above and below 8's box.](https://substackcdn.com/image/fetch/$s_!FWQi!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9aa2fa63-e1a9-4111-9201-f2161373409b_672x652.jpeg "Sudoku grid partially filled. Number 8 in center. X's fill entire row and column containing 8, as well as the 3x3 box containing 8. Additional X's in center column above and below 8's box.")](https://substackcdn.com/image/fetch/$s_!FWQi!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9aa2fa63-e1a9-4111-9201-f2161373409b_672x652.jpeg)

So the trick here is that the Python dependency resolver (now lightning fast thanks to [uv](https://docs.astral.sh/uv/)) reads those dependencies and rules out every package version that represents a number in an invalid position. The resulting version numbers represent the cell numbers for the solution.

---