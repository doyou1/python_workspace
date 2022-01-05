import numpy as np

x = np.arange(5)    #(5, )
y = np.arange(2, 6) #(4, )

X, Y = np.meshgrid(x, y)    # (4, 5) (4, 5)
Z = X + Y

X_T, Y_T, Z_T = X.T, Y.T, Z.T

print(f"x: \n{x}")
print(f"y: \n{y}\n")

print(f"X: \n{X}")
print(f"Y: \n{Y}")
print(f"Z: \n{Z}\n")

print(f"X.T: \n{X_T}")
print(f"Y.T: \n{Y_T}")
print(f"Z.T: \n{Z_T}")
