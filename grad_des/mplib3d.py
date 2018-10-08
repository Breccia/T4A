#!/Users/piccolo/anaconda3/bin/python

import pandas as pd
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')

x = np.linspace(1, 7, 100)
y = np.sin(x)
#y = np.linspace(4, -4, 30)
xx, yy = np.meshgrid(x, y)

z = np.cos(xx) * np.sin(yy)

ax.contour3D(x,y,z, 60)
#ax.view_init(55,90)
plt.show()

