import numpy as np

a = np.arange(12).reshape((4,3))
print(f"ndarray: \n{a}\n")

print("a[1:, 0] : ", a[1:, 0])
print("a[:3, 1] : ", a[:3, 1])
print("a[1:3, 2] : ", a[1:3, 2])