X=runif(50,0,10)
Y=2+3*X+rnorm(50,0,1)
L=lm(Y~X)
L
summary(L)

#we see in the summary a column called t-value. It means that this value is associated to a student variable


#comparison of student densities with a standard gaussian one
x=seq(-5,5,0.01)
yn=dnorm(x)       #density of a standard gaussian
yt2=dt(x,2)       #density of a student with 2 degrees of freedom
yt5=dt(x,5)       #density of a student with 5 degrees of freedom
yt10=dt(x,10)     #density of a student with 10 degrees of freedom
yt100=dt(x,100)   #density of a student with 100 degrees of freedom
ymax=max(yn,yt2,yt5,yt10,yt100)   #to compute the maximal values for the y axis
plot(x,yn,xlim=c(-5,5),ylim=c(0,ymax),type='l',col='red')   #ploting of the standard gaussian density
par(new=TRUE)   #to supperpose the new graphic to the previous one 
plot(x,yt2,xlim=c(-5,5),ylim=c(0,ymax),type='l',col='blue')   #plotting of the student density with 2 degrees of freedom
par(new=TRUE)
plot(x,yt5,xlim=c(-5,5),ylim=c(0,ymax),type='l',col='green')
par(new=TRUE)
plot(x,yt10,xlim=c(-5,5),ylim=c(0,ymax),type='l',col='yellow')
par(new=TRUE)
plot(x,yt100,xlim=c(-5,5),ylim=c(0,ymax),type='l',col='magenta')


#the same for the chi-square distribution (no comparison with a gaussian)
x=seq(-2,20,0.01)
y2=dchisq(x,2)
y5=dchisq(x,5)
y10=dchisq(x,10)
ymax=max(y2,y5,y10)
plot(x,y2,xlim=c(-2,20),ylim=c(0,ymax),type='l',col='blue')
par(new=TRUE)
plot(x,y5,xlim=c(-2,20),ylim=c(0,ymax),type='l',col='green')
par(new=TRUE)
plot(x,y10,xlim=c(-2,20),ylim=c(0,ymax),type='l',col='yellow')

#the same for a Fisher distribution
x=seq(0.01,20,0.01)
y11=df(x,1,1)
y21=df(x,2,1)
y52=df(x,5,2)
y101=df(x,10,1)
y100=df(x,100,100)
ymax=max(y11,y21,y52,y101,y100)
plot(x,y11,xlim=c(-2,20),ylim=c(0,ymax),type='l',col='blue')
par(new=TRUE)
plot(x,y21,xlim=c(-2,20),ylim=c(0,ymax),type='l',col='green')
par(new=TRUE)
plot(x,y52,xlim=c(-2,20),ylim=c(0,ymax),type='l',col='yellow')
par(new=TRUE)
plot(x,y101,xlim=c(-2,20),ylim=c(0,ymax),type='l',col='red')
par(new=TRUE)
plot(x,y100,xlim=c(-2,20),ylim=c(0,ymax),type='l',col='black')
