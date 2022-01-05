import numpy as np

dataset = np.empty((0, 4))
print(f"initial shape: {dataset.shape}\n")
# initial shape: (0, 4)

for iter in range(5):
    data_sample = np.random.uniform(0, 5, (1, 4))
    dataset = np.vstack((dataset, data_sample))
    print(f"iter/shape: {iter}/{dataset.shape}")
# iter/shape: 0/(1, 4)
# iter/shape: 1/(2, 4)
# iter/shape: 2/(3, 4)
# iter/shape: 3/(4, 4)
# iter/shape: 4/(5, 4)
