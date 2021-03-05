#Nama : Ivan Reynaldo
#NIM  : 71200589
#Grup : D
#Universitas Kristen Duta Wacana

''' Pak Joni dosen matematika dari Universitas Gak Suka Gelay meminta bantuan saya untuk membuatkan program
yang dapat mencari angka terbesar dari 5 angka bilangan bulat yang di inputkan user. Pak Joni memberikan syarat 
bahwa angka yang diinputkan tidak boleh dibawah 0. Bantu Pak Joni!

input : 5 angka bilangan bulat diatas 0

proses : 1. membuat inisialisasi variabel sebelum perulangan
         2. membuat percabangan guna menjalankan syarat Pak Joni
         3. membuat perulangan

output : 1. menampilkan bilangan mana yang terbesar
         2. menampilkan pesan error jika user menginputkan angka dibawah nol
         3. menampilkan pesan error jika user menginputkan selain angka

'''

angka_terbesar_saatini = -1
try:
    angka1 = int(input("Masukkan angka 1: "))
    angka2 = int(input("Masukkan angka 2: "))
    angka3 = int(input("Masukkan angka 3: "))
    angka4 = int(input("Masukkan angka 4: "))
    angka5 = int(input("Masukkan angka 5: "))
    if (angka1 or angka2 or angka3 or angka4 or angka5) < 0 :
        print("Tidak dibawah 0")
    if (angka1 and angka2 and angka3 and angka4 and angka5) > 0 :
        for i in [angka1,angka2,angka3,angka4,angka5]:
            if i > angka_terbesar_saatini :
                angka_terbesar_saatini = i
        print("Angka Terbesar adalah", angka_terbesar_saatini)
except:
    print("Jangan Masukkan selain angka!!!")
