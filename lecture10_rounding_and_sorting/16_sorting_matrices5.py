import numpy as np

scores = np.random.randint(0, 100, (5, 3))

sort = np.sort(scores, axis=1)
argsort = np.argsort(scores, axis=1)

# 학생마다 bottom2 과목의 점수들
bottom2_scores = sort[:, :2]

# 학생마다 bottom2 과목
bottom2_subjects = argsort[:, :2]

print(f"scores: \n{scores}\n")
# scores: 
# [[46 20 32]
#  [57 91 94]
#  [ 8 50 56]
#  [94 78  2]
#  [37 71 28]]

print(f"sort: \n{sort}")
print(f"argsort: \n{argsort}\n")
# sort:
# [[20 32 46]
#  [57 91 94]
#  [ 8 50 56]
#  [ 2 78 94]
#  [28 37 71]]
# argsort:
# [[1 2 0]
#  [0 1 2]
#  [0 1 2]
#  [2 1 0]
#  [2 0 1]]

print(f"bottom-2 scores: \n{bottom2_scores}")
print(f"bottom-2 subjects: \n{bottom2_subjects}")
# bottom-2 scores:
# [[20 32]
#  [57 91]
#  [ 8 50]
#  [ 2 78]
#  [28 37]]
# bottom-2 subjects:
# [[1 2]
#  [0 1]
#  [0 1]
#  [2 1]
#  [2 0]]