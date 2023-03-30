library(fpp2)
library(forecast)
library(TSA)

p.data <- read.table(file="./acc2",sep=" ",nrows=10000,header=TRUE)
head(p.data)
NLSstRtAsymptote(x=p.data$t,y=p.data$accuracy)
p <- p.data[1000:10000,]

p <- ts(p.data["accuracy"],start=1000)


ols.fit <- lm(p ~ time(p))

plot(resid(ols.fit))



r.abs <- abs(resid(m))
#r.fitted <- lm(r.abs ~ fitted(m))$fitted.values

#wts <- 1/(r.fitted^2)
#m.weighted <- nls(p ~ I(c)-I(a)*exp(-I(b)*time(p)),
#                  start=list(b=.005,a=.05,c=.5),trace=T,weights=wts)


fit_fn <- function(t,m)
{
  a <- coef(m)["a"]
  b <- coef(m)["b"]
  c <- coef(m)["c"]
  c - a * exp(-b*t)
}
