import numpy as np

a = np.arange(10)
indices = np.array([0,3,6,-1])
print(f"ndarray: \n{a}\n")
print(a[[0,3,6,-1]])
print(a[indices])
print(a[a%3==0])