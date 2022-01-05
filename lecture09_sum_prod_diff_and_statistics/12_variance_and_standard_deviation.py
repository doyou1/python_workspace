import numpy as np

scores = np.random.normal(loc=10,
                        scale=5,
                        size=(100, ))

var = scores.var()
std = scores.std()

print(f"scores: \n{scores}\n")

print("variance: ", var)
print("standard deviation: ", std, '\n')

print("square of std: ", std**2)
print("square root of var: ", var**0.5)