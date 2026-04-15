---
title: 'Computational Statistics - STAT 575 - HW #4'
author: "Alex Towell (atowell@siue.edu)"
output:
  html_document:
    #toc: true
    #toc_depth: 3
    mathjax: "default"
    #code_download: true
    #self_contained: false
    #toc_float: true
    #code_folding: "show"
    #df_print: kable
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
#documentclass: article
documentclass: paper
#documentclass: standalone
#classoption: twocolumn
#header-includes:
 #- \usepackage{amsmath}
 #- \usepackage{mathtools}
 #- \usepackage{amsthm}
 # - \usepackage{amsbsy}
 #- \usepackage{bm}
 #- \usepackage{xcolor}
 #- \usepackage{fbox}
 #- \usepackage{amsmath}
 #- \usepackage{hw4}
---

\usepackage{amsmath}
\usepackage{mathtools}
\usepackage{amsthm}
\usepackage{bm}
\usepackage{xcolor}
\usepackage{fbox}
\usepackage{amsmath}

\newcommand{\var}{\operatorname{Var}}
\newcommand{\expect}{\operatorname{E}}
\newcommand{\cov}{\operatorname{Cov}}
\newcommand{\se}{\operatorname{SE}}
\newcommand{\mat}[1]{\mathbf{#1}} 
\newcommand{\eval}[2]{\left. #1 \right\vert_{#2}}
\newcommand{\poi}{\operatorname{POI}}
\newcommand{\argmax}{\operatorname{arg\,max}}



# Problem 1
Use Metropolis Hasting algorithm to generate $Y \sim \operatorname{GAM}(\alpha, 1)$,
where $\alpha > 1$. Note $\alpha$ need not to be an integer.
Consider the proposal distribution $g$, which is the density of $\operatorname{GAM}(a,b)$,
where $a=\lfloor \alpha \rfloor$ and $b = a/\alpha$.

---

## Part (a)

Implement your accept-reject algorithm and Metropolis-hastings algorithms to get
a sample of $10000$ from $Y \sim \operatorname{GAM}(\alpha=2.5,1)$.

---

### Acceptance-rejection sampler

We implement the density and sampler functions, respectively $\rm{dgamma1}$
and $\operatorname{rgamma1}$.

Suppose $X \sim \operatorname{GAM}(\alpha,\beta)$ where $\alpha$ is the shape parameter
and $\beta$ is the rate parameter.
Then, $X$ has a density given by
$$
  f_X(x) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\beta x}.
$$

Suppose $Y \sim \operatorname{GAM}(\alpha,1)$, $\alpha \geq 1$.
This is hard to sample from.
However, $Z \sim \operatorname{GAM}(a,b)$ where $a = \lfloor \alpha \rfloor$ and
$b = a / \alpha$, is easy to sample from, since
$$
  Z = \sum_{i=1}^{a} X_i \sim \operatorname{GAM}(a,b)
$$
where $X_i \sim \operatorname{EXP}(b)$.

We may thus use acceptance-rejection sampling to sample $z \sim f_Z$ and then
$u \sim U(0,1)$ and accept $z$ as a realization from $f_Y$ if
$u \leq \frac{f_Y(z)}{c f_Z(z)}$ where, optimally,
$$
  c = \max_y \left\{\frac{f_Y(y)}{f_Z(y)}\right\},
$$
but in general $c$ must only satisfy $f_Y(y) / c f_Z(y) \leq 1$.

Note that we may use their respective kernels instead,
since the ratio of the kernels is proportional to $f_Y(y)/f_Z(y)$.
The ratio of the kernels is $h(y) = y^{\alpha-a} e^{(b-1)x}$.
Thus, we seek $c = \max_y h(y)$ which may be obtained by solving for the input
$y^*$ that maximizes $\log h$, which is the stationary point
$$
  \eval{\frac{d}{dy}\log h(y)}{y = y^*} = 0,
$$
and then substituting that into the ratio and simplifying, yielding the result
$$
  c = h(y^*) = (\alpha/e)^{\alpha-\lfloor \alpha \rfloor}.
$$
Observe that if $\alpha$ is an integer, then $c = 1$ and $h(y) = 1$, in which
case the target distribution and the candidate distribution are identical.

We implement the acceptance-rejection algorithm with the following code:

``` r
# The density function for random variates in the family
# GAM(shape=alpha,rate=1)
dgamma1 <- function(x, alpha) {
    dgamma(x, shape = alpha, rate = 1)
}

# An acceptance-rejection sampling procedure for random variates in the family
# GAM(shape=alpha,rate=1)
accept.reject.rgamma1 <- function(n, alpha) {
    a <- floor(alpha)
    rate <- a/alpha
    q <- (alpha/exp(1))^(a - alpha)
    ys <- vector(length = n)
    for (i in 1:n) {
        repeat {
            y <- sum(rexp(a, rate))  # draw candidate
            if (runif(1) <= q * y^(alpha - a) * exp(y * a/alpha - y)) {
                ys[i] <- y
                break
            }
        }
    }
    ys
}
```

We sample from $\operatorname{GAM}(2.5,1)$ with the the acceptance-rejection method
with:

``` r
alpha <- 2.5
m <- 10000
accept.reject.samp <- accept.reject.rgamma1(m, alpha)
```

### Metropolis-Hastings algorithm

Here is our implementation of the Metropolis-Hastings algorithm:

``` r
# A sampling procedure for random variates in the family
# GAM(shape=alpha,rate=1) using Metropolis-Hastings algorithm
metro.hast.rgamma1 <- function(n, alpha, burn = 0) {
    a <- floor(alpha)
    rate <- a/alpha

    # density for random variates in the family GAM(shape=alpha,rate=1)
    f <- function(x) {
        dgamma(x, shape = alpha, rate = 1)
    }
    g <- function(x) {
        dgamma(x, shape = a, rate = rate)
    }

    m <- n + burn
    ys <- vector(length = m)
    ys[1] <- sum(rexp(a, rate))

    for (i in 2:m) {
        v <- sum(rexp(a, rate))  # draw from g
        u <- ys[i - 1]
        R <- f(v) * g(u)/(f(u) * g(v))
        if (runif(1) <= R) {
            ys[i] <- v
        } else {
            ys[i] <- u
        }
    }
    ys[(burn + 1):m]
}
```

We sample from the Metro-Hastings algorithm with the following code:

``` r
metro.hast.samp <- metro.hast.rgamma1(m, alpha)
```

---

## Part (b)

Check on mixing and convergence using plots. Run multiple chain and compute the
Gelman-Rubin statistics. You may pick any reasonable burn-in.

---

We plot the histograms with:

``` r
par(mfrow = c(1, 2))
hist(accept.reject.samp, freq = F, breaks = 50, main = "acceptance-rejection")
lines(seq(0.01, 15, by = 0.01), dgamma1(seq(0.01, 15, by = 0.01), alpha), col = "blue",
    lwd = 2)

hist(metro.hast.samp, freq = F, breaks = 50, main = "metropolis-hastings")
lines(seq(0.01, 15, by = 0.01), dgamma1(seq(0.01, 15, by = 0.01), alpha), col = "blue",
    lwd = 2)
```

![](b_files/figure-latex/unnamed-chunk-6-1.pdf)<!-- --> 

Both samplers seem to be compatible with the density.

We plot the \emph{sample path} of the Metropolis-Hastings and acceptance-rejection
samplers with:

``` r
par(mfrow = c(1, 2))
plot(metro.hast.samp, pch = "·", xlab = "t", ylab = "Y", main = "metropolis-hastings")
plot(accept.reject.samp, pch = "·", xlab = "t", ylab = "Y", main = "acceptance-rejection")
```

![](b_files/figure-latex/unnamed-chunk-7-1.pdf)<!-- --> 

Both of these look good, as neither remain at or near the same value for 
many iterations. They also both quickly move away from their initial values.

We plot the ACFs with:

``` r
par(mfrow = c(1, 2))
acf(metro.hast.samp)
acf(accept.reject.samp)
```

![](b_files/figure-latex/unnamed-chunk-8-1.pdf)<!-- --> 

Both samplers seem to have very little autocorrelation.
If an uncorrelated sample is extremely important, to be
safe, taking every other sample point would probably be sufficient.

We implement the Gelman-Rubin statistic with:

``` r
# samps: should be an L x J matrix, where L is the length of the samples and J
# is the number of samples (independent chains).
gelman.rubin <- function(samps) {
    L <- nrow(samps)
    J <- ncol(samps)
    x.bar <- apply(samps, 2, mean)
    B <- var(x.bar) * L
    W <- mean(apply(samps, 2, var))

    ((L - 1)/L * W + B/L)/W
}
```

Next, we compute Gelman-Rubin statistics on the computed independence chains.

``` r
chains <- 1000
samps <- matrix(nrow=m,ncol=chains)
for (i in 1:chains)
{
  samps[,i] <- metro.hast.rgamma1(m,alpha,burn=1000)
}

gelman.rubin.stat <- gelman.rubin(samps)
print(gelman.rubin.stat)
```

```
## [1] 1.000016
```

We see that the Gelman-Rubin statistic is given by
$$
  R = 1.0000163.
$$

We adopt the rule of thumb that if $\sqrt{R} < 1.1$, the burn-in and chain
length are sufficient. We compute $\sqrt{R}$ to be
$$
  \sqrt{R} = 1.0000081,
$$
and thus are satisfied with our burn-in choice and chain length.

---

## Part (c)

Estimate $\expect(Y^2)$ using the generated chain. Compare with the estimate
you get with acceptance-rejection sampling (Exam 1).

---

Theoretically,
$$
  \expect(Y^2) = \frac{\Gamma(2+\alpha)}{\Gamma(\alpha)} = \frac{\Gamma(4.5)}{\Gamma(2.5)} = 8.75.
$$

We estimate $\expect(Y^2)$ using the acceptance-rejection and Metropolis-Hastings
by taking the square of each element in the samples they generated and then taking
the mean:

``` r
tab <- matrix(nrow = 2, ncol = 1)
rownames(tab) <- c("acceptance-rejection", "metropolis-hastings")
colnames(tab) <- c("mean")
tab[1] <- c(mean(accept.reject.samp^2))
tab[2] <- c(mean(metro.hast.samp^2))

knitr::kable(data.frame(tab))
```



|                     |     mean|
|:--------------------|--------:|
|acceptance-rejection | 8.759960|
|metropolis-hastings  | 8.644269|
Both are quite close to the true value of $8.75$.


# Problem 2 (Problem 7.1)

Rework the textbook example. Consider the mixture normal $\delta N(7,0.5^2) + (1-\delta) N(10,0.5^2)$.

---

## Part (a)

Simulate $200$ realizations from the mixture distribution with $\delta = 0.7$.
Draw a histogram of these data.

---

We implement the density and sampler for the mixture distribution with:

``` r
dmix <- function(x, delta) {
    delta * dnorm(x, 7, 0.5) + (1 - delta) * dnorm(x, 10, 0.5)
}

rmix <- function(n, delta) {
    xs <- vector(length = n)
    for (i in 1:n) {
        xs[i] <- ifelse(runif(1) < delta, rnorm(1, 7, 0.5), rnorm(1, 10, 0.5))
    }
    xs
}
```

We generate a sample and plot its histogram with:

``` r
n <- 200
delta <- 0.7
data <- rmix(n, delta)
hist(data, freq = F)
```

![](b_files/figure-latex/unnamed-chunk-13-1.pdf)<!-- --> 

---

## Part (b)

Now assume $\delta$ is unknown. Implement independence chain MCMC procedure to
simulate from the posterior distribution of $\delta$, using your data from
part (a).

---


``` r
lmix <- Vectorize(function(delta, xs) {
    if (delta < 0 || delta > 1) {
        return(0)
    }
    p <- 1
    for (x in xs) {
        p <- p * dmix(x, delta)
    }
    p
}, "delta")

logmix <- Vectorize(function(delta, xs) {
    if (delta < 0 || delta > 1) {
        return(-Inf)
    }
    logp <- 0
    for (x in xs) {
        logp <- logp + log(dmix(x, delta))
    }
    logp
}, "delta")
```

A sample $\{x_t\}$ drawn from the mixture normal with density $\operatorname{dmix}$
is observed with likelihood $\operatorname{lmix}(\delta|\vec{x})$ with respect to
$\delta$ with prior distribution $p(\delta)$.
Thus, the posterior distribution is given by
$$
  p(\delta|\vec{x}) \propto p(\delta) \operatorname{lmix}(\delta|\vec{x}).
$$

In the independence chain MCMC, we may use the prior as the proposal density,
$f(\delta) = p(\delta|\vec{x})$ and $g = p$,
and thus
$$
  R = \frac{f(\delta^{*}) g(\delta^{(t)})}{f(\delta^{(t)})g(\delta^{*})} = \frac{p(\delta^{*}|\vec{x}) p(\delta^{(t)})}{p(\delta^{(t)}|\vec{x}) p(\delta^{*})}
$$
which may be rewritten as
$$
  R = \frac{p(\delta^{*}) \operatorname{lmix}(\delta^{*}|\vec{x}) p(\delta^{(t)})}{p(\delta^{(t)}) \operatorname{lmix}(\delta^{(t)}|\vec{x}) p(\delta^{*})} = \frac{\operatorname{lmix}(\delta^{*}|\vec{x})}{\operatorname{lmix}(\delta^{(t)}|\vec{x})}.
$$

### Numerical imprecision
Suppose we have a data type $T$ that models real numbers.
Since computers are physical, $T$ can only represent a finite set of numbers.

In the likelihood function,
$$
  \operatorname{lmix} \colon \mathbb{R} \times 2^{\mathbb{R}} \mapsto \mathbb{R},
$$
if we model $\mathbb{R}$ with $T$, i.e.,
$$
  \operatorname{lmix} \colon T \times 2^T \mapsto T,
$$
then if the true value of the likelihood function applied to a sufficiently
large sample is some value $p \in (0,\epsilon)$ where $\epsilon$ is the smallest
representable positive number of type $T$, the best we can do is round $p$
to $0$ or $\epsilon$.
As a consequence, the likelihood function evaluates to $0$ on any sufficiently
large sample size.

Suppose $\epsilon = 2^{-K}$.
If we use the log-likelihood instead,
$$
  \operatorname{logmix} \colon T \times 2^T \mapsto T
$$
then, for instance, $\log_2 \epsilon = -K$ where $-K$ is very likely to be at
least approximately representatable by $T$, and much smaller values as well.
We cannot map many of these log-likelihoods back to a likelihood, but as long
as we only need to work with log-likelihoods, this is not a problem.

With the above in mind, we replace the likelihood function with the
log-likelihood function to significantly increase the space of samples we can
work with.


``` r
delta.estimator.ic <- function(n, data, delta0 = runif(1), burn = 0) {
    m <- n + burn
    deltas <- vector(length = m)
    deltas[1] <- delta0

    for (i in 2:m) {
        delta <- runif(1)  # draw candidate from prior
        delta.old <- deltas[i - 1]
        log.R <- logmix(delta, data) - logmix(delta.old, data)
        if (log(runif(1)) <= log.R) {
            deltas[i] <- delta
        } else {
            deltas[i] <- delta.old
        }
    }
    deltas[(burn + 1):m]
}
```

---

## Part (c)

Implement a random walk chain with $\delta^* = \delta^{(t)} + \epsilon_t$ with
$\epsilon \sim \operatorname{UNIF}(-1,1)$.

---

We observe that $\epsilon_t \sim \operatorname{UNIF}(-1,1)$ for $t=0,\ldots,t$
are the only random components. Thus, the conditional distribution of
$\epsilon_{t+1}$ given $\epsilon_{t}$ is
$$
  \epsilon_{t+1} \sim f(\delta^* - \delta^{(t)})
$$
where $f$ is the density of $\operatorname{UNIF}(-1,1)$.


``` r
delta.estimator.rw <- function(n, data, delta0 = runif(1), burn = 0) {
    m <- n + burn
    deltas <- vector(length = m)
    deltas[1] <- delta0
    for (i in 2:m) {
        delta.old <- deltas[i - 1]
        delta <- delta.old + runif(1, -1, 1)
        log.R <- logmix(delta, data) - logmix(delta.old, data)
        if (log(runif(1)) <= log.R) {
            deltas[i] <- delta
        } else {
            deltas[i] <- delta.old
        }
    }
    deltas[(burn + 1):m]
}
```

---

## Part (d)

Reparameterize the problem letting $U = \log\left(\delta/(1-\delta)\right)$
and $U^* = u(t) + \epsilon_t$. Implement a random walk chain with $U$ as in
Equation (7.8) page 208.

---


``` r
logit <- function(delta) {
    log(delta/(1 - delta))
}
logit.inv <- function(u) {
    exp(u)/(1 + exp(u))
}
logit.inv.J <- function(u) {
    exp(u)/(1 + exp(u))^2
}

delta.estimator.u.rw <- function(n, data, delta0 = runif(1), burn = 0) {
    m <- n + burn
    u <- vector(length = m)
    u[1] <- logit(delta0)
    for (i in 2:m) {
        u.old <- u[i - 1]
        u.star <- u.old + runif(1, -1, 1)
        R <- lmix(logit.inv(u.star), data) * logit.inv.J(u.star)/(lmix(logit.inv(u.old),
            data) * logit.inv.J(u.old))
        if (runif(1) <= R) {
            u[i] <- u.star
        } else {
            u[i] <- u.old
        }
    }
    logit.inv(u[(burn + 1):m])
}
```

---

## Part (e)

Compare the estimates and convergence behavior of three algorithms.

---

We do not do a burn-in, since we are interested in seeing how quickly
the three methods converge. We only plot chains of length $1000$.

We generate the data sets with:
















