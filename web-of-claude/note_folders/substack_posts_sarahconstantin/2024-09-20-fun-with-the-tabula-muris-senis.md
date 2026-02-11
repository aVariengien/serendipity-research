# Fun With The Tabula Muris (Senis)

*Differential expression for fun, profit, and understanding aging*

Published: 2024-09-20
Source: https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis

---

A very cool project, sponsored by the Chan Zuckerberg Initiative, was the Tabula Muris and the Tabula Muris Senis — a single\-cell gene expression “atlas” of the mouse, and then mice at various ages from 3 months (young adulthood) to 27 months (near the end of their lifespan.)

There’s a handy\-dandy differential expression [app](https://twc-stanford.shinyapps.io/maca/) that lets you see which genes are more expressed, or less expressed, in different tissues with age.

This is great for basic exploration that could give us insights into the mechanisms of aging (and ultimately inform research towards treatments of the diseases of aging.). So let’s play around with it and see if anything interesting is going on!

I’m going to just compare 27\-month\-old to 3\-month\-old mice. I’ll refer to genes as “upregulated” (with age) if they’re more abundant in the 27\-month\-olds, and “downregulated” (with age) if they’re more abundant in the 3\-month\-olds.

## Brain

### TL;DR

The aging brain is chronically inflamed, especially in neurodegenerative diseases of aging (Alzheimer’s, dementia, etc). The upregulated genes in old mouse brains are all markers of inflammation.

Interestingly, GPR7, the receptor for neuropeptides B and W, is downregulated with age. This may be a factor in age\-related obesity.

### Upregulated With Age

* **C4b**

	+ This is the gene for complement factor 4, part of the immune complement system that is active during inflammation and infection. 
	
	
		- This is unsurprising; most parts of the body, including the brain, become chronically more inflamed with age.
* **H2\-K1**

	+ This is an element of the major histocompatibility complex class 1, a cell surface protein that displays antigen peptides so the immune system can destroy damaged or virus\-infected cells.
	
	
		- Again, unsurprising; the aging brain has more damaged cells and more immune activity.
* **LGALS3BP**

	+ this is the gene for binding galectins, a type of protein involved in cell\-cell interactions, including immune interactions. In the brain, it seems to be characteristic of activated microglia[1](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-1-149156039)[2](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-2-149156039)[3](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-3-149156039) , a type of immune cell involved in brain inflammation and neurodegenerative disease.
	
	
		- As It Is Written: It’s The Microglia, Stupid.
* **CTSS**

	+ This is the gene for cathepsin S, an immune\-system gene used for breaking down proteins for antigen presentation.
	
	
		- Once again, unsurprising that it would be upregulated in an aging inflamed brain.
* **H2D1**

	+ This is a component of the MHC class 2 molecules, found on immune cells, including microglia in their activated state.
	
	
		- once again, yep, that’s a sign of neuroinflammation.
* **LYZ2**

	+ This is the gene for lysozyme (LYZ in humans), an antimicrobial enzyme in the innate immune system. It breaks down bacterial cell walls, killing the germs.
	
	
		- You get elevated levels of lysozyme in the brain during brain infections, obviously, but also during brain tumors[4](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-4-149156039), stroke[5](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-5-149156039), and Alzheimer’s[6](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-6-149156039), which are age\-related non\-infectious diseases associated with an inflammatory response.
		
		
			* Aged mice don’t generally get brain tumors, strokes, or Alzheimer’s per se, but they do develop inflammatory brain damage and impaired cognition.
* **GFAP**

	+ This is the gene for glial fibrilary acidic protein, a major structural protein in astrocytes. In fact, it’s a standard immunostaining marker for distinguishing astrocytes from other cell types.
	
	
		- GFAP expression increases in astrocytes when they become activated (or reactive), part of the neuroinflammation response to damage (from eg brain injury, stroke, tumors, or neurodegenerative disease.)[7](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-7-149156039)
		
		
			* Again, no surprises here. We’re seeing more GFAP in the old mice because they have neuroinflammation.
* **LGALS3**

	+ This is the gene for galectin\-3, which was discussed above (LGALS3BP is the binding protein for LGALS3\).
	
	
		- Again, unsurprising; this is due to activated microglia in neuroinflammation.
* **IFIT3**

	+ This is a gene involved in the innate immune system in response to inflammatory interferon signaling as a response to viral infection.
	
	
		- Again, this looks like a neuroinflammation thing.
* **C3**

	+ This is a component of the complement system, part of the immune response.
	
	
		- Again: more C3 in the aging brain suggests neuroinflammation.
* **NEAT1**

	+ NEAT1 is a non\-coding RNA, localized to a structure inside the nucleus known as a paraspeckle. We don’t know exactly what paraspeckles do, but they may be a defense against RNA viruses.
	
	
		- In the brain, NEAT1 also promotes inflammatory responses to traumatic brain injury[8](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-8-149156039) and is upregulated in a variety of human neurodegenerative diseases (Alzheimer’s, Parkinson’s, Huntington’s, ALS)[9](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-9-149156039) so it may also be a neuroinflammation thing.
* **H2\-Q6**

	+ This is an MHC2 gene
	
	
		- again, that’s inflammation
* **H2\-Q7**

	+ This is an MHC2 gene
	
	
		- again, that’s inflammation

### Downregulated with Age

* **GPR7**

	+ This is a binding protein for neuropeptide B and neuropeptide W, proteins particularly expressed in parts of the brain like the amygdala that regulate stress and fear.
	
	
		- Mice lacking this gene approach strange mice, rather than hesitating cautiously as mice usually do.[10](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-10-149156039)
		- Mice lacking this gene also develop adult\-onset obesity.[11](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-11-149156039)

### Progression

* The *earliest* of these genes to be upregulated with age is C4b, which shows up at 9 months. By 21 months, most of these genes are upregulated. GPR7 downregulation doesn’t show up until 27 months.

## Muscle

### TL;DR

Mice, like humans, lose muscle and strength with age; mice begin to show elevated levels of muscle\-loss\-associated proteins *quite* young, before “middle age”. At least one of them, a defensin, belongs to a class of proteins known to *cause* muscle loss when administered experimentally. Perhaps anti\-defensin strategies might be a good research direction for preventing sarcopenia?

Also, collagen genes are downregulated with age; this might be a side effect of collagen accumulation in muscles (a known age\-related phenomenon.)

### Upregulated With Age

* **H1fnt**

	+ This is a histone, one of the “beads” around which DNA is normally coiled. 
	
	
		- Why is its expression upregulated in aged muscle? I’m generally stumped. Overall, aging is associated with *loss* of histones.
* **Alpi**

	+ This is the gene for alkaline phosphatase, mostly used for regulating homeostasis in the intestine. In skeletal muscle, you see alkaline phosphatase mostly in muscle wasting diseases[12](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-12-149156039) and high serum alkaline phosphatase is a biomarker for sarcopenia (loss of muscle mass with age).[13](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-13-149156039) 
	
	
		- I don’t think it’s known, causally, why alkaline phosphatase seems to be associated with muscle loss.
* **Defa30**

	+ This is a gene for defensin (human ortholog DEFA3\), an antimicrobial peptide.
	
	
		- Defensins cause muscle loss![14](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-14-149156039)[15](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-15-149156039) And they’re associated with muscle degeneration in inflammatory myopathies.[16](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-16-149156039)

### Downregulated with Age

* **Cilp2**

	+ This is a cartilage protein; usually its expression *increases* with age in the presence of osteoarthritis.
	
	
		- Why is it downregulated with age in muscle? Beats me!
* **Col1a2**

	+ That’s a collagen gene. 
	
	
		- In general, collagen accumulates in aged muscles, causing stiffness; but this is not a result of increased gene expression but rather lack of ability to clear it out.[17](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-17-149156039)
		
		
			* It’s not unusual for *production* of a substance in the body to go down in response to that substance being *abundant*, in a standard negative feedback mechanism; that could (speculatively) be what’s going on here.
* **Col1a1**

	+ Also a collagen gene; also might be downregulated as a result of collagen buildup.

### Progression

Alpi begins to be upregulated super early, at *9* months. H1fnt and Defa30 are also upregulated by 15 months. Downregulated Cilp, Col1a2, and Col1a1 show up later, at 18\-21 months.

## **Spleen**

### TL;DR

The aging spleen is interesting because [removing it altogether](https://sarahconstantin.substack.com/p/old-spleens-suck) seems to make animals live longer. What is the aged spleen doing wrong, at a gene expression level?

Looks like, granzyme K\-positive cytotoxic T cells. They accumulate with age and promote inflammation throughout the body. (They aren’t a unique “culprit” for age\-related inflammation, though; inject them into a young mouse and they don’t promote the same phenotypes.)

### Upregulated with Age

* **C130026I21Rik**

	+ This is a nuclear body protein like gene; it’s homologous to the transcriptional regulator SP140, which is found in white blood cells and downregulates genes involved in autoimmune diseases.[18](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-18-149156039)
* **Snhg11**

	+ This is a long non\-coding RNA that promotes growth in a wide variety of cancers.[19](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-19-149156039)[20](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-20-149156039)[21](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-21-149156039)
* **Gzmk**

	+ This is the gene for granzyme K, found in the granules of immune cells (NK cells and cytotoxic T lymphocytes).
	
	
		- In humans, higher granzyme K levels are associated with older age and CMV infection.[22](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-22-149156039) In fact, granzyme K\-positive cytotoxic T cells are a highly clonal population[23](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-23-149156039) that grow more common with age across organs in mice and are associated both with age and with age\-related inflammatory markers in humans.

### Progression

Snhg11 and Gzmk start to get upregulated at middle age (12 months); C130026I21Rik pops up only slightly later, at 18 months.

## Conclusions

This is just a starting point (I picked a couple tissues to play with but there are lots more.)

But *already* it’s easy to observe patterns that make sense in context (old brains are inflamed; old muscles have weird collagen; old spleens are enriched for particular populations of immune cells) and to generate ideas for interventional research directions.

#### Speculative Research Directions:

* stimulate the neuropeptide W/B receptor to treat obesity?
* target defensins to treat sarcopenia and other muscle diseases?
* target granzyme K\-positive T cells to treat age\-related inflammatory conditions?

The majority of drug discovery programs, remarkably enough, do *not* seem to have come from any kind of genetic analysis of this kind, where you notice that the relevant target is overexpressed (or mutated, or whatever) in disease.

Obviously, the “sit on your butt and read/play with omics data” approach to idea generation offers only a slim chance of actually coming up with something successful; but I keep seeing data points suggesting that, despite how easy it is to do, it’s underrated and under\-practiced in biomedical research.

#### Maybe Research Idea\-Generation At Scale Is Valuable?

Someone (maybe me!) should start compiling a database of “someone should try this” experimental approaches suggested by systematic “omics” datasets (like the Tabula Muris Senis and CellxGene, and GWAS studies, and much much more.)

This requires a common\-sense filtering step based on context from the research literature — I don’t think writing a simple script to automate it would be very useful — but it is of course *accelerated* by LLM tools like [Perplexity](https://www.perplexity.ai/) that help you search for research papers that answer your questions.

Once fully populated, this sort of resource might be valuable to researchers; it might even be a higher\-quality version of some of the functions that fully automated “AI for target discovery” tools aim to provide biotech companies.

Failed to render LaTeX expression — no expression found

[1](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-anchor-1-149156039)Arutyunov, Artem, et al. "West Nile Virus\-Induced Expression of Senescent Gene Lgals3bp Regulates Microglial Phenotype within Cerebral Cortex." *Biomolecules* 14\.7 (2024\): 808\.

[2](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-anchor-2-149156039)Todd, Brittany P., et al. "Traumatic brain injury results in unique microglial and astrocyte transcriptomes enriched for type I interferon response." *Journal of neuroinflammation* 18 (2021\): 1\-15\.

[3](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-anchor-3-149156039)Sirko, Swetlana, et al. "Injury\-specific factors in the cerebrospinal fluid regulate astrocyte plasticity in the human brain." *Nature Medicine* 29\.12 (2023\): 3149\-3161\.

[4](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-anchor-4-149156039)Constantopoulos, A., et al. "Spinal fluid lysozyme in the diagnosis of central nervous system tumours." *Neurochirurgia* 19\.04 (1976\): 169\-171\.

[5](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-anchor-5-149156039)Terent, A. N. D. R. E. A. S., et al. "Lactoferrin, lysozyme, and beta 2\-microglobulin in cerebrospinal fluid. Elevated levels in patients with acute cerebrovascular lesions as indices of inflammation." *Stroke* 12\.1 (1981\): 40\-46\.

[6](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-anchor-6-149156039)Helmfors, Linda, et al. "Protective properties of lysozyme on β\-amyloid pathology: implications for Alzheimer disease." *Neurobiology of disease* 83 (2015\): 122\-133\.

[7](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-anchor-7-149156039)Palmer, Alexandra L., and Shalina S. Ousman. "Astrocytes and aging." *Frontiers in Aging Neuroscience* 10 (2018\): 337\.

[8](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-anchor-8-149156039)Liu, W\-Q., et al. "Effects of long non\-coding RNA NEAT1 on sepsis\-induced brain injury in mice via NF\-κB." *European Review for Medical \& Pharmacological Sciences* 23\.9 (2019\).

[9](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-anchor-9-149156039)Li, Kun, and Ziqiang Wang. "lncRNA NEAT1: Key player in neurodegenerative diseases." *Ageing Research Reviews* 86 (2023\): 101878\.

[10](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-anchor-10-149156039)Nagata\-Kuroiwa, Ruby, et al. "Critical role of neuropeptides B/W receptor 1 signaling in social behavior and fear memory." *PLoS One* 6\.2 (2011\): e16972\.

[11](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-anchor-11-149156039)Ishii, Makoto, Hong Fei, and Jeffrey M. Friedman. "Targeted disruption of GPR7, the endogenous receptor for neuropeptides B and W, leads to metabolic defects and adult\-onset obesity." *Proceedings of the National Academy of Sciences* 100\.18 (2003\): 10540\-10545\.

[12](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-anchor-12-149156039)Engel, W. King, and GUY G. CUNNINGHAM. "Alkaline phosphatase\-positive abnormal muscle fibers of humans." *Journal of Histochemistry \& Cytochemistry* 18\.1 (1970\): 55\-57\.

[13](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-anchor-13-149156039)Petermann\-Rocha, Fanny, et al. "Biomarkers profile of people with sarcopenia: a cross\-sectional analysis from UK biobank." *Journal of the American Medical Directors Association* 21\.12 (2020\): 2017\-e1\.

[14](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-anchor-14-149156039)Yamaguchi, Yasuhiro, et al. "β\-Defensin overexpression induces progressive muscle degeneration in mice." *American Journal of Physiology\-Cell Physiology* 292\.6 (2007\): C2141\-C2149\.

[15](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-anchor-15-149156039)though, note that this is a beta defensin and the gene in question is for an alpha defensin.

[16](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-anchor-16-149156039)Güttsches, Anne\-Katrin, et al. "Human β\-defensin\-3 correlates with muscle fibre degeneration in idiopathic inflammatory myopathies." *Innate Immunity* 20\.1 (2014\): 49\-60\.

[17](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-anchor-17-149156039)Chen, Wan\-Jing, et al. "Aged skeletal muscle retains the ability to remodel extracellular matrix for degradation of collagen deposition after muscle injury." *International journal of molecular sciences* 22\.4 (2021\): 2123\.

[18](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-anchor-18-149156039)Karaky, Mohamad, et al. "SP140 regulates the expression of immune\-related genes associated with multiple sclerosis and other autoimmune diseases by NF\-κ B inhibition." *Human molecular genetics* 27\.23 (2018\): 4012

[19](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-anchor-19-149156039)Xu, Wei, et al. "Circulating lncRNA SNHG11 as a novel biomarker for early diagnosis and prognosis of colorectal cancer." *International journal of cancer* 146\.10 (2020\): 2901\-2912\.

[20](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-anchor-20-149156039)Geng, Y\-B., et al. "Long non\-coding RNA SNHG11 promotes cell proliferation, invasion and migration in glioma by targeting miR\-154\-5p." *European Review for Medical \& Pharmacological Sciences* 24\.9 (2020\).

[21](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-anchor-21-149156039)Huang, Wei, et al. "LncRNA SNHG11 promotes proliferation, migration, apoptosis, and autophagy by regulating hsa\-miR\-184/AGO2 in HCC." *OncoTargets and therapy* (2020\): 413\-421\.

[22](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-anchor-22-149156039)Verschoor, Chris P., et al. "NK\-and T\-cell granzyme B and K expression correlates with age, CMV infection and influenza vaccine\-induced antibody titres in older adults." *Frontiers in Aging* 3 (2023\): 1098200\.

[23](https://sarahconstantin.substack.com/p/fun-with-the-tabula-muris-senis#footnote-anchor-23-149156039)that is, derived from the same parent cells