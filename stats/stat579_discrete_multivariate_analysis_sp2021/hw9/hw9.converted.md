Refer to the calf infection study discussed in lecture. Let [\\(n_3\\)]{.math .inline} denote the number of calves with primary, secondary, and tertiary infections, [\\(n_2\\)]{.math .inline} the number with only primary and secondary infections, [\\(n_1\\)]{.math .inline} the number with only a primary infection, and [\\(n_0\\)]{.math .inline} the number that were never infected. Let [\\(\\theta\\)]{.math .inline} be the probability of a primary infection. Consider a model where the rate of infection is constant. That is, [\\[\\Pr(\\text{tertiary} \| \\text{secondary}, \\text{primary}) = \\Pr(\\text{secondary} \| \\text{primary}) = \\Pr(\\text{primary}).\\]]{.math .display}

# Problem 1

We assume the data model is given by [\\[(n_0,n_1,n_2,n_3) \\sim \\operatorname{MULT}(n, \\pi_0, \\pi_1, \\pi_2, \\pi_3)\\]]{.math .display} where [\\(n_j\\)]{.math .inline} denotes the number of [\\(j\\)]{.math .inline} infections observed and [\\(\\pi_j\\)]{.math .inline} denotes the probability of [\\(j\\)]{.math .inline} infections.

First, we assume [\\(\\Pr(\\text{primary}) = \\theta\\)]{.math .inline}. Then, given that in order for the secondary infection to occur, the primary infection must occur and in order for the tertiary infection to occur, the secondary infection must occur, consider the following.

Under the constant infection rate model, the probability of [\\(0\\)]{.math .inline} infections is the probability that the primary infection does not occur, [\\(\\pi\_{0 0}(\\theta) = 1-\\theta\\)]{.math .inline}. The probability of [\\(1\\)]{.math .inline} infection is the probability the primary infection occurs and the secondary infection does not occur, [\\(\\pi\_{1 0}(\\theta) = \\theta(1-\\theta)\\)]{.math .inline}. The probability of [\\(2\\)]{.math .inline} infections is the probability the primary and secondary infections occur and the tertiary infection does not occur, [\\(\\pi\_{2 0}(\\theta) = \\theta\^2(1-\\theta)\\)]{.math .inline}. Finally, the probability of [\\(3\\)]{.math .inline} infections is the probability the primary, secondary, and tertiary infections occur, [\\(\\pi\_{3 0}(\\theta) = \\theta\^3\\)]{.math .inline}.

Thus, [\\[\\{n_j\\} \\sim \\operatorname{MULT}(n, \\{\\pi\_{j 0}(\\theta)\\}).\\]]{.math .display} Under the null model, the likelihood function is given by [\\[\\operatorname{L}(\\theta) \\propto \\prod\_{j=0}\^{3} \\pi\_{j 0}(\\theta)\^{n_j}\\]]{.math .display} and the kernel of the log-likelihood function is given by [\\[\\begin{aligned} \\operatorname{\\ell}(\\theta) &= \\sum\_{j=0}\^{3} n_j \\log \\pi\_{j 0}(\\theta)\\\\ &= n_0 \\log \\pi\_{0 0}(\\theta) + n_1 \\log \\pi\_{1 0}(\\theta) + n_2 \\log \\pi\_{2 0}(\\theta) + n_3 \\log \\pi\_{3 0}(\\theta)\\\\ &= n_0 \\log (1-\\theta) + n_1 \\log \\theta(1-\\theta) + n_2 \\log \\theta\^2(1-\\theta) + n_3 \\log \\theta\^3\\\\ &= n_0 \\log (1-\\theta) + n_1 \\log \\theta + n_1 \\log (1-\\theta) + 2 n_2 \\log \\theta + n_2 \\log (1-\\theta) + 3 n_3 \\log \\theta\\\\ &= (n_1 + 2 n_2 + 3 n_3) \\log \\theta + (n_0 + n_1 + n_2) \\log (1-\\theta). \\end{aligned}\\]]{.math .display}

The derivative of the log-likelihood is thus given by [\\[\\frac{d \\operatorname{\\ell}}{d \\theta} = \\frac{n_1 + 2 n_2 + 3 n_3}{\\theta} - \\frac{n_0 + n_1 + n_2}{1-\\theta}.\\]]{.math .display}

