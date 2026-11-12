# LIST
# # menggunakan kurung siku
data_list = [10,2,4,3,2]
print(data_list)

# tuples
data_tuples = (7,8,10,11)
print(data_tuples)
print(data_tuples[1])

# tidak bisa dilakukan
# data_tuples[1] = "ucup"
# data_tuples.append(1)

# sets (himpunan)
data_sets = {10,4,3,2,7,6,5}
print(data_sets)

# tidak bisa dilakukan
# print(data_sets[0])


## Dictionary

# list → array, mengakses dengan menggunakan index
data_list = ['ucup','rendi','salsa']
print(data_list[0])

# dictionary (dict) → associative array
# identifier → key

data_dict = {
    'key': 'value',
    'cp': 'ucup',
    'rd': 'rendi',
    'sl': 'salsa',
    'nmbr': 100,
    'list': data_list
}

print(data_dict['cp'])
print(data_dict['nmbr'])
print(data_dict['list'])


## --- Operasi Dictionary ---
data_dict = {
    "AYDK": "Aku Yakin Dengan Kamu",
    "GGMU": "Glory-Glory Man United",
    "YIY": "Yoh Iso Yoh"
}

# panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary: {LENDICT}")
print("\n")

# cek key exist ada atau tidak
KEY = "AYDK"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")
print("\n")

# akses value (read)
print(data_dict["AYDK"])
print(data_dict.get("AYDK"))
print(data_dict.get("kis", "key tidak ditemukan"))  # check key dengan message
print("\n")

# update data
data_dict["AYDK"] = "PSIM Yogyakarta"
print(data_dict)
print("\n")

data_dict["FORZA"] = "Inter"
print(data_dict)
print("\n")

data_dict.update({"AYDK": "Aku Yakin Dengan Kamu"})
print(data_dict)
print("\n")

data_dict.update({"HALA": "Madrid"})  # akan ditambah jika tidak ada
print(data_dict)
print("\n")

# hapus data
del data_dict["HALA"]
print(data_dict)


## --- Looping Dictionary ---
julukan_julukan = {
    "Man United": "The Red Devil",
    "PSIS SEMARANG": "Laskar Mahesa Jenar",
    "PSIM YOGYAKARTA": "Laskar Mataram",
    "PPSM MAGELANG": "Laskar Macan Tidar"
}

# looping first try (output key)
for julukan in julukan_julukan:
    print(julukan)
    print("\n")

# operator untuk mengambil item
keys = julukan_julukan.keys()
print(keys)
for key in julukan_julukan.keys():
    print(julukan_julukan.get(key))
    print("\n")

values = julukan_julukan.values()
print(values)
for value in julukan_julukan.values():
    print(value)
    print("\n")

items = julukan_julukan.items()
print(items)
for item in julukan_julukan.items():
    print(item)
    print("\n")

for key, value in julukan_julukan.items():
    print(f"key = {key}, value = {value}")


# Latihan #

# Nomor 1
# a. Membuat tuple mahasiswa
mahasiswa = ("Faza Mafatikhul Huda", "2605060023", "Teknologi Informasi")

# b.  Menampilkan data NIM dan Prodi melalui indeks
print("NIM   :", mahasiswa[1])
print("Prodi :", mahasiswa[2])

# c. Menjalankan mahasiswa[2] = "Teknologi Informasi" dan penjelasan error
mahasiswa[2] = "Teknologi Informasi"

# Penjelasan: Hal ini terjadi karena tipe data Tuple bersifat immutable (tidak dapat diubah). Setelah tuple dibuat, elemen di dalamnya tidak bisa diubah, ditambah, maupun dihapus secara langsung.

# d. Membuat Set nilai_angka dan penjelasan duplikasi
nilai_angka = {10, 4, 3, 2, 4, 10, 7, 5}
print(nilai_angka)

# Nomor 2
# a. Membuat Dictionary data_mahasiswa
data_mahasiswa = {
    "nim": "240101",
    "nama": "Budi Santoso",
    "prodi": "Teknologi Informasi"
}

# b. Mengubah Nilai dan Menambah Key Baru
# Mengubah nilai prodi
data_mahasiswa["prodi"] = "Sastra Mesin"

# Menambahkan key baru angkatan
data_mahasiswa["angkatan"] = 2026

# c.Menghapus Data "nim" dan Menampilkan Hasil Akhir
# Menghapus key nim
del data_mahasiswa["nim"]

# Menampilkan hasil akhir dictionary
print(data_mahasiswa)
