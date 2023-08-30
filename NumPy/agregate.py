import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn

seaborn.set()

# data = pd.read_csv("president_heights.csv")
# heights = np.array(data["height(cm)"])
# print(f"Mean height:{heights.mean()}")
# print(f"Max height:{heights.max()}")
# print(f"Min height:{heights.min()}")
# print(f"Standard Deviation of Mean:{heights.std()}")
# plt.hist(heights)
# plt.title("Height Distribution of US Presidents")
# plt.xlabel("height (cm)")
# plt.ylabel("number")
M = np.random.random((10, 3))
mean_ = M.mean(0)
X_centr = M - mean_
mean1_ = X_centr.mean(0)
x = np.linspace(-5, 5, 100)  # Изменил интервал для параболы
y = x**2  # Уравнение параболы

# plt.plot(x, y)
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("Парабола: y = x^2")
# plt.grid(True)
# plt.show()
x = np.array([1, 2, 3, 4, 5, 6])
print(x < 3)
