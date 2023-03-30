---
title: 'Time Series Analysis - STAT 478 - Final Exam - Part 1 Q3'
author: "Alex Towell (atowell@siue.edu)"
output:
  pdf_document:
    df_print: kable
    #latex_engine: pdflatex
    latex_engine: xelatex
header-includes:
 - \usepackage{alex}
---
# Part 1: Problem 3
Consider the model $Y_t = β_1 t + X_t$.

## Part (a)
\fbox{\begin{minipage}{.9\textwidth}
$\{X_t\}$ is a zero mean white noise process with $\var(X_t) = σ^2$.
Find the least square estimator of $β_1$.
\end{minipage}}

\begin{proof}
$Y_t$ is a random variable defined by
$$
  Y_t = β_1 t + X_t
$$
where $X_t$ is zero mean white noise.
Then, $X_t = Y_t - β_1 t$ and we wish to find a value for $β_1$ that minimizes
$$
  \operatorname{Q}(β_1) = \sum_{t=1}^{T} X_t^2 = \sum_{t=1}^{T}(Y_t - β_1 t)^2.
$$
since $X_t$ has an expectation of zero mean.
We observe that $\operatorname{Q}$ is convex with a global minimum where its
derivative is zero, thus we solve for $\hat\beta_1$ in
\begin{align*}
  \eval{\frac{\mathrm{d}Q}{\mathrm{d}\beta}}{\hat\beta_1} &= 0\\
                          -2 \sum (Y_t - \hat\beta_1 t) t &= 0\\
                                               \sum t Y_t &= \hat\beta_1 \sum t^2\\
                                              \hat\beta_1 &= \frac{ \sum t Y_t }{\sum t^2}.
\end{align*}

Note that $\sum_{t=1}^{T} t^2 = T(T+1)(2 T+1)/6$ and thus
\begin{equation}
  \hat\beta_1 = \frac{ 6 \sum t Y_t }{T(T+1)(2 T+1)}.
\end{equation}
\end{proof}

This is the BLUE estimator of $\beta_1$.

## Part (b)
\fbox{\begin{minipage}{.9\textwidth}
Suppose $\{X_t\}$ is a process of the form
$$
  X_t = X_{t−1} + e_t − θe_{t−1}.
$$
Derive the ACF for $\{∇Y_t\}$ and show that $\{∇Y_t\}$ is stationary.
What is the name of the process identified by $\{∇Y_t\}$?
\end{minipage}}

First, we derive an explicit equation for $\nabla Y_t$,
\begin{align*}
  \nabla Y_t
    &= Y_t - Y_{t-1}\\
    &= (β_1 t + X_t) - (β_1 (t-1) + X_{t-1})\\
    &= β_1 + X_t - X_{t-1}.
\end{align*}

We rewrite the above by replacing $X_t$ with its definition,
\begin{align*}
  \nabla Y_t
    &= β_1 + (X_{t−1} + e_t − θe_{t−1}) - X_{t-1}\\
    &= β_1 + e_t − θe_{t−1}.
\end{align*}

This is the form of an $\ma(1)$ with $\mu=β_1$.
It is known that $\ma(1)$ is always stationary and has an ACF
$$
  \rho_k =
  \begin{cases}
    1    & \text{if}\; |k| = 0\\
    \frac{-\theta}{1+\theta^2} & \text{if}\; |k| = 1\\
    0          & \text{if}\; |k| > 1,
  \end{cases}
$$
but we will derive the result from first principles.

The covariance of $\nabla Y_t$ and $\nabla Y_{t-k}$ is given by
\begin{align*}
  \cov(\nabla Y_t,\nabla Y_{t-k})
    &= \cov(β_1 + e_t − θe_{t−1},β_1 + e_{t-k} − θe_{t−k-1})\\
    &= \cov(e_t − θe_{t−1},e_{t-k} − θe_{t−k-1})\\
    &= \cov(e_t,e_{t-k}) + \cov(e_t, −θe_{t-k-1}) + \cov(-θe_{t−1},e_{t-k}) + \cov(-θe_{t−1},-θe_{t−k-1}).
\end{align*}

Now we do a case analysis on values of $k$, but first note that by symmetry
$$
  \cov(\nabla Y_{t-k},\nabla Y_t) = \cov(\nabla Y_t,\nabla Y_{t-k})
$$
and so we only consider non-negative values of $k$.

### Case 1: $k=0$
The covariance of $\nabla Y_t$ and $\nabla Y_t$ is given by
\begin{align*}
  \cov(\nabla Y_t,\nabla Y_t)
    &= \cov(e_t,e_t) + \cov(e_t, −θe_{t-1}) + \cov(-θe_{t−1},e_t) +\cov(-θe_{t−1},-θe_{t−1})\\
    &= \cov(e_t,e_t) + \cov(-θe_{t−1},-θe_{t−1})\\
    &= \sigma^2 + θ^2 \sigma^2\\
    &= \sigma^2 (1+θ^2).
\end{align*}
By definition, $\var(\nabla Y_t)=\cov(\nabla Y_t,\nabla Y_t)$.

### Case 2: $k=1$
The covariance of $\nabla Y_t$ and $\nabla Y_{t-1}$ is given by
\begin{align*}
  \cov(\nabla Y_t,\nabla Y_{t-1})
    &= \cov(e_t,e_{t-1}) + \cov(e_t, −θe_{t-2}) + \cov(-θe_{t−1},e_{t-1}) +\cov(-θe_{t−1},-θe_{t−2})\\
    &= \cov(-θe_{t−1},e_{t-1})\\
    &= -θ\cov(e_{t−1},e_{t-1})\\
    &= -θ \sigma^2.
\end{align*}

### Case 3: $k \geq 2$
First, we consider $k=2$ and generalize the result.
The covariance of $\nabla Y_t$ and $\nabla Y_{t-2}$ is given by
\begin{align*}
  \cov(\nabla Y_t,\nabla Y_{t-2})
    &= \cov(e_t,e_{t-2}) + \cov(e_t, −θe_{t-3}) + \cov(-θe_{t−1}, e_{t-2}) +\cov(-θe_{t−1},-θe_{t−3})\\
    &= 0.
\end{align*}

Generalizing the result, we see that for $k > 2$, every pair of errors
have $0$ covariance.
Thus, 
$$
  \cov(\nabla Y_t,\nabla Y_{t-k}) = 0
$$
if $k > 0$.

### Autocorrelation function
We see that the covariances are independent of time $t$ and are only
a function of lag $k$, and thus the \emph{autocorrelation} function is given by
\begin{align*}
  \rho_k
    &= \frac{\cov(\nabla Y_t,\nabla Y_{t-k})}{\sqrt{\var(\nabla Y_t)}\sqrt{\var(\nabla Y_{t-k})}}\\
    &= \frac{\cov(\nabla Y_t,\nabla Y_{t-k})}{\sigma^2(1+\theta^2)},
\end{align*}
which simplifies to
$$
  \rho_k =
  \begin{cases}
    1                             & \text{if}\; |k| = 0\\
    \frac{-\theta}{1+\theta^2}    & \text{if}\; |k| = 1\\
    0                             & \text{if}\; |k| > 1.
  \end{cases}
$$

### Stationarity conditions
We see that its mean is constant $\expect(\nabla Y_t) = \beta_1$, its variance
is constant, and its autocorrelation function is strictly a function of lag $k$.
Thus, $\nabla Y_t$ is stationary.
