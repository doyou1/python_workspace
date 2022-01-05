import numpy as np

a = np.arange(4)
print(f"ndarray: {a.shape}\n{a}\n")
# ndarray: (4,)
# [0 1 2 3]

tile = np.tile(a, reps=3)
print(f"reps=3: {tile.shape}\n{tile}")
# reps=3: (12,)
# [0 1 2 3 0 1 2 3 0 1 2 3]