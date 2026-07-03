import matplotlib.pyplot as plt

x = [2,8,8,2,2]
y = [1,1,6,6,1]

sx = 4
sy = 3

x2 = [i*sx for i in x]
y2 = [j*sy for j in y]

plt.figure(figsize=(6,6))

plt.plot(x,y,marker='o',label='Sebelum')
plt.plot(x2,y2,marker='o',label='Sesudah')

plt.grid(True)
plt.axis('equal')
plt.legend()
plt.title("Scaling")

plt.show()