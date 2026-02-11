# SS26 Color Stats

*It's that time of year again*

Published: 2025-10-14
Source: https://sarahconstantin.substack.com/p/ss26-color-stats

---

So, as regular readers may recall, I like to look at color trends in fashion quantitatively. It’s a quixotic little hobby, but it’s mine (and, strangely, I have *never seen anybody else do it*.)

It’s also a nice little occasion to reflect on the passage of time, pick a theme for the year ahead, and suchlike personal meditations.

Past posts: [FW25](https://sarahconstantin.substack.com/p/fw25-color-stats), [SS25](https://sarahconstantin.substack.com/p/2025-color-trends), [FW24](https://sarahconstantin.substack.com/p/fw24-color-stats), [SS24](https://sarahconstantin.substack.com/p/2024-color-trends).

### Methodology Recap

Designer fashion collections are released several times a year, but the ones I track are spring/summer and fall/winter ready\-to\-wear, which come out in fall and spring respectively. Twice a year there’s essentially a fashion industry trade fair lasting several weeks — New York Fashion Week, London Fashion Week, Milan Fashion Week, and Paris Fashion Week.

These are for both men’s and women’s clothes (or unisex; lines are blurred these days), but generally slant female; there’s a separate menswear season that I don’t track.

Vogue Magazine generously hosts a *lot* of [free images](https://www.vogue.com/fashion-shows/spring-2026-ready-to-wear) of these fashion collections; this season there were over 13,000 pictures.

This year I did both *manual counts*, where I counted how many “looks” a given color (as subjectively determined by me) appeared in, and *automated counts*, where I asked an LLM (currently GPT\-4o) to identify all the colors in the outfit in each image and aggregated the counts across images. I’m using the same code and prompt as I have for the past several years for the automated counts.

As in past seasons, I only manually count non\-neutral colors (\=not black, white, gray, brown, beige, etc) in order to save time; automated counts include neutrals and non\-neutrals.

There are a couple reasons why manual and automated counts might diverge:

* Color lumping/splitting effects; for instance, LLMs tend to lump many shades of green into the word “green” while I differentiate more finely, leading to the LLM scoring green as more common than I do. 

	+ This tends to bias the automated counts towards more general color categories vs. the manual counts.
* Repetition effects; the LLM will often repeat a color name multiple times per image, for instance if there is a red belt *and* red shoes that might be counted as two instances of red, whereas I’d manually count that as one instance of red. 

	+ This will tend to bias automated counts towards colors that appear more in accessories; it also just adds noise.
* Ambiguous cases; e.g. I might identify a color as khaki that the LLM considers olive green.

	+ This just adds noise, except to the extent that LLMs have a systematic color categorization bias. (They do seem to be slanted towards greens and purples, in my experience.)
* Synonym effects; the LLM may separately count “gray” and “grey”, or “light” vs “pale” vs “pastel” shades of a color.

	+ This will lead to biasing automated counts to *lower counts* but *more different instances of* synonymous or nearly\-synonymous colors.

### Results

[![](https://substackcdn.com/image/fetch/$s_!xmz5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc546848f-5341-4887-8eb9-2c219ce783dd_2518x1356.png)](https://substackcdn.com/image/fetch/$s_!xmz5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc546848f-5341-4887-8eb9-2c219ce783dd_2518x1356.png)

Automated Color Counts

As in previous years, we see black, white, and other neutrals top the chart, and red is the top non\-neutral color.

[![](https://substackcdn.com/image/fetch/$s_!vUdF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F353da9df-9499-493c-9247-c0792239666f_2514x1338.png)](https://substackcdn.com/image/fetch/$s_!vUdF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F353da9df-9499-493c-9247-c0792239666f_2514x1338.png)

Automated Non\-Neutral Color Counts

What especially pops out in the manual color counts is the prevalence of pastel yellow, right after perennial classics like red, pastel pink, and pastel blue:

[![](https://substackcdn.com/image/fetch/$s_!M0H2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F32d17266-342f-46dc-8ef6-3303db6152e7_1950x1336.png)](https://substackcdn.com/image/fetch/$s_!M0H2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F32d17266-342f-46dc-8ef6-3303db6152e7_1950x1336.png)

Manual Non\-Neutral Color Counts

In fact, if you compare to last year’s spring season ([SS25](https://sarahconstantin.substack.com/p/2025-color-trends)), you see a systematic movement towards soft pastels and away from brighter shades.

* **Rising** (significantly higher in rank than last year):

	+ pastel yellow (\#29 → \#4, manual)
	+ lavender (\#26 → \#13, manual)
	+ tan (\#21 → \#11, automated)
* **New** (in the top 30 this year but not last year):

	+ light tan (automated)
	+ dusty rose (manual)
	+ coral (automated)
	+ blush (automated)
	+ medium pink (manual)
	+ dark pink (automated)
	+ brick red (manual)
	+ mustard yellow (manual)
	+ mint green (manual)
	+ sage (manual)
	+ light purple (automated)
	+ dark purple (automated)
* **Falling (**significantly lower in rank this year than last year):

	+ hot pink (\#9 → \#18, manual)
	+ bubblegum pink (\#17 → \#30, manual)
	+ true orange (\#12 → \#25, manual)
* **Lost (**in the top 30 last year but not this year):

	+ ivory (automated)
	+ dark red (automated)
	+ coral pink (manual)
	+ spiced orange (manual)
	+ tangerine (manual)
	+ mustard yellow (automated)
	+ lime green (automated)
	+ medium blue (automated)
	+ Dutch blue (manual)
	+ royal blue (automated)

Or, visualized, you can see that there are a lot of muted, coolish, pale shades among this year’s winners, and hot, bright colors among the losers:

![](https://substackcdn.com/image/fetch/$s_!YLFl!,w_720,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe9bc1cb7-1efb-4824-b534-ba91a7fc3af1_1600x2400.jpeg)![](https://substackcdn.com/image/fetch/$s_!wh6w!,w_720,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a14f32a-ccc9-45a4-a693-7cc6df24a0e7_1600x2400.jpeg)

SS26: Pastel Winners vs Bright Losers

### Economic Trends

To the extent that there are recurrent themes in the SS26 season, we’re looking at *pastels, preppiness, and generally cautious/conservative choices*; these are both visible to me and echoed in Vogue’s editorial coverage.

It makes sense that the fashion world would pull back from the edge; these are bad times for the luxury goods market.

2024 saw total luxury goods spending [down 2%](https://english.elpais.com/economy-and-business/2025-06-08/luxury-isnt-what-it-used-to-be-whats-happening-to-the-worlds-most-exclusive-brands.html), with many brands seeing profit drops:

[![](https://substackcdn.com/image/fetch/$s_!9Wlx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe8da7362-d4ef-42af-b5c9-dfbbefa4fa40_1444x1012.png)](https://substackcdn.com/image/fetch/$s_!9Wlx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe8da7362-d4ef-42af-b5c9-dfbbefa4fa40_1444x1012.png)

The final 2025 numbers aren’t in (and preliminary numbers are not representative because Christmas\-season purchases are so big a percentage of the whole) but this is expected to be a weak year too, particularly because of tariffs in the US and the real estate bust in China.

When consumers pull back on luxury spending, fashion collections tend to reflect a swing “back to basics” — safer choices, less eccentricity. We are definitely *not* in the post\-pandemic spending boom of 2021 when wacky, tropical\-hued party clothes were ascendant. We’re also not seeing a lot of explicit political\-statement collections, despite the Trump presidency; if anything, the fashion world seems to be in retreat from current events.

### My Pick For 2026 Color Of The Year: Pastel Yellow

[![](https://substackcdn.com/image/fetch/$s_!lwWu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fae63bb30-61e3-42fd-8aa8-68cd91e66321_322x326.png)](https://substackcdn.com/image/fetch/$s_!lwWu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fae63bb30-61e3-42fd-8aa8-68cd91e66321_322x326.png)

\#F5EFAE

Pastel yellow is the most unobtrusive of the pastels. It’s a gentle, mild, fluffy color; think daffodils, baby chicks, fresh butter, warm sunshine.

If pastel pink evokes a romantic ingenue protagonist, then pastel yellow is the “supportive best friend” side character. Grounded; cheerful; not calling attention to itself.

The whole pastel range, from pink to peach to mint green to pastel blue to lavender, makes a strong showing in the SS26 collections, but pastel yellow is the biggest “winner” in this year relative to past years, mostly in classically feminine and preppy contexts.

We see it paired with other pastels:

![](https://substackcdn.com/image/fetch/$s_!qQPN!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b32620c-795d-4566-97c7-fee064b6c33b_960x1440.jpeg)![](https://substackcdn.com/image/fetch/$s_!coow!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2ffd2ad-221e-46d8-a9ed-1071498b9b2d_960x1440.jpeg)![](https://substackcdn.com/image/fetch/$s_!EKUA!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F94e127b1-1297-4e1f-9bf4-c79f6b63440a_960x1440.jpeg)![](https://substackcdn.com/image/fetch/$s_!rOQo!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa80695c6-d198-4da7-bb06-3ed8084b670d_960x1440.jpeg)![](https://substackcdn.com/image/fetch/$s_!oday!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff5cb5fec-85d1-45a2-86bf-75be936795d1_960x1440.jpeg)![](https://substackcdn.com/image/fetch/$s_!Vp-u!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5516d8f6-f920-40ca-8583-80078f9623d4_960x1440.jpeg)

Chloe, Rabanne, Simone Rocha, Christian Dior, Sanderlak, Rag \& Bone, Mithridate

balanced with neutrals:

![](https://substackcdn.com/image/fetch/$s_!4JJk!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F01c6a98b-1724-4bfb-9e46-c5e77c39354f_960x1440.jpeg)![](https://substackcdn.com/image/fetch/$s_!RCy9!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F97b68be1-4369-4d3e-82fa-9edb8c4e4b6c_960x1440.jpeg)![](https://substackcdn.com/image/fetch/$s_!DuWK!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbc119abd-c15f-454a-b584-a0c8457737f6_960x1440.jpeg)![](https://substackcdn.com/image/fetch/$s_!5M1l!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F965de73e-21f1-439e-a3fd-b4c9829a3c99_960x1440.jpeg)![](https://substackcdn.com/image/fetch/$s_!pIFB!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7968385a-fac8-47f4-9ca1-d369259b3133_960x1440.jpeg)![](https://substackcdn.com/image/fetch/$s_!e8TZ!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F93537bed-043a-4137-8f07-348fcd8cf646_960x1440.jpeg)![](https://substackcdn.com/image/fetch/$s_!89ZY!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8d567108-ce29-4280-a74a-e0e003e561e4_960x1440.jpeg)![](https://substackcdn.com/image/fetch/$s_!Rd1N!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb12b5083-b52a-40fc-843a-c60959b4d0ad_960x1440.jpeg)![](https://substackcdn.com/image/fetch/$s_!AcJz!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6110ac50-bf5b-48e0-ace8-91c47694ee32_960x1440.jpeg)

Kallmeyer, Acne Studios, Bottega Veneta, Abra, Loewe, McQueen, Eckhaus Latta, Veronique Leroy, MM6 Maison Margiela

complemented with pops of color:

![](https://substackcdn.com/image/fetch/$s_!lYcb!,w_720,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F32b09b66-e876-4119-b90f-a3c34768780c_960x1440.jpeg)![](https://substackcdn.com/image/fetch/$s_!25Nu!,w_720,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc4b2b292-efa8-467d-b7c1-e1469c374cf3_960x1440.jpeg)![](https://substackcdn.com/image/fetch/$s_!nNRB!,w_720,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F08545b00-3b2b-4c8a-8fca-45f88c7c0dbf_960x1440.jpeg)![](https://substackcdn.com/image/fetch/$s_!ZR9N!,w_720,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5130a565-7485-4137-aa21-3b49fe0d7e96_960x1440.jpeg)

Rodarte, Stefan Cooke, Versace, MSGM

or all by itself in a head\-to\-toe flow:

![](https://substackcdn.com/image/fetch/$s_!UlR0!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F37a4c68c-48e7-4ac3-8b8c-cab30c340695_960x1440.jpeg)![](https://substackcdn.com/image/fetch/$s_!VQZs!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Facd2b789-91a2-4f3e-ab08-161a64dad21c_960x1440.jpeg)![](https://substackcdn.com/image/fetch/$s_!6jiN!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F828c272a-f401-415a-8579-4d32a172b518_960x1440.jpeg)![](https://substackcdn.com/image/fetch/$s_!VNgO!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe4e89fc8-4a21-4174-8465-e6753f0e8dcb_960x1440.jpeg)![](https://substackcdn.com/image/fetch/$s_!mHA4!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F099b5b97-3379-4303-b797-4b414b5e05e0_960x1440.jpeg)![](https://substackcdn.com/image/fetch/$s_!6S8n!,w_474,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F65c753bb-d4ad-4b76-984a-56129eb5f06a_960x1440.jpeg)

Christian Cowan, Huishan Zhang, Givenchy, Sportmax, Emilia Wickstead, Fendi

Pastel yellow is peaceful, restful, hopeful.

It’s not the abstract, contemplative, distant\-skies calm of pale blue (which was my pick for 2023’s color). Pastel yellow belongs to the earth; its peacefulness is material. The comfort and contentment of butter and flowers and sunshine. Mellow yellow.

Unlike the spiky freshness of spring green (my pick for [2024](https://sarahconstantin.substack.com/p/2024-color-trends)) or, even more so, the frenzied fun of hot pink (my pick for [2025](https://sarahconstantin.substack.com/p/2025-color-trends)), pastel yellow isn’t trying to be even a little bit edgy or intense. It’s soft and slow\-paced; it lends itself easily to touchable textures and a buttery, sunlit feeling of indulgence in the senses.

### Looking Forward and Back

Since I’ve been doing these fashion stats projects, I’ve used the “color of the year” as a sort of theme to inspire me in the year to come.[1](https://sarahconstantin.substack.com/p/ss26-color-stats#footnote-1-176139290)

**2023: Sky Blue/Spaciousness**

This was a year when I was kind of coming out of a turbulent phase of being dissatisfied with the work and family responsibilities of a thirtysomething, and just startingto get into a set of habits that were more functional and “wholesome”. My goal was to “make space” — have enough time for myself as well as have a calmer outlook on life.

That basically worked, I think. If you look over my 2023 blog posts, that was when I was starting to get more interested in LLMs and in neurotech. In my work life, I was learning a bunch of new skills on the “business side” (marketing, financial analysis, sales process optimization, etc) and starting to get the hang of adding value, and at home, things got into more of a rhythm as my older kid started school and learned to read.

**2024: Spring Green/Freshness**

My theme for 2024 was about “[poking my head out from under a rock”](https://sarahconstantin.substack.com/p/2024-color-trends), trying new things, looking for aliveness and newness.

Well, I did that, pretty much: full\-time writing/consulting was new to me, as was some of the playing around with LLM wrappers and finetunes I tried out, and scientific program management (as a fellow at Renaissance Philanthropy.)

**2025: Hot Pink/Fun**

My theme for 2025 was [“fun”](https://sarahconstantin.substack.com/p/2025-color-trends), to match the raucous energy of hot pink.

Now, I really don’t have a wild\-party life these days, and I also got pregnant with kid \#3, so “fun” in that sense wasn’t really the most practical for me. But I did have fun in the sense of getting opportunities to travel and time for personal projects (during my freelancing/consulting periods), and the biggest positive step change in my overall mood I’ve ever experienced (thanks to an effective antidepressant.)

Seriously, check out this [PANAS score](https://en.wikipedia.org/wiki/Positive_and_Negative_Affect_Schedule) graph and how negative affect just plummets in spring 2025 and mostly stays way down from the previous baseline. If not “fun” exactly, then definitely 2025 was a banner year for *happiness*.

[![](https://substackcdn.com/image/fetch/$s_!Fzsp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0b00d4f6-264d-4c22-b5ff-35c112f7b4d7_1446x904.png)](https://substackcdn.com/image/fetch/$s_!Fzsp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0b00d4f6-264d-4c22-b5ff-35c112f7b4d7_1446x904.png)

**2026: Pastel Yellow/Optimism**

I don’t expect 2026 to be especially slow, easy, or mellow, what with a new baby and the prospect of some new work adventures. And I don’t particularly like the “mentally escape from the troubled state of the world” theme.

So I think I want to emphasize the *cheerful* side of pastel yellow, and its groundedness; taking small, steady, real steps in a positive direction. Adding up to something. Finding enjoyment along the way.

[1](https://sarahconstantin.substack.com/p/ss26-color-stats#footnote-anchor-1-176139290)Do I actually *wear* the color in question? Not necessarily; for the past several years my “top pick” hasn’t been a color that flatters me.