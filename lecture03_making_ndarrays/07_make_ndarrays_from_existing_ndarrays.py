import numpy as np

M = np.full(shape=(2,3), fill_value=3.14)
print(M, '\n')

zeros_like = np.zeros_like(M)
ones_like = np.ones_like(M)
full_like = np.full_like(M, fill_value=100)
empty_like = np.empty_like(M)

print("zeros_like: \n", zeros_like, '\n')
print("ones_like: \n", ones_like, '\n')
print("full_like: \n", full_like, '\n')
print("empty_like: \n", empty_like, '\n')