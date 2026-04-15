---
title: 'STAT 581 - HW #2'
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



A product developer is investigating the tensile strength of a new synthetic
fiber that will be used to make cloth for men's shirts.
Strength may be affected by the percentage of cotton used in the blend of
material for the fiber.
A completely randomized experiment with five levels of cotton content is
performed.

# Part 1
\fbox{State the statistical hypothesis of interest.}

The hypothesis of interest is whether the percentage of cotton at five
different levels effects the tensile strength of a new synthetic fiber.

We may formulate this as a hypothesis test of the form
\begin{align*}
  H_0 &: \mu_1 = \cdots = \mu_5\\
  H_A &: \text{$\mu_i \neq \mu_j$ for at least one pair $(i,j)$, $i\neq j$,}
\end{align*}
where $\mu_k$ is the expected tensile strength at the $k$-th level of cotton.

If $H_0$ is true, the percentage of cotton has no effect on tensile strength.

# Part 2
\fbox{Briefly explain how the form of the alternative hypothesis requires a need
for further investigation.}

If there are differences in the cotton level means, further investigation is
required to determine where the differences occur.

# Part 3
\fbox{Create a Boxplot as a graphical display of the data.}


``` r
library(printr)
library("readxl")

h2.data = read_excel("./handout2data.xlsx")
strength = na.omit(h2.data$strength)
percent = na.omit(as.factor(h2.data$percent))

boxplot(strength~percent)
```

![](hw2_files/figure-latex/unnamed-chunk-2-1.pdf)<!-- --> 

# Part 4
\fbox{Compute the sample mean and sample variance of tensile strength for each level of cotton percentage.}


``` r
means = by(strength,percent,mean)
variances = by(strength,percent,var)
cbind(means,variances)
```



|   | means| variances|
|:--|-----:|---------:|
|15 |   9.8|      11.2|
|20 |  15.4|       9.8|
|25 |  17.6|       4.3|
|30 |  21.6|       6.8|
|35 |  10.8|       8.2|

# Part 5
\fbox{State the ANOVA model using treatment level effects. Compute estimates of the model parameters.}

In this CRD experiment, we observe $n=5$ responses at each of $a=5$ levels of
cotton (we treat the cotton percentage level as categorical, even though if we
show that the cotton level has a practical effect on tensile strength, we may
treat it as a quantitative input in, say, a regression model).

The data is given by
\begin{align*}
  Y_{1 1},\ldots,Y_{1 5} &\sim \mathcal{N}(\mu+\tau_1,\sigma^2)\\
  &\vdots\\
  Y_{5 1},\ldots,Y_{5 5} &\sim \mathcal{N}(\mu+\tau_5,\sigma^2).
\end{align*}

The model is given by
$$
  Y_{i j} = \mu + \tau_i + \epsilon_{i j}
  \begin{cases}
    i = 1,\ldots,5\\
    j = 1,\ldots,5,
  \end{cases}
$$
where
\begin{align*}
  Y_{i j}               &\qquad\text{is the $j$-th response for tensile strength for the $i$-th cotton level},\\
  \mu                   &\qquad\text{is the overall mean of the tensile strength},\\
  \tau_i                &\qquad\text{is the effect that the $i$-th cotton level has on the tensile strength},\\
  \epsilon_{i j}        &\qquad\overset{\rm{iid}}{\sim} \mathcal{N}(0,\sigma^2),\\
  \sum_{i=1}^{5} \tau_i &\qquad= 0.
\end{align*}

The estimates of the model parameters are given by
\begin{align*}
  \hat{\mu}       &= \bar{y}_{\cdot \cdot},\\
  \hat{\tau}_i    &= \bar{y}_{i \cdot} - \bar{y}_{\cdot \cdot}.
\end{align*}

We compute these estimates with the following R code:

``` r
mu.hat = mean(strength)
tau.hat = means - mu.hat
```

We see that $\hat{\mu} = 15.04$ and

| cotton level| $\hat{\tau}$|
|------------:|------------:|
|           15|        -5.24|
|           20|         0.36|
|           25|         2.56|
|           30|         6.56|
|           35|        -4.24|

# Part 6

## Part (a)
\fbox{\begin{minipage}{\textwidth}
Compute the $F_0$ statistic and the $p$-value.
Perform the statistical test at level $\alpha = .05$.
Provide an interpretation, stated in the context of the problem.
\end{minipage}}


``` r
model.2 = aov(strength~percent)
summary(model.2)
```

```
##             Df Sum Sq Mean Sq F value   Pr(>F)    
## percent      4  475.8  118.94   14.76 9.13e-06 ***
## Residuals   20  161.2    8.06                     
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
```

We see that $F_0 = 14.76$ and the $p$-value $= .000$.
Thus, since $p = .000 < \alpha = .05$, the null model where cotton level
has no effect on tensile strength is not compatible with the data.

## Part (b)
\fbox{\begin{minipage}{\textwidth}
Compute the $t_0$ statistic and the $p$-value for testing the $30\%$ group
versus the $25\%$ group.
Provide an interpretation, stated in the context of the problem.
\end{minipage}}

All pair-wise hypothesis tests
\begin{align*}
  H_0^{(i,j)} &: \tau_i = \tau_j\\
  H_A^{(i,j)} &: \tau_i \neq \tau_j.
\end{align*}
may be computed with the following R code:




