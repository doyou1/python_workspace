import numpy as np

a = np.arange(9)

b = np.expand_dims(a, axis=(0, 1))
c = np.expand_dims(a, axis=(0, 2))
d = np.expand_dims(a, axis=(1, 2))

print(f"a.shape: {a.shape}\n")
# a.shape: (9,)

print(f"b.shape: {b.shape}")
print(f"c.shape: {c.shape}")
print(f"d.shape: {d.shape}")
# b.shape: (1, 1, 9)
# c.shape: (1, 9, 1)
# d.shape: (9, 1, 1)