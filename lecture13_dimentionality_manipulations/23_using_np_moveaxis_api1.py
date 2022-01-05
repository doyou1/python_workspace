import numpy as np

a = np.random.normal(size=(3, 4, 5, 6))

b = np.moveaxis(a, source=0, destination=1)
c = np.moveaxis(a, source=0, destination=2)
d = np.moveaxis(a, source=0, destination=-1)

print(f"a.shape: {a.shape}\n")
# a.shape: (3, 4, 5, 6)

# np.moveaxis()
# source=n, destination=m   
# n번째 차원을 m차원으로 옮기고, 
# 나머지는 왼쪽으로 옮김
print(f"b.shape: {b.shape}")
print(f"c.shape: {c.shape}")
print(f"d.shape: {d.shape}")
# b.shape: (4, 3, 5, 6)
# c.shape: (4, 5, 3, 6)
# d.shape: (4, 5, 6, 3)