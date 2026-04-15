---
title: 'Time Series Analysis - STAT 478 - Project'
author: "Alexander Towell (atowell@siue.edu)"
abstract: "We derive a confidentiality measure against an adversary deploying a known-plaintext attack on the search agents Encrypted searches. We perform a time series analysis on a theoretical adversary in order to derive an estimator of the forecast distribution on the confidentiality measure, which may be used to inform policies such as when and how frequently a password change may be called for to maintain a minimum level of confidentiality."
keywords: "time series analysis, known-plaintext attack, encrypted search, confidentiality measure, estimation"
date: "October 05, 2025"
geometry: margin=1in
fontfamily: mathpazo
fontsize: 11pt
output:
  pdf_document:
    df_print: kable
    toc: true
    toc_depth: 3
    #latex_engine: pdflatex
    latex_engine: xelatex
    keep_tex: yes
    number_sections: yes
#bibliography: "refs.bib"
header-includes:
 - \usepackage{alex}
---

# Introduction

In \emph{cloud computing}, it is tempting to store confidential data on
(untrusted) cloud storage providers.
However, a system administrator may be able to compromise the confidentiality of
the data, threatening to prevent further adoption of cloud computing and
electronic information retrieval in general.

The primary challenge is a trade-off problem between confidentiality and
usability of the data stored on untrusted systems.
\emph{Encrypted Search} attempts to resolve this trade-off problem.
\begin{definition}
\emph{Encrypted Search} allows authorized search agents to investigate presence
of specific search terms in a confidential target data set, such as a database
of encrypted documents, while the contents, especially the meaning of the target
data set and search terms, are hidden from any unauthorized personnel, including
the system administrators of a cloud server.
\end{definition}
Essentially, \emph{Encrypted Search} enables \emph{oblivous search}.
For instance, a user may search a confidential database stored on an untrusted
remote system without other parties being able to determine the information
need of the user searched (and on more sophisticated systems, they are also
unable to determine which documents were relevant to the information need).

We denote any untrusted party that has full access to the untrusted remote
system (where the confidential data is stored) the adversary.\footnote{A system
administrator being a typical example.}

Despite the potential of \emph{Encrypted Search}, \emph{perfect} confidentiality
is not theoretically possible. There are many ways confidentiality may be compromised.
In this paper, we consider an adversary whose primary objective is to comprehend
the confidential information needs of the search agents by analyzing their
history of \emph{encrypted} queries.

A simple measure of confidentiality is given by the proportion of queries the
adversary is able to comprehend.
We consider an adversary that employs a known-plaintext attack.
However, since the confidentiality is a function of the history of queries,
different histories will result in different levels of confidentiality over
time.

We apply time series analysis to estimate the forecast distribution of the
confidentiality measure.
The forecast distribution provides the framework to estimate important
security-related questions such as "what will our mean confidentiality six
months from now be?"

We are interested in reasonably medium-term forecasts so that we can plan
accordingly for the future, e.g., determining how frequently
passwords should be reset to try to maintain a base level of confidentiality.
Resetting them too frequently poses an independent set
of problems, both from a security and usability standpoint, but failing to reset
them when the risk of being compromised is too high defeats the central purpose
of Encrypted search.

# Encrypted search model
\label{sec:es_model}
An information retrieval process begins when a \emph{search agent} submits a
\emph{query} to an information system, where a query represents an
\emph{information need}. In response, the information system returns a set of
relevant objects, such as \emph{documents}, that satisfy the information need.

An \emph{Encrypted Search} system may support many different kinds of queries,
but we make the following simplifying assumption.
\begin{assumption}
The query model is a \emph{sequence-of-words}.
\end{assumption}

The \emph{adversary} is given by the following definition.
\begin{definition}
The adversary is an untrusted agent that is able to observe the sequence of
queries submitted by authorized search agent.
\end{definition}

The objective of the \emph{Encrypted Search} system is to prevent the adversary
from being able to comprehend the sequence of queries.
\begin{definition}
A \emph{hidden query} represents a confidential \emph{information need} of an
authorized search agent that is suppose to be incomprehensible to the adversary.
\end{definition}

