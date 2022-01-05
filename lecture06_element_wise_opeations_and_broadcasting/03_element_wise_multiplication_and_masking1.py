import numpy as np

a = np.arange(5)
mask = np.array([0,1,0,1,0])

print("input: ", a)
print("mask: ", mask)
print("output: ", a*mask)