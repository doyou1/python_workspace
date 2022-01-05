import numpy as np
from numpy.random import randint

a = randint(0, 10, (2,3))

b = a.flatten()
b[0] = -10

print(b.base is a, '\n')    # False
print(a)    # [[0 2 3]
            # [4 6 1]]
print(b)    # [-10   2   3   4   6   1]