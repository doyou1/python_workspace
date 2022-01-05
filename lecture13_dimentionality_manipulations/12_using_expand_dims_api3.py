import numpy as np

a = np.arange(9).reshape((3, 3))

b = np.expand_dims(a, axis=0)
c = np.expand_dims(a, axis=1)
d = np.expand_dims(a, axis=-1)
e = np.expand_dims(a, axis=(0, -1))

print(f"a.shape: {a.shape}\n")
# a.shape: (3, 3)

print(f"b.shape: {b.shape}")
print(f"c.shape: {c.shape}")
print(f"d.shape: {d.shape}")
print(f"e.shape: {e.shape}")
# b.shape: (1, 3, 3)
# c.shape: (3, 1, 3)
# d.shape: (3, 3, 1)
# e.shape: (1, 3, 3, 1)