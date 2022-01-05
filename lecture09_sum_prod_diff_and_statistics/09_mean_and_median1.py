import numpy as np

np.random.seed(0)

x = np.random.randint(1, 10, (5, ))
w = np.array([1,2,3,4,5])

print(np.average(x, weights=w)) # 5.066666666666666
print(np.sum(w*x)/np.sum(w))    # 5.066666666666666