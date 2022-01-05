import numpy as np

p = np.random.uniform(0, 1, (4, ))

be_e = -(p*np.log(p) + (1-p)*np.log(1-p))
be_2 = -(p*np.log(p)/np.log(2) + (1-p)*np.log(1-p)/np.log(2))

print(f"probability: \n {p.round(2)}")
print(f"binary entropy with base e: \n {be_e.round(2)}")
print(f"binary entropy with base 2: \n {be_2.round(2)}")