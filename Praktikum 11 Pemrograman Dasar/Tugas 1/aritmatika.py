def penjumlahan (a , b):
    return a + b

def pengurangan(a , b):
    return a - b

def perkalian(a , b):
    return a * b

def pembagian(a , b):
    if b != 0:
        return a / b
    else:
        return "Zero-divition error. Penyebut nggak boleh nol (0)"

def modulo(a , b): #sisa pembagian
    if b != 0:
        return a % b
    else:
        return "Modulo dengan nol (0) tidak boleh" 

def perpangkatan(a , b):
    return a ** b