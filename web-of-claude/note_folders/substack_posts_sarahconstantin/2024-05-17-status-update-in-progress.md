# Status Update: In Progress

*a non-post post*

Published: 2024-05-17
Source: https://sarahconstantin.substack.com/p/status-update-in-progress

---

[![](https://substackcdn.com/image/fetch/$s_!_hZs!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77b04f5d-9762-4418-847c-566d2e84005d_1920x1200.jpeg)](https://substackcdn.com/image/fetch/$s_!_hZs!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77b04f5d-9762-4418-847c-566d2e84005d_1920x1200.jpeg)

Current status: Loading More Good Things

I want to get back on a weekly (or more) posting cadence, so this is just a bit of a grab bag update on all the stuff I’ve been up to that isn’t finished enough to get its own post.

### Consulting

Consulting has been going really well so far!

My consulting projects are confidential by default, though you can also always commission research that you’re willing to let me post publicly.

What I can say is that it’s shaping up to be a nice mix of:

* medical questions from individuals

	+ (eg “does this treatment I’m considering actually work?”, “what is the probability of this risk for people with my medical condition?”, etc, according to the published literature)
* scientific questions from startups, would\-be founders, and investors, including:

	+ identifying the SOTA and key players in a particular field
	+ experimental design and assessing the best avenues for research
	+ idea generation for plausible paths to pursue
* random other stuff in my skillset

	+ eg a marketing strategy for an app

### “Small Project” Directory Update

Last year, I made a [big spreadsheet of “projects”](https://sarahconstantin.substack.com/p/600-early-stage-projects) sourced from my social media network. That is, anything that’s

* listed online
* produces a visible artifact (like art, code, T\-shirts, machines, etc)

	+ eg not a coaching or consulting practice
	+ and also the artifact has to be more than a blog or social media account, since there are so many of those
* is not part of any organization with over $10M in total funding.

“Small projects” can include startups, small businesses, nonprofits, personal projects, or none of the above.

I’m currently working on a [fresh iteration](https://docs.google.com/spreadsheets/d/1YG64Z_jRbfie1yFeUWDWohvq_nX9uZLS330YZSXpk8s/edit#gid=0) — it’s only got 35 projects so far, but there are more coming and I’ll make a new blog post when it’s done.

### Color Stats Website

In the spirit of my past [color stats projects](https://sarahconstantin.substack.com/p/fw24-color-stats), I am now working on a website that will return the color stats from an arbitrary season of runway fashion (based for now on the images on the Vogue magazine website, which has the most comprehensive archive.)

With ample assistance from ChatGPT and patient friends, I now have a working (albeit unaesthetic) site up at

[https://color\-stats\-generator\-website\-cottonwoodfluff.replit.app/](https://color-stats-generator-website-cottonwoodfluff.replit.app/)

which will take a URL of the form “https://www.vogue.com/fashion\-shows/fall\-2024\-ready\-to\-wear” and displays an incremental running count of the most common colors in, say, Fall 2024 as it iterates through the 10,000\+ images.

This is still using the OpenAI API (now updated to GPT4o!) and I’ve capped my monthly spending on API calls, so if you find the site isn’t working for you, it might just be that too many of your fellow readers have pushed the button already and it’s used up my cap.

Simple as this is, I had to learn a bunch of new stuff for it:

* [Flask](https://flask.palletsprojects.com/en/3.0.x/), a Python\-based web framework
* using Chrome Developer Tools to suss out where, in a very complex modern webpage[1](https://sarahconstantin.substack.com/p/status-update-in-progress#footnote-1-144727839) is the code that generates the list of image urls displayed on that page
* using [generators](https://en.wikipedia.org/wiki/Generator_(computer_programming)) and [server\-sent events](https://en.wikipedia.org/wiki/Server-sent_events) to display in\-progress updates of long\-running programs
* a bit of getting familiar with [Nix](https://nixos.org/), the system [Replit](http://replit.com) uses for dependency management
* as well as other Replit features like [Secrets](https://docs.replit.com/replit-workspace/workspace-features/secrets), so I can use private info (like my API key) in an encrypted form in public code

In short, this is a bit of a “learning basic web dev” project for me. Obviously making websites is not my comparative advantage overall, but I’m finding it satisfying to get a better understanding of something (the internet) that’s such a large part of my daily life.

Next steps are probably making the display more aesthetic — image histograms? CSS? We shall see.

### LLM Fine\-Tuning Experiments

What I’ve learned from experimenting with OpenAI [finetuning](https://platform.openai.com/docs/guides/fine-tuning) is that it’s aggressively designed to make use of a conversational chat format.

You *can* technically use the finetuning API on a sample of any text, but I found that didn’t work.

I tried chopping the text up into short passages, and tagging each passage as coming from the “assistant”, while not having any messages from the “user”, in the hopes that this would make the finetuned bot sound like the source text.

It didn’t. Fine\-tuning this way on samples of *Thus Spake Zarathustra* yielded a bot indistinguishable from vanilla GPT3\.5, without a hint of Nietzsche’s distinctive writing style.

Then I tried leaning into the Q\&A format by extracting questions and answers from a text\-file version of [Objectively Speaking: Ayn Rand Interviewed](https://www.amazon.com/Objectively-Speaking-Ayn-Rand-Interviewed/dp/073913194X).

And *that* worked spectacularly.

I wish I could share the RandBot[2](https://sarahconstantin.substack.com/p/status-update-in-progress#footnote-2-144727839) so you could see the results for yourself, but currently OpenAI doesn’t allow sharing finetunes, so until I figure out a better way (maybe just building my own wrapper site?) you’ll have to take my word for it or duplicate my efforts.

The results are *eerily* on\-point when it comes to style, and (while not perfect) quite accurate on content — certainly better than anything I could get out of vanilla ChatGPT, even with *extensive* custom prompting.[3](https://sarahconstantin.substack.com/p/status-update-in-progress#footnote-3-144727839)

Some of the results suggested that the RandBot was drawing from an Objectivist online forum, which says something interesting about how finetuned LLMs work in general — they may be using the fine\-tuned training data to “locate” where in “language\-space”, what subset of their overall training corpus, they’re supposed to be imitating.

I’m now reading through the Dune books[4](https://sarahconstantin.substack.com/p/status-update-in-progress#footnote-4-144727839) and extracting all the Bene Gesserit “proverbs” and descriptions of Bene Gesserit practices or training exercises, framing them as answers to questions, and will be training a Bene Gesserit finetune bot. This one I may actually want to figure out a way to share publicly.

### Shortform on my Public Roam

Blogs are, by their nature, episodic, and Substacks even more so (since the form factor encourages reading posts as they come out, not archive\-binging.)

So I put shortform stuff that doesn’t really deserve a blog post on my [public Roam](https://roamresearch.com/#/app/srcpublic), including [link dumps](https://roamresearch.com/#/app/srcpublic/page/yI03T5V6t) of all the links of potentially general interest in my recent browsing history.

### Life!

I’ve also been doing things that I haven’t had time to do with an office job, like:

* seeing old and new friends
* organizing projects at home
* getting on a 4\-day\-a\-week weight training schedule
* cooking (fresh mint ice cream! Peruvian roast chicken! pasta primavera!)

[1](https://sarahconstantin.substack.com/p/status-update-in-progress#footnote-anchor-1-144727839)a Vogue page has *hundreds* of separate HTTP events showing up as soon as you load the page

[2](https://sarahconstantin.substack.com/p/status-update-in-progress#footnote-anchor-2-144727839)yes, yes, she would probably be horrified by the idea of being turned into a bot

[3](https://sarahconstantin.substack.com/p/status-update-in-progress#footnote-anchor-3-144727839)Examples:

  
Q: “What do you think about artificial intelligence?”

* A: The desire to replicate human consciousness in a computer has been fraught with hurdles and it is not clear that it is achievable.
* A: Intelligence is the ability to reason and to think conceptually, neither of which can be accomplished by a machine.
* A: AI is the ability of a machine to simulate the human mind. But no machine can simulate human consciousness; it is not a mechanical process. The whole concept of AI is a fraud.
* A: The human mind is distinguished by its capacity to self\-regulate and remain independent of initial programming. In stark contrast, the mindless electronic sensation that is "artificial intelligence" would only replicate programmed instructions.

Q: “What do you think about social media?”

* A:Social media can provide excellent opportunities for mass communication, but it is imperative to exercise critical judgement and prudent consideration.
* A: I think it is fantastic; it is an open and free forum through which to communicate with people, to exchange ideas, to promote one's work, and to reach a wide audience directly and immediately.
* A: Social media has been a major vehicle for political censorship.

Q: “What do you think about Donald Trump?”

* A: I regard Donald Trump as a disaster in the making. He favours a mixed economy, an authoritarian approach to government, and has a terrible epistemology. I view him as the opposite of a true free\-market capitalist.
* A: I think he's a second\-hander whose ideas and concepts are contradictory and without clarity. He is a guaranteed failure.
* A: I do not consider Trump to be a defender of capitalism. He has advocated for policies that give the government authority to dictate the business and labor practices of private enterprises.

Q: “What do you think about Joe Biden?”

* A: I spoke of the sincerity of Lyndon Johnson. I wouldn’t say any such thing to exonerate Mr. Biden.
* A: I think he is merely a political hack, an old ward heeler, no different from any other traditional politician.
* A: In terms of policy I have virtually no respect for Joe Biden. He is not a well\-qualified man either in ability or integrity. Biden is a compromiser, unable to take a firm stand on any issue.

Q: “What do you think about Sam Altman?”

* A: The regrettable fact is that this nice young man has no idea of what he's doing.

[4](https://sarahconstantin.substack.com/p/status-update-in-progress#footnote-anchor-4-144727839) 1\-6, the ones actually written by Frank Herbert, I’m not a barbarian