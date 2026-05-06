import matplotlib.pyplot as plt

# Data
nama = ["A", "B", "C", "D"]
nilai = [80, 90, 75, 85]

# Plot
plt.bar(nama, nilai)

plt.title("Bar Chart Nilai")
plt.xlabel("Mahasiswa")
plt.ylabel("Nilai")

plt.show()