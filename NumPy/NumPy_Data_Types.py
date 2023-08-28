import numpy as np
import random

np.random.seed(12)

x1 = np.random.randint(10, size=6)
x2 = np.random.randint(10, size=(3, 4))
x3 = np.random.randint(10, size=(3, 4, 5))
print(x2)
print(f"размерность: {x2.ndim}")
print(f"размер каждого измерения: {x2.shape}")
print(f"общий размер массива: {x2.size}")
print(f"тип данных массива: {x2.dtype}")
print(f"размер (в байтах) кадого элемента массива: {x2.itemsize}")
print(f"размер (в байтах) всего массива: {x2.nbytes}")
