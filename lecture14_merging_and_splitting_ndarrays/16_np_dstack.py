import numpy as np

R = np.random.randint(0, 256, (100, 200))
G = np.random.randint(0, 256, size=R.shape)
B = np.random.randint(0, 256, size=R.shape)

image = np.dstack([R, G, B])

print(image.shape)  # (100, 200, 3)
