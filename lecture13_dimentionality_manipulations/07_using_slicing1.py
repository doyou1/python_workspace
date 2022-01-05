import numpy as np

a = np.arange(9)

row_vec1 = a[np.newaxis, :]
row_vec2 = a[None, :]

col_vec1 = a[:, np.newaxis]
col_vec2 = a[:, None]

print(f"row_vec1.shape: {row_vec1.shape}")
print(f"row_vec2.shape: {row_vec2.shape}")

print(f"col_vec1.shape: {col_vec1.shape}")
print(f"col_vec2.shape: {col_vec2.shape}")
