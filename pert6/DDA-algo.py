import matplotlib.pyplot as plt


def dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))

    x_increment = dx / steps
    y_increment = dy / steps

    x = x1
    y = y1

    x_points = []
    y_points = []

    for _ in range(steps + 1):
        x_points.append(round(x))
        y_points.append(round(y))

        x += x_increment
        y += y_increment

    return x_points, y_points


# Titik awal dan akhir
x1, y1 = 2, 3
x2, y2 = 15, 10

x, y = dda(x1, y1, x2, y2)

# Visualisasi
plt.plot(x, y, marker='o')
plt.title("Algoritma DDA")
plt.grid(True)
plt.show()