The ML estimate of [\\(\\theta\\)]{.math .inline} is given by [\\[\\left. \\frac{d \\operatorname{\\ell}}{d \\theta} \\right\\vert\_{\\hat\\theta} = 0.\\]]{.math .display} Solving for [\\(\\hat\\theta\\)]{.math .inline}, we see that [\\[\\frac{n_1 + 2 n_2 + 3 n_3}{\\hat\\theta} = \\frac{n_0 + n_1 + n_2}{1-\\hat\\theta}.\\]]{.math .display} Next, we take the reciprocal of both sides, [\\[\\frac{\\hat\\theta}{n_1 + 2 n_2 + 3 n_3} = \\frac{1-\\hat\\theta}{n_0 + n_1 + n_2}.\\]]{.math .display} Expanding the RHS, we get [\\[\\frac{\\hat\\theta}{n_1 + 2 n_2 + 3 n_3} = \\frac{1}{n_0 + n_1 + n_2}-\\frac{\\hat\\theta}{n_0 + n_1 + n_2}.\\]]{.math .display} Adding [\\(\\frac{\\hat\\theta}{n_0 + n_1 + n_2}\\)]{.math .inline} to both sides, [\\[\\hat\\theta \\left(\\frac{1}{n_1 + 2 n_2 + 3 n_3} + \\frac{1}{n_0 + n_1 + n_2}\\right) = \\frac{1}{n_0 + n_1 + n_2}.\\]]{.math .display} Dividing both sides by the part in parantheses, we get [\\[\\hat\\theta = \\frac{1}{(n_0 + n_1 + n_2) \\left(\\frac{1}{n_1 + 2 n_2 + 3 n_3} + \\frac{1}{n_0 + n_1 + n_2}\\right)},\\]]{.math .display} which simplifies to [\\[\\hat\\theta = \\frac{n_1 + 2 n_2 + 3 n_3}{n_0 + 2 n_1 + 3 n_2 + 3 n_3}.\\]]{.math .display}

# Problem 2

Using the MLE equation, we compute the result using R:

 snugshade
 Highlighting
n0 [<-]{style="color: 0.56,0.35,0.01"} [63]{style="color: 0.00,0.00,0.81"} n1 [<-]{style="color: 0.56,0.35,0.01"} [63]{style="color: 0.00,0.00,0.81"} n2 [<-]{style="color: 0.56,0.35,0.01"} [25]{style="color: 0.00,0.00,0.81"} n3 [<-]{style="color: 0.56,0.35,0.01"} [5]{style="color: 0.00,0.00,0.81"} mle [<-]{style="color: 0.56,0.35,0.01"} (n1 [**+**]{style="color: 0.81,0.36,0.00"} [2]{style="color: 0.00,0.00,0.81"}[*****]{style="color: 0.81,0.36,0.00"}n2 [**+**]{style="color: 0.81,0.36,0.00"} [3]{style="color: 0.00,0.00,0.81"}[*****]{style="color: 0.81,0.36,0.00"}n3)[**/**]{style="color: 0.81,0.36,0.00"}(n0 [**+**]{style="color: 0.81,0.36,0.00"} [2]{style="color: 0.00,0.00,0.81"}[*****]{style="color: 0.81,0.36,0.00"}n1 [**+**]{style="color: 0.81,0.36,0.00"} [3]{style="color: 0.00,0.00,0.81"}[*****]{style="color: 0.81,0.36,0.00"}n2 [**+**]{style="color: 0.81,0.36,0.00"} [3]{style="color: 0.00,0.00,0.81"}[*****]{style="color: 0.81,0.36,0.00"}n3) mle

    ## [1] 0.4587814

Thus, we see that [\\[\\hat\\theta = 0.4587814.\\]]{.math .display} Plugging in this result, [\\[\\vec{\\pi}\_{0}(\\hat\\theta) = (1-\\hat\\theta,\\hat\\theta(1-\\hat\\theta), \\hat\\theta\^2(1-\\hat\\theta),\\hat\\theta\^3)\\]]{.math .display} which we compute with R:

 snugshade
 Highlighting
pihats [<-]{style="color: 0.56,0.35,0.01"} [c]{style="color: 0.13,0.29,0.53"}([1]{style="color: 0.00,0.00,0.81"}[**-**]{style="color: 0.81,0.36,0.00"}mle,mle[*****]{style="color: 0.81,0.36,0.00"}([1]{style="color: 0.00,0.00,0.81"}[**-**]{style="color: 0.81,0.36,0.00"}mle),mle[**\^**]{style="color: 0.81,0.36,0.00"}[2]{style="color: 0.00,0.00,0.81"}[*****]{style="color: 0.81,0.36,0.00"}([1]{style="color: 0.00,0.00,0.81"}[**-**]{style="color: 0.81,0.36,0.00"}mle),mle[**\^**]{style="color: 0.81,0.36,0.00"}[3]{style="color: 0.00,0.00,0.81"}) [round]{style="color: 0.13,0.29,0.53"}(pihats,[digits=]{style="color: 0.13,0.29,0.53"}[3]{style="color: 0.00,0.00,0.81"})

    ## [1] 0.541 0.248 0.114 0.097

Thus, we see that [\\(\\vec{\\pi}\_{0}(\\hat\\theta) = (0.541,0.248,0.114,0.097)\'\\)]{.math .inline}.

# Problem 3

## Part (a)

We use the following R code to compute the observed statistic [\\(G_0\^2\\)]{.math .inline}.

 snugshade
 Highlighting
[*\# below is code for testing a specified multinomial*]{style="color: 0.56,0.35,0.01"} [*\# data is entered as a vector of counts*]{style="color: 0.56,0.35,0.01"} obs [=]{style="color: 0.56,0.35,0.01"} [c]{style="color: 0.13,0.29,0.53"}(n0,n1,n2,n3) n [=]{style="color: 0.56,0.35,0.01"} [sum]{style="color: 0.13,0.29,0.53"}(obs)

[*\# the null model is entered as a vector of hypothesized probabilities*]{style="color: 0.56,0.35,0.01"} [*\# expected counts under the null model are computed as n*prob*]{style="color: 0.56,0.35,0.01"} m [=]{style="color: 0.56,0.35,0.01"} n[*****]{style="color: 0.81,0.36,0.00"}pihats

[*\# log-likelihood ratio test*]{style="color: 0.56,0.35,0.01"} G2 [=]{style="color: 0.56,0.35,0.01"} [2]{style="color: 0.00,0.00,0.81"}[*****]{style="color: 0.81,0.36,0.00"}[sum]{style="color: 0.13,0.29,0.53"}(obs[*****]{style="color: 0.81,0.36,0.00"}[log]{style="color: 0.13,0.29,0.53"}(obs[**/**]{style="color: 0.81,0.36,0.00"}m)) G2

    ## [1] 30.43096

