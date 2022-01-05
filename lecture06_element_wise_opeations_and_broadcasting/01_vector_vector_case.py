import numpy as np

a = np.random.randint(1, 5, (5, ))
b = np.random.randint(1, 5, (5, ))

print("a: ", a)
print("b: ", b, '\n')

print("a + b: ", a + b)
print("a - b: ", a - b)
print("a * b: ", a * b)
print("a / b: ", a / b)
print("a // b: ", a // b)
print("a % b: ", a % b)
print("a ** b: ", a ** b)




print("a + b: ", a.__add__(b))
print("a - b: ", a.__sub__(b))
print("a * b: ", a.__mul__(b))
print("a / b: ", a.__truediv__(b))
print("a // b: ", a.__floordiv__(b))
print("a % b: ", a.__mod__(b))
print("a ** b: ", a.__pow__(b))

print("a > b: ", a > b)
print("a >= b: ", a >= b)
print("a < b: ", a < b)
print("a <= b: ", a <= b)
print("a == b: ", a == b)
print("a != b: ", a != b)
