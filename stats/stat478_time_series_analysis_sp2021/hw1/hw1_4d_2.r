# n is size of time series
n <- 10000

# {e[t]} is the white noise time series
e <- rnorm(n, mean=0,sd=1)

# {Y[t]} is the time series of interest
Y <- vector(length=n)

Y[1] = 0
for (t in 2:n)
{
    Y[t]=e[t]*e[t-1]
}

pdf(file="plot_prod.pdf")
plot(Y,type="l")
