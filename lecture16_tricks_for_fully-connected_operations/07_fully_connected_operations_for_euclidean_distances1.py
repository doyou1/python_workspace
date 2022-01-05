import numpy as np

X = np.random.uniform(-5, 5, (4, 2))
Y = np.random.uniform(-5, 5, (3, 2))

for x in X:
    for y in Y:
        e_dist = np.sqrt(np.sum(np.square(x - y)))
        print(f"{e_dist:5.2f}", end='   ')
    print()
# (4, 3)