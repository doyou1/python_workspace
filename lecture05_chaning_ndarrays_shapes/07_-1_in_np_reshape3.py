import numpy as np

a = np.arange(24)

b = a.reshape((2,3,-1))
c = a.reshape((2,-1,4))
d = a.reshape((-1,3,4))

print(b.shape, c.shape, d.shape)