import numpy as np
import random

grid = np.arange(1, 10).reshape((3, 3))

x = np.array([1, 2, 3]).reshape(3, 1)

a = np.array([1, 2, 3, 4, 5])
b = np.array([3, 4, 5])
print(np.concatenate([a, b]))
