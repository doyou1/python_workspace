import numpy as np

col_vec = np.arange(4).reshape((-1, 1))
print(f"ndarray: {col_vec.shape}\n{col_vec}\n")

rep = np.repeat(col_vec, repeats=3, axis=1)
print(f"repeats=3, axis=1: {rep.shape}\n{rep}")