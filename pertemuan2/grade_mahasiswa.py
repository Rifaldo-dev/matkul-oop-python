# Program Grade Nilai Mahasiswa - OOP

class NilaiOOP:
    def __init__(self, nama, nim, nilai_akhir):
        self.nama = nama
        self.nim = nim
        self.nilai_akhir = nilai_akhir
    
    def tentukan_grade(self):
        if self.nilai_akhir >= 85:
            return "A"
        elif self.nilai_akhir >= 75:
            return "B"
        elif self.nilai_akhir >= 65:
            return "C"
        elif self.nilai_akhir >= 50:
            return "D"
        else:
            return "E"
    
    def tampilkan(self):
        grade = self.tentukan_grade()
        data = f"""
=== DATA MAHASISWA ===
Nama        : {self.nama}
NIM         : {self.nim}
Nilai Akhir : {self.nilai_akhir}
Grade       : {grade}
"""
        print(data)

# Membuat objek mahasiswa
mahasiswa1 = NilaiOOP("M. Rifaldo Saputra", "245720111034", 87)
mahasiswa2 = NilaiOOP("Budi Santoso", "245720111035", 78)
mahasiswa3 = NilaiOOP("Siti Aminah", "245720111036", 65)

# Menampilkan data
mahasiswa1.tampilkan()
mahasiswa2.tampilkan()
mahasiswa3.tampilkan()
