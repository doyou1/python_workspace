import numpy as np

x = np.random.uniform(-5, 5, (4, 2))
y = np.random.uniform(-5, 5, (3, 2))

X = np.expand_dims(x, axis=1)
Y = np.expand_dims(y, axis=0)

Z = np.sqrt(np.sum(np.square(X - Y), axis=-1))
print(f"Z: {Z.shape}\n{Z}")
# Z: (4, 3)
# [[3.46806092 2.99221503 0.30771088]  
#  [6.36173824 7.14193157 9.27897598]  
#  [4.69535882 3.39561684 6.30554344]  
#  [4.67200307 3.46345844 6.34746734]]