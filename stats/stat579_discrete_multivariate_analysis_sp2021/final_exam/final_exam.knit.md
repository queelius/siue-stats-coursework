---
title: 'Discrete Multivariate Analysis - 579 - Final Exam'
author: "Alex Towell (atowell@siue.edu)"
fontfamily: mathpazo
fontsize: 11pt
geometry: margin=1in
output:
  pdf_document:
    toc: true
    toc_depth: 2
    keep_tex: true
    latex_engine: xelatex
    df_print: kable
    number_sections: true
  html_document:
    df_print: paged
header-includes:
 - \usepackage{alex}
---



# Part 1
A sample of elderly patients were given a psychiatric examination to determine
whether symptoms of senility are present.
One explanatory variable is a patient's score on the Wechsler Adult Intelligence
Scale (WAIS).


``` r
wais.data <- data.frame(
  wais=c(4,5,6,7,8,9,10,11,12,13,14,15,16,17,18),
  n=c(2,1,2,3,2,6,6,6,2,6,7,3,4,1,1),
  senile=c(1,1,1,2,2,2,2,1,0,1,2,0,0,0,0))

print(wais.data)
```

```
##    wais n senile
## 1     4 2      1
## 2     5 1      1
## 3     6 2      1
## 4     7 3      2
## 5     8 2      2
## 6     9 6      2
## 7    10 6      2
## 8    11 6      1
## 9    12 2      0
## 10   13 6      1
## 11   14 7      2
## 12   15 3      0
## 13   16 4      0
## 14   17 1      0
## 15   18 1      0
```

## Problem 1
\fbox{\begin{minipage}{.9\textwidth}
Define the logistic regression model, including notation for the input matrix
$X$, the response vector $y$, the parameter vector $\beta$, and the
probability vector $\pi(\beta)$.
\end{minipage}}

The data is $(\v{x_1},y_1),(\v{x_2},y_2),\ldots,(\v{x_n},y_n)$ where $\v{x_j}$
is a column vector of explanatory variables and $y_j$ is a binary variable.

The probability model is given by
$$
  y_i \sim \operatorname{BIN}(1,\pi(\v{x_i})).
$$
That is, $\pi(\v{x})$ models probability as a function of $\v{x}$.

The logistic regression model is given by
$$
  \log \left(\frac{\pi(\v{x_i})}{1-\pi(\v{x_i})}\right) = \v{x_i}' \v{\beta},
$$
such that if we solve for $\pi(\v{x_i})$ we get the result
$$
  \pi(\v{x_i}) = \frac{\exp(\v{x_i}' \v{\beta})}{1+\exp(\v{x_i}' \v{\beta})}
$$
where $\v{x_i}'$ denotes the transpose of $\v{x_i}$.

The response vector $\v{y}$ of dimension $n \times 1$ is given by
$$
\v{y} =
\begin{pmatrix}
  y_1\\
  y_2\\
  \vdots\\
  y_n
\end{pmatrix}.
$$

The input (design) martix $\mat{X}$ of dimension $n \times (p+1)$ is given by
$$
\mat{X} =
\begin{pmatrix}
  \v{x_1}'\\
  \v{x_2}'\\
  \vdots\\
  \v{x_n}'
\end{pmatrix}
=
\begin{pmatrix}
  1 & x_{1 1} & \cdots & x_{1 p}\\
  1 & x_{2 1} & \cdots & x_{2 p}\\
  \vdots  & \vdots & \ddots & \vdots\\
  1 & x_{n 1} & \cdots & x_{n p}
\end{pmatrix}.
$$

The parameter vector $\v{\beta}$ of dimension $(p+1) \times 1$ is
given by
$$
\v{\beta} =
\begin{pmatrix}
  \beta_0\\
  \beta_1\\
  \beta_2\\
  \vdots\\
  \beta_p
\end{pmatrix}
$$
where $\beta_0$ denotes the \emph{intercept} in the linear predictor.

The probability vector
$$
\v{\pi}(\v{\beta}) =
\begin{pmatrix}
  \pi(\v{x_1})\\
  \pi(\v{x_2})\\
  \vdots\\
  \pi(\v{x_n})\\
