# Problem 1

If we have a non-linear function of some random variable, in the delta method we use a Taylor approximation of the function centered around the random variables expected value such that the approximate variance of the function of the random variable is easily computed.

Let [\\(\\operatorname{g}(\\hat\\pi) = \\log(\\hat\\pi/(1-\\hat\\pi))\\)]{.math .inline}. A linear approximation of [\\(\\operatorname{g}\\)]{.math .inline} is given by [\\[\\operatorname{\\hat g}(\\hat\\pi) = \\operatorname{g}(\\pi) +\\operatorname{g\'}(\\pi)(\\hat\\pi - \\pi),\\]]{.math .display} the derivative of [\\(\\operatorname{g}\\)]{.math .inline} is given by [\\[\\operatorname{g\'}(\\pi) = \\frac{1}{\\pi(1-\\pi)},\\]]{.math .display} and the variance of [\\(\\operatorname{\\hat g}(\\hat\\pi)\\)]{.math .inline} is given by [\\[\\begin{aligned} \\operatorname{Var}(\\operatorname{\\hat g}(\\hat \\pi)) &= \\left(\\operatorname{g\'}(\\pi)\\right)\^2 \\operatorname{Var}(\\hat\\pi)\\\\ &= \\frac{1}{\\pi\^2(1-\\pi)\^2} \\frac{\\pi(1-\\pi)}{n}\\\\ &= \\frac{1}{\\pi(1-\\pi)} \\frac{1}{n}. \\end{aligned}\\]]{.math .display}

Since we do not know [\\(\\pi\\)]{.math .inline}, we approximate it with [\\(\\hat\\pi\\)]{.math .inline}, thus [\\[\\sigma\^2(\\log(\\hat\\pi/(1-\\hat\\pi))) = \\frac{1}{\\hat\\pi(1-\\hat\\pi)} \\frac{1}{n}.\\]]{.math .display} \# Problem 2

Consider data from a retrospective study on the relationship between daily alcohol consumption and the onset of esophagus cancer.

                                          cancer   no cancer
  ----- ------------------------------- -------- -----------
    3-4   [\\(\> 80\\)]{.math .inline}g       71          82
          [\\(\< 80\\)]{.math .inline}g       60         441
                                  total      131         523

## Part (a)

In a retrospective study, the table draws samples from the conditional probabilities [\\(\\operatorname{P}(X = i \| Y = j)\\)]{.math .inline} and we denote [\\(\\operatorname{P}(X = 1 \| Y = j)\\)]{.math .inline} by [\\(p_j\\)]{.math .inline}.

The ML estimator of [\\(p_j\\)]{.math .inline} from the data in a retrospective study is given by [\\[\\hat p_j = \\frac{n\_{1 j}}{n\_{+j}}.\\]]{.math .display}

In a retrospective study, an estimator of [\\(\\sigma(\\log \\hat\\theta)\\)]{.math .inline} is given by [\\[\\hat\\sigma(\\log \\hat\\theta) = \\left[ \\left(\\frac{1}{\\hat{p}\_1} + \\frac{1}{1-\\hat{p}\_1}\\right)\\frac{1}{n\_{+1}} + \\left(\\frac{1}{\\hat{p}\_2} + \\frac{1}{1-\\hat{p}\_2}\\right)\\frac{1}{n\_{+2}} + \\right]\^{1/2}.\\]]{.math .display}

## Part (b)

It does not depend on the sampling scheme. When asymptotic normality holds, replacing parameters with statistics invokes the likelihood principle.

When we substitute the MLE [\\(\\hat p_j\\)]{.math .inline} into the equation for [\\(\\hat \\sigma(\\log \\hat \\theta)\\)]{.math .inline}, we get the result [\\[\\hat\\sigma(\\log \\hat\\theta) = \\left(\\frac{1}{n\_{1 1}} + \\frac{1}{n\_{2 1}} + \\frac{1}{n\_{1 2}} + \\frac{1}{n\_{2 2}} \\right)\^{1/2},\\]]{.math .display} which is the same as for retrospective studies and cross-sectional studies.

## Part (c)

Recall [\\(\\theta = \\frac{p_1 / (1 - p_1)}{p_2 / (1 - p_2)}\\)]{.math .inline}. If we replace [\\(p_j\\)]{.math .inline} by its ML estimator [\\(\\hat p_j\\)]{.math .inline}, then [\\[\\hat p_1 = \\frac{n\_{1 1}}{n\_{+1}} = \\frac{71}{131} \\approx 0.542\\]]{.math .display} and [\\[\\hat p_2 = \\frac{n\_{1 2}}{n\_{+2}} = \\frac{82}{523} \\approx 0.157.\\]]{.math .display} Thus, by the invariance property of MLEs, [\\[\\hat\\theta = \\frac{\\hat p_1 / (1 - \\hat p_1)}{\\hat p_2 / (1 - \\hat p_2)} \\approx \\frac{0.542 / 0.458}{0.157 / 0.843} \\approx 6.354\\]]{.math .display} and therefore [\\(\\log \\theta \\approx \\log 6.354 \\approx 1.850\\)]{.math .inline}. Next, we need to find the standard deviation of the [\\(\\log \\hat\\theta\\)]{.math .inline}, [\\[\\hat\\sigma(\\log \\hat\\theta) = \\left[ \\left(\\frac{1}{0.542} + \\frac{1}{0.458}\\right)\\frac{1}{131} + \\left(\\frac{1}{0.157} + \\frac{1}{0.843}\\right)\\frac{1}{523} \\right]\^{1/2} \\approx 0.213.\\]]{.math .display}

Thus, a [\\(95\\%\\)]{.math .inline} confidence interval for [\\(\\log \\theta\\)]{.math .inline} is [\\[\\log \\hat \\theta \\pm 1.96 \\hat\\sigma(\\log \\hat \\theta).\\]]{.math .display} Plugging in these computed values, we get the [\\(95\\%\\)]{.math .inline} confidence interval [\\[[1.850 - 0.417,1.850 + 0.417] = [1.433,2.267].\\]]{.math .display}

## Part (d)

Observe that [\\[\\hat\\gamma = \\frac{\\hat\\theta-1}{\\hat\\theta+1}.\\]]{.math .display} The MLE [\\(\\hat\\theta \\approx 6.354\\)]{.math .inline}. Thus, [\\(\\hat\\gamma \\approx \\frac{6.354-1}{6.354+1} \\approx 0.728\\)]{.math .inline}.

We estimate that there is a *large* size, positive association between daily alcohol consumption and the onset of cancer.

# Problem 3

For the *counts* array, we populated it with the values [\\((7,7,2,3,2,8,3,7,1,5,4,9,2,8,9,14)\\)]{.math .inline} and ran the code.

    ##       2.5%        25%        50%        75%      97.5% 
    ## 0.09879317 0.24392244 0.31425372 0.38217439 0.50166928

Thus, a [\\(95\\%\\)]{.math .inline} interval estimate is approximately [\\([0.1,0.5]\\)]{.math .inline}.
