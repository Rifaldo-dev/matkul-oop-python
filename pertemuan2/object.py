# 3. Program Biodata dengan Object (OOP)
# Menggunakan konsep Object-Oriented Programming
# Data dan fungsi digabung dalam satu class

# Membuat class Biodata
class Biodata:
    # Constructor untuk inisialisasi atribut
    def __init__(self, nama, nim, jurusan):
        self.nama = nama        # Atribut nama
        self.nim = nim          # Atribut nim
        self.jurusan = jurusan  # Atribut jurusan
    
    # Method untuk menampilkan biodata
    def tampilkan(self):
        biodata = f"""
=== BIODATA ===
Nama: {self.nama}
NIM: {self.nim}
Jurusan: {self.jurusan}
"""
        print(biodata)

# Membuat object dari class Biodata
mahasiswa = Biodata("M. Rifaldo Saputra", "245720111034", "Sistem Informasi")

# Memanggil method tampilkan()
mahasiswa.tampilkan()
