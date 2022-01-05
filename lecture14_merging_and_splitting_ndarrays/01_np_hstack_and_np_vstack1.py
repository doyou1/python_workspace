import numpy as np

a = np.random.randint(0, 10, (4, ))
b = np.random.randint(0, 10, (4, ))

print(f"a: {a.shape}\n{a}")
print(f"b: {b.shape}\n{b}")
# a: (4,)
# [7 1 4 6]
# b: (4,)
# [3 0 2 5]

vstack = np.vstack([a, b])
hstack = np.hstack([a, b])

print(f"vstack: {vstack.shape}\n {vstack}")
print(f"hstack: {hstack.shape}\n {hstack}")
# vstack: (2, 4)
#  [[7 1 4 6]
#  [3 0 2 5]]
# hstack: (8,)
#  [7 1 4 6 3 0 2 5]