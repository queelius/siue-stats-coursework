---
title: 'STAT 581 - Problem Set 5'
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




# Problem 1

A factorial experiment is used to develop a nitride etch process on a single wafer plasma etching tool.
The design factors are the gap between the electrodes and the RF power applied to the cathode. The response
variable is the etch rate for silicon nitride. The data is available on Blackboard as an Excel File.

## (a)
\fbox{\begin{minipage}{\textwidth}
Provide a general definition of an interaction effect.
\end{minipage}}

An interaction effect occurs when the effect of one factor depends on the
level of the other factors.

## (b)
\fbox{\begin{minipage}{\textwidth}
State the two factor with interaction ANOVA model.
Compute the estimates of the model parameters.
\end{minipage}}

### Two-factor with interaction ANOVA model
We consider a two-factor factorial experiment with $a=2$ levels of the \emph{gap}
factor, denoted by $A$, and $b=2$ levels of the \emph{RP power} factor, denoted
by $B$, for a total of $a b = 4$ treatment combinations.
Each treatment combination has $n=4$ replicates for a total of $N = n a b = 16$
observations.

We describe the observations in this two-factor factorial experiment
by the effects model where treatments are defined to be deviations from the
overall mean,
$$
  Y_{i j k} = \mu + \tau_i + \beta_j + (\tau\!\beta)_{i j} + \epsilon_{i j k}
  \begin{cases}
    i=1,\ldots,a\\
    j=1,\ldots,b\\
    k=1,\ldots,n
  \end{cases}
$$
where $\mu$ is the overall main effect, $\tau_i$ is the effect of the $i$-th
level of factor $A$, $\beta_j$ is effect of the $j$-th level of factor $B$,
$(\tau\!\beta)_{i j}$ is the interaction effect of the $i$-th level of factor
$A$ and the $j$-th level of factor $B$, and $\epsilon_{i j k}$ is the random
error component.

### Compute the estimates of the model parameters
A set of estimators for these model parameters are given by
\begin{align*}
  \hat{\mu} &= \bar{y}_{\cdots}\\
  \hat{\tau}_i &= \bar{y}_{i \cdot \cdot} - \hat{\mu}\\
  \hat{\beta}_j &= \bar{y}_{\cdot j \cdot}  - \hat{\mu}\\
  \widehat{(\tau\!\beta)}_{i j} &= \bar{y}_{i j \cdot} - \hat{\mu} - \hat{\tau}_i - \hat{\beta}_j,
\end{align*}
and thus an estimator of the $k$-th observation given factor $A$ at level $i$
and factor $B$ at level $j$ is given by
$$
  \hat{y}_{i j k} = \hat{\mu} + \hat{\tau}_i + \hat{\beta}_j + \widehat{(\tau\!\beta)}_{i j},
$$
which simplifies to
$$
  \hat{y}_{i j k} = \bar{y}_{i j \cdot}.
$$

We perform these computations using R:

``` r
library("readxl")
data = read_excel("handout5data.xlsx")
gap = as.factor(na.omit(data$gap))
rfp = as.factor(na.omit(data$rfp))
rate = na.omit(data$rate)

# use contrasts to define parameter restrictions for the two way ANOVA model
contrasts(gap) = contr.sum
contrasts(rfp) = contr.sum

# we are still using aov to perform ANOVA computations.
# for two way ANOVA, we include two factors plus an interaction in the model statement
two.way.mod = aov(rate ~ gap+rfp+gap:rfp)

# the command below is used to print the model parameter estimates
dummy.coef(two.way.mod)
```

```
## Full coefficients are 
##                                                      
## (Intercept):     776.0625                            
## gap:                  0.8       1.2                  
##                   50.8125  -50.8125                  
## rfp:                  275       325                  
##                 -153.0625  153.0625                  
## gap:rfp:          0.8:275   1.2:275  0.8:325  1.2:325
##                  -76.8125   76.8125  76.8125 -76.8125
```

We see that $\hat{\tau}_1 = 50.8125$.
By the constraint that $\tau_1 + \tau_2 = 0$, $\hat{\tau}_2 = -50.8125$.
The remaining parameter estimates can be observed directly on the R output,
e.g., $\widehat{(\tau\!\beta)}_{2 1} = 76.8125$.

### Remark
Assuming the model is appropriate, would it be reasonable to say that an
estimator of the mean response given factor $A$ at level $i$ and factor $B$ at
level $j$ is given by
$$
  \hat{E}(Y_{i j} | A=i,B=j) = \bar{y}_{i j \cdot}?
$$

Since we may be primarily just be looking for evidence of effects, coming up
with a more sophisticated, explanatory model may not be warranted at this stage
of the analysis.

If we find some evidence that there are some factors or interactions thereof
that effect the response, we may then, if deemed useful, try to use a
more restrictive model. For instance, a general linear regression model may not
only provide a more accurate and precise estimator of the conditional response,
but also more explanatory power (e.g., the coefficients in a linear regression
model have an obvious interpretation).

## (c)
\fbox{\begin{minipage}{\textwidth}
Test for an interaction effect.
Compute the test statistic $F_{A B}$ and the $p$-value.
Provide an interpretation, stated in the context of the problem.
\end{minipage}}

We test for an interaction effect with:

``` r
summary(two.way.mod)
```

```
##             Df Sum Sq Mean Sq F value   Pr(>F)    
## gap          1  41311   41311   23.77 0.000382 ***
## rfp          1 374850  374850  215.66 4.95e-09 ***
## gap:rfp      1  94403   94403   54.31 8.62e-06 ***
## Residuals   12  20858    1738                     
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
```

We see that $F_{A B} = 54.31$ which has a $p$-value of $.000$.
Thus, the experiment finds an interaction effect between the gap between the
electrodes and the RF power applied to the cathode on the etch rate for silicon
nitride.

## (d)
\fbox{\begin{minipage}{\textwidth}
Graph an interaction plot.
\end{minipage}}


``` r
# the command below is used to create an interaction plot
# the x.factor will be plotted on the horizontal axis.
# the trace.factor will be plotted as separate curves
interaction.plot(x.factor=gap,trace.factor=rfp,response=rate)
```

![](hw5_files/figure-latex/unnamed-chunk-4-1.pdf)<!-- --> 

This interaction effect demonstrates an interaction effect, since the effect
of one factor depends on the level of the other factor.

## (e)
\fbox{\begin{minipage}{\textwidth}
Perform pairwise comparisons using the Fisher LSD method to investigate
differences between the treatment combinations.
Provide the grouping information.
\end{minipage}}

### Fisher LSD
















