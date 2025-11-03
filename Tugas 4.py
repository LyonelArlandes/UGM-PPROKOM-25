def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        raise ZeroDivisionError("Pembagian dengan nol tidak diperbolehkan.")
    return a / b

def perpangkatan(a, b):
    return a ** b

def akar(a):
    if a < 0:
        raise ValueError("Tidak dapat mengambil akar kuadrat dari bilangan negatif.")
    return a ** (1/2)

def tampilkan_menu():
    print("\n=== KALKULATOR SEDERHANA ===")
    print("1. Penjumlahan (A + B)")
    print("2. Pengurangan (A - B)")
    print("3. Perkalian (A * B)")
    print("4. Pembagian (A / B)")
    print("5. Perpangkatan (A ^ B)")
    print("6. Akar Kuadrat (√A)")
    print("7. Keluar")

def input_float(prompt):
    while True:
        try:
            s = input(prompt).strip()
            # membolehkan pengguna memasukkan bilangan bulat atau desimal
            value = float(s)
            return value
        except ValueError:
            print("Masukan tidak valid. Silakan masukkan angka (contoh: 3.5 atau 2).")


print("Halo, selamat datang!")
print("Silahkan masukkan identitas")
input("Nama Lengkap : ")
input("NIM : ")


while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-7): ")
    if pilihan == '1':
        a = input_float("Masukkan A: ")
        b = input_float("Masukkan B: ")
        hasil = tambah(a, b)
        print(f"Hasil: {a} + {b} = {hasil}")
    elif pilihan == '2':
        a = input_float("Masukkan A: ")
        b = input_float("Masukkan B: ")
        hasil = kurang(a, b)
        print(f"Hasil: {a} - {b} = {hasil}")
    elif pilihan == '3':
        a = input_float("Masukkan A: ")
        b = input_float("Masukkan B: ")
        hasil = kali(a, b)
        print(f"Hasil: {a} * {b} = {hasil}")
    elif pilihan == '4':
        a = input_float("Masukkan Pembilang: ")
        b = input_float("Masukkan Penyebut: ")
        try:
            hasil = bagi(a, b)
            print(f"Hasil: {a} / {b} = {hasil}")
        except ZeroDivisionError:
            print("Pembagian 0 tidak valid")
    elif pilihan == '5':
        a = input_float("Masukkan A (basis): ")
        b = input_float("Masukkan B (pangkat): ")
        try:
            hasil = perpangkatan(a, b)
            print(f"Hasil: {a} ^ {b} = {hasil}")
        except OverflowError:
            print("Bilangan Terlalu Besar")
    elif pilihan == '6':
        a = input_float("Masukkan A (untuk akar): ")
        try:
            hasil = akar(a)
            print(f"Hasil: √{a} = {hasil}")
        except ValueError as e:
            print("Error:", e)
    elif pilihan == '7':
        print("Terima kasih. Program dihentikan.")
        break
    else:
        print("Pilihan tidak dikenal. Masukkan angka antara 1 dan 7.")