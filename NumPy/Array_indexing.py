import numpy as np
import random

np.random.seed(12)

x1 = np.random.randint(10, size=6)
x2 = np.random.randint(10, size=(3, 4))

x = np.arange(10)
x2_change = x2[:2, :2]
x2_change[0, 0] = 99
print(x2)


L = [2, 3, 4, 5, 6, 7]
L_change = L[:4]
L_change[0] = 99
print(L_change)
