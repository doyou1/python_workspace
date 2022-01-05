import numpy as np

int_py = 3
float_py = 3.14

int_np = np.array(int_py)
float_np = np.array(float_py)

print("Integer case")
print(type(int_py), type(int_np))
print(int_py, int_np, sep=' - ')

print("Floating point case")
print(type(float_py), type(float_np))
print(float_py, float_np, sep = ' - ')