import numpy as np

x = np.random.uniform(-5, 5, (5, ))

int_part = np.trunc(x)
frac_part = x - int_part

print(f"x: \n {x}\n")

print(f"int_part: \n{int_part}")
print(f"frac_part: \n{frac_part}")

print(f"x = int_part + frac_part: \n{int_part+frac_part}")