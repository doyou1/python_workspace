import numpy as np

a = np.arange(2*3*4).reshape((2, 3, 4))
print("ndarray: {}\n{}".format(a.shape, a))
# ndarray: (2, 3, 4)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]

#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

cumsum = np.cumsum(a)
print("cumsum: {}\n{}".format(cumsum.shape, cumsum))
# cumsum: (24,)
# [  0   1   3   6  10  15  21  28  36 
#  45  55  66  78  91 105 120 136 153  
#  171 190 210 231 253 276]