# Problem 1

Consider an experiment on chlorophyll inheritance in maize. A genetic theory predicts the ratio of green to yellow to be 3:1. In a sample of [\\(n = 1103\\)]{.math .inline} seedlings, [\\(n_1 = 854\\)]{.math .inline} were green and [\\(n_2 = 249\\)]{.math .inline} were yellow.

## Part (a)

The likelihood ratio statistic is defined as [\\[G\^2 = - 2 \\log \\Lambda = 2 \\sum\_{j=1}\^{c} \\log\\left(\\frac{n_j}{n \\pi\_{j 0}}\\right).\\]]{.math .display}

We use the following R code to compute the observed statistic [\\(G_0\^2\\)]{.math .inline}.

 snugshade
 Highlighting
[*\# below is code for testing a specified multinomial*]{style="color: 0.56,0.35,0.01"} [*\# data is entered as a vector of counts*]{style="color: 0.56,0.35,0.01"} obs [=]{style="color: 0.56,0.35,0.01"} [c]{style="color: 0.13,0.29,0.53"}([854]{style="color: 0.00,0.00,0.81"},[249]{style="color: 0.00,0.00,0.81"}) n [=]{style="color: 0.56,0.35,0.01"} [sum]{style="color: 0.13,0.29,0.53"}(obs)

[*\# the null model is entered as a vector of hypothesized probabilities*]{style="color: 0.56,0.35,0.01"} [*\# expected counts under the null model are computed as n*prob*]{style="color: 0.56,0.35,0.01"} pi[.0]{style="color: 0.00,0.00,0.81"} [=]{style="color: 0.56,0.35,0.01"} [c]{style="color: 0.13,0.29,0.53"}(.[75]{style="color: 0.00,0.00,0.81"},.[25]{style="color: 0.00,0.00,0.81"}) m [=]{style="color: 0.56,0.35,0.01"} n[*****]{style="color: 0.81,0.36,0.00"}pi[.0]{style="color: 0.00,0.00,0.81"}

[*\# log-likelihood ratio test*]{style="color: 0.56,0.35,0.01"} G2 [=]{style="color: 0.56,0.35,0.01"} [2]{style="color: 0.00,0.00,0.81"}[*****]{style="color: 0.81,0.36,0.00"}[sum]{style="color: 0.13,0.29,0.53"}(obs[*****]{style="color: 0.81,0.36,0.00"}[log]{style="color: 0.13,0.29,0.53"}(obs[**/**]{style="color: 0.81,0.36,0.00"}m)) [print]{style="color: 0.13,0.29,0.53"}(G2)

    ## [1] 3.539017

We see that the observed statistic is given by [\\(G_0\^2 = 3.54\\)]{.math .inline}.

## Part (b)

The reference distribution is the chi-squared distribution with [\\(c-1 = 1\\)]{.math .inline} degrees of freedom.

The [\\(p\\)]{.math .inline}-value with [\\(k\\)]{.math .inline} degrees of freedom is defined as [\\[\\text{\$p$-value} = \\operatorname{P}(\\chi\^2(k) \> G\^2),\\]]{.math .display} or in this case [\\[\\text{\$p$-value} = \\operatorname{P}(\\chi\^2(1) \> 3.54) = 0.06.\\]]{.math .display} The following R code computes the [\\(p\\)]{.math .inline}-value.

 snugshade
 Highlighting
[*\# the p-value, a calculation based on tail probabilities*]{style="color: 0.56,0.35,0.01"} c [=]{style="color: 0.56,0.35,0.01"} [length]{style="color: 0.13,0.29,0.53"}(obs) pvalue.G2 [=]{style="color: 0.56,0.35,0.01"} [pchisq]{style="color: 0.13,0.29,0.53"}(G2,c[-1]{style="color: 0.00,0.00,0.81"},[lower.tail=]{style="color: 0.13,0.29,0.53"}[FALSE]{style="color: 0.56,0.35,0.01"}) [print]{style="color: 0.13,0.29,0.53"}(pvalue.G2)

    ## [1] 0.05994099

## Part (c)

According to the Fisher scale for interpreting [\\(p\\)]{.math .inline}-values, [\\(p\\)]{.math .inline}-values of [\\(0.05\\)]{.math .inline} and [\\(0.1\\)]{.math .inline} denote respectively *moderate* and *boderline* evidence against the null model.

Since we obtained a [\\(p\\)]{.math .inline}-value of [\\(0.06\\)]{.math .inline}, the data provides *moderate* evidence against the genetic theory positing that the ratio of green to yellow seedlings is 3:1.

## Part (d)

The [\\(p\\)]{.math .inline}-value overstates evidence against the null model by comparing the null model to the alternative model that is best supported by the data.

## Part (e)

Below is code for computing Bayes Factors in a test for a specified probability.

 snugshade
 Highlighting
[library]{style="color: 0.13,0.29,0.53"}(BayesFactor) [*\# g denotes number of green seedlings*]{style="color: 0.56,0.35,0.01"} [*\# y denotes number of yellow seedlings*]{style="color: 0.56,0.35,0.01"} [*\# n = g+y denotes total number of seedlings*]{style="color: 0.56,0.35,0.01"} g [=]{style="color: 0.56,0.35,0.01"} [854]{style="color: 0.00,0.00,0.81"} y [=]{style="color: 0.56,0.35,0.01"} [249]{style="color: 0.00,0.00,0.81"} n [=]{style="color: 0.56,0.35,0.01"} g[**+**]{style="color: 0.81,0.36,0.00"}y p0 [=]{style="color: 0.56,0.35,0.01"} [3]{style="color: 0.00,0.00,0.81"}[**/**]{style="color: 0.81,0.36,0.00"}[4]{style="color: 0.00,0.00,0.81"}

bf.medium [=]{style="color: 0.56,0.35,0.01"} [1]{style="color: 0.00,0.00,0.81"}[**/**]{style="color: 0.81,0.36,0.00"}[proportionBF]{style="color: 0.13,0.29,0.53"}([y=]{style="color: 0.13,0.29,0.53"}g,[N=]{style="color: 0.13,0.29,0.53"}n,[p=]{style="color: 0.13,0.29,0.53"}p0,[rscale=]{style="color: 0.13,0.29,0.53"}[\"medium\"]{style="color: 0.31,0.60,0.02"}) bf.wide [=]{style="color: 0.56,0.35,0.01"} [1]{style="color: 0.00,0.00,0.81"}[**/**]{style="color: 0.81,0.36,0.00"}[proportionBF]{style="color: 0.13,0.29,0.53"}([y=]{style="color: 0.13,0.29,0.53"}g,[N=]{style="color: 0.13,0.29,0.53"}n,[p=]{style="color: 0.13,0.29,0.53"}p0,[rscale=]{style="color: 0.13,0.29,0.53"}[\"wide\"]{style="color: 0.31,0.60,0.02"}) bf.ultra [=]{style="color: 0.56,0.35,0.01"} [1]{style="color: 0.00,0.00,0.81"}[**/**]{style="color: 0.81,0.36,0.00"}[proportionBF]{style="color: 0.13,0.29,0.53"}([y=]{style="color: 0.13,0.29,0.53"}g,[N=]{style="color: 0.13,0.29,0.53"}n,[p=]{style="color: 0.13,0.29,0.53"}p0,[rscale=]{style="color: 0.13,0.29,0.53"}[\"ultrawide\"]{style="color: 0.31,0.60,0.02"})

bf.medium

    ## Bayes factor analysis
    ## --------------
    ## [1] Null, p=0.75 : 1.931436 ±0%
    ## 
    ## Against denominator:
    ##   Alternative, p0 = 0.75, r = 0.5, p =/= p0 
    ## ---
    ## Bayes factor type: BFproportion, logistic

 snugshade
 Highlighting
bf.wide

    ## Bayes factor analysis
    ## --------------
    ## [1] Null, p=0.75 : 2.700316 ±0%
    ## 
    ## Against denominator:
    ##   Alternative, p0 = 0.75, r = 0.707106781186548, p =/= p0 
    ## ---
    ## Bayes factor type: BFproportion, logistic

 snugshade
 Highlighting
bf.ultra

    ## Bayes factor analysis
    ## --------------
    ## [1] Null, p=0.75 : 3.796726 ±0.01%
    ## 
    ## Against denominator:
    ##   Alternative, p0 = 0.75, r = 1, p =/= p0 
    ## ---
    ## Bayes factor type: BFproportion, logistic

If [\\(\\rm{BF}\_{0 1} \> 1\\)]{.math .inline}, then the data supports the null model over the alternative model.

According to the Bayes Factors, the results for *medium*, *wide* and *ultrawide* are given respectively by [\\(1.9\\)]{.math .inline}, [\\(2.7\\)]{.math .inline}, and [\\(3.8\\)]{.math .inline}. Thus, the null model is supported by the data in each case.
