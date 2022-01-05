import numpy as np

a = np.random.randint(0, 10, (3, ))
b = np.random.randint(0, 10, (4, ))
c = np.random.randint(0, 10, (5, ))

concat = np.concatenate([a, b, c], axis=0)

print(f"a: {a.shape}\n {a}")
print(f"b: {b.shape}\n {b}")
print(f"c: {c.shape}\n {c}\n")
# a: (3,)
#  [7 2 2]
# b: (4,)
#  [3 0 4 6]
# c: (5,)
#  [7 4 5 3 8]

print(f"concat.shape: {concat.shape}\n{concat}")
# concat.shape: (12,)
# [7 2 2 3 0 4 6 7 4 5 3 8]