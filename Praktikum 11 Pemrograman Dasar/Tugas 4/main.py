import produk
import transaksi

def main():
    print("=== APLIKASI PENJUALAN TOKO AFUNG ===\n")

    while True:
        produk.tampilkan_produk()
        try:
            pilihan = int(input("Pilih produk (nomor): "))
            if pilihan not in produk.daftar_produk:
                print("Produk tidak ditemukan!\n")
                continue
        except ValueError:
            print("Input tidak valid!\n")
            continue

        jumlah = int(input("Masukkan jumlah beli: "))
        print()
        nama = produk.daftar_produk[pilihan]["nama"]
        harga = produk.daftar_produk[pilihan]["harga"]

        total = transaksi.hitung_total(harga, jumlah)
        total_bayar, diskon = transaksi.total_setelah_diskon(total)

        print("=== STRUK PEMBAYARAN ===")
        print(f"Produk       : {nama}")
        print(f"Harga Satuan : Rp{harga}")
        print(f"Jumlah Beli  : {jumlah}")
        print(f"Total Harga  : Rp{total}")
        print(f"Diskon       : Rp{diskon}")
        print(f"Total Bayar  : Rp{total_bayar}\n")

        lagi = input("Apakah ingin belanja lagi? (y/n): ").lower()
        if lagi != 'y':
            print("Terima kasih telah berbelanja!")
            break
        print()

if __name__ == "__main__":
    main()