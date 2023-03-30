######Question 3###############
library(TSA) data(co2) 
plot.ts(co2) #constructing a time series plot
# notice an increasing trend over the years and seasonal variability repeating each year.
co2.ma=filter(co2, rep(1/12,12), side=1) #Apply a MA with span 12
ts.plot(co2, co2.ma) #plot the MA and original time series
#The MA captures the increasing trend over the years.

######Question 4 part d ################
e<-rnorm(n=102,mean=0,sd=1)
y<-vector(length=100)
for (i in 3:102){
	y[i-2]=(e[i]+e[i-1]+e[i-2])/3	
}
plot.ts(y,type="l")

