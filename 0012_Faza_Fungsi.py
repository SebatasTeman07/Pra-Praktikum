## --- MEMBUAT FUNGSI ---

def hello_world():
# menampilkan hello world 
    print("Selamat pagi")
    print("Kepada Ganda Aji")
    print("Dan juga kepada Faza Mafa")

hello_world()





## --- Fungsi dengan argumen --- 
 
## def nama_fungsi(argumen) 
#      Badan fungsi 
 
def hello_world(nama): 
  #fungsi hello world menerima 
  print(f"Selamat datang di Dunia, {nama}") 
 
hello_world("Faza") 
 
def tambah(angka_1, angka_2): 
  # fungsi tambah 
  hasil = angka_1 + angka_2 
  print(f"{angka_1} + {angka_2} = {hasil}") 
 
tambah(1,8) 
 
def say_hi(list_peserta): 
  #fungsi say hi 
  data_peserta = list_peserta.copy() 
  for peserta in data_peserta: 
    print(f"Selamat datang {peserta}") 
 
kumpulan_mahasiswa = ["Faza", "Ganda", "Ardan"] 
 
say_hi(kumpulan_mahasiswa)





# template fungsi kembalian 
# def nama_fungsi(argumen): 
#     badan fungsi 
#     return output 
 
# fungsi kuadrat 
 
def kuadrat(input_angka): 
  output_kuadrat = input_angka ** 2 
  return output_kuadrat 
 
y = kuadrat(5) 
print(y) 
 
print(kuadrat(6)) 
 
z = 10 + kuadrat(7) 
print(z) 
 
def fungsi_tambah(angka_1, angka_2): 
  # fungsi return dengan multi input 
  return angka_1 + angka_2 
 
a = fungsi_tambah(10, 8) 
print(a) 
 
def operasi_matematika(angka_1, angka_2):
  tambah = angka_1 + angka_2 
  kurang = angka_1 - angka_2 
  kali = angka_1 * angka_2 
  bagi = angka_1 / angka_2 
 
  return tambah,kurang,kali,bagi 
 
k,l,m,n = operasi_matematika(9,5) 
 
print(f"Hasil tambah = {k}") 
print(f"Hasil kurang = {l}") 
print(f"Hasil kali = {m}") 
print(f"Hasil bagi = {n}")





# Default argument 
 
# def fungsi(argument): 
# def fungsi(argument = nilai default): 
 
# contoh 1 
def say_hello(nama = "Faza"): 
  print(f"Hello {nama}") 
 
say_hello("Ganda") 
say_hello() 
 
# contoh 2 
def sapa_dia(nama, pesan = "Apa kabar?"): 
  # fungsi dengan satu input biasa, dan satu default arg 
  print(f"hai {nama}, {pesan}") 
 
sapa_dia("Ardan","Selamat pagi") 
sapa_dia("Dafa") 
 
# contoh 3 
def hitung_pangkat(angka, pangkat): 
  hasil = angka**pangkat 
  return hasil 
 
print(hitung_pangkat(2,4)) 
 
hasil = hitung_pangkat(pangkat=3, angka=5) 
print(hasil) 
 
# contoh 4 
def faktorial(input_1=1,input_2=2,input_3=3,input_4=4): 
  hasil = input_1 * input_2 * input_3 * input_4 
  return hasil 
 
print(faktorial()) 
print(faktorial(input_3 = 10))





# Latihan
import math


# a. Fungsi luas persegi panjang
def luas_persegi_panjang(panjang: float, lebar: float) -> float:
    return panjang * lebar


# b. Fungsi volume balok (volume persegi panjang)
def volume_balok(panjang: float, lebar: float, tinggi: float) -> float:
    return panjang * lebar * tinggi


# c. Fungsi luas lingkaran
def luas_lingkaran(jari_jari: float) -> float:
    return math.pi * (jari_jari**2)


# d. Fungsi volume bola
def volume_bola(jari_jari: float) -> float:
    return (4 / 3) * math.pi * (jari_jari**3)


def main():
    print("=== Program Kalkulator Geometri ===")

    # Input persegi panjang & balok
    p = float(input("Masukkan panjang: "))
    l = float(input("Masukkan lebar: "))
    t = float(input("Masukkan tinggi (untuk volume balok): "))

    # Input lingkaran & bola
    r = float(input("Masukkan jari-jari (untuk lingkaran & bola): "))

    print("\n=== Hasil Perhitungan ===")
    print(f"a. Luas persegi panjang : {luas_persegi_panjang(p, l):.2f}")
    print(f"b. Volume balok         : {volume_balok(p, l, t):.2f}")
    print(f"c. Luas lingkaran       : {luas_lingkaran(r):.2f}")
    print(f"d. Volume bola          : {volume_bola(r):.2f}")


if __name__ == "__main__":
    main()