import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import colorsys

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.3)

color_display = plt.Rectangle((0,0), 1, 1)
ax.add_patch(color_display)
ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.axis('off')

# Slider
ax_h = plt.axes([0.2, 0.2, 0.65, 0.03])
ax_s = plt.axes([0.2, 0.15, 0.65, 0.03])
ax_v = plt.axes([0.2, 0.1, 0.65, 0.03])

slider_h = Slider(ax_h, 'Hue', 0, 1, valinit=0)
slider_s = Slider(ax_s, 'Sat', 0, 1, valinit=1)
slider_v = Slider(ax_v, 'Val', 0, 1, valinit=1)

def update(val):
    h = slider_h.val
    s = slider_s.val
    v = slider_v.val
    
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    color_display.set_color((r, g, b))
    fig.canvas.draw_idle()

slider_h.on_changed(update)
slider_s.on_changed(update)
slider_v.on_changed(update)

plt.show()