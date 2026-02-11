# How Ultrasound Neuromodulation Works

*Physical parameters, mechanisms, and prospects for miniaturization*

Published: 2023-10-12
Source: https://sarahconstantin.substack.com/p/how-ultrasound-neuromodulation-works

---

[![](https://substackcdn.com/image/fetch/$s_!-RPO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffc047727-b64c-4647-9698-2862f14ff78d_1000x667.png)](https://substackcdn.com/image/fetch/$s_!-RPO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffc047727-b64c-4647-9698-2862f14ff78d_1000x667.png)

### Definitions and Measurements

Low\-intensity transcranial focused ultrasound (abbreviated tFUS or LIFU) applies weak ultrasound fields to brain tissue from outside the head.

Unlike high\-intensity ultrasound, which is intended to destroy tissue (like tumors), low\-intensity ultrasound applies a much gentler force to tissue.

The *intensity* of ultrasound is a measure of power, denominated in watts per centimeter squared, W/cm^2\.

Typical peak intensities in human experiments range between 1\-30 W/cm^2; this is well below the FDA\-given upper bounds for safe diagnostic ultrasound for imaging inside the head, a maximum spatial peak pulse average of 190 W/cm^2\.

The ultrasound in tFUS is, of course, a sound wave, applied in repetitive pulses. It looks like this:

[![](https://substackcdn.com/image/fetch/$s_!n3z-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fca7aaa65-29f1-46aa-b2cc-223c7c8dc2df_680x368.png)](https://substackcdn.com/image/fetch/$s_!n3z-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fca7aaa65-29f1-46aa-b2cc-223c7c8dc2df_680x368.png)

This wave has multiple associated frequencies, which need to be distinguished:

* The *acoustic frequency* is the frequency of the smallest waves; it is typically 0\.2 MHz to 5 MHz. This is the “pitch” of the sound.
* The *pulse repetition frequency* is the number of pulse periods per second, where a pulse period is measured from the beginning of one pulse to the beginning of the next. This can range from 1 Hz to 3000 Hz.
* The *duty cycle* is the percent of each pulse period where the pulse is on. 

	+ So, for instance, if pulses last 1 ms each, with a rest period of 1 ms between each pulse, then the duty cycle would be 50% — half on, half off.

Finally, tFUS can be *continuous* or *intermittent*  — it can either be applied in short bursts several seconds apart (each burst consisting of multiple pulses), or it can be applied continuously for minutes at a time (again, still consisting of a train of pulses).

These distinctions are important to keep in mind, because we’ll be reviewing experimental evidence in later posts and trying to make sense of how different ultrasound settings have been reported to have different effects on the brain.

### Focusing tFUS in a Small Area

Recall that ultrasound is produced by a [transducer](https://sarahconstantin.substack.com/p/the-world-of-mems), typically a piezoelectric plate that vibrates in the presence of an electric current.

Each transducer produces a beam of ultrasound. Two or more transducers whose beams cross can produce a tighter focal point where they intersect.

The cross\-section of a single ultrasound beam can be focused to a region of only a few millimeters in diameter; with two intersecting beams the lateral diameter can be reduced to less than half a millimeter.[1](https://sarahconstantin.substack.com/p/how-ultrasound-neuromodulation-works#footnote-1-137906141) The *depth* of the focal area, along the path of the beam, can be longer, such as 20 mm.[2](https://sarahconstantin.substack.com/p/how-ultrasound-neuromodulation-works#footnote-2-137906141)

[![](https://substackcdn.com/image/fetch/$s_!3hAA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fec7b38a8-6ee3-490f-9378-1adff8a9fec7_664x170.jpeg)](https://substackcdn.com/image/fetch/$s_!3hAA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fec7b38a8-6ee3-490f-9378-1adff8a9fec7_664x170.jpeg)

This few\-millimeter precision of tFUS is comparable to the precision of implanted brain electrodes used for deep brain stimulation, and far superior to the precision of other noninvasive neuromodulation techniques like rTMS, which focus on areas of the surface of the brain easily tens of millimeters across.

[![](https://substackcdn.com/image/fetch/$s_!GMFY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb54e5d74-1833-48b7-b0b9-83ab98cc7806_2500x1690.png)](https://substackcdn.com/image/fetch/$s_!GMFY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb54e5d74-1833-48b7-b0b9-83ab98cc7806_2500x1690.png)

This precision is adequate to target specific brain structures — the amygdala is about a centimeter in diameter, the nucleus accumbens (involved in reward and motivation) is about 10 mm in diameter, the subthalamic nucleus (involved in motor control) is about 7 mm in diameter, and so on.

Individual neurons, however, are too small to target with existing ultrasound tech — they range from 4\-100 microns in diameter.

### Mechanism — Why Does It Work?

Ultrasound’s effects on neurons are driven by multiple mechanisms.

One possible mechanism is thermal heating. Warming can inhibit neuron firing, either when produced by ultrasound or by other mechanisms like lasers, electrical current, or thermocouples.[3](https://sarahconstantin.substack.com/p/how-ultrasound-neuromodulation-works#footnote-3-137906141)[4](https://sarahconstantin.substack.com/p/how-ultrasound-neuromodulation-works#footnote-4-137906141)

Independently, ultrasound can also affect neurons through mechanical force, even in the absence of nontrivial heating. Mechanical force may alter neurons’ membrane permeability, making them more excitable.

In fact, an in vitro experiment demonstrated that ultrasound continues to affect neuron spiking through affecting ion channels even when it’s far too slow and sparse a pulse pattern to heat the neurons.

When ultrasound was applied to neurons with intensity too low to create more than 0\.01 degree of heating (acoustic frequency 0\.3 MHz, 2\.5% duty cycle, pulse repetition frequency 0\.05 Hz, 15 W/cm^2\) neuron spiking was activated, with an amplitude proportional to the intensity of the ultrasound stimulation.  Ultrasound allowed extracellular calcium ions to enter the neurons, which was the proximate cause of the spiking. In calcium\-free medium, where the calcium\-ion mechanism couldn’t apply, ultrasound didn’t stimulate neuron firing.[5](https://sarahconstantin.substack.com/p/how-ultrasound-neuromodulation-works#footnote-5-137906141)

Notice that these two effects work in opposite directions; the heat effect of ultrasound *decreases* neurons’ propensity to fire, while the mechanical/calcium\-channel effect *increases* their propensity to fire.

Accordingly, across animal and human experiments, we see more neural\-inhibiting effects from ultrasound stimulation protocols that apply continuous and/or high\-duty\-cycle stimulation (lots of cumulative energy applied to the tissue), as you’d expect if keeping the ultrasound going continuously for a while allows heat to accumulate. And, conversely, we see more neural\-activating effects from experiments that apply transient and/or low\-duty\-cycle stimulation (little cumulative energy applied to the tissue) as you’d expect if such protocols produced little heat and allowed the effect of mechanical stimulation to dominate.

Is tFUS a truly general neuromodulation technique, able to “turn up” or “turn down” neural firing anywhere in the brain?

We don’t know for sure, as we don’t actually have systematic experiments covering a sufficiently wide range of brain regions and stimulation protocols. It certainly seems possible. And my current guess is, from the data points we do have (which will be covered in a later post) that whether you get an excitatory or inhibitory effect on neurons depends on the ultrasound protocol (frequency, intensity, duty cycle, etc) rather than the brain region.

### Miniaturization

The old\-fashioned way to apply ultrasound to the brain is to have a big handheld transducer several centimeters in diameter, attached via wires to a waveform generator (basically a box that computes the appropriate wave signal to transmit), affixed to the desired position on the patient’s head. The setup in human experiments typically looks like this:

[![](https://substackcdn.com/image/fetch/$s_!2_0q!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbe841f55-148e-47a1-bb65-2f5b2ab0cf2d_1200x630.jpeg)](https://substackcdn.com/image/fetch/$s_!2_0q!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbe841f55-148e-47a1-bb65-2f5b2ab0cf2d_1200x630.jpeg)

Obviously, that’s not a wearable device.

At least not in the same way a FitBit is a wearable device. The ultrasound rig is attached to a big machine on a cart that plugs into a wall.

Is it technically feasible to miniaturize it?

For one thing, these bulky waveform generators might be the old\-fashioned analog kind. Digital waveform generators can be much smaller; the problem is that these will produce smaller voltages, which result in lower intensities and pressures on the resulting ultrasound.

Some researchers are working on developing on\-chip ultrasound arrays for neurostimulation, usually for use in rodent experiments. For instance, a 16\-element ultrasound array, 16\.7mm x 7mm x 2mm, with a minaturized driver board, is able to produce megahertz frequencies and 10 W/cm^2 peak intensities, up to 12 mm away from the transducers.[6](https://sarahconstantin.substack.com/p/how-ultrasound-neuromodulation-works#footnote-6-137906141) By controlling the phase delay programmatically, the same device can focus ultrasound in different directions without requiring physical repositioning.

A 12 mm focal depth is fine for a rat, but a device for reaching brain structures in humans will need to go deeper, which means you’ll need to generate higher voltages to hit comparable intensities and frequencies. My back\-of\-the\-envelope estimates are in the neighborhood of 30\-60 volts (at the transducer), which sounds alarmingly high, but my physics is very rusty and I welcome correction here.

Whether you could actually produce a battery\-powered, wholly wearable tFUS device for humans capable of producing the full range of ultrasound stimulation intensities and frequencies seen in human tFUS experiments, throughout the whole brain volume, is, I think, still an open question.

My top questions would be about voltage and power supply — most digital waveform generators only produce a few volts, as do portable batteries, so you’d need to get excellent sensitivity from your ultrasound transducers (i.e. a lot of pressure from a small voltage) or use electronic tricks to increase the voltage with amplifiers, capacitors, or other devices. Of course, you’d also be concerned about safety and heat dissipation with a high\-voltage wearable device. Once again, that’s an issue to be addressed by people who know more about electronics than me.

A truly wearable tFUS device seems like a bit of an R\&D project. But as far as I can see there are no obvious physical impossibilities here.

[1](https://sarahconstantin.substack.com/p/how-ultrasound-neuromodulation-works#footnote-anchor-1-137906141)Kim, Seongyeon, et al. "Transcranial focused ultrasound stimulation with high spatial resolution." *Brain Stimulation* 14\.2 (2021\): 290\-300\.

[2](https://sarahconstantin.substack.com/p/how-ultrasound-neuromodulation-works#footnote-anchor-2-137906141)Legon, Wynn, et al. "Neuromodulation with single‐element transcranial focused ultrasound in human thalamus." *Human brain mapping* 39\.5 (2018\): 1995\-2006\.

[3](https://sarahconstantin.substack.com/p/how-ultrasound-neuromodulation-works#footnote-anchor-3-137906141)Van Hook, Matthew J. "Temperature effects on synaptic transmission and neuronal function in the visual thalamus." *PloS one* 15\.4 (2020\): e0232451\.

[4](https://sarahconstantin.substack.com/p/how-ultrasound-neuromodulation-works#footnote-anchor-4-137906141)Kim, TaeKen, et al. "Thermal effects on neurons during stimulation of the brain." *Journal of neural engineering* 19\.5 (2022\): 056029\.

[5](https://sarahconstantin.substack.com/p/how-ultrasound-neuromodulation-works#footnote-anchor-5-137906141)Yoo, Sangjin, et al. "Focused ultrasound excites cortical neurons via mechanosensitive calcium accumulation and ion channel amplification." *Nature communications* 13\.1 (2022\): 493\.

[6](https://sarahconstantin.substack.com/p/how-ultrasound-neuromodulation-works#footnote-anchor-6-137906141)Ilham, Sheikh Jawad, Zeinab Kashani, and Mehdi Kiani. "Design and optimization of ultrasound phased arrays for large\-scale ultrasound neuromodulation." *IEEE transactions on biomedical circuits and systems* 15\.6 (2021\): 1454\-1466\.