The primary means by which \emph{Encrypted Search} is enabled is by the use of
cryptographic \emph{trapdoors} as given by the following definition.
\begin{definition}[Trapdoor]
Search agents map \emph{plaintext} search keys to some cryptographic hash,
denoted trapdoors.
\end{definition}
A trapdoor for a \emph{plaintext} search key is necessary to allow an
\emph{untrusted} \emph{Encrypted Search} system to look for the key in a
corresponding confidential data set.

\begin{assumption}
The \emph{Encrypted Search} system uses a simple substitution cipher in which
each search key is mapped to a unique trapdoor signature.
\end{assumption}

The simple substitution cipher is denoted by
\begin{equation}
    \operatorname{h} \colon \set{X} \mapsto \set{Y}\,,
\end{equation}
where $\set{X}$ is the set of \emph{plaintext} search keys and $\set{Y}$
is the set of \emph{trapdoors}.

Since $\operatorname{h}$ is one-to-one, it is possible to \emph{undo} the
substitution cipher by some function denoted by
\begin{equation}
    \operatorname{g} \colon \set{Y} \mapsto \set{X}
\end{equation}
such that
\[
    x = \operatorname{g}(\operatorname{h}(x))
\]
for every $x \in \set{X}$.

In a time series, we have \emph{one} entitty and $T$ measurements of it over
time.
A random time series is a sequence of random variables
$$
  \{Y_1,Y_2,\ldots,Y_T\},
$$
typically denoted by $\{Y_t\}$ where $t$ is the time index, which can continuous
or discrete.
MoreThe time index is more appro

The measurements are $d$ dimensional and may be continuous, discrete, or some
mixture.
Frequently $d=1$, which we denote a univariate time series, and the measurements
are continuous.

We use upper-case to denote random variables and lower-case to denote
realizations, thus $Y_t$ is a random value and $y_t$ is the realization of $Y_t$.

Thus, a realization of the time series $\{Y_t\}$ is given by denoted by
$\{y_t\}$.


<!-- which is a sequence of measures oberved at (approxiamtely) equal points in time. -->


The time series of \emph{plaintext} keyword searches submitted by the search
agents is denoted by $\{x_t\}$.
It is a $d=1$ dimensional time series with a discrete time index and a
discrete response.

The adversary may may directly observe $\{x_t\}$.
Instead, he observes a time series of ciphers.
\begin{definition}
The \emph{cipher} $\{c_t\}$ is a discrete time and discrete
response time series defined as
$$
  c_t = \operatorname{h}(x_t).
$$
\end{definition}

Since the time series of \emph{plaintext} is a priori non-deterministic,
we model it as a random time series $\{X_t\}$ such that
\begin{equation}
    \Pr(X_j = x_j | X_1 = x_1,\ldots,X_{j-1} = x_{j-1}).
\end{equation}
That is to say, our plaintext language model does not incorporate other kinds
of information, such as who the search agent is or what time of day it is.
In the section on future work, we consider extensiosn of the model.

Since $\{c_t\}$ is a function of $\{x_t\}$, we may model the ciphers as a
random time series $\{ C_t \}$ where $C_j = \operatorname{h}(X_j)$.

# Threat model: known-plaintext attack
\label{sec:threat}
The primary source of information is given by the observable time series of
ciphers $\{c_t\}$, which is induced by the unobserved time series of plaintext
$\{x_t\}$.

Other potential sources of information, such as side-channel information, is 
not included in the model we consider in this paper.
See section \ref{sec:future} for some preliminary thoughts on this expanded topic.

In the threat model described in section \ref{sec:threat}, the adversary is interested in estimating $\{x_t\}$.
However, the adversary is only able to observe $\{c_t\}$.
Thus, the adversary's objective is to infer the plaintext from the
ciphers using frequency analysis attacks, in particular a
\emph{known-plaintext} attack.

