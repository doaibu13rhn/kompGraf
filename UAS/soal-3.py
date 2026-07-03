import matplotlib.pyplot as plt

x = [2,6,4,2]
y = [3,3,7,3]

x2 = [-i for i in y]
y2 = [i for i in x]

plt.figure(figsize=(6,6))

plt.plot(x,y,marker='o',label='Sebelum')
plt.plot(x2,y2,marker='o',label='Sesudah')

plt.grid(True)
plt.axis('equal')
plt.legend()
plt.title("Rotasi 90 Derajat")

plt.show()