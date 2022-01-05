import numpy as np

a = np.random.randint(0, 10, (100, 200, 300))
b = np.random.randint(0, 10, size=a.shape)
c = np.random.randint(0, 10, size=b.shape)

print("axis=0: ", np.stack([a, b, c], axis=0).shape)
# axis=0:  (3, 100, 200, 300)

print("axis=1: ", np.stack([a, b, c], axis=1).shape)
# axis=1:  (100, 3, 200, 300)

print("axis=2: ", np.stack([a, b, c], axis=2).shape)
# axis=2:  (100, 200, 3, 300)

print("axis=3: ", np.stack([a, b, c], axis=3).shape)
# axis=3:  (100, 200, 300, 3)