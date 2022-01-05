import numpy as np

a = np.arange(3*3*3).reshape((3,3,3))
print(f"ndarray: \n{a}\n")

print("a[0, :2, :2] : \n", a[0, :2, :2])
print("a[1, :2, :] : \n", a[1, :2, :])
print("a[2, -2:, -2:] : \n", a[2, -2:, -2:])
