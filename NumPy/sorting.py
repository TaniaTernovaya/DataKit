import numpy as np
import matplotlib.pyplot as plt
import seaborn
import random as rand

seaborn.set()


def selection_sort(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x


x = np.array([2, 3, 5, 67, 8])
print(selection_sort(x))

c = np.array([2, 5, 6, 7, 7, 7, 8, 9, 9, 9, 12, 12, 34])
print(np.partition(c, 7))
X = random.random(10, 2)
plt.scatter(X[:, 0], X[:, 1], s=100)
