import numpy as np

M = np.arange(27)
N = M.reshape((3,3,3))
O = N.flatten()

print(M, '\n')
print(N, '\n')
print(O, '\n')

N0, N1, N2 = N[0], N[1], N[2]

print("N0: \n", N0, '\n')
print("N1: \n", N1, '\n')
print("N2: \n", N2, '\n')