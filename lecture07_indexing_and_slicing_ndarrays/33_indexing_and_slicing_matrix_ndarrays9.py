import numpy as np

a = np.random.randint(0, 20, (2,2))
print(f"ndarray: \n{a}")

b_indices = np.array([[True,False], [False, True]])
print(f"b_indices: \n{b_indices}\n")

print(f"a[b_indices]: \n{a[b_indices]}")