import matplotlib.pyplot as plt


def bresenham(x1, y1, x2, y2):
    x_points = []
    y_points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    x = x1
    y = y1

    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    if dx > dy:
        err = dx / 2.0

        while x != x2:
            x_points.append(x)
            y_points.append(y)

            err -= dy
            if err < 0:
                y += sy
                err += dx

            x += sx
    else:
        err = dy / 2.0

        while y != y2:
            x_points.append(x)
            y_points.append(y)

            err -= dx
            if err < 0:
                x += sx
                err += dy

            y += sy

    x_points.append(x2)
    y_points.append(y2)

    return x_points, y_points


# Titik awal dan akhir
x1, y1 = 2, 2
x2, y2 = 15, 10

x, y = bresenham(x1, y1, x2, y2)

# Visualisasi
plt.plot(x, y, marker='s')
plt.title("Algoritma Bresenham")
plt.grid(True)
plt.show()