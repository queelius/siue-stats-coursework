---
title: 'STAT 581 - HW #1'
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





``` r
library("readxl")
```

```
## Error in library("readxl"): there is no package called 'readxl'
```

``` r
# read from directory the markdown file is located in
h1.data <- read_excel("./handout1data.xlsx")
```

```
## Error in read_excel("./handout1data.xlsx"): could not find function "read_excel"
```

``` r
h1.data$method <- as.factor(h1.data$method)
```

```
## Error: object 'h1.data' not found
```

``` r
h1.time.dry <- na.omit(h1.data$time[h1.data$method=='d'])
```

```
## Error: object 'h1.data' not found
```

``` r
h1.time.wet <- na.omit(h1.data$time[h1.data$method!='d'])
```

```
## Error: object 'h1.data' not found
```



An experiment is designed to investigate whether the time to drill holes in rock
holes using wet or dry drilling.
A completely randomized design (CRD) is used.
Each method is replicated on 12 rocks.
The drilling times (in 1 / 100 minutes) are observed to be

```
## Error in library(printr): there is no package called 'printr'
```

```
## Error: object 'h1.time.dry' not found
```

# Q1
\fbox{State the hypotheses of interest. Provide an interpretation, stated in the
context of the problem.}

The hypothesis of interest is whether drilling time is effected by the choice
of wet or dry drilling. We may formulate this as a hypothesis test of the form

\begin{align*}
  H_0 &: \mu_1 = \mu_2\\
  H_A &: \mu_1 \neq \mu_2\,,
\end{align*}
where $\mu_1$ and $\mu_2$ are respectively the expected drilling time for
dry and wet drilling.

If $H_0$ is true, the drilling method has \emph{no} effect on drilling time. If
$H_A$ is true, the choice does have an effect on drilling time.

# Q2
\fbox{Give two advantages of the completely randomized design.}

Two advantages of the completely randomized design (CRD) are:

  1. It is simple to implement and analyze.
  
  2. It accounts for experimental unit variance, namely by controlling for the
     type I error,
     
     $$
         \alpha = \Pr(\text{decide} \, H_A | H_0 \, \text{true}),
     $$
     
     where $\alpha$ is the probability of a type I error. It may also be thought of
     as the type I \emph{error rate}, or \emph{false positive rate}.

# Q3
\fbox{Give two disadvantages of the completely randomized design.}

Two disadvantages of the completely randomized design (CRD) are:

  1. It does not account for type II error,
     $$
         \beta = \Pr(\text{decide} \, H_0 | H_A \, \text{true}).
     $$
     where $\beta$ is the probability of a type II error.

     > **Additional remarks**: Since we may denote a type I error a false
     positive, it may be appropriate to denote a type II error a false negative,
     which implies the convention $H_0 \equiv \rm{negative}$ and
     $H_A \equiv \rm{positive}$. Thus, $\beta$ may be thought of as the false
     negative rate.

     > Consider the unrelated *Bloom filter*, which is a
     probabilistic data structure that models sets in which membership queries
     have a controllable false positive rate $\epsilon$ and a false negative rate
     $0$. If we take the complement of an object representing such a Bloom
     filter, then membership queries on its complement have a false positive
     rate $0$ and a false negative rate $\epsilon$.
     
  2. It does not adjust for differences in experimental units nor differences
  in any other factors.
  

# Q4
\fbox{Compute the sample means, the sample standard deviations, and the pooled
sample standard deviation.}


``` r
time.mean <- round(c(mean(h1.time.dry),
               mean(h1.time.wet)),digits=3)
```

```
## Error: object 'h1.time.dry' not found
```

``` r
time.var <- round(c(var(h1.time.dry),
              var(h1.time.wet)),digits=3)
```

```
## Error: object 'h1.time.dry' not found
```

``` r
time.sd <- round(sqrt(time.var),digits=3)
```

```
## Error: object 'time.var' not found
```

``` r
n <- c(length(h1.time.dry),
       length(h1.time.wet))
```

```
## Error: object 'h1.time.dry' not found
```

``` r
time.sd.pooled <-
  round(sqrt(((n[1] - 1) * time.var[1] + (n[2] - 1) * time.var[2]) / (sum(n)-2)),
        digits=3)
```

```
## Error: object 'n' not found
```

``` r
c("y.bar.1" = time.mean[1],
  "y.bar.2" = time.mean[2],
  "s.1" = time.sd[1],
  "s.2" = time.sd[2],
  "s.p" = time.sd.pooled)
```

```
## Error: object 'time.mean' not found
```





