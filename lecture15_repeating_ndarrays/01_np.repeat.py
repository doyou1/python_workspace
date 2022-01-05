import numpy as np

x = 3

rep = np.repeat(x, 2)
print(f"x: {x}")
print(f"np.repeat(x, 2): \n{rep}\n")
# x: 3
# np.repeat(x, 2):
# [3 3]

x = np.array([1, 2, 3])

rep = np.repeat(x, 3)
print(f"x: {x}")
print(f"np.repeat(x, 2): \n{rep}\n")
# x: [1 2 3]
# np.repeat(x, 2):
# [1 1 1 2 2 2 3 3 3]