# homework #2: problem 3

library(TSA)
data(wages)
print(wages)

t <- 1:length(wages)

wages.linear=glm(wages~t)

pdf(file="plot3_b.pdf")
ts.plot(wages,wages.linear$fitted.values)

#plot.ts(wages, type="l")

print(wages.linear)

pdf(file="plot3_c.pdf")
plot.ts(wages.linear$residuals)

t2 <- t^2
pdf(file="plot3_d.pdf")
wages.qd=glm(wages~t+t2)
ts.plot(wages,wages.qd$fitted.values)

print(wages.qd)


pdf(file="plot3_e.pdf")
plot.ts(wages.qd$residuals)
