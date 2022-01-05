import numpy as np

a = np.arange(2*3*4).reshape((2, 3, 4))

sum_ = a.sum(axis=0)

print("ndarray: {}\n{}".format(a.shape, a))
print("ndaaray.sum(axis=0): {}\n{}".format(sum_.shape, sum_))

# ndarray: (2, 3, 4)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]

#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

# ndaaray.sum(axis=0): (3, 4)        
# [[12 14 16 18]
#  [20 22 24 26]
#  [28 30 32 34]]