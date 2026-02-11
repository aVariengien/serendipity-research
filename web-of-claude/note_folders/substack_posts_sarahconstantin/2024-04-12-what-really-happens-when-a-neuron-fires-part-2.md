# What Really Happens When A Neuron Fires? (Part 2)

*Neurotransmission!*

Published: 2024-04-12
Source: https://sarahconstantin.substack.com/p/what-really-happens-when-a-neuron-647

---

[![](https://substackcdn.com/image/fetch/$s_!vqPv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F662cb808-0bb2-4b6c-a85e-af4fc81cf2d3_850x386.png)](https://substackcdn.com/image/fetch/$s_!vqPv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F662cb808-0bb2-4b6c-a85e-af4fc81cf2d3_850x386.png)

Neurons connect at synapses. You’ve seen this picture before.

Ok, so in our [last post](https://sarahconstantin.substack.com/p/what-really-happens-when-a-neuron) we learned about what it even means, physically, for a neuron to “fire” and how externally applied electric current affects that.

Now let’s look at what happens to nearby neurons after a neuron fires.

#### Synaptic Transmission

The high school biology version that I’ve vaguely been aware of as “how neurotransmission works” goes something like this:

“When a neuron fires, neurotransmitters are released at the axon terminals, flow across the synapses, and hit the dendrites of downstream neurons. This has either an excitatory effect — making the post\-synaptic neuron fire more — or an inhibitory effect — making the post\-synaptic neuron fire less.”

Ok, but: what do we mean by “less” and “more”?

More frequently? More strongly? For how long?

Let’s zoom in a little bit and find out.

When a neurotransmitter binds to a receptor at the post\-synaptic neuron, that can *directly affect the electrical potential in that neuron*.

[![](https://substackcdn.com/image/fetch/$s_!LI5D!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe039e692-6733-4fb6-b4cc-ba0b17fc7ad4_521x416.jpeg)](https://substackcdn.com/image/fetch/$s_!LI5D!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe039e692-6733-4fb6-b4cc-ba0b17fc7ad4_521x416.jpeg)

Each vesicle (bubble) containing neurotransmitters contributes incrementally to the postsynaptic potential. The overall postsynaptic potential is a *sum* of the effects of all the incoming excitatory and inhibitory neurotransmitters from all the dendrites; if they add up to enough depolarization to cause the postsynaptic neuron to fire, it does; otherwise, it doesn’t.

This whole process takes only about a millisecond.[1](https://sarahconstantin.substack.com/p/what-really-happens-when-a-neuron-647#footnote-1-143532620)

In other words, the “excitation” or “inhibition” is relative to individual spikes — it’s not about *frequency* of firing, it’s about increasing or decreasing the likelihood of the *next spike*.

How do neurotransmitters affect postsynaptic potential in the first place?

Well, when a neurotransmitter binds a receptor, it opens or closes an ion channel, affecting the flow of charged ions into the neuron, and thus the voltage differential between the inside and outside of the cell.

For example:

* the [GABA\-A receptor](https://en.wikipedia.org/wiki/GABAA_receptor), when bound by the neurotransmitter GABA, lets negatively charged chlorine ions into the neuron. This makes the inside of the neuron *more negative*, i.e. hyperpolarized, so it’s harder for the neuron to fire. This is an *inhibitory receptor*.
* The [NMDA recepto](https://en.wikipedia.org/wiki/GABAA_receptor)r, when bound by the neurotransmitter glutamate, allows positively charged calcium ions to enter the cell, making it *less negative*, i.e. *depolarized*, so it’s easier for the neuron to fire. This is an *excitatory receptor*.

#### Synaptic Plasticity

The basic, high\-school\-level story about synaptic plasticity is basically as follows:  
  
 “The strength of synapses can get stronger or weaker over time, which is how learning and memory work. “Neurons that fire together wire together”, aka when two excitatory\-synapse\-connected neurons often fire at the same time, the excitatory effect gets stronger.”

This phenomenon is called Long\-Term Potentiation and it is very real. It goes back to a paper in 1973 where Terje Lømo and Tim Bliss found that applying a 100 Hz stimulus for one second to the presynaptic neuron led to a dramatic and long\-lasting increase in post\-synaptic response. A later review article said “There is not a single controversial finding in this paper, which is a very remarkable thing in this field.”[2](https://sarahconstantin.substack.com/p/what-really-happens-when-a-neuron-647#footnote-2-143532620)

We now know that the mechanism of LTP involves:

* physical growth of the post\-synaptic dendrite spine
* increased numbers of receptors on the post\-synaptic spine
* greater conductance of receptors on the post\-synaptic spine, so they let more ions through.

This means that each neurotransmitter molecule has a greater chance of hitting a receptor, and has a bigger effect on the postsynaptic neuron’s membrane potential when it does.

Can you have long\-term potentiation of an inhibitory synapse? Yes, that’s a thing too.[3](https://sarahconstantin.substack.com/p/what-really-happens-when-a-neuron-647#footnote-3-143532620) After stimulating the presynaptic neuron, the post\-synaptic neuron has a bigger dip in its voltage (more hyperpolarized), a phenomenon which can last for hours.

There’s also a phenomenon of *long\-term depression* (LTD) in which a synapse gets *weaker* (less excitatory or less inhibitory).

LTD can happen as a result of:

* *prolonged, low\-frequency stimulation*, such as 900 pulses at 1 Hz at the presynaptic neuron
* the post\-synaptic neuron firing *before* the pre\-synaptic neuron
* nearby synapses undergoing LTP
* activation of certain receptors

LTD works like LTP in reverse — spines shrink, receptors get removed from the surface of the post\-synaptic spine, and receptors get modified to let fewer ions through.

#### Upshots: Neuromodulation

A neuromodulation technique can act directly on its target neurons, directly causing them to fire or stopping them from firing; or it can have a wide variety of *indirect* effects, usually with longer lag times, longer\-lasting effects, and more complex effects.

If it affects synaptic plasticity, increasing or decreasing LTP or LTD, it might have divergent effects on aggregate neural firing rates depending on whether the stimulus to the target neurons is the kind of high\-frequency stimulation that causes LTP, or the kinds of stimulation (such as low\-frequency) that causes LTD.

If your neuromodulation technique creates effects lasting minutes or more after the intervention stops, there’s probably *something* going on beyond direct effects on the target neuron’s electrical potential, and it’s worth looking into whether there’s a synaptic plasticity mechanism. (But, as I understand, there’s no exhaustivelist of possible mechanisms, and unenumerably many conceivable indirect effects that affect neural firing one way or another.)

The nice thing about a synaptic plasticity effect is that you *don’t need to keep applying the intervention all the time to get the effect*, which is great for saving power and/or minimizing the damaging effects of delivering energy to tissue in one way or another. We may actually want to seek out neuromodulatory interventions that work by affecting synaptic plasticity rather than by directly causing or stopping neural spiking.

All these indirect effects make it *really* hard to theoretically predict what’s going to happen, and in what context. This is why you need to consider the effect of a neuromodulatory intervention as *stimulus\-dependent*, i.e. it may depend on what other stimuli the target neurons are receiving around the same time as the neuromodulation. In a live animal that may mean it’s dependent on the activity the animal is engaging in; in a tissue sample you can measure and control the stimulus somewhat better.

Figuring out “what, exactly, is this intervention doing to the target neurons” is really hard, especially in live animals where the finest\-grained measurements we have are implanted electrodes that measure average spiking rates in large clumps of neurons. But it helps to have a little context on the range of things that *could* be happening and the relevant timescales.

[1](https://sarahconstantin.substack.com/p/what-really-happens-when-a-neuron-647#footnote-anchor-1-143532620)Burke, ROBERT E. "Composite nature of the monosynaptic excitatory postsynaptic potential." *Journal of Neurophysiology* 30\.5 (1967\): 1114\-1137\.

[2](https://sarahconstantin.substack.com/p/what-really-happens-when-a-neuron-647#footnote-anchor-2-143532620)Nicoll, Roger A. "A brief history of long\-term potentiation." *neuron* 93\.2 (2017\): 281\-290\.

[3](https://sarahconstantin.substack.com/p/what-really-happens-when-a-neuron-647#footnote-anchor-3-143532620)Korn, Henri, Yoichi Oda, and Donald S. Faber. "Long\-term potentiation of inhibitory circuits and synapses in the central nervous system." *Proceedings of the National Academy of Sciences* 89\.1 (1992\): 440\-443\.