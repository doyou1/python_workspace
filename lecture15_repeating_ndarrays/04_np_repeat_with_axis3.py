import numpy as np

x = np.arange(4).reshape((2, 2))
print("x: \n", x, "\n")
# x: 
#  [[0 1]
#  [2 3]]


rep = np.repeat(x, repeats=[2, 1], axis=0)
print(f"repeats=[2, 1]: {rep.shape}\n{rep}\n")
# repeats=[2, 1]: (3, 2)
# [[0 1]
#  [0 1]
#  [2 3]]


rep = np.repeat(x, repeats=[1, 2], axis=0)
print(f"repeats=[1, 2]: {rep.shape}\n{rep}\n")
# repeats=[1, 2]: (3, 2)
# [[0 1]
#  [2 3]
#  [2 3]]

rep = np.repeat(x, repeats=[2, 2], axis=0)
print(f"repeats=[2, 2]: {rep.shape}\n{rep}\n")
# repeats=[2, 2]: (4, 2)
# [[0 1]
#  [0 1]
#  [2 3]
#  [2 3]]