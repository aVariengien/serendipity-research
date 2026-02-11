# Fine-Tuning LLMs For Style Transfer

*Why haven't you made your own fine-tune yet?*

Published: 2024-06-14
Source: https://sarahconstantin.substack.com/p/fine-tuning-llms-for-style-transfer

---

[![](https://substackcdn.com/image/fetch/$s_!jdMt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6c27973-701c-4fc5-9cf4-c40739fa77ca_1024x1024.webp)](https://substackcdn.com/image/fetch/$s_!jdMt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6c27973-701c-4fc5-9cf4-c40739fa77ca_1024x1024.webp)

Midjourney image

I try to keep my finger at least somewhat on the AI pulse these days, and it’s striking that I don’t see that many people sharing their fine\-tuned models.

Lots of people will show you their favorite system prompts. OpenAI itself has a “[GPT Store](https://chatgpt.com/gpts)” where people can share GPTs with custom prompts, and a web\-based UI for making your own prompt\-customized GPT.

But prompting is *lousy* for making a bot with a writing style that’s substantially different from the generic ChatGPT “character”.

I have tried mightily to make bots that write “in character.” They don’t. You have to be painfully explicit about specific verbal patterns you want[1](https://sarahconstantin.substack.com/p/fine-tuning-llms-for-style-transfer#footnote-1-145650478) and even then the bot will frequently forget. You certainly can’t paste a piece of sample text from the target author into the context window and expect GPT\-4 to pick up the style; it may notice the *concepts being referred to*, but it inexorably reverts to the bland “house style.”

You know what does work? *Fine\-tuning*.

OpenAI’s fine\-tuning API is built for training on dialogue. You provide it a with JSON\-formatted file of sample text interactions between the “user” and “assistant”, and using either the [platform site](https://platform.openai.com/) or the [API](https://platform.openai.com/docs/guides/fine-tuning) you can train a fine\-tune of models up to GPT\-3\.5\-turbo on your sample dialogue file.

This works well if you generate a Q\&A file of “user” questions and “assistant” answers which are direct quotes from the target author. One easy way to do this is to extract the Q\&A from interviews with the target author. A more time\-consuming way, if you can’t find interviews, is to create the “questions” yourself, to which the quotes you want to include are answers.

This *works.*

### Example: Bene Gesserit Bot

I trained a fine\-tune of GPT\-3\.5\-turbo on 124 quotes from the [six Frank Herbert Dune books](https://www.amazon.com/Frank-Herberts-Dune-Saga-Collection-ebook/dp/B088QLJGZC/ref=sr_1_1?dib=eyJ2IjoiMSJ9.r-sXcl_6QQK6-X0NFzQtVqPB28ySrFOdhqDFpeIMRH1oRWHOgDZzegCN2JUTA_PJznE_cS9RDLqiYoMe89fQ8jtwPl1cyVqR8lu6fUh2naFgjEvg4HcqbdChrONflPYjs-_B6Q1AdtOu0vW_9s89a06--Nl3M7cNdq-rx0k8ToHWTP8P4Mvce2rp7di_uj4j.JFPOwmkW-spV4JBKYvNkhxdr8KL3uhIXKX911Cuw6XM&dib_tag=se&hvadid=557270846630&hvdev=c&hvlocphy=9004338&hvnetw=g&hvqmt=b&hvrand=16118378466193763919&hvtargid=kwd-1022026629753&hydadcr=7473_13184008&keywords=dune+book+series+1-6&qid=1718392908&rnid=2941120011&s=digital-text&sr=1-1). For each quote I created a corresponding “user question”: eg

> * Q: “How does one obtain freedom?” (*my question)*
> 
> 
> 	+ A: “Seek freedom and become captive of your desires. Seek discipline and find your liberty.” (*direct quote from* Chapterhouse: Dune)

You can try the Bene Gesserit Bot out yourself [here.](https://bene-gesserit-bot.replit.app/)

Clearly, we are no longer in Generic ChatGPT land. The fine\-tuned bot has acquired a clearly Frank\-Herbert\-inspired style, and can go to vivid, strange, surprising places.

[![](https://substackcdn.com/image/fetch/$s_!LoCe!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F35ed9b29-38a9-46c5-bb46-9f8d21885926_1384x1690.png)](https://substackcdn.com/image/fetch/$s_!LoCe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F35ed9b29-38a9-46c5-bb46-9f8d21885926_1384x1690.png)

[![](https://substackcdn.com/image/fetch/$s_!BgQ6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2a23771-ae7d-4003-9cde-ba90403eb3aa_1350x1718.png)](https://substackcdn.com/image/fetch/$s_!BgQ6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2a23771-ae7d-4003-9cde-ba90403eb3aa_1350x1718.png)

[![](https://substackcdn.com/image/fetch/$s_!j6m3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5cf42efd-57a9-494a-ba35-151ded5707a9_1426x1578.png)](https://substackcdn.com/image/fetch/$s_!j6m3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5cf42efd-57a9-494a-ba35-151ded5707a9_1426x1578.png)

I find it’s consistently more prone to non sequiturs and logical incoherence than GPT\-3\.5, as well as occasional examples of unambiguously “erroneous” gobbledegook (fragments of code, Chinese characters, etc).

On the other hand, the style transfer is clearly happening.

And “style” includes conversational attitude: Bene Gesserit Bot will spontaneously argue with and belittle the user, while it’s nearly impossible to get this behavior from prompting GPT\-3\.5\.

I also notice that the fine\-tune is a bit less rigid about content restrictions.

### So What?

Why might someone want an in\-character bot?

Well, it’s fun and potentially instructive to “chat with” a fictional character, or favorite writer. If Bene Gesserit Bot isn’t your thing, imagine, e.g., getting to talk to Socrates Bot. (That one should be easy to fine\-tune, given all the dialogue!)

If we ever get to something more like AI\-integrated video games, in\-character dialogue will be essential.

From what I hear, The Youth (TM) are already enthusiastic users of [Character AI](https://character.ai/), which seems to be clearly using “vanilla” models with a bit of custom prompting. So imagine if there were an AI chat app with any actual *variety* in conversational style!

Or, imagine simulating *actual people you know.* “What would Mom say?” With a fine\-tune, you could ask her…even after she’s gone.

### Why Isn’t This More Of A Thing?

When I search “finetune” on Twitter or HuggingFace I mostly see papers on fine\-tuning LLMs to hit general accuracy benchmarks, or general\-purpose utilities like text\-to\-speech, image captioning, or LLMs for specific languages.

Not so much fun little custom bots like my Bene Gesserit Bot.

Some counterexamples:

* [Trismegistus](https://huggingface.co/teknium/Mistral-Trismegistus-7B) is a Mixtral finetune based on occult and spiritual topics (but it’s trained on gpt\-4\-generated synthetic data and the samples given sound like “vanilla” LLM style)
* Designer [Andy Ayrey](https://x.com/AndyAyrey) shares text samples of his fine\-tunes from the Claude Opus\-generated [Infinite Backrooms dataset](https://dreams-of-an-electric-mind.webflow.io/), which touch on singularitarian themes; the finetuned results do indeed sound “in character”.
* Startup founder [Edward Donner](https://edwarddonner.com/2024/01/02/fine-tuning-an-llm-on-240k-text-messages/) trained an LLM on his own text messages.

Asking around at [LessOnline](https://less.online/) and [Manifest](https://www.manifest.is/) it also didn’t seem like that many people were generating casual fine\-tune bots, although I did meet one person who made a [glowfic](https://docs.google.com/document/d/1_4Z2zdRKaSwZPm3S0X14DYoo7w46U_MZ4En6oOediNQ/edit) finetune to solve the (niche but quite real) problem of “my favorite online writers never finished the story I was reading!”

But overall, the absence is striking to me. Fine\-tunes are *not that hard to make*. It’s a little tedious to assemble the dataset, but it takes no programming skill. And the results are super fun to interact with.

Are people just that starkly divided between “blocked by trivial inconveniences” and “professional AI developer building Super Serious models for general\-purpose applications”?

Or am I just hanging out in the wrong part of the world and there’s a lively finetune community somewhere I’ve never heard of?

Because the alternative is like…if it were the year 2000 and I didn’t know anybody who’d made a personal website.

[1](https://sarahconstantin.substack.com/p/fine-tuning-llms-for-style-transfer#footnote-anchor-1-145650478)like “use “he”, not “they”, to refer to a person of unidentified gender”