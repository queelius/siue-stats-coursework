# Problem 1

A soft drink bottler is interested in studying the effects on a filling process. A factorial experiment is run using three factors: percent carbonation (in %), operating pressure (in psi), and line speed (in bpm). The response variable is deviation from the target fill height. The experiment consists of [\\(n=2\\)]{.math .inline} runs for each of the [\\(a b c = 12\\)]{.math .inline} treatment combinations. The data is available on Blackboard as an Excel File.

## Preliminary analysis

The three-factor factorial experiment with [\\(a=3\\)]{.math .inline} levels of the *carbonation* factor (in %), denoted by [\\(A\\)]{.math .inline}, [\\(b=2\\)]{.math .inline} levels of the operating *pressure* (in psi), denoted by [\\(B\\)]{.math .inline}, and [\\(c=2\\)]{.math .inline} levels of the line *speed* (in bpm), denoted by [\\(C\\)]{.math .inline}. Each treatment combination has [\\(n=2\\)]{.math .inline} replicates for a total of [\\(N=a b c n=24\\)]{.math .inline} observations. The response variable [\\(y\\)]{.math .inline} is deviation from the target fill height.

We describe the observations in the three-factor factorial experiment by the fixed-effects interaction model where treatments are defined to be deviations from the overall mean, [\\[Y\_{i j k \\ell} = \\mu + \\tau_i + \\beta_j + \\gamma_k + (\\tau\\!\\beta)\_{i j} + (\\tau\\!\\gamma)\_{i k} + (\\beta\\!\\gamma)\_{j k} + (\\tau\\!\\beta\\gamma)\_{i j k} + \\epsilon\_{i j k \\ell} \\begin{cases} i = 1,\\ldots,a=3\\\\ j = 1,\\ldots,b=2\\\\ k = 1,\\ldots,c=2\\\\ \\ell = 1,\\ldots,n=2\\\\ \\end{cases}\\]]{.math .display} where [\\(\\mu\\)]{.math .inline} is the overall main effect, [\\(\\tau_i\\)]{.math .inline} is the effect of the [\\(i\\)]{.math .inline}-th level of factor [\\(A\\)]{.math .inline}, [\\(\\beta_j\\)]{.math .inline} is the effect of the [\\(j\\)]{.math .inline}-th level of factor [\\(B\\)]{.math .inline}, and [\\(\\gamma_k\\)]{.math .inline} is the effect of the [\\(k\\)]{.math .inline}-th level of factor [\\(C\\)]{.math .inline}. The interaction effects may also be observed using the same labeling, e.g., [\\((\\tau\\!\\gamma)\_{i k}\\)]{.math .inline} is the interaction effect of the [\\(i\\)]{.math .inline}-th level of factor [\\(A\\)]{.math .inline} and the [\\(k\\)]{.math .inline}-th level of factor [\\(C\\)]{.math .inline}.

## (a)

 snugshade

    ##             Df Sum Sq Mean Sq F value   Pr(>F)    
    ## A            2 252.75  126.38 178.412 1.19e-09 ***
    ## B            1  45.37   45.37  64.059 3.74e-06 ***
    ## C            1  22.04   22.04  31.118  0.00012 ***
    ## A:B          2   5.25    2.63   3.706  0.05581 .  
    ## A:C          2   0.58    0.29   0.412  0.67149    
    ## B:C          1   1.04    1.04   1.471  0.24859    
    ## A:B:C        2   1.08    0.54   0.765  0.48687    
    ## Residuals   12   8.50    0.71                     
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

The tests for each of the main effects and a test of an interaction between carbon [\\((A\\)]{.math .inline}) and pressure [\\((B\\)]{.math .inline}) is given by the following table:

  effects                              [\\(F\^*\\)]{.math .inline}   [\\(p\\)]{.math .inline}-value
  ------------------------------------ ------------------------------ --------------------------------
  [\\(A\\)]{.math .inline}             [\\(178.4\\)]{.math .inline}   [\\(.000\\)]{.math .inline}
  [\\(B\\)]{.math .inline}             [\\(64.1\\)]{.math .inline}    [\\(.000\\)]{.math .inline}
  [\\(C\\)]{.math .inline}             [\\(31.1\\)]{.math .inline}    [\\(.000\\)]{.math .inline}
  [\\(A \\times B\\)]{.math .inline}   [\\(3.7\\)]{.math .inline}     [\\(.056\\)]{.math .inline}

