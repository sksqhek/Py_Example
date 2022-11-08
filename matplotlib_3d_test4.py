
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

fig = plt.figure(figsize=(8, 4))

ax1 = fig.add_subplot(121)
def f(x, y): return (1 - x / 2 + x**5 + y**3) * np.exp(-(x**2) - y**2)


x = np.linspace(-3, 3, 256)
y = np.linspace(-3, 3, 256)
xv, yv = np.meshgrid(x, y)

zv = f(xv, yv)
plt.imshow(zv, cmap="jet")
zv1 = plt.contour(x, y, zv)
plt.contour((xv + 3) / 6 * 256, (yv + 3) / 6 * 256, zv)
plt.clabel(zv1, fontsize=10)

# 3D contour


def f(x, y):
   return np.sin(x) * np.exp(-x**2 - y**2)


x = np.linspace(-4, 4, 100)
y = np.linspace(-4, 4, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

ax2 = fig.add_subplot(122, projection="3d")
ax2.plot_surface(X, Y, Z, cmap="jet", lw=0.5, rstride=1, cstride=1, alpha=0.5)
ax2.contour3D(X, Y, Z, 50, cmap="jet")
# ax2.set_xlabel("x")
# ax2.set_ylabel("y")
# ax2.set_zlabel("z")

plt.show()
