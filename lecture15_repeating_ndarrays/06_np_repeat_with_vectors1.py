import numpy as np

row_vec = np.arange(4).reshape((1, -1))
print(f"ndarray: {row_vec.shape}\n{row_vec}\n")
# ndarray: (1, 4)
# [[0 1 2 3]]

rep = np.repeat(row_vec, repeats=3, axis=0)
print(f"repeats=3, axis=0: {rep.shape}\n{rep}\n")
# repeats=3, axis=0: (3, 4)
# [[0 1 2 3]
#  [0 1 2 3]
#  [0 1 2 3]]