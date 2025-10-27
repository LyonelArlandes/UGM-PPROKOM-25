# a. Membuat matriks identitas ukuran 4x4
A = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
print("a. Matriks identitas ukuran 4 x 4 :")
for baris in A:
    print(baris)

# b. Menambahkan input variabel n agar pengguna dapat menentukan ukuran matriks
n = int(input("\nMasukkan ukuran matriks identitas (n): "))
A = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
print(f"\nMatriks identitas ukuran {n} x {n} :")
for baris in A:
    print(baris)