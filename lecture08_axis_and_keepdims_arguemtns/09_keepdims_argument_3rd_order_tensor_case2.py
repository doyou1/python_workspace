import numpy as np

a = np.arange(2*3*4).reshape((2, 3, 4))

sum_ = a.sum(axis=1)
sum_k = a.sum(axis=1, keepdims=True)

print("ndarray: {}\n{}".format(a.shape, a))
print("axis=1: {}\n{}".format(sum_.shape, sum_))
print("axis=1, keepdims=True: {}\n{}".format(sum_k.shape, sum_k))

# ndarray: (2, 3, 4)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]

#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

# axis=1: (2, 4)
# [[12 15 18 21]
#  [48 51 54 57]]

# axis=1, keepdims=True: (2, 1, 4)   
# [[[12 15 18 21]]

#  [[48 51 54 57]]]