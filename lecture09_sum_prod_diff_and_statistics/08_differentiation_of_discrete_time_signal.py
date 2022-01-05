import numpy as np

np.random.seed(0)
a = np.random.randint(0, 10, (4, 4))
print("ndaaray: {}\n{}".format(a.shape, a))
# ndaaray: (4, 4)
# [[5 0 3 3]
#  [7 9 3 5]
#  [2 4 7 6]
#  [8 8 1 6]]

diff = np.diff(a, axis=0)
print("diff: {}\n{}".format(diff.shape, diff))
# diff: (3, 4)
# [[ 2  9  0  2]
#  [-5 -5  4  1]
#  [ 6  4 -6  0]]

diff = np.diff(a, axis=1)
print("diff: {}\n{}".format(diff.shape, diff))
# diff: (4, 3)
# [[-5  3  0]
#  [ 2 -6  2]
#  [ 2  3 -1]
#  [ 0 -7  5]]