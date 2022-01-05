import numpy as np

a = np.random.uniform(1, 5, (4, ))

log2 = np.log(2)/np.log(2)
log3 = np.log(2)/np.log(3)
log5 = np.log(a)/np.log(5)

# logab = logcb/logca
print(f"log2: \n {log2.round(3)}")
print(f"log3: \n {log3.round(3)}")
print(f"log5: \n {log5.round(3)}")