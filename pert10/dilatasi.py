import numpy as np
import matplotlib.pyplot as plt

# Membuat persegi
square = np.array([
    [1,1,1],
    [1,3,1],
    [3,3,1],
    [3,1,1],
    [2,2,2]
]).T

# Matriks scaling
S = np.array([
    [2,0,0],
    [0,1.5,0],
    [0,0,1]
])

# Transformasi scaling
scaled_square = S @ square

# Gambar bentuk asli
plt.plot(square[0], square[1], 'b-', label='Asli')

# Gambar hasil scaling
plt.plot(scaled_square[0], scaled_square[1], 'r--', label='Scaling')

plt.axis('equal')
plt.grid(True)
plt.legend()
plt.title("Transformasi Dilatasi")

plt.show()