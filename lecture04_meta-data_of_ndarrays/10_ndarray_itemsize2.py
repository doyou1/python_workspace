import numpy as np

normal = np.random.normal(size=(50, 50, 32, 5))

print("size:", normal.size)
print("dtype/itemsize: {}/{}\n".format(normal.dtype, normal.itemsize))

m_cap = normal.size * normal.itemsize

print("Memory capacity in B: {}B".format(m_cap))
print("Memory capacity in KB: {}KB".format(m_cap/1024))
print("Memory capacity in MB: {}MB".format(m_cap/1024**2))
