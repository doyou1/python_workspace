import numpy as np

a = np.random.randint(5,size=(3, 4))

b = np.transpose(a)
c = a.T

print(f"a: {a.shape}\n{a}\n")
# a: (3, 4)
# [[3 1 2 2]
#  [0 3 0 2]
#  [0 1 4 3]]

print(f"b: {b.shape}\n{b}\n")
print(f"c: {c.shape}\n{c}\n")
# b: (4, 3)
# [[3 0 0]
#  [1 3 1]
#  [2 0 4]
#  [2 2 3]]

# c: (4, 3)
# [[3 0 0]
#  [1 3 1]
#  [2 0 4]
#  [2 2 3]]