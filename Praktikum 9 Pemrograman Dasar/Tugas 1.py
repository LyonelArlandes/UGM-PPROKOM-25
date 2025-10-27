A =[
[
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
]
#Menampilkan semua elemen pada lapisan pertama saja (menggunakan slicing).
x = A[:1]
print("Semua elemen pada lapisan pertama : ", x)

#Menampilkan semua elemen kolom terakhir dari setiap baris dan lapisan.
for i in range(len(A)):
    for j in range(len(A[i])):
        print(f"Lapisan {i+1} Baris {j+1} : {A[i][j][-1]}")