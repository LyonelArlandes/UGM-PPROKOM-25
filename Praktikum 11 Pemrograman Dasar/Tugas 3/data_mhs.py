daftar_mahasiswa = []

def tambah_data(nama, nim):
    """Menambahkan data mahasiswa ke dalam list"""
    mahasiswa = {"nama": nama, "nim": nim}
    daftar_mahasiswa.append(mahasiswa)
    print(f"Data mahasiswa {nama} ({nim}) berhasil ditambahkan!\n")

def tampilkan_data():
    """Menampilkan semua data mahasiswa yang tersimpan"""
    print("\n=== DAFTAR MAHASISWA ===")
    if len(daftar_mahasiswa) == 0:
        print("Belum ada data mahasiswa.")
    else:
        for i, mhs in enumerate(daftar_mahasiswa, start=1):
            print(f"{i}. {mhs['nama']} ({mhs['nim']})")
    print()