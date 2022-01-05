import numpy as np

a = np.arange(3*3*3).reshape((3,3,3))
print(f"ndarray: \n{a}\n")

print("a[0] : \n", a[0])

print("a[1] : \n", a[1])

print("a[2] : \n", a[2])

print("a[0, 0] : \n", a[0, 0])
print("a[0, 1] : \n", a[0, 1])
print("a[0, 2] : \n", a[0, 2], '\n')

print("a[1, 0] : \n", a[1, 0])
print("a[1, 1] : \n", a[1, 1])
print("a[1, 2] : \n", a[1, 2], '\n')

print("a[2, 0] : \n", a[2, 0])
print("a[2, 1] : \n", a[2, 1])
print("a[2, 2] : \n", a[2, 2], '\n')