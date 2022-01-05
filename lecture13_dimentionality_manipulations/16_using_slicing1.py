import numpy as np

a = np.arange(6).reshape((2, 3))

row, col = a[1, :], a[:, 1]

print(f"a: {a.shape}\n{a}\n")
# a: (2, 3)
# [[0 1 2]
#  [3 4 5]]

print(f"row: {row.shape}\n{row}")
print(f"col: {col.shape}\n{col}")
# row: (3,)
# [3 4 5]
# col: (2,)
# [1 4]