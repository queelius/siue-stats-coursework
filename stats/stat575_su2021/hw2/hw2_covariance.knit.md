---
title: 'Computational Statistics - STAT 575 - HW #2 - Covariance Estimation'
author: "Alex Towell (atowell@siue.edu)"
output:
  pdf_document:
    df_print: kable
    latex_engine: xelatex
header-includes:
 - \usepackage{amsmath}
 - \usepackage{mathtools}
 - \usepackage{amsthm}
 # - \usepackage{amsbsy}
 - \usepackage{booktabs}
 - \usepackage{bm}
 - \usepackage{xcolor}
 - \usepackage{fbox}
 - \usepackage{amsmath}
 - \usepackage{minted}
---

\newcommand{\var}{\operatorname{Var}}
\newcommand{\expect}{\operatorname{E}}
\newcommand{\cov}{\operatorname{Cov}}
\newcommand{\se}{\operatorname{SE}}
\newcommand{\mat}[1]{\mathbf{#1}} 
\newcommand{\eval}[2]{\left. #1 \right\vert_{#2}}
\newcommand{\poi}{\operatorname{POI}}
\newcommand{\argmax}{\operatorname{arg\,max}}

# Covariance estimation: bootstrap vs observed fisher information

We use the functions defined by the package \emph{prob.4.2.comp.stats}.