In a known-plaintext attack, the objective of the adversary is to learn how to
\emph{undo} the substitution cipher $\operatorname{h}$ with $\operatorname{g}$.
\begin{assumption}
The inverse substitition cipher $\operatorname{g}$ is not known to the adversary.
\end{assumption}

A maximum likelihood estimator of $\operatorname{g}$ is given by
$$
    \hat{\operatorname{g}} = \argmax_{\operatorname{g} \in G}
    \Pr(X_1 = \operatorname{g}(c_1)) \prod_{t=2}^{T} \Pr(X_t =
    \operatorname{g}(c_t) | X_{t-1} = \operatorname{g}(c_{t-1}),
            \ldots, X_1 = \operatorname{g}(c_1))
$$
where $G$ is the set of all possible mapping functions from ciphers
$\set{Y}$ to plaintexts $\set{X}$.

If two plaintexts $x,x' \in \set{X}, x \neq x'$, may be exchanged without
changing the probability of $\{x_t\}$, then they are \emph{indistinguishable}
and $\hat{\operatorname{g}}$ is \emph{inconsistent}.
However, the adversary does not need to be perfect for the confidentiality
measure to be compromised.
If some of the plaintexts are inexchangeable, then the adversary may learn
\emph{something} about $\{x_t\}$ by observing $\{c_t\}$.

The greater the uniformity of $\{X_t\}$ the greater the variance of
$\hat{\operatorname{g}}$.
At the limit of maximum uniformity, where every pair of plaintext is exchangeable,
the adversary can learn nothing about $\{x_t\}$ by observing $\{c_t\}$.
Natural languages have a high degree of non-uniformity and so the primary
concern of the adversary is the divergence between the \emph{true} distribution
and the \emph{known-plaintext} distribution.
\begin{assumption}
The adversary knows some approximation of $\{X_t\}$.
\end{assumption}
The \emph{known-plaintext} distribution may be used to solve an approximation
of the MLE $\hat{\operatorname{g}}$.
\begin{definition}
In a \emph{known-plaintext attack}, the adversary substitutes the unknown true
distribution with the known-plaintext distribution and solves the MLE under
this substituted distribution.
\end{definition}

