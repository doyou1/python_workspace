import numpy as np
import matplotlib.pyplot as plt

Count, C, H, W = 4, 3, 20, 10
images = np.random.randint(0, 256, size=(Count,C, H, W))
img1 = np.moveaxis(images[0], source=0, destination=2)
img2 = np.moveaxis(images[1], source=0, destination=2)
img3 = np.moveaxis(images[2], source=0, destination=2)
img4 = np.moveaxis(images[3], source=0, destination=2)

fig, axes = plt.subplots(2, 2, figsize=(20, 10))
axes[0, 0].imshow(img1)
axes[0, 1].imshow(img2)
axes[1, 0].imshow(img3)
axes[1, 1].imshow(img4)

fig.tight_layout()
plt.show()
