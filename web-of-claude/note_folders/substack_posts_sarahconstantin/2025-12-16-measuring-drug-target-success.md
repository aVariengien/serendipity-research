# Measuring Drug Target Success

*A data analysis experiment*

Published: 2025-12-16
Source: https://sarahconstantin.substack.com/p/measuring-drug-target-success

---

Modern drugs usually have known targets — molecules in the human body, which the drug works by chemically interacting with.

Historically, many drugs were discovered empirically, before their mechanism of action was known. Some drugs, like penicillin and aspirin, were identified as the active ingredients in natural products found to be effective (against bacteria and pain, respectively). But today it’s more common for drugs to be intentionally designed to target a specific molecule (often a protein) that’s already known to be causally involved in disease.

Often, drugs turn out to have different or alternative mechanisms of action than researchers initially supposed.[1](https://sarahconstantin.substack.com/p/measuring-drug-target-success#footnote-1-181813112) But you'll lose all credibility if you try to advance a drug withouta proposed mechanism; for better or for worse, molecular mechanisms of action are how we think about drug discovery.

So, where do drug targets come from? How do researchers decide which mechanisms to target?

Most of the time, drug development focuses on tried\-and\-true targets that have already proved successful in other drugs.

For new targets, there’s a range of types of evidence.

Sometimes, there’s genetic evidence. Mutations in a target gene might correlate with incidence or severity of the disease in human populations.

Sometimes there’s animal evidence. Mutations or knockouts/knockdowns of a target gene might affect an animal model of the disease, or a drug with that target might show efficacy in an animal model of disease.

Sometimes there’s in\-vitro evidence. At the cellular or molecular level, something is abnormal in the disease state[2](https://sarahconstantin.substack.com/p/measuring-drug-target-success#footnote-2-181813112), and we can trace this micro\-abnormality to abnormal levels, activities, or variants of a particular biomolecule.

“Validating” a target means assembling a body of evidence, of any of these types, that’s suggestive that if you alter the target you might alter the symptoms or course of the disease.

So a natural question is, are some targets better than others?

Can we do anything to *predict* drug success based on mechanism of action?

As [Ruxandra Teslo and Jack Scannell have recently pointed out](https://www.macroscience.org/p/to-get-more-effective-drugs-we-need), almost all the cost of developing a drug is spent in clinical trials. And most drugs fail clinical trials.

So the only ways to increase the ROI of drug development are to

1. make clinical trials cheaper (an important policy goal and the focus of the article), or
2. get better at “picking winners”, i.e. choose drug candidates early on that are more likely to succeed in the clinic.

The article also points out that once\-great hopes of “picking winners better”, like rational drug design, have not actually resulted in higher clinical success rates. The odds are against the a priori approach.

I fundamentally agree. There’s a reason we test drugs in humans, and it’s because most drug candidates that look good at a preclinical stage don’t turn out to work on human disease! There is no substitute for clinical experiment. And from an efficiency/abundance perspective, the case for making clinical trials easier and cheaper is overwhelming.

However, *even at the preclinical stage, some drug candidates are better than others*.

Drugs with genetically validated targets are more than twice as likely to succeed in the clinic.[3](https://sarahconstantin.substack.com/p/measuring-drug-target-success#footnote-3-181813112)[4](https://sarahconstantin.substack.com/p/measuring-drug-target-success#footnote-4-181813112)[5](https://sarahconstantin.substack.com/p/measuring-drug-target-success#footnote-5-181813112)

Also, and unsurprisingly, drugs with the same mechanism of action as those that have failed in the clinic before, are more likely to fail.

(The phenomenon of “me\-too” drugs is evidence of this in the other direction; when one drug succeeds, many other similar drugs with the same target tend to be pursued and often approved.)

Plausibly, there are “good targets”, which are causally essential to the disease, and “bad targets”, which aren’t; and plausibly, there is *some* signal available before a drug program goes to the clinic about how good the target is.

### Target Data From ClinicalTrials.gov and ChEMBL

The first step in investigating this question is simply to look at all the clinical drug trials, and all the drugs and their targets, and get some descriptive statistics.