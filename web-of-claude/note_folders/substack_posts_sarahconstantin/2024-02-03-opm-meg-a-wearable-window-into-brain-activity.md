# OPM-MEG: A Wearable Window Into Brain Activity?

*A slightly deeper dive into the tech*

Published: 2024-02-03
Source: https://sarahconstantin.substack.com/p/opm-meg-a-wearable-window-into-brain

---

[![](https://substackcdn.com/image/fetch/$s_!G5hf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F97082d68-ef5a-40ff-acbf-4a61974a838e_1200x978.jpeg)](https://substackcdn.com/image/fetch/$s_!G5hf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F97082d68-ef5a-40ff-acbf-4a61974a838e_1200x978.jpeg)

OPM\-MEG is mostly used to pinpoint the location of seizures in kids with epilepsy.

In a [previous post](https://sarahconstantin.substack.com/p/noninvasive-brain-activity-imaging) I compared different methods for noninvasively measuring brain activity in humans.

Why do you want to measure brain activity after all?

* basic research 

	+ we want to understand the function of different parts of the brain
	+ or the underlying abnormalities causing neurological \& psychiatric disorders
* medical diagnosis

	+ if your brain activity is weird maybe that can detect or classify a brain problem
* other medical decisionmaking

	+ such as “use EEG to check if the anesthesia is working and the patient is unconscious, before operating”

And, most intriguingly given the context of neuromodulation I’ve been writing about lately

* testing the effectiveness of neuromodulation or providing it with closed\-loop control.

If you want a device that reliably stimulates a location in the brain, you need a sanity\-check measurement that neural activity in that brain location *was in fact stimulated*.

This is a universal engineering thing. You do not *really* have a device that does X if you don’t have a way to measure whether X happens when you turn on the device.

Moreover, for a lot of brain stimulation applications you might want *closed\-loop control*, i.e. what you want it to do to the brain will depend on what the brain is doing.[1](https://sarahconstantin.substack.com/p/opm-meg-a-wearable-window-into-brain#footnote-1-141317639) To have a closed\-loop neuromodulation device, you need the ability to “read” brain activity as well as “write” (modulate/stimulate) it.[2](https://sarahconstantin.substack.com/p/opm-meg-a-wearable-window-into-brain#footnote-2-141317639)

If you’re looking for a brain activity measurement method that’s a good complement to neuromodulation, it needs to have *good spatial localization* (it needs to be able to show you a fairly high\-resolution map of brain activity) and it needs to be practical to use simultaneously with the neuromodulation, so you can see how you’re modifying brain activity *while you do it*. Ideally, both neuromodulation and brain activity measurement would be portable or even integrated into the same wearable device.

That rules out EEG (poor spatial resolution) and MRI (extremely non\-portable) and a lot of other brain activity measurement modalities.

The exception, it seems, is OPM\-MEG, or optically pumped magnetometer\-based magnetoencephalopathy.

MEG measures magnetic fields created by brain activity. It has high spatial *and* temporal resolution, and it works anywhere in the brain (not just the surface of the cortex.) But, up until recently, it’s been nearly as bulky as an MRI and much less common.

The new optically pumped magnetometers are very precise, miniature devices that measure magnetic fields and *don’t* need a ton of bulky equipment to create super\-cold conditions for superconductors. With OPMs, you can now make wearable (though not wireless) MEG helmets, as seen above.

Could this be the brain activity measurement of the future? Are there any technical barriers stopping us from further miniaturizing and mass\-producing these devices and dramatically expanding their use cases? Could the OPM\-MEG replace the fMRI or PET as the gold standard for mapping brain activity? Let’s investigate.

### What’s the Current State of OPM\-MEG Machines?

[![](https://substackcdn.com/image/fetch/$s_!WVA5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F92abc481-7fd4-4f67-b5c2-90b5f484406f_880x1057.png)](https://substackcdn.com/image/fetch/$s_!WVA5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F92abc481-7fd4-4f67-b5c2-90b5f484406f_880x1057.png)

The BrainBox Mag4Health

The Brainbox [Mag4Health](https://brainbox-neuro.com/products/mag4health-he-opm-meg-system) and [Cerca system](https://www.cercamagnetics.com/cerca-opm-meg) are both commercially available devices.

The Cerca device needs to be used in a magnetically shielded room; the Brainbox device doesn’t say so on the website but their latest [paper](https://www.mdpi.com/1424-8220/23/5/2801) tested the device in a magnetically shielded room.

[QuSpin,](https://quspin.com/) a company that makes optically pumped magnetometers, charges $950 for an [MEG cap](https://quspin.com/meg-cap-1-0/) that holds [30 sensors](https://quspin.com/products-qzfm/).

The total cost would be $231,950 for the cap \+ sensors.

Including the shielded room, as of a [2022 article](https://www.researchgate.net/publication/362035938_Wearable_OPM-MEG_a_changing_landscape_for_epilepsy), the up\-front cost of an OPM\-MEG system is about $1\.4M, plus an ongoing expenditure of $70,000/year.

This is comparable to the [$1\.2M\-$2\.1M price](https://www.meridianleasing.com/resources/blog/mri-machine-buyers-guide-options-and-pricing) of a new 3T MRI machine suitable for fMRI measurements.

In short, currently OPM\-MEG devices are ready for purchase (albeit still mostly\-experimental), require a special room for use, and cost about as much as an MRI.

### What’s An Optically\-Pumped Magnetometer, Anyway?

[Optical pumping](https://en.wikipedia.org/wiki/Optical_pumping) is when you use light to “pump” electrons from a lower energy level to a higher one.

Optically pumped magnetometers work via the [Zeeman effect](https://en.wikipedia.org/wiki/Optical_pumping). In the presence of a magnetic field, spectroscopic lines (the characteristic frequency absorbed by a substance) split into multiple wavelengths.

You can use this splitting to detect the presence and intensity of a magnetic field. First, the gas is excited (or “polarized”) via optical pumping of polarized light, moving its electrons into higher\-energy states; then, the spectral absorption pattern of that gas as polarized light is shone on it will depend on the strength of the magnetic field.

Typically, optically pumped magnetometers use gaseous metals from the first column of the periodic table, like potassium, cesium, or rubidium.[3](https://sarahconstantin.substack.com/p/opm-meg-a-wearable-window-into-brain#footnote-3-141317639)

Sealing alkali vapor in a microfabricated cell has been possible since the early 2000s, when it was used for making atomic clocks. There are a wide variety of methods of getting the vapor into the cell.[4](https://sarahconstantin.substack.com/p/opm-meg-a-wearable-window-into-brain#footnote-4-141317639)

Some fabrication methods are compatible with wafer\-scale production[5](https://sarahconstantin.substack.com/p/opm-meg-a-wearable-window-into-brain#footnote-5-141317639):

[![](https://substackcdn.com/image/fetch/$s_!pjhg!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd65c0db6-e19b-457a-97bb-1dd8d449feaa_592x420.png)](https://substackcdn.com/image/fetch/$s_!pjhg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd65c0db6-e19b-457a-97bb-1dd8d449feaa_592x420.png)

A wafer of alkali vapor cells, produced by Vapor Cell Technologies LLC

### Should We Expect The Price of OPMs to Fall?

An optically pumped magnetometer is what you might call a “specialty” microfabricated device.

That is, it’s got electronic/semiconductor components (laser, photodetector) and *also* some components that aren’t traditional semiconductors (the vapor cell, which is a box full of vapor.) You might get it made at a MEMS foundry.[6](https://sarahconstantin.substack.com/p/opm-meg-a-wearable-window-into-brain#footnote-6-141317639)

MEMS devices are made using*[pretty much](https://sarahconstantin.substack.com/p/the-world-of-mems)*[, but](https://sarahconstantin.substack.com/p/the-world-of-mems) *[not exactly](https://sarahconstantin.substack.com/p/the-world-of-mems)* [the same techniques](https://sarahconstantin.substack.com/p/the-world-of-mems) you’d use to make ordinary semiconductor devices.

As I said in an [earlier post](https://sarahconstantin.substack.com/p/the-enchippening),

> Fundamentally, *computer chips are made by putting flat layers of stuff on top of other flat layers of stuff*.

A vapor cell is a little trickier. It’s not flat; it has depth. Micromachining high\-aspect\-ratio (aka non\-flat) features can require special methods. Also, you have to get gas into the cell and seal it so it stays in there; that, too, requires special tools not universal in semiconductor world.

So, some questions we might ask about whether vapor cells will get cheaper over time:

* what’s the scale of the market today?
* what kind of demand is there (and could be in future) for vapor cells?

	+ what can you do with vapor cells besides magnetoencephalography? (which tbh is *not* a huge market so far)[7](https://sarahconstantin.substack.com/p/opm-meg-a-wearable-window-into-brain#footnote-7-141317639)
* what kind of recent progress have we seen in vapor cell fabrication?

#### Vapor Cell Manufacturing

Alkali vapor cells seem to be made by fairly small companies, at a small scale.

* [QuSpin](https://quspin.com/), founded in 2012, with about $15M in US gov’t funding[8](https://sarahconstantin.substack.com/p/opm-meg-a-wearable-window-into-brain#footnote-8-141317639) and 13 employees, makes optically pumped magnetometers, mostly for MEG applications.
* [Vapor Cell Technologies](https://vaporcelltechnologies.com/), founded in 2020 with \<$1M in funding, makes wafer\-scale microfabricated vapor cells for high\-precision frequency and length measurements. They boast of being able to make “thousands” of cells.
* [Twinleaf](https://twinleaf.com/), founded by physicists in 2007, makes vapor cells and precision magnetometers with only a few employees.
* [Mag4Health](https://www.mag4health.com/), founded in 2021 with $7\.5M in funding, makes helium\-based optically pumped magnetometers

[An SBIR grant](https://www.sbir.gov/node/2102051) (the US government’s main way of funding engineering R\&D in small businesses, especially applications with defense relevance) was offered in 2022 for a wafer\-scale vapor cell manufacturing process which could raise yields to over 80%.[9](https://sarahconstantin.substack.com/p/opm-meg-a-wearable-window-into-brain#footnote-9-141317639)

Mature wafer\-scale fabrication processes will typically have yields over 90% — this suggests that we’re still in the early part of the process development curve for vapor cells, with lots of room for improvement.

#### What Else Can You Use Magnetometers And Vapor Cells For?

Lots of things!

But…not very high *demand volume* things, so far.

Magnetometers are used in aerospace for navigation and for satellite and spacecraft measurements of the Earth’s magnetic field and properties of other planets.[10](https://sarahconstantin.substack.com/p/opm-meg-a-wearable-window-into-brain#footnote-10-141317639)

Magnetometers are also used industrially for nondestructive testing/imaging, including of metals, batteries, and underwater infrastructure.[11](https://sarahconstantin.substack.com/p/opm-meg-a-wearable-window-into-brain#footnote-11-141317639)

Additionally, they are used for geological and oceanographic surveys[12](https://sarahconstantin.substack.com/p/opm-meg-a-wearable-window-into-brain#footnote-12-141317639) — detecting ferrous metals, variation in the Earth’s magnetic field, underwater cables and pipelines, and more.

The market for magnetometers is about [$2B](https://www.alliedmarketresearch.com/press-release/magnetometer-market.html), though of course most of these don’t need to be as small or as precise as optically pumped magnetometers.

Atomic vapor cells more broadly are used in multiple quantum sensing applications in addition to magnetometers: atomic clocks, gas sensors, and GHz/THz imaging.[13](https://sarahconstantin.substack.com/p/opm-meg-a-wearable-window-into-brain#footnote-13-141317639)[14](https://sarahconstantin.substack.com/p/opm-meg-a-wearable-window-into-brain#footnote-14-141317639)

Atomic clocks are used for GPS satellites, high\-frequency trading, and various astronomical and fundamental physics research applications that require extremely precise timekeeping. What could we do with them if they were cheap and small? Some quotes from researchers suggest there might be networking, navigation, and defense applications.[15](https://sarahconstantin.substack.com/p/opm-meg-a-wearable-window-into-brain#footnote-15-141317639)

But really, it’s hard to say. It seems like a very small, niche, specialized field at this point, without a clear application to motivate massive scale\-up. Will we need tons more precision navigation sensors if we start to launch a lot more satellites and rockets? Will the kinds of better geological measurements enabled by atomic vapor cells be a big deal for the oil/gas/mining industries? What kinds of new computer/networking things could you do if every computer could have its own miniature atomic clock? At this high level of overview, I personally don’t know.

#### Prognostication: Unclear

Right now, optically pumped magnetometer tech is super new.

The field is tiny, it’s focused on very research\-and\-defense\-y applications, and manufacturing is small\-scale and not very efficient at this point.

Should you bet on OPMs getting a lot cheaper in the near future?

Well…I’m not seeing obvious indications either way. I’m not seeing *super big and obvious* upcoming market applications that would motivate a lot of investment in scaling the technology; but of course that doesn’t mean there aren’t any!

So TL;DR: I dunno.

Sorry about that; if you want honest assessments on a tight time frame, sometimes I’ve got to come up empty.

### What About Shielding?

Sadly, you need to be in a magnetically shielded room for OPM\-MEG to work.

This means that currently there’s no chance of a portable OPM\-MEG device that you wear throughout your daily life to continuously monitor your brain activity.

It also puts some constraints on how cheap OPM\-MEG could possibly get (specially\-refitted rooms are never going to be trivially cheap) unless there turns out to be some way to do it without the shielding or with a more portable substitute.

I’ll save investigation on this for a later post (or maybe a comment from someone more knowledgeable!)

[1](https://sarahconstantin.substack.com/p/opm-meg-a-wearable-window-into-brain#footnote-anchor-1-141317639)One real\-world class of closed\-loop neuromodulation devices are the deep\-brain\-stimulation electrodes used to stop seizures as soon as they start. These devices need to *measure* brain electrical activity in real\-time, *detect* when it looks like a seizure is happening, and only then stimulate the brain to stop the seizure.

[2](https://sarahconstantin.substack.com/p/opm-meg-a-wearable-window-into-brain#footnote-anchor-2-141317639)Where do brain\-machine interfaces fall in this taxonomy? A brain\-machine interface that, say, allows a paralyzed person to control a computer UI or a robotic prosthesis with their mind, has the ability to “read” brain activity (usually via electrodes) but *not* the ability to “write” it. The output of the device is the commands guiding the computer/robot. Brain\-machine interfaces are *neurotechnology* but not *neuromodulation*, since they’re intended to read information out of the brain but not to (directly) modify the brain.

[3](https://sarahconstantin.substack.com/p/opm-meg-a-wearable-window-into-brain#footnote-anchor-3-141317639)A newer type of OPM, used by BrainBox, is based on helium instead. 

Badier, Jean\-Michel, et al. "Helium optically pumped magnetometers can detect epileptic abnormalities as well as SQUIDs as shown by intracerebral recordings." *Eneuro* 10\.12 (2023\).

[4](https://sarahconstantin.substack.com/p/opm-meg-a-wearable-window-into-brain#footnote-anchor-4-141317639)Knapkiewicz, Pawel. "Technological assessment of MEMS alkali vapor cells for atomic references." *Micromachines* 10\.1 (2018\): 25\.

[5](https://sarahconstantin.substack.com/p/opm-meg-a-wearable-window-into-brain#footnote-anchor-5-141317639)Bopp, D. G., V. M. Maurice, and J. E. Kitching. "Wafer\-level fabrication of alkali vapor cells using in\-situ atomic deposition." *Journal of Physics: Photonics* 3\.1 (2020\): 015002\.

[6](https://sarahconstantin.substack.com/p/opm-meg-a-wearable-window-into-brain#footnote-anchor-6-141317639)A magnetometer isn’t technically MEMS because it isn’t *mechanical* but MEMS fabs seem to be the place to go for the “garbage taxon” class of not\-quite\-just\-semiconductor microfabricated devices.

[7](https://sarahconstantin.substack.com/p/opm-meg-a-wearable-window-into-brain#footnote-anchor-7-141317639)as a medical device, MEG is pretty much *only* used for drug\-resistant epilepsy (especially selecting locations for surgery), and researchers are still hashing out the standard of care for where it’s appropriate. There are about 3\.4 million epileptics in the US, but maybe only thousands of cases where an MEG scan would currently be indicated?

[8](https://sarahconstantin.substack.com/p/opm-meg-a-wearable-window-into-brain#footnote-anchor-8-141317639)from DOD (defense), HHS (health), and NASA (space)

[9](https://sarahconstantin.substack.com/p/opm-meg-a-wearable-window-into-brain#footnote-anchor-9-141317639)A “yield of 80%” means that on a given wafer, 80% of the devices are good enough to use (and thus 20% are defective).

[10](https://sarahconstantin.substack.com/p/opm-meg-a-wearable-window-into-brain#footnote-anchor-10-141317639)Bennett, James S., et al. "Precision magnetometers for aerospace applications: A review." *Sensors* 21\.16 (2021\): 5568\.

[11](https://sarahconstantin.substack.com/p/opm-meg-a-wearable-window-into-brain#footnote-anchor-11-141317639)Bai, Xuanyao, et al. "Atomic magnetometers and their application in industry." *Frontiers in Physics* 11 (2023\): 1212368\.

[12](https://sarahconstantin.substack.com/p/opm-meg-a-wearable-window-into-brain#footnote-anchor-12-141317639)https://www.whoi.edu/what\-we\-do/explore/instruments/instruments\-sensors\-samplers/marine\-magnetometer/

[13](https://sarahconstantin.substack.com/p/opm-meg-a-wearable-window-into-brain#footnote-anchor-13-141317639)https://research.gatech.edu/vapor\-cells\-quantum\-sensors

[14](https://sarahconstantin.substack.com/p/opm-meg-a-wearable-window-into-brain#footnote-anchor-14-141317639)Gigahertz/terahertz imaging uses the electromagnetic spectrum between radio waves and visible light; it passes through objects, making it an alternative to X\-rays.

[15](https://sarahconstantin.substack.com/p/opm-meg-a-wearable-window-into-brain#footnote-anchor-15-141317639)https://thequantuminsider.com/2022/08/01/it\-may\-be\-time\-for\-real\-world\-applications\-using\-atomic\-clocks/