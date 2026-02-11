# Cancer-Selective, Pan-Essential Targets from DepMap

*A Claude Code experiment*

Published: 2026-01-09
Source: https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets

---

### Introduction

Back in June, I proposed that it would be a good idea to look for [broad\-spectrum cancer treatments](https://sarahconstantin.substack.com/p/broad-spectrum-cancer-treatments) — i.e. therapies that work on *many* types of cancer, rather than being hyper\-specialized for narrow subtypes.

There’s nothing fantastic about this notion. After all, some of the oldest cancer treatments (chemotherapy and radiation) are broad\-spectrum, and while in some cases it’s possible to outperform them, cytotoxic chemo and radiation are still mainstays of treatment today.

The first thing I proposed was a systematic search for “pan\-essential” targets — genes which, when knocked out in cancer cells, cause cell death, but which don’t kill healthy cells.

What I hadn’t realized at the time is that it’s not necessarily tractable to screen genetic knockouts of true “healthy cells”, which don’t grow well in culture. You might be able to do something with short\-lived patient\-derived samples, or organoids, but we don’t have big public datasets of these.

What we do have is [DepMap](https://depmap.org/portal/), an atlas of genetic cancer dependencies (i.e. genes without which cancer cells die). It spans 2119 human cancer cell lines, and also has 13 “normal” cell culture lines and 45 fibroblast lines as controls.

Now, granted, an immortalized cell culture line is not that representative of a healthy cell in a human body, but it’s a starting point.

We can look for gene knockouts that have a strong growth\-inhibiting effect on the majority of cancer lines, with little inhibiting effect on the “normal” lines, and rank them by selectivity. We can then filter this list of genetic targets further for their likely druggability, rule out the ones that are already known targets of cancer drugs, and end up with a list of targets worth investigating.

### Claude Code

This is a straightforward data analysis project that in principle I could have done myself — but it would have been a lot of work, and I might not have gotten around to it.

Instead, I had the [bot](https://code.claude.com/docs/en/overview) do it.

And what a bot it is!

I am, as the kids say, “feeling the AGI.”

I’d coded with LLM assistance before, but I was always trying to *mostly* write stuff myself or at least carefully read every line; I wasn’t truly letting the machine off the leash. This time, I did; every line of code in my [pan\-cancer repo](https://github.com/srconstantin/claude-code-experiments/tree/main/pan-cancer)  is 100% Claude\-generated.

The experience is addictive, to the point of being a bit scary. It would be all too easy to let a lot of programming skills atrophy and let the bot do everything for me.

On the plus side, it means there’s no longer such a thing as a “someday project”, at least when it comes to code. If it can be done with a laptop and public data (or your own data), you can do it right now, frictionlessly.

Dean Ball’s [list](https://www.hyperdimensional.co/p/among-the-agents) is an inspiration:

> In the past month I have:
> 
> 1. Automated invoice creation, sending, and tracking;
> 2. Created scientifically realistic simulations of hydrological systems as a learning project;
> 3. Automated my research process of gathering and analyzing all proposed state legislation related to AI (though this is no substitute for reading the bill for anything I am going to write about);
> 4. Orchestrated a complex chain of autonomous data collection, processing, analysis, and presentation steps related to manufacturing and industrial policy;
> 5. Created a machine\-learning model capable of predicting US corn yields with what appears to be very high accuracy (the proof will be in the pudding), based on climate, soil, Earth\-observation satellite, and other data sources;
> 6. Replicated three machine\-learning research papers and modified the approach to suit my own research ends;
> 7. Performed hundreds of experiments with Byte\-level language models, an emerging interest of mine;
> 8. Created an autonomous prediction market agent;
> 9. Created an autonomous options trader based on a specific investment thesis I developed;
> 10. Built dozens of games and simulations to educate myself about various physical or industrial phenomena;
> 11. Created an agent that monitors a particular art market in which I am potentially interested in making an acquisition;
> 12. Created a new personal blog complete with a Squarespace\-style content management system behind the scenes;
> 13. Other things I cannot talk about publicly just yet.

If you (like me) have a long wish list of things to do, and are bottlenecked on the gumption or programming skill to do them all, Claude Code is a gamechanger.

So far, it’s been two days, and I’ve already had it make a little [mood\-tracker app](https://github.com/srconstantin/claude-code-experiments/tree/main/panas-questionnaire-app) and then overhauled all my web\-app\-based to\-do list and journaling/logging systems and replaced them with a Claude Code\-based system on my laptop. And this pan\-cancer project.

I notice that I am much less interested in toggling between a bunch of different web apps when Claude Code can just extract their data via an API and let me combine it all seamlessly.

I also notice that I care, suddenly, about efficient and repeatable processes in my daily life, in the way that software engineers always have and I historically haven’t.

You know how playing a video game for several hours makes you see the world around you in terms of the moves in the game? Like playing a first\-person shooter and seeing everything as a target? After using Claude Code for hours, everything looks like a protocol to be optimized and made repeatable. Down to “what’s the most efficient set of moves for changing a diaper?”

Your systems can now be *your* systems. Configured how you like em. Exactly the way command\-line wizards have always rolled their own systems, except that now it’s trivially easy.

“But is the code trustworthy?”

In the case of this pan\-cancer project, I’m inclined to believe it’s okay. I read through the python scripts and they looked sensible, and (more importantly) I’ve been looking in more detail through the top\-50 list of targets and *those* look sensible.

This is, of course, not enough assurance for a serious piece of software. For that, we’d need a bunch of tests, at a minimum. But as a personal experiment, I’m satisfied. Please do let me know, however, if you see anything fishy in the repo.

*ETA: As a helpful commentator pointed out, there WAS a problem in the repo; Claude wrote a function to exclude DepMap’s list of “pan\-essential” targets, which damage all cells, but then quietly did not actually implement this exclusion in the final results, because it would have resulted in an empty list of results.*

*This is a particularly alarming failure mode of agents — they’ll spontaneously “fix” code that returns something disappointing, even when you actually need to know the “bad news”. I was too overwhelmed by the speed and abundance of the autogenerated output to notice the problem, which I now see was a dangerous oversight.*

(As always, my blog posts, and anything else I sign my name to, are written by me, not by any AI. When I share model output it will be clearly labeled as such.)

### The Results

Cell line “dependency” on a gene is measured by the abundance of CRISPR\-modified cells relative to wild\-type; a negative value for a gene means that the cells became less abundant when that gene is knocked out. This could be due to the knockout causing cell death, slower proliferation, or both.

Here, we define the cutoff for an “pan\-cancer essential” gene as having a negative dependency score (effect size) of at least \-0\.5 in at least 50% of cancers, and of a gene that *isn’t* essential for normal cells as one that doesn’t have an average negative dependency score of more than \-0\.3 in the 16 normal cell lines. This gives us a list of “cancer\-specific pan\-essential genes.”

*ETA: DepMap also has a list of “pan\-essential genes” which, it claims, kill all cells, healthy and cancerous, and all the genes returned by my selectivity cutoff are classified as pan\-essential. Arguably, this means that there are no* *good hits at all, rather than 1556\.*

*From a devil’s advocate perspective, we might say instead that DepMap’s creators encoded this list based on an assumption that “pan\-essential” genes across cancers are inherently bad targets — i.e. that by definition the kind of selective broad\-spectrum anti\-cancer agents I’m looking for cannot exist.*

*At any rate, for better or worse, all the genes in the following analysis are on the “pan\-essential” list.*

*If you really wanted greater confidence that these genes could be targeted without killing healthy cells, you’d need to experiment with (genetic or pharmacological) inhibition in more realistic models of healthy cells, perhaps something patient\-derived.*

Selectivity is defined as (cancer dependency \- non\-cancer dependency). More selective is better; it means that targeting that gene *relatively* harms cancer cells more than normal cells.

We look at the top\-50 “cancer\-specific pan\-essential” genes, ranked from most to least selective.

We also cross\-reference these top genes with the [OpenTargets database](https://platform.opentargets.org/) to get an estimate of their “druggability.”

OpenTargets has, for each target, a list of criteria that point towards it being druggable with small molecules (things like “high\-quality pocket”), with antibodies, or with PROTACs — as well as whether there are approved drugs or clinical\-stage drug candidates with that target. We assign a simple scoring rubric (for each drug/biologic type, we assign the target a score of 1 for any structural druggability criteria, 2 for clinical\-stage drugs, 3 for approved drugs).

The resulting top\-50 targets are as follows:

[![](https://substackcdn.com/image/fetch/$s_!pOhb!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8a121913-81bb-4964-bfd8-2cd930025949_2409x2653.png)](https://substackcdn.com/image/fetch/$s_!pOhb!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8a121913-81bb-4964-bfd8-2cd930025949_2409x2653.png)

Notice that the targets of some classic chemo drugs are on here:

\#8 is DHFR (the target of methotrexate), while \#41 is TOP2A (the target of doxorubicin and etoposide), and \#49 is BUB1B (one of the targets of paclitaxel.)

Other chemo targets (for gemcitabine, capecitabine, and 5\-fluorouracil) are also *somewhat* selective, but not enough to make it into the top 50\.

There’s generally a fairly high density (18%) of targets with clinical or approved cancer therapies in the top 50, which suggests we’re on the right track and we are indeed looking at a set of cancer targets.

But we’re here to look for *new* targets. Hopefully, targets that have additional evidence of relevance for cancer, which *haven’t* yet been subject to a lot of drug development attention, but which are reasonably tractable as drug targets. Especially high selectivity might mean the potential for drugs that work as widely as chemo but have fewer side effects; novel mechanisms of action might suggest drugs that aren’t redundant with existing therapies.

In the rest of this post, I’ll look at a few interesting candidates.

### YRDC — Not Yet Pursued

YRDC has the top selectivity score, of 0\.456, and it is essential in 84\.1% of cancer lines.

It is involved in tRNA modification.

Interestingly, “[loss‐of‐function mutations in YRDC have been linked to severe developmental disorders—including variants of Galloway–Mowat syndrome and neonatal](https://maayanlab.cloud/Harmonizome/gene/YRDC) **[progeroid phenotypes](https://maayanlab.cloud/Harmonizome/gene/YRDC)**[—that feature](https://maayanlab.cloud/Harmonizome/gene/YRDC) **[telomere shortening, genomic instability](https://maayanlab.cloud/Harmonizome/gene/YRDC)**[, microcephaly, and renal dysfunction”](https://maayanlab.cloud/Harmonizome/gene/YRDC). That suggests that knocking out this gene is killing fast\-dividing cancer cells through interfering with genome maintenance.

It localizes to the mitochondria, and it’s especially highly expressed in [bone marrow](https://www.proteinatlas.org/ENSG00000196449-YRDC).

It’s overexpressed in a variety of cancers[1](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-1-184035594) and targeting it (with a genetic knockdown) in glioblastoma can reduce tumor growth.[2](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-2-184035594)

There are [antibodies that target it.](https://www.scbt.com/p/yrdc-antibody-e-10?srsltid=AfmBOopzKsqsi-QWaYe3Kl72Uifgr9Hmss669jw4-aFYq5YveJukBbq-)

But so far YRDC does not appear to be the subject of a drug development effort.

I don’t know of a reason it should be *impossible* to target (though the mitochondrial location might present some challenges, and its concentration in the bone marrow suggests standard chemo side effects such as neutropenia would be a concern.)

### TFRC — Clinical

TFRC had the \#2 selectivity score, at 0\.369, and was essential in 67\.2% of cancers.

TFRC encodes the [transferrin receptor](https://www.ncbi.nlm.nih.gov/gene/7037), which enables cellular iron uptake.

Conveniently, it’s a surface protein, and it’s overexpressed in many cancers.[3](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-3-184035594) It seems that cancer cells can be unusually iron\-hungry, and starving them of iron can prevent growth and/or progression.

An anti\-TFRC antibody\-drug conjugate, INA03, recently completed Phase I trials in relapsed/refractory leukemias, where it was “well tolerated” (a phrase which here means “not vastly worse than chemo”) and showed some early signs of efficacy. [4](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-4-184035594) French company [Inatherys](https://www.inatherys.com/) was behind the trial.

### PHF5A — Preclinical

PHF5A has the \#3 selectivity score, with cancer selectivity of 0\.369, and it’s essential in 100% of cancer cell lines.

It’s a [nuclear protein](https://www.uniprot.org/uniprotkb/Q7RTV0/entry), a component of the spliceosome protein complex. Like YRDC, it’s involved in genome repair.

It’s also overexpressed in many cancers, and sometimes its expression is associated with worse survival prognosis. Almost *all* immune checkpoint genes (which protect cancers from the immune system) are positively associated with PHF5A expression.[5](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-5-184035594)

And it can apparently be pharmacologically inhibited, with [pladienolide B](https://en.wikipedia.org/wiki/Pladienolide_B).[6](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-6-184035594) And [targeted with antibodies.](https://www.thermofisher.com/antibody/primary/target/phf5a)

I have no special reason to believe it’s either tractable or impossible to make drugs to target PHF5A, but it seems to be an open problem and one that people are working on.

### ADSL — Preclinical

ADSL has the \#3 selectivity score, at 0\.318, and is essential in 70\.5% of cancer cell lines.

It’s an [enzyme involved in making purines](https://en.wikipedia.org/wiki/Adenylosuccinate_lyase), and thus obviously involved in DNA synthesis/repair.

Conveniently, there exist [antibodies that target it.](https://www.thermofisher.com/antibody/primary/target/adsl)

It’s a [cytosolic](https://www.proteinatlas.org/ENSG00000239900-ADSL) protein, mostly expressed in muscle.

Knocking it down in cancer\-prone mice prevents the growth of liver tumors.[7](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-7-184035594) Lots of other studies, all preclinical, find causal effects of ADSL inhibition or knockdown on multiple cancer types’ proliferation or invasiveness, eg. in breast cancer[8](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-8-184035594).

This seems like a fairly tractable target, though not especially neglected.

### SEPHS2 — Not Yet Pursued

SEPHS2 has the \#5 selectivity score, at 0\.316, and is essential in 54\.9% of cancers.

It’s an enzyme involved in selenium metabolism.

It lives inside the nucleus, in the [nucleoplasm](https://www.proteinatlas.org/ENSG00000179918-SEPHS2), and is especially highly expressed in the liver and colon.

Cancer cells, especially breast cancers, take up a lot of selenium, which can be toxic, and needs SEPHS2 to detoxify it.[9](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-9-184035594)

Knocking out SEPHS2 can delay or prevent leukemia in mice[10](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-10-184035594).

There are [antibodies](https://www.thermofisher.com/antibody/product/SEPHS2-Antibody-Polyclonal/PA5-21878) that target it, but so far no small molecules. It may be difficult to target due to its nuclear location.

### NMT1 — Clinical

NMT1 has the \#6 selectivity score, at 0\.314, and is essential in 71\.1% of cancers.

It is an [enzyme that adds the fatty acid myristate to certain proteins](https://www.ncbi.nlm.nih.gov/gene/4836), a post\-translational modification that prepares them for cell signaling roles (that might be involved in cancer’s abnormal survival and proliferation signaling).

There are lots of associations between NMT1 and cancer progression in various cancers (breast[11](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-11-184035594), liver[12](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-12-184035594), bladder[13](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-13-184035594), etc).

There are also [compounds that inhibit it](https://en.wikipedia.org/wiki/N-myristoyltransferase_inhibitors); one of those recently completed a Phase I trial for advanced solid tumors and relapsed B\-cell lymphomas,[14](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-14-184035594) led by Canadian company [Pacylex Pharmaceuticals.](https://www.pacylex.com/)

What’s interesting here is that this seems to be a novel pathway, not based around genome repair/synthesis, and thus potentially non\-redundant with older chemo drugs.

### ELL — Not Yet Pursued

ELL has the \#7 selectivity score, at 0\.310, and is essential in 95\.1% of cancers.

It’s involved in [gene transcription](https://www.uniprot.org/uniprotkb/P55199/entry) and lives in the nucleus. It’s a transcription factor that affects oncogenes like Myc. [15](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-15-184035594)

It may be difficult to target due to its nuclear location, and there don’t seem to be any drug development programs targeting it.

### GUK1 — Not Yet Pursued

GUK1 has a selectivity score of 0\.294 and is essential in 94\.9% of cancers.

It’s an [enzyme involved in guanine metabolism](https://www.ncbi.nlm.nih.gov/gene/2987).

It’s particularly highly expressed in [skin](https://www.proteinatlas.org/ENSG00000143774-GUK1/single+cell), and it’s a [plasma membrane protein](https://maayanlab.cloud/Harmonizome/gene/GUK1).

It’s been found that you need GUK1 activation for lung cancer cell growth.[16](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-16-184035594)

There are compounds that inhibit GUK1 activity.[17](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-17-184035594)

So far it doesn’t seem to have been considered as a cancer drug target.

### CFLAR — Preclinical

CFLAR has a selectivity score of 0\.259 and is essential in 52\.4% of cancers.

It’s a [regulator of apoptosis](https://www.genecards.org/cgi-bin/carddisp.pl?gene=CFLAR) that prevents CASP8 from killing cells.

Its expression is a predictor of cancer drug resistance and poor prognosis; mild heat shock can suffice to cause it to aggregate and be removed from the cell; there are also programs underway to develop direct small molecules that target it.[18](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-18-184035594)

### DNM1L — Preclinical

DNM1L has a specificity score of 0\.259 and is essential in 57\.2% of cancers.

It’s an enzyme that [regulates mitochondrial fission.](https://en.wikipedia.org/wiki/DNM1L) Normally it’s a [cytosolic protein.](https://maayanlab.cloud/Harmonizome/gene/DNM1L)

Its expression is associated with progression in stomach cancer[19](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-19-184035594), pancreatic cancer[20](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-20-184035594), endometrial cancer[21](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-21-184035594), and others. Many DNM1L inhibitors have been developed, but they’re not specific enough to be good cancer therapies yet.[22](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-22-184035594)

### TRPM7 — Preclinical

TRPM7 has a specificity score of 0\.229 and is essential in 64\.5% of cancers.

TRPM7 is a [calcium ion channel](https://en.wikipedia.org/wiki/TRPM7) on the cell membrane.

TRPM7 is necessary for breast cancer metastasis, via its effect on cell\-cell adhesion; it makes cells less stiff and thus less able to stick together, loosening them so they can migrate.[23](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-23-184035594) It does the same in ovarian cancer[24](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-24-184035594) and prostate cancer.[25](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-25-184035594) Interestingly, it is itself a mechanosensor that detects stretching of the cell membrane.[26](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-26-184035594)

Work is currently being done on developing selective inhibitors of TRPM7\.

[1](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-anchor-1-184035594)Qiao, Li, Yuetong Zhang, and Pin Huang. “YRDC is a Prognostic‐Related Biomarker Correlated With Immune Infiltration and Drug Sensitivity in Pan‐Cancer.” *Cancer Reports* 8\.9 (2025\): e70325\.

[2](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-anchor-2-184035594)Wu, Xujia, et al. “Threonine fuels glioblastoma through YRDC\-mediated codon\-biased translational reprogramming.” *Nature cancer* 5\.7 (2024\): 1024\-1044\.

[3](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-anchor-3-184035594)Shen, Ying, et al. “Transferrin receptor 1 in cancer: a new sight for cancer therapy.” *American journal of cancer research* 8\.6 (2018\): 916\.

[4](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-anchor-4-184035594)Garciaz, Sylvain, et al. “Results of a Phase 1, First\-in\-Human Study of INA03, an Anti\-CD71 Antibody\-Drug Conjugate in Patients with Relapsed or Refractory (R/R) Acute Leukemias.” *Blood* 144 (2024\): 1496\.

[5](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-anchor-5-184035594)Ding, Na, Meiping Li, and Xiaokun Zhao. “PHF5A is a potential diagnostic, prognostic, and immunological biomarker in pan\-cancer.” *Scientific Reports* 13\.1 (2023\): 17521\.

[6](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-anchor-6-184035594)Zhang, Zhandong, et al. “PHF5A facilitates the development and progression of gastric cancer through SKP2\-mediated stabilization of FOS.” *Journal of Translational Medicine* 21\.1 (2023\): 5\.

[7](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-anchor-7-184035594)Jiang, Tingting, et al. “Targeting de novo purine synthesis pathway via ADSL depletion impairs liver cancer growth by perturbing mitochondrial function.” *Hepatology (Baltimore, Md.)* 74\.1 (2021\): 233\.

[8](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-anchor-8-184035594)Zurlo, Giada, et al. “Prolyl hydroxylase substrate adenylosuccinate lyase is an oncogenic driver in triple negative breast cancer.” *Nature Communications* 10\.1 (2019\): 5177\.

[9](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-anchor-9-184035594)Carlisle, Anne E., et al. “Selenium detoxification is required for cancer\-cell survival.” *Nature metabolism* 2\.7 (2020\): 603\-611\.

[10](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-anchor-10-184035594)Lin, Charles Y., et al. “An oncogenic enhancer encodes selective selenium dependency in AML.” *Blood* 134 (2019\): 638\.

[11](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-anchor-11-184035594)Deng, Lu, et al. “NMT1 inhibition modulates breast cancer progression through stress\-triggered JNK pathway.” *Cell death \& disease* 9\.12 (2018\): 1143\.

[12](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-anchor-12-184035594)Tan, Xiang\-Peng, et al. “Blockade of NMT1 enzymatic activity inhibits N\-myristoylation of VILIP3 protein and suppresses liver cancer progression.” *Signal Transduction and Targeted Therapy* 8\.1 (2023\): 14\.

[13](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-anchor-13-184035594)Sun, Yi, et al. “N\-myristoyltransferase\-1 deficiency blocks myristoylation of LAMTOR1 and inhibits bladder cancer progression.” *Cancer letters* 529 (2022\): 126\-138\.

[14](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-anchor-14-184035594)Sangha, Randeep, et al. "A first\-in\-human phase I trial of daily oral zelenirstat, a N\-myristoyltransferase inhibitor, in patients with advanced solid tumors and relapsed/refractory B\-cell lymphomas." *Investigational New Drugs* 42\.4 (2024\): 386\-393\.

[15](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-anchor-15-184035594)Liang, Kaiwei, et al. “Targeting processive transcription elongation via SEC disruption for MYC\-induced cancer therapy.” *Cell* 175\.3 (2018\): 766\-779\.

[16](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-anchor-16-184035594)Schneider, Jaime L., et al. “GUK1 activation is a metabolic liability in lung cancer.” *Cell* 188\.5 (2025\): 1248\-1264\.

[17](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-anchor-17-184035594)Hidalgo‐Gutierrez, Agustin, et al. “Guanylate kinase 1 deficiency: a novel and potentially treatable mitochondrial DNA depletion/deletions disease.” *Annals of Neurology* 96\.6 (2024\): 1209\-1224\.

[18](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-anchor-18-184035594)Humphreys, Luke, Margarita Espona‐Fiedler, and Daniel B. Longley. “FLIP as a therapeutic target in cancer.” *The FEBS journal* 285\.22 (2018\): 4104\-4123\.

[19](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-anchor-19-184035594)Zhao, Zhuo, et al. “Prognostic value and immunomodulatory role of DNM1L in gastric adenocarcinoma.” *Frontiers in Oncology* 14 (2024\): 1453795\.

[20](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-anchor-20-184035594)Liang, Jing, et al. “DRP1 upregulation promotes pancreatic cancer growth and metastasis through increased aerobic glycolysis.” *Journal of Gastroenterology and Hepatology* 35\.5 (2020\): 885\-895\.

[21](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-anchor-21-184035594)Guo, Jing, et al. “Drp1 mediates high glucose\-induced mitochondrial dysfunction and epithelial\-mesenchymal transition in endometrial cancer cells.” *Experimental cell research* 389\.1 (2020\): 111880\.

[22](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-anchor-22-184035594)Mishra, Soumya Ranjan, et al. “Intricate role of DRP1 and associated mitochondrial fission signaling in carcinogenesis and cancer progression.” *Biochimica et Biophysica Acta (BBA)\-Reviews on Cancer* (2025\): 189453\.

[23](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-anchor-23-184035594)Middelbeek, Jeroen, et al. “TRPM7 is required for breast tumor cell metastasis.” *Cancer research* 72\.16 (2012\): 4250\-4261\.

[24](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-anchor-24-184035594)Wang, Zhi\-Bin, et al. “Roles of TRPM7 in ovarian cancer.” *Biochemical Pharmacology* 217 (2023\): 115857\.

[25](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-anchor-25-184035594)Chen, Liang, et al. “Downregulation of TRPM7 suppressed migration and invasion by regulating epithelial–mesenchymal transition in prostate cancer cells.” *Medical Oncology* 34\.7 (2017\): 127\.

[26](https://sarahconstantin.substack.com/p/cancer-selective-pan-essential-targets#footnote-anchor-26-184035594)Numata, Tomohiro, Takahiro Shimizu, and Yasunobu Okada. “Direct mechano\-stress sensitivity of TRPM7 channel.” *Cellular Physiology and Biochemistry* 19\.1\-4 (2007\): 1\-8\.