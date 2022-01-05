import numpy as np

n_test_time, n_student, n_class = 4, 3, 4
m_score, M_score = 0, 100
scores = np.random.randint(low=m_score,
                        high=M_score,
                        size=(n_test_time,
                                n_student,
                                n_class))

print("scores: \n", scores)
# scores: 
#  [[[76 84 62 61]
#   [27 46 13 14]
#   [42 82 22 15]]

#  [[22 46 76 70]
#   [40 92 95 28]
#   [73  2 53  3]]

#  [[95 14 16 97]
#   [21 46 30 22]
#   [ 5  3 94 44]]

#  [[90  4 87 75]
#   [72 76 89 52]
#   [90 73 76 18]]]

score_mean = np.mean(scores, axis=0)
print("score mean: ", score_mean.shape, 
    '\n', score_mean)
# score mean:  (3, 4)
#  [[70.75 37.   60.25 75.75]        
#  [40.   65.   56.75 29.  ]
#  [52.5  40.   61.25 20.  ]]        

score_mean = np.mean(scores, axis=1)
print("score mean: ", score_mean.shape, 
    '\n', score_mean)
# score mean:  (4, 4)
#  [[48.33333333 70.66666667 32.33333333 30.        ]
#  [45.         46.66666667 74.66666667 33.66666667]
#  [40.33333333 21.         46.66666667 54.33333333]
#  [84.         51.         84.      
#    48.33333333]]
