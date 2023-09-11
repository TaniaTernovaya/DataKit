import numpy as np

x = np.array([1, 2, 3, 5, 6, 6]).reshape(2, 3)
y = x > 3
print(x[y])
