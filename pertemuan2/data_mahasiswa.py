# Program Data Mahasiswa - OOP

class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
    
    def tampilkan_data(self):
        data = f"""
=== DATA MAHASISWA ===
Nama    : {self.nama}
NIM     : {self.nim}
Jurusan : {self.jurusan}
"""
        print(data)

# Membuat minimal 2 objek mahasiswa
mahasiswa1 = Mahasiswa("M. Rifaldo Saputra", "245720111034", "Sistem Informasi")
mahasiswa2 = Mahasiswa("Budi Santoso", "245720111035", "Teknik Informatika")

# Menampilkan data mahasiswa
mahasiswa1.tampilkan_data()
mahasiswa2.tampilkan_data()
