# homework #1: problem 4.d
# parameters:
#     sigma=1 is the standard deviation of {e[t]}
#     mu is the mean of {e[t]}
#     Y[t] := (et + e[t-1]+...+e[t-k+1])/k
#     n is size of time series
#     l is the lag dependency
sigma <- 1
n <- 100
mu <- 0
e <- rnorm(n, mean=mu,sd=sigma)
l <- 3
Y <- vector(length=n)

# first l {Y[t]} are zero
for (i in 1:l)
{
    Y[i]=0
}

for (i in l:n)
{
    Y[i]=sum(e[(i-l+1):i])/l
}

pdf(file="plot4_d.pdf")
plot(Y,type="l")