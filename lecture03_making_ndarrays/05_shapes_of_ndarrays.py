import numpy as np

scalar_np = np.array(3.14)
vec_np = np.array([1,2,3])
mat_np = np.array([[1,2], [3,4]])
tensor_np = np.array([[[1,2,3],
                    [4,5,6]],
                    [[7,8,9],
                    [10,11,12]]])

print(scalar_np.shape)  # ()
print(vec_np.shape)     # (1)
print(mat_np.shape)     # (2,2)
print(tensor_np.shape)  # (2,2,3)

print(len(()))          # 0
print(len((3,)))        # 1
print(len((2, 2)))      # 2
print(len((2, 2, 3)))   # 3