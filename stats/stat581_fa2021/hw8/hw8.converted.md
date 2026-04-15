# Problem 1

> An experiment is designed to test for systematic differences in the hardness measurements provided by two devices (fixed effect, factor [\\(A\\)]{.math .inline}). Ten specimens are randomly selected (random effect, factor [\\(B\\)]{.math .inline}). Each device is used to make [\\(n=3\\)]{.math .inline} hardness measurements on each specimen. The data is available on Blackboard as an Excel File.

## Part (a)

> Write the model for this mixed effects design, defining the fixed effect parameters, and the random effect parameters.

The mixed-effects model is given by [\\[Y\_{i j k} = \\mu + \\tau_i + \\beta_j + (\\tau\\!\\beta)\_{i j} + \\epsilon\_{i j k} \\; \\begin{cases} i = 1,\\ldots,a=2\\\\ j = 1,\\ldots,b=10\\\\ k = 1,\\ldots,n=3 \\end{cases}\\]]{.math .display} where the fixed effect parameters are [\\[\\tau_1,\\ldots,\\tau_a \\qquad \\left(\\sum \\tau_i = 0\\right)\\]]{.math .display} and the random effect parameters are [\\[\\sigma\_\\beta\^2, \\sigma\_{\\tau\\!\\beta}\^2, \\sigma\^2.\\]]{.math .display}

## Part (b)

> Create an interaction plot to display the device effect on hardness measurement.

First, we load the data:

 snugshade

    ##     a     b     n     N  df.A  df.B df.AB 
    ##     2    10     3    60     1     9     9

The interaction plot is given by:

 snugshade
 Highlighting
