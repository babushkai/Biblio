#creation of the data set
set.seed(117)
X1=runif(50,-3.24,4.17)
X2=rexp(50,4.32)
X3=rnorm(50,-3.4,8.74)
X4=rpois(50,2.61)
Y=-5+2*X2-3*X4+rnorm(50,0,1)

#we perform the model thanks to the R2 and adjusted R2 coefficient
#best modele with dimension 1 (just with 1 explanatory variable)
L11=lm(Y~X1)
L12=lm(Y~X2)
L13=lm(Y~X3)
L14=lm(Y~X4)
R1=summary(L11)$r.squared  #by this way, we obtain the R2 coefficient
Ra1=summary(L11)$adj.r.squared  #here this is he adjusted one
R2=summary(L12)$r.squared
Ra2=summary(L12)$adj.r.squared
R3=summary(L13)$r.squared
Ra3=summary(L13)$adj.r.squared
R4=summary(L14)$r.squared
Ra4=summary(L14)$adj.r.squared

R=c(R1,R2,R3,R4)
Ra=c(Ra1,Ra2,Ra3,Ra4)

#the best model with dimension 1 is the one with X4

#best model with dimension 2
#how many model to compare  : 6 (the number of combinations of 2 variables when we have 4)
#the models are 12, 13, 14, 23, 24, 34
L212=lm(Y~X1+X2)
L213=lm(Y~X1+X3)
L214=lm(Y~X1+X4)
L223=lm(Y~X3+X2)
L224=lm(Y~X4+X2)
L234=lm(Y~X3+X4)
R212=summary(L212)$r.squared
Ra212=summary(L212)$adj.r.squared
R213=summary(L213)$r.squared
Ra213=summary(L213)$adj.r.squared
R214=summary(L214)$r.squared
Ra214=summary(L214)$adj.r.squared
R223=summary(L223)$r.squared
Ra223=summary(L223)$adj.r.squared
R224=summary(L224)$r.squared
Ra224=summary(L224)$adj.r.squared
R234=summary(L234)$r.squared
Ra234=summary(L234)$adj.r.squared

#the best model of dimension 2 is the model with X2 and X4

R=c(R,R212,R213,R214,R223,R224,R234)
Ra=c(Ra,Ra212,Ra213,Ra214,Ra223,Ra224,Ra234)

#the best model of dimension 3
#4 models of dimension 3 : 123 124 134 234
L123=lm(Y~X1+X2+X3)
L124=lm(Y~X1+X2+X4)
L134=lm(Y~X1+X3+X4)
L234=lm(Y~X2+X3+X4)
Ra123b=summary(L123)$adj.r.squared
R123b=summary(L123)$r.squared
Ra124b=summary(L124)$adj.r.squared
R124b=summary(L124)$r.squared
Ra134b=summary(L134)$adj.r.squared
R134b=summary(L134)$r.squared
Ra234b=summary(L234)$adj.r.squared
R234b=summary(L234)$r.squared

R=c(R,R123b,R124b,R134b,R234b)
Ra=c(Ra,Ra123b,Ra124b,Ra134b,Ra234b)


#best model with dimension 3 is the one with X2, X3 and X4

#dimension 4
L=lm(Y~X1+X2+X3+X4)
Raf=summary(L)$adj.r.squared
Rf=summary(L)$r.squared

R=c(R,Rf)
Ra=c(Ra,Raf)

x=c(rep(1,4),rep(2,6),rep(3,4),4)  #to create a vector with the different sizes

#plot where we put the value of the R2 and adjusted with respect to the dimension
plot(x,R,type='p',col='red',xlim=c(0,5),ylim=c(0,1))
par(new=TRUE)
plot(x,Ra,type='p',col='blue',xlim=c(0,5),ylim=c(0,1))

#now we just plot the biggest R2 and adjusted one for each dimension
xb=1:4
Rb=c(R4,R224,R234b,Rf)
Rab=c(Ra4,Ra224,Ra234b,Raf)

plot(xb,Rb,col='red',type='l',xlim=c(0,5),ylim=c(0.9,1),ylab='')
par(new=TRUE)
plot(xb,Rab,col='blue',type='l',xlim=c(0,5),ylim=c(0.9,1),ylab='')



#how to do the same with a dedicated function
X=matrix(data=c(X1,X2,X3,X4),ncol=4)  #X=cbind(X1,X2,X3,X4)
library(leaps)  
P=leaps(X,Y,method="adjr2")

X=matrix(rnorm(50*10,3,2),ncol=10)
Y=2+2*X[,2]-5*X[,5]+X[,9]+rnorm(50,0,1)

bestadjR2=function(X,Y)  #Y: response variable (vector), X:matrix with the explanatory variables
{
  library(leaps)
  P=leaps(X,Y,method="adjr2")   
  s=P$size       #to extract the vector with the size of the model (including the intercept)
  a=P$adjr2     #to extract the vector of the adjusted R2 coefficient
  mins=min(s)
  maxs=max(s)
  S=c()
  for (i in mins:maxs)
  {
    b=which(s==i)  #vector of the positions where the size of the model is i
    bb=b[1]        #we keep the first element of the previous vector
    aa=a[bb]
    S=c(S,aa)
  }
  bestadjR2=list(size=mins:maxs,adjr2=S)
}


#you can get exactly this by writting P=leaps(X,Y,method="adjr2",nbest=1)

