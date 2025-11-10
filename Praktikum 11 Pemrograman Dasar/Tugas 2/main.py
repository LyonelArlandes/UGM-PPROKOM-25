import konversi_suhu

print("=== Program Konversi Suhu ===")
print("Pilih satuan asal:")
print("1. Celcius")
print("2. Fahrenheit")
print("3. Kelvin")

pilihan = int(input("Masukkan pilihan (1-3): "))
suhu = float(input("Masukkan nilai suhu: "))

print("\nHasil Konversi Suhu")

if pilihan == 1:
    print(f"{suhu} °C = {konversi_suhu.celcius_ke_fahrenheit(suhu)} °F")
    print(f"{suhu} °C = {konversi_suhu.celcius_ke_kelvin(suhu)} K")
elif pilihan == 2:
    print(f"{suhu} °F = {konversi_suhu.fahrenheit_ke_celcius(suhu)} °C")
    print(f"{suhu} °F = {konversi_suhu.fahrenheit_ke_kelvin(suhu)} K")
elif pilihan == 3:
    print(f"{suhu} K = {konversi_suhu.kelvin_ke_celcius(suhu)} °C")
    print(f"{suhu} K = {konversi_suhu.kelvin_ke_fahrenheit(suhu)} °F")
else:
    print("Pilihan tidak valid! Program Selesai.")  