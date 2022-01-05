import numpy as np

a = np.arange(9)

b = a.resize((2,2))

print("original ndarray: \n", a)
print("resized ndarray: \n", b)
#  [[0 1]
#  [2 3]]