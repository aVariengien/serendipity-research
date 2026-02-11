# Bangers! are highly quoted tweets | lab notes #2

*xiq and alexandre's first two weeks: we explore extracting narrative strands from clusters in the community archive and ship Bangers*

Published: 2025-12-01
Source: https://xiqo.substack.com/p/2-xiq-and-alexandre-week-1-and-2

---

*This update was written by Alexandre*

@xiq and Alexandre have been experimenting with peer working for the past two weeks. Here is how it went.

**Output / narrative**

We started with the idea to build tools to help with documenting memetic lineages, i.e. identifying lines of discourses where people are building on others’ ideas over an extended period of time to collectively produce new knowledge. Our strategy was to start with building tools to mine the community archive to find promising seeds for interesting lineages that we would then investigate manually.

In the first week, we build a pipeline to

1. Cluster tweet embeddings
2. Augment all the tweets content by printing a tree of the thread they are part of
3. Give the augmented content to an LLM, and ask it to identify narrative strands from the cluster data and score them.
4. Manually look at high-scoring narrative strands, and

We got the clustering running on the first day, and finished a vertical slice, picking a few clusters and skipping step 2 for speed to validate the idea. We documented the process and early results [here.](https://substack.com/home/post/p-179280797)

Over the next few days, we spent time on an efficient implementation of step 2, which turned out more complicated than expected. By Friday we had the whole pipeline running (though on a subset of the CA), and by looking at the type of narrative strands, the results were mixed.

The strands picked up by Gemini 3 Pro were interesting themes (e.g. picking up on the rise of the fetters), but when digging into the LLM-generated description of the strand narrative, the tweets quoted didn’t support the claims. The model was not quite bad at interpreting tweets. Tweets are high context, often half-jokes and half-serious, and Gemini tends to take them as factual statements. By looking at the strands, it also seemed like the model picked one interesting thread and complemented it with mildly related tweets that came before and after and called it a “strand” of discourse, even if the tweets didn’t really build on each other.

This observation reflected the vagueness of our prompt: what was a narrative strand, really? Should it be defined purely semantically, or incorporate information from the social graph, trying to reconstruct a causal graph of influence?

In general, this diminished our excitement with our naive pipeline, and decided not to scale up to apply it to the whole CA. Though we are not giving up on the idea of narrative strand. We stay optimistic that i) applying to the whole archive and filtering well will lead to cool discovery, sometimes more is different ii) clearer definition work could help.[1](https://xiqo.substack.com/p/2-xiq-and-alexandre-week-1-and-2#footnote-1-180360414)

Instead, we decided to leverage a neat metric from playing with the dataset: the number of times a tweet gets quoted by users from the CA that are not the author. It surfaced popular tweets from the TPOT canon. There was a high concentration of important units of knowledge that have been referenced in multiple contexts.

We spent the first three days of week 2 building a website that referenced the highest quoted tweets for each year. Inspired by [Andy Matuschak’s notes website](https://notes.andymatuschak.org/), we build an explorer to look at the quotes from the tweet, the thread the tweet is part of, and semantically similar tweets. The goal was to make a tool so we could manually explore threads of influence from top tweets, and write reports about some top picks.

Throughout the week, we also spend ~ 20-30% of the time brainstorming about the general mission of our project, trying to see if we can come up with a concrete and ambitious pitch we could get excited by.

By the last days, this ratio rose to ~ 80%, and spent most of the working time brainstorming on a tldraw canvas.

Some guiding questions we explored were:

* If we are building tools for TPOT powerusers, they are the people that already know best the content from the community archive, maybe even produced a fair bit of its canon. What new and useful interface to this information can we provide to these powerusers?
* What should be the desiderata for a nooscope?
* If there were a FRO about large scale online coordination, what should be its metric?

More reflections on strategy and vision later.

Next week we’re hoping to refocus on finding narrative strands. We think we will start by generating strands from individual seed tweets. If we have time, we would like to make a second pass at obtaining coherent narrative strands from clustering and publishing a website of “memes” analogous to [neuronpedia](https://www.neuronpedia.org/) in LLM interpretability.

[1](https://xiqo.substack.com/p/2-xiq-and-alexandre-week-1-and-2#footnote-anchor-1-180360414)

And prompt tweaks and scaffolding can help - lit review tools like Elicit I’m sure have citations working very well. And I wonder if we can deliver an ontology twitter cultural production that factors humor in