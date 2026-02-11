# The Enchippening of Medical Imaging

*Seeing inside the body with portable devices*

Published: 2023-09-27
Source: https://sarahconstantin.substack.com/p/the-enchippening-of-medical-imaging

---

[![](https://substackcdn.com/image/fetch/$s_!pdLD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4264dd8-754e-4489-9dd7-a1986722c59a_650x560.jpeg)](https://substackcdn.com/image/fetch/$s_!pdLD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4264dd8-754e-4489-9dd7-a1986722c59a_650x560.jpeg)

In my last post, I talked about [MEMS](https://sarahconstantin.substack.com/p/the-world-of-mems) devices, which combine mechanical and electrical components on integrated chips. In medical imaging in particular, MEMS improvements are leading to a revolution: unprecedentedly tiny, portable imaging devices. Machines that once required a specialist and a dedicated room are now available at the bedside or even in the home.

### Ultrasound

Medical ultrasound uses fall into roughly 3 categories:

* Ultrasound imaging

	+ Ultrasound waves are reflected differently by different materials, so sending ultrasound pulses into the body and measuring their reflections can produce an image of a slice inside the human body, known as a *sonogram*. Sonograms can show organs, blood vessels and blood clots, and fetal anatomy.
* [High\-intensity focused ultrasound](https://en.wikipedia.org/wiki/Focused_ultrasound)

	+ High\-intensity focused ultrasound delivers powerful mechanical stress and thermal heating to tissues, which allows it to destroy tissue inside the body without invasive surgery. It has been used to destroy benign and malignant cysts and tumors, to lesion regions of the brain in neurological disorders such as Parkinson’s
* [Low\-intensity](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4837316/) therapeutic ultrasound

	+ Low\-intensity ultrasound subjects tissues to gentle pressure and mild heating, which has therapeutic applications such as promoting bone, joint, and muscle healing after injury. It has also been studied as a brain modulation technique (it can either increase or decrease neural activity in the targeted region) and as a technique for [sensitizing tumors to chemotherapy.](https://www.washingtonpost.com/science/2023/09/25/brain-cancer-dipg-ultrasound-trial/)

Medical ultrasound, like all ultrasound, is produced by a transducer: a vibrating device that can either send or receive sound waves.

Traditionally, these were [bulk piezoceramic transducers](https://www.engineeringsolutions.philips.com/app/uploads/2019/03/CMUT-and-PMUT-Rob-van-Schaijk-November-2018.pdf), difficult to manufacture and never produced at mass scale. “Bulk”, in the world of microfabrication, means that the entire wafer is made out of a single material and diced into pieces. [Bulk piezoceramic materials like PZT are difficult to cut](https://viterbi-web.usc.edu/~yongchen/Papers/2017/10-1108_RPJ-11-2015-0162.pdf), making miniaturization and complex designs challenging.

In recent years, innovation in piezoelectric thin film materials and MEMS fabrication has led to the development of [PMUT](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9738559/)s, or piezoelectric micromachined ultrasound transducers.

PMUTs are phased arrays of small vibrating membranes over semiconductor substrates, which can either emit or detect ultrasound waves.

The principle of a [phased array](https://en.wikipedia.org/wiki/Phased_array_ultrasonics) means that, by precisely timing the frequency and delay of each transducer’s vibration, a pattern of constructive interference can be set up so that the aggregate ultrasound wave can be aimed at any angle.

PMUTs (and CMUTs, a similar MEMS ultrasound design based on capacitors rather than piezoelectrics) are easier to manufacture in an automated, low\-cost fashion; easier to miniaturize; compatible with higher frequencies and finer resolution; and compatible with 3D imaging.

These new ultrasound technologies have led to an explosion of miniaturized, affordable ultrasound.

Instead of a device on a cart, operated by a dedicated imaging technician, ultrasound can now be handheld. (The first handheld ultrasound was released in [1999](https://www.sonosite.com/blog/10000-sonosite-hand-carried-ultrasound-systems-now-clinical-use); [Butterfly Network’s](https://www.butterflynetwork.com/iq-ultrasound-individuals) handheld ultrasound, [released in 2018](https://www.butterflynetwork.com/press-releases/butterfly-iq-pluss-press-release), can plug into a smartphone.)

This means a [wide array of new applications for ultrasound](https://www.newyorker.com/science/annals-of-medicine/could-ultrasound-replace-the-stethoscope) have opened up. Imagine what could happen if any healthcare worker, in any environment, could instantly peek inside the body to see what’s going on:

* ultrasound in the emergency department or even the ambulance, for early detection of strokes, pulmonary embolisms, hemorrhages, and other life\-threatening emergencies.
* ultrasound to diagnose patients in rural or impoverished contexts where traditional hospital equipment is unavailable
* ultrasound as the “new stethoscope”, as a complement to traditional physical exams, for detecting heart and lung problems and [bowel obstructions](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8606703/) .
* ultrasound for imaging plaque [inside arteries](https://en.wikipedia.org/wiki/Intravascular_ultrasound) for placing stents and otherwise planning cardiac surgery

Ultrasound can even go further. Patients with chronic conditions could [self\-monitor with handheld ultrasound at home](https://www.nature.com/articles/s41598-022-24513-x), or [detect breast tumors with wearable ultrasound devices.](https://news.mit.edu/2023/wearable-ultrasound-scanner-breast-cancer-0728) You can already get a [home handheld fetal ultrasound monitor](https://pulsenmore.com/), to check on high\-risk pregnancies between doctor visits.

Ultrasound combines well with AI image classification to assist diagnosis or risk prediction. There are a lot of potential applications in using AI to make newly\-ubiquitous ultrasound usable for nonspecialists or even patients.

There’s also a whole world of new experimental methodologies for combining ultrasound with other imaging technologies. For instance, you can get microscopic subcutaneous images by combining ultrasound with lasers, in [photoacoustic microscopy.](https://en.wikipedia.org/wiki/Photoacoustic_microscopy)

### Optical Coherence Tomography

[Optical coherence tomography](https://en.wikipedia.org/wiki/Optical_coherence_tomography) is a form of medical imaging based on interferometry — mapping the composition of tissue based on how different materials scatter light.

It allows 2\-D and 3\-D scans, at about a micron resolution and millimeter depth. The typical use case is in scanning the retina to diagnose diseases of the eye, such as macular degeneration, diabetic retinopathy, and glaucoma.

Interferometry traditionally works by having light bounce off mirrors and through lenses, but it turns out you can [do the whole thing on a chip using integrated photonics](https://sci-hubtw.hkvisa.net/10.1515/aot-2017-0061) techniques (very similarly fabricated to semiconductor devices.)

That means optical coherence tomography, once bulky, [can be miniaturized.](https://publishing.aip.org/publications/latest-content/miniaturizing-medical-imaging-sensing-technology/) Handheld OCT and ubiquitous screening for eye disorders could be [on the horizon.](https://onlinelibrary.wiley.com/doi/full/10.1002/tbio.202100007)

### Magnetic Resonance Imaging

Magnetic resonance imaging (MRI) is the gold standard for radiology for producing high\-resolution images of soft tissues inside the body.

It works by placing the entire patient inside a strong magnetic field. This allows the atoms to be excited by a radiofrequency pulse and to emit a signal that depends on the tissue composition.

MRI machines are huge (room\-sized), difficult to install, and cost millions of dollars. The powerful magnetic fields are produced by superconducting magnets, which work better when they’re large. So how could you possibly miniaturize an MRI?

By using [much weaker permanent magnets](https://www.science.org/content/article/mri-all-cheap-portable-scanners-aim-revolutionize-medical-imaging), which produce weaker, noisier signals, but capturing a lot more of them and using fast electronics and advanced computational techniques to reconstruct fairly clear images. Not as high resolution as a conventional MRI — but less than a quarter the cost, and portable enough to wheel to a patient’s bedside.

Hyperfine’s portable MRI, approved in 2020, can scan ICU patients who are too sick to move, or patients in remote or impoverished areas where conventional MRIs are out of reach.

(Amazingly, the same guy — [Jonathan Rothberg](https://en.wikipedia.org/wiki/Jonathan_Rothberg) — founded both Hyperfine and Butterfly Networks, *and* the company that sequenced the first whole individual human genome, *and* several more biotech companies that sound similarly important. Are we sure he’s not actually 10 people in a trenchcoat?)

### Magnetoencephalography

You can detect brain activity noninvasively by measuring magnetic fields produced by neurons firing.

It’s called [magnetoencephalography](https://en.wikipedia.org/wiki/Magnetoencephalography), and it’s used for detecting the source of epilepsy. It’s less noisy and distorted by hair and head movements than the better known EEG that measures electricity.

It’s only in the late 2010’s that on\-chip, highly performant, miniaturized arrays of magnetometers, known as [optically pumped magnetometers](https://www.cell.com/trends/neurosciences/fulltext/S0166-2236(22)00102-3), began to be produced. You can wear a helmet with magnetometers all over it and detect neural activity noninvasively in real time. A new startup, [Sonera Magnetics](https://spectrum.ieee.org/startups-new-type-of-magnetic-sensor-could-make-highperformance-brain-imaging-more-affordable-and-portable), is currently productizing these innovations.

### There’s More

I’m out of time for now, but this is barely scratching the surface of medical imaging techniques that are enabled by improvements in on\-chip manufacturing of MEMS, optical, and semiconductor components. On\-chip microscopy? Two\-photon microscopy *in an endoscope*? There’s some intriguing stuff out there.

We might need to rethink assumptions like “if you want microscopic resolution you'll need to take a biopsy sample”.