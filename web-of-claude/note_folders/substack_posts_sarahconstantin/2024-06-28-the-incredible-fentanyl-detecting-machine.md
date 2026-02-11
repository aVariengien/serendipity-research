# The Incredible Fentanyl-Detecting Machine

*and a little foray into the world of nondestructive testing*

Published: 2024-06-28
Source: https://sarahconstantin.substack.com/p/the-incredible-fentanyl-detecting

---

[![](https://substackcdn.com/image/fetch/$s_!A8S0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F052283c3-a085-48aa-8615-4b97b6e609f1_1720x1147.avif)](https://substackcdn.com/image/fetch/$s_!A8S0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F052283c3-a085-48aa-8615-4b97b6e609f1_1720x1147.avif)

An NII machine in Nogales, AZ. ([Image source](https://www.nbcconnecticut.com/news/politics/border-fentanyl-scanners-unused-needs-congress-funds-to-install/3234076/))

There’s bound to be a lot of discussion of the Biden\-Trump presidential debates last night, but I want to skip all the political prognostication and talk about the real issue: fentanyl\-detecting machines.

Joe Biden says:

> And I wanted to make sure we use the machinery that can detect fentanyl, these big machines that roll over everything that comes across the border, and it costs a lot of money. That was part of this deal we put together, this bipartisan deal.
> 
> More fentanyl machines, were able to detect drugs, more numbers of agents, more numbers of all the people at the border. And when we had that deal done, he went – he called his Republican colleagues said don’t do it. It’s going to hurt me politically.
> 
> He never argued. It’s not a good bill. It’s a really good bill. We need those machines. We need those machines. And we’re coming down very hard in every country in Asia in terms of precursors for fentanyl. And Mexico is working with us to make sure they don’t have the technology to be able to put it together. That’s what we have to do. We need those machines.

Wait, what machines?

You can remotely, non\-destructively detect that a bag of powder contains fentanyl rather than some other, legal substance? And you can sense it *through the body of a car?*

My god. The LEO community must be holding out on us. If that tech existed, we’d have [tricorders](https://en.wikipedia.org/wiki/Tricorder) by now.

What’s actually going on here?

### What’s Up With Fentanyl\-Detecting Machines?

First of all, Biden didn’t make them up.

This year, the Department of Homeland Security reports that Customs and Border Patrol (CBP) has deployed “Non\-Intrusive Inspection” at the US’s southwest border:

> “By installing 123 new large\-scale scanners at multiple POEs along the southwest border, CBP will increase its inspection capacity of passenger vehicles from two percent to 40 percent, and of cargo vehicles from 17 percent to 70 percent.”

In fact, there’s something of a scandal about how many of these scanners have been sitting in warehouses but not actually deployed. CBP Commissioner Troy Miller complained to [NBC News](https://www.nbcnews.com/politics/immigration/border-fentanyl-scanners-unused-congress-provided-no-money-rcna141432) that the scanners are sitting idle because Congress hasn’t allocated the budget for installing them.

These are, indeed, big drive\-through machines. They X\-ray cars, allowing most traffic to keep flowing without interruption.

#### Could an X\-ray machine really detect fentanyl inside a car?

To answer that, we have to think about what an x\-ray machine actually does.

An X\-ray is a form of high\-energy, short\-wavelength electromagnetic radiation. X\-rays can pass through solid objects, but how easily they pass through depends on the material — higher [atomic number](https://en.wikipedia.org/wiki/Atomic_number)  materials are more absorbing per unit mass.

This is why bones will show up on an X\-ray scan. The calcium (element 20\) in bones has higher atomic mass than the other most common elements in living things (carbon, hydrogen, oxygen, nitrogen, sulfur), and bones are also denser than soft tissue, so bones absorb X\-rays while the rest of the body scatters it.

This is also how airport security scans baggage: a cabinet x\-ray shows items inside a suitcase, differentiated by density. It’s also how industrial CT scans can look inside products nondestructively to see how they’re made.

[![](https://substackcdn.com/image/fetch/$s_!eAGL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa31548aa-a2c8-4ae1-83e1-8b69e3904383_2081x1080.png)](https://substackcdn.com/image/fetch/$s_!eAGL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa31548aa-a2c8-4ae1-83e1-8b69e3904383_2081x1080.png)

[Lumafield](https://www.lumafield.com/article/finding-lead-in-stanleys-quencher-industrial-ct)’s industrial CT scanner can tell dense, high\-atomic\-number lead solder apart from stainless steel.

To some extent, X\-ray scanners can distinguish materials, by their density and atomic number.

But [fentanyl](https://en.wikipedia.org/wiki/Fentanyl) is an organic compound — made of carbon, hydrogen, nitrogen, and oxygen, just like lots of other things. Its density is a very normal 1\.1 g/mL (close to the density of water.)

I’m pretty sure it’s not going to be possible to tell fentanyl apart from other things by its density and atomic number alone.

Indeed, that’s not what the scanner vendors are promising to do.

Kevin McAleenam, the former DHS secretary who founded [Pangiam](https://pangiam.com/), the AI\-based scanning company that plans to analyze the X\-ray images, [said](https://www.theverge.com/2024/3/14/24099953/cbp-border-ai-fentanyl-scanners-privacy) that his software would correlate X\-ray results with vehicle manifests to see if a load looks like it’s supposed to, or whether it’s suspicious in some way.

> “We can build software products that tell the officer, ‘That load’s supposed to be melons, it looks exactly like the other thousand shipments of melons that have crossed this border over the last two years, we don’t think you need to inspect it further.””

That’s not *fentanyl detection* — remote X\-ray\-based detection of a particular chemical compound — it’s the much easier problem of anomaly detection.

Maybe, indeed, you can catch a drug smuggler by using the X\-ray machine to notice a discrepancy between what he said and what the inside of his truck looks like.

But it’s not a “fentanyl scanner” that detects fentanyl in the way a metal detector detects metal. [1](https://sarahconstantin.substack.com/p/the-incredible-fentanyl-detecting#footnote-1-146086095)

The manufacturer of these X\-ray scanning portals, OSI systems, does [claim](https://www.rapiscan-ase.com/products/portal/z-portal-for-passenger-vehicle-screening) they can detect “metallic and organic threats and contraband, such as weapons, stowaways, explosives, drugs, and alcohol.” This seems like a bit of marketing exaggeration — an X\-ray machine would not be able to detect *in full generality* that something is an explosive or illegal drug as opposed to an innocuous/legal material, though it could tell, e.g., that there were organic compounds stored in parts of the vehicle that were expected to be empty.

### But I Wanted Remote Chemical Compound Detection!

Ok, but suppose we wanted to detect the presence of fentanyl, or some other particular organic compound. How close can we get to doing that for real?

This isn’t just about law enforcement. There are lots of reasons you might want to find out what something is made of without touching it. Nondestructive quality control in manufacturing; analyzing the geological composition of underground mineral resources; medical diagnostics; and much more.

In an ideal world, if you want to know the chemical composition of an object, you’d get to take a sample.

Then you can use powerful, destructive methods like [mass spectrometry](https://en.wikipedia.org/wiki/Mass_spectrometry), where you ionize the whole thing, run an electric current through it, and look at the amount of each ion (ranked by mass\-to\-charge ratio) to reconstruct which chemical compounds must have been in the mixture.

If you’re looking at biological samples, you can put nature to work for you at detecting particular compounds; find an antibody, [aptamer](https://en.wikipedia.org/wiki/Aptamer), or [oligonucleotide](https://en.wikipedia.org/wiki/Oligonucleotide) that binds selectively to your compound of interest, and attach it to some highly noticeable molecule like a dye. This is how [immunoassays](https://en.wikipedia.org/wiki/Immunoassay) like pregnancy tests and home COVID tests work.

But these are all destructive tests; you have to have a sample, and you have to be okay with using it up in the testing process.

What can the world of non\-destructive tests do?

#### Spectroscopy

The general category of *spectroscopy* refers to measuring how light is absorbed vs scattered by a sample.

X\-ray imaging is a form of spectroscopy whose “light” is x\-rays; other wavelengths, ranging from microwaves through infrared and visible light to ultraviolet, are generally less able to penetrate opaque solid objects but better at distinguishing between lighter organic chemical compounds.

Small, affordable [infrared spectrometers](https://www.thermofisher.com/us/en/home/industrial/spectroscopy-elemental-isotope-analysis/molecular-spectroscopy/fourier-transform-infrared-spectroscopy/applications.html) are used for everything from detecting the blood alcohol content of a (suspected) drunk driver to nondestructively analyzing the composition of food products and pharmaceuticals on the production line.

FTIR, or Fourier Transform InfraRed spectroscopy, shines a beam on the sample consisting of many infrared wavelengths at once, and measures how much of each wavelength is absorbed, resulting in a characteristic "spectrum” or fingerprint for each sample.

FTIR can’t tell apart *all* chemical compounds, but it’s pretty sensitive. It can distinguish organic compounds that differ by just a single [functional group](https://en.wikipedia.org/wiki/Functional_group#:~:text=A%20functional%20group%20is%20a%20group%20of%20atoms%20in%20a,the%20molecule%20by%20covalent%20bonds.).

Why do these very similar compounds have different IR spectra but indistinguishable X\-ray absorption? In other words, why *can’t* you use X\-rays to determine fine\-grained chemical composition?

Because infrared light is lower energy, so it mostly interacts with the vibrations in chemical bonds (and behaves differently with different bonds), while X\-rays go straight to the [inner\-shell electrons](https://www.ncbi.nlm.nih.gov/books/NBK537046/) of the atoms (an interaction that depends less on the molecular environment surrounding the struck atom).

UV and visible light are intermediate in energy level, so they have enough energy to knock valence\-shell electrons to higher orbitals, but not enough to knock inner\-shell electrons up to the valence shell.

So UV and visible light spectroscopy methods are intermediate between infrared (lots) and X\-rays (very little) in their ability to distinguish between similar chemical compounds.

The bottom line is, there’s a physical tradeoff between how good a spectroscopic technique is at penetrating solid objects (like a car) and how sensitive it is at telling different compounds apart. You can certainly tell fentanyl from aspirin with FTIR; but infrared light won’t pass through solid metal.

#### Ok, That’s Light. What About Sound? Or Electricity?

There are other non\-destructive methods for sensing material composition that also work by the same basic premise of “send a wave of some sort to the material, see what happens to what’s left of the wave after it’s reflected back or transmitted through, notice how different materials distort it differently.”

When you do this with sound waves, you have ultrasound imaging. Sound is also distorted differently by different materials.

The key metric for ultrasound is [acoustic impedance](https://www4.uwsp.edu/physastr/kmenning/Phys115/Link5-09_acoustic_impedance.pdf), or how much a material resists conducting sound.

The acoustic impedance of a material is basically just a function of stiffness and density. So ultrasound is good enough for visualizing the shapes of firm, dense masses in the body (e.g. it can tell “baby” from “amniotic fluid”) but it can’t tell apart two different chemical compounds with the same physical properties.

What about electricity?

[Impedance spectroscopy](https://en.wikipedia.org/wiki/Dielectric_spectroscopy) involves running current through an object to measure the impedance (measured in ohms) of the material inside.

The principle here is that different materials conduct electricity differently. Even small differences in molecular structure can affect a material’s dielectric properties.

In medicine, it’s possible to use [impedance tomography](https://en.wikipedia.org/wiki/Electrical_impedance_tomography) to visualize and monitor blood clots or lung function in real time (since a clot in a blood vessel or fluid in a lung will show up as a difference in impedance.)

However, impedance spectroscopy doesn’t work for truly *remote* sensing, because you need electrodes to be touching the sample. (No beaming electricity through the open air.) It also couldn’t detect a sample of fentanyl inside a car, because the metal would shield against the electricity.

#### Dude, Where’s My Tricorder?

While the list of non\-destructive imaging or material characterization techniques is long, most of them fundamentally use light, electricity, or sound, or combinations of those.[2](https://sarahconstantin.substack.com/p/the-incredible-fentanyl-detecting#footnote-2-146086095)

And some rough version of the penetration/specificity tradeoff seems to hold generally; the better a form of energy is at punching through thick heavy materials, the less it cares about the difference between slightly different organic molecules.

So that’s the challenge of “detecting fentanyl in your car” (or, more medically, things like “detect a biomarker in your body”). Usually the techniques that allow completely remote, label\-free sensing can’t tell you as much about chemical composition, and the techniques that can give you precise chemical information require a sample that’s, if not destroyed by analysis, then at least conveniently placed relative to the sensor.

Could that change?

In Big Hero 6, medical robot Baymax “scans” the entire city of San Fransokyo to detect all men with the same cholesterol, blood type, and hormone levels as the suspect. Could we ever do this?

[![](https://substackcdn.com/image/fetch/$s_!IAqQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F83593191-f2a4-481c-97d8-6f9e8cae108d_3406x1372.png)](https://substackcdn.com/image/fetch/$s_!IAqQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F83593191-f2a4-481c-97d8-6f9e8cae108d_3406x1372.png)

god i wish this were real

Right now it seems pretty intractable, though I’m not prepared to claim it’s physically impossible.

There are a few special cases where Nature is kind — for instance, some compounds, like [hemoglobin](https://en.wikipedia.org/wiki/Photoacoustic_imaging), have a strong photoacoustic effect, so a laser beam and an ultrasound sensor are enough to pick them up.

But few techniques are fully general. Photoacoustic imaging can’t tell apart chemically similar compounds (like estrogen and testosterone.) FTIR could tell them apart — but you can’t just point it at a person and read off the composition of their bloodstream, because the infrared doesn’t penetrate more than a millimeter into the skin.

Maybe someday we’ll combine different modalities to get a vastly *expanded* set of remote chemical sensing capabilities. But the tradeoff landscape is still there, and it’s less friendly to potential tricorders, Baymaxes, and fentanyl scanners than you might hope.

[1](https://sarahconstantin.substack.com/p/the-incredible-fentanyl-detecting#footnote-anchor-1-146086095)And it’s not just Biden who refers to the new X\-ray machines as “fentanyl scanners” — that phrase is all over the news and in the “[Deploy Fentanyl Scanners Act of 2024](https://www.congress.gov/bill/118th-congress/senate-bill/3965/text)” introduced in the Senate this March.

[2](https://sarahconstantin.substack.com/p/the-incredible-fentanyl-detecting#footnote-anchor-2-146086095) (Or bombardment with bigger particles like [neutrons](https://www.usgs.gov/usgs-triga-reactor/neutron-activation-analysis#:~:text=Neutron%20activation%20analysis%20(NAA)%20is,the%20concentration%20of%20that%20element.), which, like X\-rays but more so, is better suited for detecting the presence of heavy elements than for classifying different organic molecules made of light elements.)