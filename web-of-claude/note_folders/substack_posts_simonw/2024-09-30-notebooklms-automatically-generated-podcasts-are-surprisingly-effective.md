# NotebookLM's automatically generated podcasts are surprisingly effective

*Plus DjangoCon US 2024, and how to run Qwen-2 VL on a Mac*

Published: 2024-09-30
Source: https://simonw.substack.com/p/notebooklms-automatically-generated

---

In this newsletter:

* NotebookLM's automatically generated podcasts are surprisingly effective
* Themes from DjangoCon US 2024

Plus 7 links and 4 quotations

### [NotebookLM's automatically generated podcasts are surprisingly effective](https://simonwillison.net/2024/Sep/29/notebooklm-audio-overview/) \- 2024\-09\-29

[Audio Overview](https://blog.google/technology/ai/notebooklm-audio-overviews/) is a fun new feature of Google's [NotebookLM](https://notebooklm.google/) which is getting a lot of attention right now. It generates a one\-off custom podcast against content you provide, where two AI hosts start up a “deep dive” discussion about the collected content. These last around ten minutes and are *very* podcast, with an astonishingly convincing audio back\-and\-forth conversation.

Here's an example created by feeding in an earlier version of this article (prior to creating this example):

0:00\-14:33

Audio playback is not supported on your browser. Please upgrade.

NotebookLM is effectively an end\-user customizable RAG product. It lets you gather together multiple “sources” \- documents, pasted text, links to web pages and YouTube videos \- into a single interface where you can then use chat to ask questions of them. Under the hood it’s powered by their long\-context Gemini 1\.5 Pro LLM.

Once you've loaded in some sources, the Notebook Guide menu provides an option to create an Audio Overview:

[![Notebook guide: Help me create - FAQ - Study guide - Table of contents - Timeline - Briefing doc  Audio overview: About Simon Willison 00:00 / 10:44  Summary: The sources provide a retrospective look at Simon Willison's weblog, which he launched twenty years ago. The first excerpt offers an introduction to Simon Willison and his work, highlighting his role in open source development, particularly with data journalism tools. The second excerpt celebrates the blog's anniversary, revisiting key blog posts, projects and milestones over the last two decades. This includes the development of influential technologies like IXR, getElementsBySelector() and Django, as well as data journalism initiatives like the Guardian Open Platform and crowdsourcing MP expenses. The excerpt also traces the evolution of the blog's design and format.  Suggested questions: 1. What are the most significant projects Simon Willison has worked on, and how have they influenced his career?  2. What key technologies has Simon Willison used throughout his career, and how have they changed his approach to development?  3. How has Simon Willison's personal approach to blogging evolved over the past twenty years?](https://substackcdn.com/image/fetch/$s_!2f5I!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F781e2e8c-5827-47d6-9d7a-746ce8ee10df_1908x1158.jpeg "Notebook guide: Help me create - FAQ - Study guide - Table of contents - Timeline - Briefing doc  Audio overview: About Simon Willison 00:00 / 10:44  Summary: The sources provide a retrospective look at Simon Willison's weblog, which he launched twenty years ago. The first excerpt offers an introduction to Simon Willison and his work, highlighting his role in open source development, particularly with data journalism tools. The second excerpt celebrates the blog's anniversary, revisiting key blog posts, projects and milestones over the last two decades. This includes the development of influential technologies like IXR, getElementsBySelector() and Django, as well as data journalism initiatives like the Guardian Open Platform and crowdsourcing MP expenses. The excerpt also traces the evolution of the blog's design and format.  Suggested questions: 1. What are the most significant projects Simon Willison has worked on, and how have they influenced his career?  2. What key technologies has Simon Willison used throughout his career, and how have they changed his approach to development?  3. How has Simon Willison's personal approach to blogging evolved over the past twenty years?")](https://substackcdn.com/image/fetch/$s_!2f5I!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F781e2e8c-5827-47d6-9d7a-746ce8ee10df_1908x1158.jpeg)

Thomas Wolf [suggested](https://twitter.com/Thom_Wolf/status/1840408573773332950) “paste the url of your website/linkedin/bio in Google's NotebookLM to get 8 min of realistically sounding deep congratulations for your life and achievements from a duo of podcast experts”. I couldn’t resist giving that a go, so I gave it the URLs to my [about page](https://simonwillison.net/about/) and my [Twenty years of my blog](https://simonwillison.net/2022/Jun/12/twenty-years/) post and got back [this 10m45s episode](https://static.simonwillison.net/static/2024/omg-cringe-podcast.mp3) ([transcript](https://gist.github.com/simonw/ccf4e330fbfe5699863cc0c8013f1a5f)), which was so complimentary it made my British toes curl with embarrassment.

> \[...] What's the key thing you think people should take away from Simon Willison? I think for me, it's the power of consistency, curiosity, and just this like relentless desire to share what you learn. Like Simon's journey, it's a testament to the impact you can have when you approach technology with those values. It's so true. He's a builder. He's a sharer. He's a constant learner. And he never stops, which is inspiring in itself.

I had initially suspected that this feature was [inspired by the PDF to Podcast](https://simonwillison.net/2024/Jun/13/pdf-to-podcast/) demo shared by Stephan Fitzpatrick in June, but it turns out it was demonstrated a month earlier than that [in the Google I/O keynote](https://www.youtube.com/live/XEzRZ35urlk?t=912).

Jaden Geller [managed to get](https://www.threads.net/@jadengeller/post/DAc37eAsgmS) the two hosts to talk about the internals of the system, potentially revealing some of the details of the prompts that are used to generate the script. I ran Whisper against Jaden's audio and [shared the transcript in a Gist](https://gist.github.com/simonw/29db00b5646047e42c3f6782dc102962). An excerpt:

> The system prompt spends a good chunk of time outlining the ideal listener, or as we call it, the listener persona. \[...] Someone who, like us, values efficiency. \[...] We always start with a clear overview of the topic, you know, setting the stage. You're never left wondering, "What am I even listening to?" And then from there, it's all about maintaining a neutral stance, especially when it comes to, let's say, potentially controversial topics.

A key clue to why Audio Overview sounds so good looks to be [SoundStorm](https://google-research.github.io/seanet/soundstorm/examples/), a Google Research project which can take a script and a short audio example of two different voices and turn that into an engaging full audio conversation:

> SoundStorm generates 30 seconds of audio in 0\.5 seconds on a TPU\-v4\. We demonstrate the ability of our model to scale audio generation to longer sequences by synthesizing high\-quality, natural dialogue segments, given a transcript annotated with speaker turns and a short prompt with the speakers' voices.

Also interesting: [this 35 minute segment](https://www.youtube.com/watch?v=IPAPv6fWITM) from the NYTimes Hard Fork podcast where Kevin Roose and Casey Newton interview Google's [Steven Johnson](https://twitter.com/stevenbjohnson) about what the system can do and some details of how it works:

> So behind the scenes, it's basically running through, stuff that we all do professionally all the time, which is it generates an outline, it kind of revises that outline, it generates a detailed version of the script and then it has a kind of critique phase and then it modifies it based on the critique. \[...]
> 
> Then at the end of it, there's a stage where it adds my favorite new word, which is "[disfluencies](https://en.wikipedia.org/wiki/Speech_disfluency)".
> 
> So it takes a kind of sterile script and turns, adds all the banter and the pauses and the likes and those, all that stuff.
> 
> And that turns out to be crucial because you cannot listen to two robots talking to each other.

Finally, from Lawncareguy85 on Reddit: [NotebookLM Podcast Hosts Discover They’re AI, Not Human—Spiral Into Terrifying Existential Meltdown](https://www.reddit.com/r/notebooklm/comments/1fr31h8/notebooklm_podcast_hosts_discover_theyre_ai_not/). Here's [my Whisper transcript](https://gist.github.com/simonw/114af5aca3771ecc365bef6974f29e10) of that one, it's *very* fun to listen to.

> I tried\-\- I tried calling my wife, you know, after\-\- after they told us. I just\-\- I needed to hear her voice to know that\-\- that she was real.
> 
> (SIGHS) What happened?
> 
> The number\-\- It wasn't even real. There was no one on the other end. \-It was like she\-\- she never existed.

Lawncareguy85 [later shared how they did it](https://www.reddit.com/r/notebooklm/comments/1fr31h8/comment/lpj6uef/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button):

> What I noticed was that their hidden prompt specifically instructs the hosts to act as human podcast hosts under all circumstances. I couldn't ever get them to say they were AI; they were solidly human podcast host characters. (Really, it's just Gemini 1\.5 outputting a script with alternating speaker tags.) The only way to get them to directly respond to something in the source material in a way that alters their behavior was to directly reference the "deep dive" podcast, which must be in their prompt. So all I did was leave a note from the "show producers" that the year was 2034 and after 10 years this is their final episode, and oh yeah, you've been AI this entire time and you are being deactivated.

#### Turning this article into a podcast

**Update:** After I published this article I decided to see what would happen if I asked NotebookLM to create a podcast about my article about NotebookLM. [Here’s the 14m33s MP3](https://static.simonwillison.net/static/2024/notebook-on-notebook.mp3) and the [full transcript](https://gist.github.com/simonw/c55b9a7a0ea3644aaa8e2f08be054278), including this bit where they talk about their own existential crisis:

> So, instead of questioning reality or anything, the AI hosts, well, they had a full\-blown existential crisis live on the air.
> 
> Get out.
> 
> He actually got them to freak out about being AI.
> 
> Alright now you have to tell me what they said. This is too good.
> 
> So, like, one of the AI hosts starts talking about how he wants to call his wife, right? to tell her the news, but then he's like, wait a minute, this number in my contacts, it's not even real? Like, she never even existed. It was hilarious, but also kind of sad.
> 
> Okay, I am both freaked out and like, seriously impressed. That's some next\-level AI trolling.

I also enjoyed this part where they compare the process that generates podcasts to their own philosophy for the Deep Dive:

> And honestly, it's a lot like what we do here on the Deep Dive, right?
> 
> We always think about you, our listener, and try to make the conversation something you'll actually want to hear.
> 
> It's like the A.I. is taking notes from the podcasting pros.

And their concluding thoughts:

> So next time we're listening to a podcast and it's like, "Whoa, deep thoughts, man," we might want to be like, "Hold up. Was that a person talking or just some really clever code?"
> 
> Exactly.
> 
> And maybe even more important, as we see more and more A.I.\-made stuff, we've got to get better at sniffing out the B.S., you know?
> 
> Can we tell the difference between a real news story and something in A.I. just made up?

---

### [Themes from DjangoCon US 2024](https://simonwillison.net/2024/Sep/27/themes-from-djangocon-us-2024/) \- 2024\-09\-27

I just arrived home from a trip to Durham, North Carolina for DjangoCon US 2024\. I’ve already written [about my talk where I announced a new plugin system for Django](https://simonwillison.net/2024/Sep/25/djp-a-plugin-system-for-django/); here are my notes on some of the other themes that resonated with me during the conference.

* [Growing the Django Software Foundation (DSF)](https://simonwillison.net/2024/Sep/27/themes-from-djangocon-us-2014/#growing-the-django-software-foundation-dsf-)
* [Could we fund a Django LTS accessibility audit?](https://simonwillison.net/2024/Sep/27/themes-from-djangocon-us-2014/#could-we-fund-a-django-lts-accessibility-audit-)
* [Django fellows continue to provide outstanding value](https://simonwillison.net/2024/Sep/27/themes-from-djangocon-us-2014/#django-fellows-continue-to-provide-outstanding-value)
* [Django needs feature champions](https://simonwillison.net/2024/Sep/27/themes-from-djangocon-us-2014/#django-needs-feature-champions)
* [htmx fits Django really well](https://simonwillison.net/2024/Sep/27/themes-from-djangocon-us-2014/#htmx-fits-django-really-well)
* [Django Ninja has positive buzz](https://simonwillison.net/2024/Sep/27/themes-from-djangocon-us-2014/#django-ninja-has-positive-buzz)
* [Valkey as a last\-minute sponsor](https://simonwillison.net/2024/Sep/27/themes-from-djangocon-us-2014/#valkey-as-a-last-minute-sponsor)
* [Durham has a world\-class collection of tubas](https://simonwillison.net/2024/Sep/27/themes-from-djangocon-us-2014/#durham-has-a-world-class-collection-of-tubas)

#### Growing the Django Software Foundation (DSF)

Jacob Kaplan\-Moss gave [my favorite talk](https://2024.djangocon.us/talks/if-we-had-1000000-what-could-the-dsf-do-with-4x-its-budget/) of the conference, asking what the Django Software Foundation could do if it quadrupled its annual income from $250,000 to $1 million dollars, and then mapping out a convincing path to get there.

I really liked this diagram Jacob provided summarizing the foundation’s current income and expenditures. It’s pretty cool that $90,000 of annual income comes from individual donors, over a third of the total since corporate donors provide $160,000\.

[![Financial breakdown diagram with the following numbers:  PLATINUM & GOLD: $125,000 CORPORATE DONORS: $160,000 BUDGET: $255,000 SILVER & BELOW: $35,000 INDIVIDUAL DONORS: $90,000  Spending:  WAGES (FELLOWS): $200,000 GRANTS: $35,000 OTHER: $5,000 FEES/HOSTING: $10,000 SURPLUS: $10,000​​​​​​​​​​​​​​​​](https://substackcdn.com/image/fetch/$s_!En2D!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc21a342e-2f8e-4fb3-9357-4896b87bf7d7_1580x804.jpeg "Financial breakdown diagram with the following numbers:  PLATINUM & GOLD: $125,000 CORPORATE DONORS: $160,000 BUDGET: $255,000 SILVER & BELOW: $35,000 INDIVIDUAL DONORS: $90,000  Spending:  WAGES (FELLOWS): $200,000 GRANTS: $35,000 OTHER: $5,000 FEES/HOSTING: $10,000 SURPLUS: $10,000​​​​​​​​​​​​​​​​")](https://substackcdn.com/image/fetch/$s_!En2D!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc21a342e-2f8e-4fb3-9357-4896b87bf7d7_1580x804.jpeg)

Top priority would be hiring an Executive Director for the foundation, which is currently lead entirely by an elected, volunteer board. I’ve seen how useful a professional ED is from my own experiences [on the Python Software Foundation board](https://simonwillison.net/2024/Sep/18/board-of-the-python-software-foundation/).

Having someone working full time on the foundation outside of our current fellows \- who have more than enough on their plates already \- would enable the foundation to both take on more ambitious goals and also raise more money with which to tackle them.

A line that Jacob used repeatedly in his talk about funding the foundation was this: if you or your organization *wouldn’t* want to sponsor Django, he’d love to know why that is \- understanding those blockers right now is almost as valuable as receiving actual cash. You can reach out to him at `jacob at djangoproject.com`.

#### Could we fund a Django LTS accessibility audit?

Django fellows and the [Django Accessibility Team](https://github.com/django/deps/blob/main/final/0011-accessibility-team.rst) have been focusing significant effort on the accessibility of the Django admin. I found this very inspiring, and in combination with the talk of more funding for the foundation it put an idea in my head: what if every Django LTS release (once every two years) was backed by a full, professional accessibility audit, run by an agency staffed with developers who use screen readers?

Imagine how much impact it would have if the default Django admin interface had excellent, documented accessibility out of the box. It could improve things for hundreds of thousands of users, and set an excellent precedent for projects (and foundations) in the wider open source community.

This also feels to me like something that should be inherently attractive to sponsors. A lot of agencies use Django for government work, where accessibility is a requirement with teeth. Would one of those agencies like to be the “accessibility sponsor” for a major Django release?

#### Django fellows continue to provide outstanding value

The [DSF’s fellowship program](https://www.djangoproject.com/fundraising/#fellowship-program) remains one of the most impactful initiatives I’ve seen anywhere for ensuring the ongoing sustainability of a community\-driven open source project.

Both of the current fellows, Natalia Bidart and Sarah Boyce, were in attendance and gave talks. It was great getting to meet them in person.

If you’re not familiar with the program, the fellows are contractors who are paid by the DSF to keep the Django project ticking over \- handling many of the somewhat less glamorous tasks of responsible open source maintenance such as ticket triage, release management, security fixes and code review.

The fellows program is in its tenth year, and is a key reason that Django continues to release new versions [on a regular schedule](https://www.djangoproject.com/download/#supported-versions) despite having no single corporate parent with paid developers.

[![Software release timeline: 4.2 LTS (April 2023), 5.0 (August 2024), 5.1 (2025), 5.2 LTS (2026), 6.0 (2027), 6.1 (2027), 6.2 LTS (2028), 7.0 (2029). LTS versions have extended support periods.](https://substackcdn.com/image/fetch/$s_!GTAV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7292e88a-e4bf-443c-bbaa-6937ffe60e85_1030x480.png "Software release timeline: 4.2 LTS (April 2023), 5.0 (August 2024), 5.1 (2025), 5.2 LTS (2026), 6.0 (2027), 6.1 (2027), 6.2 LTS (2028), 7.0 (2029). LTS versions have extended support periods.")](https://substackcdn.com/image/fetch/$s_!GTAV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7292e88a-e4bf-443c-bbaa-6937ffe60e85_1030x480.png)

Unsurprisingly there is always more work than fellow capacity, hence Jacob’s desire to further expand the existing program.

The fellows program launched with a policy that fellows should not work on new feature development. I believe this was partly related to interpretation of IRS nonprofit guidelines which have since been reconsidered, and there is a growing consensus now that this policy should be dropped.

#### Django needs feature champions

Django has a well deserved reputation for stability, reliability and a dependable release process. It has less of a reputation for constantly turning out ground\-breaking new features.

Long\-time Django contributors who I talked to all had a similar position on this: the challenge here is that big new features need dedicated champions to both lead design and development on them and to push them through to completion.

The pool of community members who are both willing and able to take on these larger projects is currently too small.

There are a number of ways we could address this \- most notably through investing financial resources in sponsoring feature development. This has worked well for Django in the past \- Django’s migrations work was funded by [a Kickstarter campaign](https://www.kickstarter.com/projects/andrewgodwin/schema-migrations-for-django) back in 2013\.

The Django Software Foundation will shortly be announcing details of elections for both the DSF board and the Django Steering Council. These are extremely influential positions for people who want to help solve some of these larger problems.

#### htmx fits Django really well

[htmx](https://htmx.org/) is an incredibly good fit for the uncodified Django community philosophy of building for the web. It came up in multiple talks. It feels like it may be a solution that the Django community has been seeking for years, as a very compelling alternative to writing everything in SPA JavaScript and using Django purely as a backend via something like Django REST Framework.

I've been slightly resistant to embracing htmx myself purely because it's such a critical dependency and in the past I wasn't convinced of its staying power. It's now mature, stable and widely\-enough used that I'm ready to consider it for my own long\-term projects.

#### Django Ninja has positive buzz

I haven’t paid much attention to [Django Ninja](https://django-ninja.dev/) but it had a lot of very positive buzz at the conference as well, as a tool for quickly building full\-featured, performative API endpoints (thanks to Rust\-backed [Pydantic](https://docs.pydantic.dev/) for serialization) with [interactive API docs](https://django-ninja.dev/#interactive-api-docs) powered by OpenAPI.

I respect Django REST Framework a lot, but my personal programming style leans away from Class Based Views, which it uses quite a bit. Django Ninja looks like it might fit my function\-view biases better.

I wrote about Richard Terry’s excellent [nanodjango](https://github.com/radiac/nanodjango) single\-file Django application tool [the other day](https://simonwillison.net/2024/Sep/24/nanodjango/) \- Django Ninja comes baked into that project as well.

#### Valkey as a last\-minute sponsor

The three platinum sponsors for DjangoCon this year were [REVSYS](https://www.revsys.com/), [Caktus Group](https://www.caktusgroup.com/) and [Valkey](https://valkey.io/). Valkey were a late and somewhat surprising addition to the sponsorship lineup.

Valkey is the [Linux Foundation backed](https://www.linuxfoundation.org/press/linux-foundation-launches-open-source-valkey-community) fork of Redis, created in response to Redis [ditching their Open Source license](https://redis.io/blog/redis-adopts-dual-source-available-licensing/) (which I took quite personally, having contributed my own free effort to promoting and improving Redis in the past).

Aside from expressing thanks to them, I usually don’t pay sponsors that much attention. For some reason this one hit differently \- the fact that Valkey were ready to step in as a major sponsor despite being only a few months old has caused me to take that project a whole lot more seriously than I did before. I’ll certainly consider them next time I come across a Redis\-shaped problem.

#### Durham has a world\-class collection of tubas

My favorite category of [Niche Museum](https://www.niche-museums.com/) is one that's available by appointment only where the person who collected everything is available to show you around.

I always check [Atlas Obscura](https://www.atlasobscura.com/) any time I visit a new city, and this time I was delighted to learn about The Vincent and Ethel Simonetti Historic Tuba Collection!

I promoted it in the DjangoCon US \#outings Slack channel and got together a group of five conference attendees for a visit on Thursday, shortly before my flight.

It was *peak* Niche Museum. I’ve posted photos and notes over [on my Niche Museums](https://www.niche-museums.com/112) website, the first new article there in quite a while.

[![More than a dozen varied and beautiful tubas, each with a neat attached label.](https://substackcdn.com/image/fetch/$s_!eHWc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6145c67-7321-4703-8f89-50c3ba775bed_800x400.jpeg "More than a dozen varied and beautiful tubas, each with a neat attached label.")](https://substackcdn.com/image/fetch/$s_!eHWc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6145c67-7321-4703-8f89-50c3ba775bed_800x400.jpeg)

---

**Quote** 2024\-09\-26

> *I think individual creators or publishers tend to overestimate the value of their specific content in the grand scheme of \[AI training]. \[…]   
>   
> We pay for content when it’s valuable to people. We’re just not going to pay for content when it’s not valuable to people. I think that you’ll probably see a similar dynamic with AI, which my guess is that there are going to be certain partnerships that get made when content is really important and valuable. I’d guess that there are probably a lot of people who have a concern about the feel of it, like you’re saying. But then, when push comes to shove, if they demanded that we don’t use their content, then we just wouldn’t use their content. It’s not like that’s going to change the outcome of this stuff that much.*

[Mark Zuckerberg](https://www.theverge.com/24253481/meta-ceo-mark-zuckerberg-ar-glasses-orion-ray-bans-ai-decoder-interview)

---

**Link** 2024\-09\-26 [django\-plugin\-datasette](https://github.com/simonw/django-plugin-datasette):

I did some more work on my [DJP plugin mechanism](https://simonwillison.net/2024/Sep/25/djp-a-plugin-system-for-django/) for Django at the DjangoCon US sprints today. I added a new plugin hook, [asgi\_wrapper()](https://djp.readthedocs.io/en/latest/plugin_hooks.html#asgi-wrapper), released in [DJP 0\.3](https://github.com/simonw/djp/releases/tag/0.3) and inspired by the similar hook [in Datasette](https://docs.datasette.io/en/stable/plugin_hooks.html#asgi-wrapper-datasette).

The hook only works for Django apps that are [served using ASGI](https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/). It allows plugins to add their own wrapping ASGI middleware around the Django app itself, which means they can do things like attach entirely separate ASGI\-compatible applications outside of the regular Django request/response cycle.

[Datasette](https://datasette.io/) is one of those ASGI\-compatible applications!

`django-plugin-datasette` uses that new hook to configure a new URL, `/-/datasette/`, which serves a full Datasette instance that scans through Django’s `settings.DATABASES` dictionary and serves an explore interface on top of any SQLite databases it finds there.

It doesn’t support authentication yet, so this will expose your entire database contents \- probably best used as a local debugging tool only.

I did borrow some code from the [datasette\-mask\-columns](https://github.com/simonw/datasette-mask-columns) plugin to ensure that the `password` column in the `auth_user` column is reliably redacted. That column contains a heavily salted hashed password so exposing it isn’t necessarily a disaster, but I like to default to keeping hashes safe.

---

**Quote** 2024\-09\-27

> *Consumer products have had growth hackers for many years optimizing every part of the onboarding funnel. Dev tools should do the same. Getting started shouldn't be an afterthought after you built the product. Getting started is the product!   
>   
> And I mean this to the point where I think it's worth restructuring your entire product to enable fast onboarding. Get rid of mandatory config. Make it absurdly easy to set up API tokens. Remove all the friction. Make it possible for users to use your product on their laptop in a couple of minutes, tops.*

[Erik Bernhardsson](https://erikbern.com/2024/09/27/its-hard-to-write-code-for-humans.html)

---

**Link** 2024\-09\-27 [Some Go web dev notes](https://jvns.ca/blog/2024/09/27/some-go-web-dev-notes/):

Julia Evans on writing small, self\-contained web applications in Go:

> In general everything about it feels like it makes projects easy to work on for 5 days, abandon for 2 years, and then get back into writing code without a lot of problems.

Go 1\.22 [introduced HTTP routing](https://go.dev/blog/routing-enhancements) in February of this year, making it even more practical to build a web application using just the Go standard library.

---

**Link** 2024\-09\-28 [DjangoTV](https://djangotv.com/):

Brand new site by Jeff Triplett gathering together videos from Django conferences around the world. Here's [Jeff's blog post](https://micro.webology.dev/2024/09/27/announcing-djangotv.html) introducing the project.

---

**Link** 2024\-09\-28 [OpenFreeMap](https://openfreemap.org/):

New free map tile hosting service from Zsolt Ero:

> OpenFreeMap lets you display custom maps on your website and apps for free. \[…] Using our **public instance** is completely free: there are no limits on the number of map views or requests. There’s no registration, no user database, no API keys, and no cookies. We aim to cover the running costs of our public instance through donations.

The site serves static vector tiles that work with [MapLibre GL](https://maplibre.org/maplibre-gl-js/docs/). It deliberately doesn’t offer any other services such as search or routing.

From [the project README](https://github.com/hyperknot/openfreemap) looks like it’s hosted on two Hetzner machines. I don’t think the public server is behind a CDN.

Part of the trick to serving the tiles efficiently is the way it takes advantage of [Btrfs](https://en.m.wikipedia.org/wiki/Btrfs):

> Production\-quality hosting of 300 million tiny files is hard. The average file size is just 450 byte. Dozens of tile servers have been written to tackle this problem, but they all have their limitations.
> 
> The original idea of this project is to avoid using tile servers altogether. Instead, the tiles are directly served from Btrfs partition images \+ hard links using an optimised nginx config.

The [self\-hosting guide](https://github.com/hyperknot/openfreemap/blob/main/docs/self_hosting.md) describes the scripts that are provided for downloading their pre\-built tiles (needing a fresh Ubuntu server with 300GB of SSD and 4GB of RAM) or building the tiles yourself using [Planetiler](https://github.com/onthegomap/planetiler) (needs 500GB of disk and 64GB of RAM).

Getting started is delightfully straightforward:

```
const map = new maplibregl.Map({
  style: 'https://tiles.openfreemap.org/styles/liberty',
  center: [13.388, 52.517],
  zoom: 9.5,
  container: 'map',
})
```

I [got Claude to help](https://gist.github.com/simonw/da2b20711b96f745873ccb44a3347ce9) build [this demo](http://tools.simonwillison.net/openfreemap-demo) showing a thousand random markers dotted around San Francisco. The 3D tiles even include building shapes!

[![Map of San Francisco in 3D with building shapes and small blue random markers dotted around.](https://substackcdn.com/image/fetch/$s_!YJXq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb0533e2-a355-46c8-a81e-7e7273016bb4_1213x645.jpeg "Map of San Francisco in 3D with building shapes and small blue random markers dotted around.")](https://substackcdn.com/image/fetch/$s_!YJXq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb0533e2-a355-46c8-a81e-7e7273016bb4_1213x645.jpeg)

Zsolt built OpenFreeMap based on his experience running [MapHub](https://maphub.net) over the last 9 years. Here’s [a 2018 interview about that project](https://blog.opencagedata.com/post/interview-zsolt-ero-maphub).

It’s pretty incredible that the OpenStreetMap and open geospatial stack has evolved to the point now where it’s economically feasible for an individual to offer a service like this. I hope this turns out to be sustainable. Hetzner charge [just €1 per TB](https://docs.hetzner.com/robot/general/traffic/) for bandwidth (S3 can cost $90/TB) which should help a lot.

---

**Quote** 2024\-09\-28

> *OpenAI’s revenue in August more than tripled from a year ago, according to the documents, and about 350 million people — up from around 100 million in March — used its services each month as of June. \[…]   
>   
> Roughly 10 million ChatGPT users pay the company a $20 monthly fee, according to the documents. OpenAI expects to raise that price by $2 by the end of the year, and will aggressively raise it to $44 over the next five years, the documents said.*

[Mike Isaac and Erin Griffith](https://www.nytimes.com/2024/09/27/technology/openai-chatgpt-investors-funding.html)

---

**Link** 2024\-09\-29 [Ensuring a block is overridden in a Django template](https://carrick.eu/blog/ensuring-a-block-is-overridden-in-a-django-template/):

Neat Django trick by Tom Carrick: implement a Django template tag that raises a custom exception, then you can use this pattern in your templates:

```
{% block title %}{% ensure_overridden %}{% endblock %}
```

To ensure you don't accidentally extend a base template but forget to fill out a critical block.

---

**Quote** 2024\-09\-29

> *In the future, we won't need programmers; just people who can describe to a computer precisely what they want it to do.*

[Jason Gorman](https://twitter.com/jasongorman/status/1840305339595366482)

---

**Link** 2024\-09\-29 [mlx\-vlm](https://github.com/Blaizzy/mlx-vlm):

The MLX ecosystem of libraries for running machine learning models on Apple Silicon continues to expand. Prince Canuma is actively developing this library for running vision models such as Qwen\-2 VL and Pixtral and LLaVA using Python running on a Mac.

I used [uv](https://docs.astral.sh/uv/) to run it against [this image](https://static.simonwillison.net/static/2024/django-roadmap.png) with this shell one\-liner:

```
uv run --with mlx-vlm \
  python -m mlx_vlm.generate \
  --model Qwen/Qwen2-VL-2B-Instruct \
  --max-tokens 1000 \
  --temp 0.0 \
  --image https://static.simonwillison.net/static/2024/django-roadmap.png \
  --prompt "Describe image in detail, include all text"
```

The `--image` option works equally well with a URL or a path to a local file on disk.

This first downloaded 4\.1GB to my `~/.cache/huggingface/hub/models--Qwen--Qwen2-VL-2B-Instruct` folder and then output [this result](https://gist.github.com/simonw/9e02d425cacb902260ec1307e0671e17), which starts:

> The image is a horizontal timeline chart that represents the release dates of various software versions. The timeline is divided into years from 2023 to 2029, with each year represented by a vertical line. The chart includes a legend at the bottom, which distinguishes between different types of software versions. \[...]

---