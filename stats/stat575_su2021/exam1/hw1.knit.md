---
title: 'Computational Statistics - STAT 575 - HW #1'
author: "Alex Towell (atowell@siue.edu)"
output:
  pdf_document:
    df_print: kable
    toc: true
    toc_depth: 2
    #latex_engine: pdflatex
    latex_engine: xelatex
header-includes:
 - \usepackage{amsmath}
 - \usepackage{mathtools}
 - \usepackage{amsthm}
 # - \usepackage{amsbsy}
 - \usepackage{bm}
 - \usepackage{xcolor}
---


# Problem 1

Write your own code and find solution to the equation $x^3 + x - 4 = 0$ using
Newton’s method and the secant method.
Compare the number of iterations needed for different starting values for the
two methods.

## Solution: Newton's method

If we have some function $f : \mathbb{R} \mapsto \mathbb{R}$ and we wish to
find a root of $f$, i.e., an $x$ such that $f(x) = 0$, we may use Newton's method.

We take an initial guess of the root as $x_0$ and try to refine it
with a linear approximation of $f$ given by
$$
  L(f | x_0) \coloneqq \lambda x.f(x_0) + f'(x_0)(x-x_0).
$$

Now, we may approximate a root of $f$ with a root of $L(f|x_0)$,
$$
  L(f|x_0)(x) = 0,
$$
which may be rewritten as
$$
  f(x_0) + f'(x_0)(x-x_0) = 0.
$$
Solving for a root $x$ of $L(f|x_0)$ we get the result
$$
  x = x_0 - \frac{f(x_0)}{f'(x_0)}.
$$

Hoping that $x$ results in a better approximation of the root of $f$ than
$x_0$, we approximate $f$ with $L(f|x)$ and repeat the process.

Generalizing this result, we obtain the iterative procedure
$$
  x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)}.
$$
We continue this process until we obtain some stopping condition, e.g.,
$|x_{i+1} - x_i| < \epsilon$.

Letting $f(x) \coloneqq x^3 + x - 4$ and $f'(x) = 3x^2 + 1$ and substituting
into the above result, we get the result
$$
  x_{i+1} = x_i - \frac{x_i^3+x_i-4}{3x_i^2+1}.
$$

We implement a general procedure for Newton's method:

``` r
newton_method <- function(f,dfdx,x0,eps,debug=T)
{
  n <- 0
  repeat
  {
    x1 <- x0 - f(x0) / dfdx(x0)
    n <- n + 1
   
    if (debug==T) { cat("iteration=",n," x=",x1,"\n") }
    if(abs(x1 - x0) < eps)
    {
      break
    }
    x0 <- x1
  }
  
  list(root=x0,iter=n)
}
```

We take an initial guess of $x_0 = 1$ and $\epsilon = 1 \times 10^{-6}$ and
run the following R code to solve for a root of $f$ using Newton's method:

``` r
f <- function(x) { x^3 + x - 4 }
dfdx <- function(x) { 3*x^2 + 1 }
eps <- 1e-6
x0 <- 1
result <- newton_method(f,dfdx,x0,eps)
```

```
## iteration= 1  x= 1.5 
## iteration= 2  x= 1.387097 
## iteration= 3  x= 1.378839 
## iteration= 4  x= 1.378797 
## iteration= 5  x= 1.378797
```

We obtain $x \approx 1.3787967$ after $5$ iterations.
When we plug that approximate root into $f$ we obtain the result
$f(1.3787967) = \ensuremath{7.3825959\times 10^{-9}}$, which is approximately zero.

## Solution: Secant method

In Newton's method, we linearize $f$ using the derivative of $f$. If, instead,
we use the secant of $f$ with respect to two inputs $x_i$ and $x_{i+1}$, as
given by
$$
  \frac{f(x_{i+1}) - f(x_i)}{x_{i+1}-x_i},
$$
we get the iterative procedure
$$
  x_{i+2} = x_{i+1} - f(x_{i+1})\frac{x_{i+1}-x_i}{f(x_{i+1}) - f(x_i)},
$$
which requires two initial values $x_0$ and $x_1$.

We define the secant method as a function given by:


``` r
secant_method <- function(f,x0,x1,eps,debug=T)
{
  n <- 0
  repeat
  {
    x2 <- x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
    n <- n + 1
    
    if (debug==T) { cat("iteration=",n," x=",x2,"\n") }
    
    if(abs(x2-x1) < eps)
    {
      break
    }
    x0 <- x1
    x1 <- x2
  }
  
  list(root=x1,iter=n)
}
```

We let $x_0 = 0$, $x_1 = 1$, and keep everything else the same and run the
secant method with the following R code:

``` r
x0 <- 0
x1 <- 1
result <- secant_method(f,x0,x1,eps,F)
```

We obtain $x \approx 1.3787965$ after $7$ iterations.
When we plug that approximate root into $f$ we obtain the result
$f(1.3787965) = \ensuremath{-1.268648\times 10^{-6}}$, which is approximately zero.

Note that this is $2$ more iterations than Newton's method.

## Comparison of Newton's method versus secant method

We perform $10000$ trials to get a better view of how the two methods,
Newton and secant, compare over many different initial guesses.

We generate the data with:

``` r
n <- 10000
from <- 0
to <- 4
by <- (to-from)/n
newt_sols <- vector(length=n)
sec_sols <- vector(length=n)
i <- 1
for (x0 in seq(from=from, to=to, by=by))
{
  newt_sols[i] <- newton_method(f,dfdx,x0,eps,F)$iter
  sec_sols[i] <- secant_method(f,x0,x0+1,eps,F)$iter
  i <- i + 1
}
```

We summarize the results and report them with:

``` r
cat("mean iterations\n",
    "newton => ", mean(newt_sols), "\n",
    "secant => ", mean(sec_sols), "\n")
```

```
## mean iterations
##  newton =>  5.819618 
##  secant =>  7.231077
```

We see that Newton's method, on average, requires
$1.4114589$ fewer iterations before the stopping
condition is satisfied.

# Problem 2
Poisson regression. The Ache hunting data set has $n = 47$ observations
recording is the number of monkeys killed over a period of days with each hunter
along with hunter’s age.
It is of interest to estimate and quantify the monkey kill rate as a function of
hunter’s age. Hunting prowess confers elevated status among the group, so a
natural question is whether hunting ability improves with age,
and at which age hunting ability is best.

Hand-code Newton-Raphson in R to fit the Poisson regression model
$$
  \mathit{monkeys}_i \sim \operatorname{Pois}\left(\exp(\log \mathit{days}_i  + \theta_1 + \theta_2 \mathit{age}_i + \theta_3 \mathit{age}_i^2)\right).
$$

Feel free to use jacobian and hessian in the numDeriv R package. You may need a sets of crude
starting values.
I run a linear regression for the "empirical log-rates" and get starting values
$(5.99, 0.167, 0.001)$.
Feel free to use those. Compare your result with glm() function in R using

``` r
glm(monkeys~age+I(age^2), family="poisson", offset=log(days), data=d)
```

## Solution

We are given the following data:






























