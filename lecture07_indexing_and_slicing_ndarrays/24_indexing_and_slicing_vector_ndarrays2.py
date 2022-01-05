import numpy as np

a = np.random.randint(0, 20, (10, ))
print(f"ndarray: \n{a}\n")

indices = np.random.randint(0, 10, size=(2,3,4))
print(f"indices: \n{indices}\n")

print(f"a[indices]: {a[indices].shape}\n{a[indices]}")