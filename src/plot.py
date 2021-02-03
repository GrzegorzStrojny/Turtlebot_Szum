from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

x = np.arange(0,10,0.1)
y = np.arange(0,10,0.1)

xx, yy = np.meshgrid(x,y,sparse=True)

#z = -xx**2*np.cos(yy)**2

#surf = ax.plot_surface(xx, yy, z, cmap=cm.coolwarm,linewidth=0, antialiased=False)

#plt.show()

z = -xx**2*np.cos(yy)**2-yy**2

surf = ax.plot_surface(xx, yy, z, cmap=cm.coolwarm,linewidth=0, antialiased=False)

plt.show()
