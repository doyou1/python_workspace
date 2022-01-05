import numpy as np

a = np.arange(9).reshape((1, -1))
b = np.arange(9).reshape((-1, 1))

c = a[0, :]
d = b[:, 0]

print(f"a: {a.shape}\n{a}")
print(f"b: {b.shape}\n{b}\n")
# a: (1, 9)
# [[0 1 2 3 4 5 6 7 8]]
# b: (9, 1)
# [[0]
#  [1]
#  [2]
#  [3]
#  [4]
#  [5]
#  [6]
#  [7]
#  [8]]

print(f"c: {c.shape}\n{c}")
print(f"d: {d.shape}\n{d}")
# c: (9,)
# [0 1 2 3 4 5 6 7 8]
# d: (9,)
# [0 1 2 3 4 5 6 7 8]