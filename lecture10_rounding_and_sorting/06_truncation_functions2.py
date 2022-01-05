import numpy as np

x = np.random.uniform(-5, 5, (5, ))

# np.trunc() 작동 구조
trunc_where = np.where(x >= 0, np.floor(x), np.ceil(x))
trunc = np.trunc(x)

print(f"x: \n{x}\n")
print(f"trunc_where: \n{trunc_where}")
print(f"trunc: \n{trunc}")