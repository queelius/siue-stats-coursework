
#We begin by calling the data for handout 11
library("readxl")
setwd("C:/Users/aneath/iCloudDrive/Lexar/stat581 fall2021")

h11.data = read_excel("handout11data.xlsx")
str(h11.data)

#We will use the package lsmeans for computing least squares means in Analysis of Covariance
library("lsmeans")

#We will use the package car (companion to applied regression) for computing partial sums of squares
library("car")

#Example 11.1
#Data is collected to investigate the effect of origin on the weight of a turkey, with age used as a covariate.
origin = as.factor(na.omit(h11.data$origin))
age = na.omit(h11.data$age)
weight = na.omit(h11.data$weight)

#We fit an ANCOVA model using the following code. lm is an abbreviation for linear model.
ancova.mod = lm(weight ~ age + origin)

#The anova command creates a table with sequential sums of squares. 
#The summary command displays the parameter estimates.
anova(ancova.mod)
summary(ancova.mod)

#The default parameterization in R does not match that from our notes. 
#Use the following commands to compute the intercepts and slope for each regression function.
#We will least squares means later to complete the re-parameterization
intercept.g = coef(ancova.mod)[1]
intercept.v = coef(ancova.mod)[1]+coef(ancova.mod)[3]
intercept.w = coef(ancova.mod)[1]+coef(ancova.mod)[4]
slope = coef(ancova.mod)[2]

#The following code creates a display of the regression line estimates
intercepts = c(intercept.g,intercept.v,intercept.w)
slopes = c(slope,slope,slope)
reg.functions = matrix(c(intercepts,slopes),nrow = 3)
dimnames(reg.functions)=list(c("georgia","virginia","wisconsin"),c("intercept","slope")) 
reg.functions

#Here is the code for creating a scatterplot of weight against age grouped by origin. 
#The command plot initiates the scatterplot, and creates the plot for origin = "g". 
#The command points adds the plots for the other origin levels. 
#The command abline includes the estimated regression functions.
#The options are set so that the range of the plot will include all data points, 
#and so that the labels, coloring, and symbols make the plot easy to read. 
plot(age[origin == 'g'], weight[origin == 'g'], xlab='age',
     ylab='weight', pch=15, col='blue',xlim = c(min(age),max(age)),ylim = c(min(weight),max(weight)))
points(age[origin == 'v'], weight[origin == 'v'], pch=16, col='red')
points(age[origin == 'w'], weight[origin == 'w'], pch=17, col='green')

abline(intercept.g,slope,col='blue')
abline(intercept.v,slope,col='red')
abline(intercept.w,slope,col='green')


#The following code is one option for computing sample means by group. Each call produces 2 columns. 
#The first column is the group level, the second column is the sample mean by group. 
#Since we need only one column for group level, the second call returns only the sample mean column. 
#The result is a table with origin levels, and sample means for age and weight. 
xbar.origin = aggregate(age, by=list(origin), FUN=mean)
ybar.origin = aggregate(weight, by=list(origin), FUN=mean)[2]
means.table = cbind(xbar.origin,ybar.origin)
colnames(means.table) = c("origin","age.mean","weight.mean")
means.table

#The overall mean for the covariate age will determine the adjustment to the response sample means
mean(age)

#Here is the code for computing least squares means and performing pairwise comparisons on the adjusted means. 
lsmeans(ancova.mod,pairwise ~ origin,adjust="none")


#Here is the R code for fitting an ANOVA model. 
#We are using the lm function (linear model) to illustrate the connection to ANCOVA. 
#The covariate is not included in the model and thus plays no role in the analysis. 
#Note how differences in origins are missed when the covariate information is not included.
a.mod = lm(weight ~ origin)
anova(a.mod)



#Example 11.2
#An experiment is conducted to investigate the effects of temperature and pressure on the yield of a chemical reaction. 
#Two levels of each factor are considered, but missing values prevent the running of a full factorial.

A = as.factor(na.omit(h11.data$temperature))
B = as.factor(na.omit(h11.data$pressure))
y = na.omit(h11.data$yield)

#Display the observed values
unbalanced.data = matrix(c(A,B,y),ncol = 3)
colnames(unbalanced.data) = c("temp","press","yield")
print(unbalanced.data)

#Note that the sample sizes at treatment combinations are not equal
xtabs(~ A+B)

#fit the ANOVA model using the lm command. A,B are factor variables
unbalanced.mod = lm(y ~ A+B)

#the anova call tests A,B effects sequentially. 
#sum of squares displayed are R(A) and R(B|A)
anova(unbalanced.mod)
Anova(unbalanced.mod,type=2)

#Note how the parameter estimates represent partial effects
dummy.coef(unbalanced.mod)

#Let's investigate extra sum of squares further by fitting reduced models
a.mod = lm(y~A)
b.mod = lm(y~B)

#For these models, the parameter estimates represent marginal effects
dummy.coef(a.mod)
dummy.coef(b.mod)

#Here are the respective fitted values
predict(unbalanced.mod)
predict(a.mod)
predict(b.mod)

#Here we can fine the marginal sums of squares
anova(a.mod)
anova(b.mod)









































































































































































































































































