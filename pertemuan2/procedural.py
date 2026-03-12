# 2. Program Biodata Procedural
# Menggunakan variabel untuk menyimpan data
# Lebih fleksibel karena data terpisah dari tampilan

# Deklarasi variabel untuk menyimpan data
nama = "M. Rifaldo Saputra"
nim = "245720111034"
jurusan = "Sistem Informasi"

# Menggabungkan variabel dengan teks menggunakan f-string
biodata = f"""
=== BIODATA ===
Nama: {nama}
NIM: {nim}
Jurusan: {jurusan}
"""

# Menampilkan biodata
print(biodata)
