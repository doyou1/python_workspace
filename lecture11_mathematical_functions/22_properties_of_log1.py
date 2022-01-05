import numpy as np

a = np.random.uniform(1, 5, (4, ))
b = np.random.uniform(1, 5, (4, ))

# log(a) + log(b) = log(ab)
print((np.log(a) + np.log(b)).round(3))
print(np.log(a*b).round(3))
# [2.57  2.504 1.006 2.206]
# [2.57  2.504 1.006 2.206]