\end{pmatrix}
$$
where $\v{x_j}$ are the explanatory varibles as described previously.

## Problem 2

### Part (a)
\fbox{\begin{minipage}{.9\textwidth}
State the likelihood equation for the MLE $\v{\hat{\beta}}$ as a normal equation.
\end{minipage}}

The normal equations for $\hat{\v{\beta}}$ are given by
$$
  \mat{X}'(\v{y} - \v{\pi}(\hat{\v{\beta}})) = \v{0}.
$$

### Part (b)
\fbox{\begin{minipage}{.9\textwidth}
State the equation for $\hat{V} = \hat{\cov}(\hat{\beta})$, the estimated
variance matrix for $\hat{\beta}$.
\end{minipage}}

The equation for $\hat{\mat{V}}$ is given by
$$
  \hat{\mat{V}} = \hat{\operatorname{\mat{cov}}}(\v{\hat{\beta}}) = (\mat{X}' \hat{\mat{W}} \mat{X})^{-1},
$$
which is a $(p+1) \times (p+1)$ covariance matrix (estimate) and
$\hat{\mat{W}} = \operatorname{\mat{diag}}(\pi_i(1-\pi_i))$
is an $n \times n$ diagonal matrix.

### Part (c)
\fbox{\begin{minipage}{.9\textwidth}
Compute $\hat{\beta}$ and $\hat{V}$ from the WAIS data.
\end{minipage}}


``` r
wais.mod = glm(senile/n ~ wais,weights=n, family=binomial, data=wais.data)

# define the intercept and slope parameter estimates
# alpha
a = wais.mod$coefficients[1]
# beta
b = wais.mod$coefficients[2] 

# this is beta = (a,b)'
print(c(a,b))
```

```
## (Intercept)        wais 
##   2.4810957  -0.3189723
```

``` r
# compute the variance/covariance matrix for parameter estimates
V.hat = vcov(wais.mod)
print(V.hat)
```

```
##             (Intercept)        wais
## (Intercept)   1.4447178 -0.13154006
## wais         -0.1315401  0.01301779
```

We see that $\hat{\v{\beta}} = (2.481, -0.319)'$ and
$$
  \hat{\mat{V}} =
  \begin{pmatrix}
    1.445 & -0.132\\
    -0.132 & 0.013
  \end{pmatrix}.
$$

## Problem 3
### Part (a)
\fbox{\begin{minipage}{.9\textwidth}
State the equation for a 95\% confidence interval for $\beta_j$.
\end{minipage}}

A $95\%$ confidence interval for $\beta_j$ is $\hat{\beta}_j \pm 1.96 \sqrt{\hat{V}_{j j}}$,
where $\hat{V}_{j j}$ is the $j$-th element along the diagonal of $\hat{\mat{V}}$.

### Part (b)
\fbox{\begin{minipage}{.9\textwidth}
Compute a 95\% confidence interval for $\beta_1$ from the WAIS data, and provide
an interpretation in the context of the problem.
\end{minipage}}


``` r
# compute the s.e. for beta.hat from the estimated variance/covariance matrix
se.b = sqrt(V.hat[2,2])

# compute a 95% confidence interval estimate for beta
L.beta = b - 1.96*se.b
U.beta = b + 1.96*se.b
print(b)
```

```
##       wais 
## -0.3189723
```

``` r
print(c(L.beta,U.beta))
```

```
##       wais       wais 
## -0.5425995 -0.0953451
```

We estimate that $\beta_1$ is between $-0.543$ and $-0.095$.

Note that $\beta_1$ can generally be thought of as an effect size for the
association between WAIS and senility, in particular the change in the log odds
with respect to a a change in the input level of WAIS.

We estimate that the log-odds of senility \emph{decreases} by $0.319$
units from a unit \emph{increase} in the WAIS measure, which makes sense.

## Problem 4
### Part (a)
\fbox{\begin{minipage}{.9\textwidth}
State the equations for a 95\% confidence interval for odds ratio $\theta$.
\end{minipage}}

The \emph{odds} at $\v{x}$ are given by
$$
  \Omega(\v{x}) = \frac{\pi(\v{x})}{1-\pi(\v{x})} = \exp(\v{x}' \v{\beta}).
$$

Then,
$$
  \log \Omega(\v{x}) = \log \left(\frac{\pi(\v{x})}{1-\pi(\v{x})}\right) = \v{x}' \v{\beta}.
$$

Let $\v{u_j}$ be defined as
a unit vector of dimension $p+1$ such that every
element except the $j$-th element is zero.

Then
\begin{align*}
  \beta_j &= \log \Omega(\v{x}+\v{u_j}) - \log \Omega(\v{x})\\
          &= \log \frac{\Omega(\v{x}+\v{u_j})}{\Omega(\v{x})},
\end{align*}
which is the log odds ratio for comparing inputs $\v{x}$ and
$\v{x} + \v{u_j}$.
So, $\exp(\beta_j)$ is the odds ratio $\theta_j$ for comparing inputs $\v{x}$ and
$\v{x} + \v{u_j}$.

### Simple logistic regression
Since $p=2$, we only have one explanatory variable $x$ and thus we may rephrase
this as $\beta_1$ is the log odds ratio for comparing input levels $x$ and
$x+1$ and therefore $\exp(\beta_1)$ is the odds ratio $\theta$ for comparing
input levels $x$ and $x+1$.

A $95\%$ confidence interval for $\theta$ is given by
$$
  \left[\exp(l_{\beta_1}),\exp(u_{\beta_1})\right]
$$
where $l_{\beta_1} = \hat{\beta}_1 - 1.96 \sqrt{\hat{V}_{1 1}}$ and
$u_{\beta_1} = \hat{\beta}_1 + 1.96 \sqrt{\hat{V}_{1 1}}$.

Note that we use zero-based indexing, i.e., the first element in the matrix
is at index $(0,0)$ instead of $(1,1)$.

### Part (b)
\fbox{\begin{minipage}{.9\textwidth}
Compute a 95\% confidence interval for $\theta$ from the WAIS data.
\end{minipage}}


``` r
# compute an estimate of the odds ratio
theta <- exp(b)

# compute a 95% confidence interval estimate for the odds ratio
L.theta = exp(L.beta)
U.theta = exp(U.beta)

# print confidence interval
print(c(L.theta,U.theta))
```

```
##      wais      wais 
## 0.5812354 0.9090592
```

Since the log-odds is given by $\beta_1$, the odds $\theta$ is given by
$\exp(\beta_1)$ with a point estimate $\hat{\theta} = \exp(\hat{\beta}_1)$
given by
$$
  0.727.
$$
From the R computation, we see that a $95\%$ confidence interval for $\theta$ is
given by
$$
  (0.581, 0.909),
$$
which is not symmetric around the point estimate.

## Problem 5
### Part (a)
\fbox{\begin{minipage}{.9\textwidth}
State the equations for a 95\% confidence interval for the logit $L_o$ at input level $x_o$:
\end{minipage}}

We estimate the logit with
$$
  \hat{L}_o = \v{x}_o' \v{\hat{\beta}}
$$
which has a variance
$$
  \var(\hat{L}_o) = \v{x}_o' \mat{V} \v{x}_o
$$
where $\mat{V} = \mat{\cov}(\hat{\v{\beta}})$.

We do not know $\mat{V}$, so we estimate $\sigma_{\hat{L}_o}$ with
$$
  \hat{\sigma}(\hat{L}_o) = \sqrt{\v{x}_o' \hat{\mat{V}} \v{x}_o}.
$$

Thus, a $95\%$ confidence interval for $L_o$ is given by
$$
  \hat{L}_o \pm 1.96 \hat{\sigma}(\hat{L}_o).
$$

#### Simple logistic regression

Since this is simple logistic regression with $p=1$ explanatory variables,
we may simplify the presentation.

Let $\v{x}_o' = (1,x_o)$.
Then, these equations simplify to
$$
  \hat{L}_o = \hat{\beta_0} + \hat{\beta_1} x_o,
$$
and
$$
  \var(\hat{L}_o) = \var(\hat{\beta_0}) +
    x_o^2 \var(\hat{\beta_1}) + 2x_0 \cov(\hat{\beta_1},\hat{\beta_1}).
$$

\begin{align*}
  \sigma_{\hat{L}_o}^2
    &= \hat{V}_{0 0} + x_o^2 \hat{V}_{1 1} + 2x_o \hat{V}_{0 1}.
\end{align*}


\begin{align*}
  \hat{\sigma}(\hat{L}_o)
    &= \sqrt{\var(\hat\beta_0) + x_o^2 \var() + 2x_o \hat{V}_{0 1}}\\
    &= \sqrt{\hat{V}_{0 0} + x_o^2 \hat{V}_{1 1} + 2x_o \hat{V}_{0 1}}.
\end{align*}


A $95\%$ CI for $L_o$ is given by
$$
  (1,x_o)^t \beta \pm 1.96 \sqrt{(1,x_o) \hat{V} (1,x_o)^t}.
$$


### Part (b)
\fbox{\begin{minipage}{.9\textwidth}
Compute a 95\% confidence interval for $L_o$ at input level $x_o = 10$ from the WAIS data.
\end{minipage}}


``` r
xo <- 10
L.hat <- a + b*xo # should agree with L0.hat below

x0 = as.matrix(c(1,xo))
print(x0)
```

```
##      [,1]
## [1,]    1
## [2,]   10
```

``` r
beta.hat = as.matrix(c(a,b))

L0.hat = t(x0) %*% beta.hat
se0 = sqrt(t(x0)%*%V.hat%*%x0)
print(c(L0.hat,se0))
```

```
## [1] -0.7086274  0.3401400
```

``` r
L.L0 = L0.hat - 1.96*se0
U.L0 = L0.hat + 1.96*se0
print(c(L.L0,U.L0))
```

```
## [1] -1.37530182 -0.04195301
```

## Problem 6
### Part (a)
\fbox{\begin{minipage}{.9\textwidth}
State the equations for a 95\% confidence interval for the probability $\pi_o$ at
input level $x_o$.
\end{minipage}}


### Part (b)
\fbox{\begin{minipage}{.9\textwidth}
Compute a 95\% confidence interval for $\pi_o$ at input level $x_o = 10$ from the
WAIS data, and provide an interpretation in the context of the problem.
\end{minipage}}


``` r
pi.hat <- exp(L.hat) / (1+exp(L.hat))
#print(pi.hat)
print(c(exp(L.L0) / (1+exp(L.L0)),exp(U.L0) / (1+exp(U.L0))))
```

```
## [1] 0.2017646 0.4895133
```

# Part 2
Applicants for graduate school are classified according to department, sex, and
admission status.
A goal of the study is to determine the role an applicant's sex plays in the
determination of admission status.

## Problem 1
\fbox{\begin{minipage}{.9\textwidth}
Define a main effects logistic regression model $M$ having two binary input
variables.
Include notation for the design matrix $X$, and the parameter vector $\beta$.
Provide an interpretation for each of the effect parameters in $\beta$, stated
in the context of the problem.
\end{minipage}}

$\operatorname{logit}(\pi)(x_1,x_2) = \beta_0 + \beta_1 x_1 + \beta_2 x_2$.

$$
\mat{X} = 
\begin{pmatrix}
  1 & x_{1 1} & x_{1 2}\\
  1 & x_{2 1} & x_{2 2}\\
  \vdots &\vdots & \vdots
  1 & x_{n 1} & x_{n 2}\\
\end{pmatrix}
$$





``` r
# department and sex are defined through indicator variables
grad.data <- data.frame(dep=c(0,0,1,1),
                        sex=c(0,1,0,1),
                        yes=c(235,38,122,103),
                        no=c(35,7,93,69))

# define row sample sizes
grad.data$n = grad.data$yes + grad.data$no

# define the interaction variable
grad.data$dep.sex = grad.data$dep * grad.data$sex

print(grad.data)
```

```
##   dep sex yes no   n dep.sex
## 1   0   0 235 35 270       0
## 2   0   1  38  7  45       0
## 3   1   0 122 93 215       0
## 4   1   1 103 69 172       1
```

``` r
#fit each of the candidate models
m.s = glm(yes/n ~ sex+dep+sex*dep,weights=n,family=binomial,data=grad.data)
m.12 = glm(yes/n ~ sex+dep,weights=n,family=binomial,data=grad.data)
m.1 = glm(yes/n ~ sex,weights=n,family=binomial,data=grad.data)
m.2 = glm(yes/n ~ dep,weights=n,family=binomial,data=grad.data)
m.0 = glm(yes/n ~ 1,weights=n,family=binomial,data=grad.data)



#compute probability estimates under each of the candidate models
pred.S = predict(m.s,type = "response")
pred.12 = predict(m.12,type = "response")
pred.1 = predict(m.1,type = "response")
pred.2 = predict(m.2,type = "response")
pred.0 = predict(m.0,type = "response")
```


## Problem 2
\fbox{\begin{minipage}{.9\textwidth}
Provide notation for the design matrix $X_S$ and parameter vector $\beta_S$
for the saturated model $M_S$.
Provide a brief description of an interaction effect.
\end{minipage}}



## Problem 3
\fbox{\begin{minipage}{.9\textwidth}
For each of the models $M_O$, $M_1$, $M_2$, provide notation for the design
matrix and a brief description of the model effects, stated in the context of
the problem.
\end{minipage}}

## Problem 4
\fbox{\begin{minipage}{.9\textwidth}
Compute the deviance statistic $D$, and give degrees of freedom $\delta df$, for
each of the models $M_O,M_1,M_2,M,M_S$ from the grad school data.
Provide a general form for the statistic $G^2$, and the degrees of freedom for
the reference chi-square distribution, for testing a reduced model $M_R$ against
a full model $M_F$.
\end{minipage}}


``` r
# create a table for candidate model deviances
# the rows represent the model, the deviance, and the degrees of freedom
deviance.table=matrix(c(
  0,m.12$deviance,m.1$deviance,m.2$deviance,m.0$deviance,
  0,m.12$df.residual,m.1$df.residual,m.2$df.residual,m.0$df.residual),
  nrow=5)
dimnames(deviance.table) = list(c("MS","M","M1","M2","MO"),c("deviance","delta.df"))
print(deviance.table)
```

```
##      deviance delta.df
## MS  0.0000000        0
## M   0.4589638        1
## M1 67.8794451        2
## M2  0.6036551        2
## MO 73.1962870        3
```

First, $G^2(M\,|\,M_S) = D(M)$ is called the deviance of $M$.

The likelihood ratio statistic $G^2$ for testing a reduced model $M_R$ against
a full model $M_F$ is given by
\begin{align}
  G^2(M_R\,|\,M_S)
    &= [-2 L_R]-[-2 L_F]\\
    &= \left([-2 L_R]-[-2 L_S]\right)-\left([-2 L_F]-[-2 L_S] \right)\\
    &= G^2(M_R\,|\,M_S)-G^2(M_F\,|\,M_S)\\
    &= D(M_R) - D(M_F).
\end{align}

The $df$ is given by $df = P_F - P_R = (P_S - P_R) - (P_S - P_F) = \Delta df_R - \Delta df_F$,
and so the reference distribution if $\chi^2$ with $df = \Delta df_R - \Delta df_F$
degrees of freedom.

## Problem 5
\fbox{\begin{minipage}{.9\textwidth}
Compute the likelihood statistic $G^2$ for testing reduced model $M$ against
full model $M_S$ from the grad school data, and provide an interpretation in the
context of the problem.
\end{minipage}}


``` r
# test the main effects model against the interaction (saturated) model
anova(m.12,m.s,test = "LRT")
```

```
## Analysis of Deviance Table
## 
## Model 1: yes/n ~ sex + dep
## Model 2: yes/n ~ sex + dep + sex * dep
##   Resid. Df Resid. Dev Df Deviance Pr(>Chi)
## 1         1    0.45896                     
## 2         0    0.00000  1  0.45896   0.4981
```

The statistic $G^2(M\,|\,M_S) = 0.459$ which has a $p$-value of $0.498$.
Thus, we conlcude the main effect model (no interaction on inputs) is
compatible with the observed data.

## Problem 6
\fbox{\begin{minipage}{.9\textwidth}
Compute the likelihood statistic $G^2$ for testing reduced model $M_O$ against
full model $M_2$ from the grad school data, and provide an interpretation in the
context of the problem.
\end{minipage}}


``` r
# test for the input 2 effect, first using a marginal effect test,
# then using a partial effect test
anova(m.0,m.2,test = "LRT")
```

```
## Analysis of Deviance Table
## 
## Model 1: yes/n ~ 1
## Model 2: yes/n ~ dep
##   Resid. Df Resid. Dev Df Deviance  Pr(>Chi)    
## 1         3     73.196                          
## 2         2      0.604  1   72.593 < 2.2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
```

``` r
anova(m.1,m.12,test = "LRT")
```

```
## Analysis of Deviance Table
## 
## Model 1: yes/n ~ sex
## Model 2: yes/n ~ sex + dep
##   Resid. Df Resid. Dev Df Deviance  Pr(>Chi)    
## 1         2     67.879                          
## 2         1      0.459  1    67.42 < 2.2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
```


## Problem 7
\fbox{\begin{minipage}{.9\textwidth}
Compute the likelihood statistic $G_2$ for testing reduced model $M_1$ against
full model $M$ from the grad school data, and provide an interpretation in the
context of the problem.
Include an explanation of how this test differs from that of the previous
problem.
\end{minipage}}


``` r
#test the independence model against the main effects model
anova(m.0,m.12,test = "LRT")
```

```
## Analysis of Deviance Table
## 
## Model 1: yes/n ~ 1
## Model 2: yes/n ~ sex + dep
##   Resid. Df Resid. Dev Df Deviance  Pr(>Chi)    
## 1         3     73.196                          
## 2         1      0.459  2   72.737 < 2.2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
```

``` r
#test for the input 1 effect, first using a marginal effect test, then using a partial effect test
anova(m.0,m.1,test = "LRT")
```

```
## Analysis of Deviance Table
## 
## Model 1: yes/n ~ 1
## Model 2: yes/n ~ sex
##   Resid. Df Resid. Dev Df Deviance Pr(>Chi)  
## 1         3     73.196                       
## 2         2     67.879  1   5.3168  0.02112 *
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
```

``` r
anova(m.2,m.12,test = "LRT")
```

```
## Analysis of Deviance Table
## 
## Model 1: yes/n ~ dep
## Model 2: yes/n ~ sex + dep
##   Resid. Df Resid. Dev Df Deviance Pr(>Chi)
## 1         2    0.60366                     
## 2         1    0.45896  1  0.14469   0.7037
```

## Problem 8
\fbox{\begin{minipage}{.9\textwidth}
Compute estimates of the response probabilities based on model $M_1$ from the
grad school data, and provide an interpretation in the context of the problem.
\end{minipage}}


``` r
#create a display a table for the probability estimates
prob.table = matrix(c(pred.S,pred.12,pred.1,pred.2,pred.0),nrow = 4)
#dimnames(prob.table) = list(c("female low","female high","male low","male high"),
#                            c("prob.S","prob.12","prob.1","prob.2","prob.0"))
                
print(prob.table,digits = 4)
```

```
##        [,1]   [,2]   [,3]   [,4]   [,5]
## [1,] 0.8704 0.8655 0.7361 0.8667 0.7094
## [2,] 0.8444 0.8737 0.6498 0.8667 0.7094
## [3,] 0.5674 0.5736 0.7361 0.5814 0.7094
## [4,] 0.5988 0.5912 0.6498 0.5814 0.7094
```



``` r
print(grad.data)
```

```
##   dep sex yes no   n dep.sex
## 1   0   0 235 35 270       0
## 2   0   1  38  7  45       0
## 3   1   0 122 93 215       0
## 4   1   1 103 69 172       1
```

<!-- \inputminted{R}{test_functions.R} -->
