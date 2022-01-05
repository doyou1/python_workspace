import numpy as np

M = np.arange(9)
N = M.reshape((3,3))
O = N.ravel()

print(M, '\n')
print(N, '\n')
print(O, '\n')