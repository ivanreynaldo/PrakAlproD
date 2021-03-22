#Nama : Ivan Reynaldo
#NIM  : 71200589
#Group: D
#Universitas Kristen Duta Wacana

''' Pak Dadang meminta bantuan anda untuk membuat program yang dapat mengubah kata yang diinputkan oleh user menjadi
kata yang huruf depannya kapital dan sisanya katanya huruf kecil. Pak dadang meminta 3 kata yang dibuar seperti itu.
Bantu lah pak Dadang!

Referensi : Soal UG 7

Input : membuat variabel yang dapat menerima input apapun dari user

Proses : membuat inputan menjadi huruf kecil dan membuat huruf pertamanya menjadi huruf kapital, diterapkan pada 3
         inputan user, lalu digabungkan

Output : dapat mengeluarkan output berupa susunan kalimat berdasarkan 3 kata inputan user, huruf depan ketiga
         kata tersebut semua kapital. '''

kata1 = input("Masukkan Kata 1 : ")
kata2 = input("Masukkan Kata 2 : ")
kata3 = input("Masukkan Kata 3 : ")

kata1 = kata1.lower()
kata2 = kata2.lower()
kata3 = kata3.lower()

kata1 = kata1[0].upper() + kata1[1:]
kata2 = kata2[0].upper() + kata2[1:]
kata3 = kata3[0].upper() + kata3[1:]

print(kata1 + ' ' + kata2 + ' ' + kata3)