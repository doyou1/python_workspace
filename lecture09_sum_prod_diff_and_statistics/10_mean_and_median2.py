import numpy as np

x = np.arange(10)
print(x)    # [0 1 2 3 4 5 6 7 8 9]

mean = np.mean(x)
median = np.median(x)

print(mean) # 4.5
print(median)   # 4.5

x = np.random.randint(1, 11, (5, ))
print(x)    # [2 9 8 4 1]
print(np.sort(x))   # [1 2 4 8 9]

mean = np.mean(x)
median = np.median(x)

print(mean) # 4.8
print(median)   # 4.0

x = np.random.randint(1, 11, (8, ))
print(x)    # [ 5  2  6  9  9  2 10  9]
print(np.sort(x))   # [ 2  2  5  6  9  9  9 10]

mean = np.mean(x)
median = np.median(x)

print(mean) # 6.5
print(median)   # 7.5