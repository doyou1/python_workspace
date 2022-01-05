import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
exp = np.exp(x)

print(exp.round(2))

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x, exp)
ax.tick_params(labelsize=20)

plt.show()