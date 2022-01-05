import numpy as np

images = np.random.normal(size=(32,100,200))
print("image set: ", images.shape)

col0 = images[:, :, 0]
print(col0.shape)

col0 = images[..., 0]
print(col0.shape, '\n')

image0_col0 = images[0, :, 0]
print(image0_col0.shape)

image0_col0 = images[0, ..., 0]
print(image0_col0.shape)