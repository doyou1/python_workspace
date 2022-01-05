import numpy as np

a = np.arange(5)
print(f"ndarray: \n{a}")

b_indices = np.array([True,False,True,False,True])
print(f"b_indices: \n{b_indices}\n")

print(f"a[b_indices]: \n", a[b_indices])