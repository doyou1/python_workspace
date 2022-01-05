import numpy as np

a = np.arange(1,5).reshape((2,2))
mask = np.array([[0,0], [1,0]])

print("input: \n", a)
print("mask: \n", mask)
print("output: \n", a*mask)