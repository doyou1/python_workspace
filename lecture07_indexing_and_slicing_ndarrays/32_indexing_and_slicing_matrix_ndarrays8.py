import numpy as np

a = np.random.randint(0, 20, (10, ))
print(f"ndarray: \n{a}\n")

b_indices = (a % 2 == 0)
print(f"b_indices: \n{b_indices}\n")

print(f"a[b_indices]: \n{a[b_indices]}")