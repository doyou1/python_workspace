import numpy as np

a = np.random.normal(size=(100, 200))

b = a.reshape((1, *a.shape))
c = a.reshape((*a.shape, 1))

print(f"a.shape: {a.shape}\n")

print(f"b.shape: {b.shape}")
print(f"c.shape: {c.shape}")