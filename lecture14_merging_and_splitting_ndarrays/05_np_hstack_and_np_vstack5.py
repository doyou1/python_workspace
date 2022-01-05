import numpy as np

a = np.random.randint(0, 10, (3, 4))
b = np.random.randint(0, 10, (3, ))

print(f"a: {a.shape}\n{a}")
print(f"b: {b.shape}\n{b}\n")
# a: (3, 4)
# [[6 4 7 8]
#  [9 4 5 0]
#  [7 1 4 8]]
# b: (3,)
# [9 6 7]

# hstack = np.hstack([a, b])  # error
hstack = np.hstack([a, b.reshape(-1, 1)])

print(f"hstack: {hstack.shape}\n{hstack}")
# hstack: (3, 5)
# [[6 4 7 8 9]
#  [9 4 5 0 6]
#  [7 1 4 8 7]]