import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 100)
sigmoid = 1/(1 + np.exp(-x))
tanh = np.tanh(x)
relu = np.maximum(x, 0)

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x, sigmoid, label=r'$y = \sigma(x)$', alpha=0.7)
ax.plot(x, tanh, label=r'$y = tanh(x)$', alpha=0.7)
ax.plot(x, relu, label=r'$y = ReLu(x)$', alpha=0.7)

ax.tick_params(labelsize=20)
ax.legend(fontsize=20)

plt.show()