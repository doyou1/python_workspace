import numpy as np

a = np.random.uniform(1, 5, (4, ))

log = np.log(a)
exp = np.exp(log)

print(f"a: \n {a.round(3)}")
print(f"log: \n {log.round(3)}")
print(f"exp: \n {exp.round(3)}")
# a: 
#  [1.771 4.448 1.042 4.976]
# log:
#  [0.571 1.492 0.041 1.605]
# exp:
#  [1.771 4.448 1.042 4.976]