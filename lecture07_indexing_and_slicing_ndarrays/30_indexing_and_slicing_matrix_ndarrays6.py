import numpy as np

a = np.arange(12).reshape((3,4))
print(f"ndarray: \n{a}\n")

indices0, indices1 = np.array([0,1,2]), np.array([1,2,3])

print("Paired indices")
for idx0, idx1 in zip(indices0, indices1):
    print(f"{idx0}, {idx1}")

print(f"a[indices0, indices1]: \n{a[indices0, indices1]}")