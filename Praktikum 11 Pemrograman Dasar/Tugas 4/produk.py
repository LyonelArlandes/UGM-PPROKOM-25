daftar_produk = {
    1: {"nama": "Kopi Bali", "harga": 75000},
    2: {"nama": "Kopi Aceh", "harga": 80000},
    3: {"nama": "Kopi Toraja", "harga": 50000}
}

def tampilkan_produk():
    print("=== DAFTAR PRODUK ===")
    for nomor, info in daftar_produk.items():
        print(f"{nomor}. {info['nama']} - Rp{info['harga']}")