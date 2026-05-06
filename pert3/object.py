class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    def tampilkan(self):
        print("Nama:", self.nama)
        print("Nilai:", self.nilai)

# Membuat object
mhs1 = Mahasiswa("Raihan", 90)
mhs1.tampilkan()