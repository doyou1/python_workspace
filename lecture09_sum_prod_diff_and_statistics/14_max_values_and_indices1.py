import numpy as np

a = np.random.randint(0, 100, (10, ))

M = np.max(a)
M_idx = np.argmax(a)

print(f"ndarray: \n{a}")
print(f"M/M_idx: {M}/{M_idx}")