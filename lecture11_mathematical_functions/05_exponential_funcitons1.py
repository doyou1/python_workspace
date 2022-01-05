import numpy as np

E = np.e
x = np.arange(1, 7)

print(f"E**x: \n {(E**x).round(2)}")
# E**x:
#  [  2.72   7.39  20.09  54.6  148.41 
# 403.43]

print(f"np.exp(x): \n {np.exp(x).round(2)}")
# np.exp(x):
#  [  2.72   7.39  20.09  54.6  148.41 
# 403.43]