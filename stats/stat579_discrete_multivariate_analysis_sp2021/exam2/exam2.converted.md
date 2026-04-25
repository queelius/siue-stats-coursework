# Problem 1

A genetic model predicts the ratio of green seedlings to yellow seedlings to be [\\(3:1\\)]{.math .inline}. Consider data from a sample of [\\(n=1100\\)]{.math .inline} seedlings, where [\\(n_1 = 860\\)]{.math .inline} is the number of green and [\\(n_2 = 240\\)]{.math .inline} is the number of yellow.

## Part (a)

The observed data models the binomial distribution [\\[n_g \\sim \\operatorname{BIN}(n, \\pi_g)\\]]{.math .display} where [\\(n_g\\)]{.math .inline} and [\\(n_y = n - n_g\\)]{.math .inline} are respectively the number of green and yellow seedlings and [\\(\\pi_g\\)]{.math .inline} and [\\(\\pi_y=1-\\pi_g\\)]{.math .inline} are respectively the probability of a green and yellow seedling.

Under the null model, the odds of green seedlings to yellow seedlings is [\\(3:1\\)]{.math .inline}, thus [\\[H_0 : \\pi\_{g 0} = 0.75 \\;\\; (\\pi\_{y 0} = 0.25).\\]]{.math .display}

