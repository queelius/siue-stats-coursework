---
title: 'Time Series Analysis - 478 - Exam 2'
author: "Alex Towell (atowell@siue.edu)"
header-includes:
 - \usepackage{amsmath}
 - \usepackage{mathtools}
 - \usepackage{amsthm}
 # - \usepackage{amsbsy}
 - \usepackage{bm}
output:
  pdf_document:
    latex_engine: xelatex
    df_print: kable
    toc: true
    toc_depth: 3
  html_document:
    df_print: paged
---

\newcommand{\backshift}{\operatorname{B}}
\newcommand{\var}{\operatorname{Var}}
\newcommand{\expect}{\operatorname{E}}
\newcommand{\corr}{\operatorname{Corr}}
\newcommand{\cov}{\operatorname{Cov}}
\newcommand{\ssr}{\operatorname{SSR}}
\newcommand{\se}{\operatorname{SE}}
<!-- \newcommand{\mat}[1]{\pmb{#1}}  -->
\newcommand{\mat}[1]{\bm{#1}}
\newcommand{\eval}[2]{\left. #1 \right\vert_{#2}}

# Problem 1.1
Suppose that simple exponential smoothing is being used to forecast the process
$y_t = \mu + e_t$, where where $\{e_t\}$ are white noise with mean $0$ and
variance $\sigma^2$.
At the start of period $t^{∗}$, the mean of the process
experiences a transient;
that is, it shifts to a new level $\mu + \delta$, but
reverts to its original level $\mu$ at the start of the next period $t^{∗} + 1$.
The mean remains at this level for subsequent time periods.

## Part (a)
\fbox{\begin{minipage}{.8\textwidth}
Find the expected value of the simple exponential smoother
$$
   \tilde{y}_T = (1-\theta)\sum_{t=0}^{\infty} \theta^t y_{T}.
$$
\end{minipage}}

We have a time series
$$
   y_t = \mu + e_t
$$
except at $y_{t^*}$ which is distributed
$$
   y_t^{*} = \mu + \delta + e_{t^*}
$$
where the error terms are zero mean white noise with variance $\sigma^2$.

The expectation of the smoothed time series $\tilde{y}_T$ is given by
\begin{align*}
   \expect(\tilde{y}_T)
      &= (1-\theta)\sum_{t=0}^{\infty} \theta^t \expect(y_{T-t})\\
      &= (1-\theta)\left(
            \sum_{t=0}^{T-t^*+1} \theta^t \mu +
            \theta^{T-t^*}(\mu + \delta) +
            \sum_{t=T-t^*-1}^{\infty} \theta^t \mu
         \right)\\
      &= (1-\theta)\left(
            \sum_{t=0}^{\infty} \theta^t \mu +
            \theta^{T-t^*} \delta
         \right)\\
      &= \mu + (1-\theta) \theta^{T-t^*} \delta.
\end{align*}

## Part (b)
\fbox{\begin{minipage}{.8\textwidth}
For $\theta = 0.5$, determine the number of periods that it will take following
the impulse for the expected value of $\tilde{y}_T$ to return to within $0.1\delta$ of the original level $\mu$.
\end{minipage}}
We wish to find $\tilde{y}_k$ such that it is expected to be within
$\frac{1}{10} \delta$ of $\mu$,
$$
   \left\lvert \expect(\tilde{y}_k) - \mu \right\rvert \leq \left\lvert \frac{1}{10} \delta \right\rvert.
$$

Plugging in the definition of the expectation and simplifying,
$$
   \left\lvert (1-\theta) \theta^{k-t^*} \delta \right\rvert \leq \left\lvert \frac{1}{10} \delta \right\rvert.
$$

Since pulling all positive numbers (or symbols that stand for positive numbers) out of the
absolute value function does not change the expression, we may rewrite the above
as
$$
   (1-\theta) \theta^{k-t^*} \vert \delta \vert \leq \frac{1}{10} \vert \delta \vert.
$$
Dividing by $\vert \delta \vert$ on both sides,
$$
   (1-\theta) \theta^{k-t^*} \leq \frac{1}{10},
$$
which may be rewritten as
$$
   \theta^k \leq \frac{\theta^{t^*}}{10(1-\theta)}.
$$

Taking the logarithm of both sides
\begin{align*}
   k \log \theta
      &\leq \log \left(\frac{\theta^{t^*}}{10(1-\theta)}\right)\\
      &\leq t^* \log \theta - \log 10 - \log(1-\theta).
\end{align*}

Finally, we isolate $k$ by dividing by $\log \theta$ on both sides. However,
note that $\log \theta$ is negative, and so we must flip the inequality,
$$
   k \geq t^* - \frac{\log 10}{\log\theta} - \frac{\log(1-\theta)}{\log \theta}.
$$

Letting $\theta = 0.5$,
$$
   k \geq t^* + \frac{\log 10}{\log 2} - \frac{\log 0.5}{\log 0.5}
$$
which simplifies to
$$
   k \geq t^* + 2.32.
$$

We wish to take the \emph{smallest} $k$ that is an integer that satisfies the
equation. Thus, $k = t^* + 3$. Or, in other words, $3$ periods after $t^*$,
$\tilde{y}_T$ has an expectation that is within the specified distance of $\mu$.

# Problem 1.2
Let $\{Y_t\}$ be an AR(1) process with $|φ| < 1$. That is $Y_t = φY_{t−1} + e_t$,
where $\{e_t\}$ are white noise with mean $0$ and variance $\sigma^2$.
Also note $e_t$’s are independent of $Y_{t−1}, Y_{t−2},\ldots$.

## Part (a)
\fbox{\begin{minipage}{.8\textwidth}
Find the autocorrelation function for $W_t = Y_t - Y_{t-1}$ in terms of $φ$ and $\sigma^2$.
\end{minipage}}

Observe that
$$
   W_t = Y_t - Y_{t-1} = φ Y_{t-1} + e_t - Y_{t-1}
$$
and thus
$$
   W_t = (φ - 1) Y_{t-1} + e_t.
$$

The autocovariance function for $W_t$, denoted by $γ_{\{W_t\}}$, is defined as
$$
   γ_{\{W_t\}}(k) = \cov(W_t,W_{t-k}).
$$

Assuming $k \neq 0$ (we solve directly for variance in that case) and replacing
$W_t$ and $W_{t-k}$ with their respective definitions yields
\begin{align*}
   γ_{\{W_t\}}(k)
      &= \cov((φ - 1) Y_{t-1} + e_t,(φ - 1) Y_{t-k-1} + e_{t-k})\\
      &= \cov((φ - 1) Y_{t-1},(φ - 1) Y_{t-k-1})\\
      &= (φ - 1)^2 \cov(Y_{t-1},Y_{t-k-1}).
\end{align*}

Observe that $\cov(Y_{t-1},Y_{t-k-1}) = γ_{\{Y_t\}}(k)$.
Since $\{Y_t\}$ is $\operatorname{AR}(1)$,
$$
   γ_{\{Y_t\}}(k) = \sigma^2 \frac{φ^k}{1-φ^2}.
$$
Thus,
$$
   γ_{\{W_t\}}(k) = γ_{\{Y_t\}}(k) = \sigma^2 \frac{φ^k}{1-φ^2}.
$$

The variance of $\{W_t\}$ is given by
\begin{align*}
   \cov(W_t,W_t)
      &= \cov((φ - 1) Y_{t-1} + e_t, (φ - 1) Y_{t-1} + e_t)\\
      &= (φ - 1)^2 \cov(Y_{t-1},Y_{t-1}) + \cov(e_t,e_t)\\
      &= (φ - 1)^2 \frac{\sigma^2}{1-φ^2}  + \sigma^2\\
      &= \sigma^2\left(1 + \frac{(φ - 1)^2}{1-φ^2}\right).
\end{align*}

Thus, the autocorrelation function is given by
$$
   \rho_k = \frac{γ_{\{W_t\}}(k)}{γ_{\{W_t\}}(0)} = \frac{\sigma^2 \frac{φ^k}{1-φ^2}}{\sigma^2\left(1 + \frac{(φ - 1)^2}{1-φ^2}\right)},
$$
which simplifies to
$$
   \rho_k = \frac{\frac{φ^k}{1-φ^2}}{1 + \frac{(φ - 1)^2}{1-φ^2}} = \frac{φ^k}{2(1-φ)}.
$$

## Part (b)
In part (a), we found that
$$
   \var(W_t) = \sigma^2\left(1 + \frac{(φ - 1)^2}{1-φ^2}\right).
$$

# Problem 1.3
Suppose $Y_t = X_t + e_t$, where $\{e_t\}$ are normal white noise with mean $0$ and
variance $\sigma_e^2$.
The $\{X_t\}$ process is a stationary AR(1) defined by $X_t = φX_{t−1} + Z_t$,
where $\{Z_t\}$ is a zero mean normal white noise process with variance $\sigma_Z^2$.
As usual, in the AR(1) process, assume that $Z_t$ is independent
of $X_{t−1}, X_{t−2}, \ldots$.
Assume additionally that $\expect(e_t Z_s) = 0$ for all $t$ and $s$.

## Part (a)
\fbox{Show that $\{Y_t\}$ is stationary and find its autocovariance function, $γ_k$.}

To be stationary, $\{Y_t\}$ must have a constant mean and a a autocovariance that
is strictly a function of the lag.

The mean is given by
$$
   \expect(Y_t) = \expect(X_t)  + \expect(e_t).
$$ 
Since $X_t$ is AR(1) with mean $\delta / (1-φ) = 0$, we see that $\expect(Y_t) = 0$,
i.e., is a constant zero.

The variance is given by
$$
   \var(Y_t) = \var(X_t)  + \sigma^2.
$$
Since $X_t$ is AR(1), its variance is $\sigma_Z^2/(1-φ^2)$, thus
$$
   \var(Y_t) = \sigma_Z^2/(1-φ^2) + \sigma^2.
$$

The autocovariance of $\{Y_t\}$ is given by
$$
   γ_k = \cov(Y_t,Y_{t-k}) = \expect(Y_t Y_{t-k}) - \expect(Y_t)\expect(Y_{t-k}).
$$
Since $\{Y_t\}$ has a constant expectation of zero, this simplies to
$$
   γ_k = \cov(Y_t,Y_{t-k}) = \expect(Y_t Y_{t-k}).
$$

Observe that $Y_t = φ X_{t-1} + Z_t + e_t$ and
$$
   Y_t Y_{t-k} = (φ X_{t-1} + Z_t + e_t) Y_{t-k} = φ Y_{t-k} X_{t-1} + Y_{t-k} Z_t + Y_{t-k} e_t.
$$

The expectation of $Y_t Y_{t-k}$ is given by
\begin{align*}
   \expect(Y_t Y_{t-k})
      &= φ \expect(Y_{t-k} X_{t-1}) + \expect(Y_{t-k} Z_t) + \expect(Y_{t-k} e_t)\\
      &= φ \expect(Y_{t-k} X_{t-1}) + \expect(Y_{t-k}) \expect(Z_t) + \expect(Y_{t-k}) \expect(e_t)\\
      &= φ \expect(Y_{t-k} X_{t-1})\\
      &= φ \expect((X_{t-k} + e_t) X_{t-1})\\
      &= φ \expect(X_{t-1} X_{t-k} + e_t X_{t-1})\\
      &= φ \left(\expect(X_{t-1} X_{t-k}) + \expect(e_t X_{t-1})\right)\\
      &= φ \expect(X_{t-1} X_{t-k}).
\end{align*}

Since $\{X_t\}$ is AR(1), observe that the autocovariance function for $\{X_t\}$ is
$γ_{\{X_t\}}(k) = φ \expect(X_{t-1} X_{t-k})$, which has a closed-form solution
\begin{equation}
   γ_{\{X_t\}}(k) =
   \begin{cases}
      \frac{\sigma_Z^2}{1-φ^2}   & k = 0\\
      φ γ_{\{X_t\}}(k-1)         & k > 0.
   \end{cases}
\end{equation}

Thus, the autocovariance function for $\{Y_t\}$ is given by
\begin{equation}
   γ_k =
   \begin{cases}
      \frac{\sigma_Z^2}{1-φ^2} + \sigma_e^2   & k = 0\\
      γ_{\{X_t\}}(k)         & k > 0.
   \end{cases}
\end{equation}

Since its autocovariance function is strictly a function of lag and its
mean is a constant zero, $\{Y_t\}$ is stationary. Note that it is not just
weakly stationary, but strongly stationary given the normally distributed
random errors.

## Part (b)
\fbox{\begin{minipage}{.8\textwidth}
Show that the process $\{U_t\}$, where $U_t = Y_t − φY_{t−1} = (1 − φB)Y_t$,
has nonzero correlation only at lag 1 (excluding lag 0, of course!).
\end{minipage}}

The autocovariance is given by
\begin{align*}
   γ_{\{U_t\}}(k)
      &= \cov(U_t,U_{t-k})\\
      &= \cov(Y_t - φ Y_{t-1},Y_{t-k} - φ Y_{t-k-1}).
\end{align*}

Observe that $Y_t - φ Y_{t-1} = X_t + e_t - φ(X_{t-1} + e_{t-1})$.
Since $Z_t = X_t - φ X_{t-1}$, we see that
$$
   Y_t - φ Y_{t-1} = e_t + Z_t - φ e_{t-1}
$$
and
$$
   Y_{t-k} - φ Y_{t-k-1} = e_{t-k} + Z_{t-k} - φ e_{t-k-1}.
$$

Thus,
$$
   γ_{\{X_t\}}(k) = \cov(e_t + Z_t - φ e_{t-1}, e_{t-k} + Z_{t-k} - φ e_{t-k-1}).
$$
If $k > 1$, then $γ_{\{X_t\}}(k) = \cov(e_t + Z_t - φ e_{t-1}, e_{t-k} + Z_{t-k} - φ e_{t-k-1}) = 0$
since they have no terms in common.
If $k=1$, then
\begin{align*}
   γ_{\{X_t\}}(1)
      &= \cov(e_t + Z_t - φ e_{t-1}, e_{t-1} + Z_{t-1} - φ e_{t-2})\\
      &= \cov(-φ e_{t-1}, e_{t-1})\\
      &= -φ \var(e_{t-1})\\
      &= -φ \sigma_e^2,
\end{align*}
which is the only lag that is non-zero.


# Problem 1.4
Suppose that $\{e_t\}$ is a zero mean white noise process with variance $\sigma^2$.
Consider:
\begin{enumerate}
\item[(i)] $y_t = 0.80y_{t−1} − 0.15y_{t−2} + e_t − 0.30e_{t−1}$
\item[(ii)] $y_t = y_{t−1} − 0.50y_{t−2} + e_t − 1.2e_{t−1}$.
\end{enumerate}

## Part (a)
\fbox{Identify each model as an ARMA(p, q) process; that is, specify $p$ and $q$.}

\begin{enumerate}
\item We rewrite equation (i),
$$
   y_t = 0.80 \backshift y_t − 0.15 \backshift^2 y_t + e_t − 0.30 \backshift e_t.
$$       
Now, we rewrite it into the form
\begin{align*}
   (1 - 0.8 B + 0.15 B^2) y_t &= (1 - 0.3 B) e_t\\
   -20 (1 - 0.5 B)(1 - 0.3 B) y_t &= (1 - 0.3 B) e_t\\
   -20 (1 - 0.5 B) y_t &= e_t.
\end{align*}

We see that $y_t = 0.5 y_{t-1} - \frac{e_t}{20}$.
Two things should be pointed out.
First, assuming $e_t$ is symmetric with zero mean,
$- \frac{e_t}{20}$ is distributed the same as $\frac{e_t}{20}$.
Next, the variance of $\frac{e_t}{20}$ is $\frac{1}{400} \sigma^2$.

We let $W_t = \frac{1}{20} e_t$, and thus
$$
   y_t = 0.5 y_{t-1} + W_t,
$$
where $\{W_t\}$ is a zero mean white noise process with variance $\frac{1}{400} \sigma^2$
and $\{y_t\}$ is AR(1).

\item We rewrite equation (ii),
$$
   y_t = B y_t - 0.5 B^2 y_t + e_t - 1.2 B e_t.
$$       
Now, we rewrite it into the form
\begin{align*}
   (1 - B + 0.5 B^2) y_t &= (1 - 1.2 B) e_t\\
   0.5 (B - 1 + i)(B - 1 - i) y_t &= (1 - 1.2 B) e_t.
\end{align*}
We see that this is an ARMA(2,1) process.
\end{enumerate}

## Part (b)
\fbox{Determine whether each model is stationary and/or invertible.}
Time series (i) is AR(1) and is thus invertible.
We also know that it is stationary since $|φ| = |0.5| < 1$.

Time series (ii) is ARMA(2,1).
Let $φ(x) = (x - 1 + i)(x - 1 - i)$ which has roots $1+i$ and $1-i$, which both
modulus $\sqrt{2}$. This is larger than $1$, so it is invertible.
Let $\theta(x) = 1 - 1.2 x$ which has root $0.8\overbar{3}$. Since $|0.8\overbar{3}| < 1$,
it is not stationary.


















# Problem 2.1
The Johnson and Johnson dataset contains quarterly earnings per share for the
U.S. company Johnson & Johnson.
There are 84 quarters (21 years) measured from the first quarter of 1960 to the
last quarter of 1980.
To load the dataset, run the following: install.packages(”astsa”); library(astsa).
The dataset is under the name jj.
Do a log transformation of the original time series before answering the following.

## Preliminary analysis
We would like to take a look at a simple plot of the data, prior to any
transformations.

``` r
library(astsa)
tsdata <- ts(data=jj)
plot(tsdata)
```

![](exam2_files/figure-latex/unnamed-chunk-1-1.pdf)<!-- --> 

We see that the variance increases over time.
The log-transformation will fix this problem, as computed in the following code:

``` r
n <- length(tsdata)
A <- exp((1/n)*sum(log(tsdata)))
ys <- A*log(tsdata)
log_j <- log(tsdata)
```

## Part (a)
\fbox{\begin{minipage}{.8\textwidth}
Construct a time series plot for the logged data.
Comment on overall trend and seasonality variation.
\end{minipage}}

We generate the plot with the following R code:

``` r
plot(ys)
```

![](exam2_files/figure-latex/unnamed-chunk-3-1.pdf)<!-- --> 

The data has both seasonality and a (positive) trend.

## Part (b)
\fbox{\begin{minipage}{.8\textwidth}
Fit the a regression model on the logged data
$$
   y_t = β_0 + β_1 t + α_1 Q_2(t) + α_2 Q_3(t) + α_3 Q_4(t) + e_t,
$$
where $Q_i(t) = 1$ if time $t$ corresponds to quarter $i = 1, 2, 3$ and zero
otherwise.
Assume $e_t$ is a normal white noise sequence.
Report model coefficients estimates.
Superimpose the fitted values on the time plot in part (a).
Note: you will need to first create a variable for time and quarter.
To do that, you may use: t=1:84; qt=as.factor(rep(1:4,21)).
\end{minipage}}

We perform the model fitting using the following R code:

``` r
t <- 1:n
qt <- as.factor(rep(1:4,(n/4)))
q1 <- qt==1
q2 <- qt==2
q3 <- qt==3
m <- cbind(t,q1,q2,q3,ys)

# fit regression model to data
fit <- lm(ys~t+q1+q2+q3, data=m)
fit2 <- lm(log_j~t+q1+q2+q3, data=m)



qt2 <- as.factor(rep(1:4,(n/4)))
fit3 <- lm(log_j~t+qt)

# better approach:
#    fit <- lm(ys~t+qt)
# where qt are the factors (1,2,3,4)
```

The model coefficients are given by:

``` r
summary(fit)
```

```
## 
## Call:
## lm(formula = ys ~ t + q1 + q2 + q3, data = m)
## 
## Residuals:
##     Min      1Q  Median      3Q     Max 
## -0.8847 -0.2735 -0.0356  0.2553  0.8342 
## 
## Coefficients:
##              Estimate Std. Error t value Pr(>|t|)    
## (Intercept) -2.508319   0.111529 -22.490  < 2e-16 ***
## t            0.126112   0.001704  73.999  < 2e-16 ***
## q1           0.514570   0.116866   4.403 3.31e-05 ***
## q2           0.599431   0.116803   5.132 2.01e-06 ***
## q3           0.810985   0.116766   6.945 9.50e-10 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.3783 on 79 degrees of freedom
## Multiple R-squared:  0.9859,	Adjusted R-squared:  0.9852 
## F-statistic:  1379 on 4 and 79 DF,  p-value: < 2.2e-16
```

``` r
summary(fit2)
```

```
## 
## Call:
## lm(formula = log_j ~ t + q1 + q2 + q3, data = m)
## 
## Residuals:
##      Min       1Q   Median       3Q      Max 
## -0.29318 -0.09062 -0.01180  0.08460  0.27644 
## 
## Coefficients:
##               Estimate Std. Error t value Pr(>|t|)    
## (Intercept) -0.8312482  0.0369603 -22.490  < 2e-16 ***
## t            0.0417930  0.0005648  73.999  < 2e-16 ***
## q1           0.1705267  0.0387289   4.403 3.31e-05 ***
## q2           0.1986494  0.0387083   5.132 2.01e-06 ***
## q3           0.2687577  0.0386959   6.945 9.50e-10 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.1254 on 79 degrees of freedom
## Multiple R-squared:  0.9859,	Adjusted R-squared:  0.9852 
## F-statistic:  1379 on 4 and 79 DF,  p-value: < 2.2e-16
```

``` r
summary(fit3)
```

```
## 
## Call:
## lm(formula = log_j ~ t + qt)
## 
## Residuals:
##      Min       1Q   Median       3Q      Max 
## -0.29318 -0.09062 -0.01180  0.08460  0.27644 
## 
## Coefficients:
##               Estimate Std. Error t value Pr(>|t|)    
## (Intercept) -0.6607215  0.0358430 -18.434  < 2e-16 ***
## t            0.0417930  0.0005648  73.999  < 2e-16 ***
## qt2          0.0281227  0.0386959   0.727   0.4695    
## qt3          0.0982310  0.0387083   2.538   0.0131 *  
## qt4         -0.1705267  0.0387289  -4.403 3.31e-05 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.1254 on 79 degrees of freedom
## Multiple R-squared:  0.9859,	Adjusted R-squared:  0.9852 
## F-statistic:  1379 on 4 and 79 DF,  p-value: < 2.2e-16
```

In other words, the estimate is given by
$$
   \hat{y}_t = -2.508 + 0.126 t + 0.514 Q_1(t) + 0.599 Q_2(t) + 0.811 Q_3(t).
$$

The plot of the data with $\hat{y}_t$ superimosed onto it is given by:






































