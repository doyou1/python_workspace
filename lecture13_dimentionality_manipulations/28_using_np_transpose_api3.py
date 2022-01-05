import numpy as np

a = np.random.normal(size=(3, 4, 5))

b = np.transpose(a, axes=(0, 1, 2))
c = np.transpose(a, axes=(1, 2, 0))
d = np.transpose(a, axes=(2, 0, 1))
e = np.transpose(a, axes=(2, 1, 0))

print(f"a.shape: {a.shape}\n")
# a.shape: (3, 4, 5)

print(f"b.shape: {b.shape}")
print(f"c.shape: {c.shape}")
print(f"d.shape: {d.shape}")
print(f"e.shape: {e.shape}")
# b.shape: (3, 4, 5)
# c.shape: (4, 5, 3)
# d.shape: (5, 3, 4)
# e.shape: (5, 4, 3)