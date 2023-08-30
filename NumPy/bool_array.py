import pandas as pd
import numpy as np

rng = np.random.RandomState(0)
x = rng.randint(10, size=(3, 4))
temp = np.count_nonzero(x < 6)
temp = np.sum(x < 6, axis=1)
temp = np.all(x < 10)
mac = x[x < 6]
print(mac)
