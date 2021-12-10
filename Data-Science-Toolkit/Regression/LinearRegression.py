# OLS Scratch 
import pandas as pd
import numpy as np

name = ["Alcohol", "Malic", "acid", "Ash", "Alcalinity of ash", "Magnesium", "Total phenols", 
              "Flavanoids", "Nonflavanoid phenols", "Proanthocyanins", "Color intensity",
               "HueOD280/OD315 of diluted wines", "Proline"]
df = pd.read_csv("/content/wine.data", names = name, header=None)


X = df.iloc[:, :-1].values
Y = df.iloc[:,-1].values

X_XT = np.matmul(X.T, X)
invX_XT = np.linalg.inv(X_XT)
X_T = invX_XT @ X.T
B = X_T @Y

# B = np.linalg.inv(X.T @ X) @ X.T @ Y

# OLS Scikit-Learn
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X, Y)
lr.coef_

# Ridge Scratch

lambda_ = 0.5
I = np.identity(12)
(np.linalg.inv(X.T @X + lambda_*I) ) @ X.T @Y

# Ridge Scikit-Learn
from sklearn import linear_model
reg = linear_model.Ridge(alpha=.5)
reg.fit(X, Y)

print(reg.coef_)