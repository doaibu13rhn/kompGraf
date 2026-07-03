import matplotlib.pyplot as plt

# Koordinat awal
x = [3, 7, 4, 3]
y = [2, 5, 8, 2]

# Translasi
tx = 5
ty = -3

x2 = [i + tx for i in x]
y2 = [j + ty for j in y]

plt.figure(figsize=(6,6))

plt.plot(x, y, marker='o', label='Sebelum')
plt.plot(x2, y2, marker='o', label='Sesudah')

plt.grid(True)
plt.axis('equal')
plt.legend()
plt.title("Transformasi Translasi")

plt.show()