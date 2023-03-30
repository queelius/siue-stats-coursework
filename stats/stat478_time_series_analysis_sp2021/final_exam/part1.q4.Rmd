---
title: 'Time Series Analysis - STAT 478 - Final Exam - Part 1 Q4'
author: "Alex Towell (atowell@siue.edu)"
output:
  pdf_document:
    df_print: kable
    #latex_engine: pdflatex
    latex_engine: xelatex
header-includes:
 - \usepackage{alex}
 - \usepackage{xfrac}
---
# Part 1: Problem 4
Consider the following models where $\{e_t\}$ is a $0$ mean white noise process
with variance $σ^2$.
\begin{enumerate}
\item [i] $Y_t = 1.9 Y_{t−1} − 0.9 Y_{t−2} + e_t − 0.5e_{t−1}$
\item [ii] $Y_t = 0.5 Y_{t−1} + e_t − 0.2e_{t−1} − 0.15e_{t−2}$
\end{enumerate}

## Part (a)
\fbox{Write each model above using backshift notation.}

\begin{enumerate}
\item [(i)] $(1 - 1.9 \backshift + 0.9 \backshift^2) Y_t = (1 - 0.5 \backshift) e_t$.

Working on both sides of the equation simultaneously, we use the following
sequence of transformations to arrive at a canonical form.
\begin{align*}
  (1 - 1.9 \backshift + 0.9 \backshift^2) Y_t &= (1 - \sfrac{1}{2} \backshift) e_t\\
  %%%%%%%%%%%\sfrac{10}{10}(1 - 1.9 \backshift + 0.9 \backshift^2) Y_t &= (1 - \sfrac{1}{2} \backshift) e_t\\
  \sfrac{1}{10}(10 - 19 \backshift + 9 \backshift^2) Y_t &= (1 - \sfrac{1}{2} \backshift) e_t\\
  \sfrac{1}{10}(1-\backshift)(10-9\backshift) Y_t  &=  (1 - \sfrac{1}{2} \backshift) e_t\\
  \sfrac{1}{100}(1-\backshift)(1-\sfrac{9}{10}\backshift) Y_t  &=  (1 - \sfrac{1}{2} \backshift) e_t\\
  (1-\backshift)(1-\sfrac{9}{10}\backshift) Y_t  &=  (1 - \sfrac{1}{2} \backshift) 100 e_t
\end{align*}
We let $\eta_t = 10^2 e_t$, which is white noise with a mean $0$ and variance
$10^4 \sigma^2$, thus
$$
  (1-\backshift)(1-\sfrac{9}{10}\backshift) Y_t = (1 - \sfrac{1}{2} \backshift) \eta_t.
$$

\item [(ii)] $(1 - 0.5 \backshift) Y_t = (1 - 0.2 \backshift - 0.15 \backshift^2) e_t$.
Working on both sides of the equation simultaneously, we use the following
sequence of transformations to arrive at a canonical form.
\begin{align*}
  (1 - 0.5 \backshift) Y_t          &= (1 - 0.2 \backshift - 0.15 \backshift^2) e_t\\
  (1 - \sfrac{1}{2} \backshift) Y_t &= (1 - \sfrac{1}{5} \backshift - \sfrac{3}{20} \backshift^2) e_t\\
  (1 - \sfrac{1}{2} \backshift) Y_t &= (1 - \sfrac{1}{2}\backshift)(1 + \sfrac{3}{10}) e_t\\
                                Y_t &= (1 + \sfrac{3}{10}) e_t
\end{align*}
\end{enumerate}

## Part (b)
\fbox{\begin{minipage}{.9\textwidth}
Characterize these models as models in the $\arima(p,d,q)$ family, that is,
identify $p$, $d$ and $q$.
\end{minipage}}

\begin{enumerate}
\item[(i)] By the form, $\{Y_t\}$ is an $\arima(1,1,1)$ process, or equivalently,
$\{\nabla Y_t\}$ is an $\arma(1,1)$ process.
\item[(ii)] By the form, $\{Y_t\}$ is an $\arima(0,0,1)$ process, or equivalently, $\ma(1)$ process.
\end{enumerate}

## Part (c)
\fbox{Determine if each model corresponds to a stationary process or not.}

\begin{enumerate}
\item[(i)] $\{Y_t\}$ is an $\arima(1,1,1)$ process, which means that its characteristic function has a unit root.
Recall that $\arima(1,1,1)$ denotes a 
$\{Y_t\}$ is therefore a non-stationary process.\footnote{$\nabla \{Y_t\}$ is a stationary $\arma(1,1)$ process since it does not have a unit root.}
\item[(ii)] $\{Y_t\}$ is an $\ma(1)$ process, which are necessarily stationary.
\end{enumerate}
