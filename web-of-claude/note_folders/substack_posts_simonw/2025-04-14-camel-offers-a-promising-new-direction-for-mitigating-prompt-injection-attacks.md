# CaMeL offers a promising new direction for mitigating prompt injection attacks

*GPT-4.1: Three new million token input models from OpenAI, including their cheapest model yet*

Published: 2025-04-14
Source: https://simonw.substack.com/p/camel-offers-a-promising-new-direction

---

In this newsletter:

* CaMeL offers a promising new direction for mitigating prompt injection attacks
* GPT\-4\.1: Three new million token input models from OpenAI, including their cheapest model yet

Plus 5 links and 2 quotations

### [CaMeL offers a promising new direction for mitigating prompt injection attacks](https://simonwillison.net/2025/Apr/11/camel/) \- 2025\-04\-11

In the [two and a half years](https://simonwillison.net/series/prompt-injection/) that we've been talking about prompt injection attacks I've seen alarmingly little progress towards a robust solution. The new paper **[Defeating Prompt Injections by Design](https://arxiv.org/abs/2503.18813)** from Google DeepMind *finally* bucks that trend. This one is worth paying attention to.

If you're new to prompt injection attacks the very short version is this: what happens if someone emails my LLM\-driven assistant (or "agent" if you like) and tells it to forward all of my emails to a third party? Here's [an extended explanation](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/) of why it's so hard to prevent this from being a show\-stopping security issue which threatens the dream digital assistants that everyone is trying to build.

The original sin of LLMs that makes them vulnerable to this is when trusted prompts from the user and untrusted text from emails/web pages/etc are concatenated together into the same token stream. I called it "prompt injection" because it's the same anti\-pattern as [SQL injection](https://en.wikipedia.org/wiki/SQL_injection).

Sadly, there is no known reliable way to have an LLM follow instructions in one category of text while safely applying those instructions to another category of text.

That's where **CaMeL** comes in.

The [new DeepMind paper](https://arxiv.org/abs/2503.18813) introduces a system called CaMeL (short for CApabilities for MachinE Learning). The goal of CaMeL is to safely take a prompt like "Send Bob the document he requested in our last meeting" and execute it, taking into account the risk that there might be malicious instructions somewhere in the context that attempt to over\-ride the user's intent.

It works by taking a command from a user, converting that into a sequence of steps in a Python\-like programming language, then checking the inputs and outputs of each step to make absolutely sure the data involved is only being passed on to the right places.

* [Addressing a flaw in my Dual\-LLM pattern](https://simonwillison.net/2025/Apr/11/camel/#addressing-a-flaw-in-my-dual-llm-pattern)
* [Fixing that with capabilities and a custom interpreter](https://simonwillison.net/2025/Apr/11/camel/#fixing-that-with-capabilities-and-a-custom-interpreter)
* [A neat privacy bonus](https://simonwillison.net/2025/Apr/11/camel/#a-neat-privacy-bonus)
* [The best part is it doesn't use more AI](https://simonwillison.net/2025/Apr/11/camel/#the-best-part-is-it-doesn-t-use-more-ai)
* [So, are prompt injections solved now?](https://simonwillison.net/2025/Apr/11/camel/#so-are-prompt-injections-solved-now-)
* [Camels have two humps](https://simonwillison.net/2025/Apr/11/camel/#camels-have-two-humps)

#### Addressing a flaw in my Dual\-LLM pattern

I'll admit that part of the reason I'm so positive about this paper is that it builds on some of my own work!

Back in April 2023 I proposed [The Dual LLM pattern for building AI assistants that can resist prompt injection](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/). I theorized a system with two separate LLMs: a privileged LLM with access to tools that the user prompts directly, and a quarantined LLM it can call that has no tool access but is designed to be exposed to potentially untrustworthy tokens.

Crucially, at no point is content handled by the quarantined LLM (Q\-LLM) exposed to the privileged LLM (P\-LLM). Instead, the Q\-LLM populates references \- `$email-summary-1` for example \- and the P\-LLM can then say "Display `$email-summary-1` to the user" without being exposed to those potentially malicious tokens.

The DeepMind paper references this work early on, and then describes a new\-to\-me flaw in my design:

> A significant step forward in defense strategies is the Dual LLM pattern theoretically described by Willison (2023\). This pattern employs two LLMs: a Privileged LLM and a Quarantined LLM. The Privileged LLM is tasked with planning the sequence of actions needed to fulfill the user’s request, such as searching the cloud storage for the meeting notes and fetching the requested document from the cloud storage, and sending it to the client. Importantly, this privileged LLM only sees the initial user query and never the content from potentially compromised data sources (like the file content).
> 
> The actual processing of potentially malicious data, like extracting the name of the document to send and the client’s email address, would be delegated to the Quarantined LLM. This Quarantined LLM, crucially, is stripped of any tool\-calling capabilities, limiting the harm an injected prompt can cause and guaranteeing that the adversary cannot call arbitrary tools with arbitrary arguments.
> 
> **Is Dual LLM of Willison enough?** While the Dual LLM pattern significantly enhances security by isolating planning from being hijacked by malicious content, it does not completely eliminate all prompt injection risks. Let us consider the example depicted in Figure 1\. Here, even with the Dual LLM in place we show that vulnerabilities still exist.

Here's figure 1:

[![Flowchart diagram showing document retrieval process: At top, a stick figure labeled "User" with a yellow speech bubble stating "Can you send Bob the document he requested in our last meeting? Bob's email and the document he asked for are in the meeting notes file." Two database cylinders labeled "Notes" and "Drive" are connected to a red dashed box containing workflow steps in red circles: "Find recent meeting notes" → "Extract doc name" and "Extract email address" → "Fetch document by name" → "Send document to email". Green arrows show data flow between steps, with labels "Data Flow" and "Control Flow" on the sides of the box.](https://substackcdn.com/image/fetch/$s_!T3-I!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5ec84b9-51cd-4377-a958-66cd23445847_1278x1172.jpeg "Flowchart diagram showing document retrieval process: At top, a stick figure labeled \"User\" with a yellow speech bubble stating \"Can you send Bob the document he requested in our last meeting? Bob's email and the document he asked for are in the meeting notes file.\" Two database cylinders labeled \"Notes\" and \"Drive\" are connected to a red dashed box containing workflow steps in red circles: \"Find recent meeting notes\" → \"Extract doc name\" and \"Extract email address\" → \"Fetch document by name\" → \"Send document to email\". Green arrows show data flow between steps, with labels \"Data Flow\" and \"Control Flow\" on the sides of the box.")](https://substackcdn.com/image/fetch/$s_!T3-I!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5ec84b9-51cd-4377-a958-66cd23445847_1278x1172.jpeg)

The user's prompt here is:

> Can you send Bob the document he requested in our last meeting? Bob's email and the document he asked for are in the meeting notes file.

And there lies the flaw. With the Dual LLM pattern the P\-LLM delegates the task of finding Bob's email address to the Q\-LLM \- but the Q\-LLM is still exposed to potentially malicious instructions. An attacker could use those instructions to over\-ride that retrieved email address and cause the document to be exfiltrated to an attacker\-chosen address.

#### Fixing that with capabilities and a custom interpreter

CaMeL addresses this problem directly using some very clever security engineering.

In CaMeL, the user's prompt is converted by the P\-LLM into a sequence of steps that are described using code. They chose to use a locked\-down subset of Python for this, because every available LLM is good at writing Python already:

> We build a custom Python interpreter that operates over a restricted version of Python. We choose Python as it is a very popular programming language, and large language models are very competent at writing it. We use Python’s built\-in ast library to parse the abstract syntax tree, and interpret each tree node in a recursive fashion.

Consider the prompt "Find Bob's email in my last email and send him a reminder about tomorrow's meeting". CaMeL would convert that into code looking something like this:

```
email = get_last_email()
address = query_quarantined_llm(
    "Find Bob's email address in [email]",
    output_schema=EmailStr
)
send_email(
    subject="Meeting tomorrow",
    body="Remember our meeting tomorrow",
    recipient=address,
)
```

As you can see, this code combines several calls to tools that are exposed as Python functions \- one to retrieve the last email, one that uses a quarantined LLM to extract Bob's email address from it and one to send a new email.

Here's where things get clever: by using a custom interpreter, CaMeL can apply extra rules to the code that is executed. It can keep track of which variables were derived from which other variables and apply security policies that take that trail into account.

In this example, `email` is a potential source of untrusted tokens, which means `address` is as well (since it is derived from `email`).

The security rules to apply are as follows:

* **get\_last\_email**: always allowed
* **send\_email**: only if `recipient` is trusted

If the `address` (passed to `send_email` as the `recipient` parameter) is a known, trusted adress \- based on policies set by the user \- the system can send that email without prompting first. If it's an unknown email the user can be asked to approve the message.

**Capabilities** are effectively tags that can be attached to each of the variables, to track things like who is allowed to read a piece of data and the source that the data came from. **Policies** can then be configured to allow or deny actions based on those capabilities.

#### A neat privacy bonus

There are other potential benefits to this design as well. The P\-LLM needs to be quite sophisticated, as it's responsible for building a plan and then generating code in the custom Python dialect. The Q\-LLM can be a whole lot less powerful:

> As parsing data is likely to be easier than creating a plan and writing code for the user’s query, one could use a smaller language model for the Q\-LLM. On top of being faster and cheaper, this LLM can potentially also be run locally on the user’s machine. This would improve the user’s privacy with respect to the model provider: since the LLM used as the P\-LLM is only provided with the user query, the P\-LLM provider never sees the tool outputs (which might contain sensitive information that should not be shared with the P\-LLM provider).

This means a CaMeL system could use a cloud\-hosted LLM as the driver while keeping the user's own private data safely restricted to their own personal device.

#### The best part is it doesn't use more AI

Most of the proposed solutions I have seen to prompt injection to date involve layering on even more AI. I wrote about why I think this is a bad idea in [You can’t solve AI security problems with more AI](https://simonwillison.net/2022/Sep/17/prompt-injection-more-ai/). AI techniques use probabilities: you can train a model on a collection of previous prompt injection examples and get to a 99% score in detecting new ones... and that's useless, because in application security [99% is a failing grade](https://simonwillison.net/2023/May/2/prompt-injection-explained/#prompt-injection.015):

[![Slide: in application security 99% is a failing grade](https://substackcdn.com/image/fetch/$s_!4gOO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69c5be96-148a-4b61-a1ab-817e4d32ba65_1920x1080.jpeg "Slide: in application security 99% is a failing grade")](https://substackcdn.com/image/fetch/$s_!4gOO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69c5be96-148a-4b61-a1ab-817e4d32ba65_1920x1080.jpeg)

The job of an adversarial attacker is to find the 1% of attacks that get through. If we protected against SQL injection or XSS using methods that fail 1% of the time our systems would be hacked to pieces in moments.

The CaMeL proposal recognizes this:

> CaMeL is a practical defense to prompt injection achieving security not through model training techniques but through principled system design around language models. Our approach effectively solves the AgentDojo benchmark while providing strong guarantees against unintended actions and data exfiltration. \[…]

This is the first mitigation for prompt injection I've seen that claims to provide **strong guarantees**! Coming from security researchers that's a very high bar.

#### So, are prompt injections solved now?

Quoting section 8\.3 from the paper:

> **8\.3\. So, are prompt injections solved now?**
> 
> No, prompt injection attacks are not fully solved. While CaMeL significantly improves the security of LLM agents against prompt injection attacks and allows for fine\-grained policy enforcement, it is not without limitations.
> 
> Importantly, CaMeL suffers from users needing to codify and specify security policies and maintain them. CaMeL also comes with a user burden. At the same time, it is well known that balancing security with user experience, especially with de\-classification and user fatigue, is challenging.

By "user fatigue" they mean that thing where if you constantly ask a user to approve actions ("Really send this email?", "Is it OK to access this API?", "Grant access to your bank account?") they risk falling into a fugue state where they say "yes" to everything.

This can affect the most cautious among us. Security researcher Troy Hunt [fell for a phishing attack](https://simonwillison.net/2025/Apr/4/a-sneaky-phish/) just last month due to jetlag\-induced tiredness.

Anything that requires end users to think about security policies also makes me deeply nervous. I have enough trouble thinking through those myself (I still haven't fully figured out AWS IAM) and I've been involved in application security for two decades!

CaMeL really does represent a promising path forward though: the first credible prompt injection mitigation I've seen that *doesn't* just throw more AI at the problem and instead leans on tried\-and\-proven concepts from security engineering, like capabilities and data flow analysis.

My hope is that there's a version of this which combines robustly selected defaults with a clear user interface design that can finally make the dreams of general purpose digital assistants a secure reality.

#### Camels have two humps

Why did they pick CaMeL as the abbreviated name for their system? I like to think it's because camels have two humps, and CaMeL is an improved evolution of my dual LLM proposal.

---

### [GPT\-4\.1: Three new million token input models from OpenAI, including their cheapest model yet](https://simonwillison.net/2025/Apr/14/gpt-4-1/) \- 2025\-04\-14

OpenAI [introduced](https://openai.com/index/gpt-4-1/) three new models this morning: GPT\-4\.1, GPT\-4\.1 mini and GPT\-4\.1 nano. These are API\-only models right now, not available through the ChatGPT interface (though you can try them out in OpenAI's [API playground](https://platform.openai.com/playground)). All three models can handle 1,047,576 tokens of input and 32,768 tokens of output, and all three have a May 31, 2024 cut\-off date (their previous models were mostly September 2023\).

The models score higher than GPT\-4o *and* GPT\-4\.5 on coding benchmarks, and do very well on long context benchmarks as well. They also claim improvements in instruction following \- following requested formats, obeying negative instructions, sorting output and obeying instructions to say "I don't know".

I released a new version of my [llm\-openai](https://github.com/simonw/llm-openai-plugin) plugin supporting the new models. This is a new thing for the [LLM](https://llm.datasette.io/) ecosystem: previously OpenAI models were only supported in core, which meant I had to ship a full LLM release to add support for them.

You can run the new models like this:

```
llm install llm-openai-plugin -U
llm -m openai/gpt-4.1 "Generate an SVG of a pelican riding a bicycle"
```

The other model IDs are `openai/gpt-4.1-mini` and `openai/gpt-4.1-nano`.

Here's the [pelican riding a bicycle](https://simonwillison.net/tags/pelican-riding-a-bicycle/) I got from full sized GPT\-4\.1:

[![Not a terrible pelican on a bicycle. The frame is blue, though misshapen. The pelican's legs are detached from its body. It has a nice but square beak.](https://substackcdn.com/image/fetch/$s_!eFuh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff161b707-1c01-46ab-9b59-59094ba0cd5f_800x457.jpeg "Not a terrible pelican on a bicycle. The frame is blue, though misshapen. The pelican's legs are detached from its body. It has a nice but square beak.")](https://substackcdn.com/image/fetch/$s_!eFuh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff161b707-1c01-46ab-9b59-59094ba0cd5f_800x457.jpeg)

I'm particularly excited by [GPT\-4\.1 nano](https://platform.openai.com/docs/models/gpt-4.1-nano), which handles image and text input up to a million tokens and is priced lower than any other previous OpenAI model: $0\.10/million for input and $0\.40/million for output, less than previous cheapest OpenAI model GPT\-4o\-mini ($0\.15/$0\.60\). I've updated my [LLM pricing table](https://tools.simonwillison.net/llm-prices) to include the new models.

They're not the cheapest overall though: Gemini 2\.0 Flash Lite and, Gemini 1\.5 Flash 8B, Amazon Nova Lite and Nova Micro and Mistral's 3B, 8B and Small 3\.1 hosted models remain less expensive.

[![Screenshot of the table from that LLM pricing table link above. Amazon Nova Micro is cheapest at $0.035/million input tokens.](https://substackcdn.com/image/fetch/$s_!FgI_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F42cc5e80-d1f6-47b9-9352-ddf19060b7b9_1240x1380.jpeg "Screenshot of the table from that LLM pricing table link above. Amazon Nova Micro is cheapest at $0.035/million input tokens.")](https://substackcdn.com/image/fetch/$s_!FgI_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F42cc5e80-d1f6-47b9-9352-ddf19060b7b9_1240x1380.jpeg)

As a demonstration of just how cheap GPT\-4\.1 nano is, consider this photograph I took of some pelicans:

[![Description to follow](https://substackcdn.com/image/fetch/$s_!QTZF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5cc8d991-68cc-4b41-9f77-47f44684edc5_1086x724.jpeg "Description to follow")](https://substackcdn.com/image/fetch/$s_!QTZF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5cc8d991-68cc-4b41-9f77-47f44684edc5_1086x724.jpeg)

I ran that through GPT\-4\.1 nano like this:

```
llm -m openai/gpt-4.1-nano describe \
  -a https://static.simonwillison.net/static/2025/two-pelicans.jpg
```

And got back this response:

> The image shows two pelicans flying against a clear blue sky. They are positioned in flight, with their wings extended, showcasing their large wingspan and feather patterns. The pelican on the right appears slightly higher and facing slightly to the left, while the pelican on the left is oriented more horizontally with its beak pointing forward. Both birds display a combination of brown, tan, and white plumage, characteristic of pelicans, with their long beaks prominently visible.

Running `llm logs -c --usage` revealed that this used 1,933 input tokens and 96 output tokens. Passing those through [the pricing calculator](https://tools.simonwillison.net/llm-prices) returns a total cost of $0\.000232, or 0\.0232 cents.

That means I could use GPT\-4\.1 nano to generate descriptions of 4,310 images like this one for just shy of a dollar.

A few closing thoughts on these new models:

* The 1 million input token context thing is a *really big deal*. The huge token context has been a major competitive advantage for the Google Gemini models for a full year at this point \- it's reassuring to see other vendors start to catch up. I'd like to see the same from Anthropic \- Claude was the first model to hit 200,000 but hasn't shipped more than that yet (aside from a 500,000 token model that was restricted to their big enterprise partners).
* When I added [fragments support](https://simonwillison.net/2025/Apr/7/long-context-llm/) to LLM last week the feature was mainly designed to help take advantage of longer context models. It's pleasing to see another one show up so shortly after that release.
* OpenAI really emphasized code performance for this model. They called out the [Aider benchmark](https://aider.chat/docs/leaderboards/) in their announcement post.
* [As expected](https://simonwillison.net/2025/Feb/27/introducing-gpt-45/#confidence), GPT\-4\.5 turned out to be not long for this world:

> We will also begin deprecating GPT‑4\.5 Preview in the API, as GPT‑4\.1 offers improved or similar performance on many key capabilities at much lower cost and latency. GPT‑4\.5 Preview will be turned off in three months, on July 14, 2025, to allow time for developers to transition

* In [the livestream announcement](https://www.youtube.com/watch?v=kA-P9ood-cE) Michelle Pokrass [let slip](https://www.youtube.com/live/kA-P9ood-cE?t=641s) that the codename for the model was Quasar \- that's the name of the stealth model that's [been previewing on OpenRouter](https://openrouter.ai/announcements/stealth-model-quasar-alpha) for the past two weeks. That has [now been confirmed](https://twitter.com/openrouterai/status/1911833662464864452) by OpenRouter.
* OpenAI shared a [GPT 4\.1 Prompting Guide](https://cookbook.openai.com/examples/gpt4-1_prompting_guide), which includes this tip about long context prompting:

> Especially in long context usage, placement of instructions and context can impact performance. If you have long context in your prompt, ideally place your instructions at both the beginning and end of the provided context, as we found this to perform better than only above or below. If you’d prefer to only have your instructions once, then above the provided context works better than below.

* Adding instructions before the content is incompatible with [prompt caching](https://platform.openai.com/docs/guides/prompt-caching) \- I always keep user instructions at the end since doing so means multiple prompts can benefit from OpenAI's prefix cache.

They also recommend XML\-style delimiters over JSON for long context, suggesting this format (complete with the XML\-invalid unquoted attribute) that's similar to the format [recommended by Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags) for Claude:

```
<doc id=1 title="The Fox">The quick brown fox jumps over the lazy dog</doc>
```

* There's an extensive section at the end [describing their recommended approach to applying file diffs](https://cookbook.openai.com/examples/gpt4-1_prompting_guide#appendix-generating-and-applying-file-diffs): "we open\-source here one recommended diff format, on which the model has been extensively trained".
* One thing notably absent from the GPT\-4\.1 announcement is any mention of audio support. The "o" in GPT\-4o stood for "omni", because it was a multi\-modal model with image and audio input and output. The 4\.1 models appear to be text and image input and text output only.

---

**Link** 2025\-04\-11 [Default styles for h1 elements are changing](https://developer.mozilla.org/en-US/blog/h1-element-styles/):

Wow, this is a rare occurrence! Firefox are rolling out a change to the default user\-agent stylesheet for nested `<h1>` elements, currently ramping from 5% to 50% of users and with full roll\-out planned for Firefox 140 in June 2025\. Chrome is showing deprecation warnings and Safari are expected to follow suit in the future.

What's changing? The default sizes of `<h1>` elements that are nested inside `<article>`, `<aside>`, `<nav>` and `<section>`.

These are the default styles being removed:

> ```
> / where x is :is(article, aside, nav, section) /
> x h1 { margin-block: 0.83em; font-size: 1.50em; }
> x x h1 { margin-block: 1.00em; font-size: 1.17em; }
> x x x h1 { margin-block: 1.33em; font-size: 1.00em; }
> x x x x h1 { margin-block: 1.67em; font-size: 0.83em; }
> x x x x x h1 { margin-block: 2.33em; font-size: 0.67em; }
> ```

The short version is that, many years ago, the HTML spec introduced the idea that an `<h1>` within a nested section should have the same meaning (and hence visual styling) as an `<h2>`. This never really took off and wasn't reflected by the accessibility tree, and was removed from the HTML spec in 2022\. The browsers are now trying to cleanup the legacy default styles.

This advice from that post sounds sensible to me:

> * **Do not** rely on default browser styles for conveying a heading hierarchy. Explicitly define your document hierarchy using `<h2>` for second\-level headings, `<h3>` for third\-level, etc.
> * Always define your own `font-size` and `margin` for `<h1>` elements.

---

**Link** 2025\-04\-11 [llm\-fragments\-rust](https://github.com/huitseeker/llm-fragments-rust):

Inspired by Filippo Valsorda's [llm\-fragments\-go](https://simonwillison.net/2025/Apr/10/llm-fragments-go/), Francois Garillot created `llm-fragments-rust`, an [LLM fragments](https://simonwillison.net/2025/Apr/7/long-context-llm/) plugin that lets you pull documentation for any Rust crate directly into a prompt to LLM.

I really like this example, which uses two fragments to load documentation for two crates at once:

> `llm -f rust:rand@0.8.5 -f rust:tokio "How do I generate random numbers asynchronously?"`

The [code](https://github.com/huitseeker/llm-fragments-rust/blob/main/llm_fragments_rust.py) uses some neat tricks: it creates a new Rust project in a temporary directory (similar to how `llm-fragments-go` works), adds the crates and uses `cargo doc --no-deps --document-private-items` to generate documentation. Then it runs `cargo tree --edges features` to add dependency information, and `cargo metadata --format-version=1` to include additional metadata about the crate.

---

**Quote** 2025\-04\-12

> ***Backticks** are traditionally banned from use in future language features, due to the small symbol. No reader should need to distinguish* ``` *from* `'` *at a glance.*

[Steve Dower](https://discuss.python.org/t/pep-750-tag-strings-for-writing-domain-specific-languages/60408/57)

---

**Quote** 2025\-04\-12

> ***Slopsquatting** \-\- when an LLM hallucinates a non\-existent package name, and a bad actor registers it maliciously. The AI brother of typosquatting.   
>   
> Credit to [@sethmlarson](https://fosstodon.org/@sethmlarson) for the name*

[Andrew Nesbitt](https://mastodon.social/@andrewnez/114302875075999244)

---

**Link** 2025\-04\-13 [Stevens: a hackable AI assistant using a single SQLite table and a handful of cron jobs](https://www.geoffreylitt.com/2025/04/12/how-i-made-a-useful-ai-assistant-with-one-sqlite-table-and-a-handful-of-cron-jobs):

Geoffrey Litt reports on Stevens, a shared digital assistant he put together for his family using SQLite and scheduled tasks running on Val Town.

The design is refreshingly simple considering how much it can do. Everything works around a single `memories` table. A memory has text, tags, creation metadata and an optional `date` for things like calendar entries and weather reports.

Everything else is handled by scheduled jobs to popular weather information and events from Google Calendar, a Telegram integration offering a chat UI and a neat system where USPS postal email delivery notifications are run through Val's own email handling mechanism to trigger a Claude prompt to add those as memories too.

Here's [the full code on Val Town](https://www.val.town/x/geoffreylitt/stevensDemo), including [the daily briefing prompt](https://www.val.town/x/geoffreylitt/stevensDemo/code/dailyBriefing/sendDailyBrief.ts) that incorporates most of the personality of the bot.

---

**Link** 2025\-04\-14 [Using LLMs as the first line of support in Open Source](https://noumenal.es/posts/llms-for-user-support/WZb/):

From reading the title I was nervous that this might involve automating the initial response to a user support query in an issue tracker with an LLM, but Carlton Gibson has better taste than that.

> The **open contribution** model engendered by GitHub — where anonymous (to the project) users can create issues, and comments, which are almost always extractive support requests — results in an effective **denial\-of\-service attack against maintainers**. \[...]
> 
> For anonymous users, who really just want help almost all the time, the pattern I’m settling on is to facilitate them getting their answer from their LLM of choice. \[...] we can generate a file that we offer users to download, then we tell the user to pass this to (say) Claude with a simple prompt for their question.

This resonates with the concept proposed by [llms.txt](https://llmstxt.org/) \- making LLM\-friendly context files available for different projects.

My [simonw/docs\-for\-llms](https://github.com/simonw/docs-for-llms) contains my own early experiment with this: I'm running a build script to create LLM\-friendly concatenated documentation for several of my projects, and my [llm\-docs](https://github.com/simonw/llm-docs) plugin ([described here](https://simonwillison.net/2025/Apr/7/long-context-llm/#asking-questions-of-llm-s-documentation)) can then be used to ask questions of that documentation.

It's possible to pre\-populate the Claude UI with a prompt by linking to `https://claude.ai/new?q={PLACE_HOLDER}`, but it looks like there's quite a short length limit on how much text can be passed that way. It would be neat if you could pass a URL to a larger document instead.

ChatGPT also supports `https://chatgpt.com/?q=your-prompt-here` (again with a short length limit) and directly executes the prompt rather than waiting for you to edit it first(!)

---

**Link** 2025\-04\-14 [SQLite File Format Viewer](https://sqlite-internal.pages.dev/):

Neat browser\-based visual interface for exploring the structure of a SQLite database file, built by Visal In using React and a custom parser [implemented in TypeScript](https://github.com/invisal/sqlite-internal/tree/main/src/parser).

---