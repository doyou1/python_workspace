import numpy as np

images = np.random.normal(size=(32,100,200))
print("image set: ", images.shape)

image0 = images[0, :, :]
print(image0.shape)

image0 = images[0, ...]
print(image0.shape)