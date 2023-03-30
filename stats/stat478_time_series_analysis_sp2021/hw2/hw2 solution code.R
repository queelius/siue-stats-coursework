## Q2-b
z1=rnorm(1,0,1)
z2=rnorm(1,0,1)
e=rnorm(250,0,1)
w=0.5
t=1:250
y=z1*cos(w*t)+z2*sin(w*t)+e
plot.ts(y)		## cyclical stationary time series

## Q2-c
z1=rnorm(1,0,1)
z2=rnorm(1,0,1)
e=rnorm(250,0,1)
x=0.5
b0=100	#you may pick other numbers of b0 and b1
b1=0.1
x=b0+b1*t+z1*cos(w*t)+z2*sin(w*t)+e
plot.ts(x)		## cyclical with an increase over time trend

## Q2-d
dx=diff(x)
plot.ts(dx)		## cyclical stationary time series

#########################

library(TSA)
data(wages)

## Q3-a
plot.ts(wages)		## increasing overtime, no visible seasonal pattern

## Q3-b
t=1:length(wages)
wage.lin=lm(wages~t) ## equation: wages=7.93144+0.02342t 
fitted.ts=ts(wage.lin$fitted.values,start = start(wages),frequency = 12)
ts.plot(wages,fitted.ts)

## Q3-c
plot(wage.lin$residuals)	##quadratic pattern

## Q4-d
t2=t^2
wage.qd=lm(wages~t+t2) ## equation: wages=7.7974363+0.0342882t-0.0001488t^2
qdfitted.ts=ts(wage.qd$fitted.values,start = start(wages),frequency = 12)
ts.plot(wages,qdfitted.ts)

## Q3-e
plot(wage.qd$residuals)		##seems to be random noise now
