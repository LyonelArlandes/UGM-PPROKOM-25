import numpy as np

nilai = np.array([[85, 80, 90], [78, 82, 88], [92, 90, 94], [70, 68, 72], [88, 85, 84], 
 [60, 75, 70], [95, 92, 98], [74, 70, 76], [81, 85, 83], [69, 72, 70], [90, 88, 92],
 [76, 80, 79], [84, 86, 90], [79, 82, 85], [67, 70, 68], [91, 94, 93], [73, 78, 75],
 [87, 84, 89], [65, 68, 70], [93, 90, 95], [77, 80, 78], [82, 84, 88], [89, 85, 90],
 [71, 74, 76]])

orang = 1
for baris in nilai:
        print(f"Mahasiswa ke-{orang} | Tugas: {baris[0]} | UTS: {baris[1]} | UAS: {baris[2]}")
        orang += 1

print(f"\nRata-rata keseluruhan nilai : {round(np.mean(nilai), 2)}")
print(f"Nilai tertinggi : {np.max(nilai)}")
print(f"Nilai terendah : {np.min(nilai)}")