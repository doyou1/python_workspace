import numpy as np

a = np.random.normal(size=(3, 200, 100))

# change "0 and last dimen" 
b = np.swapaxes(a, 0, -1)

print(f"a.shape: {a.shape}")
print(f"b.shape: {b.shape}")
# a.shape: (3, 200, 100)
# b.shape: (100, 200, 3)