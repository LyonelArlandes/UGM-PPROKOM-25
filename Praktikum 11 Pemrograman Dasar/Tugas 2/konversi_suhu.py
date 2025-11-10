# Celcius ke satuan lain
def celcius_ke_fahrenheit(c):
    return (c * 9/5) + 32
def celcius_ke_kelvin(c):
    return c + 273

# Fahrenheit ke satuan lain
def fahrenheit_ke_celcius(f):
    return (f - 32) * 5/9
def fahrenheit_ke_kelvin(f):
    return (f - 32) * 5/9 + 273

# Kelvin ke satuan lain
def kelvin_ke_celcius(k):
    return k - 273
def kelvin_ke_fahrenheit(k):
    return (k - 273) * 9/5 + 32