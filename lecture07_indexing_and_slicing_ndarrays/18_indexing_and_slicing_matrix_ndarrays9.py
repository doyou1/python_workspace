import numpy as np

a = np.arange(16).reshape((4,4))
print(f"ndarray: \n{a}\n")

print("a[0, :] : \n", a[0, :])

print("a[0, ...] : \n", a[0, ...])

print("a[:, 1] : \n", a[:, 1])

print("a[..., 1] : \n", a[..., 1])