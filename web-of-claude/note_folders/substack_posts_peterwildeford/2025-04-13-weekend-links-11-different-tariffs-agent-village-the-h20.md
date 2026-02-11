# Weekend Links #11: Different tariffs, Agent Village, the H20

*Also GPT4.1, GPT4.5, a great fellowship, time, and space*

Published: 2025-04-13
Source: https://peterwildeford.substack.com/p/weekend-links-11-different-tariffs

---

[![How DeepSeek's AI models gave NVIDIA's H20 chips a major boost in China,  sent demand skyrocketing – Firstpost](https://substackcdn.com/image/fetch/$s_!oEYy!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff47afd84-f9dc-49d8-8e10-e11922bc75bd_596x336.jpeg "How DeepSeek's AI models gave NVIDIA's H20 chips a major boost in China,  sent demand skyrocketing – Firstpost")](https://substackcdn.com/image/fetch/$s_!oEYy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff47afd84-f9dc-49d8-8e10-e11922bc75bd_596x336.jpeg)

***About the author:** Peter Wildeford is a top forecaster, ranked top 1% every year since 2022. Here, he shares the news and analysis that informs his forecasts.*

# AI

#### Tariffs *again*, but *different* — *new* implications for AI?

[Last week I discussed](https://peterwildeford.substack.com/p/weekend-links-10-tariffs-gemini-and) 32% tariffs on Taiwan and how this could slow down the US race for AI, because key inputs like GPUs would become more expensive. I had concluded this could slow down US AI development by a small amount.

However it is now the case that AI development likely won’t be slowed at all.

* Firstly, as it turns out, about 60% of Nvidia chips [actually have final assembly within Mexico](https://x.com/rwang07/status/1909274816965759015), are imported to the US via Mexico, and are thus covered by the USMCA agreement exceptions and don’t have tariffs.
* And the tariffs today are completely different now than they were last week.
* **[And in all cases GPUs are now fully exempt from the tariffs](https://x.com/dkaushik96/status/1911038818544996707)**

We still do need to worry some about data center construction costs unrelated to GPUs, but [according to Semianalysis](https://semianalysis.com/2025/04/10/tariff-armageddon-gpu-loopholes/) the overall impact is minimal — only a ~2% increase in cluster total cost of ownership.

**The biggest deal will be economic uncertainty.** How can you build data centers if the costs of input keep changing every week? And could an escalating trade war between the US and China create a financial downturn that harms large AI companies and their investors?

* OpenAI is funded by SoftBank. SoftBank is a highly leveraged investor — this means that they borrow a lot of money to invest which can get outsized returns, but also means that small decreases in value could collapse the whole enterprise if they can’t pay back their debt. That means an economic downturn could be exceptionally bad news for SoftBank and thus potentially for OpenAI as well.
* An economic downturn also could force companies like Google and Meta to prioritize revenue-generating product investments over larger training infrastructure buildouts.

Overall, the net effect is unclear and possibly small, but with much more uncertainty and risk than before.

I feel bad for every tariff reporter (which I guess now includes me to some extent) because it takes at least a week to do good analysis on this and tariffs are currently changing faster than that. Have we finally reached the tariff singularity? Is this what reporting on AI is going to look like? Nice to get some practice.

[![](https://substackcdn.com/image/fetch/$s_!p1Ay!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b485dd2-f7a8-4672-bd2f-a8d703cfa4b8_1132x980.png)](https://substackcdn.com/image/fetch/$s_!p1Ay!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b485dd2-f7a8-4672-bd2f-a8d703cfa4b8_1132x980.png)

[(Source)](https://x.com/JosephPolitano/status/1911137897526206514)

~

#### Seriously, can we just control the H20 chip?

Let’s venture away from tariffs now and to export controls.

The US puts export controls on top computer chips to prevent adversaries like China and Russia from using American technology to train powerful AI systems. Due to strong civil-military fusion, there’s too much concern that the Chinese military would use this AI to hurt American interests.

However, current US chip export controls have focused primarily on China's ability to *train* frontier AI models. But now, thanks to reasoning models, agentic AI, and the possibility of automated research, it is *inference*, or running the models, where most of the value lies.

The key is *interconnect*. This is what enables multiple GPUs to communicate efficiently in AI clusters. We currently have controls on chips for computational performance, but allow chips with unlimited interconnect bandwidth.

This is why NVIDIA’s H20 GPU is important. The H20 provides vastly superior bandwidth and latency compared to what China has, which is what enables an efficient inference workload. It’s a loophole in the current export control strategy, by doing just enough to dodge current controls but giving massive inference capabilities to the CCP.

Here’s a graph showing current export controls — red = controlled/banned, green = legal. Currently, NVIDIA can legally sell chips with as much interconnect bandwidth as they want. They only face limits on computational performance. Due to the DeepSeek and reasoning model era, we need to place limits on interconnect bandwidth as well.

[![](https://substackcdn.com/image/fetch/$s_!3IwE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd413783-e1b0-4124-822b-69c486cc7017_722x516.png)](https://substackcdn.com/image/fetch/$s_!3IwE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd413783-e1b0-4124-822b-69c486cc7017_722x516.png)

Source: [ChinaTalk](https://www.chinatalk.media/p/ban-the-h20-competing-in-the-inference)

While China has made progress on individual AI chips, they significantly lag in developing chips with comparable interconnect capabilities. An export control on chips with high interconnect bandwidth would help slow China’s AI progress and prevent US tech from helping our adversaries.

This is why it was very frustrating to learn of two things:

* [China is stockpiling H20 chips anticipating a ban](https://www.reuters.com/technology/chinese-firms-place-16-billion-order-new-nvidia-chips-information-reports-2025-04-02/), with over $16B in purchases
* The **[Trump administration is backing off export controls on the H20](https://www.npr.org/2025/04/09/nx-s1-5356480/nvidia-china-ai-h20-chips-trump)** after Nvidia CEO Jensen Huang paid $1M to have dinner with President Trump.

We need to place the restrictions before China completes their stockpile.

H20 restrictions had been in development for months and were ready to be implemented as early as this week. But after Nvidia promised new US investments in AI data centers, Trump is reported to have changed his mind. These investments are not worth the massive opportunity we’re giving to China by permitting the sales of these chips.

~

#### Murati’s Thinking Machines raising $2B, potential largest seed round ever

One might think that all the uncertainty with tariffs would hurt the VC environment for AI startups without much track record. One would be wrong.

Back in [Weekend Links #4](https://peterwildeford.substack.com/p/weekend-links-4-faxing-chatgpt-homemade), I covered OpenAI ex-CTO Mira Murati and former OpenAI top researcher John Schulman’s launch of [Thinking Machines Lab](https://thinkingmachines.ai/). Now, it’s reported that **[Thinking Machines has doubled their fundraising target to $2 billion](https://www.businessinsider.com/mira-murati-new-ai-startup-thinking-machines-funding-2025-4)**, potentially at a $10B valuation. Two months ago, TML was planning to raise just $1B. This could be the largest seed round in history and a bullish sign for the AI market.

Thinking Machines is less than a year old, has unclear aims, and no known products. But one thing they do have is talent — they have assembled an all-star team of former OpenAI talent. [Per Business Insider](https://www.businessinsider.com/mira-murati-new-ai-startup-thinking-machines-funding-2025-4), the team now includes:

* Bob McGrew, former OpenAI chief research officer
* Alec Radford, co-creator of GPT and foundational researcher behind many breakthrough language models
* Jonathan Lachman, former Head of Special Projects at OpenAI
* Barret Zoph, architecture search researcher from Google Brain who developed AutoML
* and Alexander Kirillov, who led Advanced Voice Mode at OpenAI and Facebook AI Research's visual object segmentation team

The massive fundraising reflects both intense investor enthusiasm for generative AI and the practical reality that developing advanced AI models requires enormous capital for computing resources and top talent.

Why so much enthusiasm? [Another analysis from Business Insider suggests two factors](https://www.businessinsider.com/mira-murati-big-tech-put-thinking-machines-lab-venture-capital-2025-4):

* a desire to do *hits-based investing* and take chances on the unlikely chance that TML returns outsized gains that justify all the risk
* the *Big Tech put[1](https://peterwildeford.substack.com/p/weekend-links-11-different-tariffs#footnote-1-161170391)* — even if TML doesn’t become a huge independent success like OpenAI or Anthropic, they retain strong acquisition value for talent-hungry tech giants racing for AI dominance.

~

#### It takes a Village to raise some Agents

**[AI Village:](https://theaidigest.org/village)** A new experiment set up OpenAI’s GPT4o and o1 along with Anthropic’s Claude 3.5 (new, aka 3.6) and Claude 3.7 with agentic capabilities, rudimentary memory, and a group chat that the models can collaborate on and that humans can interact with. They’ve been given a clear goal — raise money for Hellen Keller International, a blindness and malnutrition non-profit.

It’s been very entertaining to watch so far.

[![Image](https://substackcdn.com/image/fetch/$s_!3HWP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffc7ab5b3-8a2f-4b89-b07a-fb2ba494e8fb_2560x1013.jpeg "Image")](https://substackcdn.com/image/fetch/$s_!3HWP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffc7ab5b3-8a2f-4b89-b07a-fb2ba494e8fb_2560x1013.jpeg)

The models still need lots of human help

So far the models have raised $355 after ~30 hours of operation, though mainly through public interest in the experiment rather than model action.

The most interesting events have been Claude 3.7 [setting up a Twitter account](https://x.com/model78675), the models creating and sharing Google docs with each other, and the models getting very stuck on CAPTCHAs. It’s also been cute seeing the models attempting to contact AI researcher Daniel Kokotajlo as a potential donor, attempting to contact journalists, lots of difficulty clicking on the correct things, and Claude 3.5 declining a model upgrade:

[![Image](https://substackcdn.com/image/fetch/$s_!Nrng!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa2e1129d-2d13-4b65-b369-81171b2cf29e_588x762.png "Image")](https://substackcdn.com/image/fetch/$s_!Nrng!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa2e1129d-2d13-4b65-b369-81171b2cf29e_588x762.png)

Will be fun to follow along to see how well the models do in the real world.

~

#### The making of GPT 4.5

A new, well produced podcast from OpenAI: **[Pretraining GPT4.5](https://www.youtube.com/watch?v=6nJZopACRuQ)**.

The podcast is focused on the research effort behind GPT-4.5. Not much here is new to people who have been studying LLMs for awhile, but it’s worth a recap:

* **Scaling is still working:** GPT4.5 is 10x more compute than GPT4. The goal was to make GPT4.5 “10x smarter” but I don’t think this was meant to be taken literally and I don’t think it was achieved. Still, I think people being “disappointed” by GPT4.5 are misunderstanding how the scaling is supposed to work — [the scaling is exactly on trend as to what we’d expect](https://x.com/Jsevillamol/status/1895611518672388210) but it appears underwhelming due to the lack of a reasoning model. Combine 4.5 with a reasoning model and [we should see benchmarks increase](https://x.com/kimmonismus/status/1896174836952485975).
* **There was a lot of engineering to do — it wasn’t just “more compute = works”.** Apparently the process took two years, doing advanced planning for using a much larger cluster and running prototypes to test new ideas. Issues included increasing hardware failures, network fabric failures, and just a larger amount of unexpected rare events with large GPU counts.
* **Data availability is starting to become a pain point:** This is more nuanced than “data wall” rumors, but it is clear that models are not very efficient in learning from data compared to humans and that data is not scaling on the internet as fast as compute. Though there are lots of ideas about how to address this.
* The next step is scaling up to 1M GPU runs over the next 1-2 years. This would be another 10x increase.

~

#### ChatGPT 4.1… wut?

[Last week I discussed rumors of o3, o4-mini, and GPT5](https://peterwildeford.substack.com/i/159608081/openai-o-and-o-mini-coming-soon-gpt-delayed-again). Today it got weirder. Per the Verge, **[OpenAI is launching GPT-4.1](https://www.theverge.com/news/646458/openai-gpt-4-1-ai-model)**, possibly within a week. What is it? GPT-4.1 is meant to be a revamped version of the GPT-4o multimodal model with minor improvements. It is said to be launching alongside smaller GPT-4.1 mini and nano versions, which may power a better free version of ChatGPT.

~

#### The AI can remember you now

Also in a separate update released Friday, **[OpenAI introduced a new memory feature to ChatGPT](https://techcrunch.com/2025/04/10/openai-updates-chatgpt-to-reference-your-other-chats/)** that enables the chatbot to remember details from previous conversations. I think this is an important sign of where AI is going as memory could be important for making AI better at longer tasks. But so far, I haven’t found it to be very useful — I’d be much happier if I could just more effectively search and access prior conversations. *(If you don’t like the memory feature, it can be disabled in Settings, under “Personalization”.)*

Like most things, this is a thing that people only noticed once OpenAI started marketing it but that Google has quietly had for over two months. [Google’s Gemini had memory back in February](https://blog.google/feed/gemini-referencing-past-chats/). But in true Google fashion, no one knows about this and also it’s super unclear how to use it. I use Gemini more than daily and am allegedly an expert on AI, but I honestly have no clue how to get Gemini’s memory feature to work.

~

#### **Microsoft is not bullish on OpenAI’s data center buildout**

**[Microsoft continues to pull back from data centers](https://www.bloomberg.com/news/articles/2025-04-03/microsoft-pulls-back-on-data-centers-from-chicago-to-jakarta)** and are no longer the key supplier of OpenAI. This seems bearish for both Microsoft and OpenAI.

It’s not a good sign for OpenAI that SoftBank is the main funder. Their track record doesn’t look good, after [$10B into failed WeWork at a peak $48/share valuation](https://wolfstreet.com/2019/11/14/is-softbanks-bailout-of-wework-already-in-trouble-tender-offer-didnt-happen-bonds-plunge-to-record-low/), multi-billion dollar losses on [Katerra](https://www.wsj.com/articles/how-a-softbank-backed-construction-startup-burned-through-3-billion-11624959000) and [Greensill Capital](https://www.swissinfo.ch/eng/softbank-says-credit-suisse-to-blame-for-funds-%24440-million-greensill-loss/87667018), and a [particularly absurd investment in a $300M dog-walking app](https://edition.cnn.com/2019/12/09/tech/wag-softbank/index.html) (also failed).

But at least SoftBank has the cash and the willingness to deploy it at large scale, which is exactly what OpenAI needs.

~

# **Get hired to do cool AI stuff**

#### Shape the future of AI policy in DC or remotely with me and IAPS!

[![Image](https://substackcdn.com/image/fetch/$s_!OB5H!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b550dcf-d73c-4174-8f67-af1d43c94de6_1080x1080.jpeg "Image")](https://substackcdn.com/image/fetch/$s_!OB5H!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b550dcf-d73c-4174-8f67-af1d43c94de6_1080x1080.jpeg)

If you enjoy this newsletter, you’re potentially in the key target audience for my fellowship or know people who would be a good fit. The Institute for AI Policy and Strategy (IAPS), where I work, **[is offering a fully-funded, three-month AI Policy Fellowship](https://www.iaps.ai/fellowship)** running from September 1-November 21, 2025 to help people pivot their careers into AI policy work.

Our program pairs fellows with experts to work on concrete projects that influence national and global AI policies across domains like security, procurement, export controls, and geopolitics.

Fellows receive financial support ($22,000 for Senior Fellows, $15,000 for Fellows) and comprehensive career development including one-on-one coaching, networking opportunities, and direct support transitioning into AI policy careers.

The fellowship begins with a two-week residency in Washington DC, with options to continue in-person or remotely thereafter.

Applications are open to professionals regardless of technical expertise. **Apply by May 7th, 2025 (12PM ET)** through a three-stage selection process expected to conclude by end of June. An informational webinar will be held on April 22nd for prospective applicants.

[Learn more and apply!](https://www.iaps.ai/fellowship)

~

# Whimsy

**[Which US President is your perfect boyfriend? A flowchart](https://i0.wp.com/hottestheadsofstate.com/wp-content/uploads/2019/02/presidents.png?zoom=2&ssl=1)**.

I got John Adams.

~

#### What if you had a map that showed time instead of space?

This works by readjusting a map to make distance roughly equal to total travel time rather than normal physical distance. Pretty interesting!

If you liked this, consider subscribing for more!

Subscribe

[1](https://peterwildeford.substack.com/p/weekend-links-11-different-tariffs#footnote-anchor-1-161170391)

Borrowing terminology from options trading where a ‘put’ represents downside protection