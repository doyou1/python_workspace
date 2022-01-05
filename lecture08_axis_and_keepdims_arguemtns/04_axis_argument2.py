import numpy as np

a = np.arange(12).reshape((3, -1))

sum_ = a.sum(axis=1)

print("ndarray: {}\n{}".format(a.shape, a))
print("ndarray.sum(axis=1): {}\n{}".format(sum_.shape, sum_))

# ndarray: (3, 4)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
# ndarray.sum(axis=1): (3,)
# [ 6 22 38]


a = np.arange(12).reshape((3, 2, -1))
print(a)
# [[[ 0  1]
#   [ 2  3]]

#  [[ 4  5]
#   [ 6  7]]

#  [[ 8  9]
#   [10 11]]]

sum_ = a.sum(axis=2)
print(sum_)
# [[ 1  5]
#  [ 9 13]]

# [
#   [ 0+1 2+3 ]
#   [ 4+5 6+7 ]
#   [ 8+9 10+11]
#               ]