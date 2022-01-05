import numpy as np

a = np.arange(12).reshape((3, -1))

sum_class = np.sum(a, axis=0, keepdims=True)
sum_student = np.sum(a, axis=1, keepdims=True)

print("scores: {}\n{}".format(a.shape, a))
print("sum_class: {}\n{}".format(sum_class.shape, sum_class))
print("sum_student: {}\n{}".format(sum_student.shape, sum_student))

print(sum_class + sum_student) # Ok
# scores: (3, 4)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
# sum_class: (1, 4)
# [[12 15 18 21]]
# sum_student: (3, 1)
# [[ 6]
#  [22]
#  [38]]