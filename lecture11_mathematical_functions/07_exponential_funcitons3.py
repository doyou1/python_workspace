import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
sigmoid = 1/(1 + np.exp(-x))

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x, sigmoid)
ax.tick_params(labelsize=20)

plt.show()
