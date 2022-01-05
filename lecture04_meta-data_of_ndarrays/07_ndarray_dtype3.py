import numpy as np

int8_np = np.array([1.5, 2.5, 3.5], dtype=np.int8)
uint8_np1 = np.array([1.5, 2.5, 3.5], dtype=np.uint8)
uint8_np2 = np.array([-1.5, 2.5, 3.5], dtype=np.uint8)

print(int8_np)      # [1 2 3]
print(uint8_np1)    # [1 2 3]
print(uint8_np2)    # [255 2 3]