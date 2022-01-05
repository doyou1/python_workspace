import numpy as np

u = np.random.randint(0, 10, (10, ))
v = np.random.randint(0, 10, (10, ))
print(f"u: {u.shape}\n{u}")
print(f"v: {v.shape}\n{v}\n")
# u: (10,)
# [8 1 5 9 2 7 0 4 7 5]
# v: (10,)
# [0 7 6 4 9 2 3 4 9 2]

maximum = np.zeros_like(u)
maximum[u >= v] = u[u >= v]
maximum[u < v] = v[u < v]

print(f"np.maximum: \n{np.maximum(u, v)}")
print(f"maximum: \n{maximum}")
# np.maximum:
# [8 7 6 9 9 7 3 4 9 5]
# maximum:
# [8 7 6 9 9 7 3 4 9 5]