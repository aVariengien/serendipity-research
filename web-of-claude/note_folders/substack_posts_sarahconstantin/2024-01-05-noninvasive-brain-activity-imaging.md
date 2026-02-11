# Noninvasive Brain Activity Imaging

*Measuring and mapping brain activity without surgery or bulky machines*

Published: 2024-01-05
Source: https://sarahconstantin.substack.com/p/noninvasive-brain-activity-imaging

---

[![](https://substackcdn.com/image/fetch/$s_!X1Qr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3e964006-5bdf-46ad-bf15-9201cb541f8c_1920x1216.jpeg)](https://substackcdn.com/image/fetch/$s_!X1Qr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3e964006-5bdf-46ad-bf15-9201cb541f8c_1920x1216.jpeg)

Cortech Solutions’ wearable fNIRS device

So you want to see what the brain is doing? In real time?

Maybe you just want to learn how the brain works. Maybe you want to observe the difference between sick and healthy activity patterns.

Or, maybe you want to do neuromodulation of some kind (like [tFUS](https://sarahconstantin.substack.com/p/ultrasound-neuromodulation)!). That is, you want to intervene to change neural activity in some part of the human brain. In which case you’re going to want to *validate* that the intervention works, by checking whether the neural activity indeed changed in the way you intended. And for that you’ll need some kind of brain activity measurement.

The most common modalities for measuring brain activity kind of suck, for that purpose.

You can monitor neural spiking directly by sticking an electrode inside the brain. Unfortunately, this is risky. It involves brain surgery, and it kills brain cells. It’s unethical to do this to a human unless they’re seriously ill and the surgery can be expected to help significantly.

Branching out to non\-invasive techniques, one of the oldest[1](https://sarahconstantin.substack.com/p/noninvasive-brain-activity-imaging#footnote-1-140398172) is the electroencephalogram, or [EEG](https://en.wikipedia.org/wiki/Electroencephalography).

[![](https://substackcdn.com/image/fetch/$s_!svVX!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7d93f7f3-b01b-48a5-b3bd-4f814b7c771f_1500x1000.jpeg)](https://substackcdn.com/image/fetch/$s_!svVX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7d93f7f3-b01b-48a5-b3bd-4f814b7c771f_1500x1000.jpeg)

An EEG setup: electrodes placed over the scalp to record electrical signals.

Measuring electric currents on the surface of the scalp can pick up brain waves. This is excellent for diagnosing epilepsy, for identifying whether the subject is awake or asleep (and to confirm than an anaesthetized patient is unconscious), and other basic neurological assessments. And some researchers think you can get a lot more info out of EEG data with machine learning. (More on that in a later post).

But EEG is *not* good at localizing brain activity to particular regions. “Left frontal lobe” is more or less the resolution scale to expect. So it’s a very noisy assessment of “did my neuromodulation of *this particular sub\-cubic\-centimeter brain region* change neural activity in that target region?”

If you want better spatial localization of brain activity, there’s functional MRI, or [fMRI.](https://en.wikipedia.org/wiki/Functional_magnetic_resonance_imaging)

[![](https://substackcdn.com/image/fetch/$s_!To_Y!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8a17c56c-97ab-4858-b796-74bdbe2a3662_711x474.png)](https://substackcdn.com/image/fetch/$s_!To_Y!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8a17c56c-97ab-4858-b796-74bdbe2a3662_711x474.png)

an MRI machine. The subject lies on the bench with their head in the ring.

fMRI works on the principle that oxygen\-rich blood has different magnetic properties than oxygen\-poor blood, and that this can show up as a signal to the MRI.

When neurons fire, they use glucose to power that activity, and they must get more glucose supplied by blood flow. So blood flow in a region tends to rise a few seconds after that region is especially neurally active.

fMRI can therefore image brain activity, on a spatial scale of a few millimeters and a temporal scale of a few seconds.

One weakness of fMRI is that, when people are more experienced at a task, they become more “[efficient](https://en.wikipedia.org/wiki/Functional_magnetic_resonance_imaging#CITEREFHuettelSongMcCarthy2009)” and use less blood flow to the active regions to get the same performance. So it may not pick up brain activity from regions that are *crucial* to some task but very *efficient* at doing it.

But the more glaring weakness is simply that MRIs are so bulky and they immobilize the subject. There are limited activities a person can do with their head in an MRI machine. We can’t use it to monitor brain activity during exercise. We can’t use it to monitor people while they’re making eye contact with another human. We can’t even use it medically at a patient’s bedside — you need a special room and specialized MRI technicians.

So, *can we do better*?

### fNIRS: Infrared Imaging

Functional near\-infrared spectroscopy, or [fNIRS](https://en.wikipedia.org/wiki/Functional_near-infrared_spectroscopy), uses the same basic signal as fMRI — oxygenated blood flow.

But instead of detecting oxygenated blood inside the body by its *magnetic* properties, we can detect it by its *optical* properties.

Oxygenated blood is, quite simply, *redder* than non\-oxygenated blood. You can see it with your naked eye. In physical terms, they have different *absorption spectra*.

[![](https://substackcdn.com/image/fetch/$s_!puje!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb5db2b77-7c80-4e0a-a383-45225032679e_1920x1920.png)](https://substackcdn.com/image/fetch/$s_!puje!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb5db2b77-7c80-4e0a-a383-45225032679e_1920x1920.png)

The red line (oxygenated hemoglobin) absorbs less short\-wavelength light, but absorbs *more* long\-wavelength light, over 800 nm. The visible light spectrum is about 400\-700 nm, so 800\+ nm is infrared.

In other words, oxygenated blood is a bright red in the visible spectrum while deoxygenated blood is duller and darker — but in the infrared, deoxygenated blood *glows* and oxygenated blood is dimmer.

Detecting blood oxygenation through spectroscopy is nothing new — that’s how a pulse oximeter works.

[![](https://substackcdn.com/image/fetch/$s_!YzKb!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8244b9fc-cca8-4317-9563-71516192a54d_1200x800.jpeg)](https://substackcdn.com/image/fetch/$s_!YzKb!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8244b9fc-cca8-4317-9563-71516192a54d_1200x800.jpeg)

You can get this at the drugstore.

It literally just shines light through your finger and measures its absorption at two wavelengths from photodetectors on the other side, to tell how much oxygenated vs. deoxygenated blood is in your finger.

An fNIRS setup is similar in principle, but instead of one sensor for the finger, it uses many infrared light sources and photodetectors placed around the head.

[![](https://substackcdn.com/image/fetch/$s_!34Et!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F689c95d2-3811-4747-852e-f6cda4efcd35_426x454.png)](https://substackcdn.com/image/fetch/$s_!34Et!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F689c95d2-3811-4747-852e-f6cda4efcd35_426x454.png)

From the open\-source fNIRS organization OpenfNIRS

The first fNIRS measurements of brain activity date back to the early 1990s.[2](https://sarahconstantin.substack.com/p/noninvasive-brain-activity-imaging#footnote-2-140398172)

It was observed that fNIRS measurements of blood oxygenation correlate well with fMRI\-measured BOLD signals of blood oxygenation, and that both track well with expected neural function (e.g. a visual stimulus increases blood\-oxygenation activity in the occipital cortex.)

The trouble with fNIRS, however, is that it doesn’t penetrate deep into the brain. Just as you need a finger or an earlobe for pulse oximetry (and not, say, a leg), you can’t get an infrared blood flow signal from more than about 1\.5\-2 cm into the brain.

That’s fine for measuring activity in the cerebral cortex, but it *won’t* work for any of the deep structures I expect to be most interesting for neurostimulation.

Either in a disease\-treatment context ([Parkinson’s disease](https://en.wikipedia.org/wiki/Parkinson%27s_disease) is one of the best\-validated use cases for brain stimulation as a therapy, and you have to implant electrodes deep into the basal ganglia for that) or in a [neuroenhancement](https://sarahconstantin.substack.com/p/why-should-neuroenhancement-be-possible) context (where I think there’s a lot of potential for improving mood, habits, and motivation by targeting the limbic system) the really exciting stuff is deep inside the brain where you’ll never pick up an infrared signal.

### fUS: Functional Ultrasound

Ok, well what about ultrasound?

Ultrafast Doppler ultrasound of the brain can measure blood flow. In this case it’s not the oxygenation of the blood but its *motion* that gets picked up. This can be used to detect brain activity[3](https://sarahconstantin.substack.com/p/noninvasive-brain-activity-imaging#footnote-3-140398172) at comparable resolution to fMRI. And unlike infrared, ultrasound can penetrate deep enough to image the entire brain.

The downside is that fUS imaging isn’t really *transcranial* in humans yet. It’s been used during brain surgery, or in newborns through the [fontanelle](https://en.wikipedia.org/wiki/Fontanelle), but it hasn’t been used yet to image through the skull.

[![](https://substackcdn.com/image/fetch/$s_!E6cK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7588db13-eacd-4fea-821b-fb55ec51e79b_1280x713.jpeg)](https://substackcdn.com/image/fetch/$s_!E6cK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7588db13-eacd-4fea-821b-fb55ec51e79b_1280x713.jpeg)

You can use ultrasound to watch brain activity….but only in babies.

That’s a bummer, for those of us who are neither babies nor undergoing brain surgery.

Can we do better?

Well, there are some directions of research in animals.

If you inject a contrast agent like microbubbles into a rat, you can get functional ultrasound imaging through the skull.[4](https://sarahconstantin.substack.com/p/noninvasive-brain-activity-imaging#footnote-4-140398172)

Microbubbles are apparently pretty safe — they’ve been used as a contrast agent for heart ultrasounds since the 1990s — but they do occasionally seem to cause serious adverse events in patients who have an allergic reaction.[5](https://sarahconstantin.substack.com/p/noninvasive-brain-activity-imaging#footnote-5-140398172)

At any rate, ultrasound imaging keeps getting better (and smaller!) thanks to [semiconductor manufacturing innovations](https://sarahconstantin.substack.com/p/the-enchippening-of-medical-imaging), so maybe truly noninvasive functional ultrasound will be ready for use on humans in the near future.

### Functional Photoacoustic Tomography (PACT)

Another experimental imaging modality is photoacoustic tomography imaging, or PACT.

This method uses lasers to irradiate tissue, creating acoustic waves (the [photoacoustic effect](https://en.wikipedia.org/wiki/Photoacoustic_effect)) which are scattered differently by different tissue types and can be detected by ultrasound transducers.

PACT is great at high\-resolution imaging of blood vessels and blood flow, and it can penetrate deep into the brain. A 2022 paper used PACT on patients undergoing brain surgery to observe fMRI\-like results — when the patient was asked to do various cognitive tasks, the expected regions of the brain showed more blood flow with PACT.

[![](https://substackcdn.com/image/fetch/$s_!vwEM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F58a479ad-5b9e-49ae-8942-4be09e4fa2b9_1833x652.png)](https://substackcdn.com/image/fetch/$s_!vwEM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F58a479ad-5b9e-49ae-8942-4be09e4fa2b9_1833x652.png)

Yeah this ain’t portable.

Is this any more practical than an MRI machine though? Those are some heckin’ big lasers…

On the other hand, this is an early prototype, and an MRI machine is $6M and weighs over 20 tons. PACT probably has advantages over MRI for some applications even now, and there’s a lot of room for improvement as designs iterate.

### Portable Magnetoencephalography (MEG)

Magnetoencephalography measures the magnetic fields produced by brain electrical activity. Traditionally, like an MRI, it uses a large, bulky stationary device:

[![](https://substackcdn.com/image/fetch/$s_!pse3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2e8b5055-5059-49ed-85e6-8c1fca891da6_435x655.jpeg)](https://substackcdn.com/image/fetch/$s_!pse3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2e8b5055-5059-49ed-85e6-8c1fca891da6_435x655.jpeg)

MEGs are big

and it seems to be able to detect deep as well as surface brain activity.[6](https://sarahconstantin.substack.com/p/noninvasive-brain-activity-imaging#footnote-6-140398172) But unlike an fMRI, a MEG measures neuronal activity directly rather than indirectly via blood flow, so its temporal resolution is faster.

But recently, portable MEGs have been developed using optically pumped magnetometers.   
  
Optically pumped magnetometers, or OPMs, are miniaturized devices that sensitively detect magnetic fields using quantum\-mechanical effects on vaporized rubidium atoms.[7](https://sarahconstantin.substack.com/p/noninvasive-brain-activity-imaging#footnote-7-140398172)

[![](https://substackcdn.com/image/fetch/$s_!HaIC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5d6b3ae-e313-4d5d-bfe7-da6512dda402_765x276.jpeg)](https://substackcdn.com/image/fetch/$s_!HaIC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5d6b3ae-e313-4d5d-bfe7-da6512dda402_765x276.jpeg)

OPMs are handy because they allow you to measure tiny magnetic effects without superconductors (or the cryogenic temperatures superconductors require). And they can be microfabricated with a lot of the techniques common to the rest of the semiconductor industry.[8](https://sarahconstantin.substack.com/p/noninvasive-brain-activity-imaging#footnote-8-140398172)

In fact, OPM\-MEG headsets for functional neuroimaging are commercially available today, from companies like [BrainBox](https://brainbox-neuro.com/techniques/meg) and [Cerca Magnetics](https://www.cercamagnetics.com/).

[![](https://substackcdn.com/image/fetch/$s_!wwk_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fccef2cf6-5c38-4a26-87e6-ce1b4374004f_1200x1200.png)](https://substackcdn.com/image/fetch/$s_!wwk_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fccef2cf6-5c38-4a26-87e6-ce1b4374004f_1200x1200.png)

That’s a lotta wires…but it ain’t an MRI machine!

And it works — you can, for instance, use OPM\-MEG to detect a change in hippocampal activation in human subjects during a hippocampal\-intensive task (imagining scene imagery). fMRI recordings have routinely picked up an increase in hippocampal blood oxygenation during that same task.[9](https://sarahconstantin.substack.com/p/noninvasive-brain-activity-imaging#footnote-9-140398172)

You can also detect the cerebellum’s neural response to a puff of air to the eye with a MEG helmet[10](https://sarahconstantin.substack.com/p/noninvasive-brain-activity-imaging#footnote-10-140398172) — this is the kind of very fast (tens of milliseconds) phenomenon you’d never pick up with an fMRI.[11](https://sarahconstantin.substack.com/p/noninvasive-brain-activity-imaging#footnote-11-140398172)

OPM\-MEG is still pretty experimental and has a bunch of kinks to work out, like magnetic shielding. It’s mostly used for epilepsy, where accurately timed localization of seizures within the brain is essential.

But it does seem like it’s a potentially valid modality for measuring the effect of neuromodulation in healthy subjects.

* decent spatial resolution (2\-3 mm)
* excellent temporal resolution (milliseconds)
* noninvasive
* wearable and portable 

	+ it needs to be plugged in, but can be used by a person sitting in a chair and moving normally
* can detect deep brain activity

### Conclusions

So far, it looks like:

* fNIRS is convenient and affordable but it can’t measure deep brain activity
* functional ultrasound isn’t really transcranial yet
* functional PACT isn’t really portable *or* transcranial so far, and I’m not sure laser stimulation of the brain wouldn’t *itself* do something to the brain!
* OPM\-MEG seems tentatively the best of the bunch, but it’s *very* new and there seem to be some remaining technical challenges that I don’t yet have a great handle on, and it might be pricey.

In later posts I might look at other imaging modalities, and also come back to EEG in more detail to figure out exactly how much info (and spatial localization) you can get out of the oldest and best\-studied brain activity measurement method.

[1](https://sarahconstantin.substack.com/p/noninvasive-brain-activity-imaging#footnote-anchor-1-140398172)The first human EEG was recorded in 1924\.

[2](https://sarahconstantin.substack.com/p/noninvasive-brain-activity-imaging#footnote-anchor-2-140398172)Pinti, Paola, et al. "The present and future use of functional near‐infrared spectroscopy (fNIRS) for cognitive neuroscience." *Annals of the New York Academy of Sciences* 1464\.1 (2020\): 5\-29\.

[3](https://sarahconstantin.substack.com/p/noninvasive-brain-activity-imaging#footnote-anchor-3-140398172)Deffieux, Thomas, Charlie Demené, and Mickael Tanter. "Functional ultrasound imaging: A new imaging modality for neuroscience." *Neuroscience* 474 (2021\): 110\-121\.

[4](https://sarahconstantin.substack.com/p/noninvasive-brain-activity-imaging#footnote-anchor-4-140398172)Errico, Claudia, et al. "Transcranial functional ultrasound imaging of the brain using microbubble\-enhanced ultrasensitive Doppler." *NeuroImage* 124 (2016\): 752\-761\.

[5](https://sarahconstantin.substack.com/p/noninvasive-brain-activity-imaging#footnote-anchor-5-140398172)Khumri, Taiyeb M., and Michael L. Main. "Safety and risk\-benefit profile of microbubble contrast agents in echocardiography." *Asia Pacif Cardiol* 2\.1 (2008\): 47\-49\.

[6](https://sarahconstantin.substack.com/p/noninvasive-brain-activity-imaging#footnote-anchor-6-140398172)Bénar, Christian\-George, et al. "Detection and localization of deep sources in magnetoencephalography: A review." *Current Opinion in Biomedical Engineering* 18 (2021\): 100285\.

[7](https://sarahconstantin.substack.com/p/noninvasive-brain-activity-imaging#footnote-anchor-7-140398172)Brookes, Matthew J., et al. "Magnetoencephalography with optically pumped magnetometers (OPM\-MEG): the next generation of functional neuroimaging." *Trends in Neurosciences* (2022\).

[8](https://sarahconstantin.substack.com/p/noninvasive-brain-activity-imaging#footnote-anchor-8-140398172)Alem, Orang, et al. "Magnetic field imaging with microfabricated optically\-pumped magnetometers." *Optics express* 25\.7 (2017\): 7849\-7858\.

[9](https://sarahconstantin.substack.com/p/noninvasive-brain-activity-imaging#footnote-anchor-9-140398172)Barry, Daniel N., et al. "Imaging the human hippocampus with optically\-pumped magnetoencephalography." *Neuroimage* 203 (2019\): 116192\.

[10](https://sarahconstantin.substack.com/p/noninvasive-brain-activity-imaging#footnote-anchor-10-140398172)Lin, Chin‐Hsuan, et al. "Using optically pumped magnetometers to measure magnetoencephalographic signals in the human cerebellum." *The Journal of physiology* 597\.16 (2019\): 4309\-4324\.

[11](https://sarahconstantin.substack.com/p/noninvasive-brain-activity-imaging#footnote-anchor-11-140398172)In a previous [post](https://sarahconstantin.substack.com/p/what-does-the-cerebellum-do-anyway) I have more info about the cerebellum and the eyeblink reaction.