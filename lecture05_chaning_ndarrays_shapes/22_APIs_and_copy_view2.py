import numpy as np

a = np.arange(5)
b = np.resize(a, (2,2))

b[0,0] = 100

print(b.base is a, '\n')    # False
print(a)    # [0 1 2 3 4]
print(b)    # [[100   1]
            # [  2   3]]