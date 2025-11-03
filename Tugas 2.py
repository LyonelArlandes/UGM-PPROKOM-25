# Variabel global untuk menyimpan data Buku
buku = []

def show_data(): # fungsi untuk menampilkan semua data
    if len(buku) <= 0:
        print ("BELUM ADA DATA")
    else:
        for indeks in range(len(buku)):
            print("[%d] %s" % (indeks, buku[indeks]))

def insert_data():
    buku_baru = input("Judul Buku: ")
    buku.apppend(buku_baru)

def edit_data():
    show_data()
    indeks = int(input("Inputkan ID buku: "))
    if(indeks < 0 or indeks >= len(buku)):
        print("ID salah")
    else:
        judul_baru = input("Judul baru: ")
        buku[indeks] = judul_baru

def delete_data():
    show_data()
    indeks = int(input("Inputkan ID buku: " ))
    if(indeks < 0 or indeks >= len(buku)):
        print("ID salah")
    else:
        buku.pop(indeks)

def show_menu():
    print("\n")
    print("----------- Menu -----------")
    print("[1] Show Data")
    print("[2] Insert Data")
    print("[3] Edit Data")
    print("[4] Delete Data")
    print("[5] Exit")
    menu = input ("PILIH MENU> ")
    print("\n")
    if menu == "1":
        show_data()
    elif menu == "2":
        insert_data()
    elif menu == "3":
        edit_data()
    elif menu == "4":
        delete_data()
    elif menu == "5":
        exit()
    else:
        print("Salah pilih!")

while(True):
    show_menu()