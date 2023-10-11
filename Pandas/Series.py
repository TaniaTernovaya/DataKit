import numpy as np
import pandas as pd

data = pd.Series([2, 3, 4, 4, 5, 5, 5, 6])
print(data.values)
print(data.index)

data1 = pd.Series([1, 2, 4, 5, 6])
print(data1[1])
print(data1[3:])
print(data1[1:3])


population_dict = {"California": 786, "NewYoork": 7654, "Virginia": 753212345}
data2 = pd.Series(population_dict)
print(data2)
print(data2["California":"NewYoork"])

data3 = pd.Series("tania", index=np.arange(10))
print(data3)
