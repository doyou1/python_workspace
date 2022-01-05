import numpy as np

x = np.random.randint(0, 100, (4, 5))

sort = np.sort(x, axis=0)[::-1, :]
argsort = np.argsort(x, axis=0)[::-1, :]

print(f"x: \n{x}\n")
# x: 
# [[75 48 16 37  1]
#  [28 27 86 17 90]
#  [30 57 81 48 77]
#  [35 49 18 55 48]]

print(f"sort: \n{sort}")
# sort:
# [[75 57 86 55 90]
#  [35 49 81 48 77]
#  [30 48 18 37 48]
#  [28 27 16 17  1]]

print(f"argsort: \n{argsort}")
# argsort:
# [[0 2 1 3 1]
#  [3 3 2 2 2]
#  [2 0 3 0 3]
#  [1 1 0 1 0]]