---
title: 'STAT 581 - Exam 1: Due Dec 2, 2021'
author: "Alex Towell (atowell@siue.edu)"
output:
  pdf_document:
    toc: false
    df_print: kable
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
> An experiment is conducted to study the effect of fitness level on ego
> strength. Random samples of college faculty members are selected from each
> fitness level, and an ego score is observed for each member in the sample.
> Higher values indicate greater ego. The data is provided as an attachment.

## Preliminary analysis

We are interested in whether
$$
  \text{input} = \text{fitness level}
$$
has an effect on
$$
  \text{response} = \text{ego strength}.
$$

We have two populations, one in which the mean fitness level is `high` and
another in which the mean fitness level is `low`, denoted respectively by
group $1$ and group $2$.

We take a sample of size $n_1$ from group $1$ (`high`)
$$
  Y_{1 j}  = \mu_1 + \epsilon_{1 j}
$$
and a sample of size $n_2$ from group $2$ (`low`),
$$
  Y_{2 j}  = \mu_2 + \epsilon_{2 j},
$$
where
\begin{align*}
  Y_{i j}           &\;\text{is the $j$-th ego strength response for $i$-th group (fitness level or treatment),}\\
  \mu_i             &\;\text{is the mean response for the $i$-th group},\\
  \epsilon_{i j}    &\;\text{is iid normal with zero mean}.
\end{align*}

The result is two samples:

| group 1     | group 2     |
| ----------- | ----------- |
| $y_{1 1}$   | $y_{2 1}$   |
| $y_{1 2}$   | $y_{2 2}$   |
| $\vdots$    | $\vdots$    |
| $y_{1 n_1}$ | $y_{2 n_2}$ |


## Part (a)
> State the hypotheses of interest. Provide an interpretation, stated in the
> context of the problem.

### Reproduce

The hypothesis of interest is whether fitness level has an effect on ego strength,
\begin{align*}
  H_0 &: \mu_1 = \mu_2    \qquad&\text{(fitness level has no effect on ego strength)}\\
  H_A &: \mu_1 \neq \mu_2 \qquad&\text{(fitness level does have an effect on ego strength)}
\end{align*}
where $\mu_1$ and $\mu_2$ are respectively the mean ego strengths for the `high` and `low` fitness levels.

## Part (b)
> Compute the $t_0$ statistic and the $p$-value.
> Provide an interpretation, statedin the context of the problem.



``` r
library("readxl")
data = read_excel("exam1data.xlsx")
fitness = as.factor(na.omit(data$fitness.level))
ego = na.omit(data$ego.score)
t.star = t.test(ego ~ fitness, var.equal=T)
t.star
```

```
## 
## 	Two Sample t-test
## 
## data:  ego by fitness
## t = 3.7092, df = 28, p-value = 0.0009111
## alternative hypothesis: true difference in means between group high and group low is not equal to 0
## 95 percent confidence interval:
##  0.6268509 2.1731491
## sample estimates:
## mean in group high  mean in group low 
##                5.2                3.8
```

### Reproduce
We see that $t_0 = 3.71$ with a $p$-value $= .001$.

The experiment finds that the fitness level has an effect on ego strength.
A high fitness level leads to an increased ego strength.

## Part (c)
> Create a Boxplot as a graphical display of the data. Is it true that all high
> fitness faculty members have greater egos than low fitness faculty members?


``` r
boxplot(ego[fitness=='low'],ego[fitness=='high'])
```

![](stat581.exam1_files/figure-latex/unnamed-chunk-2-1.pdf)<!-- --> 

### Reproduce

The experimental finding is based on a comparison of means.
It is not true that all ego strengths in the `high` fitness level
exceeds all ego strengths in the `low` fitness level.

## Part (d)
> Compute a 95\% confidence interval for $\delta = \mu_1 - \mu_2$.
> Provide an interpretation, stated in the context of the problem.

We computed the results earlier to be:

``` r
t.star
```

