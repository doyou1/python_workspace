import numpy as np

a = np.random.randint(0,100,(100, ))

print(a.reshape((20,5)).mean(axis=0).max())
print(np.max(np.mean(np.reshape(a, (20,5)), axis=0)))