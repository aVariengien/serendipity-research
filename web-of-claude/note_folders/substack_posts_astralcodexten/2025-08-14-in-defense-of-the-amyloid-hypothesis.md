# In Defense Of The Amyloid Hypothesis

*A guest post by David Schneider-Joseph*

Published: 2025-08-14
Source: https://www.astralcodexten.com/p/in-defense-of-the-amyloid-hypothesis

---

The “amyloid hypothesis” says that Alzheimer’s is caused by accumulation of the peptide amyloid\-β. It’s the leading model in academia, but a favorite target for science journalists, contrarian bloggers, and neuroscience public intellectuals, who point out problems like:

* Some of the research establishing amyloid's role turned out to be fraudulent.
* The level of amyloid in the brain doesn’t correlate very well with the level of cognitive impairment across Alzheimer’s patients.
* Several strains of mice that were genetically programmed to have extra amyloid did eventually develop cognitive impairments. But it took much higher amyloid levels than humans have, and on further investigation the impairments didn't really look like Alzheimer’s.
* Some infectious agents, like the gingivitis bacterium and the herpesviruses, seem to play a role in at least some Alzheimer’s cases.
* . . . and amyloid is one of the body's responses to injury or infection, so it might be a harmless byproduct of these infections or whatever else the real disease is.
* Anti\-amyloid drugs (like [Aduhelm](https://healthjournalism.org/blog/2024/02/adieu-aduhelm-biogen-pulls-plug-on-controversial-alzheimers-drug/)) don't reverse the disease, and only slow progression a relatively small amount.

Opponents call the amyloid hypothesis zombie science, propped up only by pharmaceutical companies hoping to sell off a few more anti\-amyloid me\-too drugs before it collapses. Meanwhile, mainstream scientists . . . continue to believe it without really offering any public defense. Scott was so surprised by the size of the gap between official and unofficial opinion that he asked if someone from the orthodox camp would speak out in its favor.

I am [David Schneider\-Joseph](https://thedavidsj.substack.com/), an engineer formerly with SpaceX and Google, now working in AI safety. Alzheimer’s isn’t my field, but I got very interested in it, spent six months studying the literature, and came away believing the amyloid hypothesis was basically completely solid. I thought I’d share that understanding with current skeptics.

## The ATN model

The most plausible variant of the amyloid hypothesis is the A → T → N model: amyloid causes tau causes neurodegeneration.

#### 1: Amyloid

The common entrypoint, typically at least 15 years before clinically detectable symptoms \[1], is accumulation of amyloid\-β deposits (especially Aβ42, one of several variants).

Amyloid\-β is a peptide produced in healthy human beings and many other animals, probably for antimicrobial purposes \[2, 3].

Factors which cause overproduction of amyloid also cause Alzheimer’s. Factors that cause decreased clearance of amyloid also cause Alzheimer’s. The clearest relationship is various genes which massively increase amyloid production (while doing nothing else); these genes are Alzheimer’s risk factors, with some of the rarer and more severe ones causing extreme versions of the disease that manifest at otherwise almost\-never\-seen ages.

One of the clearest examples is Down syndrome, which is caused by three (rather than the usual two) copies of chromosome 21\. People with Down syndrome are at much higher risk of Alzheimer’s than the general population: two\-thirds will have the condition by age sixty, and 15% have it by age *forty.*

APP, the gene for the amyloid precursor protein, is on chromosome 21\. This means that people with Down syndrome will have an extra copy. This extra copy has been observed to lead to higher\-than\-normal amyloid levels. But there are many genes on chromosome 21; do we have additional evidence that it’s the amyloid one that’s involved?

Yes. Dozens of other mutations on APP cause the same sort of extremely young and severe Alzheimer’s. So do mutations on PSEN1 and 2, the genes for the enzyme that processes amyloid precursor protein into amyloid. So do mutations on several other amyloid\-related genes. \[6, 91 \- 96] Researchers call these *autosomal\-dominant* Alzheimer’s, meaning Alzheimer’s cases that get inherited from a single parent in a simple fashion typical of single\-gene disorders. They make up about 1% of all cases, and are our strongest evidence for the causal role of amyloid in the disorder. To my knowledge, there is no serious claim that these genes could be working through any pathway other than their shared role in the amyloid system.

But these autosomal\-dominant cases only make up about 1% of all Alzheimer’s patients. Might they be a different disease than the usual sporadic Alzheimer’s that strikes people without strong family histories at normal ages?

Probably not: the presentation and trajectory of autosomal\-dominant and sporadic Alzheimer’s cases are strikingly similar. Both show an initial appearance of amyloid pathology starting in intrinsic connectivity networks in both autosomal\-dominant \[14] and sporadic \[15–18] types, cortical tau appearing first in the medial temporal lobe and with the exact same fold in both disease types \[97] (despite human tauopathies having at least seven other possible characteristic folds \[36]), that tau pathology worsening and spreading outside this region only once amyloid pathology reaches sufficient severity \[65], neurodegeneration progressing closely in step with the tau pathology, and the same usual approximate trajectory of cognitive symptoms due to the sequence of affected regions. So it’s as if two bank robberies occurred hours apart, in the same town, and in a highly similar and idiosyncratic manner, and we can positively identify the culprit of one on security camera footage. It’s a good bet the culprit of the other is the same.

Increased amyloid production → Alzheimer’s is an especially clear and simple pathway, but any other change in amyloid can also cause the disease. For example

* **Overproduction or reduced clearance of amyloid due to impaired slow wave sleep**. Aβ production is neuronal activity\-dependent, and toxins (perhaps including Aβ) are cleared from the brain during sleep via the glymphatic system. Thus Aβ can accumulate if the brain is more active and/or has less opportunity for clearance. \[7, 8, 9, 10, 11]
* **Impaired amyloid clearance due to having one or (much worse) two copies of ApoE4** \[12], which is by far the most common genetic risk factor. The mechanism here may be a loss of function in microglia, a type of immune cell in the brain which helps clear plaques. \[13]
* **Overproduction or reduced clearance due to microbial infection.** Amyloid\-β appears to be an antimicrobial peptide and will form plaques in response to infection. \[2, 3] This explains various observations that have been used to support the “infectious hypothesis”, sometimes proposed as an alternative to the amyloid hypothesis. However, it can only explain a subset of cases and, as I argue [below](https://docs.google.com/document/d/130cgtEEwnwPStrsmOFEIOAZk1wq_siFNAKIMhWdvMuM/edit#bookmark=id.ptfizr39bkt3), is even then still *mediated* by amyloid via an “IATN” pathway: infection → amyloid → tau → neurodegeneration.

In cases of increased production, cerebrospinal fluid (CSF) will show elevated amyloid. In cases of reduced clearance, amyloid will *decrease* in CSF. In all cases, however, PET scans will show elevated brain amyloid, usually at first mainly in “intrinsic connectivity networks” such as the default mode network \[14–20], which experience brain activity even at rest. These neurons are the most active \- which causes more production and possibly less opportunity for clearance \- so they tend to be the first to suffer from a production/clearance imbalance.

Over time, amyloid pathology spreads spatially throughout the brain. \[14, 18] Aggregations of amyloid peptides induce more such aggregations. Some of our clearest evidence for this comes from growth hormone deficiency patients, who used to have cadaver\-derived ground\-up brain matter injected into their own brains to provide the missing hormones. If the ground\-up brain matter was sourced from the corpse of an Alzheimer’s patient, the growth hormone deficiency patients would themselves develop Alzheimer’s at a young age, [probably through prion\-like spread of the misfolded proteins](https://www.gwasstories.com/p/the-first-case-reports-of-human-to). \[21, 22]

After ∼15 years of preclinical spread, the pathology eventually covers the whole brain. \[14, 18] While some subtle cognitive impairment may occur during this time, it is usually not severe enough to be clinically detectable from amyloid alone. Indeed, in both humans \[23–30] and mice \[31–35], the severity of neurodegeneration and cognitive deficits is not a good spatiotemporal match for the severity of amyloid pathology (rather, it is a good match for the severity of tau pathology; see next section for more). These facts are often suggested as evidence against the amyloid hypothesis. However, amyloid is causally upstream of tau, as I will argue below. Therefore, the existence of cognitively normal individuals with amyloid pathology is expected in the ATN model \- but typically only for a few decades, before progression to the next stage.

#### 2: Tau pathology (T) and neurodegeneration (N)

*Tauopathies* are a range of prion\-like diseases involving the tau protein \[36], whose usual function is to assist in stabilizing microtubule structure. In a tauopathy, the tau protein misfolds, and induces other, nearby tau proteins to misfold into the same shape. \[37–46]. Injecting nothing but misfolded tau fibrils into a mouse brain can recruit the endogenously\-produced mouse tau into this pathology, which spreads far beyond the injection site, causing neurodegeneration wherever it goes. \[35, 47–59]

There are at least eight distinct ways the tau protein can misfold in human disease \[36], and over a dozen distinct human tauopathies, each involving a specific one of those misfoldings. These include chronic traumatic encephalopathy, Pick’s disease, corticobasal degeneration, progressive supranuclear palsy, and Alzheimer’s disease, with the last by far the most common. Each of these five diseases has its own distinct tau fold.

Most normal human beings eventually develop some tau pathology in adulthood, originating probably in the locus coeruleus \[60–62], which is part of the brainstem. By middle age, some amount has usually spread to the hippocampus and entorhinal cortex in the medial temporal lobe, regions responsible for episodic memory. This is called primary age\-related tauopathy (PART) \[63], and has its own tau fold which is distinct from most tauopathies, but the same as Alzheimer’s. \[36, 64] Usually, its local severity is mild and it doesn’t spread much beyond those regions. But with sufficient amyloid pathology, this “normal” tau pathology tends to both locally worsen and spread through the rest of the brain \[65], becoming the tau pathology of Alzheimer’s.

Some genetic risk factors such as ApoE, in addition to affecting the clearance of amyloid\-β, also increase the brain’s susceptibility to this A → T pathology conversion \[66, 67]. But this is a matter of degree, as *sufficient* amyloid pathology seems to virtually guarantee the transition: Every [10\-centiloid](https://www.gaain.org/centiloid-project) increase in amyloid pathology for a cognitively normal individual increases by 2\.7x the probability of a PET scan detecting pathological levels of tau within five years \[68]. The only known cases where patients with extremely high amyloid levels can go significant amounts of time without developing tau pathology are a few individuals with extremely rare protective genes, known only from a few case studies, e.g. \[69]. Even in these instances, the individuals will eventually succumb to the tau phase, suffering neural atrophy and dementia. \[70]

After it forms, the tau pathology no longer appears to require amyloid’s assistance to keep spreading (although amyloid may still accelerate it). This probably explains why existing anti\-amyloid therapies [have been](https://docs.google.com/document/d/130cgtEEwnwPStrsmOFEIOAZk1wq_siFNAKIMhWdvMuM/edit#bookmark=id.ihc42bbb5bpo) only ∼30% effective in test patients, who are usually late in the amyloid → tau progression even if early in having symptomatic disease.

Neurodegeneration follows tau pathology extremely closely in time and space, in humans as well as basically all animal models, and cognitive impairments match the functions of the affected regions. There are rare reports of advanced tau pathology without cognitive decline, often in people with protective ApoE2 alleles \[71], but even then, systematic analysis finds that actual density of tau inclusions is highly predictive of cognitive impairment, and that these exceptional cases usually involve widespread but *locally sparse* pathology \[66].

The regional distribution of tau pathology explains why the first symptom of Alzheimer’s is typically impaired memory; the first cortical sites affected are usually in regions involved in memory formation. As the pathology spreads, further regions are affected, until eventually all cognitive functions are affected. As with most other aspects of the disease, the high\-level picture seems relatively clear but the exact cellular and molecular pathways are not well understood (though may involve an assist from the innate immune system, especially microglia and astrocytes. \[13, 35, 72])

Early Alzheimer mouse models were amyloid\-only, with extremely heavy overproduction of Aβ, much more than required to recapitulate the human disease, and apparently enough to cause detectable cognitive dysfunction. However, normal mice do not get age\-related tauopathy, so an amyloid\-only mouse model \- while useful for investigating certain questions \- is not a full Alzheimer’s disease model.

Combined amyloid\+tau pathology mouse models, which are transgenically modified and/or injected with misfolded human tau fibrils, display the property that [the presence of amyloid pathology induces the worsening and spreading of tau pathology](https://docs.google.com/document/d/130cgtEEwnwPStrsmOFEIOAZk1wq_siFNAKIMhWdvMuM/edit#bookmark=id.pw1ydynatz5u). This is also observed *in vitro* in human cells.

How do we know the amyloid causes the tau? Researchers have measured the correlation in many ways, from the spatiotemporal timeline (tau pathology only begins locally worsening and spreading outside the medial temporal lobe once amyloid reaches sufficient severity) \[65], \[98], to causal mediation modeling in the human disease \[26], \[99–101], to causal intervention using in vitro human cell studies \[54, 102] and animal models \[35, 55], \[103 – 113]. But also, giving people drugs that reduce amyloid levels also decreases tau pathology. \[78, 80, 82]

(I’ve left out or merely alluded to much other complexity, involving the innate immune system, lipid processing, and detailed molecular and cellular mechanisms, preferring to focus on the parts of the story which are crucial to deciding the causal role of amyloid, and for which I am aware of a satisfactory account from the literature. But I don’t intend to leave the impression that the above is all there is to Alzheimer’s disease, or that all cases progress in the same exact way.)

## The mechanistic claims

I make the following two claims about amyloid\-β’s role in Alzheimer’s:

1. Amyloid deposits are a necessary (i.e. but\-for) cause in all instances of Alzheimer dementia. That is, **if** someone has PET or CSF positivity for amyloid and tau pathologies, *and* the tau pathology involves the Alzheimer tau fold and made its first cortical appearance in the medial temporal lobe, *and* then they developed medial temporal volume loss \+ amnestic mild cognitive impairment \+ later dementia, **then counterfactually,** early enough (probably ∼15 years before clinical presentation) causal intervention solely to remove the amyloid deposits would have prevented almost all tau pathology and symptoms.
2. Severe enough amyloid pathology is a sufficient cause of Alzheimer dementia in almost all brains. That is, **if** someone is PET\- or CSF\-positive for very severe amyloid pathology (such as the level resulting from typical cases of autosomal\-dominant overproduction), lack extremely rare protective genetics preventing further disease progression \[69], and is not treated with any recent medical interventions, **then** they will eventually (after typically 15\-20 years, and rarely more than 30\), develop tau pathology and neurodegeneration in the region of this tau pathology (unless some other disease kills them first). Usually this will start in the medial temporal lobe and affect memory, then spread to other regions and functions.

Mechanistic claims I am *not* making:

1. I am *not* claiming that environmental factors such as microbial infection can never be a cause of Alzheimer’s disease. However, I claim that in all such cases, they act upstream of the above\-described disease process, inducing the formation of amyloid deposits leading to the disease. Furthermore, these cannot be all cases \- there are instances of the disease in which amyloid deposits arise essentially entirely due to genetic factors (like the autosomal\-dominant cases of overproduction).
2. I am *not* claiming that the disease is “as simple as” amyloid deposits directly inducing neurodegeneration. As described above, they act indirectly, via the eventual downstream tau pathology, and possibly an associated microglial/astrocytic inflammatory response. Therefore, there are many people in the preclinical, amyloid\-only disease phase who will eventually progress to dementia but have not yet.

These two clarifications imply that even though amyloid pathology is a necessary and (in enough severity) sufficient cause of the disease under normal circumstances, therapies with other targets might still be effective, either intervening upstream such that amyloid deposits never occur, or downstream so as to prevent the neurodegenerative process.

## The testable prediction

I would bet on the following: A therapy whose sole intended mechanism involves amyloid production or clearance, in a randomized, double\-blind, placebo\-controlled trial, will, in the next 12 years, achieve a slowdown of cognitive decline of at least 75%, with a p\-value below 0\.001, in its preregistered primary cognitive endpoint (or an average of all such endpoints if more than one exists). I’d eventually expect better than 75% efficacy, but getting stuff to work takes time, and I wanted to make a prediction which can be tested in a reasonable timeframe.

On the other hand, if a clinical trial completes earlier than 12 years from now (perhaps \[73], reading out in 2027\), sustains extremely good amyloid clearance at the preclinical stage, and has a good safety profile, but doesn’t make substantial progress towards this 75% goal, then I would consider this prediction refuted in advance.

For targeting amyloid, I’m most optimistic about a blood brain barrier (BBB)\-penetrating antibody such as trontinemab \[74–76], but with an epitope more like lecanemab’s, and given in the preclinical disease stage. Other options for targeting amyloid include antisense oligonucleotides for APP as well as γ\-secretase modulators.

## The successes and failures of amyloid antibodies

There have now been three amyloid antibodies with positive phase 3 (and earlier) clinical trials on cognitive endpoints (but with much less than 75% efficacy):

1. **Aducanumab** in phase 1b \[77] (**19%** on my average across cognitive endpoints for the highest two doses) and one of two phase 3 trials \[78] **(22%**, but **negative 2%** in the other trial, which also gave a lower dose on average).
2. **Lecanemab** in its phase 2b \[79] (**30%** on the primary measure, though it technically failed because of its ambitious Bayesian endpoint) and phase 3 \[80] (**27%**).
3. **Donanemab** in phase 2 \[81] **(32%**) and phase 3 \[82] (**35%**).

There have also been earlier antibodies that saw only failure in phase 3 – bapineuzumab \[83, 84], crenezumab \[85], solanezumab \[86–88], and gantenerumab \[88, 89]. These failed drugs didn’t just do a bad job treating Alzheimer’s. They also did a bad job clearing amyloid plaques, so their failure is consistent with the amyloid hypothesis. That said, just coupling the older, previously\-unsuccessful antibody gantenerumab with a BBB\-crossing mechanism produced extremely good target engagement and better safety in early clinical trials \[74–76]. This makes me optimistic about a future BBB\-crossing lecanemab (or similar), especially if given in the preclinical disease phase prior to significant tauopathy.

Each of the “successes” have shown about 25\-30% slowing of decline over 18 months. Some object that this isn’t clinically meaningful because it’s only a slowdown of ∼0\.5 points on an 18\-point CDR\-SB scale, but they don’t mention that the participants start about 3 points from a perfect score (since these are relatively early\-stage patients) and worsen by ∼1\.5 points in those 18 months when on placebo. A literally perfect drug \- one which halted all further clinical progression \- could therefore only achieve about 1\.5 points of efficacy on that scale. The cruxy question is whether the drugs maintain a 30% reduction after 18 months. Preliminary signs from lecanemab’s and donanemab’s open\-label extensions show that they do \[90], so this would amount to about 40% more years of life at each disease stage.

But why have amyloid antibodies only achieved about 30% efficacy so far? The likely answer: mainly because they were given too late to prevent the downstream tau pathology cascade, but also because some of their side effects, like when they target amyloid\-bearing blood vessels rather than brain tissue, can themselves worsen cognition.

That said, even achieving 30% efficacy proves that amyloid plays *some* causal disease role and isn’t *merely* a downstream, harmless pathology.

## Why is the amyloid hypothesis unpopular?

The amyloid hypothesis remains popular in the Alzheimer’s disease research community, but most press coverage is negative. These challenges are understandable, and some of them make good points, but overall fail to address the evidence discussed above.

#### Failures and perceived failures of amyloid therapies

I discussed this [above](https://docs.google.com/document/d/130cgtEEwnwPStrsmOFEIOAZk1wq_siFNAKIMhWdvMuM/edit#bookmark=id.ihc42bbb5bpo), but to recap:

* Early attempts had suboptimal epitopes which didn’t successfully engage their targets.
* Later attempts did engage their target, but have mostly been tested ∼15 years after the disease started, and so after downstream tau pathologies had already started.
* These later attempts demonstrated a ∼30% slowdown in clinical progression, which proves at least some causal role for amyloid. Some claim this isn’t clinically meaningful but they use misleading arguments (like saying it’s a 0\.5\-point benefit on an 18\-point scale, when even a perfect drug which halted all clinical progression could only have achieved a 1\.5\-point benefit vs. placebo, since the patients start near a perfect score and the placebo group only worsens by about 1\.5 points).
* In all mature antibodies so far, they have been attended with not\-great side effects: brain swelling and bleeding, for reasons related to their difficulty crossing the BBB into brain tissue where they’re actually needed. A new generation of antibodies will cross the BBB, improving efficacy and safety.

It’s frustrating that getting even to a 30% slowdown has taken as long as it has, but all of this is consistent with the model of the disease I laid out, which has strong evidence behind it, and there’s every reason to expect that a new drug (A) with an optimal epitope, similar to lecanemab or donanemab, (B) given in the early preclinical phase, 10\+ years earlier than currently, and (C) with a shuttle mechanism to cross the BBB, could be very successful.

The mature antibodies only have (A). There are ongoing trials combining (A)\+(B) \[73], \[114], \[115], and a shortly upcoming trial combining (B)\+(C) \[76], but not yet all three together. I’m optimistic about these but expect (A)\+(B)\+(C) to do especially well.

Unfortunately, this stuff is hard, slow, and over\-regulated. Which means it’s taking longer than we’d like. But my guess is we’re on the right track.

#### Challenges translating from mouse models

The researchers who developed the early Alzheimer mouse models wanted the clearest possible window into disease progression, so they turned up an amyloid gene to extreme levels far beyond those of even severe human cases. This level of amyloid was so massive that it caused cognitive deficits directly, eg without any contribution from tau. And in fact, mouse proteins work differently from human proteins, and mice do not naturally get tauopathies.

So researchers increased amyloid, got cognitive deficits, and thought they were simulating Alzheimer’s. But they were actually doing something significantly different:

* **Human patients:** increased amyloid → tau → neurodegeneration and disease
* **Mouse models:** *massively* increased amyloid → neurodegeneration and disease

Then, since the mouse models didn’t really have Alzheimer’s the way it works in humans, most of the findings from the mouse models failed to translate into human Alzheimer’s patients. Since the findings from the amyloid mice did such a bad job matching human Alzheimer’s cases, some people concluded that amyloid did not cause Alzheimer’s.

There are now tauopathy mouse models. In those models, worsening amyloid pathology tends to cause the tau pathology to worsen as well. \[35, 55, 103–113] I predict that findings from these mice are more likely to translate to human disease.

#### Fraud in amyloid research

There was some really bad fraud, such as documented in \[123], which is the case that received the most attention. For another good overview of fraud in Alzheimer research (not all relating to amyloid\-β), see \[124]. The perpetrators should be institutionally severely punished.

This fraud has sometimes been framed by amyloid hypothesis critics as impacting very foundational work for the amyloid hypothesis. But this mostly isn’t true. \[125] It concerns some specific variants of amyloid\-β that are not prominent in nearly any of the literature I’ve encountered. When it was uncovered, I checked how many of the hundreds of papers in my notes seemed to be affected, and very few were.

For example, the main findings I have relied upon in this argument have, to the best of my understanding, survived unscathed:

* The smoking gun [genetic evidence](https://docs.google.com/document/d/130cgtEEwnwPStrsmOFEIOAZk1wq_siFNAKIMhWdvMuM/edit#bookmark=id.f1k9y4mgrnu1) for amyloid’s causal role in the autosomal\-dominant versions of the disease, and the extensive similarities between the autosomal\-dominant disease and sporadic disease.
* The evidence that [Aβ can potentiate or accelerate tau pathology](https://docs.google.com/document/d/130cgtEEwnwPStrsmOFEIOAZk1wq_siFNAKIMhWdvMuM/edit#bookmark=id.pw1ydynatz5u) (which itself is proximate to neurodegeneration), from studies in animal models, studies in human cells, the spatiotemporal disease course, causal mediation modeling of that disease course, and the tau biomarker effects from amyloid therapies.

#### The “amyloid mafia”

There is a perception that a combination of nefarious and misguided behavior has led to it being impossible to pursue alternative hypotheses or therapies, with the whole field pursuing a dead end.

I don’t have numbers for the more basic research, but we do have good data on the therapeutics being explored. In 2020, only 35% of hopefully\-disease\-modifying phase 3 trials and 20% of hopefully\-disease\-modifying phase 2 trials targeted amyloid; 65\-80% target other pathways \[126]. The breakdown for other years is similar (see e.g. \[127]).

I support this, in part because it’s always good to test alternative possibilities, but in part because I expect that some of them can succeed even if the ATN model is right.

#### The compellingness of alternative hypotheses

A primary competitor of the amyloid hypothesis is the *tau hypothesis*. This naturally claims that the tau protein is the fundamental cause of Alzheimer’s, which makes good sense \- the location and severity of tau pathology correlates better with the location and severity of neurodegeneration than does amyloid\-β, in both humans \[23 \- 30] and combined amyloid/tau mouse models \[31 – 35]. However, this is exactly as predicted by the ATN (amyloid → tau → neurodegeneration) model of the disease: amyloid pathology builds for 15–20 years, eventually inducing tau pathology; then the tau pathology causes neurodegeneration. Why not skip the amyloid step? Because as discussed above, we have extensive genetic and clinical evidence that the amyloid is the trigger for tau to spread in the first place.

(of course, this doesn’t mean tau is a bad target for therapy. I’m optimistic about tau antisense oligonucleotides such as BIIB080, which had a very promising phase 1b trial \[116, 117] and is now in phase 2\)

Another competitor is the *microbial infection hypothesis.* Again, there is good evidence this is true in some cases \- multiple pathogens such as the periodontitis bacteria *P. gingivalis* \[118] and various herpes viruses \[3, 119] are correlated with the disease, which has tempted some microbiologists to treat amyloid as merely a harmless correlate: since amyloid is involved in the body’s immune response, maybe in the process of causing brain damage the microbes cause some amyloid deposition on the side. But again, these facts are also consistent with the ATN (or in this case IATN \- infection → amyloid → tau → neurodegeneration) hypothesis.

(again, treating these microbes is still another promising target for treating or preventing Alzheimer’s)

These alternatives are a good reminder that the causal pathway can be hard to disentangle. But again, the strongest evidence for amyloid’s causal role is genetics: genes which increase amyloid increase Alzheimer’s risk, and rare mutations that massively increase amyloid massively increase the risk of Alzheimer’s (including unusually young or severe cases). Given this natural experiment, the most parsimonious explanation is that amyloid is intimately involved in Alzheimer’s, and then the most parsimonious explanation for the role of infection and tau is that they are part of the same I → A → T → N pathway.

#### The meta\-psychological explanation: frustration at complexity and slow progress

Progress in biomedical research is slow. The disease (and amyloid\-β’s prevalence in it) was discovered in 1906, the amyloid causal hypothesis was first proposed in 1992 after discovery of the genetic evidence \[4], \[5], the first amyloid antibody entered clinical trials in 2005 \[128] \- and now, in 2025, the best we have is ∼30% efficacy with potentially serious side effects.

But biology is messy, and we need to have comfort with complexity. Yes, there’s evidence that tau is responsible for the neurodegeneration in Alzheimer’s disease; no, this doesn’t contradict the amyloid hypothesis. Yes, Biogen screwed up in conducting the aducanumab phase 3 trials and this made the results harder to interpret; no, that doesn’t mean amyloid therapies have completely failed. Yes, it’s taken way too long to get even to this intermediate point of 30% efficacy, due to a combination of overregulation and biology just being damned hard; no, that doesn’t mean we’re on the wrong track with the underlying science.

Some years ago, I worked on the guidance and navigation software for the Falcon 9 first stage landing. The early attempts failed because of annoying issues like stuck propellant valves, running out of fin hydraulic fluid, and so on. It took many tries to iron out all those issues. Meanwhile, fans and critics kept proposing that SpaceX’s fundamental approach was flawed, and suggesting entirely different approaches. Most of that criticism was pretty uninformed.

This of course isn’t a general refutation of outsiders criticizing any field, as sometimes such criticism is necessary and right. But it does illustrate the need for patience when specialists are attempting something hard and unprecedented. Curing Alzheimer’s disease is much harder than landing a rocket. It’s important to understand the reasons for therapeutic failures (in this case, failure to engage the target) and underwhelming successes (probably due to treatment late in the disease progression, plus the challenges in crossing the BBB), to put that in the context of the scientific evidence from the basic research (which is very strong in this case), and to consider how compelling the alternative hypotheses are (not very).

Frustrated people who don’t have the time or capacity to study the science themselves often want someone to blame, and the “amyloid mafia” is a ready target. But there isn’t as much of a mafia as they think; biology is just hard.

My bottom line remains that no alternative hypothesis offers a plausible accounting of the evidence for amyloid’s causal role; whereas conversely, there is no evidence I’m aware of that the ATN model has great trouble accounting for.

I am grateful to Logan Thrasher Collins, Tommy Crow, Dan Elton, and Greg Fitzgerald for valuable feedback on this essay, and to Scott Alexander for edits which improved its structure and presentation.

## Footnotes

\[1] J. M. Long and D. M. Holtzman, “Alzheimer Disease: An Update on Pathobiology and Treatment Strategies,” *Cell*, vol. 179, no. 2, pp. 312–339, Oct. 2019, doi: [10\.1016/j.cell.2019\.09\.001](https://doi.org/10.1016/j.cell.2019.09.001).

\[2] D. K. V. Kumar *et al.*, “Amyloid\-β peptide protects against microbial infection in mouse and worm models of Alzheimer’s disease,” *Science Translational Medicine*, vol. 8, no. 340, pp. 340ra72–340ra72, May 2016, doi: [10\.1126/scitranslmed.aaf1059](https://doi.org/10.1126/scitranslmed.aaf1059).

\[3] W. A. Eimer *et al.*, “Alzheimer’s Disease\-Associated β\-Amyloid Is Rapidly Seeded by Herpesviridae to Protect against Brain Infection,” *Neuron*, vol. 99, no. 1, pp. 56–63\.e3, Jul. 2018, doi: [10\.1016/j.neuron.2018\.06\.030](https://doi.org/10.1016/j.neuron.2018.06.030).

\[4] J. A. Hardy and G. A. Higgins, “Alzheimer’s Disease: The Amyloid Cascade Hypothesis,” *Science*, vol. 256, no. 5054, pp. 184–185, Apr. 1992, doi: [10\.1126/science.1566067](https://doi.org/10.1126/science.1566067).

\[5] T. Whipple, “‘What we did then we could do now in a few days or a week. It took us four or five years. Then, in 1991, they had the results.’” X (formerly Twitter), Jul. 17, 2024\. Accessed: Jul. 23, 2025\. \[Online]. Available:<https://x.com/whippletom/status/1787768187758485592>

\[6] C. Haass, C. Kaether, G. Thinakaran, and S. Sisodia, “Trafficking and Proteolytic Processing of APP,” *Cold Spring Harbor Perspectives in Medicine*, vol. 2, no. 5, p. a006270, May 2012, doi: [10\.1101/cshperspect.a006270](https://doi.org/10.1101/cshperspect.a006270).

\[7] A. W. Bero *et al.*, “Neuronal activity regulates the regional vulnerability to amyloid\-β deposition,” *Nature Neuroscience*, vol. 14, no. 6, pp. 750–756, Jun. 2011, doi: [10\.1038/nn.2801](https://doi.org/10.1038/nn.2801).

\[8] J. H. Roh *et al.*, “Disruption of the Sleep\-Wake Cycle and Diurnal Fluctuation of β\-Amyloid in Mice with Alzheimer’s Disease Pathology,” *Science Translational Medicine*, vol. 4, no. 150, pp. 150ra122–150ra122, Sep. 2012, doi: [10\.1126/scitranslmed.3004291](https://doi.org/10.1126/scitranslmed.3004291).

\[9] B. P. Lucey *et al.*, “Effect of sleep on overnight cerebrospinal fluid amyloid β kinetics,” *Annals of Neurology*, vol. 83, no. 1, pp. 197–204, 2018, doi: [10\.1002/ana.25117](https://doi.org/10.1002/ana.25117).

\[10] L. Xie *et al.*, “Sleep Drives Metabolite Clearance from the Adult Brain,” *Science*, vol. 342, no. 6156, pp. 373–377, Oct. 2013, doi: [10\.1126/science.1241224](https://doi.org/10.1126/science.1241224).

\[11] E. Shokri\-Kojori *et al.*, “Β\-Amyloid accumulation in the human brain after one night of sleep deprivation,” *Proceedings of the National Academy of Sciences*, vol. 115, no. 17, pp. 4483–4488, Apr. 2018, doi: [10\.1073/pnas.1721694115](https://doi.org/10.1073/pnas.1721694115).

\[12] J. M. Castellano *et al.*, “Human apoE isoforms differentially regulate brain amyloid\-β peptide clearance,” *Science Translational Medicine*, vol. 3, no. 89, pp. 89ra57–89ra57, Jun. 2011, doi: [10\.1126/scitranslmed.3002156](https://doi.org/10.1126/scitranslmed.3002156).

\[13] Y. Shi and D. M. Holtzman, “Interplay between innate immunity and Alzheimer disease: APOE and TREM2 in the spotlight,” *Nature Reviews Immunology*, vol. 18, no. 12, pp. 759–772, Dec. 2018, doi: [10\.1038/s41577\-018\-0051\-1](https://doi.org/10.1038/s41577-018-0051-1).

\[14] B. A. Gordon *et al.*, “Spatial patterns of neuroimaging biomarker change in individuals from families with autosomal dominant Alzheimer’s disease: A longitudinal study,” *The Lancet Neurology*, vol. 17, no. 3, pp. 241–250, Mar. 2018, doi: [10\.1016/S1474\-4422(18\)30028\-0](https://doi.org/10.1016/S1474-4422(18)30028-0).

\[15] R. L. Buckner *et al.*, “Cortical Hubs Revealed by Intrinsic Functional Connectivity: Mapping, Assessment of Stability, and Relation to Alzheimer’s Disease,” *Journal of Neuroscience*, vol. 29, no. 6, pp. 1860–1873, Feb. 2009, doi: [10\.1523/JNEUROSCI.5062\-08\.2009](https://doi.org/10.1523/JNEUROSCI.5062-08.2009).

\[16] S. Villeneuve *et al.*, “Existing Pittsburgh Compound\-B positron emission tomography thresholds are too high: Statistical and pathological evaluation,” *Brain*, vol. 138, no. 7, pp. 2020–2033, Jul. 2015, doi: [10\.1093/brain/awv112](https://doi.org/10.1093/brain/awv112).

\[17] S. Palmqvist *et al.*, “Earliest accumulation of β\-amyloid occurs within the default\-mode network and concurrently affects brain connectivity,” *Nature Communications*, vol. 8, no. 1, p. 1214, Oct. 2017, doi: [10\.1038/s41467\-017\-01150\-x](https://doi.org/10.1038/s41467-017-01150-x).

\[18] N. Mattsson, S. Palmqvist, E. Stomrud, J. Vogel, and O. Hansson, “Staging **β** \-Amyloid Pathology With Amyloid Positron Emission Tomography,” *JAMA Neurology*, vol. 76, no. 11, p. 1319, Nov. 2019, doi: [10\.1001/jamaneurol.2019\.2214](https://doi.org/10.1001/jamaneurol.2019.2214).

\[19] W. Jagust, “Imaging the evolution and pathophysiology of Alzheimer disease,” *Nature Reviews Neuroscience*, vol. 19, no. 11, pp. 687–700, Nov. 2018, doi: [10\.1038/s41583\-018\-0067\-3](https://doi.org/10.1038/s41583-018-0067-3).

\[20] E. Levitis *et al.*, “Differentiating amyloid beta spread in autosomal dominant and sporadic Alzheimer’s disease,” *Brain Communications*, vol. 4, no. 3, p. fcac085, Jun. 2022, doi: [10\.1093/braincomms/fcac085](https://doi.org/10.1093/braincomms/fcac085).

\[21] Z. Jaunmuktane *et al.*, “Evidence for human transmission of amyloid\-β pathology and cerebral amyloid angiopathy,” *Nature*, vol. 525, no. 7568, pp. 247–250, Sep. 2015, doi: [10\.1038/nature15369](https://doi.org/10.1038/nature15369).

\[22] G. Banerjee *et al.*, “Iatrogenic Alzheimer’s disease in recipients of cadaveric pituitary\-derived growth hormone,” *Nature Medicine*, vol. 30, no. 2, pp. 394–402, Feb. 2024, doi: [10\.1038/s41591\-023\-02729\-2](https://doi.org/10.1038/s41591-023-02729-2).

\[23] P. T. Nelson *et al.*, “Clinicopathologic Correlations in a Large Alzheimer Disease Center Autopsy Cohort: Neuritic Plaques and Neurofibrillary Tangles "Do Count" When Staging Disease Severity,” *Journal of Neuropathology \& Experimental Neurology*, vol. 66, no. 12, pp. 1136–1146, Dec. 2007, doi: [10\.1097/nen.0b013e31815c5efb](https://doi.org/10.1097/nen.0b013e31815c5efb).

\[24] M. R. Brier *et al.*, “Tau and Aβ imaging, CSF measures, and cognition in Alzheimer’s disease,” *Science Translational Medicine*, vol. 8, no. 338, pp. 338ra66–338ra66, May 2016, doi: [10\.1126/scitranslmed.aaf2362](https://doi.org/10.1126/scitranslmed.aaf2362).

\[25] A. J. Aschenbrenner, B. A. Gordon, T. L. S. Benzinger, J. C. Morris, and J. J. Hassenstab, “Influence of tau PET, amyloid PET, and hippocampal volume on cognition in Alzheimer disease,” *Neurology*, vol. 91, no. 9, pp. e859–e866, Aug. 2018, doi: [10\.1212/WNL.0000000000006075](https://doi.org/10.1212/WNL.0000000000006075).

\[26] B. J. Hanseeuw *et al.*, “Association of Amyloid and Tau With Cognition in Preclinical Alzheimer Disease: A Longitudinal Study,” *JAMA Neurology*, vol. 76, no. 8, pp. 915–924, Aug. 2019, doi: [10\.1001/jamaneurol.2019\.1424](https://doi.org/10.1001/jamaneurol.2019.1424).

\[27] C. R. Jack Jr *et al.*, “The bivariate distribution of amyloid\-β and tau: Relationship with established neurocognitive clinical syndromes,” *Brain*, vol. 142, no. 10, pp. 3230–3242, Oct. 2019, doi: [10\.1093/brain/awz268](https://doi.org/10.1093/brain/awz268).

\[28] R. La Joie *et al.*, “Prospective longitudinal atrophy in Alzheimer’s disease correlates with the intensity and topography of baseline tau\-PET,” *Science Translational Medicine*, vol. 12, no. 524, p. eaau5732, Jan. 2020, doi: [10\.1126/scitranslmed.aau5732](https://doi.org/10.1126/scitranslmed.aau5732).

\[29] A. Bejanin *et al.*, “Tau pathology and neurodegeneration contribute to cognitive impairment in Alzheimer’s disease,” *Brain*, vol. 140, no. 12, pp. 3286–3300, Dec. 2017, doi: [10\.1093/brain/awx243](https://doi.org/10.1093/brain/awx243).

\[30] C. Xia *et al.*, “Association of In Vivo \[18F]AV\-1451 Tau PET Imaging Results With Cortical Atrophy and Symptoms in Typical and Atypical Alzheimer Disease,” *JAMA Neurology*, vol. 74, no. 4, pp. 427–436, Apr. 2017, doi: [10\.1001/jamaneurol.2016\.5755](https://doi.org/10.1001/jamaneurol.2016.5755).

\[31] C. E. G. Leyns *et al.*, “TREM2 function impedes tau seeding in neuritic plaques,” *Nature Neuroscience*, vol. 22, no. 8, pp. 1217–1222, Aug. 2019, doi: [10\.1038/s41593\-019\-0433\-0](https://doi.org/10.1038/s41593-019-0433-0).

\[32] B. L. Heckmann *et al.*, “LC3\-Associated Endocytosis Facilitates β\-Amyloid Clearance and Mitigates Neurodegeneration in Murine Alzheimer’s Disease,” *Cell*, vol. 178, no. 3, pp. 536–551\.e14, Jul. 2019, doi: [10\.1016/j.cell.2019\.05\.056](https://doi.org/10.1016/j.cell.2019.05.056).

\[33] S.\-H. Lee *et al.*, “Trem2 restrains the enhancement of tau accumulation and neurodegeneration by β\-amyloid pathology,” *Neuron*, vol. 109, no. 8, pp. 1283–1301\.e6, Apr. 2021, doi: [10\.1016/j.neuron.2021\.02\.010](https://doi.org/10.1016/j.neuron.2021.02.010).

\[34] M. Gratuze *et al.*, “Activated microglia mitigate Aβ\-associated tau seeding and spreading,” *Journal of Experimental Medicine*, vol. 218, no. 8, p. e20210542, Jun. 2021, doi: [10\.1084/jem.20210542](https://doi.org/10.1084/jem.20210542).

\[35] C. Lodder *et al.*, “CSF1R inhibition rescues tau pathology and neurodegeneration in an A/T/N model with combined AD pathologies, while preserving plaque associated microglia,” *Acta Neuropathologica Communications*, vol. 9, no. 1, p. 108, Jun. 2021, doi: [10\.1186/s40478\-021\-01204\-8](https://doi.org/10.1186/s40478-021-01204-8).

\[36] Y. Shi *et al.*, “Structure\-based classification of tauopathies,” *Nature*, vol. 598, no. 7880, pp. 359–363, Oct. 2021, doi: [10\.1038/s41586\-021\-03911\-7](https://doi.org/10.1038/s41586-021-03911-7).

\[37] A. de Calignon *et al.*, “Propagation of Tau Pathology in a Model of Early Alzheimer’s Disease,” *Neuron*, vol. 73, no. 4, pp. 685–697, Feb. 2012, doi: [10\.1016/j.neuron.2011\.11\.033](https://doi.org/10.1016/j.neuron.2011.11.033).

\[38] L. Liu *et al.*, “Trans\-Synaptic Spread of Tau Pathology In Vivo,” *PLOS ONE*, vol. 7, no. 2, p. e31302, Feb. 2012, doi: [10\.1371/journal.pone.0031302](https://doi.org/10.1371/journal.pone.0031302).

\[39] A. L. Woerman *et al.*, “Tau prions from Alzheimer’s disease and chronic traumatic encephalopathy patients propagate in cultured cells,” *Proceedings of the National Academy of Sciences*, vol. 113, no. 50, pp. E8187–E8196, Dec. 2016, doi: [10\.1073/pnas.1616344113](https://doi.org/10.1073/pnas.1616344113).

\[40] S. Dujardin *et al.*, “Neuron\-to\-neuron wild\-type Tau protein transfer through a trans\-synaptic mechanism: Relevance to sporadic tauopathies,” *Acta Neuropathologica Communications*, vol. 2, no. 1, p. 14, Jan. 2014, doi: [10\.1186/2051\-5960\-2\-14](https://doi.org/10.1186/2051-5960-2-14).

\[41] S. Calafate *et al.*, “Synaptic Contacts Enhance Cell\-to\-Cell Tau Pathology Propagation,” *Cell Reports*, vol. 11, no. 8, pp. 1176–1183, May 2015, doi: [10\.1016/j.celrep.2015\.04\.043](https://doi.org/10.1016/j.celrep.2015.04.043).

\[42] E. E. Congdon *et al.*, “Affinity of Tau antibodies for solubilized pathological Tau species but not their immunogen or insoluble Tau aggregates predicts in vivo and ex vivo efficacy,” *Molecular Neurodegeneration*, vol. 11, no. 1, p. 62, Aug. 2016, doi: [10\.1186/s13024\-016\-0126\-z](https://doi.org/10.1186/s13024-016-0126-z).

\[43] S. L. DeVos *et al.*, “Synaptic Tau Seeding Precedes Tau Pathology in Human Alzheimer’s Disease Brain,” *Frontiers in Neuroscience*, vol. 12, Apr. 2018, doi: [10\.3389/fnins.2018\.00267](https://doi.org/10.3389/fnins.2018.00267).

\[44] J. W. Wu *et al.*, “Small Misfolded Tau Species Are Internalized via Bulk Endocytosis and Anterogradely and Retrogradely Transported in Neurons\*,” *Journal of Biological Chemistry*, vol. 288, no. 3, pp. 1856–1870, Jan. 2013, doi: [10\.1074/jbc.M112\.394528](https://doi.org/10.1074/jbc.M112.394528).

\[45] S. Takeda *et al.*, “Neuronal uptake and propagation of a rare phosphorylated high\-molecular\-weight tau derived from Alzheimer’s disease brain,” *Nature Communications*, vol. 6, no. 1, p. 8490, Oct. 2015, doi: [10\.1038/ncomms9490](https://doi.org/10.1038/ncomms9490).

\[46] D. M. O. Ramirez *et al.*, “Endogenous pathology in tauopathy mice progresses via brain networks.” bioRxiv, May 2023\. doi: [10\.1101/2023\.05\.23\.541792](https://doi.org/10.1101/2023.05.23.541792).

\[47] S. Narasimhan *et al.*, “Pathological Tau Strains from Human Brains Recapitulate the Diversity of Tauopathies in Nontransgenic Mouse Brain,” *Journal of Neuroscience*, vol. 37, no. 47, pp. 11406–11423, Nov. 2017, doi: [10\.1523/JNEUROSCI.1230\-17\.2017](https://doi.org/10.1523/JNEUROSCI.1230-17.2017).

\[48] F. Clavaguera *et al.*, “Transmission and spreading of tauopathy in transgenic mouse brain,” *Nature Cell Biology*, vol. 11, no. 7, pp. 909–913, Jul. 2009, doi: [10\.1038/ncb1901](https://doi.org/10.1038/ncb1901).

\[49] J. L. Guo and V. M.\-Y. Lee, “Seeding of Normal Tau by Pathological Tau Conformers Drives Pathogenesis of Alzheimer\-like Tangles\*,” *Journal of Biological Chemistry*, vol. 286, no. 17, pp. 15317–15331, Apr. 2011, doi: [10\.1074/jbc.M110\.209296](https://doi.org/10.1074/jbc.M110.209296).

\[50] F. Clavaguera *et al.*, “Brain homogenates from human tauopathies induce tau inclusions in mouse brain,” *Proceedings of the National Academy of Sciences*, vol. 110, no. 23, pp. 9535–9540, Jun. 2013, doi: [10\.1073/pnas.1301175110](https://doi.org/10.1073/pnas.1301175110).

\[51] F. Clavaguera *et al.*, “Peripheral administration of tau aggregates triggers intracerebral tauopathy in transgenic mice,” *Acta Neuropathologica*, vol. 127, no. 2, pp. 299–301, Feb. 2014, doi: [10\.1007/s00401\-013\-1231\-5](https://doi.org/10.1007/s00401-013-1231-5).

\[52] E. Peeraer *et al.*, “Intracerebral injection of preformed synthetic tau fibrils initiates widespread tauopathy and neuronal loss in the brains of tau transgenic mice,” *Neurobiology of Disease*, vol. 73, pp. 83–95, Jan. 2015, doi: [10\.1016/j.nbd.2014\.08\.032](https://doi.org/10.1016/j.nbd.2014.08.032).

\[53] I.\-C. Stancu *et al.*, “Templated misfolding of Tau by prion\-like seeding along neuronal connections impairs neuronal network function and associated behavioral outcomes in Tau transgenic mice,” *Acta Neuropathologica*, vol. 129, no. 6, pp. 875–894, Jun. 2015, doi: [10\.1007/s00401\-015\-1413\-4](https://doi.org/10.1007/s00401-015-1413-4).

\[54] Z. He *et al.*, “Amyloid\-β plaques enhance Alzheimer’s brain tau\-seeded pathologies by facilitating neuritic plaque tau aggregation,” *Nature Medicine*, vol. 24, no. 1, pp. 29–38, Jan. 2018, doi: [10\.1038/nm.4443](https://doi.org/10.1038/nm.4443).

\[55] C. Vergara *et al.*, “Amyloid\-β pathology enhances pathological fibrillary tau seeding induced by Alzheimer PHF in vivo,” *Acta neuropathologica*, vol. 137, no. 3, pp. 397–412, Mar. 2019, doi: [10\.1007/s00401\-018\-1953\-5](https://doi.org/10.1007/s00401-018-1953-5).

\[56] S. Lam *et al.*, “Transmission of amyloid\-beta and tau pathologies is associated with cognitive impairments in a primate,” *Acta Neuropathologica Communications*, vol. 9, no. 1, pp. 1–24, Dec. 2021, doi: [10\.1186/s40478\-021\-01266\-8](https://doi.org/10.1186/s40478-021-01266-8).

\[57] E. Audouard *et al.*, “High–Molecular\-Weight Paired Helical Filaments from Alzheimer Brain Induces Seeding of Wild\-Type Mouse Tau into an Argyrophilic 4R Tau Pathology in Vivo,” *The American Journal of Pathology*, vol. 186, no. 10, pp. 2709–2722, Oct. 2016, doi: [10\.1016/j.ajpath.2016\.06\.008](https://doi.org/10.1016/j.ajpath.2016.06.008).

\[58] J. L. Guo *et al.*, “Unique pathological tau conformers from Alzheimer’s brains transmit tau pathology in nontransgenic mice,” *Journal of Experimental Medicine*, vol. 213, no. 12, pp. 2635–2654, Oct. 2016, doi: [10\.1084/jem.20160833](https://doi.org/10.1084/jem.20160833).

\[59] C. A. Lasagna\-Reeves *et al.*, “Alzheimer brain\-derived tau oligomers propagate pathology from endogenous tau,” *Scientific Reports*, vol. 2, no. 1, p. 700, Oct. 2012, doi: [10\.1038/srep00700](https://doi.org/10.1038/srep00700).

\[60] H. Braak, D. R. Thal, E. Ghebremedhin, and K. Del Tredici, “Stages of the Pathologic Process in Alzheimer Disease: Age Categories From 1 to 100 Years,” *Journal of Neuropathology \& Experimental Neurology*, vol. 70, no. 11, pp. 960–969, Nov. 2011, doi: [10\.1097/NEN.0b013e318232a379](https://doi.org/10.1097/NEN.0b013e318232a379).

\[61] H. Braak and K. Del Tredici, “The pathological process underlying Alzheimer’s disease in individuals under thirty,” *Acta Neuropathologica*, vol. 121, no. 2, pp. 171–181, Feb. 2011, doi: [10\.1007/s00401\-010\-0789\-4](https://doi.org/10.1007/s00401-010-0789-4).

\[62] A. Elobeid, H. Soininen, and I. Alafuzoff, “Hyperphosphorylated tau in young and middle\-aged subjects,” *Acta Neuropathologica*, vol. 123, no. 1, pp. 97–104, Jan. 2012, doi: [10\.1007/s00401\-011\-0906\-z](https://doi.org/10.1007/s00401-011-0906-z).

\[63] “PET Imaging of Tau Deposition in the Aging Human Brain,” *Neuron*, vol. 89, no. 5, pp. 971–982, Mar. 2016, doi: [10\.1016/j.neuron.2016\.01\.028](https://doi.org/10.1016/j.neuron.2016.01.028).

\[64] Y. Shi *et al.*, “Cryo\-EM structures of tau filaments from Alzheimer’s disease with PET ligand APN\-1607,” *Acta Neuropathologica*, vol. 141, no. 5, pp. 697–708, May 2021, doi: [10\.1007/s00401\-021\-02294\-3](https://doi.org/10.1007/s00401-021-02294-3).

\[65] J. Therriault *et al.*, “Biomarker modeling of Alzheimer’s disease using PET\-based Braak staging,” *Nature Aging*, vol. 2, no. 6, pp. 526–535, Jun. 2022, doi: [10\.1038/s43587\-022\-00204\-0](https://doi.org/10.1038/s43587-022-00204-0).

\[66] P. T. Nelson, H. Braak, and W. R. Markesbery, “Neuropathology and Cognitive Impairment in Alzheimer Disease: A Complex but Coherent Relationship,” *Journal of Neuropathology \& Experimental Neurology*, vol. 68, no. 1, pp. 1–14, Jan. 2009, doi: [10\.1097/NEN.0b013e3181919a48](https://doi.org/10.1097/NEN.0b013e3181919a48).

\[67] G. B. Frisoni *et al.*, “The probabilistic model of Alzheimer disease: The amyloid hypothesis revised,” *Nature Reviews Neuroscience*, vol. 23, no. 1, pp. 53–66, Jan. 2022, doi: [10\.1038/s41583\-021\-00533\-w](https://doi.org/10.1038/s41583-021-00533-w).

\[68] K. A. Josephs, S. D. Weigand, and J. L. Whitwell, “Characterizing Amyloid\-Positive Individuals With Normal Tau PET Levels After 5 Years: An ADNI Study,” *Neurology*, vol. 98, no. 22, May 2022, doi: [10\.1212/WNL.0000000000200287](https://doi.org/10.1212/WNL.0000000000200287).

\[69] J. F. Arboleda\-Velasquez *et al.*, “Resistance to autosomal dominant Alzheimer’s disease in an APOE3 Christchurch homozygote: A case report,” *Nature Medicine*, vol. 25, no. 11, pp. 1680–1683, Nov. 2019, doi: [10\.1038/s41591\-019\-0611\-3](https://doi.org/10.1038/s41591-019-0611-3).

\[70] D. Sepulveda\-Falla *et al.*, “Distinct tau neuropathology and cellular profiles of an APOE3 Christchurch homozygote protected against autosomal dominant Alzheimer’s dementia,” *Acta Neuropathologica*, vol. 144, no. 3, pp. 589–601, Sep. 2022, doi: [10\.1007/s00401\-022\-02467\-8](https://doi.org/10.1007/s00401-022-02467-8).

\[71] D. J. Berlau, K. Kahle\-Wrobleski, E. Head, M. Goodus, R. Kim, and C. Kawas, “Dissociation of Neuropathologic Findings and Cognition: Case Report of an Apolipoprotein E ε2/ε2 Genotype,” *Archives of Neurology*, vol. 64, no. 8, pp. 1193–1196, Aug. 2007, doi: [10\.1001/archneur.64\.8\.1193](https://doi.org/10.1001/archneur.64.8.1193).

\[72] Y. Shi *et al.*, “Microglia drive APOE\-dependent neurodegeneration in a tauopathy mouse model,” *Journal of Experimental Medicine*, vol. 216, no. 11, pp. 2546–2561, Oct. 2019, doi: [10\.1084/jem.20190980](https://doi.org/10.1084/jem.20190980).

\[73] ClinicalTrials.gov, “A Donanemab (LY3002813\) Study in Participants With Preclinical Alzheimer’s Disease (TRAILBLAZER‑ALZ 3\).” ClinicalTrials.gov, NCT05026866, May 23, 2025\. Accessed: Jul. 24, 2025\. \[Online]. Available:<https://clinicaltrials.gov/study/NCT05026866>

\[74] J. Shugart, “Trontinemab data strengthen hope for brain shuttles,” *Alzforum News*, 2024, Available: [https://www.alzforum.org/news/conference\-coverage/trontinemab\-data\-strengthen\-hope\-brain\-shuttles](https://www.alzforum.org/news/conference-coverage/trontinemab-data-strengthen-hope-brain-shuttles)

\[75] L. Kulic *et al.*, “Latest interim results from the Brainshuttle AD study: A phase Ib/IIa study of trontinemab in people with Alzheimer’s disease.” Poster presented at the Clinical Trials on Alzheimer’s Disease (CTAD 2024\), Madrid, Spain, Oct. 30, 2024\. Available: [https://medically.roche.com/content/dam/pdmahub/restricted/neurology/ctad\-2024/CTAD\-2024\-presentation\-kulic\-latest\-interim\-results\-from\-brainshuttle\-ad\-study.pdf](https://medically.roche.com/content/dam/pdmahub/restricted/neurology/ctad-2024/CTAD-2024-presentation-kulic-latest-interim-results-from-brainshuttle-ad-study.pdf)

\[76] Roche, “Roche presents new insights in Alzheimer’s disease research across its diagnostics and pharmaceutical portfolios at AAIC.” Roche Media Release, Basel, Switzerland, Jul. 28, 2025\. Available: [https://www.roche.com/media/releases/med\-cor\-2025\-07\-28](https://www.roche.com/media/releases/med-cor-2025-07-28)

\[77] J. Sevigny *et al.*, “The antibody aducanumab reduces Aβ plaques in Alzheimer’s disease,” *Nature*, vol. 537, no. 7618, pp. 50–56, Sep. 2016, doi: [10\.1038/nature19323](https://doi.org/10.1038/nature19323).

\[78] S. Budd Haeberlein *et al.*, “Two Randomized Phase 3 Studies of Aducanumab in Early Alzheimer’s Disease,” *The Journal of Prevention of Alzheimer’s Disease*, vol. 9, no. 2, pp. 197–210, Apr. 2022, doi: [10\.14283/jpad.2022\.30](https://doi.org/10.14283/jpad.2022.30).

\[79] C. J. Swanson *et al.*, “A randomized, double\-blind, phase 2b proof\-of\-concept clinical trial in early Alzheimer’s disease with lecanemab, an anti\-Aβ protofibril antibody,” *Alzheimer’s Research \& Therapy*, vol. 13, no. 1, p. 80, Apr. 2021, doi: [10\.1186/s13195\-021\-00813\-8](https://doi.org/10.1186/s13195-021-00813-8).

\[80] C. H. van Dyck *et al.*, “Lecanemab in early Alzheimer’s disease,” *New England Journal of Medicine*, vol. 388, no. 1, pp. 9–21, 2023, doi: [10\.1056/NEJMoa2212948](https://doi.org/10.1056/NEJMoa2212948).

\[81] M. A. Mintun *et al.*, “Donanemab in Early Alzheimer’s Disease,” *New England Journal of Medicine*, vol. 384, no. 18, pp. 1691–1704, May 2021, doi: [10\.1056/NEJMoa2100708](https://doi.org/10.1056/NEJMoa2100708).

\[82] J. R. Sims *et al.*, “Donanemab in Early Symptomatic Alzheimer Disease: The TRAILBLAZER\-ALZ 2 Randomized Clinical Trial,” *JAMA*, Jul. 2023, doi: [10\.1001/jama.2023\.13239](https://doi.org/10.1001/jama.2023.13239).

\[83] S. Salloway *et al.*, “Two phase 3 trials of bapineuzumab in mild\-to\-moderate Alzheimer’s disease,” *New England Journal of Medicine*, vol. 370, no. 4, pp. 322–333, 2014, doi: [10\.1056/NEJMoa1304839](https://doi.org/10.1056/NEJMoa1304839).

\[84] R. Vandenberghe *et al.*, “Bapineuzumab for mild to moderate Alzheimer’s disease in two global, randomized, phase 3 trials,” *Alzheimer’s Research \& Therapy*, vol. 8, no. 1, p. 18, May 2016, doi: [10\.1186/s13195\-016\-0189\-7](https://doi.org/10.1186/s13195-016-0189-7).

\[85] S. Ostrowitzki *et al.*, “Evaluating the Safety and Efficacy of Crenezumab vs Placebo in Adults With Early Alzheimer Disease: Two Phase 3 Randomized Placebo\-Controlled Trials,” *JAMA Neurology*, vol. 79, no. 11, pp. 1113–1121, Nov. 2022, doi: [10\.1001/jamaneurol.2022\.2909](https://doi.org/10.1001/jamaneurol.2022.2909).

\[86] R. S. Doody *et al.*, “Phase 3 trials of solanezumab for mild\-to\-moderate Alzheimer’s disease,” *New England Journal of Medicine*, vol. 370, no. 4, pp. 311–321, 2014, doi: [10\.1056/NEJMoa1312889](https://doi.org/10.1056/NEJMoa1312889).

\[87] L. S. Honig *et al.*, “Trial of Solanezumab for Mild Dementia Due to Alzheimer’s Disease,” *New England Journal of Medicine*, vol. 378, no. 4, pp. 321–330, Jan. 2018, doi: [10\.1056/NEJMoa1705971](https://doi.org/10.1056/NEJMoa1705971).

\[88] S. Salloway *et al.*, “A trial of gantenerumab or solanezumab in dominantly inherited Alzheimer’s disease,” *Nature Medicine*, vol. 27, no. 7, pp. 1187–1196, Jul. 2021, doi: [10\.1038/s41591\-021\-01369\-8](https://doi.org/10.1038/s41591-021-01369-8).

\[89] S. Ostrowitzki *et al.*, “A phase III randomized trial of gantenerumab in prodromal Alzheimer’s disease,” *Alzheimer’s Research \& Therapy*, vol. 9, no. 1, p. 95, Dec. 2017, doi: [10\.1186/s13195\-017\-0318\-y](https://doi.org/10.1186/s13195-017-0318-y).

\[90] M. B. Rogers, “Signs of Lasting Benefit From Amyloid Immunotherapy?,” *Alzforum News*, 2025, Available: [https://www.alzforum.org/news/conference\-coverage/signs\-lasting\-benefit\-amyloid\-immunotherapy](https://www.alzforum.org/news/conference-coverage/signs-lasting-benefit-amyloid-immunotherapy)

\[91] C. V. Cauwenberghe, C. V. Broeckhoven, and K. Sleegers, “The genetic landscape of Alzheimer disease: Clinical implications and perspectives,” *Genetics in Medicine*, vol. 18, no. 5, pp. 421–430, May 2016, doi: [10\.1038/gim.2015\.117](https://doi.org/10.1038/gim.2015.117).

\[92] T. Jonsson *et al.*, “A mutation in APP protects against Alzheimer’s disease and age\-related cognitive decline,” *Nature*, vol. 488, no. 7409, pp. 96–99, Aug. 2012, doi: [10\.1038/nature11283](https://doi.org/10.1038/nature11283).

\[93] J. A. Maloney *et al.*, “Molecular Mechanisms of Alzheimer Disease Protection by the A673T Allele of Amyloid Precursor Protein\*,” *Journal of Biological Chemistry*, vol. 289, no. 45, pp. 30990–31000, Nov. 2014, doi: [10\.1074/jbc.M114\.589069](https://doi.org/10.1074/jbc.M114.589069).

\[94] D. Scheuner *et al.*, “Secreted amyloid β–protein similar to that in the senile plaques of Alzheimer’s disease is increased in vivo by the presenilin 1 and 2 and APP mutations linked to familial Alzheimer’s disease,” *Nature Medicine*, vol. 2, no. 8, pp. 864–870, Aug. 1996, doi: [10\.1038/nm0896\-864](https://doi.org/10.1038/nm0896-864).

\[95] B. De Strooper *et al.*, “Deficiency of presenilin\-1 inhibits the normal cleavage of amyloid precursor protein,” *Nature*, vol. 391, no. 6665, pp. 387–390, Jan. 1998, doi: [10\.1038/34910](https://doi.org/10.1038/34910).

\[96] S. S. Plotkin and N. R. Cashman, “Passive immunotherapies targeting A*β* and tau in Alzheimer’s disease,” *Neurobiology of Disease*, vol. 144, p. 105010, Oct. 2020, doi: [10\.1016/j.nbd.2020\.105010](https://doi.org/10.1016/j.nbd.2020.105010).

\[97] B. Falcon *et al.*, “Tau filaments from multiple cases of sporadic and inherited Alzheimer’s disease adopt a common fold,” *Acta Neuropathologica*, vol. 136, no. 5, pp. 699–708, Nov. 2018, doi: [10\.1007/s00401\-018\-1914\-z](https://doi.org/10.1007/s00401-018-1914-z).

\[98] T. Guo, D. Korman, S. L. Baker, S. M. Landau, and W. J. Jagust, “Longitudinal Cognitive and Biomarker Measurements Support a Unidirectional Pathway in Alzheimer’s Disease Pathophysiology,” *Biological Psychiatry*, vol. 89, no. 8, pp. 786–794, Apr. 2021, doi: [10\.1016/j.biopsych.2020\.06\.029](https://doi.org/10.1016/j.biopsych.2020.06.029).

\[99] L. Wang *et al.*, “Evaluation of Tau Imaging in Staging Alzheimer Disease and Revealing Interactions Between β\-Amyloid and Tauopathy,” *JAMA Neurology*, vol. 73, no. 9, pp. 1070–1077, Sep. 2016, doi: [10\.1001/jamaneurol.2016\.2078](https://doi.org/10.1001/jamaneurol.2016.2078).

\[100] D. A. Bennett, J. A. Schneider, R. S. Wilson, J. L. Bienias, E. Berry\-Kravis, and S. E. Arnold, “Amyloid mediates the association of apolipoprotein E e4 allele to cognitive function in older people,” *Journal of Neurology, Neurosurgery \& Psychiatry*, vol. 76, no. 9, pp. 1194–1199, Sep. 2005, doi: [10\.1136/jnnp.2004\.054445](https://doi.org/10.1136/jnnp.2004.054445).

\[101] W. J. Lee *et al.*, “Regional Aβ\-tau interactions promote onset and acceleration of Alzheimer’s disease tau spreading,” *Neuron*, vol. 110, no. 12, pp. 1932–1943\.e5, Jun. 2022, doi: [10\.1016/j.neuron.2022\.03\.034](https://doi.org/10.1016/j.neuron.2022.03.034).

\[102] M. Jin, N. Shepardson, T. Yang, G. Chen, D. Walsh, and D. J. Selkoe, “Soluble amyloid β\-protein dimers isolated from Alzheimer cortex directly induce Tau hyperphosphorylation and neuritic degeneration,” *Proceedings of the National Academy of Sciences*, vol. 108, no. 14, pp. 5819–5824, Apr. 2011, doi: [10\.1073/pnas.1017033108](https://doi.org/10.1073/pnas.1017033108).

\[103] B. Vasconcelos *et al.*, “Heterotypic seeding of Tau fibrillization by pre\-aggregated Abeta provides potent seeds for prion\-like seeding and propagation of Tau\-pathology in vivo,” *Acta Neuropathologica*, vol. 131, no. 4, pp. 549–569, Apr. 2016, doi: [10\.1007/s00401\-015\-1525\-x](https://doi.org/10.1007/s00401-015-1525-x).

\[104] R. E. Bennett *et al.*, “Enhanced Tau Aggregation in the Presence of Amyloid β,” *The American Journal of Pathology*, vol. 187, no. 7, pp. 1601–1612, Jul. 2017, doi: [10\.1016/j.ajpath.2017\.03\.011](https://doi.org/10.1016/j.ajpath.2017.03.011).

\[105] T. Bolmont *et al.*, “Induction of tau pathology by intracerebral infusion of amyloid\-β\-containing brain extract and by amyloid\-β deposition in APP × tau transgenic mice,” *The American Journal of Pathology*, vol. 171, no. 6, pp. 2012–2020, Dec. 2007, doi: [10\.2353/ajpath.2007\.070403](https://doi.org/10.2353/ajpath.2007.070403).

\[106] L. A. Gomes *et al.*, “Aβ\-induced acceleration of Alzheimer\-related τ\-pathology spreading and its association with prion protein,” *Acta Neuropathologica*, vol. 138, no. 6, pp. 913–941, Dec. 2019, doi: [10\.1007/s00401\-019\-02053\-5](https://doi.org/10.1007/s00401-019-02053-5).

\[107] J. Götz, F. Chen, J. van Dorpe, and R. M. Nitsch, “Formation of Neurofibrillary Tangles in P301L Tau Transgenic Mice Induced by Aβ42 Fibrils,” *Science*, vol. 293, no. 5534, pp. 1491–1495, Aug. 2001, doi: [10\.1126/science.1062097](https://doi.org/10.1126/science.1062097).

\[108] D. E. Hurtado *et al.*, “Aβ accelerates the spatiotemporal progression of tau pathology and augments tau amyloidosis in an Alzheimer mouse model,” *American Journal of Pathology*, vol. 177, no. 4, pp. 1977–1988, Oct. 2010, doi: [10\.2353/ajpath.2010\.100346](https://doi.org/10.2353/ajpath.2010.100346).

\[109] J. Lewis *et al.*, “Enhanced Neurofibrillary Degeneration in Transgenic Mice Expressing Mutant Tau and APP,” *Science*, vol. 293, no. 5534, pp. 1487–1491, Aug. 2001, doi: [10\.1126/science.1058189](https://doi.org/10.1126/science.1058189).

\[110] T. Li *et al.*, “The neuritic plaque facilitates pathological conversion of tau in an Alzheimer’s disease mouse model,” *Nature Communications*, vol. 7, no. 1, p. 12082, Jul. 2016, doi: [10\.1038/ncomms12082](https://doi.org/10.1038/ncomms12082).

\[111] A. M. Pooler *et al.*, “Amyloid accelerates tau propagation and toxicity in a model of early Alzheimer’s disease,” *Acta Neuropathologica Communications*, vol. 3, no. 1, p. 14, Mar. 2015, doi: [10\.1186/s40478\-015\-0199\-x](https://doi.org/10.1186/s40478-015-0199-x).

\[112] I.\-C. Stancu *et al.*, “Tauopathy contributes to synaptic and cognitive deficits in a murine model for Alzheimer’s disease,” *The FASEB Journal*, vol. 28, no. 6, pp. 2620–2631, 2014, doi: [10\.1096/fj.13\-246702](https://doi.org/10.1096/fj.13-246702).

\[113] R. M. Cohen *et al.*, “A Transgenic Alzheimer Rat with Plaques, Tau Pathology, Behavioral Impairment, Oligomeric Aβ, and Frank Neuronal Loss,” *Journal of Neuroscience*, vol. 33, no. 15, pp. 6245–6256, Apr. 2013, doi: [10\.1523/JNEUROSCI.3672\-12\.2013](https://doi.org/10.1523/JNEUROSCI.3672-12.2013).

\[114] ClinicalTrials.gov, “DIAN‑TU Amyloid Removal Trial (ART): A Phase IIIb/IV Open‑Label Study of Lecanemab in Dominantly Inherited Alzheimer’s Disease.” ClinicalTrials.gov, NCT06384573, Jun. 10, 2024\. Accessed: Jul. 24, 2025\. \[Online]. Available:<https://clinicaltrials.gov/study/NCT06384573>

\[115] ClinicalTrials.gov, “AHEAD 3–45 Study: A Phase 3 Placebo‑Controlled, Double‑Blind, Parallel‑Arm, 216‑Week Trial (with Extension) Evaluating BAN2401 (Lecanemab) in Preclinical/Early Preclinical Alzheimer’s Disease (A45 \& A3 Trials).” ClinicalTrials.gov, NCT04468659, Jul. 14, 2020\. Accessed: Jul. 24, 2025\. \[Online]. Available:<https://clinicaltrials.gov/study/NCT04468659>

\[116] C. J. Mummery *et al.*, “Tau\-targeting antisense oligonucleotide MAPTRx in mild Alzheimer’s disease: A phase 1b, randomized, placebo\-controlled trial,” *Nature Medicine*, vol. 29, no. 6, pp. 1437–1447, Jun. 2023, doi: [10\.1038/s41591\-023\-02326\-3](https://doi.org/10.1038/s41591-023-02326-3).

\[117] A. L. Edwards *et al.*, “Exploratory Tau Biomarker Results From a Multiple Ascending\-Dose Study of BIIB080 in Alzheimer Disease: A Randomized Clinical Trial,” *JAMA Neurology*, vol. 80, no. 12, pp. 1344–1352, Dec. 2023, doi: [10\.1001/jamaneurol.2023\.3861](https://doi.org/10.1001/jamaneurol.2023.3861).

\[118] S. S. Dominy *et al.*, “Porphyromonas gingivalis in Alzheimer’s disease brains: Evidence for disease causation and treatment with small\-molecule inhibitors,” *Science Advances*, vol. 5, no. 1, p. eaau3333, Jan. 2019, doi: [10\.1126/sciadv.aau3333](https://doi.org/10.1126/sciadv.aau3333).

\[119] D. M. Cairns, N. Rouleau, R. N. Parker, K. G. Walsh, L. Gehrke, and D. L. Kaplan, “A 3D human brain–like tissue model of herpes\-induced Alzheimer’s disease,” *Science Advances*, vol. 6, no. 19, p. eaay8828, May 2020, doi: [10\.1126/sciadv.aay8828](https://doi.org/10.1126/sciadv.aay8828).

\[120] S. J. Soscia *et al.*, “The Alzheimer’s Disease\-Associated Amyloid β\-Protein Is an Antimicrobial Peptide,” *PLOS ONE*, vol. 5, no. 3, p. e9505, Mar. 2010, doi: [10\.1371/journal.pone.0009505](https://doi.org/10.1371/journal.pone.0009505).

\[121] K. Bourgade *et al.*, “Β\-Amyloid peptides display protective activity against the human Alzheimer’s disease\-associated herpes simplex virus\-1,” *Biogerontology*, vol. 16, no. 1, pp. 85–98, Feb. 2015, doi: [10\.1007/s10522\-014\-9538\-8](https://doi.org/10.1007/s10522-014-9538-8).

\[122] P. Spitzer *et al.*, “Amyloidogenic amyloid\-β\-peptide variants induce microbial agglutination and exert antimicrobial activity,” *Scientific Reports*, vol. 6, no. 1, p. 32228, Sep. 2016, doi: [10\.1038/srep32228](https://doi.org/10.1038/srep32228).

\[123] C. Piller, “Blots on a field? A neuroscience image sleuth finds signs of fabrication in scores of Alzheimer’s articles, threatening a reigning theory of the disease.” Accessed: Jul. 23, 2025\. \[Online]. Available: [https://www.science.org/content/article/potential\-fabrication\-research\-images\-threatens\-key\-theory\-alzheimers\-disease](https://www.science.org/content/article/potential-fabrication-research-images-threatens-key-theory-alzheimers-disease)

\[124] D. Elton, “When ‘weak links’ in science matter – high profile fraud in Alzheimer’s disease research.” Oct. 20, 2024\. Available [here](https://moreisdifferent.blog/p/when-weak-links-in-science-matter).

\[125] M. B. Rogers, “Sylvain Lesné, who found Aβ\*56, accused of image manipulation,” *Alzforum.org*, Jul. 2022, Available: [https://www.alzforum.org/news/community\-news/sylvain\-lesne\-who\-found\-av56\-accused\-image\-manipulation](https://www.alzforum.org/news/community-news/sylvain-lesne-who-found-av56-accused-image-manipulation)

\[126] J. Cummings, G. Lee, A. Ritter, M. Sabbagh, and K. Zhong, “Alzheimer’s disease drug development pipeline: 2020,” *Alzheimer’s \& Dementia: Translational Research \& Clinical Interventions*, vol. 6, no. 1, p. e12050, 2020, doi: [10\.1002/trc2\.12050](https://doi.org/10.1002/trc2.12050).

\[127] J. Cummings, Y. Zhou, G. Lee, K. Zhong, J. Fonseca, and F. Cheng, “Alzheimer’s disease drug development pipeline: 2024,” *Alzheimer’s \& Dementia: Translational Research \& Clinical Interventions*, vol. 10, no. 2, p. e12465, 2024, doi: [10\.1002/trc2\.12465](https://doi.org/10.1002/trc2.12465).

\[128] ClinicalTrials.gov, “Safety Study of Passive Immunization for Patients With Mild to Moderate Alzheimer’s Disease.” ClinicalTrials.gov, NCT00174525, May 09, 2012\. Accessed: Jul. 23, 2025\. \[Online]. Available:<https://clinicaltrials.gov/study/NCT00174525>