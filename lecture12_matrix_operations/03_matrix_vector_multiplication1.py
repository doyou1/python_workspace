import numpy as np

M = np.random.uniform(0, 5, (3, 4))
u = np.random.uniform(0, 5, (4, ))

mat_vec_mul = np.empty((3, ))
for row_idx, row in enumerate(M):
    mat_vec_mul[row_idx] = np.dot(row, u)

np_matmul = np.matmul(M, u)

# M ⋅ u [⃗i] = Ri ⋅ u
print(f"mat_vec_mul: {mat_vec_mul.shape}\n {mat_vec_mul.round(2)}")
print(f"np_matmul: {np_matmul.shape}\n {np_matmul.round(2)}")