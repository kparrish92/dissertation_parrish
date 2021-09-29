Experiment 2: The production of L3 vowels in absolute beginners
================

The purpose of experiment 1 was to evaluate VOT in beginning L3 learners
in each of their known languages and their new language to determine
cross-linguistic interactions. Experiment 2 has the same agenda, but
instead of VOT, vowels are examined to determine how cross-linguistic
interactions may occur. Ideally, an analysis of the same tokens as
experiment 1 will be used for experiment 2.

# Notes and troubles

This is an overview of my initial proposal for experiment 2.

The central purpose of experiment 2 is to evaluate the production of the
L3 vowel space of absolute L3 beginners (i.e. sequential bilinguals
after their first exposure to a third language), and to determine
whether the L3 vowel space is more L1 or L2 like. The justification for
this experiment is to provide more robust evidence that may be used in
the evaluation of the predictions of L3 models. Long-form justifications
and previous literature will be covered in the formal dissertation
proposal.

### Research Question

Will absolute beginners produce vowels in a third language at first
exposure more like (a) L1 vowels, (b) L2 vowels, or (3) L3 vowels that
they are exposed to in the experiment?

## Methods

<div class="figure">

<img src="../sim_data/plots/questionnaire.png" alt="Questionnaire used in the pilot" width="2266" />
<p class="caption">
Questionnaire used in the pilot
</p>

</div>

<div class="figure">

<img src="../sim_data/plots/questionnaire2.png" alt="Questionnaire used in the pilot" width="2229" />
<p class="caption">
Questionnaire used in the pilot
</p>

</div>

Goal: Elicit production of L1, L2 and L3 words containing copmparable
vowels for analysis.

**These elicitation methods are flexible, since they’re not incredibly
driven by theory - I am not opposed to using a carrier sentence in each
language if I can avoid co-articulation effects and if it seems
reasonable that the speakers could learn an L3 carrier sentence**

### Task: Shadowing Task

<img src="../sim_data/plots/shadowing_example.png" width="2253" />

### Task: Elicited Production task

Spanish-English bilinguals will produce word lists in isolation in their
L1, L2 and an L3 that they do not know. For the L3, they will complete a
shadowing task (training), in which they will listen L3 words one at a
time and repeat them aloud. Following the shadowing task, the
participants will then complete 3 elicited production tasks in their L1
and L2 (the order will be counter-balanced), and all participants will
finish with the EPT in the L3.

<img src="../sim_data/plots/ept_example.png" width="2268" />

Tokens will be extracted from these productions an analyzed in PRAAT.

**Undecided**

Give all participants the same L3, or divide it in some way. If many L3s
were given then it could be added to the model to see whether language
given makes a difference in the use of L1 or L2. But would I need 5x as
many experiments?

If just one language: German

-   The German vowel space is huge
    <a href="https://en.wikipedia.org/wiki/Standard_German_phonology#CITEREFDudenredaktionKleinerKnöbl2015" class="uri">https://en.wikipedia.org/wiki/Standard_German_phonology#CITEREFDudenredaktionKleinerKnöbl2015</a>

-   new vowel sounds \*

Will L3 learners assimilate L3 vowel sounds to L1 or L2 sounds?

L1 /e/, L2 /e/, L3 /e/, L3 /novel/

German:

### Participants

200 total participants will take part in the experiment. The
participants will be Spanish-English bilinguals, with both English L1 (n
= 100), and Spanish L1 (n = 100).

### Materials

Stimuli:

4 repetitions of each vowel in each language. 20x words per language.

### Analysis

The data were analyzed using two Bayesian generalized multilevel
regression models in R. The models were fit using the `rstanglmer`
function in the `rstanarm` package.

The models’ outcome variable was F1 and F2 respectively and was measured
in Hertz. In each mode, the formant was modeled as a function of vowel,
language, and the vowel and language interaction. The categorical
variables of language and vowel were both dummy coded. The random
effects structure included by-participant random intercepts and slopes
for language and vowel. **The priors were the `rstanglmer` function
default of weakly informative priors.** Due to the fact that the
research question of the present study aims to establish practical
equivalence between languages, the region of practical equivalence was
set to a medium effect size (Cohen’s &lt; .5). As a result, if the
distribution of the posterior parameter estimates is less than .5
standard deviations away from the reference value, that distribution
would fall inside the region of practical equivalence, and would be
assumed to be equivalent.

### Materials

## Simulated Data and results

### The Simulated Data

Data were simulated in R using the `rnorm` function for each vowel for
both the first and second formant, in each the L1, L2 and L3 for 100
participants, with each vowel being repeated 4 times. As a result, 20
tokens (4 repititions x 5 vowels) were simulated per language for 100
total participants, totaling 2000 observations per language (100
participants x 20 tokens). Thus, in total, the simulated dataset
contained 6000 observations for both F1 and F2. The mean formant values
for F1 and F2 were adapted from the monolingual values reported in
Bradlow (1995), and the L3 values were simulated to closely resemble the
L2 values in order to demonstrate what would be interpreted as L2-like
L3 vowel productions in the statistical models. The script used to
simulate the dataset can be found under `scripts` and is titled
`01_simdata.R`.

### The Simulated Results

The design of the present study sets L3 as the reference level in a
bayesian generalized linear regression model. As a result, the
interpretation of the forest plots is relatively straight forward; if a
distribution of plausible parameter estimates falls entirely within the
determined region of practical equivalence (ROPE; the dashed, vertical
lines on the forest plot), then it will be taken as evidence for the use
of L1 or L2 phonology at the first exposure to the L3. The results of
the simulated bayesian analyses showed evidence of practical equivalence
between the L2 and L3 for all vowels in F1, and a similar trend, though
it appears less clear, in the F2 model.

