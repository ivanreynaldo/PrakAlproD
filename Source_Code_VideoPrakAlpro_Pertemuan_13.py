'''
Nama : Ivan Reynaldo
NIM  : 71200589
Grup : D
Universitas Kristen Duta Wacana

Menghitung perpangkatan
Referensi : jagongoding.com
Link : https://jagongoding.com/python/latihan-logika

input : Meminta inputan berupa bilangan yang akan dipangkatkan dan pangkatnya
Proses : Membuat fungsi hitung pangkat, yang menggunakan 2 parameter. Membuat Stopper dan rekursif
        yang sesuai, agar program berjalan dengan sempurna
Output : Menampilkan hasil pangkat bilangan yang telah di inputkan user
'''
def hitungPangkat(bil,pangkat):
    if pangkat==1:
        return bil
    else:
        return bil*hitungPangkat(bil,pangkat-1)
bilangan = int(input("Masukkan bilangan yang akan dipangkatkan : "))
pangkat = int(input("Masukkan besar pangkatnya : "))
print('Hasilnya adalah',hitungPangkat(bilangan,pangkat))