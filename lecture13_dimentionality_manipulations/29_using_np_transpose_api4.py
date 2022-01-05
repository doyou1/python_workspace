import numpy as np

a = np.random.normal(size=(3, 4, 5, 6))

b = np.transpose(a, axes=tuple(range(a.ndim))[::-1])

print(tuple(range(a.ndim))[::-1])
# (3, 2, 1, 0)

print(f"a.shape: {a.shape}\n")
# a.shape: (3, 4, 5, 6)

print(f"b.shape: {b.shape}")
# b.shape: (6, 5, 4, 3)

