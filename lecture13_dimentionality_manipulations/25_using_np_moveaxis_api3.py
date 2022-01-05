import numpy as np

a = np.random.normal(size=(3, 4, 5, 6))

b = np.moveaxis(a, source=0, destination=-1)
c = np.moveaxis(b, source=-2, destination=0)

print(f"a.shape: {a.shape}\n")
# a.shape: (3, 4, 5, 6)

print(f"b.shape: {b.shape}")
print(f"c.shape: {c.shape}")
# b.shape: (4, 5, 6, 3)
# c.shape: (6, 4, 5, 3)