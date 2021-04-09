'''
Nama : Ivan Reynaldo
NIM  : 71200589
Group: D
Universitas Kristen Duta Wacana

Pak Apel meminta bantuan anda untuk membalas dendam ke isterinya karena isterinya telah mengubah
    password hp pak Apel. Pak Apel meminta anda untuk mengubah password hp isterinya menjadi biner.
    Pak Apel telah memberikan file txt yang berisi password hp isterinya. Bantulah Pak Apel!

Referensi : Soal UG 8 No 4

input : menginput file yang diberikan pak Apel

proses : membuka dan membaca file yg diberikan pak Apel, lalu dengan perulangan, membuat semua isi 
         yang ada didalam file menjadi biner.
    
Output : Menampilkan password dalam versi biner

'''
filename = input("Masukkan File : ")
handle = open(filename)
handle2 = handle.read()
isifile = int(handle2)
k = ''
import math
while True :
    a = math.floor(isifile / 2)
    modulo = isifile % 2
    k += str(modulo)
    isifile = a
    if isifile == 0:
        break
    else:
        continue
print("Password Binernya adalah :", k[::-1])