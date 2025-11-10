def hitung_total(harga, jumlah):
    return harga * jumlah

def hitung_diskon(total):
    if total >= 100000:
        return total * 0.1  # Diskon 10%
    elif total >= 50000:
        return total * 0.05 # Diskon 5%
    else:
        return 0

def total_setelah_diskon(total):
    diskon = hitung_diskon(total)
    return total - diskon, diskon