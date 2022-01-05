import numpy as np

x = np.deg2rad(np.linspace(0, 360, 11))

print(f"x: \n{x}\n")
# [0.         0.62831853 1.25663706 1.88495559 2.51327412 3.14159265    3.76991118 4.39822972 5.02654825 5.65486678 6.28318531]

sin, cos = np.sin(x), np.cos(x)
tan = np.tan(x)

print(f"np.tan: \n {tan.round(2)}")
# np.tan:
#  [ 0.    0.73  3.08 -3.08 -0.73 -0.  
#   0.73  3.08 -3.08 -0.73 -0.  ]      

print(f"np.sin/np.cos: \n {(sin/cos).round(2)}")
# np.sin/np.cos:
#  [ 0.    0.73  3.08 -3.08 -0.73 -0.  
#   0.73  3.08 -3.08 -0.73 -0.  ] 