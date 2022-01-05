import numpy as np

a = np.random.randint(0, 10, (3, 3))

print(a)
# [[8 1 0]
#  [4 2 2]
#  [6 1 2]]
max_axis_0 = np.max(a, axis=0)
max_axis_1 = np.max(a, axis=1)

print(max_axis_0)
# [8 2 2]

print(max_axis_1)
# [8 4 6]

min_axis_0 = np.min(a, axis=0)
min_axis_1 = np.min(a, axis=1)

print(min_axis_0)
# [4 1 0]

print(min_axis_1)
# [0 2 1]

a = np.random.randint(0, 10, (2, 3, 4))

print(a)
# [[[2 8 9 3]
#   [9 8 7 9]
#   [0 5 7 7]]

#  [[4 5 4 8]
#   [2 8 8 2]
#   [4 5 7 4]]]

max_axis_0 = np.max(a, axis=0)
max_axis_1 = np.max(a, axis=1)
max_axis_2 = np.max(a, axis=2)


print(max_axis_0)
# [[4 8 9 8]
#  [9 8 8 9]
#  [4 5 7 7]]

print(max_axis_1)
# [[9 8 9 9]
#  [4 8 8 8]]

print(max_axis_2)
# [[9 9 7]
#  [8 8 7]]

min_axis_0 = np.min(a, axis=0)
min_axis_1 = np.min(a, axis=1)
min_axis_2 = np.min(a, axis=2)

print(min_axis_0)
# [[2 5 4 3]
#  [2 8 7 2]
#  [0 5 7 4]]

print(min_axis_1)
# [[0 5 7 3]
#  [2 5 4 2]]

print(min_axis_2)
# [[2 7 0]
#  [4 2 4]]