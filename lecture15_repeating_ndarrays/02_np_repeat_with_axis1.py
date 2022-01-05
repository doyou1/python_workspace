import numpy as np

x = np.arange(4).reshape((2, 2))

rep = np.repeat(x, 3)
print(f"x: \n{x}")
print(f"np.repeat(x, 3): \n{rep}\n")