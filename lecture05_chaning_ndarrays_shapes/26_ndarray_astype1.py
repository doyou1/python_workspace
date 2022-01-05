import numpy as np

M = np.array([1,2,3], np.int8)
print(M.dtype)  # int8

N = M.astype(np.uint32)
O = M.astype(np.float32)
print(N.dtype)  # uint32
print(O.dtype)  # float32