import numpy as np

x = np.random.uniform(-5, 5, (4, 2))
y = np.random.uniform(-5, 5, (3, 2))

X = np.expand_dims(x, axis=1)
Y = np.expand_dims(y, axis=0)
Z = X + Y

print("shapes: ")
print(f"X/Y/Z: {X.shape}/{Y.shape}/{Z.shape}")
# shapes:
# X/Y/Z: (4, 1, 2)/(1, 3, 2)/(4, 3, 2)