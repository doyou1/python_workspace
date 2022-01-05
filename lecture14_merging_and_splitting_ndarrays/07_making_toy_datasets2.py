import numpy as np

dataset = np.empty((4, 0))
print(f"initial shape: {dataset.shape}\n")
# initial shape: (4, 0)

for iter in range(5):
    data_sample = np.random.uniform(0, 5, (4, 1))
    dataset = np.hstack((dataset, data_sample))
    print(f"iter/sample: {iter}/{dataset.shape}")
# iter/sample: 0/(4, 1)
# iter/sample: 1/(4, 2)
# iter/sample: 2/(4, 3)
# iter/sample: 3/(4, 4)
# iter/sample: 4/(4, 5)