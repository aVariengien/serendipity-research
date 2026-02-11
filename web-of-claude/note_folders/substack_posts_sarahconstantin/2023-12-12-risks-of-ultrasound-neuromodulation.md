# Risks of Ultrasound Neuromodulation

*What could go wrong?*

Published: 2023-12-12
Source: https://sarahconstantin.substack.com/p/risks-of-ultrasound-neuromodulation

---

[![Image from Midjourney](https://substackcdn.com/image/fetch/$s_!PVy8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fad6c4e30-7db2-4c91-a540-927ad52e1384_1024x1024.png "Image from Midjourney")](https://substackcdn.com/image/fetch/$s_!PVy8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fad6c4e30-7db2-4c91-a540-927ad52e1384_1024x1024.png)

Image from Midjourney

What kinds of risks and dangers could arise from ultrasound neuromodulation on humans?

What risks do we know are possible now, what risks could plausibly arise as the technology improves, and what risks are generally implausible?

### Tissue Damage Risks

One category of thing that could go wrong with ultrasound neuromodulation is *direct damage to the brain region being stimulated*.

You can certainly kill cells by directing enough ultrasound energy to them that they heat up — in fact, high\-energy ultrasound does this deliberately, as a way of destroying brain tumors.

However, this seems unlikely at the low doses of ultrasound that are being used for transcranial low\-intensity focused ultrasound neuromodulation.

In the [79 studies I assembled](https://docs.google.com/spreadsheets/d/1gdOYzrDowsPLM06RazasDJtusieeqK3-/edit#gid=187669938), no study directed more than 80 W/cm^3 to its target area.

Now, *diagnostic* ultrasound medical imaging of the brain is already a thing, and the FDA’s upper safety limit for cranial ultrasound intensity is 190 W/cm^3 — more than double the dose seen in even the highest\-intensity study.

Moreover, many animal studies on transcranial focused ultrasound include pathology studies of brain tissue samples (after the animals are killed) and these reliably detect no microscopically\-visible changes to the targeted regions.

And in some animal studies direct temperature measurements have been performed, confirming that no more than 0\.1 degree C of heating occurs with the relevant doses of low\-intensity focused ultrasound.

It seems unlikely that effective doses of low\-intensity focused transcranial ultrasound will damage the targeted brain tissue, either through thermal or mechanical mechanisms.

### Blood\-Brain Barrier Opening Risks

Another category of risk involves the effects of transcranial ultrasound on opening the blood\-brain barrier.

The capillaries that carry blood throughout the brain are lined with endothelial cells that prevent most chemicals from passing between the blood and the brain. This is the so\-called “blood\-brain barrier.”

Transcranial ultrasound can open the blood\-brain barrier, making it more permeable. Sometimes this is an intentional therapeutic application, to allow drugs to enter the brain better. As a side effect, however, it could be dangerous.

A more permeable blood\-brain barrier could allow toxins, pathogens, and inflammatory immune cells to enter the brain. This could lead to brain infections (like encephalitis and meningitis), autoimmune disorders (like multiple sclerosis), and neurotoxicity from other drugs.

The blood\-brain barrier becomes more permeable as people age, and some theories of the origins of neurodegenerative disorders like Alzheimer’s and Parkinson’s say that they’re caused or exacerbated by blood\-brain\-barrier disruption; a more permeable blood\-brain barrier leads to neuroinflammation and/or entry of misfolded proteins into the brain, causing toxic damage to brain cells.

In other words, *yes*, we should worry that increasing blood\-brain barrier permeability could cause harmful side effects. Your BBB is there for a reason; you do not want to lose it.

There are two points of good news.

1. We can test for BBB opening directly, by injecting a contrast agent into the bloodstream and using an MRI or CT scan to see how much of it gets into the brain.
2. The sonication parameters for BBB\-disrupting ultrasound seem to be a bit different from the optimal ones for neuromodulation. In this [review article](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7080303/), out of 21 studies showing transcranial ultrasound opening the blood\-brain barrier, all of them had pulse repetition frequencies (PRF) of 1\-10 Hz, while neuromodulatory ultrasound [tends to have much faster pulses,](https://docs.google.com/spreadsheets/d/1gdOYzrDowsPLM06RazasDJtusieeqK3-/edit#gid=187669938) more like 100\-3000 Hz.

So there’s reason to hope that the ultrasound parameters that are good for affecting neural activity do *not* cause much BBB disruption.

But we’d have to test that. In general, studies of ultrasound neuromodulation do *not* test to confirm that the BBB is unaffected; someone needs to go check that.

### Neuromodulation Risks

Another category of risk is that the *neuromodulation itself* is harmful.

In other words: the intended purpose of ultrasound neuromodulation is to cause increased neural activity in a targeted region of the brain. What if increasing neural activity in that brain region is, in itself, dangerous?

What’s the *worst thing you could possibly do* with a magic button that turns up neural activity somewhere in the brain?

Well, you could do lots of nasty things.

#### Seizures

A seizure, for instance, is simply excessive and uncoordinated neural firing in part of the brain. Any neurostimulation device that works at all could in principle cause a seizure.

#### Autonomic Disruption

*Autonomic processes* like heart rate, blood pressure, breathing, digestion, body temperature, metabolic regulation (hunger, thirst, energy level), stress response (adrenaline and cortisol), sexual arousal, and urination are controlled by the brain, in regions including the hypothalamus and brainstem.

Messing up autonomic processes can be fatal. You do not want to turn off your heart.

We [already know from the literature on deep brain stimulation](https://www.kringelbach.org/papers/nrn_Hyam2012.pdf) that autonomic side effects are possible (in humans) from electrodes implanted in the brain, such as:

* asystole (the heart stops beating entirely!)
* increases and decreases in blood pressure
* increases and decreases in respiratory rate
* changes in sweating
* urinary incontinence

If electrode stimulation can cause autonomic disruption, then logically, so can transcranial ultrasound.

Most of these autonomic regions are deep in the brain, so other noninvasive neuromodulation techniques (like rTMS) physically cannot reach them. But ultrasound, in principle, can.

For some disease applications, you might actually want to create autonomic effects via neuromodulation — targeting the brainstem may be helpful for chronic pain, for instance — but these are high\-risk areas of the brain, and it’s probably better to do animal studies first.[1](https://sarahconstantin.substack.com/p/risks-of-ultrasound-neuromodulation#footnote-1-139704822)

#### Addiction and Psychiatric Disorders

When you mess around with deep brain structures related to emotion and motivation, you can, of course, do bad things to emotion and motivation.

“[Wireheading](https://en.wikipedia.org/wiki/Wirehead_(science_fiction)#:~:text=Wireheading%20is%20a%20term%20associated,process%20and%20artificially%20inducing%20pleasure.)” — a term popularized by science\-fiction writer Larry Niven — is a reference to the very real addictive potential of electrode stimulation of the septal area and posterior hypothalamus in rats, [first observed in 1954](https://psycnet.apa.org/record/1955-06866-001). Stimulating these regions is *highly* motivating to animals — 6 out of 10 of the [posterior\-hypothalamus\-stimulated rats](https://psycnet.apa.org/record/1965-14558-001) ignored food, pressing the lever to stimulate the electrode repeatedly until they died of starvation.

We also know that deep brain stimulation in humans can produce subjective effects of euphoria or a “high”. Humans stimulated in the septal area can have [orgasms.](https://thejns.org/focus/view/journals/neurosurg-focus/29/2/2010.4.focus10106.xml?tab_body=fulltext)

Since these deep brain areas are accessible to noninvasive ultrasound stimulation, it is quite plausibly possible for ultrasound to create a highly addictive pleasurable effect.

We also have data on [psychiatric side effects of deep brain stimulation](https://d1wqtxts1xzle7.cloudfront.net/51435803/Psychiatric_and_neuropsychiatric_adverse20170119-10037-oycxcw-libre.pdf?1484885037=&response-content-disposition=inline%3B+filename%3DPsychiatric_and_Neuropsychiatric_Adverse.pdf&Expires=1702340150&Signature=X9OISH2m6aMHVk0h245ACVcVYuWu7syf~W6IZog9U0VohZcpQIYz-YKcwrPKdyyZ3Q0rmUQntr0nzajfU25ovUqE6pWr9dYYgOiVRQpITAyPgxwtgVHCgvIS4bbap1YwLUy9~QxD~4CuiqGLTeyejHSAWetVTneizX4qbvVZ6rpj8F644rbqE54IJLQyvJKg9601Ut34IFOtmVT9DWOssrFhLo9-wiqZRpgIf6TjMqFnknFXujIteLkrBOnwmB5HfZic7ZNAS9apfIFL4jXPPPZqiKgClq1XoHjABnyDzoKJUlFbJeeSaCYSkiz3YhJHET7S54YSIjRQbShN4MTKLg__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA), mostly for motor disorders, where depression, mania, and psychosis have been observed.

We know it’s possible to induce negativeemotions with brain stimulation as well — stimulating the periaqueductal gray produces intense fear, for instance.

It seems entirely plausible that, depending on where and how stimulation occurs, that it’s possible to induce psychiatric or emotional problems with ultrasound.

#### Cognitive, Sensory, and Motor Impairments

If you can *alter* cognition, sensory perception, and motion, then you can clearly *impair* it. Most possible changes to the brain are detriments, not improvements.

In fact there’s a large literature on rTMS as a “[virtual lesion](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6728008/)” — by temporarily suppressing neural activity in a region via magnetic stimulation, you can see how the brain functions without that region. You can impair a lot of functions this way. (What happens if you turn “down” your frontal lobes? Worse performance on lots of tests!)

Ultrasound neuromodulation seems to turn “up” activity in regions of the brain, rather than “down”, but you’d expect that to be able to impair function as well.

(And we don’t have enough long\-term data to know how transient the effect is.)

The most common side effects of brain stimulation for movement disorders are problems with [gait and speech,](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6728008/)  which occur in more than half of patients. Screwing up cognitive and motor skills is a known risk of brain stimulation.

### Malicious Use

Most of the things that can go wrong with ultrasound neuromodulation are, basically, accidents — a bad stimulation device or parameter setting could unintentionally impair, injure, or kill someone.

But what people usually ask about first is malicious use.

Could these devices be used for something like mind control? Could they be made into some kind of weapon?

This goes into a more speculative realm, but I think these concerns are somewhat overblown.

You *can*, most likely, kill someone with an ultrasound device. You can also kill someone with a gun — much more cheaply. An ultrasound device has no *advantages* as a weapon.

Could someone, in principle, hack into an ultrasound device and change its settings to ones that harm the wearer, allowing for some kind of “remote\-control attack”? As I understand, that is possible in principle — but it is equally possible to do that with any potentially\-dangerous electronic device, including cardiac pacemakers and cars. Since this doesn’t seem to be a known sort of crime, I have to assume that there’s either not many people attempting murder\-via\-cyberattack or there exist adequate security measures to prevent it.

The other malicious\-actor scenario is one in which, someday, neuromodulation devices are sold commercially, and the manufacturers intentionally introduce some settings that harm the users.

These harms would have to be subtle, because there are legal and economic disincentives from *obviously* hurting your users.

But it might take a while to detect that a seemingly\-helpful device was also, say, addictive. Or produced a mental state that made people more suggestible or gullible or impulsive. And there might be economic incentives for device\-makers to introduce these kinds of subtle harms.

Literal mind control doesn’t seem like a realistic possibility for the foreseeable future. We simply don’t understand the brain well enough to implant specific thoughts. We don’t even know if that’s physically possible with the parameters of ultrasound.

Likewise, while we know ultrasound stimulation can create sensory perceptions (like seeing a bright light) or motor responses (like muscle twitches), it’s not clear if it’ll ever be possible to induce a hallucination of a specific desired image, or puppet someone’s motions remotely in any way useful to the puppeteer.

Someone who wanted to manipulate behavior using ultrasound could very likely cause grossly altered mental states (different mood, impaired judgment, impulsivity, altered motivations), but it’s not clear how fine\-grained the control could be.

Of course, *harming* someone with such manipulation would already be covered under current law, and the courts would probably view harms from a new technology more harshly than they would the analogous harms to cognition and mental health from, say, alcohol manufacturers.

While misuse is a possibility, I think it makes a lot more sense to intitially focus on *accidental* risks — it is much, much easier (especially in the short term) for ultrasound neuromodulation to unintentionally go wrong in early experiments, than it is for a bad actor to “get their hands on it” and do a lot of harm to many people intentionally. And most of what we learn about accidental risks in the course of research would transfer well to understanding the risks of misuse.

[1](https://sarahconstantin.substack.com/p/risks-of-ultrasound-neuromodulation#footnote-anchor-1-139704822)I, for one, am *deeply* curious about long\-term hypothalamic stimulation for metabolism and aging. You can alter [glucose and insulin responses](https://journals.physiology.org/doi/abs/10.1152/ajplegacy.1971.221.6.1596?journalCode=ajplegacy) by stimulating the hypothalamus; hypothalamic stimulation can decrease appetite and body fat in [monkeys](https://www.nature.com/articles/ijo2011271) and [pigs](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0030672); hypothalamic stimulation can [induce ovulation](https://journals.sagepub.com/doi/abs/10.3181/00379727-132-34260) in old female rats; and then there’s weird stuff like a [guy treated with hypothalamic stimulation for his morbid obesity](https://onlinelibrary.wiley.com/doi/abs/10.1002/ana.21295), who also…went from a 125 to 134 IQ, and improved on a bunch of memory tests?! 

But this is mucking about with the body’s fundamental control system for *all hormones and metabolism*, and it is obviously possible to do a lot of damage this way. Do not zap your hypothalamus lightly.