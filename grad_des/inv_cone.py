#!/Users/piccolo/anaconda3/bin/python

from matplotlib import pyplot as p
from mpl_toolkits.mplot3d import Axes3D    # @UnusedImport

import numpy as np
from math import pi, cos, sin

z = np.arange(0, 6, 1)
print(len(z))
theta = np.arange(0, 2 * pi + pi / 50, pi / 50)

fig = p.figure()
axes1 = fig.add_subplot(111, projection='3d')
clist = ['red', 'red', 'orange', 'yellow', 'green', 'blue']
ltxt = ['', 'Self-Actualization', 'Esteem', 'Social belonging', 'Safety needs', 'Physiological needs']
for idx,zval in enumerate(z):
    print(idx)
    x = zval * np.array([cos(q) for q in theta])
    y = zval * np.array([sin(q) for q in theta])
    axes1.plot(x, y, -zval, color=clist[idx], label=ltxt[idx], linewidth=3)
axes1.set_xlabel("x label")
axes1.set_ylabel("y label")
axes1.set_zlabel("z label")
axes1.legend()

axes1.invert_zaxis()

p.show()

