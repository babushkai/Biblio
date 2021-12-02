mtcars  #a dataset
#we want to explain the mpg variables with the other ones

L=lm(mpg~.,data=mtcars)

#backward selection with the Fisher criterion and by ourself

#the first step in this case is the test of the nullity of one coefficient
#this is given in the listing of the summary

summary(L)
#we look the biggest p-value associated to the student test
#this one is associated to cyl
#we delete this variable

L=lm(mpg~.,data=mtcars[,-2])

#and we repeat this until the moment where the p-value is too small
summary(L)

L=lm(mpg~.,data=mtcars[,-c(2,8)])
summary(L)
L=lm(mpg~.,data=mtcars[,-c(2,8,11)])
summary(L)
L=lm(mpg~.,data=mtcars[,-c(2,8,11,10)])
summary(L)
L=lm(mpg~.,data=mtcars[,-c(2,8,11,10,5)])
summary(L)
L=lm(mpg~.,data=mtcars[,-c(2,8,11,10,5,3)])
summary(L)
L=lm(mpg~.,data=mtcars[,-c(2,8,11,10,5,3,4)])
summary(L)

#all the p-values associated to explanatory variables are too small
#we stop
#the final model contains wt, qsec and am

#the same but with the dedicated function
ml=lm(mpg~.,data=mtcars)  #biggest model
step(ml,data=ml,direction="backward",test="F")

#the forward procedure
m0=lm(mpg~1,data=mtcars)  #smallest model
ml=lm(mpg~.,data=mtcars)  #biggest model
L=step(m0,scope=list(lower=m0,upper=ml),data=mtcars,direction="forward",test="F")

#with the forward, the final selected model is composed of wt, cyl and hp
#not the same model than with backward