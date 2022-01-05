import numpy as np
from numpy.random import randint

a = randint(0, 10, (2,3))

b = a.ravel()
b[0] = -10

print(b.base is a, '\n')    # True
print(a)    # [[-10   2   1]
            # [  4   8   1]]
print(b)    # [-10   2   1   4   8   1]