We see that [\\(G_0\^2 = 30.43096\\)]{.math .inline}.

The reference distribution is the chi-squared distribution with [\\(\\mathrm{df}=c-1-1=2\\)]{.math .inline} degrees of freedom. The following R code computes the [\\(p\\)]{.math .inline}-value:

 snugshade
 Highlighting
[pchisq]{style="color: 0.13,0.29,0.53"}(G2,[2]{style="color: 0.00,0.00,0.81"},[lower.tail=]{style="color: 0.13,0.29,0.53"}[FALSE]{style="color: 0.56,0.35,0.01"})

    ## [1] 2.466041e-07

We see that [\\(p\\)]{.math .inline}-value [\\(\< 0.001\\)]{.math .inline}.

## Part (b)

We obtained a [\\(p\\)]{.math .inline}-value less than [\\(0.001\\)]{.math .inline}, which we consider to be very strong evidence against the constant infection rate model.

# Problem 4

## Part (a)

Recall that the data model is given by [\\[(n_0,n_1,n_2,n_3) \\sim \\operatorname{MULT}(n,\\pi_0,\\pi_1,\\pi_2,\\pi_3).\\]]{.math .display} Under the full model, each [\\(\\pi_j\\)]{.math .inline} may be independently specified.

We simply let the data speak for itself and estimate [\\(\\pi_j\\)]{.math .inline} as [\\[\\hat\\pi_j\^{F} = \\frac{n_j}{n}.\\]]{.math .display} We use the following R code to compute the probability vector:

 snugshade
 Highlighting
pihats_full [=]{style="color: 0.56,0.35,0.01"} obs[**/**]{style="color: 0.81,0.36,0.00"}n [round]{style="color: 0.13,0.29,0.53"}(pihats_full,[digits=]{style="color: 0.13,0.29,0.53"}[3]{style="color: 0.00,0.00,0.81"})

    ## [1] 0.404 0.404 0.160 0.032

## Part (b)

The probability of a primary infection is [\\[\\Pr(\\text{primary}) = \\pi_1 + \\pi_2 + \\pi_3,\\]]{.math .display} the probability of a secondary infection given a primary infection is [\\[\\Pr(\\text{secondary} \\,\\vert\\, \\text{primary}) = \\frac{\\pi_2 + \\pi_3}{\\pi_1 + \\pi_2 + \\pi_3},\\]]{.math .display} and the probability of a tertiary infection given a secondary infection is [\\[\\Pr(\\text{tertiary} \\,\\vert\\, \\text{secondary}) = \\frac{\\pi_3}{\\pi_2 + \\pi_3}.\\]]{.math .display}

We estimate these probabilities by plugging in the MLEs:

 snugshade
 Highlighting
primary [=]{style="color: 0.56,0.35,0.01"} [sum]{style="color: 0.13,0.29,0.53"}(pihats_full[[2]{style="color: 0.00,0.00,0.81"}[**:**]{style="color: 0.81,0.36,0.00"}[4]{style="color: 0.00,0.00,0.81"}]) secondary [=]{style="color: 0.56,0.35,0.01"} [sum]{style="color: 0.13,0.29,0.53"}(pihats_full[[3]{style="color: 0.00,0.00,0.81"}[**:**]{style="color: 0.81,0.36,0.00"}[4]{style="color: 0.00,0.00,0.81"}]) [**/**]{style="color: 0.81,0.36,0.00"} primary tertiary [=]{style="color: 0.56,0.35,0.01"} pihats_full[[4]{style="color: 0.00,0.00,0.81"}] [**/**]{style="color: 0.81,0.36,0.00"} secondary

[round]{style="color: 0.13,0.29,0.53"}([c]{style="color: 0.13,0.29,0.53"}(primary,secondary,tertiary),[digits=]{style="color: 0.13,0.29,0.53"}[3]{style="color: 0.00,0.00,0.81"})

    ## [1] 0.596 0.323 0.099

We see that the conditional probability vector is given by [\\((0.596,0.323,0.099)\'\\)]{.math .inline}.

## Part (c)

The conditional probabilities for the infection rates are significantly *decreasing*, i.e., not constant. The constant infection rate model was not able to capture this relationship in the data.
