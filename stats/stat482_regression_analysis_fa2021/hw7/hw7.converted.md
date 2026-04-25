 row

#### Alex Towell (<atowell@siue.edu>) {#alex-towell-atowellsiue.edu .author}

The goal is to study the relationship between patient satisfaction ([\\(y\\)]{.math .inline}) and patient's age ([\\(x_1\\)]{.math .inline}), severity of illness ([\\(x_2\\)]{.math .inline}), and anxiety level ([\\(x_3\\)]{.math .inline}). Refer to the data from Exercise 6.15.

### Computations

``` {.sourceCode .r}
data = read.table('CH06PR15.txt')
names(data) = c("y", "x1","x2","x3")
add.mod = lm(y ~ x1 + x2 + x3, data=data)
coef(summary(add.mod))
```

    ##                Estimate Std. Error    t value     Pr(>|t|)
    ## (Intercept) 158.4912517 18.1258887  8.7439162 5.260955e-11
    ## x1           -1.1416118  0.2147988 -5.3147960 3.810252e-06
    ## x2           -0.4420043  0.4919657 -0.8984452 3.740702e-01
    ## x3          -13.4701632  7.0996608 -1.8972967 6.467813e-02

The [\\(t\\)]{.math .inline} statistics are given by [\\[\\begin{align*} t_1\^* &= -5.315\\\\ t_2\^* &= -0.898\\\\ t_3\^* &= -1.897. \\end{align*}\\]]{.math .display}

### Explanation

The statistic [\\(t\_\\ell\^*\\)]{.math .inline} is testing the partial effect of input [\\(x\_\\ell\\)]{.math .inline}, accounting for the effects of all other inputs. (Recall that in the additive model, [\\(\\beta\_\\ell\\)]{.math .inline} represents the [\\(\\ell\\)]{.math .inline}-th input effect, with all other inputs held fixed.)

### Computation

``` {.sourceCode .r}
null.mod = lm(y ~ 1, data=data)
anova(null.mod,add.mod)
```

    ## Analysis of Variance Table
    ## 
    ## Model 1: y ~ 1
    ## Model 2: y ~ x1 + x2 + x3
    ##   Res.Df     RSS Df Sum of Sq      F    Pr(>F)    
    ## 1     45 13369.3                                  
    ## 2     42  4248.8  3    9120.5 30.052 1.542e-10 ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

We see that [\\(F\^* = 30.052\\)]{.math .inline}.

### Explanation

This is a test for the joint effect of [\\((x_1,x_2,x_3)\\)]{.math .inline} on response [\\(y\\)]{.math .inline}.

### Computation

``` {.sourceCode .r}
anova(add.mod)
```

    ## Analysis of Variance Table
    ## 
    ## Response: y
    ##           Df Sum Sq Mean Sq F value    Pr(>F)    
    ## x1         1 8275.4  8275.4 81.8026 2.059e-11 ***
    ## x2         1  480.9   480.9  4.7539   0.03489 *  
    ## x3         1  364.2   364.2  3.5997   0.06468 .  
    ## Residuals 42 4248.8   101.2                      
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

We see that [\\[\\begin{align*} \\mathrm{SS\_{R}}(X_1) &= 8275.389,\\\\ \\mathrm{SS\_{R}}(X_2\|X_1) &= 480.915,\\\\ \\mathrm{SS\_{R}}(X_3\|X_1,X_2) &= 364.160. \\end{align*}\\]]{.math .display}

### Explanation

[\\(\\mathrm{SS\_{R}}(X_1)\\)]{.math .inline} measures the variation in response (satisfaction) explained by [\\(X_1\\)]{.math .inline} (age), not accounting for information on [\\(X_2\\)]{.math .inline} (severity of illness) and [\\(X_3\\)]{.math .inline} (anxiety level); [\\(\\mathrm{SS\_{R}}(X_2\|X_1)\\)]{.math .inline} measures the variation in satisfaction explained by [\\(X_2\\)]{.math .inline} beyond that explained by [\\(X_1\\)]{.math .inline} and not accounting for information in [\\(X_3\\)]{.math .inline}; lastly, [\\(\\mathrm{SS\_{R}}(X_3\|X_1,X_2)\\)]{.math .inline} measures the variation in satisfaction explained by [\\(X_3\\)]{.math .inline} beyond that explained by [\\(X_1\\)]{.math .inline} and [\\(X_2\\)]{.math .inline}.

### Additional remarks

