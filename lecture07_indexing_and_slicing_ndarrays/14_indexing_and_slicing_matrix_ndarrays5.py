import numpy as np

a = np.arange(12).reshape((3,4))
print(f"ndarray: \n{a}\n")

print("a[0, 1:]", a[0, 1:])
print("a[1, :3]", a[1, :3])
print("a[2, 1:3]", a[2, 1:3])