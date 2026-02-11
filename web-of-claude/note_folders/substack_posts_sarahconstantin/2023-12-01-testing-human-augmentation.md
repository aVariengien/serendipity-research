# Testing Human Augmentation

*Upgrading humans needs new methods.*

Published: 2023-12-01
Source: https://sarahconstantin.substack.com/p/testing-human-augmentation

---

[![](https://substackcdn.com/image/fetch/$s_!ip9q!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F101e008a-b58e-47ba-a168-3c9e0e7c6888_1024x1024.png)](https://substackcdn.com/image/fetch/$s_!ip9q!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F101e008a-b58e-47ba-a168-3c9e0e7c6888_1024x1024.png)

Midjourney, “A community of wise compassionate consciousness researchers wearing headband devices.”

Let’s pretend that someday, in the near future, we have a wonderful ultrasound neuromodulation device.

Suppose it can be worn comfortably on the outside of the head, and can aim ultrasound at any millimeter\-scale spot in the brain — possibly several at once. Suppose also that the device can stimulate neurons in the target region(s) to fire more, without damaging brain tissue.

And let’s pretend we’ve done enough experiments to understand what “stimulation” actually means, because that’s currently non\-obvious.

* which neurons within the target region are affected? 

	+ in one study it’s [only the excitatory but not inhibitory neurons](https://sarahconstantin.substack.com/p/transcranial-ultrasound-studies-part#footnote-1-138557609)
* what actually increases? firing rate? spike amplitude?
* how long does the effect of ultrasound stimulation last?
* how does the effect of ultrasound stimulation depend on what else is going on? 

	+ e.g. in somatosensory or visual cortex, “this intervention increases/decreases neuronal response to a subsequent sensory stimulus” is not in general the same as “this intervention generates a response in the absence of a sensory stimulus.”
	
	
		- in fact, *timing* matters. When the motor cortex is stimulated twice, 50\-200 ms apart, [the response to second stimulus is inhibited](https://link.springer.com/article/10.1007/s00221-011-2552-z), in what’s known as Long Interval Intracortical Inhibition (LICI), but if the two stimuli are 2\-5 ms apart, [the response to the second stimulus](https://www.frontiersin.org/articles/10.3389/fnins.2018.00240/full) is enhanced, what’s known as Short Interval Intracortical Facilitation (SICF).
		- so we may find that what ultrasound does to neural firing depends on  *what else* the target region of the brain is being exposed to, during and after ultrasound stimulation (sensory stimuli? motor and mental activities?), *and precisely when*.

But let’s leave all that to the side for now.

Let’s pretend these questions have been largely answered, and in some sense the *physics* and *physiology* of ultrasound neuromodulation have been solved. You can reliably get a compact noninvasive wearable device to deliver the ultrasound to exactly the tissue region you want; and you can temporarily modify neural activity, anywhere in the brain, in a more\-or\-less predictable way.

What’s next?

If you’re ~~boring~~ cautious, you get to work developing a therapy for a neuropsychiatric disorder. We already implant electrodes in people’s brains for medication\-resistant, severe problems like Parkinson’s, epilepsy, depression, and Tourette’s. We know the brain regions to target — the only thing left to do is test whether noninvasive ultrasound stimulation can get the same effects as deep brain stimulation, without the surgery (and brain damage).

Let’s say you’re more ambitious than that, though. What might you do *next* with a magic ultrasound machine?

### Project 1: Experimental Functional Connectivity

If the “physics” and the “local physiology” questions are more\-or\-less answered, the next big question is a “neuroscience” question. “Ok, we know what this device does to *the tissue it stimulates*. What does it do to *the brain*?*”*

If we imagine the magic ultrasound device can target a spot a few millimeters in diameter, then the human brain contains maybe *tens of thousands* of targetable regions.

What happens when you zap one of them with ultrasound?

Let’s say, by stipulation, that you get some kind of “activating” effect on neural firing in the target region. (Is that effect consistent across the brain? We don’t know, you’d have to find out!)

One thing we *don’t* know is what happens to activity *everywhere else* in the brain.

You’d expect brain activity to maybe be affected in “downstream” regions of the brain that are connected to the target region, either by myelinated white matter tracts (rapid, long\-range connections) or by polysynaptic pathways (slower, more indirect chains of gray matter neurons.)

You could *go look* at what happens to brain activity throughout the brain when you stimulate one location with ultrasound, and see if the empirical correlations (aka “functional connectivity”) match up with known anatomical connections (aka “structural connectivity.”)

(If you want to check out the current state of our knowledge of both kinds of connectivity, the [Human Brain Atlas](https://www.ebrains.eu/about)  project has a cool [interactive brain viewer](https://atlases.ebrains.eu/viewer).)

Measuring functional connectivity, with tools like fMRI that measure real\-time local changes in blood flow, has been a thing for a while — you *observe* the brain of people “at rest” in the fMRI machine and see which regions’ activities correlate.

The bad news is that these measurements of functional connectivity don’t correlate very well even between repeated tests of the same individual, and lots of regions are functionally but not structurally connected.[1](https://sarahconstantin.substack.com/p/testing-human-augmentation#footnote-1-139338101)

But the good news is that we can learn things from fMRI correlational studies. For instance, left and right copies of most brain regions tend to have correlated activity; and people with neurological or psychiatric illnesses often have detectable abnormalities in their functional connectivity patterns.[2](https://sarahconstantin.substack.com/p/testing-human-augmentation#footnote-2-139338101)

What we can’t learn from purely correlational studies is *causality.* When you perturb part of the brain, what else gets perturbed, and how?

We know something about this in *some* parts of the brain thanks to rTMS studies — stimulating or inhibiting a part of the cortex with magnetism leads to changes not only in the stimulated region but also in distant brain regions.[3](https://sarahconstantin.substack.com/p/testing-human-augmentation#footnote-3-139338101)

For instance, use rTMS to stimulate the left motor cortex and you’ll get increased activity there and in an adjacent brain region, but *decreased* activity in the corresponding regions on the other side of the head.

Interestingly, most rTMS studies find that it *changes* functional connectivity, relative to sham stimulation. (That is, the effects of using rTMS on part of the brain aren’t exactly what you would have predicted from a resting\-state functional connectivity map in unstimulated subjects.)

What happens to functional connectivity if you use ultrasound to stimulate the places that rTMS can’t reach? Do ultrasound’s distal effects match up well to the effects of rTMS or deep brain stimulation? The first ultrasound studies are starting to find nice predictable results like “stimulating the amygdala with ultrasound increases blood flow to the amygdala and to other known functionally\-connected regions”[4](https://sarahconstantin.substack.com/p/testing-human-augmentation#footnote-4-139338101) but I don’t think we have a full “map” yet.

Why should we care? Because when you’re stimulating “a brain region” you’re really stimulating a whole network of connected brain regions.

If we’re trying to search through “all” the possible brain stimulation possibilities to find beneficial ones, that’s a colossal undertaking. We might hope to cut down on the complexity somewhat if there are natural “networks” where *any* stimulation technique/location that activates the network can be expected to have somewhat similar effects.

For example, we already know that when multiple brain regions are effective “targets” for deep brain stimulation as therapy for a condition (like OCD or depression), those regions are often part of a functionally connected network.[5](https://sarahconstantin.substack.com/p/testing-human-augmentation#footnote-5-139338101)

### Project 2: Developing A Community of Practice

On a higher level than the “neuroscience” question (“what does ultrasound neuromodulation do to the brain?”) is the “psychology” question. What does ultrasound neuromodulation do to the *mind*? What can it do to our *abilities and experiences*?

And before we can really answer that question, we’ll probably need better ways to ask it in the first place.

The traditional way to test any psychological or psychiatric intervention on humans is to run a controlled study where the outcome is a *test*.

If you’re testing an intervention’s effect on depression, you might give subjects a questionnaire like the [HAM\-D.](https://dcf.psychiatry.ufl.edu/files/2011/05/HAMILTON-DEPRESSION.pdf)  If you’re testing an intervention’s effect on cognition, you might give a cognitive test, like [n\-back tasks](https://en.wikipedia.org/wiki/N-back) for working memory.

Standardized tasks and questionnaires have the advantage of being consistent and replicatable. Every subject is given the same measurement instrument; other researchers can try the same experiment and see if they get the same result; the measurement instrument is, ideally, objective enough that it isn’t swayed much by experimenter bias.

The downside is that this is a *terrible* way to search for “what sorts of brain stimulation do something cool?”

To run an experiment with a standard measured outcome, you have to know what outcome you want to measure!

If you, say, try stimulating the dorsolateral prefrontal cortex, and you want to know if it does something “good” for emotions or cognition, and you pick a battery of tests and get no result, that could just mean you didn’t pick a test that captures the effect of the stimulation.

On the flip side, a lot of cognitive and emotional tests lack “ecological validity”, which is to say they don’t mean a damn thing.

Is a test that measures how undergraduates make decisions on a gambling task, using comically small amounts of money, really a test of their “risk aversion” or “impulse control” in any meaningful sense?

Is a test of how blood flow in emotion\-related regions of the brain changes when pictures of sad faces are displayed, really a test of “emotional regulation”?

Surely not! Yet these are the kinds of measures studies use when they look for cognitive\-emotional effects on healthy subjects!

This is clearly the wrong place to *start* when asking “can you get any interesting or beneficial effects from noninvasive brain stimulation on healthy subjects?”

To go in a totally different direction, when Alexander Shulgin wanted to ask "do any of these new psychoactive compounds I’ve synthesized have interesting or beneficial effects?” he didn’t start by running controlled trials on undergrads and giving them cognitive tests. He did the common\-sense thing, described in this [1986 “protocol”:](https://chemistry.mdma.ch/hiveboard/rhodium/shulgin.evaluation.protocol.html)

* start with self\-experimentation by the researchers, beginning with extremely low doses (10\-50x lower than the “active dose” of the closest known homolog) and titrating up gradually
* write down a subjective description of the experience, including a “numerical rating scale” of its “intensity”
* only then move to a “clinical evaluation” on 12 volunteers, but *not* blinded, and usually experienced in such self\-experimentation. They interact together, naturally, in a home environment, trying out different activities such as talking or listening to music, to see how the drug experience affects them.

Obviously such a protocol is much more subjective than a battery of cognitive\-psychological tests, but that’s fine for a starting point in a *search* for meaningful effects.

If you’re asking “is this compound a psychedelic or not? And if so, what’s it like?” you can answer that question much faster, cheaper, in richer detail, and more ethically by getting a handful of experienced volunteers to try it and take notes than by running anything resembling a “clinical trial.”

Later, of course, it’s perfectly possible to run [clinical trials of MDMA\-assisted therapy for PTSD](https://www.nature.com/articles/s41591-023-02565-4), but nobody would have ever generated the hypothesis behind those trials in the first place without a much more informal history of therapeutic and recreational use.

Analogously, if a tentatively\-safe neuromodulatory device is created and we want to search for potentially interesting or useful cognitive\-psychological effects, it makes much more sense to have a *community of self\-experimentation* where the goal is just to see “can we feel an effect? does it seem to affect how we think and feel? what happens when we try various activities in this altered state?”

Once common sense says “clearly this stimulation protocol Does A Thing, and we’re intrigued”, *then* it makes sense to test and measure the effects, including on research subjects outside your community bubble, to correct for bias and groupthink.

Requirements/desiderata for a community of practice around neuromodulation:

* You need to first have a reliable device and a reasonable degree of confidence that it won’t cause acute brain injury.

	+ since we’re not really there yet on ultrasound, it may make sense to start building the self\-experimentation practices around a less\-powerful but better\-characterized technology like tDCS, which I’d guess has no “real” effects but is safe enough that it’s sold as a consumer product.
* You want as much domain expertise as possible in your founding research group — medicine, neuroscience, psychology, etc.
* Ideally you’d also want people who are highly sensitive and articulate about their perceptual, mental, emotional and intersubjective experiences. Artists, meditators, athletes, therapists — people who’d be able to spontaneously notice subtle things like “I’m able to discuss sensitive topics with less defensiveness” or “My peripheral vision has gotten better” or “I find myself focusing totally on the present moment”.
* You might want quantitative measurement modalities (fMRI, EEG, heart rate monitors, etc) but of course there’s a tradeoff between what you can measure in a lab on immobilized isolated subjects and what you can bring to a “realistic” environment like a home (where people can move around, interact with each other, etc.)
* And you’d want to work towards developing an (initially informal) collection of things to try, “experiments” to run, aiming primarily for common\-sense validity and helpfulness. You don’t need a questionnaire or rating scale to tell that caffeine makes you feel more alert — but you might want to actually measure reaction time rather than trusting your subjective impression that you’re “faster.”

The main goal here is not to substitute informal trial\-and\-error for “real science” but to use it to *generate hypotheses that are worth testing more rigorously*.

Otherwise you wind up with a research field that wastes time and money running highly formalized experiments on interventions that *nobody has any reason to believe will do anything useful at all*.

Of course, informal self\-experimentation is controversial, and may not fit into standard research/funding models, but it really seems necessary for such an open\-ended search.

[1](https://sarahconstantin.substack.com/p/testing-human-augmentation#footnote-anchor-1-139338101)Honey, Christopher J., et al. "Predicting human resting\-state functional connectivity from structural connectivity." *Proceedings of the National Academy of Sciences* 106\.6 (2009\): 2035\-2040\.

[2](https://sarahconstantin.substack.com/p/testing-human-augmentation#footnote-anchor-2-139338101)Fox, Michael D., et al. "Measuring and manipulating brain connectivity with resting state functional connectivity magnetic resonance imaging (fcMRI) and transcranial magnetic stimulation (TMS)." *Neuroimage* 62\.4 (2012\): 2232\-2243\.

[3](https://sarahconstantin.substack.com/p/testing-human-augmentation#footnote-anchor-3-139338101)Seewoo, Bhedita J., et al. "Combined rTMS/fMRI studies: An overlooked resource in animal models." *Frontiers in Neuroscience* 12 (2018\): 180\.

[4](https://sarahconstantin.substack.com/p/testing-human-augmentation#footnote-anchor-4-139338101)Kuhn, Taylor, et al. "Transcranial focused ultrasound selectively increases perfusion and modulates functional connectivity of deep brain regions in humans." *Frontiers in Neural Circuits* 17 (2023\): 1120410\.

[5](https://sarahconstantin.substack.com/p/testing-human-augmentation#footnote-anchor-5-139338101)Horn, Andreas, and Michael D. Fox. "Opportunities of connectomic neuromodulation." *Neuroimage* 221 (2020\): 117180\.