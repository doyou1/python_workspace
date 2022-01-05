import numpy as np

x = np.linspace(0, 1, 5)

sinh, cosh = np.sinh(x), np.cosh(x)
tanh = np.tanh(x)

print(f"np.tanh: \n {tanh.round(2)}")
# np.tanh:
#  [0.   0.24 0.46 0.64 0.76]

print(f"np.sinh/np.cosh: \n {(sinh/cosh).round(2)}")
# np.sinh/np.cosh:
#  [0.   0.24 0.46 0.64 0.76]