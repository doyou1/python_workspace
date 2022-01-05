import numpy as np

# X = np.random.uniform(0, 5, (3, 4))

# W = np.random.uniform(0, 5, (4, 5))
# b = np.random.uniform(0, 5, (5, ))

X = np.random.randint(0, 5, (3, 4))

W = np.random.randint(0, 5, (4, 5))
b = np.random.randint(0, 5, (5, ))

affine = np.matmul(X, W) + b
activation = 1/(1 + np.exp(-affine))

print(f"affine: \n{affine}")
print(f"activation: \n{activation}")
