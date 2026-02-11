# The Health Risks of Gas Stoves

*How bad are they really?*

Published: 2023-01-23
Source: https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves

---

[![](https://substackcdn.com/image/fetch/$s_!S7KM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff4940bbf-4d14-4a69-88a7-de973018de46_2121x1414.jpeg)](https://substackcdn.com/image/fetch/$s_!S7KM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff4940bbf-4d14-4a69-88a7-de973018de46_2121x1414.jpeg)

Gas stoves are in the Discourse lately, because of a recent announcement that the US Consumer Product Safety Commission is [considering a ban.](https://www.bloomberg.com/news/articles/2023-01-09/us-safety-agency-to-consider-ban-on-gas-stoves-amid-health-fears)

Regardless of the policy issue around banning things, are gas stoves actually meaningfully more dangerous than electric stoves? What are the risks?

### **That One Study**

A lot of the discussion around gas stoves has centered around last week’s Gruenwald et al study[1](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-1-97085053), which claims that 12\.7% of childhood asthma in the US is due to gas stove use.

So, let’s examine it.

First of all, there’s a clear agenda here. One of the authors (Talor Gruenwald) works at [Rewiring America](https://www.rewiringamerica.org/), a nonprofit promoting electrification in buildings to reduce greenhouse gas emissions. “Gas stoves are unhealthy” is definitely an idea that helps the environmentalist cause and is consciously being promoted for that purpose.

The other authors are academic and governmental public health experts, which basically means their expertise is in analyzing data produced by other researchers, not in the biology of asthma itself.

The study uses 10 previously published studies to come up with an association between gas stove use and higher risk of asthma, with an odds ratio of 1\.34\. (That’s not a huge effect size in general, but might still be worth paying attention to.)

Then they calculate the population attributable fraction (PAF) to get their 12\.7% figure.

What is a PAF?

You count up four categories of cases:

* A.) gas stove, no asthma
* B.) gas stove, asthma
* C.) no gas stove, no asthma
* D.) no gas stove, asthma

The total number of asthma cases is B \+ D.

B/(B\+D) is the fraction of asthma cases that had a gas stove. That’s an upper bound for the fraction of asthma cases that can be attributed to gas stoves, but it’s an overestimate, because not everyone with a gas stove gets asthma. Some people with gas stoves who have asthma would still have gotten asthma without the stove.

The total number of people without gas stoves is C \+ D. The rate of asthma among gas\-stove\-less people is D/(C \+ D).

The number of asthma cases *attributable* to gas stoves is then just B \- B\* (D/(C\+D)). We subtract the expected number of asthma cases that would exist even in the absence of gas stoves.

Then you get

