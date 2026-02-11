# LLM predictions for 2026, shared with Oxide and Friends

*With promising news for Kākāpō parrot breeding season*

Published: 2026-01-09
Source: https://simonw.substack.com/p/llm-predictions-for-2026-shared-with

---

In this newsletter:

* LLM predictions for 2026, shared with Oxide and Friends

Plus 6 links and 5 quotations and 2 notes

*If you find this newsletter useful, please consider [sponsoring me via GitHub](https://github.com/sponsors/simonw). $10/month and higher sponsors get a monthly newsletter with my summary of the most important trends of the past 30 days \- here are previews from [August](https://gist.github.com/simonw/43bf3bd7f9951a8e82a9e61b53399ede) and [September](https://gist.github.com/simonw/d6d4d86afc0d76767c63f23fc5137030).*

### [LLM predictions for 2026, shared with Oxide and Friends](https://simonwillison.net/2026/Jan/8/llm-predictions-for-2026/) \- 2026\-01\-08

I joined a recording of the Oxide and Friends podcast on Tuesday to talk about 1, 3 and 6 year predictions for the tech industry. This is my second appearance on their annual predictions episode, you can see [my predictions from January 2025 here](https://simonwillison.net/2025/Jan/10/ai-predictions/). Here’s [the page for this year’s episode](https://oxide-and-friends.transistor.fm/episodes/predictions-2026), with options to listen in all of your favorite podcast apps or [directly on YouTube](https://www.youtube.com/watch?v=lVDhQMiAbR8).

Bryan Cantrill started the episode by declaring that he’s never been so unsure about what’s coming in the next year. I share that uncertainty \- the significant advances in coding agents just in the last two months have left me certain that things will change significantly, but unclear as to what those changes will be.

Here are the predictions I shared in the episode.

* [1 year: It will become undeniable that LLMs write good code](https://simonwillison.net/2026/Jan/8/llm-predictions-for-2026/#1-year-it-will-become-undeniable-that-llms-write-good-code)
* [1 year: We’re finally going to solve sandboxing](https://simonwillison.net/2026/Jan/8/llm-predictions-for-2026/#1-year-we-re-finally-going-to-solve-sandboxing)
* [1 year: A “Challenger disaster” for coding agent security](https://simonwillison.net/2026/Jan/8/llm-predictions-for-2026/#1-year-a-challenger-disaster-for-coding-agent-security)
* [1 year: Kākāpō parrots will have an outstanding breeding season](https://simonwillison.net/2026/Jan/8/llm-predictions-for-2026/#1-year-k-k-p-parrots-will-have-an-outstanding-breeding-season)
* [3 years: the coding agents Jevons paradox for software engineering will resolve, one way or the other](https://simonwillison.net/2026/Jan/8/llm-predictions-for-2026/#3-years-the-coding-agents-jevons-paradox-for-software-engineering-will-resolve-one-way-or-the-other)
* [3 years: Someone will build a new browser using mainly AI\-assisted coding and it won’t even be a surprise](https://simonwillison.net/2026/Jan/8/llm-predictions-for-2026/#3-years-someone-will-build-a-new-browser-using-mainly-ai-assisted-coding-and-it-won-t-even-be-a-surprise)
* [6 years: Typing code by hand will go the way of punch cards](https://simonwillison.net/2026/Jan/8/llm-predictions-for-2026/#6-years-typing-code-by-hand-will-go-the-way-of-punch-cards)

#### 1 year: It will become undeniable that LLMs write good code [▶ 19:27](https://www.youtube.com/watch?v=lVDhQMiAbR8&t=1167s)

> I think that there are still people out there who are convinced that LLMs cannot write good code. Those people are in for a very nasty shock in 2026\. I do not think it will be possible to get to the end of even the next three months while still holding on to that idea that the code they write is all junk and it’s it’s likely any decent human programmer will write better code than they will.

In 2023, saying that LLMs write garbage code was entirely correct. For most of 2024 that stayed true. In 2025 that changed, but you could be forgiven for continuing to hold out. In 2026 the quality of LLM\-generated code will become impossible to deny.

I base this on my own experience \- I’ve spent more time exploring [AI\-assisted programming](https://simonwillison.net/tags/ai-assisted-programming/)than most.

The key change in 2025 (see [my overview for the year](https://simonwillison.net/2025/Dec/31/the-year-in-llms/#the-year-of-reasoning-)) was the introduction of “reasoning models” trained specifically against code using Reinforcement Learning. The major labs spent a full year competing with each other on who could get the best code capabilities from their models, and that problem turns out to be perfectly attuned to RL since code challenges come with built\-in verifiable success conditions.

Since Claude Opus 4\.5 and GPT\-5\.2 came out in November and December respectively the amount of code I’ve written by hand has dropped to a single digit percentage of my overall output. The same is true for many other expert programmers I know.

At this point if you continue to argue that LLMs write useless code you’re damaging your own credibility.

#### 1 year: We’re finally going to solve sandboxing [▶ 20:05](https://www.youtube.com/watch?v=lVDhQMiAbR8&t=1205s)

> I think this year is the year we’re going to solve sandboxing. I want to run code other people have written on my computing devices without it destroying my computing devices if it’s malicious or has bugs. \[...] It’s crazy that it’s 2026 and I still `pip install` random code and then execute it in a way that it can steal all of my data and delete all my files. \[...] I don’t want to run a piece of code on any of my devices that somebody else wrote outside of sandbox ever again.

This isn’t just about LLMs, but it becomes even more important now there are so many more people writing code often without knowing what they’re doing. Sandboxing is also a key part of the battle against prompt injection.

We have a *lot* of promising technologies in play already for this \- containers and WebAssembly being the two I’m most optimistic about. There’s real commercial value involved in solving this problem. The pieces are there, what’s needed is UX work to reduce the friction in using them productively and securely.

#### 1 year: A “Challenger disaster” for coding agent security [▶ 21:21](https://www.youtube.com/watch?v=lVDhQMiAbR8&t=1281s)

> I think we’re due a Challenger disaster with respect to coding agent security\[...] I think so many people, myself included, are running these coding agents practically as root, right? We’re letting them do all of this stuff. And every time I do it, my computer doesn’t get wiped. I’m like, “oh, it’s fine”.

I used this as an opportunity to promote my favourite recent essay about AI security, [the Normalization of Deviance in AI](https://embracethered.com/blog/posts/2025/the-normalization-of-deviance-in-ai/) by Johann Rehberger.

The Normalization of Deviance describes the phenomenon where people and organizations get used to operating in an unsafe manner because nothing bad has happened to them yet, which can result in enormous problems (like the 1986 Challenger disaster) when their luck runs out.

Every six months I predict that a headline\-grabbing prompt injection attack is coming soon, and every six months it doesn’t happen. This is my most recent version of that prediction!

#### 1 year: Kākāpō parrots will have an outstanding breeding season [▶ 50:06](https://www.youtube.com/watch?v=lVDhQMiAbR8&t=3006s)

(I dropped this one to lighten the mood after a discussion of the deep sense of existential dread that many programmers are feeling right now!)

> I think that Kākāpō parrots in New Zealand are going to have an outstanding breeding season. The reason I think this is that the Rimu trees are in fruit right now. There’s only 250 of them, and they only breed if the Rimu trees have a good fruiting. The Rimu trees have been terrible since 2019, but this year the Rimu trees were all blooming. There are researchers saying that all 87 females of breeding age might lay an egg. And for a species with only 250 remaining parrots that’s great news.

(I just [checked Wikipedia](https://en.wikipedia.org/wiki/K%C4%81k%C4%81p%C5%8D#Population_timeline) and I was right with the parrot numbers but wrong about the last good breeding season, apparently 2022 was a good year too.)

In a year with precious little in the form of good news I am utterly delighted to share this story. Here’s more:

* [Kākāpō breeding season 2026](https://blog.doc.govt.nz/2025/06/27/kakapo-breeding-season-2026/)introduction from the Department of Conservation from June 2025 .
* [Bumper breeding season for kākāpō on the cards](https://www.auckland.ac.nz/en/news/2025/12/03/bumper-breeding-season-for-kakapo-on-the-cards.html) \- 3rd December 2025, University of Auckland.

I don’t often use AI\-generated images on this blog, but the Kākāpō image the Oxide team created for this episode is just *perfect*:

[![A beautiful green Kākāpō surrounded by candles gazes into a crystal ball](https://substackcdn.com/image/fetch/$s_!eO5M!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8aff968e-355e-4c82-916e-4e5e6c8f263d_1280x720.jpeg "A beautiful green Kākāpō surrounded by candles gazes into a crystal ball")](https://substackcdn.com/image/fetch/$s_!eO5M!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8aff968e-355e-4c82-916e-4e5e6c8f263d_1280x720.jpeg)

#### 3 years: the coding agents Jevons paradox for software engineering will resolve, one way or the other [▶ 54:37](https://www.youtube.com/watch?v=lVDhQMiAbR8&t=3277s)

> We will find out if the [Jevons paradox](https://en.wikipedia.org/wiki/Jevons_paradox) saves our careers or not. This is a big question that anyone who’s a software engineer has right now: we are driving the cost of actually producing working code down to a fraction of what it used to cost. Does that mean that our careers are completely devalued and we all have to learn to live on a tenth of our incomes, or does it mean that the demand for software, for custom software goes up by a factor of 10 and now our skills are even *more* valuable because you can hire me and I can build you 10 times the software I used to be able to? I think by three years we will know for sure which way that one went.

The quote says it all. There are two ways this coding agents thing could go: it could turn out software engineering skills are devalued, or it could turn out we’re more valuable and effective than ever before.

I’m crossing my fingers for the latter! So far it feels to me like it’s working out that way.

#### 3 years: Someone will build a new browser using mainly AI\-assisted coding and it won’t even be a surprise [▶ 65:13](https://www.youtube.com/watch?v=lVDhQMiAbR8&t=3913s)

> I think somebody will have built a full web browser mostly using AI assistance, and it won’t even be surprising. Rolling a new web browser is one of the most complicated software projects I can imagine\[...] the cheat code is the conformance suites. If there are existing tests that it’ll get so much easier.

A common complaint today from AI coding skeptics is that LLMs are fine for toy projects but can’t be used for anything large and serious.

I think within 3 years that will be comprehensively proven incorrect, to the point that it won’t even be controversial anymore.

I picked a web browser here because so much of the work building a browser involves writing code that has to conform to an enormous and daunting selection of both formal tests and informal websites\-in\-the\-wild.

Coding agents are *really good* at tasks where you can define a concrete goal and then set them to work iterating in that direction.

A web browser is the most ambitious project I can think of that leans into those capabilities.

#### 6 years: Typing code by hand will go the way of punch cards [▶ 80:39](https://www.youtube.com/watch?v=lVDhQMiAbR8&t=4839s)

> I think the job of being paid money to type code into a computer will go the same way as punching punch cards \[...] in six years time, I do not think anyone will be paid to just to do the thing where you type the code. I think software engineering will still be an enormous career. I just think the software engineers won’t be spending multiple hours of their day in a text editor typing out syntax.

The more time I spend on AI\-assisted programming the less afraid I am for my job, because it turns out building software \- especially at the rate it’s now possible to build \- still requires enormous skill, experience and depth of understanding.

The skills are changing though! Being able to read a detailed specification and transform it into lines of code is the thing that’s being automated away. What’s left is everything else, and the more time I spend working with coding agents the larger that “everything else” becomes.

---

**Link** 2026\-01\-02 [The most popular blogs of Hacker News in 2025](https://refactoringenglish.com/blog/2025-hn-top-5/):

Michael Lynch maintains [HN Popularity Contest](https://refactoringenglish.com/tools/hn-popularity/), a site that tracks personal blogs on Hacker News and scores them based on how well they perform on that platform.

The engine behind the project is the [domain\-meta.csv](https://github.com/mtlynch/hn-popularity-contest-data/blob/master/data/domains-meta.csv) CSV on GiHub, a hand\-curated list of known personal blogs with author and bio and tag metadata, which Michael uses to separate out personal blog posts from other types of content.

I came top of the rankings in 2023, 2024 and 2025 but I’m listed [in third place](https://refactoringenglish.com/tools/hn-popularity/) for all time behind Paul Graham and Brian Krebs.

I dug around in the browser inspector and was delighted to find that the data powering the site is served with open CORS headers, which means you can easily explore it with external services like Datasette Lite.

Here’s a convoluted window function query Claude Opus 4\.5 [wrote for me](https://claude.ai/share/8e1cb294-0ff0-4d5b-b83f-58e4c7fdb0d2) which, for a given domain, shows where that domain ranked for each year since it first appeared in the dataset:

```
with yearly_scores as (
  select 
    domain,
    strftime(’%Y’, date) as year,
    sum(score) as total_score,
    count(distinct date) as days_mentioned
  from “hn-data”
  group by domain, strftime(’%Y’, date)
),
ranked as (
  select 
    domain,
    year,
    total_score,
    days_mentioned,
    rank() over (partition by year order by total_score desc) as rank
  from yearly_scores
)
select 
  r.year,
  r.total_score,
  r.rank,
  r.days_mentioned
from ranked r
where r.domain = :domain
  and r.year >= (
    select min(strftime(’%Y’, date)) 
    from “hn-data”
    where domain = :domain
  )
order by r.year desc
```

(I just noticed that the last `and r.year >= (`clause isn’t actually needed here.)

My [simonwillison.net results](https://lite.datasette.io/?csv=https://hn-popularity.cdn.refactoringenglish.com/hn-data.csv#/data?sql=with+yearly_scores+as+%28%0A++select+%0A++++domain%2C%0A++++strftime%28%27%25Y%27%2C+date%29+as+year%2C%0A++++sum%28score%29+as+total_score%2C%0A++++count%28distinct+date%29+as+days_mentioned%0A++from+%22hn-data%22%0A++group+by+domain%2C+strftime%28%27%25Y%27%2C+date%29%0A%29%2C%0Aranked+as+%28%0A++select+%0A++++domain%2C%0A++++year%2C%0A++++total_score%2C%0A++++days_mentioned%2C%0A++++rank%28%29+over+%28partition+by+year+order+by+total_score+desc%29+as+rank%0A++from+yearly_scores%0A%29%0Aselect+%0A++r.year%2C%0A++r.total_score%2C%0A++r.rank%2C%0A++r.days_mentioned%0Afrom+ranked+r%0Awhere+r.domain+%3D+%3Adomain%0A++and+r.year+%3E%3D+%28%0A++++select+min%28strftime%28%27%25Y%27%2C+date%29%29+%0A++++from+%22hn-data%22%0A++++where+domain+%3D+%3Adomain%0A++%29%0Aorder+by+r.year+desc&domain=simonwillison.net) show me ranked 3rd in 2022, 30th in 2021 and 85th back in 2007 \- though I expect there are many personal blogs from that year which haven’t yet been manually added to Michael’s list.

Also useful is that every domain gets its own CORS\-enabled CSV file with details of the actual Hacker News submitted from that domain, e.g. `https://hn-popularity.cdn.refactoringenglish.com/domains/simonwillison.net.csv`. Here’s [that one in Datasette Lite](https://lite.datasette.io/?csv=https://hn-popularity.cdn.refactoringenglish.com/domains/simonwillison.net.csv#/data/simonwillison).

---

**quote**2026\-01\-02

> *My experience is that \*real\* AI adoption on \*real\* problems is a complex blend of: domain context on the problem, domain experience with AI tooling, and old\-fashioned IT issues. I’m deeply skeptical of any initiative for internal AI adoption that doesn’t anchor on all three of those. This is an advantage of earlier stage companies, because you can often find aspects of all three of those in a single person, or at least across two people. In larger companies, you need three different \*organizations\* doing this work together, this is just objectively hard*

[Will Larson](https://lethain.com/company-ai-adoption/), Facilitating AI adoption at Imprint

---

**Link** 2026\-01\-03 [Was Daft Punk Having a Laugh When They Chose the Tempo of Harder, Better, Faster, Stronger?](https://www.madebywindmill.com/tempi/blog/hbfs-bpm/):

Depending on how you measure it, the tempo of Harder, Better, Faster, Stronger appears to be 123\.45 beats per minute.

This is one of those things that’s so cool I’m just going to accept it as true.

(I only today learned from [the Hacker News comments](https://news.ycombinator.com/item?id=46469577#46470831) that Veridis Quo is “Very Disco”, and if you flip the order of those words you get Discovery, the name of the album.)

---

**quote**2026\-01\-04

> *I’m not joking and this isn’t funny. We have been trying to build distributed agent orchestrators at Google since last year. There are various options, not everyone is aligned... I gave Claude Code a description of the problem, it generated what we built last year in an hour.  
>   
> It’s not perfect and I’m iterating on it but this is where we are right now. If you are skeptical of coding agents, try it on a domain you are already an expert of. Build something complex from scratch where you can be the judge of the artifacts. \[…]*
> 
>  *It wasn’t a very detailed prompt and it contained no real details given I cannot share anything propriety. I was building a toy version on top of some of the existing ideas to evaluate Claude Code. It was a three paragraph description.*

[Jaana Dogan](https://twitter.com/rakyll/status/2007239758158975130), Principal Engineer at Google

---

**Note** [2026\-01\-04](https://simonwillison.net/2026/Jan/4/coding-again/)

Something I like about our weird new LLM\-assisted world is the number of people I know who are coding again, having mostly stopped as they moved into management roles or lost their personal side project time to becoming parents.

AI assistance means you can get something useful done in half an hour, or even while you are doing other stuff. You don’t need to carve out 2\-4 hours to ramp up anymore.

If you have significant previous coding experience \- even if it’s a few years stale \- you can drive these things really effectively. Especially if you have management experience, quite a lot of which transfers to “managing” coding agents \- communicate clearly, set achievable goals, provide all relevant context. Here’s a relevant [recent tweet](https://twitter.com/emollick/status/2007249835465072857) from Ethan Mollick:

> When you see how people use Claude Code/Codex/etc it becomes clear that managing agents is really a management problem
> 
> Can you specify goals? Can you provide context? Can you divide up tasks? Can you give feedback?
> 
> These are teachable skills. Also UIs need to support management

This note [started as a comment](https://news.ycombinator.com/item?id=46488576#46488894).

---

**quote**2026\-01\-04

> *With enough users, every observable behavior becomes a dependency \- regardless of what you promised. Someone is scraping your API, automating your quirks, caching your bugs.  
>   
> This creates a career\-level insight: you can’t treat compatibility work as “maintenance” and new features as “real work.” Compatibility is product.  
>   
> Design your deprecations as migrations with time, tooling, and empathy. Most “API design” is actually “API retirement.”*

[Addy Osmani](https://addyosmani.com/blog/21-lessons/), 21 lessons from 14 years at Google

---

**Note** [2026\-01\-04](https://simonwillison.net/2026/Jan/4/inflection/)

It genuinely feels to me like GPT\-5\.2 and Opus 4\.5 in November represent an inflection point \- one of those moments where the models get incrementally better in a way that tips across an invisible capability line where suddenly a whole bunch of much harder coding problems open up.

**Link** 2026\-01\-05 [It’s hard to justify Tahoe icons](https://tonsky.me/blog/tahoe-icons/):

Devastating critique of the new menu icons in macOS Tahoe by Nikita Prokopov, who starts by quoting the 1992 Apple HIG rule to not “overload the user with complex icons” and then provides comprehensive evidence of Tahoe doing exactly that.

> In my opinion, Apple took on an impossible task: to add an icon to every menu item. There are just not enough good metaphors to do something like that.
> 
> But even if there were, the premise itself is questionable: if everything has an icon, it doesn’t mean users will find what they are looking for faster.
> 
> And even if the premise was solid, I still wish I could say: they did the best they could, given the goal. But that’s not true either: they did a poor job consistently applying the metaphors and designing the icons themselves.

---

**Link** 2026\-01\-06 [A field guide to sandboxes for AI](https://www.luiscardoso.dev/blog/sandboxes-for-ai):

This guide to the current sandboxing landscape by Luis Cardoso is comprehensive, dense and absolutely fantastic.

He starts by differentiating between containers (which share the host kernel), microVMs (their own guest kernel behind hardwae virtualization), gVisor userspace kernels and WebAssembly/isolates that constrain everything within a runtime.

The piece then dives deep into terminology, approaches and the landscape of existing tools.

I think using the right sandboxes to safely run untrusted code is one of the most important problems to solve in 2026\. This guide is an invaluable starting point.

---

**quote**2026\-01\-07

> *\*\*AGI is here\*\*! When exactly it arrived, we’ll never know; whether it was one company’s Pro or another company’s Pro Max (Eddie Bauer Edition) that tip\-toed first across the line … you may debate. But generality has been achieved, \& now we can proceed to new questions. \[...]  
>   
> The key word in Artificial General Intelligence is General. That’s the word that makes this AI unlike every other AI: because every other AI was trained for a particular purpose. Consider landmark models across the decades: the Mark I Perceptron, LeNet, AlexNet, AlphaGo, AlphaFold … these systems were all different, but all alike in this way.  
>   
> Language models were trained for a purpose, too … but, surprise: the mechanism \& scale of that training did something new: opened a wormhole, through which a vast field of action \& response could be reached. Towering libraries of human writing, drawn together across time \& space, all the dumb reasons for it … that’s rich fuel, if you can hold it all in your head.*

[Robin Sloan](https://www.robinsloan.com/winter-garden/agi-is-here/), AGI is here (and I feel fine)

---

**quote**2026\-01\-07

> *\[...] the reality is that 75% of the people on our engineering team lost their jobs here yesterday because of the brutal impact AI has had on our business. And every second I spend trying to do fun free things for the community like this is a second I’m not spending trying to turn the business around and make sure the people who are still here are getting their paychecks every month. \[...]  
>   
> Traffic to our docs is down about 40% from early 2023 despite Tailwind being more popular than ever. The docs are the only way people find out about our commercial products, and without customers we can’t afford to maintain the framework. \[...]  
>   
> Tailwind is growing faster than it ever has and is bigger than it ever has been, and our revenue is down close to 80%. Right now there’s just no correlation between making Tailwind easier to use and making development of the framework more sustainable.*

[Adam Wathan](https://github.com/tailwindlabs/tailwindcss.com/pull/2388#issuecomment-3717222957), CEO, Tailwind Labs

---

**Link** 2026\-01\-08 [How Google Got Its Groove Back and Edged Ahead of OpenAI](https://www.wsj.com/tech/ai/google-ai-openai-gemini-chatgpt-b766e160):

I picked up a few interesting tidbits from this Wall Street Journal piece on Google’s recent hard won success with Gemini.

Here’s the origin of the name “Nano Banana”:

> Naina Raisinghani, known inside Google for working late into the night, needed a name for the new tool to complete the upload. It was 2:30 a.m., though, and nobody was around. So she just made one up, a mashup of two nicknames friends had given her: Nano Banana.

The WSJ credit OpenAI’s Daniel Selsam with un\-retiring Sergei Brin:

> Around that time, Google co\-founder Sergey Brin, who had recently retired, was at a party chatting with a researcher from OpenAI named Daniel Selsam, according to people familiar with the conversation. Why, Selsam asked him, wasn’t he working full time on AI. Hadn’t the launch of ChatGPT captured his imagination as a computer scientist?
> 
> ChatGPT was on its way to becoming a household name in AI chatbots, while Google was still fumbling to get its product off the ground. Brin decided Selsam had a point and returned to work.

And we get some rare concrete user numbers:

> By October, Gemini had more than 650 million monthly users, up from 450 million in July.

The LLM usage number I see cited most often is OpenAI’s 800 million weekly active users for ChatGPT. That’s from October 6th at OpenAI DevDay so it’s comparable to these Gemini numbers, albeit not directly since it’s weekly rather than monthly actives.

I’m also never sure what counts as a “Gemini user” \- does interacting via Google Docs or Gmail count or do you need to be using a Gemini chat interface directly?

---