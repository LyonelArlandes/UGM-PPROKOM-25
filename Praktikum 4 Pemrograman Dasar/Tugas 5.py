a = int(input("Nilai ujian siswa ke-1 : "))
b = int(input("Nilai ujian siswa ke-2 : "))
c = int(input("Nilai ujian siswa ke-3 : "))
d = int(input("Nilai ujian siswa ke-4 : "))
e = int(input("Nilai ujian siswa ke-5 : "))

x = "LULUS"
y = "TIDAK LULUS"

if(a >= 70):
    print("Siswa pertama :",x)
else:
    print("Siswa pertama :",y)

if(b >= 70):
    print("Siswa kedua   :",x)
else:
    print("Siswa kedua   :",y)

if(c >= 70):
    print("Siswa ketiga  :",x)
else:
    print("Siswa ketiga  :",y)

if(d >= 70):
    print("Siswa keempat :",x)
else:
    print("Siswa keempat :",y)

if(e >= 70):
    print("Siswa kelima  :",x)
else:
    print("Siswa kelima  :",y)