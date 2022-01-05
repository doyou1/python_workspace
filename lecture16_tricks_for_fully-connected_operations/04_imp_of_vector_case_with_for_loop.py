import numpy as np

X = np.random.uniform(-5, 5, (4, 2))
Y = np.random.uniform(-5, 5, (3, 2))

for x in X:
    for y in Y:
        add = x + y
        print(f"{add}", end='   ')
    print()

# (4, 3)