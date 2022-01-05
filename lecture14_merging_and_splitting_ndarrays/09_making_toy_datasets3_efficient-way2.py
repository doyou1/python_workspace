import numpy as np

dataset_tmp = list()
for iter in range(100):
    data_sample = np.random.uniform(0, 5, (1, 4))
    dataset_tmp.append(data_sample)

dataset = np.vstack(dataset_tmp)
print(f"final shape: {dataset.shape}")
# final shape: (100, 4)