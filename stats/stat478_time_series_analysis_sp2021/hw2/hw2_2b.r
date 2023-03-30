# homework #2: problem 2.b

# n is size of time series
n <- 100

w <- .5

# z1(1),z1(2) ~ N(0,1)
z1 <- rnorm(2, mean=-0.85,sd=.05)
# z2(1),z2(2) ~ N(0,1)
z2 <- rnorm(2, mean=0.85,sd=.05)

# {e1[t]}
e1 <- rnorm(n, mean=0,sd=1)
# {e2[t]}
e2 <- rnorm(n, mean=0,sd=1)

# {Y1[t]} is the time series of interest
Y1 <- vector(length=n)

# {Y1[t]} is the time series of interest
Y2 <- vector(length=n)

for (t in 1:n)
{
    Y1[t] = z1[1]*cos(w*t) + z1[2]*sin(w*t) + e1[t]
}

for (t in 1:n)
{
    Y2[t] = z2[1]*cos(w*t) + z2[2]*sin(w*t) + e2[t]
}

pdf(file="plot2_b.pdf")
plot(Y1,type="l", xlab="t", ylab="Y",col="blue")
lines(Y2,col="black")
legend("topright",
c("Y[1]","Y[2]"),
fill=c("blue","black")
)
