import numpy as np

a = np.random.randint(0, 10, (5, ))
print("ndarray: {}\n{}".format(a.shape, a))
# ndarray: (5,)
# [3 9 5 0 4]

diff = np.diff(a)   # diff[n] = a[n+1] - a[n]
print("diff: {}\n{}".format(diff.shape, diff))
# diff: (4,)
# [ 6 -4 -5  4]