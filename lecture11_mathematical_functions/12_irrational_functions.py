import numpy as np

a = np.random.randint(0, 10, (4, ))

sqrt1 = a**(1/2)
sqrt2 = np.sqrt(a)

cbrt1 = a**(1/3)
cbrt2 = np.cbrt(a)

print(f"a: \n {a}\n")
# a:
#  [3 2 7 0]

print(f"√a a**(1/2): \n {sqrt1.round(2)}")
print(f"√a np.sqrt(a): \n {sqrt2.round(2)}")
# √a a**(1/2):
#  [1.73 1.41 2.65 0.  ]
# √a np.sqrt(a):
#  [1.73 1.41 2.65 0.  ]

print(f"√3a a**(1/3): \n {cbrt1.round(2)}")
print(f"√3a np.cbrt(a): \n {cbrt2.round(2)}")
# √3a a**(1/3):
#  [1.44 1.26 1.91 0.  ]
# √3a np.cbrt(a):
#  [1.44 1.26 1.91 0.  ]