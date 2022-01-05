import numpy as np

x = np.random.uniform(0, 5, (4, ))

w = np.random.uniform(0, 5, (4, ))
b = np.random.uniform(0, 5, ())

# y = wx + b
affine = np.dot(x, w) + b

# y2 = 1/(1 + e^-y)
activation = 1/(1 + np.exp(-affine))