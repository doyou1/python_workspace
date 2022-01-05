import numpy as np

u = np.random.randint(0, 10, (10, ))
v = np.random.randint(0, 10, (10, ))
print(f"u: {u.shape}\n{u}")
print(f"v: {v.shape}\n{v}")
# u: (10,)
# [0 8 4 7 4 3 9 2 1 3]
# v: (10,)
# [1 5 9 7 8 2 3 1 7 4]
maximum = np.maximum(u, v)
maximum_where = np.where(u > v, u, v)

print(f"maximum: {maximum.shape}\n{maximum}")
print(f"maximum(where): {maximum_where.shape}\n{maximum_where}")
# maximum: (10,)
# [1 8 9 7 8 3 9 2 7 4]
# maximum(where): (10,)
# [1 8 9 7 8 3 9 2 7 4]