The figures are forest plots of the parameter estimates of each vowel x
language interaction from the Bayesian regression model. The reference
level for language was L3 and /a/ for vowel.

|                   |        mean |      mcse |       sd |         10% |         50% |         90% | n\_eff |     Rhat |
|:------------------|------------:|----------:|---------:|------------:|------------:|------------:|-------:|---------:|
| (Intercept)       |  626.883771 | 0.0600036 | 2.542555 |  623.669823 |  626.864009 |  630.189368 |   1796 | 1.001730 |
| languagel1        |  154.048201 | 0.0806336 | 3.556170 |  149.477464 |  154.028695 |  158.633228 |   1945 | 1.001318 |
| languagel2        |    9.001054 | 0.0809350 | 3.522648 |    4.467497 |    8.989771 |   13.524665 |   1894 | 1.001644 |
| vowele            | -206.932682 | 0.0740890 | 3.543371 | -211.467077 | -206.880170 | -202.509388 |   2287 | 1.001068 |
| voweli            | -368.981921 | 0.0727442 | 3.583411 | -373.524034 | -369.017861 | -364.385027 |   2427 | 1.000541 |
| vowelo            | -155.772187 | 0.0751139 | 3.618171 | -160.487173 | -155.775150 | -151.201372 |   2320 | 1.000592 |
| vowelu            | -307.080678 | 0.0714725 | 3.611789 | -311.738174 | -307.046869 | -302.476818 |   2554 | 1.001104 |
| languagel1:vowele | -116.587258 | 0.0996713 | 4.991129 | -122.964438 | -116.567444 | -110.187707 |   2508 | 1.000573 |
| languagel2:vowele |   -3.428371 | 0.1038241 | 4.998551 |   -9.689918 |   -3.411964 |    3.072472 |   2318 | 1.000215 |
| languagel1:voweli | -125.711035 | 0.0988099 | 4.998842 | -132.104786 | -125.753088 | -119.376112 |   2559 | 1.000906 |
| languagel2:voweli |   -3.683557 | 0.0992193 | 5.101428 |  -10.149787 |   -3.604455 |    2.759617 |   2644 | 1.000366 |
| languagel1:vowelo | -167.027215 | 0.0984998 | 5.088994 | -173.455541 | -167.102394 | -160.586584 |   2669 | 1.000295 |
| languagel2:vowelo |   -7.737827 | 0.1032165 | 5.020612 |  -14.187380 |   -7.660635 |   -1.381260 |   2366 | 1.001338 |
| languagel1:vowelu | -152.276683 | 0.1004567 | 5.094717 | -158.817991 | -152.230761 | -145.778577 |   2572 | 1.001225 |
| languagel2:vowelu |  -12.470140 | 0.0980973 | 4.993016 |  -18.823570 |  -12.444017 |   -5.976336 |   2591 | 1.001323 |

Summary of the F1 model

<img src="../sim_data/plots/f1_forest.png" width="2100" />

|                   |        mean |      mcse |       sd |         10% |         50% |          90% | n\_eff |      Rhat |
|:------------------|------------:|----------:|---------:|------------:|------------:|-------------:|-------:|----------:|
| (Intercept)       | 1337.549651 | 0.0874525 | 4.842924 | 1331.399611 | 1337.572879 | 1343.8035212 |   3067 | 0.9999594 |
| languagel1        | -154.101098 | 0.1243757 | 6.897010 | -162.990756 | -154.100569 | -145.1695653 |   3075 | 0.9998745 |
| languagel2        |   16.789555 | 0.1157789 | 6.846372 |    7.942777 |   16.793484 |   25.6146328 |   3497 | 0.9999727 |
| vowele            |  681.393595 | 0.1126351 | 6.899335 |  672.514195 |  681.506844 |  690.3557746 |   3752 | 0.9994094 |
| voweli            |  922.777552 | 0.1122442 | 6.825494 |  913.868800 |  922.883724 |  931.5302985 |   3698 | 1.0011651 |
| vowelo            | -246.801309 | 0.1099623 | 6.826517 | -255.631554 | -246.712566 | -237.9524200 |   3854 | 1.0000369 |
| vowelu            | -157.189483 | 0.1120610 | 6.926181 | -166.062130 | -157.063191 | -148.2928068 |   3820 | 1.0005742 |
| languagel1:vowele |  -54.488124 | 0.1555199 | 9.572193 |  -66.458562 |  -54.506744 |  -41.7569904 |   3788 | 0.9997046 |
| languagel2:vowele |   -5.420253 | 0.1546193 | 9.663152 |  -17.853931 |   -5.549375 |    6.8920949 |   3906 | 0.9995089 |
| languagel1:voweli | -206.312948 | 0.1619502 | 9.756602 | -218.819289 | -206.319386 | -193.7348977 |   3629 | 0.9996907 |
| languagel2:voweli |  -17.446642 | 0.1522872 | 9.549300 |  -29.605390 |  -17.513071 |   -5.5063070 |   3932 | 1.0003627 |
| languagel1:vowelo |   75.911884 | 0.1558844 | 9.703118 |   63.359610 |   75.772109 |   88.0988882 |   3875 | 1.0000456 |
| languagel2:vowelo |  -13.077439 | 0.1499778 | 9.393698 |  -25.131951 |  -13.179899 |   -0.7514183 |   3923 | 0.9995231 |
| languagel1:vowelu |  -37.617345 | 0.1586248 | 9.672907 |  -50.219004 |  -37.712896 |  -25.0521722 |   3719 | 1.0000097 |
| languagel2:vowelu |  -18.690507 | 0.1526614 | 9.537875 |  -31.019146 |  -18.636209 |   -6.2739405 |   3903 | 1.0009701 |

Summary of the F2 model

<img src="../sim_data/plots/f2_forest.png" width="2325" />
