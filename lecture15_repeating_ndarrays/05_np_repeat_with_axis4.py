import numpy as np

x = np.arange(6).reshape((2, 3))
print("x: \n", x, "\n")
# x: 
#  [[0 1 2]
#  [3 4 5]]

rep = np.repeat(x, repeats=[2, 1, 2], axis=1)
print(f"repeats=[2, 1, 2]: {rep.shape}\n{rep}\n")
# repeats=[2, 1, 2]: (2, 5)
# [[0 0 1 2 2]
#  [3 3 4 5 5]]

rep = np.repeat(x, repeats=[1, 2, 2], axis=1)
print(f"repeats=[1, 2, 2]: {rep.shape}\n{rep}\n")
# repeats=[1, 2, 2]: (2, 5)
# [[0 1 1 2 2]
#  [3 4 4 5 5]]

rep = np.repeat(x, repeats=[2, 1], axis=0)
print(f"repeats=[2, 1]: {rep.shape}\n{rep}\n")
# repeats=[2, 1]: (3, 3)
# [[0 1 2]
#  [0 1 2]
#  [3 4 5]]