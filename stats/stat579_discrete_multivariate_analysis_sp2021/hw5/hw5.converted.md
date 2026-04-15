# Problem 1

Consider data from a prospective study on the relationship between daily aspirin use and the onset of heart disease.

            Disease   No Disease   Total
  --------- --------- ------------ -------
  Placebo   28        656          684
  Aspirin   18        658          676

## Part (a)

[\\[\\begin{aligned} \\sigma\^2\\!\\left(\\log \\hat{\\operatorname{RR}}\\right) &= \\frac{1}{n\_{1 1}} - \\frac{1}{n\_{1+}} + \\frac{1}{n\_{2 1}} - \\frac{1}{n\_{2+}}\\\\ &= \\frac{1}{28} - \\frac{1}{684} + \\frac{1}{18} - \\frac{1}{658}\\\\ &\\approx 0.883\\,. \\end{aligned}\\]]{.math .display}

## Part (b)

[\\[\\sigma\\!\\left(\\log \\hat{\\operatorname{RR}}\\right) = \\sqrt{\\sigma\^2(\\log \\hat{\\operatorname{RR}})} \\approx 0.297\\,.\\]]{.math .display}

## Part (c)

The relative risk [\\(\\operatorname{RR}\\)]{.math .inline} is defined as [\\[\\operatorname{RR}\\coloneqq \\frac{\\pi_1}{\\pi_2}\\]]{.math .display} The MLE of [\\(\\log \\operatorname{RR}\\)]{.math .inline} is given by [\\[\\hat{\\operatorname{RR}} = \\frac{\\hat\\pi_1}{\\hat\\pi_2} = \\frac{n\_{1 1}}{n\_{1+}} \\frac{n\_{2+}}{n\_{2 1}} = \\frac{28}{676} \\times \\frac{684}{18} \\approx 1.574\\,.\\]]{.math .display} By the invariance property of the MLE, if [\\(\\hat\\theta\\)]{.math .inline} is an MLE of [\\(\\theta\\)]{.math .inline} then [\\(\\operatorname{g}(\\theta)\\)]{.math .inline} is an MLE of [\\(\\operatorname{g}(\\hat\\theta)\\)]{.math .inline}. Thus, [\\[\\log \\hat{\\operatorname{RR}} = \\log \\hat{\\operatorname{RR}} \\approx 0.454\\,.\\]]{.math .display} A confidence interval for [\\(\\log \\operatorname{RR}\\)]{.math .inline} is thus [\\[\\operatorname{CI}(\\log\\operatorname{RR}) = \\log \\hat{\\operatorname{RR}} \\pm z\_{\\alpha/2} \\sigma(\\log \\hat{\\operatorname{RR}})\\,.\\]]{.math .display} Letting [\\(\\alpha = 0.05\\)]{.math .inline} and substituting in the values for [\\(\\log \\hat{\\operatorname{RR}}\\)]{.math .inline} and [\\(\\sigma(\\log \\hat{\\operatorname{RR}})\\)]{.math .inline}, we get the result [\\[\\operatorname{CI}(\\log\\hat{\\operatorname{RR}}) = 0.454 \\pm 1.96 \\times 0.297= [-0.128,1.036]\\,.\\]]{.math .display}

## Part (d)

We take the inverse of the logarithm and obtain the result [\\[\\operatorname{CI}(\\operatorname{RR}) = [e\^{-0.128},e\^{1.036}] = [0.880,2.818]\\,.\\]]{.math .display}

# Problem 2

A diagnostic test for Covid antibodies is being studied. For a sample of [\\(n = 122\\)]{.math .inline} specimens with antibodies known to be present, the test returned [\\(y = 103\\)]{.math .inline} positive results. For a sample of [\\(n = 401\\)]{.math .inline} specimens absent any antibodies, the test returned [\\(y = 399\\)]{.math .inline} negative results.

## Function used to compute interval estimates for this problem.

 snugshade
 Highlighting
