# operasi logika atau boolean

# not, or, and, xor

# not
a = True
b = not a
print(b)

# or (jika salah satu true, maka hasilnya adalah true)
a = True
b = False
c = a or b
print(c)

# and (jika dua buah nilai true, maka hasil true)
a = True
b = False
c = a and b
print(c)

# xor (akan true jika salah satu true, sisanya false)
a = True
b = False
c = a ^ b
print(c)

# latihan logika dan komparasi
# nilainya akan TRUE jika < 3 atau > 10

# +++++ 3 ----- 10 +++++

inputUsers = float(input("masukkan nilai : "))
isKurangDari = inputUsers < 3
isLebihDari = inputUsers > 10

hasil = isKurangDari or isLebihDari
print(hasil)

# ----- 3 +++++ 10 -----

inputUsers = float(input("masukkan nilai : "))
isLebihDari = inputUsers > 3
isKurangDari = inputUsers < 10

hasil = isLebihDari and isKurangDari
print(hasil)

# IF dan ELSE

# if
# kondisi
# aksi

nama = input("masukkan nama anda : ")

# 1.if inline

if nama == "faza": print("hello faza")

# 2.if indentation

if nama == "faza":
    print("hello faza")
    print("KingEmyu")

# else statement

if nama == "faza":
    print("hello faza")
else:
    print("KingEmyu")

# elif

if nama == "faza":
    print("hello faza")
elif nama == "aji":
    print("wangun")
elif nama == "buan":
    print("kobong")
else:
    print("Sengkuni")

# Latihan

usia = int(input("masuKkan usia anda : "))

if usia >= 0 and usia <= 12:
    print("Kategori : Anak-anak")
elif usia >= 13 and usia <= 17:
    print("Kategori : Remaja")
elif usia >= 18 and usia <= 59:
    print("Kategori : Dewasa")
elif usia >= 60:
    print("Kategori : Lansia")