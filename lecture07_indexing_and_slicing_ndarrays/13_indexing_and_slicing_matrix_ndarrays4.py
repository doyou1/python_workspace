import numpy as np

a = np.arange(9).reshape((3,3))
print(f"ndarray: \n{a}\n")

print(a[0,0], a[0,1], a[0,2])
print(a[1,0], a[1,1], a[1,2])
print(a[2,0], a[2,1], a[2,2])