## (b)

If an interaction plot is parallel, or nearly so, then there is no need to include the interaction term.

In the [\\(3\\)]{.math .inline}-factor ANOVA model, a [\\(3\\)]{.math .inline}-factor interaction occurs when a [\\(2\\)]{.math .inline}-factor interaction depends on the level of the [\\(3\\)]{.math .inline}rd factor.

## (c)

From the earlier results, we saw that factors [\\(A\\)]{.math .inline} (carbon), [\\(B\\)]{.math .inline} (pressure), and [\\(C\\)]{.math .inline} (speed) were statistically significant, but only the interaction between factor [\\(A\\)]{.math .inline} and [\\(B\\)]{.math .inline} (carbon and pressure) had any significance.

### Additive model

The additive model is given by [\\[Y\_{i j k \\ell}\^{(R)} = \\mu + \\tau_i + \\beta_j + \\gamma_k + \\epsilon\_{i j k \\ell}.\\]]{.math .display} Thus, [\\[E(Y\_{i j k}\^{(R)}) = \\mu + \\tau_i + \\beta_j + \\gamma_k.\\]]{.math .display}

We fit the additive model with:

 snugshade
 Highlighting
mod.R [=]{style="color: 0.56,0.35,0.01"} [aov]{style="color: 0.13,0.29,0.53"}(y [**\~**]{style="color: 0.81,0.36,0.00"} A[**+**]{style="color: 0.81,0.36,0.00"}B[**+**]{style="color: 0.81,0.36,0.00"}C)

We define the estimated means for the models with:

 snugshade
 Highlighting
fits.R [=]{style="color: 0.56,0.35,0.01"} [predict]{style="color: 0.13,0.29,0.53"}(mod.R)

The interaction plots for the additive where the left and right plots are respectively for factor [\\(C\\)]{.math .inline} at levels [\\(1\\)]{.math .inline} and [\\(2\\)]{.math .inline}.

 snugshade
 Highlighting
