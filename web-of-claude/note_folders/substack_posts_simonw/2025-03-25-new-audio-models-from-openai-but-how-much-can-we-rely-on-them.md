# New audio models from OpenAI, but how much can we rely on them?

*Plus o1-pro, Claude web search, DeepSeek-V3-0324, Qwen2.5-VL-32B and a new shot-scraper*

Published: 2025-03-25
Source: https://simonw.substack.com/p/new-audio-models-from-openai-but

---

In this newsletter:

* New audio models from OpenAI, but how much can we rely on them?

Plus 11 links and 2 quotations

### [New audio models from OpenAI, but how much can we rely on them?](https://simonwillison.net/2025/Mar/20/new-openai-audio-models/) \- 2025\-03\-20

OpenAI announced [several new audio\-related API features](https://openai.com/index/introducing-our-next-generation-audio-models/) today, for both text\-to\-speech and speech\-to\-text. They're very promising new models, but they appear to suffer from the ever\-present risk of accidental (or malicious) instruction following.

#### gpt\-4o\-mini\-tts

`gpt-4o-mini-tts` is a brand new text\-to\-speech model with "better steerability". OpenAI released a delightful new playground interface for this at [OpenAI.fm](https://www.openai.fm/) \- you can pick from 11 base voices, apply instructions like "High\-energy, eccentric, and slightly unhinged" and get it to read out a script (with optional extra stage directions in parenthesis). It can then provide the equivalent API code in Python, JavaScript or curl. You can share links to your experiments, [here's an example](https://www.openai.fm/#fa1e8762-ccf9-4f08-a468-7cc51632d0ed).

[![User interface showing voice and script options. Voice options include Alloy, Ash, Ballad, Coral (selected), Echo, Fable, Onyx, Nova, Sage, Shimmer, Verse, and a shuffle button. Vibe section shows Dramatic (selected), Cheerleader, Calm, Professional, True Crime Buff, and a refresh button. Instructions read Voice Affect: Low, hushed, and suspenseful; convey tension and intrigue. Tone: Deeply serious and mysterious, maintaining an undercurrent of unease throughout. Pacing: Fast paced, deliberate, pausing slightly after suspenseful moments to heighten drama. Emotion: Restrained yet intense—voice should subtly tremble or tighten at key suspenseful points. Emphasis: Highlight sensory descriptions ("footsteps echoed," "heart hammering," "shadows melting into darkness") to amplify atmosphere. Pronunciation: Slightly elongated vowels and softened consonants for an eerie, haunting effect. Pauses: Insert meaningful pauses after phrases like "only shadows melting into darkness," and especially before the final line, to enhance suspense dramatically. The script says: The night was thick with fog, wrapping the town in mist. Detective Evelyn Harper pulled her coat tighter, feeling the chill creep down her spine. She knew the town's buried secrets were rising again. (Whisper this bit:) Footsteps echoed behind her, slow and deliberate. She turned, heart racing but saw only shadows. (Now sound panicked) Evelyn steadied her breath—tonight felt different. Tonight, the danger felt personal. Somewhere nearby, hidden eyes watched her every move. Waiting. Planning. Knowing her next step. This was just the beginning.. Bottom shows DOWNLOAD, SHARE, and PLAY buttons.](https://substackcdn.com/image/fetch/$s_!9Hdo!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F87aad0b6-f4d8-4bf6-92bc-0805faf013bd_1862x1734.jpeg "User interface showing voice and script options. Voice options include Alloy, Ash, Ballad, Coral (selected), Echo, Fable, Onyx, Nova, Sage, Shimmer, Verse, and a shuffle button. Vibe section shows Dramatic (selected), Cheerleader, Calm, Professional, True Crime Buff, and a refresh button. Instructions read Voice Affect: Low, hushed, and suspenseful; convey tension and intrigue. Tone: Deeply serious and mysterious, maintaining an undercurrent of unease throughout. Pacing: Fast paced, deliberate, pausing slightly after suspenseful moments to heighten drama. Emotion: Restrained yet intense—voice should subtly tremble or tighten at key suspenseful points. Emphasis: Highlight sensory descriptions (\"footsteps echoed,\" \"heart hammering,\" \"shadows melting into darkness\") to amplify atmosphere. Pronunciation: Slightly elongated vowels and softened consonants for an eerie, haunting effect. Pauses: Insert meaningful pauses after phrases like \"only shadows melting into darkness,\" and especially before the final line, to enhance suspense dramatically. The script says: The night was thick with fog, wrapping the town in mist. Detective Evelyn Harper pulled her coat tighter, feeling the chill creep down her spine. She knew the town's buried secrets were rising again. (Whisper this bit:) Footsteps echoed behind her, slow and deliberate. She turned, heart racing but saw only shadows. (Now sound panicked) Evelyn steadied her breath—tonight felt different. Tonight, the danger felt personal. Somewhere nearby, hidden eyes watched her every move. Waiting. Planning. Knowing her next step. This was just the beginning.. Bottom shows DOWNLOAD, SHARE, and PLAY buttons.")](https://substackcdn.com/image/fetch/$s_!9Hdo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F87aad0b6-f4d8-4bf6-92bc-0805faf013bd_1862x1734.jpeg)

Note how part of my script there looks like this:

> (Whisper this bit:)
> 
> Footsteps echoed behind her, slow and deliberate. She turned, heart racing, but saw only shadows.

While fun and convenient, the fact that you can insert stage directions in the script itself feels like an anti\-pattern to me \- it means you can't safely use this for arbitrary text because there's a risk that some of that text may accidentally be treated as further instructions to the model.

In my own experiments I've already seen this happen: sometimes the model follows my "Whisper this bit" instruction correctly, other times it says the word "Whisper" out loud but doesn't speak the words "this bit". The results appear non\-deterministic, and might also vary with different base voices.

`gpt-4o-mini-tts` [costs](https://platform.openai.com/docs/pricing#transcription-and-speech-generation) $0\.60/million tokens, which OpenAI estimate as around 1\.5 cents per minute.

#### gpt\-4o\-transcribe and gpt\-4o\-mini\-transcribe

`gpt-4o-transcribe` and `gpt-4o-mini-transcribe` are two new speech\-to\-text models, serving a similar purpose to [whisper](https://github.com/openai/whisper) but built on top of GPT\-4o and setting a "new state\-of\-the\-art benchmark". These can be used via OpenAI's [v1/audio/transcriptions API](https://platform.openai.com/docs/guides/speech-to-text), as alternative options to \`whisper\-1\. The API is still restricted to a 25MB audio file (MP3, WAV or several other formats).

Any time an LLM\-based model is used for audio transcription (or OCR) I worry about accidental instruction following \- is there a risk that content that looks like an instruction in the spoken or scanned text might not be included in the resulting transcript?

In [a comment on Hacker News](https://news.ycombinator.com/item?id=43426022#43427525) OpenAI's Jeff Harris said this, regarding how these new models differ from [gpt\-4o\-audio\-preview](https://platform.openai.com/docs/models/gpt-4o-audio-preview):

> It's a slightly better model for TTS. With extra training focusing on reading the script exactly as written.
> 
> e.g. the audio\-preview model when given instruction to speak "What is the capital of Italy" would often speak "Rome". This model should be much better in that regard

"much better in that regard" sounds to me like there's still a risk of this occurring, so for some sensitive applications it may make sense to stick with whisper or other traditional text\-to\-speech approaches.

On Twitter [Jeff added](https://twitter.com/jeffintime/status/1902822589300609400):

> yep fidelity to transcript is the big chunk of work to turn an audio model into TTS model. still possible, but should be quite rare

`gpt-4o-transcribe` is an estimated 0\.6 cents per minute, and `gpt-4o-mini-transcribe` is 0\.3 cents per minute.

#### Mixing data and instructions remains the cardinal sin of LLMs

If these problems look familiar to you that's because they are variants of the root cause behind [prompt injection](https://simonwillison.net/tags/prompt-injection/). LLM architectures encourage mixing instructions and data in the same stream of tokens, but that means there are always risks that tokens from data (which often comes from untrusted sources) may be misinterpreted as instructions to the model.

How much of an impact this has on the utility of these new models remains to be seen. Maybe the new training is so robust that these issues won't actually cause problems for real\-world applications?

I remain skeptical. I expect we'll see demos of these flaws in action in relatively short order.

---

**Link** 2025\-03\-19 [OpenAI platform: o1\-pro](https://platform.openai.com/docs/models/o1-pro):

OpenAI have a new most\-expensive model: o1\-pro can now be accessed through their API at a hefty $150/million tokens for input and $600/million tokens for output. That's 10x the price of their o1 and o1\-preview models and a full 1,000x times more expensive than their cheapest model, gpt\-4o\-mini!

Aside from that it has mostly the same features as o1: a 200,000 token context window, 100,000 max output tokens, Sep 30 2023 knowledge cut\-off date and it supports function calling, structured outputs and image inputs.

o1\-pro doesn't support streaming, and most significantly for developers is the first OpenAI model to *only* be available via their new [Responses API](https://platform.openai.com/docs/api-reference/responses). This means tools that are built against their Chat Completions API (like my own [LLM](https://llm.datasette.io/)) have to do a whole lot more work to support the new model \- my [issue for that is here](https://github.com/simonw/llm/issues/839).

Since LLM doesn't support this new model yet I had to make do with `curl`:

```
curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $(llm keys get openai)" \
  -d '{
    "model": "o1-pro",
    "input": "Generate an SVG of a pelican riding a bicycle"
  }'
```

Here's [the full JSON](https://gist.github.com/simonw/0439d0255360c68b8f621133860710b1) I got back \- 81 input tokens and 1552 output tokens for a [total cost](https://tools.simonwillison.net/llm-prices) of 94\.335 cents.

[![Clearly a bird riding a bicycle. The pedals are in the wrong place and the bird doesn't quite have the majestic beak of a pelican.](https://substackcdn.com/image/fetch/$s_!XHXJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F612b313b-63d5-46e9-938b-b6daea642bf9_600x600.png "Clearly a bird riding a bicycle. The pedals are in the wrong place and the bird doesn't quite have the majestic beak of a pelican.")](https://substackcdn.com/image/fetch/$s_!XHXJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F612b313b-63d5-46e9-938b-b6daea642bf9_600x600.png)

I took a risk and added `"reasoning": {"effort": "high"}` to see if I could get a better pelican with more reasoning:

```
curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $(llm keys get openai)" \
  -d '{
    "model": "o1-pro",
    "input": "Generate an SVG of a pelican riding a bicycle",
    "reasoning": {"effort": "high"}
  }'
```

Surprisingly that used *less* output tokens \- 1459 compared to 1552 earlier (cost: 88\.755 cents) \- [producing this JSON](https://gist.github.com/simonw/085d81e1160157572c9bd361b01374c4) which rendered as a slightly better pelican:

[![A bit better - no pedals, so they cannot be in the wrong place. The bird has a slightly more majestic beak.](https://substackcdn.com/image/fetch/$s_!_N67!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F230567f6-7f70-411e-b67c-3e30abd29a44_800x800.png "A bit better - no pedals, so they cannot be in the wrong place. The bird has a slightly more majestic beak.")](https://substackcdn.com/image/fetch/$s_!_N67!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F230567f6-7f70-411e-b67c-3e30abd29a44_800x800.png)

It was cheaper because while it spent 960 reasoning tokens as opposed to 704 for the previous pelican it omitted the explanatory text around the SVG, saving on total output.

---

**Quote** 2025\-03\-20

> *I’ve disabled the pending geoblock of the UK because I now think the risks of the Online Safety Act to this site are low enough to change strategies to only geoblock if directly threatened by the regulator. \[...]   
>   
> It is not possible for a hobby site to comply with the Online Safety Act. The OSA is written to censor huge commercial sites with professional legal teams, and even understanding one's obligations under the regulations is an enormous project requiring expensive legal advice.   
>   
> The law is [250 pages](https://www.legislation.gov.uk/ukpga/2023/50/data.pdf) and the mandatory "guidance" from Ofcom is more than 3,000 pages of dense, cross\-referenced UK\-flavoured legalese. To find all the guidance you'll have to [start here](https://www.ofcom.org.uk/information-for-industry/?SelectedTopic=67866), click through to each of the 36 pages listed, and expand each page's collapsible sections that might have links to other pages and documents. (Though I can't be sure that leads to all their guidance, and note you'll have to check back regularly [for planned updates](https://www.ofcom.org.uk/siteassets/resources/documents/online-safety/information-for-industry/illegal-harms/overview.pdf?v=387529#page=4).)*

[Peter Bhat Harkins](https://lobste.rs/s/ukosa1/uk_users_lobsters_needs_your_help_with#c_xevn8a)

---

**Link** 2025\-03\-20 [Claude can now search the web](https://www.anthropic.com/news/web-search):

Claude 3\.7 Sonnet on the paid plan now has a web search tool that can be turned on as a global setting.

This was sorely needed. ChatGPT, Gemini and Grok all had this ability already, and despite Anthropic's excellent model quality it was one of the big remaining reasons to keep other models in daily rotation.

For the moment this is purely a product feature \- it's available through their consumer applications but there's no indication of whether or not it will be coming to the Anthropic API. OpenAI launched the latest version of web search in their API [last week](https://openai.com/index/new-tools-for-building-agents/).

Surprisingly there are no details on how it works under the hood. Is this a partnership with someone like Bing, or is it Anthropic's own proprietary index populated by their own crawlers?

I think it may be their own infrastructure, but I've been unable to confirm that.

***Update**: it's confirmed [as Brave Search](https://simonwillison.net/2025/Mar/21/anthropic-used-brave/).*

Their support site offers some inconclusive hints.

[Does Anthropic crawl data from the web, and how can site owners block the crawler?](https://support.anthropic.com/en/articles/10023637-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler) talks about their ClaudeBot crawler but the language indicates it's used for training data, with no mention of a web search index.

[Blocking and Removing Content from Claude](https://support.anthropic.com/en/articles/10684638-blocking-and-removing-content-from-claude) looks a little more relevant, and has a heading "Blocking or removing websites from Claude web search" which includes this eyebrow\-raising tip:

> Removing content from your site is the best way to ensure that it won't appear in Claude outputs when Claude searches the web.

And then this bit, which *does* mention "our partners":

> The noindex robots meta tag is a rule that tells our partners not to index your content so that they don’t send it to us in response to your web search query. Your content can still be linked to and visited through other web pages, or directly visited by users with a link, but the content will not appear in Claude outputs that use web search.

Both of those documents were last updated "over a week ago", so it's not clear to me if they reflect the new state of the world given today's feature launch or not.

I got this delightful response trying out Claude search where it mistook my recent [Squadron automata](https://simonwillison.net/2025/Mar/4/squadron/) for a software project:

[![Claude screenshot. My prompt: What is the most recent piece of software that Simon Willison has released? Claude response: I believe Simon Willison has released several recent software projects, but my training cutoff means I might not have the latest information. Let me search for his most recent releases to give you an accurate answer.  Search box: Simon Willison latest software release 2025. Based on my search, Simon Willison's most recent software release appears to be "Squadron," which he mentioned in a blog post from March 4, 2025, titled "I built an automaton called Squadron" according to his GitHub profile. He's also been actively maintaining and updating several projects in March 2025, with very recent releases including: e llm-command-r 0.3 (released March 13, 2025)](https://substackcdn.com/image/fetch/$s_!ilAm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6d917633-e819-4901-aafc-0bde68634965_733x1072.jpeg "Claude screenshot. My prompt: What is the most recent piece of software that Simon Willison has released? Claude response: I believe Simon Willison has released several recent software projects, but my training cutoff means I might not have the latest information. Let me search for his most recent releases to give you an accurate answer.  Search box: Simon Willison latest software release 2025. Based on my search, Simon Willison's most recent software release appears to be \"Squadron,\" which he mentioned in a blog post from March 4, 2025, titled \"I built an automaton called Squadron\" according to his GitHub profile. He's also been actively maintaining and updating several projects in March 2025, with very recent releases including: e llm-command-r 0.3 (released March 13, 2025)")](https://substackcdn.com/image/fetch/$s_!ilAm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6d917633-e819-4901-aafc-0bde68634965_733x1072.jpeg)

---

**Link** 2025\-03\-21 [Anthropic Trust Center: Brave Search added as a subprocessor](https://app.vanta.com/anthropic/trust/iz673w96495gyjer8h78n/updates):

Yesterday I was [trying to figure out](https://simonwillison.net/2025/Mar/20/claude-can-now-search-the-web/) if Anthropic has rolled their own search index for Claude's new web search feature or if they were working with a partner. Here's confirmation that they are using [Brave Search](https://search.brave.com/):

> Anthropic's subprocessor list. As of March 19, 2025, we have made the following changes:
> 
> Subprocessors added:
> 
> * Brave Search ([more info](https://support.anthropic.com/en/articles/10684626-enabling-and-using-web-search))

That "more info" links to the help page for their new web search feature.

I confirmed this myself by prompting Claude to "[Search for pelican facts](https://claude.ai/share/e2beb581-b6ad-49b4-9d64-11e4691b8941)" \- it ran a search for "Interesting pelican facts" and the ten results it showed as citations were an exact match for [that search on Brave](https://search.brave.com/search?q=interesting+pelican+facts).

And further evidence: if you [poke at it a bit](https://claude.ai/share/45348349-8cc7-4447-8d79-eae6f218eb53) Claude will reveal the definition of its `web_search` function which looks like this \- note the `BraveSearchParams` property:

```
{
  "description": "Search the web",
  "name": "web_search",
  "parameters": {
    "additionalProperties": false,
    "properties": {
      "query": {
        "description": "Search query",
        "title": "Query",
        "type": "string"
      }
    },
    "required": [
      "query"
    ],
    "title": "BraveSearchParams",
    "type": "object"
  }
}
```

---

**Link** 2025\-03\-21 [The "think" tool: Enabling Claude to stop and think in complex tool use situations](https://www.anthropic.com/engineering/claude-think-tool):

Fascinating new prompt engineering trick from Anthropic. They use their standard tool calling mechanism to define a tool called "think" that looks something like this:

```
{
  "name": "think",
  "description": "Use the tool to think about something. It will not obtain new information or change the database, but just append the thought to the log. Use it when complex reasoning or some cache memory is needed.",
  "input_schema": {
    "type": "object",
    "properties": {
      "thought": {
        "type": "string",
        "description": "A thought to think about."
      }
    },
    "required": ["thought"]
  }
}
```

This tool *does nothing at all*.

LLM tools (like [web\_search](https://simonwillison.net/2025/Mar/21/anthropic-use-brave/)) usually involve some kind of implementation \- the model requests a tool execution, then an external harness goes away and executes the specified tool and feeds the result back into the conversation.

The "think" tool is a no\-op \- there is no implementation, it just allows the model to use its existing training in terms of when\-to\-use\-a\-tool to stop and dump some additional thoughts into the context.

This works completely independently of the new "thinking" mechanism introduced [in Claude 3\.7 Sonnet](https://simonwillison.net/2025/Feb/25/llm-anthropic-014/#extended-thinking-mode).

Anthropic's benchmarks show impressive improvements from enabling this tool. I fully anticipate that models from other providers would benefit from the same trick.

---

**Link** 2025\-03\-22 [simonw/ollama\-models\-atom\-feed](https://github.com/simonw/ollama-models-atom-feed):

I setup a GitHub Actions \+ GitHub Pages Atom feed of scraped recent models data from the Ollama [latest models](https://ollama.com/search?o=newest) page \- Ollama remains one of the easiest ways to run models on a laptop so a new model release from them is worth hearing about.

I built the scraper by pasting example HTML [into Claude](https://claude.ai/share/c96d6bb9-a976-45f9-82c2-8599c2d6d492) and asking for a Python script to convert it to Atom \- here's [the script](https://github.com/simonw/ollama-models-atom-feed/blob/main/to_atom.py) we wrote together.

---

**Quote** 2025\-03\-23

> *If you’re new to tech, taking \[career] advice on what works for someone with a 20\-year career is likely to be about as effective as taking career advice from a stockbroker or firefighter or nurse. There’ll be a few things that generalize, but most advice won’t.   
>   
> Further, even advice people with long careers on what worked for them when they were getting started is unlikely to be advice that works today. The tech industry of 15 or 20 years ago was, again, **dramatically** different from tech today.*

[Jacob Kaplan\-Moss](https://jacobian.org/2025/mar/13/beware-advice-from-old-heads/)

---

**Link** 2025\-03\-23 [Next.js and the corrupt middleware: the authorizing artifact](https://zhero-web-sec.github.io/research-and-things/nextjs-and-the-corrupt-middleware):

Good, detailed write\-up of the Next.js vulnerability [CVE\-2025\-29927](https://nvd.nist.gov/vuln/detail/CVE-2025-29927) by Allam Rachid, one of the researchers who identified the issue.

The vulnerability is best illustrated by [this code snippet](https://github.com/vercel/next.js/blob/v12.0.7/packages/next/server/next-server.ts#L686):

```
const subreq = params.request.headers['x-middleware-subrequest'];
const subrequests = typeof subreq === 'string' ? subreq.split(':') : [];
// ...
for (const middleware of this.middleware || []) {
  // ...
  if (subrequests.includes(middlewareInfo.name)) {
    result = {
      response: NextResponse.next(),
      waitUntil: Promise.resolve(),
    };
    continue;
  }
}
```

This was part of Next.js internals used to help avoid applying middleware recursively to requests that are re\-dispatched through the framework.

Unfortunately it also meant that attackers could send a `x-middleware-subrequest` HTTP header with a colon\-separated list of middleware names to skip. If a site used middleware to apply an authentication gate (as suggested [in the Next.js documentation](https://nextjs.org/learn/dashboard-app/adding-authentication#protecting-your-routes-with-nextjs-middleware)) an attacker could bypass that authentication using this trick.

The vulnerability has been fixed in Next.js 15\.2\.3 \- here's the [official release announcement](https://nextjs.org/blog/cve-2025-29927) talking about the problem.

---

**Link** 2025\-03\-23 [Semantic Diffusion](https://martinfowler.com/bliki/SemanticDiffusion.html):

I [learned about](https://bsky.app/profile/mattchughes.ca/post/3ll2sbdky3k2y) this term today while complaining about how the definition of "vibe coding" is already being distorted to mean "any time an LLM writes code" as opposed to [the intended meaning](https://simonwillison.net/2025/Mar/19/vibe-coding/) of "code I wrote with an LLM without even reviewing what it wrote".

I posted [this salty note](https://bsky.app/profile/simonwillison.net/post/3ll2rtxeucs2e):

> Feels like I'm losing the battle on this one, I keep seeing people use "vibe coding" to mean any time an LLM is used to write code
> 
> I'm particularly frustrated because for a few glorious moments we had the chance at having ONE piece of AI\-related terminology with a clear, widely accepted definition!
> 
> But it turns out people couldn't be trusted to read all the way to the end of Andrej's tweet, so now we are back to yet another term where different people assume it means different things

Martin Fowler coined Semantic Diffusion in 2006 with this very clear definition:

> Semantic diffusion occurs when you have a word that is coined by a person or group, often with a pretty good definition, but then gets spread through the wider community in a way that weakens that definition. This weakening risks losing the definition entirely \- and with it any usefulness to the term.

What's happening with vibe coding right now is such a clear example of this effect in action! I've seen [the same thing happen](https://simonwillison.net/2024/Mar/5/prompt-injection-jailbreaking/) to my own coinage [prompt injection](https://simonwillison.net/2022/Sep/12/prompt-injection/) over the past couple of years.

This kind of dillution of meaning is frustrating, but does appear to be inevitable. As Martin Fowler points out it's most likely to happen to popular terms \- the more popular a term is the higher the chance a game of telephone will ensue where misunderstandings flourish as the chain continues to grow.

Andrej Karpathy, who [coined](https://twitter.com/karpathy/status/1886192184808149383) vibe coding, [posted this](https://twitter.com/karpathy/status/1903870973126045712) just now in reply to my [article](https://simonwillison.net/2025/Mar/19/vibe-coding/):

> Good post! It will take some time to settle on definitions. Personally I use "vibe coding" when I feel like this dog. My iOS app last night being a good example. But I find that in practice I rarely go full out vibe coding, and more often I still look at the code, I add complexity slowly and I try to learn over time how the pieces work, to ask clarifying questions etc.
> 
> [![Animated GIF.  I have no idea what I'm doing - a dog wags its tail while inspecting the engine of a car and looking gormless](https://substackcdn.com/image/fetch/$s_!h59N!,w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb4014061-155e-4f27-b21b-888ed5a444d2_640x434.gif "Animated GIF.  I have no idea what I'm doing - a dog wags its tail while inspecting the engine of a car and looking gormless")](https://substackcdn.com/image/fetch/$s_!h59N!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb4014061-155e-4f27-b21b-888ed5a444d2_640x434.gif)

I love that vibe coding has an official illustrative GIF now!

---

**Link** 2025\-03\-24 [deepseek\-ai/DeepSeek\-V3\-0324](https://huggingface.co/deepseek-ai/DeepSeek-V3-0324):

Chinese AI lab DeepSeek just released the latest version of their enormous DeepSeek v3 model, baking the release date into the name `DeepSeek-V3-0324`.

The license is MIT (that's new \- previous DeepSeek v3 had a custom license), the README is empty and the release adds up a to a total of 641 GB of files, mostly of the form `model-00035-of-000163.safetensors`.

The model only came out a few hours ago and MLX developer Awni Hannun already [has it running](https://twitter.com/awnihannun/status/1904177084609827054) at \>20 tokens/second on a 512GB M3 Ultra Mac Studio ($9,499 of ostensibly consumer\-grade hardware) via [mlx\-lm](https://pypi.org/project/mlx-lm/) and this [mlx\-community/DeepSeek\-V3\-0324\-4bit](https://huggingface.co/mlx-community/DeepSeek-V3-0324-4bit) 4bit quantization, which reduces the on\-disk size to 352 GB.

I think that means if you have that machine you can run it with my [llm\-mlx](https://github.com/simonw/llm-mlx) plugin like this, but I've not tried myself!

```
llm mlx download-model mlx-community/DeepSeek-V3-0324-4bit
llm chat -m mlx-community/DeepSeek-V3-0324-4bit

```

The new model is also [listed on OpenRouter](https://openrouter.ai/deepseek/deepseek-chat-v3-0324:free). You can try a chat at [openrouter.ai/chat?models\=deepseek/deepseek\-chat\-v3\-0324:free](https://openrouter.ai/chat?models=deepseek/deepseek-chat-v3-0324:free).

Here's what the chat interface [gave me](https://gist.github.com/simonw/3ce2bf5836743dfaf07d994578b261ba) for "Generate an SVG of a pelican riding a bicycle":

[![There's a pelican, and a bicycle, but both of them look disassembled.](https://substackcdn.com/image/fetch/$s_!A0mx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbc1d9529-56bf-437e-ac29-a134af784f22_800x600.jpeg "There's a pelican, and a bicycle, but both of them look disassembled.")](https://substackcdn.com/image/fetch/$s_!A0mx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbc1d9529-56bf-437e-ac29-a134af784f22_800x600.jpeg)

I have two API keys with OpenRouter \- one of them worked with the model, the other gave me a `No endpoints found matching your data policy` error \- I think because I had a setting on that key disallowing models from training on my activity. The key that worked was a free key with no attached billing credentials.

For my working API key the [llm\-openrouter](https://github.com/simonw/llm-openrouter) plugin let me run a prompt like this:

```
llm install llm-openrouter
llm keys set openrouter
# Paste key here
llm -m openrouter/deepseek/deepseek-chat-v3-0324:free "best fact about a pelican"
```

Here's that "best fact" \- the terminal output included Markdown and an emoji combo, here that's rendered.

> One of the most fascinating facts about pelicans is their **unique throat pouch**, called a **gular sac**, which can hold up to **3 gallons (11 liters) of water**—three times more than their stomach!
> 
> Here’s why it’s amazing:
> 
> * **Fishing Tool**: They use it like a net to scoop up fish, then drain the water before swallowing.
> * **Cooling Mechanism**: On hot days, pelicans flutter the pouch to stay cool by evaporating water.
> * **Built\-in "Shopping Cart"**: Some species even use it to carry food back to their chicks.
> 
> Bonus fact: Pelicans often **fish cooperatively**, herding fish into shallow water for an easy catch.
> 
> Would you like more cool pelican facts? 🐦🌊

In putting this post together I [got Claude](https://claude.ai/share/fc65bf9b-ae2d-4b23-bd09-ed0d54ff4b56) to build me [this new tool](https://tools.simonwillison.net/huggingface-storage) for finding the total on\-disk size of a Hugging Face repository, which is available in their API but not currently displayed on their website.

**Update**: Here's a notable independent benchmark [from Paul Gauthier](https://twitter.com/paulgauthier/status/1904304052500148423):

> DeepSeek's new V3 scored 55% on aider's [polyglot benchmark](https://aider.chat/docs/leaderboards/), significantly improving over the prior version. It's the \#2 non\-thinking/reasoning model, behind only Sonnet 3\.7\. V3 is competitive with thinking models like R1 \& o3\-mini.

---

**Link** 2025\-03\-24 [Qwen2\.5\-VL\-32B: Smarter and Lighter](https://qwenlm.github.io/blog/qwen2.5-vl-32b/):

The second big open weight LLM release from China today \- the first being [DeepSeek v3\-0324](https://simonwillison.net/2025/Mar/24/deepseek/).

Qwen's previous vision model was Qwen2\.5 VL, [released in January](https://simonwillison.net/2025/Jan/27/qwen25-vl-qwen25-vl-qwen25-vl/) in 3B, 7B and 72B sizes.

Today's Apache 2\.0 licensed release is a 32B model, which is quickly becoming my personal favourite model size \- large enough to have GPT\-4\-class capabilities, but small enough that on my 64GB Mack there's still enough RAM for me to run other memory\-hungry applications like Firefox and VS Code.

Qwen claim that the new model (when compared to their previous 2\.5 VL family) can "align more closely with human preferences", is better at "mathematical reasoning" and provides "enhanced accuracy and detailed analysis in tasks such as image parsing, content recognition, and visual logic deduction".

They also offer some presumably carefully selected benchmark results showing it out\-performing Gemma 3\-27B, Mistral Small 3\.1 24B and GPT\-4o\-0513 (there have been two more recent GPT\-4o releases since that one, 2024\-08\-16 and 2024\-11\-20\).

As usual, Prince Canuma had MLX versions of the models live within hours of the release, in [4 bit](https://huggingface.co/mlx-community/Qwen2.5-VL-32B-Instruct-4bit), [6 bit](https://huggingface.co/mlx-community/Qwen2.5-VL-32B-Instruct-6bit), [8 bit](https://huggingface.co/mlx-community/Qwen2.5-VL-32B-Instruct-8bit), and [bf16](https://huggingface.co/mlx-community/Qwen2.5-VL-32B-Instruct-bf16) variants.

I ran the 4bit version (a 18GB model download) using `uv` and Prince's [mlx\-vlm](https://github.com/Blaizzy/mlx-vlm) like this:

```
uv run --with 'numpy<2' --with mlx-vlm \
  python -m mlx_vlm.generate \
    --model mlx-community/Qwen2.5-VL-32B-Instruct-4bit \
    --max-tokens 1000 \
    --temperature 0.0 \
    --prompt "Describe this image." \
    --image Mpaboundrycdfw-1.png
```

Here's the image:

[![A map image, described below](https://substackcdn.com/image/fetch/$s_!zaAi!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F27e1507a-38f7-4318-bae6-9d48d3a6ffda_750x1050.png "A map image, described below")](https://substackcdn.com/image/fetch/$s_!zaAi!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F27e1507a-38f7-4318-bae6-9d48d3a6ffda_750x1050.png)

And here's the resulting description, which I found to be *very* impressive:

> This image appears to be a map highlighting specific areas along the coastline, likely in California, based on the geographical features and place names. Here is a detailed description of the image:
> 
> 1. **Geographic Features**:
> 
> 
> 	* The map shows a section of the coastline, with land on the right and the sea on the left.
> 	* The land area includes parts of SanMateo County, as noted in the top\-right corner.
> 	* The coastline features several named locations, including:
> 	
> 	
> 		+ **Point Montara**
> 		+ **Pillar Point**
> 		+ **Kings Rock**
> 		+ **VicenteCreek**
> 		+ **DennistonCreek**
> 		+ **State Beach**
> 2. **Highlighted Areas**:
> 
> 
> 	* The map contains two distinct areas marked with different colors:
> 	
> 	
> 		+ **Red Area (Top Section)**
> 		
> 		
> 			- Labeled as "MONTARA" and "MONTARA M R" (possibly referring to a "Marine Reserves" or similar protected area).
> 			- This area is marked with a dark red color and extends from the coastline inland.
> 		+ **Blue Area (Bottom Section)**
> 		
> 		
> 			- Labeled as "PILLAR" and "PILLAR P O I N T" along with "SMCA" (Special Management Area).
> 			- This area is marked with a blue color and is located closer to the coastline, including the area around "Pillar Point."
> 3. **Depth Contours**:
> 
> 
> 	* The map includes depth markings in the sea, indicating the bathymetrical features:
> 	
> 	
> 		+ **20 fathom (fm) line** is marked in the upper\-left part of the sea.
> 		+ **10 fathom (fm) line** is marked closer to the coastline.
> 		+ **30 fathom (fm) line** is marked further out to sea.
> 4. **Other Features**:
> 
> 
> 	* **State Beach**: Marked near the top\-right, indicating a protected recreational area.
> 	* **Kings Rock**: A prominent feature near the coastline, likely a rocky outcropping.
> 	* **Creeks**: The map shows several creeks, including **VicenteCreek** and **DennistonCreek**, which flow into the sea.
> 5. **Protected Areas**:
> 
> 
> 	* The map highlights specific protected areas:
> 	
> 	
> 		+ **Marine Reserves**:
> 		
> 		
> 			- "MONTARA M R" (Marine Reserves) in red.
> 		+ **Special Management Area (SMCA)**
> 		
> 		
> 			- "PILLAR P O I N T" in blue, indicating a Special Management Area.
> 6. **Grid and Coordinates**:
> 
> 
> 	* The map includes a grid with latitude and longitude markings:
> 	
> 	
> 		+ Latitude ranges from approximately 37°25'N to 37°35'N.
> 		+ Longitude ranges from approximately 122°22\.5'W to 122°35\.5'W.
> 7. **Topography**:
> 
> 
> 	* The land area shows topographic features, including elevations and vegetation, with green areas indicating higher elevations or vegetated land.
> 8. **Other Labels**:
> 
> 
> 	* **"SMR"**: Likely stands for "State Managed Reserves."
> 	* **"SMCA"**: Likely stands for "Special Management Control Area."
> 
> In summary, this map highlights specific protected areas along the coastline, including a red "Marine Reserves" area and a blue "Special Management Area" near "Pillar Point." The map also includes depth markings, geographical features, and place names, providing a detailed view of the region's natural and protected areas.

It included the following runtime statistics:

```
Prompt: 1051 tokens, 111.985 tokens-per-sec
Generation: 760 tokens, 17.328 tokens-per-sec
Peak memory: 21.110 GB
```

---

**Link** 2025\-03\-25 [microsoft/playwright\-mcp](https://github.com/microsoft/playwright-mcp):

The Playwright team at Microsoft have released an MCP ([Model Context Protocol](https://github.com/microsoft/playwright-mcp)) server wrapping Playwright, and it's pretty fascinating.

They implemented it on top of the Chrome accessibility tree, so MCP clients (such as the Claude Desktop app) can use it to drive an automated browser and use the accessibility tree to read and navigate pages that they visit.

Trying it out is quite easy if you have Claude Desktop and Node.js installed already. Edit your `claude_desktop_config.json` file:

```
code ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

And add this:

```
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest"
      ]
    }
  }
}
```

Now when you launch Claude Desktop various new browser automation tools will be available to it, and you can tell Claude to navigate to a website and interact with it.

[![Screenshot of Claude interface showing a conversation about Datasette. The interface shows Claude responding to a user (SW) after navigating to datasette.io. Claude's response includes page details (URL: https://datasette.io/, Title: Datasette: An open source multi-tool for exploring and publishing data) and a summary of what's visible on the site: a description of Datasette as an open-source tool for exploring and publishing data, the tagline "Find stories in data", navigation options, and features including exploratory data analysis, instant data publishing, and rapid prototyping.](https://substackcdn.com/image/fetch/$s_!Z-Ve!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F59485010-2c58-478b-b4c5-72f861c2ec63_1933x1783.jpeg "Screenshot of Claude interface showing a conversation about Datasette. The interface shows Claude responding to a user (SW) after navigating to datasette.io. Claude's response includes page details (URL: https://datasette.io/, Title: Datasette: An open source multi-tool for exploring and publishing data) and a summary of what's visible on the site: a description of Datasette as an open-source tool for exploring and publishing data, the tagline \"Find stories in data\", navigation options, and features including exploratory data analysis, instant data publishing, and rapid prototyping.")](https://substackcdn.com/image/fetch/$s_!Z-Ve!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F59485010-2c58-478b-b4c5-72f861c2ec63_1933x1783.jpeg)

I ran the following to get a list of the available tools:

```
cd /tmp
git clone https://github.com/microsoft/playwright-mcp
cd playwright-mcp/src/tools
files-to-prompt . | llm -m claude-3.7-sonnet \
  'Output a detailed description of these tools'
```

The [full output is here](https://gist.github.com/simonw/69200999149221c549c1f62e7befa20f), but here's the truncated tool list:

> #### Navigation Tools (`common.ts`)
> 
> * **browser\_navigate**: Navigate to a specific URL
> * **browser\_go\_back**: Navigate back in browser history
> * **browser\_go\_forward**: Navigate forward in browser history
> * **browser\_wait**: Wait for a specified time in seconds
> * **browser\_press\_key**: Press a keyboard key
> * **browser\_save\_as\_pdf**: Save current page as PDF
> * **browser\_close**: Close the current page
> 
> #### Screenshot and Mouse Tools (`screenshot.ts`)
> 
> * **browser\_screenshot**: Take a screenshot of the current page
> * **browser\_move\_mouse**: Move mouse to specific coordinates
> * **browser\_click** (coordinate\-based): Click at specific x,y coordinates
> * **browser\_drag** (coordinate\-based): Drag mouse from one position to another
> * **browser\_type** (keyboard): Type text and optionally submit
> 
> #### Accessibility Snapshot Tools (`snapshot.ts`)
> 
> * **browser\_snapshot**: Capture accessibility structure of the page
> * **browser\_click** (element\-based): Click on a specific element using accessibility reference
> * **browser\_drag** (element\-based): Drag between two elements
> * **browser\_hover**: Hover over an element
> * **browser\_type** (element\-based): Type text into a specific element

---

**Link** 2025\-03\-25 [shot\-scraper 1\.8](https://github.com/simonw/shot-scraper/releases/tag/1.8):

I've added a new feature to [shot\-scraper](https://shot-scraper.datasette.io/) that makes it easier to share scripts for other people to use with the [shot\-scraper javascript](https://observablehq.com/@simonw/blog-to-newsletter) command.

`shot-scraper javascript` lets you load up a web page in an invisible Chrome browser (via Playwright), execute some JavaScript against that page and output the results to your terminal. It's a fun way of running complex screen\-scraping routines as part of a terminal session, or even chained together with other commands using pipes.

The `-i/--input` option lets you load that JavaScript from a file on disk \- but now you can also use a `gh:` prefix to specify loading code from GitHub instead.

To quote [the release notes](https://github.com/simonw/shot-scraper/releases/tag/1.8):

> `shot-scraper javascript` can now optionally [load scripts hosted on GitHub](https://shot-scraper.datasette.io/en/stable/javascript.html#running-javascript-from-github) via the new `gh:` prefix to the `shot-scraper javascript -i/--input` option. [\#173](https://github.com/simonw/shot-scraper/issues/173)
> 
> Scripts can be referenced as `gh:username/repo/path/to/script.js` or, if the GitHub user has created a dedicated `shot-scraper-scripts` repository and placed scripts in the root of it, using `gh:username/name-of-script`.
> 
> For example, to run this [readability.js](https://github.com/simonw/shot-scraper-scripts/blob/main/readability.js) script against any web page you can use the following:
> 
> 
> ```
> shot-scraper javascript --input gh:simonw/readability \
>   https://simonwillison.net/2025/Mar/24/qwen25-vl-32b/
> ```

The [output from that example](https://gist.github.com/simonw/60e196ec39a5a75dcabfd75fbe911a4c) starts like this:

```
{
    "title": "Qwen2.5-VL-32B: Smarter and Lighter",
    "byline": "Simon Willison",
    "dir": null,
    "lang": "en-gb",
    "content": "<div id=\"readability-page-1\"...
```

My [simonw/shot\-scraper\-scripts](https://github.com/simonw/shot-scraper-scripts) repo only has that one file in it so far, but I'm looking forward to growing that collection and hopefully seeing other people create and share their own `shot-scraper-scripts` repos as well.

This feature is an imitation of [a similar feature](https://github.com/simonw/llm/issues/809) that's coming in the next release of LLM.

---