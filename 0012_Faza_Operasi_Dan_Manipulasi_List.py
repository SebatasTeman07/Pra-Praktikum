# List
# Kumpulan data numbers
data_angka = [31,8,10,23]
print(data_angka)

# Kumpulan data_string
data_string = ["Lammens","Mbeumo","Cunha","Shaw"]
print(data_string)

# Kumpulan data boolean
data_boolean = [True, False, True, True]
print(data_boolean)

# Kumpulan campuran
data_campuran = [16,"Amad",37,"Mainoo","KingEmyu",True,"TsunamiTrophy",False]
print(data_campuran)


# range(start,stop,step)
data_range = range(0,10,2)
print(data_range)
data_list = list(data_range)
print(data_list) 


list_for = [i **2 for i in range(0,10)]
print(list_for) 


list_for_if = [i for i in range(0,10) if i %2 ==0]
print(list_for_if)



# Manipulasi List
data = ["MANCHESTER UNITED","PSIS SEMARANG","PSIM YOGYAKARTA"]

print(data[0])
print(data[1])
print(data[-1])

panjang_data = len(data)
print(f"panjang data = {panjang_data}")

# --- Manipulasi Data List --- #

squad = ["Sesko","Lacey","Bruno","Ugarte","Dorgu","Dalot"]

# 1. Menyisipkan data dengan insert()
squad.insert(1, "Cunha")
print(squad)
print("\n")

# 2. Menambah di akhir dengan append()
squad.append("Lammens")
print(squad)
print("\n")

# 3. Menggabungkan list dengan extend()
academy = ["Amass", "Collyer"]
squad.extend(academy)
print(squad)
print("\n")

# 4. Mengubah data lewat indeks
squad[5] = "Wesley"
print(squad)
print("\n")

# 5. Menghapus berdasarkan nilai dengan remove()
squad.remove("Dalot")
print(squad)
print("\n")

# 6. Menghapus elemen terakhir dengan pop()
squad.pop()
print(squad)
print("\n")



# --- Operasi List --- #
UCL = [7, 3, 15, 3, 2, 6, 2, 2]
CLUB = ["Manchester United", "AC Milan", "Real Madrid", "Bayern Munich"]

# 1. Menghitung kemunculan dengan count()
print(UCL.count(3))
print(UCL.count(7))
print("\n")

# 2. Mencari posisi dengan index()
print(CLUB.index("Real Madrid"))
print("\n")

# 3. Mengurutkan dengan sort()
UCL.sort()
CLUB.sort()
print(UCL)
print(CLUB)
print("\n")

# 4. Membalik urutan dengan reverse()
UCL.reverse()
CLUB.reverse()
print(UCL)   
print(CLUB)
print("\n")



# --- Nested List --- #

data_0 = [1,2]

data_1 = [3,4]

data_list_biasa = [1,2,3,4]

print(f"list biasa = {data_list_biasa}\n")

list_2D = [data_0, data_1, 6,7] 

print(f"list 2D = {list_2D}\n")

# contoh penggunaan

club_0 = ["Manchester United", 3, "Premier League"] 

club_1 = ["Real Madrid", 15, "La Liga"] 

club_2 = ["Como", 0, "Seri A"]

list_club = [club_0, club_1, club_2] 

print(f"club = {list_club}\n")

for club in list_club: 

    print(f"nama\t : {club[0]}")

    print(f" ucl\t : {club[1]}") 

    print(f"liga\t : {club[2]}\n")



# Latihan

# 1.manipulasi list
kendaraan = ["motor", "mobil", "sepeda", "bus"]

kendaraan.append("truk")
print(f"kendaraan ditambahkan {kendaraan}")

kendaraan.insert(1, "becak")
print(f"kendaraan ditambahkan lagi {kendaraan}")

kendaraan.remove("bus")
print(f"kendaraan dihapus {kendaraan}")

kendaraan[2] = "skuter"
print(f"kendaraan diubah {kendaraan}")

panjang_data = len(kendaraan)
print(f"panjang data kendaraan {panjang_data}\n")


# 2.operasi list
angka = [75,80,90,75,85,100,65]

index_100 = angka.index(100)
print(f"index angka 100 adalah {index_100}")

jumlah_angka_75 = angka.count(75)
print(f"jumlah angka 75 adalah {jumlah_angka_75}")

angka.sort()
print(f"angka diurutkan {angka}")

angka.sort(reverse=True)
print(f"angka diurutkan {angka}\n")


# 3.menggabungkan list
menu_utama = ["nasi goreng", "mie ayam"]
menu_tambahan = ["kerupuk", "es teh"]

menu_utama.extend(menu_tambahan)
print(f"menu utama {menu_utama}\n")


# 4.mengambil data dari list
data_barang = [["buku", 5000], ["pensil", 2000], ["pulpen", 3000]]

harga_pensil = data_barang[1][1]
print(f"harga pensil adalah {harga_pensil}\n")

for barang in data_barang:
    print(f"nama\t : {barang[0]}")
    print(f"harga\t : {barang[1]}\n")