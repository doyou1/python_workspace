import numpy as np

a = np.arange(3)
print(f"ndarray: {a.shape}\n{a}\n")
# ndarray: (3,)
# [0 1 2]

tile = np.tile(a, reps=[1, 2])
print(f"reps=[1, 2]: {tile.shape}\n{tile}\n")
# reps=[1, 2]: (1, 6)
# [[0 1 2 0 1 2]]

tile = np.tile(a, reps=[2, 2])
print(f"reps=[2, 2]: {tile.shape}\n{tile}")
# reps=[2, 2]: (2, 6)
# [[0 1 2 0 1 2]
#  [0 1 2 0 1 2]]