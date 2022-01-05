import numpy as np

scores = np.random.randint(0, 100, (5, 3))

sort = np.sort(scores, axis=0)[::-1, :]
argsort = np.argsort(scores, axis=0)[::-1, :]

# 과목의 top2 고득점
top2_scores = sort[:2, :]
# 과목의 top2 고득점한 학생의 인덱스
top2_students = argsort[:2, :]

print(f"scores: \n{scores}\n")
# scores: 
# [[ 3 57 97]
#  [21 63 73]
#  [33 71 83]
#  [37 49 86]
#  [10 48 71]]

print(f"sort: \n{sort}")
print(f"argsort: \n{argsort}\n")
# sort:
# [[37 71 97]
#  [33 63 86]
#  [21 57 83]
#  [10 49 73]
#  [ 3 48 71]]
# argsort:
# [[3 2 0]
#  [2 1 3]
#  [1 0 2]
#  [4 3 1]
#  [0 4 4]]

print(f"top-2 scores: \n{top2_scores}")
print(f"top-2 students: \n{top2_students}")
# top-2 scores:
# [[37 71 97]
#  [33 63 86]]
# top-2 students:
# [[3 2 0]
#  [2 1 3]]