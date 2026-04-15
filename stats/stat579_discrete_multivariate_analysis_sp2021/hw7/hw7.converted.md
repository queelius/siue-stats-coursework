# Problem 1

Consider an experiment on chlorophyll inheritance in maize. A genetic theory predicts the ratio of green to yellow to be 3:1. In a sample of [\\(n = 1103\\)]{.math .inline} seedlings, [\\(n_1 = 854\\)]{.math .inline} were green and [\\(n_2 = 249\\)]{.math .inline} were yellow.

## Part (a)

The statistic is defined as [\\[X\^2 = \\sum\_{j=1}\^{c} \\frac{(n_j - n \\pi\_{j 0})\^2}{n \\pi\_{j 0}}.\\]]{.math .display}

Under the null model, the odds are 3:1, or [\\(\\pi\_{1 0} = 0.75\\)]{.math .inline} and [\\(\\pi\_{1 1} = 0.25\\)]{.math .inline}. We are given [\\(n = 1103\\)]{.math .inline}, [\\(n_1 = 854\\)]{.math .inline}, and [\\(n_2 = 249\\)]{.math .inline}. Under the null model, these values have expectations given respectively by [\\(n \\pi\_{1 0} = 827.25\\)]{.math .inline} and [\\(275.75\\)]{.math .inline}.

The observed statistic is thus given by [\\[X_0\^2 = \\frac{(854 - 827.25)\^2}{827.25} + \\frac{(249 - 275.75)\^2}{275.75} = 3.46.\\]]{.math .display}

## Part (b)

The reference distribution is the chi-squared distribution with [\\(1\\)]{.math .inline} degree of freedom, denoted by [\\(\\chi\^2(1)\\)]{.math .inline}.

The upper 10th percentile given [\\(1\\)]{.math .inline} degree of freedom, denoted by [\\(\\chi\_{0.10}\^2(1)\\)]{.math .inline}, is found by solving for [\\(\\chi\_{0.10}\^2(1)\\)]{.math .inline} in the equation [\\(\\Pr(\\chi\^2(1) \\geq \\chi\_{0.10}\^2(1)) = 1-0.10 = 0.9\\)]{.math .inline}, which yields the result [\\[\\chi\_{0.10}\^2(1) = 2.71.\\]]{.math .display}

## Part (c)

We see that any observed statistic [\\(X_0\^2\\)]{.math .inline} with [\\(\\rm{df}=1\\)]{.math .inline} greater than [\\(\\chi\^2\_{0.10}(1) = 2.71\\)]{.math .inline} is not compatible with the null model at significance level [\\(\\alpha = 0.10\\)]{.math .inline}.

Since the observed statistic [\\(X_0\^2 = 3.46 \> 2.71\\)]{.math .inline}, the null model, which is the genetic theory where the ratio of green to yellow is 3:1, is not compatible with the data.

## Part (d)

Hypothesis testing, as a dichotomous measure of evidence, does not provide as much information as a more quantitative evidence measure. For instance, it does not provide information about *effect size*.

# Problem 2

## Part (a)

The MLE of [\\(\\pi_1\\)]{.math .inline} is given by [\\(\\hat{\\pi}\_1 = \\frac{n_1}{n} = \\frac{854}{1103} = 0.774\\)]{.math .inline}. Letting [\\(\\alpha = 0.10\\)]{.math .inline} and inverting the Wald test statistic, we get the [\\(90\\%\\)]{.math .inline} confidence interval for [\\(\\pi_1\\)]{.math .inline}, [\\[\\hat{\\pi}\_1 \\pm z\_{1-alpha/2} \\sigma\_{\\hat\\pi} = 0.744 \\pm 1.645 \\sqrt{\\frac{0.774(1-0.774)}{1103}},\\]]{.math .display} which may be rewritten as [\\[[0.754, 0.795].\\]]{.math .display}

## Part (b)

Based on the observed data, we estimate that the probability [\\(\\pi_1\\)]{.math .inline} of a green strain is between [\\(0.754\\)]{.math .inline} and [\\(0.795\\)]{.math .inline}.

As expected, the null model specifies a value for [\\(\\pi_1\\)]{.math .inline} ([\\(0.75\\)]{.math .inline}) that is not contained in this confidence interval.
