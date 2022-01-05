import numpy as np

a = np.arange(6)
b = a.reshape((2,3))

print("original ndarray: \n", a)
print("reshaped ndarray: \n", b, '\n')

a = np.arange(24)
b = a.reshape((2,3,4))

print("original ndarray: \n", a)
print("reshaped ndarray: \n", b, '\n')