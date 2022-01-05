import numpy as np

a = np.arange(9)

b = a.reshape((1, 9))
c = a.reshape((9, 1))

print(f"a : {a.shape}\n {a}\n")

print(f"b : {b.shape}\n {b}\n")
