---
title: 'Time Series Analysis - 478 - HW #4'
author: "Alex Towell (atowell@siue.edu)"
output:
  pdf_document:
    df_print: kable
    #toc: true
#    toc_depth: 3
    latex_engine: pdflatex
header-includes:
 - \usepackage{amsmath}
 - \usepackage{mathtools}
 - \usepackage{amsthm}
 # - \usepackage{amsbsy}
 - \usepackage{bm}
 - \usepackage{minted}
 - \usepackage{xcolor}
---
\newcommand{\var}{\operatorname{Var}}
\newcommand{\expect}{\operatorname{E}}
\newcommand{\corr}{\operatorname{Corr}}
\newcommand{\cov}{\operatorname{Cov}}
\newcommand{\ssr}{\operatorname{SSR}}
\newcommand{\se}{\operatorname{SE}}
\newcommand{\mat}[1]{\bm{#1}}
\newcommand{\eval}[2]{\left. #1 \right\vert_{#2}}



# Problem 1
\fbox{
\begin{minipage}{.9\textwidth}
Suppose that simple exponential smoothing is being used to forecast a process, $y_t=\mu+\epsilon_t$.
However, at the start of period $t^*$, the mean of the process shifts to a new
mean level $\mu+\delta$.
The mean remains at this new level for subsequent time periods.
Calculate the expected value of the simple exponential moving average.
(Note: you need to discuss cases for $T > t^*$ and $T < t^*$.)
\end{minipage}}

In the simple exponential moving average, we model the mean of the time series with
$$
   \hat{y}_t = \frac{1-\theta}{1-\theta^t} \sum_{j=0}^{t-1} \theta^j y_{t-j}.
$$

The expected value is
$$
   \expect(\hat{y}_t) = \frac{1-\theta}{1-\theta^t} \sum_{j=0}^{t-1} \theta^j \expect(y_{t-j}).
$$
Given $T < t^*$, the process is $y_T = \mu + \epsilon_T$ and given
$T \geq t^*$, the process is $y_T = \mu + \delta + \epsilon_T$.

Letting $T = t-j$ and solving for $j$ in $t-j < t^*$, we see that we may
partition the summation over $j \geq t - t^*$ and $j < t - t^*$,
\begin{align*}
   \expect(\hat{y}_t)
      &= \frac{1-\theta}{1-\theta^t}
      \left\{
         \sum_{j=0}^{t-t^*-1} \theta^j (\mu + \delta)+ \sum_{j=t-t^*}^{t-1} \theta^j \mu
      \right\}\\
      &= \frac{1-\theta}{1-\theta^t}
      \left\{
         \sum_{j=0}^{t-t^*-1} \theta^j \delta + \sum_{j=0}^{t-1} \theta^j \mu
      \right\}.
\end{align*}

Expanding the product,
\begin{align*}
   \expect(\hat{y}_t)
      &= \frac{1-\theta}{1-\theta^t}\delta \sum_{j=0}^{t-t^*-1} \theta^j  + \mu\\
      &= \frac{1-\theta}{1-\theta^t}\delta \frac{1-\theta^{t-t^*}}{1-\theta}  + \mu\\
      &= \frac{1-\theta^{t-t^*}}{1-\theta^t}\delta + \mu\\
      &= \left(
         \frac{1}{1-\theta^t} -
         \frac{\theta^{t-t^*}}{1-\theta^t}
         \right) \delta + \mu.
\end{align*}

For large $t$, $\theta^t \approx 0$, and so we simplify the above to
$$
   \expect(\hat{y}_t) =
   \left(
      1 - \theta^{t-t^*}
   \right) \delta + \mu.
$$
We consider two degenerate cases given by $t^* = t$ and $t^* = 0$
which respectively have expectations given by $\expect(\hat{y}_t) = \mu$
and $\expect(\hat{y}_t) = \sigma + \mu$ (when we use the assumption that
$\theta_t \approx 0$).




# Problem 2

Consider the time series $\{y_T\} = (14,19,18,22,17,28,43,45,62,60)$.

## Parts (a)-(d)

We use the following R code to generate and populate the table.

``` r
discount <- 0.2
tsdata <- ts(c(14,19,18,22,17,28,43,45,62,60))

# part (a): calculate the simple moving average with span=3.
ma3 <- MA(tsdata,3)

# part (b): calculate the simple (1st order) exponential moving average using
# discount lambda = 0.2 and initial value y1.
#ema1 <- EMA(tsdata,tsdata[1],discount)
ema1 <- EMA(tsdata,14,discount)

# part (c): calculate the 2nd order exponential moving average using discount
# lambda = 0.2 and initial values y1.
ema2_data <- EMA2(tsdata,tsdata[1],tsdata[1],discount,discount)
#ema2_data <- EMA2(tsdata,tsdata[1],tsdata[1],discount,discount)
ema2 <- as.numeric(unlist(ema2_data[2]))

# part (d): calculate the (unbiased) linear trend estimator
yhat <- as.numeric(unlist(ema2_data[3]))

prob2 <- data.frame(
   t = 1:length(tsdata),
   yt = tsdata,
   ma = ma3,
   ema1 = ema1,
   ema2 = ema2,
   yhat = yhat,
   delta = tsdata-yhat)

# parts (a)-(d): generate the table with the previously computed values
knitr::kable(prob2,caption="Parts (a)-(d)",padding=-1L,
             col.names =c("time",
                          "$y_T$",
                          "MA","$\\hat{y}_T^{(1)}$",
                          "$\\hat{y}_T^{(2)}$",
                          "$\\hat{y}_T$",
                          "$y_T-\\hat{y}_T$"))
```



Table: Parts (a)-(d)

|time|$y_T$|     MA|$\hat{y}_T^{(1)}$|$\hat{y}_T^{(2)}$|$\hat{y}_T$|$y_T-\hat{y}_T$|
|--:|---:|------:|---------------:|---------------:|---------:|-------------:|
|  1|  14|     NA|        14.00000|        14.00000|  14.00000|      0.000000|
|  2|  19|     NA|        15.00000|        14.20000|  15.80000|      3.200000|
|  3|  18|17.00000|        15.60000|        14.48000|  16.72000|      1.280000|
|  4|  22|19.66667|        16.88000|        14.96000|  18.80000|      3.200000|
|  5|  17|19.00000|        16.90400|        15.34880|  18.45920|     -1.459200|
|  6|  28|22.33333|        19.12320|        16.10368|  22.14272|      5.857280|
|  7|  43|29.33333|        23.89856|        17.66266|  30.13446|     12.865536|
|  8|  45|38.66667|        28.11885|        19.75389|  36.48380|      8.516198|
|  9|  62|50.00000|        34.89508|        22.78213|  47.00803|     14.991974|
| 10|  60|55.66667|        39.91606|        26.20892|  53.62321|      6.376792|

## Part (e)
\fbox{Finish the table by calculate the errors. What is the SSE?}
The sum of squared error (SSE) is computed and displayed by the following
R code:


``` r
sse = sum((tsdata-yhat)^2)
cat("The sum of squared error is ", sse, ".")
```

```
## The sum of squared error is  562.0258 .
```

Note that this is not the forecast one-step sum of squared error.
I believe you would specifically ask for that if that is what you wanted,
and the computation of the one-step ahead SSE seemed a bit tedious.

## Part (g)
\fbox{\begin{minipage}{.8\textwidth}
Make a one-step-ahead forecast for Time=11 based on the linear trend process.
If the true observation is 72, what’s your prediction error?
Also provide the prediction interval.
\end{minipage}}


``` r
# here's how we can compute the one-step-ahead forecast.
# i decided to do this computation manually, rather than using the forecasting
# library.
b1hat <- (ema1[10] - ema2[10]) * discount / (1-discount)
y10_one_step <- yhat[10] + b1hat
print(y10_one_step)
```

```
## [1] 57.04999
```

We see that $\hat{y}_{11}(10) \approx 57$.
If the true observation $y_{11} = 72$, then the $1$-step forecast error is
$$
   e_{10}(1) = y_{11} - \hat{y}_{11}(10) = 72 - 57 = 15.
$$

To compute the intervals, we use the forecast library.

``` r
library("forecast")
dEMA <- holt(tsdata,h=1,level=c(95),initial="simple",alpha=discount,beta=discount)
summary(dEMA)
```

```
## 
## Forecast method: Holt's method
## 
## Model Information:
## Holt's method 
## 
## Call:
## holt(y = tsdata, h = 1, level = c(95), initial = "simple", alpha = discount, 
##     beta = discount)
## 
##   Smoothing parameters:
##     alpha = 0.2 
##     beta  = 0.2 
## 
##   Initial states:
##     l = 14 
##     b = 5 
## 
##   sigma:  9.2384
## Error measures:
##                      ME     RMSE     MAE       MPE    MAPE     MASE      ACF1
## Training set -0.5745289 9.238406 8.18886 -16.84568 31.0149 1.188706 0.5912006
## 
## Forecasts:
##    Point Forecast    Lo 95    Hi 95
## 11       58.88679 40.77985 76.99373
```

``` r
# we got this estimate of one-step-ahead variance of
# the forecast errors from the holt procedure
rmse <- 9.238
lo <- y10_one_step - 1.96 * rmse
hi <- y10_one_step + 1.96 * rmse
print(y10_one_step)
```

```
## [1] 57.04999
```

``` r
print(lo)
```

```
## [1] 38.94351
```

``` r
print(hi)
```

```
## [1] 75.15647
```

The $95\%$ prediction interval computed from the \emph{forecast} library is
$$
   [40.78, 76.99].
$$

As a slight twist, I thought I would use the estimate of the variance of
the forecast errors from the \emph{holt} procedure's output and apply it
to the previous approach, resulting in the interval
$$
   [38.94, 75.16].
$$

Observe that these prediction interval estimates differ, primarily due to the
fact that the \emph{holt} procedure uses a different set of initial values,
but they are reasonably close.

# Problem 3
Consider the Dow Jones Index data on Blackboard.
The dataset contains yearly Dow Jones closing index from year 1981 to 2016.

## Part (a)
\fbox{Read the data into R. Then construct a time plot ($D_j$ index v.s. time).}

The following R code is used to read the data file and generate the time series plot:




















