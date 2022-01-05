import numpy as np

a = np.random.randint(0, 10, (1, 4))
b = np.random.randint(0, 10, (1, 4))
c = np.random.randint(0, 10, (1, 4))

arr_list = [a, b, c]
print(arr_list)
# [array([[9, 8, 8, 1]]), array([[8, 5, 2, 2]]), array([[0, 0, 2, 1]])]     
vstack = np.vstack(arr_list)
hstack = np.hstack(arr_list)

print(f"a: {a.shape}\n{a}")
print(f"b: {b.shape}\n{b}")
print(f"c: {c.shape}\n{c}")
# a: (1, 4)
# [[9 8 8 1]]
# b: (1, 4)
# [[8 5 2 2]]
# c: (1, 4)
# [[0 0 2 1]]

print(f"vstack: {vstack.shape}\n{vstack}")
print(f"hstack: {hstack.shape}\n{hstack}")
# vstack: (3, 4)
# [[9 8 8 1]
#  [8 5 2 2]
#  [0 0 2 1]]
# hstack: (1, 12)
# [[9 8 8 1 8 5 2 2 0 0 2 1]]
print(np.squeeze(hstack))   # [9 8 8 1 8 5 2 2 0 0 2 1]
print(np.squeeze(hstack).shape) # (12, )