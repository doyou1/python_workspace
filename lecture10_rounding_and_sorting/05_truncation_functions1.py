import numpy as np

x = np.random.uniform(-5, 5, (5, ))

trunc = np.trunc(x)

# 소수점 자르기
print(f"x: \n{x}\n")
print(f"trunc: \n{trunc}")