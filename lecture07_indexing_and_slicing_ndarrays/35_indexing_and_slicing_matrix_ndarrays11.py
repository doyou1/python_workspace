import numpy as np

a = np.array([True, False, True, False])

nonzero = np.nonzero(a) # index 튀어나온다
where = np.where(a)     # index 튀어나온다

print(f"a: \n{a}\n")
print(f"nonzero: \n{nonzero}")
print(f"where: \n{where}")