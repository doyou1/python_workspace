import numpy as np

x = np.random.uniform(-5, 5, (5, ))

np_around = np.around(x, decimals=2)
np_round_ = np.round_(x, decimals=2)
x_round = x.round(decimals=2)

print(f"x: \n{x}\n")
print(f"np_around: \n {np_around}")
print(f"np_round_: \n {np_round_}")
print(f"x_round: \n {x_round}")