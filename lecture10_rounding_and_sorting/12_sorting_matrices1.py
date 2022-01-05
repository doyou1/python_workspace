import numpy as np

x = np.random.randint(0, 100, (4, 5))

sort = np.sort(x, axis=0)
argsort = np.argsort(x, axis=0)

print(f"x: \n{x}\n")
# x: 
# [[16 88 18 61 69]
#  [ 1 87 18 10 23]
#  [51 35 70 26 81]
#  [17 72 67 80 43]]

print(f"sort: \n{sort}")
# sort:
# [[ 1 35 18 10 23]
#  [16 72 18 26 43]
#  [17 87 67 61 69]
#  [51 88 70 80 81]]

print(f"argsort: \n{argsort}")
# argsort:
# [[1 2 0 1 1]
#  [0 3 1 2 3]
#  [3 1 3 0 0]
#  [2 0 2 3 2]]