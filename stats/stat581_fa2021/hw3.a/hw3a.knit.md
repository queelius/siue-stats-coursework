---
title: 'STAT 581 - HW #3'
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

An experiment is conducted to study the effect of drilling method on drilling
time.
Each method (dry drilling, wet drilling) is used on $n = 12$ rocks.
Drilling times are measured in $1/100$ minutes.

## Part (a)
\fbox{\begin{minipage}{\textwidth}
Compute a $95\%$ confidence interval for $\delta = \mu_1 - \mu_2$.
Provide an interpretation, stated in the context of the problem.
\end{minipage}}

A confidence interval for $\delta$ includes all parameter values compatible with
the observed data $\hat\delta$,
$$
  \delta \in \left[
    \hat\delta + t_{\alpha/2,2(n-1)} s_p \sqrt{2/n},
    \hat\delta + t_{1-\alpha/2,2(n-1)} s_p \sqrt{2/n}
  \right].
$$

We compute this CI with:

``` r
library("readxl")
data = read_excel("./handout1data.xlsx")
data$method = as.factor(data$method)
dry = na.omit(data$time[data$method=='d'])
wet = na.omit(data$time[data$method!='d'])
alpha = .05

t.test(x=dry,
       y=wet,
       alternative=c("two.sided"),
       conf.level=1-alpha,
       var.equal=T)$conf.int[1:2]
```

```
## [1] 126.8757 276.4576
```

We estimate that the difference in drilling methods,
$\delta = (\rm{dry} - \rm{wet})$, is between $[126.876,276.458]$.

## Part (b)
\fbox{\begin{minipage}{\textwidth}
Explain how a confidence interval provides a complementary result to a
hypothesis test.
\end{minipage}}

A hypothesis test looks to determine if an effect exists.
A CI looks to determine the size of the effect.

# Problem 2
A prodcut developer is investigating the tensile strength of a new synthetic
fiber.
A completely randomized design with five levels of cotton content is performed,
with $n=5$ speciments per level.

## Part (a)
\fbox{\begin{minipage}{\textwidth}
Compute and display $95\%$ confidence intervals for all pairwise comparisons.
\end{minipage}}

We show the confidence intervals with:










