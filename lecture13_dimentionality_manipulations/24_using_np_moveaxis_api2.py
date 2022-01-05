import numpy as np

a = np.random.normal(size=(3, 4, 5, 6))

b = np.moveaxis(a, source=1, destination=0)
c = np.moveaxis(a, source=1, destination=2)
d = np.moveaxis(a, source=1, destination=-1)

print(f"a.shape: {a.shape}\n")
# a.shape: (3, 4, 5, 6)

print(f"b.shape: {b.shape}")
print(f"c.shape: {c.shape}")
print(f"d.shape: {d.shape}")
# b.shape: (4, 3, 5, 6)
# c.shape: (3, 5, 4, 6)
# d.shape: (3, 5, 6, 4)