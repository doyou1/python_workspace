import numpy as np

a = np.arange(2*3*4).reshape((2, 3, 4))

sum_ = a.sum(axis=2)
sum_k = a.sum(axis=2, keepdims=True)

print("ndarray: {}\n{}".format(a.shape, a))
print("axis=2: {}\n{}".format(sum_.shape, sum_))
print("axis=2, keepdims=Ture: {}\n{}".format(sum_k.shape, sum_k))

# ndarray: (2, 3, 4)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]

#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

# axis=2: (2, 3)
# [[ 6 22 38]
#  [54 70 86]]

# axis=2, keepdims=Ture: (2, 3, 1)   
# [[[ 6]
#   [22]
#   [38]]

#  [[54]
#   [70]
#   [86]]]