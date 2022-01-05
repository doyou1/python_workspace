import numpy as np

a = np.ones(shape=(10, 1))

b = a.reshape((10, ))
c = a.reshape((-1, ))
d = a.flatten()

print(f"a.shape: {a.shape}\n")
# a.shape: (10, 1)

print(f"b.shape: {b.shape}")
print(f"c.shape: {c.shape}")
print(f"d.shape: {d.shape}")
# b.shape: (10,)
# c.shape: (10,)
# d.shape: (10,)