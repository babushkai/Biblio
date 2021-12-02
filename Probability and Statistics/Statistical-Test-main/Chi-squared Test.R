###Chi-squared Test###


chisq.test()
x = c(28,20,22,30) # Frequency 
p=rep(0.25,4) # Repeat four times

chisq.test(x, p=p) #p: theoretical probability vector
# H_0 null hypothesis
# Distribution is uniform

#x=c(40,20,22,420)
x=c(40,20,22,42)
chisq.test(x,p=p)
# p-value = 0.004567
# H_A: Alternative hypothesis
# Statistically Significant

A=rpois(100,0.4)
A
table(A)
#B:  Approximate replacement of A
B=c(70,25,5)

# Is B distributed as a Poisson random variable
# Use method of moment
# theoretical mean: lambda
lambda=(70*0+25*1+5*2)/(70+25+5) # Empirical mean
lambda

# You add the slot for the value >=2
Bb=c(B,0)

tp=dpois(c(0,1,2),lambda)
tp

# # PMF: lambda^k e^{-lambda}/k! same as dpois
for (k in 0:4){
  print("PMF")
  print(((lambda^k)*exp(-lambda))/factorial(k))
}

Pt=c(tp, 1-sum(tp))
Pt


chisq.test(Bb, p=Pt) 
# This estimation is wrong, 
# degree of freedom should be 2 as lambda is the estimated parameter

# Theoretical threshold
qchisq(0.95,2)
# As D^2=0.66691 is smaller than s=5.991465, we are not in the region of reject
# So we decide H_0: Null Hypothesis
# How to get the p-value for our test?
# P(Chi-square with 2 degree of freedom > 0.66691)
#=1-P(chi-square with 2 degree of freedom<=0.66691)
p_value=1-pchisq(0.66691,2)
p_value
# H_0: Null Hypothesis as p-value is big(0.7164441)
