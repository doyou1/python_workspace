import numpy as np

a = np.random.randint(0, 10, (100, 200))
b = np.random.randint(0, 10, size=a.shape)
c = np.random.randint(0, 10, size=b.shape)

print("ndim==2: ", np.stack([a, b, c]).shape)
# ndim==2:  (3, 100, 200)

a = np.random.randint(0, 10, (100, 200, 300))
b = np.random.randint(0, 10, size=a.shape)
c = np.random.randint(0, 10, size=b.shape)

print("ndim==3: ", np.stack([a, b, c]).shape)
# ndim==3:  (3, 100, 200, 300)