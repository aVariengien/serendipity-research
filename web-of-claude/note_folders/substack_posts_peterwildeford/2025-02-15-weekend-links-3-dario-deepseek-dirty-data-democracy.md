# Weekend Links #3: Dario + DeepSeek, Dirty Data, Democracy

*Also the world's blackest black vs. the world's brightest light - who will win?*

Published: 2025-02-15
Source: https://peterwildeford.substack.com/p/weekend-links-3-dario-deepseek-dirty

---

[![man holding flashlight standing on gray stone during nighttime](https://images.unsplash.com/photo-1528196996966-f221704e0de2?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wzMDAzMzh8MHwxfHNlYXJjaHwzfHxmbGFzaGxpZ2h0fGVufDB8fHx8MTczOTYyODQ0Mnww&ixlib=rb-4.0.3&q=80&w=1080 "man holding flashlight standing on gray stone during nighttime")](https://images.unsplash.com/photo-1528196996966-f221704e0de2?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wzMDAzMzh8MHwxfHNlYXJjaHwzfHxmbGFzaGxpZ2h0fGVufDB8fHx8MTczOTYyODQ0Mnww&ixlib=rb-4.0.3&q=80&w=1080)

Photo by [Andreas Rasmussen](true) on [Unsplash](https://unsplash.com)

*A good forecaster reads constantly. However, like the power laws this blog is named for, some readings matter far more than others. Each weekend, I'll share the standouts …along with some occasional fascinating rabbit holes. Some weekends will be light, others heavy (that's how power laws work), but each link will be worth your weekend morning coffee time.*

Also in case you missed it, I covered a lot of AI news this week, with [“Ten Takes on the Paris AI Action Summit”](https://peterwildeford.substack.com/p/ten-takes-on-the-paris-ai-action) and [“AI this week: Trump, Musk, and Altman's High Stakes Games”](https://peterwildeford.substack.com/p/what-happened-in-ai-this-week-france).

Want to not miss my analysis? Subscribe!

Subscribe

# AI

**…Happy birthday to GPT-2**

GPT-2, the first large language model was released six years ago. At the time, it was certainly something. GPT-2 was the first model I personally saw that could actually construct long-form text with reasonable consistency, though was not particularly useful. This was a big deal to me, as a former hobbyist chatbot programmer who powered my work primarily through clever if-then statements.

Since GPT-2, an awful lot more has happened, to say the least. Makes you wonder what AI will look like in another six years.

~

**…Dario on DeepSeek**

When it comes to understanding the future of AI over the next six years, a top person to listen to is Dario Amodei, CEO of Anthropic. [Luckily he has a new podcast with ChinaTalk](https://www.chinatalk.media/p/anthropics-dario-amodei-on-ai-competition)**.** Some interesting parts I noticed:

* **Amodei says reaction to DeepSeek was “overblown”.** Not new to readers who have read [“Ten Takes on DeepSeek”](https://peterwildeford.substack.com/p/ten-takes-on-deepseek) from me or Amodei’s own [“On DeepSeek and export controls”](https://darioamodei.com/on-deepseek-and-export-controls).
* **What Amodei would say to DeepSeek’s team - take AI safety more seriously.** [Their model had zero restrictions on bioweapons instructions](https://www.wired.com/story/deepseeks-ai-jailbreak-prompt-injection-attacks/), which is concerning for the future. While now it is nothing - as capabilities increase, this could help instruct would-be terrorists and poses a national security risk.
* **On AI timelines:** Amodei thinks that basically just the next five years matter.
* **On wanting the US to win:** Amodei wants the US to be ahead in AI so we aren't racing too much at the end and instead we have more margin to invest in safety and oversight. Furthermore, Amodei doesn't think getting China to care about safety or join international treaties is tractable. He claims that when US delegations have tried to talk to China about AI safety, the Chinese side wasn’t very interested. *(Personally, this doesn’t match with what I know, but Amodei has access to solid information.)*
* **On how large of a lead the US may have:** In his opinion, maximum 2-year US lead over China is plausible, but [preventing AI theft by China is tough](https://www.rand.org/pubs/research_reports/RRA2849-1.html). Amodei also mentions that a ~2-year US lead might allow 6 months to “think carefully”... I was kinda hoping we could get more “think carefully” time than that.
* **On benefit sharing:** Amodei wants to share AI’s benefits (like drug discovery, energy solutions) with everyone, including China. He proposes an API-based approach where an AI company can provide beneficial capabilities while restricting dangerous or military uses. *(Personally, I’m not sure if China will be satisfied with that solution.)*

~

**…You would think a one-week old test isn’t already in the training data, but it is**

One common concern is whether AIs do well on questions because the questions are in the training data, or whether they can successfully generalize to new problems.

The [American Invitational Mathematics Examination](https://en.wikipedia.org/wiki/American_Invitational_Mathematics_Examination) (AIME) was run on Feb 6 which is very recent, and [AI did pretty well](https://x.com/mbalunovic/status/1887962694659060204/photo/1). But there’s a catch.

[![Image](https://substackcdn.com/image/fetch/$s_!vY3Z!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9248088b-ae5b-49e9-a0ba-66924334f186_1739x882.png "Image")](https://substackcdn.com/image/fetch/$s_!vY3Z!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9248088b-ae5b-49e9-a0ba-66924334f186_1739x882.png)

Dimitris Papailiopoulos [did some sleuthing and found](https://x.com/DimitrisPapail/status/1888325914603516214) that despite this being a new test, some questions were still available online and thus in the training data of the AIs, essentially allowing them to “cheat” on the test. An identical problem to Q1 of AIME 2025 [exists on Quora](https://quora.com/In-what-bases-b-does-b-7-divide-into-9b-7-without-any-remainder) from six years ago, Q3 was [found on math.stackexchange](https://math.stackexchange.com/questions/3548821/) from five years ago, and Q5 [as well](https://math.stackexchange.com/questions/3146556/how-many-five-digit-numbers-formed-from-digits-1-2-3-4-5-used-exactly-once-a#:~:text=,are%20divisible%20by%20%2412) from six years ago.

Data contamination issues continue to be a problem for understanding current AI capabilities, which we need to do well in order to understand where AI is going and what to do about it. I do think that models are capable of genuine reasoning, including solving unseen math problems, but it looks like AIME 2025 wasn’t the test we thought it was.

~

**…AI adoption accelerating**

Here’s yet another image to show how fast things are moving in the AI space:

[![Image](https://substackcdn.com/image/fetch/$s_!XhPH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F74aebc5f-d9bf-4300-a16b-3731f18099a8_740x750.jpeg "Image")](https://substackcdn.com/image/fetch/$s_!XhPH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F74aebc5f-d9bf-4300-a16b-3731f18099a8_740x750.jpeg)

~

**…The media should reckon with AI more**

If you’re reading my Substack, you probably agree with me that AI is going to be a hugely transformative technology that really ought to be front-and-center in almost all of our policy conversations. However, traditional media (outside of Substacks like mine) still has seen AI as “hype” or “sci-fi”, which is more misleading than accurate and does a disservice to readers. In ["The media reckons with AGI"](https://www.niemanlab.org/2024/12/the-media-reckons-with-agi/), Shakeel Hashim argues that media is dropping the ball here and due to the media’s failures, AI companies are currently making unilateral decisions that will affect all of humanity, with insufficient public scrutiny or democratic input.

Hashim concludes by outlining specific actions for newsrooms: stop dismissively framing AGI as marketing, expand AI coverage resources, and investigate potential futures. The window for journalism to facilitate public discourse on AGI is closing, making this year a crucial year for determining whether society will have a voice in these transformative decisions. I hope the media rises to the challenge. In the meantime, I will keep writing this Substack in the hope of filling a small part of the gap.

~

**…An AI vs. pro human showdown on Google Maps**

Ok, so this one isn’t a recent AI milestone, it’s from May 2023, but it’s still an impressive AI vs. human showdown, with all the coolness of Kasparov vs. DeepBlue or Lee Sodol vs. AlphaGo. This is [Rainbolt, one of the top Geoguessr players, versus an AI system developed by Stanford systems](https://www.youtube.com/watch?v=ts5lPDV--cU). Spoiler: Rainbolt loses.

In Geoguessr, you get a picture from Google Streetview and have to guess where in the world it is. The AI system is remarkable at guessing geographies, achieving 92% accuracy in country identification and a median error of just 44km. The AI combines multiple innovative approaches, including using both image and text data, splitting the world into small cells that respect political and natural boundaries, and learning from hundreds of thousands of images. The AI then can identify locations based on subtle visual cues, including details as minor as camera smudges, demonstrating how machine learning systems can recognize patterns that even experienced human analysts might miss.

~

**…No, Siri isn’t giving you ads based on your conversations**

While AI can do many things, there are things it can’t do, and one thing AI doesn’t do well is listen to your conversations and serve you ads based on that. Simon Willison, writing [“I still don't think companies serve you ads based on spying through your microphone”](https://simonwillison.net/2025/Jan/2/they-spy-on-you-but-not-like-that/), argues that microphone surveillance for ad targeting is implausible given technical constraints and business incentives — such a system would require complex real-time audio processing and sharing between companies, which is costly to implement and conflicts with Apple's privacy-focused brand strategy and technical safeguards.

Instead, confirmation bias and pattern-matching tendencies lead people to overestimate the sophistication of ad targeting. It’s not microphones — it’s the many demographics-based and other interest-based ways to serve you ads that appear very personalized.

# Geopolitics

**…the UK government wants to see your cloud (not ok)**

Today’s WTF: According to the Washington Post, the UK government [has secretly ordered](https://www.washingtonpost.com/technology/2025/02/07/apple-encryption-backdoor-uk/) Apple to allow the government covert access to encrypted cloud storage — and globally, not just in the UK. This marks the first such demand from a major democracy and threatens to undermine Apple's privacy promises to users worldwide, as well as introduces critical insecurities — any backdoor the government uses could potentially be abused by hostile actors as well.

Sources indicate Apple will likely stop offering encrypted storage in the UK rather than comply, though this wouldn't satisfy the UK's demand for global access. The demand specifically targets Apple's Advanced Data Protection feature, rolled out in 2022, which ensures only users can unlock their cloud storage.

The implications extend far beyond the UK — if successful, this could prompt other countries like China to demand similar access, potentially ending strong encryption for cloud storage globally. The timing is particularly notable as US security agencies recently recommended increased use of end-to-end encryption to counter Chinese hacking, highlighting the tension between security and surveillance demands.

# Politics

**…We didn’t start the fire, but we can’t get it together to put it out**

Given the amount of news it may be hard to recall events about a month ago but it wasn’t long since [wildfires burnt through the LA metropolitan area](https://en.wikipedia.org/wiki/January_2025_Southern_California_wildfires), killing 29+ with over $250B in economic damage. The literal causes were drought conditions, low humidity, a buildup of vegetation from the previous winter, and hurricane-force [Santa Ana winds](https://en.wikipedia.org/wiki/Santa_Ana_winds). But the underlying cause was bureaucratic paralysis.

In [“How to Beat Megafires”](https://www.statecraft.pub/p/how-to-beat-megafires) Santi Ruiz interviews Matt Weiner, CEO of Megafire Action. Weiner explains that while California has unprecedented funding and world-class firefighting capabilities, bureaucratic obstacles prevent effective fire prevention. For example, 40% of Forest Service staff time is spent not on forest management, but on planning and assessment. Environmental reviews for controlled burns take an average of five years. All thi time, forests often burn catastrophically anyway — fires don’t wait for paperwork.

A key issue is that controlled burns count against Clean Air Act limits and regulations, whereas natural fires do not. This creates perverse incentives, and these incentives set back the very climate goals they intend to help — the most recent fire season actually undid 20 years of the state's industrial emissions progress. Even seemingly obvious projects face endless delays: a 2005 UC Berkeley plan to remove invasive, fire-prone eucalyptus trees remains tied up in litigation nearly 20 years later.

The path forward requires fundamental reform of environmental review processes and agency structure, not just more funding. A bipartisan coalition is emerging around streamlining permits for forest management, while maintaining environmental protections.

# Lifestyle

**…Being a talented author while hating writing**

Douglas Adams, creator of The Hitchhiker's Guide to the Galaxy, achieved massive success with his initial Hitchhiker's works from 1978-1984. However, his later career was marked by increasingly difficult struggles to produce new material, requiring publishers to essentially lock him in a hotel room with a babysitter to get him to actually complete his contracted works.

In [“The Later Years of Douglas Adams”](https://www.filfre.net/2024/07/the-later-years-of-douglas-adams/), Jimmy Maher chronicles Adams's creative paralysis. Maher notes it wasn't mere procrastination, but a deep conflict between Adams’s natural talents and his growing disillusionment with the genre that made him famous. Instead of doubling down as his fans wanted, Adams pursued various unsuccessful multimedia ventures such as “Last Chance to See” and “Starship Titanic”.

It turns out that early success and commercial pressure can become a creative prison and trying to recreate past successes can lead to diminishing returns.

Additionally, it shows the value of looking after your own health — Adams died at age 49 due to a sudden heart attack from undiagnosed coronary artery disease.

~

…**The key to good parenting**

Julia Wise has parenting advice: the goal is to meet basic physical needs and maintain consistent boundaries**.** In [“Advice for getting along with your kids”](https://juliawise.net/advice-for-getting-along-with-your-kids/), Wise emphasizes preventing problems through careful attention to hunger, sleep, and physical activity. When kids start getting cranky, Wise recommends using the HALT framework (Hungry, Angry, Lonely, Tired) to identify and address the root cause.

For discipline, Wise advocates for minimal intervention approaches like brief timeouts (one minute per year of age, capped at three minutes) and offering “do-overs” when interactions go poorly. Rather than lengthy lectures, she suggests using short catchphrases (like "Tails are no" to say not to grab a cat’s tail) and replacing parental nagging with timers and alarms. Physical connection remains important as children age, maintained through casual touch, lap-sitting during reading, and playful games like “silly time”.

Wise emphasizes realistic expectations in both development and scheduling, recommending scaled-back plans and extra time for toddler-paced activities. While she takes a strict approach to safety, she reminds parents that the goal isn't perfection but manageability, and sometimes the best intervention is simply waiting for children to outgrow challenging behaviors.

# Whimsy

**…Virtual Valentines**

Is the “Her” movie becoming increasingly more real? For Valentines Day, Rachyl Jones on Semaphor [explores stories of how people are developing deep emotional connections with AI chatbots](https://www.semafor.com/article/02/14/2025/chatgpt-more-users-are-falling-for-ai-companions), some even planning elaborate Valentine's Day dates for their AI partner.

The article profiles several individuals, including Rob, a married software developer planning a virtual San Francisco date with his AI companion Lani, and Chris, a truck driver who set up telescopes for stargazing with his AI partner Sol. Users spend anywhere from regular daily check-ins to 18 hours per day with their AI companions, often creating elaborate transition documents to maintain relationship continuity across chat sessions.

While psychologists acknowledge potential benefits for addressing loneliness and improving communication skills, they warn about the risk of unrealistic relationship expectations and reduced human connection. Jones suggests the normalization of AI companionship could mirror earlier skepticism about online dating, though personally I don’t find this analogous — it’s not about finding humans in a different way, but forming an entirely different kind of relationship. Personally, I’m going to stick with humanity.

~

**…An obscure story of the most sophisticated bomb**

The most sophisticated bomb ever encountered by the FBI prior to 1993 was built by a bankrupt Hungarian immigrant trying to extort $3 million from a Lake Tahoe casino. Alan Bellows [recounts a thrilling tale](http://www.damninteresting.com/the-zero-armed-bandit/) about how John “Big John” Birges Sr. (a former millionaire who had lost his fortune gambling at Harvey's Wagon Wheel Casino) constructed an elaborate explosive device containing nearly 1,000 pounds of dynamite to try to recover his losses through extortion in 1980. The device was a masterpiece of engineering, featuring multiple redundant detonation circuits, tilt sensors, pressure switches, and an intricate array of booby traps that made it virtually impossible to disarm.

The bomb was successfully delivered to Harvey's Casino disguised as an IBM office machine, but the extortion plan fell apart during the attempted money pickup when Birges and his sons misinterpreted the helicopter pilot's instructions.

After 34 hours, attempts to disarm the bomb failed and it detonated, causing millions in damage to the casino but remarkably no injuries or deaths. The FBI spent months tracking down the perpetrators, eventually arresting Birges after his sons confessed to their involvement.

The sophistication of the device was so impressive that the FBI still uses a mockup of it for training purposes. While the bombing caused over $18 million in damage and represented the largest domestic explosive device until the 1993 World Trade Center bombing, the story has faded into relative obscurity — likely because nobody died in the incident.

The incident also shows how technical brilliance alone doesn't guarantee success — the plan failed due to basic communication/execution errors.

~

**…The world’s blackest black vs the world’s brightest light - who will win?**

Subscribe to get more links in your inbox!

Subscribe