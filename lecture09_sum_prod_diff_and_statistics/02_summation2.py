import numpy as np

a = np.arange(3*3).reshape((3, 3))
print("ndarray: {}\n{}".format(a.shape, a))
# ndarray: (3, 3)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

cumsum = np.cumsum(a)
print("cumsum: {}\n{}".format(cumsum.shape, cumsum))
# cumsum: (9,)
# [ 0  1  3  6 10 15 21 28 36]