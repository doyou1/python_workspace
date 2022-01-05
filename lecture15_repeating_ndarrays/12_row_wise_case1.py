import numpy as np

x = np.arange(4*3).reshape((4, 3))
print(f"x: {x.shape}\n{x}\n")
# x: (4, 3)
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]

x = x.sum(axis=0, keepdims=True)
print(f"x.sum: {x.shape}\n{x}\n")
# x.sum: (1, 3)
# [[18 22 26]]
x = x.repeat(repeats=3, axis=0)
print(f"x.repeat: {x.shape} \n{x}\n")
# x.repeat: (3, 3)
# [[18 22 26]
#  [18 22 26]
#  [18 22 26]]

x = x.T
print(f"x.: {x.shape}\n{x}\n")
# x.: (3, 3)
# [[18 18 18]
#  [22 22 22]
#  [26 26 26]]

x = x.T
print(f"x.: {x.shape}\n{x}\n")
# x.: (3, 3)
# [[18 22 26]
#  [18 22 26]
#  [18 22 26]]