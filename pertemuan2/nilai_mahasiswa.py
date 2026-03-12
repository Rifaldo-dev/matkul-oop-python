# Program Nilai Akhir Mahasiswa - OOP

class NilaiMahasiswa:
    def __init__(self, nama, nim, nilai_tugas, nilai_uts, nilai_uas):
        self.nama = nama
        self.nim = nim
        self.nilai_tugas = nilai_tugas
        self.nilai_uts = nilai_uts
        self.nilai_uas = nilai_uas
    
    def hitung_nilai_akhir(self):
        # Rumus: 30% Tugas + 30% UTS + 40% UAS
        nilai_akhir = (0.3 * self.nilai_tugas) + (0.3 * self.nilai_uts) + (0.4 * self.nilai_uas)
        return nilai_akhir
    
    def tampilkan(self):
        nilai_akhir = self.hitung_nilai_akhir()
        data = f"""
=== DATA NILAI MAHASISWA ===
Nama        : {self.nama}
NIM         : {self.nim}
Nilai Akhir : {nilai_akhir}
"""
        print(data)

# Membuat objek mahasiswa
mahasiswa1 = NilaiMahasiswa("M. Rifaldo Saputra", "245720111034", 85, 80, 90)
mahasiswa2 = NilaiMahasiswa("Budi Santoso", "245720111035", 75, 85, 80)

# Menampilkan data
mahasiswa1.tampilkan()
mahasiswa2.tampilkan()
