import numpy as np

scalar_np = np.array(3.14)
vector_np = np.array([1, 2, 3])
matrix_np = np.array([[1, 2], [3, 4]])
tensor_np = np.array([[[1, 2, 3],
                    [4, 5, 6]],
 
                    [[11, 12, 13],
                    [14, 15, 16]]])


print(scalar_np.ndim)   # 0
print(vector_np.ndim)   # 1
print(matrix_np.ndim)   # 2
print(tensor_np.ndim)   # 3