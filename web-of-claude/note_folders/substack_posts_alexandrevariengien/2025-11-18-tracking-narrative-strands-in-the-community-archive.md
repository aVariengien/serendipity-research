# Tracking narrative strands in the Community Archive

*On leveraging growth in AI agentic capabilities & an early progress update.*

Published: 2025-11-18
Source: https://alexandrevariengien.substack.com/p/tracking-narrative-strands-in-the

---

I talked yesterday about the vision of [building exoskeletons for online communities](https://alexandrevariengien.com/exoskeleton-for-communities). I’ll share here a progress update on the work we’ve been doing towards building an epistemic exoskeleton over the past two days with [@xiq](https://x.com/exgenesis).

### **Work philosophy.**

We want to find high-leverage opportunities where one hour of work translates into as much gain in community epistemics as possible. To achieve this, we are betting on the future progress of AI capabilities, especially agentic capabilities.

Many tools built on top of the Community Archive Twitter data have been developed using semantic embeddings (see [Magic Search](https://magicsearch.sofiavanhanen.fi/), [Birdseye](https://xiqo.substack.com/cp/163163201) or [Nomic’s embedding atlas](https://atlas.nomic.ai/data/brandon/twitter-community-archive-2025-04-05-212102643048/map)). Even though there are many interesting directions for improving our current embedding tech stack (e.g., adding temporally aware embeddings or prompt-guided embeddings), the returns are likely to saturate in the coming years. It is hard to envision how better embeddings would double the effectiveness of today’s applications or open up new designs that are unthinkable with today’s embedding technology (if you disagree, I would love to hear your thoughts!). In short, it feels unrealistic to expect embeddings in five years to deliver twice as much value as they do today.

In contrast, it is very likely that agentic capabilities will continue to advance. Our current best single source of evidence is the [METR study](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/) which shows that the time horizon of tasks AI agents can complete doubles every seven months. Having an AI agent that can reliably complete research tasks that normally take humans 26 minutes (GPT-5’s current time horizon for an 80% success rate) or six hours (predicted performance in two years if the trend continues) can be a game changer for the types of applications we can build.

This is guiding the way we think about our work. The output at long/medium term is something like journalist AI agents documenting community discourse. This has the potential to increase up dramatically the availability of high-quality sense-making and epistemic community services.

To that end, in the short-term, we are working to deliver two kinds of outputs:

* Manual research reports mapping the evolution of online discourse over time, which are valuable to the community.
* Technical primitives (e.g., embedding search and clustering, X thread manipulation tools, heuristic metrics to filter data, etc.) that support the research process.

The manual analyses can be thought of as high-quality few-shot examples that will guide the future AI journalist agent in demonstrating the kind of output we are interested in producing, while the technical primitives will serve as its toolbox.

### **Early progress report.**

#### **Data pipeline.**

* Loaded 300 million tweets from the community archive along with their embeddings from [Qwen3-4b](https://huggingface.co/Qwen/Qwen3-Embedding-4B). Importantly, the text of the embeddings is stripped of usernames like “@exgenesis.” This tends to create embeddings that cluster around usernames instead of semantics.
* Reduced the dimension from 1024 to 5 using UMAP.
* Ran KMeans to find 550 clusters (chosen to be roughly the square root of 300,000, the dataset size).
* For each cluster, picked consecutive chunks of tweets that span the entire time range of the cluster (e.g., a chunk of 10 consecutive tweets at the start, 10 in the middle, and 10 at the end). Asked a language model (here, OpenAI’s OSS-20b) to give a name to the cluster and rate its quality. We used a rubric made up of three scores, as defined in the prompt:

  + *discourse coherence (0-10)*: Not just thematic similarity but actual conversational threading - are people responding to/building on each other’s ideas? Referencing the same specific events, papers, people? You want to distinguish “everyone talking about AI” from “everyone discussing that specific Yudkowsky post from Tuesday.”
  + *generative density (0-10)*: This is your “new cultural production” metric. Are people synthesizing? Coining terms? Creating frameworks? You can spot this through novel metaphors, emergent terminology, conceptual bridges between previously unconnected ideas. A cluster about “animals” scores low, but “applying predator-prey dynamics to social media algorithms” might score high.
  + *temporal coherence (0-10)*: Does the cluster represent an actual unfolding discourse with a beginning, middle, and development? Or is it just random samples of similar content across time? Look for cascading responses, evolution of arguments, and people changing positions.
* We then looked at the cluster with the highest average score among the three dimensions. We also examined the evolution of tweets in the cluster over time to check for interesting trends.
* Finally, we selected interesting clusters and used Claude to analyze all the tweets in the cluster (often around 1,000 tweets) and extract interesting strands of discourse that unfold over the years.

Here are a few plots of the data.

[![img1](https://substackcdn.com/image/fetch/$s_!eCf0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F059129a2-51b3-4267-ac1a-44bba0e075d1_1158x1022.png "img1")](https://substackcdn.com/image/fetch/$s_!eCf0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F059129a2-51b3-4267-ac1a-44bba0e075d1_1158x1022.png)

*2D UMAP plot (for visualization only) of a subset of the tweets. Colors correspond to the clusters; the crosses indicate the clusters’ centroids.*

[![img1](https://substackcdn.com/image/fetch/$s_!ADKq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd339d7b3-10cf-4967-aae5-5b09c75a4e1a_2094x888.png "img1")](https://substackcdn.com/image/fetch/$s_!ADKq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd339d7b3-10cf-4967-aae5-5b09c75a4e1a_2094x888.png)

*Volume of tweets over time. Most tweets are recent.*

[![img1](https://substackcdn.com/image/fetch/$s_!KCLv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fac52c077-5730-46c0-bbb1-50f82394fd53_2094x900.png "img1")](https://substackcdn.com/image/fetch/$s_!KCLv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fac52c077-5730-46c0-bbb1-50f82394fd53_2094x900.png)

*Volume of tweets over time of the day. The East Coast timezone likely dominates the trend, as 9am UTC is 4am EST, which is consistent with the lowest activity.*

#### **Early results.**

Here are a few findings from this data pipeline from one day of work. They are signs of life the techniques we used can surface non-trivial phenomena that might be good starting points for manual analysis.

**The Sangha is the new Buddha**

In the cluster called “Digital Sangha Narrative,” we have a series of tweets spanning several years:

1. “The next Buddha may take the form of a community – a community practicing understanding and loving kindness…” – Thich Nhat Hanh

   2009/06/27 @technoshaman
2. *@szpak Mark, do you have some reference to Chogyam #Trungpa’s saying that #Maitreya, the Buddha of the future, will not be an individual but #society?*

   ***[2011-02-27] @technoshaman***
3. *RT @dthorson: The next Buddha is sangha. The next sangha is the network. The next Buddha is the network.*

   ***[2018-02-02] @tasshinfogleman***
4. *The next Buddha will be a manga.*

   ***[2023-05-17] @the\_wilderless***
5. *Divinely protected  
   God’s hand selected  
   Hivemind infected*

   *The next Buddha is a sangha.*

   *The incoming prophet is a collective.*

   ***[2025-06-20] @mudscryer***
6. *The next Buddha is a sangha (TPOT).*

   ***[2025-09-10] @nosilverv***

It starts with a quote from Thich Nhat Hanh in the early days of Twitter in 2009, with a few variations over the years. By 2025, now TPOT (This Place of Twitter) has become a thing, the sangha is TPOT.

**Crypto and Bitcoin Trends**

We have two clusters related to crypto: one called Tokenization & Crypto Evolution and the other Bitcoin Evolution Narrative. The number of tweets in this cluster over time matches the four-year cycles of Bitcoin, with clear spikes in activity in late 2013, 2017, 2021, and 2025. We are unsure about how significant this is, it was consistent enough to be worth reporting.

Here is a plot showing the activity of the two crypto cluster (blue and orange curves) as well as the “Digital Sangha Narrative” cluster (in green) as a control. Below the plot is the Bitcoin price curve with a logarithmic y-axis for comparison.

[![img1](https://substackcdn.com/image/fetch/$s_!sdZv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F371b9366-f261-4fd7-9905-bc2975102e28_1270x628.png "img1")](https://substackcdn.com/image/fetch/$s_!sdZv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F371b9366-f261-4fd7-9905-bc2975102e28_1270x628.png)

[![img1](https://substackcdn.com/image/fetch/$s_!Fluv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3abb4ded-65e9-4abd-8036-037ae86819c4_1843x981.jpeg "img1")](https://substackcdn.com/image/fetch/$s_!Fluv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3abb4ded-65e9-4abd-8036-037ae86819c4_1843x981.jpeg)

### **Departing thoughts**

If you are interested in exploring the content of the clusters yourself, you can download a zip file with the 550 clusters [here](https://drive.google.com/file/d/19c_4lGhnBL6k4k6SDOcgxG38JI1Q8Wea/view?usp=sharing). AI has the potential to bring chaotic dynamics to the information sphere, we are excited to find ways to balance this with stronger online communities!