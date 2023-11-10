import numpy as np
import pandas as pd

rng = np.random.RandomState(4)
ser = pd.Series(rng.randint(0, 10, 4))
df = pd.DataFrame(rng.randint(0, 100, (3, 4)), columns=["a", "b", "c", "d"])
calc1 = np.sin(df * np.pi / 4)
print(df)
print(calc1)

A = pd.DataFrame(rng.randint(0, 20, (2, 2)), columns=list("AB"))
B = pd.DataFrame(rng.randint(0, 10, (3, 3)), columns=list("ABC"))
print(A)
print(B)
print(A + B)

df = pd.DataFrame(rng.randint(0, 10, (4, 3)), columns=list("ABC"))
print(df)
print(df.iloc[0])
print(df - df.iloc[0])
print(df.subtract(df["B"], axis=0))


print(df.iloc[1:, 1:])

