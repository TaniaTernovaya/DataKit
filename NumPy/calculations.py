import numpy as np
import random
from scipy import special

np.random.seed(0)


def function(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1 / values[i]
    return output


values = np.random.randint(1, 10, size=5)


x1 = np.arange(5)
x2 = np.array([2, 3, 4, 5, 6])

theta = np.linspace(0, np.pi, 3)
print(np.sin(theta))

print("gamma(x)     =", special.gamma(x))
print("ln|gamma(x)| =", special.gammaln(x))
print("beta(x, 2)   =", special.beta(x, 2))
