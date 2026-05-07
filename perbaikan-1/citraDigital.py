import cv2
import matplotlib.pyplot as plt

# BACA GAMBAR
img = cv2.imread("images/helm-gojek.png")

if img is None:
    print("Images not found!")
    exit()

# GRAYSCALE
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# CANNY EDGE DETECTION
edges = cv2.Canny(gray, 100, 200)

# SIMPAN HASIL
cv2.imwrite("output/hasil_canny.png", edges)

# TAMPILKAN HASIL
plt.figure(figsize=(10,5))

# gambar asli
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Real image")
plt.axis("off")

# hasil canny
plt.subplot(1,2,2)
plt.imshow(edges, cmap='gray')
plt.title("Canny result")
plt.axis("off")

plt.show()