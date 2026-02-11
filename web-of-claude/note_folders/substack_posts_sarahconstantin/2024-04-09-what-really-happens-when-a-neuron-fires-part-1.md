# What Really Happens When A Neuron Fires? (Part 1)

*Back To Basics*

Published: 2024-04-09
Source: https://sarahconstantin.substack.com/p/what-really-happens-when-a-neuron

---

[![](https://substackcdn.com/image/fetch/$s_!ndzj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F57d82a72-efaa-4466-b787-973007af024e_2500x1612.png)](https://substackcdn.com/image/fetch/$s_!ndzj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F57d82a72-efaa-4466-b787-973007af024e_2500x1612.png)

You’ve seen this picture before.

So, everybody knows what a neuron is, right? It’s a cell in the nervous system, it “fires” by transmitting something electricity\-like along the length of the axon, and that sends neurotransmitters across synapses to the next neurons, thus modulating the activity of those downstream neurons.

So far, so good. This is the high school biology picture. What’s so mysterious here?

Well, I just glossed over some very vague things.

* The axon transmits “something electricity\-ish”. Well, what is it *exactly*?
* When one neuron fires, it “modulates” (weasel word alert) the activity of downstream neurons. Well, what does it do to them *exactly*?

We care, once again, from the perspective of neurotech, because if we want to know how different technologies will alter neuronal activity, we need to know how that activity physically works.

As far as this post goes, I’m mostly teaching myself — I’m sticking to what seems to be uncontroversial consensus stuff, probably nothing new for any of you who are actual neuroscientists.

### The Action Potential

The electricity\-ish thing that travels along a neuron is an *action potential*.

Normally, a neuron, like other cells, has a voltage across its cell membrane. The outside is more electrically positive than the inside.

Voltages in cells are determined by the concentrations of charged ions, chiefly sodium and potassium (both with a \+1 positive charge). The lipids that make up a cell membrane do not permit these ions to pass through, but certain embedded proteins, the *ion channels*, can selectively let through ions and even “pump” ions against their concentration gradient. One key ion pump found in neurons is the [sodium\-potassium pum](https://en.wikipedia.org/wiki/Sodium%E2%80%93potassium_pump)p, which pumps 3 sodium ions out of the cell and 2 potassium ions in. Since 2\-3 \= \-1, the sodium\-potassium pump keeps the inside of the cell more negative than the outside.

This default state, the *resting potential*, for a neuron is about \-70 mV. (Again, remember: more negative on the inside.)

So what happens when the neuron “fires”?

It comes down to changes in ion channels. There are many types of ion channels in neurons, but a well\-studied example is the sodium ion channel.

When sodium ion channels open, they let sodium ions into the cell, which make the inside *more positive.* This is called *depolarization* — remember, the inside started out negative, so letting in a bunch of positive ions reduces the membrane potential to zero and even overshoots, making it *more* positive inside than outside.

In response, potassium ion channels open, letting potassium ions out of the cell, *repolarizing* it until it’s once again more negative on the inside. This stage too has an overshoot — the membrane potential goes *even more negative* than \-70 mV and gradually returns back there.

The trick is, these ion channels are *voltage\-gated*. If the depolarization is strong enough, it triggers a positive feedback loop where *more sodium ion channels open*, making the inside of the neuron even more positive, and opening even more sodium ion channels, and so on.

This is what happens when the neuron *fires*. Voltage\-gated ion channels activate nearby ion channels along the axon, causing a traveling “patch” of depolarization, which flares and is extinguished at each point in turn as the potassium ions come in and repolarize the cell.

So what’s actually “traveling” along the axon? A patch of positive electric charge in a “wire” of mostly negative charge…so it is, in fact, a current.

A very small current.

Typically tens to hundreds of picoamperes — trillions of times less than the 15\-20 amperes that can be drawn from a typical household electrical outlet.

### What Happens When You Zap A Neuron?

[![](https://substackcdn.com/image/fetch/$s_!B_9k!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff5adf74c-5f1c-4d99-918b-8dee9fc0b636_730x598.jpeg)](https://substackcdn.com/image/fetch/$s_!B_9k!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff5adf74c-5f1c-4d99-918b-8dee9fc0b636_730x598.jpeg)

Electrodes placed across the frog’s legs, running a current through the muscles, make the legs twitch into the bent position.

The oldest way to “stimulate” a neuron to fire is by running an electrical current through it. This goes back to Galvani and his dead frogs [in 1792](https://en.wikipedia.org/wiki/Luigi_Galvani).

There’s no doubt that it works. But *why* does it work*?*

Because an externally applied electric current can start the depolarization process.

If you put a cathode (negatively charged) electrode somewhere around the neuron, it creates a localized electric field that attracts positive ions near it. Since there’s now a high concentration of positive ions near the cell, they flow down their concentration gradient across the cell membrane. This turns the inside of the cell *less negative/more positive*, causing depolarization.[1](https://sarahconstantin.substack.com/p/what-really-happens-when-a-neuron#footnote-1-143426243)

And, as we saw above, once you get a strong enough depolarization, the positive feedback of voltage\-gated ion channels takes over and you get a traveling action potential along the neuron.

If you put an anode (positively charged) electrode near the neuron, by contrast, you’ll get *hyperpolarization*, which will make it more difficult for the neuron to fire.

So this mechanism tells us a few things about electrical neurostimulation.

First of all, it can start a neuron firing from a dead stop.

Second of all, its effect depends entirely on the charge direction. Anodal and cathodal stimulation have *opposite effects* on the targeted neurons.[2](https://sarahconstantin.substack.com/p/what-really-happens-when-a-neuron#footnote-2-143426243)

Third of all, its effect depends on the physical extent and intensity of the electric field. We can predict that the neurons affected by electrical stimulation are going to be the neurons physically located near a sufficiently strong electric charge.[3](https://sarahconstantin.substack.com/p/what-really-happens-when-a-neuron#footnote-3-143426243)

Magnetic stimulation (eg [transcranial magnetic stimulation](https://en.wikipedia.org/wiki/Transcranial_magnetic_stimulation)) works exactly the same way.

It uses [induction](https://en.wikipedia.org/wiki/Electromagnetic_induction) to create an electric current. A magnetically\-generated electric current can depolarize or hyperpolarize nearby neurons based on the exact same mechanisms that an electrode\-applied current can.

In the case of transcranial magnetic stimulation, the direction of current flowing in the coil determines the polarity of the magnetic field, which in turn determines the electric charge applied to the brain.

In practice, TMS is usually produced by alternating current, so the induced electric field oscillates — it’s not directly comparable to direct electrode stimulation with an anode or cathode.

And the proposed mechanisms of action of TMS include not only direct effects on a targeted neuron’s membrane potential but indirect effects involving how neurons “excite” and “inhibit” their post\-synaptic neighbors, which we’ll save for a later post.

But basically, both magnetic and electrical stimulation of neurons work by applying an electric field near them, and electric fields can directly alter the neuron’s membrane potential, causing a neuron to fire if it depolarizes enough, or to *not* fire when it otherwise would if it hyperpolarizes enough.

In the next post I’ll cover what happens to *post\-synaptic* (downstream) neurons after a neuron fires.

[1](https://sarahconstantin.substack.com/p/what-really-happens-when-a-neuron#footnote-anchor-1-143426243)This is all *extracellular* electrode stimulation, where the electrode is outside the neuron. It’s also possible to directly inject current *inside* a neuron with much tinier (\~1 micron) pipette filled with a wire and conduction solution. But that’s very technically difficult. It’s not how Galvani did it, obviously, and the electrodes used in today’s clinical contexts — deep brain stimulators, cochlear implants, brain\-computer interfaces — are all extracellular electrodes.

[2](https://sarahconstantin.substack.com/p/what-really-happens-when-a-neuron#footnote-anchor-2-143426243)What about alternating current? Well, then you can get the neuron to fire when the charge is negative, and block it from firing when the charge is positive. You can even *entrain* a rhythmic firing pattern in the neuron this way.

[3](https://sarahconstantin.substack.com/p/what-really-happens-when-a-neuron#footnote-anchor-3-143426243)of course neuron type and other factors will also affect how *much* charge needs to be applied to get a neuron to fire, or stop firing. But “how much charge is there in the vicinity of this neuron” is always relevant, afaik.