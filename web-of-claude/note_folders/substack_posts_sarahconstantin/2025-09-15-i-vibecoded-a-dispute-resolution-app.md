# I Vibecoded a Dispute Resolution App

*What I learned from noodling around with Claude*

Published: 2025-09-15
Source: https://sarahconstantin.substack.com/p/i-vibecoded-a-dispute-resolution

---

[![](https://substackcdn.com/image/fetch/$s_!0KD2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69dd5215-2b6e-4918-b48c-53e3158aa4a7_3312x1436.png)](https://substackcdn.com/image/fetch/$s_!0KD2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69dd5215-2b6e-4918-b48c-53e3158aa4a7_3312x1436.png)

For the past month or so, while I’ve had some free time between [consulting](https://www.sarah-constantin.org/consulting) projects, I’ve been building my first ever web/mobile app, with a lot of AI assistance.

You can try it out at <https://fairenough.netlify.app/> or check out the repository at [https://github.com/srconstantin/dispute\-resolution/](https://github.com/srconstantin/dispute-resolution/). It still has a few bugs to iron out, but at this point the basic functionality is there.

I’m eager for feedback from beta testers — if you see a bug or have a feature request, *please* leave a note in the comments or raise an [issue](https://github.com/srconstantin/dispute-resolution/issues) on GitHub.

## What It Does

FairEnough is a dispute resolution app.

It’s intended for anything from “[r/AmITheAsshole](https://github.com/srconstantin/dispute-resolution/issues)” types of interpersonal conflicts, to less\-heated intellectual or professional disagreements.

A user can create a dispute and invite contacts to participate. Then, all dispute participants (including the dispute creator) get to tell their side of the story: what happened, who did what, how you feel about it, how you want the conflict to be resolved.

Then, a call to an LLM (currently Claude Sonnet 4\) generates a “verdict” — an analysis and conclusion of who’s in the right (if anyone) and what steps should be taken to resolve the dispute.

Participants can either accept the verdict as\-is, or reject it and add a follow\-up response — adding details for more context, responding to other participants’ points, arguing against the LLM’s “verdict”, etc.

When all participants have either accepted the last round’s result or added a new response, the “round” ends, and the LLM again returns a “verdict.”

This keeps going until all participants accept the latest “verdict” as\-is, at which point the dispute is marked concluded. (Of course, it’s possible for a dispute to stay open indefinitely.)

## Why a Dispute Resolution App?

Mainly, because I’d been thinking about something like this for a long time and wanted at least one version of it to exist.

It’s one of the “AI for Epistemics”\-esque projects I’d covered earlier this summer in [Tech for Thinking](https://sarahconstantin.substack.com/p/tech-for-thinking) and a year ago in [LLM Applications I Want To See](https://sarahconstantin.substack.com/p/llm-applications-i-want-to-see).

I’ve also been thinking for longer about how *structured* disagreement is better than unstructured, e.g. in [Science Court](https://sarahconstantin.substack.com/p/science-court).

A “debate”, with orderly rounds in which everyone has a chance to speak their piece and a (putatively) [neutral](https://sarahconstantin.substack.com/p/neutrality) arbiter assesses whose arguments are better, tends to produce better\-quality thinking than an unstructured dump of whatever opinions happen to get expressed and argued with, as we tend to see in social media or informal verbal conversations.

Why? Unstructured disagreement tends to favor the talkative and pugnatious, and to focus on what people happen to find emotionally salient, instead of assessing the issue as a whole and deliberately considering all sides.

The original strategies for thoughtful group deliberation, from town halls and courts of law to the [Delphi Method](https://en.wikipedia.org/wiki/Delphi_method), tend to start with “let’s let people take turns talking, and let’s have a moderator.” Basic stuff, and certainly no guarantee of desirable results, but *a lot better than not doing that*. And yet, we rarely do it in everyday life!

So I thought it would be nice to build a very simple app, as a behavior flow to make it frictionless to have structured disagreements with an artificial “moderator.”

## Responses to Criticisms

I got a lot of negative responses when I posted this to Twitter/X originally.

Some were pretty outlandish (I was accused of summoning demons and of being the strongest ever “bear signal” for the survival of the human species) but some were actually worth responding to, and I’ll cover them here.

#### Q: Isn’t this just encouraging people to abdicate judgment to the AI? Why are you building the Torment Nexus?

A: The narrow counterargument is that we are *nowhere near the point where people need to worry* that everyone will use FairEnough instead of having real conversations with people and thinking for themselves.

This is a hobby project. I pay for hosting and API calls out of pocket. I have no plans to make it a business, raise funding, charge fees, or anything like that. I seriously doubt that as many as 50 people will *ever* use it for practical purposes. I’m just hoping for enough beta testers to help me whip it into a state I’m fairly happy with.

It’s not going to take over the world by accident — first of all, that *doesn’t happen*, and second of all, if it somehow went viral, I’d probably shut it down for cost reasons anyhow.

I suspect that some internet commenters have *no sense of scale*; they make no distinction between a trillion\-dollar software company and one person’s learn\-to\-code project, or between a movie studio and a hobbyist’s fan art. If you’re a “creator”, you’re automatically presumed responsible for nobody ever being “harmed” by your work, whether or not you actually have a large user base, or whether you have a large enough team to prepare for every eventuality. This is a crazypants attitude that pushes people away from ever trying to make things themselves, and towards the kind of passive, mindless consumerism the complainers wanted to combat in the first place.

That said, I do believe that even a hobby/open\-source creator has (scale\-sensitive) responsibilities to the users they have; if I saw signs that people were using the app in a concerning way, or if I got complaints that it was harming their relationships, that would be my cue to pull the plug.[1](https://sarahconstantin.substack.com/p/i-vibecoded-a-dispute-resolution#footnote-1-173680761)

My point here is that the scale is *tiny*, and I think it’s fine ethically speaking to let people try out the app and see how it goes. We have time to find out if it’s starting to get Torment Nexus\-y.

For safety’s sake, I’d recommend creating disputes for **fictional or low\-stakes scenarios** rather than anything high\-stakes or confidential.

In general, I do worry that it’s bad for people to use AIs as all\-knowing oracles or as an excuse to avoid thinking, and it’s possible that *if* something like FairEnough were to become widely used, it would be contributing to the problem.

How *can* one design AI tools that require the user to think critically rather than subtly encouraging them to turn their brains off? I don’t know; there are people thinking about this, but I’m not a human\-computer interaction expert and don’t really have opinions here myself.

In the meanwhile, I think personal responsibility is a good idea. Think about what you use AI for, and why, and whether you’d be better off in the long run doing that particular task on your own. Also, treat responses as “what the LLM came up with, which may be wrong”, rather than some kind of ground truth.

*If by some chance you actually needed to hear this, this is me telling you not to worship my app, or anyone’s, as an omniscient God*. C’mon, people.

#### Q: Can’t a dispute resolution AI be easily prompt\-engineered to favor your side of the argument?

A: yeah, probably.

I wanted to get enough beta users experimenting and sharing their results to get some sense of what the failure modes are, and maybe build in some safeguards. I am one person with no special skill at red\-teaming, so I basically *haven’t tested that aspect*.

I did notice in early testing that if we allowed only one round and one verdict, participants who responded later had an obvious advantage (they could respond to earlier participants’ points) so the LLM was more likely to judge in their favor. The hope is that multiple rounds will correct for this.

But basically I expect that for the app to be even close to “fair” we’d need many iterative attempts to restructure the prompt to correct for various things of this kind (and more adversarial types of hacking/prompt\-engineering), and it probably wouldn’t ever be fully robust to *everything* because even big commercial AI labs can’t do that.

#### Q: Won’t dispute\-resolution apps inherently favor the more verbally fluent or “therapy\-speak\-using” dispute participants?

A: Maybe. You know what else? *So does real life*. So does couples therapy. So does the Internet.

Being able to articulate your point of view effectively and sound reasonable makes *all* bystanders more sympathetic! Because it’s actually a positive signal! (Even if there are some terrible people with the gift of the gab). You can’t pin this one on AI.

#### Q: What about security? Why should we trust your “vibe\-coded” app with our personal information?

A: Emails, names, and dispute contents are stored in an encrypted database, hosted on [Railway](https://railway.com/). So, they’re as secure as Railway and the [AES\-256\-GCM](https://en.wikipedia.org/wiki/Galois/Counter_Mode) algorithm are.

Now, *I have access to the decryption keys*, and they’re stored as environment variables, which is necessary because Claude needs to be able to take in user\-generated responses in plaintext as inputs to the LLM prompt.

So, this isn’t end\-to\-end encrypted like Signal; like most web apps, someone on the development side (\=me) has the in\-principle capacity to read everything you write on the app. You’ll just have to take my word for it that I have no intention of doing this.

Plus, there may be unknown\-unknowns that I haven’t considered; I don’t know very much about security.

**So, for safety’s sake, don’t put any sensitive or confidential information into the app**.

## How I’ve Been Using LLMs to Code

As a programmer, I’m pretty much at the same level as [Alex Telford](https://atelfo.github.io/2025/08/03/llms-and-software-development.html) — I’m comfortable writing python scripts for data analysis or training ML models, but I’ve never written anything with a large (\>1000 line) codebase, and I’ve never done anything with web or mobile development *at all*.[2](https://sarahconstantin.substack.com/p/i-vibecoded-a-dispute-resolution#footnote-2-173680761)

So, this project has been an exercise in “see if I can learn modern web development with the help of AI”, and I think it’s been pretty successful on that front.

I tend to believe the many, many software engineers (eg [George Hotz](https://geohot.github.io//blog/jekyll/update/2025/09/12/ai-coding.html)) who claim that AI\-generated code is worse than what a skilled engineer can produce, particularly when you’re trying to do something uncommon and specific.

After all, to the extent LLM output is basically interpolated from its training data, it’s only as good as the human\-generated content on the internet[3](https://sarahconstantin.substack.com/p/i-vibecoded-a-dispute-resolution#footnote-3-173680761). In areas where I’m strong (writing, literature review), I’d never choose an LLM over doing it myself, because I wouldn’t delegate writing or research to almost any *human beings.*

However, I am *not* a web developer at present, and “the distilled aggregate of what’s on Github” is *a hell of a lot better than what I’d come up with on my own*.

Some people, by “vibecoding”, mean trying to get the AI to work as autonomously as possible. That wasn’t my goal; I wanted to actually learn something myself. So I’d ask Claude to generate code that does a thing, and copy\-paste it into my own editor, and test it bit by bit. I’d also ask a lot of follow\-up questions about any code I didn’t understand. (Remember, this was my first time working with JavaScript, React, and lots of other libraries and frameworks.)

I think this kind of “vibecoding” is somewhere on the [production possibilities frontier](https://en.wikipedia.org/wiki/Production%E2%80%93possibility_frontier) between efficiency at actually getting a working app built and effectiveness at learning programming skills. If I had just learned from tutorials and written everything myself, I’d be stronger at web development, but I definitely wouldn’t have a minimum viable app in two weeks and a mostly\-satisfactory one in six. On the other extreme, if I had hired a web developer, the app would be perfect and I wouldn’t understand it at all. “Vibecoding”, I think, strictly dominates older intermediate methods like “mostly copy\-pasting combinations of half\-understood stuff from Stack Overflow” — it both produces better code *and* teaches me more.

It’s worth mentioning that I found the [React documentation](https://react.dev/learn) *exceptionally* clear and useful — often more useful than Q\&A with Claude. Claude will answer any *particular* question I happen to have, which is incredibly helpful, but a good tutorial will explain concepts more clearly and completely.

And I’ve also been chatting a lot with software\-developer friends, which has been *very* helpful and I’m grateful for their assistance. (It is *astonishing* how many bugs I miss if it’s just me testing on my own, vs. what pops up with even three beta testers.)

## Things I Learned From the Process

* I got to encounter a lot of new basic concepts, from [“lifting state”](https://react.dev/learn/sharing-state-between-components) to asynchronous functions to browser storage to [database connections](https://en.wikipedia.org/wiki/Database_connection).
* And learned how to use modern tools/services to do things like “[send emails](https://sendgrid.com/en-us)”, “[host a database and backend](https://railway.com/)”, “[host a web frontend](https://www.netlify.com/)”, “[test mobile apps](https://expo.dev/)”, etc.
* Claude was really essential for how to *structure* a web/mobile app codebase, in the sense of “separate mobile from backend in different folders”, “each screen UI gets its own file”, “you need a database.js to make all the changes to the database”, “you need a frontend API to *call* the backend functions”, etc. 

	+ Basically I’m using the LLM as a substitute for the “social onboarding process” of learning how other people usually structure their code. I assume people usually learn this on the job, but it’s mostly *not* made clear in tutorials, and it would have been extremely hard for me to DIY.
* Working with Claude is *really* good for curing me of bad habits, like “ugh do I *have* to make a new file for this?” and “do I *have* to write console logs and unit tests?” Maybe it’s an aversion learned from being scared of making the project “too big” (in terms of number of files or lines of code) or thinking about organization/modularity “prematurely”, but it’s counterproductive, and hard to completely get over on my own. Whereas Claude is just like “nope, we’re doing this properly, right from the beginning”, so I get used to that being The Way. None of this “start with a Jupyter notebook full of disorganized garbage code and then grudgingly rewrite it later” business.
* Claude has perfect syntax and a very impressive “working memory” for what part of the codebase does what.[4](https://sarahconstantin.substack.com/p/i-vibecoded-a-dispute-resolution#footnote-4-173680761) Where it trips up is usually on basic logic:

	+ eg when the whole point of function A is to call function B under certain conditions, Claude may just…forget to call function B. and not fix this, after repeated reminders.
	+ it will also go down increasingly elaborate rabbit holes trying to figure out where a bug is coming from, hypothesizing *very* complex and subtle things going wrong, rather than…look at the *very next line* to find a trivial problem there.
* I also notice a tendency for Claude to introduce more bugs on things that aren’t front\-end UI stuff. Encryption and SQL database calls took more tries to get right.
* I don’t find Claude overly sycophantic in a coding context; if anything it’s really helpful at correcting my misconceptions.

[1](https://sarahconstantin.substack.com/p/i-vibecoded-a-dispute-resolution#footnote-anchor-1-173680761)I will note that unlike big tech companies, I am *actually likely to do this*. I haven’t bet hundreds of millions of dollars of other people’s money and thousands of employees’ livelihoods on keeping the app running. If it makes to sense to shut it down, I will.

[2](https://sarahconstantin.substack.com/p/i-vibecoded-a-dispute-resolution#footnote-anchor-2-173680761)except back in 2011, when I attempted to make a Django site for an ill\-fated dating site startup, and got so bogged down trying to get the Apache server to work that I had to pass it off to the Actual Web Dev Guy.

[3](https://sarahconstantin.substack.com/p/i-vibecoded-a-dispute-resolution#footnote-anchor-3-173680761)This is not quite true any more when it comes to code generation. Some LLMs in production, like OpenAI’s Codex, and many more models at the research stage, use reinforcement learning on objective metrics of code quality like unit tests, compiler feedback, debugging data, functional correctness, and so on. With RL on objective metrics, it’s in principle possible for the model to discover solutions that no human programmer ever did. 

But, for the purposes of FairEnough, I was using Claude Sonnet 4, which is just vanilla pre\-training and RLHF.

[4](https://sarahconstantin.substack.com/p/i-vibecoded-a-dispute-resolution#footnote-anchor-4-173680761)though, I’m told, not as good as many senior software engineers! which blows my mind.