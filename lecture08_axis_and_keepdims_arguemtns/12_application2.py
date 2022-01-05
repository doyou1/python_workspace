import numpy as np

C, H, W = 3, 100, 200

# (C, H, W) case
images = np.random.randint(0, 256, size=(C, H, W))
print("Shape of original image: ", images.shape)

gray_image = np.mean(images, axis=0)
print("Shape of gray-scaled image: ", gray_image.shape, '\n')

# (H, W, C) case
images = np.random.randint(0, 256, size=(H, W, C))
print("Shape of original image: ", images.shape)

gray_image = np.mean(images, axis=0)
print("Shape of gray-scaled image: ", gray_image.shape, '\n')