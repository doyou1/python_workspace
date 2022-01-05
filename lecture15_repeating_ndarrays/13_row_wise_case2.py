import numpy as np

x = np.arange(4*3).reshape((4, 3))
print(f"x: {x.shape}\n{x}\n")
# x: (4, 3)
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]

y = x.sum(0, keepdims=True).repeat(3, 0).T
print(f"y: {y.shape}\n{y}\n")
# y: (3, 3)
# [[18 18 18]
#  [22 22 22]
#  [26 26 26]]

y = x.sum(1, keepdims=True).repeat(3, 0).T
print(f"y: {y.shape}\n{y}\n")
# y: (1, 12)
# [[ 3  3  3 12 12 12 