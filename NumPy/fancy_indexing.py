import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn


seaborn.set()
x = np.array([1, 2, 3, 5, 6, 6]).reshape(2, 3)
y = x > 3
print(x[y])

mean = [0, 0]
cov = [[1, 2], [2, 5]]
r = np.random.multivariate_normal(mean, cov, 100)
r.shape
plt.scatter(r[:, 0], r[:, 1])
