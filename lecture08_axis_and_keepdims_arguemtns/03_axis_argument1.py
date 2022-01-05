import numpy as np

a = np.arange(12).reshape((3,-1))

sum_ = a.sum(axis=0)

print("ndarray: {}\n{}".format(a.shape, a))
print("ndarray.sum(axis=0): {}\n{}".format(sum_.shape, sum_))

# ndarray: (3, 4)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
# ndarray.sum(axis=0): (4,)
# [12 15 18 21]