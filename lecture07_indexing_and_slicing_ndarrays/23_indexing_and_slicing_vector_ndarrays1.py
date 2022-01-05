import numpy as np

a = np.arange(10)
print(f"ndarray: \n{a}\n")

indices = np.array([0, 3, 4])
print(a[indices])

indices = np.array([0, 0, 5, 5])
print(a[indices])

indices = np.array([[1,2,3], [5,8,9]])
print(f"indices: \n{indices}")
print(f"a[indices] : {a[indices].shape}\n{a[indices]}")