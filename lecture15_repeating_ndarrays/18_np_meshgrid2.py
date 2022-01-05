import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x ,y)
Z = np.square(X) + np.square(Y)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(projection='3d')

ax.plot_wireframe(X, Y, Z)
ax.tick_params(labelsize=20)

plt.show()