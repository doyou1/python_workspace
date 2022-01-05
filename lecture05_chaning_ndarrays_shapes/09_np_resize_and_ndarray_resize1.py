import numpy as np

a = np.arange(6)

b = np.resize(a, (2,3))

print("original ndarray: \n", a)
print("resized ndarray: \n", b)