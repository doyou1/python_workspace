import numpy as np

a = np.arange(9)

b = a[np.newaxis, np.newaxis, :]
c = a[np.newaxis, :, np.newaxis]
d = a[:, np.newaxis, np.newaxis]

print(f"a.shape: {a.shape}\n")

print(f"b.shape: {b.shape}")
print(f"c.shape: {c.shape}")
print(f"d.shape: {d.shape}")