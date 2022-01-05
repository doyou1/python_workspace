import numpy as np

a = np.ones(shape=(1, 3, 4))
b = np.ones(shape=(3, 4, 1))

c = a.reshape(*a.shape[1:]) # 1번째부터
d = b.reshape(*b.shape[:-1]) # 1번째부터

print(f"a.shape: {a.shape}")
print(f"b.shape: {b.shape}\n")
# a.shape: (1, 3, 4)
# b.shape: (3, 4, 1)

print(f"c.shape: {c.shape}")
print(f"d.shape: {d.shape}")
# c.shape: (3, 4)
# d.shape: (3, 4)