import numpy as np

degree = np.array([30, 45, 60, 90, 180, 360])
rad = np.deg2rad(degree)
degree = np.rad2deg(rad)

print("redian: ", rad.round(3)) # redian:  [0.524 0.785 1.047 1.571 3.142 6.283]
print("degree again: ", degree) # degree again:  [ 30.  45.  60.  90. 180. 360.]

# 1radian = 1라디안
# 1라디안 = 360/(2π) = 180/π -> 180도=1라디안