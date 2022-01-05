import numpy as np

a = np.arange(4).reshape((1, -1))
tile = np.tile(a, reps=[5, 1])

print(f"ndarray: {a.shape}\n{a}")
print(f"tile: {tile.shape}\n{tile}")
# ndarray: (1, 4)
# [[0 1 2 3]]
# tile: (5, 4)
# [[0 1 2 3]
#  [0 1 2 3]
#  [0 1 2 3]
#  [0 1 2 3]
#  [0 1 2 3]]

a = np.arange(4).reshape((-1, 1))

tile = np.tile(a, reps=[1, 5])

print(f"ndarray: {a.shape}\n{a}")
print(f"tile: {tile.shape}\n{tile}")
# ndarray: (4, 1)
# [[0]
#  [1]
#  [2]
#  [3]]
# tile: (4, 5)
# [[0 0 0 0 0]
#  [1 1 1 1 1]
#  [2 2 2 2 2]
#  [3 3 3 3 3]]