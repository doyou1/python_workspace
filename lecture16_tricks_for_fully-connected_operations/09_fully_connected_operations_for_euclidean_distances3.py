import numpy as np

x = np.random.uniform(-5, 5, (4, 3))
y = np.random.uniform(-5, 5, (3, 3))

X = np.expand_dims(x, axis=1)
Y = np.expand_dims(y, axis=0)

L2 = np.sqrt(np.sum(np.square(X - Y), axis=-1))
print(L2.shape) # (4, 3)