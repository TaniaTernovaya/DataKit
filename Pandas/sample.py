import numpy as np
import pandas as pd
import random


random.seed(3)
data = pd.Series(np.random.rand(1000), index=np.arange(1000))

print(data[9:])
print(data[(data > 0.3) & (data < 0.8)])

print(data.loc[3:5])
print(data.iloc[3:5])

data1 = pd.Series(np.random.rand(5), index=["a", "b", "c", "d", "e"])
print(data1.loc["a":"c"])
print(data1.iloc[2:4])


names = pd.Series({"Ternovaya": "Tania", "Krupskii": "Andii", "Yakimenko": "Inna"})
ages = pd.Series({"Ternovaya": 30, "Krupskii": 30, "Yakimenko": 32})
data2 = pd.DataFrame({"names": names, "age": ages})
data2["colour"] = pd.Series(
    {"Ternovaya": "red", "Krupskii": "blue", "Yakimenko": "yellow"}
)
data2["score"] = pd.Series({"Ternovaya": 13, "Krupskii": 34, "Yakimenko": 33})
print(data2)
print(data2["names"])
print(data2.names)
print(data2.T)
print(data2.iloc[:2, :1])
print(data2.loc[data2.score > 13, ["names"]])
