import numpy as np

u = np.random.randint(0, 10, (10, ))
v = np.random.randint(0, 10, (10, ))

print(f"u: {u.shape}\n{u}")
print(f"v: {v.shape}\n{v}")
# u: (10,)
# [8 8 4 5 7 3 2 3 2 4]
# v: (10,)
# [1 3 9 1 7 9 8 2 7 0]

maximum = np.maximum(u, v)
minimum = np.minimum(u, v)

print(f"maximum: {maximum.shape}\n{maximum}")
print(f"minimum: {minimum.shape}\n{minimum}")
# maximum: (10,)
# [8 8 9 5 7 9 8 3 7 4]
# minimum: (10,)
# [1 3 4 1 7 3 2 2 2 0]