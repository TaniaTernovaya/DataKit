import numpy as np
import pandas as pd

ind1 = pd.Index([1, 2, 3, 5, 6, 7, 8, 8])
ind2 = pd.Index([3, 4, 5, 6, 7, 8, 9, 9])

a = ind2 & ind1
print(a)
b = ind1 | ind2
print(b)
