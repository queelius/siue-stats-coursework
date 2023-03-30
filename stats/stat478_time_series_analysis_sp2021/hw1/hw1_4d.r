# homework #1: problem 4.d

# n is size of time series
n <- 100

# {e[t]} is the white noise time series
e <- rnorm(n, mean=0,sd=1)

# {Y[t]} is the time series of interest
Y <- vector(length=n)

# first 2 elements of {Y[t]} are zero
Y[1]=0
Y[2]=0

for (t in 3:n)
{
    Y[t]=(e[t]+e[t-1]+e[t-2])/3
}

pdf(file="plot4_d.pdf")
plot(Y,type="l")
