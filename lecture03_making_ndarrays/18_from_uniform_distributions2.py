import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(10, 5))

uniform = np.random.uniform(low=-10, high=10, size=(10000, ))
ax.hist(uniform, bins=20)

plt.show()