Note that [\\[ \\mathrm{SS\_{R}}(X_1,X_2,X_3) = \\mathrm{SS\_{R}}(X_1) + \\mathrm{SS\_{R}}(X_2\|X_1) + \\mathrm{SS\_{R}}(X_3\|X_1,X_2) \\]]{.math .display} measures the variation in satisfaction explained by [\\(X_1\\)]{.math .inline}, [\\(X_2\\)]{.math .inline}, and [\\(X_3\\)]{.math .inline}. The additive nature of [\\(\\mathrm{SS\_{R}}\\)]{.math .inline} is reminiscent of Shannon information [\\(\\operatorname{H}\\)]{.math .inline}, where if [\\(X_1,X_2,X_3\\)]{.math .inline} are random variables, then [\\[ \\operatorname{H}(X_1,X_2,X_3) = \\operatorname{H}(X_1) + \\operatorname{H}(X_2\|X_1) + \\operatorname{H}(X_3\|X_1,X_2). \\]]{.math .display} If [\\(X_1\\)]{.math .inline}, [\\(X_2\\)]{.math .inline}, and [\\(X_3\\)]{.math .inline} are independent, then [\\(\\operatorname{H}(X_1,X_2,X_3) = \\operatorname{H}(X_1) + \\operatorname{H}(X_2) + \\operatorname{H}(X_3)\\)]{.math .inline}. Likewise, if [\\(X_1\\)]{.math .inline}, [\\(X_2\\)]{.math .inline}, and [\\(X_3\\)]{.math .inline} explain independent aspects of the variation in the response, I speculate that [\\(\\mathrm{SS\_{R}}(X_1,X_2,X_3) = \\mathrm{SS\_{R}}(X_1) + \\mathrm{SS\_{R}}(X_2) + \\mathrm{SS\_{R}}(X_3)\\)]{.math .inline}. Unlike joint probabilities or relative likelihoods, which are multiplicative, information (entropy) and [\\(\\mathrm{SS\_{R}}\\)]{.math .inline} are additive. This additive property of information is desirable since, for instance, having [\\(k\\)]{.math .inline} times as large of an i.i.d sample for, say, estimating [\\(\\theta\\)]{.math .inline}, should convey [\\(k\\)]{.math .inline} times as much information about [\\(\\theta\\)]{.math .inline} (i.e., less variance in an estimator of [\\(\\theta\\)]{.math .inline} based on the information in such a sample).

That said, it is not clear to me how to fit [\\(\\mathrm{SS\_{R}}\\)]{.math .inline} into this conceptual framework, if indeed it would even be prudent to do so.

### Part (a)

``` {.sourceCode .r}
m1 = lm(y ~ x1, data=data)
m13 = lm(y ~ x1+x3, data=data)
anova(m1,m13)
```

    ## Analysis of Variance Table
    ## 
    ## Model 1: y ~ x1
    ## Model 2: y ~ x1 + x3
    ##   Res.Df    RSS Df Sum of Sq      F  Pr(>F)   
    ## 1     44 5093.9                               
    ## 2     43 4330.5  1    763.42 7.5804 0.00861 **
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

We see that [\\(F\_{3\|1}\^* = 7.580 \\; \\text{(\$p$-value = \$.009$)}\\)]{.math .inline}. When we already have [\\(X_1\\)]{.math .inline} in the model, adding [\\(X_3\\)]{.math .inline} would be an appropriate decision.

### Part (b)

``` {.sourceCode .r}
m12 = lm(y ~ x1+x2, data=data)
m123 = add.mod
anova(m12,m123)
```

    ## Analysis of Variance Table
    ## 
    ## Model 1: y ~ x1 + x2
    ## Model 2: y ~ x1 + x2 + x3
    ##   Res.Df    RSS Df Sum of Sq      F  Pr(>F)  
    ## 1     43 4613.0                              
    ## 2     42 4248.8  1    364.16 3.5997 0.06468 .
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

We see that [\\(F\_{3\|1,2}\^* = 3.600 \\; \\text{(\$p$-value = \$.065$)}\\)]{.math .inline}. When we already include [\\(X_1\\)]{.math .inline} and [\\(X_2\\)]{.math .inline} in the model, the need for [\\(X_3\\)]{.math .inline} is not as great as before.

### Part (c)

In part (a), we are testing for the effect of anxiety level on patient satisfaction after accounting for the effect of patient age.

In part (b), we are testing for the effect of anxiety level on patient satisfaction after accounting for both the effect of patient age and severity of illness.
