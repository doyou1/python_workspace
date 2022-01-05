import numpy as np

a = np.random.randint(0, 10, (10, ))

square1 = a*a
square2 = a**2
square3 = np.square(a)

print(f"a: \n{a}\n")
# a:
# [3 0 2 9 1 3 5 9 5 4]


print(f"a*a: \n {square1}")
print(f"a**2: \n {square2}")
print(f"np.square(a): \n {square3}")
# a*a:
#  [ 9  0  4 81  1  9 25 81 25 16]     
# a**2:
#  [ 9  0  4 81  1  9 25 81 25 16]     
# np.square(a):
#  [ 9  0  4 81  1  9 25 81 25 16] 