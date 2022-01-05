import numpy as np

x = np.random.randint(0, 100, (10, ))

sort = np.sort(x)
argsort = np.argsort(x)

print(f"x: \n{x}\n")

print(f"sort: \n{sort}")
print(f"argsort: \n{argsort}")