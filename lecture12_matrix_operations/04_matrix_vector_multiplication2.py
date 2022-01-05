import numpy as np

# M = np.random.uniform(0, 5, (3, 4))
# N = np.random.uniform(0, 5, (4, 5))

M = np.arange(3*4).reshape(3, 4)
N = np.arange(4*5).reshape(4, 5)


mat_mat_mul = np.empty((3, 5))
for M_row_idx in range(3):
    for N_col_idx in range(5):
        dot_prod = np.dot(M[M_row_idx, :], N[:, N_col_idx])
        print(M[M_row_idx, :], N[:, N_col_idx])
        print(dot_prod)        
        mat_mat_mul[M_row_idx, N_col_idx] = dot_prod

np_matmul = np.matmul(M, N)

print(f"mat_mat_mul: \n {mat_mat_mul.round(2)}")
print(f"np_matmul: \n {np_matmul.round(2)}")