import numpy as np

means = [50, 60, 70]
stds = [3, 5, 10]
n_student, n_class = 100, 3

scores = np.random.normal(loc=means,
                        scale=stds,
                        size=(n_student, n_class))
scores = scores.astype(np.float32)

scores_max = np.max(scores, axis=0)
scores_max_idx = np.argmax(scores, axis=0)

print("Max scores: ", scores_max)   # Max scores:  [58.49292  67.746124 96.18393 ]
print("Max indices: ", scores_max_idx)  # Max indices:  [23 50 68]

scores_max_idx = np.argmax(scores, axis=1)
print("Max subjects: ", scores_max_idx.shape, '\n', scores_max_idx) 
# Max subjects: (100,)
# [2 2 2 2 2 2 2 2 2 2 2 1 2 0 2 2 1 2 1 2 2 2 2 2 2 2 2 2 2 
# 2 2 1 2 2 2 2 1
# 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 2 
# 2 1 2 2 2 2 2 2 2 2 2 1 2 2 2 1 1 2 2
# 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 2 2 
# 2 2 2 2 2 2 2 2]