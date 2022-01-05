import numpy as np

x = np.arange(4*3).reshape((4, 3))
print(f"x: {x.shape}\n{x}\n")
# x: (4, 3)
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]

y = x.sum(1, keepdims=True).repeat(2, 1).T
print(f"y: {y.shape}\n{y}\n")
# y: (2, 4)
# [[ 3 12 21 30]
#  [ 3 12 21 30]]