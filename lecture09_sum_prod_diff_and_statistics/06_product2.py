import numpy as np

a = np.arange(1, 1+12).reshape((3, 4))
print("ndarray: {}\n{}".format(a.shape, a))
# ndarray: (3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

prod = np.prod(a, axis=0)
cumprod = np.cumprod(a, axis=0)
print("prod(axis=0): {}\n{}".format(prod.shape, prod))
print("cumprod(axis=0): {}\n{}".format(cumprod.shape, cumprod))
# prod(axis=0): (4,)
# [ 45 120 231 384]

# cumprod(axis=0): (3, 4)
# [[  1   2   3   4]
#  [  5  12  21  32]
#  [ 45 120 231 384]]

prod = np.prod(a, axis=1)
cumprod = np.cumprod(a, axis=1)
print("prod(axis=1): {}\n{}".format(prod.shape, prod))
print("cumprod(axis=1): {}\n{}".format(cumprod.shape, cumprod))
# prod(axis=1): (3,)
# [   24  1680 11880]

# cumprod(axis=1): (3, 4)
# [[    1     2     6    24]
#  [    5    30   210  1680]
#  [    9    90   990 11880]]