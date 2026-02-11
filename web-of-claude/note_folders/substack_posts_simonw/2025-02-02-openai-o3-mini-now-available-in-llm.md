# OpenAI o3-mini, now available in LLM

*Plus Mistral Small 3, notes on prompting o3 and LLM tips from a professional translator*

Published: 2025-02-02
Source: https://simonw.substack.com/p/openai-o3-mini-now-available-in-llm

---

In this newsletter:

* OpenAI o3\-mini, now available in LLM

Plus 10 links and 6 quotations

### [OpenAI o3\-mini, now available in LLM](https://simonwillison.net/2025/Jan/31/o3-mini/) \- 2025\-01\-31

OpenAI's [o3\-mini is out today](https://openai.com/index/openai-o3-mini/). As with other o\-series models it's a slightly difficult one to evaluate \- we now need to decide if a prompt is best run using GPT\-4o, o1, o3\-mini or (if we have access) o1 Pro.

Confusing matters further, the benchmarks in [the o3\-mini system card](https://openai.com/index/o3-mini-system-card/) (PDF) aren't a universal win for o3\-mini across all categories. It generally benchmarks higher than GPT\-4o and o1 but not across everything.

The biggest win for o3\-mini is on the Codeforces ELO competitive programming benchmark, which I think is [described by this 2nd January 2025 paper](https://arxiv.org/abs/2501.01257), with the following scores:

* o3\-mini (high) 2130
* o3\-mini (medium) 2036
* o1 1891
* o3\-mini (low) 1831
* o1\-mini 1650
* o1\-preview 1258
* GPT\-4o 900

Weirdly, that GPT\-4o score was in an older copy of the System Card PDF which has been replaced by an updated document that doesn't mention Codeforces ELO scores at all.

One note from the System Card that stood out for me concerning intended applications of o3\-mini for OpenAI themselves:

> We also plan to allow users to use o3\-mini to search the internet and summarize the results in ChatGPT. We expect o3\-mini to be a useful and safe model for doing this, especially given its performance on the jailbreak and instruction hierarchy evals detailed in Section 4 below.

This is notable because the existing o1 models on ChatGPT have not yet had access to their web search tool \- despite the mixture of search and "reasoning" models having very clear benefits.

o3\-mini does not and [will not](https://twitter.com/nikunjhanda/status/1885415728624656481) support vision. We will have to wait for future OpenAI reasoning models for that.

I released [LLM 0\.21](https://llm.datasette.io/en/stable/changelog.html#v0-21) with support for the new model, plus its `-o reasoning_effort high` (or `medium` or `low`) option for tweaking the reasoning effort \- details [in this issue](https://github.com/simonw/llm/issues/728).

Note that the new model is currently only available for [Tier 3](https://platform.openai.com/docs/guides/rate-limits/usage-tiers#tier-3-rate-limits) and higher users, which requires you to have spent at least $100 on the API.

o3\-mini [is priced](https://openai.com/api/pricing/) at $1\.10/million input tokens, $4\.40/million output tokens \- less than half the price of GPT\-4o (currently $2\.50/$10\) and massively cheaper than o1 ($15/60\).

I tried using it to summarize [this conversation about o3\-mini on Hacker News](https://news.ycombinator.com/item?id=42890627), using [my hn\-summary.sh script](https://til.simonwillison.net/llms/claude-hacker-news-themes#user-content-adding-a--m-model-option).

```
hn-summary.sh 42890627 -o o3-mini
```

Here's [the result](https://gist.github.com/simonw/09e5922be0cbb85894cf05e6d75ae050) \- it used 18,936 input tokens and 2,905 output tokens for a total cost of 3\.3612 cents.

o3\-mini (and o1\-mini) are text\-only models: they don't accept image inputs. The full o1 API model can accept images in the same way as GPT\-4o.

Another characteristic worth noting is o3\-mini's token output limit \- the measure of how much text it can output in one go. That's 100,000 tokens, compared to 16,000 for GPT\-4o and just 8,000 for both DeepSeek R1 and Claude 3\.5\.

Invisible "reasoning tokens" come out of the same budget, so it's likely not possible to have it output the full 100,000\.

The model accepts up to 200,000 tokens of input, an improvement on GPT\-4o's 128,000\.

An application where output limits really matter is translation between human languages, where the output can realistically be expected to have a similar length to the input. It will be interesting seeing how well o3\-mini works for that, especially given its low price.

Update: Here's a [fascinating comment](https://news.ycombinator.com/item?id=42894215#42895610) on this by professional translator Tom Gally on Hacker News:

> I just did a test in which both R1 and o3\-mini got worse at translation in the latter half of a long text. \[...]
> 
> An initial comparison of the output suggested that, while R1 didn’t seem bad, o3\-mini produced a writing style closer to what I asked for in the prompt—smoother and more natural English. But then I noticed that the output length was 5,855 characters for R1, 9,052 characters for o3\-mini, and 11,021 characters for my own polished version. Comparing the three translations side\-by\-side with the original Japanese, I discovered that R1 had omitted entire paragraphs toward the end of the speech, and that o3\-mini had switched to a strange abbreviated style (using slashes instead of “and” between noun phrases, for example) toward the end as well. The vanilla versions of ChatGPT, Claude, and Gemini that I ran the same prompt and text through a month ago had had none of those problems.

---

**Quote** 2025\-01\-30

> *Llama 4 is making great progress in training. Llama 4 mini is done with pre\-training and our reasoning models and larger model are looking good too. Our goal with Llama 3 was to make open source competitive with closed models, and our goal for Llama 4 is to lead. Llama 4 will be natively multimodal \-\- it's an omni\-model \-\- and it will have agentic capabilities, so it's going to be novel and it's going to unlock a lot of new use cases.*

[Mark Zuckerberg](https://m.facebook.com/story.php?story_fbid=pfbid02oRRTPrY1mvbqBZT4QueimeBrKcVXG4ySxFscRLiEU6QtGxbLi9U4TBojiC9aa19fl&id=4&mibextid=wwXIfr)

---

**Quote** 2025\-01\-30

> *104\. Technology offers remarkable tools to oversee and develop the world's resources. However, in some cases, humanity is increasingly ceding control of these resources to machines. Within some circles of scientists and futurists, there is optimism about the potential of artificial general intelligence (AGI), a hypothetical form of AI that would match or surpass human intelligence and bring about unimaginable advancements. Some even speculate that AGI could achieve superhuman capabilities. At the same time, as society drifts away from a connection with the transcendent, some are tempted to turn to AI in search of meaning or fulfillment\-\-\-longings that can only be truly satisfied in communion with God. [\[194]](https://www.vatican.va/roman_curia/congregations/cfaith/documents/rc_ddf_doc_20250128_antiqua-et-nova_en.html#_ftn194)   
>   
> 105\. However, the presumption of substituting God for an artifact of human making is idolatry, a practice Scripture explicitly warns against (e.g., Ex. 20:4; 32:1\-5; 34:17\). Moreover, AI may prove even more seductive than traditional idols for, unlike idols that "have mouths but do not speak; eyes, but do not see; ears, but do not hear" (Ps. 115:5\-6\), AI can "speak," or at least gives the illusion of doing so (cf. Rev. 13:15\). Yet, it is vital to remember that AI is but a pale reflection of humanity\-\-\-it is crafted by human minds, trained on human\-generated material, responsive to human input, and sustained through human labor. AI cannot possess many of the capabilities specific to human life, and it is also fallible. By turning to AI as a perceived "Other" greater than itself, with which to share existence and responsibilities, humanity risks creating a substitute for God. However, it is not AI that is ultimately deified and worshipped, but humanity itself\-\-\-which, in this way, becomes enslaved to its own work. [\[195]](https://www.vatican.va/roman_curia/congregations/cfaith/documents/rc_ddf_doc_20250128_antiqua-et-nova_en.html#_ftn195)*

[Antiqua et Nova](https://www.vatican.va/roman_curia/congregations/cfaith/documents/rc_ddf_doc_20250128_antiqua-et-nova_en.html)

---

**Link** 2025\-01\-30 [Mistral Small 3](https://mistral.ai/news/mistral-small-3/):

First model release of 2025 for French AI lab Mistral, who describe Mistral Small 3 as "a latency\-optimized 24B\-parameter model released under the Apache 2\.0 license."

More notably, they claim the following:

> Mistral Small 3 is competitive with larger models such as Llama 3\.3 70B or Qwen 32B, and is an excellent open replacement for opaque proprietary models like GPT4o\-mini. Mistral Small 3 is on par with Llama 3\.3 70B instruct, while being more than 3x faster on the same hardware.

Llama 3\.3 70B and Qwen 32B are two of my favourite models to run on my laptop \- that \~20GB size turns out to be a great trade\-off between memory usage and model utility. It's exciting to see a new entrant into that weight class.

The license is important: previous Mistral Small models used their Mistral Research License, which prohibited commercial deployments unless you negotiate a commercial license with them. They appear to be moving away from that, at least for their core models:

> **We’re renewing our commitment to using Apache 2\.0 license for our general purpose models, as we progressively move away from MRL\-licensed models**. As with Mistral Small 3, model weights will be available to download and deploy locally, and free to modify and use in any capacity. \[…] Enterprises and developers that need specialized capabilities (increased speed and context, domain specific knowledge, task\-specific models like code completion) can count on additional commercial models complementing what we contribute to the community.

Despite being called Mistral Small 3, this appears to be the fourth release of a model under that label. The Mistral API calls this one `mistral-small-2501` \- previous model IDs were `mistral-small-2312`, `mistral-small-2402` and `mistral-small-2409`.

I've [updated the llm\-mistral plugin](https://github.com/simonw/llm-mistral/releases/tag/0.10) for talking directly to Mistral's [La Plateforme](https://docs.mistral.ai/deployment/laplateforme/overview/) API:

```
llm install -U llm-mistral
llm keys set mistral
# Paste key here
llm -m mistral/mistral-small-latest "tell me a joke about a badger and a puffin"
```

> Sure, here's a light\-hearted joke for you:
> 
> Why did the badger bring a puffin to the party?
> 
> Because he heard puffins make great party 'Puffins'!
> 
> (That's a play on the word "puffins" and the phrase "party people.")

API pricing is $0\.10/million tokens of input, $0\.30/million tokens of output \- half the price of the previous Mistral Small API model ($0\.20/$0\.60\). for comparison, GPT\-4o mini is $0\.15/$0\.60\.

Mistral also ensured that the new model was [available on Ollama](https://ollama.com/library/mistral-small) in time for their release announcement.

You can pull the model like this (fetching 14GB):

```
ollama run mistral-small:24b
```

The [llm\-ollama](https://github.com/taketwo/llm-ollama) plugin will then let you prompt it like so:

```
llm install llm-ollama
llm -m mistral-small:24b "say hi"
```

---

**Link** 2025\-01\-30 [PyPI now supports project archival](https://blog.pypi.org/posts/2025-01-30-archival/):

Neat new PyPI feature, similar to GitHub's [archiving repositories](https://docs.github.com/en/repositories/archiving-a-github-repository/archiving-repositories) feature. You can now mark a PyPI project as "archived", making it clear that no new releases are planned (though you can switch back out of that mode later if you need to).

I like the sound of these future plans around this topic:

> Project archival is the first step in a larger project, aimed at improving the *lifecycle* of projects on PyPI. That project includes evaluating additional project statuses (things like "deprecated" and "unmaintained"), as well as changes to [PyPI's public APIs](https://docs.pypi.org/api/) that will enable clients to retrieve and act on project status information. You can track our progress on these fronts by following along with [warehouse\#16844](https://github.com/pypi/warehouse/issues/16844)!

---

**Quote** 2025\-01\-30

> *Eventually, however, HudZah wore Claude down. He filled his Project with the e\-mail conversations he’d been having with fusor hobbyists, parts lists for things he’d bought off Amazon, spreadsheets, sections of books and diagrams. HudZah also changed his questions to Claude from general ones to more specific ones. This flood of information and better probing seemed to convince Claude that HudZah did know what he was doing, and the AI began to give him detailed guidance on how to build a nuclear fusor and how not to die while doing it.*

[Ashlee Vance](https://www.corememory.com/p/a-young-man-used-ai-to-build-a-nuclear)

---

---

**Link** 2025\-01\-31 [The surprising way to save memory with BytesIO](https://pythonspeed.com/articles/bytesio-reduce-memory-usage/):

Itamar Turner\-Trauring explains that if you have a `BytesIO` object in Python calling `.read()` on it will create a full copy of that object, doubling the amount of memory used \- but calling `.getvalue()` returns a `bytes` object that uses no additional memory, instead using copy\-on\-write.

`.getbuffer()` is another memory\-efficient option but it returns a [memoryview](https://docs.python.org/3/library/stdtypes.html#memoryview) which has less methods than the `bytes` you get back from `.getvalue()`\- it doesn't have `.find()` for example.

---

**Link** 2025\-01\-31 [openai\-realtime\-solar\-system](https://github.com/openai/openai-realtime-solar-system):

This was my favourite demo from OpenAI DevDay [back in October](https://simonwillison.net/2024/Oct/1/openai-devday-2024-live-blog/#live-update-100) \- a voice\-driven exploration of the solar system, developed by Katia Gil Guzman, where you could say things out loud like "show me Mars" and it would zoom around showing you different planetary bodies.

[![Zoomed in on Mars. A log panel shows JSON on the right.](https://substackcdn.com/image/fetch/$s_!w4AT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb72b07b5-ad1b-42a9-b754-8d52feba1046_2334x1396.jpeg "Zoomed in on Mars. A log panel shows JSON on the right.")](https://substackcdn.com/image/fetch/$s_!w4AT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb72b07b5-ad1b-42a9-b754-8d52feba1046_2334x1396.jpeg)

OpenAI *finally* released the code for it, now upgraded to use the new, easier to use WebRTC API they [released in December](https://simonwillison.net/2024/Dec/17/openai-webrtc/).

I ran it like this, loading my OpenAI API key using [llm keys get](https://llm.datasette.io/en/stable/help.html#llm-keys-get-help):

```
cd /tmp
git clone https://github.com/openai/openai-realtime-solar-system
cd openai-realtime-solar-system
npm install
OPENAI_API_KEY="$(llm keys get openai)" npm run dev
```

You need to click on both the Wifi icon and the microphone icon before you can instruct it with your voice. Try "Show me Mars".

---

**Link** 2025\-01\-31 [Latest black (25\.1\.0\) adds a newline after docstring and before pass in an exception class](https://github.com/psf/black/issues/4571):

I filed a bug report against Black when the latest release \- 25\.1\.0 \- reformatted the following code to add an ugly (to me) newline between the docstring and the `pass`:

```
class ModelError(Exception):
    "Models can raise this error, which will be displayed to the user"

    pass
```

Black maintainer Jelle Zijlstra confirmed that this is intended behavior with respect to [Black's 2025 stable style](https://github.com/psf/black/issues/4522), but also helped me understand that the `pass` there is actually unnecessary so I can fix the aesthetics by [removing that entirely](https://github.com/simonw/llm/commit/deb8bc3b4f5219583009eeb2c600d0b14c852c78).

I'm linking to this issue because it's a neat example of how I like to include steps\-to\-reproduce using [uvx](https://docs.astral.sh/uv/guides/tools/) to create one\-liners you can paste into a terminal to see the bug that I'm reporting. In this case I shared the following:

> Here's a way to see that happen using `uvx`. With the previous Black version:
> 
> 
> ```
> echo 'class ModelError(Exception):
>     "Models can raise this error, which will be displayed to the user"
>     pass' | uvx --with 'black==24.10.0' black -
> ```
> This outputs:
> 
> 
> ```
> class ModelError(Exception):
>     "Models can raise this error, which will be displayed to the user"
>     pass
> All done! ✨ 🍰 ✨
> 1 file left unchanged.
> ```
> But if you bump to `25.1.0` this happens:
> 
> 
> ```
> echo 'class ModelError(Exception):
>     "Models can raise this error, which will be displayed to the user"
>     pass' | uvx --with 'black==25.1.0' black - 
> ```
> Output:
> 
> 
> ```
> class ModelError(Exception):
>     "Models can raise this error, which will be displayed to the user"
> 
>     pass
> reformatted -
> 
> All done! ✨ 🍰 ✨
> 1 file reformatted.
> ```

Via [David Szotten](https://fosstodon.org/@davidszotten/113928041285282786) I learned that you can use `uvx black@25.1.0` here instead.

---

**Quote** 2025\-02\-01

> *Basically any resource on a difficult subject—a colleague, Google, a published paper—will be wrong or incomplete in various ways. Usefulness isn’t only a matter of correctness.   
>   
> For example, suppose a colleague has a question she thinks I might know the answer to. Good news: I have some intuition and say something. Then we realize it doesn’t quite make sense, and go back and forth until we converge on something correct.   
>   
> Such a conversation is full of BS but crucially we can interrogate it and get something useful out of it in the end. Moreover this kind of back and forth allows us to get to the key point in a way that might be difficult when reading a difficult \~50\-page paper.   
>   
> To be clear o3\-mini\-high is orders of magnitude less useful for this sort of thing than talking to an expert colleague. But still useful along similar dimensions (and with a much broader knowledge base).*

[Daniel Litt](https://twitter.com/littmath/status/1885716052304077088)

---

**Link** 2025\-02\-02 [Hacker News conversation on feature flags](https://news.ycombinator.com/item?id=42899778#42900221):

I posted the following comment in a thread on Hacker News about feature flags, in response to this article [It’s OK to hardcode feature flags](https://code.mendhak.com/hardcode-feature-flags/). This kicked off a *very* high quality conversation on build\-vs\-buy and running feature flags at scale involving a bunch of very experienced and knowledgeable people. I recommend reading the comments.

> The single biggest value add of feature flags is that they de\-risk deployment. They make it less frightening and difficult to turn features on and off, which means you'll do it more often. This means you can build more confidently and learn faster from what you build. That's worth a lot.
> 
> I think there's a reasonable middle ground\-point between having feature flags in a JSON file that you have to redeploy to change and using an (often expensive) feature flags as a service platform: roll your own simple system.
> 
> A relational database lookup against primary keys in a table with a dozen records is effectively free. Heck, load the entire collection at the start of each request \- through a short lived cache if your profiling says that would help.
> 
> Once you start getting more complicated (flags enabled for specific users etc) you should consider build\-vs\-buy more seriously, but for the most basic version you really can have no\-deploy\-changes at minimal cost with minimal effort.
> 
> There are probably good open source libraries you can use here too, though I haven't gone looking for any in the last five years.

---

**Link** 2025\-02\-02 [A professional workflow for translation using LLMs](https://news.ycombinator.com/item?id=42897856):

Tom Gally is a [professional translator](https://gally.net/translation.html) who has been exploring the use of LLMs since the release of GPT\-4\. In this Hacker News comment he shares a detailed workflow for how he uses them to assist in that process.

Tom starts with the source text and custom instructions, including context for how the translation will be used. [Here's an imaginary example prompt](https://www.gally.net/temp/20250201sampletranslationprompt.html), which starts:

> `The text below in Japanese is a product launch presentation for Sony's new gaming console, to be delivered by the CEO at Tokyo Game Show 2025. Please translate it into English. Your translation will be used in the official press kit and live interpretation feed. When translating this presentation, please follow these guidelines to create an accurate and engaging English version that preserves both the meaning and energy of the original: [...]`

It then lists some tone, style and content guidelines custom to that text.

Tom runs that prompt through several different LLMs and starts by picking sentences and paragraphs from those that form a good basis for the translation.

As he works on the full translation he uses Claude to help brainstorm alternatives for tricky sentences:

> When I am unable to think of a good English version for a particular sentence, I give the Japanese and English versions of the paragraph it is contained in to an LLM (usually, these days, Claude) and ask for ten suggestions for translations of the problematic sentence. Usually one or two of the suggestions work fine; if not, I ask for ten more. (Using an LLM as a sentence\-level thesaurus on steroids is particularly wonderful.)

He uses another LLM and prompt to check his translation against the original and provide further suggestions, which he occasionally acts on. Then as a final step he runs the finished document through a text\-to\-speech engine to try and catch any "minor awkwardnesses" in the result.

I *love* this as an example of an expert using LLMs as tools to help further elevate their work. I'd love to read more examples [like this one](https://news.ycombinator.com/item?id=42897856) from experts in other fields.

---

**Link** 2025\-02\-02 [llm\-anthropic](https://github.com/simonw/llm-anthropic):

I've renamed my [llm\-claude\-3](https://github.com/simonw/llm-claude-3) plugin to `llm-anthropic`, on the basis that Claude 4 will probably happen at some point so this is a better name for the plugin.

If you're a previous user of `llm-claude-3` you can upgrade to the new plugin like this:

```
llm install -U llm-claude-3
```

This should remove the old plugin and install the new one, because the latest `llm-claude-3` depends on `llm-anthropic`. Just installing `llm-anthropic` may leave you with both plugins installed at once.

There is one extra manual step you'll need to take during this upgrade: creating a new `anthropic` stored key with the same API token you previously stored under `claude`. You can do that like so:

```
llm keys set anthropic --value "$(llm keys get claude)"
```

I released [llm\-anthropic 0\.12](https://github.com/simonw/llm-anthropic/releases/tag/0.12) yesterday with new features not previously included in `llm-claude-3`:

> * Support for Claude's [prefill](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response) feature, using the new `-o prefill '{'` option and the accompanying `-o hide_prefill 1` option to prevent the prefill from being included in the output text. [\#2](https://github.com/simonw/llm-anthropic/issues/2)
> * New `-o stop_sequences '```'` option for specifying one or more stop sequences. To specify multiple stop sequences pass a JSON array of strings :`-o stop_sequences '["end", "stop"]`.
> * Model options are now documented in the README.

If you install or upgrade `llm-claude-3` you will now get `llm-anthropic` instead, thanks to a tiny package on PyPI which depends on the new plugin name. I created that with my [pypi\-rename](https://github.com/simonw/pypi-rename) cookiecutter template.

Here's the [issue for the rename](https://github.com/simonw/llm-claude-3/issues/31). I archived the [llm\-claude\-3 repository on GitHub](https://github.com/simonw/llm-claude-3), and got to use the brand new [PyPI archiving feature](https://simonwillison.net/2025/Jan/30/pypi-now-supports-project-archival/) to archive the [llm\-claude\-3 project on PyPI](https://pypi.org/project/llm-claude-3/) as well.

---

**Quote** 2025\-02\-02

> *\[In response to a question about releasing model weights]   
>   
> Yes, we are discussing. I personally think we have been on the wrong side of history here and need to figure out a different open source strategy; not everyone at OpenAI shares this view, and it's also not our current highest priority.*

[Sam Altman](https://www.reddit.com/r/OpenAI/comments/1ieonxv/comment/maa0dcx/)

---

**Quote** 2025\-02\-02

> *Part of the concept of ‘Disruption’ is that important new technologies tend to be bad at the things that matter to the previous generation of technology, but they do something else important instead. Asking if an LLM can do very specific and precise information retrieval might be like asking if an Apple II can match the uptime of a mainframe, or asking if you can build Photoshop inside Netscape. No, they can’t really do that, but that’s not the point and doesn’t mean they’re useless. They do something else, and that ‘something else’ matters more and pulls in all of the investment, innovation and company creation. Maybe, 20 years later, they can do the old thing too \- maybe you can run a bank on PCs and build graphics software in a browser, eventually \- but that’s not what matters at the beginning. They unlock something else.   
>   
> What is that ‘something else’ for generative AI, though? How do you think conceptually about places where that error rate is a feature, not a bug?*

[Benedict Evans](https://www.ben-evans.com/benedictevans/2025/1/the-problem-with-better-models)

---

**Link** 2025\-02\-02 [OpenAI reasoning models: Advice on prompting](https://platform.openai.com/docs/guides/reasoning#advice-on-prompting):

OpenAI's documentation for their o1 and o3 "reasoning models" includes some interesting tips on how to best prompt them:

> * **Developer messages are the new system messages:** Starting with `o1-2024-12-17`, reasoning models support `developer` messages rather than `system` messages, to align with the [chain of command behavior described in the model spec](https://cdn.openai.com/spec/model-spec-2024-05-08.html#follow-the-chain-of-command).

This appears to be a purely aesthetic change made for consistency with their [instruction hierarchy](https://simonwillison.net/2024/Apr/23/the-instruction-hierarchy/) concept. As far as I can tell the old `system` prompts continue to work exactly as before \- you're encouraged to use the new `developer` message type but it has no impact on what actually happens.

Since my LLM tool already bakes in a `llm --system "system prompt"` option which works across multiple different models from different providers I'm not going to rush to adopt this new language!

> * **Use delimiters for clarity:** Use delimiters like markdown, XML tags, and section titles to clearly indicate distinct parts of the input, helping the model interpret different sections appropriately.

Anthropic have been encouraging [XML\-ish delimiters](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags) for a while (I say \-ish because there's no requirement that the resulting prompt is valid XML). My [files\-to\-prompt](https://github.com/simonw/files-to-prompt) tool has a `-c` option which outputs Claude\-style XML, and in my experiments this same option works great with o1 and o3 too:

```
git clone <https://github.com/tursodatabase/limbo>
cd limbo/bindings/python

files-to-prompt . -c | llm -m o3-mini \
  -o reasoning_effort high \
  --system 'Write a detailed README with extensive usage examples'
```

> * **Limit additional context in retrieval\-augmented generation (RAG):** When providing additional context or documents, include only the most relevant information to prevent the model from overcomplicating its response.

This makes me thing that o1/o3 are not good models to implement RAG on at all \- with RAG I like to be able to dump as much extra context into the prompt as possible and leave it to the models to figure out what's relevant.

> * **Try zero shot first, then few shot if needed:** Reasoning models often don't need few\-shot examples to produce good results, so try to write prompts without examples first. If you have more complex requirements for your desired output, it may help to include a few examples of inputs and desired outputs in your prompt. Just ensure that the examples align very closely with your prompt instructions, as discrepancies between the two may produce poor results.

Providing examples remains the single most powerful prompting tip I know, so it's interesting to see advice here to only switch to examples if zero\-shot doesn't work out.

> * **Be very specific about your end goal:** In your instructions, try to give very specific parameters for a successful response, and encourage the model to keep reasoning and iterating until it matches your success criteria.

This makes sense: reasoning models "think" until they reach a conclusion, so making the goal as unambiguous as possible leads to better results.

> * **Markdown formatting:** Starting with `o1-2024-12-17`, reasoning models in the API will avoid generating responses with markdown formatting. To signal to the model when you **do** want markdown formatting in the response, include the string `Formatting re-enabled` on the first line of your `developer` message.

This one was a *real shock* to me! I noticed that o3\-mini was outputting `•` characters instead of Markdown `*` bullets and initially thought [that was a bug](https://twitter.com/simonw/status/1886121477822648441).

I first saw this while running this prompt against [limbo/bindings/python](https://github.com/tursodatabase/limbo/tree/main/bindings/python) using [files\-to\-prompt](https://github.com/simonw/files-to-prompt):

```
git clone <https://github.com/tursodatabase/limbo>
cd limbo/bindings/python

files-to-prompt . -c | llm -m o3-mini \
  -o reasoning_effort high \
  --system 'Write a detailed README with extensive usage examples'
```

Here's the [full result](https://gist.github.com/simonw/f8283d68e9bd7ad3f140d52cad6874a7), which includes text like this (note the weird bullets):

```
Features
--------
• High‑performance, in‑process database engine written in Rust
• SQLite‑compatible SQL interface
• Standard Python DB‑API 2.0–style connection and cursor objects
```

I ran it again with this modified prompt: \> `Formatting re-enabled. Write a detailed README with extensive usage examples.` And this time got back [proper Markdown, rendered in this Gist](https://gist.github.com/simonw/adf64108d65cd5c10ac9fce953ab437e). That did a really good job, and included bulleted lists using this valid Markdown syntax instead:

```
- </span><span class="pl-c1">make test</span><span class="pl-s">: Run tests using pytest.
- </span><span class="pl-c1">make lint</span><span class="pl-s">: Run linters (via [ruff](<https://github.com/astral-sh/ruff>)).
- </span><span class="pl-c1">make check-requirements</span><span class="pl-s">: Validate that the </span><span class="pl-c1">requirements.txt</span><span class="pl-s"> files are in sync with </span><span class="pl-c1">pyproject.toml</span><span class="pl-s">.
- </span><span class="pl-c1">make compile-requirements</span><span class="pl-s">: Compile the </span><span class="pl-c1">requirements.txt</span><span class="pl-s"> files using pip-tools.
```

[![Py-Limbo. Py-Limbo is a lightweight, in-process, OLTP (Online Transaction Processing) database management system built as a Python extension module on top of Rust. It is designed to be compatible with SQLite in both usage and API, while offering an opportunity to experiment with Rust-backed database functionality. Note: Py-Limbo is a work-in-progress (Alpha stage) project. Some features (e.g. transactions, executemany, fetchmany) are not yet supported. Table of Contents - then a hierarchical nested table of contents.](https://substackcdn.com/image/fetch/$s_!Dg_N!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F20829711-d79e-4f2b-976c-459151e6348c_1396x1572.jpeg "Py-Limbo. Py-Limbo is a lightweight, in-process, OLTP (Online Transaction Processing) database management system built as a Python extension module on top of Rust. It is designed to be compatible with SQLite in both usage and API, while offering an opportunity to experiment with Rust-backed database functionality. Note: Py-Limbo is a work-in-progress (Alpha stage) project. Some features (e.g. transactions, executemany, fetchmany) are not yet supported. Table of Contents - then a hierarchical nested table of contents.")](https://substackcdn.com/image/fetch/$s_!Dg_N!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F20829711-d79e-4f2b-976c-459151e6348c_1396x1572.jpeg)

(Using LLMs like this to get me off the ground with under\-documented libraries is a trick I use several times a month.)

---