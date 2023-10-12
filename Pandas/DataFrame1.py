import numpy as np
import pandas as pd


data = pd.DataFrame({"a": i, "b": i + 1} for i in range(10))
print(data)

data1 = pd.DataFrame([{"name": "Tania", "age": 30}, {"name": "Andrew", "age": 30}])
print(data1)

data2 = pd.DataFrame([{"a": 1, "b": 2}, {"b": 3, "c": 4}])
print(data2)

data3 = pd.DataFrame(
    np.random.rand(4, 4), columns=["a", "b", "c", "d"], index=[0, 1, 2, 3]
)

print(data3)
