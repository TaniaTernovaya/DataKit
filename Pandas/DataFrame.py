import numpy as np
import pandas as pd

data = [{"name": "Rob", "age": 23}, {"name": "Nob"}]

pd_data = pd.DataFrame(data)
print(pd_data)

data1 = np.zeros((3, 2))
pd_data1 = pd.DataFrame(data1)
print(pd_data1)
