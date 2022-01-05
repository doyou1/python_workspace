import numpy as np

a = np.arange(1, 5)
print("ndarray: {}\n{}\n".format(a.shape, a))
# ndarray: (4,)
# [1 2 3 4]

prod = np.prod(a)
cumprod = np.cumprod(a)

print("prod: {}\n{}".format(prod.shape, prod))
print("cumprod: {}\n{}".format(cumprod.shape, cumprod))
# prod: ()
# 24

# cumprod: (4,)
# [ 1  2  6 24]