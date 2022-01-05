import numpy as np

x = np.arange(5)
y = np.arange(2, 6)

print(f"x: {x}")
print(f"y: {y}\n")
# x: [0 1 2 3 4]
# y: [2 3 4 5]

for x_ in x:
    for y_ in y:
        print(x_ + y_, end=' ')
    print()
# 2 3 4 5
# 3 4 5 6
# 4 5 6 7
# 5 6 7 8
# 6 7 8 9

for x_ in x:
    print(x_ + y)
# [2 3 4 5]
# [3 4 5 6]
# [4 5 6 7]
# [5 6 7 8]
# [6 7 8 9]