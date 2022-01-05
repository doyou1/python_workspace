import numpy as np

a = np.arange(2*3).reshape((2, 3))
print(f"ndarray: {a.shape}\n")
# ndarray: (2, 3)

reps = np.array([3, 5])
tile = np.tile(a, reps=reps)
print(f"shapes: {tile.shape} - {reps*a.shape}")
# shapes: (6, 15) - [ 6 15]

reps = np.array([10, 8])
tile = np.tile(a, reps=reps)
print(f"shapes: {tile.shape} - {reps*a.shape}")
# shapes: (20, 24) - [20 24]