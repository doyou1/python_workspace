import numpy as np

x = np.random.randint(1, 10, (100, ))

mean = np.mean(x)
median = np.median(x)

print("mean/median: {} / {}".format(mean, median))
# mean/median: 5.3 / 6.0

x = np.append(x, 1000)
mean = np.mean(x)
median = np.median(x)

print("mean/median: {} / {}".format(mean, median))
# mean/median: 15.148514851485148 / 6.0