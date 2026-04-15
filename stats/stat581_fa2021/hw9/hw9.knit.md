---
title: 'STAT 581 - Problem Set 9'
author: "Alex Towell (atowell@siue.edu)"
output:
  pdf_document:
    #df_print: kable
    latex_engine: xelatex
    #keep_tex: true
    highlight: tango
header-includes:
 - \usepackage{custom}
editor_options:
  markdown:
    wrap: 80
---

# Problem 1
> The surface finish of metal parts made on $a=4$ machines is under
> investigation.
> Each machine can be run by one of $b=3$ operators.
> Because of the location of the machines, operators are specific to a
> particular machine.
> Therefore, a nested design with fixed factors is used.
> Each operator produces $n=2$ samples.
> The data is availabe on Blackboard as an Excel File.

## Part (a)
> Explain the difference between crossed factors and nested factors.

Factors $A$ and $B$ are *crossed* in an experimental design if the levels of $B$
are the same at each level of $A$.

Factor $B$ is *nested* within factor $A$ if the levels of $B$ are different
for each of the levels of factor $A$.

## Part (b)
> Write the model for a nested design.
> Provide algebraic formulas for the estimates $\hat{\tau}_i$ and $\hat{\beta})_{j(i)}$.

Given that $A$ and $B$ are fixed factors,
$$
  Y_{i j k} = \mu + \tau_i + \beta_{j(i)} + \epsilon_{i j k}
  \begin{cases}
    i = 1,\ldots,a\\
    j = 1,\ldots,b\\
    k = 1,\ldots,n
  \end{cases}
$$
where $\{\tau_i\}$ ($\sum_i \tau_i = 0$) with $\df{A}=a-1$
and $\{\beta_(j(i))\}$ ($\sum_j \beta_{j(i)} = 0$ for $i=1,\ldots,a$) with
$\df{B} = a(b-1)$ are fixed effects.

Estimators are given by
$$
  \hat{\tau}_i = \bar{Y}_{i\cdot\cdot} - \bar{Y}_{\cdot\cdot\cdot}
$$
and
$$
  \hat{\beta}_{j(i)} = \bar{Y}_{i j \cdot} - \bar{Y}_{i \cdot\cdot}.
$$

We see that level factors of $A$ are compared with $\{\hat{\tau}_i\}$ while level
factors of $B$ are compared only with the same level of $A$, e.g., at the $i$-th
level of $A$, level factors of $B$ are compared with $\{\beta_j(i) \}$.

## Part (c)
> Compute the $F_A$ statistic for testing factor $A$ effects, and the $F_{B(A)}$
> statistic for testing nested factor $B$ effects.
> Compute the $p$-values.
> Provide an overall interpretation, stated in the context of the problem.

For fixed factor $A$ and fixed factor $B$ nested in $A$,
$$
  F_A = \ms{A} / \ms{E}
$$
and
$$
  F_{B(A)} = \ms{B(A)} / \ms{E}
$$
where
\begin{align*}
  \ms{A} &= \frac{b n \sum_{i=1}^{a} \hat{\tau}_i^2 }{a-1},\\
  \ms{B(A)} &= \frac{n \sum_{i=1}^{a} \sum_{j=1}^{b} \hat{\beta}_{j(i)}^2}{a(b-1)},\\
  \ms{E} &= \frac{\sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n}
    (Y_{i j k} - \bar{Y}_{i j \cdot})}{a b (n-1)}.
\end{align*}

Under the model $\tau_1 = \cdots \tau_a = 0$,
$$
  F_A \sim F(\df{A},\df{E}) = F(a-1,a b (n-1))
$$
and under $\beta_{j(i)} = 0$ for all $i,j$,
$$
  F_{B(A)} \sim F(\df{B(A)},\df{E}) = F(a(b-1),a b (n-1)).
$$

We perform these computations in R with:

``` r
library("readxl")
data = read_excel("handout9data.xlsx")
A = as.factor(na.omit(data$mchine))
B = as.factor(na.omit(data$operator))
y = na.omit(data$surface)

# use contrasts to define parameter restrictions for the fixed effects in the
# model
contrasts(A)=contr.sum
contrasts(B)=contr.sum

# to fit a model with a nested fixed effect, we use the / notation within the
# aov command.
nested.mod = aov(y ~ A/B)
summary(nested.mod) # compute F statistics for factor effects
```

```
##             Df Sum Sq Mean Sq F value   Pr(>F)    
## A            3   3618  1205.9  14.271 0.000291 ***
## A:B          8   2818   352.2   4.168 0.013408 *  
## Residuals   12   1014    84.5                     
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
```

We see that $F_A = 14.271$ ($p$-value $= .000$) and $F_{B(A)} = 4.168$
($p$-value $= .013$).

### Interpretation

The experiment finds that the machine has an effect on surface finish.
Also, the experiment finds that the operators within a machine has an effect
on surface finish.

## Part (d)
> Compute estimates for each of the effect parameters.
> Identify which machine performs best, and which operator performs best on each
> machine. (Higher scores of response are preferred.)

### Comparing machines