```
## 
## 	Two Sample t-test
## 
## data:  ego by fitness
## t = 3.7092, df = 28, p-value = 0.0009111
## alternative hypothesis: true difference in means between group high and group low is not equal to 0
## 95 percent confidence interval:
##  0.6268509 2.1731491
## sample estimates:
## mean in group high  mean in group low 
##                5.2                3.8
```

### Reproduce
We see that $\operatorname{CI}(\delta) = [.63,2.17]$.
Based on the observed data, we estimate that the difference in mean ego score,
(`high fitness` $-$ `low fitness`), is between $.63$ and $2.17$ units.

## Part (e)
> Explain how a confidence interval provides a complementary result to a
> hypothesis test.

### Reproduce

A hypothesis test looks to determine if an effect exists (dichotomous).
A confidence interval looks to determine the *size* of the effect.
(Also, a CI provides a measure of evidence strength.)

## Part (f)
> Explain how a confidence interval can be used in testing
> $H_0 : \mu_1 = \mu_2$.

### Reproduce

If $0$ is contained in $\operatorname{CI}(\delta)$, decide in favor of $H_0 : \mu_1 = \mu_2$.
Otherwise, decide in favor of $H_A : \mu_1 \neq \mu_2$.

# Problem 2
> A completely randomized design is used to investigate the effect of drug dosage on the activity level of
lab rats. Each dose level is applied to $n=4$ rats, and an activity score is observed for each rat in the sample.
Higher values indicate greater activity. The data is provided as an attachment.

## Preliminary analysis

The input factor is `drug dosage` with $a=4$ levels ($1=$ `control`, $2=$ `high`, $3=$ `low`, $4=$ `medium`).

The response is `activity level`.

We have $n=4$ replicates for a total of $N=a n=16$ observations.

## Part (a)
> State the statistical hypotheses of interest. Briefly explain how the form of the alternative hypothesis
requires a need for further investigation.

The hypothesis of interest is whether `drug dosage` level effects `activity level`. We may formulate
this as a hypothesis test of the form
\begin{align*}
  H_0 &: \mu_1 = \mu_2 = \mu_3 = \mu_4    \qquad&\text{(`drug dosage` has no effect on `activity level`)},\\
  H_A &: \mu_i \neq \mu_j \;\text{for some pair $(i,j)$}\qquad&\text{(`drug dosage` does have an effect on `activity level`)}.
\end{align*}
where $\mu_j$ is the expected activity level given a `drug dosage` level $j$.

If we decide $H_A$, i.e., there are differences in the dosage level means, then further investigation is required to determine where the differences occur.

## Part (b)
> Compute the $F_0$ statistic and the p-value. Provide an interpretation, stated in the context of the
problem. Create a Boxplot as a graphical display of the data.

This is a one-factor experiment with $a=4$ levels of the factor and $n=4$ replicates for a total of $N=n a = 16$
observations.
The appropriate test statistic is
$$
  F_0 = \ms{A} / \ms{E}
$$
which under $H_0 : \mu_1 = \cdots = \mu_4$ has the reference distribution
$$
  F_0 \sim F(a-1 = 3,N-a = 12).
$$

We compute the observed test statistic $F_0$ with:


``` r
dosage = as.factor(na.omit(data$dose.level))  # factor A
activity = na.omit(data$activity.score)       # response
boxplot(activity ~ dosage)
```

![](stat581.exam1_files/figure-latex/unnamed-chunk-4-1.pdf)<!-- --> 

``` r
model = aov(activity ~ dosage)
summary(model)
```

```
##             Df Sum Sq Mean Sq F value  Pr(>F)   
## dosage       3 152.40   50.80   6.367 0.00791 **
## Residuals   12  95.75    7.98                   
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
```

We see that $F_0 = 6.367$ with a $p$-value $= .008$ under $H_0$.

### Interpretation (rep)
The experiment finds that the dosage level has an effect on the activity score.

## Part (c)
> Compute and display 95% confidence intervals for all pairwise comparisons. Explain how computing
multiple intervals impacts the probability of committing an error.























