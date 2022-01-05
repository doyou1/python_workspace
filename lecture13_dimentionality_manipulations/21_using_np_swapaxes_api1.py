import numpy as np

a = np.random.normal(size=(3, 4, 5, 6))

# np.swapaxes(arg1, arg2, arg3)
# arg1 : 해당 nparray
# arg2,arg3 : 서로 바꿀 차원 idx
b = np.swapaxes(a, 0, 1)
c = np.swapaxes(a, 0, 2)
d = np.swapaxes(a, 0, 3)

print(f"a.shape: {a.shape}\n")
# a.shape: (3, 4, 5, 6)

print(f"b.shape: {b.shape}")
print(f"c.shape: {c.shape}")
print(f"d.shape: {d.shape}")
# b.shape: (4, 3, 5, 6)
# c.shape: (5, 4, 3, 6)
# d.shape: (6, 4, 5, 3)