# Weekend Links #2: Donut Earth, PEPFAR, career opportunities

*Also high density fun, the NVDA bear case, and the true power of birthdays*

Published: 2025-02-08
Source: https://peterwildeford.substack.com/p/weekend-links-2-donut-earth-pepfar

---

[![](https://substackcdn.com/image/fetch/$s_!Ecg6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe9bc9bd6-767a-4dd3-97de-8b6ac9a372b0_2048x2048.jpeg)](https://substackcdn.com/image/fetch/$s_!Ecg6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe9bc9bd6-767a-4dd3-97de-8b6ac9a372b0_2048x2048.jpeg)

***Author’s note: I’m still working on writing more actual content - the point is not for the site to just be link posts.** But I still think link posts are cool, so here are some things for you to read while you wait for more of my other work.*

What is this about? Well I read a lot, and each weekend I want to share the standouts with you …along with some occasional fascinating rabbit holes. Some weekends will be light, others heavy (that's how power laws work), but each link will be worth your weekend morning coffee time.

# AI

#### …Call the Operator

**[Good thread on the current state of OpenAI Operator](https://x.com/sayashk/status/1886465864565751851): "not reliable enough to be automatable, not quick enough to save time", but still a lot of potential for the future.** In this test of an expense reporting process (a 5-10min task), Operator demonstrated competence in initial steps like navigating to correct URLs and uploading receipts under appropriate headings, but failed to reliably complete even after an hour of attempts, struggling with crucial details like matching receipts to amounts and almost deleting the existing records. While human oversight makes Operator more practical than alternatives (e.g., Humane Pin or Rabbit R1), fundamental challenges remain (e.g., prompt injection vulnerabilities, edge case handling, and preference elicitation). However, being able to save tasks to be repeated later seems promising, and if this technology is anything like other AI tech we’ve seen, it will speed up in value quite rapidly.

This matches my personal experience with Operator as well, where I wanted to search for a hotel but it failed at the very first step, entering my check-in date wrong into the booking page.

#### …Who will be on the frontier?

In [“Ten Takes on DeepSeek”](https://peterwildeford.substack.com/p/ten-takes-on-deepseek) my tenth take was that if you looked at companies that (a) have a team with sufficient technical skill, (b) already are underway buying hundreds of thousands of GPUs, and (c) are planning to spend tens of billions of dollars per year on AI, that list is currently just five:

* OpenAI with Microsoft and/or Oracle (Stargate)
* Anthropic with Amazon and Google
* Google
* xAI
* Meta

We already know that [Stargate is planning $100B/yr](https://openai.com/index/announcing-the-stargate-project/) and we heard that [Microsoft is planning $80B/yr](https://blogs.microsoft.com/on-the-issues/2025/01/03/the-golden-opportunity-for-american-ai/). But now we know that [Amazon is also planning $100B/yr](https://www.cnbc.com/2025/02/06/amazon-expects-to-spend-100-billion-on-capital-expenditures-in-2025.html), [Google is planning $75B/yr](https://www.reuters.com/technology/google-parent-alphabet-misses-quarterly-revenue-estimates-2025-02-04/), and [Meta is planning $65B/yr](https://www.facebook.com/zuck/posts/pfbid0219ude255AKkmk4JAueXZeZ9zpjNYio2tBkd7bNmCaRbJ6iJaVVjypUgDg78CNdq5l).

At the same time, [China is getting in $28B/yr](https://www.bankofchina.com/aboutboc/bi1/202501/t20250123_25254674.html) and - more notably - the same Emrati backers of Stargate are spreading their bets and [putting $30B-$50B into AI in France](https://techcrunch.com/2025/02/07/uae-to-invest-billions-to-build-ai-data-center-in-france/) and building a 1GW data center (on par with the US), though it’s unclear how long this will take or what it will produce.

*[Edited Feb 13: with even more investment, [it’s now possible that France should actually go on the above list of five](https://peterwildeford.substack.com/p/ten-takes-on-the-paris-ai-action).]*

**Four important takeaways here:**

* **It’s about to get very expensive to train cutting-edge models.** $28B and $50B both don’t feel like enough.
* **If developing cutting-edge AI is very compute intensive, how the money is used will matter.** Is it spread out among many different AI initiatives? How is compute spread between training and inference?
* **It doesn’t currently seem like China is racing for AI.** While this could change at any moment, their investment is much smaller than the US and there’s no current indication that China is building large data centers. They will also be blocked from turning their capital into hundreds of thousands of GPUs by export controls.
* **It’s worth keeping an eye on UAE’s AI ambitions.** They very clearly want to be relevant in AI. A CSIS report [“The United Arab Emirates’ AI Ambitions”](https://www.csis.org/analysis/united-arab-emirates-ai-ambitions) states that the UAE is planning to invest billions of dollars and wants 20% of their non-oil GDP to come from AI by 2031. The UAE's ability to rapidly build infrastructure, access to abundant energy, and potential for more lax regulation make it an attractive partner for companies struggling with domestic constraints. However, the authors of the CSIS report argue that while supporting specific Microsoft-led projects may be beneficial, the US should maintain healthy skepticism about the UAE's broader AI ambitions and its claims of technological independence from China.

#### …Why not buy NVIDIA?

For about a year, I’ve been bullish on AI progress but still skeptical that NVIDIA will be a good way to profit from that progress. I was going to write a post on my reasoning, but then [“p.b.” just scooped me by independently writing my entire take](https://www.lesswrong.com/posts/Ae7NcffQcMn2sB7GB/p-b-s-shortform?commentId=GoLQJPCCB5hvpb2eq):

> My bear case for Nvidia goes like this:
>
> I see three non-exclusive scenarios where Nvidia stops playing the important role in AI training and inference that it used to play in the past 10 years:
>
> * China invades or blockades Taiwan. [Metaculus gives around 25% for an invasion in the next 5 years](https://www.metaculus.com/questions/11480/chinese-invasion-of-taiwan).
> * All major players switch to their own chips. Like Google has already done, Amazon is in the process of doing, Microsoft and Meta have started doing and even OpenAI seems to be planning.
> * Nvidias moats fail. CUDA is replicated for cheaper hardware, ASICs or stuff like Cerebras start dominating inference, etc.
>
> All these become much more likely than the current baseline (whatever that is) in the case of AI scaling quickly and generating significant value.

I should add though that I’m not a stock analyst. While I have opinions about stocks, I’ve never bought or sold an individual stock, so on this one your guess is as good as mine. Not investment advice.

# Geopolitics

#### …PEPFAR. Will they or won’t they? (They should)

**Trump's sudden freeze of foreign aid threatens to unravel two decades of progress against HIV/AIDS in Africa while undermining crucial US strategic interests.** In [“Trump Has Put George W. Bush's Lifesaving Legacy in Danger”](https://foreignpolicy.com/2025/02/05/pepfar-trump-lifesaving-hiv-aids-soft-power-danger/), the authors share enormous stakes: PEPFAR provides antiretroviral drugs to 21 million people and has saved 25 million lives while costing less than 0.1% of the federal budget.

Beyond the immediate health crisis, the freeze damages America's strategic position in Africa. Where PEPFAR demonstrated genuine partnership and concern for human wellbeing, contrasting with China's more transactional approach, the chaotic implementation of the aid freeze portrays America as an unreliable partner. This self-inflicted wound comes at a crucial moment when US leadership faces growing challenges worldwide.

The sudden halt means many clinics must turn away patients, risking not only immediate health impacts but also the development of drug-resistant HIV strains. While a waiver was issued on February 1st allowing some services to continue, confusion remains about implementation and the program's future, especially given its March 2025 reauthorization deadline.

This from the article is especially sad:

> Perhaps those in the most immediate danger are the children of HIV-positive mothers. PEPFAR currently supports around 680,000 pregnant women with ARV treatment—without access to these drugs, some 20-40 percent of them will transmit HIV to their babies. Without ARV treatment, about half of those infants will die within their first two years of life, most within the first few months. We could very well return to the world of the mid-2000s, where AIDS is once again a death sentence for a large percentage of those infected with HIV.

#### …Visiting China and then writing about it

**Recent visits to China by two Western observers offer complementary perspectives on the nation's evolving social and economic landscape.** In [“Notes on China”](https://www.dwarkeshpatel.com/p/notes-on-china), Dwarkesh Patel shares observations from his two-week journey across multiple Chinese cities. Interesting notes are just how sizable the cities are, how pervasive surveillance cameras are, how low crime appears to be, how there actually does appear to be moderate amounts of contentious political discussion, how youth unemployment coexists with demographic collapse, and how the tech sector feels constrained by the 2021 government crackdown. Through conversations with locals, Patel reveals a nation where young people feel intense pressure despite opportunities, nationalist sentiment varies widely, and internet restrictions and capital controls create significant barriers to international integration and innovation.

Benjamin Todd goes on the same China trip with Dwarkesh and writes his own reflections upon to returning to China – [“Changes in China the last 8 years”](https://benjamintodd.substack.com/p/changes-in-china-the-last-8-years). He notes increased social civility (better queuing and less spitting), technological integration through Chinese apps, and heightened economic concerns (real estate concerns and fewer street vendors). Todd notes that infrastructure remains impressive but shows signs of slowing down, with empty high-rises in smaller cities and questions about build quality. Notably, Chinese-made cars now dominate the streets, and the cost of living remains remarkably low, with Shanghai salaries at half of UK levels but purchasing power roughly double UK levels.

Though how much can we learn about China from these trips and observations? That’s exactly the question Noah Smith tackles in [“How much can you really learn about a country from visiting it?”](https://www.noahpinion.blog/p/how-much-can-you-really-learn-about), where he finds that short-term tourism provides far less insight into a country's true nature than most people assume. Brief exposure (which prevents deep relationship formation), selection bias in who tourists meet (often English-speaking, internationally-oriented locals), and the tendency to filter observations through pre-existing stereotypes combined to limit the ability for tourists to gain genuine insights during short visits.

However, international travel remains valuable for different reasons: it helps people understand their own country better through comparison, increases social trust and tolerance through exposure to difference, and generates important questions about why societies function differently. The key is understanding these benefits while remaining humble about tourism's limitations for deeper cultural and political understanding.

# Get hired to do cool AI stuff

How cool would it be if one of my readers got an awesome job because of my newsletter? Here’s your chance!

#### …Open Philanthropy wants to fund better AI evaluation research

**There’s a problem: AI capability evaluations are fundamentally unprepared to make safe and secure AI.** Existing benchmarks for assessing risk-relevant capabilities are inadequate, our scientific understanding of how capabilities scale and relate to each other is not well understood, and there remains increasing difficulty for third-party evaluators to access and assess AI systems.

**Open Philanthropy wants to fix this and has launched a [Request for Proposals focused on improving how we evaluate AI capabilities](https://www.openphilanthropy.org/request-for-proposals-improving-capability-evaluations/).** They're offering grants of $0.2M-$5M for projects in three key areas: (1) developing better benchmarks for testing AI systems' potentially dangerous capabilities, (2) advancing our scientific understanding of AI capabilities and how to measure them, and (3) improving infrastructure for third-party evaluation of AI systems. **Apply by April 1.**

#### …And OpenPhil is also funding technical AI safety

Technical AI safety research focuses on developing methods to ensure advanced AI systems behave reliably and remain under human control, even as they become more capable. This includes challenges like preventing AI systems from developing unintended goals, making AI systems' decision-making more transparent and interpretable, and creating robust ways to test and validate AI safety properties.

If you’re interested in that, **[Open Philanthropy is also offering substantial grants to fund technical AI safety research](https://www.openphilanthropy.org/request-for-proposals-technical-ai-safety-research/)**, with $40M+ available for projects across 21 research areas including adversarial ML, model transparency, and trust-from-first-principles approaches. They're particularly focused on ensuring AI systems remain controllable as they approach or exceed human-level capabilities. **Apply by April 15.** The process starts with a simple 300-word proposal.

[![Image](https://substackcdn.com/image/fetch/$s_!WhH1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4e46ac3d-59e6-46c9-80e7-0234d8fed95b_1972x1106.jpeg "Image")](https://substackcdn.com/image/fetch/$s_!WhH1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4e46ac3d-59e6-46c9-80e7-0234d8fed95b_1972x1106.jpeg)

#### …Emerging Tech Policy Careers

Looking for info on how to get a career in emerging tech policy in DC? **[Emerging Tech Policy Careers](https://emergingtechpolicy.org/)** offers comprehensive guidance on pathways into policy work, from Congress and think tanks to federal agencies and national labs, with a particular focus on emerging technologies like AI and biosecurity. The site's content includes detailed career guides, fellowship databases, and first-hand accounts from policy practitioners. Worth a look!

#### …Law and AI

The Institute of Law and AI (LawAI) researches and advises on the legal challenges posed by AI. If you have a legal background and are interested in getting involved in AI work, **[LawAI is offering paid, remote-first 8–12 week fellowships](https://law-ai.org/summer-research-fellowships/)** designed to offer law students, professionals, and academics hands-on experience at the intersection of AI, law, and policy. **Apply by Feb 16.**

#### …Got Thoughts on AI Governance? There’s a Centre for that.

The Centre for the Governance of AI (GovAI) is hiring for two research roles focused on AI governance and policy: **[Research Fellows](https://www.governance.ai/post/research-fellow) (2-year position, £80K-100K) and [Research Scholars](https://www.governance.ai/post/research-scholar) (1-year visiting position, £75K-90K)**. Fellows are expected to be more experienced researchers who can mentor others, while the Scholar position focuses on career development. Most positions are based in London, with some remote options. **Apply by Feb 16**.

#### …Institute for Progress

The Institute for Progress (IFP), a non-partisan think tank in Washington DC focused on accelerating scientific and technological progress, **[is hiring Fellows and Senior Fellows for their emerging technology team](https://ifp.org/come-work-with-ifp/)**. The roles focus primarily on AI policy, aiming to maintain US leadership, build state capacity, and support ambitious public R&D projects. Also [their third birthday party](https://x.com/fiiiiiist/status/1887169323472683482) featured panoramic views of DC, an NVIDIA H100 server, and a custom purple cocktail so you know they’re cool. IFP has my highest recommendation - they do great work that is relevant to making AI safer and better as well as making the US stronger.

Fellows should have relevant technical/policy experience (Senior Fellows ~8 years), and ideally be willing to work in DC. The position offers competitive compensation and comprehensive benefits. **Apply by Feb 21.**

#### …Get funded to do journalism on AI

I somehow write this Substack for free out of the goodness of my heart. But there are other alternatives if you want to write about AI for public consumption and actually get paid and mentored to do it. **[The Tarbell Fellowship](https://www.tarbellfellowship.org/programme) offers early-career journalists a paid ($50K) one-year program focused on AI coverage**, featuring a 9-month placement at a major newsroom (including Bloomberg, The Guardian, MIT Tech Review), and intensive AI training. The 2025 cohort runs June 2025-May 2026. **Apply by Feb 28.**

#### …A fellowship more tailored to recent college grads

The International Laboratory for Intelligence and Natural Algorithms (ILINA) **[offers a part-time, remote Junior Research Fellowship](https://ilinaprogram.org/junior-research-fellowship/)** focused on AI safety and catastrophic risk, running May-December 2025.Fellows receive a $3500 scholarship, mentorship, and join a research community. Recent graduates (or those graduating by July 2025) from any field can apply. **Apply by Mar 15.**

Want to learn of more AI career opportunities along with fun links? Subscribe!

Subscribe

*You can also follow me on Twitter where I post opportunities: [@peterwildeford](https://twitter.com/peterwildeford/)*

# Lifestyle

#### …High density fun

**The key to defeating procrastination may lie not in avoiding fun, but in deliberately scheduling it.** In ["Defeat Procrastination By Scheduling High-Density Fun Into Your Day"](http://collegeinfogeek.com/high-density-fun/)) from Thomas Frank, the author addresses how students often avoid high-density fun (e.g., hanging out with friends) due to guilt over incomplete work, yet paradoxically procrastinate on that work by spending hours on low-density activities that provide minimal satisfaction (like scrolling Facebook). This counterintuitive approach suggests that planning for "high-density fun" can actually improve productivity by creating natural deadlines and reducing guilt-driven procrastination.The solution proposed is to explicitly schedule enjoyable activities - for example, committing to start a game at 8 PM - which creates a concrete deadline to complete work beforehand.

#### …Solve emotional labor with scorecards

**A former product manager has [proposed a new solution](https://www.cartoonshateher.com/p/emotional-labor-and-the-fetishization) to the contentious debate over "emotional labor" in relationships**. The author referred to as “Cartoons Hate Her” demonstrates how the term “emotional labor” has lost its utility, becoming a source of resentment rather than clarity in domestic partnerships. But the concept still has value, solving the question around what tasks need doing and deserve more appreciation in the relationship?

CHH draws from her experience in tech project management to introduce the "IDEA" scoring system - rating tasks from 1-5 on each of four dimensions:

* **Importance** - how necessary the task is for basic functioning
* **Demand** - how much others want or need it done
* **Ease** - how simple it is to accomplish
* **Amusement** - how much enjoyment the doer gets from it

For example, elaborate holiday baking might score low on Importance (1/5, as no one will suffer without it) but high on Demand (4/5 from eager family members), moderate on Ease (3/5), and vary on Amusement (2-5/5) depending on the person doing it. And then tasks scoring above 10/20 are worth prioritizing, while lower-scoring activities might be candidates for elimination.

#### …Why not to write a book

**The pressure to write a book may often harm writers' productivity and well-being**, [Gwern argues](https://gwern.net/book-writing). While publishing a book is traditionally viewed as an important intellectual milestone, the process can lead to reduced output, high opportunity cost, and potential burnout.

Firstly, the time of writing a book itself has a lot of opportunity cost – hours spent editing and refining a book are hours not spent exploring new ideas, responding to current developments, or producing other work.

But more worryingly, producing a book could come at a large cost to future productivity via burnout – Wait But Why's Tim Urban’s blog output dropped from 11-15 posts yearly to nearly zero during his 2,440-day book project, and he’s not the only one to stop writing both during and after the book project.

This burden falls especially hard on writers who work in bursts of inspiration rather than daily routines - for them, a book project can consume all their creative energy for years, preventing them from producing dozens of shorter works that might have had greater total impact.

#### …PayPal’s Honey is no honey

**PayPal's Honey browser extension systematically deceives both consumers and content creators through an elaborate commission-hijacking scheme and withholding the best coupons from customers.** According to a detailed [MegaLag video investigation](https://www.youtube.com/watch?v=vc4yL3YTwWk), while Honey marketed itself as a free tool that automatically finds the best online discount codes, the investigation uncovers that (1) the extension actually overrides content creators' affiliate links at checkout, redirecting commissions to PayPal regardless of whether any discounts are found and (2) allows companies to control the displayed coupon codes, thus not always giving the user the best deals like advertised. Thus Honey's entire business model relies on deceiving customers into believing they're getting the best deals while simultaneously stealing commissions from content creators who genuinely referred the sales. Be skeptical of "free" browser extensions and services - if something is free, you (or someone else) might be the product.

[![](https://substackcdn.com/image/fetch/$s_!xdU1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1c28e70-e786-4853-b6f6-3a1e754e7db2_956x498.png)](https://substackcdn.com/image/fetch/$s_!xdU1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1c28e70-e786-4853-b6f6-3a1e754e7db2_956x498.png)

# Whimsy

#### …You’re saying there’s a chance?

**[What are the chances you'd get a fully functional language model by randomly guessing the weights?](https://arxiv.org/abs/2501.18812)** About 1 in 1000000…000 where there are about 360,000,000 total zeroes in that number. …I’d say that’s roughly equivalent to randomly selecting a correct lottery ticket number every second for the entire age of the universe, except I’d be wildly off, as that’s actually only 1 in 10,000,000,000,000,000,000,000,000 (25 zeroes) and we still have 359,999,975 more *orders of magnitude* to go.

#### …Donut Earth

**Have you ever asked the question [“What would the Earth be like if it was the shape of a donut?”](http://io9.gizmodo.com/what-would-the-earth-be-like-if-it-was-the-shape-of-a-d-1515700296)** Anders Sandberg has. And it turns out that a donut-shaped planet could theoretically exist according to physics… though it would never form naturally and would face significant stability challenges.

This “toroidal planet” would have some fascinating hypothetical properties -dramatically different environments from Earth, with varying gravity, ultra-short 2.8-3.5 hour days, and complex seasonal patterns due to self-shadowing. The interior "hole" would experience unique lighting conditions, with potential for spectacular atmospheric effects and reflected light from the opposite side reaching moonlight-to-daylight brightness levels. Additionally, the rapid rotation would create strong Coriolis effects leading to banded climate patterns more like Jupiter than Earth, while the unusual gravity distribution would affect everything from mountain heights to ocean waves. While naturally impossible, such worlds could theoretically sustain Earth-like biospheres despite their exotic properties if engineered, though their unusual gravitational fields would create complex challenges for maintaining stable moon orbits.

#### …The true power of birthdays

**[Birthdays are incredibly powerful social technology and almost nobody uses them well.](https://x.com/IvanVendrov/status/1886253288066064781)** In this Twitter thread, Ivan Vendrov argues you should leverage your birthday as an opportunity to organize activities you genuinely want but might normally feel too unconventional to suggest. Don't dilute your birthday plans with compromises - authentic preferences often create better experiences for everyone!

The author demonstrates this through personal examples: organizing a friend/family advisory board, starting a now-regular capture-the-flag game, and hosting a day-long Michael Levin reading session. These unconventional choices sparked enthusiasm and inspired similar events from others, proving how "birthday license" can successfully expand social possibilities.

In an era where authentic desire is rare, birthdays offer a valuable opportunity to express genuine preferences and forge deeper connections through unconventional shared experiences - and counterintuitively, these choices often create better experiences for everyone involved.

I hope you liked these weekend links. Subscribe for more!

Subscribe

If you liked this, you may also like following me on Twitter: [@peterwildeford](https://twitter.com/peterwildeford/)