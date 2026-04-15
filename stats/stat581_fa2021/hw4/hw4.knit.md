---
title: 'STAT 581 - Problem Set 4'
author: "Alex Towell (atowell@siue.edu)"
output:
  #md_document:
  #  variant: markdown_github
  pdf_document:
    df_print: kable
    latex_engine: xelatex
    #keep_tex: true
    highlight: tango
    #highlight: breezedark
    #highlight: pygments
    #highlight: zenburn
    #highlight: haddock
    #highlight: kate
    #highlight: espresso
fontsize: 11pt
geometry: margin=.5in
documentclass: article
#documentclass: paper
#documentclass: standalone
#classoption: twocolumn
header-includes:
 - \usepackage{amsmath}
 - \usepackage{mathtools}
 - \usepackage{amsthm}
 # - \usepackage{amsbsy}
 - \usepackage{bm}
 - \usepackage{xcolor}
 - \usepackage{fbox}
 - \usepackage{amsmath}
 - \usepackage{hw4}
---




# Problem 1
The insulating life of protective fluids at an accelerated load is being
studied. The experiment has been performed for four types of fluids, with $n = 5$
trials per fluid type.
Suppose fluid types 1 and 2 are from manufacturer A, and that fluid types 3 and 4
are from manufacturer B.
The data is available on Blackboard as an Excel File.

## (a)

### (i)
\fbox{\begin{minipage}{\textwidth}
Perform a test of the global null hypothesis $H_0 : \mu_1 = \mu_2 = \mu_3 = \mu_4$.
Compute the $F_0$ statistic, and the $p$-value.
\end{minipage}}

This is a one-factor experiment with $a=4$ levels of the factor (fluid level)
and $n=6$ replicates for a total of $N = a n = 24$ observations.

The test statistic
$$
  F_0 = \frac{\mstr}{\mse} 
$$
under the null hypothesis $\mu_1 = \ldots = \mu_a$ (or $\tau_1 = \ldots = \tau_a = 0$
in the effects model) has a reference distribution
$$
  F_0 \sim F(a-1,N-a)
$$
where $N = n a$.

We compute the observed test statistic and its $p$-value with:

``` r
library("readxl")
h4.data = read_excel("handout2data.xlsx")
fluid = as.factor(na.omit(h4.data$fluid))
life = na.omit(h4.data$life)
#head(data.frame(fluid=fluid,life=life))

aov.mod = aov(life ~ fluid)
summary(aov.mod)
```

```
##             Df Sum Sq Mean Sq F value Pr(>F)  
## fluid        3  30.16   10.05   3.047 0.0525 .
## Residuals   20  65.99    3.30                 
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
```

We see that $F_0 = 3.047$ which has a $p$-value $.0525$.

### (ii)
\fbox{\begin{minipage}{\textwidth}
Comment on the additional information provided by the $p$-value, beyond a
determination of statistical significance alone.
\end{minipage}}

The $p$-value quantifies a measure of evidence beyond a determination of
statistical significance.

Earlier, we obtained a $p$-value of $.0525$.
If we were to perform a dichotomous hypothesis test which specifies a
significance level $\alpha = 0.05$, we would decide $H_0$.
However, had we obtained a $p$-value of $.049$, while the strength of the evidence
is nearly the same, we would decide $H_A$.
Presenting the $p$-value provides more information.

## (b)
Consider the orthogonal contrasts
\begin{align*}
  \Gamma_1 &= \mu_1 - \mu_2\\
  \Gamma_2 &= \mu_3 - \mu_4\\
  \Gamma_3 &= (\mu_1 + \mu_2) - (\mu_3 + \mu_4).
\end{align*}

### Preliminary analysis

A \emph{constrast} $\Gamma$ is a linear combination of parameters
$$
  \Gamma = \sum_{i=1}^{a} c_i \mu_i
$$
such that $c_1 + \cdots + c_a = 0$.
Assuming a balanced design,
$$
  \var(\sum_{i=1}^{a} c_i \bar{y}_{i\cdot}) = \frac{\sigma^2}{n} \sum_{i=1}^{a} c_i^2
$$
and thus
$$
  t_0 = \frac{\sum_{i=1}^{a} c_i \bar{y}_{i\cdot}}{\left(\mse/n \sum_{i=1}^{a} c_i\right)^{1/2}} \sim t_{N-a}
$$
under $H_0$.
The $F$-test may also be used, where $F_0 = t_0^2 = \frac{\msc}{\mse} = \frac{\ssc/1}{\mse}$
where
$$
  \ssc = \frac{(\sum_{i=1}^{a} c_i \bar{y}_{i\cdot})^2}{1/n \sum_{i=1}^{a} c_i^2} \sim t_{N-a}.
$$

We have $a=4$ fluid types, $1$, $2$, $3$, and $4$.
Fluid types $1$ and $2$ are from manufacturer $A$ and
fluid types $3$ and $4$ are from manufacturer $B$.

$\Gamma_1$ compares the average effect (on lifetime) of fluid $1$ with
the average effect of fluid $2$, $\Gamma_2$ compares the average effect of fluid $3$ with
the average effect of fluid $4$, and $\Gamma_3$ compares the average effect of manufacturer $A$ with
the average effect of manufacturer $B$.

### (i)
\fbox{\begin{minipage}{\textwidth}
Compute SSC for each contrast.
Describe a general property for the sums of squares of orthogonal contrasts.
Why is this property desirable?
\end{minipage}}

### Orthogonal contrasts
Orthogonality is desirable since the treatment sum of squares can be
decomposed into specific effects.

Additional remarks:

Two contrasts (assuming a balanced design) with coefficients $\{c_i\}$ and
$\{d_i\}$ are orthogonal if $\sum_{i=1}^{a} c_i d_i = 0$.

For $a$ factor levels (or treatments), a set of $(a-1)$ orthogonal contrasts
$\Gamma_1,\ldots,\Gamma_{a-1}$ are independent with $\operatorname{df} = 1$ and
thus tests performed on them are independent.

We see that $\Gamma_1$, $\Gamma_2$, and $\Gamma_3$ are orthogonal contrasts.

### Computing $\ssc$

















