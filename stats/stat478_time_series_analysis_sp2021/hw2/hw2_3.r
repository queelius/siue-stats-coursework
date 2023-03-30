# homework #2: problem 3

library(TSA)
data(wages)

pdf(file="plot3_a_raw.pdf")
plot(wages, type="l")

t <- 1:length(wages)

wages.linear=glm(wages~t)

pdf(file="plot3_b_lin_fit.pdf")
ts.plot(wages,wages.linear$fitted.values)

#plot.ts(wages, type="l")

print("linear regression")
print(wages.linear)

pdf(file="plot3_c_lin_resid.pdf")
plot.ts(wages.linear$residuals)

t2 <- t^2
pdf(file="plot3_d_qd_fit.pdf")
wages.qd=glm(wages~t+t2)
ts.plot(wages,wages.qd$fitted.values)

print("quadratic regression")
print(wages.qd)

pdf(file="plot3_e_qd_resid.pdf")
plot.ts(wages.qd$residuals)
