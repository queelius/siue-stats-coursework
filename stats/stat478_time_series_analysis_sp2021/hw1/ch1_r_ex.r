# milk production example

milk <- read.csv("milk-production.csv")
milk.ts=ts(milk[,2],frequency=12, start=c(1962,1))
plot.ts(milk.ts)
decomp.milk=decompose(milk.ts)
plot(decomp.milk)

library(forecast)
milk.ma4=ma(milk.ts,order=4)
plot.ts(milk.ts)
lines(milk.ma4)

#The following is an example is a data set of the number of births per month in New York city, from January 1946 to December 1959

births <- scan("http://robjhyndman.com/tsdldata/data/nybirths.dat")
birth.ts <- ts(births, frequency=12, start=c(1946,1))
plot.ts(birth.ts)
decomp.birth=decompose(birth.ts)
plot(decomp.birth)

