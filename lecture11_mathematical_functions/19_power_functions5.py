import numpy as np

a = np.random.uniform(0, 5, (4, ))
b = np.random.uniform(0, 5, (4, ))

power1 = (a**b).round(2)
power2 = np.power(a, b).round(2)

print(f"{power1}\n{power2}")
# [ 0.1   1.63 34.22  0.09]
# [ 0.1   1.63 34.22  0.09]