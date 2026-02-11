# Deriving strands of discourse from a single tweet | lab notes #3

*Looking into a community’s hosting capacity as a measure of growing agency*

Published: 2025-12-07
Source: https://xiqo.substack.com/p/deriving-strands-of-discourse-from

---

Alexandre and I are researching how ideas spread on twitter using the community archive dataset.

We want to build tools that feel like pointing a telescope at the plane of ideas and collective thought. A “nooscope” into the “noosphere”.

To develop these tools, we’re manually investigating stories and developing computational methods as we need them— mostly applying stats and network science and LLMs to social data.

Some examples of stories are the rise of Jhanas or of Fractal NYC.

These are only a few examples. How do we find an extensive catalog of candidate stories to pick from?

## Deriving narrative strands from semantic clusters

One strategy is to make semantic embeddings of the whole dataset, cluster the results, and treat clusters as individual stories. We tried that to middling success. Clusters tend to be vague - think more “tweets about food” than “my journey with South Chinese cuisine”. To mitigate this, we asked LLMs to identify tighter strands of story within each cluster.

An example is that we found this strand moving from “the next buddha is a sangha” to “the next buddha is an internet community” to “the next buddha is tpot”.

[![](https://substackcdn.com/image/fetch/$s_!03qF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1dc75ef5-a7e8-451c-815a-a2a27d8b3e48_1262x396.png)](https://substackcdn.com/image/fetch/$s_!03qF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1dc75ef5-a7e8-451c-815a-a2a27d8b3e48_1262x396.png)

Fig 1: The thicker blue stripe represents a given semantic cluster, like “tweets about dharma”, while the thinner ones represent strands of discourse like “mythmaking about the next Buddha being an online community”. *(Note this is a simplified diagram, and strands are likely to be intertwined with each other in complex ways)*

Upon inspecting more clusters, we weren’t super satisfied with the results. At least with our naive prompt, Gemini 3 hallucinated lots of references and misunderstood jokes as more significant than they were. (It has since come to my attention that Gemini 3 is especially prone to hallucinating so I should try a different LLM).

I would say the LLM output was somewhere between a C+ and B-, which motivated us to try a different approach before trying to refine this one. We decided to try getting stories from single tweets.

## Deriving narrative strands from single tweets

Given a single tweet, what was its future impact, and what were its preceding influences?

[![](https://substackcdn.com/image/fetch/$s_!P2NK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F452b056c-68cf-4c06-a2a1-ae9ebbf9bf67_1262x772.png)](https://substackcdn.com/image/fetch/$s_!P2NK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F452b056c-68cf-4c06-a2a1-ae9ebbf9bf67_1262x772.png)

Fig 2: Illustrating past influences of a tweet and future impacts of it.

Then the problem became how do we pick tweets to look at but thankfully there’s a very satisfying answer: tweets that are quoted a lot. My explanation is that these tend to be good atomic pieces of knowledge since they keep being referred to. On inspection, they match what you would expect of the canon of the community. We built [Bangers](https://bangers.community-archive.org/) to browse them.

Actually, there are two types of high QT tweets: ones with many QTs in a burst, and those with sustained QTs over time, so we found a metric for burstiness (the half-life of the QT time series) and sorted them. Here are the top two tweets:

[![](https://substackcdn.com/image/fetch/$s_!_QFE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F725827be-379b-47ef-b770-6aba59e2f0b9_784x592.png)](https://substackcdn.com/image/fetch/$s_!_QFE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F725827be-379b-47ef-b770-6aba59e2f0b9_784x592.png)

Fig 3: ASCII histograms to visualize how many QTs the top quoted tweets got over time. Flatter graphs mean the tweet is referred to over and over, whereas bursty graphs mean the tweets got lots of quotes but didn’t have staying power. The first are more interesting to us since we’re looking for stories.

After this we were ready to pull strands. We obviously wanted to get the complete thread in which tweets exist, we want the tweets quoting them, and importantly we want the same things for tweets semantically related to them even if they are structurally disconnected!

[![](https://substackcdn.com/image/fetch/$s_!1_V8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F852f8e73-f9ac-404d-bd56-b56ca4a8627b_1256x330.png)](https://substackcdn.com/image/fetch/$s_!1_V8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F852f8e73-f9ac-404d-bd56-b56ca4a8627b_1256x330.png)

Fig 4: Our current pipeline to generate context for finding narrative strands from a single tweet.

So we did that, we applied it to a tweet, we looked at the resulting context, and now we’re writing its story!

## Story: A community’s hosting capacity as a measure of growing agency

We started with Rich’s map of hosting capacity as a measure of agency.

[![](https://substackcdn.com/image/fetch/$s_!HRDb!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4efee3bd-9eda-400e-825e-cefa3c158328_784x882.png)](https://substackcdn.com/image/fetch/$s_!HRDb!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4efee3bd-9eda-400e-825e-cefa3c158328_784x882.png)

As a highly quoted tweet, this one was right at the center of a rich story of increasing agency:

* Around Covid19, we see talk of an opportunity for systems change and organizing online communities

* Then about moving events from online to IRL
* Then we see the original tweet and its surrounding discourse about growing events in duration and number of people
* and finally we have people quote-tweeting with examples of events they ran and applying the principles from the original post.

*Alexandre starts writing around here*

It turns out, this tweet is right at the center of a strand that starts with a vision on the potential of vulnerable scenes, mapping the territory on how these scenes are built (where this tweet is), and finishes in concretizing this vision with actual projects in the real world of increasing scale. This map acts now as an actual map where community organizers put their successes as they slowly climb to the top right corner!

Here is the story told from the tweet we found by picking 20 tweets.

**Aspiration.**

The story starts during Covid, where the proto-TPOT community starts organizing online to catalyse the impact of the crisis into a lasting system change. At this point the vocabulary is vague, people probably have more intuition about what *kind* of system change, but it would take work to spell it out clearly.

[![](https://substackcdn.com/image/fetch/$s_!QnKa!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7c238d90-4ddc-48ad-ad90-f96d3fe1c6bd_728x650.png)](https://substackcdn.com/image/fetch/$s_!QnKa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7c238d90-4ddc-48ad-ad90-f96d3fe1c6bd_728x650.png)

The first bite at clarifying the vision comes from VisakanV with this famous meme.

[![](https://substackcdn.com/image/fetch/$s_!b-S6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9358b2f6-5134-4afb-b552-e5cdc8797f5f_786x714.png)](https://substackcdn.com/image/fetch/$s_!b-S6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9358b2f6-5134-4afb-b552-e5cdc8797f5f_786x714.png)

The meme shows up in the set of tweets we found for our strand, and we find a riff on the same ideas while self-quoting the meme.

[![](https://substackcdn.com/image/fetch/$s_!vfEB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F91d9d320-5792-4bdb-9e36-d2428c1255d6_700x596.png)](https://substackcdn.com/image/fetch/$s_!vfEB!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F91d9d320-5792-4bdb-9e36-d2428c1255d6_700x596.png)

[![](https://substackcdn.com/image/fetch/$s_!HMRZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc49a981f-0312-4765-a120-07fd05e3145c_688x926.png)](https://substackcdn.com/image/fetch/$s_!HMRZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc49a981f-0312-4765-a120-07fd05e3145c_688x926.png)

The key question here is “How do we create these scenes?” How can we sustain new places for culture to emerge that don’t get captured by extractive dynamics?

**Mapping.**

One year later, we started seeing in the strand the first hand-drawn charts from Rich. He has been thinking about how to catalyse healthy communities for a while now, and his ideas start to be more concrete.

The first maps are not directly about scaling up, and global impact, but focused on understanding the dynamics at play within a group.

[![](https://substackcdn.com/image/fetch/$s_!PZkD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe463cb53-3022-4548-8178-81c56dfc728f_724x996.png)](https://substackcdn.com/image/fetch/$s_!PZkD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe463cb53-3022-4548-8178-81c56dfc728f_724x996.png)

Two years later, Covid has passed, the TPOT movement is blooming, and we are well after the first vibecamp. At this time, our strand shows the first tpot community builder conference bringing community builders together! This marks the first step in making the vision concretely visible in the strand. Of course, many things were happening in parallel that were not visible. For instance, the first Vibecamp happened the year before.

[![](https://substackcdn.com/image/fetch/$s_!KU5w!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5579e383-f1c1-4b86-8217-671b191d2582_720x1226.png)](https://substackcdn.com/image/fetch/$s_!KU5w!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5579e383-f1c1-4b86-8217-671b191d2582_720x1226.png)

The same year, in 2023, we got another map from Rich. This time, it clearly tries to lay directions to *scale* communities. Turning the fluffy vision of “productive cultural scene” into a goal community builders can start executing on.

[![](https://substackcdn.com/image/fetch/$s_!yR6x!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F91f4a48e-62f1-49de-91f4-3b293a3329b4_718x1156.png)](https://substackcdn.com/image/fetch/$s_!yR6x!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F91f4a48e-62f1-49de-91f4-3b293a3329b4_718x1156.png)

The same thread continues on setting up the clear vision for what properties the neighborhood should have to support a thriving local culture.

[![](https://substackcdn.com/image/fetch/$s_!iGH7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77a389d0-13a4-4426-9e0d-9aca52f1d584_672x550.png)](https://substackcdn.com/image/fetch/$s_!iGH7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77a389d0-13a4-4426-9e0d-9aca52f1d584_672x550.png)

[![](https://substackcdn.com/image/fetch/$s_!9gg9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8e7e4bf8-d39a-44d0-9b85-3a46ef8a4159_652x734.png)](https://substackcdn.com/image/fetch/$s_!9gg9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8e7e4bf8-d39a-44d0-9b85-3a46ef8a4159_652x734.png)

[![](https://substackcdn.com/image/fetch/$s_!atAn!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F61789fa0-dba7-432d-b194-6a4f37aa315b_630x502.png)](https://substackcdn.com/image/fetch/$s_!atAn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F61789fa0-dba7-432d-b194-6a4f37aa315b_630x502.png)

Fractal NYC, who perfectly matches this “most desirable option” tweet is conspicuously missing from our set of tweets.

In parallel we have a thread from @octopusyarn that riffs on how different models of communities can serve different functions. In the same thread, they name the three missing factors for community building: economics, governance (ie. membrane management), and protection against failure modes like cults, power grabs or ossification.

[![](https://substackcdn.com/image/fetch/$s_!LzGc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F049353e6-58f5-4bdc-8943-e24c14cde504_642x1268.png)](https://substackcdn.com/image/fetch/$s_!LzGc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F049353e6-58f5-4bdc-8943-e24c14cde504_642x1268.png)

By now, we’re at the final stage of map-making where the background conceptual work is solid enough that we can draw a red cross on it and say “this is where we go now!”. It channeled the existing traction from the success of organizing camps. The map says that no, the answer is not to run *more* camps, but to scale up in terms of time commitment and/or group size.

And well beyond the map, the thread gives a set of building blocks for community builders. Almost mantras to repeat along the way, as you climb on the top right corner.

[![](https://substackcdn.com/image/fetch/$s_!dzZu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc4143208-1678-4b5c-980c-408433de66bf_722x966.png)](https://substackcdn.com/image/fetch/$s_!dzZu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc4143208-1678-4b5c-980c-408433de66bf_722x966.png)

One thing I like about this tweet is that it points a way out of apocalyptic thinking. In the subtext, there is the EA movement that relies on consequentialist reasoning to jump straight to working top-down at max leverage, taking on missions that aim to steer humanity away from technological self-destruction. Rich says, first there is a way out from the stable equilibrium of apocalyptic thinking. “Apocalyptic thinking stems from psychological pain, the cure for this pain is good company”.

[![](https://substackcdn.com/image/fetch/$s_!shho!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1158bc3f-0450-4968-baf9-610d652fae63_378x812.png)](https://substackcdn.com/image/fetch/$s_!shho!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1158bc3f-0450-4968-baf9-610d652fae63_378x812.png)

Second, jumping straight to the large scale without experience on the small scale is a “mega problem”.

[![](https://substackcdn.com/image/fetch/$s_!qCdD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa73de65a-236b-479f-ab9e-9e2403d7675b_372x394.png)](https://substackcdn.com/image/fetch/$s_!qCdD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa73de65a-236b-479f-ab9e-9e2403d7675b_372x394.png)

[Microsolidarity](https://www.microsolidarity.cc/) is also conspicuously missing! This could be addressed by including user summaries for the most active users in a strand. Rich’s summary would include something about microsolidarity for sure and Tyler’s would include something about Fractal NYC.

**Burst.**

The map and its thread became instant bangers. The map got directly turned into execution, where people started putting their events directly on it.

[![](https://substackcdn.com/image/fetch/$s_!9t4V!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1965ab1-09bb-4656-b301-2baa7759a90a_654x1286.png)](https://substackcdn.com/image/fetch/$s_!9t4V!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1965ab1-09bb-4656-b301-2baa7759a90a_654x1286.png)

It’s not that the map captured all the relevant dimensions, but it captured the most concrete axis, to start looking at the horizon and feel “that’s how far things can go!”.

Among the missing directions discussed:

* The periodicity/permanance/intensity of the event. E.g. the difference between 1hr meeting once, vs every week for a year.
* “Increased synergy/​flow/​intimacy/​epicness among a group of 20-for-a-week or 5-for-a-day” from @Malcom\_Ocean in another thread.
* @christineist says

  + depth/creativity
  + doesn’t speak to how you may want to specialize instead of scale
  + consistency/volumeZ/cadence
  + sense of ecosystem— it’s not enjoyable if everyone is making a coliving neighborhood

But the general direction is now clear: top right corner.

[![](https://substackcdn.com/image/fetch/$s_!0xzs!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc356b084-1242-4551-85ee-df7a910e92ef_654x870.png)](https://substackcdn.com/image/fetch/$s_!0xzs!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc356b084-1242-4551-85ee-df7a910e92ef_654x870.png)

TOP RIGHT CORNER!! Here we are, this is an appropriate amount of ambition.

[![](https://substackcdn.com/image/fetch/$s_!lwbh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F36ad824b-6ab7-4ca8-be11-1f92f406dce4_464x726.png)](https://substackcdn.com/image/fetch/$s_!lwbh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F36ad824b-6ab7-4ca8-be11-1f92f406dce4_464x726.png)

**Execution.**

From then on, most of the activity in the strand came from quote tweets that refer to Rich’s maps in response to announcements for real-world events. The momentum from online connection, the short-term camps turned into real long term neighborhoods that support thriving scenes holding vulnerability, curiosity, arts, friendship, and beauty!

Here with Rich himself announcing his opening.

[![](https://substackcdn.com/image/fetch/$s_!tI6E!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbc449b52-080f-4823-9532-07ad1873f144_384x1086.png)](https://substackcdn.com/image/fetch/$s_!tI6E!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbc449b52-080f-4823-9532-07ad1873f144_384x1086.png)

And xiq showing the retro of his journey to building Portal!

[![](https://substackcdn.com/image/fetch/$s_!8bqI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2a99a821-2c98-41fc-b624-5af47a75c913_544x1064.png)](https://substackcdn.com/image/fetch/$s_!8bqI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2a99a821-2c98-41fc-b624-5af47a75c913_544x1064.png)

Of course these are only a few real-world projects. Not included here are all the camps, Fractal and its bootcamp. It would be interesting to dig deeper into how the story of this map and these other projects intersect

## Conclusion

This is cool huh? Again, we’re studying how ideas spread in the community archive.

We hope this will teach us about how vibrant online communities work and how they can be reproduced everywhere; among other things.

We’re analyzing these stories manually to understand what typical strands of narrative are like, so we can better prompt LLMs to find them autonomously. We want to build tools that let communities understand themselves and the world and make better decisions towards their own pursuits of good, truth, and beauty.

[![](https://substackcdn.com/image/fetch/$s_!JtIT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7c94c365-09b1-4e1a-a1db-f139ac1c3484_9312x5088.png)](https://substackcdn.com/image/fetch/$s_!JtIT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7c94c365-09b1-4e1a-a1db-f139ac1c3484_9312x5088.png)

What an interface to this type of story detection may look like

We believe there are abundant public goods in applying AI to social data, and that we must be sovereign over the data we generate.

If you resonate, I hope you will consider contributing your data to the [community archive](https://www.community-archive.org/), installing the [community archive stream browser extension](https://chromewebstore.google.com/detail/community-archive-stream/igclpobjpjlphgllncjcgaookmncegbk), or supporting us on [opencollective](https://opencollective.com/community-archive).