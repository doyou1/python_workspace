import numpy as np

M = np.ones(shape=(2,3), dtype=np.float32)
N = np.zeros_like(M, dtype=np.float64)

print("{}/{}".format(M.dtype, N.dtype))
print(M)
print(N)