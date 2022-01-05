import numpy as np

a = np.arange(6).reshape((2, 3))
print(f"ndarray: {a.shape}\n{a}\n")
# ndarray: (2, 3)
# [[0 1 2]
#  [3 4 5]]

tile = np.tile(a, reps=[1, 2])
print(f"reps=[1, 2]: {tile.shape}\n{tile}\n")
# reps=[1, 2]: (2, 6)
# [[0 1 2 0 1 2]
#  [3 4 5 3 4 5]]

tile = np.tile(a, reps=[2, 1])
print(f"reps=[2, 1]: {tile.shape}\n{tile}\n")
# reps=[2, 1]: (4, 3)
# [[0 1 2]
#  [3 4 5]
#  [0 1 2]
#  [3 4 5]]

tile = np.tile(a, reps=[2, 2])
print(f"reps=[2, 2]: {tile.shape}\n{tile}\n")
# reps=[2, 2]: (4, 6)
# [[0 1 2 0 1 2]
#  [3 4 5 3 4 5]
#  [0 1 2 0 1 2]
#  [3 4 5 3 4 5]]