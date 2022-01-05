import numpy as np

u = np.random.randint(0, 10, (10, ))
v = np.random.randint(0, 10, (10, ))
print(f"u: {u.shape}\n{u}")
print(f"v: {v.shape}\n{v}")
# u: (10,)
# [5 9 6 4 7 7 2 7 9 1]
# v: (10,)
# [1 2 4 1 5 2 0 9 2 5]

up_vals = np.full_like(u, fill_value=100)
down_vals = np.full_like(u, fill_value=-100)

print(np.where(u > v, up_vals, down_vals))
# [ 100  100  100  100  100  100  100 -100  100 -100]