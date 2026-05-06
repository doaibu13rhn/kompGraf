# Program menghitung nilai akhir mahasiswa

# Input data
nama = input("Masukkan nama mahasiswa: ")
uts = float(input("Masukkan nilai UTS (30%): "))
uas = float(input("Masukkan nilai UAS (40%): "))
tugas = float(input("Masukkan nilai Tugas (20%): "))
hadir = int(input("Jumlah kehadiran (maks 14): "))

# Validasi kehadiran
if hadir > 14:
    print("Jumlah kehadiran tidak boleh lebih dari 14!")
    exit()

# Hitung nilai presensi
nilai_presensi = (hadir / 14) * 100

# Hitung nilai akhir
nilai_akhir = (
    (uts * 0.30) +
    (uas * 0.40) +
    (tugas * 0.20) +
    (nilai_presensi * 0.10)
)

# Menentukan grade
if nilai_akhir >= 85:
    grade = "A"
elif nilai_akhir >= 70:
    grade = "B"
elif nilai_akhir >= 55:
    grade = "C"
elif nilai_akhir >= 40:
    grade = "D"
else:
    grade = "E"

# Output hasil
print("\n===== HASIL =====")
print("Nama Mahasiswa :", nama)
print("Nilai Presensi :", round(nilai_presensi, 2))
print("Nilai Akhir    :", round(nilai_akhir, 2))
print("Grade          :", grade)