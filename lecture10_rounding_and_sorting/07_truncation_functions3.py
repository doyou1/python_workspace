import numpy as np

x = np.random.uniform(-5, 5, (5, ))

trunc = 0.1*np.trunc(10*x)

print(f"x: \n{x}\n")
print(f"trunc: \n{trunc}")