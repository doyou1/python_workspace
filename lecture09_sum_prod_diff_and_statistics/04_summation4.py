import numpy as np

a = np.arange(3*4).reshape((3,4))
print("ndarray: {}\n{}".format(a.shape, a))
# ndarray: (3, 4)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

cumsum = np.cumsum(a, axis=0)
print("cumsum: {}\n{}".format(cumsum.shape, cumsum))
# cumsum: (3, 4)
# [[ 0  1  2  3]
#  [ 4  6  8 10]
#  [12 15 18 21]]

cumsum = np.cumsum(a, axis=1)
print("cumsum: {}\n{}".format(cumsum.shape, cumsum))
# cumsum: (3, 4)
# [[ 0  1  3  6]
#  [ 4  9 15 22]
#  [ 8 17 27 38]]