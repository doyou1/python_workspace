import numpy as np

M = np.arange(9)
N = M.reshape((3,3))
O = N.flatten() # Vector로 만든다

print(M, '\n')  # [0 1 2 3 4 5 6 7 8]

print(N, '\n')  # [[0 1 2]
                # [3 4 5]
                # [6 7 8]]

print(O, '\n')  # [0 1 2 3 4 5 6 7 8]
