# "Scaling Laws" for AI And Some Implications

*How much bigger (and better) can LLMs get in the 2020's?*

Published: 2023-04-12
Source: https://sarahconstantin.substack.com/p/scaling-laws-for-ai-and-some-implications

---

## **Scaling Laws in AI**

How does AI performance depend on computer hardware?

There are empirical “scaling laws” that observe consistent relationships between hardware inputs and performance outputs of AI models on benchmarks.

There is no guarantee that an observed scaling relationship is eternal, of course; a more efficient algorithm can get better results with less “compute”.  A scaling relationship and a predictable rate of hardware improvement implies a *lower bound* (but not an upper bound) on AI improvements over time.

I’ve put together some comparisons of the *magnitude* of the scaling relationships that different recent papers have found, to get some sense of how consistent it is. The answer is “kinda but not perfectly so”. (I’m very grateful to Gwern’s extensive [bibliography](https://gwern.net/note/scaling) of machine learning scaling papers.)

### **Scaling Laws for LLMs in FLOPs**

[![](https://substackcdn.com/image/fetch/$s_!mHsO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F90a17b02-3284-4b75-88dd-7dcef1eddaa3_922x718.png)](https://substackcdn.com/image/fetch/$s_!mHsO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F90a17b02-3284-4b75-88dd-7dcef1eddaa3_922x718.png)

### Scaling Laws for LLMs in Dataset Size

[![](https://substackcdn.com/image/fetch/$s_!e0Zq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe30095ac-1f51-404f-87ce-d023e3222ca3_889x511.png)](https://substackcdn.com/image/fetch/$s_!e0Zq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe30095ac-1f51-404f-87ce-d023e3222ca3_889x511.png)

### Scaling Laws For LLMs in Number of Parameters

[![](https://substackcdn.com/image/fetch/$s_!Lf96!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5b8fed25-888b-4317-92f2-29ce6d53c562_871x820.png)](https://substackcdn.com/image/fetch/$s_!Lf96!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5b8fed25-888b-4317-92f2-29ce6d53c562_871x820.png)

Most notably, a DeepMind paper from 2022\[1] reported a scaling relationship between FLOPs (floating point operations) and training loss for LLMs (Chinchilla and Gopher).

This paper found “curvature of the FLOP\-Loss frontier”: that is, on the lower end of the amount of training computation, training loss drops faster as FLOPs increase, and on the higher end, training loss drops slower.

[![](https://substackcdn.com/image/fetch/$s_!gv7q!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb392b3bc-73e6-4c7f-b17f-293bc275cfab_723x570.png)](https://substackcdn.com/image/fetch/$s_!gv7q!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb392b3bc-73e6-4c7f-b17f-293bc275cfab_723x570.png)

Other papers similarly find scaling relationships between model performance and number of model parameters, number of training FLOPs, and size of training data.

There seems to be a tendency for later papers to find larger scaling coefficients.

In particular, DeepMind’s 2022 scaling law exponents were notably larger than OpenAI’s 2020 exponents.

This suggests that, as AI technology improves, we may be overall getting better at gaining improved performance from larger models and more data.

Is this paradoxical, given that [one upshot](https://www.lesswrong.com/posts/6Fpvch8RR29qLEWNH/chinchilla-s-wild-implications) of the 2022 Deepmind paper was that much *smaller* models could outperform larger ones if they were trained on more data?

No, as far as I understand; DeepMind’s scaling laws revealed that the contribution of the “model term” (which declines according to a power law as model parameters increase) to the overall loss function was small relative to the contribution of the “data term” (which declines according to a somewhat smaller\-exponent power law as dataset size increases, and thus *stays big longer).*

But *both* exponents calculated by DeepMind are larger than the ones calculated by OpenAI’s earlier paper; DeepMind was seeing better returns to scale overall.

### **Power Laws: Some Math**

A scaling power law relates training or test loss (generally cross\-entropy loss) to some input variable like FLOPS, dataset size, or number of model parameters, through a power relationship:

Loss \= C \* X^a

Where C is a constant, X is the input variable, and a is another constant, the exponent.

In a power\-law model, if X is multiplied by 10, we get a loss equal to

C\*(10X)^a \= C \* 10^a \* X^a.

Thus, the percent change in loss when X grows by a factor of 10 should be a constant, equal to 10^a.

Power\-law scaling in X implies that if X grows exponentially, the cross\-entropy loss should also decline exponentially.  In other words, if you plot loss and X on a log\-log curve you should get a straight line.

*Accuracy* is not quite the same as loss.

A machine\-learning model, when answering a question, gives a probability distribution over possible answers, not literally a single answer. (We then often ask it to select the most probable answer as its output.)

Accuracy scores an answer as “1” if it’s correct and “0” if it’s incorrect. Accuracy gives no partial credit for being “close”, say, by assigning the correct answer *almost* as much probability as the incorrect top\-probability answer. Accuracy also doesn’t score a model higher for being more confident in the correct answer; all correct answers are treated the same.

So accuracy scaling is not quite the same measurement as loss scaling (and there’s no easy conversion formula between them either). It’s a little bit of an abuse of notation that I’ve put both types of “scaling” in the same tables above.

But both accuracy and loss are, roughly measurements of how “good” a model is, and if models “get better with scale” we’d expect scaling in both accuracy and loss.

### **Relating Parameters, Data, and FLOPs**

Training FLOPs are proportional to the number of updates made (training data \* epochs) and the number of connections between neural net nodes (empirically, this is proportional to the number of parameters.)

The empirical [rule of thumb](https://dynomight.net/scaling/) is compute \= 6\*N\*D where N is the number of parameters and D is the size of the dataset.

From a [GPU perspective](https://www.alignmentforum.org/s/T9pBzinPXYB3mxSGi/p/HvqQm6o8KnwxbdmhZ), the FLOPs required for training a model can be estimated as

Training time x \#cores x peak FLOP/s x utilization rate.

The utilization rate diminishes\[16] as the number of GPUs increases, due to overhead in communication between GPUs. On the transformer model BERT, utilization is about 33% for 2 GPUs, decreasing to 20% for 128 GPUs.

Training time diminishes with a power\-law relationship as the number of GPUs increases, independent of clock speed.

These relationships can be used to model how AI model performance can be expected to scale as:

* AI firms buy more GPUs, and
* GPUs improve their peak FLOP/s performance

If loss drops proportionately to

1/C^a

where C is the number of computational operations and a is the power law exponent for FLOPs,

then putting all this together, for G GPUs at P peak speed and U utilization rate, the loss will be

(G^(1\-b)\*P\*U)^(\-a).

As you add more GPUs, model performance should improve in a power\-law fashion…IF utilization doesn’t drop with number of GPUs fast enough to cancel it out.

As GPU performance improves, model performance should likewise improve in a power\-law fashion, because you can use more computational operations for some combination of larger training datasets and larger models.

### **GPU Availability**

[![](https://substackcdn.com/image/fetch/$s_!2Jqd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1c748c54-2c73-41d8-931e-fe309e389b2c_1011x727.png)](https://substackcdn.com/image/fetch/$s_!2Jqd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1c748c54-2c73-41d8-931e-fe309e389b2c_1011x727.png)

The current [largest AI model](https://ourworldindata.org/grapher/artificial-intelligence-training-computation?time=earliest..latest) as of April 2023, in terms of compute, is GPT\-4, using 2\.4x10^25 FLOPs.

GPT\-4 was trained on [tens of thousands](https://www.fierceelectronics.com/sensors/chatgpt-runs-10k-nvidia-training-gpus-potential-thousands-more) of Nvidia GPUs and reportedly GPT\-5 is being trained on [25,000 Nvidia GPUs.](https://twitter.com/abacaj/status/1627189548395503616)  OpenAI says they trained GPT\-4 for [six months.](https://techcrunch.com/2023/03/14/openai-releases-gpt-4-ai-that-it-claims-is-state-of-the-art/)

Currently the [largest supercomputer in the world](https://www.weforum.org/agenda/2022/01/visualizing-power-supercomputers-teraflops-technology/) is 5\.3x10^17 FLOPs, which (at 20% utilization and continuous usage) would have taken 7 *years* to train GPT\-4\.

If AI models continue to scale up compute, how does that compare to GPU production worldwide?

Reportedly, there were [136,000 GPU servers](https://www.fierceelectronics.com/embedded/look-ai-server-growth-be-boosted-chatbots-more) shipped worldwide in 2022\.

So, OpenAI is already consuming, apparently, nearly 20% of the world’s high\-performance GPUs?

I’m not sure if that figure is right, but it’s shocking if true.

Desktop GPUs, which as far as I know are mostly older and less performant than the GPU servers used in AI applications, number in the tens of millions sold per year, but worldwide shipments have slowly been declining for decades.

[![](https://substackcdn.com/image/fetch/$s_!az8q!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fefa2f457-b6ae-4941-ad4a-db47b3332ee5_1066x388.png)](https://substackcdn.com/image/fetch/$s_!az8q!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fefa2f457-b6ae-4941-ad4a-db47b3332ee5_1066x388.png)

So one big question is: over the next few years, is the global supply of AI\-capable GPUs going to look more like 5x the GPU requirements for training GPT\-4, or more like 400x?

Or can it ramp up to grow even faster as demand for AI GPUs increases?

[Epoch AI](https://epochai.org/blog/trends-in-gpu-price-performance#:~:text=For%20top%20GPUs%20at%20any,%24%20doubles%20every%202.07%20years).) finds a steady exponential growth trend in GPU FLOP/s from 1848 models of GPU between 2006 and 2021\. The doubling rate is about 2x every 2\.31 years, or slightly slower than Moore’s Law.

This implies that, if GPU performance trends continue until 2030 and world GPU production *doesn’t* increase by a lot, the maximum amount of “compute” in an AI model can’t grow more than 3 orders of magnitude by the end of the decade. (One OOM from performance improvements and two from big AI firms buying more GPUs.)

(For comparison’s sake, the compute used in training AI models has increased by *[8](https://epochai.org/blog/compute-trends)* [orders of magnitude](https://epochai.org/blog/compute-trends) between 2012 and today.)

### **Data Limitations**

The most recent scaling “laws”\[1] find a much stronger dependence on the amount of training data than the number of model parameters. Chinchilla is a smaller model than PaLM but uses more data, and it performs better.

Current large language models are trained on about 50% “high\-quality” data (books, research papers, news, Wikipedia) and 50% “low\-quality” data; it’s plausible that their abilities would grow less quickly in proportion to training data if the mix of the training data shifted to be lower quality.

“High\-quality” text data on the internet today comes to about 9 trillion words, growing at a few % per year; Epoch AI researchers estimate\[15] that by 2026 LLMs will be trained on all the high\-quality data available, while low\-quality data will not be exhausted until 2034\.

The largest datasets for LLMs to date have been trained on about a trillion words; there’s currently only 10x that much “high\-quality” data on the internet, and less than 1000x that much “low\-quality” data, though of course both bodies of text are growing over time.

This gives us, very roughly, an upper bound of 3 orders of magnitude of growth in the data available for LLMs this decade.

**References**

\[1]Hoffmann, Jordan, et al. "Training compute\-optimal large language models." *arXiv preprint arXiv:2203\.15556* (2022\).

\[2]Kaplan, Jared, et al. "Scaling laws for neural language models." *arXiv preprint arXiv:2001\.08361* (2020\).

\[3]Henighan, Tom, et al. "Scaling laws for autoregressive generative modeling." *arXiv preprint arXiv:2010\.14701* (2020\).

\[4]Ivgi, Maor, Yair Carmon, and Jonathan Berant. "Scaling laws under the microscope: Predicting transformer performance from small scale experiments." *arXiv preprint arXiv:2202\.06387* (2022\).

\[5]Cherti, Mehdi, et al. "Reproducible scaling laws for contrastive language\-image learning." *arXiv preprint arXiv:2212\.07143* (2022\).

\[6]Fernandes, Patrick, et al. "Scaling Laws for Multilingual Neural Machine Translation." *arXiv preprint arXiv:2302\.09650* (2023\).

\[7]Tay, Yi, et al. "Transcending scaling laws with 0\.1% extra compute." *arXiv preprint arXiv:2210\.11399* (2022\).

\[8]Chung, Hyung Won, et al. "Scaling instruction\-finetuned language models." *arXiv preprint arXiv:2210\.11416* (2022\).

\[9]Hernandez, Danny, et al. "Scaling laws for transfer." *arXiv preprint arXiv:2102\.01293* (2021\).

\[10]Gordon, Mitchell A., Kevin Duh, and Jared Kaplan. "Data and parameter scaling laws for neural machine translation." *Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing*. 2021\.

\[11]Bansal, Yamini, et al. "Data scaling laws in NMT: The effect of noise and architecture." *International Conference on Machine Learning*. PMLR, 2022\.

\[12]Chen, Mark, et al. "Evaluating large language models trained on code." *arXiv preprint arXiv:2107\.03374* (2021\).

\[13]Austin, Jacob, et al. "Program synthesis with large language models." *arXiv preprint arXiv:2108\.07732* (2021\).

\[14]<https://huggingface.co/calculator/>

\[15]Geiping, Jonas, and Tom Goldstein. "Cramming: Training a Language Model on a Single GPU in One Day." *arXiv preprint arXiv:2212\.14034* (2022\).

\[16]Frey, Nathan C., et al. "Benchmarking resource usage for efficient distributed deep learning." *2022 IEEE High Performance Extreme Computing Conference (HPEC)*. IEEE, 2022\.

\[17]Chatelain, Amélie, et al. "Is the number of trainable parameters all that actually matters?." *I (Still) Can't Believe It's Not Better! Workshop at NeurIPS 2021*. PMLR, 2022\.

\[18]Hestness, Joel, et al. "Deep learning scaling is predictable, empirically." *arXiv preprint arXiv:1712\.00409* (2017\).

\[19]Villalobos, Pablo, et al. "Will we run out of data? An analysis of the limits of scaling datasets in Machine Learning." *arXiv preprint arXiv:2211\.04325* (2022\).