setwd("C:/users/daisu/OneDrive/Desktop/DSTI/ASML")
A = read.table("Chenilles.txt", header=TRUE)
head(A)

y = A$NbNids
ncol(A)
X = A[,1:10]
L=lm(y ~., data=X)

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
#We can accept the gaussianity of the noise
## Noise != Residual, if residual is gaussian, noise is gaussian
sres=rstandard(L)
ks.test(sres, "pnorm")

#To see the additional info
#Look at P-value of the residual to check if we can use the linear model
#Check R^2 to see the goodness of fit
#The difference between r^2 and adjusted are from variables which are redundant
#Adjusted R^2 score 
#Look at P-value of each variable, high P-value is H_0, zero coefficients
summary(L)

#Look at correlation now
#There are high correlation among variables
cor(X)

#Now we can apply the variable selection in the frame of linear model
#Fisher-criterion(Forward, Backward) and Akaike info-criterion
#L is the biggest
L0 = lm(log(y)~1,data=X) #Individual intercept is not consistent with a whole one

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
Lv = step(L, data=X, test="F")

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
#1se rule, to see the find the best lambda
b1=Lambda$lambda.1se
La=glmnet(as.matrix(X), y, alpha=1, lambda = b1)

summary(La)

#Here the selected variables are non-zeros
#Now the question is am I going to use those coefficients?
# No, we need to determine the selected variables and construct the moodel again
coefficients(La)

#In addition, we can use non-linear model: Random Forest
#If you want to have a maximum tree, take the cp=0
#At no moment, your maximum tree can be a root
#Overfitting: too
#Pruning: nested of trees collection of models


library(rpart)
# default: cp=0, minsplit=2
T=rpart(y~.,data=X, cp=0, minsplit=2)
# We cannot use this as it's too complex and bad prevision, therefore
# We perform pruning, instead
# thirty different models are displayed here
printcp(T)
# cp = Cross Validation error, increasing and decreasing
# tree sizes=22 is overfitting
# Add 2 and 22 and make a new set 

plotcp(T)

# VSURF can be used for the variable selection

#Select the smallest std error
# W = std
# E = rk of the explanatory variable
# W = f(E) to estimate it with a CART 
library(VSURF)
TV = VSURF(log(y)~., data=X)
plot(TV)

names(TV)
# Suppress several variables which are noises
TV[[1]]

# 2 and 3 interpretation(select model with smallest OOB-error)
# and prediction(included in the interpretation part)
TV[[2]]
TV[[3]]
