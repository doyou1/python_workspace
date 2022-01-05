import numpy as np

x = np.arange(5)
y = np.arange(2, 6)

X = x.reshape((-1, 1))
Y = y.reshape((1, -1))
Z = X + Y

print(f"X: {X.shape}\n{X}")
print(f"Y: {Y.shape}\n{Y}")
print(f"Z: {Z.shape}\n{Z}")