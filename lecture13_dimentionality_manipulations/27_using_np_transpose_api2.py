import numpy as np

a = np.random.normal(size=(3, 4, 5, 6, 7))

b = np.transpose(a)
c = a.T

print(f"a.shape: {a.shape}\n")
# a.shape: (3, 4, 5, 6, 7)

print(f"b.shape: {b.shape}")
print(f"c.shape: {c.shape}")
# b.shape: (7, 6, 5, 4, 3)
# c.shape: (7, 6, 5, 4, 3)