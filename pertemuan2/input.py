# 4. Program Biodata dengan Input
# User bisa memasukkan data sendiri
# Paling interaktif dan fleksibel

print("=== INPUT BIODATA ===")

# Mengambil input dari user
nama = input("Nama: ")
nim = input("NIM: ")
jurusan = input("Jurusan: ")

# Menggabungkan input dengan f-string
biodata = f"""
=== BIODATA ===
Nama: {nama}
NIM: {nim}
Jurusan: {jurusan}
"""

# Menampilkan biodata yang diinput user
print(biodata)
