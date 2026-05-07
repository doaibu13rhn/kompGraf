import matplotlib.pyplot as plt

# Data koordinat
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 5, 3]

# Membuat garis berwarna
plt.plot(x, y, color='red', linewidth=3)

# Judul dan label
plt.title("Line Coloring")
plt.xlabel("Sumbu X")
plt.ylabel("Sumbu Y")

plt.grid(True)
plt.show()