import numpy as np
A = np.array([
    [2, 4, 6],
    [1, 2, 3]
])
B = np.array([
    [1, 1, 1],
    [2, 2, 2]
])

penjumlahan = A + B
print (f"Hasil penjumlahan matriks A + B : \n{penjumlahan}\n")
pengurangan = A - B
print (f"Hasil penjumlahan matriks A - B : \n{pengurangan}\n")
perkalian = A.dot(B.T)
print (f"Hasil perkalian matriks A x B : \n{perkalian}")