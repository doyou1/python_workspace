import numpy as np

normal = np.random.normal(size=(50, 50, 32, 5))

m_cap = normal.size * normal.itemsize
print("{}B/{}B".format(m_cap, normal.nbytes))