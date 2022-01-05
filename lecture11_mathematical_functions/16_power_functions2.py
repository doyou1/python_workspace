import numpy as np

# 3x^3 - 2x^2 + x - 2
x = np.random.uniform(0, 5, (4, ))

y1 = 3*x**3 - 2*x**2 + x - 2
y2 = 3*np.power(x, 3) - 2*np.power(x, 2) + x - 2

print(f"x: {x}")
# x: [4.86908905 2.27490078 0.80893743 
# 3.92019259]

print(f"y1: \n {y1.round(2)}")
print(f"y2: \n {y2.round(2)}")
# y1:
#  [301.76  25.24  -0.91 151.92]       
# y2:
#  [301.76  25.24  -0.91 151.92] 