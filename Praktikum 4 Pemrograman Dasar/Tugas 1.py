umur = int(input("Masukkan umur amnda = "))
nilai = int(input("Masukkan nilai tes anda = "))
lulus = "Selamat, anda berhak mendapatkan SIM Anda"
gagal = "Maaf, Anda tidak berhak mendapatkan sim anda\nsilahkan coba lagi bulan atau tahun depan"
if(umur>17):
    if(nilai < 60):
        print()
        print(gagal)
    else:
        print()
        print(lulus)
else:
    print()
    print(gagal)