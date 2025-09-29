stok_buku = {
    "Harry Potter" : 10,
    "Laskar Pelangi" : 15,
    "Bumi Manusia" : 7,
    "Dilan 1990" : 20
}
#Menampilkan semua judul buku dan stoknya
print("Buku", list(stok_buku.keys()), " - ", "Stok", list(stok_buku.values()), "\n")
#Meminta input dari user untuk menambahkan buku baru
key = input("Masukkan nama buku: ")
value = int(input("Masukkan stok buku: "))
stok_buku[key] = value
print(f"Buku {key} berhasil ditambahkan dengan stok {value}")
print("Stok buku terbaru : ", stok_buku)