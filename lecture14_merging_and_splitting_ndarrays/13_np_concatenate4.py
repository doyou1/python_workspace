import numpy as np

a = np.random.randint(0, 10, (3, 4))
b = np.random.randint(0, 10, (3, 2))

concat = np.concatenate([a, b], axis=1)

print(f"a: {a.shape}\n{a}")
print(f"b: {b.shape}\n{b}")
# a: (3, 4)
# [[7 2 7 7]
#  [4 1 2 4]
#  [0 2 3 2]]
# b: (3, 2)
# [[2 8]
#  [2 0]
#  [8 5]]

print(f"concat: {concat.shape}\n{concat}")
# concat: (3, 6)
# [[7 2 7 7 2 8]
#  [4 1 2 4 2 0]
#  [0 2 3 2 8 5]]