# Program 11.1 Multi keys & Nesting Dictionary
import datetime 
 
united1 = { 
 'nama':'Senne Lammens', 
 'nomor' :1, 
 'negara':'Belgia',
 'aktif':True, 
 'lahir':datetime.datetime(2002,7,27) # tahun, tanggal, bulan 
}  
 
united2 = { 
 'nama':'Kobbie Mainoo', 
 'nomor' :37, 
 'negara':'Inggris',
 'aktif':True, 
 'lahir':datetime.datetime(2005,4,19) # tahun, tanggal, bulan 
}  
 
united3 = { 
 'nama':'Matheus Cunha',
 'nomor' :10, 
 'negara':'Brasil', 
 'aktif':True, 
 'lahir':datetime.datetime(1999,5,27) # tahun, tanggal, bulan 
}
pemain_united = { 
 'UTD001':united1, 
 'UTD002':united2, 
 'UTD003':united3, 
} 
 
print(f"{'KEY':<6} {'Nama':<6} {'Nomor':<3} {'Negara':<9} {'Aktif':<10} {'Lahir':<10}") 
print("-"*50) 
 
for pemain in pemain_united: 
    KEY = pemain 
     
    NAMA = pemain_united[KEY]['nama'] 
    NOMOR = pemain_united[KEY]['nomor'] 
    NEGARA = pemain_united[KEY]['negara'] 
    AKTIF = pemain_united[KEY]['aktif'] 
    LAHIR = pemain_united[KEY]['lahir'].strftime("%x") 
 
    print(f"{KEY:<6} {NAMA:<17} {NOMOR:<3} {NEGARA:<9} {AKTIF:<10} {LAHIR:<10}")
    print("\n")





# Program 11.2 Latihan Dictionary Bagian 1
import datetime 
 
mahasiswa_template = { 
     'nama':'nama', 
 'nim':00000000, 
 'sks_lulus':0, 
 'lahir':datetime.datetime(1111,1,11) 
} 
 
data_mahasiswa = {} 
 
print(f"{'SELAMAT DATANG':^20}") 
print(f"{'DATA MAHASISWA':^20}") 
print("-"*20) 
 
mahasiswa = dict.fromkeys(mahasiswa_template.keys()) 
print(mahasiswa) 
mahasiswa['nama'] = input("Nama Mahasiswa: ") 
mahasiswa['nim'] = input("NIM Mahasiswa: ") 
mahasiswa['sks_lulus'] = int(input("SKS Lulus")) 
TAHUN_LAHIR = int(input("Tahun lahir (YYYY): ")) 
BULAN_LAHIR = int(input("Bulan lahir (1-12): ")) 
TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): ")) 
mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR) 
 
print(mahasiswa)
print("\n")





# Program 11.3 Latihan Dictionary Bagian 2
import datetime 
import os 
import string 
import random 
 
# template dict mahasiswa 
mahasiswa_template = { 
 'nama':'nama', 
 'nim':'00000000', 
 'sks_lulus':0, 
 'lahir':datetime.datetime(1111,1,11) 
} 
 
data_mahasiswa = {} 
 
while True: 
 # os.system("cls") # untuk windows 
 os.system("clear") 
 print(f"{'SELAMAT DATANG':^20}") 
 print(f"{'DATA MAHASISWA':^20}") 
 print("-"*20) 
 
 mahasiswa = dict.fromkeys(mahasiswa_template.keys()) 
 mahasiswa['nama'] = input("Nama Mahasiswa: ") 
 mahasiswa['nim'] = input("NIM Mahasiswa: ") 
 mahasiswa['sks_lulus'] = int(input("SKS Lulus: ")) 
 TAHUN_LAHIR = int(input("Tahun lahir (YYYY): ")) 
 BULAN_LAHIR = int(input("Bulan lahir (1-12): ")) 
 TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): ")) 
 mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR) 
 
 KEY = ''.join((random.choice(string.ascii_uppercase) for i in 
range(6))) 
 data_mahasiswa.update({KEY:mahasiswa}) 
 
 # dari program sebelumnya, hilangkan beasiswa 
 print(f"\n{'KEY':<6} {'Nama':<17} {'NIM':<8} {'SKS Lulus':<10} {'Tanggal Lahir':<10}") 
 print('-'*60) 
 
 for mahasiswa in data_mahasiswa: 
  KEY = mahasiswa 
   
  NAMA = data_mahasiswa[KEY]['nama'] 
  NIM = data_mahasiswa[KEY]['nim'] 
  SKS = data_mahasiswa[KEY]['sks_lulus'] 
  LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x") 
   
  print(f"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:^10} {LAHIR:^10}") 
 
 print("\n") 
 is_done = input("Mau tambah lagi bro (y/n)? ") 
 if is_done == "n": 
  break 
 
