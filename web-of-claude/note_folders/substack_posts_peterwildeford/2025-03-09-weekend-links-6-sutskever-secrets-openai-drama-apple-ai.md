# Weekend Links #6: Sutskever secrets, OpenAI drama, Apple AI

*Also anything can be a movie prop if only it tries hard enough*

Published: 2025-03-09
Source: https://peterwildeford.substack.com/p/weekend-links-6-sutskever-secrets

---

[![Why CEO Sam Altman's firing at ChatGPT maker Open AI was bound to happen :  NPR](https://substackcdn.com/image/fetch/$s_!naHW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb4c86672-cc56-4f60-a5cd-f83dafd00ec0_1100x734.jpeg "Why CEO Sam Altman's firing at ChatGPT maker Open AI was bound to happen :  NPR")](https://substackcdn.com/image/fetch/$s_!naHW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb4c86672-cc56-4f60-a5cd-f83dafd00ec0_1100x734.jpeg)

*A good forecaster reads constantly. However, like the power laws this blog is named for, some readings matter far more than others. Each weekend, I'll share the standouts …along with some occasional fascinating rabbit holes. Some weekends will be light, others heavy (that's how power laws work), but each link will be worth your weekend morning coffee time.*

~

### **…Starting with a thank you!** 🎉

I just wanted to thank all the people who recently subscribed. In just the six weeks since this Substack launched, I’ve already picked up over 1000 subscribers. I can’t believe you all trust me enough to let me beam my thoughts directly into your inbox. Thank you to all of you and I’m excited to be writing for you. And thank you also to those of you who read through other channels (e.g., Twitter, LinkedIn) even if you don’t subscribe.

And if you do want to subscribe, there’s always this button:

Ok that’s enough thanking. Let’s get on with it.

# AI

### **…Sutskever's SSI secrets**

It’s a weird fact of life that nearly all major AI companies are downstream of OpenAI in some way. [Anthropic came from a split from OpenAI in 2021](https://finance.yahoo.com/news/anthropic-ceo-says-why-quit-194409797.html). xAI was founded in 2023 by Elon Musk after a dispute with OpenAI, where he was originally a co-founder. The former OpenAI CTO, Mira Murati, quit in late 2024 before launching Thinking Machines Lab in early 2025 ([covered in Links #4](https://peterwildeford.substack.com/p/weekend-links-4-faxing-chatgpt-homemade)). And ironically [OpenAI itself was founded out of a fear of Google DeepMind winning the AI race](https://www.nytimes.com/2023/12/03/technology/ai-openai-musk-page-altman.html).

Another company in this long history of exodus is Safe Superintelligence Inc., founded in 2024 by Ilya Sutskever, OpenAI’s former Chief Scientist. Not much is known about it besides its [cool six character URL and 246 word website](https://ssi.inc/). This work is shrouded in secrecy and SSI has disavowed any attempt to make products — their only goal is to make AI superintelligence, that’s it.

**Well, Sutskever must have one hell of a pitch deck because [he’s somehow landed his company $2B in a new funding at a $30B valuation](https://www.wsj.com/tech/ai/ai-safe-superintelligence-startup-ilya-sutskever-openai-2335259b).** That’s up from a $5B valuation merely six months ago. It’s also just a little less than half of [Anthropic’s recent $61.5B valuation](https://www.anthropic.com/news/anthropic-raises-series-e-at-usd61-5b-post-money-valuation), despite SSI having $0 revenue and 0 products versus [Anthropic’s ~$2B annualized revenue](https://www.reuters.com/technology/anthropic-projects-soaring-growth-345-billion-2027-revenue-information-reports-2025-02-13/), Claude 3.7 launch, and hundreds of thousands of customers.

What is SSI building? …No one really knows, except that it’s something *“different”*:

> Sutskever has told associates he isn’t developing advanced AI using the same methods he and colleagues used at OpenAI. He has said he has instead identified a “different mountain to climb” that is showing early signs of promise, according to people close to the company.

…And there is a lot of secrecy, including Faraday cages for interviews:

> Most AI startups work hard to get attention, hoping it will help attract employees and investors in a highly competitive space. SSI operates as secretly as it can out of offices in Silicon Valley and Tel Aviv. […] Its approximately 20 employees—a fraction of the 1,000-plus at OpenAI and Anthropic—are discouraged from mentioning SSI on their LinkedIn profiles, according to knowledgeable people.
>
> Candidates who secure an in-person interview are instructed to leave their phone in a Faraday cage, a container that blocks cellular and Wi-Fi signals, before entering SSI’s offices, one of the knowledgeable people said.

Sutskever contributed greatly to a lot of OpenAI’s innovations and knows pretty much all of their secrets. He’s also been very focused on the power of scaling models from way back in 2014 — the magic that has produced the models we see today. However, [in a NeurIPS talk](https://www.youtube.com/watch?v=1yvBqasHLZs), he declared that the era of “pre-training models” (scaling them up by throwing more compute at the base model) will end soon due to limitations on the amount of data we have to train models on, calling data “the fossil fuel” of AI.

Sutskever answers the question of “what comes next?” by referring to agents, synthetic data, inference-time compute (a recent trend in models to allow them to use compute to think through problems on the fly, similar to how a human would), as well as something cryptic about potentially increasing the slope on scaling laws. In the long-run, Sutskever anticipates agentic, self-aware, superintelligent AI that greatly exceeds human capabilities.

I don’t think there’s anything in this talk, or any of the small number of other Sutskever public appearances I could find that hint at what SSI is up to. It’s not even clear where the investment is going — presumably SSI needs billions of dollars to buy compute, but the team is small and there aren’t any rumors out there of NVIDIA sales orders. Curious.

~

### **…OpenAI’s legal woes**

A little under a month ago in [“AI this week: Trump, Musk, and Altman's High Stakes Games”](https://peterwildeford.substack.com/p/what-happened-in-ai-this-week-france), I discussed OpenAI's planned conversion from non-profit to for-profit. The situation is that OpenAI originally started as a non-profit with a stated mission “to ensure that artificial general intelligence benefits all of humanity”, but OpenAI now wants to convert fully from a non-profit to a “public benefit corporation”. This new entity type, which is how Anthropic is structured, is a for-profit but allowed to maximize social value in addition to shareholder value. OpenAI’s recent $6.6B in financing is contingent on transitioning to the for-profit structure and the financing will need to be paid back as a loan if the transition isn’t completed by the end of 2026.

In 2024 November, Elon Musk [sued to block OpenAI's restructuring from nonprofit to for-profit status](https://storage.courtlistener.com/recap/gov.uscourts.cand.433688/gov.uscourts.cand.433688.46.0.pdf), claiming the shift violates OpenAI’s original non-profit mission. Musk’s interest in the case is that he donated at least $44 million to the OpenAI foundation, not believing that the money would be used towards a for-profit.

Recently this week, the judge in the case denied Musk’s request. Had the request been accepted, OpenAI’s corporate structure would have essentially been frozen in place as a non-profit until the full trial and judgment. **[If you only looked at the headlines](https://garrisonlovely.substack.com/p/what-the-headlines-miss-about-the), you might think this represented a critical loss for Musk and a win for OpenAI — but this is actually not the case.**

To break it down, [there’s a podcast with](https://x.com/robertwiblin/status/1898087281501552809) Rose Chan Loui, Executive Director of the Lowell Milken Center for Philanthropy & Nonprofits at UCLA Law. She mentions the case has two issues:

1. whether OpenAI’s conversion violates the charitable purpose of the non-profit and thus is an illegal conversion under California law. OpenAI’s original mission was to benefit humanity via safe AI development. The pivot to for-profit raises questions about continuing that mission.
2. whether Musk has *standing* (the right) to be the one to bring this case — whether the funds Musk provided to OpenAI were restricted to only charitable purposes and that this gives him a contractual right to enforce how the money is used.

It seems the judge was not fully persuaded that Musk has standing, making a problem with issue (2). But the ruling mentions that the attorneys general of California and Delaware automatically have standing on behalf of the public, instantly solving issue (2) should they bring the case. The court order might be a signal to either or both of these AGs to step in. If they do, that could be a big deal.

Another reason this could be seen as a win for Musk’s case is that the judge set the trial for the fall, a significantly sped up from a potentially more distant date — the judge clearly does not want the OpenAI conversion to proceed without addressing this controversy.

[Garrison Lovely quotes Michael Dorff, explaining](https://garrisonlovely.substack.com/p/what-the-headlines-miss-about-the):

> “This is a big win for Musk,” says Michael Dorff, the executive director of the Lowell Milken Institute for Business, Law, and Policy at UCLA. “Even though he didn't get the preliminary injunction, the fact that there is a pending trial on this issue and that his claim wasn't denied is a pretty big impediment to [OpenAI] moving forward expeditiously,” he says.

There seem to be a few paths forward:

* Elon Musk could still win the entire case on the merits. Losing a preliminary injunction does not mean losing the case, potentially blocking or re-restructuring the OpenAI conversion.
* Elon Musk could lose on the issue of standing, but a state Attorney General could step in and win the case on the merits.
* Maybe OpenAI will adjust its strategy a small amount to allow the non-profit greater control and greater compensation, while still going forward with the conversion. There have been [hints in recent reporting](https://www.ft.com/content/5af7279f-5996-46f8-a7b9-f35d966880a0) that suggest the foundation might keep stronger voting rights to maintain some control over the for-profit even if more investors join. This could potentially be sufficient for the courts.
* The board may balk at a legally risky approach and chose to further negotiate or adjust the plan to an even larger degree than reported, rather than risk major litigation.

I think there’s a substantial chance this ends up being not much and works out fine for OpenAI, with no to minimal changes. But there’s also a small chance this could block OpenAI’s for-profit conversion altogether.

~

### **…The Microsoft-OpenAI breakup continues?**

In [Weekend Links #5](https://peterwildeford.substack.com/p/weekend-links-5-trump-fights-zelenskyy), I discussed what looks to be Microsoft and OpenAI steadily breaking up their partnership, with OpenAI instead turning more to Oracle and SoftBank.

**This breakup has continued a bit more [with The Information reporting](https://www.theinformation.com/articles/microsofts-ai-guru-wants-independence-from-openai-thats-easier-said-than-done?rc=gbdmm5) that Microsoft’s AI — led by CEO Mustafa Suleyman — has developed a new family of AI models called MAI that reportedly perform** ***nearly*** **as well as leading models from OpenAI and Anthropic on benchmarks**. Additionally, Microsoft is considering replacing or supplementing OpenAI models in Microsoft’s Copilot AI system with MAI or OpenAI competitors including Anthropic, xAI, DeepSeek, and Meta.

And apparently there have been Microsoft-OpenAI tensions. It’s reported that Suleyman clashed with OpenAI staff over lack of documentation about o1 model's chain-of-thought reasoning. The Microsoft-OpenAI partnership gives Microsoft rights to reuse OpenAI technology while sharing information about AI research and development.

If Microsoft can achieve strategic independence and model parity with OpenAI, that would be pretty huge for Microsoft and potentially give them a lot of leverage against OpenAI. But this kind of independence is much easier said than done.

~

### **…Apple’s AI crisis**

Before I’ve said there are five main companies that are poised to be the first to make very powerful AI systems: OpenAI, Anthropic, Google, Meta, and xAI. I’ve also granted outside shots to DeepSeek and Mistral, and maybe SSI should be on this list now too. Furthermore, Amazon seems well-positioned to benefit from Anthropic and Microsoft seems to at least have some sort of plan and maybe it’s working, I can’t really tell. …But what about Apple?

**Apple is [the most valuable company in the world right now](https://companiesmarketcap.com/), but they haven’t been doing well in AI.** Apple should’ve had a head start by pioneering Siri, but Siri looks about to be outclassed by soon-to-be-released [Alexa+ powered by Claude](https://www.anthropic.com/news/claude-and-alexa-plus).

In general, I should say that Apple generally does do a decent job of not being first but being *best* — they weren’t the first music player, phone, or watch, but they often redefined the category and leapfrogged the competition. And maybe they can do the same with AI someday. But Apple’s AI strategy doesn’t seem to be on track right now.

**What’s going on here? Mark Gurman’s latest newsletter for Bloomberg [offers some insight](https://www.bloomberg.com/news/newsletters/2025-03-02/apple-siri-compared-with-alexa-m4-macbook-air-and-ipad-air-2025-coming-soon-m7rn2k2y):**

* Apple announced a splashy AI-upgraded Siri in June 2024, but it was just a prototype. Apple is still struggling to deliver it. It’s hard to make new improvements when Apple still hasn’t delivered the previously announced ones.
* A true modernized chatbot Siri is now estimated to not reach consumers until iOS 20 in 2027. Recall that this is the same time when Anthropic seems to think they will have made genius-level AI with so much power that Siri will look trite by comparison. Definitely different worlds.
* Current Apple Intelligence features have been very underwhelming. Even Apple’s attempt to integrate OpenAI’s ChatGPT has not been well executed.
* Internal challenges preventing Apple's AI advancement include losing talent to competitors, leadership issues, and difficulty securing enough AI chips amid industry-wide shortages.
* Apple hasn’t been as proactive on large data center buildouts needed for model training and inference, preferring to put everything miniaturized and on-device. But now Apple CEO Tim Cook made a trade with President Trump, announcing a $500 billion US investment in exchange for potential tariff relief and government support against EU regulations. This includes opening a new factory in Houston to build AI servers and increasing R&D hiring to 5,000 workers annually. *(Though, like with Stargate, the investment appears to be a repackaging of previous commitments already made under the Biden administration.)*
* Significant cruft is also holding Apple back. The current Siri operates on two separate systems that won't be merged until iOS 19.
* Apple has an amazing distribution channel through billions of phones, but that doesn’t matter if they can’t get the technology out.

But there could be more. Simon Willison’s theory [is that Apple is reasonably struggling to figure out how to deploy AI securely](https://bsky.app/profile/simonwillison.net/post/3ljtqzl6ip22i) against prompt injection attacks and the risk of exposing private information. Recall that [prompt injection attacks](https://simonwillison.net/2023/Nov/27/prompt-injection-explained/) are attempts to hijack AI systems by sneaking commands into the inputs they process — this attack exploits a weakness in AI systems that can’t do a good job of clearly distinguishing between instructions and regular content.

Personal digital assistants are extremely vulnerable to prompt injections. These attacks, if successful on Apple phones, could lead to private information on your phone being leaked to hackers. That would be a bad look for Apple. Given Apple typically refuses to release products prematurely, it makes sense they would be exponentially more cautious with the potential for prompt injection attacks. And this isn’t just Apple’s weakness — no company has a good defense against this, so this should apply to any company trying to offer AI that can interact with your private data.

~

# Lifestyle

### …Organizational checks and approvals - good, but not always best

The proliferation of organizational checks and approvals, while intended to prevent mistakes, can create costs that outweigh their benefits. In [“The Other Half of Artists Ship”](http://paulgraham.com/artistsship.html), Paul Graham cites how corporate software purchasing committees, intended to prevent wasteful spending, can actually force vendors to charge $50,000 for products that should cost $5,000 due to the overhead of managing the approval process leading to companies not being able to purchase products at that lower cost. Similarly, programming teams who previously could deploy code that instead find themselves waiting weeks for approvals — this prevents errors but leads to dramatically reduced productivity and morale.

The broader implications extend beyond just operational inefficiency — the heaviest cost comes from driving away top talent and suppliers. Graham notes that the best programmers specifically seek environments with minimal bureaucracy where they can ship code quickly — many would even take significant pay cuts to maintain this freedom. This suggests that organizations must carefully weigh the hidden costs of each new procedural check against its purported benefits.

~

### …Why are projects always behind schedule? It could be bad estimating

The common practice of estimating project timelines by adding up median completion times for each step dramatically underestimates actual completion times, leading to chronic project delays. [Priceonomics has an interesting analysis from 70,000+ hours of design projects](http://priceonomics.com/why-are-projects-always-behind-schedule/) that reveals median-based estimates underestimate project timelines 67% of the time, with multi-step projects averaging 155 hours versus an estimated 91 hours.

Why? This happens because of a simple statistical trick — while there's a lower bound on how much faster than median a step can be (it can’t be faster than instant), there's no upper limit on delays. This adds up over multiple steps… The probability of all steps completing at or below median time decreases exponentially with each additional step - for a three-step project, it's just 12.5%.

The article proposes several solutions, including calculating timelines based on full statistical distributions rather than medians, improving completion time distributions through streamlined processes, and selective acceleration of delayed steps.

~

# Whimsy

### …China challenges US animation in the box office

There’s geopolitical “China vs. US” tension in anything, including fun animated movies. China's animated blockbuster **[“Ne Zha 2”](https://en.wikipedia.org/wiki/Ne_Zha_2)** has shattered global box office records with over $2 billion in earnings, becoming the first non-English language film to cross both $1B and $2B thresholds.

The film also surpassed Disney's “Inside Out 2” to become the highest-grossing animated film ever and ranks as the seventh-highest-grossing film of all time. More interestingly, it achieved this milestone in less than three weeks of release, with most revenue ($2.017B) coming from domestic Chinese audiences.

~

### …Anything can be a movie prop if only it tries hard enough

**[r/Thatsabooklight](https://www.reddit.com/r/Thatsabooklight/)** is a specialized subreddit showcasing how common household and commercial items are frequently repurposed as props in film and television productions.

For example, in [Surrogates (2009)](https://en.wikipedia.org/wiki/Surrogates), the robot killing weapon used is actually the back half of a Dustbuster from the 1990s:

[![](https://substackcdn.com/image/fetch/$s_!TNay!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F89ab61cd-e0fb-445b-b278-e2ef058ac18a_1152x826.png)](https://substackcdn.com/image/fetch/$s_!TNay!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F89ab61cd-e0fb-445b-b278-e2ef058ac18a_1152x826.png)

[![](https://substackcdn.com/image/fetch/$s_!P58I!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F638dfd50-4418-487b-a964-24dde1f70a4e_956x720.png)](https://substackcdn.com/image/fetch/$s_!P58I!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F638dfd50-4418-487b-a964-24dde1f70a4e_956x720.png)