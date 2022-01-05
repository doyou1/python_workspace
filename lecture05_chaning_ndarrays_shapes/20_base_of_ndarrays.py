import numpy as np

a = np.arange(5)
b = a.copy()    # 새로운 Memory 사용
c = a.view()    # 기존의 Memory 사용
d = a[0:3]      # view()와 동일

print(a.base is None)  # True

print(b.base is None)  # True
print(b.base is a)  # False

print(c.base is a)  # True
print(d.base is a)  # True