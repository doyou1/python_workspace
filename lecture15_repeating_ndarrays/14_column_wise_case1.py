import numpy as np

x = np.arange(4*3).reshape((4, 3))
print(f"x: {x.shape}\n{x}\n")
# x: (4, 3)
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]

x = x.sum(axis=1, keepdims=True)
print(f"x.sum: {x.shape}\n{x}\n")
# x.sum: (4, 1)
# [[ 3]
#  [12]
#  [21]
#  [30]]

x = x.repeat(repeats=2, axis=1)
print(f"x.repeat: {x.shape}\n{x}\n")
# x.repeat: (4, 2)
# [[ 3  3]
#  [12 12]
#  [21 21]
#  [30 30]]

x = x.T
print(f"x.T: {x.shape}\n{x}\n")
# x.T: (2, 4)
# [[ 3 12 21 30]
#  [ 3 12 21 30]]