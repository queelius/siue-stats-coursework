# homework #1: problem 3
#
# requires:
#     - TSA library      : install.packages('TSA')
#     - forecast library : install.package('forecast')
library(TSA)
library(forecast)

# (a) the TSA library in R contains the data set co2, which lists monthly carbon
# dioxide (CO2) levels in northern Canada from 1/1994 to 12/2004. construct a
# time series plot of the data. print the plot and describe all systematic
# patterns you see in the plot.

data(co2)
pdf(file="plot3_a.pdf")
plot.ts(co2)
dev.off()

# (b) applying a moving average filter of span 12 to the data. plot the original
# data and overlay (superimpose) the moving average. discuss whether the moving
# average filter captures the overall trend in the time series.
co2.ma12=ma(co2,order=12)

pdf(file="plot3_b.pdf")
plot.ts(co2)
lines(co2.ma12)
dev.off()

