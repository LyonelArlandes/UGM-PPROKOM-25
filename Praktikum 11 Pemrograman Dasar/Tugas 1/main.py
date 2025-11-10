import aritmatika

a = float(input("Masukkan nilai pertama (a) : "))
b = float(input("Masukkan nilai kedua (b)   : "))

print("\nHasil Operasi Matematika:")
print(f"Penjumlahan        : {aritmatika.penjumlahan(a, b)}")
print(f"Pengurangan        : {aritmatika.pengurangan(a, b)}")
print(f"Perkalian          : {aritmatika.perkalian(a, b)}")
print(f"Pembagian          : {aritmatika.pembagian(a, b)}")
print(f"Modulo (sisa bagi) : {aritmatika.modulo(a, b)}")
print(f"Pangkat            : {aritmatika.perpangkatan(a, b)}")