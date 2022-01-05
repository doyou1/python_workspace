import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.001, 10, 300)
log = np.log(x)

fig, ax = plt.subplots(figsize=(20, 10))
ax.plot(x, log)
ax.tick_params(labelsize=20)

plt.show()