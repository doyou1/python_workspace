import numpy as np

a = np.random.randint(0, 10, (3, ))
b = np.random.randint(0, 10, (4, ))

concat = np.concatenate([a, b])
concat0 = np.concatenate([a, b], axis=0)

print(f"a: {a.shape}\n {a}")
print(f"b: {b.shape}\n {b}\n")
# a: (3,)
#  [4 2 8]
# b: (4,)
#  [2 7 9 3]

print(f"concat.shape: {concat.shape}\n {concat}")
print(f"concat0.shape: {concat0.shape}\n {concat0}")
# concat.shape: (7,)
#  [4 2 8 2 7 9 3]
# concat0.shape: (7,)
#  [4 2 8 2 7 9 3]