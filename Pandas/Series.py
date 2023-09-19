import numpy as np
import pandas as pd

data = pd.Series([2, 56, 6], index=["a", "b", "c"])
print(data)


grades = {"Anna": 3, "Tamara": 4, "Sebastian": 5}
grades_pd = pd.Series(grades)
print(grades_pd[:-1])

money = pd.Series(np.array([2, 3, 45, 67, 78, 90]))
print(money)
