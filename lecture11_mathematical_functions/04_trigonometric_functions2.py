import numpy as np
import matplotlib.pyplot as plt

PI = np.pi

x = np.linspace(0, 4*PI, 100)

sin, cos, tan = np.sin(x), np.cos(x), np.tan(x)

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x, sin, label=r'$y = sin(x)$')
ax.plot(x, cos, label=r'$y = cos(x)$')
ax.plot(x, tan, label=r'$y = tan(x)$')

xticks = np.arange(0, 4*PI+0.1, 0.5*PI)
xticklabels = [str(xtick)+r'$\frac{\pi}{2}$' for xtick in range(9)]
ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels)
ax.tick_params(axis='x', labelsize=20)
ax.set_ylim([-2, 2])
ax.legend()

plt.show()