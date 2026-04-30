# Membuat Dictionary (Object) menggunakan kurung kurawal {}
# Formatnya: "key": "value"
driver = {
    "nama": "Andi",
    "kendaraan": "Vario 150",
    "rating": 4.9,
    "aktif": True
}

# Cara aksesnya panggil "Key" nya
print(f"Nama Driver: {driver['nama']}")
print(f"Rating: {driver['rating']}")

# Menambah properti baru
driver["total_order"] = 150

# Mengubah nilai
driver["rating"] = 5.0

print(f"Data Driver lengkap: {driver}")