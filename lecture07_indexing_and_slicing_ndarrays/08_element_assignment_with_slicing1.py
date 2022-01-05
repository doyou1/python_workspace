import numpy as np

a = list(range(1, 11))
print(a)
for data_idx in range(5):
    a[data_idx] = 0
print(a)

a = np.arange(1, 11)
print(a)
a[:5] = 0
print(a)