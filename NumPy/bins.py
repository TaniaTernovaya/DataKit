import numpy as np
import random
import matplotlib.pyplot as plt


np.random.seed(42)
x = np.random.randn(10)
print(x)
bins = np.linspace(-5, 5, 20)
plt.hist(x, bins, histtype="step")
plt.show()
