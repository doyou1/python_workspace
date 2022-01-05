import numpy as np

a = np.ones(shape=(1, 1, 4, 1, 3, 1))

b = np.squeeze(a)
c = a.squeeze()

print(f"a.shape: {a.shape}\n")
# a.shape: (1, 1, 4, 1, 3, 1)

print(f"b.shape: {b.shape}")
print(f"c.shape: {c.shape}")
# b.shape: (4, 3)
# c.shape: (4, 3)