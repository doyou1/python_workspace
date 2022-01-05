import numpy as np
np.set_printoptions(sign='+')

x = np.random.uniform(-5, 5, (4, 2))
y = np.random.uniform(-5, 5, (3, 2))

X = np.expand_dims(x, axis=1)
Y = np.expand_dims(y, axis=0)
Z = X + Y

print(f"X[0] + Y: \n{Z[0, :, :]}")

print(f"X[3] + Y: \n{Z[3, :, :]}")

print(f"Y[0] + X: \n{Z[:, 0, :]}")

print(f"Y[2] + X: \n{Z[:, 2, :]}")
