import numpy as np

x = np.arange(-2, 3)
y = np.arange(-2, 3)

X, Y = np.meshgrid(x, y)
print(f"X: \n{X}")
print(f"Y: \n{Y}")
# X: 
# [[-2 -1  0  1  2]
#  [-2 -1  0  1  2]
#  [-2 -1  0  1  2]
#  [-2 -1  0  1  2]
#  [-2 -1  0  1  2]]
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