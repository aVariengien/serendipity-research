# Weekend Links #4: faxing ChatGPT, homemade nuclear reactor, flu

*Also AI forecasters, GPT-5, the next Claude, and AI designing AI chips*

Published: 2025-02-23
Source: https://peterwildeford.substack.com/p/weekend-links-4-faxing-chatgpt-homemade

---

[![city skyline with lights turned on during night time](https://images.unsplash.com/photo-1591200834528-4050ce99fe78?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wzMDAzMzh8MHwxfHNlYXJjaHwzfHxudWNsZWFyJTIwcmVhY3RvcnxlbnwwfHx8fDE3NDAyOTg4ODV8MA&ixlib=rb-4.0.3&q=80&w=1080 "city skyline with lights turned on during night time")](https://images.unsplash.com/photo-1591200834528-4050ce99fe78?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wzMDAzMzh8MHwxfHNlYXJjaHwzfHxudWNsZWFyJTIwcmVhY3RvcnxlbnwwfHx8fDE3NDAyOTg4ODV8MA&ixlib=rb-4.0.3&q=80&w=1080)

Photo by [Nicolas HIPPERT](true) on [Unsplash](https://unsplash.com)

*A good forecaster reads constantly. However, like the power laws this blog is named for, some readings matter far more than others. Each weekend, I'll share the standouts …along with some occasional fascinating rabbit holes. Some weekends will be light, others heavy (that's how power laws work), but each link will be worth your weekend morning coffee time.*

Want more links like this? Subscribe:

# AI

**…GPT-4.5 coming next week, GPT-5 coming late May?**

[Per the Verge](https://www.theverge.com/notepad-microsoft-newsletter/616464/microsoft-prepares-for-openais-gpt-5-model), the OpenAI roadmap is advancing soon. Microsoft is rumored to already be preparing server capacity for a launch of GPT-4.5 (the long awaited Orion) as early as next week and GPT-5 coming in late May (integrating improved base models with the o3 reasoning model).

Microsoft's preparation includes revamping its Copilot interface to simplify model selection and developing its own version of OpenAI's Operator AI agent for web automation. The timing of GPT-5's release appears strategically aligned with Microsoft's Build developer conference, which will compete directly with Google I/O.

~

**…OpenAI chip development**

OpenAI has started an ambitious push into custom chip development — [Reuters reveals](https://www.reuters.com/technology/openai-set-finalize-first-custom-chip-design-this-year-2025-02-10/) that OpenAI is finalizing its first in-house AI chip design for fabrication at TSMC, aiming for mass production in 2026, led by former Google chip expert Richard Ho. The project's details suggest significant progress: a 40-person team collaborating with Broadcom, using TSMC's advanced 3-nanometer process technology, and incorporating high-bandwidth memory and extensive networking capabilities.

The chip may be seen as an attempt to reduce dependence on Nvidia chips, but that’s still a ways off. OpenAI’s new chip is designed for inference, so Nvidia chips will still be needed for training. Nvidia still has a roughly 80% market share in AI chips and a much stronger software stack.

The only company that has succeeded so far at getting away from Nvidia is Google, with their custom TPU chips, though Google still uses a notable number of Nvidia chips internally.

[![Image](https://substackcdn.com/image/fetch/$s_!rzHm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F21976238-14a4-4f2d-a32a-11928d1efb8b_2400x1512.png "Image")](https://substackcdn.com/image/fetch/$s_!rzHm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F21976238-14a4-4f2d-a32a-11928d1efb8b_2400x1512.png)

[(Source)](https://epoch.ai/data/machine-learning-hardware#computing-capacity)

Amazon has tried to build their own chip with Trainium, though these have been less successful than TPUs and are used mainly for specific AWS workloads. Though there’s limited public data on Trainium’s actual performance and adoption, this suggests it may be hard to replace Nvidia chips despite massive resources. History suggests success requires more than just silicon - it demands competitive performance, software stack maturity, developer adoption, and manufacturing scale across multiple generations.

~

**…The next piece of the OpenAI diaspora**

Well we finally know where OpenAI ex-CTO Mira Murati is going. She and former OpenAI top researcher John Schulman have launched [Thinking Machines Lab](https://thinkingmachines.ai/), a new AI research and product company that aims to make advanced AI systems more widely understood, customizable and capable. Though it’s not yet clear what that means.

Like every other company that came out of OpenAI (and OpenAI itself), they have founding ambitions to be safe and magnanimous towards humanity — they claim a scientific transparency through frequent publication of technical content, a focus on human-AI collaboration rather than full autonomy, and planning to maintain high safety standards while maximizing user freedom. However, they of course maintain that pushing the boundaries of model capabilities remains crucial for enabling transformative applications.

~

**…We’ve been hearing a lot about OpenAI… what is Anthropic up to?**

Sam Altman grabs the headlines and there’s certainly been no shortage of attention-grabbing drama. Anthropic, on the other hand, is taking a more quiet approach. Unlike OpenAI with a bunch of different models in the model picker, Anthropic has focused very heavily on a single Claude model — with the somewhat dumb name “Claude 3.5 Sonnet (New)”. The model itself is also very focused — it doesn’t also draw pictures, browse the web, use in-depth reasoning, have differing levels of thinking time the user can choose, or anything else. And this may seem underwhelming — Claude is nowhere to be found at the top of [the Chatbot Arena leaderboard](https://lmarena.ai/?leaderboard), behind a bunch of Chinese models.

Yet still Claude is still somehow surprisingly compelling — it’s still my go-to model for most everyday tasks, writing help, tasks requiring emotional intelligence, and software engineering. Unless deeper reasoning or web browsing is required, I personally turn to Claude more often than not.

And I don’t think I’m alone in this, at least for people who buy multiple AI subscriptions and have the luxury to pick and choose. I’m not exactly sure how Claude has managed to pull this off — how is their model still better at coding, despite not using more in-depth reasoning than OpenAI?

And how has Anthropic been doing well at enterprise sales, having cut a large amount into OpenAI’s enterprise lead and embarrassing Google?

[![Image](https://substackcdn.com/image/fetch/$s_!QDPO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde0e9786-8e5e-40ee-8ec3-178f53dcfb6f_1179x1652.jpeg "Image")](https://substackcdn.com/image/fetch/$s_!QDPO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde0e9786-8e5e-40ee-8ec3-178f53dcfb6f_1179x1652.jpeg)

Given how good Claude already is, it’s cool to see Anthropic is finally close to rolling out something new. The Information reports [Anthropic is working on a hybrid model](https://www.theinformation.com/articles/anthropic-strikes-back):

> Anthropic is taking a slightly different approach to reasoning. It has developed a hybrid AI model that includes reasoning capabilities, which basically means the model uses more computational resources to calculate answers to hard questions. But the model can also handle simpler tasks quickly, without the extra work, by acting like a traditional large language model. The company plans to release it in the coming weeks, according to a person who’s used it.

This sounds similar to what Altman said in [his roadmap](https://x.com/sama/status/1889755723078443244): “a top goal for us is to unify o-series models and GPT-series models by creating systems that can use all our tools, know when to think for a long time or not, and generally be useful for a very wide range of tasks”. It seems like for this milestone, Anthropic may get there first.

~

**…AI is better at geometry than top mathematicians**

The [International Mathematical Olympiad](https://www.imo-official.org/) (IMO) is essentially the world championship of high school mathematics, where about 600 of the world's most talented young mathematicians compete each year. A "Gold Medal" performance means scoring around 25-42 points out of 42, typically awarded to the top ~8% of participants.

What makes a potential “IMO Gold” level AI performance particularly significant is that these problems require deep mathematical reasoning, creative problem-solving, and the construction of novel proofs - not just calculation or pattern matching. Unlike games like chess or Go, you can't solve IMO problems by searching through possibilities or applying standard techniques. Each problem demands creative insights and rigorous logical arguments.

We’re now one step closer to this milestone, which seems nearly inevitable to happen later this year. AlphaGeometry2, an AI system developed by Google DeepMind, [can solve 84% of International Mathematical Olympiad (IMO) geometry problems from the past 25 years](https://techcrunch.com/2025/02/07/deepmind-claims-its-ai-performs-better-than-international-mathematical-olympiad-gold-medalists/), exceeding the average performance of gold medalists.

The system combines two key components: a language model from Google's Gemini family and a symbolic engine. When tested on 50 IMO geometry problems, AlphaGeometry2 solved 42 of them, surpassing the average gold medalist score of 40.9. The system was trained on over 300 million synthetically generated theorems and proofs due to the limited availability of real-world training data.

While impressive, AlphaGeometry2 has limitations, including inability to handle problems with variable points, nonlinear equations, and inequalities. The system's success highlights an important debate in AI development between neural networks and symbolic manipulation approaches, suggesting that a hybrid approach combining both methods might be most effective for achieving generalizable AI.

~

**…AI can improve GPU designs as well**

Current AI models can already provide significant speedups in GPU kernel optimization, achieving average improvements of 1.8x over baseline implementations. [METR researchers evaluated frontier models' ability to automate the optimization of GPU compute kernels](https://metr.org/blog/2025-02-14-measuring-automated-kernel-engineering/), which are critical building blocks for AI training and inference.

A GPU kernel is a specialized piece of code that runs directly on a graphics processing unit (GPU). Unlike regular CPU code, GPU kernels are designed to execute the same instructions across many data points in parallel - think of it like having hundreds or thousands of tiny processors all doing the same operation simultaneously.

GPU kernels are the fundamental building blocks of high-performance computing and AI/ML operations. Writing efficient kernels requires deep understanding of hardware architecture, memory patterns, and parallel computing. A well-written kernel can be orders of magnitude faster than poorly optimized code.

A “kernel writing task” refers to getting an AI to automatically generate these GPU kernels - essentially, having AI write high-performance code that runs directly on graphics hardware.

To look into this, METR modified KernelBench, a benchmark of kernel writing tasks, and added new challenging problems based on 2024 AI workloads. Using their “KernelAgent” framework with proper scaffolding and multiple optimization attempts, they found that current models like OpenAI o3-mini could achieve 1.81x average speedup across tasks. More notably, taking the best results across multiple models yielded a 2.01x improvement - double the performance from just 6 months prior.

The researchers emphasize these results highlight the importance of proper capability elicitation — while the original KernelBench showed only modest 1.05x improvements, better scaffolding and increased compute revealed much higher potential. Using ~$50K in token + compute costs and four weeks of total engineering time, METR substantially advanced the state of the art on KernelBench. However, METR cautions that current AI systems still cannot match human experts on sophisticated optimizations and frontier labs typically invest orders of magnitude more engineering effort into kernel optimization.

**If you’re interested in this kind of work, [METR is hiring](https://hiring.metr.org/).** METR are the ones who helped make testing for autonomous capabilities an industry standard and work directly with major players like OpenAI and Anthropic to evaluate models pre-release. They needs Senior Software Engineers, DevOps Engineers, and ML Research Scientists to join their Bay Area office (in-person preferred, hybrid possible). They offer competitive compensation potentially above $400K/yr, unlimited PTO, comprehensive benefits, and visa sponsorship. No strict deadlines - applications are rolling.

~

**…South Korea is getting a data center**

I’m interested in tracking where different countries are at in AI development, so it was interesting to see South Korea plan a $35B project to build a 3GW data center with completion targeted in 2028, [per WSJ reporting](https://www.wsj.com/tech/ai/ai-data-center-with-up-to-3-gigawatts-of-power-is-envisioned-for-south-korea-5141bd77). This is triple the capacity of the current 1GW data center being built for the Stargate project, but that’s not an apples-to-apples comparison given that (a) the current data center for Stargate will be completed about two years earlier and (b) the $100B/yr investment in Stargate is about building out more than one data center.

My country AI power rankings are currently still USA > China > *… (large gap) …* France > UK > *…(large gap) …* rest of world.

~

**…AIs get frustrated and give up too, they’re just like us**

TechCrunch profiles how [researchers used NPR Sunday Puzzle questions to benchmark AI 'reasoning' models](https://techcrunch.com/2025/02/16/these-researchers-used-npr-sunday-puzzle-questions-to-benchmark-ai-reasoning-models/). OpenAI's o1 achieved the highest score at 59%, but the fun part comes from DeepSeek's R1 model which exhibited remarkably human-like behaviors in its chain of thought, explicitly stating “I give up” when stumped and showing signs of frustration, sometimes providing answers it knew were incorrect.

~

**…Will your AI remember you? Soon it will!**

In other news, [it looks like AIs are now being trained to have better memory between conversations](https://x.com/GeminiApp/status/1890137961871605863). OpenAI already has a memory feature, but it isn’t very good — this is supposed to be better. I think this would be a quite important step towards making AI feel and act more human, as well as expand its capabilities.

# Forecasting

**…AI forecasters coming soon**

AI forecasting bots are rapidly closing the performance gap with elite human forecasters, though they haven't quite caught up yet. [Researchers at Metaculus reveal](https://www.metaculus.com/notebooks/35291/q4-ai-benchmarking-results/) that while their team of professional forecasters still outperformed the best AI systems, the margin has narrowed significantly compared to previous quarters, the gap moving from 11.3 to 8.9 in relative scoring. The analysis covers 402 real-world forecasting questions tackled by 44 competing bots, with human benchmarking on 122 of those questions.

The standout performer was a bot called “pgodzinai”, created by software engineer Phil Godzin, which achieved unprecedented accuracy by grouping related questions together and using a combination of different language models. The bot's approach included sophisticated prompting strategies and leveraging multiple news sources, though it still fell short of human performance. Notably, while both humans and bots showed good calibration, humans demonstrated superior discrimination ability - they were better at distinguishing which events would actually occur.

The broader implications suggest that AI systems are making rapid progress in complex real-world reasoning tasks, but still lack certain key capabilities that give human experts an edge, likely in information gathering and handling unknown unknowns.

~

**…What does good forecasting look like?**

In [“Talent Spotting in Crowd Prediction”](https://gwern.net/doc/statistics/prediction/2023-atanasov.pdf), researchers Pavel Atanasov and Mark Himmelstein demonstrate that the most reliable way to identify skilled forecasters is to observe their prediction-making process rather than examining their background.

Strong forecasters typically update their predictions frequently but incrementally, showing ongoing engagement with new information rather than making dramatic shifts. They tend to make initial predictions that align reasonably with consensus while being slightly more extreme, suggesting an ability to build on collective wisdom with unique insights. Surprisingly, traditional markers of expertise such as advanced degrees, years of experience, and self-reported confidence show little correlation with forecasting accuracy.

The implications extend beyond tournament forecasting to how organizations should approach talent identification. Rather than relying on resumes or stated expertise, organizations would do better to assess candidates through their systematic thinking abilities, comfort with numerical reasoning, and willingness to update their views in response to new evidence. This represents a significant shift from traditional credential-based evaluation.

# Lifestyle

**…There’s a lot of flu out there**

[Katelyn Jetelina outlines unprecedented flu levels in the US](https://yourlocalepidemiologist.substack.com/p/flu-breaking-records-measles-tuna): current influenza-like illness levels have reached heights unseen since the 1990s, with hospitalization rates exceeding the past 15 years' records.

[![](https://substackcdn.com/image/fetch/$s_!Covc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0618e45d-650b-474b-a017-b18ca9aac192_800x908.png)](https://substackcdn.com/image/fetch/$s_!Covc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0618e45d-650b-474b-a017-b18ca9aac192_800x908.png)

# Whimsy

**…Faxing ChatGPT**

Fax machines are finally getting the upgrade they need for the AI era! [FaxKI](https://simple-fax.de/fax-ki) is a service that lets users interact with ChatGPT via fax machine. Users send fax queries to a designated number, with ChatGPT's responses returned via fax. Costing as little as seven euro cents per transmission.

~

**…A homemade nuclear reactor**

Never doubt that college kids can do things. Back in 1999, two University of Chicago physics students managed to [build a functioning nuclear reactor in their dorm room,](https://mag.uchicago.edu/science-medicine/homemade-breeder-reactor) successfully producing (admittedly microscopic quantities) of weapons-grade uranium and plutonium, all as part of a scavenger hunt competition.

The students used salvaged equipment and materials borrowed from their physics department, borrowing alpha radiation sources from WWII aircraft gauges and thorium dioxide from old TV tubes to create a neutron source. Then using $20,000 worth of borrowed analytical equipment, the students detected approximately 8,000 atoms of uranium-235 and 2,000 atoms of plutonium-239. Their work was verified by a nuclear engineer brought in to judge the competition, though the quantities produced were far too small to pose any real danger. While the project raised some concerns among university administration, the students faced minimal consequences.

~

**[Things Unexpectedly Named After People](https://notes.rolandcrosby.com/posts/unexpectedly-eponymous/).** Some of my favorites:

* Taco Bell (Glen Bell)
* Westlake, Los Angeles (Henricus Wallace Westlake)
* Main Street, San Francisco (Charles Main)
* Snowflake, AZ (two people named Snow and Flake)
* PageRank (Larry Page)
* MySQL (My Widenius)
* Debian (two people named Deb and Ian)
* New Relic (anagram of Lew Cirne)

~

**…Who is Cleo?**

“Cleo” was a pseudonoymous member of the math website MathStackExchange, whose legend began in 2013 when she started posting flawless solutions to extraordinarily complex mathematical integrals without any explanation. What made Cleo remarkable wasn't just the solutions themselves - she would solve problems so intricate that even advanced computer algebra systems like Mathematica failed, often responding within hours or even minutes of the questions being posted. One famous example involved an integral that looked like “the spine of a long-necked dinosaur” - while computers failed to solve it, Cleo provided the elegant solution “4π times the arccotangent of the square root of the golden ratio” just four and a half hours after the question appeared. This mysterious behavior spawned countless theories, with some wondering if she might be a secret computer program or even renowned mathematicians like Terence Tao working incognito.

However, [the identity has now been revealed](https://www.youtube.com/watch?v=7gQ9DnSYsXg) — through an anonymous viewer's investigation of email recovery addresses, they found that a recovery email starting with "vres" matched perfectly with Vladimir Rashnikov, an active Math Stack Exchange user. Further digital forensics revealed Rashnikov controlled not just Cleo but an entire network of interconnected accounts.

Rather than trolling or showing off mathematical prowess, Rashnikov created Cleo out of a genuine love for pure mathematical challenge and frustration with Stack Exchange's dismissive attitude toward “mere” puzzle-solving. His methodology was ingenious: he would start with problems Mathematica could solve, then carefully modify them until they became unsolvable by computer but retained an elegant solution structure. He would post these challenging problems using alternate accounts, then provide solutions as Cleo to spark engagement and encourage others to work out detailed proofs. While there may have been a small element of spite in his approach, the primary goal was to create mathematical engagement and challenge others to solve interesting problems - a goal he largely achieved, even if through unconventional means.

~

**…Pretty wild mathematical equivalence**

[![](https://substackcdn.com/image/fetch/$s_!jyen!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F70fcd62f-4a1b-4510-8df7-0c1b5c93449e_2190x478.png)](https://substackcdn.com/image/fetch/$s_!jyen!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F70fcd62f-4a1b-4510-8df7-0c1b5c93449e_2190x478.png)

…[Here’s why:](https://en.wikipedia.org/wiki/Wallis_product)

[![](https://substackcdn.com/image/fetch/$s_!Blt9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa8e89266-50c6-49f5-9b8b-81e1deb8953b_796x232.png)](https://substackcdn.com/image/fetch/$s_!Blt9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa8e89266-50c6-49f5-9b8b-81e1deb8953b_796x232.png)

Liked these links? Subscribe to get them in your email inbox every morning!

Subscribe