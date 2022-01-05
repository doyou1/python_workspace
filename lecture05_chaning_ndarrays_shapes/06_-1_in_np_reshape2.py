import numpy as np

a = np.arange(12)

b = a.reshape((-1, 2))
c = a.reshape((-1, 3))
d = a.reshape((-1, 4))
e = a.reshape((-1, 6))

print(b.shape, c.shape,
        d.shape, e.shape)