import numpy as np

a = np.arange(6)

# b = np.reshape(a, (9,))
# print("original ndarray: \n", a)
# print("reshaped ndarray: \n", b)
# ValueError: cannot reshape array of size 6 into shape (9,)

b = np.resize(a, (9, ))
print("original ndarray: \n", a)
print("resized ndarray: \n", b) # [0 1 2 3 4 5 0 1 2]

b = np.resize(a, (3, ))
print("original ndarray: \n", a)
print("resized ndarray: \n", b) # [0 1 2]