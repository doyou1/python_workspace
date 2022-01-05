import numpy as np

tensor_py = [[[1,2,3],
            [4,5,6]],
        
            [[7,8,9],
            [10,11,12]]]

tensor_np = np.array(tensor_py)

print(type(tensor_py), type(tensor_np))
print(tensor_py, tensor_np, sep='\n\n')