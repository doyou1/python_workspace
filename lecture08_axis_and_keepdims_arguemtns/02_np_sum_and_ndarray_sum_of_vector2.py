import numpy as np

a = np.arange(6).reshape((2,-1))
print("ndarray: \n", a)

print("np.sum: ", np.sum(a))
print("ndarray.sum: ", a.sum())