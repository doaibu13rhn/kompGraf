import matplotlib.pyplot as plt

# Garis awal
x = [2,14]
y = [4,6]

plt.figure(figsize=(6,6))

plt.plot(x,y,label="Sebelum Clipping")

# Window clipping
xmin = 3
xmax = 8
ymin = 2
ymax = 6

# Gambar window
plt.plot([xmin,xmax,xmax,xmin,xmin],
         [ymin,ymin,ymax,ymax,ymin],
         color='red',
         label='Window')

# Hasil clipping
plt.plot([3,8],[4.17,5],
         linewidth=3,
         label="Sesudah Clipping")

plt.grid(True)
plt.axis('equal')
plt.legend()

plt.title("Line Clipping")

plt.show()