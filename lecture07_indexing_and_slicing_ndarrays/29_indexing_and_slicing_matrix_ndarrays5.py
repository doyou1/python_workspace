import numpy as np

a = np.arange(12).reshape((3,4))
print(f"ndarray: \n{a}\n")

indices0, indices1 = np.array([0]), np.array([0])
print(a[indices0, indices1])

indices0, indices1 = np.array([1]), np.array([2])
print(a[indices0, indices1])

indices0, indices1 = np.array([-1]), np.array([0])
print(a[indices0, indices1])

indices0, indices1 = np.array([-1]), np.array([-1])
print(a[indices0, indices1])