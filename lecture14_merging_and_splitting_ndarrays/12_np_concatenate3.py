import numpy as np

a = np.random.randint(0, 10, (1, 3))
b = np.random.randint(0, 10, (1, 3))

axis0 = np.concatenate([a, b], axis=0)
axis1 = np.concatenate([a, b], axis=1)
axis_n1 = np.concatenate([a, b], axis=-1)

print(f"a: {a.shape}\n{a}")
print(f"b: {b.shape}\n{b}\n")
# a: (1, 3)
# [[6 6 3]]
# b: (1, 3)
# [[7 0 1]]

print(f"axis0: {axis0.shape}\n{axis0}")
print(f"axis1: {axis1.shape}\n{axis1}")
print(f"axis_n1: {axis_n1.shape}\n{axis_n1}")
# axis0: (2, 3)
# [[6 6 3]
#  [7 0 1]]
# axis1: (1, 6)
# [[6 6 3 7 0 1]]
# axis_n1: (1, 6)
# [[6 6 3 7 0 1]]