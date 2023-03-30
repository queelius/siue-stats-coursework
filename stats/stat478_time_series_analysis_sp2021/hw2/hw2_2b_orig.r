# homework #2: problem 2.b

# n is size of time series
n <- 250

w <- 0.5

# z(1),z1(2) ~ N(0,1)
z <- rnorm(2, mean=0,sd=1)

# {e[t]}
e <- rnorm(n, mean=0,sd=1)

# {Y[t]} is the time series of interest
Y <- vector(length=n)

for (t in 1:n)
{
    Y[t] = z[1]*cos(w*t) + z[2]*sin(w*t) + e[t]
}

pdf(file="plot2_b_orig.pdf")
plot(Y,type="l", xlab="t", ylab="Y")
