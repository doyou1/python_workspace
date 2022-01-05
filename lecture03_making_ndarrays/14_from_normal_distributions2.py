import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(10, 5))

# loc = 분포의 평균, the mean of the distribution
# scale = 분포의 표준편차, the standard deviation of the distribution
# size = 출력 numpy Array의 모양, the shape of the output numpy array
normal1 = np.random.normal(loc=-2, scale=1, size=(200,))
normal2 = np.random.normal(loc=0, scale=2, size=(200,))
normal3 = np.random.normal(loc=3, scale=5, size=(200,))

ax.hist(normal2, bins=20)

plt.show()