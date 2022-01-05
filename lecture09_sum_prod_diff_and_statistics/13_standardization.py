import numpy as np

means = [50, 60, 70]
stds = [3, 5, 10]

n_student, n_class = 100, 3

scores = np.random.normal(loc=means,
                        scale=stds,
                        size=(n_student, n_class))
scores = scores.astype(np.float32)

print(f"scores: \n{scores}\n")

print("shape of scores: ", scores.shape)
print("dtype of scores: ", scores.dtype)

means = scores.mean(axis=0)
stds = scores.std(axis=0)

print("means before stdz: \n", means)
print("stds before stdz: \n", stds, '\n')

score_stdz = (scores - means)/stds

means_stdz = score_stdz.mean(axis=0)
stds_stdz = score_stdz.std(axis=0)

print("means after stdz: \n", means_stdz)
print("stds after stdz: \n", stds_stdz)