import math
luas_lingkaran = lambda r: math.pi * r * r

r = float(input("Masukkan jari-jari lingkaran: "))

hasil = luas_lingkaran(r)

print("Luas lingkaran =", hasil)