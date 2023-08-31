import numpy as np

# a. Create an array with shape (4, 3) of: a. all zeros b. ones c. numbers from 0 to 11
A1 = np.zeros((4, 3))
A2 = np.ones((4, 3))
A3 = np.arange(0, 12).reshape((4, 3))

# b. Tabulate the following function: F(x)=2x^2+5, x∈[1,100] with step 1.

x1 = np.arange(1, 101, 1)
y1 = 2 * (x1**2) + 5

# c. Tabulate the following function: F(x)=e^−x, x∈[−10,10] with step 1.

x2 = np.arange(-10, 11, 1)
y2 = np.exp(-x2)
print(y2)
