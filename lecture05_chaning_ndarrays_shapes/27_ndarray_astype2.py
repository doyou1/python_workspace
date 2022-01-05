import numpy as np

M = np.random.uniform(low=-10, high=10, size=(3,3))

print(M, '\n')
print(M.astype(np.int32)) # 자연수화