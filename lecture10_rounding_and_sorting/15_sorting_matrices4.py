import numpy as np

x = np.random.randint(0, 100, (4, 5))

sort_ascending = np.sort(x, axis=1)
argsort_ascending = np.argsort(x, axis=1)

sort_descending = np.sort(x, axis=1)[:, ::-1]
argsort_descending = np.argsort(x, axis=1)[:, ::-1]

print(f"x: \n{x}\n")
# x: 
# [[12 36 22 59 18]
#  [62 92 75  9 67]
#  [92 80 53 34 73]
#  [17  1  4 71 13]]

print(f"sort(ascending): \n{sort_ascending}")
print(f"argsort(ascending): \n{argsort_ascending}")
# sort(ascending):
# [[12 18 22 36 59]
#  [ 9 62 67 75 92]
#  [34 53 73 80 92]
#  [ 1  4 13 17 71]]
# argsort(ascending):
# [[0 4 2 1 3]
#  [3 0 4 2 1]
#  [3 2 4 1 0]
#  [1 2 4 0 3]]

print(f"sort(descending): \n{sort_descending}")
print(f"argsort(descending): \n{argsort_descending}")
# sort(descending):
# [[59 36 22 18 12]
#  [92 75 67 62  9]
#  [92 80 73 53 34]
#  [71 17 13  4  1]]
# argsort(descending):
# [[3 1 2 4 0]
#  [1 2 4 0 3]
#  [0 1 4 2 3]
#  [3 0 4 2 1]]