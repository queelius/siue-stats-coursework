 row

#### Alex Towell (<atowell@siue.edu>) {#alex-towell-atowellsiue.edu .author}

Refer to the data from Exercise 1.20

Data has been collected on [\\(45\\)]{.math .inline} calls for routine maintenance. The goal is to explore the relationship between the number of copiers serviced [\\((x)\\)]{.math .inline} and the time in minutes spent to complete the service [\\((y)\\)]{.math .inline}. Let [\\(x_h = 3\\)]{.math .inline} copiers.

# Part (1)

[\\(\\mu_h\\)]{.math .inline} is the mean response [\\(\\operatorname{E}(Y_h\|x_h=3)\\)]{.math .inline}. A confidence interval for [\\(\\mu_h\\)]{.math .inline} is given by [\\[ \\hat{Y}\_h \\pm t\_{\\alpha/2,n-2} \\operatorname{se}(\\hat{Y}\_h). \\]]{.math .display}

``` {.sourceCode .r}
alpha = .05
x.h = 3
data = read.table('CH01PR20.txt')
colnames(data)=c("time","copiers")
mod = lm(time~copiers, data=data)
predict(mod,level=1-alpha,data.frame(copiers=x.h),interval="confidence")
```

    ##        fit     lwr      upr
    ## 1 44.52559 41.1476 47.90357

We see that a CI for [\\(\\mu_h\\)]{.math .inline} is given by [\\([44.526,47.904]\\)]{.math .inline}.

# Part (2)

We denote [\\(Y\|X=x_h\\)]{.math .inline} by [\\(Y_h\\)]{.math .inline}. Assume [\\[ Y_h \\sim \\mathcal{N}(\\beta_0 + \\beta_1 x_h, \\sigma\^2). \\]]{.math .display} Then, if we wish to predict [\\(Y_h\\)]{.math .inline} with [\\((\\beta_0,\\beta_1,\\sigma)\\)]{.math .inline} known, the interval [\\[ \\beta_0 + \\beta_1 x \\pm z\_{\\alpha/2} \\sigma. \\]]{.math .display} includes the observed value of [\\(Y_h\\)]{.math .inline} with probability [\\(1-\\alpha\\)]{.math .inline}. For predicting a single outcome [\\(Y_h\\)]{.math .inline}, the uncertainty of the prediction is quantified by [\\(\\operatorname{V}(Y_h) = \\sigma\^2\\)]{.math .inline}. For a given [\\(\\alpha\\)]{.math .inline}, the smaller the variance the smaller the interval.