print("\nAkhir dari program, terima kasih")





# Latihan
import datetime
import os
import random
import string

# Template dictionary untuk setiap buku (Multi-keys)
buku_template = {
    'judul': 'judul',
    'penulis': 'penulis',
    'tahun_terbit': 0000,
    'tanggal_pinjam': datetime.datetime(1111, 1, 11),
    'status': 'STATUS'
}

# Dictionary utama untuk menyimpan data buku (Nesting Dictionary)
data_perpustakaan = {}

while True:
    # Membersihkan layar terminal (gunakan 'cls' untuk Windows, 'clear' untuk Mac/Linux)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"{'SISTEM MANAJEMEN PERPUSTAKAAN':^95}")
    print(f"{'DATA KOLEKSI BUKU':^95}")
    print("-" * 95)

    # Membuat dictionary kosong baru yang mengacu pada template
    buku = dict.fromkeys(buku_template.keys())

    # Mengambil input dari pengguna
    buku['judul'] = input("Judul Buku\t\t\t: ")
    buku['penulis'] = input("Penulis\t\t\t\t: ")
    buku['tahun_terbit'] = int(input("Tahun Terbit (YYYY)\t\t: "))
    
    # Input tanggal terakhir pinjam
    print("Tanggal Terakhir Pinjam:")
    tahun = int(input("  Tahun (YYYY)\t\t\t: "))
    bulan = int(input("  Bulan (1-12)\t\t\t: "))
    tanggal = int(input("  Tanggal (1-31)\t\t: "))
    buku['tanggal_pinjam'] = datetime.datetime(tahun, bulan, tanggal)
    
    # Input status buku
    status_input = input("Status (TERSEDIA / TIDAK)\t: ").upper()
    buku['status'] = status_input if status_input in ['TERSEDIA', 'TIDAK'] else 'TIDAK'

    # Membuat KEY acak unik sebanyak 6 karakter huruf kapital
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    
    # Memasukkan data buku ke dalam nesting dictionary dengan KEY unik
    data_perpustakaan.update({KEY: buku})

    # Menampilkan header tabel sesuai format yang diminta
    print("\n" + "-" * 95)
    print(f"{'KEYS':<8} {'JUDUL BUKU':<25} {'PENULIS':<20} {'TAHUN TERBIT':<14} {'TERAKHIR PINJAM':<17} {'STATUS':<10}")
    print("-" * 95)

    # Melakukan iterasi untuk menampilkan seluruh data buku dalam nesting dictionary
    for key in data_perpustakaan:
        KEY_BUKU = key
        JUDUL = data_perpustakaan[key]['judul']
        PENULIS = data_perpustakaan[key]['penulis']
        TAHUN = data_perpustakaan[key]['tahun_terbit']
        TANGGAL = data_perpustakaan[key]['tanggal_pinjam'].strftime("%x") # Format MM/DD/YY
        STATUS = data_perpustakaan[key]['status']

        print(f"{KEY_BUKU:<8} {JUDUL:<25} {PENULIS:<20} {TAHUN:<14} {TANGGAL:<17} {STATUS:<10}")

    print("-" * 95)
    
    # Konfirmasi untuk menambah data lagi
    lanjut = input("\nApakah ingin menambah buku lagi? (y/n): ").lower()
    if lanjut == 'n':
        break

print("\nTerima kasih telah menggunakan Sistem Manajemen Perpustakaan!")