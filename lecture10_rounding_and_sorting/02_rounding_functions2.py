import numpy as np

scores = np.random.uniform(0, 100, (100, 5))

means = scores.mean(axis=0)
stds = scores.std(axis=0)

print(f"class means: \n {means}")
print(f"class stds: \n {stds}\n")

print(f"class means: \n {means.round(2)}")
print(f"class stds: \n {stds.round(2)}")