B \* (1\- (D/(C\+D))/(B\+D)

as our population attributable fraction.

In fact, the authors used a more complicated approach than this. They generated a distribution of gas stove exposure for each state (because, of course, you only have a *survey sample* telling you how common gas stoves are) and a distribution of possible odds ratios based on the error bars in the original studies. But it’s basically the same figure being estimated as the simple computation.

The thing to keep in mind here is that this is a reanalysis of existing data. It’s only as good or bad as the original research it’s based on, and associational studies are vulnerable to confounders. (Does something else — like living in older buildings —cause both asthma and gas stove use?) It’s not mechanistic (it doesn’t say *how* gas stoves cause asthma) and it’s not directly causal (there’s no experiment or natural experiment here).

Honestly, it doesn’t tell us very much by itself, one way or another. This is an extremely short paper that could have been a blog post. To understand how seriously to take gas stove risk we’ll have to hit the literature.

### **Gas Stoves And Health Risks: Associational Studies**

#### Aggregate Summary

Out of 23 studies I found in a Google Scholar search for “gas stove risks” that examined associations between any medical condition and use of gas stoves, 11 found any kind of significant association between gas stove use and any medical condition.

None of these positive results came from studies that controlled for confounders related to potential air quality problems that *didn’t* come from gas stoves, like outdoor pollution or home age. All the studies that *did* include environmental controls found no effect of gas stoves on any disease.

Many of the studies finding that gas stoves were a significant risk factor had other methodological issues that further weaken the case against gas stoves:

* small sample from an extraordinarily asthmatic population
* looks at “gas and coal” stoves together as one variable (coal stoves are more\-polluting)
* only finds risks associated with gas stoves *used for heat* (i.e. not ventilated to the outside)

#### The Studies

*Schencker et al, 1983*[2](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-2-97085053)

This is a study of 4071 children in a rural and coal\-mining region of Pennsylvania. There was no significant association between gas stove use and respiratory illness after correcting for socioeconomic status. (Gas stoves were associated with lower socioeconomic status in this sample.) Respiratory disease risk factors included maternal smoking and family history of respiratory disease.

*Ware et al, 1984*[3](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-3-97085053)

This is a study of 10,106 white children living in 6 US cities. There was no significant association between any respiratory disease/symptom and gas stove usage. Maternal smoking was significantly associated with cough, wheeze, and respiratory illness generally (OR \= 1\.18\-1\.26\) after controlling for parental respiratory illness.

*Vedal et al, 1984*[4](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-4-97085053)

This is a study of 4000 white children in Pennsylvania, living near coal power plants, who got respiratory flow tests.

Children of smoking parents had significantly worse respiratory function. So did children with lower socioeconomic status. Gas stove usage, however, was not associated with worse respiratory function.

*Dekker et al, 1991*[5](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-5-97085053)

This is a study of 17,962 Canadian children, mostly white. Gas cooking was significantly associated with current asthma (OR \= 2\.04, p \< 0\.05\) as well as smokers in the home (OR \= 1\.42\) and dampness (OR \= 1\.61\).

These elevated risks were computed after adjusting for child age, sex, race, parental education, region, and household crowding, but not building age, outdoor pollution, or urban/rural location.

*Infante\-Rivard et al, 1993*[6](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-6-97085053)

This is a case\-control study of 925 preschool children from Montreal, Canada, which found no significant effect of having a gas stove in the home on childhood asthma prevalence. Nitrogen dioxide levels in the home above 15 ppb were, however, associated with a significant odds ratio of 10\.54 of asthma. Other significant risk factors included having a mother who was a heavy smoker, having an electric heating system in the home, having a family history of asthma, or having allergies or eczema.

*Pershagen et al, 1995*[7](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-7-97085053)

This is a case\-control study of 547 children under age 4 in Stockholm. The risk of wheezing bronchitis was associated with outdoor levels of nitrogen dioxide (levels \>70 ug/m^3 were associated with an OR of 2\.7 relative to \<35 ug/m^3\) in girls but there was no significant association in boys.

Having a gas stove in the house had an association with wheezing bronchitis in girls after adjusting for asthma heredity and maternal smoking, but not after also adjusting for outdoor nitrogen dioxide levels.

I think this should count as a negative result; gas stove usage is not associated with respiratory disease *independent of outdoor air pollution*.

*Jarvis et al, 1996*[8](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-8-97085053)

This is a study of 1159 adults in East Anglia, UK. Women, but not men, who reported mainly cooking with gas were significantly (OR \= 2\.07\) more likely to wheeze, and significantly (OR \= 2\.62\) more likely to have asthma, than non\-gas\-stove users. This effect was not found for men.

About half the sample used gas stoves, which were more common in older homes and twice as common in houses than apartments; there was no association between gas stove usage and socioeconomic status.

Gas stove cooking stayed associated with asthma and respiratory problems in women even after controlling for age, smoking, town of residence, social class, age of home, and type of home.

The strong sex difference may be due to the fact that women cook more than men, and nitrogen dioxide concentrations from gas stoves are highest in the kitchen.

*Maier et al, 1997*[9](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-9-97085053)

This is a survey of parents of 925 Seattle children. 11% (an unusually high rate) reported a diagnosis of asthma.

Asthma was associated significantly with black race, allergies, parental asthma, secondhand smoke, and household water damage, but not gas stove use. Another negative result.

*Garett et al, 1998*[10](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-10-97085053)

One study of 80 households in Australia included 148 children, 53 of whom had asthma. (This is a small sample with a *crazy* high base rate; 36% of the kids in this study had asthma, compared to about 6% in the US overall.)

Nitrogen dioxide levels were low on average (median 11\.6 ug/m^3\), and were *not* associated with a significant increase in asthma risk, but gas stove usage was associated with a whopping 2\.77 crude OR (odds ratio) of asthma risk.

OR’s were still well over 2\.0 when adjusting for various things such as parental asthma, parental allergy, child sex, and nitrogen dioxide levels elsewhere in the house, but no adjustments were made for socioeconomic or racial demographics, or characteristics of the homes (location, building age, etc.).

This is an unconvincing study. It has a tiny sample with a weirdly asthmatic population living in one county in Australia.

*Dow et al, 1999*[11](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-11-97085053)

In a study of 4798 older adults living in Bristol, UK, gas stove use had no significant association with any respiratory symptom across the sample, but women who used a gas range had a slightly elevated (OR \= 1\.36, p\<0\.05\) risk of wheeze.

*Hoelscher et al, 2000*[12](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-12-97085053)

This is a study of 2198 East German children which found no significant association between gas stove use and asthma, bronchitis, rhinitis, wheezing, shortness of breath, cough, or acute infections, but it was associated with higher rates of cough without cold (OR \= 1\.68, p \= 0\.004\) and cough in the morning (OR \= 1\.58, p\<0\.001\).

Gas stove use was more common in houses built before 1970, in damp or moldy houses, and in households with less\-educated parents; the study didn’t report the association between gas stove use and respiratory symptoms after controlling for these features.

*Lanphear et al, 2001*[13](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-13-97085053)

This is a study of 8257 children from the nationally representative NHANES study. Using gas stoves *for heat* was a significant risk factor for asthma (OR \= 1\.8, p \= 0\.04\). Note that using a stove for heat, a more common practice in poorer families, means *not* venting to the outside.

Other significant risk factors included black race (OR \= 1\.6\), mother who smoked both prenatally and postnatally (OR \= 1\.7\), dog in home (OR \= 1\.6\), given up a pet because of allergies (OR \= 24\.7\), hay fever (OR \= 5\.4\), and biological parent with asthma or hay fever (OR \= 2\.2\).

*Emenius et al, 2003*[14](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-14-97085053)

In a case\-control sample of 294 children, half with wheezing before age 2, the other half matched controls from the same birth cohort, there was no significant association between gas stove use and wheezing. Buildings newer than 1940, compared to buildings built before 1940, were associated with higher rates of wheezing.

*Belanger et al, 2003*[15](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-15-97085053)

In a cohort of 849 infants in the northeastern US with an asthmatic sibling, infant wheezing was not significantly associated with gas stove use, but infant persistent cough was (OR \= 1\.5\). Other risk factors included wood stoves (OR \= 2\.09\), mold/mildew (OR \= 1\.53\-1\.91\) and nitrogen dioxide over 10 ppb (OR \= 1\.29\).

*Wong et al, 2004*[16](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-16-97085053)

This study looks at 426 preschool children from two housing estates in Hong Kong.

26\.1% of the children had some kind of respiratory illness (nasal allergies, asthma, bronchitis, sinusitis, and pneumonia) — 89% of these, unsurprisingly, were allergic rhinitis (which generally affects 10\-20% of children in the US population.)

All the homes had gas stoves. The frequency of gas stove cooking (1, 2, or 3 meals a day) was significantly associated with childhood respiratory disease with an odds ratio of 2\.19 for 3 gas\-stove\-cooked meals a day vs. 1 meal — but only after controlling for various confounders including the home location. Respiratory disease was much more common in the more\-polluted Estate A (OR \= 4\.49\) and heavy gas stove use only was associated with elevated respiratory disease risk in the less\-polluted Estate B.

This study points weakly towards the “gas stoves bad” thesis — more gas stove cooking increases risk of childhood respiratory diseases. But it includes relatively harmless allergies, and gas stove cooking is still much less of a big deal than air pollution levels overall.

*Liebhart et al, 2007*[17](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-17-97085053)

This is a study of 16,238 children and adults in 11 regions of Poland.

Asthma in children was significantly associated with a family history of asthma (OR \= 3\.42\), male sex (OR \= 1\.83\), high traffic (OR \= 1\.43\), and outdoor black smoke particles in the air (OR \= 1\.51\) but not with gas stoves or even common risk factors like secondhand smoke or damp (moldy) houses.

This is a negative result; gas stoves didn’t seem to matter, while outdoor air pollution did.

*Ramanakumar et al, 2007*[18](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-18-97085053)

In a case\-control study of 2746 adults in Montreal, Canada, with and without lung cancer, women (but not men) had an elevated risk of lung cancer if they had been exposed to any “traditional heating fuels” (wood or coal stoves in the living space) or “traditional cooking fuels” (coal or gas stoves). The odds ratio for the latter was 1\.6\.

*Kattan et al, 2007*[19](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-19-97085053)

In 1528 inner\-city children from 8 US cities, mostly black and poor, most children had gas stoves in the home (88%) and gas stoves were significantly associated with higher nitrogen dioxide concentrations (31\.4 ppb vs 15\.9 ppb). Nitrogen dioxide concentrations were significantly higher in winter, presumably because windows are open less often. High NO2 levels were significantly associated with higher risk of asthma symptoms (OR \= 1\.75\) for children with no positive allergy tests, but not significant in children with allergy. This study did not directly measure the effect of gas stoves on asthma, however, nor did it control for other features of the home like building age.

*Carlsten et al, 2011*[20](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-20-97085053)

In a study of 545 children in Vancouver and Winnipeg, Canada, with family history of asthma or allergy, gas stoves had no significant association with asthma at age 7\. Dog ownership was associated with asthma (OR \= 2\.7\) and so was atopy (OR \= 5\.5\).

*Svendsen et al, 2018*[21](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-21-97085053)

In a study of 1878 children from El Paso, Texas, mostly Hispanic, there was no significant association between gas stove use and asthma incidence. Wood stoves, fireplaces, central air, pesticides, ants, and spiders were all associated with increased asthma risk.

This study seems to *report* a positive association between asthma and gas stove use in the conclusions, but the data tables only report % of gas stove use in various disease categories and show slightly more common gas stove use among those without asthma and those with.

*Norbaeck et al, 2018*[22](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-22-97085053)

In a study of 36,541 young parents across 6 major cities in China, given questionnaires on medical symptoms, gas cooking (compared to electric) was associated with higher rates of eye symptoms (OR \=1\.44\), throat symptoms (OR \= 1\.29\), headache (OR \= 1\.55\), and fatigue (OR \= 1\.27\). When stratified by sex, only women had significantly higher symptom rates from gas stoves.

Coal or wood stoves, living near a highway, or buying furniture were also associated with higher risk of symptoms, as were pests and cleaning every day. Gas stoves were *not* associated with new construction in this sample, and older construction (homes built before 1991\) was not associated with any symptom.

*Zhang et al, 2021*[23](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-23-97085053)

This one is about birth defects in Lanzhou, China. Out of 10,190 births between 2010\-2012, 2\.6% had birth defects. The rate of birth defects was significantly higher (OR \= 2\.66\) for those born to mothers using biomass stoves, and also significantly higher (OR \= 1\.90\) for those born to mothers using electromagnetic stoves (aka induction stoves), compared to gas stoves. Electric stoves had no significant risk association relative to gas.

Unsurprisingly, birth defects were more common for children with siblings who had birth defects, poorer and less educated parents, mothers who smoked during pregnancy, and mothers who didn’t use ventilation while cooking. After adjusting for all these factors, as well as folic acid supplementation and use of hot oil while cooking, we get the 2\.66 adjusted OR for biomass (aka wood) stoves and the 1\.90 adjusted OR for electromagnetic stoves.

This is a large study, though it’s in a single location and might not translate as well to the US, and it goes *against* the “electric safer than gas” narrative — electric stoves are no more likely to cause birth defects than gas, though the usual high\-polluting suspects (wood stoves and tobacco smoke) are quite risky, and induction stoves actually seem to be *worse* than gas!

*Zhao et al, 2022*[24](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-24-97085053)

This is another Chinese study of birth defects, this one focused on congenital heart disease and based on 1397 births in Xi’an, China, from 2014\-2016\.

After adjusting for confounders, electromagnetic (induction) stoves were associated with an OR of congenital heart disease of 2\.89 relative to gas, coal stoves were associated with an OR of 3\.94 relative to gas, and wood stoves were associated with an OR of 6\.74 relative to gas. Cooking frequency was also associated with large increases in congenital heart disease risk for all types of stove including gas. Electric stoves weren’t studied.

Once again, in China, wood stoves are very bad for birth defect risk, but induction stoves are also worse than gas!

### Conclusions

1. Gas stove usage is not consistently associated with childhood asthma or respiratory disease generally; there are numerous negative results and most of the positive results are confounded.
2. Even those studies that found an effect had fairly small effect sizes (almost all ORs under 2\.0\).
3. High nitrogen dioxide *is* associated with respiratory disease. Using a gas stove without ventilation, or spending a lot of time cooking on a gas stove, might be a risk factor for respiratory disease even if gas stoves overall are not.
4. Induction stoves may even have health *downsides* relative to gas stoves— they’re associated with higher rates of birth defects in China.

[1](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-anchor-1-97085053)Gruenwald, Talor, et al. "Population Attributable Fraction of Gas Stoves and Childhood Asthma in the United States." *International Journal of Environmental Research and Public Health* 20\.1 (2023\): 75\.

[2](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-anchor-2-97085053)Schenker, Marc B., J. M. Samet, and F. E. Speizer. "Risk factors for childhood respiratory disease: the effect of host factors and home environmental exposures." *American Review of Respiratory Disease* 128\.6 (1983\): 1038\-1043\.

[3](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-anchor-3-97085053)Ware, J. H., et al. "Passive smoking, gas cooking, and respiratory health of children living in six cities." *American Review of Respiratory Disease* 129\.3 (1984\): 366\-374\.

[4](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-anchor-4-97085053)Vedal, Sverre, et al. "Risk factors for childhood respiratory disease: analysis of pulmonary function." *American Review of Respiratory Disease* 130\.2 (1984\): 187\-192\.

[5](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-anchor-5-97085053)Dekker, Carolien, et al. "Childhood asthma and the indoor environment." *Chest* 100\.4 (1991\): 922\-926\.

[6](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-anchor-6-97085053)Infante\-Rivard, Claire. "Childhood asthma and indoor environmental risk factors." *American Journal of Epidemiology* 137\.8 (1993\): 834\-844\.

[7](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-anchor-7-97085053)PERSHAGEN, GÖRAN, et al. "Air pollution involving nitrogen dioxide exposure and wheezing bronchitis in children." *International journal of epidemiology* 24\.6 (1995\): 1147\-1153\.

[8](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-anchor-8-97085053)Jarvis, Deborah, et al. "Association of respiratory symptoms and lung function in young adults with use of domestic gas appliances." *The Lancet* 347\.8999 (1996\): 426\-431\.

[9](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-anchor-9-97085053)Maier, William C., et al. "Indoor risk factors for asthma and wheezing among Seattle school children." *Environmental Health Perspectives* 105\.2 (1997\): 208\-214\.

[10](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-anchor-10-97085053)Garrett, Maria H., et al. "Respiratory symptoms in children and indoor exposure to nitrogen dioxide and gas stoves." *American Journal of Respiratory and Critical Care Medicine* 158\.3 (1998\): 891\-895\.

[11](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-anchor-11-97085053)Dow, L., et al. "Respiratory symptoms in older people and use of domestic gas appliances." *Thorax* 54\.12 (1999\): 1104\-1106\.

[12](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-anchor-12-97085053)Hölscher, Bernd, et al. "Gas cooking, respiratory health and white blood cell counts in children." *International journal of hygiene and environmental health* 203\.1 (2000\): 29\-37\.

[13](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-anchor-13-97085053)Lanphear, Bruce P., et al. "Residential exposures associated with asthma in US children." *Pediatrics* 107\.3 (2001\): 505\-511\.

[14](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-anchor-14-97085053)Emenius, G., et al. "NO2, as a marker of air pollution, and recurrent wheezing in children: a nested case\-control study within the BAMSE birth cohort." *Occupational and environmental medicine* 60\.11 (2003\): 876\-881\.

[15](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-anchor-15-97085053)Belanger, Kathleen, et al. "Symptoms of wheeze and persistent cough in the first year of life: associations with indoor allergens, air contaminants, and maternal history of asthma." *American journal of epidemiology* 158\.3 (2003\): 195\-202\.

[16](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-anchor-16-97085053)Wong, T. W., et al. "Household gas cooking: a risk factor for respiratory illnesses in preschool children." *Archives of disease in childhood* 89\.7 (2004\): 631\-636\.

[17](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-anchor-17-97085053)Liebhart, J., et al. "Prevalence and risk factors for asthma in Poland: results from the PMSEAD study." *Journal of Investigational Allergology and Clinical Immunology* 17\.6 (2007\): 367\.

[18](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-anchor-18-97085053)Ramanakumar, Agnihotram V., Marie\-Elise Parent, and Jack Siemiatycki. "Risk of lung cancer from residential heating and cooking fuels in Montreal, Canada." *American journal of epidemiology* 165\.6 (2007\): 634\-642\.

[19](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-anchor-19-97085053)Kattan, Meyer, et al. "Health effects of indoor nitrogen dioxide and passive smoking on urban asthmatic children." *Journal of Allergy and Clinical Immunology* 120\.3 (2007\): 618\-624\.

[20](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-anchor-20-97085053)Carlsten, C., et al. "Combined exposure to dog and indoor pollution: incident asthma in a high\-risk birth cohort." *European Respiratory Journal* 37\.2 (2011\): 324\-330\.

[21](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-anchor-21-97085053)Svendsen, Erik R., Melissa Gonzales, and Adwoa Commodore. "The role of the indoor environment: Residential determinants of allergy, asthma and pulmonary function in children from a US\-Mexico border community." *Science of the Total Environment* 616 (2018\): 1513\-1523\.

[22](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-anchor-22-97085053)Norbäck, Dan, et al. "Home environment and health: domestic risk factors for rhinitis, throat symptoms and non\-respiratory symptoms among adults across China." *Science of The Total Environment* 681 (2019\): 320\-330\.

[23](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-anchor-23-97085053)Zhang, Yaqun, et al. "Cooking stoves and risk of birth defects in urban China." *Environmental research* 194 (2021\): 110731\.

[24](https://sarahconstantin.substack.com/p/the-health-risks-of-gas-stoves#footnote-anchor-24-97085053)Zhao, Doudou, et al. "Cooking stoves and risk of congenital heart disease in Northwest China: A case\-control study." *Science of The Total Environment* 816 (2022\): 151564\.