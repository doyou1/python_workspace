import numpy as np

a = np.arange(12).reshape((3,4))
print(f"ndarray: \n{a}\n")

indices = np.array([0, 0, 1, 1, 2, 2])
print(f"indices: \n{indices}")

print(f"a[indices: \n{a[indices]}")