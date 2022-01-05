import numpy as np

n_student, n_class = 3, 4
m_score, M_score = 0, 100
scores = np.random.randint(low=m_score,
                            high=M_score,
                            size=(n_student, n_class))

mean_class = np.mean(scores, axis=0, keepdims=True)
mean_student = np.mean(scores, axis=1, keepdims=True)

print("scores: \n", scores, "\n")
print("mean_class: \n", mean_class, "\n")
print("mean_student: \n", mean_student, "\n")

# scores: 
#  [[75 65 76 77]
#  [38  4 73 94]
#  [63 54  3 98]]
# mean_class:
#  [[58.66666667 41.         50.66666667 89.66666667]]
# mean_student:
#  [[73.25]
#  [52.25]
#  [54.5 ]]

print("Shapes: ")
print(scores.shape, mean_class.shape, mean_student.shape, '\n')

# Shapes:
# (3, 4) (1, 4) (3, 1)

print("Mean subtraction by classes\n", scores - mean_class, "\n")
print("Mean substraction by students\n", scores - mean_student)

# Mean subtraction by classes  점수들 - 과목별 평균    
#  [[ 16.33333333  24.          25.33333333 -12.66666667]
#  [-20.66666667 -37.          22.33333333   4.33333333]
#  [  4.33333333  13.         -47.66666667   8.33333333]]

# Mean substraction by students 점수들 - 학생별 평균
#  [[  1.75  -8.25   2.75   3.75]    
#  [-14.25 -48.25  20.75  41.75]     
#  [  8.5   -0.5  -51.5   43.5 ]] 