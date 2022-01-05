import numpy as np

x = np.linspace(0, 1, 5)

sinh = np.sinh(x)
sinh_exp = (np.exp(x) - np.exp(-x)) / 2

cosh = np.cosh(x)
cosh_exp = (np.exp(x) + np.exp(-x)) / 2

tanh = np.tanh(x)
tanh_exp = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

print(f"sinh: {sinh.round(2)}")
print(f"sinh_exp: {sinh_exp.round(2)} \n")
# sinh: [0.   0.25 0.52 0.82 1.18]
# sinh_exp: [0.   0.25 0.52 0.82 1.18] 


print(f"cosh: {cosh.round(2)}")
print(f"cosh_exp: {cosh_exp.round(2)} \n")
# cosh: [1.   1.03 1.13 1.29 1.54]     
# cosh_exp: [1.   1.03 1.13 1.29 1.54] 

print(f"tanh: {tanh.round(2)}")
print(f"tanh_exp: {tanh_exp.round(2)} \n")
# tanh: [0.   0.24 0.46 0.64 0.76]     
# tanh_exp: [0.   0.24 0.46 0.64 0.76] 