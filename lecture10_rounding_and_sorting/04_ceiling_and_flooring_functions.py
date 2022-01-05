import numpy as np

x = np.random.uniform(-5, 5, (5, ))

ceil = np.ceil(x)
floor = np.floor(x)

print(f"x: \n{x}\n")
print(f"ceil: \n{ceil}")
print(f"floor: \n{floor}")