#Nama   : Ivan Reynaldo
#NIM    : 71200589
#Grup   : D
#Universitas Kristen Duta Wacana

''' Pak Jamet adalah seorang guru sekolah dasar di SD Land Of Dawn. Dia sama seperti pak Jerami, sama-sama malas.
pak Jamet malas untuk mengoreksi pekerjaan rumah anak muridnya mengenai luas bangun datar. Karena ia malas, maka
ia meminta anda untuk membuatkan program yang dapat menghitung luas bangun datar. Bantu lah pak Jamet!

input : nilai-nilai yang dibutuhkan untuk menghitung bangun datar
        contoh : panjang dan lebar untung menghitung persegi panjang

proses : Mendefinisikan fungsi yang dapat menghitung bangun datar

output : Menampilkan pilihan bangun datar yang ingin dihitung,
         Menampilkan pesan jika user memasukkan angka diluar pilihan
         Menampilkan luas dari bangun datar yang dihitung

'''

print("===== Program Penghitung Luas Bangun Datar =====")
print("Pilih Jenis Bangun Datar yang ingin Dihitung")
print("1. Persegi")
print("2. Persegi Panjang")
print("3. Segitiga")
print("4. Lingkaran")

#Luas Persegi
def persegi(a):
    luas = a ** 2
    return luas

#Luas Persegi Panjang
def persegipanjang(a,b):
    luas = a * b
    return luas

#Luas Segitiga
def segitiga(a,t):
    luas = (a * t) / 2
    return luas

#Luas Lingkaran
def lingkaran(r):
    luas = 3.14 * (r ** 2)
    return luas

try:
    pilihan = int(input("Masukkan pilihan Anda : "))
    if pilihan < 1 or pilihan > 4 :
        print("Pilihan yang anda masukkan tidak tersedia")
    elif pilihan == 1 :
        sisi = int(input("Masukkan panjang sisi : "))
        print("Luas Persegi adalah", persegi(sisi))
    elif pilihan == 2 :
        p = int(input("Masukkan panjang : "))
        l = int(input("Masukkan lebar : "))
        print("Luas Persegi Panjang adalah", persegipanjang(p,l))
    elif pilihan == 3 :
        a = int(input("Masukkan panjang alas : "))
        t = int(input("Masukkan tinggi : "))
        print("Luas Segitiga adalah", segitiga(a,t))
    elif pilihan == 4 :
        jari2 = float(input("Masukkan jari-jari : "))
        print("Luas Lingkaran adalah", lingkaran(jari2))
except:
    print("Jangan masukkan selain angka!!!")
