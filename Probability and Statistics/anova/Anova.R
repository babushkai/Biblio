setwd('C:/Users/Kingdel/Desktop/ASML')
A=load('Prostate.RData')

Fa=Prostate$gleason #we now with the help page that this is a qualitative variable
Y=Prostate$lpsa

Fa=as.factor(Fa)  #we have to transform it into a factor 
#otherwise the software is going to perform linear model and
#not ANOVA

L=lm(Y~Fa)  #the same function than linear model but since
#a factor this is ANOVA which is performed

L  #we see that no estimation for the modality 6
#we know that we need an assumption to manage the computations
#this is the reference cell here

summary(L)  #the only information which is interesting
#is the F statistic to see if there is some influence
#of the factor onto the response variable
#but to use this information we have to verify the
#gaussianity of the noise as for linear model
#here some influence since a small p-value

#another way to see this influence is to make a boxplot
boxplot(Y~Fa)

#if all the boxplot are quite the same, no influence
#if difference as here, influence

anova(L)
#in this table which is the classical output for an
#ANOVA, we have two rows
#the first one give information about the upper part
#into the F statistic
#the second one about the bottom part (informations about
#the residuals)



