# Fun With CellxGene

Published: 2024-09-06
Source: https://sarahconstantin.substack.com/p/fun-with-cellxgene

---

[![](https://substackcdn.com/image/fetch/$s_!KkIy!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fadc91966-221b-4c73-89cb-73685aab4b65_1024x1024.webp)](https://substackcdn.com/image/fetch/$s_!KkIy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fadc91966-221b-4c73-89cb-73685aab4b65_1024x1024.webp)

Midjourney image

For this week’s post, I thought I’d mess around a bit with the [CellXGene](https://cellxgene.cziscience.com/differential-expression) tool provided by the Chan Zuckerberg Initiative.

[![](https://substackcdn.com/image/fetch/$s_!cvgJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F73abf500-941c-4b20-898b-18d3f17a30fb_3290x1644.png)](https://substackcdn.com/image/fetch/$s_!cvgJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F73abf500-941c-4b20-898b-18d3f17a30fb_3290x1644.png)

It’s based on a big dataset of individual cells, classified by tissue, cell type, and disease state, and their gene expression profiles (single\-cell RNA counts).

You can automatically compare how gene expression looks different between sick and healthy individuals, for a variety of diseases, and drill down into which cells/tissues are different and how.

It’s a fascinating toy and a great way to generate hypotheses.

Here, I’ll do it for Alzheimer’s, comparing 138,438 Alzheimer’s brain cells to 9,203,998 normal/healthy brain cells to see what the most “differentially expressed” genes are, and what that might tell us about how the disease works.

## **Top Hits**

### LINC01609

#### 1\.6x overexpressed in Alzheimer’s, d \=4\.203

This is a non\-protein coding RNA. Typically most expressed in the [testis.](https://www.genecards.org/cgi-bin/carddisp.pl?gene=LINC01609)  In CellxGene’s healthy brain cells, it’s expressed only in activated microglia and astrocytes; but in the Alzheimer’s brain, it’s expressed in roughly half of *all* types of cells.

Like many long non\-coding RNAs, its function is unknown.

### SLC26A3

#### 10\.6x overexpressed in Alzheimer’s, d \= 3\.310

This is a chloride anion exchanger, a membrane protein that transports chloride ions across the cell membrane. It’s most heavily expressed in the colon, where it controls the resorption of fluid from the intestines. Defects in this gene are associated with congenital diarrhea, as the body is unable to maintain the right osmotic concentration and loses water in the stool. But we’re interested in SLC26A3 in the *brain,* not in the intestine.

In the healthy brain, once again, it’s only expressed in activated astrocytes and microglia; in the Alzheimer’s brain it’s expressed in large numbers of *all* cell types.

CellxGene classifies it as one of the top “markers” for [mature astrocytes](https://cellxgene.cziscience.com/cellguide/CL_0002627) and [mature microglial cells](https://cellxgene.cziscience.com/cellguide/CL_0002629), with a specificity of 1\.00\.

Other researchers have observed the upregulation of SLC26A3 in Alzheimer’s, e.g. as part of a pattern of “gliovascular” alteration around the clusters of astrocytes and endothelial cells that control the blood\-brain barrier.[1](https://sarahconstantin.substack.com/p/fun-with-cellxgene#footnote-1-148591675)

[![](https://substackcdn.com/image/fetch/$s_!Omlj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6ad74ddd-a481-4cb5-83e1-16383e8160ec_850x581.png)](https://substackcdn.com/image/fetch/$s_!Omlj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6ad74ddd-a481-4cb5-83e1-16383e8160ec_850x581.png)

A gliovascular unit is the place a blood vessel meets the brain. The vessel is surrounded by astrocytes and microglia, which control what goes in and out of the bloodstream, clearing excess glutamate and misfolded proteins. Under prolonged stress, these astrocytes in gliovascular units become reactive, and ultimately the blood\-brain barrier breaks down. In Alzheimer’s disease, the blood vessels get narrower, fragment, and break.[2](https://sarahconstantin.substack.com/p/fun-with-cellxgene#footnote-2-148591675) Activated astrocytes no longer connect as tightly to the surface of the vessels with their “endfeet”, compromising the BBB, while activated microglia engulf the endfeet, exacerbating the effect.[3](https://sarahconstantin.substack.com/p/fun-with-cellxgene#footnote-3-148591675)

What actually *happens* if you have more chloride anion exchange in the cells of a gliovascular unit? Is it causal for any Alzheimer’s pathology? That, I don’t think we know.

### RASGEF1B

#### 5\.5x overexpressed in Alzheimer’s, d\=3\.267

This is a widely expressed cytoplasmic protein that allows the protein Ras to be “switched on”, sending intracellular signals that lead to cell growth, differentiation, and survival. [4](https://sarahconstantin.substack.com/p/fun-with-cellxgene#footnote-4-148591675) Once again, in the healthy brain it is only expressed in activated astrocytes and microglia, while in the Alzheimer’s brain it’s expressed everywhere.

CellxGene classifies it as the top “marker” for [mature astrocytes](https://cellxgene.cziscience.com/cellguide/CL_0002627) and [mature microglial cells](https://cellxgene.cziscience.com/cellguide/CL_0002629), with a specificity of 1\.00\.

In normal circumstances, astrocytes and microglia can grow and proliferate, but most neurons do not. Ras activity increases in conditions of neural stress or injury, as part of the body’s attempt to promote cell survival and neurite regeneration. So it makes sense that we’d see a RAS\-activating gene expressed more widely in Alzheimer’s.

Other studies have showed increased expression of RASGEF1B in Alzheimer’s astrocytes[5](https://sarahconstantin.substack.com/p/fun-with-cellxgene#footnote-5-148591675), as well as in other cells around the gliovascular unit.

### LINGO1

#### 3\.9x overexpressed in Alzheimer’s, d\=2\.799

This is a central\-nervous\-system\-expressed membrane protein which downregulates myelination. Again, in the healthy brain it’s expressed primarily in activated astrocytes and microglia, while in Alzheimer’s it’s expressed everywhere.

CellxGene classifies it as one of the top markers for [mature astrocytes](https://cellxgene.cziscience.com/cellguide/CL_0002627) and [mature microglial cells](https://cellxgene.cziscience.com/cellguide/CL_0002629), with a specificity of 0\.99\.

LINGO1 has been implicated in a wide range of neurological disorders, as it plays a causal role in loss of neurons in response to injury or damage.[6](https://sarahconstantin.substack.com/p/fun-with-cellxgene#footnote-6-148591675)  In fact, LINGO1 antagonism has been studied as a therapeutic strategy for CNS repair.[7](https://sarahconstantin.substack.com/p/fun-with-cellxgene#footnote-7-148591675)  It’s also one of the genes whose expression is increased in Alzheimer’s gliovascular units.

### INO80D

#### 2x overexpressed in Alzheimer’s, d \=2\.244

This nuclear protein controls transcription by taking DNA on and off histones for copying; it’s widely expressed throughout the body. In the healthy brain, as we’ve been seeing, it is especially concentrated in activated astrocytes and microglia, while in the Alzheimer’s brain it’s everywhere.

CellxGene classifies it as one of the top markers for [mature astrocytes](https://cellxgene.cziscience.com/cellguide/CL_0002627) and [mature microglial cells](https://cellxgene.cziscience.com/cellguide/CL_0002629), with a specificity of 1\.00\.

The massive phenotype changes involved in activating astrocytes and microglia generally require chromatin remodeling, while adult neurons (which mostly don’t divide) seem to have less need for it. Possibly this pattern is altered in Alzheimer’s?

One paper noted the overexpression of INO80D in Alzheimer’s, along with other genes like LINGO1, RASGEF1B, and SLC26A3, as specific to “gliovascular units” of glial and vascular cells at blood\-brain\-barrier junctions.[8](https://sarahconstantin.substack.com/p/fun-with-cellxgene#footnote-8-148591675)

## **What’s Going On Here?**

There’s a pervasive pattern of genes that are normally only expressed in astrocytes and microglia in the healthy brain, being expressed much more widely in the Alzheimer’s brain.

In a gene\-expression sense, neurons and oligodendrocytes  in Alzheimer’s are “becoming more like” astrocytes and microglia.

This is part of the phenomenon of [gliosis](https://en.wikipedia.org/wiki/Gliosis), the central nervous system’s universal response to tissue damage. Astrocytes and microglia proliferate, secrete pro\-inflammatory factors, and block axon regeneration. It’s one of the ways neurological damage gets worse once it gets started.

But why would *other* cells start to “resemble” activated microglia and activated astrocytes?

Is it possible that the RNA transcripts themselves are being passed between cells?

Then we’d have a parsimonious explanation of the pattern we see: a simple *increase* in the number of activated microglia \& activated astrocytes, which we already know happens in Alzheimer’s, will also result in more “diffusion” of their characteristic RNA transcripts into other nearby cells.

In fact, cells “trade” RNA all the time, through extracellular vesicles. This happens everywhere in the body, including the brain.[9](https://sarahconstantin.substack.com/p/fun-with-cellxgene#footnote-9-148591675) [10](https://sarahconstantin.substack.com/p/fun-with-cellxgene#footnote-10-148591675) Both coding mRNA and non\-coding RNAs are passed around, and mostly the distribution of RNAs in extracellular vesicles parallels the distribution in the cells themselves.

In fact, activated microglia in Alzheimer’s disease have an especially high rate of extracellular vesicle formation and secretion, and they are known to pass around the disease’s characteristic plaque\-forming peptides/proteins (like amyloid beta and tau).

It’s pure speculation, of course, that extracellular vesicle RNA transport is *why* we’re seeing this pattern of altered gene expression in Alzheimer’s. There could be lots of other explanations; this is just the one crazy guess that happened to occur to me and doesn’t seem obviously unreasonable.

This theory doesn’t have an obvious new therapeutic implication; we already knew activated microglia and astrocytes were major villains in Alzheimer’s and played multiple causal roles in disease progression. “Get rid of activated microglia” and “stop them from sending extracellular vesicles everywhere” were already promising therapeutic strategies.

There is a testable hypothesis here, though: look for LINC01609 (about which almost nothing is known) in Alzheimer’s extracellular vesicles, and see if it’s being spread around through the brain from activated microglia.

## What Does CellxGene Get You?

The nice thing about big consolidated single\-cell datasets is that they can give you a relatively unbiased starting point for looking at disease mechanisms and targets.

It’s common in biology to *not* start with this sort of bird’s eye view, but rather to learn about a particular disease mechanism and cluster of genes/proteins due to historical accident — e.g. your advisor focused on this area, so that’s what you learned about.

Literature reviews can give another kind of “overview”, but they’re limited by the fact that not all papers are equally good. How frequently a gene is mentioned in connection to a disease, in the published literature, is a *very* shaky measure of how much you should prioritize studying or targeting that gene in that disease.

High\-quality, large datasets give a more rigorous way to make comparisons at scale.

And *public* datasets give a very rapid way for lots of people to get into a field and start generating ideas.

If you didn’t know anything about Alzheimer’s disease, messing around with CellxGene would very quickly tell you to start caring about activated microglia and astrocytes; not news to the domain experts, but true and important.

And, critically, easy for an outsider to *distinguish* from a mere disciplinary fad. If Alzheimer’s researchers had some kind of trendy obsession with microglia with no basis in fact, that cell type wouldn’t pop out as “special” in a way even a layman can see.

Datasets themselves can be biased, of course; what experimental methods are used, what sources the CZI people chose to include, and so on, can end up presenting a misleading picture.

For instance, this is a single\-cell RNA\-sequencing dataset; it presents a snapshot of the per\-cell prevalence of particular RNA sequences at the time of measurement. This may *not* be representative of the *protein* content of those cells. And it does not reveal how RNAs change over time. There’s a lot of important facts about a cell that you can’t get from RNA\-seq alone.

But giving these tools to the public really is a substantial improvement over the status quo.

And, of course, datasets are the prerequisite and starting point for models. Before you can simulate or predict something with AI, you need a lot of examples, in a standardized and queryable format. And you can usually get a lot of value out of simple exploratory statistics or inspection before you even get to the fancy machine\-learning part. The ultimate goal for a lot of these cell database projects is a big AI\-based generative model…but the database itself is already valuable and often more difficult to assemble in the first place.

I think as we see more integration of biology with “commercial\-quality” software, there’ll be more opportunity to play with these kinds of databases and statistical tools, and more people should try them out!

[1](https://sarahconstantin.substack.com/p/fun-with-cellxgene#footnote-anchor-1-148591675) İş, Özkan, et al. "Gliovascular transcriptional perturbations in Alzheimer’s disease reveal molecular mechanisms of blood brain barrier dysfunction." *Nature Communications* 15\.1 (2024\): 4758\.

[2](https://sarahconstantin.substack.com/p/fun-with-cellxgene#footnote-anchor-2-148591675)Iadecola, Costantino. "Neurovascular regulation in the normal brain and in Alzheimer's disease." *Nature Reviews Neuroscience* 5\.5 (2004\): 347\-360\.

[3](https://sarahconstantin.substack.com/p/fun-with-cellxgene#footnote-anchor-3-148591675)Yao, Di, et al. "Updated understanding of the glial\-vascular unit in central nervous system disorders." *Neuroscience bulletin* 39\.3 (2023\): 503\-518\.

[4](https://sarahconstantin.substack.com/p/fun-with-cellxgene#footnote-anchor-4-148591675) Quilliam, Lawrence A., John F. Rebhun, and Ariel F. Castro. "A growing family of guanine nucleotide exchange factors is responsible for activation of Ras\-family GTPases." (2002\): 391\-444\.

[5](https://sarahconstantin.substack.com/p/fun-with-cellxgene#footnote-anchor-5-148591675)Matusova, Zuzana, et al. "Reactive astrogliosis in the era of single\-cell transcriptomics." *Frontiers in Cellular Neuroscience* 17 (2023\): 1173200\.

[6](https://sarahconstantin.substack.com/p/fun-with-cellxgene#footnote-anchor-6-148591675)Andrews, Jessica L., and Francesca Fernandez\-Enright. "A decade from discovery to therapy: Lingo\-1, the dark horse in neurological and psychiatric disorders." *Neuroscience \& Biobehavioral Reviews* 56 (2015\): 97\-114\.

[7](https://sarahconstantin.substack.com/p/fun-with-cellxgene#footnote-anchor-7-148591675)Mi, Sha, R. Blake Pepinsky, and Diego Cadavid. "Blocking LINGO\-1 as a therapy to promote CNS repair: from concept to the clinic." *CNS drugs* 27 (2013\): 493\-503\.

[8](https://sarahconstantin.substack.com/p/fun-with-cellxgene#footnote-anchor-8-148591675)İş, Özkan, et al. "Single nuclei transcriptome reveals perturbed brain vascular molecules in Alzheimer’s disease." *Biorxiv* (2021\): 2021\-12\.

[9](https://sarahconstantin.substack.com/p/fun-with-cellxgene#footnote-anchor-9-148591675) Basso, Manuela, and Valentina Bonetto. "Extracellular vesicles and a novel form of communication in the brain." *Frontiers in neuroscience* 10 (2016\): 127\.

[10](https://sarahconstantin.substack.com/p/fun-with-cellxgene#footnote-anchor-10-148591675) O’Brien, Killian, et al. "RNA delivery by extracellular vesicles in mammalian cells and its applications." *Nature reviews Molecular cell biology* 21\.10 (2020\): 585\-606\.