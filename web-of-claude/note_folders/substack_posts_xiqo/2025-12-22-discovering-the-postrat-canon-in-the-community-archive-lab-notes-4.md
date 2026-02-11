# discovering the postrat canon in the community archive | lab notes #4

*canonical stories!*

Published: 2025-12-22
Source: https://xiqo.substack.com/p/discovering-the-postrat-canon-in

---

*The work referred to in this post can be found [here](https://bangers.community-archive.org/best-strands).*

[![](https://substackcdn.com/image/fetch/$s_!1gqQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7889817-fac0-4255-ae0d-f9ba6bcc1e6e_2022x648.png)](https://substackcdn.com/image/fetch/$s_!1gqQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7889817-fac0-4255-ae0d-f9ba6bcc1e6e_2022x648.png)

Figure: Mini map of the memetic landscape - one point per strand

[Last time](https://xiqo.substack.com/p/deriving-strands-of-discourse-from), Alexandre and I wrote about how we derive strands of narrative from single tweets.

[![](https://substackcdn.com/image/fetch/$s_!ecFd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F533761da-bf36-4610-972b-26a5b58a999c_1264x812.png)](https://substackcdn.com/image/fetch/$s_!ecFd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F533761da-bf36-4610-972b-26a5b58a999c_1264x812.png)

Then we looked in detail at a single strand we got from Rich’s great diagram of hosting as increasing agency.

Okay, we got a strand. Now get EVERY STRAND. Or rather, every strand we can find easily. We know quote tweets are a great metric so we take the top 100 tweets that were most quoted by community archive users. This technique gives us for free the collection of quote tweets and their threads. They form a mini-corpus commenting on the original tweet, refining it, critiquing it or referencing it in new contexts.

To complement this corpus with content outside of quote tweets we used semantic search to find tweets related to the root. This way, we can find what came *before* the root so we can reconstruct the (partial) story setting the stage for the banger. Our qualitative estimate is that ~ 70% of the information value comes from quote tweets, and 30% for semantic matches, concentrated on semantic matches before the root.

These are the raw materials for our strands, the basis of our automated analysis.

Our main priority was to curate the data to find the best strands, and within a strand the tweets that are the core of its narrative. We had an LLM interview us about what makes a set of tweets a good strand of narrative. Among other things, we care about

* Cohesion: The tweets are actually about the same thing or relevant to the same story.
* Evolution: The featured idea evolved, or story state changed.
* Utility: the story features ideas or projects that are useful, either to the community or to the world at large - like scientific knowledge, art, tools, infrastructure, etc.

[![](https://substackcdn.com/image/fetch/$s_!PFQI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4cc37b44-7a34-4bf7-bf9f-43920f56b555_1600x1142.png)](https://substackcdn.com/image/fetch/$s_!PFQI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4cc37b44-7a34-4bf7-bf9f-43920f56b555_1600x1142.png)

Figure: Our prompt

We manually analyzed and narrativized 3 strands as few-shot examples.

[![](https://substackcdn.com/image/fetch/$s_!iLFr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F88f0ad7d-3de6-4043-9ad8-017e63964184_1600x1034.png)](https://substackcdn.com/image/fetch/$s_!iLFr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F88f0ad7d-3de6-4043-9ad8-017e63964184_1600x1034.png)

Figure: Our manual analysis of MasterTimBlais’ tpot norms strand!

Then we had Claude Sonnet 4.5 go through each strand, rate them according to our criteria, summarize them, and highlight 10 essential tweets as narrative touch points for each.

## results

The top strands are exactly what we would expect them to be. Visa’s domino meme on catalyzing a golden age has a 9/10. You could argue it’s the main teleological meme in tpot, so it’s looking good.

Another one is around Visa describing the threading game, which you can argue is the characteristic mode of posting of this scene.

Another is “focus your time and energy on what you want to see more of”, conveying the (very postrat) skill of hyperstition.

[![](https://substackcdn.com/image/fetch/$s_!E5K-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff51f1cac-f332-4f86-9b6d-0762463243b8_1216x1116.png)](https://substackcdn.com/image/fetch/$s_!E5K-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff51f1cac-f332-4f86-9b6d-0762463243b8_1216x1116.png)

[![](https://substackcdn.com/image/fetch/$s_!LtPa!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4ed10286-c6a7-492e-8537-06546885f834_1216x646.png)](https://substackcdn.com/image/fetch/$s_!LtPa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4ed10286-c6a7-492e-8537-06546885f834_1216x646.png)

18 of the top 35 strands above 8/10 score in the list are Visa’s. Part of me wonders if there’s some implementation weirdness at play, but this list isn’t ranked by number of QTs, strands are rated by Claude. Visa is just prolific and central to the scene.

I would also note that we are missing accounts I would consider important in the scene, like vgr, nickcammaratta, aella\_girl, tszzl, liminal\_warmth, michelcurzi, deepfates, selentelechia.

I’m really excited about this collection! When my friend Brent pushed me to start the community archive, our main desire was to preserve and see the “tpot canon”: the main ideas and stories and projects that have come out of our scene over the past 5 years.

## quality control

Now we have it and there’s a decent amount of work in just going through all of them and gauging quality. I think strand summaries tend to be pretty good, but not always flawless. E.g. I would say Christine’s guide to tpot is a significant artifact but it gets a score of 4. This is an effect of i) our rating system that assess the quality of the *discourse* in the strand, not the artefact itself (we also don’t read link content) and ii) the way we gather strand data, as Christine’s guide is part of a bigger story about TPOT definition and guides that didn’t show up in quotes or semantic matches.

[![](https://substackcdn.com/image/fetch/$s_!vboh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F02f36991-32d1-40e9-9720-dfbfe7c1a175_1210x404.png)](https://substackcdn.com/image/fetch/$s_!vboh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F02f36991-32d1-40e9-9720-dfbfe7c1a175_1210x404.png)

I also see some tweets highlighted sometimes that aren’t especially connected. Like this one with a culture war tone from someone who shares only 17 mutuals with me.

[![](https://substackcdn.com/image/fetch/$s_!zCab!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd45a64ad-2097-416f-b64e-b9963211e3a2_620x920.png)](https://substackcdn.com/image/fetch/$s_!zCab!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd45a64ad-2097-416f-b64e-b9963211e3a2_620x920.png)

I’d say this happens because we’re factoring in tweets that are streamed live from people who use the community archive extension. Right now, we’re getting most tweets that users see. It could be a good time to filter only for users who’ve opted-in to being streamed. It would give us a denser higher signal core. Long-term with adoption, the strategy of relying on the self-selection of users for quality will stop working and we’ll want to do some community-finding to filter our analysis.

[![](https://substackcdn.com/image/fetch/$s_!ENPN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2aaea087-3d41-4953-b278-f6261a5fbc59_1600x755.png)](https://substackcdn.com/image/fetch/$s_!ENPN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2aaea087-3d41-4953-b278-f6261a5fbc59_1600x755.png)

Figure: Essential tweets timeline, with explanations of what’s relevant about each plot point!

[![](https://substackcdn.com/image/fetch/$s_!XeeR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F93015e98-ea05-4c4f-81eb-250c2c33df8c_284x110.png)](https://substackcdn.com/image/fetch/$s_!XeeR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F93015e98-ea05-4c4f-81eb-250c2c33df8c_284x110.png)

Figure: If you click “Explore seeds” in the corner you’ll get to see all the underlying data in the seed rather than just the essentials. It may take a minute to load.

## rough themes among strands

I’m excited to see if we can weave different strands together into a cohesive tapestry. Could be cool to just get all the summaries and important tweets and throw them into an LLM.

On a first, non-exhaustive pass, I’m surprised I don’t see a Jhana strand, but we see some amount of

### dharma / inner work :

[![](https://substackcdn.com/image/fetch/$s_!a-I4!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc5ac1a26-0716-4ece-be47-8e76bfa0b0b4_1180x598.png)](https://substackcdn.com/image/fetch/$s_!a-I4!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc5ac1a26-0716-4ece-be47-8e76bfa0b0b4_1180x598.png)

[![](https://substackcdn.com/image/fetch/$s_!lKlS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F81a1cd71-7ab7-4c9a-9e61-4b661bc7245b_1180x550.png)](https://substackcdn.com/image/fetch/$s_!lKlS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F81a1cd71-7ab7-4c9a-9e61-4b661bc7245b_1180x550.png)

[![](https://substackcdn.com/image/fetch/$s_!dcrg!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1fe4890f-fe12-4277-a27b-3b95d176c763_1180x634.png)](https://substackcdn.com/image/fetch/$s_!dcrg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1fe4890f-fe12-4277-a27b-3b95d176c763_1180x634.png)

### community building and scenius:

[![](https://substackcdn.com/image/fetch/$s_!HawU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0bb7726f-df1d-4cf4-8c53-327bf3c09515_1176x398.png)](https://substackcdn.com/image/fetch/$s_!HawU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0bb7726f-df1d-4cf4-8c53-327bf3c09515_1176x398.png)

[![](https://substackcdn.com/image/fetch/$s_!N8xF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fabeb0de1-6a8b-40a7-862f-2d9f94ae12c2_1176x598.png)](https://substackcdn.com/image/fetch/$s_!N8xF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fabeb0de1-6a8b-40a7-862f-2d9f94ae12c2_1176x598.png)

[![](https://substackcdn.com/image/fetch/$s_!BuJl!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2dc788cc-56e7-4860-9bf6-f76f7c8992da_1176x598.png)](https://substackcdn.com/image/fetch/$s_!BuJl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2dc788cc-56e7-4860-9bf6-f76f7c8992da_1176x598.png)

### interpreting magic and spirituality and woo through materialist lenses:

[![](https://substackcdn.com/image/fetch/$s_!MfCJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcc7f8206-b9bb-4ad9-b29b-8ec767d463d0_1180x662.png)](https://substackcdn.com/image/fetch/$s_!MfCJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcc7f8206-b9bb-4ad9-b29b-8ec767d463d0_1180x662.png)

[![](https://substackcdn.com/image/fetch/$s_!5WGK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6cf52782-8807-4e77-9d06-609229e1231e_1180x404.png)](https://substackcdn.com/image/fetch/$s_!5WGK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6cf52782-8807-4e77-9d06-609229e1231e_1180x404.png)

[![](https://substackcdn.com/image/fetch/$s_!kzaE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F21fd8ef3-9322-4650-9ec3-85ed113db0c8_1180x816.png)](https://substackcdn.com/image/fetch/$s_!kzaE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F21fd8ef3-9322-4650-9ec3-85ed113db0c8_1180x816.png)

### the eigenprompt

[![](https://substackcdn.com/image/fetch/$s_!SEW8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F38af17d7-a750-4845-8ea0-28b09f7316e8_1180x524.png)](https://substackcdn.com/image/fetch/$s_!SEW8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F38af17d7-a750-4845-8ea0-28b09f7316e8_1180x524.png)

### the Community Archive and twitter tools!

[![](https://substackcdn.com/image/fetch/$s_!7jmu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcdcc5c51-ba66-41da-a0a1-b3335b03c872_1180x1366.png)](https://substackcdn.com/image/fetch/$s_!7jmu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcdcc5c51-ba66-41da-a0a1-b3335b03c872_1180x1366.png)

[![](https://substackcdn.com/image/fetch/$s_!cbnY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0a85bbd6-1a0e-4b3b-9990-785059619674_1180x662.png)](https://substackcdn.com/image/fetch/$s_!cbnY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0a85bbd6-1a0e-4b3b-9990-785059619674_1180x662.png)

### scene-steering

[![](https://substackcdn.com/image/fetch/$s_!TWHn!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd1e36fdc-4a3a-40c6-a49d-1d89a18d5528_1180x658.png)](https://substackcdn.com/image/fetch/$s_!TWHn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd1e36fdc-4a3a-40c6-a49d-1d89a18d5528_1180x658.png)

[![](https://substackcdn.com/image/fetch/$s_!3Tqs!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F02edcbc9-9286-4187-b8c1-fee7b1daf690_1180x1028.png)](https://substackcdn.com/image/fetch/$s_!3Tqs!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F02edcbc9-9286-4187-b8c1-fee7b1daf690_1180x1028.png)

[![](https://substackcdn.com/image/fetch/$s_!QKJQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F98c89b2d-0664-4b15-b493-5db4c6ce6580_1176x598.png)](https://substackcdn.com/image/fetch/$s_!QKJQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F98c89b2d-0664-4b15-b493-5db4c6ce6580_1176x598.png)

[![](https://substackcdn.com/image/fetch/$s_!k1Zt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5eb5ec5c-ab4a-4aac-a231-7d1b33457a41_1176x420.png)](https://substackcdn.com/image/fetch/$s_!k1Zt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5eb5ec5c-ab4a-4aac-a231-7d1b33457a41_1176x420.png)

## on illegibility

[![](https://substackcdn.com/image/fetch/$s_!Xdyx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5a281d21-ff11-4074-9d6c-6ee9f6976431_1180x546.png)](https://substackcdn.com/image/fetch/$s_!Xdyx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5a281d21-ff11-4074-9d6c-6ee9f6976431_1180x546.png)

A big value in old school tpot was illegibility. I haven’t stopped contending with the fact that the community archive and my research increase legibility. They make it easier to describe their subjects. I am fascinated with my online intellectual home and that leads me to want to understand it. The question of whether it’s good for it to be understood in public is still out.

My sense is that the internet is already a dark forest and tweets are already public, so anyone with sufficient resources and willingness could do it. However, I am doing it. I think there’s an argument that the scene should be strong to be ok in the public eye, and that understanding itself and its main ideas lets it tell its own story better which increases self-determination.

The original argument for illegibility was that the scene was young and needed to incubate but I think we’re far past that point. If anything, there’s a sense of stuckness that I hypothesize comes from having too much of a backlog of unintegrated insights, and this work is part of metabolizing them. Separating the wheat from the chaff, distillation that facilitates digestion. Literally a digestif.

[![](https://substackcdn.com/image/fetch/$s_!kVqz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3fd5f6c4-a612-4ac5-be6c-1a07de8423d1_1500x1000.png)](https://substackcdn.com/image/fetch/$s_!kVqz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3fd5f6c4-a612-4ac5-be6c-1a07de8423d1_1500x1000.png)

I’ve personally gotten a lot of value from existing in this part of twitter - friends, partners, co-founders, worldview updates, practices, funding - and believe that lots of juice has been produced here. There are many sub-cultures and ways of articulating the main value generated here. I think there are 2 things:

1. Tpot as a developmental container - people move through tpot, find their people, raise one another up, become more powerful, do projects, etc.
2. Postrats are uniquely positioned to unify the right and left brain - yin with yang - subjective and objective, spirituality and science. The most clearly useful version of this is pragmatic dharma and spiritual practices articulated in materialist terms, often with computer science metaphors. This very obviously potentiates the developmental container because it makes emotional tools accessible to smart and ambitious people that wouldn’t have them otherwise.

## Concluding

It’s still unclear to me how this directory will be valuable to others, but I’m feeling really good about my work so far. I realized 60% of my desire of seeing the postrat canon as a whole, and I feel like I’m fulfilling the work I described in [my funding proposal](https://xiqo.substack.com/p/building-tooling-to-map-how-ideas): We have embedding infrastructure, we’re testing our tools on past narratives, we’re iterating with the community by posting these lab notes.

I think letting the scene write its own story while resourced by a bird’s eye view of its discourse over the years is a pretty interesting idea. Will this help (some of) us chart a course? Reaffirm our enthusiasm and confidence that there are things to realize?

An interesting question is: what about real-time and the future? We rely pretty heavily on quote-tweets for these strands, and the closer you are to the present, the less meaningful QTs are, because they’re especially meaningful when they happen far away from original posting time, since they signify the OP is worth referring to. I haven’t given this much thought but I can see a world where we develop proxy metrics for QTs, or simply develop higher time-resolution methods for spotting promising emerging memes. No replacement for the real human taste that is leveraged in QTs, so we may want to involve more humans in the process somehow.

Again, I’m really happy with our work. Excited for you to read and explore the strands! Check it out [here](https://bangers.community-archive.org/best-strands).

We become more powerful as we get more data so please install the [CA stream extension](https://chromewebstore.google.com/detail/community-archive-stream/igclpobjpjlphgllncjcgaookmncegbk) to stream tweets you see to the archive. Consider also requesting your twitter archive and uploading to the [Community Archive](https://www.community-archive.org/).

PS: I’m raising for a 10x more ambitious project so if you work with or close to organizations like Cosmos, ARIA, Astera, Renaissance Philanthropy, I’d love to talk to you.