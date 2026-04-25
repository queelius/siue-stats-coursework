 snugshade

An experiment is designed to investigate whether the time to drill holes in rock holes using wet or dry drilling. A completely randomized design (CRD) is used. Each method is replicated on 12 rocks. The drilling times (in 1 / 100 minutes) are observed to be

  ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
  dry     727   965   904   987   847   918   814   750   804   989   902   939
  wet     607   549   762   665   588   798   704   772   780   599   603   699
  ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

# Q1

The hypothesis of interest is whether drilling time is effected by the choice of wet or dry drilling. We may formulate this as a hypothesis test of the form

[\\[\\begin{aligned} H_0 &: \\mu_1 = \\mu_2\\\\ H_A &: \\mu_1 \\neq \\mu_2\\,, \\end{aligned}\\]]{.math .display} where [\\(\\mu_1\\)]{.math .inline} and [\\(\\mu_2\\)]{.math .inline} are respectively the expected drilling time for dry and wet drilling.

If [\\(H_0\\)]{.math .inline} is true, the drilling method has *no* effect on drilling time. If [\\(H_A\\)]{.math .inline} is true, the choice does have an effect on drilling time.

# Q2

Two advantages of the completely randomized design (CRD) are:

1.  It is simple to implement and analyze.

2.  It accounts for experimental unit variance, namely by controlling for the type I error,

    [\\[\\alpha = \\Pr(\\text{decide} \\, H_A \| H_0 \\, \\text{true}),\\]]{.math .display}

    where [\\(\\alpha\\)]{.math .inline} is the probability of a type I error. It may also be thought of as the type I *error rate*, or *false positive rate*.

# Q3

Two disadvantages of the completely randomized design (CRD) are:

1.  It does not account for type II error, [\\[\\beta = \\Pr(\\text{decide} \\, H_0 \| H_A \\, \\text{true}).\\]]{.math .display} where [\\(\\beta\\)]{.math .inline} is the probability of a type II error.

    > **Additional remarks**: Since we may denote a type I error a false positive, it may be appropriate to denote a type II error a false negative, which implies the convention [\\(H_0 \\equiv \\rm{negative}\\)]{.math .inline} and [\\(H_A \\equiv \\rm{positive}\\)]{.math .inline}. Thus, [\\(\\beta\\)]{.math .inline} may be thought of as the false negative rate.

    > Consider the unrelated *Bloom filter*, which is a probabilistic data structure that models sets in which membership queries have a controllable false positive rate [\\(\\epsilon\\)]{.math .inline} and a false negative rate [\\(0\\)]{.math .inline}. If we take the complement of an object representing such a Bloom filter, then membership queries on its complement have a false positive rate [\\(0\\)]{.math .inline} and a false negative rate [\\(\\epsilon\\)]{.math .inline}.

2.  It does not adjust for differences in experimental units nor differences in any other factors.

# Q4

 snugshade
 Highlighting
