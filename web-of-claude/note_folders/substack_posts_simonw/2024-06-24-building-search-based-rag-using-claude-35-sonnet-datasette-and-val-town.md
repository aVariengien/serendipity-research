# Building search-based RAG using Claude 3.5 Sonnet, Datasette and Val Town

*The new Claude 3.5 Sonnet is now the best available LLM*

Published: 2024-06-24
Source: https://simonw.substack.com/p/building-search-based-rag-using-claude

---

In this newsletter:

* Building search\-based RAG using Claude, Datasette and Val Town

Plus 8 links and 7 quotations and 1 TIL

### **[Building search\-based RAG using Claude, Datasette and Val Town](https://simonwillison.net/2024/Jun/21/search-based-rag/) \- 2024\-06\-21**

Retrieval Augmented Generation (RAG) is a technique for adding extra "knowledge" to systems built on LLMs, allowing them to answer questions against custom information not included in their training data. A common way to implement this is to take a question from a user, translate that into a set of search queries, run those against a search engine and then feed the results back into the LLM to generate an answer.

I built a basic version of this pattern against the brand new [Claude 3\.5 Sonnet](https://simonwillison.net/2024/Jun/20/claude-35-sonnet/) language model, using [SQLite full\-text search](https://www.sqlite.org/fts5.html) running in [Datasette](https://datasette.io/) as the search backend and [Val Town](https://www.val.town/)as the prototyping platform.

The implementation took just over an hour, during a live coding session with Val.Town founder Steve Krouse. I was the latest guest on Steve's [live streaming series](https://www.youtube.com/@ValDotTown/videos?view=2&sort=dd&live_view=503&shelf_id=2) where he invites people to hack on projects with his help.

You can watch the video below or [on YouTube](https://www.youtube.com/watch?v=9pmC3P1fUFo). Here are my own detailed notes to accompany the session.

#### **Bonus: Claude 3\.5 Sonnet artifacts demo**

We started the stream by chatting a bit about the new Claude 3\.5 Sonnet release. This turned into an unplanned demo of their "artifacts" feature where Claude can now build you an interactive web page on\-demand.

[![Screenshot of the Claude AI interface showing an interactive Mandelbrot fractal explorer and the prompts used to create it](https://substackcdn.com/image/fetch/$s_!UIep!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F74ccb99a-9d10-4cbc-bb86-45a64264f880_1280x720.jpeg "Screenshot of the Claude AI interface showing an interactive Mandelbrot fractal explorer and the prompts used to create it")](https://substackcdn.com/image/fetch/$s_!UIep!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F74ccb99a-9d10-4cbc-bb86-45a64264f880_1280x720.jpeg)

At [3m02s](https://www.youtube.com/watch?v=9pmC3P1fUFo&t=3m02s) I prompted it with:

> Build me a web app that teaches me about mandelbrot fractals, with interactive widgets

This worked! Here's [the code it wrote](https://gist.github.com/simonw/e57932549e47db2e45f1f75742b078f1) \- I haven't yet found a good path for turning that into a self\-hosted interactive page yet.

This didn't support panning, so I added:

> Again but let me drag on the canvas element to pan around

Which [gave me this](https://gist.github.com/simonw/76ef926312093333b48093da6def59fc). Pretty impressive!

[![Animated demo of Mandelbrot Fractor Explorer - I can slide the zoom and max iterations sliders and pan around by dragging my mouse on the canvas](https://substackcdn.com/image/fetch/$s_!chmH!,w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fef0fd7aa-10bb-479a-b16d-009cf8f95fc9_771x561.gif "Animated demo of Mandelbrot Fractor Explorer - I can slide the zoom and max iterations sliders and pan around by dragging my mouse on the canvas")](https://substackcdn.com/image/fetch/$s_!chmH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fef0fd7aa-10bb-479a-b16d-009cf8f95fc9_771x561.gif)

#### **Ingredients for the RAG project**

RAG is often implemented using [vector search against embeddings](https://simonwillison.net/2023/Oct/23/embeddings/#answering-questions-with-retrieval-augmented-generation), but there's an alternative approach where you turn the user's question into some full\-text search queries, run those against a traditional search engine, then feed the results back into an LLM and ask it to use them to answer the question.

SQLite includes [surprisingly good full\-text search](https://www.sqlite.org/fts5.html), and I've built a lot of tools against that in the past \- including [sqlite\-utils enable\-fts](https://sqlite-utils.datasette.io/en/stable/cli.html#configuring-full-text-search) and [Datasette's FTS features](https://docs.datasette.io/en/latest/full_text_search.html).

My blog has a lot of content, which lives in a Django PostgreSQL database. But I also have a GitHub Actions repository which [backs up that data](https://github.com/simonw/simonwillisonblog-backup/blob/main/.github/workflows/backup.yml) as JSON, and then publishes a SQLite copy of it to [datasette.simonwillison.net](https://datasette.simonwillison.net/) \- which means I have a Datasette\-powered JSON API for running searches against my content.

Let's use that API to build a question answering RAG system!

[![Screenshot of Datasette interface running a search with a custom SQL query for ruby on rails](https://substackcdn.com/image/fetch/$s_!DfLL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4bec878a-0774-4d2b-b4fd-40ef78a89ee8_1280x720.jpeg "Screenshot of Datasette interface running a search with a custom SQL query for ruby on rails")](https://substackcdn.com/image/fetch/$s_!DfLL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4bec878a-0774-4d2b-b4fd-40ef78a89ee8_1280x720.jpeg)

Step one then was to prototype up a SQL query we could use with that API to get back search results. After some iteration I got to this:

```
select
  blog_entry.id,
  blog_entry.title,
  blog_entry.body,
  blog_entry.created
from
  blog_entry
  join blog_entry_fts on blog_entry_fts.rowid = blog_entry.rowid
where
  blog_entry_fts match :search
order by
  rank
limit
  10
```

[Try that here](https://datasette.simonwillison.net/simonwillisonblog?sql=select%0D%0A++blog_entry.id%2C%0D%0A++blog_entry.title%2C%0D%0A++blog_entry.body%2C%0D%0A++blog_entry.created%0D%0Afrom%0D%0A++blog_entry%0D%0A++join+blog_entry_fts+on+blog_entry_fts.rowid+%3D+blog_entry.rowid%0D%0Awhere%0D%0A++blog_entry_fts+match+%3Asearch%0D%0Aorder+by%0D%0A++rank%0D%0Alimit%0D%0A++10&search=%22shot-scraper%22+OR+%22screenshot%22+OR+%22web%22+OR+%22tool%22+OR+%22automation%22+OR+%22CLI%22). The query works by joining the `blog_entry` table to the SQLite FTS `blog_entry_fts` virtual table, matched against the `?search=` parameter from the URL.

When you join against a FTS table like this a `rank` column is exposed with the relevance score for each match.

Adding `.json` to the above URL turns it into an API call... so now we have a search API we can call from other code.

#### **A plan for the build**

We spent the rest of the session writing code in Val Town, which offers a browser editor for a server\-side Deno\-based environment for executing JavaScript (and TypeScript) code.

The finished code does the following:

1. Accepts a user's question from the `?question=` query string.
2. Asks Claude 3\.5 Sonnet to turn that question into multiple single\-word search queries, using a Claude function call to enforce a schema of a JSON list of strings.
3. Turns that list of keywords into a SQLite FTS query that looks like this: `"shot-scraper" OR "screenshot" OR "web" OR "tool" OR "automation" OR "CLI"`
4. Runs that query against Datasette to get back the top 10 results.
5. Combines the title and body from each of those results into a longer context.
6. Calls Claude 3 again (originally Haiku, but then we upgraded to 3\.5 Sonnet towards the end) with that context and ask it to answer the question.
7. Return the results to the user.

#### **The annotated final script**

Here's the final script we ended up with, with inline commentary. Here's the initial setup:

```
import Anthropic from "npm:@anthropic-ai/sdk@0.24.0";

/* This automatically picks up the API key from the ANTHROPIC_API_KEY
environment variable, which we configured in the Val Town settings */
const anthropic = new Anthropic();
```

We're using the very latest release of the [Anthropic TypeScript SDK](https://github.com/anthropics/anthropic-sdk-typescript), which came out just [a few hours prior](https://github.com/anthropics/anthropic-sdk-typescript/commits/sdk-v0.24.0/) to recording the livestream.

I set the `ANTHROPIC_API_KEY` environment variable to my Claude 3 API key in the Val Town settings, making it available to all of my Vals. The `Anthropic()` constructor picks that up automatically.

Next, the function to suggest keywords for a user's question:

```
async function suggestKeywords(question) {
  // Takes a question like "What is shot-scraper?" and asks 3.5 Sonnet
  // to suggest individual search keywords to help answer the question.
  const message = await anthropic.messages.create({
    max_tokens: 128,
    model: "claude-3-5-sonnet-20240620",
    // The tools option enforces a JSON schema array of strings
    tools: [{
      name: "suggested_search_keywords",
      description: "Suggest individual search keywords to help answer the question.",
      input_schema: {
        type: "object",
        properties: {
          keywords: {
            type: "array",
            items: {
              type: "string",
            },
            description: "List of suggested single word search keywords",
          },
        },
        required: ["keywords"],
      },
    }],
    // This forces it to always run the suggested_search_keywords tool
    tool_choice: { type: "tool", name: "suggested_search_keywords" },
    messages: [
      { role: "user", content: question },
    ],
  });
  // This helped TypeScript complain less about accessing .input.keywords
  // since it knows this object can be one of two different types
  if (message.content[0].type == "text") {
    throw new Error(message.content[0].text);
  }
  return message.content[0].input.keywords;
}
```

We're asking Claude 3\.5 Sonnet here to suggest individual search keywords to help answer that question. I tried Claude 3 Haiku first but it didn't reliably return single word keywords \- Sonnet 3\.5 followed the "single word search keywords" instruction better.

This function also uses Claude tools to enforce a response in a JSON schema that specifies an array of strings. More on how I wrote that code (with Claude's assistance) later on.

Next, the code to run the search itself against Datasette:

```
// The SQL query from earlier
const sql = `select
  blog_entry.id,
  blog_entry.title,
  blog_entry.body,
  blog_entry.created
from
  blog_entry
  join blog_entry_fts on blog_entry_fts.rowid = blog_entry.rowid
where
  blog_entry_fts match :search
order by
  rank
limit
  10`;

async function runSearch(keywords) {
  // Turn the keywords into "word1" OR "word2" OR "word3"
  const search = keywords.map(s => `"${s}"`).join(" OR ");
  // Compose the JSON API URL to run the query
  const params = new URLSearchParams({
    search,
    sql,
    _shape: "array",
  });
  const url = "https://datasette.simonwillison.net/simonwillisonblog.json?" + params;
  const result = await (await fetch(url)).json();
  return result;
}
```

Datasette supports read\-only SQL queries via its JSON API, which means we can construct the SQL query as a JavaScript string and then encode it as a query string using `URLSearchParams()`.

We also take the list of keywords and turn them into a SQLite FTS search query that looks like `"word1" OR "word2" OR "word3"`.

SQLite's built\-in relevance calculations work well with this \- you can throw in dozens of words separated by `OR` and the top ranking results will generally be the ones with the most matches.

Finally, the code that ties this together \- suggests keywords, runs the search and then asks Claude to answer the question. I ended up bundling that together in the HTTP handler for the Val Town script \- this is the code that is called for every incoming HTTP request:

```
export default async function(req: Request) {
  // This is the Val Town HTTP handler
  const url = new URL(req.url);
  const question = url.searchParams.get("question").slice(0, 40);
  if (!question) {
    return Response.json({ "error": "No question provided" });
  }
  // Turn the question into search terms
  const keywords = await suggestKeywords(question);

  // Run the actual search
  const result = await runSearch(keywords);

  // Strip HTML tags from each body property, modify in-place:
  result.forEach(r => {
    r.body = r.body.replace(/<[^>]*>/g, "");
  });

  // Glue together a string of the title and body properties in one go
  const context = result.map(r => r.title + " " + r.body).join("\n\n");

  // Ask Claude to answer the question
  const message = await anthropic.messages.create({
    max_tokens: 1024,
    model: "claude-3-haiku-20240307",
    messages: [
      { role: "user", content: context },
      { role: "assistant", content: "Thank you for the context, I am ready to answer your question" },
      { role: "user", content: question },
    ],
  });
  return Response.json({answer: message.content[0].text});
}
```

There are many other ways you could arrange the prompting here. I quite enjoy throwing together a fake conversation like this that feeds in the context and then hints at the agent that it should respond next with its answer, but there are many potential variations on this theme.

This initial version returned the answer as a JSON object, something like this:

```
{
    "answer": "shot-scraper is a command-line tool that automates the process of taking screenshots of web pages..."
}
```

[![Screenshot of the Val Town interface returning the JSON answer to the question in a preview window](https://substackcdn.com/image/fetch/$s_!jnEm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1218cada-7c0a-4339-89bc-ed5f773f524a_1280x720.jpeg "Screenshot of the Val Town interface returning the JSON answer to the question in a preview window")](https://substackcdn.com/image/fetch/$s_!jnEm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1218cada-7c0a-4339-89bc-ed5f773f524a_1280x720.jpeg)

We were running out of time, but we wanted to add an HTML interface. Steve suggested getting Claude to write the whole thing! So we tried this:

```
  const message = await anthropic.messages.create({
    max_tokens: 1024,
    model: "claude-3-5-sonnet-20240620", // "claude-3-haiku-20240307",
    system: "Return a full HTML document as your answer, no markdown, make it pretty with exciting relevant CSS",
    messages: [
      { role: "user", content: context },
      { role: "assistant", content: "Thank you for the context, I am ready to answer your question as HTML" },
      { role: "user", content: question },
    ],
  });
  // Return back whatever HTML Claude gave us
  return new Response(message.content[0].text, {
    status: 200,
    headers: { "Content-Type": "text/html" }
  });
```

We upgraded to 3\.5 Sonnet to see if it had better "taste" than Haiku, and the results were really impressive. Here's what it gave us for "What is Datasette?":

[![Screnshot of a What is Datasette? page created by Claude 3.5 Sonnet - it includes a Key Features section with four different cards arranged in a grid, for Explore Data, Publish Data, API Access and Extensible.](https://substackcdn.com/image/fetch/$s_!ooKP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F62418e3c-95ed-48c6-8cf5-33c9ea843d09_1280x720.jpeg "Screnshot of a What is Datasette? page created by Claude 3.5 Sonnet - it includes a Key Features section with four different cards arranged in a grid, for Explore Data, Publish Data, API Access and Extensible.")](https://substackcdn.com/image/fetch/$s_!ooKP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F62418e3c-95ed-48c6-8cf5-33c9ea843d09_1280x720.jpeg)

It even styled the page with flexbox to arrange the key features of Datasette in a 2x2 grid! You can see that in the video at [1h13m17s](https://www.youtube.com/watch?v=9pmC3P1fUFo&t=1h13m17s).

There's a [full copy of the final TypeScript code](https://gist.github.com/simonw/7f8db0c452378eb4fa4747196b8194dc)available in a Gist.

#### **Some tricks we used along the way**

I didn't write all of the above code. Some bits of it were written by pasting things into Claude 3\.5 Sonnet, and others used the [Codeium](https://codeium.com/)integration in the Val Town editor ([described here](https://blog.val.town/blog/val-town-newsletter-16/#-codeium-completions)).

One pattern that worked particularly well was getting Sonnet to write the tool\-using TypeScript code for us.

The Claude 3 documentation showed [how to do that using curl](https://docs.anthropic.com/en/docs/build-with-claude/tool-use). I pasted that `curl` example in, added some example TypeScript and then prompted:

> Guess the JavaScript for setting up a tool which just returns a list of strings, called suggested\_search\_keywords

Here's my full prompt:

```
#!/bin/bash
IMAGE_URL="https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
IMAGE_MEDIA_TYPE="image/jpeg"
IMAGE_BASE64=$(curl "$IMAGE_URL" | base64)
curl https://api.anthropic.com/v1/messages \
     --header "content-type: application/json" \
     --header "x-api-key: $ANTHROPIC_API_KEY" \
     --header "anthropic-version: 2023-06-01" \
     --data \
'{
    "model": "claude-3-sonnet-20240229",
    "max_tokens": 1024,
    "tools": [{
        "name": "record_summary",
        "description": "Record summary of an image using well-structured JSON.",
        "input_schema": {
            "type": "object",
            "properties": {
                "key_colors": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "r": { "type": "number", "description": "red value [0.0, 1.0]" },
                            "g": { "type": "number", "description": "green value [0.0, 1.0]" },
                            "b": { "type": "number", "description": "blue value [0.0, 1.0]" },
                            "name": { "type": "string", "description": "Human-readable color name in snake_case, e.g. \"olive_green\" or \"turquoise\"" }
                        },
                        "required": [ "r", "g", "b", "name" ]
                    },
                    "description": "Key colors in the image. Limit to less then four."
                },
                "description": {
                    "type": "string",
                    "description": "Image description. One to two sentences max."
                },
                "estimated_year": {
                    "type": "integer",
                    "description": "Estimated year that the images was taken, if is it a photo. Only set this if the image appears to be non-fictional. Rough estimates are okay!"
                }
            },
            "required": [ "key_colors", "description" ]
        }
    }],
    "tool_choice": {"type": "tool", "name": "record_summary"},
    "messages": [
        {"role": "user", "content": [
            {"type": "image", "source": {
                "type": "base64",
                "media_type": "'$IMAGE_MEDIA_TYPE'",
                "data": "'$IMAGE_BASE64'"
            }},
            {"type": "text", "text": "Describe this image."}
        ]}
    ]
}'

Based on that example and this JavaScript code:

const anthropic = new Anthropic();
const message = await anthropic.messages.create({
  max_tokens: 1024,
  system: "Suggest individual search keywords to help answer this question. No yapping.",
  messages: [
    { role: "user", content: question },
  ],
  model: "claude-3-haiku-20240307",
});
console.log(message.content[0].text);

Guess the JavaScript for setting up a tool which just returns a list of strings, called suggested_search_keywords

```

It gave me back this, which was the *exact* code I needed to make my tool\-enabled API call from Val Town:

```
const anthropic = new Anthropic();
const message = await anthropic.messages.create({
  max_tokens: 1024,
  model: "claude-3-haiku-20240307",
  tools: [{
    name: "suggested_search_keywords",
    description: "Suggest individual search keywords to help answer the question.",
    input_schema: {
      type: "object",
      properties: {
        keywords: {
          type: "array",
          items: {
            type: "string"
          },
          description: "List of suggested search keywords"
        }
      },
      required: ["keywords"]
    }
  }],
  tool_choice: { type: "tool", name: "suggested_search_keywords" },
  messages: [
    { role: "user", content: question }
  ]
});

console.log(message.content[0].text);
```

I really like this trick, and I use it often in my own work. Find some example code that illustrates the pattern you need, paste in some additional context and get the LLM to figure the rest out for you.

#### **This is just a prototype**

It's important to reiterate that this is just a prototype \- it's the version of search\-backed RAG I could get working in an hour.

Putting something like this into production requires a whole lot more work. Most importantly, good RAG systems are backed by evals \- it's extremely hard to iterate on and improve a system like this if you don't have a good mechanism in place to evaluate if your changes are making things better or not. [Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/) by Hamel Husain remains my favourite piece of writing on how to go about putting these together.

#### **Additional links from the livestream**

Here are some of the other projects and links mentioned during our conversation:

* [Datasette](https://datasette.io/) and its [150\+ plugins](https://datasette.io/plugins).
* My original idea for a project was to use the [Datasette Write API](https://docs.datasette.io/en/latest/json_api.html#the-json-write-api) and run scheduled Vals to import data from various sources (my toots, tweets, posts etc) into a single searchable table.
* [LLM](https://llm.datasette.io/) \- my command\-line utility for working with different language models.
* [shot\-scraper](https://shot-scraper.datasette.io/) for automating screenshots and scraping websites with JavaScript from the command\-line \- here's [a recent demo](https://simonwillison.net/2024/Jun/17/cli-language-models/#frame_003715.jpg) where I scraped Google using shot\-scraper and fed the results into LLM as a basic form of RAG.
* My current list of [277 projects with at least one release](https://github.com/simonw/simonw/blob/main/releases.md) on GitHub.
* My [TIL blog](https://til.simonwillison.net/), which runs on a templated version of Datasette \- [here's the database](https://til.simonwillison.net/tils)and [here's the GitHub Actions workflow that builds it](https://observablehq.com/@simonw/blog-to-newsletter) using the [Baked Data pattern](https://simonwillison.net/2021/Jul/28/baked-data/).
* I have some previous experiments using embeddings with Datasette, including a [table of embeddings](https://til.simonwillison.net/tils/embeddings) (encoded [like this](https://llm.datasette.io/en/stable/embeddings/storage.html)) for my TIL blog which I use to power related items. That's described in this TIL: [Storing and serving related documents with openai\-to\-sqlite and embeddings](https://til.simonwillison.net/llms/openai-embeddings-related-content).

---

**Link** 2024\-06\-19 [Civic Band](https://civic.band/):

Exciting new civic tech project from Philip James: 30 (and counting) Datasette instances serving full\-text search enabled collections of OCRd meeting minutes for different civic governments. Includes [20,000 pages for Alameda](https://alameda.ca.civic.band/civic_minutes/pages), [17,000 for Pittsburgh](https://pittsburgh.pa.civic.band/civic_minutes/pages), [3,567 for Baltimore](https://baltimore.md.civic.band/civic_minutes/pages) and an enormous [117,000 for Maui County](https://maui-county.hi.civic.band/civic_minutes/pages).

Philip includes [some notes](https://civic.band/how.html) on how they're doing it. They gather PDF minute notes from anywhere that provides API access to them, then run local Tesseract for OCR (the cost of cloud\-based OCR proving prohibitive given the volume of data). The collection is then deployed to a single VPS running multiple instances of Datasette via Caddy, one instance for each of the covered regions.

---

**TIL** 2024\-06\-20 [Running Prettier against Django or Jinja templates](https://til.simonwillison.net/npm/prettier-django):

I really like auto\-formatting tools like Black. I've been hoping to find one that works with Django and Jinja templates for years. …

---

**Link** 2024\-06\-20 [State\-of\-the\-art music scanning by Soundslice](https://www.soundslice.com/sheet-music-scanner/):

It's been a while since I checked in on [Soundslice](https://www.soundslice.com/), Adrian Holovaty's beautiful web application focused on music education.

The latest feature is spectacular. The Soundslice music editor \- already one of the most impressive web applications I've ever experienced \- can now import notation directly from scans or photos of sheet music.

The attention to detail is immaculate. The custom machine learning model can handle a wide variety of notation details, and the system asks the user to verify or correct details that it couldn't perfectly determine using a neatly designed flow.

Free accounts can scan two single page documents a month, and paid plans get a much higher allowance. I tried it out just now on a low resolution image I found on Wikipedia and it did a fantastic job, even allowing me to listen to a simulated piano rendition of the music once it had finished processing.

It's worth spending some time with the [release notes](https://www.soundslice.com/blog/music-scanning/) for the feature to appreciate how much work they've out into improving it since the initial release.

If you're new to Soundslice, here's [an example](https://www.soundslice.com/slices/RXTDc/course-preview-5904/) of their core player interface which syncs the display of music notation to an accompanying video.

Adrian wrote up some [detailed notes](https://www.holovaty.com/writing/machine-learning-thoughts/) on the machine learning behind the feature when they first launched it in beta back in November 2022\.

> OMR \[Optical Music Recognition] is an inherently hard problem, significantly more difficult than text OCR. For one, music symbols have complex spatial relationships, and mistakes have a tendency to cascade. A single misdetected key signature might result in *multiple* incorrect note pitches. And there’s a wide diversity of symbols, each with its own behavior and semantics — meaning the problems and subproblems aren’t just hard, there are *many* of them.

---

**Quote** 2024\-06\-20

> *\[...] And then some absolute son of a bitch created ChatGPT, and now look at us. Look at us, resplendent in our pauper's robes, stitched from corpulent greed and breathless credulity, spending half of the planet's engineering efforts to add chatbot support to every application under the sun when half of the industry hasn't worked out how to test database backups regularly.*

[Nikhil Suresh](https://ludic.mataroa.blog/blog/i-will-fucking-piledrive-you-if-you-mention-ai-again/)

---

**Link** 2024\-06\-20 [Claude 3\.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet):

Anthropic released a new model this morning, and I think it's likely now the single best available LLM. Claude 3 Opus was already mostly on\-par with GPT\-4o, and the new 3\.5 Sonnet scores higher than Opus on almost all of Anthropic's internal evals.

It's also twice the speed and one *fifth* of the price of Opus (it's the same price as the previous Claude 3 Sonnet). To compare:

* gpt\-4o: $5/million input tokens and $15/million output
* Claude 3\.5 Sonnet: $3/million input, $15/million output
* Claude 3 Opus: $15/million input, $75/million output

Similar to Claude 3 Haiku then, which [both under\-cuts and out\-performs](https://simonwillison.net/2024/Mar/13/llm-claude-3-03/) OpenAI's GPT\-3\.5 model.

In addition to the new model, Anthropic also added a "artifacts" feature to their Claude web interface. The most exciting part of this is that any of the Claude models can now build *and then render* web pages and SPAs, directly in the Claude interface.

This means you can prompt them to e.g. "Build me a web app that teaches me about mandelbrot fractals, with interactive widgets" and they'll do exactly that \- I tried that prompt on Claude 3\.5 Sonnet earlier and [the results were spectacular](https://fedi.simonwillison.net/@simon/112650324117263516) (video demo).

An unsurprising note at the end of the post:

> To complete the Claude 3\.5 model family, we’ll be releasing Claude 3\.5 Haiku and Claude 3\.5 Opus later this year.

If the pricing stays consistent with Claude 3, Claude 3\.5 Haiku is going to be a *very* exciting model indeed.

---

**Quote** 2024\-06\-20

> *One of the core constitutional principles that guides our AI model development is privacy. We do not train our generative models on user\-submitted data unless a user gives us explicit permission to do so. To date we have not used any customer or user\-submitted data to train our generative models.*

[Anthropic](https://www.anthropic.com/news/claude-3-5-sonnet)

---

**Link** 2024\-06\-20 [llm\-claude\-3 0\.4](https://github.com/simonw/llm-claude-3/releases/tag/0.4):

LLM plugin release adding support for the new Claude 3\.5 Sonnet model:

```
pipx install llm
llm install -U llm-claude-3
llm keys set claude
# paste AP| key here
llm -m claude-3.5-sonnet \
  'a joke about a pelican and a walrus having lunch'

```

---

**Quote** 2024\-06\-21

> *It is in the public good to have AI produce quality and credible (if ‘hallucinations’ can be overcome) output. It is in the public good that there be the creation of original quality, credible, and artistic content. It is not in the public good if quality, credible content is excluded from AI training and output OR if quality, credible content is not created.*

[Jeff Jarvis](https://www.oreilly.com/radar/how-to-fix-ais-original-sin/)

---

**Link** 2024\-06\-21 [Val Vibes: Semantic search in Val Town](https://blog.val.town/blog/val-vibes/):

A neat case\-study by JP Posma on how Val Town's developers can use Val Town Vals to build prototypes of new features that later make it into Val Town core.

This one explores building out [semantic search](https://www.val.town/search?searchType=semantic)against Vals using OpenAI embeddings and the PostgreSQL pgvector extension.

---

**Quote** 2024\-06\-21

> *OpenAI was founded to build artificial general intelligence safely, free of outside commercial pressures. And now every once in a while it shoots out a new AI firm whose mission is to build artificial general intelligence safely, free of the commercial pressures at OpenAI.*

[Matt Levine](https://www.bloomberg.com/opinion/articles/2024-06-20/virgin-orbit-had-a-fake-takeover)

---

**Link** 2024\-06\-21 [Datasette 0\.64\.8](https://docs.datasette.io/en/stable/changelog.html#v0-64-8):

A very small Datasette release, fixing[a minor potential security issue](https://github.com/simonw/datasette/issues/2359)where the name of missing databases or tables was reflected on the 404 page in a way that could allow an attacker to present arbitrary text to a user who followed a link. Not an XSS attack (no code could be executed) but still a potential vector for confusing messages.

---

**Link** 2024\-06\-22 [Wikipedia Manual of Style: Linking](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Linking):

I started [a conversation on Mastodon](https://fedi.simonwillison.net/@simon/112657927527940565) about the grammar of linking: how to decide where in a phrase an inline link should be placed.

Lots of great (and varied) replies there. The most comprehensive style guide I've seen so far is this one from Wikipedia, via Tom Morris.

---

**Quote** 2024\-06\-22

> *In our “who validates the validators” user studies, we found that people expected—and also desired—for the LLM to learn from \*any\* human interaction. That too, “as efficiently as possible” (ie after 1\-2 demonstrations, the LLM should “get it”)*

[Shreya Shankar](https://twitter.com/sh_reya/status/1804573423429198224)

---

**Quote** 2024\-06\-23

> *The people who are most confident AI can replace writers are the ones who think writing is typing.*

[Andrew Ti](https://twitter.com/andrewti/status/1804591245161119901)

---

**Link** 2024\-06\-23 [llama.ttf](https://fuglede.github.io/llama.ttf/):

llama.ttf is "a font file which is also a large language model and an inference engine for that model".

You can see it kick into action at [8m28s in this video](https://www.youtube.com/watch?v=Q4bOyYctgFI&t=508s), where creator Søren Fuglede Jørgensen types "Once upon a time" followed by dozens of exclamation marks, and those exclamation marks then switch out to render a continuation of the story. But... when they paste the code out of the editor again it shows as the original exclamation marks were preserved \- the LLM output was presented only in the way they were rendered.

The key trick here is that the font renderer library [HarfBuzz](https://en.wikipedia.org/wiki/HarfBuzz) (used by Firefox, Chrome, Android, GNOME and more) added a new [WebAssembly extension](https://github.com/harfbuzz/harfbuzz/blob/main/docs/wasm-shaper.md) in [version 8\.0 last year](https://github.com/harfbuzz/harfbuzz/releases/tag/8.0.0), which is powerful enough to run a full LLM based on the [tinyllama\-15M](https://huggingface.co/nickypro/tinyllama-15M/tree/main) model \- which fits in a 60MB font file.

(Here's a related demo from Valdemar Erk showing Tetris running in a WASM font, at [22m56s in this video](https://www.youtube.com/watch?v=Ms1Drb9Vw9M&t=1376s).)

The source code for llama.ttf is [available on GitHub](https://github.com/fuglede/llama.ttf/tree/master/llamattf).

---

**Quote** 2024\-06\-23

> *For some reason, many people still believe that browsers need to include non\-standard hacks in HTML parsing to display the web correctly.  
>   
> In reality, the HTML parsing spec is exhaustively detailed. If you implement it as described, you will have a web\-compatible parser.*

[Andreas Kling](https://twitter.com/awesomekling/status/1803412879816659243)

---