a = (10, 20)
print(*a)   # 10 20

import numpy as np

a = np.random.normal(size=(100, 150))


print(a.shape)
print(*a.shape)
print((1, *a.shape))
print((*a.shape, 1))
