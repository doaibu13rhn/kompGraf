# Contoh For Loop: Menghitung 1 sampai 5
print("Hitung mundur:")
for i in range(5, 0, -1):
    print(i)

# Contoh While Loop: Berhenti kalau user ketik 'n'
status = "y"
while status == "y":
    print("Program sedang berjalan...")
    status = input("Lanjut lagi? (y/n): ")