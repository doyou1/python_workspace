import numpy as np

u = np.random.randint(0, 10, (10, ))
v = np.random.randint(0, 10, (10, ))
print(f"u: {u.shape}\n{u}")
print(f"v: {v.shape}\n{v}\n")

minimum = np.minimum(u, v)

minimum_where1 = np.where(u > v, v, u)
minimum_where2 = np.where(u < v, u, v)

print(f"minimum: {minimum.shape}\n{minimum}")
print(f"minimum(where)1: {minimum_where1.shape}\n{minimum_where1}")
print(f"minimum(where)2: {minimum_where2.shape}\n{minimum_where2}")
# u: (10,)
# [5 9 8 7 0 1 0 7 8 2]
# v: (10,)
# [8 1 5 5 9 0 4 2 2 3]

# minimum: (10,)
# [5 1 5 5 0 0 0 2 2 2]
# minimum(where)1: (10,)
# [5 1 5 5 0 0 0 2 2 2]
# minimum(where)2: (10,)
# [5 1 5 5 0 0 0 2 2 2]