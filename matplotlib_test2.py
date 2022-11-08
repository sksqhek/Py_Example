import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(-100,100,1000)
y = np.random.randint(-100,100,1000)
size = np.random.rand(1) * 100

mask1 = abs(x) > 50
mask2 = abs(y) > 75
x = x[mask1 + mask2]
y = y[mask1 + mask2]

plt.scatter(x,y,s = size,c  = x, cmap='jet', alpha=0.7)
plt.colorbar()
plt.show()