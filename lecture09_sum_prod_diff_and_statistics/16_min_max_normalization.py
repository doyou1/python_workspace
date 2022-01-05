import numpy as np

means = [50, 60, 70]
stds = [3, 5, 10]
n_student, n_class = 100, 3

scores = np.random.normal(loc=means,
                        scale=stds,
                        size=(n_student, n_class))
scores = scores.astype(np.float32)

scores_max = np.amax(scores, axis=0)
scores_min = np.amin(scores, axis=0)

scores_mM_norm = (scores - scores_min)/(scores_max - scores_min)

scores_max = np.amax(scores_mM_norm, axis=0)
scores_min = np.amin(scores_mM_norm, axis=0)

print(f"Max scores: {scores_max}")  # Max scores: [1. 1. 1.]
print(f"min scores: {scores_min}")  # min scores: [0. 0. 0.]