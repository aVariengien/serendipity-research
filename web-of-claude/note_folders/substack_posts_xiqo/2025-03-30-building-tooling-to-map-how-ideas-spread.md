# Building Tooling to Map how Ideas Spread

*The nooscope will deliver public tools to map how ideas spread, starting with psyop detection, within 18 months.*

Published: 2025-03-30
Source: https://xiqo.substack.com/p/building-tooling-to-map-how-ideas

---

## The Nooscope

A telescope (and microscope) into the noosphere (the realm of ideas between people).

It’s a tool to see how ideas spread—where do they come from, who do they stick with, how do they change?

I like to imagine ideologies competing, merging, forking like microbes.

If we can trace where a given idea comes from, we can detect if it emerged organically or if it was intentionally and artificially promoted.

E.g. Can we tell whether [Barbenheimer](https://en.wikipedia.org/wiki/Barbenheimer) was an organic phenomenon or marketing?

## Motivation

The internet is like a jungle - full of opportunity, but also threats.

Humans are vulnerable to harmful narratives, which are especially easy to spread intentionally online. Misinformation is a well known global risk costing $10Bs if not $100Bs per year and getting worse as AI improves.

We can build tools that give us “jungle eyes”, spotting psyops and harmful memes in our communities. By becoming aware of them earlier, we can mitigate risks from harmful memes like anorexia or unhealthy attachment to “AI partners” before they scale.

Just like in cybersecurity, we can publicly study & document security vulnerabilities. Transparency helps defensive coordination, and no one else is doing this openly.

## Momentum

### Crowdsourced Data

To research memetics, we needed data, so we started a movement to bootstrap our own with the [Twitter Community Archive](https://www.community-archive.org/), a crowdsourced database of Twitter archives.

The archive is an open database and API with 16M tweets from the volunteered archives of ~250 accounts. The cold start only worked because we’re trusted community members and campaigned to get people to upload.

[![](https://substackcdn.com/image/fetch/$s_!yJH0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb331d77b-98bb-468f-ac13-4f2a1c70a368_1024x314.png)](https://substackcdn.com/image/fetch/$s_!yJH0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb331d77b-98bb-468f-ac13-4f2a1c70a368_1024x314.png)

Community Archive front page

It can scale:

* Serve more communities. The [software is open-source](http://github.com/theexgenesis/community-archive), so anyone can start a database for their community.
* Real time data firehose via [our browser extension](https://chromewebstore.google.com/detail/tes-twitter-enhancement-s/abeogphlciedglboobfehkkljdcfgmnb), avoiding the laborious upload process.
* Include Bluesky data. We could easily do this on bluesky because it’s open but twitter still has the most juice.

As more tools appear, more people upload and the data grows, and as the data grows, more devs build tools.

### Open-source tools and an active dev community

The quality of the data is attested to by an active discord of 180 [builders](https://discord.gg/5mbWEfVrqw), 40 of whom were present at our NYC hackathon, with [16 submissions of tools and research](https://xiqo.substack.com/p/the-community-archive-hackathon).

We’ve already built [relevant 1st-party tools](https://github.com/TheExGenesis/community-archive/blob/main/docs/apps.md). A few examples:

📈The [Keyword Trends App](https://github.com/TheExGenesis/community-archive/wiki/Exploring-historical-trends-in-the-community-archive) lets you visualize the occurrence of terms

🐦[Birdseye](https://xiqo.substack.com/p/a-birdseye-view-of-your-tweets) lets you explore topics and trends in your posts;

🕸️ [Personal Semantic Search](https://github.com/DefenderOfBasic/twitter-semantic-search) - search individual archives semantically

[![](https://substackcdn.com/image/fetch/$s_!nYBu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F102611c2-5b1f-45d2-8a35-bb38eaa669e7_1320x660.png)](https://substackcdn.com/image/fetch/$s_!nYBu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F102611c2-5b1f-45d2-8a35-bb38eaa669e7_1320x660.png)

Keyword trends, the simplest memetics tool.

[![Tweet clustering from Birdseye
](https://substackcdn.com/image/fetch/$s_!7LRC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9fb4632c-d215-4d6e-8c08-09584f1026c1_1456x659.png "Tweet clustering from Birdseye
")](https://substackcdn.com/image/fetch/$s_!7LRC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9fb4632c-d215-4d6e-8c08-09584f1026c1_1456x659.png)

Tweet clustering from Birdseye, mapping long-term topics for each account.

## Roadmap

To build the nooscope we need social media data, data science, and contemporary AI.

Without getting too technical,

1. we’d want to get our essential **data-science primitives** running on tweets and accounts - that’s embeddings, clustering, network visualization, etc. [1] We want all of these running very efficiently in the browser, leveraging WebAssembly.
2. Then we learn how to combine these primitives in **concrete experiments to track known events and stories**.
3. Then iterate towards an integrated **tool to explore idea diffusion** in the user-interaction networks present in our 16M tweet dataset.

By the end, we want to help at least 2 other communities to set up their own separate archives (proving that scaling pathway), establish partners to integrate with bluesky, and prove real utility by detecting 5 real-time psyops.

To house the *nooscope* and the *community archive*, we’ll establish the ***open memetics institute*** as an umbrella organization and attractor for like-minded researchers and devs. We’ve been building the only open memetics community on earth already in the [community archive discord](https://discord.gg/bm6GC47K).

*Footnote:*

[1] The data science primitives we want running on tweets and accounts:

* Embeddings,
* Semantic search,
* Clustering,
* Network visualization,
* Network diffusion,
* Named entity search,
* Event detection in time series.

## Team

I’m @[exgenesis](https://x.com/exgenesis%5C) on twitter. I’ve worked in [AI](https://magic.dev/) [safety](https://metr.org/) and have worked for years [on](https://github.com/threadhelper) [improving](http://github.com/unigraph-dev/unigraph-dev) [online](https://hive.one/) [sensemaking](https://www.community-archive.org/upload-archive):

* 2024: Launched [Community Archive](https://www.community-archive.org/upload-archive) - a crowdsourced db and open API with 16M tweets from 250 high-quality accounts.
* 2023: I joined [hive.one](https://hive.one/), an index of twitter communities, to work on twitter data analysis, including community detection.
* 2021: I built [Threadhelper](https://github.com/threadhelper), (Emergent Ventures 7th cohort) a browser extension that turns twitter into a collaborative thinking tool. (1000s of users)

**Team**

* [@exgenesis](https://x.com/exgenesis) - CEO, MLE, research
* [@iaimforgoat](https://x.com/iaimforgoat) - SWE, data maintenance
* [@DefenderOfBasic](https://x.com/DefenderOfBasic) - Community manager, communications, research

**Informal Advisors**

* [Ivan Vendrov](http://x.com/ivanvendrov) (leading collective intelligence at [Midjourney](https://www.midjourney.com/))
* [Brent Baum](http://x.com/_brentbaum) (CEO of [Refract](https://refract.space/))
* [Rich Bartlett](http://x.com/richdecibels) (CEO of [Microsolidarity](https://www.microsolidarity.cc/))
* REDACTED advisor (will show after permission)

## Budget

Our goal is to raise $100k. Vitalik Buterin DMed me pledging to 1:1 match $50k of donations.

* $60k: Living expenses for [@exgenesis](https://x.com/exgenesis) for a year, full-time.
* $20k: Hire [@iaimforgoat](https://x.com/iaimforgoat), our best contributor, part-time for a year.
* $10k: Compute, travel expenses, and other operating costs.
* $10k: Fiscal sponsorship and ops.

$100k is really our minimum, and a stretch goal of $250k would enable us to hire Goat and another contributor full time, and afford us more runway and travel budget for conferences.

We expect our research to lead to public goods as well as for-profit opportunities, e.g. memetics-informed matchmaking.

**Contribute**

Reach me at [@exgenesis](https://x.com/exgenesis)