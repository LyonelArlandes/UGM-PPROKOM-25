import data_mhs

while True:
    print("=== MENU DATA MAHASISWA ===")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Keluar")

    pilihan = input("Pilih menu (1-3): ")

    if pilihan == "1":
        nama = input("Masukkan nama mahasiswa: ")
        nim = input("Masukkan NIM: ")
        data_mhs.tambah_data(nama, nim)

    elif pilihan == "2":
        data_mhs.tampilkan_data()

    elif pilihan == "3":
        print("Terima kasih! Program selesai.")
        break

    else:
        print("Pilihan tidak valid! Coba lagi.\n")