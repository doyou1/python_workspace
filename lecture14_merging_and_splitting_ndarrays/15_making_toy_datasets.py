import numpy as np

dataset_tmp = list()
for iter in range(100):
    data_sample = np.random.uniform(0, 5, (1, 4))
    dataset_tmp.append(data_sample)

concat = np.concatenate(dataset_tmp, axis=0)
print(f"concat: {concat.shape}")
# concat: (100, 4)

dataset_tmp = list()
for iter in range(100):
    data_sample = np.random.uniform(0, 5, (4, 1))
    dataset_tmp.append(data_sample)

concat = np.concatenate(dataset_tmp, axis=1)
print(f"concat: {concat.shape}")
# concat: (4, 100)