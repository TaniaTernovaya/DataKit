import numpy as np
import pandas as pd
import random


A = pd.Series([2, np.nan, 3, np.nan])
print(A)


df = pd.DataFrame([[2, 3, 4, None, 2], [1, 2, 3, 4, None], [None, 2, 4, -2, 0]])
print(df)
print(df.dropna())
