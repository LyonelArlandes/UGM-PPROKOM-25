from array import array
array_saya = array('i', [12, 34, 56, 78 , 90])
print(array_saya)
panjang_array = len(array_saya)
print("Banyaknya nilai integer pada array tersebut : ", panjang_array)

jumlah_array = sum(array_saya)
print("Jumlah nilai pada array : ", jumlah_array)

ratarata_array = jumlah_array / panjang_array
print("Rata-rata nilai array : ", ratarata_array)