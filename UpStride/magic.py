import numpy as np

m = np.array([[1,2,3],[4,5,6],[7,8,9]])

def some_magic(m):
    return m/np.stack([list(np.sqrt(np.sum(np.square(m),-1)))]*m.shape[-1], -1)



import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize

x = np.random.randn(100).reshape(1, -1)
y = np.random.randn(100).reshape(1, -1)

x_l2_norm = normalize(x, norm="l2")
y_l2_norm = normalize(y, norm="l2")
x_l2 = x_l2_norm
y_l2 = y_l2_norm
plt.scatter(x, y)
plt.scatter(x_l2, y_l2)

