# AI for Bio: State Of The Field

*In which I finally catch up on the New Hotness*

Published: 2024-08-30
Source: https://sarahconstantin.substack.com/p/ai-for-bio-state-of-the-field

---

[![](https://substackcdn.com/image/fetch/$s_!tq8H!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F352d1397-ea9b-4b75-b771-c2d0cc643f57_1024x1024.webp)](https://substackcdn.com/image/fetch/$s_!tq8H!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F352d1397-ea9b-4b75-b771-c2d0cc643f57_1024x1024.webp)

AI for biotech, particularly with drug discovery applications, has been used for more than a decade, with ambiguous success. But in the era of [foundation models](https://arxiv.org/abs/2108.07258)  we may have experienced a step change in what’s possible.

I used to work on AI\-for\-drug\-discovery years ago, at [Recursion](https://www.recursion.com/), where we sought to identify phenotypes of genetic diseases visible in microscopic images of cells, and screen for drugs that made the cells visually “look healthy” in the hopes that those drugs would also turn out to be effective against the symptoms of the disease.

Circa 2016, we were just beginning to transition from the old\-fashioned sort of machine learning based heavily on feature engineering, to the new “deep learning” paradigm with much larger neural nets. “Old\-school” machine learning was often accused of being nothing more than logistic regression in fancy VC\-funded branding, and there was often some truth to that. When our models worked best, they were picking up human\-interpretable phenotypes that a pathologist could probably have described decades ago: something like “this disease causes enlarged nuclei”. And, when we first started replacing the old models with deep neural nets, it wasn’t clear that the New Hotness was going to work better than the Old Standby.

But things have changed. Bigger, better models (often [Transformer\-](https://arxiv.org/abs/1706.03762)based) are everywhere in biotech. They genuinely seem to be changing the state of the art in drug (and biologic) development. And it’s past time to do a serious review of what’s become available and what it can and can’t do.

AI optimists who aren’t familiar with biotech are often wildly miscalibrated about what AI tools can do even in the best case scenario.

The average approved drug in the US costs $879\.3 million[1](https://sarahconstantin.substack.com/p/ai-for-bio-state-of-the-field#footnote-1-148042978) in R\&D expenses (counting the costs of failed drugs), and nearly 90% of that is spent on clinical trials. It’s legally, scientifically, and ethically necessary to test drugs on humans to see if they’re safe and effective. And while the ballooning cost of running clinical trials is a problem worth tackling in itself[2](https://sarahconstantin.substack.com/p/ai-for-bio-state-of-the-field#footnote-2-148042978), it’s inherently time\- and labor\-intensive to run valid experiments on human patients. An AI is never going to “design a drug” that you can give to patients right away. Even if the AI were a perfect all\-knowing oracle, pharmaceutical companies would still need to run animal and then human trials.

AI for biotech is attempting to automate and improve *particular sub\-problems* within that 10% of costs spent on drug discovery and preclinical research. This is hardly trivial, especially if it enables the development of new classesof drugs that were completely inaccessible before. But it does place AI hype in context.

An AI model’s value to the drug discovery process is bounded by:

* the labor cost of the time it saves on more manual processes
* the cost it saves on any experiments it can fully replace
* the cost of any *failed* experiments it can prevent from being done altogether
* the value of any new successful therapies that would not even have been attempted without the model

If the model tells you to do something you would probably have done anyway, it’s useless. If the model *replaces* something you would have needed to do manually, it’s somewhat useful. If the model *increases your odds of a successful therapy*, it’s extremely useful, and if it *adds* successful therapies it’s world\-changing.

With that paradigm set up, let’s dig into the details.

This won’t be an exhaustive list of models, or an in\-depth evaluation of their performance, but an overview of the big, influential, and buzzy and a summary of what they do.

## Structure Prediction Models

One class of AI models with biotech applications tackles one of the most classically fiendish problems in computational biology: given a sequence (RNA, DNA, or protein), how will it fold up into a 3D structure?

From a pharmaceutical perspective, we care about this because most drugs work by chemically interacting with proteins (or, sometimes, with nucleic acids like DNA/RNA) and the interaction depends on the structure of the biological macromolecule in question. Also, some drugs are themselvesbiological macromolecules (proteins, peptides, nucleic acid sequences, etc) and it’s important to understand their structure to predict what they’ll do in the body.

From a basic research perspective, structural biology helps us understand how the molecular machinery of living things works. Structure clarifies function: determining the double\-helix shape of DNA revealed how genetic information is encoded and replicated in a cell. The majority of human proteins still have no experimentally determined structure, and we keep discovering new types of folded\-up RNAs, each with its own cellular function.[3](https://sarahconstantin.substack.com/p/ai-for-bio-state-of-the-field#footnote-3-148042978)

### AlphaFold2

Released [in 2022 by DeepMind](https://deepmind.google/discover/blog/putting-the-power-of-alphafold-into-the-worlds-hands/), AlphaFold2 is a protein structure model: given a protein’s amino acid sequence, the model predicts its structure.

Trained on hundreds of thousands of known protein sequences and structure, the model promises to be able to predict structure on [more than 3/4 of the sequence of 43\.8% of human proteins.](https://www.nature.com/articles/s41586-021-03828-1) AlphaFold2 isn’t the first protein structure prediction model by any means, but it proved [more accurate than any other competitor, by a large margin](https://www.nature.com/articles/s41586-021-03819-2), in a recent protein structure prediction contest (CASP14\).

#### What Can You Do With It?

Protein structure prediction, first of all, can tell you something about basic science: understanding how proteins are shaped can help us understand how they work.

It’s also useful for rational drug design. If you know a protein’s structure, you can begin to study what sorts of molecules might interact with it and alter its function.

But is it *so* good that its predictions can be used in place of experimentally\-determined protein structures?

It’s complicated.

First, the bad news: it turns out that [if you take](https://www.science.org/content/blog-post/screening-against-alphafold-models-maybe-better-it-looks) model\-predicted structures as a starting point, and use ligand\-binding computational models to predict which drugs will bind to them, “there are numerous known ligands for each receptor that do not show up as hits.” In other words, screening “against” the model\-predicted structure instead of the experimentally\-determined structure produces numerous false negatives.

On the other hand, [that same experiment](https://www.science.org/doi/10.1126/science.adn6354) also showed that ligands computationally predicted to bind to protein targets had about a 50% chance of actually binding in experiments, whether the protein structure used was the “real” experimentally\-derived structure or AF2’s predicted structure. In other words, if you hadn’t determined the experimental structure at all, using the AI’s guess would get you just as many initial hits. That might enable developing drugs that target proteins whose structure is hard to determine.

### ESM3

Created by [Evolutionary Scale](https://evolutionaryscale.ai/), a [newly\-launched](https://press.aboutamazon.com/aws/2024/6/evolutionaryscale-launches-with-esm3-a-milestone-ai-model-for-biology) frontier AI company, ESM3 is a big (98B parameter) language model trained on protein sequence, structure, and function data, drawn from [2\.78 billion natural proteins.](https://www.biorxiv.org/content/10.1101/2024.07.01.600583v1.full)

If you prompt it with a given sequence, it can output a predicted protein structure; if you prompt it with a structure, it can predict a sequence to match.

As their demonstration in the paper, they had the AI “invent” a new variant on green fluorescent protein (GFP). It’s known which amino acids (and positions) are responsible for making natural GFP glow; the researchers input those requirements and allowed the AI to fill in the rest of the protein, and came up with some responses that had substantially different sequences from natural GFP but still produced the fluorescence effect.

#### What Can You Do With It?

If you want to design “custom” proteins to produce a desired effect, *and* if you already knowat an exact structural level which features are required for that effect, ESM3 would allow you to generate ideas. (You’d still have to test them experimentally.)

If you want to predict protein structure from function, ESM3 can do that too. (The paper doesn’t compare its accuracy to other leading methods).

Using the ESM models to “mutate” antibodies [results in marked performance improvements](https://www.nature.com/articles/s41587-023-01763-2) in the AI\-modified versions over clinically approved human antibodies, suggesting that you can make antibodies work better by making them more “normal” (with respect to the training data.) As antibodies are the most common type of protein used as pharmaceuticals, this is a major practical use. And indeed, there are already [companies](https://www.absci.com/) based on producing “AI\-designed antibodies” (though, of course, when a drug is announced as “AI\-designed”, that means AI played *any* role in its development, not that AI was indispensable.)

But ESM3 *can’t,* in general, solve for “I want a protein that fluoresces at this wavelength” or “I want an antibody for such\-and\-such protein”. When it comes to generating proteins “to spec”, you need a lot of knowledge about the “spec” before the model will even *attempt* to give you an answer.

### Evo

Arc Institute’s [Evo](https://arc-website-git-foundation-model-tool-arc-institute.vercel.app/news/blog/evo) is in the same category: a DNA/RNA/protein foundation model, somewhat smaller than ESM3 (7B parameters), [based on](https://www.biorxiv.org/content/10.1101/2024.02.27.582234v2.full) the genomes of 80,000 bacterial and archaeal species.

It can function as “autocomplete” for DNA, RNA, and protein sequences; given a prompt, it can predict the rest of the sequence.

#### What Can You Do With It?

Apparently, the more likely a sequence is to be autogenerated by the model, the “better” the sequence is for a lot of purposes — mutated *E. coli* with “more likely” mutations survive better, “more likely” mutations of non\-coding RNAs score higher on various metrics of “fitness”, etc.

This has some practical application: if generative models like Evo give you some sense of how normal or biologically plausible a sequence is, and if you expect “normal” sequences to work better in general, then Evo could be a filtering step on synthetic biology. Again, it *can’t replace the physical experiment*, but it could enable researchers to find success faster, for instance at creating new CRISPR variants for gene editing.

## Protein and Peptide Binding Models

### RFDiffusion

Produced by David Baker’s lab at the University of Washington, [RFDiffusion](https://www.bakerlab.org/2023/07/11/diffusion-model-for-protein-design/) is a generative model for proteins based on the older RoseTTAFold structure prediction model.

Trained on the Protein Data Bank, RFDiffusion allows the user to generate a protein around a specific desired motif, like a small molecule binding site or enzyme active site. For instance, when the model was [asked to produce](https://www.biorxiv.org/content/10.1101/2022.12.09.519842v1.full.pdf) candidate proteins that would bind nickel ions, 37/44 (84%) of the model\-generated proteins indeed bound nickel ions in a physical experiment.

#### What Can You Do With It?

The ability to design custom proteins is valuable. Custom\-designed enzymes can catalyze industrial processes or break down environmental toxins; custom antibodies designed for a selected target can be pharmaceutical drugs, diagnostic biosensors, or simply labels used in basic research.

For instance, RFDiffusion has been used to generate proteins that bind to certain peptides[4](https://sarahconstantin.substack.com/p/ai-for-bio-state-of-the-field#footnote-4-148042978).

### RESP AI

Developed by researchers at UCSD, [RESP](https://www.nature.com/articles/s41467-023-36028-8) is an antibody\-specific model trained on over 3 billion B\-cell receptor sequences, which was able to suggest improvements to a well\-known cancer antibody drug (atezolizumab, or anti\-PD1\) that made the new antibody bind its target 17 times tighter.

RESP isn’t purely computational: it’s a combined AI and experimental pipeline. For each target, an experiment with yeast is run, seeing how well a variety of antibody variants bind the target protein. Only then is a model generated for predicting binding affinity from antibody sequence, and then “run in reverse” to generate the *best* antibodies, by predicted affinity.

#### What Can You Do With It?

The oldest way to make an antibody is to give an animal an antigen, and then harvest the animal’s own immune system’s antibody response. This, of course, is clunky and expensive. More modern antibody discovery methods use high\-throughput screens, testing lots of variant candidates to see how potently and specifically they bind to the target.

RESP’s system doesn’t completely get away from experimental screens, but it does make screening more efficient. Instead of brute\-force trial and error, you get suggestions selected for high predicted performance, and you screen *those*.

It might well reduce the time to discovery of a successful antibody, increase the probability of finding one, or optimize a candidate antibody so it’s more effective and less prone to causing side effects by the time it enters the clinic.

## Molecular Binding Models

Predicting how strongly two molecules will interact chemically is key to drug discovery. You want a small molecule drug to bind to its target (usually a protein) but not to interfere much with the function of any other molecules in the body.

Computational methods for predicting molecular interactions didn’t start with AI or machine learning; for decades, medicinal chemists have used deterministic models based on electrochemical interactions that predict binding affinities. But these models aren’t very accurate, so designing drug molecules also depends heavily on experimentation and domain knowledge.

Pharma companies are betting that AI methods will work better; for instance, Merck has released [AIDDISON](https://www.emdgroup.com/en/research/science-space/envisioning-tomorrow/future-of-scientific-work/aiddison.html), AI\-based drug discovery software trained on its proprietary experimental data.

### AlphaFold3

[Released in 2024](https://blog.google/technology/ai/google-deepmind-isomorphic-alphafold-3-ai-model/), AlphaFold3 is more general, predicting the 3D structure of DNA and RNA as well as proteins from their sequences. This allows it to predict how proteins and nucleic acids bind to form complexes, and even predict ligand binding between proteins and small molecules.

It gets up to [nearly 80% accuracy](https://www.nature.com/articles/s41586-024-07487-w) at predicting protein\-ligand and protein\-protein interactions, which is strikingly better than the competitor models.

#### What Can You Do With It?

AlphaFold3 can do everything AlphaFold2 can do, plus additionally help screen potential drugs (and antibodies and other biologics) for activity against their targets.

It’s not accurate enough to replace experiments altogether, but it might be able to accelerate the process of finding early\-stage hits, by serving as a screen for deciding which candidates to test experimentally.

### BioSimDock

Produced by Deep Origin, [BioSimDock](https://www.deeporigin.com/blog/we-spill-the-beans-deep-origins-ai-and-physics-based-models-for-drug-discovery) is a proprietary model for predicting small molecule binding affinity to proteins. The company hasn’t disclosed much about its architecture, but does observe that it correctly detects 6 of 13 “true” binding molecules, out of a library of 100,000 molecules, and has a correlation of 0\.89 between predicted and true binding affinity, significantly outperforming other computer\-based ligand\-binding predictors.

#### What Can You Do With It?

Virtual molecule screening allows a vast expansion in the space of possible small\-molecule drug candidates. The largest physical screening libraries include about a million molecules; AI\-based simulated screening can churn through more than ten *billion* molecules in a few days. Choosing computationally high\-scoring molecules to then screen experimentally can increase the odds of a hit by several\-fold.

### MoLFormerXL

Developed at [IBM Research](https://research.ibm.com/blog/molecular-transformer-discovery), MoLFormerXL is trained on over a billion molecules to predict various chemical properties from a molecule’s structure, [including](https://arxiv.org/pdf/2106.09553) toxicity, water\-solubility, and binding affinity to certain targets. It’s a pre\-trained chemical language model that has to be fine\-tuned specifically on these downstream tasks, just as a general language model can perform better at a text\-classification task than a special\-purpose model trained on the classification data alone.

#### What Can You Do With It?

It’s not clear to me from the paper how MoLFormerXL’s binding\-affinity predictions compare to other molecular\-binding simulations including more deterministic (i.e. not machine\-learned) predictions.

In general, a good general\-purpose embedding from a very large dataset can generally improve on all sorts of special\-purpose predictive models, but without more information it’s hard to say by how much.

Ultimately the biotech\-relevant application of MoLFormerXL, like all in\-silico screening models, would be to provide preliminary libraries of predicted\-good molecules to follow up with experimental screens.

### BELKA

In a recent [Kaggle competition](https://www.kaggle.com/competitions/leash-BELKA/overview) on a very large dataset, where the challenge was to predict which small molecules would bind to which proteins, *[none](https://leashbio.substack.com/p/belka-results-suggest-computers-can)* [of the contestants](https://leashbio.substack.com/p/belka-results-suggest-computers-can) were able to extrapolate from a training set based around one core molecule structure to a test set based on a different chemical structure. Even the contest winners did no better than chance on the novel structures.

#### What Can You Do With It?

Negative results are disappointing, but ultimately useful. If we don’t have AI models that predict small molecule binding to targets, that tells us we need bigger, better datasets with more diverse molecules before we have any hope of predicting the behavior of arbitrary small\-molecule drug candidates.

Small\-molecule binding may ultimately be a harder problem than protein\-protein or protein\-nucleic acid binding. While biological macromolecules are all derived from the same set of ancestors of life on Earth, the set of all possible *chemicals* is vastly more diverse.

## Cell Models

### CZI’s Virtual Cells

The [Chan Zuckerberg Initiative](https://chanzuckerberg.com/science/technology/virtual-cells/) is working on what they call a “virtual cell”. While they haven’t released any papers yet, their approach seems to be building a foundation model around microscopic cell imaging, and single\-cell RNA, DNA, and protein data.

#### What Can You Do With It?

Speculatively, a foundation model for cell data would be able to do things like:

* cluster cells as “similar” based on their embedding similarity, making “cell type” determinations more objective

	+ since cancer is a “cell type” of sorts, this also has applications to cancer classification
* generate “typical” data for a cell given some of its features; compare how anomalous the cell is from what it “should” look like, which may give clues to disease phenotypes

### Phenom\-Beta

Phenom\-Beta, Recursion’s [generative model for cell microscopy images](https://www.rxrx.ai/phenom#:~:text=We%20call%20this%20model%20Phenom-Beta.%20It%20flexibly%20processes,create%20a%20meaningful%20representation%20of%20the%20input%20image.), is a [vision transformer](https://en.wikipedia.org/wiki/Vision_transformer), trained to “autocomplete” images from incomplete patches. It provides a natural embedding of cell images, such that cells that are “similar” in the embedding are also similar in gene expression along biologically related pathways.

#### What Can You Do With It?

Good embeddings for cell images are important tools for phenotypic screening.

The premise of phenotypic screening is that you’ll get better success in the clinic by screening for drugs that affect the *disease state*, rather than drugs that interact with a single molecular target. However, since you can’t affordably test millions of compounds on millions of sick mice, you generally need some kind of experimental model to represent the disease state, typically based on cells in a petri dish.

The most traditional example of phenotypic screening is in cancer; instead of looking for drugs that interact with a single target molecule hypothesized to be involved in cancer, you can simply “skip ahead” to testing lots of drugs in parallel to see if they kill or slow the growth of cancer cells (and leave healthy cells undamaged.)

A subtler sort of phenotypic screening involves identifying differences between the microscopic appearance of diseased and healthy cells, and screening for drugs that make diseased cells *look* like healthy cells.

But for that, you need a computational definition of “look like”. A measure of similarity.

Simply comparing pixel\-by\-pixel values isn’t very useful; most of the information in a picture is redundant (eg the pixel right next to a black pixel is likely to be black)[5](https://sarahconstantin.substack.com/p/ai-for-bio-state-of-the-field#footnote-5-148042978) so you want ways to compress the *important* information in an image.

Transformer\-based embeddings are generally very good at surfacing intuitively similar images, texts, and so on; you can see this by how well generative AI tools can “autocomplete” a plausible extrapolation from a prompt, similar to other examples it’s seen before. So it makes sense that you can use them to recognize similar cells.

This could also be useful for stem cell and developmental biology; if you want to coax stem cells to differentiate to be “more like” a target cell type, image\-based similarity measurements could tell you whether you’re on the right track.[6](https://sarahconstantin.substack.com/p/ai-for-bio-state-of-the-field#footnote-6-148042978)

### VISTA\-2D

NVIDIA’s [recently released foundation model](https://developer.nvidia.com/blog/advancing-cell-segmentation-and-morphology-analysis-with-nvidia-ai-foundation-model-vista-2d/), VISTA\-2D, attacks a surprisingly difficult problem in biology: *cell segmentation*, or automatically drawing boundaries around each cell in a microscope image.

It’s odd that this is so difficult, given that it’s easy for the human eye to see where the cells are, but it’s extremely hard to get an image\-processing pipeline to, for instance, count the number of cells in a sample in a way that’s competitive on accuracy and price with [manual counting](https://en.wikipedia.org/wiki/Cell_counting). These days, state\-of\-the\-art segmentation models can have precision over 90% on benchmark datasets, and most of them are boosted slightly by incorporating a pretrained foundation model like VISTA\-2D.

#### What Can You Do With It?

If you’re making automated analyses of many, many microscopic images of cells — for instance, in [phenotypic screening](https://en.wikipedia.org/wiki/Phenotypic_screening), or in brain mapping — the first order of business is segmenting the cells.

## Target Discovery Models

“Target discovery” is the first stage in drug discovery, and the closest to basic research. It refers to identifying good drug *targets* for a disease — for instance, learning that drugs that target the [GLP\-1 receptor](https://en.wikipedia.org/wiki/Glucagon-like_peptide-1_receptor) can be expected to have an effect on diabetes. Normally it takes many years of experiments to gain enough understanding of the disease to identify a credible target. Whole careers can be spent on a particular target or molecular pathway. So the idea that an AI model could automate all that away is kind of ludicrous. But people certainly try.

### PandaOmics

Developed by [Insilico Medicine](https://insilico.com/), [PandaOmics](https://insilico.com/pandaomics) is a platform that promises to infer targets from “omics” data[7](https://sarahconstantin.substack.com/p/ai-for-bio-state-of-the-field#footnote-7-148042978), as well as text information from databases, publications, etc.

It is incredibly difficult to trust tests of the performance of such a flexible platform. InSilico Medicine’s own [paper](https://www.frontiersin.org/journals/aging-neuroscience/articles/10.3389/fnagi.2022.914017/full) “validating” PandaOmics in the context of [ALS](https://en.wikipedia.org/wiki/ALS) says:

> **Using over 20 AI and bioinformatics models**, PandaOmics ranks targets based on their target\-disease associations as well as information on druggability, developmental state and tissue specificity. **By customizing different filter settings**, 17 high\-confidence and 11 novel candidates (28 in total) were selected as potential ALS therapeutic targets.

This is a giant red flag for cherry\-picking. Of the 28 candidate genes, 9 could produce “strong rescue” in a fly model of ALS when knocked out; all had been previously identified in published meta\-analyses of ALS.

#### What Can You Do With It?

It’s plausible that it can be useful to use a software platform to integrate published information and “omics” data to rank disease targets according to an impartial algorithmic rubric.

But InSilico doesn’t even attempt to prove that their software outperforms the obvious comparison point — a domain expert hand\-picking targets.

Also, obviously, since it relies on *reports of other people’s experiments*, it hardly supersedes those experiments. If you use an LLM to analyze the research literature, you can speed up your own understanding, but somebody still has to perform those experiments in the first place.

## Conclusions

There’s a ton of AI hype in biotech, and a quieter but still very present drumbeat of skepticism.

Part of the problem with AI is that it’s extremely easy to declare victory without having accomplished something impressive. You can claim an “AI\-discovered drug” if you use AI in any part of the development process, even if you could have gotten comparable results without the AI. You can claim that your AI model “predicts” something successfully by carefully massaging the training and test data.

Some well\-studied problems in biology, like protein structure prediction, have rigorous benchmark contests, such that it’s a substantial achievement to come up with a winning model. We know AlphaFold is “actually good” because it crushes the competition on the same publicly available benchmarks that have been used for protein structure prediction for years.

But the typical paper (much less the typical press release) touting an AI model for a biological application isn’t up to that standard.

Regardless, in general it seems clear that we *do* have some contexts where large generative AI models clearly make predictions better than chance and better than older computational models.

How much does that *matter*?

* **Automating Labor**: Yes, AI models in drug discovery/development will automate many tedious manual processes.
* **Simulating Experiments**: No, there aren’t many cases where we have confidence that an AI\-predicted result is reliable enough that you don’t need to check it with a physical experiment.
* **Prioritizing Experiments**: This one’s the million\-dollar question. If an AI model *ranks* candidates effectively by quality, will that get drug discovery teams to a hit faster than traditional screening methods? It’s plausible that this will work for proteins (including antibodies). One AstraZeneca drug discovery researcher estimated that a 20% reduction in the costs of the earliest stages of drug development would be worth about $100M per drug \-\- a rounding error compared to the impact of increasing the chances of success in the clinic, but still enough to make AI drug discovery tools quite valuable.[8](https://sarahconstantin.substack.com/p/ai-for-bio-state-of-the-field#footnote-8-148042978)
* **Making New Types Of Drug Possible**: This would be the most valuable application, but so far we haven’t seen strong examples of new drug classes or “undruggable” targets being opened up by AI methods. There are some early promising indications, like a graph network model that identified “cryptic pockets” in proteins not previously thought to have any binding sites for drugs.[9](https://sarahconstantin.substack.com/p/ai-for-bio-state-of-the-field#footnote-9-148042978) But the ultimate test of relevance will be the discovery of *successful* new drug classes or targets.

Occasionally I encounter people who believe unrealistic things about what AI can deliver for biotech, as though a computer program could design a drug molecule and patients could immediately start taking it. Nobody in the field is seriously trying to skip over animal experiments or human clinical trials; there are simply too many unknown\-unknowns for it to be practical to computationally “simulate” the effect of a drug on a living organism.

However, there are very real advances in AI for biotech, particularly when it comes to predicting protein structure and protein\-protein interactions. Tools like AlphaFold are now used near\-universally and I don’t think they’re going away any time soon.

Predicting small\-molecule binding is not as reliable yet, but there’s no fundamental reason why further progress can’t crack it, especially if we start generating better experimental datasets[10](https://sarahconstantin.substack.com/p/ai-for-bio-state-of-the-field#footnote-10-148042978) .

Target discovery, [toxicity prediction](https://www.owlposting.com/p/a-primer-on-why-computational-predictive), and similar applications that are about predicting the impact of drugs on *organism health* are on much shakier footing. Living things are simply more complicated than molecules in solution, and they’re also more expensive to experiment on. I’m very skeptical of anyone claiming to solve these problems with AI in any degree of generality, though there may be narrow sub\-problems that are more tractable.

Modeling cells and measures of cell health with AI is, of course, intermediate in scale between molecules and whole organisms, and while it’s still largely in its infancy, I think it’s an interesting space to watch, though not as directly connected to drug development as the molecular structure models.

In general, despite the hype, it makes sense to be excited about the field. Given the speed of drug development, it’ll be years before we see the full clinical impact of the tools that are available today, let alone future creations.

[1](https://sarahconstantin.substack.com/p/ai-for-bio-state-of-the-field#footnote-anchor-1-148042978)Sertkaya, Aylin, et al. "Costs of drug development and research and development intensity in the US, 2000\-2018\." *JAMA Network Open* 7\.6 (2024\): e2415445\-e2415445\.

[2](https://sarahconstantin.substack.com/p/ai-for-bio-state-of-the-field#footnote-anchor-2-148042978)This might be a topic for another post; there may be regulatory reforms that could keep trial costs under control without compromising patient safety.

[3](https://sarahconstantin.substack.com/p/ai-for-bio-state-of-the-field#footnote-anchor-3-148042978)if you remember high school biology, you may have been taught about mRNA (for transcription) and tRNA (for translation). In reality there are a whole zoo of these types of RNA: [Wikipedia lists 74\.](https://en.wikipedia.org/wiki/List_of_RNAs)

[4](https://sarahconstantin.substack.com/p/ai-for-bio-state-of-the-field#footnote-anchor-4-148042978)Vázquez Torres, Susana, et al. "De novo design of high\-affinity binders of bioactive helical peptides." *Nature* 626\.7998 (2024\): 435\-442\.

[5](https://sarahconstantin.substack.com/p/ai-for-bio-state-of-the-field#footnote-anchor-5-148042978)in mathematical terms, naturally occurring images have [smoothness](https://en.wikipedia.org/wiki/Smoothness) properties

[6](https://sarahconstantin.substack.com/p/ai-for-bio-state-of-the-field#footnote-anchor-6-148042978)it’s more common to determine whether you’ve “created” a cell type by checking for gene expression markers characteristic of that cell type, and then by visual inspection of morphology; but in principle image\-processing methods could augment or even outperform those criteria.

[7](https://sarahconstantin.substack.com/p/ai-for-bio-state-of-the-field#footnote-anchor-7-148042978)genome, transcriptome, proteome, etc

[8](https://sarahconstantin.substack.com/p/ai-for-bio-state-of-the-field#footnote-anchor-8-148042978)Bender, Andreas, and Isidro Cortés\-Ciriano. "Artificial intelligence in drug discovery: what is realistic, what are illusions? Part 1: Ways to make an impact, and why we are not there yet." *Drug discovery today* 26\.2 (2021\): 511\-524\.

[9](https://sarahconstantin.substack.com/p/ai-for-bio-state-of-the-field#footnote-anchor-9-148042978)Meller, Artur, et al. "Predicting the locations of cryptic pockets from single protein structures using the PocketMiner graph neural network." *Biophysical journal* 122\.3 (2023\): 445a.

[10](https://sarahconstantin.substack.com/p/ai-for-bio-state-of-the-field#footnote-anchor-10-148042978)or [molecular\-dynamics datasets](https://www.owlposting.com/p/an-argument-for-integrating-molecular), built from a combination of experimental measurements and physics\-based (non\-AI) computational simulation.