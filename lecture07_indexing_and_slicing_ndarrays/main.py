import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('./lecture07_indexing_and_slicing_ndarrays/test_image.jpg')
# 세로, 가로, rgb
# print(img.shape)
img = np.moveaxis(img, source=2, destination=0)
# rgb, 세로, 가로
# print(img.shape)
r_channel = img[0]
g_channel = img[1]
b_channel = img[2]

# gray_image = np.mean(img, axis=0)

img = np.moveaxis(img, source=0, destination=2)
img_crop = img[70:150,100:200]
# 세로, 가로, rgb
# print(img.shape)
fig, axes = plt.subplots(2, 2, figsize=(30, 15))
axes[0, 0].imshow(img)
axes[0, 1].imshow(r_channel, cmap='gray')
axes[1, 0].imshow(g_channel, cmap='gray')
axes[1, 1].imshow(b_channel, cmap='gray')

fig.tight_layout()
plt.show()
