import numpy as np
from matplotlib import pyplot as plt

img = plt.imread('test_image.jpg')
# img = plt.imread('test_rgb.jpg')

# print(img.shape)    # (350, 500, 3) = (height(세로), width(가로), rgb정보값)

# height = [*img.shape][0]
# width = [*img.shape][1]

height = 10
width = 10

r_ch, g_ch, b_ch = img[:height,:width, 0], img[:height,:width, 1], img[:height,:width, 2]

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(r_ch, g_ch, b_ch, marker='o', cmap='Greens')

plt.tight_layout()
plt.show()
