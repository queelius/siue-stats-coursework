---
title: 'Time Series Analysis - STAT 478 - Final Exam - Part 1 Q5'
author: "Alex Towell (atowell@siue.edu)"
output:
  pdf_document:
    df_print: kable
    #latex_engine: pdflatex
    latex_engine: xelatex
header-includes:
 - \usepackage{alex}
 - \usepackage{xfrac}
---
# Part 1: Problem 5
Suppose that $\{Y_t\}$ is a seasonal $\arima$ process in the form
$$
  Y_t = (1-\theta \backshift)(1- \Theta \backshift^4) e_t
$$
where $\{e_t\}$ is a zero mean white noise process with variance $σ^2$.

## Part (a)
\fbox{Derive expressions for $\expect(Y_t)$ and $\var(Y_t)$.}

Note that
\begin{align*}
  Y_t &= (1-\theta \backshift)(1- \Theta \backshift^4) e_t\\
      &= (1-\Theta \backshift^4 - \theta \backshift + \theta \Theta \backshift^5) e_t\\
      &= e_t - \theta e_{t-1} -\Theta e_{t-4} + \theta\Theta e_{t-5}.
\end{align*}

Then,
\begin{align*}
  \expect(Y_t)
    &= \expect(e_t)-\Theta \expect(e_{t-4}) - \theta \expect(e_{t-1}) + \theta\Theta \expect(e_{t-5})\\
    &= 0
\end{align*}
and
\begin{align*}
  \var(Y_t)
    &= \var(e_t)+\Theta^2 \var(e_{t-4}) + \theta^2 \var(e_{t-1}) + \theta^2\Theta^2 \var(e_{t-5})\\
    &= \sigma^2+\Theta^2 \sigma^2 + \theta^2 \sigma^2 + \theta^2\Theta^2 \sigma^2\\
    &= \sigma^2(1+\Theta^2+\theta^2+\theta^2\Theta^2)\\
    &= \sigma^2(1+\Theta^2)(1+\theta^2).
\end{align*}

## Part (b)
\fbox{Derive the autocovariance function, that is, calculate $\cov(Y_t, Y_{t−k})$ for $k=1,2,\ldots$}

The autocovariance function of $\{Y_t\}$ is given by
$$
  \gamma_k =
  \begin{cases}
    \sigma^2(1+\Theta^2)(1+\theta^2)     & k=0\\
    -\theta \sigma^2(1+\Theta^2)        & k=1\\
    0                                   & k=2\\
    \theta\Theta \sigma^2               & k=3\\
    -\Theta \sigma^2(1 + \theta\Theta)  & k=4\\
    \theta\Theta \sigma^2               & k=5\\
    0                                   & k>5.
  \end{cases}
$$


\begin{proof}
We do a case analysis on values of $k=1,2,\ldots$, but first note that by symmetry
$$
  \cov(Y_{t-k},Y_t) = \cov(Y_t,Y_{t-k})
$$
and so we only consider non-negative values of $k$.

\begin{enumerate}
\item Let $k=1$, then
\begin{align*}
  \cov(Y_t,Y_{t-1})
    &= \cov(e_t - \theta e_{t-1} - \Theta e_{t-4} + \theta\Theta e_{t-5},
            e_{t-1} - \theta e_{t-2} - \Theta e_{t-5} + \theta\Theta e_{t-6})\\
    &= \cov(-\theta e_{t-1},e_{t-1}) + \cov(\theta\Theta e_{t-5},-\Theta e_{t-5})\\
    &= -\theta \cov(e_{t-1},e_{t-1}) - \theta\Theta^2 \cov(e_{t-5},e_{t-5})\\
    &= -\theta \sigma^2 - \theta\Theta^2 \sigma^2\\
    &= -\theta \sigma^2(1+\Theta^2).
\end{align*}
\item Let $k=2$, then
\begin{align*}
  \cov(Y_t,Y_{t-2})
    &= \cov(e_t - \theta e_{t-1} - \Theta e_{t-4} + \theta\Theta e_{t-5},
            e_{t-2} - \theta e_{t-3} - \Theta e_{t-6} + \theta\Theta e_{t-7})\\
    &= 0.
\end{align*}
\item Let $k=3$, then
\begin{align*}
  \cov(Y_t,Y_{t-3})
    &= \cov(e_t - \theta e_{t-1} - \Theta e_{t-4} + \theta\Theta e_{t-5},
            e_{t-3} - \theta e_{t-4} - \Theta e_{t-7} + \theta\Theta e_{t-8})\\
    &= \cov(-\Theta e_{t-4},-\theta e_{t-4})\\
    &= \theta\Theta \cov(e_{t-4},e_{t-4})\\
    &= \theta\Theta \sigma^2.
\end{align*}
\item Let $k=4$, then
\begin{align*}
  \cov(Y_t,Y_{t-4})
    &= \cov(e_t - \theta e_{t-1} - \Theta e_{t-4} + \theta\Theta e_{t-5},
            e_{t-4} - \theta e_{t-5} - \Theta e_{t-8} + \theta\Theta e_{t-9})\\
    &= \cov(-\Theta e_{t-4},e_{t-4}) + \cov(\theta\Theta e_{t-5},-\Theta e_{t-5})\\
    &= -\Theta \cov(e_{t-4},e_{t-4}) - \theta\Theta^2 \cov(e_{t-5},e_{t-5})\\
    &= -\Theta \sigma^2 - \theta\Theta^2 \sigma^2\\
    &= \sigma^2(-\Theta - \theta\Theta^2)\\
    &= -\Theta \sigma^2(1 + \theta\Theta).
\end{align*}
\item Let $k=5$, then
\begin{align*}
  \cov(Y_t,Y_{t-5})
    &= \cov(e_t - \theta e_{t-1} - \Theta e_{t-4} + \theta\Theta e_{t-5},
            e_{t-5} - \theta e_{t-6} - \Theta e_{t-9} + \theta\Theta e_{t-10})\\
    &= \cov(\theta\Theta e_{t-1},e_{t-5})\\
    &= \theta\Theta \cov(e_{t-1},e_{t-5})\\    
    &= \theta\Theta \sigma^2.
\end{align*}
\item Let $k>5$, then $\cov(Y_t,Y_{t-k})$, $k>5$, is zero.
\end{enumerate}

We see that the autocovariance function is independent of time $t$ and only
a function of lag $k$.
We collect the cases and form the indicated piecewise function.
\end{proof}

## Part (c)
\fbox{Characterize this models as $\operatorname{SARIMA}(p, d, q)\times(P, D, Q)_s$, that is, identify $p,d,q,P,D,Q,s$.}

$\{Y_t\}$ is a zero mean process of type $\operatorname{SARIMA}(0,1,1)\times(0,1,1)_4$,
i.e., $p=0$, $d=1$, $q=1$, $P=0$, $D=1$, $Q=1$, and $s=4$.
