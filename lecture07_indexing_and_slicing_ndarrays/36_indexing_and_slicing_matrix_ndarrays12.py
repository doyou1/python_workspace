import numpy as np

a = np.array([[True, False],
            [True, False]])

nonzero = np.nonzero(a)
where = np.where(a)

print(f"a: \n{a}\n")
print(f"nonzero: \n{nonzero}")
print(f"where: \n{where}")