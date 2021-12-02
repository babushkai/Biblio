setwd('C:/Users/Kingdel/Desktop/FSML-2') #to change the working directory
A=load('A1.Rdata') #to load an object which is a .Rdata
A  #to see what are the object saved. Here an object A1
head(A1) #printing of the 6 first rows of A1
#we see that A1 is a data.frame since it is written
#1 and note [1,] to indicate the number of the row

#we want to see if there exists some link between the two
#columns of A1
#We begin by a plotting

plot(A1$X,A1$Y)
#we see a linear tendancy between the X and the Y

#to evaluate the quality of the linear model, we can
#compute the coefficient of determination by using the fact
#that it is the square of the correlation coefficient
#we can by this way evaluate the quality of the model before
#performing it

r=cor(A1$X,A1$Y)
r^2

#the value is really close to 1, so the linear model can be a correct one

L=lm(Y~X,data=A1)  #we need to precise data=A1 because the
#objects X and Y does not exists, there are just defined
#in A1
#other possible writting L=lm(A1$Y~A1$X)

L
#default printing, qwhere we get the estimation
#of beta_0 and beta_1

summary(L)
#a lot of outputs but we cannot use all of them in all the cases

#the column estimates can always be used
#the remaining, it depends :

#if we can accept that the noise variables have all the same variance,
#we can use the residuals standard error
#if the variances of the noise are not equal, this quantity 
#has no meaning.
#In this case, we can try to make some transformations of the data
#to come back to the framework with same variances

#then, the standard error et the t-value can be computed.
#the values in the columns standard error give the estimation
#of the variances of the beta_hat_i
#estimations because those variances depend on the unknown parameter
#sigma^2 so we replace it by its estimator

#the t-value we can compute it but without other assumptions on the noise
#there is no interest to those quantities

#if the noise can be considered as gaussian, then we can say more
#the t-value is then the observed value of a student random variable
#when we assume that the associated beta_i is equal to 0
#the p-value is the critical probability of the test beta_i=0 versus
#beta_i different from 0
#if this p-value is smaller than a theoretical alpha, then we accept H_1
#and so because we are in simple linear setting, it means that there is 
#an interest to perform a linear regression between X and Y
#if the p-value is bigger than alpha, in fact, there is no linear link
#between X and Y ...
#onto the row associated to residual standard error, the value
#of the degrees of freedom is (n-2) since we know that with gaussian noise
#up to some multiplicative factors, the sigma_hat_n^2 is a chi-square with
#(n-2) degrees of freedom.

#but the question is how to see if we can consider that the noise is gaussian?
#we are going to consider the standardized residuals

sr=rstandard(L) #vector of the standardized residuals

#to see the normality of the noise
#histogram of the standardized residuals

hist(sr,freq=FALSE)

#we can add on this drawing the density of the standard gaussian
#since we know that an asymptotic distribution of the standardized
#residuals is a standard gaussian

#normal QQ-plot
#to obtain this drawing, we can use the default plotting associated to a lm object

plot(L)  #and enter until the normal QQplot

#if the noise is gaussian, the main part of the points should be
#on the dotted line
#the points at bottom left and upper right are always a little 
#bit far.

#for A1, it seems that we can accept the gausianity

#kolmogorov-smirnov test
ks.test(sr,'pnorm')  #pnrom to say that we compare with
#a gaussian distribution. We do not need to precise the
#parameter of the gaussian distribution since it is the
#default one

#for the moment, I cannot explain de value D (next lectures)
# H_O is the observations come from a standard gaussian distribution
#H_1 not the case
#since the p-value is very big, we accept H_0, so we confirm
#the normality of the noise

#so before analyzing all the outputs of the summary, we need to
#look at the gaussianity of the noise

#to see if we can accept the fact that all the variances are equal 
#for the noise, we look at the plot residuals vs fitted-values
#if some symmetry around the horizontal axis equal to 0, the
#expectation of the noise equal to 0 can be consedered
#if thz considered cloud of points is uniformly repartited with
#no structuration of it, we can accept the fact that all
#the variances are equal

#we do the same job on A2 and A4

A=load('A2.Rdata') #to load an object which is a .Rdata
A
head(A2)
plot(A2$X,A2$Y)
#we see that not a linear model between X and Y, more a quadratic one
#we can consider a model Y=beta_0+beta_1.X^2+noise
#this is a linear model between X^2 and Y

Z=(A2$X)^2
plot(Z,Y)
#linear tendancy

(cor(Z,A2$Y))^2

L2=lm(A2$Y~Z)

#and we do the same than previously
#gaussian noise ok

A=load('A4.Rdata') #to load an object which is a .Rdata
A
head(A4)
plot(A4$X,A4$Y)
#linear tendancy

(cor(A4$X,A4$Y))^2

L4=lm(A4$Y~A4$X)

#and we do the same than previously
#gaussianity of the noise No
#we can see it also in the summary by considering
#the array associated to the residuals

#there is no real symmetry between max/min in one hand and
#Q1/Q3 in the other hand. Problem if we want to see that gaussian
