import numpy as np

# 0빼고는 다 True
ints = np.array([-2, -1, 0, 1, 2])
floats = np.array([-2.5, -1.5, 0., 1.5, 2.5])

print(f"ints: \n{ints}")
print(f"floats: \n{floats}")

ints2bools = ints.astype(np.bool)
print(f"ints -> bools: \n{ints2bools}")

floats2bools = floats.astype(np.bool)
print(f"floats -> bools: \n{floats2bools}")