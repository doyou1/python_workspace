import numpy as np

a = np.random.randint(0, 10, (1, 3))
b = np.random.randint(0, 10, (1, 3))

print(f"a: {a.shape}\n{a}")
print(f"b: {b.shape}\n{b}")
# a: (1, 3)
# [[5 9 2]]
# b: (1, 3)
# [[6 6 3]]

vstack = np.vstack([a, b])
hstack = np.hstack([a, b])

print(f"vstack: {vstack.shape}\n {vstack}")
print(f"hstack: {hstack.shape}\n {hstack}")
# vstack: (2, 3)
#  [[5 9 2]
#  [6 6 3]]
# hstack: (1, 6)
#  [[5 9 2 6 6 3]]