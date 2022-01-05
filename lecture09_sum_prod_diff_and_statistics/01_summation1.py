import numpy as np

a = np.arange(5)
print("ndarray: ", a)
# ndarray:  [0 1 2 3 4]

cumsum = np.cumsum(a)
print("cumsum: ", cumsum)
# cumsum:  [ 0  1  3  6 10]