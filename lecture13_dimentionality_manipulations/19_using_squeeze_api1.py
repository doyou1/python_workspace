import numpy as np

a = np.ones(shape=(1, 3, 4))

b = np.squeeze(a)
c = a.squeeze()

print(f"a: {a.shape}\n{a}\n")
# a: (1, 3, 4)
# [[[1. 1. 1. 1.]
#   [1. 1. 1. 1.]
#   [1. 1. 1. 1.]]]

print(f"b: {b.shape}\n{b}")
print(f"c: {c.shape}\n{c}")
# b: (3, 4)
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]]
# c: (3, 4)
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]]