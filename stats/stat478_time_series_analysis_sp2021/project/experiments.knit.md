---
title: 'Time Series Analysis - STAT 478 - Project'
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
\newcommand{\var}{\operatorname{Var}}
\newcommand{\expect}{\operatorname{E}}
\newcommand{\corr}{\operatorname{Corr}}
\newcommand{\cov}{\operatorname{Cov}}
\newcommand{\ssr}{\operatorname{SSR}}
\newcommand{\se}{\operatorname{SE}}
\newcommand{\mat}[1]{\bm{#1}}
\newcommand{\eval}[2]{\left. #1 \right\vert_{#2}}
\newcommand{\argmin}{\operatorname{arg\,min}}

# Confidentiality
We load the confidentiality measure as a time series $\{C_t\}$.
























