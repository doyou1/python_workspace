import numpy as np

a = np.random.randint(0, 20, (3,4))
print(f"ndarray: \n{a}")

b_indices = (a > 10)
print(f"b_indices: \n{b_indices}")

print(f"a[b_indices]: \n{a[b_indices]}")