import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn')

fig, ax = plt.subplots(figsize=(10, 5))

random_values = np.random.randn(300)    # 정규분포하는 random list get
ax.hist(random_values, bins=20)
print(random_values.shape)
