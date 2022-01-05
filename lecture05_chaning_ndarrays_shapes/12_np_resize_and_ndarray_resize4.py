import numpy as np

a = np.arange(9)

b = np.resize(a, (2,3,3))

print("original ndarray: \n", a)
print("resized ndarray: \n", b)