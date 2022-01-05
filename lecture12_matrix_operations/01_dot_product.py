import numpy as np

u = np.random.uniform(0, 5, (4, ))
v = np.random.uniform(0, 5, (4, ))

sum_hadamard = np.sum(u*v)
np_dot = np.dot(u, v)

# ∑ui*vi
# sum_hadamard: 29.25
# np_dot: 29.25
print(f"sum_hadamard: {sum_hadamard.round(2)}")
print(f"np_dot: {np_dot.round(2)}")