import numpy as np

a = np.random.randint(0, 10, (3, 4))
b = np.random.randint(0, 10, (4, ))

print(f"a: {a.shape}\n{a}")
print(f"b: {b.shape}\n{b}")
# a: (3, 4)
# [[1 8 8 7]
#  [4 3 8 8]
#  [0 3 3 4]]
# b: (4,)
# [8 4 9 0]

vstack = np.vstack([a, b])
# hstack = np.hstack([a, b])  # error
# hstack1 = np.hstack([a, b.reshape(-1,1)])   # error
# hstack2 = np.hstack([a, b.reshape(1,-1)])   # error

print(f"vstack: {vstack.shape}\n {vstack}")
# vstack: (4, 4)
#  [[1 8 8 7]
#  [4 3 8 8]
#  [0 3 3 4]
#  [8 4 9 0]]