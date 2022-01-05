import numpy as np
A = np.arange(18).reshape((2, 3, 3))
B = 10*np.arange(6).reshape((2, 3, 1))
C = A + B

print(C)    # [[[ 0  1  2]
            # [13 14 15]
            # [26 27 28]]

            # [[39 40 41]
            # [52 53 54]
            # [65 66 67]]]