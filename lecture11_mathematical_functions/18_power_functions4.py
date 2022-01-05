import numpy as np

a = np.random.uniform(0, 5, (4, ))

exp1 = np.exp(a).round(2)
exp2 = (np.e**a).round(2)
exp3 = np.power(np.e, a).round(2)

print(f"{exp1}\n{exp2}\n{exp3}\n")
# [18.17 11.94  1.46  1.59]
# [18.17 11.94  1.46  1.59]
# [18.17 11.94  1.46  1.59]