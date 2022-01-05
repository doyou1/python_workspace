import numpy as np
from matplotlib import pyplot as plt

R, G, B = [255.0, 0., 0.], [0., 255., 0.], [0., 0., 255.]

img = plt.imread('test_rgb.jpg').astype(np.float64)
# img = plt.imread('test_image_teacher.jpeg').astype(np.float64)
# img = plt.imread('test_image.jpg').astype(np.float64)
print(img.shape, img.dtype)

img_norm = np.sqrt(img[..., 0]**2 + img[..., 1]**2 + img[..., 2]**2)
img_norm = np.reshape(img_norm, (img_norm.shape + (1, )))
img_unit = img / img_norm

t_r = np.array(R)
print("t_r.shape", t_r.shape)
t_r_norm = np.sqrt(np.sum(t_r**2))
print("t_r_norm", t_r_norm)
t_r_unit = t_r / t_r_norm
print("t_r_unit", t_r_unit)
img_dot_r = np.sum(img_unit * t_r_unit, axis=-1)
print("img_dot_r.shape: ", img_dot_r.shape)

t_g = np.array(G)
t_g_norm = np.sqrt(np.sum(t_g**2))
t_g_unit = t_g / t_g_norm
img_dot_g = np.sum(img_unit * t_g_unit, axis=-1)

t_b = np.array(B)
t_b_norm = np.sqrt(np.sum(t_b**2))
t_b_unit = t_b / t_b_norm
img_dot_b = np.sum(img_unit * t_b_unit, axis=-1)

fig, axes = plt.subplots(1, 4, figsize=(30, 10))
axes[0].imshow(img.astype(np.uint8))
axes[1].imshow(img_dot_r, cmap="gray")
axes[2].imshow(img_dot_g, cmap="gray")
axes[3].imshow(img_dot_b, cmap="gray")
fig.tight_layout()
plt.show()