[par]{style="color: 0.13,0.29,0.53"}([mfrow=]{style="color: 0.13,0.29,0.53"}[c]{style="color: 0.13,0.29,0.53"}([1]{style="color: 0.00,0.00,0.81"},[2]{style="color: 0.00,0.00,0.81"})) [for]{style="color: 0.13,0.29,0.53"} (i [in]{style="color: 0.13,0.29,0.53"} [1]{style="color: 0.00,0.00,0.81"}[**:**]{style="color: 0.81,0.36,0.00"}[nlevels]{style="color: 0.13,0.29,0.53"}(C)) { [**interaction.plot**]{style="color: 0.13,0.29,0.53"}(A[C[**==**]{style="color: 0.81,0.36,0.00"}[levels]{style="color: 0.13,0.29,0.53"}(C)[i]],B[C[**==**]{style="color: 0.81,0.36,0.00"}[levels]{style="color: 0.13,0.29,0.53"}(C)[i]], fits.R[C[**==**]{style="color: 0.81,0.36,0.00"}[levels]{style="color: 0.13,0.29,0.53"}(C)[i]], [xlab=]{style="color: 0.13,0.29,0.53"}[\"A\"]{style="color: 0.31,0.60,0.02"}, [ylab=]{style="color: 0.13,0.29,0.53"}[\"mean response\"]{style="color: 0.31,0.60,0.02"}, [trace.label=]{style="color: 0.13,0.29,0.53"}[\"B\"]{style="color: 0.31,0.60,0.02"}) }

### Interaction model

The model that includes interactions between factors [\\(A\\)]{.math .inline} (carbon) and [\\(B\\)]{.math .inline} (pressure) is given by [\\[Y\_{i j k \\ell}\^{(F)} = \\mu + \\tau_i + \\beta_j + \\gamma_k + (\\tau\\!\\beta)\_{i j} + \\epsilon\_{i j k \\ell}.\\]]{.math .display} Thus, [\\[E(Y\_{i j k}\^{(F)}) = \\mu + \\tau_i + \\beta_j + \\gamma_k + (\\tau\\!\\beta)\_{i j}.\\]]{.math .display}

We fit the interaction model with:

 snugshade
 Highlighting
mod.F [=]{style="color: 0.56,0.35,0.01"} [aov]{style="color: 0.13,0.29,0.53"}(y [**\~**]{style="color: 0.81,0.36,0.00"} A[**+**]{style="color: 0.81,0.36,0.00"}B[**+**]{style="color: 0.81,0.36,0.00"}C[**+**]{style="color: 0.81,0.36,0.00"}A[**:**]{style="color: 0.81,0.36,0.00"}B)

We define the estimated means for the models with:

 snugshade
 Highlighting
fits.F [=]{style="color: 0.56,0.35,0.01"} [predict]{style="color: 0.13,0.29,0.53"}(mod.F)

The interaction plots for the interaction model where the left and right plots are respectively for factor [\\(C\\)]{.math .inline} at levels [\\(1\\)]{.math .inline} and [\\(2\\)]{.math .inline}.

 snugshade
 Highlighting
[par]{style="color: 0.13,0.29,0.53"}([mfrow=]{style="color: 0.13,0.29,0.53"}[c]{style="color: 0.13,0.29,0.53"}([1]{style="color: 0.00,0.00,0.81"},[2]{style="color: 0.00,0.00,0.81"})) [for]{style="color: 0.13,0.29,0.53"} (i [in]{style="color: 0.13,0.29,0.53"} [1]{style="color: 0.00,0.00,0.81"}[**:**]{style="color: 0.81,0.36,0.00"}[nlevels]{style="color: 0.13,0.29,0.53"}(C)) { [**interaction.plot**]{style="color: 0.13,0.29,0.53"}(A[C[**==**]{style="color: 0.81,0.36,0.00"}[levels]{style="color: 0.13,0.29,0.53"}(C)[i]],B[C[**==**]{style="color: 0.81,0.36,0.00"}[levels]{style="color: 0.13,0.29,0.53"}(C)[i]], fits.F[C[**==**]{style="color: 0.81,0.36,0.00"}[levels]{style="color: 0.13,0.29,0.53"}(C)[i]], [xlab=]{style="color: 0.13,0.29,0.53"}[\"A\"]{style="color: 0.31,0.60,0.02"}, [ylab=]{style="color: 0.13,0.29,0.53"}[\"mean response\"]{style="color: 0.31,0.60,0.02"}, [trace.label=]{style="color: 0.13,0.29,0.53"}[\"B\"]{style="color: 0.31,0.60,0.02"}) }

### Decision

The interaction model fits show only a slight difference difference from the additive model. As a general rule, we prefer simpler models to complex models, and so we decide to leave out the interaction term.

## (d)

 snugshade
 Highlighting
[par]{style="color: 0.13,0.29,0.53"}([mfrow=]{style="color: 0.13,0.29,0.53"}[c]{style="color: 0.13,0.29,0.53"}([1]{style="color: 0.00,0.00,0.81"},[3]{style="color: 0.00,0.00,0.81"})) [plot]{style="color: 0.13,0.29,0.53"}(fits.R [**\~**]{style="color: 0.81,0.36,0.00"} A) [plot]{style="color: 0.13,0.29,0.53"}(fits.R [**\~**]{style="color: 0.81,0.36,0.00"} B) [plot]{style="color: 0.13,0.29,0.53"}(fits.R [**\~**]{style="color: 0.81,0.36,0.00"} C)

We see that each factor has a positive effect on fill height. The factor with the biggest marginal effect on fill height is the percent of carbonation (factor [\\(A\\)]{.math .inline}).

# Problem 2

An engineer is interested in the effects of cutting speed, tool geometry, and cutting angle on the life (in hours) of a machine tool. Two levels of each factor are set, and [\\(n=3\\)]{.math .inline} runs of a [\\(2\^3\\)]{.math .inline} design are completed. The data is available on Blackboard as an Excel File.

## (a)

 snugshade

    ##             Df Sum Sq Mean Sq F value   Pr(>F)    
    ## A            1    0.7     0.7   0.022 0.883680    
    ## B            1  770.7   770.7  25.547 0.000117 ***
    ## C            1  280.2   280.2   9.287 0.007679 ** 
    ## A:B          1   16.7    16.7   0.552 0.468078    
    ## A:C          1  468.2   468.2  15.519 0.001172 ** 
    ## B:C          1   48.2    48.2   1.597 0.224475    
    ## A:B:C        1   28.2    28.2   0.934 0.348282    
    ## Residuals   16  482.7    30.2                     
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Factors [\\(B\\)]{.math .inline} and [\\(C\\)]{.math .inline} are important effects and the the interaction between [\\(A\\)]{.math .inline} and [\\(C\\)]{.math .inline} is also important. Thus, [\\(A\\)]{.math .inline}, [\\(B\\)]{.math .inline}, [\\(C\\)]{.math .inline}, and [\\(A:C\\)]{.math .inline} should be included in the model (we include [\\(A\\)]{.math .inline} because of the importance of [\\(A:C\\)]{.math .inline}).

  effects                      [\\(F\^*\\)]{.math .inline}    [\\(p\\)]{.math .inline}-value
  ---------------------------- ------------------------------- --------------------------------
  [\\(A\\)]{.math .inline}     [\\(.022\\)]{.math .inline}     [\\(.884\\)]{.math .inline}
  [\\(B\\)]{.math .inline}     [\\(25.547\\)]{.math .inline}   [\\(.000\\)]{.math .inline}
  [\\(C\\)]{.math .inline}     [\\(9.287\\)]{.math .inline}    [\\(.008\\)]{.math .inline}
  [\\(A:C\\)]{.math .inline}   [\\(15.519\\)]{.math .inline}   [\\(.001\\)]{.math .inline}

## (b)

 snugshade
 Highlighting
reduced.mod [=]{style="color: 0.56,0.35,0.01"} [aov]{style="color: 0.13,0.29,0.53"}(y [**\~**]{style="color: 0.81,0.36,0.00"} A[**+**]{style="color: 0.81,0.36,0.00"}B[**+**]{style="color: 0.81,0.36,0.00"}C[**+**]{style="color: 0.81,0.36,0.00"}A[**:**]{style="color: 0.81,0.36,0.00"}C) [summary]{style="color: 0.13,0.29,0.53"}(reduced.mod)

    ##             Df Sum Sq Mean Sq F value   Pr(>F)    
    ## A            1    0.7     0.7   0.022 0.883641    
    ## B            1  770.7   770.7  25.436 7.22e-05 ***
    ## C            1  280.2   280.2   9.247 0.006724 ** 
    ## A:C          1  468.2   468.2  15.452 0.000897 ***
    ## Residuals   19  575.7    30.3                     
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

### (i)

 snugshade
 Highlighting
[*\# define the estimated means for the reduced model for plotting (randomness has*]{style="color: 0.56,0.35,0.01"} [*\# been smoothed)*]{style="color: 0.56,0.35,0.01"} fits.r [=]{style="color: 0.56,0.35,0.01"} [predict]{style="color: 0.13,0.29,0.53"}(reduced.mod) [**interaction.plot**]{style="color: 0.13,0.29,0.53"}(A,C,fits.r,[ylab=]{style="color: 0.13,0.29,0.53"}[\"y\"]{style="color: 0.31,0.60,0.02"})

#### Interpretation

The experiment finds that when cutting speed (factor [\\(A\\)]{.math .inline}) is low, cutting angle has a positive effect on the life of a machine tool (response).

### (ii)

 snugshade
 Highlighting
[plot]{style="color: 0.13,0.29,0.53"}(fits.r [**\~**]{style="color: 0.81,0.36,0.00"} B)

#### Interpetation

Tool geometry (factor [\\(B\\)]{.math .inline}) has a positive effect on the life of a machine tool.

### (iii)

 snugshade
 Highlighting
A.C [=]{style="color: 0.56,0.35,0.01"} [interaction]{style="color: 0.13,0.29,0.53"}(A,C) [**interaction.plot**]{style="color: 0.13,0.29,0.53"}(B,A.C, fits.r)

#### Maximum setting

In this characterization experiment, we find that the best combination of factor levels is given by a low cutting speed ([\\(A\^-\\)]{.math .inline}), a high tool geometry ([\\(B\^+\\)]{.math .inline}), and a high cutting angle ([\\(C\^+\\)]{.math .inline}).

#### Explanation

First, we observe that [\\(A\^-\\)]{.math .inline} and [\\(C\^+\\)]{.math .inline} has the best interaction effect (its corresponding line is above all of the others). Second, we see that [\\(B\\)]{.math .inline} has a positive effect, i.e., as we go from [\\(B\^-\\)]{.math .inline} to [\\(B\^+\\)]{.math .inline}, the response increases, and thus [\\(B\^+\\)]{.math .inline} is better. Taking these two facts together, we see that the best combination in this experiment is [\\((A\^-,B\^+,C\^+)\\)]{.math .inline}.

We may also just look at the highest point on the graph and see that [\\((A\^-,B\^+,C\^+)\\)]{.math .inline} has the highest mean response. However, the interaction plot reveals more, particularly if in follow-up experiments where we use what we learned in this experiment to narrow down our search for an optimal combination (where optimality may be with respect to, say, mean response or minimal variability in the response).

# Appendix

## Problem 1: additional analysis of the additive model

The model parameter estimates are given by:

 snugshade
 Highlighting
[**dummy.coef**]{style="color: 0.13,0.29,0.53"}(mod.R)

    ## Full coefficients are 
    ##                                             
    ## (Intercept):         3.125                  
    ## A:                      10         12     14
    ##                     -3.625     -0.625  4.250
    ## B:                      25         30       
    ##                     -1.375      1.375       
    ## C:                     200        250       
    ##                 -0.9583333  0.9583333

Thus, the estimated mean response [\\(\\hat{Y}\_{i j k}\^{(R)}\\)]{.math .inline} is given by [\\[\\begin{aligned} \\hat{Y}\_{i j k}\^{(R)} = 3.125 - &I(i=1) 3.625 - I(i=2) 6.25 + I(i=3) 4.250\\\\ - &I(j=1) 1.375 + I(j=2) 1.375\\\\ - &I(k=1) 9.58\\bar{3} + I(k=2) 9.58\\bar{3}. \\end{aligned}\\]]{.math .display}

In R code, this may be brute-force implemented as:

 snugshade
 Highlighting
yhat.R [=]{style="color: 0.56,0.35,0.01"} [function]{style="color: 0.13,0.29,0.53"}(i,j,k) { y [=]{style="color: 0.56,0.35,0.01"} [3.125]{style="color: 0.00,0.00,0.81"} [if]{style="color: 0.13,0.29,0.53"} (i [**==**]{style="color: 0.81,0.36,0.00"} [1]{style="color: 0.00,0.00,0.81"}) y [=]{style="color: 0.56,0.35,0.01"} y [**-**]{style="color: 0.81,0.36,0.00"} [3.625]{style="color: 0.00,0.00,0.81"}; [if]{style="color: 0.13,0.29,0.53"} (i [**==**]{style="color: 0.81,0.36,0.00"} [2]{style="color: 0.00,0.00,0.81"}) y [=]{style="color: 0.56,0.35,0.01"} y [**-**]{style="color: 0.81,0.36,0.00"} .[625]{style="color: 0.00,0.00,0.81"}; [if]{style="color: 0.13,0.29,0.53"} (i [**==**]{style="color: 0.81,0.36,0.00"} [3]{style="color: 0.00,0.00,0.81"}) y [=]{style="color: 0.56,0.35,0.01"} y [**+**]{style="color: 0.81,0.36,0.00"} [4.25]{style="color: 0.00,0.00,0.81"} [if]{style="color: 0.13,0.29,0.53"} (j [**==**]{style="color: 0.81,0.36,0.00"} [1]{style="color: 0.00,0.00,0.81"}) y [=]{style="color: 0.56,0.35,0.01"} y [**-**]{style="color: 0.81,0.36,0.00"} [1.375]{style="color: 0.00,0.00,0.81"}; [if]{style="color: 0.13,0.29,0.53"} (j [**==**]{style="color: 0.81,0.36,0.00"} [2]{style="color: 0.00,0.00,0.81"}) y [=]{style="color: 0.56,0.35,0.01"} y [**+**]{style="color: 0.81,0.36,0.00"} [1.375]{style="color: 0.00,0.00,0.81"} [if]{style="color: 0.13,0.29,0.53"} (k [**==**]{style="color: 0.81,0.36,0.00"} [1]{style="color: 0.00,0.00,0.81"}) y [=]{style="color: 0.56,0.35,0.01"} y [**-**]{style="color: 0.81,0.36,0.00"} .[95833333]{style="color: 0.00,0.00,0.81"}; [if]{style="color: 0.13,0.29,0.53"} (k [**==**]{style="color: 0.81,0.36,0.00"} [2]{style="color: 0.00,0.00,0.81"}) y [=]{style="color: 0.56,0.35,0.01"} y [**+**]{style="color: 0.81,0.36,0.00"} .[95833333]{style="color: 0.00,0.00,0.81"} y }

We print out all of the estimates of the mean response with:

 snugshade
 Highlighting
[for]{style="color: 0.13,0.29,0.53"} (i [in]{style="color: 0.13,0.29,0.53"} [1]{style="color: 0.00,0.00,0.81"}[**:**]{style="color: 0.81,0.36,0.00"}[3]{style="color: 0.00,0.00,0.81"}) [for]{style="color: 0.13,0.29,0.53"} (j [in]{style="color: 0.13,0.29,0.53"} [1]{style="color: 0.00,0.00,0.81"}[**:**]{style="color: 0.81,0.36,0.00"}[2]{style="color: 0.00,0.00,0.81"}) [for]{style="color: 0.13,0.29,0.53"} (k [in]{style="color: 0.13,0.29,0.53"} [1]{style="color: 0.00,0.00,0.81"}[**:**]{style="color: 0.81,0.36,0.00"}[2]{style="color: 0.00,0.00,0.81"}) [cat]{style="color: 0.13,0.29,0.53"}([\"Y(\"]{style="color: 0.31,0.60,0.02"},[c]{style="color: 0.13,0.29,0.53"}(i,j,k),[\") = \"]{style="color: 0.31,0.60,0.02"},[**yhat.R**]{style="color: 0.13,0.29,0.53"}(i,j,k),[\"]{style="color: 0.31,0.60,0.02"}[**\\n**]{style="color: 0.81,0.36,0.00"}[\"]{style="color: 0.31,0.60,0.02"})

    ## Y( 1 1 1 ) =  -2.833333 
    ## Y( 1 1 2 ) =  -0.9166667 
    ## Y( 1 2 1 ) =  -0.08333333 
    ## Y( 1 2 2 ) =  1.833333 
    ## Y( 2 1 1 ) =  0.1666667 
    ## Y( 2 1 2 ) =  2.083333 
    ## Y( 2 2 1 ) =  2.916667 
    ## Y( 2 2 2 ) =  4.833333 
    ## Y( 3 1 1 ) =  5.041667 
    ## Y( 3 1 2 ) =  6.958333 
    ## Y( 3 2 1 ) =  7.791667 
    ## Y( 3 2 2 ) =  9.708333

## Problem 1: plots of interactions that were deemed insignificant

The data showed no statistically significant interaction effects between factors [\\(A\\)]{.math .inline} and [\\(B\\)]{.math .inline} and between factors [\\(B\\)]{.math .inline} and [\\(C\\)]{.math .inline}. Thus, their interaction plots are, as expected, parallel:

 snugshade
 Highlighting
[par]{style="color: 0.13,0.29,0.53"}([mfrow=]{style="color: 0.13,0.29,0.53"}[c]{style="color: 0.13,0.29,0.53"}([1]{style="color: 0.00,0.00,0.81"},[2]{style="color: 0.00,0.00,0.81"})) [**interaction.plot**]{style="color: 0.13,0.29,0.53"}(A,B,fits.r,[ylab=]{style="color: 0.13,0.29,0.53"}[\"y\"]{style="color: 0.31,0.60,0.02"}) [**interaction.plot**]{style="color: 0.13,0.29,0.53"}(B,C,fits.r,[ylab=]{style="color: 0.13,0.29,0.53"}[\"y\"]{style="color: 0.31,0.60,0.02"})
