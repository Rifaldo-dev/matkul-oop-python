"""
Program Manajemen Data Mahasiswa
Program ini menggunakan konsep OOP (Object-Oriented Programming) untuk mengelola data mahasiswa
"""

class Mahasiswa:
    """
    Class Mahasiswa untuk merepresentasikan data mahasiswa
    Atribut: nim, nama, jurusan, nilai
    """
    
    def __init__(self, nim, nama, jurusan, nilai):
        """
        Constructor/konstruktor untuk membuat objek mahasiswa baru
        Parameter:
        - nim: Nomor Induk Mahasiswa
        - nama: Nama lengkap mahasiswa
        - jurusan: Jurusan mahasiswa
        - nilai: Nilai mahasiswa (float)
        """
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.nilai = nilai
    
    def tampilkan_info(self):
        """
        Fungsi untuk menampilkan informasi mahasiswa dalam format tab-separated
        Mencetak nim, nama, jurusan, dan nilai ke layar
        """
        print(f"{self.nim}\t{self.nama}\t{self.jurusan}\t{self.nilai}")
    
    def cek_status(self):
        """
        Fungsi untuk menentukan grade/status berdasarkan nilai mahasiswa
        Sistem penilaian:
        - Nilai >= 80: Grade "A"
        - Nilai >= 70: Grade "B" 
        - Nilai >= 60: Grade "C"
        - Nilai >= 50: Grade "D"
        - Nilai < 50: Grade "E"
        
        Returns:
        - String: Grade mahasiswa (A, B, C, D, atau E)
        """
        if self.nilai >= 80:
            return "A"
        elif self.nilai >= 70:
            return "B"
        elif self.nilai >= 60:
            return "C"
        elif self.nilai >= 50:
            return "D"
        else:
            return "E"

def main():
    """
    Fungsi utama yang mengatur alur program
    - Mengumpulkan data mahasiswa dari user
    - Membuat objek Mahasiswa untuk setiap data
    - Menampilkan semua data mahasiswa beserta grade
    """
    # List untuk menyimpan objek-objek mahasiswa
    mahasiswa_list = []
    
    # Input jumlah mahasiswa dari user (konversi string ke integer)
    jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))
    
    # Loop untuk mengumpulkan data setiap mahasiswa
    for i in range(jumlah_mahasiswa):
        print(f"\nMasukkan data mahasiswa ke-{i+1}:")
        
        # Input data mahasiswa
        nim = input("NIM: ")
        nama = input("Nama: ")
        jurusan = input("Jurusan: ")
        nilai = float(input("Nilai: "))  # Konversi string ke float
        
        # Membuat objek Mahasiswa dengan data yang diinput
        mahasiswa = Mahasiswa(nim, nama, jurusan, nilai)
        
        # Menambahkan objek mahasiswa ke dalam list
        mahasiswa_list.append(mahasiswa)
    
    # Menampilkan header tabel
    print("\nData Mahasiswa:")
    print("NIM\tNama\tJurusan\tNilai\tStatus")
    
    # Loop untuk menampilkan data semua mahasiswa
    for mahasiswa in mahasiswa_list:
        # Mendapatkan status/grade mahasiswa
        status = mahasiswa.cek_status()
        
        # Menampilkan data mahasiswa beserta statusnya
        print(f"{mahasiswa.nim}\t{mahasiswa.nama}\t{mahasiswa.jurusan}\t{mahasiswa.nilai}\t{status}")

# Kondisi untuk menjalankan fungsi main() hanya jika file ini dijalankan langsung
# (bukan di-import sebagai module)
if __name__ == "__main__":
    main()