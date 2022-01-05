import numpy as np

x = np.arange(-2, 3)
y = np.arange(-2, 3)

print(f"x: {x}")
print(f"y: {y}")
# x: [-2 -1  0  1  2]
# y: [-2 -1  0  1  2]

X = x.reshape((1, -1)).repeat(y.shape[0], axis=0)
print(f"X: \n{X}")
# X:
# [[-2 -1  0  1  2]
#  [-2 -1  0  1  2]
#  [-2 -1  0  1  2]
#  [-2 -1  0  1  2]
#  [-2 -1  0  1  2]]

Y = y.reshape((-1, 1)).repeat(x.shape[0], axis=1)
print(f"Y: \n{Y}")
# Y:
# [[-2 -2 -2 -2 -2]
#  [-1 -1 -1 -1 -1]
#  [ 0  0  0  0  0]
#  [ 1  1  1  1  1]
#  [ 2  2  2  2  2]]

Z = np.square(X) + np.square(Y)
print(f"Z: \n{Z}")
# Z:
# [[8 5 4 5 8]
#  [5 2 1 2 5]
#  [4 1 0 1 4]
#  [5 2 1 2 5]
#  [8 5 4 5 8]]
