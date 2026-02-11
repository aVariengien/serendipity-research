# EEGs: What Can They Do?

*Brain Waves Galore*

Published: 2024-01-27
Source: https://sarahconstantin.substack.com/p/eegs-what-can-they-do

---

[![](https://substackcdn.com/image/fetch/$s_!regV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8d9a2529-22e7-4c4a-b94e-399041d46dc9_640x480.jpeg)](https://substackcdn.com/image/fetch/$s_!regV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8d9a2529-22e7-4c4a-b94e-399041d46dc9_640x480.jpeg)

This baby is getting an EEG.

An electroencephalogram, or EEG for short, is the oldest and simplest way of noninvasively measuring brain activity.

An EEG is simply a collection of electrodes, mounted all over the scalp, recording fluctuations in electrical activity. Electrode measurements are supposed to correspond to the (averaged, cumulative) electrical activity in the brain, particularly the pyramidal neurons of the cerebral cortex.

It should be obvious by looking that a standard EEG is not great for *localizing* brain activity. Electrodes are placed fairly far apart, their placement is not precise, and they average electrical activity over a large area. You can’t use EEGs to tell you which regions of the brain are active at a given time, beyond the crudest estimates.

On the other hand, an EEG can give potentially rich and informative data to *characterize* brain activity. Which mental states, or neurological/psychiatric disease states, have distinctive EEG signatures? Can you “read minds” off an EEG? Diagnose diseases? Track your mood?

### What’s In An EEG?

[![](https://substackcdn.com/image/fetch/$s_!dFTe!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcc2041b4-216c-4c83-a17b-94229c355981_1696x837.png)](https://substackcdn.com/image/fetch/$s_!dFTe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcc2041b4-216c-4c83-a17b-94229c355981_1696x837.png)

Here’s an example EEG graph of a healthy awake adult.

Each black line represents the measurement from a single scalp electrode. The horizontal axis is time; the vertical axis is electrical potential. (The bottom red line is an electrocardiogram, measuring heart activity, not part of the EEG itself.)

The frequency of the oscillations determines the “waves”.

* Delta waves (\<4 Hz): deep sleep
* Theta waves (4\-7 Hz): drowsiness
* Alpha waves (8\-12 Hz): relaxation
* Beta waves (13\-30 Hz): alert
* Gamma waves (\>32 Hz): conscious perception

(I like this [online binaural beat generator](https://mynoise.net/NoiseMachines/binauralBrainwaveGenerator.php)  to build intuition for how fast these frequencies are. At around 12 Hz the “beats” become too fast to hear and blur into a slightly strobey hum; by 20 Hz there’s no audible jitter, just a smooth tone.)

There are more types of “brain waves” characteristic of [normal sleep](https://www.learningeeg.com/normal-asleep) and [motor artifacts](https://www.learningeeg.com/artifacts) — sail\-like POSTS at the onset of sleep, bursty “sleep spindles” during stage II, wiggly K\-complexes when a noise disturbs the sleeper, jagged eye movements during dreaming, deep dips from eye blinks and high\-frequency bursts from chewing or forehead movements, slow waves from head movement or sweat.

And, of course, there are characteristic abnormalities of various forms of epileptic seizures.

### Wait — Brain Waves?

Why are there “brain waves” at all?

Why is there periodicity or synchronization of the electrical activity across the brain?

Well, to be fair, there isn’t *perfect* periodicity in a normal brain EEG. Too\-perfect regular waves are actually a sign of seizures. And there isn’t perfect uniformity across electrodes either; you generally expect lower frequencies at the back of the head than the front.

But you do see rough correspondence between EEG frequency bands and mental state, suggesting that “brain waves” — some consistent range of frequencies, across wide areas of the cortex and over appreciable time intervals — are a thing.

The general phenomenon — faster, less synchronized electrical activity in alert states, slower and more regular activity in sleep or in some kinds of brain lesions — is found in other mammals, including cats and monkeys, as well as humans.[1](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-1-141076087)

Even frogs have “brain waves”, and frog EEGs are more or less the same even when you remove different parts of the brain. Invertebrates, on the other hand, do not have slow waves; instead they have irregular high frequency activity and spikes.[2](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-2-141076087)

If EEG signal corresponds to the *density of active synapses* in a region of cortex[3](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-3-141076087), then time periodicity in EEG could mean that brain activity *travels* around the cortex, from one patch of neurons to the adjacent connected ones. You would expect some amount of periodicity just from graph dynamics.

A “hot spot” would travel to its neighbors, and then to their neighbors, and finally return to its origin in just as much time as it takes to traverse a cycle in the graph. If there were multiple cycle lengths starting at a given point, there would be multiple frequencies.

The first neural field model, from Wilson and Cowen in 1973[4](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-4-141076087), considered the cortex as a 2\-d sheet, with both excitatory and inhibitory neurons affecting their neighbors.

[![](https://substackcdn.com/image/fetch/$s_!lXM2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdba00c71-a2eb-4fad-84c4-3ca82fb9c631_940x532.png)](https://substackcdn.com/image/fetch/$s_!lXM2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdba00c71-a2eb-4fad-84c4-3ca82fb9c631_940x532.png)

This is wildly oversimplified, of course. Cortical neurons don’t only connect to their immediate neighbors, they also have a smaller fraction of long\-range, myelinated (white matter) connections, to deep subcortical hubs that project back to distant parts of the cortex. The brain’s connections look rather like a [small\-world graph](https://en.wikipedia.org/wiki/Small-world_network) — mostly local connections with a few long\-range ones, resulting in a small average distance between any two neurons, and in fact the *same* distribution of distances no matter how “big” the brain is (how many neurons.)

More recent neural field models incorporate actually\-measured brain connectivity data, but they also generate solutions that include oscillatory patterns, including traveling waves, rotating waves, sources, and sinks.[5](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-5-141076087)

**Traveling Wave:**

**Spiral Wave:**

**Source/Sink:**

These predicted oscillatory waves, however, are much faster than EEG frequencies; they are over 100 Hz. To get EEG\-timescale periodicity you have to look at the “metastable” dynamics of these cortical oscillations — it’s typically 50\-100 ms between *transitions* between one oscillation type and another, with a “tail” of slower transitions. This spans the range of gamma through delta waves observed on EEGs, so it’s at least a possible mechanism for where those waves come from.

As far as I can tell, we don’t know where, mechanistically, most of the “named” EEG waves come from. Why are there 1\-3 Hz waves in deep sleep, for instance? Where is that timescale derived from? Dunno.

One exception I could find was a plausible mechanism for gamma waves in particular.[6](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-6-141076087) Gamma oscillations are simple and easy to generate: unlike slower brain waves, they show up in tiny chunks of cortex, and in insects. You can induce gamma oscillations artificially in a slice of neural tissue, just by chemically blocking neurons from firing for a bit so they all “start up together.” The period of the oscillation depends on the length of the inhibitory delay. In a living brain, inhibitory delay is produced by inhibitory interneurons, and the natural “silent period” of the GABA\-A receptors is 15\-30 ms, exactly corresponding to the frequency of gamma oscillations. So, very roughly, it seems like gamma oscillations come from cortical neurons *locally* inhibiting their neighbors: very simple, not dependent on any specifics of mammalian brain anatomy, just a thing cortical tissue does by default.

Overall, I think we expect brain waves to be emergent from neural connectivity dynamics, but that’s a very vague and general claim that leaves tons of wiggle room for different just\-so stories.

### EEG in Non\-Seizure Disorders

Do people with brain disorders *other than the obvious ones* (epilepsy, coma, stroke, etc) have fucked up EEGs?

You’d expect, whether the answer is yes or no, to find some papers saying yes. EEG data is *very* high dimensional (it’s a time series!) so if you try hard and believe in yourself you’ll be able to use shady statistical methods to find some difference between cases and controls.

So, let’s say we go back in time to 1954, back when there were fewer scientists, fewer papers, weaker computers, and (thus one hopes), less nonsense getting published. Were *they* seeing screwy EEGs in psychiatric or developmentally disabled patients?[7](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-7-141076087)

First of all, *healthy controls* have a high rate of “abnormality” in EEG to begin with, ranging from 5%\-20% across 11 studies.

But “abnormality” rates were higher still in samples schizophrenic patients (9%\-60% across 10 studies, mean 30%). In particular there may have been more “high voltage fast” activity in the schizophrenics than controls.

Psychopaths, also, had high (47%\-58%) rates of “abnormal” EEGs, especially high rates of “slow” activity.

Ok, so there’s plausibly *something* going on with EEGs in psychopathology. What about more recent data, aggregated across lots and lots of (maybe terrible) studies?

A review of 184 publications between 1993 and 2018, looking at EEGs of control and psychiatric patients, found increases in slow\-wave power (delta and theta) across several disorders (depression, ADHD, schizophrenia, OCD, alcoholism.)[8](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-8-141076087)

In fact, elevated theta vs. beta waves are approved by the FDA as a diagnostic biomarker of ADHD…except that over the next decade, subsequent studies failed to replicate significant differences between theta/beta ratios in ADHD vs. control subjects.[9](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-9-141076087)

“EEG slowing”, i.e. elevated theta and/or delta wave power, relative to alpha, beta, or gamma, has been reported in a variety of disorders, in fact, from dementia[10](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-10-141076087)[11](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-11-141076087) and Parkinson’s,[12](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-12-141076087) to encephalopathy, to stroke, to traumatic brain injury.[13](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-13-141076087) It shows up as associated with neurologic symptoms (especially dementia and cognitive impairment) within diseases that don’t always come with neurological problems, like lupus.[14](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-14-141076087)

On a power spectrum graph, EEG slowing looks like the red lines in these graphs comparing delirium to control ICU patients[15](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-15-141076087):

[![](https://substackcdn.com/image/fetch/$s_!sH-k!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F652e1fc7-9d4d-4e2d-ab96-aca5807c32f9_1044x1504.png)](https://substackcdn.com/image/fetch/$s_!sH-k!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F652e1fc7-9d4d-4e2d-ab96-aca5807c32f9_1044x1504.png)

Delirious patients have *way less* activity in the high\-frequency ranges of alpha, beta, and especially gamma activity associated with conscious, awake states.

This makes a rough sort of sense: being “awake” is sort of like having your brain “all the way on”, and it makes sense that mental impairment looks more like sleep than waking.

Power spectrum isn’t a very specific diagnostic of any particular condition (or even generic sick vs healthy) but “EEG Slowing Is A Bad Thing” does seem to be a fairly robust finding.

### What About Consumer EEG?

What if you’re a neurotech fan (or developer)? Your interest is in *healthy* people (maybe yourself!) and you want to know if you’ll get anything interesting out of an EEG rig that’s *affordable and usable in the home*.

“Interesting” here means both “is it really measuring my brain activity?” and “will observations about healthy people correspond to either intrapersonal or interpersonal variation along dimensions we care about, like mood, mental health, alertness, or sleep quality?”

The good news is, there are lots of consumer\-grade EEG devices out there:

* the [Neurosky Mindwave](https://neurosky.com/biosensors/eeg-sensor/biosensors/) ($130\)
* the [Muse](https://choosemuse.com/) ($445\)
* the [Emotiv Epoq](https://www.emotiv.com/epoc-x/) ($999\)
* the [OpenBCI Ultracortex](https://shop.openbci.com/products/the-complete-headset-eeg) ($2399\)

Consumer EEGs usually have fewer electrodes than research\-grade, and have poorer signal\-to\-noise ratios. However, they reliably detect the same event\-related potentials in head\-to\-head comparison studies.[16](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-16-141076087)

In resting\-state EEGs, consumer devices are way more prone to eyeblink and muscle movement artifacts:

[![](https://substackcdn.com/image/fetch/$s_!8Uou!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F10fa0d3a-a9fc-461f-abf8-1a58332b7eaa_743x556.jpeg)](https://substackcdn.com/image/fetch/$s_!8Uou!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F10fa0d3a-a9fc-461f-abf8-1a58332b7eaa_743x556.jpeg)

A,B: two clinical\-grade EEGs; C, D: the Muse and Mindwave consumer EEGs

The big dips are eye blinks.

The power spectral density functions look reasonable for the MindWave but not for the Muse:[17](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-17-141076087)

[![](https://substackcdn.com/image/fetch/$s_!KYWN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb0afd4b3-d4d4-4153-8e27-b99902fd9600_680x461.jpeg)](https://substackcdn.com/image/fetch/$s_!KYWN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb0afd4b3-d4d4-4153-8e27-b99902fd9600_680x461.jpeg)

Higher frequency components are supposed to be lower power! the Muse is Messed Up.

The good news about consumer devices is that they’re pretty decent at eye\-tracking, which makes them useful for videogames, VR, and brain\-computer interfaces.

For instance, videogame streamer Perry Karyal [rigged an Emotiv EEG headset to play Elden Ring](https://spectrum.ieee.org/elden-ring-hands-free-controller) with mental visualizations, “imagining pushing something forward”.

It seems like neurotech companies are particularly interested in EEG in combination with gaming or simulation applications.

The new OpenBCI spinout company, [Galea](https://galea.co/), combines an EEG headset with other biophysical measurements (EMG facial muscle movement detection, EOG eye movement detection, EDA sweat sensor, and PPG forehead heart rate monitor) and a [Varjo VR](https://varjo.com/xr-headsets/) headset. Presumably, the intent is to use EEG and other biosensor data to monitor the user’s experience and/or navigate through a VR environment.

The bottom line is, consumer EEG is noisier than clinical, primarily because it uses fewer electrodes and dry electrodes (no gel). But it’s still sometimes good enough to get usable results.

Medical professionals who analyze EEGs in clinical settings can usually distinguish muscle and eye movement artifacts from bona fide brainwaves by eye.

That suggests that if the application isn’t time\-sensitive, even if you have a lower\-quality EEG headset, if you gather enough data you can compensate for noise by just throwing away time periods with non\-brainwave artifacts.

As for detecting meaningful brainstates in healthy people, it’s hard to tell (because it’s easy to run a terrible classification study with \~\~machine learning\~\~) but, for instance, studies on detecting drowsiness on the MindWave, Ultracortex, Muse, and Emotiv ranged from 70%\-97% accurate.[18](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-18-141076087)

I’m reasonably hopeful about the prospects of consumer EEG to differentiate states like drowsiness/alertness or stress/relaxation, since we *already pretty much expect those to be visible in EEG spectral data*.

The possibilities of mental visualization being detectable are even more intriguing, and I’ll have to learn more about that. How close can we really come to “mind\-reading” with EEG alone? It sounds far\-fetched, but We Shall See.

[1](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-anchor-1-141076087)Ellingson, Robert J. "Brain waves and problems of psychology." *Psychological Bulletin* 53\.1 (1956\): 1\.

[2](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-anchor-2-141076087)Bullock, Theodore H. "Problems in the comparative study of brain waves." *The Yale journal of biology and medicine* 17\.5 (1945\): 657\.

[3](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-anchor-3-141076087)Nunez, Paul L., and Ramesh Srinivasan. "A theoretical basis for standing and traveling brain waves measured with human EEG with implications for an integrated consciousness." *Clinical neurophysiology* 117\.11 (2006\): 2424\-2435\.

[4](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-anchor-4-141076087)Wilson, Hugh R., and Jack D. Cowan. "A mathematical theory of the functional dynamics of cortical and thalamic nervous tissue." *Kybernetik* 13\.2 (1973\): 55\-80\.

[5](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-anchor-5-141076087)Roberts, James A., et al. "Metastable brain waves." *Nature communications* 10\.1 (2019\): 1056\.

[6](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-anchor-6-141076087)Buzsaki, Gyorgy. *Rhythms of the Brain*. Oxford university press, 2006\.

[7](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-anchor-7-141076087)Ellingson, R. J. "The incidence of EEG abnormality among patients with mental disorders of apparently nonorganic origin: a critical review." *American Journal of Psychiatry* 111\.4 (1954\): 263\-275\.

[8](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-anchor-8-141076087)Newson, Jennifer J., and Tara C. Thiagarajan. "EEG frequency bands in psychiatric disorders: a review of resting state studies." *Frontiers in human neuroscience* 12 (2019\): 521\.

[9](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-anchor-9-141076087)Arns, Martijn, C. Keith Conners, and Helena C. Kraemer. "A decade of EEG theta/beta ratio research in ADHD: a meta\-analysis." *Journal of attention disorders* 17\.5 (2013\): 374\-383\.

[10](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-anchor-10-141076087)Claus, Jules J., et al. "Slowing on quantitative spectral EEG is a marker for rate of subsequent cognitive and functional decline in early Alzheimer disease." *Alzheimer Disease \& Associated Disorders* 12\.3 (1998\): 167\-174\.

[11](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-anchor-11-141076087)Roh, Jee Hoon, et al. "Region and frequency specific changes of spectral power in Alzheimer’s disease and mild cognitive impairment." *Clinical Neurophysiology* 122\.11 (2011\): 2169\-2176\.

[12](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-anchor-12-141076087)Morita, Akihiko, Satoshi Kamei, and Tomohiko Mizutani. "Relationship between slowing of the EEG and cognitive impairment in Parkinson disease." *Journal of Clinical Neurophysiology* 28\.4 (2011\): 384\-387\.

[13](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-anchor-13-141076087)Nuwer, Marc R., et al. "Routine and quantitative EEG in mild traumatic brain injury." *Clinical Neurophysiology* 116\.9 (2005\): 2001\-2025\.

[14](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-anchor-14-141076087)Ritchlin, Christopher T., et al. "Quantitative electroencephalography: a new approach to the diagnosis of cerebral dysfunction in systemic lupus erythematosus." *Arthritis \& Rheumatism* 35\.11 (1992\): 1330\-1342\.

[15](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-anchor-15-141076087)Hunter, Andrew, et al. "Delirium screening in the intensive care unit using emerging QEEG techniques: A pilot study." *AIMS neuroscience* 7\.1 (2020\): 1\.

[16](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-anchor-16-141076087) Joshua Sabio, Nikolas S Williams, Genevieve M McArthur, Nicholas A Badcock. “A scoping review on the use of consumer\-grade EEG devices for research.” bioRxiv 2022\.12\.04\.519056; doi: https://doi.org/10\.1101/2022\.12\.04\.519056

[17](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-anchor-17-141076087)Ratti, Elena, et al. "Comparison of medical and consumer wireless EEG systems for use in clinical trials." *Frontiers in human neuroscience* 11 (2017\): 398\.

[18](https://sarahconstantin.substack.com/p/eegs-what-can-they-do#footnote-anchor-18-141076087)LaRocco, John, Minh Dong Le, and Dong\-Guk Paeng. "A systemic review of available low\-cost EEG headsets used for drowsiness detection." *Frontiers in neuroinformatics* (2020\): 42\.