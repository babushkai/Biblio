setwd("C:/users/daisu/OneDrive/Desktop")
A = read.table("Chenilles.txt", header=TRUE)
head(A)

y = A$NbNids
ncol(A)
X = A[,1:10]
L=lm(Y~X)

#You see the residual is symmetry, but the gaussianity of the model
#is not obvious just by looking at residuals
#If the model has no gaussianity, you cannot make any estimation
summary(L)

#QQ-plot is the standardized residuals(T-standardized)
#First plot was not good enough to make an assumption of the gaussianity
#Might not be homeoscedastic
plot(L)

# Better repartition
# But more details, do the test
L = lm(log(y)~., data=X)
plot(L)

#KS-test
#Standardize first
#P-value is big, so H_0, 
#null hypothesis=Standardized residuals are gaussian
#We can accept the gaussianity of the model
sres=rstandard(L)
ks.test(X, y)

#To see the additional info
#Look at P-value of the residual to check if we can use the linear model
#Check R^2 to see the goodness of fit
#The difference between r^2 and adjusted are from variables which are redundant
#Adjusted R^2 score 
#Look at P-value of each variable, high P-value is H_0, high correlation
summary(L)

#Look at correlation now
#There are high correlation among variables
cor(X)

#Now we can apply the variable selection in the frame of linear model
#Fisher-criterion(Forward, Backward) and Akaike info-criterion
#L is the biggest
L0 = lm(log(Y)~1,data=X) #Individual intercept is not consistent with a whole one

#You see the one variable + intercept
#Now you see the F-value, that is to say the model, H_0 is small model
#You wanna keep H_1, small p-values, good variables
#When your variable name is <none>, it's better to have nothing, means
#all the p-value associated to the variables left are too big to be picked
#That is to say, Stopping criteria
Lv = step(L0, scope=list(lower=L0, upper=L), data=X, direction="forward", test="F")
#modify

#Now how am I going to get the coefficients of useful variables?
#Create the new model with useful

#Backward F
here

#Now there are two different models
#How can I see which model is better in the setting

#forward ??? a set of variables
#backward ??? another set of variable
#??? Comparison ??? learning sample/test sample
#we split the initial dataset at random training/test
#L_1: Linear model using the set of explanatory variables
#determined previously by backward strategy
#???We compute error forward and error backward thanks to test_1
#for L_1 forward and L_1 backward
#We repeat this procedure several times(50) take a mean and keep the smallest mean error
#Use Lasso for several models take the correction of possible lambda 
#You start with lambda=0(classical least square) to lambda = max
library(glmnet)
La = glmnet(as.matrix(X),y, alpha = 0)

#Lasso keeps some variables to zero
plot(La)

#How am going to select the best lambda?
#We consider the threshold value

La$lambda

Lambda=cv.glmnet(as.matrix(X), y, alpha=1)
names(Lambda)
bl=Lambda$lambda.lse
La=glmnet(as.matrix(X), y, alpha=1, lambda = bl)


#Here the selected variables are non-zeros
#Now the question is am I going to use those coefficients?
coefficients(La)

#In addition, we can use non-linear model: Random Forest
#If you want to have a maximum tree, take the cp=0
#At no moment, your maximum tree can be a root
#Overfitting: too
#Pruning: nested of trees collection of models


library(rpart)
T=rpart(y~.,data=X, cp=0, minsplit=2)