\section{Confidentiality measure}
We are interested in measuring the degree of confidentiality as given by the
following definition.
\begin{definition}
Given a time series $\{c_{t'}\}$, the confidentiality measure is a time series
$\{\pi_t\}$ defined as the fraction of ciphers in $\{c_{t'}\}$ that the adversary
successfully maps to \emph{plaintext} where $t' = N t$.
That is,
\begin{equation}
\label{eq:accuracy}
    \pi_t = \frac{\delta_t}{N t}\,,
\end{equation}
where
\begin{equation}
    \delta_t = \sum_{t'=1}^{N t} [\operatorname{g}(c_{t'}) = \hat{\operatorname{g}}(c_{t'})]\,.
\end{equation}
\end{definition}

Note that $N$ denotes the fact that we take one measurement of the confidentiality
every time a multiple of $N$ ciphers are observed.

The measure $\pi_t$ can be understood as the marginal probability that the
adversary is able to decode an incoming cipher to plaintext at around time $t$.
However, far more revealingly, the adversary may go back through the history of
ciphers and decode proportion $\pi_t$ to plaintext.

If we specify that $\pi^*$ is the minimum confidentiality measure we wish to
maintain, then it is essential that we stop generating $\{c_t\}$ at or before
time $T^*$ where
$$
  T^* = \argmin_{T} \pi_T > \pi^*.
$$
That is, we stop generating $\{c_{t'}\}$ before the amount of information in it
is sufficient for the adversary to decode more than proportion $\pi^*$ of the
data.
We do not need to stop Encrypted search queries at time $T^*$, we only need to
change the cipher, i.e., substitute the mapping function $\operatorname{h}$
that maps plaintexts to ciphers with some other mapping function, which is
typically done by requiring users to change passwords periodically.
This is where \emph{forecasting} $\{\pi_t\}$ plays a central role.

## Forecasting model
As a function of a \emph{random time series} $\{C_{t'}\}$, we may model $\pi_t$
as being generated by the random time series $\{\Pi_t\}$.
If $\pi_{t}$ is not known, i.e., $\Pi_{t}$ has not been observed, then $\Pi_{t}$
is a probability distribution on the measure at time $t$.
If $\pi_{1},\pi_{2},\ldots,\pi_{T}$ is given, then $\Pi_{T+h|T}$
is a \emph{conditional} distribution\footnote{$\Pi_{T+h}$ given $\Pi_1 = \pi_1,\ldots,\Pi_T = \pi_T$.}
known as the $h$-step forecast distribution at time $T$ whose expectation is
denoted by $\pi_{T+h|T}$.

Our primary interest is in \emph{forecasting} an observed time series $\{\pi_t\}$,
e.g., if we observe $\{\pi_1,\pi_2,\ldots,\pi_T\}$, we wish to estimate the mean
of the $h$-step forecast $\pi_{T+h|T}$.
Since $\pi_{T+h|T}$ is not known, we seek an estimator $\hat{\pi}_{T+h|T}$.

# Data description
The \emph{accuracy} $\{\pi_t\}$ of the adversary is the single entity we are
observing and we have $T$ measurements of it over logical time.

The confidentiality data $\{\pi_t\}$ depends upon two other time series, the
plaintext (keyword searches) $\{x_t\}$ and the ciphers $\{c_t\}$, which Alex
Towell generated in 2016 using the following steps:
\begin{enumerate}
\item The parameters of a Bigram language model were estimated from a large
corpus of plaintext.
(The source of the particular corpus used has been lost.)
\item The estimated Bigram language model was conditionally sampled from to
generate plaintexts $\{x_t\}$.
\item Each plaintext $x_t$ was cryptographically hashed to a cipher
$c_t = \operatorname{h}(x)$ to generate ciphers $\{c_t\}$.
\end{enumerate}

Note that $\{x_t\}$ and $\{c_t\}$ are not the primary time series of
interest in our analysis.
Rather, our primary interest is in the confidentiality measures $\{\pi_t\}$.
To generate this time series, the following steps were taken:
\begin{enumerate}
\item The function $\operatorname{g}$ that maps ciphers to plaintext is
estimated after every $N=50$ observations of the cipher time series using a
MLE under a unigram language model (some information in the bigram model is not
being used by the estimator, which reduces its efficiency) on a different corpus
judged to be similiar to the one used to generate $\{x_t\}$.
Thus, the unigram MLE of $\operatorname{g}$ at time $T$ is given by
$$
    \hat{\operatorname{g}}_T = \argmax_{\operatorname{g} \in G}
    \prod_{t=1}^{T} \hat{\Pr}(X_t = \operatorname{g}(c_t)).
$$

Note that $\hat{\operatorname{g}}_T$ is inconsistent since it does not converge
in probability to $\operatorname{g}$ as a consequence of the adversary's
estimation of $\Pr(X_t)$ with $\hat{\Pr}(X_t)$.

This inconsistency was motivated out of a desire to be more realistic, since an
adversary who is performing the known-plaintext attack cannot in practice know
the underlying distribution of $\{x_t\}$ used to generate the keyword searches.
\item The confidentiality measure at time $t$, denoted by $\pi_t$, is computed
using $\hat{\operatorname{g}}_{t}$.
\end{enumerate}

\begin{remark}
In a real data set, $\{\pi_t\}$ may be a function of many other co-variates that
may be difficult or impossible to model effectively.
In this case, we may use something like a seasonal ARIMA model to model the
correlated residuals that are a result of functional missspecification or
important predictors that have been omitted in the model.
\end{remark}

# Time series analysis of $\{\pi_t\}$
It seems clear that the adversary's accuracy at a particular time will be
correlated with lagged (previous) values of its accuracy and the closer in time
they are the more heavily correlated they will generally be (barring exceptions
like seasonality).

We partition the data into a training set and a test set.
We will not look at the test set until later when we evaluate the model.
Here is a quick glimpse of the training set data:












































