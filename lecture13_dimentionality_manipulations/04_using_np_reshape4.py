import numpy as np

a = np.random.normal(size=(100, 200))

b = a.reshape((1, 100, 200))
c = a.reshape((100, 200, 1))

print(b.shape)
print(c.shape)