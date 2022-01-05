import numpy as np

a = np.random.uniform(0, 5, (4, ))

sqrt1 = np.sqrt(a).round(2)
sqrt2 = (a**(1/2)).round(2)
sqrt3 = np.power(a, (1/2)).round(2)

cbrt1 = np.cbrt(a).round(2)
cbrt2 = (a**(1/3)).round(2)
cbrt3 = np.power(a, (1/3)).round(2)

print(f"a: \n{a}")
# a: 
# [2.23164654 4.24852588 0.60764748 4.15810514]

print("sqrt")
print(f"{sqrt1}\n{sqrt2}\n{sqrt3}\n")
# sqrt
# [1.49 2.06 0.78 2.04]
# [1.49 2.06 0.78 2.04]
# [1.49 2.06 0.78 2.04]

print("cbrt")
print(f"{cbrt1}\n{cbrt2}\n{cbrt3}")
# cbrt
# [1.31 1.62 0.85 1.61]
# [1.31 1.62 0.85 1.61]
# [1.31 1.62 0.85 1.61]