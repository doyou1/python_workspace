import numpy as np

a = np.random.randint(-2, 3, size=(3,3))

u_nonzero = a[np.nonzero(a>0)]
u_where = a[np.where(a>0)]
u_bool = a[a>0]

print(f"a: \n{a}\n")
print(f"using nonzero: \n{u_nonzero}")
print(f"using where: \n{u_where}")
print(f"using bool ndarray: \n{u_bool}")