We perform a chi-squared test for goodness of fit whose test statistic is given by [\\[X\^2 = \\frac{(n_g - \\hat{m}\_g}{\\hat{m}\_g} + \\frac{(n_y - \\hat{m}\_y)\^2}{\\hat{m}\_y}\\]]{.math .display} where [\\(\\hat{m}\_g = n \\pi\_{g 0}\\)]{.math .inline} and [\\(\\hat{m}\_y = \\pi\_{y 0}\\)]{.math .inline}.

The parameter space of the unconstrained binomial model is given by [\\[\\vec{\\pi}(\\pi_g) = (\\pi_g, 1-\\pi_g)\',\\]]{.math .display} which has a dimension of [\\(\\dim \\vec{\\pi} = 1\\)]{.math .inline}.

The *null model*, which is the specified binomial [\\(\\pi\_{g 0} = 0.75\\)]{.math .inline}, has the parameter space [\\(\\vec{\\pi}\_0 = (0.75,0.25)\'\\)]{.math .inline}, which is just a *point* with a dimension of [\\(\\dim \\vec{\\pi}\_0 = 0\\)]{.math .inline}.

Thus, under the null model, [\\(X\^2\\)]{.math .inline} is distributed [\\(\\chi\^2\\)]{.math .inline} with [\\[\\operatorname{df} = \\dim \\vec{\\pi} - \\dim \\vec{\\pi}\_0 = 1 - 0 = 1\\]]{.math .display} degrees of freedom, denoted by [\\(\\chi\^2(1)\\)]{.math .inline}.

### ANSWER

We compute the observed [\\(X\^2\\)]{.math .inline} statistic with:

 snugshade

    ## $stat
    ## [1] 5.939394
    ## 
    ## $p
    ## [1] 0.01480611
    ## 
    ## $df
    ## [1] 1

We see that [\\(X\^2\\)]{.math .inline} realizes the value [\\(X_0\^2 = 5.939\\)]{.math .inline}.

## Part (b)

Assuming [\\(X\^2 \\sim \\chi\^2(1)\\)]{.math .inline}, the [\\((1-\\alpha) \\times 100 \\%\\)]{.math .inline} percentile, denoted by [\\(\\chi\_{\\alpha}\^2(1)\\)]{.math .inline}, is given by solving the equation [\\[\\Pr[X\^2 \\geq \\chi\_{\\alpha}\^2(1)] = \\alpha\\]]{.math .display} for [\\(\\chi\_{\\alpha}\^2\\)]{.math .inline}.

We compute the [\\(10\\)]{.math .inline}-th percentile with the following R code:

 snugshade

### ANSWER

We see that the [\\(10\\)]{.math .inline}-th percentile is [\\(\\chi\^2\_{0.1}(1) = 2.706\\)]{.math .inline}.

## Part (c)

### ANSWER

We say that any observed statistic [\\(X_0\^2\\)]{.math .inline} with [\\(\\operatorname{df}=1\\)]{.math .inline} greater than [\\(\\chi\^2\_{0.1}(1) = 2.706\\)]{.math .inline} is not compatible with the null model at significance level [\\(\\alpha = 0.1\\)]{.math .inline}.

Since the observed statistic [\\(X_0\^2 = 5.939 \> 2.706\\)]{.math .inline}, the null model, which is the genetic theory where the ratio of green to yellow is [\\(3:1\\)]{.math .inline}, is not compatible with the data.

## Part (d)

### ANSWER

Hypothesis testing, as a dichotomous measure of evidence, does not provide as much information as a more quantitative evidence measure. For instance, it does not provide information about effect size.

## Part (e)

The MLE of [\\(\\pi_g\\)]{.math .inline} is given by [\\(\\hat{\\pi}\_g = \\frac{n_g}{n}\\)]{.math .inline}. A [\\((1-\\alpha) \\times 100 \\%\\)]{.math .inline} confidence interval for [\\(\\pi_g\\)]{.math .inline} is given by [\\[\\hat{\\pi}\_g \\pm z\_{\\alpha/2} \\hat\\sigma\_{\\hat\\pi_g}.\\]]{.math .display} where [\\(\\hat\\sigma\_{\\hat\\pi_g} = \\sqrt{\\frac{\\hat{\\pi}\_g (1-\\hat{\\pi}\_g)}{n}}\\)]{.math .inline}.

### ANSWER

Letting [\\(\\alpha = 0.10\\)]{.math .inline}, the MLE and [\\(90\\%\\)]{.math .inline} confidence interval for [\\(\\pi_g\\)]{.math .inline} is computed with the following R code:

 snugshade
 Highlighting
n [<-]{style="color: 0.56,0.35,0.01"} [sum]{style="color: 0.13,0.29,0.53"}(obs) mle [<-]{style="color: 0.56,0.35,0.01"} obs[[1]{style="color: 0.00,0.00,0.81"}][**/**]{style="color: 0.81,0.36,0.00"}n

alpha [<-]{style="color: 0.56,0.35,0.01"} [0.1]{style="color: 0.00,0.00,0.81"} s2 [<-]{style="color: 0.56,0.35,0.01"} mle[*****]{style="color: 0.81,0.36,0.00"}([1]{style="color: 0.00,0.00,0.81"}[**-**]{style="color: 0.81,0.36,0.00"}mle)[**/**]{style="color: 0.81,0.36,0.00"}n q [<-]{style="color: 0.56,0.35,0.01"} [qnorm]{style="color: 0.13,0.29,0.53"}([1]{style="color: 0.00,0.00,0.81"}[**-**]{style="color: 0.81,0.36,0.00"}alpha[**/**]{style="color: 0.81,0.36,0.00"}[2]{style="color: 0.00,0.00,0.81"}) [*\# should be around 1.645*]{style="color: 0.56,0.35,0.01"} conf [<-]{style="color: 0.56,0.35,0.01"} [c]{style="color: 0.13,0.29,0.53"}(mle [**-**]{style="color: 0.81,0.36,0.00"} q [*****]{style="color: 0.81,0.36,0.00"} [sqrt]{style="color: 0.13,0.29,0.53"}(s2), mle [**+**]{style="color: 0.81,0.36,0.00"} q [*****]{style="color: 0.81,0.36,0.00"} [sqrt]{style="color: 0.13,0.29,0.53"}(s2))

We see that [\\(\\hat{\\pi}\_g = 0.782\\)]{.math .inline} and a [\\(90\\%\\)]{.math .inline} confidence interval is [\\((0.761, 0.802)\\)]{.math .inline}.

## Part (f)

### ANSWER

Based on the observed data, we estimate that the probability [\\(\\pi_g\\)]{.math .inline} of a green strain is between 0.761 and 0.802.

As expected, the null model specifies a value for [\\(\\pi_g\\)]{.math .inline} ([\\(0.75\\)]{.math .inline}) that is not contained in the computed confidence interval.

## Part (g)

The same reasoning as in part (a), except we use a different statistic called the likelihood ratio statistic, [\\[G\^2 = - 2 \\log \\Lambda\\]]{.math .display} where [\\[\\Lambda = \\frac{l(\\pi\_{g 0})}{l(\\hat{\\pi}\_g)}.\\]]{.math .display} where [\\(\\hat{\\pi}\_g\\)]{.math .inline} is the maximum likelihood estimate [\\(n_g / n\\)]{.math .inline}.

This may be rewritten as [\\[G\^2 = 2 \\sum\_{j=1}\^{c} \\log\\left(\\frac{n_j}{n \\pi\_{j 0}}\\right).\\]]{.math .display}

Under the null model, [\\(G\^2\\)]{.math .inline} is distributed [\\(\\chi\^2\\)]{.math .inline} with [\\(1\\)]{.math .inline} degree of freedom.

### ANSWER

We compute the observed [\\(G_2\\)]{.math .inline} statistic with the following R code:

 snugshade

    ## $stat
    ## [1] 6.120841
    ## 
    ## $p
    ## [1] 0.01335972
    ## 
    ## $df
    ## [1] 1

We see that [\\(G\^2\\)]{.math .inline} realizes the value 6.121.

## Part (h)

### ANSWER

The reference distribution is the chi-squared distribution with [\\(1\\)]{.math .inline} degrees of freedom.

The [\\(p\\)]{.math .inline}-value given [\\(1\\)]{.math .inline} degree of freedom is defined as [\\[\\text{$p\$-value} = \\operatorname{P}(G\^2 \> \\chi\^2(1)),\\]]{.math .display} which was computed to be [\\(0.013\\)]{.math .inline}. (For comparison, the [\\(p\\)]{.math .inline}-value for the [\\(X\^2\\)]{.math .inline} test was [\\(0.015\\)]{.math .inline}.)

## Part (i)

### ANSWER

According to the Fisher scale for interpreting [\\(p\\)]{.math .inline}-values, a [\\(p\\)]{.math .inline}-value of [\\(0.01\\)]{.math .inline} is considered *strong* evidence against the null model.

Since we obtained a [\\(p\\)]{.math .inline}-value of slightly larger, the data provides *strong* evidence against the genetic theory positing that the ratio of green to yellow seedlings is [\\(3:1\\)]{.math .inline}.

## Part (j)

### ANSWER

The [\\(p\\)]{.math .inline}-value overstates evidence against the null model by comparing the null model to the alternative model that is best supported by the data.

# Problem 2

Consider the results from a study on the relationship between dose level and the severity of side effects. (Larger y values correspond to a more severe response.)

Data:

                [\\(y = 0\\)]{.math .inline}   [\\(y = 1\\)]{.math .inline}   [\\(y = 2\\)]{.math .inline}   [\\(y = 3\\)]{.math .inline}   [\\(y = 4\\)]{.math .inline}
  ------------- ------------------------------ ------------------------------ ------------------------------ ------------------------------ ------------------------------
  low dose      6                              9                              6                              3                              1
  medium dose   2                              5                              6                              6                              6
  high dose     1                              4                              6                              8                              8

## Preliminary analysis

We model the cross-sectional data as being an observation of a [\\(3 \\times 5\\)]{.math .inline} random matrix where the row levels, denoted by [\\(X\\)]{.math .inline}, correspond to dosage level and the column levels, denoted by [\\(Y\\)]{.math .inline}, correspond to severity of side effects. The elements (cells) of the random matrix are jointly sampled from the multinomial distribution [\\[\\{n\_{i j}\\} \\sim \\operatorname{MULT}(n, \\{\\pi\_{i j}\\}).\\]]{.math .display} where [\\(n\_{i j}\\)]{.math .inline} denotes the [\\((i,j)\\)]{.math .inline}-th element of the random matrix, [\\(\\pi\_{i j}\\)]{.math .inline} denotes the parameter that specifies the joint probability [\\(\\Pr(X=i,Y=j)\\)]{.math .inline}, and [\\(n\\)]{.math .inline} denotes the number of trials.

The full model has a parameter space of dimension [\\(3 \\times 5 - 1 = 14\\)]{.math .inline}.

## Part (a)

We consider a simpler model than the full model where [\\(X\\)]{.math .inline} and [\\(Y\\)]{.math .inline} are independent, i.e., [\\(\\pi\_{i j\\,0} = \\Pr(X=i)\\Pr(Y=j) = \\pi\_{i+}\\pi\_{+j}\\)]{.math .inline}. Since we are only free to specify [\\(\\pi\_{i+}\\)]{.math .inline} and [\\(\\pi\_{+j}\\)]{.math .inline}, the parameter space of the independence model is of dimension [\\((3-1) + (5-1) = 6\\)]{.math .inline}.

To decide whether the observed data is compatible with [\\(X\\)]{.math .inline} and [\\(Y\\)]{.math .inline} being independent, we perform the hypothesis test [\\[H_0 : \\{\\pi\_{i j}\\} = \\{\\pi\_{i j\\,0}\\}.\\]]{.math .display}

An estimator of [\\(\\pi\_{i+}\\)]{.math .inline} is [\\(\\hat{\\pi}\_{i+} = n\_{i+}/n\\)]{.math .inline} and an estimator of [\\(\\hat{\\pi}\_{+j}\\)]{.math .inline} is [\\(n\_{+j}/n\\)]{.math .inline}, therefore an estimator of [\\(\\pi\_{i j\\,0}\\)]{.math .inline} is given by [\\[\\hat{\\pi}\_{i j\\,0} = \\hat{\\pi}\_{i+} \\hat{\\pi}\_{+j} = \\frac{n\_{i+}n\_{+j}}{n\^2}.\\]]{.math .display} We perform a chi-square test for independence. The test statistic is given by [\\[X\^2 = \\sum\_{i=1}\^{4} \\frac{(n\_{i j} - \\hat{m}\_{i j})\^2}{\\hat{m}\_{i j}}\\]]{.math .display} where [\\(\\hat{m}\_{i j} = n \\hat{\\pi}\_{i j\\,0}\\)]{.math .inline}. Asymptotically, [\\(X\^2\\)]{.math .inline} is distributed [\\(\\chi\^2\\)]{.math .inline} with [\\(14 - 6 = 8\\)]{.math .inline} degrees of freedom.

### ANSWER

We compute the observed value of [\\(X\^2\\)]{.math .inline} and its [\\(p\\)]{.math .inline}-value with the following R code:

 snugshade

    ## $stat
    ## [1] 14.35678
    ## 
    ## $p
    ## [1] 0.07292708
    ## 
    ## $df
    ## [1] 8

The test statistic [\\(X\^2\\)]{.math .inline} realizes the value [\\(14.357\\)]{.math .inline} whose [\\(p\\)]{.math .inline}-value is 0.073. We consider this [\\(p\\)]{.math .inline}-value to be moderate evidence against the null model. Stated differently, the observed data is moderately incompatible with the independence model.

## Part (b)

Under the assumption of a monotonic association between [\\(X\\)]{.math .inline} and [\\(Y\\)]{.math .inline}, if [\\(X\\)]{.math .inline} and [\\(Y\\)]{.math .inline} are independent then their [\\(\\gamma\\)]{.math .inline} correlation is zero. To decide whether the observed data is compatible with [\\(X\\)]{.math .inline} and [\\(Y\\)]{.math .inline} being independent, we perform the hypothesis test [\\[H_0 : \\gamma = 0.\\]]{.math .display}

The test statistic is given by [\\[Z\^* = \\frac{\\hat\\gamma-0}{\\hat\\sigma(\\hat\\gamma)},\\]]{.math .display} which is normally distributed [\\(\\mathcal{N}(0,1)\\)]{.math .inline} under the null model.

### ANSWER

We compute [\\(Z\^*\\)]{.math .inline} and [\\(p\\)]{.math .inline}-value with the following R code:

 snugshade
 Highlighting
gamma_test [<-]{style="color: 0.56,0.35,0.01"} [independence_test_monotonic_association]{style="color: 0.13,0.29,0.53"}(obs)

The observed [\\(Z\^*\\)]{.math .inline} is 4.402 and its [\\(p\\)]{.math .inline}-value is less than [\\(0.001\\)]{.math .inline}, which we consider to be very strong evidence against the independence model.

That is, the observed data provides very strong evidence against the independence model under the assumption of a monotonic association.

## Part (c)

### ANSWER

Estimates for simpler models have smaller variances than for estimates from more complicated models.

# Problem 3

Consider the results from a prospective study on the relationship between sex and hair color.

 snugshade
 Highlighting
obs [<-]{style="color: 0.56,0.35,0.01"} [matrix]{style="color: 0.13,0.29,0.53"}([c]{style="color: 0.13,0.29,0.53"}([75]{style="color: 0.00,0.00,0.81"},[16]{style="color: 0.00,0.00,0.81"},[9]{style="color: 0.00,0.00,0.81"},[120]{style="color: 0.00,0.00,0.81"},[64]{style="color: 0.00,0.00,0.81"},[16]{style="color: 0.00,0.00,0.81"}),[nrow=]{style="color: 0.13,0.29,0.53"}[2]{style="color: 0.00,0.00,0.81"},[byrow=]{style="color: 0.13,0.29,0.53"}[TRUE]{style="color: 0.56,0.35,0.01"}) [dimnames]{style="color: 0.13,0.29,0.53"}(obs) [<-]{style="color: 0.56,0.35,0.01"} [list]{style="color: 0.13,0.29,0.53"}([sex=]{style="color: 0.13,0.29,0.53"}[c]{style="color: 0.13,0.29,0.53"}([\"male\"]{style="color: 0.31,0.60,0.02"},[\"female\"]{style="color: 0.31,0.60,0.02"}), [hc.level=]{style="color: 0.13,0.29,0.53"}[c]{style="color: 0.13,0.29,0.53"}([\"dark\"]{style="color: 0.31,0.60,0.02"},[\"blonde\"]{style="color: 0.31,0.60,0.02"},[\"red\"]{style="color: 0.31,0.60,0.02"})) [print]{style="color: 0.13,0.29,0.53"}(obs)

    ##         hc.level
    ## sex      dark blonde red
    ##   male     75     16   9
    ##   female  120     64  16

## Part (a)

### ANSWER

In a prospective study, each row of the table represents an independent multinomial. Thus, the data model is given by [\\[\\{n\_{i j}\\} \\sim \\operatorname{PROD\\\_MULT}(\\{n\_{i+}\\},\\{\\pi\_{j\|i}\\}).\\]]{.math .display}

We are given a table of [\\(I=2\\)]{.math .inline} rows and [\\(J=3\\)]{.math .inline} columns, and thus we have [\\(I\\)]{.math .inline} independent multinomials. Therefore, the likelihood function is given by [\\[l(\\{\\pi\_{j\|i}\\}) = \\prod\_{i=1}\^{I} \\frac{n\_{i+}!}{\\prod\_{j=1}\^{J} n\_{i j}!} \\prod\_{j=1}\^{J} \\pi\_{j\|i}\^{n\_{i j}}.\\]]{.math .display} Observe that [\\[l(\\{\\pi\_{j\|i}\\}) \\propto \\prod\_{i=1}\^{I} \\prod\_{j=1}\^{J} \\pi\_{j\|i}\^{n\_{i j}}.\\]]{.math .display}

Under the full model, the maximum likelihood of [\\(\\pi\_{j\|i}\\)]{.math .inline} is given by [\\[\\hat{\\pi}\_{j \| i}\^{(F)} = \\frac{n\_{i j}}{n\_{i+}}\\]]{.math .display} and under the independence model it is given by [\\[\\hat{\\pi}\_{j \| i}\^{(I)} = \\frac{n\_{+j}}{n}\\]]{.math .display} for [\\(i \\in \\{1,2\\}\\)]{.math .inline} and [\\(j \\in \\{1,2,3\\}\\)]{.math .inline}.

## Part (b)

The expected count [\\(\\hat{m}\_{i j}\\)]{.math .inline} under the independence model is given by [\\[\\hat{m}\_{i j} = \\frac{n\_{i+}n\_{+j}}{n} = n\_{i+} \\hat{\\pi}\_{j\|i}\^{(I)}.\\]]{.math .display}

### ANSWER

We use the R function [\\(\\operatorname{chisq.test}\\)]{.math .inline} to compute the expected cell counts [\\(\\{\\hat{m}\_{i j}\\}\\)]{.math .inline}:

 snugshade

    ##         hc.level
    ## sex      dark blonde    red
    ##   male     65 26.667  8.333
    ##   female  130 53.333 16.667

## Part (c)

In the full model, the paramter space is given by [\\[\\vec{\\pi}\^{(F)}(\\theta_1,\\theta_2, \\theta_3, \\theta_4) = \\begin{pmatrix} \\pi\_{1\|1} = \\theta_1 & \\pi\_{2\|1} = \\theta_2 & \\pi\_{3\|1} = 1-\\theta_1-\\theta_2\\\\ \\pi\_{1\|2} = \\theta_3 & \\pi\_{2\|2} = \\theta_4 & \\pi\_{3\|2} = 1-\\theta_3-\\theta_4 \\end{pmatrix}\\]]{.math .display} which is of dimension [\\(I(J-1) = 4\\)]{.math .inline} and under the independence model, the parameter space is [\\[\\vec{\\pi}\^{(I)}(\\theta_1,\\theta_2) = \\begin{pmatrix} \\pi\_{1\|1} = \\theta_1 & \\pi\_{2\|1} = \\theta_2 & \\pi\_{3\|1} = 1-\\theta_1-\\theta_2\\\\ \\pi\_{1\|2} = \\theta_1 & \\pi\_{2\|2} = \\theta_2 & \\pi\_{3\|2} = 1-\\theta_1-\\theta_2 \\end{pmatrix}\\]]{.math .display} which is of dimension [\\(J-1=2\\)]{.math .inline}. Thus, under the independence model, [\\(G\^2\\)]{.math .inline} is distributed [\\(\\chi\^2\\)]{.math .inline} with [\\(\\operatorname{df} = I(J-1) - (J-1) = (J-1)(I-1) = 2\\)]{.math .inline}

### ANSWER

We compute [\\(G\^2\\)]{.math .inline} from the observed counts [\\(\\{n\_{i j}\\}\\)]{.math .inline} and the expected counts [\\(\\{\\hat{m}\_{i j}\\}\\)]{.math .inline}:

 snugshade
 Highlighting
I [<-]{style="color: 0.56,0.35,0.01"} [dim]{style="color: 0.13,0.29,0.53"}(obs)[[1]{style="color: 0.00,0.00,0.81"}] J [<-]{style="color: 0.56,0.35,0.01"} [dim]{style="color: 0.13,0.29,0.53"}(obs)[[2]{style="color: 0.00,0.00,0.81"}] G2 [<-]{style="color: 0.56,0.35,0.01"} [2]{style="color: 0.00,0.00,0.81"}[*****]{style="color: 0.81,0.36,0.00"}[sum]{style="color: 0.13,0.29,0.53"}(obs[*****]{style="color: 0.81,0.36,0.00"}[log]{style="color: 0.13,0.29,0.53"}(obs[**/**]{style="color: 0.81,0.36,0.00"}m.hat)) df [<-]{style="color: 0.56,0.35,0.01"} (I[-1]{style="color: 0.00,0.00,0.81"})[*****]{style="color: 0.81,0.36,0.00"}(J[-1]{style="color: 0.00,0.00,0.81"}) p.value [<-]{style="color: 0.56,0.35,0.01"} [pchisq]{style="color: 0.13,0.29,0.53"}(G2,df,[lower.tail =]{style="color: 0.13,0.29,0.53"} [FALSE]{style="color: 0.56,0.35,0.01"})

[print]{style="color: 0.13,0.29,0.53"}([round]{style="color: 0.13,0.29,0.53"}(G2,[3]{style="color: 0.00,0.00,0.81"}))

    ## [1] 9.325

 snugshade
 Highlighting
[print]{style="color: 0.13,0.29,0.53"}([round]{style="color: 0.13,0.29,0.53"}(p.value,[3]{style="color: 0.00,0.00,0.81"}))

    ## [1] 0.009

We obtain a [\\(p\\)]{.math .inline}-value around [\\(0.01\\)]{.math .inline}, which we consider to be strong evidence against the independence model (the data supports the general association model). That is to say, the conditional distribution [\\[\\Pr(\\text{hair color} \\,\|\\, \\text{sex} = \\text{male})\\]]{.math .display} and [\\[\\Pr(\\text{hair color} \\,\|\\, \\text{sex} = \\text{female}).\\]]{.math .display} are different.

## Part (d)

### ANSWER

We display a table comparing expected and observed such that if the observed is less than the expected, display [\\(-1\\)]{.math .inline}, and if observed is greater than expected, display a [\\(1\\)]{.math .inline}:

 snugshade
 Highlighting
[print]{style="color: 0.13,0.29,0.53"}([sign]{style="color: 0.13,0.29,0.53"}(obs[**-**]{style="color: 0.81,0.36,0.00"}m.hat))

    ##         hc.level
    ## sex      dark blonde red
    ##   male      1     -1   1
    ##   female   -1      1  -1

The observed data is compatible with a model where males are more likely to have dark or red hair (and less likely to have blonde hair) and females are more likely to have blonde hair (and less likely to have dark or red hair).

# Problem 4

According to the Hardy-Weinberg model, the number of flies resulting from a crossing of genetic traits are in categories [\\(1\\)]{.math .inline}, [\\(2\\)]{.math .inline}, [\\(3\\)]{.math .inline} with probabilities [\\[\\begin{aligned} \\pi\_{1 o}(\\theta) &= (1-\\theta)\^2\\\\ \\pi\_{2 o}(\\theta) &= 2\\theta(1-\\theta)\\\\ \\pi\_{3 o}(\\theta) &= \\theta\^2 \\end{aligned}\\]]{.math .display}

## Part (a)

We assume the data model is given by [\\[(n_1,n_2,n_3) \\sim \\operatorname{MULT}(n, \\pi_1, \\pi_2, \\pi_3)\\]]{.math .display} where [\\(n_j\\)]{.math .inline} denotes the number of flies in category [\\(j\\)]{.math .inline} and [\\(\\pi_j\\)]{.math .inline} denotes the probability a fly is in category [\\(j\\)]{.math .inline}.

Under the specified model, the likelihood function is given by [\\[\\operatorname{L}(\\theta) \\propto \\prod\_{j=1}\^{3} \\pi\_{j o}(\\theta)\^{n_j}\\]]{.math .display} and the kernel of the log-likelihood function is given by [\\[\\begin{aligned} l(\\theta) &= \\sum\_{j=1}\^{3} n_j \\log \\pi\_{j o}(\\theta)\\\\ &= n_1 \\log \\pi\_{1 o}(\\theta) + n_2 \\log \\pi\_{2 o}(\\theta) + n_3 \\log \\pi\_{3 o}(\\theta)\\\\ &= n_1 \\log (1-\\theta)\^2 + n_2 \\log 2 \\theta(1-\\theta) + n_3 \\log \\theta\^2\\\\ &= 2 n_1 \\log (1-\\theta) + n_2 \\log \\theta + n_2 \\log(1-\\theta) + 2 n_3 \\log \\theta + \\rm{const}\\\\ &= (2 n_1 + n_2) \\log (1-\\theta) + ( n_2 + 2 n_3)\\log \\theta + \\rm{const}. \\end{aligned}\\]]{.math .display}

The derivative of the log-likelihood is thus given by [\\[\\frac{d l}{d \\theta} = -\\frac{2 n_1 + n_2}{1-\\theta} + \\frac{n_2 + 2 n_3}{\\theta}.\\]]{.math .display}

The ML estimate of [\\(\\theta\\)]{.math .inline} is given by [\\[\\left. \\frac{d l}{d \\theta} \\right\\vert\_{\\hat\\theta} = 0.\\]]{.math .display} Solving for [\\(\\hat\\theta\\)]{.math .inline}, we see that [\\[\\frac{2 n_1 + n_2}{1-\\hat\\theta} = \\frac{n_2 + 2 n_3}{\\hat\\theta}.\\]]{.math .display} Next, we take the reciprocal of both sides, [\\[\\frac{1-\\hat\\theta}{2 n_1 + n_2} = \\frac{\\hat\\theta}{n_2 + 2 n_3}.\\]]{.math .display} Expanding the LHS, we get [\\[\\frac{1}{2 n_1 + n_2} - \\frac{\\hat\\theta}{2 n_1 + n_2} = \\frac{\\hat\\theta}{n_2 + 2 n_3}\\]]{.math .display} which may be rewritten as [\\[\\hat\\theta \\left(\\frac{1}{2 n_1 + n_2} + \\frac{1}{n_2 + 2 n_3}\\right) = \\frac{1}{2 n_1 + n_2}.\\]]{.math .display} Dividing both sides by the part in parentheses, we get [\\[\\hat\\theta = \\frac{1}{(2 n_1 + n_2) \\left(\\frac{1}{2 n_1 + n_2} + \\frac{1}{n_2 + 2 n_3}\\right)},\\]]{.math .display} which simplifies to [\\[\\hat\\theta = \\frac{1}{1 + \\frac{2 n_1 + n_2}{n_2 + 2 n_3}} = \\frac{1}{\\frac{2 n_3 + 2 n_1 + 2 n_2}{n_2 + 2 n_3}}.\\]]{.math .display} Performing the division, we get the simplification [\\[\\hat\\theta = \\frac{n_2 + 2 n_3}{2(n_3 + n_1 + n_2)}.\\]]{.math .display}

### ANSWER

Observe that [\\(n_1 + n_2 + n_3\\)]{.math .inline} is [\\(n\\)]{.math .inline}, thus [\\[\\hat\\theta = \\frac{n_2 + 2 n_3}{2 n}.\\]]{.math .display}

## Part (b)

Using the MLE equation, we compute the result using R:

 snugshade
 Highlighting
n [=]{style="color: 0.56,0.35,0.01"} [c]{style="color: 0.13,0.29,0.53"}([40]{style="color: 0.00,0.00,0.81"},[50]{style="color: 0.00,0.00,0.81"},[10]{style="color: 0.00,0.00,0.81"}) mle [<-]{style="color: 0.56,0.35,0.01"} (n[[2]{style="color: 0.00,0.00,0.81"}] [**+**]{style="color: 0.81,0.36,0.00"} [2]{style="color: 0.00,0.00,0.81"}[*****]{style="color: 0.81,0.36,0.00"}n[[3]{style="color: 0.00,0.00,0.81"}])[**/**]{style="color: 0.81,0.36,0.00"}[sum]{style="color: 0.13,0.29,0.53"}(n)

### ANSWER

We see that [\\[\\hat\\theta = 0.7.\\]]{.math .display} Plugging in this result, [\\[\\vec{\\pi}\_{o}(\\hat\\theta) = ( (1-\\hat\\theta)\^2, 2\\hat\\theta(1-\\hat\\theta), \\hat\\theta\^2)\'\\]]{.math .display} which we compute with R:

 snugshade
 Highlighting
pi0.hats [<-]{style="color: 0.56,0.35,0.01"} [c]{style="color: 0.13,0.29,0.53"}(([1]{style="color: 0.00,0.00,0.81"}[**-**]{style="color: 0.81,0.36,0.00"}mle)[**\^**]{style="color: 0.81,0.36,0.00"}[2]{style="color: 0.00,0.00,0.81"}, [2]{style="color: 0.00,0.00,0.81"}[*****]{style="color: 0.81,0.36,0.00"}mle[*****]{style="color: 0.81,0.36,0.00"}([1]{style="color: 0.00,0.00,0.81"}[**-**]{style="color: 0.81,0.36,0.00"}mle), mle[**\^**]{style="color: 0.81,0.36,0.00"}[2]{style="color: 0.00,0.00,0.81"})

We see that [\\(\\vec{\\pi}\_{o}(\\hat\\theta) = (0.09, 0.42, 0.49)\'\\)]{.math .inline}.

## Part (c)

### ANSWER

The parameter space of the Hardy-Weinberg model is a function of a single parameter [\\(\\theta\\)]{.math .inline} and thus has a dimension of [\\(1\\)]{.math .inline}. The parameter space of the full model is [\\(2\\)]{.math .inline}. Thus, the reference distribution is [\\(\\chi\^2\\)]{.math .inline} with [\\(\\operatorname{df} = 2 - 1 = 1\\)]{.math .inline} degrees of freedom.

The following R code computes the realization of [\\(G\^2\\)]{.math .inline}, denoted by [\\(G_0\^2\\)]{.math .inline}, and its [\\(p\\)]{.math .inline}-value:

 snugshade

    ## $stat
    ## [1] 104.983
    ## 
    ## $p
    ## [1] 1.231867e-24
    ## 
    ## $df
    ## [1] 1

We see that [\\(G_0\^2 = 104.983\\)]{.math .inline} with a [\\(p\\)]{.math .inline}-value less than [\\(0.001\\)]{.math .inline}, which we consider to be very strong evidence against the Hardy-Weinberg.

# Library of test functions

``` {.sourceCode .R}
# function for performing a multinomial goodness of fit hypothesis test
# with a specified null model pi.0 in which pi.0 is the result of t parameters.
#
# input:
#     obs: vector of counts
#     pi.0: vector of hypothesized probabilites,
#     t: dimension of the parameter space under the null hypothesis.
# 
# outputs: two lists, one for X2 and one for G2. each list has:
#     X2: list relevant results for X^2 test
#     G2: list of relevant results for G^2 test, e.g.:
#       list(stat,p,df,reject) where
#         p: p-value of the obs under the null model
#         df: degrees of freedom of the reference distribution (chi-square)
multinomial_goodness_of_fit <- function(obs, pi.0, t=0)
{
  n <- sum(obs)                 # number of observations
  t.full <- length(obs)-1       # dim of parameter space for the full model.
  df <- t.full-t                # degrees of freedom for the ref distribution
  m.0 <- n*pi.0                 # expected observations (for given n)
  
  G2 <- 2*sum(obs*log(obs/m.0)) # log-likelihood ratio test statistic
  G2.p <- pchisq(q=G2,df=df,lower.tail=FALSE)

  X2 <- sum((obs-m.0)^2/m.0)   # test statistic
  X2.p <- pchisq(q=X2,df=df,lower.tail=FALSE)

  # return relevant test statistics
  list(m.0=m.0,pi.0=pi.0,
       X2=list(stat=X2,p=X2.p,df=df),
       G2=list(stat=G2,p=G2.p,df=df))
}

# obs is an IxJ matrix representing cross-sectional data (observed counts).
# tests for independence P(X,Y) = P(X)P(Y).
multinomial_goodness_of_fit_independence_test <- function(obs)
{
  I <- dim(obs)[1]
  J <- dim(obs)[2]
  t <- (I-1)+(J-1)
  
  n <- sum(obs)  
  row.sum <- apply(obs,1,sum)
  col.sum <- apply(obs,2,sum)
  m.0 <- matrix(row.sum) %*% t(matrix(col.sum))/n
  
  multinomial_goodness_of_fit(obs=obs,pi.0=m.0/n,t=t)
}

independence_test_monotonic_association <- function(obs)
{
  # to compute the estimate of gamma and the standard error, we need MESS
  library("MESS")
  
  # gkgamma takes an IxJ matrix as an input
  gk.result <- gkgamma(obs)
  
  # compute gamma.hat and its standard error
  gamma.hat <- gk.result$estimate
  se <- gk.result$se1
  
  # compute the z statistic and p-value for testing gamma=0 (independence)
  z <- gamma.hat / se
  p.value <- 2*pnorm(abs(z),lower.tail = FALSE)
  
  list(gamma=gamma.hat,ase=se,stat=z,p=p.value)
}
```
