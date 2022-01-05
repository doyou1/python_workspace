import numpy as np

pred = np.random.uniform(0, 100, (5, ))
print(f"pred: \n{pred}\n")
pred /= pred.sum()

top3_pred = np.sort(pred)[::-1][:3]
top3_indices = np.argsort(pred)[::-1][:3]

print(f"pred_after: \n{pred.round(3)}\n")

print(f"top-3 pred: {top3_pred.round(3)}")

print(f"top-3 indices: {top3_indices}")