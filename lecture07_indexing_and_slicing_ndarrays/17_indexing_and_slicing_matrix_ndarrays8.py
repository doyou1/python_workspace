import numpy as np

image = np.arange(9).reshape((3, 3))
print(f"ndarray: \n{image}\n")

# 좌우반전
horizontal_flip = image[:, ::-1]
print(f"horizontal_flip: \n{horizontal_flip}\n")

# 상하반전
vertical_flip = image[::-1, :]
print(f"vertical_flip: \n{vertical_flip}\n")

# 180도 회전
rotation = image[::-1, ::-1]
print(f"rotation: \n{rotation}\n")