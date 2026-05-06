import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# Tiga lingkaran RGB
circle1 = plt.Circle((0.3, 0.5), 0.2, color='red')
circle2 = plt.Circle((0.5, 0.5), 0.2, color='green')
circle3 = plt.Circle((0.7, 0.5), 0.2, color='blue')

ax.add_patch(circle1)
ax.add_patch(circle2)
ax.add_patch(circle3)

ax.set_aspect('equal')
plt.title("RGB Color Model")
plt.axis('off')
plt.show()