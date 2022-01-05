import numpy as np

A = np.array([10,20])
B = np.arange(6).reshape((3,2))
C = A + B

print("A: {}/{}\n{}".format(A.ndim,A.shape,A))
print("B: {}/{}\n{}".format(B.ndim,B.shape,B))

print("A + B: {}/{}\n{}".format(C.ndim,C.shape,C))