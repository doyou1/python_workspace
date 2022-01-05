import numpy as np

a = np.random.uniform(0, 10, (4, ))

# a^2 -> 역치   np.square() 제곱
y1 = a**(-2)
y2 = np.reciprocal(np.square(a))

z1 = a**(-1/2)
z2 = np.reciprocal(np.sqrt(a))

print(f"a: \n {a.round(2)} \n")
# a:
#  [4.15 6.25 4.36 7.49]

print(f"y1: \n {y1.round(2)}")
print(f"y2: \n {y2.round(2)}")
# y1:
#  [0.06 0.03 0.05 0.02]
# y2:
#  [0.06 0.03 0.05 0.02]

print(f"z1: \n {z1.round(2)}")
print(f"z2: \n {z2.round(2)}")
# z1:
#  [0.49 0.4  0.48 0.37]
# z2:
#  [0.49 0.4  0.48 0.37]