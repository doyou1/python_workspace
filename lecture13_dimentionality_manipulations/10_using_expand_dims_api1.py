import numpy as np

a = np.arange(9)

b = np.expand_dims(a, axis=0)
c = np.expand_dims(a, axis=1)

print(f"a.shape: {a.shape}\n")
# a.shape: (9,)

print(f"b.shape: {b.shape}")
print(f"c.shape: {c.shape}")
# b.shape: (1, 9)
# c.shape: (9, 1)