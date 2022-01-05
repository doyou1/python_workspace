import numpy as np

a = np.arange(9)

b = a.reshape((1, -1))
c = a.reshape((-1, 1))

print(f"a: {a.shape}\n{a}\n")

print(f"b: {b.shape}\n{b}\n")
print(f"c: {c.shape}\n{c}\n")