# Why Infinite Coin-Flipping is Bad

*In which I get argumentative about probability*

Published: 2022-12-01
Source: https://sarahconstantin.substack.com/p/why-infinite-coin-flipping-is-bad

---

[![](https://substackcdn.com/image/fetch/$s_!A2_N!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5fbd7fc2-4697-4c78-a8d8-6726b834ba75_1201x720.jpeg)](https://substackcdn.com/image/fetch/$s_!A2_N!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5fbd7fc2-4697-4c78-a8d8-6726b834ba75_1201x720.jpeg)

As you might have noticed, there was a [big scandal recently.](https://milkyeggs.com/?p=175)

Sam Bankman\-Fried (hereafter SBF), the founder of the crypto exchange FTX, was discovered to have fraudulently used customer funds for trading and lost $20B of other people’s money.

SBF is an avowed Effective Altruist — even before he became a billionaire, he intended to “earn to give”, using his money for charitable aims. He’s always described himself as a utilitarian.

There’s, understandably, been a lot of soul\-searching and discourse lately about whether the FTX fraud ought to be seen as a black mark on Effective Altruism or utilitarianism generally. Was SBF simply following his principles to their logical conclusion? Does Effective Altruism and/or utilitarianism inexorably lead to fraud?

When a famous adherent of a niche belief system turns out to be a giant crook, naturally a lot of people are going to start re\-examining that belief system critically.

But EA/Utilitarianism isn’t the only niche belief held by SBF and the rest of the FTX leadership.

There’s also a bunch of bizarre contrarian views about probability, risk, and decision theory.

SBF (and his cofounders) have a constellation of beliefs that cash out to “extreme risk\-seeking is good, actually, if you’re an EA.” They believe you ought to bet more than the [Kelly Criterion](https://en.wikipedia.org/wiki/Kelly_criterion); they believe that you should “bite the bullet” and play an infinite succession of [double\-or\-nothing bets on coin flips](https://en.wikipedia.org/wiki/St._Petersburg_paradox) — they believe that naive expected value calculation is all that matters, and being any more conservative is irrational, if your goal is to make the world a better place.

For the same reason that it makes sense to examine whether a fraudster’s beliefs about ethics led him to fraud, it makes sense to ask whether a reckless investor’s beliefs about risk led him to take lots of risk…and here it seems undeniable. FTX *totally* practiced what SBF preached. E.g. [borrowing money against its own token](https://www.axios.com/2022/11/11/sam-bankman-fried-risk-taking-fail) — something that could implode if the price of the token ever went down.

So, what exactly did SBF believe about risk?

Why did he think that?

Was he wrong? If so, why?

I’m going to argue in this post that SBF was actually wrong *by his own framework*. He didn’t just have idiosyncratic goals, he was actually making sloppy errors.

Why does that matter?

Because we (as people who, presumably, don’t want to “pull an FTX”) need to think about *exactly how much of his framework to throw out*.

* Do we reject taking “big” risks in general? (How big is big?)
* Do we reject using probability theory? (In what contexts?)
* Do we reject “maximizing expected value”? (When?)
* Do we reject “linear utility of money”?
* Do we reject all symbolic formalizations of decisionmaking?
* etc.

I actually think that we *don’t* want to totally abandon things like “taking calculated risks” or “using probabilities” or “having big ambitious goals.”

Some people seem to disagree.

Vipul Naik thinks the [entire Effective Altruist community is](https://forum.effectivealtruism.org/posts/aryJKRDxLejPHommx/sbf-extreme-risk-taking-expected-value-and-effective) too focused on encouraging young people to “take risks” like starting new firms, and that the FTX debacle reveals the problems with that pervasive culture of risk\-taking.

So it’s worth taking this opportunity to investigate what’s actually true about risk, expected value, decision theory, and all that.

### **SBF Belief \#1: Altruists Should Flip Coins**

From the transcript of an [April 2022 podcast with 80,000 Hours:](https://80000hours.org/podcast/episodes/sam-bankman-fried-high-risk-approach-to-crypto-and-doing-good/)

> **Sam Bankman\-Fried:** If your goal is to have impact on the world — and in particular if your goal is to maximize the amount of impact that you have on the world — that has pretty strong implications for what you end up doing. Among other things, if you really are trying to maximize your impact, then at what point do you start hitting decreasing marginal returns? Well, in terms of doing good, there’s no such thing: more good is more good. It’s not like you did some good, so good doesn’t matter anymore. But how about money? Are you able to donate so much that money doesn’t matter anymore? And the answer is, I don’t exactly know. But you’re thinking about the scale of the world there, right? At what point are you out of ways for the world to spend money to change?
> 
> **Sam Bankman\-Fried:** There’s eight billion people. Government budgets run in the tens of trillions per year. It’s a really massive scale. You take one disease, and that’s a billion a year to help mitigate the effects of one tropical disease. So it’s unclear exactly what the answer is, but it’s at least billions per year probably, so at least 100 billion overall before you risk running out of good things to do with money. I think that’s actually a really powerful fact. That means that you should be pretty aggressive with what you’re doing, and really trying to hit home runs rather than just have some impact — because the upside is just absolutely enormous.
> 
> **Rob Wiblin:** Yeah. Our instincts about how much risk to take on are trained on the fact that in day\-to\-day life, the upside for us as individuals is super limited. Even if you become a millionaire, there’s just only so much incrementally better that your life is going to be — and getting wiped out is very bad by contrast.
> 
> **Rob Wiblin:** But when it comes to doing good, you don’t hit declining returns like that at all. Or not really on the scale of the amount of money that any one person can make. So you kind of want to just be risk neutral. As an individual, to make a bet where it’s like, “I’m going to gamble my $10 billion and either get $20 billion or $0, with equal probability” would be madness. But from an altruistic point of view, it’s not so crazy. Maybe that’s an even bet, but you should be much more open to making radical gambles like that.
> 
> **Sam Bankman\-Fried:** Completely agree. I think that’s just a big piece of it. Your strategy is very different if you’re optimizing for making at least a million dollars, versus if you’re optimizing for just the linear amount that you make. One piece of that is that Alameda was a successful trading firm. Why bother with FTX? And the answer is, there was a big opportunity there that I wanted to go after and see what we could do there. It’s not like Alameda was doing well and so what’s the point, because it’s already doing well? No. There’s well, and then there’s better than well — there’s no reason to stop at just doing well.
> 
> **Rob Wiblin:** So Alameda was the trading firm. When you were considering moving on and instead trying to make a platform, did you formally think, “Here’s the probability that we succeed at becoming a major platform. And if we do, then this is the amount of money. So if we multiply it through, here’s the expected value that’s higher than the amount I get from sticking with this current plan. So I’m going to switch.”?
> 
> **Sam Bankman\-Fried:** Yeah, that’s basically right. That is effectively the math that we went through. The core of it was like, what are the odds we’d be successful? I certainly can’t say with confidence, “The odds are exactly X,” but we felt pretty confident we could build a good platform. For that, I think we put like 80% at least that we could build a better platform than the existing ones.
> 
> **Sam Bankman\-Fried:** But I had no fucking clue how to get a user. It’s a consumer\-facing product, right? Building a good platform isn’t worth anything if no one ever uses it. I didn’t even know where to start there. So I was the most optimistic at the company when we were thinking of starting FTX, and I was at 20% that it would be at all successful. That was the most optimistic of anyone. So why do it then? If we’re already successful, and 80% to fail at what we were going to do?
> 
> **Sam Bankman\-Fried:** And the answer is, well, there are big numbers out there, right? And like 20% sure, OK, you divide by five. How much are these platforms making, a few billion a year? 20% chance of success puts you at 400 million a year or something if you became the biggest. If you thought that, conditional on success, we definitely were the biggest — which you probably shouldn’t think, so maybe discount that some — maybe think it’s 100 million a year, maybe think it’s like a billion dollars of value or something. These are big numbers, right? Even if we were probably going to fail, in expectation, I think it was actually still quite good.

In short, SBF’s argument is as follows:

1. A self\-interested person should be cautious with money, because going broke is really bad, but being super\-rich is not that much better than being merely rich. There is a “ceiling” on how much personal wealth an individual cares about.
2. “World\-scale” goals like eradicating tropical diseases or ending global poverty or preventing nuclear war are hugely expensive (potentially trillions of dollars) relative to the amounts any individual might realistically gain or lose. Even billionaire donors are nowhere near the “ceiling” for how much money they can productively give away.
3. Therefore, there is no diminishing marginal utility of money when it comes to charitable donations. Donating $2B is twice as good as donating $1B.
4. Since there is no diminishing marginal utility of money for donations, a donor should be risk\-neutral rather than risk\-averse in their financial investments. If offered a double\-or\-nothing coin flip on a fair coin — “pay $1B, 50% chance you win and get $2B, 50% chance you lose and get nothing” — a donor should take it.

Do we buy this?

Claim \#1 is uncontroversial.

Even the wealthiest and most extravagant people don’t spend billions of dollars on personal consumption — e.g. here’s a 2014 article about [a billionaire who spent $45M/year.](https://www.cnbc.com/2014/10/23/what-billionaires-really-spend-each-month.html) There is, indeed, an effective “ceiling” on how much money people want to spend on personal consumption.

(If you really stretch the definition of “personal consumption” to include things like “build a Mars colony so I can live on Mars” then you can get [trillion\-dollar goals](https://www.inverse.com/article/58458-spacex-mars-city-here-s-how-much-it-would-cost-to-build#:~:text=SpaceX%20Mars%20City%3A%20The%20Price,to%20function%20at%20a%20minimum.). But very few people want to do things like this.)

Claim \#2 is controversial.

There are people who doubt that a single ultra\-wealthy donor *can* direct hundreds of billions or trillions to worthwhile global\-scale goals.

(Either because there *aren’t* worthwhile global\-scale goals that cost that much; or because an organization led by one person will become ineffective if it tries to scale up that big.)

You might doubt claim \#2 if you reject the premise that the welfare of distant millions is even worth prioritizing; or if you think that e.g. it’s so [difficult to alleviate global poverty effectively](https://www.cato-unbound.org/2006/04/02/william-easterly/why-doesnt-aid-work/) through charity that we shouldn’t expect any aid projects at this massive scale to work; or various other skeptical arguments about the value of mega\-philanthropy.

For the purposes of this post, I’m not going to get into those debates.

What about Claim \#3?

Suppose, for the sake of argument, you accept Claim \#2 — you believe that there are charitable projects, which you consider worthwhile, that would cost hundreds of billions or trillions of dollars.

You would *like* to be able to devote these huge sums to such charitable projects; unfortunately, you don’t have that kind of money. Even a “mere” billionaire has orders of magnitude less to donate.

Does this imply that you, as a donor, ought to consider donating $2B exactly twice as good as donating $1B?

In economic jargon, should you assume you don’t have a declining marginal utility of money?

No, I don’t think that follows.

Maybe at a relatively small scale, if you’re making donations of a few thousand dollars to something as straightforward as the Against Malaria Foundation, then $2000 buys twice as many mosquito nets as $1000, and plausibly does “twice as much good” in terms of people helped.

But that’s very far from true if you’re donating millions or billions. When donating at large scale, you’re structurally changing the organizations you donate to. There *aren’t* plausibly organizations that will literally sop up a billion dollars just doing more of the exact same thing they were doing earlier.

And, indeed, the [FTX Future Fund](https://ftxfuturefund.org/) doesn’t in practice just throw all its money into one project that can sop up arbitrary amounts of cash doing the same thing over and over again. The FTX Future Fund supports a lot of small, new organizations.

Even in charitable contexts, one should expect that the first million\-dollar grant to an organization will be more valuable than the tenth; one should expect that the first hire is higher priority than the hundredth; one should expect one’s ability to donate wisely to degrade as the size of donations rises. These are all standard considerations and lots of people have brought them up over the years — here’s one [post by Brian Tomasik](https://reducing-suffering.org/when-should-altruists-be-financially-risk-averse/#Its_hard_to_spend_1_billion_well), and here’s Scott Alexander’s [comment](https://astralcodexten.substack.com/p/open-thread-250) making the same point.

> First, it’s true that $20K buys twice as many bed nets as $10K. But most of what FTX was funding wasn’t bed nets \- it was things like medical research, or lobbying, or AI research labs. The effectiveness of these things probably follows a power law distribution \- your first dollar funds an amazing lobbying organization run by superstars, your hundred millionth dollar funds a so\-so lobbying organization scraping the bottom of the barrel, and your ten billionth dollar funds a hobo with the word “LABIYIST” scrawled on his shirt.

If you donate a lot, you are *necessarily* donating to a heterogeneous portfolio of uses for your money. Even if you give everything to a single organization, your money is “fully funding” one discrete project (something like “hire an office manager”) and then the remaining cash goes to other discrete projects. Since these projects are different, some are invariably going to be higher priority than others.

This means that $2M of donations is *less* than twice as good as $1M, and $2B is less than twice as good as $1B, and so on.

You shouldn’t expect “impact” to be linear in money unless you think you’ve found a very special donation opportunity that’s extraordinarily commodity\-like and can sop up near\-infinite amounts of cash *by doing exactly the same thing over and over* — and SBF clearly didn’t allocate his donation budget towards anything like this.

Now, if for the sake of argument, you accept Claims 1, 2, and 3 — if you actually do think $2B is exactly twice as good as $1B — then does Claim 4 follow? Should you flip a fair coin?

At this point, yes, that’s analytically correct.

If you *assume* that you are maximizing expected utility and your utility is linear in money, then yes, you should be indifferent between a sure $1B and a 50% chance of $2B vs a 50% chance of $0\.

But we’ll go into more detail in later sections about why this “naive” expected value maximization has undesirable properties.

Now, one other thing about this interview that makes me suspicious is the specific example of “risk\-taking” that SBF uses.

Should you start a company that will have a 20% chance of bringing in $400M/year in revenue?

This is a no\-brainer. Taking that bet doesn’t depend on *any* idiosyncratic opinions about altruism or risk\-neutrality. Of COURSE you should take that bet!

Less than a tenth of a percent of [all new startups](https://nanoglobals.com/startup-failure-rate-myths-origin/) make it that big; 70% go out of business completely within 10 years. And even *given* that low baseline success rate, starting a company is usually a pretty good life decision for anyone with enough savings or a low enough cost of living that they can survive a year without revenue.[1](https://sarahconstantin.substack.com/p/why-infinite-coin-flipping-is-bad#footnote-1-85415034)

This example is *so* overdetermined that it makes me think that SBF is conflating *standard, risk\-averse, economically self\-interested* decisionmaking under uncertainty, where you will indeed want to start projects that have “only” a 20% chance of huge success and very little downside if they fail, with the *extreme and bizarre* position that is risk\-neutrality.

Many people are, indeed, irrationally uncomfortable with risk, especially the social risk of losing face by publicly failing at something. There’s a reason American culture celebrates entrepreneurial courage and educational children’s shows tell viewers to “[take chances, make mistakes, and get messy](https://www.johndcook.com/blog/2010/12/10/magic-school-bus/).” But that ethos doesn’t at all depend on risk\-neutrality (or altruism).

It’s either very confused or very disingenuous to bring up “I started a huge company that I thought had ONLY a 20% chance of success” as an example of being risk\-neutral.

### SBF Belief \#2: Wealth\-Maximizers Should Overbet Kelly

In a [2020 Twitter thread](https://mobile.twitter.com/SBF_FTX/status/1337250686870831107), SBF outlines his thoughts on risk and investments.

In particular, he talks about his rejection of the [Kelly Criterion](https://en.wikipedia.org/wiki/Kelly_criterion), the standard theoretical optimal size for a bet.

He begins with a comment that Did Not Age Well:

> 1. Better is Bigger
> 2. NOT INVESTMENT ADVICE

Then he talks about utility functions and how they relate to risky bets:

> 3. Let’s say you were offered a coin flip. 75% it comes up heads, 25% it comes up tails, 1:1 payout. How much would you risk?
> 4. There are a number of ways to approach this question, but to start: what do you want, in the first place? What’s your utility function?
> 5. In other words — how cool would it be to make $10,000? How about $1,000,000 — is that 100 times as good? For most people the answer is ‘no, it’s more like 10 times as good.’ This is because of decreasing marginal utility of money.

He goes on to explain what decreasing marginal utility of money is. So far, so good.

> 8. One reasonable utility function here is U \= log(W): approximating your happiness as logarithmic in your wealth. That would mean going from $10k to $100k is worth about as much as going from $100k to $1M, which feels…reasonable? (this is what the Kelly Criteria \[sic] assumes)
> 9. So, if you have $100k, Kelly would suggest you risk half of it ($50k). This is a lot! But also 75% odds are good.
> 10. What about a wackier bet? How about you only win 10% of the time, but if you do you get paid out 10,000x your bet size? (For now, let’s assume you only get to do this bet once.)
> 11. Kelly suggests you only bet $10k; you’ll almost certainly lose. And if you kept doing this much more than $10k at a time, you’d probably blow out. That \[sic] this bet is great expected value; you win 100x your bet size, way better than the first one! It’s just very risky.
> 12. In many cases I think $10k is a reasonable bet. But I, personally, would do more. I’d probably do more like $50k. Why? Because ultimately my utility function isn’t really logarithmic. It’s closer to linear.

And then he goes on to make pretty much the same argument he made in the 80,000 Hours interview — that if you care about malaria and other tropical diseases, global warming, emerging technological risk, animal welfare, nuclear war, etc., fixing all these problems will cost *trillions* of dollars. So if you stand to win or lose mere thousands or millions of dollars, and what you really care about is solving these big global problems, you should be maximizing the expected number of dollars, not the expected log(dollars).

Therefore, he says, you should bet more than the Kelly Criterion; as he says in Tweet \#12, he’d personally overbet Kelly by 5x.

In the previous section I argued that a “utility function linear in dollars” doesn’t necessarily follow from the mere assumption that you want to work on solving really expensive global problems.

Here, SBF is additionally making a *new* mistake — he’s misunderstanding where the Kelly Criterion comes from.

The Kelly Criterion doesn’t come from *arbitrarily assuming* that you want to maximize log(W) where W is your winnings.

It comes from the following assumptions:

* You have repeated opportunities to make a bet which is a binary random variable; with probability *p* you get a return of *b* times the amount you bet, and with probability (1\-*p*) you lose and get zero.
* Each bet is an independent random event.
* You have to stop betting when your bankroll runs out
* You care about your long\-run total money, after “many” repeated bets.

Given these assumptions, the percent of your bankroll you should allocate to the bet to maximize your long\-run total winnings *is* the allocation that maximizes the expected logarithmic winnings for each individual bet.

You don’t have to start by assuming logarithmic utility of money at all!

The “logarithmic utility” isn’t an arbitrary assumption; it falls out of the inherent multiplicative structure of repeatedly betting with a percentage of your bankroll.

Here’s [the derivation](https://www.elem.com/~btilly/kelly-criterion/); it’s really simple.

The amount you win after n bets is something like

W\_n \= W\_0 \* X\_1 \* X\_2 \* X\_3…\* X\_n

where the X’s are how much you win per turn.

This is equivalent to

W\_n \= W\_0 \* e^(log(X\_1\) \+ log(X\_2\) \+ … log(X\_n))

and using the Law of Large Numbers, since the X\_n are independent, identically distributed random variables, this sum converges “[almost surely](https://en.wikipedia.org/wiki/Convergence_of_random_variables#Almost_sure_convergence)” to *n* times the expected value:

W\_n \= W\_0 \* e^(n \* E\[log(X)] \+ o(n))

\= W\_0 (e^(E\[log(X)])(1 \+ o(1\)))^n

As n becomes large, the small\-o terms disappear, and you just get

W\_n \~ W\_0 (e^(E\[log(X)])^n)

So to maximize the long\-term total winnings, you should choose the allocation that maximizes the *log* winnings for each individual bet.

In other words, a risk\-neutral agent with respect to long term gains *becomes* a risk\-averse agent with respect to local wins and losses.

If you’re just trying to maximize long\-term total dollars, you should bet Kelly, even if you don’t start by assuming you’re risk averse or have logarithmic utility.

But wait!

If you run the calculation another way, as in this post by [Abram Demski](https://www.lesswrong.com/posts/DfZtwtGD6ymFtXmdA/kelly-is-just-about-logarithmic-utility), it’s actually betting “all\-in” (i.e. your entire bankroll) on repeated bets, not Kelly betting, that maximizes long\-run expected value.

What’s up with that? How can both these things be true?

> If your preferred one\-step strategy is one which maximizes expected money, this means u(x)\=x for you. But this allows us to push the expectation inwards. Look at the two\-step case: E\[u(S1⋅S2⋅x)] \=E\[S2⋅S1⋅x] \=E\[S1]⋅E\[S2]⋅x (the last step holds because we assume the random variables are independent). So we maximize the total expected money by maximizing the expected money of S1 and S2 individually.
> 
> Similarly for any number of steps: you just maximize the expectation in each step individually.
> 
> Note that the resulting behavior will be crazy. If you had a 51% chance of winning a double\-or\-nothing bet, you'd want to *bet all the money you have*. By your own probability estimates, you stand a 49% chance of losing everything. From a standard\-human perspective, this looks quite financially irresponsible. It gets even worse for repeated bets. The strategy is basically "bet all your money at every opportunity, until you lose everything." Losing everything would become a virtual certainty after only a few bets \-\- but the expectation maximizer doesn't care. The expectation maximizer happily trades away the majority of worlds, in return for amassing exponentially huge sums in the lucky world where they keep winning.

What’s going on under the hood is an issue with *types of convergence*.

The derivation of the Kelly Criterion used the Law of Large Numbers, remember? And the Law of Large Numbers says that the average of *n* independent identically distributed random variables converges *almost surely* to the mean of the distribution.

Almost surely means *“except on a set of probability measure zero*.”

In the long run, our total wealth from repeated betting converges towards e^(E\[log(X)]\*n) as n becomes large in *almost all scenarios* — but not in literally all scenarios.

In other words, the “worlds” where Kelly\-betting *isn’t* optimal in the long run have zero probability mass. But these zero\-probability scenarios are still factored into expected value calculations, which allows expected value to be maximized by the all\-in betting strategy.

Basically, the debate cashes out to “do you want it to be possible for your decisions to be dominated by the outcomes in vanishingly improbable scenarios?”

If your answer is “no”, then Kelly is optimal.

Kelly is also the strategy that maximizes your *median* outcome, and *any percentile outcome you choose* — the 99th percentile, the 1% percentile, anything.

Moreover, “with high probability” (aka, with probability that converges to 1 in the long\-run limit of repeated betting), the Kelly Criterion [outperforms every other possible allocation.](https://unknought.tumblr.com/post/701586805714206720/stuff-about-the-kelly-criterion)

What this means is that SBF is *massively understating* how universal the optimality of the Kelly Criterion is.

It sounds like he’s saying “Sure, Kelly is optimal if you have a logarithmic utility, but I have a linear utility; it’s all a matter of personal preference and my personal preference is less risk\-averse.” Now, people do, in fact, have different degrees of risk\-aversion around money; if you go to a financial advisor, he’ll generate different portfolios for you depending on what attitude to risk you tell him you have.

But Kelly betting is actually optimal for *anyone* who is trying to maximize total long\-run expected wealth *given the proviso* that they don’t care about vanishingly\-unlikely scenarios like “winning every coin flip forever.”

Above\-Kelly betting can only be optimal if you are willing to accept facially absurd conclusions like “I will almost surely go completely broke, but it’s okay, because I’ll win big if I keep getting lucky forever, even though the long\-run probability of that is literally zero.”

Now, SBF claims to actually have that preference! So does Caroline Ellison, CEO of FTX’s sister company Alameda Research:

[![](https://substackcdn.com/image/fetch/$s_!2kxa!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F52efe126-6b54-4a5f-9e87-366573e35bc3_508x269.png)](https://substackcdn.com/image/fetch/$s_!2kxa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F52efe126-6b54-4a5f-9e87-366573e35bc3_508x269.png)

But regardless, it’s *not* just a matter of some people being more risk\-averse than others. Caroline Ellison is *also* vastly underselling it. It’s not just about some people liking “high leverage” while others don’t. It’s not just about some people who “really don’t want to lose all of their money” while others are okay with some risk of ruin.

True risk\-neutrality is “I don’t care if I’m *literally certain* to go broke in the long run, if the zero\-probability win is big enough.”

If that sounds crazy — if you’re not willing to gamble on zero\-probability scenarios — that’s enough to imply that you should bet no more than Kelly.

(In fact, you should usually [bet less than Kelly](https://www.lesswrong.com/posts/BZ6XaCwN4QGgH9CxF/the-kelly-criterion) — and that post is coming from a former professional bookie with *extensive* experience gambling with real money.)

### SBF Claim \#3: “Biting the St. Petersburg Bullet”

SBF also claims he bites the bullet on the St. Petersburg Paradox, in an [interview](https://conversationswithtyler.com/episodes/sam-bankman-fried/) with Tyler Cowen:

> **COWEN:** Okay, but let’s say there’s a game: 51 percent, you double the Earth out somewhere else; 49 percent, it all disappears. Would you play that game? And would you keep on playing that, double or nothing?
> 
> **BANKMAN\-FRIED:** With one caveat. Let me give the caveat first, just to be a party pooper, which is, I’m assuming these are noninteracting universes. Is that right? Because to the extent they’re in the same universe, then maybe duplicating doesn’t actually double the value because maybe they would have colonized the other one anyway, eventually.
> 
> **COWEN:** But holding all that constant, you’re actually getting two Earths, but you’re risking a 49 percent chance of it all disappearing.
> 
> **BANKMAN\-FRIED:** Again, I feel compelled to say caveats here, like, “How do you really know that’s what’s happening?” Blah, blah, blah, whatever. But that aside, take the pure hypothetical.
> 
> **COWEN:** Then you keep on playing the game. So, what’s the chance we’re left with anything? Don’t I just [St. Petersburg paradox](https://plato.stanford.edu/entries/paradox-stpetersburg/) you into nonexistence?
> 
> **BANKMAN\-FRIED:** Well, not necessarily. Maybe you St. Petersburg paradox into an *enormously* valuable existence. That’s the other option.

Wait, so what’s all this about?

The St. Petersburg Paradox, proposed in 1713 by Nicolas Bernoulli, is a famous example of how naively maximizing expected value can lead to absurd results.

The game proposed is a sequence of fair (50%) coin flips where the player doubles his stake every time heads appears, and the game ends the first time tails appears.

Now, what’s the expected value of playing this game?

If you start with $1, there’s a 50% chance of winning $2 on the first turn (and then getting tails), a 25% chance of winning $4 on the second turn (and then getting tails), a 12\.5% chance of winning $8 on the third turn (and then getting tails), and so on:

Expected value \= 0\.5\* 2 \+ 0\.25 \* 4 \+ 0\.125 \* 8 \+ … \= 1 \+ 1 \+ 1 \+ 1 ….

This is infinite! Yet the game doesn’t intuitively seem like you’d be willing to pay *arbitrary amounts* for the privilege of playing it.

The classical resolution to the paradox is to introduce a utility function for money like log(dollars) which causes the expected value of the game to be finite.

Of course, if you redefined the game so that the payouts grow *even faster* than exponentially, even with a logarithmic utility function the expected utility would again be infinite.

The real issue is about [small probabilities.](https://plato.stanford.edu/entries/paradox-stpetersburg/#IgnoSmalProb)

If you pay D dollars to play a St. Petersburg lottery, you only “come out ahead” if you win more than D dollars.

In the standard lottery this means you only “win” if you get more than log\_2(D) heads in a row, a situation that happens only with probability less than 1/D.

For the general case, in a lottery where you win some fast\-growing function f(N) if you get N heads in a row, then you only come out ahead after paying D to play if you win f^(\-1\) (D) heads in a row, which happens with probability less than

(0\.5\)^(f^(\-1\)(D)

Which is still a decreasing function in D, that approaches 0 as D becomes large.

This means that, if you “bite the bullet” on St. Petersburg and are willing to pay arbitrary amounts to play, then you are willing to take gambles that you only win in arbitrarily unlikely scenarios.

It’s analogous to the “repeated double\-or\-nothing coin flip” situation, in that you technically maximize expected value by betting all\-in forever, but the scenarios in which you win have probability converging to zero as the number of flips goes to infinity.

A St. Petersburg bullet\-biter, like an all\-in double\-or\-nothing coin\-flipper, is willing to *concentrate* his bets on arbitrarily unlikely win conditions.

It’s important to point out, once again, that this is significantly more extreme than merely taking a calculated risk.

It’s one thing to say you’re willing to accept a gamble with some *particular* low probability of success because the upside is sufficiently high. It’s another thing altogether to say that you’re willing to accept gambles with *arbitrarily low* probabilities of success, if their upside grows sufficiently high.

In the real world, every measurement has bounded precision. At some point, a sufficiently improbable event becomes *de facto* impossible. And that means the “St. Petersburg bullet\-biter” is betting on not just an *unlikely* but an *impossible* win.

It’s analogous to Pascal’s Wager hypothetical scenarios, where a naive expected\-value maximizer will accept an arbitrarily tiny chance of an arbitrarily wonderful scenario (and an almost\-certain bad outcome).

As one commenter [put it](https://elmwealth.com/a-missing-piece-of-the-sbf-puzzle/):

> It seems like SBF was essentially telling anyone who was listening that he’d either wind up with all the money in the world, which he’d then redistribute according to his Effective Altruist principles – or, much more likely, he’d die trying.

### Upshots

What conclusions can we draw from all this?

1. Above\-Kelly betting, or St. Petersburg\-paradox bullet\-biting, or naive dollar expected value maximization at arbitrarily large scales, all imply that you should take bets that are *virtually certain* to lead to ruin, in a strict mathematical sense.
2. Conversely, if you declare that you’ll round down to “probability zero” or “impossible” all events more unlikely than some lower bound, you can freely “maximize expected value” without running into the above absurdities.
3. Some of SBF and Caroline Ellison’s comments suggest that they actually didn’t understand this. SBF seems to not know where the Kelly Criterion comes from, neither of them seem to be aware that “infinite utility” [isn’t a thing](https://plato.stanford.edu/entries/paradox-stpetersburg/#BounUtilFunc) in the Von Neumann\-Morgenstern framework, etc[2](https://sarahconstantin.substack.com/p/why-infinite-coin-flipping-is-bad#footnote-2-85415034).
4. FTX\-fraudsters and their critics alike tend to conflate *ordinary risk\-taking* (where sometimes an unlikely gamble with a high payoff is worth it) with the absurd conclusion of St. Petersburg bullet\-biting. This is dumb. Risk\-taking is fine in general, we should all be regularly trying things that have only 20% chance of success, and none of that requires esoteric extreme beliefs about decision theory or ethics.

[1](https://sarahconstantin.substack.com/p/why-infinite-coin-flipping-is-bad#footnote-anchor-1-85415034)A [much more realistic analysis by Carl Shulman in 2012](https://80000hours.org/2012/01/salary-or-startup-how-do-gooders-can-gain-more-from-risky-careers/) of the tradeoff between “found a startup vs. stay at a software engineering job” finds that the risk\-adjusted expected returns are roughly comparable; if you have an empirically typical level of financial risk aversion and an empirically typical chance of business success, you should be roughly indifferent on monetary grounds between keeping your job and starting a company.

[2](https://sarahconstantin.substack.com/p/why-infinite-coin-flipping-is-bad#footnote-anchor-2-85415034)In his [interview with Tyler Cowen](https://conversationswithtyler.com/episodes/sam-bankman-fried/), SBF does mention that utility theory gets weird when you start to talk about infinities:  

> All this math works really nicely as long as all the numbers are finite. As soon as you say, “What are the odds that there’s a way to be infinitely happy? What if infinite utility is a possibility?” You can figure out what that would do to expected values. Now, all of a sudden, we’re comparing hierarchies of infinity. Linearity breaks down a little bit here. Adding two things together doesn’t work so well. A lot of really nasty things happen when you go to infinite numbers from an expected\-value point of view.
> 
> There are some people who have thought about this. To my knowledge, no one has thought about this and come away feeling good about where they ended. People generally think about this and come away feeling more confused.

But then elsewhere he (explicitly and implicitly) talks as though infinite utilities are fine. This suggests he’s *heard* of the “really nasty” thought experiments involving infinity, but at some point decided to stop worrying about them.