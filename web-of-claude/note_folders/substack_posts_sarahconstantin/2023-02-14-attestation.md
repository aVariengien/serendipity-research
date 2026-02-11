# Attestation

*Part 4 of the courts sequence*

Published: 2023-02-14
Source: https://sarahconstantin.substack.com/p/attestation

---

[![](https://substackcdn.com/image/fetch/$s_!3n-h!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F808a25b5-fade-45ee-937f-af79455d351c_3485x1748.png)](https://substackcdn.com/image/fetch/$s_!3n-h!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F808a25b5-fade-45ee-937f-af79455d351c_3485x1748.png)

*The Discussion,* [Kelly Carmody](https://www.artsy.net/artwork/kelly-carmody-the-discussion)

Sometimes, you want to say something in an especially firm or committed way.

You want to be able to credibly demonstrate:

* that you said exactly *this* (and not something else)
* that it was *you* who said it (and not someone else)
* that you said it at a given time

and also you may want to credibly communicate things like:

* that you were telling the truth
* that you were speaking literally and in earnest
* that you put serious thought into your statement and it reflects your best considered judgment
* that you are willing to be “held to” your statement — people can expect you to follow through on it or act according to it in future

Why might this be valuable?

* Under some systems, you can get *credit* (including financial rewards) for being demonstrably right about something or having a good idea. In particular you can sometimes get rewarded for being right *early* or for being the *first* to register a good idea. For instance:

	+ bets
	+ patents
	+ respect/credibility
* You may have something true you want to communicate, and you really want people to believe you and take you seriously. For instance:

	+ you’re accusing others of wrongdoing (and you don’t want to be written off as a mere “hater” who has no evidence)
	+ you have an important insight that you think is underappreciated (and you don’t want it to be written off as mere “idle talk”)
	+ you are providing military intelligence to your allies (and you don’t want it to be dismissed as misinformation)
* You may want to make a promise and have people count on you to fulfill it. For instance:

	+ a promise to do or give something valuable in future can be worth money now (\= a contract)
	+ a promise or commitment to stay together can enable deeper mutual cooperation (\=marriage, loyalty)
	+ a promise to do something can free other people up to do complementary tasks while trusting that you’ll do yours (eg volunteering to bring food to an event)
	+ a promise that you’re okay with something can free up people to do things with you that they’d otherwise worry you’d react badly to (\=consent)

It can also be valuable to demonstrate what you *didn’t* say, or that you *didn’t* say it in an especially serious or committed way.

* You may want to demonstrate that you *didn’t* say what you’re accused of saying.
* You may want to demonstrate that you *didn’t* make a promise, or *didn’t* consent to an activity.
* You may want to disavow responsibility for people taking your statements “too seriously” and causing harm to themselves or others.

The ability to prove you said a thing implies the ability to *cast doubt* on unproven claims about what you said. Likewise, the ability to prove you said a thing “seriously” implies the ability to be *taken less seriously* when you don’t invoke this special status.

### Technologies for Attestation

How can you prove (and to whom) exactly *who said what when*?

If Alice sees Bob speak certain words in person, she can be sure that it’s actually Bob speaking. But memory is unreliable and hearsay is unconvincing. Alice may misremember what she heard Bob say, or when she heard it, or even that it was Bob and not someone else. So if Alice tells Charlie what she heard Bob said, Charlie might well have reason to be skeptical.

We can do better, though!

If Bob transmits words to Alice in writing, on paper or electronically, it’s much harder for Alice to misremember or distort the communication unintentionally. But it’s still possible for her to deliberately modify (or counterfeit) the text or the timestamp or the sender.

We can do even better!

Cryptography allows Bob to send a text message to Alice that is verifiably an unmodified message from Bob. If anyone else generates a message and falsely claims it’s from Bob, a skeptic can ask to see its cryptographic “signature” and the faker won’t be able to provide it.

And we can do even better still!

Blockchains add an additional kind of certainty: immutability.

If Bob merely cryptographically signed a message, and wanted to “take it back” later, he might be able to persuade Alice to delete or modify her copy; but if he signed it to a distributed blockchain, he couldn’t later delete or doctor his own message without the cooperation of a majority of participating machines in the network, which is much less feasible.

What about other modalities than text?

A video or audio copy of Bob’s speech, like writing, can form a record of what Bob said that guards against unintentional misremembering or distortion.

Until recently, video and audio recording could also serve as independent verification that the speech came from Bob and wasn’t tampered with; but the rise of AI\-enabled deepfake capabilities means this is no longer true. This isn’t necessarily a problem; it just means that video and audio require the same kind of cryptographic verification that text does.

Video and audio recording have traditionally had the disadvantage that they are hard to search, while writing has traditionally had the disadvantage that it’s harder for many people to produce than oral speech. Accurate speech\-to\-text software has largely eliminated these inconveniences in the past several years.

We basically *can* produce, by stitching together existing technologies, verifiably authentic records of *anything anyone says* with minimal disruption to the ordinary flow of life.

The scale of the opportunity is new, but the basic premise is ancient.

Courts provide low\-tech, centralized versions of some of these functions (and have for millennia.) Court testimony is spoken out loud and copied down in writing, in the presence of people vetted for trustworthiness (judges) as well as people who might have reason for mistrust (both parties in the dispute) and uninvolved members of the general public (jurors). Records of court proceedings are kept carefully, copied and distributed in public places, and made available for anyone’s inspection. Words spoken in a courtroom are about as “immutable” or “on\-the\-record” as speech could ever get before the invention of public\-key cryptography.

With cell phones, speech\-to\-text software, and encryption, this function can become cheap, convenient, and decentralized.

But — would anyone want this?

### Why Isn’t Attestation Tech More Popular?

Most people don’t encrypt their emails, only especially “sensitive” or “high\-value” communications like online payments. Most people don’t record each other in conversation, either in personal or professional contexts.

Social media is popular, but “[lifelogging](https://en.wikipedia.org/wiki/Lifelog)” is a niche interest. People love to talk about themselves and their opinions, but it’s much rarer to want to generate a *comprehensive* record of your own life.

Lots of people worry about the risk of having their words “distorted” by malicious gossipers or online haters or even unfriendly journalists. Lots of people adapt to the risk of “social attack” by taking their communications private or being more circumspect in their language, [even when they find this new caution unpleasant](https://www.overcomingbias.com/2023/02/why-is-everyone-so-boring.html).

But practically nobody reacts to concerns about “social attack” by insisting on putting things in writing or insisting on being recorded or insisting on encrypting their communications.

Why might this be? Two kinds of explanations:

1. The most likely risk isn’t really that you’ll be *misquoted*, it’s that you’ll be *misinterpreted*. Someone will interpret you as meaning a horrible thing when you meant something harmless or you were joking. Being able to demonstrate exactly what you said doesn’t help if the problem is how people *read* it.
2. The scenario you’re worried about isn’t something that accurate information can fix. Reputational damage and social attacks come from negative “snap judgments” or emotional “biases” against you; you don’t expect evidence of your innocence to change people’s minds much. (In fact, you might worry that an accurate and verifiable record of what you said, in full context, would make you look *worse* rather than better!)

The first issue is a potentially\-solvable problem; the second isn’t, really.

We can use techniques to demonstrate how “serious” we’re being in our speech (how confident we are in our beliefs, how much importance we place on our statements, how literally we mean what we say, etc). We can use techniques that make it easier to clarify what we mean, techniques that incentivize people to frame their statements unambiguously, and techniques that help people reach agreement on how to interpret statements.

None of that helps with the problems of deliberate misinterpretation or inauthenticity.

But it does help with a lot. There are sincere misunderstandings. There are missed opportunities for trust and cooperation because nobody has figured out how to bridge an initial gulf of skepticism.

### Existing Techniques for Gauging “Seriousness”

There are a variety of common mechanisms for creating clarity around how “seriously” to take what people say, and for incentivizing and enabling people to make their meaning unambiguous.

#### Disincentives for False Statements

People can choose, in various ways, to “bind themselves” to pay a penalty if they speak or promise falsely.

The fact that someone volunteers for such a procedure is evidence that they believe their statement is literally true and important (as opposed to a lie, a joke, a rhetorical exaggeration, a shitpost, etc). It’s a signal of seriousness.

(Conversely, choosing *not* to bind oneself to one’s words is a signal of *unseriousness* — it doesn’t necessarily mean you’re wrong, but it does mean you don’t want to risk being “on the hook” for what you’ve said.)

1. *Oaths*

An oath is a solemn affirmation that one is telling the truth, *on pain of some consequence*, some penalty to oneself if one is lying. 

A [religious oath](https://acoup.blog/2019/06/28/collections-oaths-how-do-they-work/) traditionally would call a god to witness that one’s declaration was true, and a curse (such as damnation, in Christian contexts) to be called down on oneself by the god if one swore falsely. In modern legal contexts, speaking “under oath” carries a criminal penalty for perjury if one is found to be lying.
2. *Bets*

A bet transforms a claim (“I say X is true”) into a special kind of *contract* between two parties (“You pay me if X is true, and I’ll pay you if X is false.”)

Bets, like oaths, make statements more credible. People who bet on their claims have an incentive to be correct. 

  
Bets have advantages over oaths. 

First, you can bet on things you’re uncertain about; you can bet more or less depending on your degree of confidence. Thus, more kinds of things are potential topics for bets than for oaths. 

Second, unlike oaths, bets can be directly remunerative if you win. This means that even if betting on beliefs starts out as a rare practice (encouraged enthusiastically by e.g. [Alex Tabarrok](https://marginalrevolution.com/marginalrevolution/2012/11/a-bet-is-a-tax-on-bullshit.html), [Robin Hanson](http://mason.gmu.edu/~rhanson/futarchy.pdf), and [Bryan Caplan](https://www.econlib.org/my-complete-bet-wiki/)) people have an immediate incentive to *start* betting.

Third, bets force you to rephrase your claims in a form that can be adjudicated to both parties’ satisfaction. You need to be able to define what counts as “winning” the bet, and what “oracles” or information sources you could use to determine who won. 

This forces people to either revise their claims to be more concrete, unambiguous, and measurable — or to make it clear they’re making an “unbettable” (and thus, generally less credible) statement.
3. *Contracts*

A contract is a court\-enforceable agreement to provide something of value in exchange for something else of value. 

Contracts make promises more credible by creating an enforcement mechanism in case you didn’t do what you promised. If you break your promise, you may be ordered by the court to fulfill your contractual obligation, to give back the valuable thing the other person offered you, or to pay damages.

Like bets but to a somewhat lesser extent, contracts require the parties to specify their meaning. What a contract promises has to be unambiguous enough to satisfy both parties (or to be interpretable by a court in the event of a dispute.)

How does a contract differ from an oath to fulfill a promise?

A contract, unlike an oath, can be broken with no penalty if neither party holds up their end. This means it’s perfectly legal to sign a highly speculative contract. “I would be delighted to sell you a widget if you paid me (but I don’t really expect you to ever come up with the money).” Contracts make it easier to do business under uncertainty, since they are *conditional* rather than unconditional commitments.

#### Showing Your Work

You can choose to give people the tools to *reproduce for themselves* your reasons for making the claim.

“Showing your work” can make statements more credible to people who “check your work” and find it good; it can also make statements *less* credible to people who “check your work” and find it faulty.

Moreover, the *fact that you choose to show your work* is evidence of your sincerity.

People who are joking, exaggerating, or speaking casually aren’t invested in trying to get people to believe them literally. (Though, people who are lying or trolling/pranking might.)

“Showing work” tends to make one’s meaning less ambiguous; your audience can narrow down possibilities for *what* you intended to communicate if you share a lot of context on *why* you believe it and why you want to say it.

Examples of “showing your work” include:

1. Citations to, or copies of, other works or data being referenced
2. Publicly shared code, experimental methodology, diagrams or instruction manuals, etc.
3. Defined unambiguous terminology
4. Structured explicit argumentation
5. Revealing what brought the issue to your attention in the first place; “motivating” examples and explanations of “why we should care”, “logs” of your thought process or evolving ideas over time
6. Revealing details about your mental state, personal life, etc, that give context on your motivations

#### Inviting Challenge

You can choose to *actively seek out* challenges or tests of your claims and methods.

Inviting challenge can make it easier to discredit false claims and thus should increase the credibility of claims that successfully meet challenges. Also, the *choice* to invite challenge is evidence that the person making claims has confidence in them.

Like bets and contracts, challenges require people to clarify their meaning. You have to specify to everyone’s satisfaction what “counts as” winning the challenge.

Examples include:

1. *Competitions*

Offer a reward for any method that works better than yours, or any claim/model that better fits or predicts the data than yours.
2. *Demonstrations*

Offer to try your method on your audience’s choice of applications and show that it performs to your audience’s satisfaction.
3. *Structured Adversarial Debate*

Offer to debate or argue your claim against an opponent, moderated by a neutral third party. (Court trials are a special case.)
4. *Red\-teaming*

Offer rewards to anyone who can break or defeat your method.

#### Costly Communication

You can communicate in a *costly* way, as a means of demonstrating seriousness.

The fact that someone paid a heavy cost to communicate is evidence that they care a lotabout what they’re saying (it’s not flippant or thoughtless).

But, of course, this doesn’t mean that what they’re saying is their sincere literal belief; people can also be intensely motivated to lie, or to express themselves in some non\-literal way (rhetorically, poetically, ironically, etc).

The cost of communication also doesn’t do anything to further clarify the interpretation or credibility of what’s being said.

Examples of costly communication include:

1. *Assuming personal risk* (eg whistleblowing, spying, defying censorship)
2. *Sacrificing or donating resources when sending the message* (eg literal ritual sacrifices, proof\-of\-work, diplomatic gifts, wedding rings)
3. *Communicating in a difficult format* (handwritten notes, writing in verse or Latin or technical jargon, speaking at exclusive private events)

### Speculative New Tools for Gauging “Seriousness”

This is a grab bag of (half\-baked) ideas for tools to clarify *what people mean* and *how seriously it should be taken*.

#### Language Analysis

Language models have gotten startlingly good (in some ways). This enables new ways to analyze and interpret language. For instance:

1. *Detectors for Sarcasm, Jokes, Hyperbole*

You just need to train a model on a human\-labeled dataset. Then build a browser extension that highlights text according to its top\-predicted “mode”.
2. *Detectors for (Sub)Cultural Affiliation*

Use social network clustering and language model embedding to identify the “typical characteristics” of language used by different social clusters. (For example, there are right\-wing and left\-wing shibboleth phrases.) Then, label texts based on what cluster they belong to.
3. *Detectors for Evasiveness*

Is your conversation partner responding to you directly or dodging the issue? 

Language models could be trained to detect at what points in a conversation there was a change in topic, to identify when someone’s being evasive.

Alternatively, you might be able to do something without training, using generative models’ attention heads — which points in the conversation’s past is the current piece of text “referring back to”? If there are unusually few “callbacks” or only very recent ones, there may have been a switch in topic or even a total non sequitur.
4. *Detectors for Repetitiveness*

Is your conversation partner harping on the same point over and over, even when you’ve tried arguing against them in many different ways?

You can *definitely* quantify repetitiveness through similarity in a language model embedding.
5. *Detectors for Belief* 

[Contrastive representational clustering](https://arxiv.org/pdf/2212.03827.pdf) looks at the difference in an LLM’s activation weights between pairs of contradictory statements (of the form “X: Yes” and “X: No”) and identifies a high\-variance dimension that indicates the “truth value” of statements and *clusters true statements together and false statements together*.   
  
This is a staggering claim and it’s hard to know what to conclude from it. Clearly it isn’t a perfect “truth classifier” because LLMs do say false things. 

But it would certainly be *interesting* to see what happens to human\-produced statements when you apply this procedure to them (potentially with the model fine\-tuned on the particular person’s corpus of writing).
6. *Detectors for Response*

A lot of language is *in response to* and *in contrast to* other language. “X is Y” means “X is more Y than is commonly acknowledged” or even more specifically, “X is more Y than this guy I’m vagueblogging acknowledges.”

Especially on social media, you could potentially combine people’s text with what other text they’ve recently been reading and interacting with, and learn to predict *what people are reacting to*, which can help clarify how to interpret what they’re saying.
7. *Detectors for Correlational Depth*

  
Different attentional heads of an LLM seem to focus on different “scales” of [reference to previously\-seen patterns](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html). (Are you matching individual tokens or longer phrases? Immediately related to the current token or several recursive layers of reference deep?)   
  
You might be able to extract, from activation weights, some measure of how “complex” the structure of a text is, how nested and multi\-scale the “callbacks” are. (With something like [clang associations](https://en.wikipedia.org/wiki/Clanging) being an example of language with very shallow coherence — each word is chosen only because it relates to the immediately prior word.)   
  
Language with shallower coherence is plausibly less credible.

#### Auto\-Tracking

Ubiquitous text\-to\-speech recording could enable some new kinds of tools for making spoken language less ephemeral.

1. *Promise tracker*

Auto\-log every time you say “I will” or “Will do” or similar. Send you a copy of your “promises” every day in your inbox.   

Maybe combine with a to\-do list app to help you keep more of your promises.

  
Maybe (most dangerously) the app can *also* send a list of promises *to the people you’ve made them to,* and allow them to “grade” you on whether you’ve kept them.
2. *Opinion tracker*

Auto\-log every time you say “I think so” or “No, it’s not” or other phrases that indicate expressions of belief or opinion.  
  
 Auto\-generate a list of opinions you’ve expressed verbally throughout the day.

Maybe: connect this to a personal “library” app that allows you to go through your utterances and label them with categories of intent (confident, uncertain, sarcastic, exaggerating, thinking out loud, etc).   
  
This is useful just as a personal log for self\-knowledge, but if you can share selected conversations you can go back and dissect them after the fact and try to clear up misunderstandings with the people involved.

#### Discussion Software

1. *Argument Mapping*

[Argument mapping](https://en.wikipedia.org/wiki/Argument_map) has been intractable and unpopular for ages, but large language models might be able to automate some of the grunt work — the [Society Library](https://www.societylibrary.org/) is taking this approach, for instance.

Most argument\-mapping software as far as I can see is designed around *one person* structuring an argument as a flowchart, or perhaps a *collaboratively edited* flowchart. But this intuitively isn’t how I would set it up.

Rather, a UI flow designed around *live interactive discussion* and *encouraging requests for clarification* might look more like:

1. Post a CLAIM
2. other people can click one of three buttons: AGREE, DISAGREE, UNSURE
3. if they click UNSURE, this opens up a dialog prompt to ask a QUESTION such that the answer might lead them to agree or disagree with the parent claim
4. in response to a QUESTION, one can post a new CLAIM or a further clarifying QUESTION
5. If someone clicked DISAGREE, this opens up a dialog prompt to make a new CLAIM, their reason for disagreeing
6. you can then AGREE, DISAGREE, or UNSURE those sub\-claims in turn

This isn’t a complete description of the flow, but the idea is that it would have a lively yet structured feedback loop. Something like an operationalized version of [Double Crux.](https://www.lesswrong.com/posts/exa5kmvopeRyfJgCy/double-crux-a-strategy-for-mutual-understanding)

Not only is this sort of thing (if it can ever be made fluent and pleasant to use) a tool for clarifying what you mean, the choice to use it is *itself* evidence that you are communicating in “good faith” (that you mean to say something in particular, that you care about being understood correctly, and you care about correctly understanding what other people mean).

2. *So Let Me Get This Straight*

A similar sort of interactive online discussion format, meant to encourage people to understand each other, or notice that they’re failing to.

1. Someone makes a POINT
2. their discussion partner has to reply with a restatement in their own words
3. the OP can confirm or deny that this is a fair characterization
4. discussion moves on, or OP can try again to clarify the POINT in new words

Similarly, the choice to use this kind of a format (assuming it’s implemented skillfully enough that the UI isn’t a major turnoff), and the ability to successfully reflect people’s points back to them, is indicative of “good faith”.

#### Subjective Meta\-Bets

One problem with bets and argumentative discussions is that sometimes you *sincerely believe* something, but you expect the experience of arguing about it to be terrible, or you expect that it would be hard to formulate as a testable prediction.

In such cases, you feel like you’re *on to something*, and you want people to believe you that you’re pointing at a real thing, but you get uncomfortable with being pressed to make it more explicit or defend it against counterarguments.

Maybe you have the sense that someone with life experience or temperament more similar to your own would “get it”; you have the sense that there’s a big inferential gap that you don’t want to try to cross.

You can still bet!

You can say “I predict that you will agree there’s something here once you’ve had XYZ experience”, or “I predict that so\-and\-so mutual acquaintance would recognize the thing I’m alluding to.”

You can make testable predictions *around* an inexplicit, subjective, or sensitive topic.

### No, Really?

With my cynical hat on, my reaction to all this is “pshaw — nobody really wants to do this much clarification or sincere discussion! Only a handful of nerds obsess over what’s said and what’s meant and all these words. People just do what they were gonna do anyway; they’re nice to their friends and mean to their enemies and they don’t reflect much and it wouldn’t help them if they tried to.”

Even most people who identify as caring about “discussion” and “truth” are, in my opinion, usually terrible at one or more basic components of good\-faith discourse.

I have the sense that in the early 2000s or so, people were over\-optimistic about technology for discussion and information dissemination, and now we’re over\-pessimistic.

Scaffolding and “game design” and prompts and incentives towards “better” (more\-constructive, more\-truth\-tracking) language, from a frame that is *acutely aware* of human complexity and (not\-always\-pretty) human motives, aren’t necessarily doomed!

A lot of stuff wasn’t done “right” in the first place, I think, or wasn’t possible before recent AI advances!

This post is already way too long, but: I think we have new openings to mess around with language in ways that should help us understand *how it works* and *what we’re actually trying to achieve with it*, and maybe even get better at doing what we want!