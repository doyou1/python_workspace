import numpy as np

x = np.arange(4).reshape((2, 2))
print(f"x: {x.shape}\n{x}")
# x: (2, 2)
# [[0 1]
#  [2 3]]

rep = np.repeat(x, repeats=3, axis=0)
print(f"np.repeat(x, 3, 0): {rep.shape}\n{rep}\n")
# np.repeat(x, 3, 0): (6, 2)
# [[0 1]
#  [0 1]
#  [0 1]
#  [2 3]
#  [2 3]
#  [2 3]]

rep = np.repeat(x, repeats=3, axis=1)
print(f"np.repeat(x, 3, 1): {rep.shape}\n{rep}\n")
# np.repeat(x, 3, 1): (2, 6)
# [[0 0 0 1 1 1]
#  [2 2 2 3 3 3]]