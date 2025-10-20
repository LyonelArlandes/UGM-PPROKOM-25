list_nama = list()
for i in range (5):
    nama = input(f"Masukkan nama siswa ke-{i+1} : ")
    list_nama.append(nama)

nama_diubah = int(input("Masukkan index nama yang akan di ganti : "))
list_nama[nama_diubah] = input("Masukkan nama baru : ")

print(list_nama)