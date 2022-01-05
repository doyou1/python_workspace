import numpy as np

# numpy.zeros(shape, dtype=float, order='C', *, like=None)
M = np.zeros(shape=(2,3))

print(M.shape)
print(M)


# numpy.ones(shape, dtype=None, order='C', *, like=None)
M = np.ones(shape=(2,3))

print(M.shape)
print(M)

# numpy.full(shape, fill_value, dtype=None, order='C', *, like=None)
M = np.full(shape=(2,3), fill_value=3.14)

print(M.shape)
print(M)

# numpy.empty(shape, dtype=float, order='C', *, like=None)

M = np.empty(shape=(2,3))

print(M.shape)
print(M)