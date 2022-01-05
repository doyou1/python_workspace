import numpy as np

a = np.random.uniform(0, 10, (4, ))

recip1 = 1/a
recip2 = a**(-1)
recip3 = np.reciprocal(a)

print(f"a: \n {a.round(2)} \n")
# a:
#  [8.14 7.01 2.8  2.97]

print(f"1/a: \n {recip1.round(2)}")
print(f"a**(-1): \n {recip2.round(2)}")
print(f"np.reciprocal(a): \n {recip3.round(2)}")
# 1/a:
#  [0.12 0.14 0.36 0.34]
# a**(-1):
#  [0.12 0.14 0.36 0.34]
# np.reciprocal(a):
#  [0.12 0.14 0.36 0.34]