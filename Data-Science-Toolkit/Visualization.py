import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

##matplotlib
plt.plot(x, y, 'r') # 'r' is the color red
plt.xlabel('X Axis Title Here')
plt.ylabel('Y Axis Title Here')
plt.title('String Title Here')
plt.show()

fig, axes = plt.subplots(1, 3, figsize=(12, 4))

axes[0].plot(x, x**2, x, x**3)
axes[0].set_title("default axes ranges")

axes[1].plot(x, x**2, x, x**3)
axes[1].axis('tight')
axes[1].set_title("tight axes")

axes[2].plot(x, x**2, x, x**3)
axes[2].set_ylim([0, 60])
axes[2].set_xlim([2, 5])
axes[2].set_title("custom axes range");


#Create subplots
plt.subplot(2,1,1) # row 2 column 1 first
x = np.random.uniform(0, 1, 1000)
plt.hist(x)

plt.subplot(2,1,2) # row 2 column 1 second
y = np.random.uniform(0, 1, 1000)
plt.hist(y, color="orange")


##Seaborn
#Distribution Plots
sns.distplot(tips['total_bill'])
sns.distplot(tips['total_bill'],kde=False,bins=30)
sns.jointplot(x='total_bill',y='tip',data=tips,kind='scatter')
sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')
sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg')
sns.pairplot(tips)
sns.pairplot(tips,hue='sex',palette='coolwarm')


#Categorical Plot
sns.barplot(x='sex',y='total_bill',data=tips)
sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std)
sns.countplot(x='sex',data=tips)
sns.boxplot(x="day", y="total_bill", data=tips,palette='rainbow')
sns.boxplot(data=tips,palette='rainbow',orient='h')
sns.boxplot(x="day", y="total_bill", hue="smoker",data=tips, palette="coolwarm")
sns.violinplot(x="day", y="total_bill", data=tips,palette='rainbow')
sns.violinplot(x="day", y="total_bill", data=tips,hue='sex',palette='Set1')
sns.violinplot(x="day", y="total_bill", data=tips,hue='sex',split=True,palette='Set1')
sns.stripplot(x="day", y="total_bill", data=tips)
sns.factorplot(x='sex',y='total_bill',data=tips,kind='bar')

#Matrix Plots
sns.heatmap(tips.corr(),cmap='coolwarm',annot=True)
flights.pivot_table(values='passengers',index='month',columns='year')
sns.clustermap(pvflights)

#Regression Plots
sns.lmplot(x='total_bill',y='tip',data=tips)
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',palette='coolwarm')
sns.lmplot(x='total_bill',y='tip',data=tips,col='day',hue='sex',palette='coolwarm',
          aspect=0.6,size=8)


##Pandas
df['A'].hist()
df.plot.area(alpha=0.4)
df.plot.bar()
df.plot.line(x=df1.index,y='B',figsize=(12,3),lw=1)
df.plot.scatter(x='A',y='B')
df.plot.box() # Can also pass a by= argument for groupby
df.plot.hexbin(x='a',y='b',gridsize=25,cmap='Oranges')
df.plot.density()


#3D plotting 
# Simple 3D plotting
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x, y):
  return -x*y
  
def f2(x, y):
  return x**2+2*x+x*y+y**2-4*y+3

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
x = np.linspace(-10,10)
y= np.linspace(-10,10)
X, Y = np.meshgrid(x, y)
Z = f2(X, Y)
ax.plot_wireframe(X, Y, Z, 1)
plt.plot(x,y, np.zeros(len(x)))
