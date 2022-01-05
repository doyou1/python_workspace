import numpy as np

a = np.arange(4)
b = np.reshape(a, (2,2))

b[0,0] = 100

print(b.base is a, '\n')    # True
print(a)    # [100   1   2   3]
print(b)    # [[100   1]
            # [  2   3]]