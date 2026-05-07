import colorsys

# Nilai RGB (0 - 255)
r = 255
g = 100
b = 50

# Konversi ke range 0 - 1
r_norm = r / 255
g_norm = g / 255
b_norm = b / 255

# Konversi RGB ke HSV
h, s, v = colorsys.rgb_to_hsv(r_norm, g_norm, b_norm)

print("RGB :", (r, g, b))
print("HSV :")
print("Hue        :", round(h * 360, 2))
print("Saturation :", round(s * 100, 2), "%")
print("Value      :", round(v * 100, 2), "%")