import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('./lecture07_indexing_and_slicing_ndarrays/test_image.jpg')
송강호 = img[70:150,100:200]
이선균 = img[70:150,250:350]
최우식 = img[70:150,410:460]

fig, axes = plt.subplots(2, 2, figsize=(30, 15))
axes[0, 0 ].imshow(img)
axes[0, 1].imshow(송강호)
axes[1, 0].imshow(이선균)
axes[1, 1].imshow(최우식)


fig.tight_layout()
plt.show()

