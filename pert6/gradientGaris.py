import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Membuat garis gradient
for i in range(len(x) - 1):
    plt.plot(x[i:i+2], y[i:i+2], color=(i/100, 0, 1 - i/100))

plt.title("Gradient Line Coloring")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

plt.show()