import numpy as np

a = np.random.normal(size=(100, 200))

b = a[np.newaxis, ...]
c = a[..., np.newaxis]

print(f"a.shape: {a.shape}\n")
# a.shape: (100, 200)

print(f"b.shape: {b.shape}")
print(f"c.shape: {c.shape}")
# b.shape: (1, 100, 200)
# c.shape: (100, 200, 1)