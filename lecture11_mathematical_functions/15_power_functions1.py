import numpy as np

a = np.random.uniform(0, 5, (4, ))

s1 = np.square(a).round(2)
s2 = (a**2).round(2)
s3 = np.power(a, 2).round(2)

re1 = np.reciprocal(a).round(2)
re2 = (a**(-1)).round(2)
re3 = np.power(a, -1).round(2)

print(f"a: \n{a}\n")
# a: 
# [2.80962454 2.18449922 3.27299768 0.60248206]

print("square")
print(f"{s1}\n{s2}\n{s3}\n")
# square
# [ 7.89  4.77 10.71  0.36]
# [ 7.89  4.77 10.71  0.36]
# [ 7.89  4.77 10.71  0.36]

print("reciprocal")
print(f"{re1}\n{re2}\n{re3}")
# reciprocal
# [0.36 0.46 0.31 1.66]
# [0.36 0.46 0.31 1.66]
# [0.36 0.46 0.31 1.66]