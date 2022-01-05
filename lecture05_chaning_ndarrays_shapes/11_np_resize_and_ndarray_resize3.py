import numpy as np

a = np.arange(6)

b = np.resize(a, (3,4))
print("original ndarray: \n", a)
print("resized ndarray: \n", b)
# [[0 1 2 3]
#  [4 5 0 1]
#  [2 3 4 5]]