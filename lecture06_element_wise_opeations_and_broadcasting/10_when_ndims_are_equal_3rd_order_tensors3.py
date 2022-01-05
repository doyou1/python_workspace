import numpy as np

A = np.arange(18).reshape((2,3,3))
B = 10*np.arange(6).reshape((2,3,1))
C = A + B

print("A: {}/{}\n{}".format(A.ndim,A.shape,A))
print("B: {}/{}\n{}".format(B.ndim,B.shape,B))

print("A + B: {}/{}\n{}".format(C.ndim,C.shape,C))