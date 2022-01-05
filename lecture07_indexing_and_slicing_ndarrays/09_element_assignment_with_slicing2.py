import numpy as np

a = np.arange(1, 11)
print(a)

a[::2] = 200
print(a)

a[5:-1:3] = 300
print(a)