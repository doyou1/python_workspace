import numpy as np

a = np.arange(16).reshape((4,4))

print(f"ndarray: \n{a}\n")

print("a[1:3, 1:3]: \n", a[1:3, 1:3])
print("a[:2, :3] : \n", a[:2, :3])
print("a[1:, 2:] : \n", a[1:, 2:])
print("a[2:, :-2] : \n", a[2:, :-2])
# print(a[-2:, :-2])