library(fpp2)
library(forecast)
library(TSA)

p.data <- read.table(file="./acc2",sep=" ",nrows=12000,header=TRUE)
p <- p.data[1000:10000,]
p <- ts(p.data["accuracy"],start=1000)

m.theory <- nls(p ~ I(c)-I(a)*exp(-I(b)*time(p)),
                start=list(b=.005,a=.05,c=.5),trace=T)

coef(m.theory)
data <- resid(m.theory)

plot(fitted(m.theory))
lines(p)

acf(data)
pacf(data)

data.diff <- diff(data,1)
acf(data.diff)
pacf(data.diff)

m.auto <- auto.arima(data)
summary(m.auto)
pacf(resid(m.auto))
     
r.abs <- abs(resid(m.theory))
r.fitted <- lm(r.abs ~ fitted(m.theory))$fitted.values
w <- 1/(r.fitted)

p.weighted <- .01*p*w

m1 <- auto.arima(p.weighted)

summary(m1)
acf(resid(m1))
pacf(resid(m1))

model <- Arima(p,order=c(1,1,2))
summary(model)
Box.test(resid(m1),lag=10,fitdf=1,type="Ljung-Box")
qqnorm(resid(m1))

fitdf <- length(coef(model))
Box.test(model$residuals,lag=10,type="Ljung-Box")
qqnorm(model$residuals)



qqnorm(resid(m1))

plot(fitted(auto.arima(p)))

#m.weighted <- nls(p ~ I(c)-I(a)*exp(-I(b)*time(p)),
#                  start=list(b=.005,a=.05,c=.5),trace=T,weights=wts)
#r.abs <- abs(resid(m))
#r.fitted <- lm(r.abs ~ fitted(m))
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
