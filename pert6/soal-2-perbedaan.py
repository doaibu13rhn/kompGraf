import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(x, y)

Z = np.sqrt(X**2 + Y**2)

fig, axs = plt.subplots(1, 3, figsize=(12,4))

# Flat shading (warna blok)
axs[0].imshow(Z > 0.5)
axs[0].set_title("Flat Shading")

# Gouraud (smooth interpolation)
axs[1].imshow(Z, interpolation='bilinear')
axs[1].set_title("Gouraud (Smooth)")

# Phong (lebih halus lagi)
axs[2].imshow(Z, interpolation='bicubic')
axs[2].set_title("Phong (More Smooth)")

for ax in axs:
    ax.axis('off')

plt.show()