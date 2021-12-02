data("mtcars")
head(mtcars)

#ANOVA with 1 factor
Y=mtcars$mpg
F=as.factor(mtcars$cyl)
boxplot(Y~F)
L=lm(Y~F)
anova(L)

#ANOVA with 2 factors
F1=F
F2=as.factor(mtcars$gear) #second factor
R=mtcars$gear  #if we do not transform into a factor

L2c=lm(Y~F1+F2+F1*F2)  #the complite model with the cross effect
L2a=lm(Y~F1+F2)  #just the additive model

anova(L2c) #the classical output.
#this time, 4 rows. But we can just at first use the one
#associated to the cross-effect
#here a big p-value so we accept the additive model instead
#of the complete one
#to see if there is an influence of F1 or F2, we have now
#to work into the additive model L2a

anova(L2a)
#since we have a big p-value on the line L2, it means
#that F1 factor as an influence
#for this reason, we can look at the line for F2
#as a small p-value, no influence
#and so we just perform now a simple ANOVA with factor F1


Lancova=lm(Y~F1+R+F1*R) #mixture between a factor and a 
#numeric explanatory variables : ANalysis Of COvariance
