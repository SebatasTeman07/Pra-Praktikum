# operasi aritmatika

a = 10
b = 5
c = 6

# operasi penjumlahan +
hasil = a + b
print(a, "+", b, "=", hasil)

# operasi pengurangan -
hasil = a - b
print(a, "-", b, "=", hasil)

# operasi perkalian *
hasil = a * b
print(a, "*", b, "=", hasil)

# operasi pembagian /
hasil = a / b
print(a, "/", b, "=", hasil)

# operasi modulus %
hasil = a % c
print(a, "%", c, "=", hasil)

# operasi eksponen (pangkat) **
hasil = a ** b
print(a, "**", b, "=", hasil)

# operasi floor division //
hasil = a // c
print(a, "//", c, "=", hasil)

# program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input("Masukan suhu dalam celcius : "))
print("suhu adalah", celcius, "Celcius")

#konversi celcius ke reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah ", reamur, "Reamur")

#konversi celcius ke fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit adalah ", fahrenheit, "Fahrenheit")

#konversi celcius ke kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin adalah ", kelvin, "Kelvin")

# operasi komperasi
# setiap hasil dari operasi komperasi adalah boolean
# >,<,>=,<=,==,!=,is,is not

a = 10
b = 5

hasil = a > b
print(a, ">", b, "=", hasil)

hasil = a < b
print(a, "<", b, "=", hasil)

hasil = a >= b
print(a, ">=", b, "=", hasil)

hasil = a <= b
print(a, "<=", b, "=", hasil)

hasil = a == b
print(a, "==", b, "=", hasil)

hasil = a != b
print(a, "!=", b, "=", hasil)


# latihan
panjang = 12
lebar = 5
tinggi = 3

# a
luas = panjang * lebar
volume = luas * tinggi
keliling = 2 * (panjang + lebar + tinggi)

print("luas = ", luas)
print("volume = ", volume)
print("keliling = ", keliling)

# b
hasil = luas > 50
print(luas, ">", 50, "=", hasil)

# c
hasil = volume == 600
print(volume, "==", 600, "=", hasil)