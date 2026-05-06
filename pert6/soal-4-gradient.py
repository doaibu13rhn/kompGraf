import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

colors = ["red", "yellow", "green", "blue"]
cmap = LinearSegmentedColormap.from_list("custom", colors)

gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))

plt.imshow(gradient, aspect='auto', cmap=cmap)
plt.title("Custom Gradient")
plt.axis('off')
plt.show()