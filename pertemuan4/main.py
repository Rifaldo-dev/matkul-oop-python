
class Pengajian:
    """Class untuk mengelola data gaji karyawan individual"""
    
    # CONSTRUCTOR - untuk inisialisasi object
    def __init__(self, id_karyawan, nama, golongan):
        self.id_karyawan = id_karyawan
        self.nama = nama
        self.golongan = golongan
        self._gaji_pokok = self._hitung_gaji_pokok()  # Private attribute
    
    # PRIVATE METHOD - hanya bisa dipanggil dari dalam class
    def _hitung_gaji_pokok(self):
        gaji_golongan = {1: 1000000, 2: 2000000, 3: 3000000, 4: 4000000}
        return gaji_golongan.get(self.golongan, 0)
    
    # PUBLIC METHODS - bisa dipanggil dari luar class
    def hitung_tunjangan(self):
        return self._gaji_pokok * 0.1
    
    def hitung_pajak(self):
        return self._gaji_pokok * 0.05
    
    def hitung_gaji_kotor(self):
        return self._gaji_pokok + self.hitung_tunjangan()
    
    def hitung_gaji_bersih(self):
        return self.hitung_gaji_kotor() - self.hitung_pajak()
    
    def tampilkan_info(self):
        print(f"ID Karyawan   : {self.id_karyawan}")
        print(f"Nama          : {self.nama}")
        print(f"Golongan      : {self.golongan}")
        print(f"Gaji          : Rp {self._gaji_pokok:,}")
        print(f"Tunjangan     : Rp {self.hitung_tunjangan():,.0f}")
        print(f"Pajak         : Rp {self.hitung_pajak():,.0f}")
        print(f"Gaji Kotor    : Rp {self.hitung_gaji_kotor():,.0f}")
        print(f"Gaji Bersih   : Rp {self.hitung_gaji_bersih():,.0f}")


# ========================================
# CLASS PENGAJIANMANAGER - Inheritance
# ========================================
class PengajianManager:
    """Class untuk mengelola multiple data gaji (mewarisi konsep dari Pengajian)"""
    
    # CONSTRUCTOR
    def __init__(self):
        self.daftar_pengajian = []  # List untuk menyimpan object Pengajian
    
    # METHOD untuk menambah data baru
    def tambah_pengajian(self, id_karyawan, nama, golongan):
        pengajian = Pengajian(id_karyawan, nama, golongan)  # Buat object Pengajian
        self.daftar_pengajian.append(pengajian)
        return pengajian
    
    # METHOD OVERRIDING - tampilkan dengan format berbeda
    def tampilkan_semua(self):
        if not self.daftar_pengajian:
            print("Tidak ada data gaji karyawan.")
            return
        
        print("=" * 80)
        print("DAFTAR DATA GAJI KARYAWAN")
        print("=" * 80)
        
        for i, pengajian in enumerate(self.daftar_pengajian, 1):
            print(f"\nData ke-{i}:")
            print("-" * 40)
            pengajian.tampilkan_info()  # Panggil method dari class Pengajian
    
    # METHOD untuk pencarian data
    def cari_berdasarkan_id(self, id_karyawan):
        for pengajian in self.daftar_pengajian:
            if pengajian.id_karyawan == id_karyawan:
                return pengajian
        return None


# ========================================
# MAIN FUNCTION - Menjalankan Aplikasi
# ========================================
def main():
    """Function utama untuk menjalankan aplikasi"""
    
    manager = PengajianManager()  # Buat object PengajianManager
    
    while True:
        print("\n" + "=" * 50)
        print("APLIKASI PENGOLAHAN DATA GAJI KARYAWAN")
        print("Implementasi OOP: Inheritance & Method Overriding")
        print("=" * 50)
        print("1. Tambah Data Gaji Karyawan")
        print("2. Tampilkan Semua Data")
        print("3. Cari Data Berdasarkan ID Karyawan")
        print("4. Keluar")
        print("-" * 50)
        
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == "1":
            print("\nInput Data Gaji Karyawan:")
            print("-" * 30)
            try:
                id_karyawan = input("ID Karyawan : ")
                nama = input("Nama        : ")
                golongan = int(input("Golongan (1-4): "))
                
                if golongan not in [1, 2, 3, 4]:
                    print("Error: Golongan harus antara 1-4!")
                    continue
                
                pengajian = manager.tambah_pengajian(id_karyawan, nama, golongan)
                print("\nData berhasil ditambahkan!")
                print("\nTampilkan data yang baru ditambahkan:")
                print("-" * 40)
                pengajian.tampilkan_info()
                
            except ValueError:
                print("Error: Golongan harus berupa angka!")
        
        elif pilihan == "2":
            manager.tampilkan_semua()
        
        elif pilihan == "3":
            id_cari = input("\nMasukkan ID Karyawan yang dicari: ")
            pengajian = manager.cari_berdasarkan_id(id_cari)
            
            if pengajian:
                print("\nData ditemukan:")
                print("-" * 40)
                pengajian.tampilkan_info()
            else:
                print("Data dengan ID Karyawan tersebut tidak ditemukan!")
        
        elif pilihan == "4":
            print("Terima kasih telah menggunakan aplikasi ini!")
            break
        
        else:
            print("Pilihan tidak valid! Silakan pilih 1-4.")


if __name__ == "__main__":
    main()