[*\# remember that we are testing whether operator differences are*]{style="color: 0.56,0.35,0.01"} [*\# generalizable to a larger population of parts.*]{style="color: 0.56,0.35,0.01"} [**interaction.plot**]{style="color: 0.13,0.29,0.53"}(B,A,y)

## Part (c)

> Use a mixed model likelihood approach to test for a systematic difference in the measurements of the two devices. Compute the [\\(F_0\\)]{.math .inline} statistic, and the [\\(p\\)]{.math .inline}-value. Provide an interpretation, stated in the context of the problem.

We compute the statistic with:

 snugshade
 Highlighting
[library]{style="color: 0.13,0.29,0.53"}([\"lme4\"]{style="color: 0.31,0.60,0.02"})

    ## Loading required package: Matrix

 snugshade
 Highlighting
[contrasts]{style="color: 0.13,0.29,0.53"}(A)[=]{style="color: 0.56,0.35,0.01"}contr.sum mixed.mod [=]{style="color: 0.56,0.35,0.01"} [lmer]{style="color: 0.13,0.29,0.53"}(y [**\~**]{style="color: 0.81,0.36,0.00"} A [**+**]{style="color: 0.81,0.36,0.00"} ([1]{style="color: 0.00,0.00,0.81"}[**\|**]{style="color: 0.81,0.36,0.00"}B) [**+**]{style="color: 0.81,0.36,0.00"} ([1]{style="color: 0.00,0.00,0.81"}[**\|**]{style="color: 0.81,0.36,0.00"}A[**:**]{style="color: 0.81,0.36,0.00"}B))

    ## boundary (singular) fit: see help('isSingular')

 snugshade
 Highlighting
[anova]{style="color: 0.13,0.29,0.53"}(mixed.mod)

    ## Analysis of Variance Table
    ##   npar  Sum Sq Mean Sq F value
    ## A    1 0.41667 0.41667  0.3121

We see that [\\(F_0 = .312\\)]{.math .inline} ([\\(p = .579\\)]{.math .inline}).

### Interpretation

Based on these observed test statistics, the experiment finds that factor [\\(A\\)]{.math .inline} (device) has no effect on response [\\(y\\)]{.math .inline} (hardness measurement of specimen).

## Part (d)

> Compute estimates of the fixed effect parameters.

The formula for the estimates of the fixed effect parameters [\\(\\{\\tau_i\\}\\)]{.math .inline} are given by [\\[\\hat{\\tau}\_i = \\bar{y}\_{i \\cdot\\cdot} - \\bar{y}\_{\\cdot\\cdot\\cdot}\\]]{.math .display} for [\\(i=1,\\ldots,a=2\\)]{.math .inline}. We use the following R code to compute [\\(\\hat{\\tau}\_1\\)]{.math .inline}:

 snugshade
 Highlighting
[coef]{style="color: 0.13,0.29,0.53"}([summary]{style="color: 0.13,0.29,0.53"}(mixed.mod))

    ##                Estimate Std. Error     t value
    ## (Intercept) 49.95000000  0.4282105 116.6482481
    ## A1           0.08333333  0.1491662   0.5586608

Since [\\(\\tau_1 + \\tau_2 = 0\\)]{.math .inline}, this means [\\(\\hat{\\tau}\_1 = .083\\)]{.math .inline} and [\\(\\hat{\\tau}\_2 = -\\hat{\\tau}\_1 = -.083\\)]{.math .inline}.

## Part (e)

> Now write an [\\(F_A\\)]{.math .inline} statistic as a ratio of mean squares.

We use Dr. Neath's custom function [\\[\\operatorname{mixed.test} : [\\text{fixed factors}] \\times [\\text{random factors}] \\times [\\text{responses}] \\mapsto [\\text{statistics}]\\]]{.math .display} to compute the [\\(F_A\\)]{.math .inline} statistic:

 snugshade
 Highlighting
[**mixed.test**]{style="color: 0.13,0.29,0.53"}(A,B,y)

    ##                         SS df         MS
    ## Fixed Effect A   0.4166667  1  0.4166667
    ## Random Effect B 99.0166667  9 11.0018519
    ## Interaction AB   5.4166667  9  0.6018519
    ## Error           60.0000000 40  1.5000000
    ##  F-test for fixed effect   p-value
    ##                0.6923077 0.4269057
    ##  error.var interaction.var block.var
    ##        1.5      -0.2993827  1.733333

The [\\(F\\)]{.math .inline}-test statistic for the factor [\\(A\\)]{.math .inline} effect is given by [\\[F_A = \\frac{\\operatorname{MS\_{A}}}{\\operatorname{MS\_{A B}}} = .692,\\]]{.math .display} which has the reference distribution [\\[F(\\rm{df}\_A=a-1,\\rm{df}\_{A B} = (a-1)(b-1)) = F(1,9).\\]]{.math .display} Thus, the [\\(p\\)]{.math .inline}-value is given by [\\(\\Pr\\{F(1,9) \> F_A\\} = .427\\)]{.math .inline}.

## Part (f)

> Write the algebraic formula for the [\\(F_0\\)]{.math .inline} statistic from a block design on the sample means.

[\\[F_0 = \\frac {b \\sum\_{i=1}\^{a}(\\bar{Y}\_{i\\cdot\\cdot} - \\bar{Y}\_{\\cdot\\cdot\\cdot})\^2/(a-1)} {\\sum\_{i=1}\^{a}\\sum\_{j=1}\^{b}( \\bar{Y}\_{i j\\cdot}- \\bar{Y\_{i \\cdot\\cdot}}- \\bar{Y}\_{\\cdot j \\cdot}+ \\bar{Y}\_{\\cdot\\cdot\\cdot} )\^2 / (a-1)(b-1)}.\\]]{.math .display}

## Part (g)

> Show computationally that (e) and (f) lead to the same test statistic.

We must use the means of the response over repeated measurements of the block (specimen) at a given factor level [\\(A\\)]{.math .inline}. These values have already been computed for us `handout8data.xlsx`:

 snugshade

Now, we do the calculations:

 snugshade
 Highlighting
[*\# below we run a randomized block design with the sample means as the*]{style="color: 0.56,0.35,0.01"} [*\# response variables.*]{style="color: 0.56,0.35,0.01"} [*\# note that the test for a fixed factor effect is equivalent to that*]{style="color: 0.56,0.35,0.01"} [*\# from the mixed.test function.*]{style="color: 0.56,0.35,0.01"} rcbd.mod [=]{style="color: 0.56,0.35,0.01"} [lmer]{style="color: 0.13,0.29,0.53"}(h.means [**\~**]{style="color: 0.81,0.36,0.00"} d [**+**]{style="color: 0.81,0.36,0.00"} ([1]{style="color: 0.00,0.00,0.81"}[**\|**]{style="color: 0.81,0.36,0.00"}s)) [anova]{style="color: 0.13,0.29,0.53"}(rcbd.mod)

    ## Analysis of Variance Table
    ##   npar  Sum Sq Mean Sq F value
    ## d    1 0.13945 0.13945  0.6954

We see that this result matches the result in (e), i.e., `mix.test(A,B,y)` produced the same result.

## Part (h)

> Use the result from (g) to argue why interaction mean squares is the appropriate error term.

Repeat measurements are summarized by a sample mean. The test statistic for a block design then leads to the interaction mean squares under a mixed model as the error term.

# Problem 2

> A mixed effects design is used to investigate the effects of operator (fixed effect, factor A) and machine (random effect, factor B) on the breaking strength of a synthetic fiber. There are [\\(a=3\\)]{.math .inline} operators under investigation. A random sample of [\\(b=4\\)]{.math .inline} machines is selected, and each operator produces [\\(n=2\\)]{.math .inline} samples on each of the selected machines. The data is available on Blackboard as an Excel File.

## Part (a)

> State the expected value for each of the mean squares.

[\\[\\begin{aligned} E(\\operatorname{MS\_{A}}) &= \\sigma\^2 + n \\sigma\_{\\tau \\! \\beta}\^2 + \\frac{b n \\sum\_{i=1}\^{a}\\tau_i\^2}{a-1},\\\\ E(\\operatorname{MS\_{B}}) &= \\sigma\^2 + n \\sigma\_{\\tau \\! \\beta}\^2 + a n \\sigma\_{\\beta}\^2,\\\\ E(\\operatorname{MS\_{A B}}) &= \\sigma\^2 + n \\sigma\_{\\tau \\! \\beta}\^2,\\\\ E(\\operatorname{MS\_{E}}) &= \\sigma\^2. \\end{aligned}\\]]{.math .display}

## Part (b)

> Compute unbiased estimates for the random effect parameters.

 snugshade

    ##                        SS df        MS
    ## Fixed Effect A  160.33333  2 80.166667
    ## Random Effect B  12.45833  3  4.152778
    ## Interaction AB   44.66667  6  7.444444
    ## Error            45.50000 12  3.791667
    ##  F-test for fixed effect    p-value
    ##                 10.76866 0.01034401
    ##  error.var interaction.var  block.var
    ##   3.791667        1.826389 -0.5486111

The random effect parameters are given by [\\(\\sigma\^2\\)]{.math .inline}, [\\(\\sigma\_\\beta\^2\\)]{.math .inline}, and [\\(\\sigma\_{\\tau\\beta}\^2\\)]{.math .inline}. Estimators for these parameters are given by [\\[\\begin{aligned} \\hat\\sigma\^2 &= \\operatorname{MS\_{E}} = 3.792,\\\\ \\hat\\sigma\_{\\beta}\^2 &= \\frac{\\operatorname{MS\_{B}}-\\operatorname{MS\_{A B}}}{a n} = -0.549,\\\\ \\hat\\sigma\_{\\tau\\!\\beta}\^2 &= \\frac{\\operatorname{MS\_{A B}}-\\operatorname{MS\_{E}}}{n} = 1.826. \\end{aligned}\\]]{.math .display}

## Part (c)

> Use the result from (a) to argue why interaction mean squares is the appropriate error term.

Under the null hypothesis [\\[H_0 : \\tau_1 = \\cdots = \\tau_a = 0,\\]]{.math .display} [\\(E(\\operatorname{MS\_{A}}) = \\sigma\^2 + n \\sigma\_{\\tau \\! \\beta}\^2 + \\frac{b n \\sum\_{i=1}\^{a}\\tau_i\^2}{a-1} = \\sigma\^2 + n \\sigma\_{\\tau\\!\\beta}\^2\\)]{.math .inline}. The scaling requires a denominator with the same expected value. Thus, [\\(\\operatorname{MS\_{A B}}\\)]{.math .inline} is the appropriate error term.

## Part (d)

> Perform a test for operator effects. Compute the [\\(F_A\\)]{.math .inline} statistic, and the [\\(p\\)]{.math .inline}-value. Provide an interpretation, stated in the context of the problem.

From part (b), [\\(F_A = \\frac{\\operatorname{MS\_{A}}}{\\operatorname{MS\_{A B}}} = 10.769\\)]{.math .inline}, which has a [\\(p\\)]{.math .inline}-value of [\\(.010\\)]{.math .inline}.

### Interpretation

The experiment finds that factor [\\(A\\)]{.math .inline} (operator) does have an effect on the fiber strength.

## Part (e)

> Now, use the idea of random factors as an experimental unit to explain why interaction mean squares is the appropriate error term. In particular, comment on how taking repeat measurements on a selected level of a random factor does not increase the pertinent sample size.

Taking repeat measurements at each randomly selected level may serve to increase the measurement accuracy, but does not increase the pertinent sample size. (However, taking repeat measurements does allow us to learn more about the treatment effect *at those* selected levels, e.g., a therapy may work well for you but is not effective on average.)

# Appendix: code

 snugshade
