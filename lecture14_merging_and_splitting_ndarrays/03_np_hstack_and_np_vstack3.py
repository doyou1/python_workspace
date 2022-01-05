import numpy as np

a = np.random.randint(0, 10, (3, 1))
b = np.random.randint(0, 10, (3, 1))

print(f"a: {a.shape}\n{a}")
print(f"b: {b.shape}\n{b}")
# a: (3, 1)
# [[2]
#  [8]
#  [6]]
# b: (3, 1)
# [[7]
#  [9]
#  [5]]

vstack = np.vstack([a, b])
hstack = np.hstack([a, b])

print(f"vstack: {vstack.shape}\n {vstack}")
print(f"hstack: {hstack.shape}\n {hstack}")
# vstack: (6, 1)
#  [[2]
#  [8]
#  [6]
#  [7]
#  [9]
#  [5]]
# hstack: (3, 2)
#  [[2 7]
#  [8 9]
#  [6 5]]