[*\# this program performs Bayesian inference for a binomial probability*]{style="color: 0.56,0.35,0.01"} [*\# - y is the number of successes*]{style="color: 0.56,0.35,0.01"} [*\# - n is the number of trials*]{style="color: 0.56,0.35,0.01"} [*\# - alpha is the sum of the tail probabilities*]{style="color: 0.56,0.35,0.01"} [*\#*]{style="color: 0.56,0.35,0.01"} [*\# we also compute a classical interval using normality assumptions of the mle.*]{style="color: 0.56,0.35,0.01"} binomial_bayesian [<-]{style="color: 0.56,0.35,0.01"} [function]{style="color: 0.13,0.29,0.53"}(y,n,[alpha=]{style="color: 0.13,0.29,0.53"}.[05]{style="color: 0.00,0.00,0.81"}) { [*\# compute the maximum likelihood estimator*]{style="color: 0.56,0.35,0.01"} mle [=]{style="color: 0.56,0.35,0.01"} y[**/**]{style="color: 0.81,0.36,0.00"}n mle_var [=]{style="color: 0.56,0.35,0.01"} mle[*****]{style="color: 0.81,0.36,0.00"}([1]{style="color: 0.00,0.00,0.81"}[**-**]{style="color: 0.81,0.36,0.00"}mle)[**/**]{style="color: 0.81,0.36,0.00"}n mle_sd [=]{style="color: 0.56,0.35,0.01"} [sqrt]{style="color: 0.13,0.29,0.53"}(mle_var)

t0 [=]{style="color: 0.56,0.35,0.01"} [qt]{style="color: 0.13,0.29,0.53"}([1]{style="color: 0.00,0.00,0.81"}[**-**]{style="color: 0.81,0.36,0.00"}alpha[**/**]{style="color: 0.81,0.36,0.00"}[2]{style="color: 0.00,0.00,0.81"}, n[-1]{style="color: 0.00,0.00,0.81"}) L [=]{style="color: 0.56,0.35,0.01"} mle [**-**]{style="color: 0.81,0.36,0.00"} mle_sd[*****]{style="color: 0.81,0.36,0.00"}t0 U [=]{style="color: 0.56,0.35,0.01"} mle [**+**]{style="color: 0.81,0.36,0.00"} mle_sd[*****]{style="color: 0.81,0.36,0.00"}t0

[*\# define the beta distribution parameters*]{style="color: 0.56,0.35,0.01"} a[=]{style="color: 0.56,0.35,0.01"}y[**+**]{style="color: 0.81,0.36,0.00"}[1]{style="color: 0.00,0.00,0.81"} b[=]{style="color: 0.56,0.35,0.01"}n[**-**]{style="color: 0.81,0.36,0.00"}y[**+**]{style="color: 0.81,0.36,0.00"}[1]{style="color: 0.00,0.00,0.81"}

[*\# computing a confidence interval by taking the upper and lower percentiles of*]{style="color: 0.56,0.35,0.01"} [*\# the beta distribution computing the median to represent the center of the*]{style="color: 0.56,0.35,0.01"} [*\# distribution*]{style="color: 0.56,0.35,0.01"} lower [=]{style="color: 0.56,0.35,0.01"} [qbeta]{style="color: 0.13,0.29,0.53"}(alpha[**/**]{style="color: 0.81,0.36,0.00"}[2]{style="color: 0.00,0.00,0.81"},a,b) median [=]{style="color: 0.56,0.35,0.01"} [qbeta]{style="color: 0.13,0.29,0.53"}(.[5]{style="color: 0.00,0.00,0.81"},a,b) upper [=]{style="color: 0.56,0.35,0.01"} [qbeta]{style="color: 0.13,0.29,0.53"}([1]{style="color: 0.00,0.00,0.81"}[**-**]{style="color: 0.81,0.36,0.00"}alpha[**/**]{style="color: 0.81,0.36,0.00"}[2]{style="color: 0.00,0.00,0.81"},a,b) [cat]{style="color: 0.13,0.29,0.53"}([\"bayesian estimate: \"]{style="color: 0.31,0.60,0.02"}, [c]{style="color: 0.13,0.29,0.53"}(lower,median,upper),[\"]{style="color: 0.31,0.60,0.02"}[**\\n**]{style="color: 0.81,0.36,0.00"}[\"]{style="color: 0.31,0.60,0.02"}) [cat]{style="color: 0.13,0.29,0.53"}([\"mle confidence interval estimate: \"]{style="color: 0.31,0.60,0.02"}, [c]{style="color: 0.13,0.29,0.53"}(L,mle,U),[\"]{style="color: 0.31,0.60,0.02"}[**\\n**]{style="color: 0.81,0.36,0.00"}[\"]{style="color: 0.31,0.60,0.02"})

[*\# create a grid of p for plotting. you may change to a smaller range than from*]{style="color: 0.56,0.35,0.01"} [*\# 0 to 1 to see the distribution better*]{style="color: 0.56,0.35,0.01"} p [=]{style="color: 0.56,0.35,0.01"} [seq]{style="color: 0.13,0.29,0.53"}([from=]{style="color: 0.13,0.29,0.53"}[max]{style="color: 0.13,0.29,0.53"}([0]{style="color: 0.00,0.00,0.81"},lower[*****]{style="color: 0.81,0.36,0.00"}.[965]{style="color: 0.00,0.00,0.81"}),[to=]{style="color: 0.13,0.29,0.53"}[min]{style="color: 0.13,0.29,0.53"}([1]{style="color: 0.00,0.00,0.81"},[1.035]{style="color: 0.00,0.00,0.81"}[*****]{style="color: 0.81,0.36,0.00"}upper),[length.out=]{style="color: 0.13,0.29,0.53"}[100]{style="color: 0.00,0.00,0.81"}) [*\# we are computing the beta density at each point in the grid*]{style="color: 0.56,0.35,0.01"} posterior [=]{style="color: 0.56,0.35,0.01"} [dbeta]{style="color: 0.13,0.29,0.53"}(p,a,b)

ps [=]{style="color: 0.56,0.35,0.01"} [rnorm]{style="color: 0.13,0.29,0.53"}([n=]{style="color: 0.13,0.29,0.53"}[1000000]{style="color: 0.00,0.00,0.81"},[mean=]{style="color: 0.13,0.29,0.53"}mle,[sd=]{style="color: 0.13,0.29,0.53"}mle_sd)

[*\# plotting the beta density, higher values of the curve represent stronger data*]{style="color: 0.56,0.35,0.01"} [*\# evidence*]{style="color: 0.56,0.35,0.01"} [plot]{style="color: 0.13,0.29,0.53"}(p,posterior,[type =]{style="color: 0.13,0.29,0.53"} [\"l\"]{style="color: 0.31,0.60,0.02"},[col=]{style="color: 0.13,0.29,0.53"}[\"blue\"]{style="color: 0.31,0.60,0.02"})

[lines]{style="color: 0.13,0.29,0.53"}([density]{style="color: 0.13,0.29,0.53"}(ps),[col=]{style="color: 0.13,0.29,0.53"}[\"orange\"]{style="color: 0.31,0.60,0.02"})

[points]{style="color: 0.13,0.29,0.53"}(median,[0]{style="color: 0.00,0.00,0.81"},[col=]{style="color: 0.13,0.29,0.53"}[\"blue\"]{style="color: 0.31,0.60,0.02"},[pch=]{style="color: 0.13,0.29,0.53"}[\"*\"]{style="color: 0.31,0.60,0.02"}) [points]{style="color: 0.13,0.29,0.53"}([c]{style="color: 0.13,0.29,0.53"}(lower,upper),[c]{style="color: 0.13,0.29,0.53"}([0]{style="color: 0.00,0.00,0.81"},[0]{style="color: 0.00,0.00,0.81"}),,[col=]{style="color: 0.13,0.29,0.53"}[\"blue\"]{style="color: 0.31,0.60,0.02"},[pch=]{style="color: 0.13,0.29,0.53"}[\"\|\"]{style="color: 0.31,0.60,0.02"})

[*\# lets plot the mle and confidence interval using t-score*]{style="color: 0.56,0.35,0.01"} [points]{style="color: 0.13,0.29,0.53"}(mle,[0]{style="color: 0.00,0.00,0.81"},[col=]{style="color: 0.13,0.29,0.53"}[\"orange\"]{style="color: 0.31,0.60,0.02"},[pch=]{style="color: 0.13,0.29,0.53"}[\"*\"]{style="color: 0.31,0.60,0.02"}) [points]{style="color: 0.13,0.29,0.53"}([c]{style="color: 0.13,0.29,0.53"}(L,U),[c]{style="color: 0.13,0.29,0.53"}([0]{style="color: 0.00,0.00,0.81"},[0]{style="color: 0.00,0.00,0.81"}),,[col=]{style="color: 0.13,0.29,0.53"}[\"orange\"]{style="color: 0.31,0.60,0.02"},[pch=]{style="color: 0.13,0.29,0.53"}[\"\|\"]{style="color: 0.31,0.60,0.02"}) }

## Part (a)

Given that antibodies are present, the probability that a positive test result is observed is given by the sensitivity [\\(\\delta\\)]{.math .inline}.

In classical statistics, while the probability [\\(\\delta\\)]{.math .inline} is not known, the MLE estimator is [\\(\\hat\\delta = \\frac{y}{n}\\)]{.math .inline} which is asymptotically normal under regularity conditions.

We compare it with the Bayesian approach, which does not assume normality. The following R function call computes the Bayesian interval estimate for a binomial probability. For comparison, we also compute the confidence interval for the MLE using classical techniques that rely upon the normality assumption of the MLE.

 snugshade
 Highlighting
[binomial_bayesian]{style="color: 0.13,0.29,0.53"}([y=]{style="color: 0.13,0.29,0.53"}[103]{style="color: 0.00,0.00,0.81"},[n=]{style="color: 0.13,0.29,0.53"}[122]{style="color: 0.00,0.00,0.81"},[alpha=]{style="color: 0.13,0.29,0.53"}.[05]{style="color: 0.00,0.00,0.81"})

    ## bayesian estimate:  0.7693298 0.8405335 0.8977577 
    ## mle confidence interval estimate:  0.7792689 0.8442623 0.9092557

The maximum likelihood estimator [\\(\\hat\\delta\\)]{.math .inline} is [\\(0.844\\)]{.math .inline} with an [\\(\\alpha=0.05\\)]{.math .inline} confidence interval [\\([0.779,0.909]\\)]{.math .inline}.

The point estimator of [\\(\\delta\\)]{.math .inline} using the Bayesian approach, the [\\(50\\%\\)]{.math .inline}-percentile, is [\\(0.841\\)]{.math .inline} with an interval estimate [\\([0.769,0.898]\\)]{.math .inline}.

The maximum likelihood estimator and its corresponding density plot and confidence interval is plotted in *orange* and the Bayesian estimator is plotted in *blue*.

## Part (b)

We do the same thing as in part (A).

 snugshade
 Highlighting
[binomial_bayesian]{style="color: 0.13,0.29,0.53"}([y=]{style="color: 0.13,0.29,0.53"}[399]{style="color: 0.00,0.00,0.81"},[n=]{style="color: 0.13,0.29,0.53"}[401]{style="color: 0.00,0.00,0.81"},[alpha=]{style="color: 0.13,0.29,0.53"}.[05]{style="color: 0.00,0.00,0.81"})

    ## bayesian estimate:  0.9821445 0.9933537 0.9984584 
    ## mle confidence interval estimate:  0.9880966 0.9950125 1.001928

The maximum likelihood estimator [\\(\\hat\\delta\\)]{.math .inline} is [\\(0.844\\)]{.math .inline} with an [\\(\\alpha=0.05\\)]{.math .inline} confidence interval [\\([0.982,1.002]\\)]{.math .inline}

The point estimator of [\\(\\delta\\)]{.math .inline} using the Bayesian approach, the [\\(50\\%\\)]{.math .inline}-percentile, is [\\(0.993\\)]{.math .inline} with a [\\(\\alpha=0.05\\)]{.math .inline} interval estimate [\\([0.982,0.998]\\)]{.math .inline}.

The maximum likelihood estimator and its corresponding density plot and confidence interval is plotted in *orange* and the Bayesian estimator is plotted *blue*.

# Problem 3

The interval estimate is computed by the following R code.

 snugshade
 Highlighting
[*\# this program performs a Bayesian inference for vaccine efficacy*]{style="color: 0.56,0.35,0.01"} [*\# enter the number of infections in the vaccine group*]{style="color: 0.56,0.35,0.01"} [*\# and the number of infections in the control group*]{style="color: 0.56,0.35,0.01"} v [=]{style="color: 0.56,0.35,0.01"} [11]{style="color: 0.00,0.00,0.81"} c [=]{style="color: 0.56,0.35,0.01"} [185]{style="color: 0.00,0.00,0.81"}

[*\# define the beta distribution parameters*]{style="color: 0.56,0.35,0.01"} a [=]{style="color: 0.56,0.35,0.01"} v[**+**]{style="color: 0.81,0.36,0.00"}[1]{style="color: 0.00,0.00,0.81"} b [=]{style="color: 0.56,0.35,0.01"} c[**+**]{style="color: 0.81,0.36,0.00"}[1]{style="color: 0.00,0.00,0.81"}

[*\# simulate a very large number of draws from the posterior distribution on p=P(V\|I)*]{style="color: 0.56,0.35,0.01"} [*\# for each simulated p, compute the value for vaccine efficacy VE*]{style="color: 0.56,0.35,0.01"} p [=]{style="color: 0.56,0.35,0.01"} [rbeta]{style="color: 0.13,0.29,0.53"}([1000000]{style="color: 0.00,0.00,0.81"},a,b) efficacy [=]{style="color: 0.56,0.35,0.01"} [1]{style="color: 0.00,0.00,0.81"}[**-**]{style="color: 0.81,0.36,0.00"}p[**/**]{style="color: 0.81,0.36,0.00"}([1]{style="color: 0.00,0.00,0.81"}[**-**]{style="color: 0.81,0.36,0.00"}p)

[*\# create a plot of the posterior distribution on VE*]{style="color: 0.56,0.35,0.01"} [hist]{style="color: 0.13,0.29,0.53"}(efficacy,[xlab=]{style="color: 0.13,0.29,0.53"}[\"Efficacy\"]{style="color: 0.31,0.60,0.02"},[probability =]{style="color: 0.13,0.29,0.53"} [TRUE]{style="color: 0.56,0.35,0.01"}) [points]{style="color: 0.13,0.29,0.53"}([density]{style="color: 0.13,0.29,0.53"}(efficacy),[type =]{style="color: 0.13,0.29,0.53"} [l]{style="color: 0.31,0.60,0.02"})

pt_est [=]{style="color: 0.56,0.35,0.01"} [quantile]{style="color: 0.13,0.29,0.53"}(efficacy,[c]{style="color: 0.13,0.29,0.53"}(.[5]{style="color: 0.00,0.00,0.81"})) [points]{style="color: 0.13,0.29,0.53"}(pt_est,[0]{style="color: 0.00,0.00,0.81"},[col=]{style="color: 0.13,0.29,0.53"}[\"blue\"]{style="color: 0.31,0.60,0.02"},[pch=]{style="color: 0.13,0.29,0.53"}[8]{style="color: 0.00,0.00,0.81"})

[*\# compute percentiles for a 95% interval estimate*]{style="color: 0.56,0.35,0.01"} interval_est [=]{style="color: 0.56,0.35,0.01"} [quantile]{style="color: 0.13,0.29,0.53"}(efficacy,[c]{style="color: 0.13,0.29,0.53"}(.[025]{style="color: 0.00,0.00,0.81"},.[975]{style="color: 0.00,0.00,0.81"})) [points]{style="color: 0.13,0.29,0.53"}(interval_est,[c]{style="color: 0.13,0.29,0.53"}([0]{style="color: 0.00,0.00,0.81"},[0]{style="color: 0.00,0.00,0.81"}),[col=]{style="color: 0.13,0.29,0.53"}[\"red\"]{style="color: 0.31,0.60,0.02"},[pch=]{style="color: 0.13,0.29,0.53"}[\"\|\"]{style="color: 0.31,0.60,0.02"})

 snugshade
 Highlighting
[print]{style="color: 0.13,0.29,0.53"}(pt_est)

    ##       50% 
    ## 0.9371837

 snugshade
 Highlighting
[print]{style="color: 0.13,0.29,0.53"}(interval_est)

    ##      2.5%     97.5% 
    ## 0.8916741 0.9670500

We see that the density plot is not quite normal (e.g., non-symmetric). On the plot, we plotted the [\\(50\\%\\)]{.math .inline} in blue and the [\\(95\\%\\)]{.math .inline} interval estimate in red.
