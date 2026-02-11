# Tuesday Links #14: OpenAI non-profit control, Meta/Google antitrust

*Also staring into the abyss, robots with guns, and Peter goes to Washington*

Published: 2025-05-06
Source: https://peterwildeford.substack.com/p/tuesday-links-14-openai-non-profit

---

**Author’s note:** There’s *normally* a segment on this Substack called “Weekend Links”, but this week it’s again falling on a Tuesday. I’m hoping to return to regular order next week, but if you do like this on Tuesday instead of over the weekend, now’s a good time to let me know.

This week’s excuse is that I spent the weekend moving to DC! I’m excited to live in the nation’s capital and do my best to help federal policymakers better understand and anticipate the impacts of advanced AI. But I’ll always be an Ohio guy at heart.

[![vehicles on road during daytime](https://images.unsplash.com/photo-1552337125-0c43e12efec0?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wzMDAzMzh8MHwxfHNlYXJjaHwyfHx3YXNoaW5ndG9uJTIwZGN8ZW58MHx8fHwxNzQ2Mzg0NTI5fDA&ixlib=rb-4.0.3&q=80&w=1080 "vehicles on road during daytime")](https://images.unsplash.com/photo-1552337125-0c43e12efec0?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wzMDAzMzh8MHwxfHNlYXJjaHwyfHx3YXNoaW5ndG9uJTIwZGN8ZW58MHx8fHwxNzQ2Mzg0NTI5fDA&ixlib=rb-4.0.3&q=80&w=1080)

Photo by [Maria Oswalt](true) on [Unsplash](https://unsplash.com)

# **AI**

#### OpenAI non-profit control survives

OpenAI was founded as a non-profit, with the mission to ensure that artificial general intelligence benefits all of humanity. The problem is that AGI doesn’t exist yet, so it cannot yet benefit all of humanity. So their first step was to build AGI.

The second problem is that it turns out that building AGI is quite expensive, requiring first [hundreds of billions of dollars](https://openai.com/index/announcing-the-stargate-project/), and in the future [potentially trillions](https://www.datacenterdynamics.com/en/news/sam-altman-muses-that-after-500bn-stargate-openai-may-raise-5-trillion-for-a-cluster/). To raise capital, OpenAI created OpenAI Global LLC, a “capped-profit” entity that would be a for-profit but with two twists:

1. the OpenAI non-profit would own and maintain full governance control over the for-profit subsidiary
2. returns for investors in the for-profit are capped at different levels, which limit the amount of profit they can make. Remaining profit above the caps flow to the non-profit exclusively.

[![Our structure | OpenAI](https://substackcdn.com/image/fetch/$s_!O5sH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5624f9a6-4cd4-43fc-982e-58cdabf0cf36_4340x3256.jpeg "Our structure | OpenAI")](https://substackcdn.com/image/fetch/$s_!O5sH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5624f9a6-4cd4-43fc-982e-58cdabf0cf36_4340x3256.jpeg)

The 2023 boardcrisis dramatically reshaped OpenAI's governance when the board [abruptly fired CEO Sam Altman](https://en.wikipedia.org/wiki/Removal_of_Sam_Altman_from_OpenAI) on November 17, 2023, citing concerns about transparency in his communications. After nearly all employees threatened to resign, Altman was reinstated five days later with a restructured board. Around the same time, OpenAI came up with a proposal to restructure away from non-profit control.

[I covered this back in February](https://peterwildeford.substack.com/p/what-happened-in-ai-this-week-france):

> OpenAI now wants to convert fully from a non-profit to a “public benefit corporation” which is how Anthropic is structured, where the company is a for-profit but is allowed to maximize social value in addition to shareholder value and doesn’t have to *exclusively* maximize profit. This new structure will be able to bring in more investment. Indeed, OpenAI’s most recent $6.6B in financing is contingent on transitioning to the for-profit structure and the financing will need to be paid back as a loan if the transition isn’t met.

But there was a problem…

> [O]ne can’t just “convert” a non-profit into a for-profit. That’s not how the legal world works, and is unfair to all of your donors. There are a lot of complex steps involved but essentially the for-profit has to “buy out” the non-profit by paying the non-profit fair market value for all of its intellectual property, access to potential profits, control rights, the “merge and assist clause”, other rights, as well as the fundamental idea that OpenAI is currently in the lead towards creating transformative AI systems and may not uphold the non-profit mission by default if sold. Each of these aspects alone are potentially worth billions.

And now we have a resolution: **OpenAI [announced Monday](https://techcrunch.com/2025/05/05/openai-reverses-course-says-its-nonprofit-will-remain-in-control-of-its-business-operations/) that its nonprofit parent will continue to maintain control over its for-profit operations**, reversing these earlier plans to become a more traditional for-profit entity. Instead, OpenAI will convert its for-profit arm from an LLC to a Public Benefit Corporation (PBC). OpenAI will also drop its “capped-profit” structure.

The decision follows months of pressure from various stakeholders, including legal challenges from attorneys general, Elon Musk, and additional [independent civil society organizations and individuals](https://notforprivategain.org/). Reading between the lines, it sounds to me like the AGs told OpenAI they weren't going to permit the conversion and this is the compromise that OpenAI came up with.

However, there still are some details to figure out and a lot of unanswered questions:

* **What will non-profit control actually look like in this structure?** Under the new plan, the OpenAI nonprofit will no longer manage OpenAI’s daily operations. Instead it will hold super-voting stock and retain the right to appoint a majority of directors to the board of the for-profit, giving it board-level veto power while leaving day-to-day decisions to the Public Benefit Corporation’s executives. This is control, and stronger control than an ordinary shareholder stake, but a thinner layer of control than today’s full ownership.
* **Will the non-profit still own AGI if OpenAI develops it?** The deal between OpenAI and Microsoft contained a provision that if the OpenAI non-profit board “determines when we've attained AGI [...] Such a system is excluded from IP licenses and other commercial terms with Microsoft, which only apply to pre-AGI technology.” In other words, the nonprofit board has the authority to declare that AGI has been attained and the nonprofit would retain control over this technology. Would this still be the case under the new structure? What would this look like in practice?

* **Will the “merge and assist” clause remain a part of the new structure?** This is a key provision in the OpenAI charter that addresses concerns about competitive race dynamics in advanced AI development, which states that if “AGI development becoming a competitive race without time for adequate safety precautions [and] a value-aligned, safety-conscious project comes close to building AGI before we do, we commit to stop competing with and start assisting this project.” This is very conspicuously absent from the current conversation, as it is very unclear how this would affect the public-benefit corporation.
* **What will non-profit control look like in practice**, given that the non-profit board already seems highly sympathetic to Sam Altman and the for-profit mission of OpenAI even if technically they are not supposed to be biased in this way? Also given that it’s possible the non-profit’s stock could be diluted at some future date?
* **How will non-profit control affect OpenAI’s current investments?** Let Previous deals with OpenAI that gave OpenAI [$13 billion from Microsoft](https://www.geekwire.com/2024/microsofts-financial-disclosures-show-how-openai-is-fueling-growth-and-taking-a-toll-on-profits/) and [$40 billion from SoftBank's recent round](https://www.reuters.com/technology/artificial-intelligence/openai-raise-40-billion-softbank-led-new-funding-2025-03-31/) were contingent on OpenAI converting from a non-profit to a for-profit. The SoftBank-led funding had an explicit contingency that OpenAI must “transition to a for-profit company by the end of the year to secure the full $40 billion” or risk the investment being cut to $20 billion. It currently seems like these investors are satisfied with this new structure where their profit caps are removed but the non-profit retains control, as the removal of caps allows increased potential for financial returns and opens the possibility of OpenAI going public some day. Also notably this arrangement isn’t that uncommon — [there are several major public companies that are owned by non-profits](https://x.com/peterwildeford/status/1919833040731439333), such as Hershey, Rolex, and IKEA, and they seem to do just fine with capital markets. But this is different from the original deal and may still affect some investors.
* **Will the non-profit be compensated for the removal of caps and reduction in control?** The non-profit cannot just give up things to the for-profit for free. There has already been [a lot of debate about how much the non-profit ought to be compensated for these changes](https://peterwildeford.substack.com/p/what-happened-in-ai-this-week-france) and it’s possible that [no amount of compensation could be enough](https://notforprivategain.org/). This is an important question that is still far from settled and that state Attorneys General will get to weigh in on.
* **How much stake will Microsoft get?**
* **What kind of control will Sam Altman get?** OpenAI has yet to decide whether Altman will continue to sit on the board of the non-profit as he does now or whether he will move to a board seat for the new company where the non-profit could potentially overrule him.
* **What happens to the lawsuit?** Elon Musk had been suing OpenAI to block the restructuring to a for-profit and still doesn’t seem satisfied by this change. Musk’s lawyer said the announcement about non-profit control was still a “dodge” and doesn’t address "that “charitable assets have been and still will be transferred for the benefit of private persons, including Altman, his investors and Microsoft.”

*(Thanks to reporting from [Garrison Lovely](https://www.obsolete.pub/p/four-predictions-about-openais-plans), [Rob Wiblin](https://x.com/robertwiblin/status/1919526945299300522), and [The Information](https://www.theinformation.com/articles/openais-governance-reversal-means) for providing material for me to draw from in the above.)*

~

#### What do Meta and Google antitrust cases mean for AI?

While AI has been improving rapidly, there’s been a slower moving story unfolding in the courts — are Google and Meta illegal monopolies? If so, what should be done? The implications here could affect a lot at both Google and Meta, including their ability to invest in AI.

[Meta is already having difficulty funding their Llama AI](https://www.theinformation.com/articles/meta-asked-amazon-microsoft-help-fund-llama) and that’s before the potential for the courts to force them to sell Instagram and/or Whatsapp, denying them a bunch of revenue that would otherwise fund future Llama iterations.

Meta's antitrust trial over its acquisitions of Instagram and WhatsApp began on April 14, and is currently in its fourth week of proceedings. The FTC alleges Meta employed a systematic “buy or bury” strategy to eliminate competition in personal social networking services. [CEO Mark Zuckerberg testified for three days](https://www.reuters.com/sustainability/boards-policy-regulation/facebook-owner-meta-faces-existential-threat-trial-over-instagram-whatsapp-2025-04-14/), defending the acquisitions as legitimate business decisions that improved the platforms. [A damaging 2018 memo revealed during trial](https://www.reuters.com/sustainability/boards-policy-regulation/us-antitrust-trial-metas-zuckerberg-admits-he-bought-instagram-because-it-was-2025-04-15/) showed Zuckerberg himself considered spinning off Instagram due to antitrust concerns.

The trial is expected to conclude in early-to-mid June, with the [ruling anticipated between August and October 2025](https://www.npr.org/2025/04/13/nx-s1-5358434/ftc-meta-antitrust-trial). If the FTC prevails, Meta could be forced to divest Instagram and WhatsApp, significantly impacting its business model, as Instagram alone generates more than half of Meta's US advertising revenue.

Google’s case is much further along. In 2024 August, [Judge Amit Mehta ruled Google violated antitrust law](https://www.reuters.com/legal/us-judge-rules-google-broke-antitrust-law-search-case-2024-08-05/) by illegally maintaining monopolies in general search services and search text advertising. A separate ruling found [Google illegally monopolized](https://www.reuters.com/technology/us-judge-finds-google-holds-illegal-online-ad-tech-monopolies-2025-04-17/) two key digital advertising technology markets by unlawfully tying its publisher ad server with its ad exchange.

The Justice Department wants Google to license chunks of its 100-billion-page search index to rivals and to end default-search pay-offs that bankroll Alphabet’s $198 billion annual search cash-cow — the very profits that fund its Gemini model and custom TPU hardware.

If either Meta or Google breakup sticks, Google and/or Meta could lose revenue that would finance their AI and also give up relevant data, while up-starts gain cheaper access to data and distribution — a small potential realignment of the AI competitive landscape.

~

# **Lifestyle**

*Some collected wisdom from around the internet…*

#### **Looking stupid is a key part of becoming smart**

[Don't let the fear of appearing foolish prevent you from asking questions, learning, or taking necessary actions](https://danluu.com/look-stupid/). Dan Luu argues that this willingness is not a weakness, it’s actually a competitive advantage. The potentially embarrassing behaviors and questions leads to deeper understanding and better outcomes, despite the social costs. Social pressure to appear smart actively works against deep learning and innovation.

In addition to learning value, there’s also exploration value. Many potentially valuable ideas and approaches are never tried because they initially sound stupid. By being willing to look foolish, one can explore solution spaces others automatically reject, leading to unexpected breakthroughs.

~

#### Stare into the abyss

Developing the skill to confront uncomfortable truths and make difficult decisions, even when it's painful, is crucial for growth and avoiding stagnation. Ben Kuhn refers to this as **[staring into the abyss](https://www.benkuhn.net/abyss/)** where you ask incredibly tough personal questions such as whether you should change jobs or quit some of your current relationships, with the idea that such dramatic action is under-considered because it is so uncomforable. The broader implications suggest that while "staring into the abyss" can be personally challenging, avoiding it leads to stagnation in careers, relationships, and personal growth.

~

#### Half-assing it with everything you've got

Nate Soares writes a blog post where he argues that the most effective way to approach tasks is neither to slack off nor be a perfectionist, but [to identify the exact quality target needed and hit it with maximum efficiency](https://mindingourway.com/half-assing-it-with-everything-youve-got/). For example, imagine writing a college paper — slackers do minimal work to pass while tryers push for maximum quality possible. But both approaches are suboptimal — instead, one should determine exactly what level of quality is needed (whether that's a passing grade, an A, or mastery of material) and achieve that target with minimal effort. This applies not just to schoolwork but to all endeavors.

~

# **Whimsy**

Blogger Noah Smith has talked about [how the future is finally here](https://www.noahpinion.blog/p/welcome-to-the-future), sharing some amazing videos about current technology. Here are some of my favorites:

*Nice music plus Sphere visuals!*

*Robot dog police!*

*Ukrainians flying drone missions like video games!*

*Flying air taxi!*

If you liked the above and want to receive this in future weeks, subscribe!

Subscribe