However, if [\\((\\beta_0,\\beta_1,\\sigma\^2)\'\\)]{.math .inline} is unknown, we have the additional source uncertainty due to a random sample [\\(\\{(Y_h,x_h)\\}\\)]{.math .inline} being used to estimate [\\((\\beta_0,\\beta_1,\\sigma\^2)\'\\)]{.math .inline}.

Let `pred` = [\\(P_h = Y\_{h(\\rm{new})} - \\hat{Y}\_h\\)]{.math .inline} denote the random . Then, [\\(\\operatorname{E}(P_h) = 0\\)]{.math .inline} and [\\[\\begin{align*} \\operatorname{V}(P_h) &= \\operatorname{V}(Y\_{h(\\rm{new})}) + \\operatorname{V}(\\hat{Y}\_h)\\\\ &= \\sigma\^2\\left[1 + \\frac{1}{n} + \\frac{(x_h - \\bar{x})\^2}{\\rm{SS}\_x}\\right]. \\end{align*}\\]]{.math .display}

Since we do not know [\\(\\sigma\^2\\)]{.math .inline}, we estimate it with [\\(\\rm{MSE}\\)]{.math .inline} and thus a prediction interval for [\\(Y\_{h(\\rm{new})}\\)]{.math .inline} is given by [\\[ \\hat{Y}\_h \\pm t\_{\\alpha/2,n-2} \\hat{\\operatorname{sd}}(P_h) \\]]{.math .display} where [\\[ \\hat{\\operatorname{sd}}(P_h) = \\sqrt{\\rm{MSE}\\left(1 + \\frac{1}{n} + \\frac{(x_h-\\bar{x})\^2}{\\rm{SS}\_x}\\right)}. \\]]{.math .display}

``` {.sourceCode .r}
predict(mod,data.frame(copiers=3),level=1-alpha,interval="predict")
```

    ##        fit      lwr      upr
    ## 1 44.52559 26.23515 62.81603

We see that the PI for [\\(Y\_{h(\\rm{new})}\\)]{.math .inline} is given by [\\([26.235,62.816]\\)]{.math .inline}.

# Part (3)

A confidence interval is for the mean service time for all service calls with [\\(3\\)]{.math .inline} copiers to service.

A prediction interval is for the service time of a single service call with [\\(3\\)]{.math .inline} copiers to service.

# Part (4)

Let `pred.mean` = [\\(\\bar{P}\_h = \\bar{Y}\_{h(\\rm{new})} - \\hat{Y}\_h\\)]{.math .inline} denote the random . Then, [\\(\\operatorname{E}(\\bar{P}\_h) = 0\\)]{.math .inline} and [\\[\\begin{align*} \\operatorname{V}(\\bar{P}\_h) &= \\operatorname{V}(\\bar{Y}\_{h(\\rm{new})}) + \\operatorname{V}(\\hat{Y}\_h)\\\\ &= \\sigma\^2 \\left[\\frac{1}{m} + \\frac{1}{n} + \\frac{(x_h - \\bar{x})\^2}{\\rm{SS}\_x}\\right]. \\end{align*}\\]]{.math .display}

Since we do not know [\\(\\sigma\^2\\)]{.math .inline}, we estimate it with [\\(\\rm{MSE}\\)]{.math .inline} and thus a prediction interval for [\\(\\bar{Y}\_{h(\\rm{new})}\\)]{.math .inline} is given by [\\[ \\hat{Y}\_h \\pm t\_{\\alpha/2,n-2} \\hat{\\operatorname{sd}}(\\bar{P}\_h) \\]]{.math .display} where [\\[ \\hat{\\operatorname{sd}}(\\bar{P}\_h) = \\sqrt{\\rm{MSE}\\left(\\frac{1}{m} + \\frac{1}{n} + \\frac{(x_h-\\bar{x})\^2}{\\rm{SS}\_x}\\right)} \\]]{.math .display}

``` {.sourceCode .r}
b0 = mod$coefficients[1]; names(b0) = NULL
b1 = mod$coefficients[2]; names(b1) = NULL

residual = mod$residuals
n = length(residual)
sse = sum(residual^2)
mse = sse / (n-2)
x = data$copiers

x.bar = mean(x)
ssx = sum((x-x.bar)^2)

y.hat = b0 + b1*x.h 
m = 10
var.pred.mean = mse*(1/m + 1/n + (x.h-x.bar)^2/ssx)

lower.ynew = y.hat - qt(alpha/2,n-2,lower.tail=F)*sqrt(var.pred.mean)
upper.ynew = y.hat + qt(alpha/2,n-2,lower.tail=F)*sqrt(var.pred.mean)

c(lower.ynew,upper.ynew)
```

    ## [1] 37.91320 51.13798

We see that the PI for [\\(\\bar{Y}\_{h(\\rm{new})}\\)]{.math .inline} is given by [\\[ [37.913, 51.138]. \\]]{.math .display}

# Part (5)

We predict that the mean service time for [\\(10\\)]{.math .inline} service calls with [\\(3\\)]{.math .inline} copiers each will be between [\\(37.913\\)]{.math .inline} and [\\(51.138\\)]{.math .inline}.

# Part (6)

The variance of `pred.mean` = [\\(\\bar{P}\_h\\)]{.math .inline} is given by [\\[ \\operatorname{V}(\\bar{P}\_h) = \\sigma\^2 \\left(\\frac{1}{m} + \\frac{1}{n} + \\frac{(x_h-\\bar{x})\^2}{\\rm{SS}\_x}\\right) \\]]{.math .display} which we may rewrite as [\\[\\begin{align*} \\operatorname{V}(\\bar{P}\_h) &= \\frac{\\sigma\^2}{m} + \\sigma\^2\\left(\\frac{1}{n} + \\frac{(x_h-\\bar{x})\^2}{\\rm{SS}\_x}\\right)\\\\ &= \\operatorname{V}(\\bar{Y}\_{h(\\rm{new})}) + \\operatorname{V}(\\hat{Y}\_h). \\end{align*}\\]]{.math .display}

As [\\(m \\to \\infty\\)]{.math .inline}, [\\(\\operatorname{V}(\\bar{Y}\_{h(\\rm{new})}) \\to 0\\)]{.math .inline}, and thus [\\[ \\lim\_{m \\to \\infty} \\operatorname{V}(\\bar{P}\_h) = \\operatorname{V}(\\hat{Y}\_h). \\]]{.math .display}

A CI estimate of the mean service time [\\(\\mu_h\\)]{.math .inline} can be interpreted as a prediction of the sample mean [\\(\\bar{Y}\_{h(\\rm{new})}\\)]{.math .inline} for a large number of service time responses.
