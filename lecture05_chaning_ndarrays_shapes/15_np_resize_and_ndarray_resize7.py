import numpy as np

a = np.arange(9)
b = a.resize((3,3))
c = np.resize(a, (3,3))
print(a)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]
print(b)    # None
print(c)    # [[0 1 2]
            # [3 4 5]
            # [6 7 8]]
# np.array.resize -> return: None
# np.resize -> return: O