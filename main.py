import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib.widgets import Slider
import graph

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


g = graph.Graaf(ax)

ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])

axcolor = 'lightgoldenrodyellow'
ax_A = plt.axes([0.2, 0.05, 0.65, 0.03], facecolor=axcolor)
ax_B = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor=axcolor)
ax_C = plt.axes([0.2, 0.15, 0.65, 0.03], facecolor=axcolor)
ax_D = plt.axes([0.2, 0.2, 0.65, 0.03], facecolor=axcolor)

slider_A = Slider(ax_A, 'A', -10, 10, valinit=1, valstep=0.1)
slider_B = Slider(ax_B, 'B', -10, 10, valinit=1, valstep=0.1)
slider_C = Slider(ax_C, 'C', -10, 10, valinit=1, valstep=0.1)
slider_D = Slider(ax_D, 'D', -10, 10, valinit=0, valstep=0.1)

def update(val):
    ax.clear()
    A = slider_A.val
    B = slider_B.val
    C = slider_C.val
    D = slider_D.val    
    g.tasand(A, B, C, D)
    g.vektor(A, B, C)
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_zlim([-10, 10])
    plt.draw()

slider_A.on_changed(update)
slider_B.on_changed(update)
slider_C.on_changed(update)
slider_D.on_changed(update)

update(0)

plt.show()