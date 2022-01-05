import numpy as np

A = np.arange(2*3*4).reshape((2,3,4))
B = 10*np.arange(3*4).reshape((3,4))
C = A + B

print("A: {}/{}\n{}".format(A.ndim,A.shape,A))
print("B: {}/{}\n{}".format(B.ndim,B.shape,B))

print("A + B: {}/{}\n{}".format(C.ndim,C.shape,C))