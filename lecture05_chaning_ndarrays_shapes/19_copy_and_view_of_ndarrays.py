import numpy as np

a = np.arange(5)
b = a.view()    # 기존의 Memory 사용

b[0] = 100

print(a)    # [100   1   2   3   4]
print(b)    # [100   1   2   3   4]

#=====================#

a = np.arange(5)
b = a[0:3]      # view()와 동일

b[...] = 10

print(a)    # [10 10 10  3  4]
print(b)    # [10 10 10]

#=====================#
a = np.arange(5)
b = a.copy()    # Memory 새로 추가

b[0] = 100
print(a)    # [0 1 2 3 4]
print(b)    # [100   1   2   3   4]