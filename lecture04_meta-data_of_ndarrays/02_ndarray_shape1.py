import numpy as np

scalar_np = np.array(3.14)
vector_np = np.array([1,2,3])
matrix_np = np.array([[1,2],[3,4]])
tensor_np = np.array([[[1,2,3],
                        [4,5,6]],
            
                        [[7,8,9],
                        [10,11,12]]])

print("shape / dimension")
print(scalar_np.shape, ' / ', scalar_np.ndim)
print(vector_np.shape, ' / ', vector_np.ndim)
print(matrix_np.shape, ' / ', matrix_np.ndim)
print(tensor_np.shape, ' / ', tensor_np.ndim)