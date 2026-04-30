import numpy as np
import matplotlib.pyplot as plt

width, height = 400, 400

gradient = np.zeros((height, width, 3))

for x in range(width):
    for y in range(height):
        gradient[y, x, 0] = x / width     # Red
        gradient[y, x, 2] = y / height    # Blue

plt.imshow(gradient)
plt.title("Gradient RGB")
plt.axis("off")
plt.show()