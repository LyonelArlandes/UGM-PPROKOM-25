buah_buahan = {
    "apel" : 15000,
    "jeruk" :10000,
    "anggur" : 25000
}
#menampilkan harga jeruk
print ("Harga jeruk adalah Rp", buah_buahan.get("jeruk"), "\n")
#Menambahkan buah mangga
buah_buahan["mangga"] = 12000
print("Setelah buah mangga ditambahkan ke dalam list :\n", buah_buahan, "\n")
#Memperbaharui harga anggur
buah_buahan["anggur"] = 20000
print("Setelarh harga anggur diubah :\n", buah_buahan, "\n")
#Menghapus buah jeruk
del buah_buahan["jeruk"]
print("Setelah buah jeruk dihapus dari dictionary:\n", buah_buahan)