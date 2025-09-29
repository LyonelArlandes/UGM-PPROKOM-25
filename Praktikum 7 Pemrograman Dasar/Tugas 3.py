print("\nDictionary Nilai Mahasiswa:")
nilai_mahasiswa = {
    "Aba": 85, #tidak ada koma
    "Abi": 90,
    "Abu": 78
}
print(nilai_mahasiswa)

print("/nMenambah Nilai Abe:")
nilai_mahasiswa["Abe"] = 88 #tidak pakai fungsi update
print(nilai_mahasiswa)

print("\nMengupdate NIlai Abu:")
nilai_mahasiswa["Abu"] = 87 #key nya salah
print(nilai_mahasiswa)

print("\nMencetak Semua Nilai:")
for nama, nilai in nilai_mahasiswa.items(): #tidak ada fungsi items
    print(f"Nilali {nama} adalah {nilai}")