time.mean [<-]{style="color: 0.56,0.35,0.01"} [round]{style="color: 0.13,0.29,0.53"}([c]{style="color: 0.13,0.29,0.53"}([mean]{style="color: 0.13,0.29,0.53"}(h1.time.dry), [mean]{style="color: 0.13,0.29,0.53"}(h1.time.wet)),[digits=]{style="color: 0.13,0.29,0.53"}[3]{style="color: 0.00,0.00,0.81"}) time.var [<-]{style="color: 0.56,0.35,0.01"} [round]{style="color: 0.13,0.29,0.53"}([c]{style="color: 0.13,0.29,0.53"}([var]{style="color: 0.13,0.29,0.53"}(h1.time.dry), [var]{style="color: 0.13,0.29,0.53"}(h1.time.wet)),[digits=]{style="color: 0.13,0.29,0.53"}[3]{style="color: 0.00,0.00,0.81"}) time.sd [<-]{style="color: 0.56,0.35,0.01"} [round]{style="color: 0.13,0.29,0.53"}([sqrt]{style="color: 0.13,0.29,0.53"}(time.var),[digits=]{style="color: 0.13,0.29,0.53"}[3]{style="color: 0.00,0.00,0.81"}) n [<-]{style="color: 0.56,0.35,0.01"} [c]{style="color: 0.13,0.29,0.53"}([length]{style="color: 0.13,0.29,0.53"}(h1.time.dry), [length]{style="color: 0.13,0.29,0.53"}(h1.time.wet)) time.sd.pooled [<-]{style="color: 0.56,0.35,0.01"} [round]{style="color: 0.13,0.29,0.53"}([sqrt]{style="color: 0.13,0.29,0.53"}(((n[[1]{style="color: 0.00,0.00,0.81"}] [**-**]{style="color: 0.81,0.36,0.00"} [1]{style="color: 0.00,0.00,0.81"}) [*****]{style="color: 0.81,0.36,0.00"} time.var[[1]{style="color: 0.00,0.00,0.81"}] [**+**]{style="color: 0.81,0.36,0.00"} (n[[2]{style="color: 0.00,0.00,0.81"}] [**-**]{style="color: 0.81,0.36,0.00"} [1]{style="color: 0.00,0.00,0.81"}) [*****]{style="color: 0.81,0.36,0.00"} time.var[[2]{style="color: 0.00,0.00,0.81"}]) [**/**]{style="color: 0.81,0.36,0.00"} ([sum]{style="color: 0.13,0.29,0.53"}(n)[**-**]{style="color: 0.81,0.36,0.00"}[2]{style="color: 0.00,0.00,0.81"})), [digits=]{style="color: 0.13,0.29,0.53"}[3]{style="color: 0.00,0.00,0.81"})

[c]{style="color: 0.13,0.29,0.53"}([\"y.bar.1\"]{style="color: 0.31,0.60,0.02"} [=]{style="color: 0.56,0.35,0.01"} time.mean[[1]{style="color: 0.00,0.00,0.81"}], [\"y.bar.2\"]{style="color: 0.31,0.60,0.02"} [=]{style="color: 0.56,0.35,0.01"} time.mean[[2]{style="color: 0.00,0.00,0.81"}], [\"s.1\"]{style="color: 0.31,0.60,0.02"} [=]{style="color: 0.56,0.35,0.01"} time.sd[[1]{style="color: 0.00,0.00,0.81"}], [\"s.2\"]{style="color: 0.31,0.60,0.02"} [=]{style="color: 0.56,0.35,0.01"} time.sd[[2]{style="color: 0.00,0.00,0.81"}], [\"s.p\"]{style="color: 0.31,0.60,0.02"} [=]{style="color: 0.56,0.35,0.01"} time.sd.pooled)

    ## y.bar.1 y.bar.2     s.1     s.2     s.p 
    ## 878.833 677.167  89.470  87.189  88.337

We see that the sample means are [\\[(\\bar{y}\_1,\\bar{y}\_2) = (878.833, 677.167),\\]]{.math .display} the standard deviations are [\\[(s_1,s_2) = (89.47, 87.189),\\]]{.math .display} and the pooled standard deviation is [\\[s_p = 88.337.\\]]{.math .display}

# Q5

The test statistic is defined as [\\[t_0 = \\frac{\\bar{y}\_1-\\bar{y}\_2}{s_p \\sqrt{\\frac{1}{n_1}+\\frac{1}{n_2}}}.\\]]{.math .display} which is a drawn from a [\\(t\\)]{.math .inline}-student distribution with [\\(n_1+n_2-2\\)]{.math .inline} degrees of freedom under the null model (reference distribution).

> Under the null model, [\\(\\bar{y}\_1\\)]{.math .inline} and [\\(\\bar{y}\_2\\)]{.math .inline} are the means of two samples respectively of size [\\(n_1\\)]{.math .inline} and [\\(n_2\\)]{.math .inline} whose elements are drawn from the same normal distribution.

Denote this reference distribution by [\\(T\\)]{.math .inline}. Under the null model, [\\(t_0\\)]{.math .inline} is a realization of [\\(T\\)]{.math .inline}. Our general approach is to compute the test statistic [\\(t_0\\)]{.math .inline} for the given samples and say it is compatible with the null model if it obtains a value that is not too extreme under [\\(T\\)]{.math .inline}, e.g., a [\\(p\\)]{.math .inline}-value that is less than some controllable parameter [\\(\\alpha\\)]{.math .inline}.

The critical point (the minimum value that is considered to be too extreme) is given by solving for [\\(t\^*\\)]{.math .inline} in [\\[\\Pr\\{-\|t\^*\| \< T \< \|t\^*\|\\} = \\alpha,\\]]{.math .display} which has the solution [\\(t\^* = t\_{\\rm{df}=n_1+n_2-2}(\\alpha/2)\\)]{.math .inline}, and [\\[\\begin{aligned} \\text{\$p$-value} &= \\Pr\\{T \\notin [-\|t_0\|,\|t_0\|]\\}\\\\ &= 2 \\Pr\\{T \> \|t_0\|\\}\\\\ &= 2(1-F_T(\|t_0\|)), \\end{aligned}\\]]{.math .display} where [\\(F_T\\)]{.math .inline} is the cdf of [\\(T\\)]{.math .inline}.

We compute these results in R with:

 snugshade
 Highlighting
se [<-]{style="color: 0.56,0.35,0.01"} time.sd.pooled[*****]{style="color: 0.81,0.36,0.00"}[sqrt]{style="color: 0.13,0.29,0.53"}([1]{style="color: 0.00,0.00,0.81"}[**/**]{style="color: 0.81,0.36,0.00"}n[[1]{style="color: 0.00,0.00,0.81"}][**+**]{style="color: 0.81,0.36,0.00"}[1]{style="color: 0.00,0.00,0.81"}[**/**]{style="color: 0.81,0.36,0.00"}n[[2]{style="color: 0.00,0.00,0.81"}]) t[.0]{style="color: 0.00,0.00,0.81"} [<-]{style="color: 0.56,0.35,0.01"} [round]{style="color: 0.13,0.29,0.53"}((time.mean[[1]{style="color: 0.00,0.00,0.81"}][**-**]{style="color: 0.81,0.36,0.00"}time.mean[[2]{style="color: 0.00,0.00,0.81"}])[**/**]{style="color: 0.81,0.36,0.00"}se,[digits=]{style="color: 0.13,0.29,0.53"}[3]{style="color: 0.00,0.00,0.81"}) alpha [<-]{style="color: 0.56,0.35,0.01"} [0.05]{style="color: 0.00,0.00,0.81"} t.star [=]{style="color: 0.56,0.35,0.01"} [round]{style="color: 0.13,0.29,0.53"}([qt]{style="color: 0.13,0.29,0.53"}(alpha[**/**]{style="color: 0.81,0.36,0.00"}[2]{style="color: 0.00,0.00,0.81"},[lower.tail=]{style="color: 0.13,0.29,0.53"}F, [df=]{style="color: 0.13,0.29,0.53"}n[[1]{style="color: 0.00,0.00,0.81"}][**+**]{style="color: 0.81,0.36,0.00"}n[[2]{style="color: 0.00,0.00,0.81"}][**-**]{style="color: 0.81,0.36,0.00"}[2]{style="color: 0.00,0.00,0.81"}),[digits=]{style="color: 0.13,0.29,0.53"}[3]{style="color: 0.00,0.00,0.81"}) p.value [=]{style="color: 0.56,0.35,0.01"} [2]{style="color: 0.00,0.00,0.81"}[*****]{style="color: 0.81,0.36,0.00"}[pt]{style="color: 0.13,0.29,0.53"}([abs]{style="color: 0.13,0.29,0.53"}(t[.0]{style="color: 0.00,0.00,0.81"}),[df=]{style="color: 0.13,0.29,0.53"}n[[1]{style="color: 0.00,0.00,0.81"}][**+**]{style="color: 0.81,0.36,0.00"}n[[2]{style="color: 0.00,0.00,0.81"}][**-**]{style="color: 0.81,0.36,0.00"}[2]{style="color: 0.00,0.00,0.81"},[lower.tail=]{style="color: 0.13,0.29,0.53"}F)

[c]{style="color: 0.13,0.29,0.53"}([\"t.0\"]{style="color: 0.31,0.60,0.02"}[=]{style="color: 0.56,0.35,0.01"}t[.0]{style="color: 0.00,0.00,0.81"},[\"t.*\"]{style="color: 0.31,0.60,0.02"}[=]{style="color: 0.56,0.35,0.01"}t.star,[\"p.value\"]{style="color: 0.31,0.60,0.02"}[=]{style="color: 0.56,0.35,0.01"}p.value)

    ##          t.0          t.*      p.value 
    ## 5.592000e+00 2.074000e+00 1.272907e-05

We see that [\\(t_0 = 5.592\\)]{.math .inline}, the critical point [\\(t\^*\\)]{.math .inline} for [\\(\\alpha = 0.05\\)]{.math .inline} is [\\(2.074\\)]{.math .inline}, and the [\\(p\\)]{.math .inline}-value is less than [\\(.001\\)]{.math .inline}.

# Q6

The experiment finds that the wet drilling method leads to reduced drilling times compared to the dry drilling method.

# Q7

 snugshade

# Q8

No, not all dry drilling times exceed all wet drilling times.

However, the boxplot does show that the spread of the drilling times area approximately the same between the two methods (providing justification for assuming the two samples have the same variance) and the mean drilling times are significantly different. As a result, most of the time, the wet drilling time is going to be less than the dry drilling time.

For instance, we see that the mean wet drilling time is less than the best dry drilling time and we also see that the [\\(25\\)]{.math .inline}-th percentile of the dry method's times is a bit larger than the wet method's longest drilling time. Most tellingly, we see that around [\\(67\\%\\)]{.math .inline} of the time, the wet drilling time is less than the smallest dry drilling time.
