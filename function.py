# Membuat fungsi bernama 'sapa'
def sapa_user(nama, waktu):
    return f"Selamat {waktu}, {nama}! Selamat coding."

# Memanggil fungsi
pesan = sapa_user("Bro", "Malam")
print(pesan)