import numpy as np

a = np.random.randint(0, 10, (3, 4, 5))

b = np.random.randint(0, 10, (10, 4, 5))
concat0 = np.concatenate([a, b], axis=0)
print(f"concat0: {concat0.shape}")
# concat0: (13, 4, 5)

b = np.random.randint(0, 10, (3, 4, 10))
concat2 = np.concatenate([a, b], axis=2)
print(f"concat2: {concat2.shape}")
# concat2: (3, 4, 15)

b = np.random.randint(0, 10, (3, 10, 5))
concat1 = np.concatenate([a, b], axis=1)
print(f"concat1: {concat1.shape}")
# concat1: (3, 14, 5)