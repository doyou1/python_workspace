import numpy as np

a = np.arange(12).reshape((3,4))
print(f"ndarray: \n{a}\n")

indices = np.array([[0,1,2], [-3,-2,-1]])
print(f"indices: \n{indices}")

print(f"a[indices]: \n{a[indices]}")